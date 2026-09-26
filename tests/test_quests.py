import unittest

from textrpg import GameState, RuleError
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


if __name__ == "__main__":
    unittest.main()
