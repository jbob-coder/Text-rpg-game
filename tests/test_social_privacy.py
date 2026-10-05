from __future__ import annotations

from pathlib import Path
import unittest

from textrpg.android_bridge import create_session


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "vertical_slice_01.json"


def walk_keys(value):
    if isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from walk_keys(item)
    elif isinstance(value, list):
        for item in value:
            yield from walk_keys(item)


class SocialPrivacyProjectionTests(unittest.TestCase):
    def test_tamsin_private_memory_does_not_cross_player_safe_bridge(self):
        session = create_session(CONTENT)
        session.choose("TAKE_DEAD_RELAY")
        session.choose("USE_MAINTENANCE_SEAL")
        view = session.choose("TELL_TAMSIN_GATE_TWELVE")

        self.assertIn(
            "MEM_TAMSIN_PLAYER_SHARED_GATE_TWELVE",
            {
                memory["memory_id"]
                for memory in session.state.npcs["NPC_TAMSIN"]["memories"]
            },
        )

        visible_choices = {
            choice["id"]: choice["text"]
            for choice in view["scene"]["choices"]
        }
        self.assertIn("ENTER_GATE_TWELVE_WITH_TAMSIN", visible_choices)
        self.assertIn(
            "earlier trust",
            visible_choices["ENTER_GATE_TWELVE_WITH_TAMSIN"],
        )

        rendered = repr(view)
        self.assertNotIn("MEM_TAMSIN_PLAYER_SHARED_GATE_TWELVE", rendered)
        self.assertNotIn("KNOW_RELAY_DESTINATION_SERVICE_GATE_12", rendered)
        self.assertNotIn("GOAL_UNDERSTAND_GATE_TWELVE", rendered)

        keys = set(walk_keys(view))
        self.assertNotIn("memories", keys)
        self.assertNotIn("knowledge", keys)
        self.assertNotIn("goals", keys)
        self.assertNotIn("story_state", keys)
        self.assertNotIn("personality", keys)


if __name__ == "__main__":
    unittest.main()
