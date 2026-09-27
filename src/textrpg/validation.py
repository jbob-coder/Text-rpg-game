from __future__ import annotations

import re
from typing import Any, Dict, Iterable, List, Mapping, Set

from .core import RuleError
from .modifiers import validate_modifier_mapping, validate_modifier_path


STABLE_ID = re.compile(r"^[A-Z][A-Z0-9_]*$")
SUPPORTED_CONDITIONS: Set[str] = {
    "flag",
    "stat_min",
    "stat_max",
    "relationship_min",
    "knows",
    "npc_knows",
    "party_has",
    "ability_rank_min",
    "has_perk",
    "item_min",
}
SUPPORTED_EFFECTS: Set[str] = {
    "set_flag",
    "add_player",
    "set_player",
    "relationship",
    "learn",
    "inventory",
    "quest_stage",
    "npc_learn",
    "personality",
    "party_add",
    "party_remove",
    "add_perk",
}


def _validate_id(value: Any, label: str, errors: List[str]) -> None:
    if not isinstance(value, str) or not STABLE_ID.fullmatch(value):
        errors.append(f"{label} must be a stable uppercase ID: {value!r}")


def _walk_conditions(conditions: Any, location: str, errors: List[str]) -> None:
    if not isinstance(conditions, list):
        errors.append(f"{location} must be a list")
        return
    for index, condition in enumerate(conditions):
        item_location = f"{location}.condition[{index}]"
        if not isinstance(condition, Mapping):
            errors.append(f"{item_location} must be an object")
            continue
        kind = condition.get("type")
        if kind not in SUPPORTED_CONDITIONS:
            errors.append(f"{item_location} has unsupported type {kind!r}")
            continue
        if kind in {"stat_min", "stat_max"}:
            try:
                validate_modifier_path(condition.get("path"))
            except ValueError as exc:
                errors.append(f"{item_location} has invalid stat path: {exc}")


def _walk_effects(effects: Any, location: str, errors: List[str]) -> None:
    if not isinstance(effects, list):
        errors.append(f"{location}.effects must be a list")
        return
    for index, effect in enumerate(effects):
        item_location = f"{location}.effect[{index}]"
        if not isinstance(effect, Mapping):
            errors.append(f"{item_location} must be an object")
            continue
        kind = effect.get("type")
        if kind not in SUPPORTED_EFFECTS:
            errors.append(f"{item_location} has unsupported type {kind!r}")
            continue
        if kind == "add_perk":
            try:
                validate_modifier_mapping(
                    effect.get("modifiers", {}),
                    source=f"{item_location}.add_perk",
                )
            except ValueError as exc:
                errors.append(f"{item_location} has invalid modifiers: {exc}")


def validate_scenes(scenes: Mapping[str, Dict[str, Any]]) -> List[str]:
    """Statically validate authored scene data before it reaches a playthrough."""
    errors: List[str] = []
    scene_ids = set(scenes.keys())
    global_choice_ids: Set[str] = set()

    for scene_id, scene in scenes.items():
        _validate_id(scene_id, "scene_id", errors)
        if not isinstance(scene, Mapping):
            errors.append(f"{scene_id} must be an object")
            continue
        choices = scene.get("choices", [])
        if not isinstance(choices, list):
            errors.append(f"{scene_id}.choices must be a list")
            continue

        for index, choice in enumerate(choices):
            location = f"{scene_id}.choices[{index}]"
            if not isinstance(choice, Mapping):
                errors.append(f"{location} must be an object")
                continue
            choice_id = choice.get("id")
            _validate_id(choice_id, f"{location}.id", errors)
            if isinstance(choice_id, str):
                if choice_id in global_choice_ids:
                    errors.append(f"Duplicate choice id: {choice_id}")
                global_choice_ids.add(choice_id)

            if not isinstance(choice.get("text"), str) or not choice.get("text", "").strip():
                errors.append(f"{location}.text must be non-empty")

            _walk_conditions(choice.get("visible_if", []), f"{location}.visible_if", errors)
            _walk_conditions(choice.get("requires", []), f"{location}.requires", errors)

            outcomes = choice.get("outcomes", {})
            if not isinstance(outcomes, dict) or not outcomes:
                errors.append(f"{location}.outcomes must be a non-empty object")
                continue

            if "check" in choice:
                check = choice["check"]
                if not isinstance(check, Mapping):
                    errors.append(f"{location}.check must be an object")
                elif "stat" not in check:
                    errors.append(f"{location}.check must define stat")
                else:
                    try:
                        validate_modifier_path(check.get("stat"))
                    except ValueError as exc:
                        errors.append(f"{location}.check has invalid stat path: {exc}")
                    skill_path = check.get("skill")
                    if skill_path is not None:
                        try:
                            validate_modifier_path(skill_path)
                            if not str(skill_path).startswith("skills."):
                                errors.append(
                                    f"{location}.check skill must use skills.<id>: {skill_path!r}"
                                )
                        except ValueError as exc:
                            errors.append(f"{location}.check has invalid skill path: {exc}")

            for outcome_name, outcome in outcomes.items():
                outcome_location = f"{location}.outcomes.{outcome_name}"
                if not isinstance(outcome, dict):
                    errors.append(f"{outcome_location} must be an object")
                    continue
                _walk_effects(outcome.get("effects", []), outcome_location, errors)
                next_scene = outcome.get("next_scene")
                if next_scene is not None and next_scene not in scene_ids:
                    errors.append(f"{outcome_location} points to unknown scene {next_scene!r}")

            choice_next = choice.get("next_scene")
            if choice_next is not None and choice_next not in scene_ids:
                errors.append(f"{location} points to unknown scene {choice_next!r}")

    return errors


def assert_valid_scenes(scenes: Mapping[str, Dict[str, Any]]) -> None:
    errors = validate_scenes(scenes)
    if errors:
        raise RuleError("Invalid authored content:\n- " + "\n- ".join(errors))
