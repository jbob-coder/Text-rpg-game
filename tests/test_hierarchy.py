import copy
import unittest

from textrpg.core import RuleError
from textrpg.hierarchy import (
    apply_role_promotion,
    assign_region_controller,
    highest_eligible_role,
    role_eligibility,
    validate_role_definitions,
)


class BeastHierarchyTests(unittest.TestCase):
    def setUp(self):
        self.definitions = {
            "solitary": {"rank": 0},
            "pack_member": {"rank": 1, "requires_social_species": True},
            "veteran": {"rank": 2, "min_level": 4, "min_victories": 2},
            "guardian": {"rank": 3, "min_level": 5, "min_victories": 3},
            "chieftain": {
                "rank": 4, "requires_social_species": True, "min_intelligence": 3,
                "min_level": 6, "min_followers": 2, "min_victories": 4,
            },
            "commander": {
                "rank": 5, "requires_social_species": True, "min_intelligence": 4,
                "min_level": 8, "min_followers": 3, "min_victories": 6,
                "can_control_territory": True,
            },
            "territory_ruler": {
                "rank": 6, "requires_social_species": True, "min_intelligence": 4,
                "min_level": 10, "min_followers": 5, "min_victories": 10,
                "min_territories": 1, "can_control_territory": True,
            },
            "regional_apex": {
                "rank": 7, "min_level": 14, "min_victories": 15,
                "can_control_territory": True,
            },
        }
        self.species = {"social_species": True}
        self.beast = {
            "beast_id": "BEAST_COMMANDER", "species_id": "SPECIES_STONEFANG",
            "level": 8, "development_xp": 900.0, "intelligence": 4,
            "role": "chieftain", "alive": True, "encounter_memory": {},
            "adaptations": [], "followers": ["B1", "B2", "B3"],
        }
        self.region = {
            "region_id": "REGION_PASS", "beast_ids": ["BEAST_COMMANDER", "B1", "B2", "B3"],
            "carrying_capacity": 8, "resource_score": 0.8,
            "territory_controller": None, "last_simulated_minutes": 0,
        }

    def test_role_definitions_validate(self):
        validate_role_definitions(self.definitions)

    def test_high_level_alone_does_not_make_commander(self):
        beast = copy.deepcopy(self.beast)
        beast["level"] = 20
        beast["intelligence"] = 1
        result = role_eligibility(beast, self.species, "commander", self.definitions, victories=20)
        self.assertFalse(result["eligible"])
        self.assertIn("insufficient_intelligence", result["reasons"])

    def test_commander_requires_followers_and_victories(self):
        no_followers = copy.deepcopy(self.beast)
        no_followers["followers"] = []
        result = role_eligibility(no_followers, self.species, "commander", self.definitions, victories=10)
        self.assertIn("insufficient_followers", result["reasons"])
        result = role_eligibility(self.beast, self.species, "commander", self.definitions, victories=2)
        self.assertIn("insufficient_victories", result["reasons"])

    def test_non_social_species_cannot_take_social_command_role(self):
        result = role_eligibility(self.beast, {"social_species": False}, "commander", self.definitions, victories=10)
        self.assertFalse(result["eligible"])
        self.assertIn("species_not_social", result["reasons"])

    def test_highest_eligible_role_uses_all_requirements(self):
        result = highest_eligible_role(self.beast, self.species, self.definitions, victories=7)
        self.assertEqual(result["role_id"], "commander")

    def test_promotion_changes_role_only_when_eligible_and_higher_rank(self):
        result = apply_role_promotion(self.beast, self.species, self.definitions, "commander", victories=7)
        self.assertEqual(result["before_role"], "chieftain")
        self.assertEqual(self.beast["role"], "commander")
        with self.assertRaises(RuleError):
            apply_role_promotion(self.beast, self.species, self.definitions, "veteran", victories=7)

    def test_commander_can_become_region_controller_explicitly(self):
        apply_role_promotion(self.beast, self.species, self.definitions, "commander", victories=7)
        result = assign_region_controller(self.region, self.beast, self.definitions)
        self.assertEqual(result["new_controller"], "BEAST_COMMANDER")
        self.assertEqual(self.region["territory_controller"], "BEAST_COMMANDER")

    def test_non_controller_role_cannot_claim_region(self):
        with self.assertRaises(RuleError):
            assign_region_controller(self.region, self.beast, self.definitions)
        self.assertIsNone(self.region["territory_controller"])

    def test_controller_must_be_present_in_region(self):
        apply_role_promotion(self.beast, self.species, self.definitions, "commander", victories=7)
        region = copy.deepcopy(self.region)
        region["beast_ids"].remove("BEAST_COMMANDER")
        with self.assertRaises(RuleError):
            assign_region_controller(region, self.beast, self.definitions)

    def test_eligibility_query_is_non_mutating(self):
        before = copy.deepcopy(self.beast)
        role_eligibility(self.beast, self.species, "commander", self.definitions, victories=7)
        highest_eligible_role(self.beast, self.species, self.definitions, victories=7)
        self.assertEqual(self.beast, before)


if __name__ == "__main__":
    unittest.main()
