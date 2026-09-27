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
    "not_knows",
    "npc_knows",
    "npc_not_knows",
    "party_has",
    "ability_rank_min",
    "technique_discoverable",
    "has_perk",
    "not_has_perk",
    "technique_stage_min",
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
    "ability_discover",
    "technique_discover",
    "technique_practice",
    "technique_use",
    "power_recover",
    "skill_train",
    "recover_resources",
}


def _validate_id(value: Any, label: str, errors: List[str]) -> None:
    if not isinstance(value, str) or not STABLE_ID.fullmatch(value):
        errors.append(f"{label} must be a stable uppercase ID: {value!r}")


def _walk_conditions(conditions: Iterable[Mapping[str, Any]], location: str, errors: List[str]) -> None:
    for index, condition in enumerate(conditions):
        kind = condition.get("type")
        condition_location = f"{location}.condition[{index}]"
        if kind not in SUPPORTED_CONDITIONS:
            errors.append(f"{condition_location} has unsupported type {kind!r}")
            continue
        if kind == "technique_discoverable":
            _validate_id(
                condition.get("ability_id"),
                f"{condition_location}.ability_id",
                errors,
            )
            _validate_id(
                condition.get("technique_id"),
                f"{condition_location}.technique_id",
                errors,
            )
        if kind == "technique_stage_min":
            _validate_id(
                condition.get("ability_id"),
                f"{condition_location}.ability_id",
                errors,
            )
            _validate_id(
                condition.get("technique_id"),
                f"{condition_location}.technique_id",
                errors,
            )
            if condition.get("stage") not in {
                "discovered",
                "unstable",
                "learned",
                "practiced",
                "mastered",
            }:
                errors.append(
                    f"{condition_location}.stage has unsupported value "
                    f"{condition.get('stage')!r}"
                )


def _walk_effects(effects: Iterable[Mapping[str, Any]], location: str, errors: List[str]) -> None:
    npc_effects = {
        "relationship",
        "npc_learn",
        "npc_goal_create",
        "npc_goal_progress",
        "npc_story_transition",
        "personality",
        "party_add",
        "party_remove",
    }
    power_effects = {
        "ability_discover",
        "technique_discover",
        "technique_practice",
        "technique_use",
        "power_recover",
    }
    for index, effect in enumerate(effects):
        kind = effect.get("type")
        effect_location = f"{location}.effect[{index}]"
        if kind not in SUPPORTED_EFFECTS:
            errors.append(f"{effect_location} has unsupported type {kind!r}")
            continue
        if kind in npc_effects:
            _validate_id(effect.get("npc"), f"{effect_location}.npc", errors)
        if kind in power_effects:
            _validate_id(
                effect.get("ability_id"),
                f"{effect_location}.ability_id",
                errors,
            )
        if kind in {"technique_discover", "technique_practice", "technique_use"}:
            _validate_id(
                effect.get("technique_id"),
                f"{effect_location}.technique_id",
                errors,
            )
        if kind in {"technique_practice", "power_recover", "skill_train", "recover_resources"}:
            minutes = effect.get("minutes")
            minimum = 30 if kind == "technique_practice" else 1
            if not isinstance(minutes, int) or minutes < minimum:
                errors.append(
                    f"{effect_location}.minutes must be an integer >= {minimum}"
                )
        if kind == "skill_train":
            skill = effect.get("skill")
            if not isinstance(skill, str) or not skill:
                errors.append(f"{effect_location}.skill must be non-empty text")


REGISTRY_CATEGORIES = ("knowledge", "perks", "items", "conditions")


def validate_registries(registries: Mapping[str, Mapping[str, Any]]) -> List[str]:
    """Validate optional stable-ID registries used for cross-reference checks."""
    errors: List[str] = []
    if not isinstance(registries, Mapping):
        return ["registries must be an object"]

    for category in registries:
        if category not in REGISTRY_CATEGORIES:
            errors.append(f"registries has unsupported category {category!r}")

    for category in REGISTRY_CATEGORIES:
        records = registries.get(category, {})
        if not isinstance(records, Mapping):
            errors.append(f"registries.{category} must be an object")
            continue
        for stable_id, metadata in records.items():
            _validate_id(stable_id, f"registries.{category} id", errors)
            if not isinstance(metadata, Mapping):
                errors.append(
                    f"registries.{category}.{stable_id} metadata must be an object"
                )
    return errors


