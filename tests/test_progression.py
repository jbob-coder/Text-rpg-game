import unittest

from textrpg import GameState, RuleError, gain_ability_mastery, mastery_stage, technique_available


class ProgressionTests(unittest.TestCase):
    def test_mastery_stage_thresholds(self):
        self.assertEqual(mastery_stage(0), "discovered")
        self.assertEqual(mastery_stage(70), "learned")
        self.assertEqual(mastery_stage(400), "mastered")

    def test_ability_rank_requires_accumulated_mastery(self):
        s = GameState(seed="x", scene_id="A")
        gain_ability_mastery(s, "ABILITY_EXAMPLE", 99)
        self.assertEqual(s.abilities["ABILITY_EXAMPLE"]["rank"], 0)
        gain_ability_mastery(s, "ABILITY_EXAMPLE", 1)
        self.assertEqual(s.abilities["ABILITY_EXAMPLE"]["rank"], 1)

    def test_technique_can_require_knowledge_and_perk(self):
        s = GameState(seed="x", scene_id="A")
        gain_ability_mastery(s, "ABILITY_EXAMPLE", 350)
        req = {
            "rank_min": 2,
            "mastery_xp_min": 300,
            "knowledge": ["KNOW_FORM"],
            "perks": ["PERK_CONTROL"],
        }
        self.assertFalse(technique_available(s, "ABILITY_EXAMPLE", req))
        s.knowledge["KNOW_FORM"] = {}
        s.perks["PERK_CONTROL"] = {"source": "mentor"}
        self.assertTrue(technique_available(s, "ABILITY_EXAMPLE", req))


    def test_invalid_mastery_numbers_and_rank_thresholds_are_rejected(self):
        s = GameState(seed="x", scene_id="A")
        for value in (True, float("nan"), float("inf"), -1):
            with self.assertRaises(RuleError):
                gain_ability_mastery(s, "ABILITY_BAD", value)

        with self.assertRaises(RuleError):
            gain_ability_mastery(
                s,
                "ABILITY_BAD",
                1,
                rank_thresholds=(0, 100, 50),
            )
        with self.assertRaises(RuleError):
            gain_ability_mastery(
                s,
                "ABILITY_BAD",
                1,
                rank_thresholds=(),
            )
        with self.assertRaises(RuleError):
            mastery_stage(float("nan"))

if __name__ == "__main__":
    unittest.main()
