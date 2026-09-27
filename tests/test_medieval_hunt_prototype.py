import copy
import unittest

from textrpg.armor import armor_layers_for_zone
from textrpg.beasts import adaptation_readiness, record_encounter_observation
from textrpg.combat import build_targeting_view, reachable_target_zone_ids
from textrpg.crystals import effective_crystal_integrity
from textrpg.forge import preview_crystal_integration
from textrpg.weapons import weapon_targeting_contract
from textrpg.wounds import (
    apply_zone_damage,
    crystal_harvest_damage_from_zone_hit,
)


class MedievalHuntPrototypeIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.weapon_definitions = {
            "WEAPON_HUNTER_SPEAR": {
                "weapon_id": "WEAPON_HUNTER_SPEAR",
                "name": "Hunter Spear",
                "family": "spear",
                "range_bands": ["close", "reach"],
                "weight": 2.6,
                "reach": 2.2,
                "handling": 66.0,
                "balance": 0.76,
                "momentum": 32.0,
                "guard": 17.0,
                "penetration": 48.0,
                "recovery": 1.05,
                "stamina_burden": 6.5,
                "max_durability": 100,
                "crystal_socket_count": 1,
                "min_crystal_stability": 0.60,
                "damage_profile": {
                    "cutting": 4.0,
                    "piercing": 34.0,
                    "blunt": 3.0,
                },
                "targeting_tags": ["general", "piercing", "polearm"],
                "armor_interaction_tags": ["anti_gap"],
                "allowed_crystal_tags": ["beast_core", "weapon_safe"],
            }
        }
        self.weapon_instance = {
            "instance_id": "WEAPON_INSTANCE_HUNTER_SPEAR",
            "weapon_id": "WEAPON_HUNTER_SPEAR",
            "material_id": "MATERIAL_IRON",
            "forge_quality": 0.72,
            "condition": 0.92,
            "durability": 91,
            "integrated_crystal_ids": [],
            "provenance": {"smith_id": "NPC_SMITH_HALE"},
        }
        self.targeting_weapon = weapon_targeting_contract(
            self.weapon_definitions["WEAPON_HUNTER_SPEAR"]
        )

        self.body_zones = {
            "ZONE_CHEST": {
                "name": "Chest",
                "allowed_facings": ["front", "left_flank", "right_flank"],
                "allowed_range_bands": ["close", "reach", "ranged"],
            },
            "ZONE_RIGHT_FORELEG": {
                "name": "Right Foreleg",
                "allowed_facings": ["front", "right_flank"],
                "allowed_range_bands": ["close", "reach"],
            },
            "ZONE_HEAD": {
                "name": "Head",
                "allowed_facings": ["front", "left_flank", "right_flank"],
                "allowed_range_bands": ["close", "reach", "ranged"],
                "requires_any_state_tags": [
                    "defender_knocked_down",
                    "attacker_elevated",
                ],
            },
            "ZONE_CORE": {
                "name": "Heart Crystal",
                "allowed_facings": ["front"],
                "allowed_range_bands": ["close", "reach"],
                "requires_all_state_tags": ["core_exposed"],
                "required_weapon_tags": ["piercing"],
            },
        }
        self.combat_state = {
            "range_band": "reach",
            "relative_facing": "front",
            "relative_elevation": "level",
            "defender_posture": "standing",
            "state_tags": [],
            "blocked_zones": [],
        }

        self.wound_profiles = {
            "ZONE_RIGHT_FORELEG": {
                "thresholds": [
                    {
                        "integrity_lte": 0.75,
                        "tags": ["foreleg_wounded"],
                        "disabled_actions": [],
                    },
                    {
                        "integrity_lte": 0.35,
                        "tags": ["foreleg_crippled"],
                        "disabled_actions": ["heavy_charge"],
                    },
                ],
                "crystal_damage_multiplier": 0.0,
            },
            "ZONE_CORE": {
                "thresholds": [
                    {
                        "integrity_lte": 0.60,
                        "tags": ["core_damaged"],
                        "disabled_actions": [],
                    },
                    {
                        "integrity_lte": 0.20,
                        "tags": ["core_critical"],
                        "disabled_actions": ["crystal_burst"],
                    },
                ],
                "crystal_damage_multiplier": 0.8,
            },
        }
        self.body_state = {
            zone_id: {"integrity": 1.0, "tags": [], "disabled_actions": []}
            for zone_id in self.body_zones
        }

        self.beast = {
            "beast_id": "BEAST_STONEFANG_001",
            "species_id": "SPECIES_STONEFANG",
            "level": 8,
            "development_xp": 125.0,
            "intelligence": 3,
            "role": "veteran",
            "alive": True,
            "encounter_memory": {},
            "adaptations": [],
            "followers": [],
        }

        self.crystal_definitions = {
            "CRYSTAL_STONEFANG_HEART": {
                "name": "Stonefang Heart Crystal",
                "affinities": ["impact", "guard"],
                "tags": ["beast_core", "weapon_safe"],
                "allowed_source_types": ["beast"],
            }
        }
        self.crystal_instance = {
            "instance_id": "CRYSTAL_INSTANCE_STONEFANG_001",
            "crystal_id": "CRYSTAL_STONEFANG_HEART",
            "source_type": "beast",
            "source_id": "BEAST_STONEFANG_001",
            "beast_id": "BEAST_STONEFANG_001",
            "grade": 3,
            "purity": 0.88,
            "stability": 0.75,
            "integrity": 1.0,
            "size": 1.4,
            "resonance": 12.0,
            "harvest_damage": 0.0,
            "appraisal_state": "known",
            "traits": ["TRAIT_GUARD_PULSE"],
        }

        self.armor_definitions = {
            "ARMOR_BEAST_PLATE": {
                "armor_id": "ARMOR_BEAST_PLATE",
                "name": "Beast Plate",
                "slot": "body",
                "covered_zones": ["ZONE_CHEST"],
                "weight": 12.0,
                "flexibility": 0.25,
                "noise": 0.75,
                "fatigue_burden": 10.0,
                "max_durability": 200,
                "crystal_socket_count": 0,
                "resistances": {
                    "cutting": 45.0,
                    "piercing": 30.0,
                    "blunt": 20.0,
                },
                "tags": ["beast_plate"],
            }
        }
        self.equipped_armor = {
            "body": {
                "instance_id": "ARMOR_INSTANCE_BEAST_PLATE",
                "armor_id": "ARMOR_BEAST_PLATE",
                "material_id": "MATERIAL_BEAST_PLATE",
                "forge_quality": 0.7,
                "condition": 1.0,
                "durability": 200,
                "integrated_crystal_ids": [],
                "provenance": {},
            }
        }

    def test_first_encounter_retreat_and_memory_change_rematch(self):
        initial_targets = reachable_target_zone_ids(
            self.combat_state,
            self.targeting_weapon,
            self.body_zones,
        )
        self.assertEqual(initial_targets, ["ZONE_CHEST", "ZONE_RIGHT_FORELEG"])
        self.assertNotIn("ZONE_HEAD", initial_targets)
        self.assertNotIn("ZONE_CORE", initial_targets)

        chest_layers = armor_layers_for_zone(
            self.equipped_armor,
            self.armor_definitions,
            "ZONE_CHEST",
        )
        foreleg_layers = armor_layers_for_zone(
            self.equipped_armor,
            self.armor_definitions,
            "ZONE_RIGHT_FORELEG",
        )
        self.assertEqual(len(chest_layers), 1)
        self.assertEqual(foreleg_layers, [])

        apply_zone_damage(
            self.body_state,
            zone_id="ZONE_RIGHT_FORELEG",
            damage_fraction=0.35,
            profiles=self.wound_profiles,
        )
        self.assertIn(
            "foreleg_wounded",
            self.body_state["ZONE_RIGHT_FORELEG"]["tags"],
        )

        for minute in (100, 120):
            record_encounter_observation(
                self.beast,
                kind="target_zone",
                value="ZONE_RIGHT_FORELEG",
                time_minutes=minute,
                confidence_increment=0.5,
            )
        record_encounter_observation(
            self.beast,
            kind="retreat",
            value="player_retreated",
            time_minutes=130,
            confidence_increment=0.5,
        )

        readiness = adaptation_readiness(
            self.beast,
            kind="target_zone",
            value="ZONE_RIGHT_FORELEG",
            adaptation_type="behavioral",
        )
        self.assertTrue(readiness["ready"])

        rematch = copy.deepcopy(self.combat_state)
        rematch["state_tags"] = ["defender_knocked_down"]
        rematch_targets = build_targeting_view(
            rematch,
            self.targeting_weapon,
            self.body_zones,
        )
        rematch_ids = [entry["id"] for entry in rematch_targets["target_zones"]]
        self.assertIn("ZONE_HEAD", rematch_ids)
        self.assertNotIn("ZONE_CORE", rematch_ids)

    def test_core_kill_tradeoff_can_damage_loot_then_feed_forge_preview(self):
        execution_state = copy.deepcopy(self.combat_state)
        execution_state["state_tags"] = ["core_exposed"]
        targets = reachable_target_zone_ids(
            execution_state,
            self.targeting_weapon,
            self.body_zones,
        )
        self.assertIn("ZONE_CORE", targets)

        core_damage = 0.50
        apply_zone_damage(
            self.body_state,
            zone_id="ZONE_CORE",
            damage_fraction=core_damage,
            profiles=self.wound_profiles,
        )
        harvest_damage = crystal_harvest_damage_from_zone_hit(
            zone_id="ZONE_CORE",
            damage_fraction=core_damage,
            profiles=self.wound_profiles,
        )
        self.assertEqual(harvest_damage, 0.40)

        harvested_crystal = copy.deepcopy(self.crystal_instance)
        harvested_crystal["harvest_damage"] = harvest_damage
        self.assertEqual(effective_crystal_integrity(harvested_crystal), 0.60)

        preview = preview_crystal_integration(
            self.weapon_instance,
            self.weapon_definitions,
            harvested_crystal,
            self.crystal_definitions,
        )
        self.assertTrue(preview["compatible"])
        self.assertEqual(
            preview["integrated_crystal_ids"],
            ["CRYSTAL_INSTANCE_STONEFANG_001"],
        )

    def test_environment_changes_target_list_without_mutating_anatomy(self):
        anatomy_before = copy.deepcopy(self.body_zones)
        initial = reachable_target_zone_ids(
            self.combat_state,
            self.targeting_weapon,
            self.body_zones,
        )

        changed = copy.deepcopy(self.combat_state)
        changed["state_tags"] = [
            "defender_knocked_down",
            "core_exposed",
        ]
        later = reachable_target_zone_ids(
            changed,
            self.targeting_weapon,
            self.body_zones,
        )

        self.assertNotEqual(initial, later)
        self.assertIn("ZONE_HEAD", later)
        self.assertIn("ZONE_CORE", later)
        self.assertEqual(self.body_zones, anatomy_before)


if __name__ == "__main__":
    unittest.main()
