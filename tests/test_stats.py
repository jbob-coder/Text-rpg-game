import unittest

from textrpg import GameState, RulesEngine
from textrpg.stats import derived_stats, effective_player_value, initialize_resources, validate_player_stats


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

    def test_derived_stats_use_equipment_perk_condition_and_set_modifiers_once(self):
        state = self.state()
        state.equipment["body"] = {
            "item_id": "ITEM_BODY",
            "set_id": "SET_SCOUT",
            "modifiers": {
                "attributes.endurance": 5,
                "derived.max_health": 10,
            },
        }
        state.equipment["hands"] = {
            "item_id": "ITEM_HANDS",
            "set_id": "SET_SCOUT",
            "modifiers": {"skills.athletics": 4},
        }
        state.perks["PERK_STEADY"] = {
            "modifiers": {"attributes.will": 2},
        }
        state.player["conditions"] = {
            "COND_SPRAIN": {
                "modifiers": {
                    "attributes.agility": -10,
                    "derived.evasion": -2,
                }
            }
        }
        sets = {
            "SET_SCOUT": {
                "thresholds": {
                    "2": {
                        "modifiers": {
                            "attributes.perception": 4,
                            "derived.initiative": 3,
                        }
                    }
                }
            }
        }

        values = derived_stats(state, equipment_sets=sets)

        # max_health = 50 + (60+5)*2 + (30+2)*0.5 + direct derived +10
        self.assertEqual(values["max_health"], 206.0)
        # initiative = (50-10)*0.7 + (45+4)*0.3 + direct derived +3
        self.assertEqual(values["initiative"], 45.7)
        # evasion = effective agility/perception/athletics formula, then -2 once
        self.assertEqual(values["evasion"], 37.4)

        self.assertEqual(state.player["attributes"]["endurance"], 60)
        self.assertEqual(state.player["attributes"]["will"], 30)

    def test_resource_maxima_follow_effective_derived_stats_without_refill_overflow(self):
        state = self.state()
        initialize_resources(state, refill=True)
        original_health = state.player["resources"]["health"]
        state.equipment["body"] = {
            "item_id": "ITEM_ENDURANCE_COAT",
            "modifiers": {"attributes.endurance": 10},
        }
        maxima = initialize_resources(state)
        self.assertEqual(maxima["health"], 205.0)
        self.assertEqual(state.player["resources"]["max_health"], 205.0)
        self.assertEqual(state.player["resources"]["health"], original_health)

        state.player["conditions"] = {
            "COND_MAJOR_WOUND": {
                "modifiers": {"attributes.endurance": -30},
            }
        }
        initialize_resources(state)
        self.assertEqual(state.player["resources"]["max_health"], 145.0)
        self.assertEqual(state.player["resources"]["health"], 145.0)

    def test_effective_player_value_matches_check_modifier_contract(self):
        state = self.state()
        state.equipment["body"] = {
            "item_id": "ITEM_BODY",
            "modifiers": {"attributes.might": 5},
        }
        state.perks["PERK_POWER"] = {
            "modifiers": {"attributes.might": 2},
        }
        state.player["conditions"] = {
            "COND_WEAKNESS": {
                "modifiers": {"attributes.might": -3},
            }
        }
        self.assertEqual(
            effective_player_value(state, "attributes.might"),
            44.0,
        )

        engine = RulesEngine({
            "A": {
                "choices": [{
                    "id": "CHECK_MIGHT",
                    "text": "Check effective might.",
                    "check": {
                        "stat": "attributes.might",
                        "difficulty": 0,
                        "variance": 0,
                    },
                    "outcomes": {
                        "critical_success": {"effects": []},
                        "success": {"effects": []},
                        "failure": {"effects": []},
                        "critical_failure": {"effects": []},
                    },
                }]
            }
        })
        event = engine.choose(state, "CHECK_MIGHT")
        self.assertEqual(event["check"]["base"], 44.0)


if __name__ == "__main__":
    unittest.main()
