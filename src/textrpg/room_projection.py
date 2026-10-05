from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, Mapping

from .core import RuleError


ROOM_PROJECTION_VERSION = 1

_ALLOWED_ACTOR_KEYS = {
    "presentation_id",
    "actor_id",
    "public_name",
    "visual_family",
    "placement_key",
    "pose_key",
    "outfit_key",
    "visible_tags",
    "inspectable",
    "dialogue_available",
    "actions",
}


def _required_text(record: Mapping[str, Any], key: str) -> str:
    value = record.get(key)
    if not isinstance(value, str) or not value:
        raise RuleError(f"room actor {key} must be non-empty text")
    return value


def _optional_text(record: Mapping[str, Any], key: str) -> str | None:
    value = record.get(key)
    if value is None:
        return None
    if not isinstance(value, str) or not value:
        raise RuleError(f"room actor {key} must be non-empty text when present")
    return value


def _text_list(record: Mapping[str, Any], key: str) -> list[str]:
    value = record.get(key, [])
    if not isinstance(value, list) or any(not isinstance(item, str) or not item for item in value):
        raise RuleError(f"room actor {key} must be a list of non-empty text values")
    return list(value)


def build_room_projection(scene: Mapping[str, Any], location_id: str) -> Dict[str, Any]:
    """Build one detached, player-safe room projection from authored visible presence.

    This function deliberately accepts only the public scene-level actor contract. It never
    receives GameState.npcs and therefore cannot serialize NPC personality, knowledge, memories,
    goals, or story state by accident.
    """
    if not isinstance(scene, Mapping):
        raise RuleError("room projection requires a scene mapping")
    if not isinstance(location_id, str) or not location_id:
        raise RuleError("room projection location_id must be non-empty text")

    authored_location = scene.get("location_id")
    if authored_location is not None and authored_location != location_id:
        raise RuleError("room projection location does not match current scene location")

    raw_actors = scene.get("actors", [])
    if not isinstance(raw_actors, list):
        raise RuleError("scene actors must be a list")

    actors: list[Dict[str, Any]] = []
    seen: set[str] = set()
    for raw in raw_actors:
        if not isinstance(raw, Mapping):
            raise RuleError("scene actor entries must be objects")
        unknown = set(raw) - _ALLOWED_ACTOR_KEYS
        if unknown:
            raise RuleError(f"room actor contains unsupported fields: {sorted(unknown)}")
        if "x" in raw or "y" in raw:
            raise RuleError("room actor records cannot contain presentation coordinates")

        presentation_id = _required_text(raw, "presentation_id")
        if presentation_id in seen:
            raise RuleError(f"duplicate room actor presentation_id: {presentation_id}")
        seen.add(presentation_id)

        inspectable = raw.get("inspectable", False)
        dialogue_available = raw.get("dialogue_available", False)
        if not isinstance(inspectable, bool):
            raise RuleError("room actor inspectable must be boolean")
        if not isinstance(dialogue_available, bool):
            raise RuleError("room actor dialogue_available must be boolean")

        actor = {
            "presentation_id": presentation_id,
            "known_actor_id": _optional_text(raw, "actor_id"),
            "display_name": _required_text(raw, "public_name"),
            "visual_family": _required_text(raw, "visual_family"),
            "placement_key": _required_text(raw, "placement_key"),
            "pose_key": _optional_text(raw, "pose_key"),
            "outfit_key": _optional_text(raw, "outfit_key"),
            "visible_tags": _text_list(raw, "visible_tags"),
            "inspectable": inspectable,
            "dialogue_available": dialogue_available,
            "actions": _text_list(raw, "actions"),
        }
        actors.append(actor)

    actors.sort(key=lambda actor: actor["presentation_id"])
    return deepcopy(
        {
            "projection_version": ROOM_PROJECTION_VERSION,
            "location_id": location_id,
            "actors": actors,
            "active_speaker_presentation_id": None,
        }
    )
