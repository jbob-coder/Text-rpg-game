import json
import unittest
from pathlib import Path

from textrpg import GameState, RuleError, RulesEngine


ROOT = Path(__file__).resolve().parents[1]


def load_engine():
    data = json.loads((ROOT / "content" / "sample_scene.json").read_text(encoding="utf-8"))
    return RulesEngine(data["scenes"])


def state(seed="test-seed"):
    return GameState(
        seed=seed,
        scene_id="SAMPLE_ARCHIVE_ENTRY",
        player={
            "attributes": {"intellect": 55},
            "skills": {"technical_systems": 12},
            "resources": {"focus": 50},
        },
        relationships={"NPC_MARA": {"trust": 25}},
        knowledge={"KNOW_CIPHER_SIGNATURE": {"source": "earlier_scene"}},
        inventory={"ITEM_CIPHER_KEY": 1},
    )


class RulesEngineTests(unittest.TestCase):
    def test_visibility_and_requirements(self):
        engine = load_engine()
        s = state()
        ids = {c["id"]: c for c in engine.available_choices(s)}
        self.assertTrue(ids["ASK_MARA_PRIVATELY"]["enabled"])
        self.assertTrue(ids["USE_CIPHER_KEY"]["enabled"])

    def test_hidden_choice_stays_hidden_without_knowledge(self):
        engine = load_engine()
        s = state()
        s.knowledge.clear()
        ids = {c["id"] for c in engine.available_choices(s)}
        self.assertNotIn("USE_CIPHER_KEY", ids)

    def test_choice_persists_knowledge_and_relationship(self):
        engine = load_engine()
        s = state()
        event = engine.choose(s, "ASK_MARA_PRIVATELY")
        self.assertIn("KNOW_ARCHIVE_ACCIDENT", s.knowledge)
        self.assertEqual(s.relationships["NPC_MARA"]["trust"], 27)
        self.assertEqual(s.time_minutes, 6)
        self.assertEqual(event["next_scene"], "SAMPLE_ARCHIVE_DECISION")

    def test_deterministic_check(self):
        engine = load_engine()
        a = state("same-seed")
        b = state("same-seed")
        ea = engine.choose(a, "FORCE_PANEL")
        eb = engine.choose(b, "FORCE_PANEL")
        self.assertEqual(ea["check"], eb["check"])

    def test_locked_choice_rejected(self):
        engine = load_engine()
        s = state()
        s.relationships["NPC_MARA"]["trust"] = 0
        with self.assertRaises(RuleError):
            engine.choose(s, "ASK_MARA_PRIVATELY")


