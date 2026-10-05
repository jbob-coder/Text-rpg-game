import json
import unittest
from pathlib import Path

from textrpg import (
    GameState,
    RulesEngine,
    build_status_view,
    dumps_state,
    loads_state,
    npc_remembers,
    technique_discovery_status,
    validate_character_visuals,
    validate_content_pack,
)


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
            validate_content_pack(
                data["scenes"],
                data["quests"],
                data.get("powers", {}),
                data.get("registries"),
            ),
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
        self.assertTrue(
            npc_remembers(
                state,
                "NPC_TAMSIN",
                "MEM_TAMSIN_PLAYER_SHARED_GATE_TWELVE",
            )
        )
        tunnel_choices = {choice["id"] for choice in engine.available_choices(state)}
        self.assertIn("ENTER_GATE_TWELVE_WITH_TAMSIN", tunnel_choices)
        self.assertNotIn(
            "ENTER_GATE_TWELVE_WITH_TAMSIN_AFTER_RECOVERY",
            tunnel_choices,
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
        self.assertFalse(
            npc_remembers(
                state,
                "NPC_TAMSIN",
                "MEM_TAMSIN_PLAYER_SHARED_GATE_TWELVE",
            )
        )
        tunnel_choices = {choice["id"] for choice in engine.available_choices(state)}
        self.assertNotIn("ENTER_GATE_TWELVE_WITH_TAMSIN", tunnel_choices)
        self.assertIn(
            "ENTER_GATE_TWELVE_WITH_TAMSIN_AFTER_RECOVERY",
            tunnel_choices,
        )


    def test_tamsin_memory_persists_and_changes_later_authored_choice(self):
        data = load_slice()
        engine = RulesEngine(
            data["scenes"],
            quest_definitions=data["quests"],
            power_definitions=data.get("powers", {}),
        )
        state = make_state(data)

        for choice_id in [
            "TAKE_DEAD_RELAY",
            "USE_MAINTENANCE_SEAL",
            "TELL_TAMSIN_GATE_TWELVE",
        ]:
            engine.choose(state, choice_id)

        memories = state.npcs["NPC_TAMSIN"]["memories"]
        self.assertEqual(
            ["MEM_TAMSIN_PLAYER_SHARED_GATE_TWELVE"],
            [memory["memory_id"] for memory in memories],
        )

        resumed = loads_state(dumps_state(state))
        self.assertTrue(
            npc_remembers(
                resumed,
                "NPC_TAMSIN",
                "MEM_TAMSIN_PLAYER_SHARED_GATE_TWELVE",
                tags=["trust"],
            )
        )
        visible = {
            choice["id"]: choice["text"]
            for choice in engine.available_choices(resumed)
        }
        self.assertIn("ENTER_GATE_TWELVE_WITH_TAMSIN", visible)
        self.assertNotIn("ENTER_GATE_TWELVE_WITH_TAMSIN_AFTER_RECOVERY", visible)
        self.assertIn("earlier trust", visible["ENTER_GATE_TWELVE_WITH_TAMSIN"])

        engine.choose(resumed, "ENTER_GATE_TWELVE_WITH_TAMSIN")
        self.assertEqual(
            "ENTERED_GATE_TWELVE",
            resumed.npcs["NPC_TAMSIN"]["story_state"]["TRACK_RELAY_CASE"],
        )
        self.assertEqual(
            1,
            sum(
                memory["memory_id"] == "MEM_TAMSIN_PLAYER_SHARED_GATE_TWELVE"
                for memory in resumed.npcs["NPC_TAMSIN"]["memories"]
            ),
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

        directional = data["powers"]["ABILITY_TRACE_ECHO"]["techniques"][
            "TECHNIQUE_DIRECTIONAL_TRACE"
        ]
        discovery = technique_discovery_status(
            state,
            "ABILITY_TRACE_ECHO",
            "TECHNIQUE_DIRECTIONAL_TRACE",
            directional,
        )
        self.assertFalse(discovery["available"])
        self.assertNotIn(
            "TECHNIQUE_DIRECTIONAL_TRACE",
            state.abilities["ABILITY_TRACE_ECHO"]["techniques"],
        )
        self.assertNotIn("rank", discovery["reasons"])
        self.assertIn("mastery_xp", discovery["reasons"])
        self.assertIn(
            "knowledge:KNOW_TRACE_ECHO_PATTERN_STABLE", discovery["reasons"]
        )
        self.assertIn("perk:PERK_TRACE_TOLERANCE", discovery["reasons"])
        self.assertIn(
            "technique:TECHNIQUE_SIGNAL_PULSE:learned", discovery["reasons"]
        )

        engine.choose(state, "BEGIN_TRACE_STABILIZATION_PLAN")
        self.assertTrue(state.flags["vertical_slice_01.power_session_complete"])
        self.assertEqual(state.scene_id, "TRACE_STABILIZATION_HUB")
        self.assertEqual(
            state.quests["QUEST_TRACE_STABILIZATION"]["stage"],
            "STAGE_FOUNDATION",
        )


    def test_trace_echo_progression_is_deterministic_across_save_resume(self):
        data = load_slice()

        def engine_for_slice():
            return RulesEngine(
                data["scenes"],
                quest_definitions=data["quests"],
                power_definitions=data.get("powers", {}),
            )

        state = make_state(data)
        engine = engine_for_slice()
        for choice_id in [
            "TAKE_DEAD_RELAY",
            "USE_MAINTENANCE_SEAL",
            "KEEP_GATE_TWELVE_SECRET",
            "LEAVE_DEPOT_ALONE",
            "CONTINUE_BELOW_GATE_TWELVE",
            "FOLLOW_TRACE_ECHO",
        ]:
            engine.choose(state, choice_id)

        discovered_snapshot = dumps_state(state)

        uninterrupted = loads_state(discovered_snapshot)
        uninterrupted_engine = engine_for_slice()
        uninterrupted_engine.choose(uninterrupted, "PRACTICE_SIGNAL_PULSE_ONE_HOUR")

        resumed = loads_state(discovered_snapshot)
        resumed = loads_state(dumps_state(resumed))
        resumed_engine = engine_for_slice()
        resumed_engine.choose(resumed, "PRACTICE_SIGNAL_PULSE_ONE_HOUR")
        resumed_after_save = loads_state(dumps_state(resumed))

        def progression_fingerprint(candidate):
            ability = candidate.abilities["ABILITY_TRACE_ECHO"]
            technique = ability["techniques"]["TECHNIQUE_SIGNAL_PULSE"]
            return {
                "ability_mastery_xp": ability["mastery_xp"],
                "ability_mastery_stage": ability["mastery_stage"],
                "technique_mastery_xp": technique["mastery_xp"],
                "technique_stage": technique["stage"],
                "stamina": candidate.player["resources"]["stamina"],
                "focus": candidate.player["resources"]["focus"],
                "trace_resonance": candidate.player["power_resources"]["trace_resonance"],
                "time_minutes": candidate.time_minutes,
                "quest_stage": candidate.quests["QUEST_GATE_TWELVE_ECHO"]["stage"],
            }

        expected = progression_fingerprint(uninterrupted)
        self.assertEqual(expected, progression_fingerprint(resumed))
        self.assertEqual(expected, progression_fingerprint(resumed_after_save))
        self.assertEqual(8.0, expected["technique_mastery_xp"])
        self.assertGreater(expected["ability_mastery_xp"], 0.0)

        view = build_status_view(
            resumed_after_save,
            engine_for_slice(),
            ability_definitions=data["powers"],
        )
        ability_view = next(
            item for item in view["abilities"]
            if item["id"] == "ABILITY_TRACE_ECHO"
        )
        technique_view = next(
            item for item in ability_view["techniques"]
            if item["technique_id"] == "TECHNIQUE_SIGNAL_PULSE"
        )
        self.assertEqual(expected["ability_mastery_xp"], ability_view["mastery_xp"])
        self.assertEqual(expected["technique_mastery_xp"], technique_view["mastery_xp"])
        self.assertNotIn("requirements", repr(ability_view))
        self.assertNotIn("discovery_requirements", repr(ability_view))

        practice_events = [
            event for event in resumed_after_save.history
            if event.get("type") == "technique_practice"
            and event.get("ability_id") == "ABILITY_TRACE_ECHO"
            and event.get("technique_id") == "TECHNIQUE_SIGNAL_PULSE"
        ]
        self.assertEqual(1, len(practice_events))
        self.assertEqual(60, practice_events[0]["minutes"])

    def test_directional_trace_is_earned_through_training_research_and_tolerance(self):
        data = load_slice()
        state = make_state(data)
        engine = RulesEngine(
            data["scenes"],
            quest_definitions=data["quests"],
            power_definitions=data.get("powers", {}),
        )

        for choice_id in [
            "TAKE_DEAD_RELAY",
            "USE_MAINTENANCE_SEAL",
            "KEEP_GATE_TWELVE_SECRET",
            "LEAVE_DEPOT_ALONE",
            "CONTINUE_BELOW_GATE_TWELVE",
            "FOLLOW_TRACE_ECHO",
            "PRACTICE_SIGNAL_PULSE_ONE_HOUR",
            "USE_SIGNAL_PULSE_ON_RELAY",
            "RECOVER_TRACE_RESONANCE_THIRTY_MINUTES",
            "BEGIN_TRACE_STABILIZATION_PLAN",
        ]:
            engine.choose(state, choice_id)

        for _ in range(4):
            engine.choose(state, "PRACTICE_SIGNAL_PULSE_TWO_HOURS")

        signal = state.abilities["ABILITY_TRACE_ECHO"]["techniques"][
            "TECHNIQUE_SIGNAL_PULSE"
        ]
        self.assertGreaterEqual(signal["mastery_xp"], 40)
        self.assertIn(signal["stage"], {"learned", "practiced", "mastered"})
        self.assertGreaterEqual(
            state.abilities["ABILITY_TRACE_ECHO"]["mastery_xp"],
            20,
        )

        engine.choose(state, "RECOVER_EIGHT_HOURS")
        for _ in range(6):
            engine.choose(state, "TRAIN_POWER_FUNDAMENTALS_TWO_HOURS")
        self.assertGreaterEqual(state.player["skills"]["powers"], 10)

        engine.choose(state, "ANALYZE_STABLE_TRACE_PATTERN")
        self.assertIn("KNOW_TRACE_ECHO_PATTERN_STABLE", state.knowledge)
        self.assertEqual(
            state.quests["QUEST_TRACE_STABILIZATION"]["stage"],
            "STAGE_FOUNDATION",
        )

        engine.choose(state, "COMPLETE_TRACE_TOLERANCE_PROTOCOL")
        self.assertIn("PERK_TRACE_TOLERANCE", state.perks)
        self.assertEqual(
            state.quests["QUEST_TRACE_STABILIZATION"]["stage"],
            "STAGE_DIRECTIONAL",
        )

        choices = {
            choice["id"]: choice
            for choice in engine.available_choices(state)
        }
        self.assertTrue(choices["DISCOVER_DIRECTIONAL_TRACE"]["enabled"])

        engine.choose(state, "DISCOVER_DIRECTIONAL_TRACE")
        directional = state.abilities["ABILITY_TRACE_ECHO"]["techniques"][
            "TECHNIQUE_DIRECTIONAL_TRACE"
        ]
        self.assertEqual(directional["mastery_xp"], 0.0)
        self.assertEqual(directional["stage"], "discovered")
        self.assertEqual(
            state.quests["QUEST_TRACE_STABILIZATION"]["status"],
            "completed",
        )

        resonance_before = state.player["power_resources"]["trace_resonance"]
        engine.choose(state, "TRY_DIRECTIONAL_TRACE_ON_SERVICE_FORK")
        self.assertEqual(
            state.player["power_resources"]["trace_resonance"],
            resonance_before - 4,
        )
        self.assertEqual(directional["mastery_xp"], 3.0)
        self.assertEqual(directional["stage"], "discovered")
        self.assertIn("COND_ECHO_STRAIN", state.player["conditions"])
        self.assertEqual(
            state.player["conditions"]["COND_ECHO_STRAIN"]["severity"],
            2,
        )
        self.assertIn(
            "KNOW_DIRECTIONAL_TRACE_POINTS_DEEPER",
            state.knowledge,
        )

        engine.choose(state, "RECOVER_DIRECTIONAL_TRACE_ONE_HOUR")
        self.assertEqual(
            state.player["power_resources"]["trace_resonance"],
            resonance_before - 2,
        )
        self.assertNotIn("COND_ECHO_STRAIN", state.player["conditions"])

        engine.choose(state, "END_DIRECTIONAL_TRACE_PROTOTYPE")
        self.assertTrue(
            state.flags["vertical_slice_01.directional_trace_discovered"]
        )
        self.assertTrue(
            state.flags["vertical_slice_01.directional_trace_first_use_complete"]
        )


if __name__ == "__main__":
    unittest.main()
