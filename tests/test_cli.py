import unittest
from pathlib import Path

from textrpg import load_content_pack
from textrpg.cli import apply_choice_number, render_scene, render_state_summary


ROOT = Path(__file__).resolve().parents[1]
SLICE = ROOT / "content" / "vertical_slice_01.json"


class CliTests(unittest.TestCase):
    def test_render_scene_shows_title_and_numbered_choice(self):
        pack = load_content_pack(SLICE)
        output = render_scene(pack.engine, pack.state)
        self.assertIn("The Last Light in Platform Nine", output)
        self.assertIn("1. Take responsibility for the relay case.", output)

    def test_apply_choice_number_advances_scene(self):
        pack = load_content_pack(SLICE)
        event = apply_choice_number(pack.engine, pack.state, 1)
        self.assertEqual(event["choice"], "TAKE_DEAD_RELAY")
        self.assertEqual(pack.state.scene_id, "OPENING_RELAY_CASING")

    def test_state_summary_reports_party_and_quest(self):
        pack = load_content_pack(SLICE)
        apply_choice_number(pack.engine, pack.state, 1)
        output = render_state_summary(pack.state)
        self.assertIn("Party: solo", output)
        self.assertIn("QUEST_DEAD_RELAY", output)
        self.assertIn("STAGE_RELAY", output)


if __name__ == "__main__":
    unittest.main()
