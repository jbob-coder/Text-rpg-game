import copy
import unittest

from textrpg.beasts import (
    adaptation_readiness,
    command_eligibility,
    communication_tier,
    encounter_memory_capacity,
    record_encounter_observation,
    validate_beast_state,
)
from textrpg.core import RuleError


class BeastMemoryAndAdaptationTests(unittest.TestCase):
    def setUp(self):
        self.beast = {
            "beast_id": "BEAST_001",
            "species_id": "SPECIES_STONEFANG",
            "level": 8,
            "development_xp": 125.0,
            "intelligence": 3,
            "role": "veteran",
            "alive": True,
            "encounter_memory": {},
            "adaptations": [],
            "followers": ["BEAST_002", "BEAST_003"],
        }

    def test_valid_beast_state(self):
        validate_beast_state(self.beast)

    def test_invalid_intelligence_is_rejected(self):
        beast = copy.deepcopy(self.beast)
        beast["intelligence"] = 6
        with self.assertRaises(RuleError):
            validate_beast_state(beast)

    def test_memory_capacity_scales_with_intelligence(self):
        low = copy.deepcopy(self.beast)
        low["intelligence"] = 0
        high = copy.deepcopy(self.beast)
        high["intelligence"] = 5
        self.assertEqual(encounter_memory_capacity(low), 4)
        self.assertEqual(encounter_memory_capacity(high), 24)

    def test_recording_observation_increases_count_and_confidence(self):
        first = record_encounter_observation(
            self.beast,
            kind="weapon_family",
            value="spear",
            time_minutes=100,
            confidence_increment=0.25,
        )
        second = record_encounter_observation(
            self.beast,
            kind="weapon_family",
            value="spear",
            time_minutes=130,
            confidence_increment=0.25,
        )
        self.assertEqual(first["observations"], 1)
        self.assertEqual(second["observations"], 2)
        self.assertGreater(second["confidence"], first["confidence"])
        self.assertEqual(second["last_seen"], 130)

    def test_memory_does_not_invent_unobserved_player_behavior(self):
        result = adaptation_readiness(
            self.beast,
            kind="target_zone",
            value="right_foreleg",
            adaptation_type="behavioral",
        )
        self.assertFalse(result["ready"])
        self.assertIn("no_observation", result["reasons"])

    def test_behavioral_adaptation_requires_repeated_observation(self):
        record_encounter_observation(
            self.beast,
            kind="target_zone",
            value="right_foreleg",
            time_minutes=100,
            confidence_increment=0.5,
        )
        first = adaptation_readiness(
            self.beast,
            kind="target_zone",
            value="right_foreleg",
            adaptation_type="behavioral",
        )
        self.assertFalse(first["ready"])
        self.assertIn("insufficient_observations", first["reasons"])

        record_encounter_observation(
            self.beast,
            kind="target_zone",
            value="right_foreleg",
            time_minutes=120,
            confidence_increment=0.5,
        )
        second = adaptation_readiness(
            self.beast,
            kind="target_zone",
            value="right_foreleg",
            adaptation_type="behavioral",
        )
        self.assertTrue(second["ready"])

    def test_tactical_adaptation_is_intelligence_gated(self):
        beast = copy.deepcopy(self.beast)
        beast["intelligence"] = 1
        for minute in (100, 110, 120, 130):
            record_encounter_observation(
                beast,
                kind="range_band",
                value="reach",
                time_minutes=minute,
                confidence_increment=1.0,
            )
        result = adaptation_readiness(
            beast,
            kind="range_band",
            value="reach",
            adaptation_type="tactical",
        )
        self.assertFalse(result["ready"])
        self.assertIn("insufficient_intelligence", result["reasons"])

    def test_biological_adaptation_requires_time_and_resources(self):
        beast = copy.deepcopy(self.beast)
        for minute in (100, 200, 300, 400):
            record_encounter_observation(
                beast,
                kind="target_zone",
                value="left_shoulder",
                time_minutes=minute,
                confidence_increment=1.0,
            )
        early = adaptation_readiness(
            beast,
            kind="target_zone",
            value="left_shoulder",
            adaptation_type="biological",
            elapsed_minutes=1000,
            resource_score=1.0,
        )
        self.assertFalse(early["ready"])
        self.assertIn("insufficient_time", early["reasons"])

        starved = adaptation_readiness(
            beast,
            kind="target_zone",
            value="left_shoulder",
            adaptation_type="biological",
            elapsed_minutes=10080,
            resource_score=0.2,
        )
        self.assertFalse(starved["ready"])
        self.assertIn("insufficient_resources", starved["reasons"])

        ready = adaptation_readiness(
            beast,
            kind="target_zone",
            value="left_shoulder",
            adaptation_type="biological",
            elapsed_minutes=10080,
            resource_score=0.8,
        )
        self.assertTrue(ready["ready"])

    def test_communication_tier_is_limited_by_species_and_intelligence(self):
        species = {"max_communication_tier": 2}
        self.assertEqual(communication_tier(self.beast, species), 2)
        species["max_communication_tier"] = 5
        self.assertEqual(communication_tier(self.beast, species), 3)

    def test_command_eligibility_uses_authored_requirements(self):
        species = {
            "social_species": True,
            "command_requirements": {
                "min_intelligence": 3,
                "min_level": 8,
                "min_followers": 2,
            },
        }
        result = command_eligibility(self.beast, species)
        self.assertTrue(result["eligible"])

        weaker = copy.deepcopy(self.beast)
        weaker["intelligence"] = 2
        weaker_result = command_eligibility(weaker, species)
        self.assertFalse(weaker_result["eligible"])
        self.assertIn("insufficient_intelligence", weaker_result["reasons"])

    def test_command_requires_social_species(self):
        species = {
            "social_species": False,
            "command_requirements": {
                "min_intelligence": 1,
                "min_level": 1,
                "min_followers": 0,
            },
        }
        result = command_eligibility(self.beast, species)
        self.assertFalse(result["eligible"])
        self.assertIn("species_not_social", result["reasons"])

    def test_readiness_and_capability_queries_do_not_mutate(self):
        beast_before = copy.deepcopy(self.beast)
        species = {
            "social_species": True,
            "max_communication_tier": 5,
            "command_requirements": {
                "min_intelligence": 3,
                "min_level": 1,
                "min_followers": 0,
            },
        }
        adaptation_readiness(
            self.beast,
            kind="retreat",
            value="player_retreated",
            adaptation_type="behavioral",
        )
        communication_tier(self.beast, species)
        command_eligibility(self.beast, species)
        self.assertEqual(self.beast, beast_before)

    def test_memory_capacity_evicts_lowest_confidence_old_memory(self):
        beast = copy.deepcopy(self.beast)
        beast["intelligence"] = 0
        for index in range(4):
            record_encounter_observation(
                beast,
                kind="terrain",
                value=f"terrain_{index}",
                time_minutes=index,
                confidence_increment=0.1,
            )

        record_encounter_observation(
            beast,
            kind="weapon_family",
            value="sword",
            time_minutes=100,
            confidence_increment=1.0,
        )

        self.assertEqual(len(beast["encounter_memory"]), 4)
        self.assertIn("weapon_family:sword", beast["encounter_memory"])
        self.assertNotIn("terrain:terrain_0", beast["encounter_memory"])

    def test_unknown_observation_kind_is_rejected(self):
        with self.assertRaises(RuleError):
            record_encounter_observation(
                self.beast,
                kind="mind_reading",
                value="anything",
                time_minutes=0,
            )


if __name__ == "__main__":
    unittest.main()
