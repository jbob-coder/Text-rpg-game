import unittest

from textrpg import GameState, RuleError
from textrpg.social import (
    adjust_relationship,
    eligible_leak_targets,
    execute_leak_event,
    npc_learn,
    relationship_meets,
    set_goal,
    share_knowledge,
    transition_story_state,
    update_goal_progress,
)


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

    def test_leak_event_executes_deterministic_first_candidate(self):
        state = GameState(
            seed="s",
            scene_id="A",
            npcs={
                "NPC_A": {
                    "personality": {"discipline": 10, "honesty": 90},
                    "knowledge": {},
                },
                "NPC_B": {},
                "NPC_C": {},
            },
        )
        npc_learn(state, "NPC_A", "KNOW_X", source="PLAYER", secrecy=1)
        event = execute_leak_event(
            state,
            holder="NPC_A",
            knowledge_id="KNOW_X",
            network={"NPC_A": ["NPC_C", "NPC_B"]},
        )
        self.assertEqual(event["candidates"], ["NPC_B", "NPC_C"])
        self.assertEqual(event["recipients"], ["NPC_B"])
        self.assertIn("KNOW_X", state.npcs["NPC_B"]["knowledge"])
        self.assertNotIn("KNOW_X", state.npcs["NPC_C"]["knowledge"])
        self.assertIn("leak", state.npcs["NPC_B"]["memories"][-1]["tags"])

    def test_leak_event_can_use_explicit_eligible_recipient(self):
        state = GameState(
            seed="s",
            scene_id="A",
            npcs={
                "NPC_A": {
                    "personality": {"discipline": 10, "honesty": 90},
                    "knowledge": {},
                },
                "NPC_B": {},
                "NPC_C": {},
            },
        )
        npc_learn(state, "NPC_A", "KNOW_X", source="PLAYER", secrecy=1)
        event = execute_leak_event(
            state,
            holder="NPC_A",
            knowledge_id="KNOW_X",
            network={"NPC_A": ["NPC_B", "NPC_C"]},
            recipients=["NPC_C"],
            event_id="LEAK_ARCHIVE_RUMOR",
        )
        self.assertEqual(event["event_id"], "LEAK_ARCHIVE_RUMOR")
        self.assertEqual(event["recipients"], ["NPC_C"])
        self.assertIn("KNOW_X", state.npcs["NPC_C"]["knowledge"])

    def test_leak_event_rejects_ineligible_recipient(self):
        state = GameState(
            seed="s",
            scene_id="A",
            npcs={
                "NPC_A": {
                    "personality": {"discipline": 10, "honesty": 90},
                    "knowledge": {},
                },
                "NPC_B": {},
                "NPC_C": {},
            },
        )
        npc_learn(state, "NPC_A", "KNOW_X", source="PLAYER", secrecy=1)
        with self.assertRaises(RuleError):
            execute_leak_event(
                state,
                holder="NPC_A",
                knowledge_id="KNOW_X",
                network={"NPC_A": ["NPC_B"]},
                recipients=["NPC_C"],
            )
        self.assertNotIn("KNOW_X", state.npcs["NPC_C"]["knowledge"])

    def test_relationship_axes_are_bounded_and_evaluated_independently(self):
        state = GameState(
            seed="s",
            scene_id="A",
            relationships={"NPC_A": {"trust": 95, "suspicion": 20}},
        )
        event = adjust_relationship(
            state,
            "NPC_A",
            {"trust": 20, "suspicion": 15},
            source="SCENE_TEST",
        )
        self.assertEqual(state.relationships["NPC_A"]["trust"], 100.0)
        self.assertEqual(state.relationships["NPC_A"]["suspicion"], 35.0)
        self.assertEqual(event["type"], "relationship_change")
        self.assertTrue(
            relationship_meets(
                state,
                "NPC_A",
                minimums={"trust": 80},
                maximums={"suspicion": 40},
            )
        )
        self.assertFalse(
            relationship_meets(
                state,
                "NPC_A",
                minimums={"trust": 80},
                maximums={"suspicion": 30},
            )
        )

    def test_goal_progress_completes_without_replacing_goal_identity(self):
        state = GameState(seed="s", scene_id="A")
        goal = set_goal(
            state,
            "NPC_A",
            "GOAL_FIND_ARCHIVE",
            priority=80,
            progress=25,
            source="story",
        )
        self.assertEqual(goal["status"], "active")
        event = update_goal_progress(
            state,
            "NPC_A",
            "GOAL_FIND_ARCHIVE",
            75,
        )
        self.assertEqual(event["status"], "completed")
        self.assertEqual(
            state.npcs["NPC_A"]["goals"]["GOAL_FIND_ARCHIVE"]["progress"],
            100.0,
        )
        with self.assertRaises(RuleError):
            set_goal(state, "NPC_A", "GOAL_FIND_ARCHIVE")

    def test_story_state_transition_is_guarded(self):
        state = GameState(seed="s", scene_id="A")
        first = transition_story_state(
            state,
            "NPC_A",
            "TRACK_PERSONAL",
            "OPENING",
            allowed_from=[None],
            reason="introduced",
        )
        self.assertEqual(first["from_state"], None)
        self.assertEqual(
            state.npcs["NPC_A"]["story_state"]["TRACK_PERSONAL"],
            "OPENING",
        )
        with self.assertRaises(RuleError):
            transition_story_state(
                state,
                "NPC_A",
                "TRACK_PERSONAL",
                "FINALE",
                allowed_from=["MIDPOINT"],
            )
        self.assertEqual(
            state.npcs["NPC_A"]["story_state"]["TRACK_PERSONAL"],
            "OPENING",
        )

    def test_goal_progress_rejects_closed_goal(self):
        state = GameState(seed="s", scene_id="A")
        set_goal(
            state,
            "NPC_A",
            "GOAL_SHORT",
            progress=100,
            status="completed",
        )
        with self.assertRaises(RuleError):
            update_goal_progress(state, "NPC_A", "GOAL_SHORT", 1)


if __name__ == "__main__":
    unittest.main()
