"""Regression checks for durable quest records at the save/load boundary."""

import json
import unittest
from copy import deepcopy

from textrpg import GameState, RuleError, dumps_state, loads_state


class QuestSaveRecordContractTests(unittest.TestCase):
    def payload_with_quest(self, record):
        return json.dumps({
            "schema_version": 1,
            "seed": "quest-save",
            "scene_id": "SCENE_A",
            "quests": {"QUEST_A": record},
        })

    def test_load_rejects_non_object_quest_records(self):
        for record in (None, [], "bad", 3):
            with self.subTest(record=record):
                with self.assertRaisesRegex(RuleError, "QUEST_A must be an object"):
                    loads_state(self.payload_with_quest(record))

    def test_load_rejects_invalid_quest_stage_and_status(self):
        for field, value, error in (
            ("stage", 3, "stage must be non-empty text"),
            ("stage", "", "stage must be non-empty text"),
            ("status", "paused", "status is invalid"),
            ("status", None, "status is invalid"),
        ):
            with self.subTest(field=field, value=value):
                with self.assertRaisesRegex(RuleError, error):
                    loads_state(self.payload_with_quest({field: value}))

    def test_load_rejects_invalid_objective_and_event_containers(self):
        for field, value, error in (
            ("completed_objectives", {}, "completed_objectives must be a list"),
            ("completed_objectives", [1], "completed_objectives must be a list"),
            ("failed_objectives", ["OBJ_X", None], "failed_objectives must be a list"),
            ("history", {}, "history must be a list of objects"),
            ("history", ["bad-event"], "history must be a list of objects"),
        ):
            with self.subTest(field=field, value=value):
                with self.assertRaisesRegex(RuleError, error):
                    loads_state(self.payload_with_quest({field: value}))

    def test_rejects_invalid_quest_ids_and_runtime_state_without_mutation(self):
        for quest_id in ("", 7):
            with self.subTest(quest_id=quest_id):
                state = GameState(
                    seed="quest-save",
                    scene_id="SCENE_A",
                    quests={quest_id: {"stage": "STAGE_A"}},
                )
                snapshot = deepcopy(state.snapshot())
                with self.assertRaisesRegex(RuleError, "state.quests IDs"):
                    dumps_state(state)
                self.assertEqual(state.snapshot(), snapshot)

    def test_legacy_and_graph_quest_records_round_trip_unchanged(self):
        state = GameState(
            seed="quest-save",
            scene_id="SCENE_A",
            quests={
                # The legacy quest_stage effect only wrote stage and status.
                "QUEST_LEGACY": {"stage": "STAGE_A", "status": "active"},
                "QUEST_GRAPH": {
                    "stage": "STAGE_B",
                    "status": "active",
                    "completed_objectives": ["OBJ_FIRST"],
                    "failed_objectives": [],
                    "history": [
                        {"type": "quest_started", "stage": "STAGE_B"},
                    ],
                },
            },
        )
        restored = loads_state(dumps_state(state))
        self.assertEqual(restored.snapshot(), state.snapshot())


if __name__ == "__main__":
    unittest.main()
