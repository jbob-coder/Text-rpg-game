import copy
import unittest

from textrpg.combat import reachable_target_zone_ids
from textrpg.core import RuleError
from textrpg.weapons import (
    validate_weapon_definition,
    validate_weapon_instance,
    weapon_player_view,
    weapon_targeting_contract,
)


class WeaponContractTests(unittest.TestCase):
    def setUp(self):
        self.definition = {
            "weapon_id": "WEAPON_IRON_SPEAR",
            "name": "Iron Spear",
            "family": "spear",
            "range_bands": ["close", "reach"],
            "weight": 2.8,
            "reach": 2.1,
            "handling": 62.0,
            "balance": 0.72,
            "momentum": 35.0,
            "guard": 18.0,
            "penetration": 44.0,
            "recovery": 1.15,
            "stamina_burden": 7.0,
            "max_durability": 100,
            "crystal_socket_count": 1,
            "damage_profile": {
                "cutting": 5.0,
                "piercing": 32.0,
                "blunt": 4.0,
            },
            "targeting_tags": ["general", "piercing", "polearm"],
            "armor_interaction_tags": ["anti_gap"],
            "allowed_crystal_tags": ["weapon_safe"],
            "internal_balance_notes": {"do_not_expose": True},
        }
        self.definitions = {"WEAPON_IRON_SPEAR": self.definition}
        self.instance = {
            "instance_id": "WEAPON_INSTANCE_001",
            "weapon_id": "WEAPON_IRON_SPEAR",
            "material_id": "MATERIAL_IRON",
            "forge_quality": 0.75,
            "condition": 0.9,
            "durability": 87,
            "integrated_crystal_ids": ["CRYSTAL_INSTANCE_001"],
            "provenance": {
                "smith_id": "NPC_SMITH_001",
                "origin_id": "SETTLEMENT_001",
            },
        }

    def test_valid_weapon_definition(self):
        validate_weapon_definition(self.definition)

    def test_valid_weapon_instance(self):
        validate_weapon_instance(self.instance, self.definitions)

    def test_damage_profile_requires_supported_positive_damage(self):
        invalid = copy.deepcopy(self.definition)
        invalid["damage_profile"] = {"fire": 10}
        with self.assertRaises(RuleError):
            validate_weapon_definition(invalid)

        zero = copy.deepcopy(self.definition)
        zero["damage_profile"] = {
            "cutting": 0,
            "piercing": 0,
            "blunt": 0,
        }
        with self.assertRaises(RuleError):
            validate_weapon_definition(zero)

    def test_weapon_ranges_are_strict(self):
        invalid = copy.deepcopy(self.definition)
        invalid["range_bands"] = ["close", "orbital"]
        with self.assertRaises(RuleError):
            validate_weapon_definition(invalid)

    def test_instance_cannot_exceed_socket_capacity(self):
        invalid = copy.deepcopy(self.instance)
        invalid["integrated_crystal_ids"] = [
            "CRYSTAL_INSTANCE_001",
            "CRYSTAL_INSTANCE_002",
        ]
        with self.assertRaises(RuleError):
            validate_weapon_instance(invalid, self.definitions)

    def test_instance_durability_cannot_exceed_definition_max(self):
        invalid = copy.deepcopy(self.instance)
        invalid["durability"] = 101
        with self.assertRaises(RuleError):
            validate_weapon_instance(invalid, self.definitions)

    def test_non_finite_physical_values_are_rejected(self):
        for field in ("weight", "reach", "handling", "penetration", "recovery"):
            with self.subTest(field=field):
                invalid = copy.deepcopy(self.definition)
                invalid[field] = float("nan")
                with self.assertRaises(RuleError):
                    validate_weapon_definition(invalid)

    def test_targeting_contract_integrates_with_combat_rules(self):
        targeting = weapon_targeting_contract(self.definition)
        combat_state = {
            "range_band": "reach",
            "relative_facing": "front",
            "relative_elevation": "level",
            "defender_posture": "standing",
            "state_tags": ["core_exposed"],
            "blocked_zones": [],
        }
        zones = {
            "ZONE_CORE": {
                "name": "Core",
                "allowed_facings": ["front"],
                "allowed_range_bands": ["reach"],
                "requires_all_state_tags": ["core_exposed"],
                "required_weapon_tags": ["piercing"],
            }
        }
        self.assertEqual(
            reachable_target_zone_ids(combat_state, targeting, zones),
            ["ZONE_CORE"],
        )

    def test_player_view_exposes_physical_tradeoffs(self):
        view = weapon_player_view(self.instance, self.definitions)
        self.assertEqual(view["family"], "spear")
        self.assertEqual(view["reach"], 2.1)
        self.assertEqual(view["penetration"], 44.0)
        self.assertEqual(view["recovery"], 1.15)
        self.assertEqual(view["integrated_crystal_ids"], ["CRYSTAL_INSTANCE_001"])

    def test_player_view_does_not_expose_internal_balance_metadata(self):
        view = weapon_player_view(self.instance, self.definitions)
        self.assertNotIn("internal_balance_notes", repr(view))
        self.assertNotIn("do_not_expose", repr(view))

    def test_hidden_definition_redacts_weapon(self):
        definitions = copy.deepcopy(self.definitions)
        definitions["WEAPON_IRON_SPEAR"]["player_visible"] = False
        self.assertEqual(
            weapon_player_view(self.instance, definitions),
            {
                "instance_id": "WEAPON_INSTANCE_001",
                "name": "Unknown Weapon",
            },
        )

    def test_validation_and_views_do_not_mutate_inputs(self):
        definition_before = copy.deepcopy(self.definition)
        instance_before = copy.deepcopy(self.instance)
        validate_weapon_definition(self.definition)
        validate_weapon_instance(self.instance, self.definitions)
        weapon_targeting_contract(self.definition)
        weapon_player_view(self.instance, self.definitions)
        self.assertEqual(self.definition, definition_before)
        self.assertEqual(self.instance, instance_before)


if __name__ == "__main__":
    unittest.main()
