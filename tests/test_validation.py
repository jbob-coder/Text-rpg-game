import json
import unittest
from pathlib import Path

from textrpg import RuleError, assert_valid_scenes, validate_scenes


ROOT = Path(__file__).resolve().parents[1]


class ValidationTests(unittest.TestCase):
    def test_sample_content_is_valid(self):
        scenes = json.loads((ROOT / "content" / "sample_scene.json").read_text(encoding="utf-8"))["scenes"]
        self.assertEqual(validate_scenes(scenes), [])

    def test_duplicate_choice_and_missing_scene_are_reported(self):
        scenes = {
            "SCENE_A": {"choices": [
                {"id": "CHOICE_X", "text": "A", "outcomes": {"default": {"next_scene": "SCENE_MISSING"}}},
                {"id": "CHOICE_X", "text": "B", "outcomes": {"default": {}}},
            ]}
        }
        errors = validate_scenes(scenes)
        self.assertTrue(any("Duplicate choice id" in e for e in errors))
        self.assertTrue(any("unknown scene" in e for e in errors))

    def test_assert_valid_raises(self):
        with self.assertRaises(RuleError):
            assert_valid_scenes({"bad-id": {"choices": []}})

    def test_invalid_stat_and_perk_modifier_paths_are_reported(self):
        scenes = {
            "SCENE_A": {
                "choices": [
                    {
                        "id": "CHOICE_A",
                        "text": "Try it",
                        "requires": [
                            {"type": "stat_min", "path": "attributes.migth", "value": 10}
                        ],
                        "outcomes": {
                            "default": {
                                "effects": [
                                    {
                                        "type": "add_perk",
                                        "perk_id": "PERK_BAD",
                                        "modifiers": {"derived.max_heath": 5},
                                    }
                                ]
                            }
                        },
                    }
                ]
            }
        }
        errors = validate_scenes(scenes)
        self.assertTrue(any("invalid stat path" in e for e in errors))
        self.assertTrue(any("invalid modifiers" in e for e in errors))

    def test_check_skill_must_use_skill_namespace(self):
        scenes = {
            "SCENE_A": {
                "choices": [
                    {
                        "id": "CHOICE_A",
                        "text": "Try it",
                        "check": {
                            "stat": "attributes.might",
                            "skill": "attributes.agility",
                        },
                        "outcomes": {"default": {}},
                    }
                ]
            }
        }
        errors = validate_scenes(scenes)
        self.assertTrue(any("skill must use skills.<id>" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
