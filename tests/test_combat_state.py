from __future__ import annotations

import unittest

from textrpg.combat_schema import TacticalCell, TacticalCoord, TacticalMap
from textrpg.combat_state import (
    ACTIVATION_ACTIVE,
    ACTIVATION_SKIPPED,
    PHASE1_ACTION_BUDGET,
    CombatSession,
    TacticalActorState,
)


def two_by_two_map(*, blocked: TacticalCoord | None = None) -> TacticalMap:
    cells = []
    for y in range(2):
        for x in range(2):
            coord = TacticalCoord(x, y, 0)
            cells.append(
                TacticalCell(
                    coord,
                    blocks_movement=coord == blocked,
                )
            )
    return TacticalMap(
        "MAP_SESSION_TEST",
        1,
        2,
        2,
        (0,),
        tuple(cells),
    )


def actor(
    actor_id: str,
    x: int,
    y: int,
    *,
    faction_id: str = "FACTION_TEST",
    initiative: float = 10,
    incapacitated: bool = False,
) -> TacticalActorState:
    return TacticalActorState(
        actor_id=actor_id,
        faction_id=faction_id,
        coord=TacticalCoord(x, y, 0),
        initiative=initiative,
        incapacitated=incapacitated,
    )


class CombatStateTests(unittest.TestCase):
    def test_session_initialization_snapshots_stable_initiative_order(self) -> None:
        low = actor("ACTOR_LOW", 0, 0, initiative=4)
        tie_b = actor("ACTOR_TIE_B", 1, 0, initiative=9)
        tie_a = actor("ACTOR_TIE_A", 0, 1, initiative=9)

        session = CombatSession(
            encounter_id="ENCOUNTER_SESSION_TEST",
            tactical_map=two_by_two_map(),
            seed=17,
            actors=(low, tie_b, tie_a),
        )

        self.assertEqual(1, session.round_index)
        self.assertEqual(0, session.activation_index)
        self.assertEqual(0, session.event_index)
        self.assertIsNone(session.active_actor_id)
        self.assertEqual(
            ("ACTOR_TIE_A", "ACTOR_TIE_B", "ACTOR_LOW"),
            session.initiative_order,
        )

        low.initiative = 99
        self.assertEqual(
            ("ACTOR_TIE_A", "ACTOR_TIE_B", "ACTOR_LOW"),
            session.initiative_order,
        )

    def test_session_rejects_duplicate_actor_ids_and_solid_spawn_conflict(self) -> None:
        with self.assertRaisesRegex(ValueError, "duplicate tactical actor id"):
            CombatSession(
                encounter_id="ENCOUNTER_SESSION_TEST",
                tactical_map=two_by_two_map(),
                seed=1,
                actors=(
                    actor("ACTOR_DUP", 0, 0),
                    actor("ACTOR_DUP", 1, 0),
                ),
            )

        with self.assertRaisesRegex(ValueError, "solid occupancy conflict"):
            CombatSession(
                encounter_id="ENCOUNTER_SESSION_TEST",
                tactical_map=two_by_two_map(),
                seed=1,
                actors=(
                    actor("ACTOR_A", 0, 0),
                    actor("ACTOR_B", 0, 0),
                ),
            )

    def test_session_rejects_unknown_or_blocked_spawn(self) -> None:
        with self.assertRaisesRegex(ValueError, "unknown cell"):
            CombatSession(
                encounter_id="ENCOUNTER_SESSION_TEST",
                tactical_map=two_by_two_map(),
                seed=1,
                actors=(actor("ACTOR_A", 9, 9),),
            )

        blocked = TacticalCoord(1, 1, 0)
        with self.assertRaisesRegex(ValueError, "blocked cell"):
            CombatSession(
                encounter_id="ENCOUNTER_SESSION_TEST",
                tactical_map=two_by_two_map(blocked=blocked),
                seed=1,
                actors=(actor("ACTOR_A", 1, 1),),
            )

    def test_activation_starts_with_four_budget_and_uses_round_snapshot(self) -> None:
        first = actor("ACTOR_FIRST", 0, 0, initiative=20)
        second = actor("ACTOR_SECOND", 1, 0, initiative=10)
        session = CombatSession(
            encounter_id="ENCOUNTER_SESSION_TEST",
            tactical_map=two_by_two_map(),
            seed=1,
            actors=(second, first),
        )

        active = session.begin_next_activation()

        self.assertIs(first, active)
        self.assertEqual("ACTOR_FIRST", session.active_actor_id)
        self.assertEqual(1, session.activation_index)
        self.assertEqual(PHASE1_ACTION_BUDGET, first.action_budget)
        self.assertEqual(ACTIVATION_ACTIVE, first.activation_state)
        self.assertEqual(0, session.event_index)
        self.assertEqual([], session.committed_events)

    def test_incapacitated_actor_is_skipped_if_state_changes_before_activation(self) -> None:
        first = actor("ACTOR_FIRST", 0, 0, initiative=20)
        second = actor("ACTOR_SECOND", 1, 0, initiative=10)
        session = CombatSession(
            encounter_id="ENCOUNTER_SESSION_TEST",
            tactical_map=two_by_two_map(),
            seed=1,
            actors=(first, second),
        )
        first.incapacitated = True

        active = session.begin_next_activation()

        self.assertEqual(ACTIVATION_SKIPPED, first.activation_state)
        self.assertEqual(0, first.action_budget)
        self.assertIs(second, active)
        self.assertEqual("ACTOR_SECOND", session.active_actor_id)
        self.assertEqual(2, session.activation_index)

    def test_incapacitated_spawn_is_nonblocking_by_phase1_default(self) -> None:
        body = actor("ACTOR_BODY", 0, 0, incapacitated=True)
        active = actor("ACTOR_ACTIVE", 0, 0)
        session = CombatSession(
            encounter_id="ENCOUNTER_SESSION_TEST",
            tactical_map=two_by_two_map(),
            seed=1,
            actors=(body, active),
        )

        self.assertEqual(("ACTOR_ACTIVE",), session.initiative_order)


    def test_activation_completion_expires_budget_and_allows_next_actor(self) -> None:
        first = actor("ACTOR_FIRST", 0, 0, initiative=20)
        second = actor("ACTOR_SECOND", 1, 0, initiative=10)
        session = CombatSession(
            encounter_id="ENCOUNTER_SESSION_TEST",
            tactical_map=two_by_two_map(),
            seed=1,
            actors=(first, second),
        )

        self.assertIs(first, session.begin_next_activation())
        first.action_budget = 2
        completed = session.complete_active_activation()

        self.assertIs(first, completed)
        self.assertEqual(0, first.action_budget)
        self.assertIsNone(session.active_actor_id)

        self.assertIs(second, session.begin_next_activation())
        self.assertEqual(PHASE1_ACTION_BUDGET, second.action_budget)

    def test_round_advance_resnapshots_initiative_only_after_round_completion(self) -> None:
        first = actor("ACTOR_FIRST", 0, 0, initiative=20)
        second = actor("ACTOR_SECOND", 1, 0, initiative=10)
        session = CombatSession(
            encounter_id="ENCOUNTER_SESSION_TEST",
            tactical_map=two_by_two_map(),
            seed=1,
            actors=(first, second),
        )

        with self.assertRaisesRegex(ValueError, "activations remain"):
            session.advance_round()

        self.assertIs(first, session.begin_next_activation())
        second.initiative = 30
        session.complete_active_activation()
        self.assertIs(second, session.begin_next_activation())
        session.complete_active_activation()

        self.assertTrue(session.round_is_complete())
        self.assertIsNone(session.begin_next_activation())
        self.assertEqual(("ACTOR_SECOND", "ACTOR_FIRST"), session.advance_round())
        self.assertEqual(2, session.round_index)
        self.assertEqual(0, session.activation_index)
        self.assertEqual(0, first.action_budget)
        self.assertEqual(0, second.action_budget)

    def test_incapacitated_actor_stays_out_of_next_round_snapshot(self) -> None:
        first = actor("ACTOR_FIRST", 0, 0, initiative=20)
        second = actor("ACTOR_SECOND", 1, 0, initiative=10)
        session = CombatSession(
            encounter_id="ENCOUNTER_SESSION_TEST",
            tactical_map=two_by_two_map(),
            seed=1,
            actors=(first, second),
        )

        session.begin_next_activation()
        session.complete_active_activation()
        session.begin_next_activation()
        session.complete_active_activation()
        first.incapacitated = True

        self.assertEqual(("ACTOR_SECOND",), session.advance_round())
        self.assertEqual(ACTIVATION_SKIPPED, first.activation_state)


if __name__ == "__main__":
    unittest.main()
