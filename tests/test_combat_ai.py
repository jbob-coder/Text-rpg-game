from copy import deepcopy
from dataclasses import replace
import json
import unittest

from textrpg import combat_ai as ai
from textrpg.combat_rules import Objective
from textrpg.combat_schema import TacticalCoord
from test_combat_objectives import encounter


class CombatAITests(unittest.TestCase):
    def test_objective_move_has_priority_and_selection_is_read_only(self):
        session, controller = encounter((Objective("REACH", "REACH_CELL", "PLAYER", anchor_id="OBJECTIVE"),))
        before = deepcopy(session.__dict__)
        decision = ai.choose_action(controller, "PLAYER")
        self.assertEqual("ACTION_MOVE", decision.selected.action_id)
        self.assertEqual(TacticalCoord(5, 0, 0), decision.selected.goal)
        self.assertEqual(before, session.__dict__)
        controller.commit_movement("PLAYER", decision.selected.action_id, decision.selected.goal)
        self.assertEqual("completed", session.encounter_status)

    def test_hidden_actor_location_does_not_change_choice_or_candidates(self):
        session, controller = encounter((Objective("REACH", "REACH_CELL", "PLAYER", anchor_id="OBJECTIVE"),))
        profile = ai.AIProfile(hostile_actor_ids=("ENEMY",))
        first = ai.choose_action(controller, "PLAYER", profile=profile)
        session.actors["ENEMY"].coord = TacticalCoord(3, 0, 0)
        second = ai.choose_action(controller, "PLAYER", profile=profile)
        self.assertEqual(first, second)
        self.assertNotIn("ENEMY", json.dumps(first.diagnostics))
        session.tactical_map = replace(session.tactical_map, cells=tuple(
            replace(cell, hazard_ids=("SECRET_TRAP",)) if cell.coord.x == 2 else cell
            for cell in session.tactical_map.cells))
        self.assertEqual(second, ai.choose_action(controller, "PLAYER", profile=profile))

    def test_hidden_target_cannot_be_added_by_focus_order(self):
        session, controller = encounter()
        session.combat_actions["SHOT"] = {"category": "attack", "cost": 1,
            "range_max": 6, "requires_detection": True, "requires_los": True}
        controller.action_loadouts["PLAYER"] += ("SHOT",)
        profile = ai.AIProfile(hostile_actor_ids=("ENEMY",))
        order = ai.CompanionOrder("FOCUS_TARGET", "ENEMY")
        hidden = ai.choose_action(controller, "PLAYER", profile=profile, order=order)
        self.assertNotEqual("SHOT", hidden.selected.action_id)
        controller.knowledge.record_detection("PLAYER", "ENEMY", detected=True)
        known = ai.choose_action(controller, "PLAYER", profile=profile, order=order)
        self.assertEqual("SHOT", known.selected.action_id)
        self.assertEqual("ENEMY", known.selected.target_key)

    def test_hold_order_changes_utility_without_changing_legal_candidates(self):
        session, controller = encounter()
        normal = ai.choose_action(controller, "PLAYER", goal=TacticalCoord(4, 0, 0))
        held = ai.choose_action(controller, "PLAYER", goal=TacticalCoord(4, 0, 0),
                                order=ai.CompanionOrder("HOLD"))
        self.assertEqual("ACTION_MOVE", normal.selected.action_id)
        self.assertEqual("ACTION_END", held.selected.action_id)
        self.assertEqual({(c.action_id, c.target_key) for c in normal.candidates},
                         {(c.action_id, c.target_key) for c in held.candidates})

    def test_withdraw_order_moves_to_exit_then_uses_legal_retreat(self):
        session, controller = encounter()
        order = ai.CompanionOrder("WITHDRAW")
        move = ai.choose_action(controller, "PLAYER", order=order).selected
        self.assertEqual(TacticalCoord(0, 0, 0), move.goal)
        controller.commit_movement("PLAYER", move.action_id, move.goal)
        retreat = ai.choose_action(controller, "PLAYER", order=order).selected
        self.assertEqual("RETREAT", retreat.action_id)
        controller.commit_retreat("PLAYER", retreat.action_id, retreat.target_key)
        self.assertEqual("retreated", session.encounter_status)

    def test_stable_tie_does_not_depend_on_loadout_iteration(self):
        session, controller = encounter()
        session.combat_actions["ZZ_MOVE"] = dict(session.combat_actions["ACTION_MOVE"])
        controller.action_loadouts["PLAYER"] += ("ZZ_MOVE",)
        first = ai.choose_action(controller, "PLAYER", goal=TacticalCoord(4, 0, 0))
        controller.action_loadouts["PLAYER"] = tuple(reversed(controller.action_loadouts["PLAYER"]))
        self.assertEqual(first, ai.choose_action(controller, "PLAYER", goal=TacticalCoord(4, 0, 0)))
        self.assertEqual("ACTION_MOVE", first.selected.action_id)

    def test_candidate_limit_is_enforced_and_end_remains_available(self):
        session, controller = encounter()
        decision = ai.choose_action(controller, "PLAYER", profile=ai.AIProfile(max_candidates=3))
        self.assertLessEqual(len(decision.candidates), 3)
        self.assertIn("ACTION_END", [candidate.action_id for candidate in decision.candidates])
        session.actors["PLAYER"].action_budget = 0
        self.assertEqual("ACTION_END", ai.choose_action(controller, "PLAYER").selected.action_id)

    def test_beast_doctrine_uses_same_knowledge_and_legality(self):
        session, controller = encounter()
        profile = ai.AIProfile(doctrine="beast", hostile_actor_ids=("ENEMY",))
        decision = ai.choose_action(controller, "PLAYER", profile=profile)
        self.assertTrue(all(candidate.target_key != "ENEMY" for candidate in decision.candidates))
        for candidate in decision.candidates:
            controller.action("PLAYER", candidate.action_id)

    def test_cautious_and_aggressive_doctrine_rank_the_same_legal_choices_differently(self):
        session, controller = encounter()
        session.combat_actions["SHOT"] = {"category": "attack", "cost": 1,
            "range_max": 6, "requires_detection": True, "requires_los": True}
        controller.action_loadouts["PLAYER"] += ("SHOT",)
        controller.knowledge.record_detection("PLAYER", "ENEMY", detected=True)
        session.tactical_map = replace(session.tactical_map, cells=tuple(
            replace(cell, cover=(("E", 2),)) if cell.coord.x == 2 else cell
            for cell in session.tactical_map.cells))
        cautious = ai.choose_action(controller, "PLAYER",
            profile=ai.AIProfile(doctrine="cautious", hostile_actor_ids=("ENEMY",)))
        aggressive = ai.choose_action(controller, "PLAYER",
            profile=ai.AIProfile(doctrine="aggressive", hostile_actor_ids=("ENEMY",)))
        self.assertEqual("ACTION_MOVE", cautious.selected.action_id)
        self.assertEqual(TacticalCoord(2, 0, 0), cautious.selected.goal)
        self.assertEqual("SHOT", aggressive.selected.action_id)
        self.assertEqual({(c.action_id, c.target_key) for c in cautious.candidates},
                         {(c.action_id, c.target_key) for c in aggressive.candidates})

    def test_developer_diagnostics_and_private_objectives_are_not_projected(self):
        session, controller = encounter((Objective("SECRET_ENEMY_GOAL", "REACH_CELL", "ENEMY", anchor_id="OBJECTIVE"),))
        before = controller.player_view("PLAYER")
        decision = ai.choose_action(controller, "PLAYER")
        controller.developer_diagnostics = decision.diagnostics
        self.assertEqual(before, controller.player_view("PLAYER"))
        projected = json.dumps(controller.player_view("PLAYER"))
        for secret in ("utility", "candidates", "SECRET_ENEMY_GOAL", "ENEMY"):
            self.assertNotIn(secret, projected)


if __name__ == "__main__":
    unittest.main()
