import unittest

from textrpg import GameState, RuleError, dumps_state, loads_state


class PersistenceTests(unittest.TestCase):
    def test_round_trip_preserves_extended_state(self):
        state = GameState(
            seed="save-seed",
            scene_id="SCENE_1",
            party=["NPC_A"],
            abilities={"ABILITY_X": {"rank": 1, "mastery_xp": 120}},
            perks={"PERK_X": {"source": "training"}},
        )
        loaded = loads_state(dumps_state(state))
        self.assertEqual(loaded.snapshot(), state.snapshot())

    def test_unknown_schema_is_rejected(self):
        raw = '{"schema_version":999,"seed":"x","scene_id":"A"}'
        with self.assertRaises(RuleError):
            loads_state(raw)


    def test_round_trip_preserves_ability_discovery_and_visibility_state(self):
        state = GameState(
            seed="ability-save",
            scene_id="SCENE_A",
            abilities={
                "ABILITY_FLUX": {
                    "rank": 2,
                    "mastery_xp": 350.0,
                    "mastery_stage": "mastered",
                    "control": 12.0,
                    "efficiency": 8.0,
                    "techniques": {
                        "TECHNIQUE_PULSE": {
                            "mastery_xp": 40.0,
                            "stage": "learned",
                            "uses": 4,
                            "ready_at_minutes": 120,
                            "discovered_at_minutes": 10,
                        }
                    },
                    "evolution_visibility": {
                        "EVOLUTION_STABLE": {
                            "state": "partial",
                            "hint": "A stable pattern is required.",
                            "known_requirements": ["mastery"],
                        }
                    },
                    "evolutions": [],
                }
            },
        )
        loaded = loads_state(dumps_state(state))
        self.assertEqual(loaded.abilities, state.abilities)

if __name__ == "__main__":
    unittest.main()