class ExtendedStateTests(unittest.TestCase):
    def test_equipment_and_perks_modify_checks_without_mutating_base_stat(self):
        engine = load_engine()
        s = state("equipment-seed")
        s.equipment["hands"] = {
            "item_id": "ITEM_TOOL_GLOVES",
            "modifiers": {"attributes.intellect": 4},
        }
        s.perks["PERK_METHODICAL"] = {
            "source": "training",
            "modifiers": {"skills.technical_systems": 3},
        }
        event = engine.choose(s, "FORCE_PANEL")
        self.assertEqual(s.player["attributes"]["intellect"], 55)
        self.assertEqual(event["check"]["base"], 59.0)
        self.assertEqual(event["check"]["skill"], 15.0)

    def test_npc_knowledge_and_party_conditions(self):
        engine = RulesEngine({
            "A": {"choices": [{
                "id": "PRIVATE_GROUP_LINE",
                "text": "Use a fact only this group can act on.",
                "visible_if": [
                    {"type": "party_has", "npc": "NPC_MARA"},
                    {"type": "npc_knows", "npc": "NPC_MARA", "knowledge_id": "KNOW_ROUTE"}
                ],
                "outcomes": {"default": {"effects": []}}
            }]}
        })
        s = GameState(
            seed="x",
            scene_id="A",
            party=["NPC_MARA"],
            npcs={"NPC_MARA": {"knowledge": {"KNOW_ROUTE": {}}}},
        )
        self.assertEqual([c["id"] for c in engine.available_choices(s)], ["PRIVATE_GROUP_LINE"])

    def test_personality_effect_is_bounded(self):
        engine = RulesEngine({"A": {"choices": [{
            "id": "PRESSURE",
            "text": "Pressure NPC",
            "outcomes": {
                "default": {
                    "effects": [
                        {"type": "personality", "npc": "NPC_MARA", "axis": "caution", "value": 250}
                    ]
                }
            }
        }]}})
        s = GameState(seed="x", scene_id="A")
        engine.choose(s, "PRESSURE")
        self.assertEqual(s.npcs["NPC_MARA"]["personality"]["caution"], 100)

    def test_conditions_and_set_bonuses_modify_effective_values_once(self):
        engine = RulesEngine(
            {
                "A": {
                    "choices": [{
                        "id": "TEST_CHECK",
                        "text": "Resolve an effective-stat check.",
                        "check": {
                            "stat": "attributes.intellect",
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
            },
            equipment_sets={
                "SET_ANALYST": {
                    "thresholds": {
                        "2": {"modifiers": {"attributes.intellect": 4}},
                    }
                }
            },
        )
        s = GameState(
            seed="x",
            scene_id="A",
            player={
                "attributes": {"intellect": 55},
                "conditions": {
                    "COND_CONCUSSION": {
                        "modifiers": {"attributes.intellect": -3},
                    }
                },
            },
            equipment={
                "head": {
                    "item_id": "ITEM_VISOR",
                    "set_id": "SET_ANALYST",
                    "modifiers": {"attributes.intellect": 1},
                },
                "body": {
                    "item_id": "ITEM_COAT",
                    "set_id": "SET_ANALYST",
                    "modifiers": {"attributes.intellect": 1},
                },
            },
        )
        event = engine.choose(s, "TEST_CHECK")
        self.assertEqual(s.player["attributes"]["intellect"], 55)
        self.assertEqual(event["check"]["base"], 58.0)

    def test_relationship_max_can_gate_authored_choice(self):
        engine = RulesEngine({
            "A": {
                "choices": [{
                    "id": "LOW_SUSPICION_LINE",
                    "text": "Speak while suspicion is still low.",
                    "requires": [{
                        "type": "relationship_max",
                        "npc": "NPC_A",
                        "axis": "suspicion",
                        "value": 30,
                    }],
                    "outcomes": {"default": {"effects": []}},
                }]
            }
        })
        s = GameState(
            seed="x",
            scene_id="A",
            relationships={"NPC_A": {"suspicion": 20}},
        )
        choice = engine.available_choices(s)[0]
        self.assertTrue(choice["enabled"])
        s.relationships["NPC_A"]["suspicion"] = 40
        choice = engine.available_choices(s)[0]
        self.assertFalse(choice["enabled"])

    def test_relationship_effect_is_bounded(self):
        engine = RulesEngine({
            "A": {
                "choices": [{
                    "id": "TRUST_EVENT",
                    "text": "Apply a large relationship change.",
                    "outcomes": {
                        "default": {
                            "effects": [{
                                "type": "relationship",
                                "npc": "NPC_A",
                                "axis": "trust",
                                "value": 250,
                            }]
                        }
                    },
                }]
            }
        })
        s = GameState(
            seed="x",
            scene_id="A",
            relationships={"NPC_A": {"trust": 10}},
        )
        engine.choose(s, "TRUST_EVENT")
        self.assertEqual(s.relationships["NPC_A"]["trust"], 100.0)


    def test_negative_knowledge_conditions_are_first_class_gates(self):
        engine = RulesEngine({
            "A": {
                "choices": [
                    {
                        "id": "PLAYER_DOES_NOT_KNOW",
                        "text": "Visible before the player learns.",
                        "visible_if": [{
                            "type": "not_knows",
                            "knowledge_id": "KNOW_X",
                        }],
                        "outcomes": {"default": {"effects": []}},
                    },
                    {
                        "id": "NPC_DOES_NOT_KNOW",
                        "text": "Visible before the NPC learns.",
                        "visible_if": [{
                            "type": "npc_not_knows",
                            "npc": "NPC_A",
                            "knowledge_id": "KNOW_X",
                        }],
                        "outcomes": {"default": {"effects": []}},
                    },
                ]
            }
        })
        state = GameState(seed="x", scene_id="A", npcs={"NPC_A": {}})
        ids = {choice["id"] for choice in engine.available_choices(state)}
        self.assertEqual(ids, {"PLAYER_DOES_NOT_KNOW", "NPC_DOES_NOT_KNOW"})

        state.knowledge["KNOW_X"] = {}
        state.npcs["NPC_A"]["knowledge"] = {"KNOW_X": {}}
        self.assertEqual(engine.available_choices(state), [])

    def test_scene_effects_can_drive_npc_goal_and_story_state(self):
        engine = RulesEngine({
            "A": {
                "choices": [{
                    "id": "SOCIAL_STATE",
                    "text": "Create and advance authored NPC state.",
                    "outcomes": {
                        "default": {
                            "effects": [
                                {
                                    "type": "npc_story_transition",
                                    "npc": "NPC_A",
                                    "track_id": "TRACK_CASE",
                                    "to_state": "INVOLVED",
                                    "allowed_from": [None],
                                },
                                {
                                    "type": "npc_goal_create",
                                    "npc": "NPC_A",
                                    "goal_id": "GOAL_CASE",
                                    "priority": 80,
                                    "progress": 10,
                                },
                                {
                                    "type": "npc_goal_progress",
                                    "npc": "NPC_A",
                                    "goal_id": "GOAL_CASE",
                                    "delta": 25,
                                },
                            ]
                        }
                    },
                }]
            }
        })
        state = GameState(seed="x", scene_id="A")
        engine.choose(state, "SOCIAL_STATE")
        self.assertEqual(
            state.npcs["NPC_A"]["story_state"]["TRACK_CASE"],
            "INVOLVED",
        )
        self.assertEqual(
            state.npcs["NPC_A"]["goals"]["GOAL_CASE"]["progress"],
            35.0,
        )


    def test_choice_time_advances_and_expires_timed_conditions(self):
        engine = RulesEngine({
            "A": {
                "choices": [{
                    "id": "WAIT",
                    "text": "Wait five minutes.",
                    "time_cost_minutes": 5,
                    "outcomes": {"default": {"effects": []}},
                }]
            }
        })
        state = GameState(
            seed="x",
            scene_id="A",
            player={
                "conditions": {
                    "COND_SHORT": {
                        "duration_minutes": 5,
                        "severity": 1,
                        "source": "test",
                        "tags": [],
                        "modifiers": {},
                    }
                }
            },
        )
        engine.choose(state, "WAIT")
        self.assertEqual(state.time_minutes, 5)
        self.assertNotIn("COND_SHORT", state.player["conditions"])


    def test_scene_effects_can_discover_and_practice_power_gradually(self):
        engine = RulesEngine({
            "A": {
                "choices": [{
                    "id": "DISCOVER",
                    "text": "Notice the latent pattern.",
                    "outcomes": {
                        "default": {
                            "effects": [
                                {
                                    "type": "ability_discover",
                                    "ability_id": "ABILITY_TRACE_ECHO",
                                    "family": "perception",
                                    "form": "latent",
                                },
                                {
                                    "type": "technique_discover",
                                    "ability_id": "ABILITY_TRACE_ECHO",
                                    "technique_id": "TECHNIQUE_SIGNAL_PULSE",
                                },
                            ],
                            "next_scene": "B",
                        }
                    },
                }]
            },
            "B": {
                "choices": [{
                    "id": "PRACTICE",
                    "text": "Practice for one hour.",
                    "outcomes": {
                        "default": {
                            "effects": [{
                                "type": "technique_practice",
                                "ability_id": "ABILITY_TRACE_ECHO",
                                "technique_id": "TECHNIQUE_SIGNAL_PULSE",
                                "minutes": 60,
                            }]
                        }
                    },
                }]
            },
        })
        state = GameState(
            seed="x",
            scene_id="A",
            player={"resources": {"focus": 20.0, "stamina": 20.0}},
        )
        engine.choose(state, "DISCOVER")
        ability = state.abilities["ABILITY_TRACE_ECHO"]
        self.assertEqual(ability["mastery_xp"], 0.0)
        self.assertEqual(
            ability["techniques"]["TECHNIQUE_SIGNAL_PULSE"]["mastery_xp"],
            0.0,
        )

        engine.choose(state, "PRACTICE")
        self.assertEqual(state.time_minutes, 60)
        self.assertEqual(
            ability["techniques"]["TECHNIQUE_SIGNAL_PULSE"]["mastery_xp"],
            8.0,
        )
        self.assertEqual(
            ability["techniques"]["TECHNIQUE_SIGNAL_PULSE"]["stage"],
            "discovered",
        )


    def test_technique_discoverable_condition_tracks_runtime_requirements(self):
        power_definitions = {
            "ABILITY_TRACE": {
                "techniques": {
                    "TECHNIQUE_DIRECTIONAL": {
                        "discovery_requirements": {
                            "rank_min": 1,
                            "knowledge": ["KNOW_TRACE_PATTERN"],
                        }
                    }
                }
            }
        }
        engine = RulesEngine(
            {
                "A": {
                    "choices": [{
                        "id": "DISCOVER_DIRECTIONAL",
                        "text": "Study the directional pattern.",
                        "requires": [{
                            "type": "technique_discoverable",
                            "ability_id": "ABILITY_TRACE",
                            "technique_id": "TECHNIQUE_DIRECTIONAL",
                        }],
                        "outcomes": {"default": {"effects": []}},
                    }]
                }
            },
            power_definitions=power_definitions,
        )
        state = GameState(
            seed="x",
            scene_id="A",
            abilities={"ABILITY_TRACE": {"rank": 0, "mastery_xp": 0, "techniques": {}}},
        )
        self.assertFalse(engine.available_choices(state)[0]["enabled"])
        state.abilities["ABILITY_TRACE"]["rank"] = 1
        state.knowledge["KNOW_TRACE_PATTERN"] = {}
        self.assertTrue(engine.available_choices(state)[0]["enabled"])


    def test_technique_stage_and_negative_perk_conditions(self):
        engine = RulesEngine({
            "A": {"choices": [{
                "id": "RESEARCH",
                "text": "Research after learning the technique.",
                "requires": [
                    {
                        "type": "technique_stage_min",
                        "ability_id": "ABILITY_TRACE",
                        "technique_id": "TECHNIQUE_PULSE",
                        "stage": "learned",
                    },
                    {
                        "type": "not_has_perk",
                        "perk_id": "PERK_TOLERANCE",
                    },
                ],
                "outcomes": {"default": {"effects": []}},
            }]}
        })
        state = GameState(
            seed="x",
            scene_id="A",
            abilities={
                "ABILITY_TRACE": {
                    "techniques": {
                        "TECHNIQUE_PULSE": {
                            "stage": "unstable",
                            "mastery_xp": 20,
                        }
                    }
                }
            },
        )
        self.assertFalse(engine.available_choices(state)[0]["enabled"])
        state.abilities["ABILITY_TRACE"]["techniques"]["TECHNIQUE_PULSE"][
            "stage"
        ] = "learned"
        self.assertTrue(engine.available_choices(state)[0]["enabled"])
        state.perks["PERK_TOLERANCE"] = {}
        self.assertFalse(engine.available_choices(state)[0]["enabled"])

    def test_scene_effects_can_train_skill_and_recover_resources(self):
        engine = RulesEngine({
            "A": {"choices": [{
                "id": "TRAIN",
                "text": "Train.",
                "outcomes": {
                    "default": {
                        "effects": [{
                            "type": "skill_train",
                            "skill": "powers",
                            "minutes": 120,
                        }],
                        "next_scene": "B",
                    }
                },
            }]},
            "B": {"choices": [{
                "id": "REST",
                "text": "Recover.",
                "outcomes": {
                    "default": {
                        "effects": [{
                            "type": "recover_resources",
                            "minutes": 480,
                        }]
                    }
                },
            }]},
        })
        state = GameState(
            seed="x",
            scene_id="A",
            player={
                "attributes": {
                    "might": 30,
                    "agility": 30,
                    "endurance": 30,
                    "intellect": 40,
                    "will": 40,
                    "perception": 40,
                    "presence": 30,
                },
                "skills": {},
                "resources": {
                    "health": 100,
                    "stamina": 100,
                    "focus": 80,
                    "resolve": 50,
                },
            },
        )
        engine.choose(state, "TRAIN")
        self.assertGreater(state.player["skills"]["powers"], 0)
        stamina_after_training = state.player["resources"]["stamina"]
        focus_after_training = state.player["resources"]["focus"]
        engine.choose(state, "REST")
        self.assertGreater(
            state.player["resources"]["stamina"], stamina_after_training
        )
        self.assertGreater(
            state.player["resources"]["focus"], focus_after_training
        )
        self.assertEqual(state.time_minutes, 600)


if __name__ == "__main__":
    unittest.main()
