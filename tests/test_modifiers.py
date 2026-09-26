import unittest

from textrpg import GameState, RuleError, RulesEngine, effective_player_value, modifier_breakdown, validate_modifier_path
from textrpg.stats import derived_stats, initialize_resources


SET_DEFINITIONS = {
    "SET_SCOUT": {
        "thresholds": {
            "2": {"modifiers": {"attributes.might": 5, "derived.evasion": 2}}
        }
    }
}


class ModifierPipelineTests(unittest.TestCase):
    def test_all_sources_stack_once_without_mutating_base(self):
        state = GameState(
            seed="s",
            scene_id="A",
            player={
                "attributes": {"might": 10},
                "conditions": {
                    "COND_INJURED": {"modifiers": {"attributes.might": -4}}
                },
            },
            equipment={
                "body": {
                    "item_id": "ITEM_BODY",
                    "set_id": "SET_SCOUT",
                    "modifiers": {"attributes.might": 2},
                },
                "hands": {
                    "item_id": "ITEM_HANDS",
                    "set_id": "SET_SCOUT",
                    "modifiers": {},
                },
            },
            perks={
                "PERK_DRILLED": {"modifiers": {"attributes.might": 3}}
            },
        )

        self.assertEqual(effective_player_value(state, "attributes.might", SET_DEFINITIONS), 16.0)
        self.assertEqual(state.player["attributes"]["might"], 10)

        breakdown = modifier_breakdown(state, "attributes.might", SET_DEFINITIONS)
        self.assertEqual(breakdown["base"], 10.0)
        self.assertEqual(breakdown["equipment:body"], 2.0)
        self.assertEqual(breakdown["set:SET_SCOUT:2"], 5.0)
        self.assertEqual(breakdown["perk:PERK_DRILLED"], 3.0)
        self.assertEqual(breakdown["condition:COND_INJURED"], -4.0)
        self.assertEqual(breakdown["total"], 16.0)

    def test_rule_requirements_use_set_and_condition_modifiers(self):
        engine = RulesEngine(
            {
                "A": {
                    "choices": [
                        {
                            "id": "FORCE_DOOR",
                            "text": "Force the door",
                            "requires": [
                                {"type": "stat_min", "path": "attributes.might", "value": 15}
                            ],
                            "outcomes": {"default": {"effects": []}},
                        }
                    ]
                }
            },
            set_definitions=SET_DEFINITIONS,
        )
        state = GameState(
            seed="s",
            scene_id="A",
            player={
                "attributes": {"might": 10},
                "conditions": {
                    "COND_BRUISED": {"modifiers": {"attributes.might": -1}}
                },
            },
            equipment={
                "body": {"item_id": "A", "set_id": "SET_SCOUT", "modifiers": {}},
                "hands": {"item_id": "B", "set_id": "SET_SCOUT", "modifiers": {}},
            },
            perks={"PERK_PUSH": {"modifiers": {"attributes.might": 1}}},
        )

        choice = engine.available_choices(state)[0]
        self.assertTrue(choice["enabled"])

        state.player["conditions"]["COND_EXHAUSTED"] = {
            "modifiers": {"attributes.might": -2}
        }
        choice = engine.available_choices(state)[0]
        self.assertFalse(choice["enabled"])

    def test_derived_stats_use_effective_inputs_and_direct_derived_modifiers(self):
        state = GameState(
            seed="s",
            scene_id="A",
            player={
                "attributes": {
                    "might": 0,
                    "agility": 0,
                    "endurance": 10,
                    "intellect": 0,
                    "will": 10,
                    "perception": 0,
                    "presence": 0,
                },
                "skills": {},
                "conditions": {
                    "COND_WOUNDED": {"modifiers": {"attributes.endurance": -2}}
                },
            },
            perks={
                "PERK_TOUGH": {"modifiers": {"derived.max_health": 7}}
            },
        )

        first = derived_stats(state)
        second = derived_stats(state)
        self.assertEqual(first["max_health"], 78.0)
        self.assertEqual(second["max_health"], 78.0)
        self.assertEqual(state.player["attributes"]["endurance"], 10)

        initialize_resources(state, refill=True)
        self.assertEqual(state.player["resources"]["health"], 78.0)

    def test_set_bonus_can_modify_derived_value_directly(self):
        state = GameState(
            seed="s",
            scene_id="A",
            player={"attributes": {}, "skills": {}},
            equipment={
                "body": {"item_id": "A", "set_id": "SET_SCOUT", "modifiers": {}},
                "hands": {"item_id": "B", "set_id": "SET_SCOUT", "modifiers": {}},
            },
        )
        values = derived_stats(state, SET_DEFINITIONS)
        self.assertEqual(values["evasion"], 2.0)

    def test_modifier_path_registry_rejects_typos(self):
        with self.assertRaises(ValueError):
            validate_modifier_path("attributes.migth")
        with self.assertRaises(ValueError):
            validate_modifier_path("derived.max_heath")
        self.assertEqual(validate_modifier_path("skills.ranged"), "skills.ranged")

    def test_rules_engine_rejects_invalid_set_modifier_paths(self):
        with self.assertRaises(RuleError):
            RulesEngine(
                {"A": {"choices": []}},
                set_definitions={
                    "SET_BAD": {
                        "thresholds": {
                            "2": {"modifiers": {"derived.max_heath": 5}}
                        }
                    }
                },
            )

    def test_rules_engine_explains_effective_and_derived_values(self):
        state = GameState(
            seed="s",
            scene_id="A",
            player={
                "attributes": {
                    "might": 10,
                    "agility": 10,
                    "perception": 0,
                    "endurance": 0,
                    "intellect": 0,
                    "will": 0,
                    "presence": 0,
                },
                "skills": {"athletics": 0},
            },
            equipment={
                "body": {
                    "item_id": "A",
                    "set_id": "SET_SCOUT",
                    "modifiers": {"attributes.might": 2},
                },
                "hands": {"item_id": "B", "set_id": "SET_SCOUT", "modifiers": {}},
            },
        )
        engine = RulesEngine({"A": {"choices": []}}, set_definitions=SET_DEFINITIONS)

        might = engine.explain_player_value(state, "attributes.might")
        self.assertEqual(might["total"], 17.0)
        self.assertEqual(might["breakdown"]["base"], 10.0)
        self.assertEqual(might["breakdown"]["equipment:body"], 2.0)
        self.assertEqual(might["breakdown"]["set:SET_SCOUT:2"], 5.0)

        evasion = engine.explain_player_value(state, "derived.evasion")
        self.assertEqual(evasion["total"], 8.5)
        self.assertEqual(
            evasion["breakdown"]["inputs"]["attributes.agility"]["contribution"],
            6.5,
        )
        self.assertEqual(
            evasion["breakdown"]["direct_modifiers"]["set:SET_SCOUT:2"],
            2.0,
        )

    def test_rules_engine_can_gate_on_full_derived_value(self):
        engine = RulesEngine(
            {
                "A": {
                    "choices": [
                        {
                            "id": "DODGE_GAP",
                            "text": "Cross the moving gap",
                            "requires": [
                                {"type": "stat_min", "path": "derived.evasion", "value": 8}
                            ],
                            "outcomes": {"default": {"effects": []}},
                        }
                    ]
                }
            },
            set_definitions=SET_DEFINITIONS,
        )
        state = GameState(
            seed="s",
            scene_id="A",
            player={
                "attributes": {
                    "agility": 10,
                    "perception": 0,
                    "might": 0,
                    "endurance": 0,
                    "intellect": 0,
                    "will": 0,
                    "presence": 0,
                },
                "skills": {"athletics": 0},
            },
            equipment={
                "body": {"item_id": "A", "set_id": "SET_SCOUT", "modifiers": {}},
                "hands": {"item_id": "B", "set_id": "SET_SCOUT", "modifiers": {}},
            },
        )
        # Base evasion is 6.5; the active two-piece set adds +2 => 8.5.
        self.assertTrue(engine.available_choices(state)[0]["enabled"])


if __name__ == "__main__":
    unittest.main()
