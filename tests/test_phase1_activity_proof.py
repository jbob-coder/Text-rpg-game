from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from textrpg import RuleError, load_content_pack, load_state, save_state
from textrpg.android_bridge import AndroidBridgeError, open_android_session


ROOT = Path(__file__).resolve().parents[1]
SLICE = ROOT / "content" / "vertical_slice_01.json"
ACTIVITY_ID = "TRAIN_POWER_FUNDAMENTALS_TWO_HOURS"

ROUTE_TO_TRACE_STABILIZATION = [
    "TAKE_DEAD_RELAY",
    "USE_MAINTENANCE_SEAL",
    "KEEP_GATE_TWELVE_SECRET",
    "LEAVE_DEPOT_ALONE",
    "CONTINUE_BELOW_GATE_TWELVE",
    "FOLLOW_TRACE_ECHO",
    "PRACTICE_SIGNAL_PULSE_ONE_HOUR",
    "USE_SIGNAL_PULSE_ON_RELAY",
    "RECOVER_TRACE_RESONANCE_THIRTY_MINUTES",
    "BEGIN_TRACE_STABILIZATION_PLAN",
]


def advance_engine_to_training_hub(pack) -> None:
    for choice_id in ROUTE_TO_TRACE_STABILIZATION:
        pack.engine.choose(pack.state, choice_id)
    if pack.state.scene_id != "TRACE_STABILIZATION_HUB":
        raise AssertionError(f"Expected Trace Stabilization Hub, got {pack.state.scene_id}")


def advance_session_to_training_hub(session) -> None:
    for choice_id in ROUTE_TO_TRACE_STABILIZATION:
        session.choose(choice_id)
    if session.state.scene_id != "TRACE_STABILIZATION_HUB":
        raise AssertionError(f"Expected Trace Stabilization Hub, got {session.state.scene_id}")


def projected_skill(view, skill_id: str) -> dict:
    skills = view["status"]["skills"]
    for group in skills.values():
        for skill in group:
            if skill["id"] == skill_id:
                return skill
    raise AssertionError(f"Projected skill not found: {skill_id}")


def projected_resource(view, resource_id: str) -> dict:
    return next(item for item in view["status"]["resources"] if item["id"] == resource_id)


