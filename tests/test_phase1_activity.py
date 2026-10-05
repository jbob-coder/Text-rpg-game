from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from textrpg.android_bridge import AndroidBridgeError, create_session


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "vertical_slice_01.json"
ACTIVITY_ID = "TRAIN_POWER_FUNDAMENTALS_TWO_HOURS"
TRACE_HUB_ROUTE = (
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
)


class Phase1ActivityProofTests(unittest.TestCase):
    def reach_trace_hub(self, session) -> None:
        for choice_id in TRACE_HUB_ROUTE:
            session.choose(choice_id)
        self.assertEqual("TRACE_STABILIZATION_HUB", session.state.scene_id)

    @staticmethod
    def projected_skill(view, skill_id: str):
        groups = view["status"]["skills"]
        for entries in groups.values():
            for entry in entries:
                if entry["id"] == skill_id:
                    return entry
        raise AssertionError(f"Missing projected skill: {skill_id}")

    @staticmethod
    def projected_resource(view, resource_id: str):
        for entry in view["status"]["resources"]:
            if entry["id"] == resource_id:
                return entry
        raise AssertionError(f"Missing projected resource: {resource_id}")

    def test_trace_chamber_activity_commits_time_cost_progress_and_save_load(self):
        with TemporaryDirectory() as directory:
            save_path = Path(directory) / "activity.json"
            session = create_session(CONTENT, save_path=save_path)

            opening_choices = {
                choice["id"] for choice in session.scene_view()["scene"]["choices"]
            }
            self.assertNotIn(ACTIVITY_ID, opening_choices)

            self.reach_trace_hub(session)
            hub = session.scene_view()
            activity = next(
                choice for choice in hub["scene"]["choices"]
                if choice["id"] == ACTIVITY_ID
            )
            self.assertTrue(activity["enabled"])
            self.assertIn("two hours", activity["text"].lower())
            self.assertEqual("TRACE_CHAMBER", hub["meta"]["location"])

            skill_before = float(session.state.player.get("skills", {}).get("powers", 0))
            time_before = session.state.time_minutes
            stamina_before = float(session.state.player["resources"]["stamina"])
            focus_before = float(session.state.player["resources"]["focus"])

            view = session.choose(ACTIVITY_ID)

            self.assertEqual("TRACE_STABILIZATION_HUB", session.state.scene_id)
            self.assertEqual(time_before + 120, session.state.time_minutes)
            self.assertEqual(stamina_before - 16.0, session.state.player["resources"]["stamina"])
            self.assertEqual(focus_before - 10.0, session.state.player["resources"]["focus"])
            self.assertGreater(session.state.player["skills"]["powers"], skill_before)
            self.assertEqual(2.0, session.state.player["skills"]["powers"])

            training_event = session.state.history[-2]
            choice_event = session.state.history[-1]
            self.assertEqual("training", training_event["type"])
            self.assertEqual("powers", training_event["skill"])
            self.assertEqual(120, training_event["minutes"])
            self.assertEqual(ACTIVITY_ID, choice_event["choice"])

            projected = self.projected_skill(view, "powers")
            self.assertEqual(2.0, projected["base"])
            self.assertEqual(2.0, projected["effective"])
            self.assertEqual(session.state.time_minutes, view["meta"]["time_minutes"])
            self.assertEqual(
                session.state.player["resources"]["stamina"],
                self.projected_resource(view, "stamina")["current"],
            )
            self.assertEqual(
                session.state.player["resources"]["focus"],
                self.projected_resource(view, "focus")["current"],
            )

            session.save()
            restored = create_session(CONTENT, save_path=save_path)
            loaded = restored.load()

            self.assertEqual(session.state.time_minutes, restored.state.time_minutes)
            self.assertEqual(
                session.state.player["skills"]["powers"],
                restored.state.player["skills"]["powers"],
            )
            self.assertEqual(
                session.state.player["resources"],
                restored.state.player["resources"],
            )
            self.assertEqual(
                session.state.player["skills"]["powers"],
                self.projected_skill(loaded, "powers")["base"],
            )

    def test_activity_requirement_failure_spends_nothing(self):
        session = create_session(CONTENT)
        self.reach_trace_hub(session)
        session.state.player["resources"]["stamina"] = 15.0
        before = deepcopy(session.state.snapshot())

        activity = next(
            choice for choice in session.scene_view()["scene"]["choices"]
            if choice["id"] == ACTIVITY_ID
        )
        self.assertFalse(activity["enabled"])

        with self.assertRaises(AndroidBridgeError) as caught:
            session.choose(ACTIVITY_ID)

        self.assertEqual("CHOICE_ERROR", caught.exception.code)
        self.assertEqual(before, session.state.snapshot())

    def test_activity_rolls_back_when_time_preflight_fails(self):
        session = create_session(CONTENT)
        self.reach_trace_hub(session)
        conditions = session.state.player.setdefault("conditions", {})
        conditions["COND_D068_BAD_TIMER"] = {
            "severity": 1,
            "duration_minutes": True,
            "source": "D068_TEST",
            "tags": [],
            "modifiers": {},
            "applied_at": session.state.time_minutes,
        }
        before = deepcopy(session.state.snapshot())

        with self.assertRaises(AndroidBridgeError) as caught:
            session.choose(ACTIVITY_ID)

        self.assertEqual("CHOICE_ERROR", caught.exception.code)
        self.assertEqual(before, session.state.snapshot())


if __name__ == "__main__":
    unittest.main()
