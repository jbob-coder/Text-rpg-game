import json
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path

from textrpg import (
    GameState,
    RulesEngine,
    add_memory,
    load_content_pack,
    load_state,
    npc_remembers,
    save_state,
    validate_scenes,
)
from textrpg.android_bridge import create_session


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "vertical_slice_01.json"
MEMORY_ID = "MEM_TAMSIN_ENTERED_GATE_TWELVE_WITH_JACK"
REFLECTION_CHOICE = "ASK_TAMSIN_ABOUT_SHARED_ENTRY"


def cooperative_to_opening_end(pack):
    for choice_id in (
        "TAKE_DEAD_RELAY",
        "USE_MAINTENANCE_SEAL",
        "TELL_TAMSIN_GATE_TWELVE",
        "ENTER_GATE_TWELVE_WITH_TAMSIN",
    ):
        pack.engine.choose(pack.state, choice_id)


class TamsinMemoryProofTests(unittest.TestCase):
    def test_npc_remembers_is_read_only(self):
        state = GameState(seed="memory", scene_id="SCENE_A")
        add_memory(
            state,
            "NPC_TAMSIN",
            MEMORY_ID,
            importance=4,
            tags=["gate_twelve", "shared_entry"],
        )
        before = deepcopy(state.snapshot())

        self.assertTrue(npc_remembers(state, "NPC_TAMSIN", MEMORY_ID))
        self.assertFalse(npc_remembers(state, "NPC_TAMSIN", "MEM_OTHER_EVENT"))
        self.assertFalse(npc_remembers(state, "NPC_MISSING", MEMORY_ID))
        self.assertEqual(before, state.snapshot())

    def test_memory_effect_without_tags_matches_validator_defaults(self):
        scenes = {
            "SCENE_A": {
                "title": "A",
                "body": "B",
                "choices": [
                    {
                        "id": "REMEMBER",
                        "text": "Remember",
                        "outcomes": {
                            "default": {
                                "effects": [
                                    {
                                        "type": "npc_memory_add",
                                        "npc": "NPC_TAMSIN",
                                        "memory_id": "MEM_NO_TAGS_REQUIRED",
                                    }
                                ]
                            }
                        },
                    }
                ],
            }
        }
        self.assertEqual([], validate_scenes(scenes))

        state = GameState(seed="memory", scene_id="SCENE_A")
        engine = RulesEngine(scenes)
        engine.choose(state, "REMEMBER")

        memory = state.npcs["NPC_TAMSIN"]["memories"].single if False else state.npcs["NPC_TAMSIN"]["memories"][0]
        self.assertEqual("MEM_NO_TAGS_REQUIRED", memory["memory_id"])
        self.assertEqual([], memory["tags"])

    def test_validation_rejects_malformed_memory_effect(self):
        scenes = {
            "SCENE_A": {
                "title": "A",
                "body": "B",
                "choices": [
                    {
                        "id": "CHOICE_A",
                        "text": "Remember",
                        "outcomes": {
                            "default": {
                                "effects": [
                                    {
                                        "type": "npc_memory_add",
                                        "npc": "NPC_TAMSIN",
                                        "memory_id": "not-stable",
                                        "importance": 0,
                                        "tags": ["ok", ""],
                                    }
                                ]
                            }
                        },
                    }
                ],
            }
        }

        errors = validate_scenes(scenes)

        self.assertTrue(any("memory_id" in error for error in errors))
        self.assertTrue(any("importance" in error for error in errors))
        self.assertTrue(any("tags" in error for error in errors))

    def test_memory_survives_save_and_unlocks_later_reaction(self):
        pack = load_content_pack(CONTENT)
        cooperative_to_opening_end(pack)

        self.assertEqual("OPENING_END", pack.state.scene_id)
        self.assertTrue(npc_remembers(pack.state, "NPC_TAMSIN", MEMORY_ID))
        visible_before_save = {
            choice["id"] for choice in pack.engine.available_choices(pack.state)
        }
        self.assertIn(REFLECTION_CHOICE, visible_before_save)

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "tamsin_memory.json"
            save_state(path, pack.state)
            loaded = load_state(path)

        self.assertTrue(npc_remembers(loaded, "NPC_TAMSIN", MEMORY_ID))
        pack.state = loaded
        visible_after_load = {
            choice["id"] for choice in pack.engine.available_choices(pack.state)
        }
        self.assertIn(REFLECTION_CHOICE, visible_after_load)

        before_respect = pack.state.relationships["NPC_TAMSIN"]["respect"]
        pack.engine.choose(pack.state, REFLECTION_CHOICE)

        self.assertTrue(pack.state.flags["opening.tamsin_shared_entry_reflected"])
        self.assertEqual(
            before_respect + 1,
            pack.state.relationships["NPC_TAMSIN"]["respect"],
        )
        self.assertNotIn(
            REFLECTION_CHOICE,
            {choice["id"] for choice in pack.engine.available_choices(pack.state)},
        )

    def test_memory_route_is_deterministic(self):
        def run_once():
            pack = load_content_pack(CONTENT)
            cooperative_to_opening_end(pack)
            memory = next(
                item
                for item in pack.state.npcs["NPC_TAMSIN"]["memories"]
                if item["memory_id"] == MEMORY_ID
            )
            choices = [
                choice["id"] for choice in pack.engine.available_choices(pack.state)
            ]
            return memory, choices

        self.assertEqual(run_once(), run_once())

    def test_private_memory_is_not_exposed_but_reaction_is_player_safe(self):
        session = create_session(CONTENT)
        for choice_id in (
            "TAKE_DEAD_RELAY",
            "USE_MAINTENANCE_SEAL",
            "TELL_TAMSIN_GATE_TWELVE",
            "ENTER_GATE_TWELVE_WITH_TAMSIN",
        ):
            session.choose(choice_id)

        self.assertTrue(npc_remembers(session.state, "NPC_TAMSIN", MEMORY_ID))
        view = session.scene_view()
        encoded = json.dumps(view, sort_keys=True)

        self.assertIn(
            REFLECTION_CHOICE,
            {choice["id"] for choice in view["scene"]["choices"]},
        )
        self.assertNotIn(MEMORY_ID, encoded)
        self.assertNotIn('"memories"', encoded)
        self.assertNotIn('"goals"', encoded)
        self.assertNotIn('"story_state"', encoded)


if __name__ == "__main__":
    unittest.main()
