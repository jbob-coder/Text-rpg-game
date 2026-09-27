import unittest

from textrpg import GameState, RuleError, gain_ability_mastery
from textrpg.powers import (
    ability_evolution_status,
    discover_ability,
    discover_technique,
    evolve_ability,
    gain_technique_mastery,
    practice_technique,
    recover_power_resource,
    technique_discovery_status,
    validate_power_definitions,
    technique_stage,
    technique_use_status,
    use_technique,
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


    def test_power_definition_resource_contract_and_recovery(self):
        definition = {
            "family": "sensory",
            "resource": {
                "path": "power_resources.trace_resonance",
                "maximum": 10,
                "starting": 10,
                "recovery_per_hour": 2,
            },
            "techniques": {},
        }
        self.assertEqual(validate_power_definitions({"ABILITY_TRACE": definition}), [])
        state = GameState(seed="x", scene_id="A")
        discover_ability(state, "ABILITY_TRACE", definition=definition)
        self.assertEqual(state.player["power_resources"]["trace_resonance"], 10)
        state.player["power_resources"]["trace_resonance"] = 6
        event = recover_power_resource(state, "ABILITY_TRACE", definition, minutes=30)
        self.assertEqual(state.player["power_resources"]["trace_resonance"], 7.0)
        self.assertEqual(event["gained"], 1.0)
        self.assertEqual(state.time_minutes, 30)

    def test_invalid_power_resource_definition_is_rejected(self):
        errors = validate_power_definitions({
            "ABILITY_TRACE": {
                "resource": {
                    "path": "resources.focus",
                    "maximum": 10,
                    "starting": 11,
                    "recovery_per_hour": -1,
                },
                "techniques": {},
            }
        })
        self.assertTrue(any("power_resources" in error for error in errors))
        self.assertTrue(any("starting" in error for error in errors))
        self.assertTrue(any("recovery_per_hour" in error for error in errors))


    def test_technique_discovery_requirements_block_until_earned(self):
        state = GameState(
            seed="s",
            scene_id="A",
            player={
                "attributes": {"perception": 45, "will": 45},
                "skills": {"powers": 10},
            },
            inventory={"ITEM_TRACE_LENS": 1},
            flags={"TRACE_RESEARCHED": True},
        )
        discover_ability(state, "ABILITY_TRACE")
        discover_technique(state, "ABILITY_TRACE", "TECHNIQUE_PULSE")
        definition = {
            "discovery_requirements": {
                "rank_min": 1,
                "mastery_xp_min": 100,
                "knowledge": ["KNOW_TRACE_PATTERN"],
                "perks": ["PERK_TRACE_TOLERANCE"],
                "attributes": {"perception": 45, "will": 45},
                "skills": {"powers": 10},
                "flags": {"TRACE_RESEARCHED": True},
                "items": {"ITEM_TRACE_LENS": 1},
                "techniques": {"TECHNIQUE_PULSE": "learned"},
            }
        }

        status = technique_discovery_status(
            state, "ABILITY_TRACE", "TECHNIQUE_DIRECTIONAL", definition
        )
        self.assertFalse(status["available"])
        self.assertIn("rank", status["reasons"])
        self.assertIn("knowledge:KNOW_TRACE_PATTERN", status["reasons"])
        self.assertIn("perk:PERK_TRACE_TOLERANCE", status["reasons"])
        self.assertIn(
            "technique:TECHNIQUE_PULSE:learned", status["reasons"]
        )
        with self.assertRaises(RuleError):
            discover_technique(
                state, "ABILITY_TRACE", "TECHNIQUE_DIRECTIONAL", definition
            )

        gain_ability_mastery(state, "ABILITY_TRACE", 100)
        state.knowledge["KNOW_TRACE_PATTERN"] = {}
        state.perks["PERK_TRACE_TOLERANCE"] = {"source": "training"}
        gain_technique_mastery(state, "ABILITY_TRACE", "TECHNIQUE_PULSE", 40)

        self.assertTrue(
            technique_discovery_status(
                state, "ABILITY_TRACE", "TECHNIQUE_DIRECTIONAL", definition
            )["available"]
        )
        record = discover_technique(
            state, "ABILITY_TRACE", "TECHNIQUE_DIRECTIONAL", definition
        )
        self.assertEqual(record["stage"], "discovered")
        self.assertEqual(record["mastery_xp"], 0.0)

    def test_invalid_discovery_requirement_definition_is_rejected(self):
        errors = validate_power_definitions({
            "ABILITY_TRACE": {
                "techniques": {
                    "TECHNIQUE_DIRECTIONAL": {
                        "discovery_requirements": {
                            "rank_min": -1,
                            "knowledge": ["bad-id"],
                            "items": {"ITEM_X": 0},
                            "techniques": {"TECHNIQUE_X": "impossible"},
                        }
                    }
                }
            }
        })
        self.assertTrue(any("rank_min" in error for error in errors))
        self.assertTrue(any("knowledge" in error for error in errors))
        self.assertTrue(any("quantity" in error for error in errors))
        self.assertTrue(any("unsupported stage" in error for error in errors))


    def test_power_validation_rejects_unknown_and_self_technique_dependencies(self):
        errors = validate_power_definitions({
            "ABILITY_TRACE": {
                "techniques": {
                    "TECHNIQUE_A": {
                        "discovery_requirements": {
                            "techniques": {
                                "TECHNIQUE_A": "learned",
                                "TECHNIQUE_MISSING": "learned",
                            }
                        }
                    }
                }
            }
        })
        self.assertTrue(any("cannot require itself" in error for error in errors))
        self.assertTrue(any("unknown technique" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
