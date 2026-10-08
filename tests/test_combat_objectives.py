from copy import deepcopy
import unittest
from unittest.mock import patch

from textrpg import combat_rules as rules
from textrpg.combat_schema import TacticalAnchor, TacticalCell, TacticalCoord, TacticalMap
from textrpg.combat_state import CombatSession
from test_combat_turns import actions, actor


def encounter(objectives=(), *, player_x=1):
    tactical_map = TacticalMap("MAP_OBJECTIVES", 1, 7, 1, (0,),
        tuple(TacticalCell(TacticalCoord(x, 0, 0)) for x in range(7)),
        objective_anchors=(TacticalAnchor("OBJECTIVE", TacticalCoord(5, 0, 0)),),
        exits=(TacticalAnchor("EXIT_GATE", TacticalCoord(0, 0, 0)),))
    definitions = actions()
    definitions.update({
        "INTERACT": {"category": "interact", "cost": 1, "range_max": 1, "requires_los": True},
        "RETREAT": {"category": "retreat", "cost": 1},
        "DETECT": {"category": "detect", "cost": 1, "range_max": 6},
    })
    session = CombatSession(encounter_id="ENCOUNTER_TEST", seed="saved-seed",
        tactical_map=tactical_map, actors=(actor("PLAYER", TacticalCoord(player_x, 0, 0), initiative=20),
                                          actor("ENEMY", TacticalCoord(6, 0, 0), faction_id="ENEMY", initiative=5)),
        combat_actions=definitions)
    session.begin_next_activation()
    controller = rules.EncounterRules(session, controller_id="PLAYER", objectives=objectives,
        action_loadouts={actor_id: tuple(definitions) for actor_id in session.actors},
        detection_stats={"PLAYER": rules.DetectionStats(100, 0), "ENEMY": rules.DetectionStats(0, 0)})
    return session, controller


