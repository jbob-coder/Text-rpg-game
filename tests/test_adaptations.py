import copy
import unittest

from textrpg.adaptations import (
    adaptation_player_view,
    apply_adaptation,
    eligible_adaptations,
    validate_adaptation_definitions,
)
from textrpg.beasts import record_encounter_observation
from textrpg.core import RuleError


class AdaptationApplicationTests(unittest.TestCase):
    def setUp(self):
        self.beast = {
            "beast_id": "BEAST_001",
            "species_id": "SPECIES_STONEFANG",
            "level": 5,
            "development_xp": 400.0,
            "intelligence": 3,
            "role": "veteran",
            "alive": True,
            "encounter_memory": {},
            "adaptations": [],
            "followers": [],
        }
        self.definitions = {
            "ADAPT_GUARD_RIGHT_FORELEG": {
                "name": "Guarded Right Foreleg",
                "observation_kind": "target_zone",
                "observation_value": "ZONE_RIGHT_FORELEG",
                "adaptation_type": "behavioral",
                "granted_tags": ["protect_right_foreleg"],
                "priority": 10,
                "player_visible": True,
            },
            "ADAPT_AVOID_REACH": {
                "name": "Reach-Aware Footwork",
                "observation_kind": "range_band",
                "observation_value": "reach",
                "adaptation_type": "tactical",
                "granted_tags": ["avoid_reach_band"],
                "priority": 20,
                "player_visible": False,
            },
        }

    def _observe_foreleg(self):
        for minute in (100, 120):
            record_encounter_observation(
                self.beast, kind="target_zone", value="ZONE_RIGHT_FORELEG",
                time_minutes=minute, confidence_increment=0.5,
            )

    def test_definition_validation_uses_known_observation_and_adaptation_vocab(self):
        validate_adaptation_definitions(self.definitions)
        invalid = copy.deepcopy(self.definitions)
        invalid["BAD"] = {
            "observation_kind": "telepathy",
            "observation_value": "x",
            "adaptation_type": "behavioral",
        }
        with self.assertRaises(RuleError):
            validate_adaptation_definitions(invalid)

    def test_no_observation_means_no_eligible_adaptation(self):
        self.assertEqual(eligible_adaptations(self.beast, self.definitions), [])

    def test_repeated_observation_unlocks_behavioral_adaptation(self):
        self._observe_foreleg()
        eligible = eligible_adaptations(self.beast, self.definitions)
        self.assertEqual([entry["adaptation_id"] for entry in eligible], ["ADAPT_GUARD_RIGHT_FORELEG"])

    def test_apply_adaptation_persists_id_and_tags(self):
        self._observe_foreleg()
        result = apply_adaptation(self.beast, self.definitions, "ADAPT_GUARD_RIGHT_FORELEG")
        self.assertEqual(result["granted_tags"], ["protect_right_foreleg"])
        self.assertIn("ADAPT_GUARD_RIGHT_FORELEG", self.beast["adaptations"])
        self.assertIn("protect_right_foreleg", self.beast["adaptation_tags"])

    def test_not_ready_adaptation_cannot_be_forced(self):
        with self.assertRaises(RuleError):
            apply_adaptation(self.beast, self.definitions, "ADAPT_GUARD_RIGHT_FORELEG")
        self.assertEqual(self.beast["adaptations"], [])

    def test_same_adaptation_cannot_apply_twice(self):
        self._observe_foreleg()
        apply_adaptation(self.beast, self.definitions, "ADAPT_GUARD_RIGHT_FORELEG")
        with self.assertRaises(RuleError):
            apply_adaptation(self.beast, self.definitions, "ADAPT_GUARD_RIGHT_FORELEG")

    def test_hidden_adaptation_is_not_in_player_view(self):
        self.beast["adaptations"] = ["ADAPT_GUARD_RIGHT_FORELEG", "ADAPT_AVOID_REACH"]
        view = adaptation_player_view(self.beast, self.definitions)
        self.assertEqual(view, [{"id": "ADAPT_GUARD_RIGHT_FORELEG", "name": "Guarded Right Foreleg", "type": "behavioral"}])

    def test_eligibility_query_does_not_mutate_beast(self):
        self._observe_foreleg()
        before = copy.deepcopy(self.beast)
        eligible_adaptations(self.beast, self.definitions)
        self.assertEqual(self.beast, before)


if __name__ == "__main__":
    unittest.main()
