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

    def test_structural_authoring_errors_are_reported_not_crashed(self):
        scenes = {
            "SCENE_BAD": {
                "choices": [
                    "not-an-object",
                    {
                        "id": "CHOICE_BAD",
                        "text": "Broken",
                        "visible_if": {"type": "flag"},
                        "requires": [123],
                        "outcomes": {
                            "default": {
                                "effects": {"type": "set_flag"}
                            }
                        },
                    },
                ]
            },
            "SCENE_NOT_OBJECT": "broken",
        }
        errors = validate_scenes(scenes)
        self.assertTrue(any("must be an object" in e for e in errors))
        self.assertTrue(any("visible_if must be a list" in e for e in errors))
        self.assertTrue(any("condition[0] must be an object" in e for e in errors))
        self.assertTrue(any("effects must be a list" in e for e in errors))

    def test_choice_time_cost_must_be_non_negative_integer(self):
        scenes = {
            "SCENE_A": {
                "choices": [
                    {
                        "id": "CHOICE_BAD_TIME",
                        "text": "Bad",
                        "time_cost_minutes": -1,
                        "outcomes": {"default": {}},
                    },
                    {
                        "id": "CHOICE_BOOL_TIME",
                        "text": "Bad bool",
                        "time_cost_minutes": True,
                        "outcomes": {"default": {}},
                    },
                ]
            }
        }
        errors = validate_scenes(scenes)
        self.assertEqual(
            sum("time_cost_minutes must be a non-negative integer" in e for e in errors),
            2,
        )

    def test_content_pack_rejects_unknown_power_reference(self):
        scenes = {
            "SCENE_A": {"choices": [{
                "id": "CHOICE_POWER",
                "text": "Discover.",
                "outcomes": {"default": {"effects": [{
                    "type": "ability_discover",
                    "ability_id": "ABILITY_MISSING",
                }]}}
            }]}
        }
        errors = validate_content_pack(scenes, {}, {})
        self.assertTrue(any("unknown power" in error for error in errors))

    def test_content_pack_rejects_unknown_technique_reference(self):
        scenes = {
            "SCENE_A": {"choices": [{
                "id": "CHOICE_POWER",
                "text": "Practice.",
                "outcomes": {"default": {"effects": [{
                    "type": "technique_practice",
                    "ability_id": "ABILITY_TRACE",
                    "technique_id": "TECHNIQUE_MISSING",
                    "minutes": 60,
                }]}}
            }]}
        }
        powers = {"ABILITY_TRACE": {"techniques": {}}}
        errors = validate_content_pack(scenes, {}, powers)
        self.assertTrue(any("unknown technique" in error for error in errors))

    def test_power_recovery_effect_contract_is_strict(self):
        scenes = {
            "SCENE_A": {"choices": [
                {
                    "id": "CHOICE_BAD_RECOVERY_TIME",
                    "text": "Recover.",
                    "outcomes": {"default": {"effects": [{
                        "type": "power_recover",
                        "ability_id": "ABILITY_TRACE",
                        "minutes": True,
                    }]}}
                },
                {
                    "id": "CHOICE_BAD_RECOVERY_QUALITY",
                    "text": "Recover badly.",
                    "outcomes": {"default": {"effects": [{
                        "type": "power_recover",
                        "ability_id": "ABILITY_TRACE",
                        "minutes": 30,
                        "quality": float("nan"),
                    }]}}
                },
            ]}
        }
        errors = validate_scenes(scenes)
        self.assertTrue(any(".minutes must be an integer >= 1" in e for e in errors))
        self.assertTrue(any(".quality must be finite non-negative numeric" in e for e in errors))

    def test_power_effect_ids_must_be_stable(self):
        scenes = {
            "SCENE_A": {"choices": [{
                "id": "CHOICE_BAD_POWER_ID",
                "text": "Bad.",
                "outcomes": {"default": {"effects": [{
                    "type": "technique_use",
                    "ability_id": "bad ability",
                    "technique_id": "bad technique",
                }]}}
            }]}
        }
        errors = validate_scenes(scenes)
        self.assertTrue(any("ability_id must be a stable uppercase ID" in e for e in errors))
        self.assertTrue(any("technique_id must be a stable uppercase ID" in e for e in errors))

if __name__ == "__main__":
    unittest.main()
