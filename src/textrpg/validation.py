from __future__ import annotations

import re
from typing import Any, Dict, Iterable, List, Mapping, Set

from .core import RuleError


STABLE_ID = re.compile(r"^[A-Z][A-Z0-9_]*$")
SUPPORTED_CONDITIONS: Set[str] = {
    "flag",
    "stat_min",
    "stat_max",
    "relationship_min",
    "relationship_max",
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
    "quest_start",
    "quest_objective_complete",
    "quest_objective_fail",
    "quest_fail",
    "npc_learn",
    "npc_goal_create",
    "npc_goal_progress",
    "npc_story_transition",
    "personality",
    "party_add",
    "party_remove",
    "add_perk",
}


def _validate_id(value: Any, label: str, errors: List[str]) -> None:
    if not isinstance(value, str) or not STABLE_ID.fullmatch(value):
        errors.append(f"{label} must be a stable uppercase ID: {value!r}")


def _walk_conditions(conditions: Iterable[Mapping[str, Any]], location: str, errors: List[str]) -> None:
    for index, condition in enumerate(conditions):
        kind = condition.get("type")
        if kind not in SUPPORTED_CONDITIONS:
            errors.append(f"{location}.condition[{index}] has unsupported type {kind!r}")


def _walk_effects(effects: Iterable[Mapping[str, Any]], location: str, errors: List[str]) -> None:
    for index, effect in enumerate(effects):
        kind = effect.get("type")
        if kind not in SUPPORTED_EFFECTS:
            errors.append(f"{location}.effect[{index}] has unsupported type {kind!r}")


def validate_scenes(scenes: Mapping[str, Dict[str, Any]]) -> List[str]:
    """Statically validate authored scene data before it reaches a playthrough."""
    errors: List[str] = []
    scene_ids = set(scenes.keys())
    global_choice_ids: Set[str] = set()

    for scene_id, scene in scenes.items():
        _validate_id(scene_id, "scene_id", errors)
        choices = scene.get("choices", [])
        if not isinstance(choices, list):
            errors.append(f"{scene_id}.choices must be a list")
            continue

        for index, choice in enumerate(choices):
            location = f"{scene_id}.choices[{index}]"
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

            if "check" in choice and "stat" not in choice["check"]:
                errors.append(f"{location}.check must define stat")

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


def validate_content_pack(
    scenes: Mapping[str, Dict[str, Any]],
    quests: Mapping[str, Mapping[str, Any]] | None = None,
) -> List[str]:
    """Validate scenes plus authored quest definitions and their cross-references."""
    from .quests import validate_quest_definitions

    quest_definitions = quests or {}
    errors = list(validate_scenes(scenes))
    errors.extend(validate_quest_definitions(quest_definitions))

    for scene_id, scene in scenes.items():
        for choice_index, choice in enumerate(scene.get("choices", [])):
            for outcome_name, outcome in choice.get("outcomes", {}).items():
                if not isinstance(outcome, Mapping):
                    continue
                for effect_index, effect in enumerate(outcome.get("effects", [])):
                    effect_type = effect.get("type")
                    if effect_type not in {
                        "quest_stage",
                        "quest_start",
                        "quest_objective_complete",
                        "quest_objective_fail",
                        "quest_fail",
                    }:
                        continue

                    location = (
                        f"{scene_id}.choices[{choice_index}]."
                        f"outcomes.{outcome_name}.effect[{effect_index}]"
                    )
                    quest_id = effect.get("quest_id")
                    definition = quest_definitions.get(quest_id)

                    if definition is None:
                        errors.append(
                            f"{location} references unknown quest {quest_id!r}"
                        )
                        continue

                    stages = definition.get("stages", {})

                    if effect_type == "quest_stage":
                        stage_id = effect.get("stage")
                        if stage_id not in stages:
                            errors.append(
                                f"{location} references unknown stage "
                                f"{stage_id!r} for quest {quest_id!r}"
                            )

                    if effect_type in {
                        "quest_objective_complete",
                        "quest_objective_fail",
                    }:
                        objective_id = effect.get("objective_id")
                        matching_stages = [
                            stage_id
                            for stage_id, stage in stages.items()
                            if objective_id in stage.get("objectives", {})
                        ]
                        if not matching_stages:
                            errors.append(
                                f"{location} references unknown objective "
                                f"{objective_id!r} for quest {quest_id!r}"
                            )

    return errors


def assert_valid_content_pack(
    scenes: Mapping[str, Dict[str, Any]],
    quests: Mapping[str, Mapping[str, Any]] | None = None,
) -> None:
    errors = validate_content_pack(scenes, quests)
    if errors:
        raise RuleError("Invalid authored content pack:\n- " + "\n- ".join(errors))
