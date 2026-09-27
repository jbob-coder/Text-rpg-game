import copy
import unittest

from textrpg.beasts import record_encounter_observation
from textrpg.core import RuleError
from textrpg.voice import eligible_barks, select_beast_bark, validate_voice_definitions


class BeastVoiceTests(unittest.TestCase):
    def setUp(self):
        self.beast = {
            "beast_id": "BEAST_001",
            "species_id": "SPECIES_STONEFANG",
            "level": 8,
            "development_xp": 125.0,
            "intelligence": 4,
            "role": "commander",
            "alive": True,
            "encounter_memory": {},
            "adaptations": [],
            "adaptation_tags": [],
            "followers": ["BEAST_002"],
        }
        self.species = {
            "max_communication_tier": 4,
        }
        self.definitions = {
            "BARK_GROWL": {
                "text": "A low warning growl.",
                "min_tier": 0,
                "max_tier": 5,
                "contexts": ["encounter"],
                "priority": 1,
            },
            "BARK_COMMAND_HOLD": {
                "text": "Hold the line.",
                "min_tier": 4,
                "max_tier": 5,
                "contexts": ["encounter"],
                "roles": ["commander", "territory_ruler", "regional_apex"],
                "priority": 20,
            },
            "BARK_REMEMBER_SPEAR": {
                "text": "The long fang again.",
                "min_tier": 3,
                "max_tier": 5,
                "contexts": ["encounter"],
                "memory_requirement": {"kind": "weapon_family", "value": "spear"},
                "priority": 30,
            },
            "BARK_PROTECT_LEG": {
                "text": "Guard the wounded side.",
                "min_tier": 3,
                "max_tier": 5,
                "contexts": ["encounter"],
                "required_adaptation_tags": ["protect_right_foreleg"],
                "priority": 40,
            },
        }

    def test_voice_definitions_validate(self):
        validate_voice_definitions(self.definitions)

    def test_species_cap_limits_intelligence_expression(self):
        species = {"max_communication_tier": 2}
        candidates = eligible_barks(self.beast, species, self.definitions, context="encounter")
        self.assertEqual([item["bark_id"] for item in candidates], ["BARK_GROWL"])

    def test_commander_line_requires_role_and_tier(self):
        selected = select_beast_bark(self.beast, self.species, self.definitions, context="encounter")
        self.assertEqual(selected["bark_id"], "BARK_COMMAND_HOLD")
        low = copy.deepcopy(self.beast)
        low["intelligence"] = 2
        self.assertEqual(
            select_beast_bark(low, self.species, self.definitions, context="encounter")["bark_id"],
            "BARK_GROWL",
        )

    def test_memory_line_appears_only_after_observation(self):
        before = [item["bark_id"] for item in eligible_barks(self.beast, self.species, self.definitions, context="encounter")]
        self.assertNotIn("BARK_REMEMBER_SPEAR", before)
        record_encounter_observation(
            self.beast, kind="weapon_family", value="spear", time_minutes=100,
            confidence_increment=0.5,
        )
        after = [item["bark_id"] for item in eligible_barks(self.beast, self.species, self.definitions, context="encounter")]
        self.assertIn("BARK_REMEMBER_SPEAR", after)
        self.assertEqual(after[0], "BARK_REMEMBER_SPEAR")

    def test_adaptation_line_requires_adaptation_tag(self):
        before = [item["bark_id"] for item in eligible_barks(self.beast, self.species, self.definitions, context="encounter")]
        self.assertNotIn("BARK_PROTECT_LEG", before)
        self.beast["adaptation_tags"] = ["protect_right_foreleg"]
        selected = select_beast_bark(self.beast, self.species, self.definitions, context="encounter")
        self.assertEqual(selected["bark_id"], "BARK_PROTECT_LEG")

    def test_context_filters_lines(self):
        self.assertIsNone(select_beast_bark(self.beast, self.species, self.definitions, context="sleeping"))

    def test_selection_is_deterministic_priority_then_id(self):
        definitions = copy.deepcopy(self.definitions)
        definitions["BARK_A"] = {
            "text": "A",
            "min_tier": 0,
            "max_tier": 5,
            "contexts": ["encounter"],
            "priority": 50,
        }
        definitions["BARK_B"] = {
            "text": "B",
            "min_tier": 0,
            "max_tier": 5,
            "contexts": ["encounter"],
            "priority": 50,
        }
        self.assertEqual(
            select_beast_bark(self.beast, self.species, definitions, context="encounter")["bark_id"],
            "BARK_A",
        )

    def test_invalid_tier_or_role_is_rejected(self):
        bad_tier = copy.deepcopy(self.definitions)
        bad_tier["BARK_GROWL"]["min_tier"] = 6
        with self.assertRaises(RuleError):
            validate_voice_definitions(bad_tier)
        bad_role = copy.deepcopy(self.definitions)
        bad_role["BARK_COMMAND_HOLD"]["roles"] = ["emperor_of_space"]
        with self.assertRaises(RuleError):
            validate_voice_definitions(bad_role)

    def test_queries_do_not_mutate_beast(self):
        before = copy.deepcopy(self.beast)
        eligible_barks(self.beast, self.species, self.definitions, context="encounter")
        select_beast_bark(self.beast, self.species, self.definitions, context="encounter")
        self.assertEqual(self.beast, before)


if __name__ == "__main__":
    unittest.main()
