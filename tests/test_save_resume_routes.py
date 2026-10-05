import tempfile
import unittest
from pathlib import Path

from textrpg import build_status_view, load_content_pack, load_state, save_state


ROOT = Path(__file__).resolve().parents[1]
SLICE = ROOT / "content" / "vertical_slice_01.json"


class SaveResumeRouteTests(unittest.TestCase):
    def run_round_trip(self, before_save, after_load):
        pack = load_content_pack(SLICE)
        for choice_id in before_save:
            pack.engine.choose(pack.state, choice_id)

        with tempfile.TemporaryDirectory() as temp_dir:
            save_path = Path(temp_dir) / "save.json"
            save_state(save_path, pack.state)
            loaded = load_state(save_path)

        self.assertEqual(loaded.snapshot(), pack.state.snapshot())
        pack.state = loaded

        for choice_id in after_load:
            pack.engine.choose(pack.state, choice_id)

        return pack.state

    def test_cooperative_route_survives_save_resume(self):
        state = self.run_round_trip(
            [
                "TAKE_DEAD_RELAY",
                "USE_MAINTENANCE_SEAL",
                "TELL_TAMSIN_GATE_TWELVE",
            ],
            [
                "ENTER_GATE_TWELVE_WITH_TAMSIN",
                "CONTINUE_BELOW_GATE_TWELVE",
            ],
        )
        self.assertEqual(state.flags["opening.route"], "tunnel_with_tamsin")
        self.assertIn("NPC_TAMSIN", state.party)
        self.assertEqual(state.scene_id, "POWER_GATE_TWELVE_SIGNAL")

    def test_solo_route_survives_save_resume(self):
        state = self.run_round_trip(
            [
                "TAKE_DEAD_RELAY",
                "USE_MAINTENANCE_SEAL",
                "KEEP_GATE_TWELVE_SECRET",
            ],
            [
                "LEAVE_DEPOT_ALONE",
                "CONTINUE_BELOW_GATE_TWELVE",
            ],
        )
        self.assertEqual(state.flags["opening.route"], "solo")
        self.assertEqual(state.party, [])
        self.assertEqual(state.scene_id, "POWER_GATE_TWELVE_SIGNAL")

    def test_failure_recovery_route_survives_save_resume(self):
        state = self.run_round_trip(
            [
                "TAKE_DEAD_RELAY",
                "FORCE_RELAY_CASING",
                "ASK_TAMSIN_FOR_RECOVERY_HELP",
            ],
            [
                "ASK_TAMSIN_TO_JOIN_KNOWN_ROUTE",
                "ENTER_GATE_TWELVE_WITH_TAMSIN",
                "CONTINUE_BELOW_GATE_TWELVE",
            ],
        )
        self.assertIn("NPC_TAMSIN", state.party)
        self.assertEqual(
            state.npcs["NPC_TAMSIN"]["story_state"]["TRACK_RELAY_CASE"],
            "ENTERED_GATE_TWELVE",
        )
        self.assertEqual(state.scene_id, "POWER_GATE_TWELVE_SIGNAL")

    def test_first_power_practice_is_deterministic_across_save_boundary(self):
        prefix = [
            "TAKE_DEAD_RELAY",
            "USE_MAINTENANCE_SEAL",
            "KEEP_GATE_TWELVE_SECRET",
            "LEAVE_DEPOT_ALONE",
            "CONTINUE_BELOW_GATE_TWELVE",
            "FOLLOW_TRACE_ECHO",
        ]

        uninterrupted = load_content_pack(SLICE)
        for choice_id in prefix:
            uninterrupted.engine.choose(uninterrupted.state, choice_id)
        uninterrupted.engine.choose(
            uninterrupted.state,
            "PRACTICE_SIGNAL_PULSE_ONE_HOUR",
        )

        resumed = load_content_pack(SLICE)
        for choice_id in prefix:
            resumed.engine.choose(resumed.state, choice_id)
        with tempfile.TemporaryDirectory() as temp_dir:
            save_path = Path(temp_dir) / "progression.json"
            save_state(save_path, resumed.state)
            resumed.state = load_state(save_path)
        resumed.engine.choose(
            resumed.state,
            "PRACTICE_SIGNAL_PULSE_ONE_HOUR",
        )

        def progression_fingerprint(pack):
            ability = pack.state.abilities["ABILITY_TRACE_ECHO"]
            technique = ability["techniques"]["TECHNIQUE_SIGNAL_PULSE"]
            status = build_status_view(
                pack.state,
                pack.engine,
                ability_definitions=pack.raw.get("powers", {}),
                condition_definitions=pack.registries.get("conditions", {}),
            )
            ability_view = next(
                item
                for item in status["abilities"]
                if item["id"] == "ABILITY_TRACE_ECHO"
            )
            return {
                "ability_mastery_xp": ability["mastery_xp"],
                "ability_mastery_stage": ability["mastery_stage"],
                "technique_mastery_xp": technique["mastery_xp"],
                "technique_stage": technique["stage"],
                "stamina": pack.state.player["resources"]["stamina"],
                "focus": pack.state.player["resources"]["focus"],
                "time_minutes": pack.state.time_minutes,
                "quest_stage": pack.state.quests["QUEST_GATE_TWELVE_ECHO"]["stage"],
                "ability_view": ability_view,
            }

        expected = progression_fingerprint(uninterrupted)
        actual = progression_fingerprint(resumed)

        self.assertEqual(expected, actual)
        self.assertEqual(actual["technique_mastery_xp"], 8.0)
        self.assertEqual(actual["quest_stage"], "STAGE_FIRST_USE")
        self.assertEqual(actual["ability_view"]["id"], "ABILITY_TRACE_ECHO")
        self.assertEqual(
            [item["technique_id"] for item in actual["ability_view"]["techniques"]],
            ["TECHNIQUE_SIGNAL_PULSE"],
        )
        projected = repr(actual["ability_view"])
        self.assertNotIn("discovery_requirements", projected)
        self.assertNotIn("requirements", projected)
        self.assertNotIn("effects", projected)

    def test_first_power_practice_survives_save_resume(self):
        state = self.run_round_trip(
            [
                "TAKE_DEAD_RELAY",
                "USE_MAINTENANCE_SEAL",
                "KEEP_GATE_TWELVE_SECRET",
                "LEAVE_DEPOT_ALONE",
                "CONTINUE_BELOW_GATE_TWELVE",
                "FOLLOW_TRACE_ECHO",
            ],
            [
                "PRACTICE_SIGNAL_PULSE_ONE_HOUR",
                "USE_SIGNAL_PULSE_ON_RELAY",
                "RECOVER_TRACE_RESONANCE_THIRTY_MINUTES",
                "BEGIN_TRACE_STABILIZATION_PLAN",
            ],
        )
        technique = state.abilities["ABILITY_TRACE_ECHO"]["techniques"][
            "TECHNIQUE_SIGNAL_PULSE"
        ]
        self.assertEqual(technique["mastery_xp"], 10.0)
        self.assertEqual(technique["stage"], "unstable")
        self.assertEqual(state.player["power_resources"]["trace_resonance"], 9.0)
        self.assertTrue(state.flags["vertical_slice_01.power_session_complete"])
        self.assertEqual(state.scene_id, "TRACE_STABILIZATION_HUB")
        self.assertEqual(
            state.quests["QUEST_TRACE_STABILIZATION"]["status"],
            "active",
        )


    def test_directional_trace_unlock_survives_save_resume(self):
        state = self.run_round_trip(
            [
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
                "PRACTICE_SIGNAL_PULSE_TWO_HOURS",
                "PRACTICE_SIGNAL_PULSE_TWO_HOURS",
                "PRACTICE_SIGNAL_PULSE_TWO_HOURS",
                "PRACTICE_SIGNAL_PULSE_TWO_HOURS",
                "RECOVER_EIGHT_HOURS",
                "TRAIN_POWER_FUNDAMENTALS_TWO_HOURS",
                "TRAIN_POWER_FUNDAMENTALS_TWO_HOURS",
                "TRAIN_POWER_FUNDAMENTALS_TWO_HOURS",
                "TRAIN_POWER_FUNDAMENTALS_TWO_HOURS",
                "TRAIN_POWER_FUNDAMENTALS_TWO_HOURS",
                "TRAIN_POWER_FUNDAMENTALS_TWO_HOURS",
                "ANALYZE_STABLE_TRACE_PATTERN",
                "COMPLETE_TRACE_TOLERANCE_PROTOCOL",
            ],
            [
                "DISCOVER_DIRECTIONAL_TRACE",
                "TRY_DIRECTIONAL_TRACE_ON_SERVICE_FORK",
                "RECOVER_DIRECTIONAL_TRACE_ONE_HOUR",
                "END_DIRECTIONAL_TRACE_PROTOTYPE",
            ],
        )
        directional = state.abilities["ABILITY_TRACE_ECHO"]["techniques"][
            "TECHNIQUE_DIRECTIONAL_TRACE"
        ]
        self.assertEqual(directional["mastery_xp"], 3.0)
        self.assertIn(
            "KNOW_DIRECTIONAL_TRACE_POINTS_DEEPER",
            state.knowledge,
        )
        self.assertNotIn("COND_ECHO_STRAIN", state.player["conditions"])
        self.assertEqual(
            state.quests["QUEST_TRACE_STABILIZATION"]["status"],
            "completed",
        )
        self.assertTrue(
            state.flags["vertical_slice_01.directional_trace_discovered"]
        )
        self.assertTrue(
            state.flags["vertical_slice_01.directional_trace_first_use_complete"]
        )


if __name__ == "__main__":
    unittest.main()
