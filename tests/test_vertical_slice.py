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
            validate_content_pack(data["scenes"], data["quests"], data.get("powers", {})),
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
            power_definitions=data.get("powers", {}),
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
        self.assertEqual(
            state.npcs["NPC_TAMSIN"]["story_state"]["TRACK_RELAY_CASE"],
            "ENTERED_GATE_TWELVE",
        )
        self.assertEqual(
            state.npcs["NPC_TAMSIN"]["goals"]["GOAL_UNDERSTAND_GATE_TWELVE"]["progress"],
            50.0,
        )

        engine.choose(state, "CONTINUE_BELOW_GATE_TWELVE")
        self.assertTrue(state.flags["vertical_slice_01.opening_complete"])
        self.assertEqual(state.scene_id, "POWER_GATE_TWELVE_SIGNAL")
        self.assertEqual(
            state.quests["QUEST_GATE_TWELVE_ECHO"]["stage"],
            "STAGE_DISCOVER",
        )

    def test_solo_route_preserves_private_destination_knowledge(self):
        data = load_slice()
        state = make_state(data)
        engine = RulesEngine(
            data["scenes"],
            quest_definitions=data["quests"],
            power_definitions=data.get("powers", {}),
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
        self.assertEqual(
            state.npcs["NPC_TAMSIN"]["story_state"]["TRACK_RELAY_CASE"],
            "PLAYER_LEFT_WITH_RELAY_SECRET",
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
            power_definitions=data.get("powers", {}),
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
        self.assertEqual(
            state.npcs["NPC_TAMSIN"]["story_state"]["TRACK_RELAY_CASE"],
            "KNOWS_GATE_TWELVE",
        )
        self.assertEqual(
            state.npcs["NPC_TAMSIN"]["goals"]["GOAL_UNDERSTAND_GATE_TWELVE"]["progress"],
            10.0,
        )

        visible = {choice["id"] for choice in engine.available_choices(state)}
        self.assertNotIn("TELL_TAMSIN_GATE_TWELVE", visible)
        self.assertNotIn("KEEP_GATE_TWELVE_SECRET", visible)
        self.assertIn("ASK_TAMSIN_TO_JOIN_KNOWN_ROUTE", visible)
        self.assertIn("LEAVE_TAMSIN_AT_DEPOT_AFTER_RECOVERY", visible)

        engine.choose(state, "ASK_TAMSIN_TO_JOIN_KNOWN_ROUTE")
        self.assertIn("NPC_TAMSIN", state.party)
        self.assertEqual(
            state.npcs["NPC_TAMSIN"]["story_state"]["TRACK_RELAY_CASE"],
            "JOINS_GATE_TWELVE",
        )
        self.assertEqual(
            state.npcs["NPC_TAMSIN"]["goals"]["GOAL_UNDERSTAND_GATE_TWELVE"]["progress"],
            25.0,
        )


    def test_first_power_requires_discovery_then_paid_practice(self):
        data = load_slice()
        state = make_state(data)
        engine = RulesEngine(
            data["scenes"],
            quest_definitions=data["quests"],
            power_definitions=data.get("powers", {}),
        )

        engine.choose(state, "TAKE_DEAD_RELAY")
        engine.choose(state, "USE_MAINTENANCE_SEAL")
        engine.choose(state, "KEEP_GATE_TWELVE_SECRET")
        engine.choose(state, "LEAVE_DEPOT_ALONE")
        engine.choose(state, "CONTINUE_BELOW_GATE_TWELVE")

        before_focus = state.player["resources"]["focus"]
        before_stamina = state.player["resources"]["stamina"]

        engine.choose(state, "FOLLOW_TRACE_ECHO")
        ability = state.abilities["ABILITY_TRACE_ECHO"]
        technique = ability["techniques"]["TECHNIQUE_SIGNAL_PULSE"]
        self.assertEqual(ability["rank"], 0)
        self.assertEqual(ability["mastery_xp"], 0.0)
        self.assertEqual(technique["mastery_xp"], 0.0)
        self.assertEqual(technique["stage"], "discovered")
        self.assertEqual(
            state.quests["QUEST_GATE_TWELVE_ECHO"]["stage"],
            "STAGE_PRACTICE",
        )

        time_before_practice = state.time_minutes
        engine.choose(state, "PRACTICE_SIGNAL_PULSE_ONE_HOUR")
        self.assertEqual(state.time_minutes, time_before_practice + 60)
        self.assertEqual(state.player["resources"]["focus"], before_focus - 6)
        self.assertEqual(state.player["resources"]["stamina"], before_stamina - 4)
        self.assertEqual(technique["mastery_xp"], 8.0)
        self.assertEqual(technique["stage"], "discovered")
        self.assertEqual(
            state.quests["QUEST_GATE_TWELVE_ECHO"]["stage"],
            "STAGE_FIRST_USE",
        )
        self.assertEqual(state.player["power_resources"]["trace_resonance"], 10)

        engine.choose(state, "USE_SIGNAL_PULSE_ON_RELAY")
        self.assertEqual(state.player["power_resources"]["trace_resonance"], 8.0)
        self.assertIn("COND_ECHO_STRAIN", state.player["conditions"])
        self.assertIn("KNOW_GATE_TWELVE_RECENT_TRACE", state.knowledge)
        self.assertEqual(technique["mastery_xp"], 10.0)
        self.assertEqual(technique["stage"], "unstable")

        engine.choose(state, "RECOVER_TRACE_RESONANCE_THIRTY_MINUTES")
        self.assertEqual(state.player["power_resources"]["trace_resonance"], 9.0)
        self.assertNotIn("COND_ECHO_STRAIN", state.player["conditions"])
        self.assertEqual(
            state.quests["QUEST_GATE_TWELVE_ECHO"]["status"],
            "completed",
        )

        engine.choose(state, "END_TRACE_ECHO_FOUNDATION_SLICE")
        self.assertTrue(state.flags["vertical_slice_01.power_session_complete"])


if __name__ == "__main__":
    unittest.main()
