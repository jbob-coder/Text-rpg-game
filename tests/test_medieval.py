import unittest

from textrpg.core import RuleError
from textrpg.medieval import (
    beast_role_eligibility,
    build_targeting_view,
    reachable_target_zones,
    validate_beast_runtime_state,
    validate_crystal_instance,
    validate_weapon_definition,
)


class MedievalContractTests(unittest.TestCase):
    def weapon(self):
        return {
            "family": "spear",
            "range_bands": ["close", "reach"],
            "target_tags": ["high", "mid", "limb", "core"],
            "damage_profile": {"pierce": 8, "blunt": 2},
            "weight": 4.5,
            "reach": 2.2,
            "recovery": 1.0,
        }

    def zones(self):
        return {
            "ZONE_HEAD": {
                "label": "Head",
                "facings": ["front", "left_flank", "right_flank"],
                "range_bands": ["close", "reach", "ranged"],
                "tags": ["high"],
            },
            "ZONE_HEART_CORE": {
                "label": "Heart/Core",
                "facings": ["left_flank", "right_flank"],
                "range_bands": ["close", "reach"],
                "tags": ["core", "mid"],
                "requires_exposure_tags": ["CORE_EXPOSED"],
                "vital": True,
                "crystal_risk": True,
            },
            "ZONE_HIND_LEG": {
                "label": "Hind leg",
                "facings": ["left_flank", "right_flank", "rear"],
                "range_bands": ["close", "reach"],
                "tags": ["limb"],
            },
        }

    def combat(self, **changes):
        state = {
            "facing": "front",
            "range_band": "reach",
            "attacker_posture": "standing",
            "defender_posture": "standing",
            "elevation": "level",
            "exposure_tags": [],
            "blocked_zones": [],
        }
        state.update(changes)
        return state

    def test_weapon_contract_rejects_nonfinite_and_empty_damage(self):
        bad = self.weapon()
        bad["weight"] = float("nan")
        bad["damage_profile"] = {"pierce": 0}
        errors = validate_weapon_definition("WEAPON_SPEAR", bad)
        self.assertTrue(any("weight" in error for error in errors))
        self.assertTrue(any("positive damage" in error for error in errors))

    def test_beast_crystal_requires_beast_provenance(self):
        crystal = {
            "instance_id": "CRYSTAL_INSTANCE_1",
            "crystal_id": "CRYSTAL_WOLF_HEART",
            "source_type": "beast",
            "grade": 2,
            "purity": 80,
            "stability": 70,
            "harvest_integrity": 95,
            "size": 1.2,
            "resonance_tags": ["frost"],
        }
        errors = validate_crystal_instance(crystal)
        self.assertTrue(any("source_beast_id" in error for error in errors))
        crystal["source_beast_id"] = "BEAST_WHITE_FANG"
        self.assertEqual(validate_crystal_instance(crystal), [])

    def test_front_position_does_not_expose_all_body_zones(self):
        self.assertEqual(
            reachable_target_zones(self.combat(), self.zones(), self.weapon()),
            ["ZONE_HEAD"],
        )

    def test_battle_state_change_unlocks_core_and_flank_targets(self):
        state = self.combat(
            facing="left_flank",
            exposure_tags=["CORE_EXPOSED"],
        )
        self.assertEqual(
            reachable_target_zones(state, self.zones(), self.weapon()),
            ["ZONE_HEAD", "ZONE_HEART_CORE", "ZONE_HIND_LEG"],
        )

    def test_weapon_range_can_make_every_zone_unavailable(self):
        dagger = {
            "family": "dagger",
            "range_bands": ["grapple", "close"],
            "target_tags": ["high", "mid", "limb", "core"],
            "damage_profile": {"pierce": 5},
        }
        self.assertEqual(
            reachable_target_zones(self.combat(range_band="reach"), self.zones(), dagger),
            [],
        )

    def test_blocked_zone_is_removed_even_when_geometry_matches(self):
        state = self.combat(blocked_zones=["ZONE_HEAD"])
        self.assertEqual(reachable_target_zones(state, self.zones(), self.weapon()), [])

    def test_targeting_view_does_not_leak_authored_access_rules(self):
        view = build_targeting_view(
            self.combat(facing="left_flank", exposure_tags=["CORE_EXPOSED"]),
            self.zones(),
            self.weapon(),
        )
        self.assertEqual(
            set(view),
            {"facing", "range_band", "targets"},
        )
        for target in view["targets"]:
            self.assertEqual(set(target), {"zone_id", "label"})
            self.assertNotIn("requires_exposure_tags", target)
            self.assertNotIn("crystal_risk", target)

    def test_beast_runtime_contract_keeps_level_and_intelligence_separate(self):
        beast = {
            "beast_id": "BEAST_1",
            "species_id": "SPECIES_WOLF",
            "level": 40,
            "development_xp": 1200,
            "intelligence_tier": 1,
            "role": "veteran",
            "follower_count": 0,
            "memories": [],
            "adaptations": [],
        }
        self.assertEqual(validate_beast_runtime_state(beast), [])
        gate = beast_role_eligibility(
            beast,
            {
                "min_level": 20,
                "min_intelligence_tier": 4,
                "min_followers": 3,
                "territory_required": True,
            },
        )
        self.assertFalse(gate["eligible"])
        self.assertEqual(gate["missing"], ["intelligence", "followers", "territory"])

    def test_commander_gate_can_be_satisfied_without_changing_level(self):
        beast = {
            "beast_id": "BEAST_1",
            "species_id": "SPECIES_WOLF",
            "level": 40,
            "development_xp": 1200,
            "intelligence_tier": 4,
            "role": "veteran",
            "follower_count": 5,
            "territory_id": "REGION_ASH_PASS",
            "memories": [],
            "adaptations": [],
        }
        gate = beast_role_eligibility(
            beast,
            {
                "min_level": 20,
                "min_intelligence_tier": 4,
                "min_followers": 3,
                "territory_required": True,
            },
        )
        self.assertEqual(gate, {"eligible": True, "missing": []})

    def test_invalid_contracts_raise_before_targeting(self):
        with self.assertRaises(RuleError):
            reachable_target_zones(
                self.combat(range_band="teleport"),
                self.zones(),
                self.weapon(),
            )


if __name__ == "__main__":
    unittest.main()
