import copy
import unittest

from textrpg.core import RuleError
from textrpg.forge import (
    crystal_weapon_compatibility,
    preview_crystal_integration,
    validate_forge_job,
)


class ForgeContractTests(unittest.TestCase):
    def setUp(self):
        self.weapon_definitions = {
            "WEAPON_IRON_SPEAR": {
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
                "min_crystal_stability": 0.60,
                "damage_profile": {
                    "cutting": 5.0,
                    "piercing": 32.0,
                    "blunt": 4.0,
                },
                "targeting_tags": ["general", "piercing", "polearm"],
                "armor_interaction_tags": ["anti_gap"],
                "allowed_crystal_tags": ["weapon_safe", "beast_core"],
            }
        }
        self.weapon_instance = {
            "instance_id": "WEAPON_INSTANCE_001",
            "weapon_id": "WEAPON_IRON_SPEAR",
            "material_id": "MATERIAL_IRON",
            "forge_quality": 0.75,
            "condition": 0.9,
            "durability": 87,
            "integrated_crystal_ids": [],
            "provenance": {},
        }
        self.crystal_definitions = {
            "CRYSTAL_EMBER_HEART": {
                "name": "Ember Heart Crystal",
                "affinities": ["heat", "impact"],
                "tags": ["beast_core", "weapon_safe"],
                "allowed_source_types": ["beast"],
            },
            "CRYSTAL_FRAGILE_VEIN": {
                "name": "Fragile Vein Crystal",
                "affinities": ["spark"],
                "tags": ["mine"],
                "allowed_source_types": ["mine"],
            },
        }
        self.beast_crystal = {
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

    def test_compatible_crystal_can_use_open_socket(self):
        result = crystal_weapon_compatibility(
            self.weapon_instance,
            self.weapon_definitions,
            self.beast_crystal,
            self.crystal_definitions,
        )
        self.assertTrue(result["compatible"])
        self.assertEqual(result["open_sockets"], 1)

    def test_full_socket_blocks_integration(self):
        weapon = copy.deepcopy(self.weapon_instance)
        weapon["integrated_crystal_ids"] = ["CRYSTAL_EXISTING"]
        result = crystal_weapon_compatibility(
            weapon,
            self.weapon_definitions,
            self.beast_crystal,
            self.crystal_definitions,
        )
        self.assertFalse(result["compatible"])
        self.assertIn("no_open_socket", result["reasons"])

    def test_incompatible_crystal_tags_are_rejected(self):
        crystal = {
            "instance_id": "CRYSTAL_INSTANCE_002",
            "crystal_id": "CRYSTAL_FRAGILE_VEIN",
            "source_type": "mine",
            "source_id": "DEPOSIT_001",
            "deposit_id": "DEPOSIT_001",
            "stability": 0.8,
            "integrity": 1.0,
        }
        result = crystal_weapon_compatibility(
            self.weapon_instance,
            self.weapon_definitions,
            crystal,
            self.crystal_definitions,
        )
        self.assertFalse(result["compatible"])
        self.assertIn("incompatible_crystal_tags", result["reasons"])

    def test_low_stability_blocks_integration(self):
        crystal = copy.deepcopy(self.beast_crystal)
        crystal["stability"] = 0.4
        result = crystal_weapon_compatibility(
            self.weapon_instance,
            self.weapon_definitions,
            crystal,
            self.crystal_definitions,
        )
        self.assertFalse(result["compatible"])
        self.assertIn("insufficient_crystal_stability", result["reasons"])

    def test_destroyed_crystal_blocks_integration(self):
        crystal = copy.deepcopy(self.beast_crystal)
        crystal["integrity"] = 0.0
        result = crystal_weapon_compatibility(
            self.weapon_instance,
            self.weapon_definitions,
            crystal,
            self.crystal_definitions,
        )
        self.assertFalse(result["compatible"])
        self.assertIn("crystal_destroyed", result["reasons"])

    def test_preview_is_non_mutating(self):
        weapon_before = copy.deepcopy(self.weapon_instance)
        crystal_before = copy.deepcopy(self.beast_crystal)
        result = preview_crystal_integration(
            self.weapon_instance,
            self.weapon_definitions,
            self.beast_crystal,
            self.crystal_definitions,
        )
        self.assertTrue(result["compatible"])
        self.assertEqual(
            result["integrated_crystal_ids"],
            ["CRYSTAL_INSTANCE_001"],
        )
        self.assertEqual(self.weapon_instance, weapon_before)
        self.assertEqual(self.beast_crystal, crystal_before)

    def test_valid_forge_job_requires_ordered_stage_prefix(self):
        job = {
            "job_id": "FORGE_JOB_001",
            "equipment_instance_id": "WEAPON_INSTANCE_001",
            "completed_stages": [
                "material_selection",
                "shaping",
            ],
            "current_stage": "finishing",
            "minutes_spent": 120,
            "quality_inputs": {
                "material_quality": 0.7,
                "smith_execution": 0.8,
            },
        }
        validate_forge_job(job)

    def test_skipped_forge_stage_is_rejected(self):
        job = {
            "job_id": "FORGE_JOB_001",
            "equipment_instance_id": "WEAPON_INSTANCE_001",
            "completed_stages": [
                "material_selection",
                "finishing",
            ],
            "current_stage": "crystal_housing",
            "minutes_spent": 120,
            "quality_inputs": {},
        }
        with self.assertRaises(RuleError):
            validate_forge_job(job)

    def test_current_stage_must_match_completed_prefix(self):
        job = {
            "job_id": "FORGE_JOB_001",
            "equipment_instance_id": "WEAPON_INSTANCE_001",
            "completed_stages": ["material_selection"],
            "current_stage": "inspection",
            "minutes_spent": 30,
            "quality_inputs": {},
        }
        with self.assertRaises(RuleError):
            validate_forge_job(job)

    def test_forge_quality_inputs_are_bounded(self):
        job = {
            "job_id": "FORGE_JOB_001",
            "equipment_instance_id": "WEAPON_INSTANCE_001",
            "completed_stages": [],
            "current_stage": "material_selection",
            "minutes_spent": 0,
            "quality_inputs": {
                "smith_execution": 1.5,
            },
        }
        with self.assertRaises(RuleError):
            validate_forge_job(job)


if __name__ == "__main__":
    unittest.main()