class Phase1ActivityProofTests(unittest.TestCase):
    def test_trace_chamber_training_is_legal_and_commits_authoritative_cost_progress_time(self):
        pack = load_content_pack(SLICE)
        advance_engine_to_training_hub(pack)

        scene = pack.engine.get_scene(pack.state)
        self.assertEqual("TRACE_CHAMBER", scene["location_id"])
        choices = {
            choice["id"]: choice
            for choice in pack.engine.build_scene_view(pack.state)["choices"]
        }
        self.assertIn(ACTIVITY_ID, choices)
        self.assertTrue(choices[ACTIVITY_ID]["enabled"])

        before_skill = pack.state.player["skills"].get("powers", 0.0)
        before_stamina = pack.state.player["resources"]["stamina"]
        before_focus = pack.state.player["resources"]["focus"]
        before_time = pack.state.time_minutes
        before_turn = pack.state.turn
        history_start = len(pack.state.history)

        pack.engine.choose(pack.state, ACTIVITY_ID)

        self.assertEqual(before_time + 120, pack.state.time_minutes)
        self.assertEqual(before_turn + 1, pack.state.turn)
        self.assertAlmostEqual(before_stamina - 16.0, pack.state.player["resources"]["stamina"])
        self.assertAlmostEqual(before_focus - 10.0, pack.state.player["resources"]["focus"])
        self.assertGreater(pack.state.player["skills"]["powers"], before_skill)
        self.assertEqual("TRACE_STABILIZATION_HUB", pack.state.scene_id)

        activity_events = pack.state.history[history_start:]
        training = [event for event in activity_events if event.get("type") == "training"]
        self.assertEqual(1, len(training))
        self.assertEqual("powers", training[0]["skill"])
        self.assertEqual(120, training[0]["minutes"])
        self.assertEqual(pack.state.time_minutes, training[0]["time_minutes"])
        self.assertEqual(ACTIVITY_ID, activity_events[-1]["choice"])

    def test_trace_chamber_training_persists_exact_result_through_save_load(self):
        pack = load_content_pack(SLICE)
        advance_engine_to_training_hub(pack)
        pack.engine.choose(pack.state, ACTIVITY_ID)

        expected = {
            "skill": pack.state.player["skills"]["powers"],
            "stamina": pack.state.player["resources"]["stamina"],
            "focus": pack.state.player["resources"]["focus"],
            "time_minutes": pack.state.time_minutes,
            "scene_id": pack.state.scene_id,
            "turn": pack.state.turn,
            "training_events": [
                event for event in pack.state.history
                if event.get("type") == "training" and event.get("skill") == "powers"
            ],
        }

        with TemporaryDirectory() as directory:
            save_path = Path(directory) / "activity.json"
            save_state(save_path, pack.state)
            loaded = load_state(save_path)

        actual = {
            "skill": loaded.player["skills"]["powers"],
            "stamina": loaded.player["resources"]["stamina"],
            "focus": loaded.player["resources"]["focus"],
            "time_minutes": loaded.time_minutes,
            "scene_id": loaded.scene_id,
            "turn": loaded.turn,
            "training_events": [
                event for event in loaded.history
                if event.get("type") == "training" and event.get("skill") == "powers"
            ],
        }
        self.assertEqual(expected, actual)

    def test_d068_bonus_invalid_timed_condition_rolls_back_whole_authored_activity(self):
        pack = load_content_pack(SLICE)
        advance_engine_to_training_hub(pack)

        # The authored resource requirements remain satisfied, so the failure occurs
        # inside the training/time preflight after RulesEngine.choose has started its
        # transaction rather than at choice availability.
        pack.state.player["conditions"]["COND_CORRUPT_ACTIVITY"] = {
            "duration_minutes": -1,
            "severity": 1,
            "source": "D-068-B",
            "tags": [],
            "modifiers": {},
        }
        choices = {
            choice["id"]: choice
            for choice in pack.engine.build_scene_view(pack.state)["choices"]
        }
        self.assertTrue(choices[ACTIVITY_ID]["enabled"])

        before = deepcopy(pack.state.snapshot())
        with self.assertRaises(RuleError):
            pack.engine.choose(pack.state, ACTIVITY_ID)

        self.assertEqual(before, pack.state.snapshot())

    def test_android_bridge_presents_requests_and_persists_same_activity_without_local_math(self):
        with TemporaryDirectory() as directory:
            save_path = Path(directory) / "slot-0.json"
            session = open_android_session(SLICE, save_path=save_path)
            advance_session_to_training_hub(session)

            before = session.scene_view()
            activity = next(
                choice for choice in before["scene"]["choices"]
                if choice["id"] == ACTIVITY_ID
            )
            self.assertTrue(activity["enabled"])
            self.assertIn("two hours", activity["text"].lower())

            before_skill = projected_skill(before, "powers")["effective"]
            before_stamina = projected_resource(before, "stamina")["current"]
            before_focus = projected_resource(before, "focus")["current"]
            before_time = before["meta"]["time_minutes"]

            after = session.choose(ACTIVITY_ID)

            self.assertEqual(before_time + 120, after["meta"]["time_minutes"])
            self.assertAlmostEqual(
                before_stamina - 16.0,
                projected_resource(after, "stamina")["current"],
            )
            self.assertAlmostEqual(
                before_focus - 10.0,
                projected_resource(after, "focus")["current"],
            )
            self.assertGreater(projected_skill(after, "powers")["effective"], before_skill)

            session.save()
            restored = open_android_session(SLICE, save_path=save_path)
            loaded = restored.load()

            self.assertEqual(after["meta"]["time_minutes"], loaded["meta"]["time_minutes"])
            self.assertEqual(
                projected_skill(after, "powers")["effective"],
                projected_skill(loaded, "powers")["effective"],
            )
            self.assertEqual(
                projected_resource(after, "stamina")["current"],
                projected_resource(loaded, "stamina")["current"],
            )
            self.assertEqual(
                projected_resource(after, "focus")["current"],
                projected_resource(loaded, "focus")["current"],
            )

    def test_android_bridge_locked_activity_rejects_without_mutation(self):
        session = open_android_session(SLICE)
        advance_session_to_training_hub(session)
        session.state.player["resources"]["stamina"] = 15.0

        view = session.scene_view()
        activity = next(
            choice for choice in view["scene"]["choices"]
            if choice["id"] == ACTIVITY_ID
        )
        self.assertFalse(activity["enabled"])
        before = deepcopy(session.state.snapshot())

        with self.assertRaises(AndroidBridgeError) as caught:
            session.choose(ACTIVITY_ID)

        self.assertEqual("CHOICE_ERROR", caught.exception.code)
        self.assertEqual(before, session.state.snapshot())


if __name__ == "__main__":
    unittest.main()
