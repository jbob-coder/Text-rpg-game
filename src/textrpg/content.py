from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, fields
from pathlib import Path
from typing import Any, Dict, Mapping

from .core import GameState, RuleError, RulesEngine, validate_game_state_structure
from .json_contract import loads_strict_json
from .stats import validate_player_stats
from .validation import assert_valid_content_pack
from .visuals import assert_valid_character_visuals


@dataclass
class LoadedContentPack:
    content_id: str
    title: str
    canon_status: str
    raw: Dict[str, Any]
    registries: Dict[str, Any]
    state: GameState
    engine: RulesEngine


def content_pack_from_mapping(data: Mapping[str, Any]) -> LoadedContentPack:
    """Validate and instantiate one authored playable content pack."""
    if not isinstance(data, Mapping):
        raise RuleError("Content pack must be an object")

    content_id = data.get("content_id")
    title = data.get("title")
    canon_status = data.get("canon_status", "unspecified")

    if not isinstance(content_id, str) or not content_id:
        raise RuleError("Content pack requires content_id")
    if not isinstance(title, str) or not title.strip():
        raise RuleError("Content pack requires non-empty title")
    if not isinstance(canon_status, str) or not canon_status:
        raise RuleError("Content pack canon_status must be text")

    scenes = data.get("scenes", {})
    quests = data.get("quests", {})
    characters = data.get("characters", {})
    equipment_sets = data.get("equipment_sets", {})
    powers = data.get("powers", {})
    registries = data.get("registries")
    world_map = data.get("world_map")

    if not isinstance(scenes, Mapping) or not scenes:
        raise RuleError("Content pack requires non-empty scenes")
    if not isinstance(quests, Mapping):
        raise RuleError("Content pack quests must be an object")
    if not isinstance(characters, Mapping):
        raise RuleError("Content pack characters must be an object")
    if not isinstance(equipment_sets, Mapping):
        raise RuleError("Content pack equipment_sets must be an object")
    if not isinstance(powers, Mapping):
        raise RuleError("Content pack powers must be an object")
    if registries is not None and not isinstance(registries, Mapping):
        raise RuleError("Content pack registries must be an object")
    if world_map is not None and not isinstance(world_map, Mapping):
        raise RuleError("Content pack world_map must be an object")

    assert_valid_content_pack(scenes, quests, powers, registries, world_map)
    assert_valid_character_visuals(characters)

    initial = data.get("initial_state")
    if not isinstance(initial, Mapping):
        raise RuleError("Content pack requires initial_state")

    allowed = {field.name for field in fields(GameState)}
    unknown = sorted(set(initial) - allowed)
    if unknown:
        raise RuleError(
            "initial_state has unsupported fields: " + ", ".join(unknown)
        )

    state = GameState(**dict(initial))
    validate_game_state_structure(state)
    if state.scene_id not in scenes:
        raise RuleError(
            f"initial_state.scene_id points to unknown scene: {state.scene_id}"
        )

    stat_errors = validate_player_stats(state)
    if stat_errors:
        raise RuleError("Invalid initial player stats:\n- " + "\n- ".join(stat_errors))

    if registries is not None:
        known = {
            category: set(registries.get(category, {}).keys())
            for category in ("knowledge", "perks", "items", "conditions")
            if isinstance(registries.get(category, {}), Mapping)
        }
        initial_refs = {
            "knowledge": state.knowledge.keys(),
            "perks": state.perks.keys(),
            "items": state.inventory.keys(),
            "conditions": state.player.get("conditions", {}).keys()
            if isinstance(state.player.get("conditions", {}), Mapping)
            else (),
        }
        for category, ids in initial_refs.items():
            for stable_id in ids:
                if stable_id not in known.get(category, set()):
                    raise RuleError(
                        f"initial_state references unknown {category} ID: {stable_id}"
                    )

    engine = RulesEngine(
        scenes,
        equipment_sets=equipment_sets,
        quest_definitions=quests,
        power_definitions=powers,
        perk_definitions=(registries or {}).get("perks", {}),
    )

    return LoadedContentPack(
        content_id=content_id,
        title=title,
        canon_status=canon_status,
        raw=dict(data),
        registries=dict(registries or {}),
        state=state,
        engine=engine,
    )


def _apply_room_presence_sidecar(source: Path, data: Any) -> Any:
    """Merge optional authored room-presence records into scene definitions before validation."""
    sidecar = source.with_name(f"{source.stem}_room_presence.json")
    if not sidecar.exists():
        return data
    if not isinstance(data, Mapping):
        return data
    try:
        presence = loads_strict_json(sidecar.read_text(encoding="utf-8"))
    except OSError as exc:
        raise RuleError(f"Could not read room presence sidecar: {sidecar}") from exc
    except ValueError as exc:
        raise RuleError(f"Invalid strict JSON room presence sidecar: {sidecar}") from exc
    if not isinstance(presence, Mapping):
        raise RuleError("Room presence sidecar must be an object keyed by scene ID")

    merged = deepcopy(dict(data))
    scenes = merged.get("scenes")
    if not isinstance(scenes, dict):
        raise RuleError("Room presence sidecar requires content scenes object")
    for scene_id, actors in presence.items():
        if not isinstance(scene_id, str) or not scene_id:
            raise RuleError("Room presence sidecar scene IDs must be non-empty text")
        scene = scenes.get(scene_id)
        if not isinstance(scene, dict):
            raise RuleError(f"Room presence sidecar references unknown scene: {scene_id}")
        if "actors" in scene:
            raise RuleError(f"Room presence sidecar duplicates inline actors for scene: {scene_id}")
        if not isinstance(actors, list):
            raise RuleError(f"Room presence sidecar actors must be a list: {scene_id}")
        scene["actors"] = deepcopy(actors)
    return merged


def load_content_pack(path: str | Path) -> LoadedContentPack:
    """Load UTF-8 JSON authored content and its optional room-presence sidecar safely."""
    source = Path(path)
    try:
        data = loads_strict_json(source.read_text(encoding="utf-8"))
    except OSError as exc:
        raise RuleError(f"Could not read content pack: {source}") from exc
    except ValueError as exc:
        raise RuleError(f"Invalid strict JSON content pack: {source}") from exc
    return content_pack_from_mapping(_apply_room_presence_sidecar(source, data))
