"""Regression tests for malformed authored content discriminator types."""

import unittest

from textrpg import (
    RuleError,
    assert_valid_scenes,
    validate_content_pack,
    validate_scenes,
)


class InvalidContentDiscriminatorTests(unittest.TestCase):
    @staticmethod
    def scene(*, condition=None, effect=None):
        choice = {
            "id": "CHOICE_TEST",
            "text": "Continue",
            "outcomes": {"default": {"effects": [] if effect is None else [effect]}},
        }
        if condition is not None:
            choice["requires"] = [condition]
        return {"SCENE_TEST": {"choices": [choice]}}

    def test_unhashable_condition_types_return_errors(self):
        for kind in ([], {}, ["flag"], {"type": "flag"}):
            with self.subTest(kind=kind):
                scenes = self.scene(condition={"type": kind})
                errors = validate_scenes(scenes)
                self.assertTrue(any("unsupported type" in error for error in errors))
                with self.assertRaises(RuleError):
                    assert_valid_scenes(scenes)

    def test_unhashable_effect_types_return_errors_in_full_pack_validation(self):
        for kind in ([], {}, ["inventory"], {"type": "inventory"}):
            with self.subTest(kind=kind):
                scenes = self.scene(effect={"type": kind})
                self.assertTrue(
                    any("unsupported type" in error for error in validate_scenes(scenes))
                )
                # Follow-on registry/quest/power cross-reference passes must not
                # crash after the scene validator has reported the invalid type.
                errors = validate_content_pack(scenes, registries={"knowledge": {}})
                self.assertTrue(any("unsupported type" in error for error in errors))

    def test_unhashable_technique_stage_is_reported_as_invalid_value(self):
        for stage in ([], {}, ["learned"]):
            with self.subTest(stage=stage):
                scenes = self.scene(
                    condition={
                        "type": "technique_stage_min",
                        "ability_id": "ABILITY_TEST",
                        "technique_id": "TECH_TEST",
                        "stage": stage,
                    }
                )
                errors = validate_scenes(scenes)
                self.assertTrue(any(".stage has unsupported value" in e for e in errors))

    def test_valid_discriminators_still_work(self):
        scenes = self.scene(
            condition={"type": "item_min", "quantity": 1},
            effect={"type": "inventory", "item_id": "ITEM_TEST", "quantity": 1},
        )
        self.assertEqual([], validate_scenes(scenes))


if __name__ == "__main__":
    unittest.main()
