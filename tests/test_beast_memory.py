import unittest

from textrpg.core import RuleError
from textrpg.beast_memory import (
    adaptation_eligibility,
    record_encounter_observations,
    validate_encounter_memory,
)


class BeastMemoryTests(unittest.TestCase):
    def beast(self, **changes):
        state = {
            "beast_id": "BEAST_WHITE_FANG",
            "species_id": "SPECIES_WOLF",
            "level": 20,
            "development_xp": 500,
            "intelligence_tier": 3,
            "role": "veteran",
            "follower_count": 0,
            "memories": [],
            "adaptations": [],
        }
        state.update(changes)
        return state

    def memory(self, **changes):
        memory = {
            "memory_id": "MEMORY_PLAYER_1",
            "opponent_id": "PLAYER_1",
            "encounter_count": 0,
            "last_seen_time_minutes": 0,
            "observations": {},
        }
        memory.update(changes)
        return memory

    def test_recording_observations_is_copy_on_write(self):
        original = self.memory()
        updated = record_encounter_observations(
            original,
            {"OBS_WEAPON_SPEAR": 0.8},
            occurred_at_minutes=100,
        )
        self.assertEqual(original["observations"], {})
        self.assertEqual(original["encounter_count"], 0)
        self.assertEqual(updated["encounter_count"], 1)
        self.assertEqual(updated["observations"]["OBS_WEAPON_SPEAR"]["count"], 1)

    def test_repeated_observation_accumulates_count_and_confidence_average(self):
        memory = record_encounter_observations(
            self.memory(),
            {"OBS_ATTACK_RIGHT_LEG": 0.6},
            occurred_at_minutes=100,
        )
        memory = record_encounter_observations(
            memory,
            {"OBS_ATTACK_RIGHT_LEG": 1.0},
            occurred_at_minutes=200,
        )
        record = memory["observations"]["OBS_ATTACK_RIGHT_LEG"]
        self.assertEqual(record["count"], 2)
        self.assertEqual(record["confidence"], 0.8)

    def test_adaptation_requires_actual_observation_evidence(self):
        result = adaptation_eligibility(
            self.beast(),
            self.memory(last_seen_time_minutes=100),
            {
                "min_intelligence_tier": 2,
                "min_elapsed_minutes": 60,
                "required_observations": {
                    "OBS_WEAPON_SPEAR": {"min_count": 2, "min_confidence": 0.7}
                },
            },
            current_time_minutes=500,
        )
        self.assertFalse(result["eligible"])
        self.assertEqual(result["missing"], ["observation_count:OBS_WEAPON_SPEAR"])

    def test_adaptation_checks_intelligence_time_count_and_confidence_independently(self):
        memory = self.memory(
            last_seen_time_minutes=100,
            observations={"OBS_WEAPON_SPEAR": {"count": 2, "confidence": 0.5}},
        )
        result = adaptation_eligibility(
            self.beast(intelligence_tier=1),
            memory,
            {
                "min_intelligence_tier": 3,
                "min_elapsed_minutes": 200,
                "required_observations": {
                    "OBS_WEAPON_SPEAR": {"min_count": 2, "min_confidence": 0.8}
                },
            },
            current_time_minutes=250,
        )
        self.assertEqual(
            result["missing"],
            ["intelligence", "elapsed_time", "observation_confidence:OBS_WEAPON_SPEAR"],
        )

    def test_adaptation_becomes_eligible_after_evidence_and_time(self):
        memory = self.memory(
            encounter_count=3,
            last_seen_time_minutes=100,
            observations={
                "OBS_WEAPON_SPEAR": {"count": 3, "confidence": 0.9},
                "OBS_DODGE_LEFT": {"count": 2, "confidence": 0.8},
            },
        )
        result = adaptation_eligibility(
            self.beast(intelligence_tier=4),
            memory,
            {
                "min_intelligence_tier": 3,
                "min_elapsed_minutes": 240,
                "required_observations": {
                    "OBS_WEAPON_SPEAR": {"min_count": 2, "min_confidence": 0.75},
                    "OBS_DODGE_LEFT": {"min_count": 2, "min_confidence": 0.75},
                },
            },
            current_time_minutes=400,
        )
        self.assertEqual(
            result,
            {"eligible": True, "missing": [], "elapsed_minutes": 300},
        )

    def test_invalid_observation_confidence_is_rejected(self):
        with self.assertRaises(RuleError):
            record_encounter_observations(
                self.memory(),
                {"OBS_WEAPON_SPEAR": float("nan")},
                occurred_at_minutes=10,
            )

    def test_memory_validator_rejects_malformed_records(self):
        memory = self.memory(
            observations={"OBS_WEAPON_SPEAR": {"count": True, "confidence": 2.0}}
        )
        errors = validate_encounter_memory(memory)
        self.assertTrue(any("count" in error for error in errors))
        self.assertTrue(any("confidence" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
