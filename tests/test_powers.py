import unittest

from textrpg import GameState, RuleError, gain_ability_mastery
from textrpg.powers import (
    ability_evolution_status,
    ability_player_view,
    discover_ability,
    discover_technique,
    evolve_ability,
    gain_technique_mastery,
    practice_technique,
    technique_stage,
    technique_use_status,
    use_technique,
    validate_evolution_definition,
    validate_technique_definition,
)
from textrpg.simulation import advance_time


class PowerRuntimeTests(unittest.TestCase):
    def state(self):
        state = GameState(
            seed="power-seed",
            scene_id="A",
            player={
                "attributes": {
                    "might": 30,
                    "agility": 30,
                    "endurance": 30,
                    "intellect": 40,
                    "will": 45,
                    "perception": 30,
                    "presence": 30,
                },
                "skills": {"powers": 25, "athletics": 20},
                "resources": {"focus": 20.0, "stamina": 30.0},
                "power_resources": {"flux": 12.0},
            },
            flags={"TRAINED_WITH_MENTOR": True},
            inventory={"ITEM_CORE_SHARD": 1},
        )
        gain_ability_mastery(state, "ABILITY_FLUX", 350)
        discover_technique(state, "ABILITY_FLUX", "TECHNIQUE_PULSE")
        return state

    def definition(self):
        return {
            "stage_min": "discovered",
            "requirements": {
                "rank_min": 2,
                "mastery_xp_min": 300,
                "attributes": {"will": 40},
                "skills": {"powers": 20},
                "flags": {"TRAINED_WITH_MENTOR": True},
            },
            "costs": {
                "resources.focus": 4,
                "power_resources.flux": 3,
            },
            "cooldown_minutes": 15,
            "mastery_gain": 10,
            "ability_mastery_gain": 5,
        }

    def test_discover_ability_creates_shell_without_free_mastery(self):
        state = GameState(seed="s", scene_id="A")
        ability = discover_ability(
            state,
            "ABILITY_TRACE_ECHO",
            family="perception",
            form="latent",
            tags=["sensory"],
        )
        self.assertEqual(ability["rank"], 0)
        self.assertEqual(ability["mastery_xp"], 0.0)
        self.assertEqual(ability["family"], "perception")
        self.assertEqual(ability["form"], "latent")
        self.assertEqual(state.history[-1]["type"], "ability_discovered")

        history_count = len(state.history)
        discover_ability(state, "ABILITY_TRACE_ECHO", family="different")
        self.assertEqual(len(state.history), history_count)
        self.assertEqual(state.abilities["ABILITY_TRACE_ECHO"]["family"], "perception")

    def test_technique_stage_thresholds(self):
        self.assertEqual(technique_stage(0), "discovered")
        self.assertEqual(technique_stage(10), "unstable")
        self.assertEqual(technique_stage(40), "learned")
        self.assertEqual(technique_stage(300), "mastered")

    def test_use_spends_resources_sets_cooldown_and_records_history(self):
        state = self.state()
        event = use_technique(
            state, "ABILITY_FLUX", "TECHNIQUE_PULSE", self.definition()
        )
        self.assertEqual(state.player["resources"]["focus"], 16.0)
        self.assertEqual(state.player["power_resources"]["flux"], 9.0)
        self.assertEqual(
            state.abilities["ABILITY_FLUX"]["techniques"]["TECHNIQUE_PULSE"][
                "ready_at_minutes"
            ],
            15,
        )
        self.assertEqual(event["type"], "technique_use")
        self.assertEqual(state.history[-1]["technique_id"], "TECHNIQUE_PULSE")

    def test_insufficient_resource_rejects_without_partial_spend(self):
        state = self.state()
        state.player["power_resources"]["flux"] = 2
        before_focus = state.player["resources"]["focus"]
        status = technique_use_status(
            state, "ABILITY_FLUX", "TECHNIQUE_PULSE", self.definition()
        )
        self.assertFalse(status["available"])
        self.assertIn("resource:power_resources.flux", status["reasons"])
        with self.assertRaises(RuleError):
            use_technique(
                state, "ABILITY_FLUX", "TECHNIQUE_PULSE", self.definition()
            )
        self.assertEqual(state.player["resources"]["focus"], before_focus)

    def test_cooldown_uses_world_time(self):
        state = self.state()
        use_technique(state, "ABILITY_FLUX", "TECHNIQUE_PULSE", self.definition())
        with self.assertRaises(RuleError):
            use_technique(
                state, "ABILITY_FLUX", "TECHNIQUE_PULSE", self.definition()
            )
        advance_time(state, 15)
        self.assertTrue(
            technique_use_status(
                state, "ABILITY_FLUX", "TECHNIQUE_PULSE", self.definition()
            )["available"]
        )

    def test_drawback_applies_authored_condition(self):
        state = self.state()
        definition = self.definition()
        definition["drawbacks"] = [
            {
                "type": "condition",
                "condition_id": "COND_POWER_STRAIN",
                "severity": 2,
                "duration_minutes": 30,
                "tags": ["power", "fatigue"],
                "modifiers": {"attributes.will": -2},
            }
        ]
        event = use_technique(
            state, "ABILITY_FLUX", "TECHNIQUE_PULSE", definition
        )
        self.assertIn("COND_POWER_STRAIN", state.player["conditions"])
        self.assertEqual(event["drawbacks"], ["COND_POWER_STRAIN"])

    def test_use_can_advance_technique_mastery(self):
        state = self.state()
        use_technique(state, "ABILITY_FLUX", "TECHNIQUE_PULSE", self.definition())
        technique = state.abilities["ABILITY_FLUX"]["techniques"]["TECHNIQUE_PULSE"]
        self.assertEqual(technique["mastery_xp"], 10.0)
        self.assertEqual(technique["stage"], "unstable")
        gain_technique_mastery(state, "ABILITY_FLUX", "TECHNIQUE_PULSE", 30)
        self.assertEqual(technique["stage"], "learned")

    def test_use_can_advance_overall_ability_mastery(self):
        state = self.state()
        before = state.abilities["ABILITY_FLUX"]["mastery_xp"]
        event = use_technique(
            state, "ABILITY_FLUX", "TECHNIQUE_PULSE", self.definition()
        )
        self.assertEqual(state.abilities["ABILITY_FLUX"]["mastery_xp"], before + 5)
        self.assertIsNotNone(event["ability_mastery"])

    def test_evolution_requires_technique_stage_and_other_prerequisites(self):
        state = self.state()
        definition = {
            "requirements": {
                "rank_min": 2,
                "mastery_xp_min": 300,
                "knowledge": ["KNOW_FLUX_PATTERN"],
                "perks": ["PERK_CONTROL"],
                "attributes": {"will": 40},
                "skills": {"powers": 20},
                "flags": {"TRAINED_WITH_MENTOR": True},
                "items": {"ITEM_CORE_SHARD": 1},
                "techniques": {"TECHNIQUE_PULSE": "learned"},
            },
            "result": {"form": "stabilized_flux"},
        }
        status = ability_evolution_status(
            state, "ABILITY_FLUX", "EVOLUTION_STABLE", definition
        )
        self.assertFalse(status["available"])

        state.knowledge["KNOW_FLUX_PATTERN"] = {}
        state.perks["PERK_CONTROL"] = {"source": "mentor"}
        gain_technique_mastery(state, "ABILITY_FLUX", "TECHNIQUE_PULSE", 40)

        status = ability_evolution_status(
            state, "ABILITY_FLUX", "EVOLUTION_STABLE", definition
        )
        self.assertTrue(status["available"])

    def test_evolution_changes_form_grants_perk_and_cannot_repeat(self):
        state = self.state()
        state.knowledge["KNOW_FLUX_PATTERN"] = {}
        gain_technique_mastery(state, "ABILITY_FLUX", "TECHNIQUE_PULSE", 40)
        definition = {
            "requirements": {
                "rank_min": 2,
                "knowledge": ["KNOW_FLUX_PATTERN"],
                "techniques": {"TECHNIQUE_PULSE": "learned"},
            },
            "result": {
                "form": "stabilized_flux",
                "rank_floor": 3,
                "tags": ["stable"],
                "consume_items": {"ITEM_CORE_SHARD": 1},
                "grant_perks": {
                    "PERK_FLUX_CONTROL": {
                        "modifiers": {"attributes.will": 2},
                        "tags": ["power"],
                    }
                },
            },
        }
        event = evolve_ability(
            state, "ABILITY_FLUX", "EVOLUTION_STABLE", definition
        )
        self.assertEqual(state.abilities["ABILITY_FLUX"]["form"], "stabilized_flux")
        self.assertGreaterEqual(state.abilities["ABILITY_FLUX"]["rank"], 3)
        self.assertEqual(state.abilities["ABILITY_FLUX"]["rank_floor"], 3)
        self.assertNotIn("ITEM_CORE_SHARD", state.inventory)
        self.assertEqual(event["consumed_items"], {"ITEM_CORE_SHARD": 1})
        self.assertIn("PERK_FLUX_CONTROL", state.perks)
        self.assertEqual(event["type"], "ability_evolution")

        gain_ability_mastery(state, "ABILITY_FLUX", 1)
        self.assertGreaterEqual(state.abilities["ABILITY_FLUX"]["rank"], 3)

        with self.assertRaises(RuleError):
            evolve_ability(
                state, "ABILITY_FLUX", "EVOLUTION_STABLE", definition
            )


    def test_practice_technique_costs_time_resources_and_progresses_slowly(self):
        state = self.state()
        before_focus = state.player["resources"]["focus"]
        before_stamina = state.player["resources"]["stamina"]
        before_time = state.time_minutes

        event = practice_technique(
            state,
            "ABILITY_FLUX",
            "TECHNIQUE_PULSE",
            minutes=60,
        )

        technique = state.abilities["ABILITY_FLUX"]["techniques"]["TECHNIQUE_PULSE"]
        self.assertEqual(state.time_minutes, before_time + 60)
        self.assertEqual(state.player["resources"]["focus"], before_focus - 6)
        self.assertEqual(state.player["resources"]["stamina"], before_stamina - 4)
        self.assertEqual(technique["mastery_xp"], 8.0)
        self.assertEqual(technique["stage"], "discovered")
        self.assertEqual(event["type"], "technique_practice")

    def test_practice_technique_uses_diminishing_returns_and_mentor_bonus(self):
        state = self.state()
        first = practice_technique(
            state,
            "ABILITY_FLUX",
            "TECHNIQUE_PULSE",
            minutes=60,
            mentor_bonus=0.5,
        )
        first_gain = (
            first["technique_mastery_after"] - first["technique_mastery_before"]
        )

        state.player["resources"]["focus"] = 100
        state.player["resources"]["stamina"] = 100
        state.abilities["ABILITY_FLUX"]["techniques"]["TECHNIQUE_PULSE"]["mastery_xp"] = 300
        state.abilities["ABILITY_FLUX"]["techniques"]["TECHNIQUE_PULSE"]["stage"] = "mastered"
        second = practice_technique(
            state,
            "ABILITY_FLUX",
            "TECHNIQUE_PULSE",
            minutes=60,
            mentor_bonus=0.5,
        )
        second_gain = (
            second["technique_mastery_after"] - second["technique_mastery_before"]
        )
        self.assertLess(second_gain, first_gain)

    def test_practice_rejects_insufficient_resources_without_partial_mutation(self):
        state = self.state()
        state.player["resources"]["focus"] = 1
        before = dict(state.player["resources"])
        before_time = state.time_minutes
        before_mastery = state.abilities["ABILITY_FLUX"]["techniques"]["TECHNIQUE_PULSE"]["mastery_xp"]

        with self.assertRaises(RuleError):
            practice_technique(
                state,
                "ABILITY_FLUX",
                "TECHNIQUE_PULSE",
                minutes=60,
            )

        self.assertEqual(state.player["resources"], before)
        self.assertEqual(state.time_minutes, before_time)
        self.assertEqual(
            state.abilities["ABILITY_FLUX"]["techniques"]["TECHNIQUE_PULSE"]["mastery_xp"],
            before_mastery,
        )


    def test_player_view_shows_only_discovered_techniques_and_visible_evolutions(self):
        state = self.state()
        state.player["power_resources"]["max_flux"] = 20.0
        ability = state.abilities["ABILITY_FLUX"]
        ability["control"] = 12
        ability["efficiency"] = 8
        ability["evolution_visibility"] = {
            "EVOLUTION_HIDDEN": {"state": "hidden"},
            "EVOLUTION_HINTED": {
                "state": "hinted",
                "label": "Unknown evolution",
                "hint": "A stable pattern may be required.",
            },
            "EVOLUTION_KNOWN": {
                "state": "known",
                "known_requirements": ["mastery", "TECHNIQUE_PULSE"],
            },
        }

        definition = {
            "name": "Flux",
            "resource": {
                "label": "Flux",
                "current_path": "power_resources.flux",
                "max_path": "power_resources.max_flux",
            },
            "techniques": {
                "TECHNIQUE_PULSE": {"name": "Pulse"},
                "TECHNIQUE_SECRET": {"name": "Secret Technique"},
            },
            "evolutions": {
                "EVOLUTION_HIDDEN": {
                    "name": "Hidden Form",
                    "requirements": {"mastery_xp_min": 9999},
                },
                "EVOLUTION_HINTED": {
                    "name": "Hinted Form",
                    "requirements": {"rank_min": 4},
                },
                "EVOLUTION_KNOWN": {
                    "name": "Stable Flux",
                    "requirements": {"knowledge": ["KNOW_SECRET_PATTERN"]},
                },
            },
        }

        view = ability_player_view(state, "ABILITY_FLUX", definition)
        self.assertEqual(view["name"], "Flux")
        self.assertEqual(view["resource"], {"label": "Flux", "current": 12.0, "max": 20.0})
        self.assertEqual(view["control"], 12.0)
        self.assertEqual(view["efficiency"], 8.0)
        self.assertEqual(
            [item["technique_id"] for item in view["techniques"]],
            ["TECHNIQUE_PULSE"],
        )
        self.assertEqual(
            [item["evolution_id"] for item in view["evolutions"]],
            ["EVOLUTION_HINTED", "EVOLUTION_KNOWN"],
        )
        self.assertNotIn("requirements", view["evolutions"][0])
        self.assertNotIn("requirements", view["evolutions"][1])
        self.assertEqual(view["evolutions"][0]["name"], "Unknown evolution")
        self.assertEqual(view["evolutions"][1]["name"], "Stable Flux")

    def test_player_view_reports_cooldown_remaining_without_advancing_time(self):
        state = self.state()
        use_technique(state, "ABILITY_FLUX", "TECHNIQUE_PULSE", self.definition())
        view = ability_player_view(
            state,
            "ABILITY_FLUX",
            {"techniques": {"TECHNIQUE_PULSE": {"name": "Pulse"}}},
        )
        technique = view["techniques"][0]
        self.assertFalse(technique["ready"])
        self.assertEqual(technique["cooldown_remaining_minutes"], 15)
        self.assertEqual(state.time_minutes, 0)

    def test_player_view_rejects_boolean_numeric_fields(self):
        state = self.state()
        state.abilities["ABILITY_FLUX"]["control"] = True
        with self.assertRaises(RuleError):
            ability_player_view(state, "ABILITY_FLUX")

    def test_invalid_technique_definition_is_rejected_before_mutation(self):
        state = self.state()
        before_focus = state.player["resources"]["focus"]
        before_flux = state.player["power_resources"]["flux"]
        before_uses = state.abilities["ABILITY_FLUX"]["techniques"]["TECHNIQUE_PULSE"]["uses"]

        invalid = self.definition()
        invalid["drawbacks"] = [
            {
                "type": "condition",
                "condition_id": "",
                "severity": True,
                "duration_minutes": -1,
            }
        ]
        self.assertTrue(validate_technique_definition(invalid))
        with self.assertRaises(RuleError):
            use_technique(state, "ABILITY_FLUX", "TECHNIQUE_PULSE", invalid)

        self.assertEqual(state.player["resources"]["focus"], before_focus)
        self.assertEqual(state.player["power_resources"]["flux"], before_flux)
        self.assertEqual(
            state.abilities["ABILITY_FLUX"]["techniques"]["TECHNIQUE_PULSE"]["uses"],
            before_uses,
        )

    def test_invalid_evolution_definition_is_rejected_before_mutation(self):
        state = self.state()
        state.knowledge["KNOW_FLUX_PATTERN"] = {}
        gain_technique_mastery(state, "ABILITY_FLUX", "TECHNIQUE_PULSE", 40)
        invalid = {
            "requirements": {
                "rank_min": 2,
                "knowledge": ["KNOW_FLUX_PATTERN"],
                "techniques": {"TECHNIQUE_PULSE": "learned"},
            },
            "result": {
                "form": "bad_form",
                "rank_floor": -1,
                "consume_items": {"ITEM_CORE_SHARD": -1},
                "grant_perks": {"PERK_BAD": "not-an-object"},
            },
        }
        before_inventory = dict(state.inventory)
        before_form = state.abilities["ABILITY_FLUX"].get("form")
        self.assertTrue(validate_evolution_definition(invalid))
        with self.assertRaises(RuleError):
            evolve_ability(state, "ABILITY_FLUX", "EVOLUTION_BAD", invalid)
        self.assertEqual(state.inventory, before_inventory)
        self.assertEqual(state.abilities["ABILITY_FLUX"].get("form"), before_form)
        self.assertNotIn("PERK_BAD", state.perks)

    def test_boolean_power_resource_is_rejected(self):
        state = self.state()
        state.player["power_resources"]["flux"] = True
        with self.assertRaises(RuleError):
            technique_use_status(
                state, "ABILITY_FLUX", "TECHNIQUE_PULSE", self.definition()
            )

    def test_power_requirements_use_effective_attribute_values_with_sets(self):
        state = self.state()
        state.player["attributes"]["will"] = 35
        state.player["conditions"] = {
            "COND_DISTRACTED": {"modifiers": {"attributes.will": -1}}
        }
        state.perks["PERK_FOCUSED"] = {
            "modifiers": {"attributes.will": 3}
        }
        state.equipment = {
            "body": {
                "item_id": "ITEM_ATTUNE_BODY",
                "set_id": "SET_ATTUNE",
                "modifiers": {"attributes.will": 1},
            },
            "hands": {
                "item_id": "ITEM_ATTUNE_HANDS",
                "set_id": "SET_ATTUNE",
                "modifiers": {},
            },
        }
        sets = {
            "SET_ATTUNE": {
                "thresholds": {
                    "2": {"modifiers": {"attributes.will": 2}}
                }
            }
        }

        without_set = technique_use_status(
            state,
            "ABILITY_FLUX",
            "TECHNIQUE_PULSE",
            self.definition(),
        )
        self.assertFalse(without_set["available"])
        self.assertIn("attribute:will", without_set["reasons"])

        with_set = technique_use_status(
            state,
            "ABILITY_FLUX",
            "TECHNIQUE_PULSE",
            self.definition(),
            equipment_sets=sets,
        )
        self.assertTrue(with_set["available"])

    def test_evolution_requirements_use_effective_stats(self):
        state = self.state()
        state.player["attributes"]["will"] = 38
        state.perks["PERK_TEMP_CONTROL"] = {
            "modifiers": {"attributes.will": 2}
        }
        definition = {
            "requirements": {
                "rank_min": 2,
                "attributes": {"will": 40},
            },
            "result": {"form": "effective_threshold_form"},
        }
        status = ability_evolution_status(
            state,
            "ABILITY_FLUX",
            "EVOLUTION_EFFECTIVE",
            definition,
        )
        self.assertTrue(status["available"])

    def test_invalid_technique_mastery_numbers_are_rejected(self):
        state = self.state()
        for value in (True, float("nan"), float("inf"), -1):
            with self.assertRaises(RuleError):
                gain_technique_mastery(
                    state,
                    "ABILITY_FLUX",
                    "TECHNIQUE_PULSE",
                    value,
                )
        with self.assertRaises(RuleError):
            technique_stage(float("nan"))

    def test_fractional_item_requirement_is_rejected(self):
        invalid = self.definition()
        invalid["requirements"]["items"] = {"ITEM_CORE_SHARD": 1.5}
        errors = validate_technique_definition(invalid)
        self.assertTrue(any("must be an integer" in error for error in errors))

    def test_player_view_rejects_unsafe_resource_projection_paths(self):
        state = self.state()
        definition = {
            "resource": {
                "label": "Bad",
                "current_path": "attributes.will",
            }
        }
        with self.assertRaises(RuleError):
            ability_player_view(state, "ABILITY_FLUX", definition)

    def test_player_view_rejects_non_string_known_requirements(self):
        state = self.state()
        state.abilities["ABILITY_FLUX"]["evolution_visibility"] = {
            "EVOLUTION_BAD": {
                "state": "known",
                "known_requirements": [{"hidden": "raw-data"}],
            }
        }
        with self.assertRaises(RuleError):
            ability_player_view(
                state,
                "ABILITY_FLUX",
                {"evolutions": {"EVOLUTION_BAD": {"name": "Bad"}}},
            )

    def test_player_view_rejects_non_finite_or_invalid_projection_state(self):
        state = self.state()
        state.abilities["ABILITY_FLUX"]["control"] = float("nan")
        with self.assertRaises(RuleError):
            ability_player_view(state, "ABILITY_FLUX")

        state = self.state()
        state.abilities["ABILITY_FLUX"]["techniques"]["TECHNIQUE_PULSE"]["uses"] = True
        with self.assertRaises(RuleError):
            ability_player_view(state, "ABILITY_FLUX")

        state = self.state()
        state.player["power_resources"]["flux"] = float("inf")
        with self.assertRaises(RuleError):
            ability_player_view(
                state,
                "ABILITY_FLUX",
                {
                    "resource": {
                        "current_path": "power_resources.flux",
                    }
                },
            )

    def test_discover_ability_rejects_malformed_metadata_before_history_mutation(self):
        state = GameState(seed="s", scene_id="A")
        with self.assertRaises(RuleError):
            discover_ability(state, "", family="perception")
        with self.assertRaises(RuleError):
            discover_ability(state, "ABILITY_BAD", tags="sensory")
        with self.assertRaises(RuleError):
            discover_ability(state, "ABILITY_BAD", data=["not", "mapping"])
        self.assertEqual(state.abilities, {})
        self.assertEqual(state.history, [])

    def test_discover_technique_records_discovery_once(self):
        state = GameState(seed="s", scene_id="A")
        discover_ability(state, "ABILITY_TRACE", family="perception")
        before = len(state.history)
        discover_technique(state, "ABILITY_TRACE", "TECHNIQUE_SCAN")
        self.assertEqual(state.history[-1]["type"], "technique_discovered")
        self.assertEqual(len(state.history), before + 1)
        discover_technique(state, "ABILITY_TRACE", "TECHNIQUE_SCAN")
        self.assertEqual(len(state.history), before + 1)

    def test_practice_rejects_invalid_numeric_inputs_without_mutation(self):
        for kwargs in (
            {"minutes": True},
            {"minutes": 60, "intensity": float("nan")},
            {"minutes": 60, "mentor_bonus": float("inf")},
            {"minutes": 60, "stamina_per_hour": -1},
        ):
            state = self.state()
            before_resources = dict(state.player["resources"])
            before_time = state.time_minutes
            before_mastery = dict(
                state.abilities["ABILITY_FLUX"]["techniques"]["TECHNIQUE_PULSE"]
            )
            with self.assertRaises(RuleError):
                practice_technique(
                    state,
                    "ABILITY_FLUX",
                    "TECHNIQUE_PULSE",
                    **kwargs,
                )
            self.assertEqual(state.player["resources"], before_resources)
            self.assertEqual(state.time_minutes, before_time)
            self.assertEqual(
                state.abilities["ABILITY_FLUX"]["techniques"]["TECHNIQUE_PULSE"],
                before_mastery,
            )

    def test_invalid_cost_path_is_rejected_before_any_mutation(self):
        state = self.state()
        invalid = self.definition()
        invalid["costs"] = {"attributes.will": 1}
        before_player = dict(state.player)
        before_technique = dict(
            state.abilities["ABILITY_FLUX"]["techniques"]["TECHNIQUE_PULSE"]
        )

        errors = validate_technique_definition(invalid)
        self.assertTrue(any("resources.<id> or power_resources.<id>" in e for e in errors))
        with self.assertRaises(RuleError):
            use_technique(state, "ABILITY_FLUX", "TECHNIQUE_PULSE", invalid)

        self.assertEqual(state.player, before_player)
        self.assertEqual(
            state.abilities["ABILITY_FLUX"]["techniques"]["TECHNIQUE_PULSE"],
            before_technique,
        )

    def test_invalid_drawback_modifier_path_is_rejected_before_spending(self):
        state = self.state()
        invalid = self.definition()
        invalid["drawbacks"] = [
            {
                "type": "condition",
                "condition_id": "COND_BAD",
                "severity": 1,
                "tags": ["strain"],
                "modifiers": {"attributes.migth": -1},
            }
        ]
        before_focus = state.player["resources"]["focus"]
        before_flux = state.player["power_resources"]["flux"]

        errors = validate_technique_definition(invalid)
        self.assertTrue(any("modifiers invalid" in e for e in errors))
        with self.assertRaises(RuleError):
            use_technique(state, "ABILITY_FLUX", "TECHNIQUE_PULSE", invalid)

        self.assertEqual(state.player["resources"]["focus"], before_focus)
        self.assertEqual(state.player["power_resources"]["flux"], before_flux)
        self.assertNotIn("COND_BAD", state.player.get("conditions", {}))

    def test_unknown_power_requirement_ids_are_definition_errors(self):
        technique = self.definition()
        technique["requirements"]["attributes"] = {"wil": 1}
        technique["requirements"]["skills"] = {"powerz": 1}
        errors = validate_technique_definition(technique)
        self.assertTrue(any("unknown ID 'wil'" in e for e in errors))
        self.assertTrue(any("unknown ID 'powerz'" in e for e in errors))

        evolution = {
            "requirements": {
                "attributes": {"wil": 1},
                "skills": {"powerz": 1},
            },
            "result": {},
        }
        errors = validate_evolution_definition(evolution)
        self.assertTrue(any("unknown ID 'wil'" in e for e in errors))
        self.assertTrue(any("unknown ID 'powerz'" in e for e in errors))

    def test_corrupt_mastery_state_is_rejected_before_technique_spend(self):
        state = self.state()
        state.abilities["ABILITY_FLUX"]["mastery_xp"] = float("nan")
        before_focus = state.player["resources"]["focus"]
        before_flux = state.player["power_resources"]["flux"]

        with self.assertRaises(RuleError):
            use_technique(
                state,
                "ABILITY_FLUX",
                "TECHNIQUE_PULSE",
                self.definition(),
            )

        self.assertEqual(state.player["resources"]["focus"], before_focus)
        self.assertEqual(state.player["power_resources"]["flux"], before_flux)

    def test_invalid_evolution_perk_modifier_is_rejected_before_form_or_item_mutation(self):
        state = self.state()
        state.inventory["ITEM_CORE_SHARD"] = 2
        definition = {
            "requirements": {},
            "result": {
                "form": "stable",
                "consume_items": {"ITEM_CORE_SHARD": 1},
                "grant_perks": {
                    "PERK_BAD": {
                        "modifiers": {"derived.max_heath": 5},
                        "tags": ["evolution"],
                    }
                },
            },
        }
        before_inventory = dict(state.inventory)
        before_form = state.abilities["ABILITY_FLUX"].get("form")

        errors = validate_evolution_definition(definition)
        self.assertTrue(any("modifiers invalid" in e for e in errors))
        with self.assertRaises(RuleError):
            evolve_ability(
                state,
                "ABILITY_FLUX",
                "EVOLUTION_BAD_PERK",
                definition,
            )

        self.assertEqual(state.inventory, before_inventory)
        self.assertEqual(state.abilities["ABILITY_FLUX"].get("form"), before_form)
        self.assertNotIn("PERK_BAD", state.perks)

if __name__ == "__main__":
    unittest.main()
