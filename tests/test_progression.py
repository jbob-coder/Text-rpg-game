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

    def test_corrupt_existing_ability_mastery_is_rejected_without_mutation(self):
        state = GameState(
            seed="x",
            scene_id="A",
            abilities={
                "ABILITY_BAD": {
                    "rank": 1,
                    "mastery_xp": float("nan"),
                    "mastery_stage": "learned",
                    "techniques": {},
                }
            },
        )
        before = dict(state.abilities["ABILITY_BAD"])
        with self.assertRaises(RuleError):
            gain_ability_mastery(state, "ABILITY_BAD", 10)
        self.assertEqual(
            state.abilities["ABILITY_BAD"]["rank"],
            before["rank"],
        )
        self.assertTrue(
            str(state.abilities["ABILITY_BAD"]["mastery_xp"]) == "nan"
        )
        self.assertEqual(
            state.abilities["ABILITY_BAD"]["mastery_stage"],
            before["mastery_stage"],
        )

    def test_invalid_rank_floor_is_rejected_before_mastery_mutation(self):
        state = GameState(
            seed="x",
            scene_id="A",
            abilities={
                "ABILITY_BAD": {
                    "rank": 0,
                    "rank_floor": True,
                    "mastery_xp": 0.0,
                    "mastery_stage": "discovered",
                    "techniques": {},
                }
            },
        )
        with self.assertRaises(RuleError):
            gain_ability_mastery(state, "ABILITY_BAD", 10)
        self.assertEqual(state.abilities["ABILITY_BAD"]["mastery_xp"], 0.0)

if __name__ == "__main__":
    unittest.main()
