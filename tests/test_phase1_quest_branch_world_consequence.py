from __future__ import annotations

import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from textrpg.android_bridge import create_session


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "vertical_slice_01.json"
FIXTURE = ROOT / "tests" / "fixtures" / "d075_dead_relay_branch_diff.json"

COOPERATIVE_ROUTE = (
    "TAKE_DEAD_RELAY",
    "USE_MAINTENANCE_SEAL",
    "TELL_TAMSIN_GATE_TWELVE",
    "ENTER_GATE_TWELVE_WITH_TAMSIN",
)
SOLO_ROUTE = (
    "TAKE_DEAD_RELAY",
    "USE_MAINTENANCE_SEAL",
    "KEEP_GATE_TWELVE_SECRET",
    "LEAVE_DEPOT_ALONE",
)
GATE_KNOWLEDGE = "KNOW_RELAY_DESTINATION_SERVICE_GATE_12"
SHARED_MEMORY = "MEM_TAMSIN_ENTERED_GATE_TWELVE_WITH_JACK"
TAMSIN_TRACK = "TRACK_RELAY_CASE"
TAMSIN_GOAL = "GOAL_UNDERSTAND_GATE_TWELVE"


def load_fixture() -> dict:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def branch_fingerprint(session, view: dict) -> dict:
    quest = session.state.quests["QUEST_DEAD_RELAY"]
    tamsin = session.state.npcs["NPC_TAMSIN"]
    goal = tamsin.get("goals", {}).get(TAMSIN_GOAL)
    return {
        "quest_status": quest["status"],
        "quest_stage": quest["stage"],
        "route": session.state.flags.get("opening.route"),
        "party_has_tamsin": "NPC_TAMSIN" in session.state.party,
        "tamsin_knows_gate_twelve": GATE_KNOWLEDGE in tamsin.get("knowledge", {}),
        "tamsin_memory_ids": sorted(
            memory["memory_id"]
            for memory in tamsin.get("memories", [])
            if isinstance(memory, dict) and isinstance(memory.get("memory_id"), str)
        ),
        "tamsin_story_state": tamsin.get("story_state", {}).get(TAMSIN_TRACK),
        "tamsin_trust": session.state.relationships["NPC_TAMSIN"]["trust"],
        "tamsin_suspicion": session.state.relationships["NPC_TAMSIN"]["suspicion"],
        "tamsin_goal_progress": None if goal is None else goal.get("progress"),
        "player_safe_choice_ids": [
            choice["id"] for choice in view["scene"]["choices"]
        ],
    }


def durable_branch_fingerprint(session) -> dict:
    view = session.scene_view()
    fingerprint = branch_fingerprint(session, view)
    fingerprint.pop("player_safe_choice_ids")
    return fingerprint


class Phase1QuestBranchWorldConsequenceTests(unittest.TestCase):
    def _complete_and_reload(self, save_path: Path, route: tuple[str, ...]):
        session = create_session(CONTENT, save_path=save_path)
        for choice_id in route:
            session.choose(choice_id)
        self.assertEqual("OPENING_END", session.state.scene_id)
        session.save()

        resumed = create_session(CONTENT, save_path=save_path)
        view = resumed.load()
        self.assertEqual("OPENING_END", resumed.state.scene_id)
        return resumed, view

    def test_dead_relay_resolutions_persist_and_create_player_safe_divergence(self):
        fixture = load_fixture()
        with TemporaryDirectory() as directory:
            root = Path(directory)
            cooperative = create_session(CONTENT)
            solo = create_session(CONTENT)
            self.assertEqual(cooperative.state.snapshot(), solo.state.snapshot())

            cooperative, cooperative_view = self._complete_and_reload(
                root / "cooperative.json",
                COOPERATIVE_ROUTE,
            )
            solo, solo_view = self._complete_and_reload(
                root / "solo.json",
                SOLO_ROUTE,
            )

            common = fixture["common_terminal"]
            for session in (cooperative, solo):
                quest = session.state.quests[fixture["quest_id"]]
                self.assertEqual(common["quest_status"], quest["status"])
                self.assertEqual(common["quest_stage"], quest["stage"])

            cooperative_choices = [
                choice["id"] for choice in cooperative_view["scene"]["choices"]
            ]
            solo_choices = [
                choice["id"] for choice in solo_view["scene"]["choices"]
            ]
            self.assertIn("ASK_TAMSIN_ABOUT_SHARED_ENTRY", cooperative_choices)
            self.assertNotIn("ASK_TAMSIN_ABOUT_SHARED_ENTRY", solo_choices)

            cooperative_encoded = json.dumps(cooperative_view, sort_keys=True)
            self.assertNotIn(SHARED_MEMORY, cooperative_encoded)
            self.assertNotIn('"memories"', cooperative_encoded)

            cooperative_before_navigation = durable_branch_fingerprint(cooperative)
            solo_before_navigation = durable_branch_fingerprint(solo)

            cooperative.choose("RETURN_TO_DISTRICT_BEFORE_TRACE")
            solo.choose("RETURN_TO_DISTRICT_BEFORE_TRACE")
            cooperative.save()
            solo.save()

            cooperative_later = create_session(
                CONTENT,
                save_path=root / "cooperative.json",
            )
            solo_later = create_session(
                CONTENT,
                save_path=root / "solo.json",
            )
            cooperative_later.load()
            solo_later.load()

            self.assertEqual(
                fixture["later_common_checkpoint"],
                cooperative_later.state.scene_id,
            )
            self.assertEqual(
                fixture["later_common_checkpoint"],
                solo_later.state.scene_id,
            )
            self.assertEqual(
                cooperative_before_navigation,
                durable_branch_fingerprint(cooperative_later),
            )
            self.assertEqual(
                solo_before_navigation,
                durable_branch_fingerprint(solo_later),
            )

    def test_normalized_branch_difference_fixture_matches_only_intended_semantics(self):
        fixture = load_fixture()
        with TemporaryDirectory() as directory:
            root = Path(directory)
            cooperative, cooperative_view = self._complete_and_reload(
                root / "cooperative.json",
                COOPERATIVE_ROUTE,
            )
            solo, solo_view = self._complete_and_reload(
                root / "solo.json",
                SOLO_ROUTE,
            )

            cooperative_fingerprint = branch_fingerprint(
                cooperative,
                cooperative_view,
            )
            solo_fingerprint = branch_fingerprint(solo, solo_view)

            expected_cooperative = {
                **fixture["common_terminal"],
                **fixture["cooperative"],
            }
            expected_solo = {
                **fixture["common_terminal"],
                **fixture["solo"],
            }
            self.assertEqual(expected_cooperative, cooperative_fingerprint)
            self.assertEqual(expected_solo, solo_fingerprint)

            actual_diff_keys = sorted(
                key
                for key in cooperative_fingerprint
                if cooperative_fingerprint[key] != solo_fingerprint[key]
            )
            self.assertEqual(
                fixture["expected_semantic_diff_keys"],
                actual_diff_keys,
            )


if __name__ == "__main__":
    unittest.main()
