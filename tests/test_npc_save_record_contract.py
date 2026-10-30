"""Regression tests for durable NPC shell shapes in JSON saves."""

import json
import unittest

from textrpg import GameState, RuleError, dumps_state, loads_state


class NPCSaveRecordContractTests(unittest.TestCase):
    @staticmethod
    def save_with_npc(record):
        return json.dumps({
            "schema_version": 1,
            "seed": "npc-save",
            "scene_id": "SCENE_A",
            "npcs": {"NPC_A": record},
        })

    def test_load_rejects_non_object_npc_records(self):
        for record in (None, [], "not-an-object", True):
            with self.subTest(record=record):
                with self.assertRaisesRegex(RuleError, "NPC_A must be an object"):
                    loads_state(self.save_with_npc(record))

    def test_load_rejects_invalid_optional_npc_containers(self):
        for field, value in (
            ("personality", []),
            ("knowledge", "corrupt"),
            ("goals", None),
            ("story_state", []),
        ):
            with self.subTest(field=field):
                with self.assertRaisesRegex(
                    RuleError, "state.npcs.NPC_A." + field + " must be an object"
                ):
                    loads_state(self.save_with_npc({field: value}))

    def test_load_rejects_invalid_memory_container_or_entries(self):
        for memories in ("corrupt", {}, ["not-an-event"], [None]):
            with self.subTest(memories=memories):
                with self.assertRaisesRegex(
                    RuleError, "NPC_A.memories must be a list of objects"
                ):
                    loads_state(self.save_with_npc({"memories": memories}))

    def test_bad_npc_keys_and_runtime_records_rejected_without_mutation(self):
        for npc_id in ("", 9):
            with self.subTest(npc_id=npc_id):
                state = GameState(
                    seed="npc-save", scene_id="SCENE_A",
                    npcs={npc_id: {"knowledge": {}}},
                )
                before = state.snapshot()
                with self.assertRaisesRegex(RuleError, "state.npcs IDs"):
                    dumps_state(state)
                self.assertEqual(state.snapshot(), before)

        state = GameState(
            seed="npc-save", scene_id="SCENE_A",
            npcs={"NPC_A": {"memories": "corrupt"}},
        )
        before = state.snapshot()
        with self.assertRaisesRegex(
            RuleError, "NPC_A.memories must be a list of objects"
        ):
            dumps_state(state)
        self.assertEqual(state.snapshot(), before)

    def test_partial_and_full_npc_records_preserve_save_schema(self):
        state = GameState(
            seed="npc-save", scene_id="SCENE_A",
            npcs={
                # Old saves and lazily allocated NPC shells can be partial.
                "NPC_MINIMAL": {},
                "NPC_PARTIAL": {"story_state": {"TRACK_A": "OPEN"}},
                "NPC_FULL": {
                    "personality": {"honesty": 75},
                    "knowledge": {"KNOW_A": {"source": "PLAYER", "secrecy": 1}},
                    "memories": [{"memory_id": "MEM_A", "importance": 1}],
                    "goals": {"GOAL_A": {"status": "paused"}},
                    "story_state": {"TRACK_A": "OPEN"},
                },
            },
        )
        restored = loads_state(dumps_state(state))
        self.assertEqual(restored.snapshot(), state.snapshot())
        self.assertEqual(restored.schema_version, 1)


if __name__ == "__main__":
    unittest.main()
