import unittest

from textrpg.beast_harvest import (
    apply_body_zone_damage,
    harvest_beast_crystal,
    validate_body_zone_runtime,
    validate_crystal_definition,
)
from textrpg.core import RuleError
from textrpg.crystal_forging import integrate_crystal
from textrpg.medieval import validate_crystal_instance


class BeastHarvestTests(unittest.TestCase):
    def beast(self, **changes):
        state = {
            "beast_id": "BEAST_WHITE_FANG",
            "species_id": "SPECIES_WOLF",
            "level": 20,
            "development_xp": 500,
            "intelligence_tier": 2,
            "role": "veteran",
            "follower_count": 0,
            "memories": [],
            "adaptations": [],
            "life_state": "dead",
        }
        state.update(changes)
        return state

    def core_zone(self, **changes):
        zone = {
            "zone_id": "ZONE_HEART_CORE",
            "max_integrity": 100,
            "damage_taken": 0,
            "hits": 0,
            "damage_by_type": {},
        }
        zone.update(changes)
        return zone

    def definition(self, **changes):
        definition = {
            "crystal_id": "CRYSTAL_WOLF_HEART",
            "core_zone_id": "ZONE_HEART_CORE",
            "base_grade": 2,
            "base_purity": 86,
            "base_stability": 90,
            "size": 1.1,
            "resonance_tags": ["frost"],
            "core_damage_sensitivity": 1.0,
            "decay_per_hour": 2.0,
        }
        definition.update(changes)
        return definition

    def equipment(self):
        return {
            "instance_id": "ITEMINSTANCE_SPEAR_1",
            "definition_id": "WEAPON_SPEAR_IRON",
            "material_id": "MATERIAL_IRON",
            "forge_quality": 80,
            "condition": 100,
            "crystal_sockets": [
                {
                    "socket_id": "SOCKET_PRIMARY",
                    "max_grade": 3,
                    "allowed_source_types": ["beast"],
                    "allowed_resonance_tags": ["frost"],
                    "allowed_modes": ["socket", "fusion"],
                    "crystal": None,
                }
            ],
        }

    def test_crystal_definition_contract_accepts_valid_definition(self):
        self.assertEqual(validate_crystal_definition(self.definition()), [])

    def test_zone_damage_is_copy_on_write_and_capped(self):
        original = self.core_zone(damage_taken=90, hits=1, damage_by_type={"pierce": 90})
        updated = apply_body_zone_damage(original, 50, "pierce")
        self.assertEqual(original["damage_taken"], 90)
        self.assertEqual(updated["damage_taken"], 100.0)
        self.assertEqual(updated["damage_by_type"]["pierce"], 100.0)
        self.assertTrue(updated["broken"])

    def test_direct_core_damage_reduces_harvest_integrity_and_stability(self):
        pristine = harvest_beast_crystal(
            self.beast(),
            self.core_zone(),
            self.definition(),
            instance_id="CRYSTALINSTANCE_PRISTINE",
            harvest_skill=100,
            tool_quality=100,
        )
        damaged = harvest_beast_crystal(
            self.beast(),
            self.core_zone(damage_taken=60, hits=2, damage_by_type={"pierce": 60}),
            self.definition(),
            instance_id="CRYSTALINSTANCE_DAMAGED",
            harvest_skill=100,
            tool_quality=100,
        )
        self.assertEqual(pristine["harvest_integrity"], 100.0)
        self.assertLess(damaged["harvest_integrity"], pristine["harvest_integrity"])
        self.assertLess(damaged["stability"], pristine["stability"])
        self.assertEqual(damaged["harvest"]["core_damage_percent"], 60.0)

    def test_extraction_skill_and_tool_quality_cannot_restore_combat_damage(self):
        zone = self.core_zone(damage_taken=50, hits=1, damage_by_type={"cut": 50})
        expert = harvest_beast_crystal(
            self.beast(), zone, self.definition(),
            instance_id="CRYSTALINSTANCE_EXPERT",
            harvest_skill=100, tool_quality=100,
        )
        novice = harvest_beast_crystal(
            self.beast(), zone, self.definition(),
            instance_id="CRYSTALINSTANCE_NOVICE",
            harvest_skill=0, tool_quality=0,
        )
        self.assertEqual(expert["harvest_integrity"], 50.0)
        self.assertEqual(novice["harvest_integrity"], 25.0)
        self.assertLessEqual(expert["harvest_integrity"], 50.0)

    def test_delayed_harvest_reduces_integrity_when_definition_decays(self):
        immediate = harvest_beast_crystal(
            self.beast(), self.core_zone(), self.definition(),
            instance_id="CRYSTALINSTANCE_NOW",
            harvest_skill=100, tool_quality=100,
            elapsed_minutes=0,
        )
        late = harvest_beast_crystal(
            self.beast(), self.core_zone(), self.definition(),
            instance_id="CRYSTALINSTANCE_LATE",
            harvest_skill=100, tool_quality=100,
            elapsed_minutes=300,
        )
        self.assertEqual(immediate["harvest_integrity"], 100.0)
        self.assertEqual(late["harvest_integrity"], 90.0)

    def test_live_beast_cannot_be_harvested(self):
        with self.assertRaises(RuleError):
            harvest_beast_crystal(
                self.beast(life_state="alive"),
                self.core_zone(),
                self.definition(),
                instance_id="CRYSTALINSTANCE_BAD",
                harvest_skill=100,
                tool_quality=100,
            )

    def test_core_zone_must_match_species_crystal_definition(self):
        with self.assertRaises(RuleError):
            harvest_beast_crystal(
                self.beast(),
                self.core_zone(zone_id="ZONE_HEAD"),
                self.definition(),
                instance_id="CRYSTALINSTANCE_BAD",
                harvest_skill=100,
                tool_quality=100,
            )

    def test_harvested_crystal_is_valid_and_can_enter_forging_contract(self):
        crystal = harvest_beast_crystal(
            self.beast(),
            self.core_zone(damage_taken=20, hits=1, damage_by_type={"pierce": 20}),
            self.definition(),
            instance_id="CRYSTALINSTANCE_FORGE",
            harvest_skill=90,
            tool_quality=80,
        )
        self.assertEqual(validate_crystal_instance(crystal), [])
        fitted = integrate_crystal(
            self.equipment(),
            crystal,
            "SOCKET_PRIMARY",
            mode="socket",
            integration_quality=87,
            smith_id="NPC_SMITH_1",
        )
        installed = fitted["crystal_sockets"][0]["crystal"]
        self.assertEqual(installed["source_beast_id"], "BEAST_WHITE_FANG")
        self.assertEqual(installed["harvest_integrity"], crystal["harvest_integrity"])
        self.assertEqual(installed["harvest"]["core_damage_percent"], 20.0)

    def test_zone_runtime_rejects_damage_above_maximum(self):
        errors = validate_body_zone_runtime(self.core_zone(damage_taken=101))
        self.assertTrue(any("cannot exceed" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
