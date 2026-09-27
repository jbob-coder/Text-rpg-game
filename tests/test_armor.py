import copy
import unittest

from textrpg.armor import (
    armor_layers_for_zone,
    armor_player_view,
    validate_armor_definition,
    validate_armor_instance,
)
from textrpg.core import RuleError


class ArmorContractTests(unittest.TestCase):
    def setUp(self):
        self.definitions = {
            "ARMOR_IRON_CUIRASS": {
                "armor_id": "ARMOR_IRON_CUIRASS",
                "name": "Iron Cuirass",
                "slot": "body",
                "covered_zones": ["ZONE_CHEST", "ZONE_ABDOMEN", "ZONE_BACK"],
                "weight": 9.5,
                "flexibility": 0.35,
                "noise": 0.65,
                "fatigue_burden": 8.0,
                "max_durability": 160,
                "crystal_socket_count": 1,
                "resistances": {
                    "cutting": 38.0,
                    "piercing": 25.0,
                    "blunt": 16.0,
                },
                "tags": ["plate", "metal"],
                "allowed_crystal_tags": ["armor_safe"],
                "internal_notes": {"hidden": True},
            },
            "ARMOR_MAIL_COIF": {
                "armor_id": "ARMOR_MAIL_COIF",
                "name": "Mail Coif",
                "slot": "head",
                "covered_zones": ["ZONE_HEAD", "ZONE_NECK"],
                "weight": 2.2,
                "flexibility": 0.7,
                "noise": 0.45,
                "fatigue_burden": 2.0,
                "max_durability": 90,
                "crystal_socket_count": 0,
                "resistances": {
                    "cutting": 24.0,
                    "piercing": 12.0,
                    "blunt": 5.0,
                },
                "tags": ["mail", "metal"],
            },
        }
        self.cuirass = {
            "instance_id": "ARMOR_INSTANCE_001",
            "armor_id": "ARMOR_IRON_CUIRASS",
            "material_id": "MATERIAL_IRON",
            "forge_quality": 0.8,
            "condition": 0.9,
            "durability": 145,
            "integrated_crystal_ids": ["CRYSTAL_INSTANCE_010"],
            "provenance": {"smith_id": "NPC_SMITH_001"},
        }
        self.coif = {
            "instance_id": "ARMOR_INSTANCE_002",
            "armor_id": "ARMOR_MAIL_COIF",
            "material_id": "MATERIAL_IRON",
            "forge_quality": 0.65,
            "condition": 1.0,
            "durability": 90,
            "integrated_crystal_ids": [],
            "provenance": {},
        }

    def test_valid_armor_definition_and_instance(self):
        validate_armor_definition(self.definitions["ARMOR_IRON_CUIRASS"])
        validate_armor_instance(self.cuirass, self.definitions)

    def test_coverage_must_not_be_empty(self):
        invalid = copy.deepcopy(self.definitions["ARMOR_IRON_CUIRASS"])
        invalid["covered_zones"] = []
        with self.assertRaises(RuleError):
            validate_armor_definition(invalid)

    def test_unknown_resistance_type_is_rejected(self):
        invalid = copy.deepcopy(self.definitions["ARMOR_IRON_CUIRASS"])
        invalid["resistances"]["arcane"] = 10
        with self.assertRaises(RuleError):
            validate_armor_definition(invalid)

    def test_instance_cannot_exceed_socket_capacity(self):
        invalid = copy.deepcopy(self.cuirass)
        invalid["integrated_crystal_ids"] = ["C1", "C2"]
        with self.assertRaises(RuleError):
            validate_armor_instance(invalid, self.definitions)

    def test_zone_query_returns_only_covering_layers(self):
        equipped = {
            "body": self.cuirass,
            "head": self.coif,
        }
        chest = armor_layers_for_zone(equipped, self.definitions, "ZONE_CHEST")
        self.assertEqual(len(chest), 1)
        self.assertEqual(chest[0]["armor_id"], "ARMOR_IRON_CUIRASS")

        head = armor_layers_for_zone(equipped, self.definitions, "ZONE_HEAD")
        self.assertEqual(len(head), 1)
        self.assertEqual(head[0]["armor_id"], "ARMOR_MAIL_COIF")

    def test_uncovered_zone_returns_no_layers(self):
        equipped = {
            "body": self.cuirass,
            "head": self.coif,
        }
        self.assertEqual(
            armor_layers_for_zone(equipped, self.definitions, "ZONE_HAND"),
            [],
        )

    def test_wrong_slot_is_rejected(self):
        equipped = {"head": self.cuirass}
        with self.assertRaises(RuleError):
            armor_layers_for_zone(equipped, self.definitions, "ZONE_CHEST")

    def test_player_view_exposes_coverage_tradeoffs(self):
        view = armor_player_view(self.cuirass, self.definitions)
        self.assertEqual(view["slot"], "body")
        self.assertIn("ZONE_CHEST", view["covered_zones"])
        self.assertEqual(view["resistances"]["cutting"], 38.0)
        self.assertEqual(view["weight"], 9.5)
        self.assertEqual(view["integrated_crystal_ids"], ["CRYSTAL_INSTANCE_010"])

    def test_player_view_omits_internal_definition_metadata(self):
        view = armor_player_view(self.cuirass, self.definitions)
        self.assertNotIn("internal_notes", repr(view))
        self.assertNotIn("hidden", repr(view))

    def test_non_finite_values_are_rejected(self):
        invalid = copy.deepcopy(self.definitions["ARMOR_IRON_CUIRASS"])
        invalid["weight"] = float("nan")
        with self.assertRaises(RuleError):
            validate_armor_definition(invalid)

    def test_queries_do_not_mutate_inputs(self):
        definitions_before = copy.deepcopy(self.definitions)
        cuirass_before = copy.deepcopy(self.cuirass)
        equipped = {"body": self.cuirass}
        armor_layers_for_zone(equipped, self.definitions, "ZONE_CHEST")
        armor_player_view(self.cuirass, self.definitions)
        self.assertEqual(self.definitions, definitions_before)
        self.assertEqual(self.cuirass, cuirass_before)


if __name__ == "__main__":
    unittest.main()
