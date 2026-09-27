import copy
import unittest

from textrpg.core import RuleError
from textrpg.territory import (
    carrying_pressure,
    conflict_score,
    region_simulation_steps,
    resolve_beast_conflict,
    validate_ecology_rules,
    validate_region_state,
)


class TerritoryEcologyTests(unittest.TestCase):
    def setUp(self):
        self.region = {
            "region_id": "REGION_STONE_PASS",
            "beast_ids": ["BEAST_A", "BEAST_B"],
            "carrying_capacity": 4,
            "resource_score": 0.7,
            "territory_controller": None,
            "last_simulated_minutes": 1000,
        }
        self.a = {
            "beast_id": "BEAST_A", "species_id": "SPECIES_WOLF", "level": 8,
            "development_xp": 500.0, "intelligence": 1, "role": "veteran",
            "alive": True, "encounter_memory": {}, "adaptations": [], "followers": [],
        }
        self.b = {
            "beast_id": "BEAST_B", "species_id": "SPECIES_STONEFANG", "level": 6,
            "development_xp": 350.0, "intelligence": 4, "role": "commander",
            "alive": True, "encounter_memory": {}, "adaptations": [],
            "followers": ["BEAST_C", "BEAST_D"],
        }
        self.profile_a = {
            "combat_power": 55.0, "terrain_affinity": 0.5, "morale": 0.8,
            "resource_score": 0.7, "injury_burden": 0.0, "exhaustion": 0.0,
        }
        self.profile_b = {
            "combat_power": 50.0, "terrain_affinity": 0.8, "morale": 0.9,
            "resource_score": 0.8, "injury_burden": 0.0, "exhaustion": 0.0,
        }
        self.rules = {
            "weights": {
                "level": 3.0,
                "combat_power": 1.0,
                "intelligence": 2.0,
                "followers": 2.0,
                "terrain_affinity": 10.0,
                "morale": 5.0,
                "resource_score": 5.0,
                "injury_penalty": 25.0,
                "exhaustion_penalty": 20.0,
            },
            "deterministic_variance": 1.5,
        }

    def test_region_and_rules_validate(self):
        validate_region_state(self.region)
        validate_ecology_rules(self.rules)

    def test_region_simulation_is_cadence_based(self):
        self.assertEqual(region_simulation_steps(self.region, now_minutes=1059, cadence_minutes=60), 0)
        self.assertEqual(region_simulation_steps(self.region, now_minutes=1120, cadence_minutes=60), 2)

    def test_carrying_pressure_reflects_population_capacity(self):
        self.assertEqual(carrying_pressure(self.region), 0.5)
        crowded = copy.deepcopy(self.region)
        crowded["beast_ids"] = [f"B{i}" for i in range(8)]
        self.assertEqual(carrying_pressure(crowded), 2.0)

    def test_conflict_is_deterministic_for_same_seed_state_and_time(self):
        first = resolve_beast_conflict(
            seed="WORLD_SEED", time_minutes=1200, region=self.region,
            beast_a=self.a, profile_a=self.profile_a, beast_b=self.b, profile_b=self.profile_b,
            rules=self.rules,
        )
        second = resolve_beast_conflict(
            seed="WORLD_SEED", time_minutes=1200, region=self.region,
            beast_a=self.a, profile_a=self.profile_a, beast_b=self.b, profile_b=self.profile_b,
            rules=self.rules,
        )
        self.assertEqual(first, second)

    def test_level_is_not_the_only_power_input(self):
        result = resolve_beast_conflict(
            seed="WORLD_SEED", time_minutes=1200, region=self.region,
            beast_a=self.a, profile_a=self.profile_a, beast_b=self.b, profile_b=self.profile_b,
            rules=self.rules,
        )
        self.assertEqual(result["winner_id"], "BEAST_B")
        self.assertGreater(self.a["level"], self.b["level"])

    def test_injuries_can_reverse_otherwise_strong_beast(self):
        healthy = conflict_score(self.b, self.profile_b, self.region, self.rules)["base_score"]
        injured_profile = copy.deepcopy(self.profile_b)
        injured_profile["injury_burden"] = 1.0
        injured = conflict_score(self.b, injured_profile, self.region, self.rules)["base_score"]
        self.assertLess(injured, healthy)

    def test_intelligence_and_followers_have_separate_contributions(self):
        score = conflict_score(self.b, self.profile_b, self.region, self.rules)
        self.assertEqual(score["contributions"]["intelligence"], 8.0)
        self.assertEqual(score["contributions"]["followers"], 4.0)

    def test_rules_require_complete_explicit_weights(self):
        invalid = copy.deepcopy(self.rules)
        del invalid["weights"]["intelligence"]
        with self.assertRaises(RuleError):
            validate_ecology_rules(invalid)

    def test_conflict_does_not_mutate_region_or_beasts(self):
        region_before = copy.deepcopy(self.region)
        a_before = copy.deepcopy(self.a)
        b_before = copy.deepcopy(self.b)
        resolve_beast_conflict(
            seed="WORLD_SEED", time_minutes=1200, region=self.region,
            beast_a=self.a, profile_a=self.profile_a, beast_b=self.b, profile_b=self.profile_b,
            rules=self.rules,
        )
        self.assertEqual(self.region, region_before)
        self.assertEqual(self.a, a_before)
        self.assertEqual(self.b, b_before)

    def test_duplicate_region_beasts_are_rejected(self):
        invalid = copy.deepcopy(self.region)
        invalid["beast_ids"] = ["BEAST_A", "BEAST_A"]
        with self.assertRaises(RuleError):
            validate_region_state(invalid)


if __name__ == "__main__":
    unittest.main()
