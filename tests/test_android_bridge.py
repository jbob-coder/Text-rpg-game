from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from textrpg.android_bridge import AndroidBridgeError, create_session


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "vertical_slice_01.json"
FORBIDDEN_AUTHORED_KEYS = {"requires", "visible_if", "outcomes", "effects"}


def walk_keys(value):
    if isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from walk_keys(item)
    elif isinstance(value, list):
        for item in value:
            yield from walk_keys(item)


class AndroidBridgeTests(unittest.TestCase):
    def test_new_session_returns_player_safe_scene_and_status(self):
        session = create_session(CONTENT)

        view = session.scene_view()

        self.assertEqual({"scene", "status", "meta"}, set(view))
        self.assertIn("id", view["scene"])
        self.assertIn("title", view["scene"])
        self.assertIn("body", view["scene"])
        self.assertIn("choices", view["scene"])
        self.assertIn("resources", view["status"])
        self.assertEqual(0, view["meta"]["turn"])
        self.assertEqual(0, view["meta"]["time_minutes"])

        leaked = FORBIDDEN_AUTHORED_KEYS.intersection(set(walk_keys(view)))
        self.assertEqual(set(), leaked)

    def test_invalid_choice_is_controlled_and_does_not_mutate_state(self):
        session = create_session(CONTENT)
        before = deepcopy(session.state.snapshot())

        with self.assertRaises(AndroidBridgeError) as caught:
            session.choose("CHOICE_DOES_NOT_EXIST")

        self.assertEqual("CHOICE_ERROR", caught.exception.code)
        self.assertEqual(before, session.state.snapshot())

    def test_choose_returns_updated_player_safe_view(self):
        session = create_session(CONTENT)
        initial = session.scene_view()
        enabled = [choice for choice in initial["scene"]["choices"] if choice["enabled"]]
        self.assertTrue(enabled)

        updated = session.choose(enabled[0]["id"])

        self.assertEqual(1, updated["meta"]["turn"])
        leaked = FORBIDDEN_AUTHORED_KEYS.intersection(set(walk_keys(updated)))
        self.assertEqual(set(), leaked)

    def test_save_and_load_round_trip(self):
        with TemporaryDirectory() as directory:
            save_path = Path(directory) / "save.json"
            session = create_session(CONTENT, save_path=save_path)
            initial = session.scene_view()
            enabled = [choice for choice in initial["scene"]["choices"] if choice["enabled"]]
            session.choose(enabled[0]["id"])
            expected = session.scene_view()
            session.save()

            restored = create_session(CONTENT, save_path=save_path)
            loaded = restored.load()

            self.assertEqual(expected, loaded)
            self.assertEqual(expected, restored.scene_view())

    def test_load_failure_does_not_replace_current_state(self):
        with TemporaryDirectory() as directory:
            save_path = Path(directory) / "save.json"
            save_path.write_text('{"schema_version":999}', encoding="utf-8")
            session = create_session(CONTENT, save_path=save_path)
            before = deepcopy(session.state.snapshot())

            with self.assertRaises(AndroidBridgeError) as caught:
                session.load()

            self.assertEqual("LOAD_ERROR", caught.exception.code)
            self.assertEqual(before, session.state.snapshot())


if __name__ == "__main__":
    unittest.main()
