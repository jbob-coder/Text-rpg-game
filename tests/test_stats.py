import unittest

from textrpg import GameState
from textrpg.stats import derived_stats, initialize_resources, validate_player_stats


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


if __name__ == "__main__":
    unittest.main()
