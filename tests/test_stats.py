import unittest

from textrpg import DERIVED_FORMULAS, DERIVED_STAT_SPECS, GameState, RulesEngine, validate_modifier_path
from textrpg.stats import derived_stat_breakdown, derived_stats, effective_player_value, initialize_resources, validate_player_stats


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


    def test_derived_formula_registry_is_consistent(self):
        self.assertEqual(set(DERIVED_FORMULAS), set(DERIVED_STAT_SPECS))
        for formula in DERIVED_FORMULAS.values():
            for path in formula.get("terms", {}):
                self.assertEqual(validate_modifier_path(path), path)

    def test_capacity_derived_values_are_floored_at_zero(self):
        state = self.state()
        state.perks["PERK_COLLAPSE"] = {
            "modifiers": {
                "derived.max_health": -1000,
                "derived.carry_capacity": -1000,
            }
        }
        values = derived_stats(state)
        self.assertEqual(values["max_health"], 0.0)
        self.assertEqual(values["carry_capacity"], 0.0)

        state.player["resources"] = {"health": 20}
        initialize_resources(state)
        self.assertEqual(state.player["resources"]["max_health"], 0.0)
        self.assertEqual(state.player["resources"]["health"], 0.0)

    def test_derived_breakdown_exposes_floor_adjustment(self):
        state = self.state()
        state.perks["PERK_COLLAPSE"] = {
            "modifiers": {"derived.max_health": -1000}
        }
        breakdown = derived_stat_breakdown(state, "max_health")
        self.assertLess(breakdown["raw_total"], 0.0)
        self.assertEqual(breakdown["floor"], 0.0)
        self.assertGreater(breakdown["floor_adjustment"], 0.0)
        self.assertEqual(breakdown["total"], 0.0)

    def test_contest_style_derived_values_can_go_negative(self):
        state = self.state()
        state.perks["PERK_STAGGERED"] = {
            "modifiers": {"derived.initiative": -1000}
        }
        self.assertLess(derived_stats(state)["initiative"], 0.0)

    def test_foundation_stats_keyword_api_remains_compatible(self):
        state = self.state()
        state.equipment = {
            "body": {"item_id": "A", "set_id": "SET_COMPAT", "modifiers": {}},
            "hands": {"item_id": "B", "set_id": "SET_COMPAT", "modifiers": {}},
        }
        sets = {
            "SET_COMPAT": {
                "thresholds": {
                    "2": {"modifiers": {"derived.max_health": 5}}
                }
            }
        }
        values = derived_stats(state, equipment_sets=sets)
        self.assertEqual(
            values["max_health"],
            derived_stats(state, set_definitions=sets)["max_health"],
        )
        maxima = initialize_resources(state, equipment_sets=sets)
        self.assertEqual(maxima["health"], values["max_health"])

    def test_non_finite_player_stats_are_reported(self):
        state = self.state()
        state.player["attributes"]["might"] = float("nan")
        state.player["skills"]["athletics"] = float("inf")
        errors = validate_player_stats(state)
        self.assertTrue(any("attribute might must be finite numeric" in e for e in errors))
        self.assertTrue(any("skill athletics must be finite numeric" in e for e in errors))

if __name__ == "__main__":
    unittest.main()
