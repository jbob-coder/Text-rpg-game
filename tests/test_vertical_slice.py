import json
import unittest
from pathlib import Path

from textrpg import GameState, RulesEngine, validate_character_visuals, validate_content_pack


ROOT = Path(__file__).resolve().parents[1]


def load_slice():
    return json.loads(
        (ROOT / "content" / "vertical_slice_01.json").read_text(encoding="utf-8")
    )


def make_state(data):
    return GameState(**data["initial_state"])


class VerticalSliceTests(unittest.TestCase):
    def test_content_pack_and_visual_identities_are_valid(self):
        data = load_slice()
        self.assertEqual(
            validate_content_pack(data["scenes"], data["quests"]),
            [],
        )
        self.assertEqual(
            validate_character_visuals(data["characters"]),
            [],
        )

    def test_cooperative_route_completes_quest_with_party_state(self):
        data = load_slice()
        state = make_state(data)
        engine = RulesEngine(
            data["scenes"],
            quest_definitions=data["quests"],
        )

        engine.choose(state, "TAKE_DEAD_RELAY")
        self.assertEqual(
            state.quests["QUEST_DEAD_RELAY"]["stage"],
            "STAGE_RELAY",
        )
        self.assertIn(
            "OBJ_RECOVER_RELAY",
            state.quests["QUEST_DEAD_RELAY"]["completed_objectives"],
        )

        engine.choose(state, "USE_MAINTENANCE_SEAL")
        self.assertEqual(state.scene_id, "OPENING_DECISION")
        self.assertEqual(
            state.quests["QUEST_DEAD_RELAY"]["stage"],
            "STAGE_DECIDE",
        )
        self.assertIn(
            "KNOW_RELAY_DESTINATION_SERVICE_GATE_12",
            state.knowledge,
        )

        engine.choose(state, "TELL_TAMSIN_GATE_TWELVE")
        self.assertEqual(
            state.quests["QUEST_DEAD_RELAY"]["stage"],
            "STAGE_TUNNEL_ROUTE",
        )
        self.assertIn("NPC_TAMSIN", state.party)
        self.assertIn(
            "KNOW_RELAY_DESTINATION_SERVICE_GATE_12",
            state.npcs["NPC_TAMSIN"]["knowledge"],
        )

        engine.choose(state, "ENTER_GATE_TWELVE_WITH_TAMSIN")
        self.assertEqual(
            state.quests["QUEST_DEAD_RELAY"]["status"],
            "completed",
        )
        self.assertEqual(state.flags["opening.route"], "tunnel_with_tamsin")

        engine.choose(state, "END_VERTICAL_SLICE")
        self.assertTrue(state.flags["vertical_slice_01.complete"])

    def test_solo_route_preserves_private_destination_knowledge(self):
        data = load_slice()
        state = make_state(data)
        engine = RulesEngine(
            data["scenes"],
            quest_definitions=data["quests"],
        )

        engine.choose(state, "TAKE_DEAD_RELAY")
        engine.choose(state, "USE_MAINTENANCE_SEAL")
        engine.choose(state, "KEEP_GATE_TWELVE_SECRET")

        self.assertNotIn(
            "KNOW_RELAY_DESTINATION_SERVICE_GATE_12",
            state.npcs["NPC_TAMSIN"]["knowledge"],
        )
        self.assertGreater(
            state.relationships["NPC_TAMSIN"]["suspicion"],
            5,
        )
        self.assertEqual(
            state.quests["QUEST_DEAD_RELAY"]["stage"],
            "STAGE_SOLO_ROUTE",
        )

        engine.choose(state, "LEAVE_DEPOT_ALONE")
        self.assertEqual(state.flags["opening.route"], "solo")
        self.assertEqual(
            state.quests["QUEST_DEAD_RELAY"]["status"],
            "completed",
        )

    def test_failed_force_route_recombines_through_recovery(self):
        data = load_slice()
        state = make_state(data)
        engine = RulesEngine(
            data["scenes"],
            quest_definitions=data["quests"],
        )

        engine.choose(state, "TAKE_DEAD_RELAY")
        event = engine.choose(state, "FORCE_RELAY_CASING")

        self.assertEqual(event["outcome"], "critical_failure")
        self.assertEqual(state.scene_id, "OPENING_RECOVERY")
        self.assertEqual(
            state.quests["QUEST_DEAD_RELAY"]["stage"],
            "STAGE_RECOVER",
        )
        self.assertTrue(state.flags["relay.signal_lost"])

        engine.choose(state, "ASK_TAMSIN_FOR_RECOVERY_HELP")
        self.assertEqual(state.scene_id, "OPENING_DECISION")
        self.assertEqual(
            state.quests["QUEST_DEAD_RELAY"]["stage"],
            "STAGE_DECIDE",
        )
        self.assertIn(
            "KNOW_RELAY_DESTINATION_SERVICE_GATE_12",
            state.npcs["NPC_TAMSIN"]["knowledge"],
        )


if __name__ == "__main__":
    unittest.main()
