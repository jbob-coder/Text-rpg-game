import tempfile
import unittest
from pathlib import Path
from unittest import mock

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


    def test_closed_input_exits_gracefully_without_changing_state(self):
        for exception in (EOFError, KeyboardInterrupt):
            with self.subTest(exception=exception.__name__):
                pack = load_content_pack(SLICE)
                before = pack.state.snapshot()
                messages = []

                def closed_input(_prompt):
                    raise exception()

                returned = play(pack, input_fn=closed_input, output_fn=messages.append)
                self.assertIs(returned, pack.state)
                self.assertEqual(returned.snapshot(), before)
                self.assertIn("Input closed; exiting.", messages)

    def test_cli_missing_load_save_reports_error_and_exit_code(self):
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "missing-save.json"
            with mock.patch("builtins.print") as printer:
                code = main([str(SLICE), "--load-save", str(missing)])
        self.assertEqual(code, 2)
        self.assertIn("Could not read save file", printer.call_args.args[0])

    def test_cli_invalid_utf8_load_save_reports_error_and_exit_code(self):
        with tempfile.TemporaryDirectory() as directory:
            corrupted = Path(directory) / "invalid-encoding.json"
            corrupted.write_bytes(bytes([0xFF]))
            with mock.patch("builtins.print") as printer:
                code = main([str(SLICE), "--load-save", str(corrupted)])
        self.assertEqual(code, 2)
        self.assertIn("Could not read save file", printer.call_args.args[0])

    def test_manual_save_failure_is_reported_without_crashing(self):
        pack = load_content_pack(SLICE)
        before = pack.state.snapshot()
        commands = iter(["save", "quit"])
        output = []
        with mock.patch(
            "textrpg.cli.save_state", side_effect=PermissionError("disk is read-only")
        ):
            returned = play(
                pack,
                save_path="ignored.json",
                input_fn=lambda _prompt: next(commands),
                output_fn=output.append,
            )
        self.assertIs(returned, pack.state)
        self.assertEqual(returned.snapshot(), before)
        self.assertIn("Save failed: disk is read-only", output)
        self.assertFalse(any(message.startswith("Saved:") for message in output))

    def test_auto_save_failure_does_not_misreport_player_choice(self):
        pack = load_content_pack(SLICE)
        commands = iter(["1", "quit"])
        output = []
        with mock.patch(
            "textrpg.cli.save_state", side_effect=PermissionError("disk is read-only")
        ):
            returned = play(
                pack,
                save_path="ignored.json",
                input_fn=lambda _prompt: next(commands),
                output_fn=output.append,
            )
        self.assertEqual(returned.turn, 1)
        self.assertEqual(returned.scene_id, "OPENING_RELAY_CASING")
        self.assertIn(
            "Auto-save failed: disk is read-only; progress remains in memory.",
            output,
        )
        self.assertFalse(any(message.startswith("Invalid action:") for message in output))

if __name__ == "__main__":
    unittest.main()
