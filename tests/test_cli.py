import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from textrpg import load_content_pack
from textrpg.cli import apply_choice_number, main, play, render_scene, render_state_summary


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


    def test_eof_exits_cleanly_without_advancing_game(self):
        pack = load_content_pack(SLICE)
        before = pack.state.snapshot()
        output = []

        def no_input(_prompt):
            raise EOFError()

        result = play(pack, input_fn=no_input, output_fn=output.append)
        self.assertIs(result, pack.state)
        self.assertEqual(before, pack.state.snapshot())
        self.assertTrue(any("Input closed" in line for line in output))

    def test_keyboard_interrupt_exits_cleanly(self):
        pack = load_content_pack(SLICE)
        before = pack.state.snapshot()
        output = []

        def interrupted(_prompt):
            raise KeyboardInterrupt()

        result = play(pack, input_fn=interrupted, output_fn=output.append)
        self.assertEqual(result.snapshot(), before)
        self.assertTrue(any("Input closed" in line for line in output))

    def test_manual_save_error_is_reported_and_loop_continues(self):
        pack = load_content_pack(SLICE)
        responses = iter(["save", "quit"])
        output = []
        with patch("textrpg.cli.save_state", side_effect=OSError("disk full")) as save:
            play(
                pack,
                save_path=Path("unwritable.json"),
                input_fn=lambda _: next(responses),
                output_fn=output.append,
            )
        self.assertEqual(save.call_count, 1)
        self.assertTrue(any("Save failed: disk full" in line for line in output))
        self.assertFalse(any("Saved:" in line for line in output))

    def test_autosave_error_reports_unsaved_progress_without_undoing_choice(self):
        pack = load_content_pack(SLICE)
        responses = iter(["1", "quit"])
        output = []
        with patch("textrpg.cli.save_state", side_effect=OSError("disk full")) as save:
            state = play(
                pack,
                save_path=Path("unwritable.json"),
                input_fn=lambda _: next(responses),
                output_fn=output.append,
            )
        self.assertEqual(save.call_count, 1)
        self.assertEqual(state.scene_id, "OPENING_RELAY_CASING")
        self.assertTrue(any("Autosave failed: disk full" in line for line in output))
        self.assertTrue(any("Progress is only in memory" in line for line in output))
        self.assertFalse(any("Invalid action" in line for line in output))

    def test_missing_resume_file_has_clean_cli_error(self):
        with TemporaryDirectory() as folder:
            nonexistent_save = Path(folder) / "missing.json"
            stdout = StringIO()
            with redirect_stdout(stdout):
                status = main([str(SLICE), "--load-save", str(nonexistent_save)])
        self.assertEqual(status, 2)
        self.assertIn("Cannot start game: Could not load save:", stdout.getvalue())
        self.assertIn("missing.json", stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