def _registry_reference_errors(
    scenes: Mapping[str, Dict[str, Any]],
    powers: Mapping[str, Mapping[str, Any]],
    registries: Mapping[str, Mapping[str, Any]],
) -> List[str]:
    errors: List[str] = []
    known = {
        category: set(registries.get(category, {}).keys())
        if isinstance(registries.get(category, {}), Mapping)
        else set()
        for category in REGISTRY_CATEGORIES
    }

    def require(category: str, stable_id: Any, location: str) -> None:
        if not isinstance(stable_id, str) or stable_id not in known[category]:
            errors.append(
                f"{location} references unknown {category[:-1] if category.endswith('s') else category} "
                f"{stable_id!r}"
            )

    for scene_id, scene in scenes.items():
        for choice_index, choice in enumerate(scene.get("choices", [])):
            for gate_name in ("visible_if", "requires"):
                for index, condition in enumerate(choice.get(gate_name, [])):
                    location = f"{scene_id}.choices[{choice_index}].{gate_name}[{index}]"
                    kind = condition.get("type")
                    if kind in {"knows", "not_knows", "npc_knows", "npc_not_knows"}:
                        require("knowledge", condition.get("knowledge_id"), location)
                    elif kind in {"has_perk", "not_has_perk"}:
                        require("perks", condition.get("perk_id"), location)
                    elif kind == "item_min":
                        require("items", condition.get("item_id"), location)

            for outcome_name, outcome in choice.get("outcomes", {}).items():
                if not isinstance(outcome, Mapping):
                    continue
                for effect_index, effect in enumerate(outcome.get("effects", [])):
                    location = (
                        f"{scene_id}.choices[{choice_index}].outcomes."
                        f"{outcome_name}.effect[{effect_index}]"
                    )
                    kind = effect.get("type")
                    if kind in {"learn", "npc_learn"}:
                        require("knowledge", effect.get("knowledge_id"), location)
                    elif kind == "inventory":
                        require("items", effect.get("item_id"), location)
                    elif kind == "add_perk":
                        require("perks", effect.get("perk_id"), location)

    for ability_id, definition in powers.items():
        if not isinstance(definition, Mapping):
            continue
        for technique_id, technique in definition.get("techniques", {}).items():
            if not isinstance(technique, Mapping):
                continue
            for field_name in ("discovery_requirements", "requirements"):
                requirements = technique.get(field_name, {})
                if not isinstance(requirements, Mapping):
                    continue
                base = f"powers.{ability_id}.{technique_id}.{field_name}"
                for knowledge_id in requirements.get("knowledge", []):
                    require("knowledge", knowledge_id, base)
                for perk_id in requirements.get("perks", []):
                    require("perks", perk_id, base)
                for item_id in requirements.get("items", {}):
                    require("items", item_id, base)
            for index, drawback in enumerate(technique.get("drawbacks", [])):
                if isinstance(drawback, Mapping) and drawback.get("type") == "condition":
                    require(
                        "conditions",
                        drawback.get("condition_id"),
                        f"powers.{ability_id}.{technique_id}.drawbacks[{index}]",
                    )
    return errors


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
    powers: Mapping[str, Mapping[str, Any]] | None = None,
    registries: Mapping[str, Mapping[str, Any]] | None = None,
) -> List[str]:
    """Validate scenes plus quest/power definitions and cross-references."""
    from .powers import validate_power_definitions
    from .quests import validate_quest_definitions

    quest_definitions = quests or {}
    power_definitions = powers or {}
    errors = list(validate_scenes(scenes))
    errors.extend(validate_quest_definitions(quest_definitions))
    errors.extend(validate_power_definitions(power_definitions))
    if registries is not None:
        errors.extend(validate_registries(registries))
        errors.extend(_registry_reference_errors(scenes, power_definitions, registries))

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

    for scene_id, scene in scenes.items():
        for choice_index, choice in enumerate(scene.get("choices", [])):
            for outcome_name, outcome in choice.get("outcomes", {}).items():
                if not isinstance(outcome, Mapping):
                    continue
                for effect_index, effect in enumerate(outcome.get("effects", [])):
                    effect_type = effect.get("type")
                    if effect_type not in {
                        "ability_discover",
                        "technique_discover",
                        "technique_practice",
                        "technique_use",
                        "power_recover",
                    }:
                        continue
                    location = (
                        f"{scene_id}.choices[{choice_index}]."
                        f"outcomes.{outcome_name}.effect[{effect_index}]"
                    )
                    ability_id = effect.get("ability_id")
                    definition = power_definitions.get(ability_id)
                    if definition is None:
                        errors.append(
                            f"{location} references unknown power {ability_id!r}"
                        )
                        continue
                    if effect_type in {
                        "technique_discover",
                        "technique_practice",
                        "technique_use",
                    }:
                        technique_id = effect.get("technique_id")
                        if technique_id not in definition.get("techniques", {}):
                            errors.append(
                                f"{location} references unknown technique "
                                f"{technique_id!r} for power {ability_id!r}"
                            )

    for scene_id, scene in scenes.items():
        for choice_index, choice in enumerate(scene.get("choices", [])):
            for gate_name in ("visible_if", "requires"):
                for condition_index, condition in enumerate(choice.get(gate_name, [])):
                    if condition.get("type") not in {
                        "technique_discoverable",
                        "technique_stage_min",
                    }:
                        continue
                    location = (
                        f"{scene_id}.choices[{choice_index}].{gate_name}."
                        f"condition[{condition_index}]"
                    )
                    ability_id = condition.get("ability_id")
                    definition = power_definitions.get(ability_id)
                    if definition is None:
                        errors.append(
                            f"{location} references unknown power {ability_id!r}"
                        )
                        continue
                    technique_id = condition.get("technique_id")
                    if technique_id not in definition.get("techniques", {}):
                        errors.append(
                            f"{location} references unknown technique "
                            f"{technique_id!r} for power {ability_id!r}"
                        )

    return errors


def assert_valid_content_pack(
    scenes: Mapping[str, Dict[str, Any]],
    quests: Mapping[str, Mapping[str, Any]] | None = None,
    powers: Mapping[str, Mapping[str, Any]] | None = None,
    registries: Mapping[str, Mapping[str, Any]] | None = None,
) -> None:
    errors = validate_content_pack(scenes, quests, powers, registries)
    if errors:
        raise RuleError("Invalid authored content pack:\n- " + "\n- ".join(errors))
