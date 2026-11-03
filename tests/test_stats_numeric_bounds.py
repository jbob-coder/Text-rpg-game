"""Overflow regression checks for authoritative player statistics and resources."""

import unittest

from textrpg import GameState, RuleError
from textrpg.stats import derived_stat_breakdown, initialize_resources, validate_player_stats


def state():
    return GameState(
        seed="stats-boundary-test",
        scene_id="SCENE_TEST",
        player={
            "attributes": {
                "might": 40,
                "agility": 50,
                "endurance": 60,
                "intellect": 70,
                "will": 30,
                "perception": 45,
                "presence": 35,
            },
            "skills": {"athletics": 20},
        },
    )


class StatsNumericBoundsTests(unittest.TestCase):
    def test_very_large_integer_attributes_report_errors_without_overflow(self):
        character = state()
        character.player["attributes"]["might"] = 10 ** 400
        character.player["skills"]["athletics"] = -(10 ** 400)
        errors = validate_player_stats(character)
        self.assertTrue(any("attribute might must be finite numeric" in e for e in errors))
        self.assertTrue(any("skill athletics must be finite numeric" in e for e in errors))

    def test_invalid_current_resource_is_rejected_without_partial_mutation(self):
        character = state()
        character.player["resources"] = {"focus": 10 ** 400, "health": 50.0}
        before = dict(character.player["resources"])
        with self.assertRaisesRegex(RuleError, "Current resource must be a finite number: focus"):
            initialize_resources(character)
        self.assertEqual(character.player["resources"], before)

    def test_derived_formula_rejects_infinite_single_contribution(self):
        character = state()
        character.player["attributes"]["endurance"] = 1e308
        with self.assertRaisesRegex(RuleError, "Non-finite contribution for derived.max_health"):
            derived_stat_breakdown(character, "max_health")

    def test_derived_formula_rejects_infinite_combined_total(self):
        character = state()
        character.player["attributes"]["endurance"] = 5e307
        character.perks["PERK_LARGE"] = {"modifiers": {"derived.max_health": 1e308}}
        with self.assertRaisesRegex(RuleError, "Non-finite total for derived.max_health"):
            derived_stat_breakdown(character, "max_health")

    def test_normal_stat_computation_and_resource_initialization_unchanged(self):
        character = state()
        self.assertEqual(derived_stat_breakdown(character, "max_health")["total"], 185.0)
        maxima = initialize_resources(character, refill=True)
        self.assertEqual(maxima["health"], 185.0)
        self.assertEqual(character.player["resources"]["health"], 185.0)


if __name__ == "__main__":
    unittest.main()
