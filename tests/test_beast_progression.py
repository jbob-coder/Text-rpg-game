import copy
import unittest

from textrpg.beast_progression import (
    apply_development_event,
    level_for_xp,
    preview_development_event,
    validate_development_rules,
    validate_level_thresholds,
)
from textrpg.core import RuleError


class BeastProgressionTests(unittest.TestCase):
    def setUp(self):
        self.thresholds = [0, 100, 250, 500, 900]
        self.rules = {
            "meaningful_hunt": {"base_xp": 80.0},
            "survive_hunter": {"base_xp": 150.0},
            "trivial_foraging": {"base_xp": 5.0, "enabled": False},
        }
        self.beast = {
            "beast_id": "BEAST_001",
            "species_id": "SPECIES_STONEFANG",
            "level": 2,
            "development_xp": 120.0,
            "intelligence": 2,
            "role": "veteran",
            "alive": True,
            "encounter_memory": {},
            "adaptations": [],
            "followers": [],
        }

    def test_thresholds_start_at_zero_and_increase(self):
        self.assertEqual(validate_level_thresholds(self.thresholds), [0.0, 100.0, 250.0, 500.0, 900.0])
        with self.assertRaises(RuleError):
            validate_level_thresholds([10, 100])
        with self.assertRaises(RuleError):
            validate_level_thresholds([0, 100, 100])

    def test_level_for_xp_uses_highest_reached_threshold(self):
        self.assertEqual(level_for_xp(0, self.thresholds), 1)
        self.assertEqual(level_for_xp(249.9, self.thresholds), 2)
        self.assertEqual(level_for_xp(250, self.thresholds), 3)
        self.assertEqual(level_for_xp(99999, self.thresholds), 5)

    def test_novelty_reduces_repeat_farming(self):
        fresh = preview_development_event(
            self.beast, event_type="meaningful_hunt", significance=1.0, novelty=1.0,
            rules=self.rules, level_thresholds=self.thresholds,
        )
        repeated = preview_development_event(
            self.beast, event_type="meaningful_hunt", significance=1.0, novelty=0.1,
            rules=self.rules, level_thresholds=self.thresholds,
        )
        self.assertEqual(fresh["xp_gain"], 80.0)
        self.assertEqual(repeated["xp_gain"], 8.0)

    def test_significance_scales_development(self):
        result = preview_development_event(
            self.beast, event_type="meaningful_hunt", significance=0.5, novelty=1.0,
            rules=self.rules, level_thresholds=self.thresholds,
        )
        self.assertEqual(result["xp_gain"], 40.0)

    def test_apply_can_level_beast(self):
        result = apply_development_event(
            self.beast, event_type="survive_hunter", significance=1.0, novelty=1.0,
            rules=self.rules, level_thresholds=self.thresholds,
        )
        self.assertEqual(result["after_xp"], 270.0)
        self.assertEqual(result["after_level"], 3)
        self.assertEqual(self.beast["level"], 3)
        self.assertEqual(self.beast["development_xp"], 270.0)

    def test_disabled_event_gives_no_progress(self):
        result = preview_development_event(
            self.beast, event_type="trivial_foraging", significance=1.0, novelty=1.0,
            rules=self.rules, level_thresholds=self.thresholds,
        )
        self.assertEqual(result["xp_gain"], 0.0)
        self.assertEqual(result["after_level"], 2)

    def test_level_xp_mismatch_is_rejected(self):
        invalid = copy.deepcopy(self.beast)
        invalid["level"] = 4
        with self.assertRaises(RuleError):
            preview_development_event(
                invalid, event_type="meaningful_hunt", significance=1.0, novelty=1.0,
                rules=self.rules, level_thresholds=self.thresholds,
            )

    def test_preview_is_non_mutating(self):
        before = copy.deepcopy(self.beast)
        preview_development_event(
            self.beast, event_type="meaningful_hunt", significance=1.0, novelty=1.0,
            rules=self.rules, level_thresholds=self.thresholds,
        )
        self.assertEqual(self.beast, before)

    def test_invalid_significance_or_novelty_is_rejected(self):
        for significance, novelty in ((1.1, 1.0), (1.0, -0.1), (True, 1.0)):
            with self.subTest(significance=significance, novelty=novelty):
                with self.assertRaises(RuleError):
                    preview_development_event(
                        self.beast, event_type="meaningful_hunt",
                        significance=significance, novelty=novelty,
                        rules=self.rules, level_thresholds=self.thresholds,
                    )

    def test_rules_reject_non_finite_xp(self):
        invalid = {"hunt": {"base_xp": float("nan")}}
        with self.assertRaises(RuleError):
            validate_development_rules(invalid)


if __name__ == "__main__":
    unittest.main()
