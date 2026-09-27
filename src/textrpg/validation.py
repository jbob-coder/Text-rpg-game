from __future__ import annotations

import re
from math import isfinite
from typing import Any, Dict, Iterable, List, Mapping, Set

from .core import RuleError
from .modifiers import validate_modifier_mapping, validate_modifier_path


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
        if kind == "technique_discoverable":
            _validate_id(
                condition.get("ability_id"),
                f"{item_location}.ability_id",
                errors,
            )
            _validate_id(
                condition.get("technique_id"),
                f"{item_location}.technique_id",
                errors,
            )
        if kind == "technique_stage_min":
            _validate_id(
                condition.get("ability_id"),
                f"{item_location}.ability_id",
                errors,
            )
            _validate_id(
                condition.get("technique_id"),
                f"{item_location}.technique_id",
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
                    f"{item_location}.stage has unsupported value "
                    f"{condition.get('stage')!r}"
                )


def _walk_effects(effects: Any, location: str, errors: List[str]) -> None:
    if not isinstance(effects, list):
        errors.append(f"{location}.effects must be a list")
        return

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
        item_location = f"{location}.effect[{index}]"
        if not isinstance(effect, Mapping):
            errors.append(f"{item_location} must be an object")
            continue

        kind = effect.get("type")
        if kind not in SUPPORTED_EFFECTS:
            errors.append(f"{item_location} has unsupported type {kind!r}")
            continue

        if kind in npc_effects:
            _validate_id(effect.get("npc"), f"{item_location}.npc", errors)

        if kind in power_effects:
            _validate_id(
                effect.get("ability_id"),
                f"{item_location}.ability_id",
                errors,
            )

        if kind in {"technique_discover", "technique_practice", "technique_use"}:
            _validate_id(
                effect.get("technique_id"),
                f"{item_location}.technique_id",
                errors,
            )

        if kind in {"technique_practice", "power_recover", "skill_train", "recover_resources"}:
            minutes = effect.get("minutes")
            minimum = 30 if kind == "technique_practice" else 1
            if (
                isinstance(minutes, bool)
                or not isinstance(minutes, int)
                or minutes < minimum
            ):
                errors.append(
                    f"{item_location}.minutes must be an integer >= {minimum}"
                )

        if kind == "power_recover" and "quality" in effect:
            quality = effect.get("quality")
            if (
                isinstance(quality, bool)
                or not isinstance(quality, (int, float))
                or not isfinite(float(quality))
                or float(quality) < 0
            ):
                errors.append(
                    f"{item_location}.quality must be finite non-negative numeric"
                )

        if kind == "skill_train":
            skill = effect.get("skill")
            if not isinstance(skill, str) or not skill:
                errors.append(f"{item_location}.skill must be non-empty text")

        if kind == "npc_goal_create":
            _validate_id(effect.get("goal_id"), f"{item_location}.goal_id", errors)
            priority = effect.get("priority", 50)
            if (
                isinstance(priority, bool)
                or not isinstance(priority, int)
                or priority < 0
                or priority > 100
            ):
                errors.append(
                    f"{item_location}.priority must be an integer in range 0..100"
                )
            progress = effect.get("progress", 0)
            if (
                isinstance(progress, bool)
                or not isinstance(progress, (int, float))
                or not isfinite(float(progress))
                or float(progress) < 0
                or float(progress) > 100
            ):
                errors.append(
                    f"{item_location}.progress must be finite numeric in range 0..100"
                )

        if kind == "npc_goal_progress":
            _validate_id(effect.get("goal_id"), f"{item_location}.goal_id", errors)
            delta = effect.get("delta")
            if (
                isinstance(delta, bool)
                or not isinstance(delta, (int, float))
                or not isfinite(float(delta))
            ):
                errors.append(f"{item_location}.delta must be finite numeric")
            threshold = effect.get("completion_threshold", 100)
            if (
                isinstance(threshold, bool)
                or not isinstance(threshold, (int, float))
                or not isfinite(float(threshold))
                or float(threshold) <= 0
                or float(threshold) > 100
            ):
                errors.append(
                    f"{item_location}.completion_threshold must be finite numeric in range (0, 100]"
                )

        if kind == "add_perk":
            try:
                validate_modifier_mapping(
                    effect.get("modifiers", {}),
                    source=f"{item_location}.add_perk",
                )
            except ValueError as exc:
                errors.append(f"{item_location} has invalid modifiers: {exc}")

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
        if not isinstance(scene, Mapping):
            continue
        choices = scene.get("choices", [])
        if not isinstance(choices, list):
            continue
        for choice_index, choice in enumerate(choices):
            if not isinstance(choice, Mapping):
                continue
            for gate_name in ("visible_if", "requires"):
                conditions = choice.get(gate_name, [])
                if not isinstance(conditions, list):
                    continue
                for index, condition in enumerate(conditions):
                    if not isinstance(condition, Mapping):
                        continue
                    location = f"{scene_id}.choices[{choice_index}].{gate_name}[{index}]"
                    kind = condition.get("type")
                    if kind in {"knows", "not_knows", "npc_knows", "npc_not_knows"}:
                        require("knowledge", condition.get("knowledge_id"), location)
                    elif kind in {"has_perk", "not_has_perk"}:
                        require("perks", condition.get("perk_id"), location)
                    elif kind == "item_min":
                        require("items", condition.get("item_id"), location)

            outcomes = choice.get("outcomes", {})
            if not isinstance(outcomes, Mapping):
                continue
            for outcome_name, outcome in outcomes.items():
                if not isinstance(outcome, Mapping):
                    continue
                effects = outcome.get("effects", [])
                if not isinstance(effects, list):
                    continue
                for effect_index, effect in enumerate(effects):
                    if not isinstance(effect, Mapping):
                        continue
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
        techniques = definition.get("techniques", {})
        if not isinstance(techniques, Mapping):
            continue
        for technique_id, technique in techniques.items():
            if not isinstance(technique, Mapping):
                continue
            for field_name in ("discovery_requirements", "requirements"):
                requirements = technique.get(field_name, {})
                if not isinstance(requirements, Mapping):
                    continue
                base = f"powers.{ability_id}.{technique_id}.{field_name}"
                knowledge = requirements.get("knowledge", [])
                if isinstance(knowledge, list):
                    for knowledge_id in knowledge:
                        require("knowledge", knowledge_id, base)
                perks = requirements.get("perks", [])
                if isinstance(perks, list):
                    for perk_id in perks:
                        require("perks", perk_id, base)
                items = requirements.get("items", {})
                if isinstance(items, Mapping):
                    for item_id in items:
                        require("items", item_id, base)
            drawbacks = technique.get("drawbacks", [])
            if not isinstance(drawbacks, list):
                continue
            for index, drawback in enumerate(drawbacks):
                if isinstance(drawback, Mapping) and drawback.get("type") == "condition":
                    require(
                        "conditions",
                        drawback.get("condition_id"),
                        f"powers.{ability_id}.{technique_id}.drawbacks[{index}]",
                    )
    return errors

