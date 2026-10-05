from __future__ import annotations

from copy import deepcopy
from pathlib import Path

import pytest

from textrpg.android_bridge import AndroidBridgeError, open_android_session


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


def _room_for(scene_id: str, location_id: str):
    session = open_android_session(CONTENT)
    session.state.scene_id = scene_id
    # Direct fixture navigation must keep the durable location aligned with the
    # authored scene. The production projection deliberately rejects mismatch.
    session.state.flags["location_id"] = location_id
    return session, session.scene_view()["room"]


def test_initial_opening_projects_exactly_support_courier_and_tamsin() -> None:
    session = open_android_session(CONTENT)
    before = deepcopy(session.state.snapshot())

    view = session.scene_view()

    assert view["room"]["projection_version"] == 1
    assert view["room"]["location_id"] == "PLATFORM_NINE"
    assert [actor["presentation_id"] for actor in view["room"]["actors"]] == [
        "NPC_TAMSIN",
        "SUPPORT_WOUNDED_COURIER",
    ]
    courier = next(actor for actor in view["room"]["actors"] if actor["presentation_id"] == "SUPPORT_WOUNDED_COURIER")
    assert courier["known_actor_id"] is None
    assert session.state.snapshot() == before


@pytest.mark.parametrize(
    ("scene_id", "location_id", "placement_key"),
    [
        ("OPENING_DECISION", "PLATFORM_NINE", "PLATFORM_NINE_TAMSIN_RIGHT"),
        ("OPENING_RECOVERY", "RELAY_WORKBENCH", "RELAY_WORKBENCH_TAMSIN_RIGHT"),
        ("OPENING_TUNNEL", "SERVICE_TUNNEL", "SERVICE_TUNNEL_TAMSIN_RIGHT"),
    ],
)
def test_opening_tamsin_presence_equivalence(scene_id: str, location_id: str, placement_key: str) -> None:
    _, room = _room_for(scene_id, location_id)

    assert room["location_id"] == location_id
    assert [(actor["presentation_id"], actor["placement_key"]) for actor in room["actors"]] == [
        ("NPC_TAMSIN", placement_key)
    ]


def test_unrelated_scene_does_not_infer_actor_presence_from_prose_or_location() -> None:
    _, room = _room_for("OPENING_RELAY_CASING", "RELAY_WORKBENCH")
    assert room["actors"] == []


def test_room_payload_redacts_private_npc_and_relationship_state() -> None:
    session = open_android_session(CONTENT)
    view = session.scene_view()
    keys = set(_walk_keys(view["room"]))

    assert PRIVATE_NPC_KEYS.isdisjoint(keys)
    assert "relationships" not in keys
    assert "trust" not in keys
    assert "suspicion" not in keys


def test_invalid_authored_actor_presence_fails_through_player_safe_view_boundary() -> None:
    session = open_android_session(CONTENT)
    scene = session.engine.get_scene(session.state)
    original = scene.get("actors")
    scene["actors"] = [{"presentation_id": "BROKEN"}]
    try:
        with pytest.raises(AndroidBridgeError) as caught:
            session.scene_view()
        assert caught.value.code == "VIEW_ERROR"
        assert "public_name" not in caught.value.public_message
    finally:
        if original is None:
            scene.pop("actors", None)
        else:
            scene["actors"] = original
