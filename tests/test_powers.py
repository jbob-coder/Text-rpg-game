import unittest

from textrpg import GameState, RuleError, gain_ability_mastery
from textrpg.powers import (
    ability_evolution_status,
    ability_player_view,
    discover_technique,
    evolve_ability,
    gain_technique_mastery,
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

if __name__ == "__main__":
    unittest.main()
