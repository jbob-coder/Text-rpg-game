import unittest

from textrpg import GameState, RuleError
from textrpg.simulation import apply_condition, advance_time, recover, train, train_attribute, validate_time_advance
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


    def test_invalid_condition_modifier_path_is_rejected(self):
        state = self.state()
        with self.assertRaises(RuleError) as context:
            apply_condition(
                state,
                "COND_BAD",
                modifiers={"skills.athletcs": -3},
            )
        self.assertIn("Invalid condition modifiers", str(context.exception))

    def test_attribute_training_intensity_is_bounded(self):
        state = self.state()
        with self.assertRaises(RuleError):
            train_attribute(state, attribute="might", minutes=120, intensity=0)
        with self.assertRaises(RuleError):
            train_attribute(state, attribute="might", minutes=120, intensity=2.1)

    def test_condition_temporal_and_metadata_contracts_are_strict(self):
        state = self.state()
        with self.assertRaises(RuleError):
            apply_condition(state, "", severity=1)
        with self.assertRaises(RuleError):
            apply_condition(state, "COND_BOOL", severity=True)
        with self.assertRaises(RuleError):
            apply_condition(state, "COND_NEG", duration_minutes=-1)
        with self.assertRaises(RuleError):
            apply_condition(state, "COND_TAG", tags="fatigue")

    def test_time_and_training_reject_boolean_or_non_finite_values(self):
        state = self.state()
        with self.assertRaises(RuleError):
            advance_time(state, True)
        with self.assertRaises(RuleError):
            recover(state, 60, quality=float("nan"))
        with self.assertRaises(RuleError):
            train(
                state,
                skill="athletics",
                minutes=60,
                intensity=float("inf"),
            )
        with self.assertRaises(RuleError):
            train_attribute(
                state,
                attribute="might",
                minutes=120,
                intensity=True,
            )

    def test_invalid_timed_condition_rejects_without_advancing_time(self):
        state = self.state()
        state.player["conditions"] = {
            "COND_CORRUPT": {
                "duration_minutes": True,
                "severity": 1,
                "source": "test",
                "tags": [],
                "modifiers": {},
            }
        }
        before_time = state.time_minutes
        with self.assertRaises(RuleError):
            validate_time_advance(state, 10)
        self.assertEqual(state.time_minutes, before_time)
        with self.assertRaises(RuleError):
            advance_time(state, 10)
        self.assertEqual(state.time_minutes, before_time)

    def test_training_preflights_time_before_mutating_resources_or_skill(self):
        state = self.state()
        state.player["conditions"] = {
            "COND_CORRUPT": {
                "duration_minutes": -1,
                "severity": 1,
                "source": "test",
                "tags": [],
                "modifiers": {},
            }
        }
        before_resources = dict(state.player["resources"])
        before_skill = state.player["skills"]["technical_systems"]
        before_time = state.time_minutes
        with self.assertRaises(RuleError):
            train(state, skill="technical_systems", minutes=60)
        self.assertEqual(state.player["resources"], before_resources)
        self.assertEqual(state.player["skills"]["technical_systems"], before_skill)
        self.assertEqual(state.time_minutes, before_time)

    def test_attribute_training_preflights_time_before_mutating_attribute(self):
        state = self.state()
        state.player["conditions"] = {"COND_BAD": "not-an-object"}
        before = state.player["attributes"]["might"]
        with self.assertRaises(RuleError):
            train_attribute(state, attribute="might", minutes=120)
        self.assertEqual(state.player["attributes"]["might"], before)
        self.assertEqual(state.time_minutes, 0)

    def test_training_rejects_corrupt_skill_before_resource_normalization(self):
        state = self.state()
        state.player["skills"]["technical_systems"] = float("nan")
        state.player["resources"].pop("max_health", None)
        before_resources = dict(state.player["resources"])
        with self.assertRaises(RuleError):
            train(state, skill="technical_systems", minutes=60)
        self.assertEqual(state.player["resources"], before_resources)
        self.assertTrue(
            str(state.player["skills"]["technical_systems"]) == "nan"
        )

    def test_attribute_training_rejects_corrupt_attribute_without_time_change(self):
        state = self.state()
        state.player["attributes"]["might"] = float("inf")
        before_time = state.time_minutes
        with self.assertRaises(RuleError):
            train_attribute(state, attribute="might", minutes=120)
        self.assertEqual(state.time_minutes, before_time)
        self.assertEqual(state.player["attributes"]["might"], float("inf"))

if __name__ == "__main__":
    unittest.main()
