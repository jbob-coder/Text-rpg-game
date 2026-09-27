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


if __name__ == "__main__":
    unittest.main()
