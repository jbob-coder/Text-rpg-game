import tempfile
import unittest
from pathlib import Path

from textrpg import load_content_pack, load_state, save_state


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
                "END_TRACE_ECHO_FOUNDATION_SLICE",
            ],
        )
        technique = state.abilities["ABILITY_TRACE_ECHO"]["techniques"][
            "TECHNIQUE_SIGNAL_PULSE"
        ]
        self.assertEqual(technique["mastery_xp"], 10.0)
        self.assertEqual(technique["stage"], "unstable")
        self.assertEqual(state.player["power_resources"]["trace_resonance"], 9.0)
        self.assertTrue(state.flags["vertical_slice_01.power_session_complete"])


if __name__ == "__main__":
    unittest.main()
