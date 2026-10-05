from __future__ import annotations

import pytest

from textrpg.core import RuleError
from textrpg.room_projection import build_room_projection


def _tamsin() -> dict:
    return {
        "presentation_id": "NPC_TAMSIN",
        "actor_id": "NPC_TAMSIN",
        "public_name": "Tamsin",
        "visual_family": "NPC_TAMSIN",
        "placement_key": "PLATFORM_NINE_TAMSIN_RIGHT",
        "pose_key": "front",
        "outfit_key": "default",
        "visible_tags": [],
        "inspectable": True,
        "dialogue_available": False,
        "actions": [],
    }


def test_room_projection_is_versioned_detached_and_player_safe() -> None:
    scene = {"location_id": "PLATFORM_NINE", "actors": [_tamsin()]}

    projected = build_room_projection(scene, "PLATFORM_NINE")

    assert projected == {
        "projection_version": 1,
        "location_id": "PLATFORM_NINE",
        "actors": [
            {
                "presentation_id": "NPC_TAMSIN",
                "known_actor_id": "NPC_TAMSIN",
                "display_name": "Tamsin",
                "visual_family": "NPC_TAMSIN",
                "placement_key": "PLATFORM_NINE_TAMSIN_RIGHT",
                "pose_key": "front",
                "outfit_key": "default",
                "visible_tags": [],
                "inspectable": True,
                "dialogue_available": False,
                "actions": [],
            }
        ],
        "active_speaker_presentation_id": None,
    }
    scene["actors"][0]["public_name"] = "Changed later"
    assert projected["actors"][0]["display_name"] == "Tamsin"


def test_room_projection_orders_presentations_deterministically() -> None:
    tamsin = _tamsin()
    courier = {
        "presentation_id": "SUPPORT_WOUNDED_COURIER",
        "public_name": "Wounded courier",
        "visual_family": "SUPPORT_WOUNDED_COURIER",
        "placement_key": "PLATFORM_NINE_COURIER_LEFT",
    }

    projected = build_room_projection(
        {"location_id": "PLATFORM_NINE", "actors": [tamsin, courier]},
        "PLATFORM_NINE",
    )

    assert [actor["presentation_id"] for actor in projected["actors"]] == [
        "NPC_TAMSIN",
        "SUPPORT_WOUNDED_COURIER",
    ]


def test_room_projection_rejects_duplicate_presentations() -> None:
    scene = {"location_id": "PLATFORM_NINE", "actors": [_tamsin(), _tamsin()]}

    with pytest.raises(RuleError, match="duplicate room actor presentation_id"):
        build_room_projection(scene, "PLATFORM_NINE")


def test_room_projection_rejects_location_mismatch() -> None:
    with pytest.raises(RuleError, match="location does not match"):
        build_room_projection(
            {"location_id": "PLATFORM_NINE", "actors": []},
            "SERVICE_TUNNEL",
        )


@pytest.mark.parametrize(
    "forbidden_field",
    ["personality", "knowledge", "memories", "goals", "story_state", "x", "y"],
)
def test_room_projection_rejects_private_or_presentation_only_fields(forbidden_field: str) -> None:
    actor = _tamsin()
    actor[forbidden_field] = {} if forbidden_field not in {"x", "y"} else 12

    with pytest.raises(RuleError, match="unsupported fields"):
        build_room_projection(
            {"location_id": "PLATFORM_NINE", "actors": [actor]},
            "PLATFORM_NINE",
        )


def test_room_projection_rejects_malformed_actor_contract() -> None:
    actor = _tamsin()
    actor["inspectable"] = "yes"

    with pytest.raises(RuleError, match="inspectable must be boolean"):
        build_room_projection(
            {"location_id": "PLATFORM_NINE", "actors": [actor]},
            "PLATFORM_NINE",
        )
