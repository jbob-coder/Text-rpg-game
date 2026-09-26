import unittest

from textrpg import GameState
from textrpg.stats import derived_stat_breakdown, derived_stats, initialize_resources, validate_player_stats


class StatsTests(unittest.TestCase):
    def state(self):
        return GameState(
            seed="s",
            scene_id="A",
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
                "skills": {"athletics": 20, "defense": 10, "ranged": 25, "leadership": 15},
            },
        )

    def test_derived_stats(self):
        values = derived_stats(self.state())
        self.assertEqual(values["max_health"], 185.0)
        self.assertEqual(values["max_focus"], 107.0)

    def test_resource_init(self):
        state = self.state()
        initialize_resources(state, refill=True)
        self.assertEqual(state.player["resources"]["health"], 185.0)

    def test_unknown_stat_is_reported(self):
        state = self.state()
        state.player["attributes"]["magic_number"] = 4
        self.assertTrue(any("unknown attribute" in e for e in validate_player_stats(state)))

    def test_capacity_derived_values_are_floored_at_zero(self):
        state = self.state()
        state.perks["PERK_COLLAPSE"] = {
            "modifiers": {
                "derived.max_health": -1000,
                "derived.carry_capacity": -1000,
            }
        }
        values = derived_stats(state)
        self.assertEqual(values["max_health"], 0.0)
        self.assertEqual(values["carry_capacity"], 0.0)

        state.player["resources"] = {"health": 20}
        initialize_resources(state)
        self.assertEqual(state.player["resources"]["max_health"], 0.0)
        self.assertEqual(state.player["resources"]["health"], 0.0)

    def test_derived_breakdown_exposes_floor_adjustment(self):
        state = self.state()
        state.perks["PERK_COLLAPSE"] = {
            "modifiers": {"derived.max_health": -1000}
        }
        breakdown = derived_stat_breakdown(state, "max_health")
        self.assertLess(breakdown["raw_total"], 0.0)
        self.assertEqual(breakdown["floor"], 0.0)
        self.assertGreater(breakdown["floor_adjustment"], 0.0)
        self.assertEqual(breakdown["total"], 0.0)

    def test_contest_style_derived_values_can_go_negative(self):
        state = self.state()
        state.perks["PERK_STAGGERED"] = {
            "modifiers": {"derived.initiative": -1000}
        }
        self.assertLess(derived_stats(state)["initiative"], 0.0)


if __name__ == "__main__":
    unittest.main()
