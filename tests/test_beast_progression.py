import unittest

from textrpg.beast_progression import (
    award_beast_development,
    level_for_total_xp,
    total_xp_required_for_level,
    validate_progression_definition,
)
from textrpg.core import RuleError


class BeastProgressionTests(unittest.TestCase):
    def beast(self, **changes):
        state = {
            "beast_id": "BEAST_WHITE_FANG",
            "species_id": "SPECIES_WOLF",
            "level": 1,
            "development_xp": 0,
            "intelligence_tier": 2,
            "role": "pack_member",
            "follower_count": 0,
            "memories": [],
            "adaptations": [],
        }
        state.update(changes)
        return state

    def definition(self, **changes):
        definition = {
            "base_level_xp": 100,
            "growth_factor": 1.5,
            "repeat_decay": 0.5,
            "min_repeat_factor": 0.1,
            "max_xp_per_event": 500,
            "max_level": 10,
        }
        definition.update(changes)
        return definition

    def event(self, **changes):
        event = {
            "event_id": "EVENT_HUNT_1",
            "repeat_key": "EVENTCLASS_HUNT_DEER",
            "type": "hunt",
            "meaningful": True,
            "base_xp": 80,
            "significance": 1.0,
        }
        event.update(changes)
        return event

    def test_progression_definition_is_strict(self):
        self.assertEqual(validate_progression_definition(self.definition()), [])
        errors = validate_progression_definition(self.definition(repeat_decay=2))
        self.assertTrue(any("repeat_decay" in error for error in errors))

    def test_level_thresholds_grow_deterministically(self):
        self.assertEqual(total_xp_required_for_level(1, self.definition()), 0.0)
        self.assertEqual(total_xp_required_for_level(2, self.definition()), 100.0)
        self.assertEqual(total_xp_required_for_level(3, self.definition()), 250.0)
        self.assertEqual(level_for_total_xp(249, self.definition()), 2)
        self.assertEqual(level_for_total_xp(250, self.definition()), 3)

    def test_meaningful_event_awards_xp_copy_on_write(self):
        original = self.beast()
        updated = award_beast_development(original, self.event(), self.definition())
        self.assertEqual(original["development_xp"], 0)
        self.assertEqual(updated["development_xp"], 80.0)
        self.assertEqual(updated["development_history"]["EVENTCLASS_HUNT_DEER"], 1)

    def test_repeat_decay_reduces_farming_value(self):
        first = award_beast_development(self.beast(), self.event(), self.definition())
        second = award_beast_development(
            first,
            self.event(event_id="EVENT_HUNT_2"),
            self.definition(),
        )
        self.assertEqual(first["development_log"][-1]["awarded_xp"], 80.0)
        self.assertEqual(second["development_log"][-1]["awarded_xp"], 40.0)

    def test_repeat_factor_has_floor_instead_of_reaching_negative_or_nan(self):
        beast = self.beast(development_history={"EVENTCLASS_HUNT_DEER": 20})
        updated = award_beast_development(beast, self.event(), self.definition())
        self.assertEqual(updated["development_log"][-1]["repeat_factor"], 0.1)
        self.assertEqual(updated["development_log"][-1]["awarded_xp"], 8.0)

    def test_nonmeaningful_event_gives_no_xp_and_does_not_consume_novelty(self):
        updated = award_beast_development(
            self.beast(),
            self.event(meaningful=False),
            self.definition(),
        )
        self.assertEqual(updated["development_xp"], 0.0)
        self.assertEqual(updated["development_history"], {})
        self.assertEqual(updated["development_log"][-1]["awarded_xp"], 0.0)

    def test_event_can_level_beast_up_but_never_regresses_existing_level(self):
        leveled = award_beast_development(
            self.beast(development_xp=90),
            self.event(base_xp=20),
            self.definition(),
        )
        self.assertEqual(leveled["level"], 2)

        high_level = award_beast_development(
            self.beast(level=8, development_xp=0),
            self.event(base_xp=1),
            self.definition(),
        )
        self.assertEqual(high_level["level"], 8)

    def test_event_award_is_capped(self):
        updated = award_beast_development(
            self.beast(),
            self.event(base_xp=5000),
            self.definition(max_xp_per_event=200),
        )
        self.assertEqual(updated["development_log"][-1]["awarded_xp"], 200.0)

    def test_invalid_history_is_rejected_before_mutation(self):
        beast = self.beast(development_history={"EVENTCLASS_HUNT_DEER": True})
        with self.assertRaises(RuleError):
            award_beast_development(beast, self.event(), self.definition())
        self.assertEqual(beast["development_xp"], 0)


if __name__ == "__main__":
    unittest.main()
