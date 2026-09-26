import unittest

from textrpg import GameState
from textrpg.social import eligible_leak_targets, npc_learn, share_knowledge


class SocialTests(unittest.TestCase):
    def test_private_knowledge_has_owner(self):
        state = GameState(seed="s", scene_id="A")
        npc_learn(state, "NPC_A", "KNOW_SECRET", source="PLAYER", secrecy=5)
        self.assertIn("KNOW_SECRET", state.npcs["NPC_A"]["knowledge"])
        self.assertNotIn("KNOW_SECRET", state.knowledge)

    def test_share_creates_recipient_memory(self):
        state = GameState(seed="s", scene_id="A")
        npc_learn(state, "NPC_A", "KNOW_SECRET", source="PLAYER", secrecy=2)
        share_knowledge(
            state,
            speaker="NPC_A",
            recipient="NPC_B",
            knowledge_id="KNOW_SECRET",
        )
        self.assertIn("KNOW_SECRET", state.npcs["NPC_B"]["knowledge"])
        self.assertTrue(state.npcs["NPC_B"]["memories"])

    def test_leak_candidates_are_deterministic(self):
        state = GameState(
            seed="s",
            scene_id="A",
            npcs={
                "NPC_A": {
                    "personality": {"discipline": 10, "honesty": 90},
                    "knowledge": {},
                    "memories": [],
                    "goals": {},
                    "story_state": {},
                },
                "NPC_B": {},
                "NPC_C": {},
            },
        )
        npc_learn(state, "NPC_A", "KNOW_X", source="PLAYER", secrecy=1)
        targets = eligible_leak_targets(
            state,
            holder="NPC_A",
            knowledge_id="KNOW_X",
            network={"NPC_A": ["NPC_C", "NPC_B", "NPC_B"]},
        )
        self.assertEqual(targets, ["NPC_B", "NPC_C"])


if __name__ == "__main__":
    unittest.main()
