import json
import unittest
from pathlib import Path

from textrpg import RuleError, assert_valid_content_pack, assert_valid_scenes, validate_content_pack, validate_scenes


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

    def test_content_pack_validates_scene_quest_stage_reference(self):
        scenes = {
            "SCENE_A": {
                "choices": [{
                    "id": "CHOICE_START",
                    "text": "Advance quest.",
                    "outcomes": {
                        "default": {
                            "effects": [{
                                "type": "quest_stage",
                                "quest_id": "QUEST_TEST",
                                "stage": "STAGE_TWO",
                            }]
                        }
                    },
                }]
            }
        }
        quests = {
            "QUEST_TEST": {
                "start_stage": "STAGE_ONE",
                "stages": {
                    "STAGE_ONE": {"objectives": {}},
                    "STAGE_TWO": {"terminal": True, "objectives": {}},
                },
            }
        }
        self.assertEqual(validate_content_pack(scenes, quests), [])
        assert_valid_content_pack(scenes, quests)

    def test_content_pack_reports_unknown_quest_stage_reference(self):
        scenes = {
            "SCENE_A": {
                "choices": [{
                    "id": "CHOICE_START",
                    "text": "Advance quest.",
                    "outcomes": {
                        "default": {
                            "effects": [{
                                "type": "quest_stage",
                                "quest_id": "QUEST_TEST",
                                "stage": "STAGE_MISSING",
                            }]
                        }
                    },
                }]
            }
        }
        quests = {
            "QUEST_TEST": {
                "start_stage": "STAGE_ONE",
                "stages": {"STAGE_ONE": {"objectives": {}}},
            }
        }
        errors = validate_content_pack(scenes, quests)
        self.assertTrue(any("unknown stage" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
