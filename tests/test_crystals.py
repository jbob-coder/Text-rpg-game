import copy
import unittest

from textrpg.core import RuleError
from textrpg.crystals import (
    crystal_player_view,
    effective_crystal_integrity,
    validate_crystal_definitions,
    validate_crystal_instance,
)


class CrystalContractTests(unittest.TestCase):
    def setUp(self):
        self.definitions = {
            "CRYSTAL_EMBER_HEART": {
                "name": "Ember Heart Crystal",
                "affinities": ["heat", "impact"],
                "tags": ["beast_core"],
                "allowed_source_types": ["beast"],
                "internal_effects": [{"type": "hidden_balance_data"}],
            },
            "CRYSTAL_CLEAR_VEIN": {
                "name": "Clear Vein Crystal",
                "affinities": ["stability"],
                "tags": ["mine"],
                "allowed_source_types": ["mine"],
            },
        }
        self.beast_instance = {
            "instance_id": "CRYSTAL_INSTANCE_001",
            "crystal_id": "CRYSTAL_EMBER_HEART",
            "source_type": "beast",
            "source_id": "BEAST_001",
            "beast_id": "BEAST_001",
            "grade": 3,
            "purity": 0.85,
            "stability": 0.72,
            "integrity": 0.9,
            "size": 1.25,
            "resonance": 14.0,
            "harvest_damage": 0.2,
            "appraisal_state": "known",
            "traits": ["TRAIT_HEAT_PULSE"],
        }

    def test_valid_beast_crystal_instance(self):
        validate_crystal_instance(self.beast_instance, self.definitions)

    def test_source_type_must_match_definition(self):
        instance = copy.deepcopy(self.beast_instance)
        instance["source_type"] = "mine"
        instance["deposit_id"] = "DEPOSIT_001"
        with self.assertRaises(RuleError):
            validate_crystal_instance(instance, self.definitions)

    def test_beast_source_requires_beast_id(self):
        instance = copy.deepcopy(self.beast_instance)
        del instance["beast_id"]
        with self.assertRaises(RuleError):
            validate_crystal_instance(instance, self.definitions)

    def test_mine_source_requires_deposit_id(self):
        instance = {
            "instance_id": "CRYSTAL_INSTANCE_002",
            "crystal_id": "CRYSTAL_CLEAR_VEIN",
            "source_type": "mine",
            "source_id": "DEPOSIT_001",
        }
        with self.assertRaises(RuleError):
            validate_crystal_instance(instance, self.definitions)

    def test_non_finite_or_out_of_range_quality_is_rejected(self):
        for field, value in (
            ("purity", float("nan")),
            ("stability", 1.1),
            ("integrity", -0.1),
            ("harvest_damage", 1.5),
        ):
            with self.subTest(field=field):
                instance = copy.deepcopy(self.beast_instance)
                instance[field] = value
                with self.assertRaises(RuleError):
                    validate_crystal_instance(instance, self.definitions)

    def test_unknown_appraisal_hides_definition_and_traits(self):
        instance = copy.deepcopy(self.beast_instance)
        instance["appraisal_state"] = "unknown"
        view = crystal_player_view(instance, self.definitions)
        self.assertEqual(view["name"], "Unknown Crystal")
        self.assertNotIn("crystal_id", view)
        self.assertNotIn("traits", view)
        self.assertNotIn("affinities", view)
        self.assertNotIn("resonance", view)

    def test_partial_appraisal_reveals_identity_but_not_deep_properties(self):
        instance = copy.deepcopy(self.beast_instance)
        instance["appraisal_state"] = "partial"
        view = crystal_player_view(instance, self.definitions)
        self.assertEqual(view["name"], "Ember Heart Crystal")
        self.assertEqual(view["grade"], 3)
        self.assertEqual(view["source_type"], "beast")
        self.assertNotIn("crystal_id", view)
        self.assertNotIn("purity", view)
        self.assertNotIn("traits", view)

    def test_known_appraisal_reveals_safe_properties_without_internal_definition_data(self):
        view = crystal_player_view(self.beast_instance, self.definitions)
        self.assertEqual(view["crystal_id"], "CRYSTAL_EMBER_HEART")
        self.assertEqual(view["affinities"], ["heat", "impact"])
        self.assertEqual(view["traits"], ["TRAIT_HEAT_PULSE"])
        self.assertNotIn("internal_effects", repr(view))
        self.assertNotIn("hidden_balance_data", repr(view))

    def test_hidden_definition_is_redacted_even_if_instance_is_known(self):
        definitions = copy.deepcopy(self.definitions)
        definitions["CRYSTAL_EMBER_HEART"]["player_visible"] = False
        view = crystal_player_view(self.beast_instance, definitions)
        self.assertEqual(
            view,
            {
                "instance_id": "CRYSTAL_INSTANCE_001",
                "appraisal_state": "unknown",
                "name": "Unknown Crystal",
            },
        )

    def test_effective_integrity_models_harvest_damage_without_mutation(self):
        before = copy.deepcopy(self.beast_instance)
        self.assertEqual(effective_crystal_integrity(self.beast_instance), 0.72)
        self.assertEqual(self.beast_instance, before)

    def test_duplicate_definition_tags_are_rejected(self):
        definitions = copy.deepcopy(self.definitions)
        definitions["CRYSTAL_CLEAR_VEIN"]["tags"] = ["mine", "mine"]
        with self.assertRaises(RuleError):
            validate_crystal_definitions(definitions)


if __name__ == "__main__":
    unittest.main()
