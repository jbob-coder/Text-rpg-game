from __future__ import annotations

from typing import Any, Dict, Mapping


class RoomProjectionError(ValueError):
    """Raised when authored room-presence data cannot be projected safely."""


_REQUIRED_TEXT = ("presentation_id", "public_name", "visual_family", "placement_key")
_FORBIDDEN_PRESENTATION_KEYS = {
    "x", "y", "z", "personality", "knowledge", "memories", "goals",
    "story_state", "relationships", "flags", "visible_if", "requires",
}


def _optional_text(value: Any, field: str) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise RoomProjectionError(f"{field} must be non-empty text when present")
    return value


def build_room_projection(
    scene: Mapping[str, Any],
    *,
    location_id: str,
) -> Dict[str, Any]:
    """Project authored scene presence into the version-1 player-safe room contract."""
    if not isinstance(location_id, str) or not location_id.strip():
        raise RoomProjectionError("location_id must be non-empty text")
    if not isinstance(scene, Mapping):
        raise RoomProjectionError("scene must be an object")

    raw_actors = scene.get("actors", [])
    if not isinstance(raw_actors, list):
        raise RoomProjectionError("scene.actors must be a list")

    actors: list[Dict[str, Any]] = []
    seen: set[str] = set()
    for index, raw in enumerate(raw_actors):
        if not isinstance(raw, Mapping):
            raise RoomProjectionError(f"scene.actors[{index}] must be an object")
        forbidden = _FORBIDDEN_PRESENTATION_KEYS.intersection(raw)
        if forbidden:
            raise RoomProjectionError(
                f"scene.actors[{index}] contains forbidden projection fields: "
                + ", ".join(sorted(forbidden))
            )

        for field in _REQUIRED_TEXT:
            value = raw.get(field)
            if not isinstance(value, str) or not value.strip():
                raise RoomProjectionError(
                    f"scene.actors[{index}].{field} must be non-empty text"
                )

        presentation_id = raw["presentation_id"]
        if presentation_id in seen:
            raise RoomProjectionError(f"duplicate room presentation_id: {presentation_id}")
        seen.add(presentation_id)

        visible_tags = raw.get("visible_tags", [])
        if not isinstance(visible_tags, list) or any(
            not isinstance(tag, str) or not tag.strip() for tag in visible_tags
        ):
            raise RoomProjectionError(
                f"scene.actors[{index}].visible_tags must be a list of non-empty text"
            )

        actors.append({
            "presentation_id": presentation_id,
            "known_actor_id": _optional_text(raw.get("actor_id"), "actor_id"),
            "display_name": raw["public_name"],
            "visual_family": raw["visual_family"],
            "placement_key": raw["placement_key"],
            "pose_key": _optional_text(raw.get("pose_key"), "pose_key"),
            "outfit_key": _optional_text(raw.get("outfit_key"), "outfit_key"),
            "visible_tags": list(visible_tags),
            "inspectable": bool(raw.get("inspectable", False)),
            "dialogue_available": bool(raw.get("dialogue_available", False)),
            "actions": [],
        })

    return {
        "projection_version": 1,
        "location_id": location_id,
        "actors": actors,
        "active_speaker_presentation_id": None,
    }
