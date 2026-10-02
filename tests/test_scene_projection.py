import copy
import json
import unittest

from textrpg import GameState, RuleError, RulesEngine


class SceneProjectionTests(unittest.TestCase):
    def fixture(self):
        state = GameState(seed="scene-view", scene_id="SCENE_A",
                          player={"attributes": {"might": 10}})
        scenes = {
            "SCENE_A": {
                "title": "The entrance", "body": "A closed door.",
                "author_notes": {"future": "SECRET_AUTHOR_NOTE"},
                "choices": [
                    {
                        "id": "CHOICE_INSPECT", "text": "Inspect the door",
                        "check": {"stat": "attributes.might", "difficulty": 5},
                        "time_cost_minutes": 3,
                        "metadata": {"spoiler": "SECRET_METADATA"},
                        "outcomes": {"default": {
                            "next_scene": "SCENE_FUTURE",
                            "effects": [{"type": "set_flag", "key": "SECRET_TRIGGER", "value": True}],
                        }},
                    },
                    {
                        "id": "CHOICE_LOCKED", "text": "Lift the door",
                        "requires": [{"type": "stat_min", "path": "attributes.might", "value": 50}],
                        "disabled_reason": "You cannot lift it yet.",
                    },
                    {
                        "id": "CHOICE_SECRET", "text": "SECRET_LINE",
                        "visible_if": [{"type": "flag", "key": "SECRET_KNOWLEDGE"}],
                    },
                ],
            },
            "SCENE_FUTURE": {"choices": []},
        }
        return state, RulesEngine(scenes)

    def test_choices_allow_only_visible_fields_and_preserve_locking(self):
        state, engine = self.fixture()
        before = copy.deepcopy(state.snapshot())
        choices = engine.available_choices(state)
        self.assertEqual(choices, [
            {"id": "CHOICE_INSPECT", "text": "Inspect the door", "enabled": True},
            {"id": "CHOICE_LOCKED", "text": "Lift the door", "enabled": False,
             "disabled_reason": "You cannot lift it yet."},
        ])
        self.assertEqual(state.snapshot(), before)
        for choice_id in ("CHOICE_LOCKED", "CHOICE_SECRET"):
            with self.assertRaises(RuleError):
                engine.choose(state, choice_id)
        self.assertEqual(state.snapshot(), before)

    def test_scene_projection_is_detached_and_execution_uses_authored_rules(self):
        state, engine = self.fixture()
        before = copy.deepcopy(state.snapshot())
        authored = copy.deepcopy(engine.scenes)
        view = engine.build_scene_view(state)
        self.assertEqual(set(view), {"id", "title", "body", "choices"})
        self.assertEqual(view["id"], "SCENE_A")
        self.assertEqual(view["title"], "The entrance")
        self.assertEqual(view["body"], "A closed door.")
        self.assertNotIn("SECRET", json.dumps(view))
        self.assertNotIn("SCENE_FUTURE", json.dumps(view))
        self.assertEqual(state.snapshot(), before)
        view["choices"][0]["text"] = "changed"
        view["choices"][0]["outcomes"] = {"default": {"effects": []}}
        view["choices"].clear()
        self.assertEqual(engine.scenes, authored)
        event = engine.choose(state, "CHOICE_INSPECT")
        self.assertIsNotNone(event["check"])
        self.assertTrue(state.flags["SECRET_TRIGGER"])
        self.assertEqual(state.scene_id, "SCENE_FUTURE")
        self.assertEqual(state.time_minutes, 3)

    def test_projection_rejects_structured_data_in_visible_text_fields(self):
        for field in ("title", "body"):
            with self.subTest(scene_field=field):
                state, engine = self.fixture()
                engine.scenes["SCENE_A"][field] = {"hidden": "SECRET"}
                with self.assertRaises(RuleError):
                    engine.build_scene_view(state)
        for field, index in (("id", 0), ("text", 0), ("disabled_reason", 1)):
            with self.subTest(choice_field=field):
                state, engine = self.fixture()
                engine.scenes["SCENE_A"]["choices"][index][field] = {"hidden": "SECRET"}
                with self.assertRaises(RuleError):
                    engine.available_choices(state)


if __name__ == "__main__":
    unittest.main()
