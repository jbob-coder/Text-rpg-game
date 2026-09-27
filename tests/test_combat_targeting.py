import copy
import unittest

from textrpg.combat import (
    build_targeting_view,
    explain_target_zone_access,
    reachable_target_zone_ids,
    validate_body_zone_definitions,
    validate_combat_state,
)
from textrpg.core import RuleError


class CombatTargetingTests(unittest.TestCase):
    def setUp(self):
        self.state = {
            "range_band": "reach",
            "relative_facing": "front",
            "relative_elevation": "level",
            "defender_posture": "standing",
            "state_tags": [],
            "blocked_zones": [],
        }
        self.spear = {
            "weapon_id": "WEAPON_TEST_SPEAR",
            "range_bands": ["close", "reach"],
            "targeting_tags": ["general", "piercing", "polearm"],
        }
        self.zones = {
            "ZONE_CHEST": {
                "name": "Chest",
                "allowed_facings": ["front", "left_flank", "right_flank"],
                "allowed_range_bands": ["close", "reach", "ranged"],
            },
            "ZONE_BACK": {
                "name": "Back",
                "allowed_facings": ["rear"],
                "allowed_range_bands": ["close", "reach", "ranged"],
            },
            "ZONE_HEAD": {
                "name": "Head",
                "allowed_facings": ["front", "left_flank", "right_flank"],
                "allowed_range_bands": ["close", "reach", "ranged"],
                "requires_any_state_tags": [
                    "head_reachable",
                    "defender_knocked_down",
                    "attacker_elevated",
                ],
                "weaknesses": ["internal_secret"],
                "on_hit_effects": [{"type": "hidden"}],
            },
            "ZONE_CORE": {
                "name": "Core",
                "allowed_facings": ["front"],
                "allowed_range_bands": ["close", "reach"],
                "requires_all_state_tags": ["core_exposed"],
                "required_weapon_tags": ["piercing"],
                "description": "An exposed crystalline core.",
            },
        }

    def test_reachable_zones_respect_facing_and_state_requirements(self):
        self.assertEqual(
            reachable_target_zone_ids(self.state, self.spear, self.zones),
            ["ZONE_CHEST"],
        )

    def test_battle_state_change_unlocks_previously_unreachable_head(self):
        changed = copy.deepcopy(self.state)
        changed["state_tags"].append("defender_knocked_down")
        self.assertEqual(
            reachable_target_zone_ids(changed, self.spear, self.zones),
            ["ZONE_CHEST", "ZONE_HEAD"],
        )

    def test_relative_facing_changes_available_zone(self):
        changed = copy.deepcopy(self.state)
        changed["relative_facing"] = "rear"
        self.assertEqual(
            reachable_target_zone_ids(changed, self.spear, self.zones),
            ["ZONE_BACK"],
        )

    def test_weapon_out_of_range_returns_no_targets(self):
        changed = copy.deepcopy(self.state)
        changed["range_band"] = "ranged"
        self.assertEqual(
            reachable_target_zone_ids(changed, self.spear, self.zones),
            [],
        )

    def test_environment_can_block_otherwise_reachable_zone(self):
        changed = copy.deepcopy(self.state)
        changed["blocked_zones"] = ["ZONE_CHEST"]
        self.assertEqual(
            reachable_target_zone_ids(changed, self.spear, self.zones),
            [],
        )

    def test_core_requires_both_exposure_and_suitable_weapon(self):
        changed = copy.deepcopy(self.state)
        changed["state_tags"] = ["core_exposed"]
        self.assertIn(
            "ZONE_CORE",
            reachable_target_zone_ids(changed, self.spear, self.zones),
        )
        hammer = {
            "weapon_id": "WEAPON_TEST_HAMMER",
            "range_bands": ["close", "reach"],
            "targeting_tags": ["general", "blunt"],
        }
        self.assertNotIn(
            "ZONE_CORE",
            reachable_target_zone_ids(changed, hammer, self.zones),
        )

    def test_player_view_excludes_unreachable_and_hidden_internal_metadata(self):
        changed = copy.deepcopy(self.state)
        changed["state_tags"] = ["defender_knocked_down", "core_exposed"]
        view = build_targeting_view(changed, self.spear, self.zones)

        ids = [entry["id"] for entry in view["target_zones"]]
        self.assertEqual(ids, ["ZONE_CHEST", "ZONE_HEAD", "ZONE_CORE"])
        serialized = repr(view)
        self.assertNotIn("weaknesses", serialized)
        self.assertNotIn("internal_secret", serialized)
        self.assertNotIn("on_hit_effects", serialized)

    def test_hidden_zone_is_not_exposed_by_player_view(self):
        zones = copy.deepcopy(self.zones)
        zones["ZONE_CHEST"]["player_visible"] = False
        self.assertIn(
            "ZONE_CHEST",
            reachable_target_zone_ids(self.state, self.spear, zones),
        )
        view = build_targeting_view(self.state, self.spear, zones)
        self.assertEqual(view["target_zones"], [])

    def test_debug_explanation_is_separate_from_player_view(self):
        result = explain_target_zone_access(
            self.state,
            self.spear,
            self.zones,
            "ZONE_HEAD",
        )
        self.assertEqual(
            result,
            {
                "zone_id": "ZONE_HEAD",
                "reachable": False,
                "blocked_reason": "missing_state_alternative",
            },
        )

    def test_invalid_state_or_zone_metadata_is_rejected(self):
        invalid_state = copy.deepcopy(self.state)
        invalid_state["range_band"] = "teleport"
        with self.assertRaises(RuleError):
            validate_combat_state(invalid_state)

        invalid_zones = copy.deepcopy(self.zones)
        invalid_zones["ZONE_CHEST"]["allowed_facings"] = ["front", "inside"]
        with self.assertRaises(RuleError):
            validate_body_zone_definitions(invalid_zones)

    def test_queries_are_non_mutating(self):
        before_state = copy.deepcopy(self.state)
        before_weapon = copy.deepcopy(self.spear)
        before_zones = copy.deepcopy(self.zones)
        reachable_target_zone_ids(self.state, self.spear, self.zones)
        build_targeting_view(self.state, self.spear, self.zones)
        self.assertEqual(self.state, before_state)
        self.assertEqual(self.spear, before_weapon)
        self.assertEqual(self.zones, before_zones)


if __name__ == "__main__":
    unittest.main()
