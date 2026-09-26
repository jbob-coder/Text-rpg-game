import unittest

from textrpg import GameState
from textrpg.simulation import apply_condition, advance_time, recover, train, train_attribute
from textrpg.stats import initialize_resources


class SimulationTests(unittest.TestCase):
    def state(self):
        state = GameState(
            seed="s",
            scene_id="A",
            player={
                "attributes": {
                    "might": 40,
                    "agility": 40,
                    "endurance": 50,
                    "intellect": 50,
                    "will": 50,
                    "perception": 40,
                    "presence": 40,
                },
                "skills": {"athletics": 20, "technical_systems": 10},
            },
        )
        initialize_resources(state, refill=True)
        return state

    def test_conditions_expire_with_time(self):
        state = self.state()
        apply_condition(state, "COND_BRUISED", duration_minutes=30)
        self.assertEqual(advance_time(state, 29), [])
        self.assertEqual(advance_time(state, 1), ["COND_BRUISED"])

    def test_training_consumes_resources_and_takes_time(self):
        state = self.state()
        before = state.player["skills"]["technical_systems"]
        event = train(state, skill="technical_systems", minutes=60)
        self.assertGreater(event["after"], before)
        self.assertEqual(state.time_minutes, 60)
        self.assertLess(state.player["resources"]["stamina"], state.player["resources"]["max_stamina"])

    def test_high_skill_has_diminishing_returns(self):
        low = self.state()
        high = self.state()
        high.player["skills"]["technical_systems"] = 90
        low_gain = train(low, skill="technical_systems", minutes=60)["gain"]
        high_gain = train(high, skill="technical_systems", minutes=60)["gain"]
        self.assertGreater(low_gain, high_gain)

    def test_attribute_training_is_slow(self):
        state = self.state()
        event = train_attribute(state, attribute="might", minutes=120)
        self.assertLess(event["gain"], 1)

    def test_recovery_is_bounded(self):
        state = self.state()
        state.player["resources"]["health"] = 1
        recover(state, 600, quality=2)
        self.assertLessEqual(
            state.player["resources"]["health"],
            state.player["resources"]["max_health"],
        )


if __name__ == "__main__":
    unittest.main()
