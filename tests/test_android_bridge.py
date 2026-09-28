import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BRIDGE_PATH = ROOT / "android" / "app" / "src" / "main" / "python" / "android_bridge.py"
CONTENT_PATH = ROOT / "content" / "vertical_slice_01.json"


def load_bridge_module():
    spec = importlib.util.spec_from_file_location("android_bridge_under_test", BRIDGE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load Android bridge module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_content_json():
    return CONTENT_PATH.read_text(encoding="utf-8")


class AndroidBridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bridge = load_bridge_module()
        cls.content_json = load_content_json()

    def test_initial_view_uses_player_safe_scene_projection(self):
        session = self.bridge.create_session(self.content_json)
        view = json.loads(session.view_json())

        self.assertEqual(view["game"]["content_id"], "CONTENT_VERTICAL_SLICE_01")
        self.assertEqual(view["scene"]["id"], "OPENING_DEPOT_BLACKOUT")
        self.assertEqual(view["turn"], 0)
        self.assertEqual(view["time_minutes"], 0)

        choices = view["scene"]["choices"]
        self.assertEqual(len(choices), 1)
        self.assertEqual(choices[0]["id"], "TAKE_DEAD_RELAY")
        self.assertEqual(
            set(choices[0]),
            {"id", "text", "enabled"},
        )

        encoded = json.dumps(view["scene"], sort_keys=True)
        self.assertNotIn("outcomes", encoded)
        self.assertNotIn("effects", encoded)
        self.assertNotIn("next_scene", encoded)
        self.assertNotIn("requires", encoded)
        self.assertNotIn("visible_if", encoded)

    def test_choice_executes_engine_and_returns_schema_one_save(self):
        session = self.bridge.create_session(self.content_json)
        result = json.loads(session.choose_json("TAKE_DEAD_RELAY"))

        self.assertEqual(result["view"]["scene"]["id"], "OPENING_RELAY_CASING")
        self.assertEqual(result["view"]["turn"], 1)
        self.assertEqual(result["view"]["time_minutes"], 2)

        save = json.loads(result["save"])
        self.assertEqual(save["schema_version"], 1)
        self.assertEqual(save["scene_id"], "OPENING_RELAY_CASING")
        self.assertEqual(save["turn"], 1)
        self.assertEqual(save["time_minutes"], 2)
        self.assertEqual(save["inventory"]["ITEM_DEAD_RELAY"], 1)
        self.assertIn("QUEST_DEAD_RELAY", save["quests"])

    def test_save_resume_restores_authoritative_state(self):
        first = self.bridge.create_session(self.content_json)
        result = json.loads(first.choose_json("TAKE_DEAD_RELAY"))

        resumed = self.bridge.create_session(self.content_json, result["save"])
        resumed_view = json.loads(resumed.view_json())

        self.assertEqual(resumed_view["scene"]["id"], "OPENING_RELAY_CASING")
        self.assertEqual(resumed_view["turn"], 1)
        self.assertEqual(resumed_view["time_minutes"], 2)

        resumed_save = json.loads(resumed.save_json())
        self.assertEqual(resumed_save["inventory"]["ITEM_DEAD_RELAY"], 1)
        self.assertIn("QUEST_DEAD_RELAY", resumed_save["quests"])

    def test_invalid_choice_does_not_mutate_bridge_session(self):
        session = self.bridge.create_session(self.content_json)
        before = session.save_json()

        with self.assertRaises(self.bridge.RuleError):
            session.choose_json("NOT_A_REAL_CHOICE")

        self.assertEqual(session.save_json(), before)
        view = json.loads(session.view_json())
        self.assertEqual(view["scene"]["id"], "OPENING_DEPOT_BLACKOUT")
        self.assertEqual(view["turn"], 0)

    def test_unsupported_save_schema_is_rejected(self):
        session = self.bridge.create_session(self.content_json)
        save = json.loads(session.save_json())
        save["schema_version"] = 999

        with self.assertRaises(self.bridge.RuleError):
            self.bridge.create_session(
                self.content_json,
                json.dumps(save),
            )


if __name__ == "__main__":
    unittest.main()
