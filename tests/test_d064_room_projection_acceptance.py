from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import unittest

from textrpg.android_bridge import AndroidBridgeError, create_session


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "vertical_slice_01.json"
PRIVATE_NPC_KEYS = {"personality", "knowledge", "memories", "goals", "story_state"}


def _walk_keys(value):
    if isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from _walk_keys(item)
    elif isinstance(value, list):
        for item in value:
            yield from _walk_keys(item)


def _room_for(scene_id: str):
    session = create_session(CONTENT)
    session.state.scene_id = scene_id
    return session, session.scene_view()["room"]


class D064RoomProjectionAcceptanceTests(unittest.TestCase):
    def test_initial_opening_projects_exactly_support_courier_and_tamsin(self) -> None:
        session = create_session(CONTENT)
        before = deepcopy(session.state.snapshot())

        view = session.scene_view()

        self.assertEqual(1, view["room"]["projection_version"])
        self.assertEqual("PLATFORM_NINE", view["room"]["location_id"])
        self.assertEqual(
            ["NPC_TAMSIN", "SUPPORT_WOUNDED_COURIER"],
            [actor["presentation_id"] for actor in view["room"]["actors"]],
        )
        courier = next(
            actor
            for actor in view["room"]["actors"]
            if actor["presentation_id"] == "SUPPORT_WOUNDED_COURIER"
        )
        self.assertIsNone(courier["known_actor_id"])
        self.assertEqual(before, session.state.snapshot())

    def test_opening_tamsin_presence_equivalence(self) -> None:
        cases = (
            ("OPENING_DECISION", "PLATFORM_NINE", "PLATFORM_NINE_TAMSIN_RIGHT"),
            ("OPENING_RECOVERY", "RELAY_WORKBENCH", "RELAY_WORKBENCH_TAMSIN_RIGHT"),
            ("OPENING_TUNNEL", "SERVICE_TUNNEL", "SERVICE_TUNNEL_TAMSIN_RIGHT"),
        )
        for scene_id, location_id, placement_key in cases:
            with self.subTest(scene_id=scene_id):
                _, room = _room_for(scene_id)
                self.assertEqual(location_id, room["location_id"])
                self.assertEqual(
                    [("NPC_TAMSIN", placement_key)],
                    [
                        (actor["presentation_id"], actor["placement_key"])
                        for actor in room["actors"]
                    ],
                )

    def test_unrelated_scene_does_not_infer_actor_presence_from_prose_or_location(self) -> None:
        _, room = _room_for("OPENING_RELAY_CASING")
        self.assertEqual([], room["actors"])

    def test_room_payload_redacts_private_npc_and_relationship_state(self) -> None:
        session = create_session(CONTENT)
        view = session.scene_view()
        keys = set(_walk_keys(view["room"]))

        self.assertTrue(PRIVATE_NPC_KEYS.isdisjoint(keys))
        self.assertNotIn("relationships", keys)
        self.assertNotIn("trust", keys)
        self.assertNotIn("suspicion", keys)

    def test_invalid_authored_actor_presence_fails_through_player_safe_view_boundary(self) -> None:
        session = create_session(CONTENT)
        scene = session.engine.get_scene(session.state)
        original = scene.get("actors")
        scene["actors"] = [{"presentation_id": "BROKEN"}]
        try:
            with self.assertRaises(AndroidBridgeError) as caught:
                session.scene_view()
            self.assertEqual("VIEW_ERROR", caught.exception.code)
            self.assertNotIn("public_name", caught.exception.public_message)
        finally:
            if original is None:
                scene.pop("actors", None)
            else:
                scene["actors"] = original


if __name__ == "__main__":
    unittest.main()