def validate_scenes(scenes: Any) -> List[str]:
    """Statically validate authored scene data before it reaches a playthrough."""
    errors: List[str] = []
    if not isinstance(scenes, Mapping):
        return ["scenes must be an object"]
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

            time_cost = choice.get("time_cost_minutes", 0)
            if (
                isinstance(time_cost, bool)
                or not isinstance(time_cost, int)
                or time_cost < 0
            ):
                errors.append(
                    f"{location}.time_cost_minutes must be a non-negative integer"
                )

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


def validate_content_pack(
    scenes: Mapping[str, Dict[str, Any]],
    quests: Mapping[str, Mapping[str, Any]] | None = None,
    powers: Mapping[str, Mapping[str, Any]] | None = None,
    registries: Mapping[str, Mapping[str, Any]] | None = None,
) -> List[str]:
    """Validate scenes, quest/power definitions, and authored cross-references."""
    from .powers import validate_power_definitions
    from .quests import validate_quest_definitions

    quest_definitions = {} if quests is None else quests
    power_definitions = {} if powers is None else powers
    errors = list(validate_scenes(scenes))
    errors.extend(validate_quest_definitions(quest_definitions))
    errors.extend(validate_power_definitions(power_definitions))

    quest_lookup = quest_definitions if isinstance(quest_definitions, Mapping) else {}
    power_lookup = power_definitions if isinstance(power_definitions, Mapping) else {}
    if registries is not None:
        errors.extend(validate_registries(registries))
        if isinstance(scenes, Mapping):
            errors.extend(
                _registry_reference_errors(
                    scenes,
                    power_lookup,
                    registries,
                )
            )

    if not isinstance(scenes, Mapping):
        return errors

    for scene_id, scene in scenes.items():
        if not isinstance(scene, Mapping):
            continue
        choices = scene.get("choices", [])
        if not isinstance(choices, list):
            continue
        for choice_index, choice in enumerate(choices):
            if not isinstance(choice, Mapping):
                continue
            outcomes = choice.get("outcomes", {})
            if not isinstance(outcomes, Mapping):
                continue
            for outcome_name, outcome in outcomes.items():
                if not isinstance(outcome, Mapping):
                    continue
                effects = outcome.get("effects", [])
                if not isinstance(effects, list):
                    continue
                for effect_index, effect in enumerate(effects):
                    if not isinstance(effect, Mapping):
                        continue
                    effect_type = effect.get("type")
                    location = (
                        f"{scene_id}.choices[{choice_index}]."
                        f"outcomes.{outcome_name}.effect[{effect_index}]"
                    )

                    if effect_type in {
                        "quest_stage",
                        "quest_start",
                        "quest_objective_complete",
                        "quest_objective_fail",
                        "quest_fail",
                    }:
                        quest_id = effect.get("quest_id")
                        definition = quest_lookup.get(quest_id)
                        if definition is None:
                            errors.append(
                                f"{location} references unknown quest {quest_id!r}"
                            )
                        elif isinstance(definition, Mapping):
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
                                    if isinstance(stage, Mapping)
                                    and objective_id in stage.get("objectives", {})
                                ]
                                if not matching_stages:
                                    errors.append(
                                        f"{location} references unknown objective "
                                        f"{objective_id!r} for quest {quest_id!r}"
                                    )

                    if effect_type in {
                        "ability_discover",
                        "technique_discover",
                        "technique_practice",
                        "technique_use",
                        "power_recover",
                    }:
                        ability_id = effect.get("ability_id")
                        definition = power_lookup.get(ability_id)
                        if definition is None:
                            errors.append(
                                f"{location} references unknown power {ability_id!r}"
                            )
                            continue
                        if not isinstance(definition, Mapping):
                            continue

                        if effect_type in {
                            "technique_discover",
                            "technique_practice",
                            "technique_use",
                        }:
                            technique_id = effect.get("technique_id")
                            techniques = definition.get("techniques", {})
                            if (
                                not isinstance(techniques, Mapping)
                                or technique_id not in techniques
                            ):
                                errors.append(
                                    f"{location} references unknown technique "
                                    f"{technique_id!r} for power {ability_id!r}"
                                )

    for scene_id, scene in scenes.items():
        if not isinstance(scene, Mapping):
            continue
        choices = scene.get("choices", [])
        if not isinstance(choices, list):
            continue
        for choice_index, choice in enumerate(choices):
            if not isinstance(choice, Mapping):
                continue
            for gate_name in ("visible_if", "requires"):
                conditions = choice.get(gate_name, [])
                if not isinstance(conditions, list):
                    continue
                for condition_index, condition in enumerate(conditions):
                    if not isinstance(condition, Mapping):
                        continue
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
                    if not isinstance(definition, Mapping):
                        continue
                    technique_id = condition.get("technique_id")
                    techniques = definition.get("techniques", {})
                    if (
                        not isinstance(techniques, Mapping)
                        or technique_id not in techniques
                    ):
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
