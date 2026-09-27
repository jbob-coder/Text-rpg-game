import copy
import unittest

from textrpg.core import RuleError
from textrpg.wounds import (
    aggregate_body_impairments,
    apply_zone_damage,
    consequence_state_for_integrity,
    crystal_harvest_damage_from_zone_hit,
    validate_body_runtime_state,
    validate_wound_profiles,
)


class WoundContractTests(unittest.TestCase):
    def setUp(self):
        self.profiles = {
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
            "ZONE_RIGHT_EYE": {
                "thresholds": [
                    {
                        "integrity_lte": 0.5,
                        "tags": ["right_eye_impaired"],
                        "disabled_actions": [],
                    },
                    {
                        "integrity_lte": 0.0,
                        "tags": ["right_eye_destroyed"],
                        "disabled_actions": ["depth_precision_bite"],
                    },
                ],
                "crystal_damage_multiplier": 0.0,
            },
            "ZONE_CORE": {
                "thresholds": [
                    {
                        "integrity_lte": 0.6,
                        "tags": ["core_damaged"],
                        "disabled_actions": [],
                    },
                    {
                        "integrity_lte": 0.2,
                        "tags": ["core_critical"],
                        "disabled_actions": ["crystal_burst"],
                    },
                ],
                "crystal_damage_multiplier": 0.8,
            },
        }
        self.body = {
            "ZONE_RIGHT_FORELEG": {
                "integrity": 1.0,
                "tags": [],
                "disabled_actions": [],
            },
            "ZONE_RIGHT_EYE": {
                "integrity": 1.0,
                "tags": [],
                "disabled_actions": [],
            },
            "ZONE_CORE": {
                "integrity": 1.0,
                "tags": [],
                "disabled_actions": [],
            },
        }

    def test_valid_profiles_and_body_state(self):
        validate_wound_profiles(self.profiles)
        validate_body_runtime_state(self.body)

    def test_thresholds_must_be_descending(self):
        invalid = copy.deepcopy(self.profiles)
        invalid["ZONE_RIGHT_FORELEG"]["thresholds"] = [
            {"integrity_lte": 0.3},
            {"integrity_lte": 0.8},
        ]
        with self.assertRaises(RuleError):
            validate_wound_profiles(invalid)

    def test_consequence_state_accumulates_reached_thresholds(self):
        result = consequence_state_for_integrity(
            "ZONE_RIGHT_FORELEG",
            0.30,
            self.profiles,
        )
        self.assertIn("foreleg_wounded", result["tags"])
        self.assertIn("foreleg_crippled", result["tags"])
        self.assertIn("heavy_charge", result["disabled_actions"])

    def test_apply_damage_updates_only_target_zone(self):
        before_eye = copy.deepcopy(self.body["ZONE_RIGHT_EYE"])
        event = apply_zone_damage(
            self.body,
            zone_id="ZONE_RIGHT_FORELEG",
            damage_fraction=0.30,
            profiles=self.profiles,
        )
        self.assertEqual(event["after_integrity"], 0.7)
        self.assertIn("foreleg_wounded", event["tags"])
        self.assertEqual(self.body["ZONE_RIGHT_EYE"], before_eye)

    def test_repeated_damage_can_disable_action(self):
        apply_zone_damage(
            self.body,
            zone_id="ZONE_RIGHT_FORELEG",
            damage_fraction=0.40,
            profiles=self.profiles,
        )
        event = apply_zone_damage(
            self.body,
            zone_id="ZONE_RIGHT_FORELEG",
            damage_fraction=0.30,
            profiles=self.profiles,
        )
        self.assertEqual(event["after_integrity"], 0.3)
        self.assertIn("heavy_charge", event["disabled_actions"])

    def test_aggregate_impairments_deduplicates(self):
        self.body["ZONE_RIGHT_FORELEG"]["tags"] = ["slowed", "wounded"]
        self.body["ZONE_RIGHT_EYE"]["tags"] = ["wounded", "vision_loss"]
        self.body["ZONE_RIGHT_FORELEG"]["disabled_actions"] = ["charge"]
        self.body["ZONE_RIGHT_EYE"]["disabled_actions"] = ["charge", "aimed_bite"]
        result = aggregate_body_impairments(self.body)
        self.assertEqual(result["tags"], ["slowed", "wounded", "vision_loss"])
        self.assertEqual(
            result["disabled_actions"],
            ["charge", "aimed_bite"],
        )

    def test_core_hit_translates_to_crystal_harvest_damage(self):
        damage = crystal_harvest_damage_from_zone_hit(
            zone_id="ZONE_CORE",
            damage_fraction=0.5,
            profiles=self.profiles,
        )
        self.assertEqual(damage, 0.4)

    def test_non_core_hit_does_not_damage_crystal_when_multiplier_zero(self):
        damage = crystal_harvest_damage_from_zone_hit(
            zone_id="ZONE_RIGHT_FORELEG",
            damage_fraction=0.8,
            profiles=self.profiles,
        )
        self.assertEqual(damage, 0.0)

    def test_harvest_damage_is_capped(self):
        profiles = copy.deepcopy(self.profiles)
        profiles["ZONE_CORE"]["crystal_damage_multiplier"] = 2.0
        damage = crystal_harvest_damage_from_zone_hit(
            zone_id="ZONE_CORE",
            damage_fraction=0.8,
            profiles=profiles,
        )
        self.assertEqual(damage, 1.0)

    def test_unknown_runtime_zone_is_rejected(self):
        with self.assertRaises(RuleError):
            apply_zone_damage(
                self.body,
                zone_id="ZONE_LEFT_WING",
                damage_fraction=0.2,
                profiles=self.profiles,
            )

    def test_invalid_damage_does_not_mutate_state(self):
        before = copy.deepcopy(self.body)
        with self.assertRaises(RuleError):
            apply_zone_damage(
                self.body,
                zone_id="ZONE_CORE",
                damage_fraction=1.5,
                profiles=self.profiles,
            )
        self.assertEqual(self.body, before)

    def test_query_functions_do_not_mutate_inputs(self):
        profiles_before = copy.deepcopy(self.profiles)
        body_before = copy.deepcopy(self.body)
        consequence_state_for_integrity("ZONE_CORE", 0.5, self.profiles)
        aggregate_body_impairments(self.body)
        crystal_harvest_damage_from_zone_hit(
            zone_id="ZONE_CORE",
            damage_fraction=0.5,
            profiles=self.profiles,
        )
        self.assertEqual(self.profiles, profiles_before)
        self.assertEqual(self.body, body_before)


if __name__ == "__main__":
    unittest.main()
