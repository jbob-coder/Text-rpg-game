import copy
import unittest

from textrpg import (
    GameState,
    RuleError,
    RulesEngine,
    build_status_view,
    inspect_status_value,
    discover_ability,
    discover_technique,
    gain_ability_mastery,
    dumps_state,
    loads_state,
)


class StatusProjectionTests(unittest.TestCase):
    def test_hidden_perk_provenance_is_redacted_after_save_resume(self):
        state, engine = self.state_and_engine()
        state.perks["PERK_HIDDEN"] = {"visible": False, "modifiers": {"attributes.will": 4}}
        state.perks["PERK_PUBLIC"] = {"modifiers": {"attributes.will": 2}}
        for candidate in (state, loads_state(dumps_state(state))):
            before = copy.deepcopy(candidate.snapshot())
            view = inspect_status_value(candidate, engine, "attributes.will")
            self.assertNotIn("PERK_HIDDEN", repr(view))
            self.assertNotIn("COND_HIDDEN", repr(view))
            self.assertEqual(view["total"], 18.0)
            self.assertEqual(view["breakdown"]["unidentified_modifier"], 3.0)
            self.assertEqual(view["breakdown"]["perk:PERK_PUBLIC"], 2.0)
            self.assertEqual(candidate.snapshot(), before)
            self.assertIn("PERK_HIDDEN", repr(engine.explain_player_value(candidate, "attributes.will")))

    def test_definition_hidden_perks_are_redacted_in_derived_breakdowns(self):
        state, engine = self.state_and_engine()
        state.perks["PERK_SECRET_CAP"] = {"visible": True, "modifiers": {"derived.max_health": 7}}
        state.player["conditions"]["COND_SECRET_CAP"] = {
            "visible": False, "modifiers": {"derived.max_health": -4},
        }
        engine.perk_definitions = {"PERK_SECRET_CAP": {"player_visible": False}}
        view = inspect_status_value(state, engine, "derived.max_health")
        self.assertNotIn("PERK_SECRET_CAP", repr(view))
        self.assertNotIn("COND_SECRET_CAP", repr(view))
        self.assertEqual(view["total"], 92.0)
        self.assertEqual(view["breakdown"]["direct_modifiers"]["unidentified_modifier"], 3.0)

    def test_malformed_perk_visibility_cannot_silently_become_visible(self):
        for bad in (0, None, "false", []):
            with self.subTest(bad=bad):
                state, engine = self.state_and_engine()
                state.perks["PERK_STATUS"]["visible"] = bad
                with self.assertRaises(RuleError):
                    inspect_status_value(state, engine, "attributes.might")
                del state.perks["PERK_STATUS"]["visible"]
                engine.perk_definitions = {"PERK_STATUS": {"player_visible": bad}}
                with self.assertRaises(RuleError):
                    inspect_status_value(state, engine, "attributes.might")

    def test_authored_hidden_perk_stays_hidden_after_grant_and_save(self):
        state = GameState(seed="s", scene_id="SCENE_A", player={"attributes": {"will": 10}})
        engine = RulesEngine({"SCENE_A": {"choices": [{
            "id": "GRANT", "text": "Continue", "outcomes": {"default": {"effects": [{
                "type": "add_perk", "perk_id": "PERK_HIDDEN", "visible": False,
                "modifiers": {"attributes.will": 4},
            }]}},
        }]}})
        engine.choose(state, "GRANT")
        loaded = loads_state(dumps_state(state))
        self.assertIs(loaded.perks["PERK_HIDDEN"].get("visible"), False)
        view = inspect_status_value(loaded, engine, "attributes.will")
        self.assertNotIn("PERK_HIDDEN", repr(view))
        self.assertEqual(view["total"], 14.0)

    def state_and_engine(self):
        state = GameState(
            seed="status-seed",
            scene_id="SCENE_A",
            player={
                "name": "Jack",
                "origin": "Unknown",
                "attributes": {
                    "might": 10,
                    "agility": 12,
                    "endurance": 14,
                    "intellect": 11,
                    "will": 13,
                    "perception": 9,
                    "presence": 8,
                },
                "skills": {
                    "athletics": 5,
                    "ranged": 4,
                    "defense": 3,
                    "powers": 2,
                },
                "resources": {
                    "health": 60.0,
                    "stamina": 40.0,
                    "focus": 30.0,
                    "resolve": 20.0,
                },
                "conditions": {
                    "COND_VISIBLE": {
                        "severity": 2,
                        "duration_minutes": 30,
                        "tags": ["injury"],
                        "modifiers": {"attributes.might": -1},
                    },
                    "COND_HIDDEN": {
                        "severity": 1,
                        "duration_minutes": 10,
                        "tags": ["hidden"],
                        "visible": False,
                        "modifiers": {"attributes.will": -1},
                    },
                },
            },
            equipment={
                "body": {
                    "item_id": "ITEM_BODY",
                    "set_id": "SET_STATUS",
                    "modifiers": {"attributes.might": 2},
                },
                "hands": {
                    "item_id": "ITEM_HANDS",
                    "set_id": "SET_STATUS",
                    "modifiers": {},
                },
            },
            perks={
                "PERK_STATUS": {
                    "modifiers": {"attributes.might": 1},
                }
            },
        )
        engine = RulesEngine(
            {"SCENE_A": {"choices": []}},
            equipment_sets={
                "SET_STATUS": {
                    "thresholds": {
                        "2": {
                            "modifiers": {
                                "attributes.might": 3,
                                "derived.max_health": 5,
                            }
                        }
                    }
                }
            },
        )
        discover_ability(
            state,
            "ABILITY_TRACE",
            family="perception",
            form="latent",
        )
        gain_ability_mastery(state, "ABILITY_TRACE", 100)
        discover_technique(state, "ABILITY_TRACE", "TECHNIQUE_SCAN")
        state.abilities["ABILITY_TRACE"]["evolution_visibility"] = {
            "EVOLUTION_HIDDEN": {"state": "hidden"},
            "EVOLUTION_KNOWN": {
                "state": "known",
                "known_requirements": ["mastery"],
            },
        }
        return state, engine

    def test_status_projection_uses_rules_and_does_not_mutate_state(self):
        state, engine = self.state_and_engine()
        before = copy.deepcopy(state.snapshot())

        view = build_status_view(
            state,
            engine,
            ability_definitions={
                "ABILITY_TRACE": {
                    "name": "Trace",
                    "techniques": {
                        "TECHNIQUE_SCAN": {"name": "Scan"},
                        "TECHNIQUE_SECRET": {"name": "Secret"},
                    },
                    "evolutions": {
                        "EVOLUTION_HIDDEN": {
                            "name": "Hidden Form",
                            "requirements": {"mastery_xp_min": 9999},
                        },
                        "EVOLUTION_KNOWN": {
                            "name": "Focused Trace",
                            "requirements": {"knowledge": ["KNOW_SECRET"]},
                        },
                    },
                }
            },
            condition_definitions={
                "COND_VISIBLE": {"name": "Strained Arm"},
                "COND_HIDDEN": {"name": "Hidden Effect"},
            },
        )

        self.assertEqual(state.snapshot(), before)

        might = next(item for item in view["attributes"] if item["id"] == "might")
        self.assertEqual(might["base"], 10.0)
        # 10 base +2 equipment +3 set +1 perk -1 visible condition
        self.assertEqual(might["effective"], 15.0)
        self.assertEqual(might["delta"], 5.0)
        self.assertNotIn("breakdown", might)

        self.assertEqual(
            [item["id"] for item in view["conditions"]],
            ["COND_VISIBLE"],
        )
        self.assertEqual(view["conditions"][0]["name"], "Strained Arm")
        self.assertNotIn("modifiers", view["conditions"][0])

        ability = view["abilities"][0]
        self.assertEqual(ability["name"], "Trace")
        self.assertEqual(
            [item["technique_id"] for item in ability["techniques"]],
            ["TECHNIQUE_SCAN"],
        )
        self.assertEqual(
            [item["evolution_id"] for item in ability["evolutions"]],
            ["EVOLUTION_KNOWN"],
        )
        self.assertNotIn("requirements", ability["evolutions"][0])

    def test_resources_use_derived_max_without_mutating_current_value(self):
        state, engine = self.state_and_engine()
        state.player["resources"]["health"] = 999.0
        before = copy.deepcopy(state.snapshot())

        view = build_status_view(state, engine)
        health = next(item for item in view["resources"] if item["id"] == "health")

        self.assertTrue(health["over_cap"])
        self.assertEqual(health["current"], 999.0)
        self.assertGreater(health["max"], 0.0)
        self.assertEqual(state.snapshot(), before)

    def test_hidden_condition_definition_is_not_exposed(self):
        state, engine = self.state_and_engine()
        state.player["conditions"]["COND_VISIBLE"]["visible"] = True
        view = build_status_view(
            state,
            engine,
            condition_definitions={
                "COND_VISIBLE": {
                    "name": "Secret Diagnosis",
                    "player_visible": False,
                }
            },
        )
        self.assertEqual(view["conditions"], [])

    def test_status_projection_rejects_structured_identity_leak(self):
        state, engine = self.state_and_engine()
        state.player["background"] = {"secret": "INTERNAL_FLAG"}
        with self.assertRaises(RuleError):
            build_status_view(state, engine)


    def test_deep_status_inspection_uses_rules_explainability(self):
        state, engine = self.state_and_engine()

        might = inspect_status_value(state, engine, "attributes.might")
        self.assertEqual(might["total"], 15.0)
        self.assertEqual(might["breakdown"]["base"], 10.0)
        self.assertEqual(might["breakdown"]["equipment:body"], 2.0)
        self.assertEqual(might["breakdown"]["set:SET_STATUS:2"], 3.0)
        self.assertEqual(might["breakdown"]["perk:PERK_STATUS"], 1.0)
        self.assertEqual(might["breakdown"]["condition:COND_VISIBLE"], -1.0)

        health = inspect_status_value(state, engine, "derived.max_health")
        self.assertEqual(health["kind"], "derived")
        self.assertIn("inputs", health["breakdown"])
        self.assertIn("direct_modifiers", health["breakdown"])

    def test_deep_status_inspection_rejects_hidden_or_raw_paths(self):
        state, engine = self.state_and_engine()
        for path in (
            "quests.QUEST_SECRET",
            "abilities.ABILITY_TRACE",
            "relationships.NPC_SECRET",
            "attributes.unknown",
            "skills.unknown",
            "derived.unknown",
        ):
            with self.assertRaises(RuleError):
                inspect_status_value(state, engine, path)


    def test_deep_status_inspection_redacts_hidden_condition_identifier(self):
        state, engine = self.state_and_engine()
        view = inspect_status_value(state, engine, "attributes.will")

        rendered = repr(view)
        self.assertNotIn("COND_HIDDEN", rendered)
        self.assertIn("unidentified_modifier", view["breakdown"])
        self.assertEqual(view["total"], 12.0)

    def test_deep_status_inspection_honors_hidden_condition_definition(self):
        state, engine = self.state_and_engine()
        state.player["conditions"]["COND_SECRET_CAP"] = {
            "severity": 1,
            "duration_minutes": 20,
            "tags": ["secret"],
            "visible": True,
            "modifiers": {"derived.max_health": -4},
        }

        view = inspect_status_value(
            state,
            engine,
            "derived.max_health",
            condition_definitions={
                "COND_SECRET_CAP": {
                    "name": "Classified",
                    "player_visible": False,
                }
            },
        )

        rendered = repr(view)
        self.assertNotIn("COND_SECRET_CAP", rendered)
        self.assertIn(
            "unidentified_modifier",
            view["breakdown"]["direct_modifiers"],
        )

if __name__ == "__main__":
    unittest.main()
