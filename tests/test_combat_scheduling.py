from __future__ import annotations

from copy import deepcopy
import hashlib
from itertools import permutations
import unittest
from unittest.mock import patch

from textrpg import combat_state
from textrpg.combat_schema import TacticalCoord
from textrpg.core import GameState
from textrpg.persistence import dumps_state
from test_combat_turns import actions, active_session, actor, line_map


class CombatSchedulingTests(unittest.TestCase):
    def test_reaction_order_uses_priority_frozen_initiative_and_stable_ids(self):
        session = combat_state.CombatSession(
            encounter_id="ORDER", tactical_map=line_map(4), seed=1,
            actors=tuple(actor(name, TacticalCoord(x, 0, 0), initiative=initiative)
                         for x, (name, initiative) in enumerate(
                             (("A", 20), ("B", 20), ("C", 10), ("D", 5)))),
        )
        candidate = combat_state.ReactionCandidate
        expected = (
            candidate("D", "HIGH", trigger_priority=2),
            candidate("A", "A_FIRST"),
            candidate("A", "Z_LAST"),
            candidate("B", "REACTION"),
            candidate("C", "REACTION"),
        )
        session.actors["C"].initiative = 100
        before = deepcopy(session.__dict__)
        for supplied in permutations(expected):
            self.assertEqual(expected, session.order_reactions(supplied))
        self.assertEqual(before, session.__dict__)

    def test_reaction_candidates_validate_priority_and_actor_membership(self):
        candidate = combat_state.ReactionCandidate
        for priority in (True, False, 1.5, "2", None):
            with self.subTest(priority=priority), self.assertRaises(ValueError):
                candidate("A", "R", trigger_priority=priority)
        self.assertEqual(0, candidate("A", "R").trigger_priority)
        session, primary = active_session(line_map(3))
        future = actor("FUTURE", TacticalCoord(2, 0, 0))
        session.add_reinforcement(future)
        before = deepcopy(session.__dict__)
        for supplied in ((object(),), (candidate("UNKNOWN", "R"),),
                         (candidate("FUTURE", "R"),)):
            with self.subTest(candidates=supplied), self.assertRaises(ValueError):
                session.order_reactions(supplied)
            self.assertEqual(before, session.__dict__)

    def test_incapacitated_active_actor_cannot_move_prepare_or_end(self):
        for operation in ("move", "prepare", "end"):
            with self.subTest(operation=operation):
                session, primary = active_session(line_map(3))
                primary.incapacitated = True
                before = deepcopy(session.__dict__)
                with self.assertRaisesRegex(ValueError, "incapacitated"):
                    self.commit(session, primary.actor_id, operation)
                self.assertEqual(before, session.__dict__)

    def test_incapacitation_ends_active_turn_and_discards_reserved_budget(self):
        second = actor("SECOND", TacticalCoord(2, 0, 0), initiative=5)
        session, primary = active_session(line_map(3), extra_actors=(second,))
        self.commit(session, primary.actor_id, "prepare")
        primary.incapacitated = True
        event_index = session.event_index
        self.assertIs(second, session.begin_next_activation())
        self.assertEqual(combat_state.ACTIVATION_SKIPPED, primary.activation_state)
        self.assertEqual((0, 0, None), (primary.action_budget,
                                     primary.reaction_reserve,
                                     primary.reserved_reaction_id))
        self.assertEqual(event_index, session.event_index)

    def test_skipped_incapacitated_actor_loses_old_reserve(self):
        second = actor("SECOND", TacticalCoord(2, 0, 0), initiative=5)
        session, primary = active_session(line_map(3), extra_actors=(second,))
        second.reaction_reserve = 1
        second.reserved_reaction_id = "R"
        second.incapacitated = True
        session.complete_active_activation()
        self.assertIsNone(session.begin_next_activation())
        self.assertEqual((0, None), (second.reaction_reserve,
                                   second.reserved_reaction_id))

    def test_reaction_rechecks_incapacitation_after_candidate_ordering(self):
        session, primary = active_session(line_map(3))
        self.commit(session, primary.actor_id, "prepare")
        queued, = session.order_reactions((
            combat_state.ReactionCandidate(primary.actor_id, "REACTION"),))
        primary.incapacitated = True
        before = deepcopy(session.__dict__)
        with self.assertRaisesRegex(ValueError, "incapacitated"):
            session.consume_reaction(actor_id=queued.actor_id,
                                     reaction_id=queued.reaction_id)
        self.assertEqual(before, session.__dict__)

    def test_ended_encounter_rejects_actions_and_scheduler_mutations(self):
        for operation in ("move", "prepare", "end", "consume", "begin",
                          "complete", "advance", "reinforce"):
            with self.subTest(operation=operation):
                session, primary = active_session(line_map(3))
                if operation == "consume":
                    self.commit(session, primary.actor_id, "prepare")
                if operation == "advance":
                    session.complete_active_activation()
                session.encounter_status = "resolved"
                before = deepcopy(session.__dict__)
                with self.assertRaisesRegex(ValueError, "encounter.*active"):
                    self.commit(session, primary.actor_id, operation)
                self.assertEqual(before, session.__dict__)

    def test_all_commits_roll_back_even_after_event_was_appended(self):
        for operation in ("move", "sprint", "prepare", "consume", "end"):
            with self.subTest(operation=operation):
                session, primary = active_session(line_map(3))
                if operation == "consume":
                    self.commit(session, primary.actor_id, "prepare")
                before = deepcopy(session.__dict__)
                append = session._append_event

                def fail_after_append(**kwargs):
                    append(**kwargs)
                    raise RuntimeError("failure after append")

                with patch.object(session, "_append_event", fail_after_append):
                    with self.assertRaisesRegex(RuntimeError, "after append"):
                        self.commit(session, primary.actor_id, operation)
                self.assertEqual(before, session.__dict__)

    def test_movement_event_preserves_existing_reaction_reserve(self):
        session, primary = active_session(line_map(3))
        self.commit(session, primary.actor_id, "prepare")
        event = self.commit(session, primary.actor_id, "move")
        self.assertEqual((1, 1), (event.reserve_before, event.reserve_after))
        self.assertEqual(1, primary.reaction_reserve)

    def test_invalid_next_round_initiative_rejects_without_partial_advance(self):
        for initiative in (float("nan"), float("inf"), True, "fast"):
            with self.subTest(initiative=initiative):
                session, primary = active_session(line_map(3))
                session.complete_active_activation()
                primary.initiative = initiative
                before = deepcopy(session.__dict__)
                with self.assertRaisesRegex(ValueError, "initiative"):
                    session.advance_round()
                self.assertEqual(before, session.__dict__)

    def test_sprint_accepts_ten_points_and_rejects_eleven_without_commit(self):
        session, primary = active_session(line_map(12))
        before = deepcopy(session.__dict__)
        with self.assertRaisesRegex(ValueError, "allowance"):
            session.commit_movement(actor_id=primary.actor_id, action_id="ACTION_SPRINT",
                                    goal=TacticalCoord(11, 0, 0))
        self.assertEqual(before, session.__dict__)
        event = session.commit_movement(actor_id=primary.actor_id, action_id="ACTION_SPRINT",
                                        goal=TacticalCoord(10, 0, 0))
        self.assertEqual(TacticalCoord(10, 0, 0), event.coord_after)
        self.assertEqual(2, event.budget_after)

    def test_saved_game_seed_runs_deterministically_without_durable_mutation(self):
        durable = GameState(seed="campaign-seed", scene_id="SCENE_TEST",
                            player={"attributes": {"Strength": 5}},
                            flags={"FLAG_TEST": True})
        before = dumps_state(durable)

        def run(previews):
            primary = actor("A", TacticalCoord(0, 0, 0))
            session = combat_state.CombatSession(
                encounter_id="REPLAY", tactical_map=line_map(4), seed=durable.seed,
                actors=(primary,), combat_actions=actions())
            session.begin_next_activation()
            for _ in range(previews):
                session.preview_movement(actor_id="A", action_id="ACTION_MOVE",
                                         goal=TacticalCoord(1, 0, 0))
            self.commit(session, "A", "move")
            self.commit(session, "A", "prepare")
            self.commit(session, "A", "end")
            self.commit(session, "A", "consume")
            session.add_reinforcement(actor("B", TacticalCoord(3, 0, 0), initiative=30))
            session.advance_round()
            self.assertEqual("B", session.begin_next_activation().actor_id)
            self.commit(session, "B", "end")
            return session

        first, second = run(0), run(3)
        self.assertEqual(first.committed_events, second.committed_events)
        self.assertEqual(first.normalized_transcript(), second.normalized_transcript())
        self.assertEqual(first.transcript_hash(), second.transcript_hash())
        expected = hashlib.sha256(b"campaign-seed|REPLAY|1|1|1|A|ACTION_MOVE|1,0,0").hexdigest()
        self.assertEqual(expected, first.committed_events[0].digest)
        self.assertEqual(before, dumps_state(durable))
        self.assertEqual(list(range(1, 6)), [event.event_index for event in first.committed_events])

    @staticmethod
    def commit(session, actor_id, operation):
        if operation in ("move", "sprint"):
            return session.commit_movement(actor_id=actor_id,
                action_id="ACTION_MOVE" if operation == "move" else "ACTION_SPRINT",
                goal=TacticalCoord(1, 0, 0))
        if operation == "prepare":
            return session.reserve_reaction(actor_id=actor_id,
                prepare_action_id="ACTION_PREPARE_REACTION", reaction_id="REACTION")
        if operation == "consume":
            return session.consume_reaction(actor_id=actor_id, reaction_id="REACTION")
        if operation == "end":
            return session.commit_end_activation(actor_id=actor_id, action_id="ACTION_END")
        if operation == "begin":
            return session.begin_next_activation()
        if operation == "complete":
            return session.complete_active_activation()
        if operation == "advance":
            return session.advance_round()
        if operation == "reinforce":
            return session.add_reinforcement(actor("B", TacticalCoord(2, 0, 0)))
        raise AssertionError(f"unhandled test operation: {operation}")


if __name__ == "__main__":
    unittest.main()
