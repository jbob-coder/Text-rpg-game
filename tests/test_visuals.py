import unittest

from textrpg import RuleError
from textrpg.visuals import (
    assert_valid_character_visuals,
    character_generation_contract,
    validate_character_visuals,
)


class VisualIdentityTests(unittest.TestCase):
    def record(self):
        return {
            "height_class": "average",
            "body_proportions": "slim athletic; 7.5-head adult proportion",
            "skin_tone": "medium warm brown",
            "hair": {
                "shape": "angular layered crop",
                "length": "short",
                "palette": "near-black with muted cool highlights",
            },
            "eye_color": "dark brown",
            "default_outfit": "charcoal utility jacket over a pale work shirt",
            "silhouette_anchors": [
                "high jacket collar",
                "narrow shoulder satchel",
            ],
            "role_markers": ["district maintenance badge"],
            "equipment_attachment_points": ["left hip", "satchel strap"],
            "permanent_marks": ["small notch through right eyebrow"],
            "forbidden_deviations": [
                "no long hair",
                "no bright saturated jacket",
            ],
            "emotion_set": [
                "neutral",
                "concerned",
                "angry",
                "relieved",
            ],
            "poses": ["front", "profile", "three-quarter"],
            "palette": {
                "jacket": "#30343B",
                "shirt": "#C9C7BE",
            },
            "approved_reference_assets": [],
        }

    def test_valid_identity_passes(self):
        records = {"NPC_TAMSIN": self.record()}
        self.assertEqual(validate_character_visuals(records), [])
        assert_valid_character_visuals(records)

    def test_missing_identity_field_is_reported(self):
        record = self.record()
        del record["silhouette_anchors"]
        errors = validate_character_visuals({"NPC_TAMSIN": record})
        self.assertTrue(
            any("missing required visual field: silhouette_anchors" in e for e in errors)
        )

    def test_duplicate_expression_is_rejected(self):
        record = self.record()
        record["emotion_set"].append("neutral")
        errors = validate_character_visuals({"NPC_TAMSIN": record})
        self.assertTrue(any("emotion_set contains duplicate entries" in e for e in errors))

    def test_generation_contract_preserves_identity_and_canon_rule(self):
        contract = character_generation_contract("NPC_TAMSIN", self.record())
        self.assertEqual(contract["character_id"], "NPC_TAMSIN")
        self.assertEqual(
            contract["identity"]["permanent_marks"],
            ["small notch through right eyebrow"],
        )
        self.assertIn("candidate-only", contract["canon_rule"])

    def test_invalid_character_id_rejected(self):
        with self.assertRaises(RuleError):
            character_generation_contract("bad-id", self.record())


    def test_visual_validator_rejects_non_mapping_root_without_crash(self):
        self.assertEqual(
            validate_character_visuals([]),
            ["character visual records must be an object"],
        )


    def test_unhashable_list_entries_are_rejected_without_type_error(self):
        for field in (
            "silhouette_anchors", "role_markers", "equipment_attachment_points",
            "permanent_marks", "forbidden_deviations", "emotion_set", "poses",
        ):
            with self.subTest(field=field):
                record = self.record()
                record[field] = ["valid", {"invalid": "object"}]
                errors = validate_character_visuals({"NPC_TAMSIN": record})
                self.assertTrue(
                    any(f"{field} entries must be non-empty strings" in e for e in errors)
                )
                with self.assertRaises(RuleError):
                    character_generation_contract("NPC_TAMSIN", record)

    def test_null_required_scalar_or_hair_is_rejected(self):
        for field in ("height_class", "body_proportions", "skin_tone", "default_outfit", "hair"):
            with self.subTest(field=field):
                record = self.record()
                record[field] = None
                errors = validate_character_visuals({"NPC_TAMSIN": record})
                self.assertTrue(any(f"NPC_TAMSIN.{field}" in e for e in errors))
                with self.assertRaises(RuleError):
                    character_generation_contract("NPC_TAMSIN", record)

    def test_null_required_lists_are_rejected(self):
        for field in (
            "silhouette_anchors", "role_markers", "equipment_attachment_points",
            "permanent_marks", "forbidden_deviations", "emotion_set", "poses",
        ):
            with self.subTest(field=field):
                record = self.record()
                record[field] = None
                errors = validate_character_visuals({"NPC_TAMSIN": record})
                self.assertIn(f"NPC_TAMSIN.{field} must be a list", errors)
                with self.assertRaises(RuleError):
                    character_generation_contract("NPC_TAMSIN", record)

    def test_null_optional_palette_does_not_crash_generation(self):
        record = self.record()
        record["palette"] = None
        errors = validate_character_visuals({"NPC_TAMSIN": record})
        self.assertIn("NPC_TAMSIN.palette must be an object", errors)
        with self.assertRaises(RuleError):
            character_generation_contract("NPC_TAMSIN", record)

        del record["palette"]
        self.assertEqual(validate_character_visuals({"NPC_TAMSIN": record}), [])
        self.assertEqual(character_generation_contract("NPC_TAMSIN", record)["palette"], {})

    def test_null_optional_reference_assets_returns_contract_error(self):
        record = self.record()
        record["approved_reference_assets"] = None
        errors = validate_character_visuals({"NPC_TAMSIN": record})
        self.assertTrue(any("approved_reference_assets must be a list" in e for e in errors))
        with self.assertRaises(RuleError):
            character_generation_contract("NPC_TAMSIN", record)


if __name__ == "__main__":
    unittest.main()