class CombatObjectiveTests(unittest.TestCase):
    def test_reach_objective_resolves_only_after_committed_movement(self):
        objective = rules.Objective("REACH", "REACH_CELL", "PLAYER", anchor_id="OBJECTIVE")
        session, controller = encounter((objective,))
        before = deepcopy(session.__dict__)
        controller.knowledge.preview_movement("PLAYER", "ACTION_MOVE", TacticalCoord(5, 0, 0))
        self.assertEqual(before, session.__dict__)
        self.assertEqual("pending", controller.objective_results["REACH"])
        controller.commit_movement("PLAYER", "ACTION_MOVE", TacticalCoord(5, 0, 0))
        self.assertEqual("completed", controller.objective_results["REACH"])
        self.assertEqual("completed", session.encounter_status)

    def test_interaction_then_escape_resolves_without_elimination(self):
        objectives = (rules.Objective("READ", "INTERACT_RETRIEVE", "PLAYER", anchor_id="OBJECTIVE"),
                      rules.Objective("LEAVE", "ESCAPE", "PLAYER", anchor_id="EXIT_GATE"))
        session, controller = encounter(objectives, player_x=4)
        controller.commit_interaction("PLAYER", "INTERACT", "READ")
        self.assertEqual("active", session.encounter_status)
        controller.commit_movement("PLAYER", "ACTION_MOVE", TacticalCoord(0, 0, 0))
        controller.commit_retreat("PLAYER", "RETREAT", "EXIT_GATE")
        self.assertEqual("completed", session.encounter_status)
        self.assertEqual({"READ": "completed", "LEAVE": "completed"}, controller.objective_results)
        self.assertTrue(session.actors["PLAYER"].withdrawn)
        self.assertFalse(session.actors["ENEMY"].incapacitated)
        self.assertNotIn("PLAYER", [occupant.actor_id for occupant in session._occupants()])

    def test_retreat_must_reach_an_authored_exit_and_does_not_grant_objective(self):
        objective = rules.Objective("READ", "INTERACT_RETRIEVE", "PLAYER", anchor_id="OBJECTIVE")
        session, controller = encounter((objective,))
        before = deepcopy(session.__dict__)
        for exit_id in ("EXIT_GATE", "OFF_MAP"):
            with self.assertRaises(ValueError):
                controller.commit_retreat("PLAYER", "RETREAT", exit_id)
            self.assertEqual(before, session.__dict__)
        controller.commit_movement("PLAYER", "ACTION_MOVE", TacticalCoord(0, 0, 0))
        controller.commit_retreat("PLAYER", "RETREAT", "EXIT_GATE")
        self.assertEqual("retreated", session.encounter_status)
        self.assertEqual("pending", controller.objective_results["READ"])

    def test_enemy_withdrawal_removes_future_turn_and_reaction_authority(self):
        session, controller = encounter()
        session.complete_active_activation()
        enemy = session.begin_next_activation()
        enemy.coord = TacticalCoord(0, 0, 0)
        session.reserve_reaction(actor_id="ENEMY", prepare_action_id="ACTION_PREPARE_REACTION", reaction_id="R")
        controller.commit_retreat("ENEMY", "RETREAT", "EXIT_GATE")
        self.assertEqual("active", session.encounter_status)
        self.assertEqual((0, None), (enemy.reaction_reserve, enemy.reserved_reaction_id))
        self.assertEqual(("PLAYER",), session.advance_round())
        with self.assertRaises(ValueError):
            session.consume_reaction(actor_id="ENEMY", reaction_id="R")

    def test_interaction_revalidates_budget_range_and_ownership_atomically(self):
        objective = rules.Objective("READ", "INTERACT_RETRIEVE", "PLAYER", anchor_id="OBJECTIVE")
        session, controller = encounter((objective,))
        before = deepcopy(session.__dict__)
        with self.assertRaises(ValueError):
            controller.commit_interaction("PLAYER", "INTERACT", "READ")
        self.assertEqual(before, session.__dict__)
        session.actors["PLAYER"].coord = TacticalCoord(4, 0, 0)
        session.actors["PLAYER"].action_budget = 0
        with self.assertRaises(ValueError):
            controller.commit_interaction("PLAYER", "INTERACT", "READ")
        self.assertEqual("pending", controller.objective_results["READ"])
        self.assertEqual(0, session.event_index)

    def test_post_append_failures_restore_objective_departure_and_detection_state(self):
        objective = rules.Objective("READ", "INTERACT_RETRIEVE", "PLAYER", anchor_id="OBJECTIVE")
        for operation in ("interact", "retreat", "detect", "move"):
            with self.subTest(operation=operation):
                session, controller = encounter((objective,), player_x=0 if operation == "retreat" else 4)
                before = deepcopy(session.__dict__)
                results_before = dict(controller.objective_results)
                append = session._append_event

                def fail(**kwargs):
                    append(**kwargs)
                    raise RuntimeError("append failure")

                with patch.object(session, "_append_event", fail), self.assertRaises(RuntimeError):
                    if operation == "interact":
                        controller.commit_interaction("PLAYER", "INTERACT", "READ")
                    elif operation == "retreat":
                        controller.commit_retreat("PLAYER", "RETREAT", "EXIT_GATE")
                    elif operation == "detect":
                        controller.commit_detection("PLAYER", "DETECT")
                    else:
                        controller.commit_movement("PLAYER", "ACTION_MOVE", TacticalCoord(5, 0, 0))
                self.assertEqual(before, session.__dict__)
                self.assertEqual(results_before, controller.objective_results)
                self.assertEqual({}, controller.knowledge.contacts)

    def test_detection_is_deterministic_committed_and_preview_neutral(self):
        sessions = []
        for previews in (0, 3):
            session, controller = encounter()
            for _ in range(previews):
                controller.player_view("PLAYER")
            controller.commit_detection("PLAYER", "DETECT")
            self.assertEqual(1, session.event_index)
            self.assertEqual(3, session.actors["PLAYER"].action_budget)
            self.assertEqual("DETECTED", controller.player_view("PLAYER")["contacts"][0]["awareness"])
            sessions.append((session.normalized_transcript(), controller.player_view("PLAYER")))
        self.assertEqual(*sessions)

    def test_committed_enemy_movement_runs_observer_specific_detection(self):
        session, controller = encounter()
        self.assertEqual([], controller.player_view("PLAYER")["contacts"])
        session.complete_active_activation()
        session.begin_next_activation()
        controller.commit_movement("ENEMY", "ACTION_MOVE", TacticalCoord(5, 0, 0))
        contact, = controller.player_view("PLAYER")["contacts"]
        self.assertEqual("DETECTED", contact["awareness"])
        self.assertEqual("5,0,0", contact["coord"])
        self.assertEqual(1, session.event_index)

    def test_arrived_reinforcement_does_not_break_existing_observers(self):
        session, controller = encounter()
        session.add_reinforcement(actor("NEW", TacticalCoord(0, 0, 0), initiative=5))
        session.complete_active_activation()
        session.begin_next_activation()
        session.complete_active_activation()
        controller.advance_round()
        session.begin_next_activation()
        controller.commit_movement("PLAYER", "ACTION_MOVE", TacticalCoord(2, 0, 0))
        self.assertEqual(1, session.event_index)

    def test_survival_counts_completed_rounds_and_protect_fails_on_incapacity(self):
        objective = rules.Objective("SURVIVE", "SURVIVE_ROUNDS", "PLAYER", rounds=1)
        session, controller = encounter((objective,))
        session.complete_active_activation()
        session.begin_next_activation()
        session.complete_active_activation()
        self.assertEqual("pending", controller.objective_results["SURVIVE"])
        controller.advance_round()
        self.assertEqual("completed", controller.objective_results["SURVIVE"])
        objective = rules.Objective("PROTECT", "PROTECT_ACTOR", "PLAYER", target_ids=("ENEMY",), rounds=1)
        session, controller = encounter((objective,))
        session.actors["ENEMY"].incapacitated = True
        controller.evaluate_objectives()
        self.assertEqual("failed", controller.objective_results["PROTECT"])
        self.assertEqual("failed", session.encounter_status)

    def test_invalid_objective_binding_rejects_before_mutating_session(self):
        session, _ = encounter()
        before = deepcopy(session.__dict__)
        with self.assertRaises(ValueError):
            rules.EncounterRules(session, controller_id="PLAYER",
                objectives=(rules.Objective("BAD", "REACH_CELL", "PLAYER", anchor_id="MISSING"),),
                action_loadouts={actor_id: tuple(session.combat_actions) for actor_id in session.actors})
        self.assertEqual(before, session.__dict__)

    def test_actor_cannot_use_an_action_outside_its_loadout(self):
        session, controller = encounter()
        controller.action_loadouts["PLAYER"] = ("ACTION_END",)
        before = deepcopy(session.__dict__)
        with self.assertRaises(ValueError):
            controller.commit_detection("PLAYER", "DETECT")
        self.assertEqual(before, session.__dict__)

    def test_departed_controller_can_still_receive_the_resolution_view(self):
        session, controller = encounter(player_x=0)
        controller.commit_retreat("PLAYER", "RETREAT", "EXIT_GATE")
        view = controller.player_view("PLAYER")
        self.assertEqual("retreated", view["encounter_status"])
        self.assertEqual(0, view["action_budget"])
        self.assertEqual([], view["visible_cells"])

    def test_departed_observer_records_cannot_break_later_actor_movement(self):
        session, controller = encounter()
        controller.knowledge.record_detection("ENEMY", "PLAYER", detected=True)
        session.complete_active_activation()
        enemy = session.begin_next_activation()
        enemy.coord = TacticalCoord(0, 0, 0)
        controller.commit_retreat("ENEMY", "RETREAT", "EXIT_GATE")
        controller.advance_round()
        session.begin_next_activation()
        controller.commit_movement("PLAYER", "ACTION_MOVE", TacticalCoord(2, 0, 0))
        self.assertEqual(TacticalCoord(2, 0, 0), session.actors["PLAYER"].coord)

    def test_detection_failure_after_observation_rolls_back_cost_and_contacts(self):
        session, controller = encounter()
        before = deepcopy(session.__dict__)
        record = controller.knowledge.record_detection

        def fail(*args, **kwargs):
            record(*args, **kwargs)
            raise RuntimeError("after observation")

        with patch.object(controller.knowledge, "record_detection", fail), self.assertRaises(RuntimeError):
            controller.commit_detection("PLAYER", "DETECT")
        self.assertEqual({}, controller.knowledge.contacts)
        self.assertEqual(before, session.__dict__)

    def test_elimination_disable_and_capture_require_their_own_conditions(self):
        objective = rules.Objective("ELIMINATE", "ELIMINATE", "PLAYER", target_ids=("ENEMY",))
        session, controller = encounter((objective,))
        controller.evaluate_objectives()
        self.assertEqual("active", session.encounter_status)
        session.actors["ENEMY"].incapacitated = True
        controller.evaluate_objectives()
        self.assertEqual("completed", session.encounter_status)

        objective = rules.Objective("DISABLE", "DISABLE_OBJECT", "PLAYER", anchor_id="OBJECTIVE")
        session, controller = encounter((objective,), player_x=4)
        controller.commit_interaction("PLAYER", "INTERACT", "DISABLE")
        self.assertEqual("completed", controller.objective_results["DISABLE"])

        objective = rules.Objective("CAPTURE", "CAPTURE_ACTOR", "PLAYER", target_ids=("ENEMY",))
        session, controller = encounter((objective,), player_x=5)
        controller.knowledge.record_detection("PLAYER", "ENEMY", detected=True)
        with self.assertRaises(ValueError):
            controller.commit_interaction("PLAYER", "INTERACT", "CAPTURE")
        session.actors["ENEMY"].incapacitated = True
        controller.commit_interaction("PLAYER", "INTERACT", "CAPTURE")
        self.assertEqual("completed", controller.objective_results["CAPTURE"])


if __name__ == "__main__":
    unittest.main()
