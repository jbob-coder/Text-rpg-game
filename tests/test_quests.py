import unittest

from textrpg import GameState, RuleError, RulesEngine
from textrpg.quests import (
    available_objectives,
    complete_objective,
    fail_objective,
    fail_quest,
    start_quest,
    validate_quest_definitions,
)


class QuestGraphTests(unittest.TestCase):
    def definition(self):
        return {
            "start_stage": "STAGE_INVESTIGATE",
            "stages": {
                "STAGE_INVESTIGATE": {
                    "objectives": {
                        "OBJ_FIND_RECORD": {"required": True},
                        "OBJ_INTERVIEW_WITNESS": {
                            "required": True,
                            "requires_objectives": ["OBJ_FIND_RECORD"],
                        },
                        "OBJ_SEARCH_ROOF": {
                            "required": False,
                            "on_complete": {"next_stage": "STAGE_SECRET_ROUTE"},
                        },
                    },
                    "on_complete": {"next_stage": "STAGE_DECIDE"},
                    "on_fail": {"next_stage": "STAGE_DAMAGE_CONTROL"},
                },
                "STAGE_SECRET_ROUTE": {
                    "objectives": {
                        "OBJ_USE_SECRET_ROUTE": {
                            "on_complete": {"next_stage": "STAGE_DECIDE"}
                        }
                    }
                },
                "STAGE_DAMAGE_CONTROL": {
                    "objectives": {
                        "OBJ_LIMIT_DAMAGE": {
                            "on_complete": {"next_stage": "STAGE_DECIDE"}
                        }
                    }
                },
                "STAGE_DECIDE": {
                    "objectives": {
                        "OBJ_REVEAL": {
                            "on_complete": {"next_stage": "STAGE_COMPLETE"}
                        },
                        "OBJ_CONCEAL": {
                            "on_complete": {"next_stage": "STAGE_COMPLETE"}
                        },
                    }
                },
                "STAGE_COMPLETE": {
                    "terminal": True,
                    "terminal_status": "completed",
                    "objectives": {},
                },
            },
        }

    def state(self):
        return GameState(seed="quest-seed", scene_id="SCENE_A")

    def test_valid_definition_passes_static_validation(self):
        self.assertEqual(
            validate_quest_definitions({"QUEST_ARCHIVE": self.definition()}),
            [],
        )

    def test_invalid_stage_reference_is_reported(self):
        definition = self.definition()
        definition["stages"]["STAGE_INVESTIGATE"]["on_complete"] = {
            "next_stage": "STAGE_MISSING"
        }
        errors = validate_quest_definitions({"QUEST_ARCHIVE": definition})
        self.assertTrue(any("unknown stage" in error for error in errors))

    def test_malformed_objective_metadata_is_reported_without_validator_crash(self):
        definition = self.definition()
        objective = definition["stages"]["STAGE_INVESTIGATE"]["objectives"][
            "OBJ_INTERVIEW_WITNESS"
        ]
        objective["required"] = "yes"
        objective["requires_objectives"] = None

        errors = validate_quest_definitions({"QUEST_ARCHIVE": definition})

        self.assertTrue(any(".required must be a boolean" in error for error in errors))
        self.assertTrue(
            any(".requires_objectives must be a list" in error for error in errors)
        )

    def test_objective_prerequisites_control_availability(self):
        state = self.state()
        definition = self.definition()
        start_quest(state, "QUEST_ARCHIVE", definition)

        self.assertEqual(
            available_objectives(state, "QUEST_ARCHIVE", definition),
            ["OBJ_FIND_RECORD", "OBJ_SEARCH_ROOF"],
        )

        complete_objective(
            state,
            "QUEST_ARCHIVE",
            "OBJ_FIND_RECORD",
            definition,
        )
        self.assertEqual(
            available_objectives(state, "QUEST_ARCHIVE", definition),
            ["OBJ_INTERVIEW_WITNESS", "OBJ_SEARCH_ROOF"],
        )

    def test_all_required_objectives_advance_stage(self):
        state = self.state()
        definition = self.definition()
        start_quest(state, "QUEST_ARCHIVE", definition)

        complete_objective(state, "QUEST_ARCHIVE", "OBJ_FIND_RECORD", definition)
        complete_objective(
            state, "QUEST_ARCHIVE", "OBJ_INTERVIEW_WITNESS", definition
        )

        quest = state.quests["QUEST_ARCHIVE"]
        self.assertEqual(quest["stage"], "STAGE_DECIDE")
        self.assertEqual(quest["completed_objectives"], [])

    def test_optional_objective_can_branch_to_secret_stage(self):
        state = self.state()
        definition = self.definition()
        start_quest(state, "QUEST_ARCHIVE", definition)

        complete_objective(state, "QUEST_ARCHIVE", "OBJ_SEARCH_ROOF", definition)

        self.assertEqual(
            state.quests["QUEST_ARCHIVE"]["stage"],
            "STAGE_SECRET_ROUTE",
        )

    def test_failure_uses_authored_failure_route(self):
        state = self.state()
        definition = self.definition()
        start_quest(state, "QUEST_ARCHIVE", definition)

        fail_objective(state, "QUEST_ARCHIVE", "OBJ_FIND_RECORD", definition)

        self.assertEqual(
            state.quests["QUEST_ARCHIVE"]["stage"],
            "STAGE_DAMAGE_CONTROL",
        )

    def test_terminal_stage_completes_quest(self):
        state = self.state()
        definition = self.definition()
        start_quest(state, "QUEST_ARCHIVE", definition)

        complete_objective(state, "QUEST_ARCHIVE", "OBJ_SEARCH_ROOF", definition)
        complete_objective(
            state, "QUEST_ARCHIVE", "OBJ_USE_SECRET_ROUTE", definition
        )
        complete_objective(state, "QUEST_ARCHIVE", "OBJ_REVEAL", definition)

        self.assertEqual(state.quests["QUEST_ARCHIVE"]["stage"], "STAGE_COMPLETE")
        self.assertEqual(state.quests["QUEST_ARCHIVE"]["status"], "completed")
        self.assertEqual(state.history[-1]["type"], "quest_terminal")

    def test_manual_failure_closes_quest(self):
        state = self.state()
        definition = self.definition()
        start_quest(state, "QUEST_ARCHIVE", definition)
        event = fail_quest(state, "QUEST_ARCHIVE", reason="deadline_expired")
        self.assertEqual(event["type"], "quest_failed")
        self.assertEqual(state.quests["QUEST_ARCHIVE"]["status"], "failed")
        with self.assertRaises(RuleError):
            available_objectives(state, "QUEST_ARCHIVE", definition)

    def test_scene_effect_can_start_quest_graph(self):
        definition = self.definition()
        engine = RulesEngine(
            {
                "SCENE_A": {
                    "choices": [{
                        "id": "START_CASE",
                        "text": "Take the case.",
                        "outcomes": {
                            "default": {
                                "effects": [{
                                    "type": "quest_start",
                                    "quest_id": "QUEST_ARCHIVE",
                                }]
                            }
                        },
                    }]
                }
            },
            quest_definitions={"QUEST_ARCHIVE": definition},
        )
        state = self.state()
        engine.choose(state, "START_CASE")
        self.assertEqual(state.quests["QUEST_ARCHIVE"]["status"], "active")
        self.assertEqual(
            state.quests["QUEST_ARCHIVE"]["stage"],
            "STAGE_INVESTIGATE",
        )

    def test_scene_effect_can_complete_graph_objective_and_advance(self):
        definition = self.definition()
        state = self.state()
        start_quest(state, "QUEST_ARCHIVE", definition)
        complete_objective(state, "QUEST_ARCHIVE", "OBJ_FIND_RECORD", definition)

        engine = RulesEngine(
            {
                "SCENE_A": {
                    "choices": [{
                        "id": "INTERVIEW",
                        "text": "Interview the witness.",
                        "outcomes": {
                            "default": {
                                "effects": [{
                                    "type": "quest_objective_complete",
                                    "quest_id": "QUEST_ARCHIVE",
                                    "objective_id": "OBJ_INTERVIEW_WITNESS",
                                }]
                            }
                        },
                    }]
                }
            },
            quest_definitions={"QUEST_ARCHIVE": definition},
        )
        engine.choose(state, "INTERVIEW")
        self.assertEqual(state.quests["QUEST_ARCHIVE"]["stage"], "STAGE_DECIDE")


    def test_start_quest_rejects_corrupt_history_without_creating_quest(self):
        state = self.state()
        state.history = "corrupt"
        before_quests = dict(state.quests)

        with self.assertRaises(RuleError):
            start_quest(state, "QUEST_ARCHIVE", self.definition())

        self.assertEqual(state.quests, before_quests)

    def test_complete_objective_preflights_quest_history_before_mutation(self):
        state = self.state()
        definition = self.definition()
        start_quest(state, "QUEST_ARCHIVE", definition)
        quest = state.quests["QUEST_ARCHIVE"]
        quest["history"] = "corrupt"
        before_completed = list(quest["completed_objectives"])
        before_state_history = list(state.history)

        with self.assertRaises(RuleError):
            complete_objective(
                state,
                "QUEST_ARCHIVE",
                "OBJ_FIND_RECORD",
                definition,
            )

        self.assertEqual(quest["completed_objectives"], before_completed)
        self.assertEqual(state.history, before_state_history)

    def test_complete_objective_rejects_invalid_definition_without_mutation(self):
        state = self.state()
        definition = self.definition()
        start_quest(state, "QUEST_ARCHIVE", definition)
        broken = self.definition()
        broken["stages"]["STAGE_INVESTIGATE"]["on_complete"] = {
            "next_stage": "STAGE_MISSING"
        }
        quest = state.quests["QUEST_ARCHIVE"]
        before_completed = list(quest["completed_objectives"])
        before_history = list(state.history)

        with self.assertRaises(RuleError):
            complete_objective(
                state,
                "QUEST_ARCHIVE",
                "OBJ_FIND_RECORD",
                broken,
            )

        self.assertEqual(quest["completed_objectives"], before_completed)
        self.assertEqual(state.history, before_history)

    def test_fail_quest_rejects_corrupt_state_history_without_closing_quest(self):
        state = self.state()
        definition = self.definition()
        start_quest(state, "QUEST_ARCHIVE", definition)
        quest = state.quests["QUEST_ARCHIVE"]
        state.history = "corrupt"

        with self.assertRaises(RuleError):
            fail_quest(state, "QUEST_ARCHIVE", reason="test_failure")

        self.assertEqual(quest["status"], "active")


if __name__ == "__main__":
    unittest.main()
