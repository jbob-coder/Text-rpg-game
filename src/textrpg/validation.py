from __future__ import annotations

import re
from math import isfinite
from typing import Any, Dict, Iterable, List, Mapping, Set

from .core import RuleError, validate_resource_requirement
from .equipment import validate_item_definition
from .modifiers import validate_modifier_mapping, validate_modifier_path


STABLE_ID = re.compile(r"^[A-Z][A-Z0-9_]*$")
SUPPORTED_CONDITIONS: Set[str] = {
    "flag",
    "stat_min",
    "stat_max",
    "resource_min",
    "relationship_min",
    "relationship_max",
    "knows",
    "not_knows",
    "npc_knows",
    "npc_not_knows",
    "npc_remembers",
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
    "npc_memory_add",
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
        if kind == "resource_min":
            try:
                validate_resource_requirement(condition)
            except RuleError as exc:
                errors.append(f"{item_location} has invalid resource requirement: {exc}")
        if kind == "npc_remembers":
            _validate_id(condition.get("npc"), f"{item_location}.npc", errors)
            _validate_id(
                condition.get("memory_id"),
                f"{item_location}.memory_id",
                errors,
            )
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
        if kind == "item_min":
            quantity = condition.get("quantity", 1)
            if (
                isinstance(quantity, bool)
                or not isinstance(quantity, int)
                or quantity <= 0
            ):
                errors.append(
                    f"{item_location}.quantity must be a positive integer"
                )


def _walk_effects(effects: Any, location: str, errors: List[str]) -> None:
    if not isinstance(effects, list):
        errors.append(f"{location}.effects must be a list")
        return

    npc_effects = {
        "relationship",
        "npc_learn",
        "npc_memory_add",
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

        if kind == "inventory":
            quantity = effect.get("quantity")
            if (
                isinstance(quantity, bool)
                or not isinstance(quantity, int)
                or quantity == 0
            ):
                errors.append(
                    f"{item_location}.quantity must be a non-zero integer"
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

        if kind == "npc_memory_add":
            _validate_id(
                effect.get("memory_id"),
                f"{item_location}.memory_id",
                errors,
            )
            importance = effect.get("importance", 1)
            if (
                isinstance(importance, bool)
                or not isinstance(importance, int)
                or importance < 1
                or importance > 5
            ):
                errors.append(
                    f"{item_location}.importance must be an integer in range 1..5"
                )
            tags = effect.get("tags", [])
            if (
                not isinstance(tags, list)
                or not all(isinstance(tag, str) and tag for tag in tags)
            ):
                errors.append(
                    f"{item_location}.tags must be a list of non-empty strings"
                )
            data = effect.get("data")
            if data is not None and not isinstance(data, Mapping):
                errors.append(f"{item_location}.data must be an object")

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
            if "visible" in effect and not isinstance(effect["visible"], bool):
                errors.append(f"{item_location}.visible must be boolean")
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
            elif category == "items":
                try:
                    validate_item_definition(stable_id, metadata)
                except RuleError as exc:
                    errors.append(f"registries.items.{stable_id} is invalid: {exc}")
            elif category == "perks" and "player_visible" in metadata:
                if not isinstance(metadata["player_visible"], bool):
                    errors.append(f"registries.perks.{stable_id}.player_visible must be boolean")
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


def validate_world_map(
    world_map: Any,
    scenes: Mapping[str, Dict[str, Any]],
) -> List[str]:
    """Validate authored map graph and optional scene destinations."""
    errors: List[str] = []
    if world_map is None:
        return errors
    if not isinstance(world_map, Mapping):
        return ["world_map must be an object"]

    nodes = world_map.get("nodes", {})
    edges = world_map.get("edges", [])
    if not isinstance(nodes, Mapping):
        return ["world_map.nodes must be an object"]
    if not isinstance(edges, list):
        errors.append("world_map.edges must be a list")
        edges = []

    node_ids: set[str] = set()
    scene_ids = set(scenes.keys()) if isinstance(scenes, Mapping) else set()

    for location_id, node in nodes.items():
        location = f"world_map.nodes.{location_id}"
        _validate_id(location_id, "world_map node id", errors)
        if isinstance(location_id, str):
            node_ids.add(location_id)
        if not isinstance(node, Mapping):
            errors.append(f"{location} must be an object")
            continue

        for axis in ("x", "y"):
            value = node.get(axis)
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not isfinite(float(value))
                or float(value) < 0
                or float(value) > 100
            ):
                errors.append(
                    f"{location}.{axis} must be finite numeric in range 0..100"
                )

        scene_id = node.get("scene_id")
        if scene_id is not None:
            if not isinstance(scene_id, str) or not scene_id:
                errors.append(f"{location}.scene_id must be non-empty text")
            elif scene_id not in scene_ids:
                errors.append(
                    f"{location}.scene_id references unknown scene {scene_id!r}"
                )

        discover_flag = node.get("discover_flag")
        if discover_flag is not None and (
            not isinstance(discover_flag, str) or not discover_flag
        ):
            errors.append(f"{location}.discover_flag must be non-empty text")

    for index, edge in enumerate(edges):
        location = f"world_map.edges[{index}]"
        if not isinstance(edge, Mapping):
            errors.append(f"{location} must be an object")
            continue
        start = edge.get("from")
        end = edge.get("to")
        if start not in node_ids:
            errors.append(f"{location}.from references unknown node {start!r}")
        if end not in node_ids:
            errors.append(f"{location}.to references unknown node {end!r}")
        travel_minutes = edge.get("travel_minutes", 10)
        if (
            isinstance(travel_minutes, bool)
            or not isinstance(travel_minutes, int)
            or travel_minutes < 0
        ):
            errors.append(
                f"{location}.travel_minutes must be a non-negative integer"
            )

    if isinstance(scenes, Mapping):
        for scene_id, scene in scenes.items():
            if not isinstance(scene, Mapping):
                continue
            location_id = scene.get("location_id")
            if (
                location_id is not None
                and isinstance(location_id, str)
                and location_id not in node_ids
            ):
                errors.append(
                    f"scene {scene_id!r} references unknown world_map node "
                    f"{location_id!r}"
                )

    return errors


_COMBAT_ACTION_FIELDS = {
    "action_id",
    "category",
    "cost",
    "range_min",
    "range_max",
    "requires_los",
    "requires_detection",
    "requires_identification",
    "allows_last_known_position",
    "allows_blind_area_targeting",
    "tags",
}
_COMBAT_ARCHETYPE_FIELDS = {
    "archetype_id",
    "action_ids",
    "footprint",
    "tags",
    "metadata",
}
_ENCOUNTER_FIELDS = {
    "encounter_id",
    "map_id",
    "location_id",
    "title",
    "trigger",
    "participants",
    "deployment",
    "objective_set",
    "retreat_policy",
    "ai_profiles",
    "aftermath_profile",
    "time_cost_minutes",
    "canon_status",
    "action_ids",
    "archetype_ids",
    "metadata",
}
_ENCOUNTER_PARTICIPANT_FIELDS = {
    "actor_id",
    "persistent_ref",
    "archetype_id",
    "faction_id",
    "action_ids",
    "deployment_zone",
    "required",
    "tags",
}


def _unknown_field_errors(
    record: Mapping[str, Any],
    allowed: Set[str],
    label: str,
) -> List[str]:
    unknown = sorted(set(record) - allowed, key=str)
    if not unknown:
        return []
    return [
        f"{label} has unsupported fields: "
        + ", ".join(str(field) for field in unknown)
    ]


def _validate_text_list(value: Any, label: str, errors: List[str]) -> List[str]:
    if not isinstance(value, list):
        errors.append(f"{label} must be a list")
        return []
    result: List[str] = []
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item:
            errors.append(f"{label}[{index}] must be non-empty text")
            continue
        result.append(item)
    if len(set(result)) != len(result):
        errors.append(f"{label} cannot contain duplicates")
    return result


def validate_tactical_maps(tactical_maps: Any) -> List[str]:
    """Validate strict authored tactical maps and canonical topology."""

    from .combat_schema import parse_tactical_map_definition

    if not isinstance(tactical_maps, Mapping):
        return ["tactical_maps must be an object"]
    errors: List[str] = []
    for map_id, definition in tactical_maps.items():
        if not isinstance(map_id, str):
            errors.append("tactical map IDs must be text")
            continue
        try:
            parse_tactical_map_definition(map_id, definition)
        except ValueError as exc:
            errors.append(str(exc))
    return errors


def validate_combat_actions(combat_actions: Any) -> List[str]:
    """Validate D-069 action definitions without resolving action behavior."""

    if not isinstance(combat_actions, Mapping):
        return ["combat_actions must be an object"]
    errors: List[str] = []
    for action_id, raw in combat_actions.items():
        _validate_id(action_id, "combat action id", errors)
        label = f"combat_actions.{action_id}"
        if not isinstance(raw, Mapping):
            errors.append(f"{label} must be an object")
            continue
        errors.extend(_unknown_field_errors(raw, _COMBAT_ACTION_FIELDS, label))
        if raw.get("action_id") != action_id:
            errors.append(f"{label}.action_id must equal mapping key {action_id}")
        category = raw.get("category")
        if not isinstance(category, str) or not category:
            errors.append(f"{label}.category must be non-empty text")
        cost = raw.get("cost")
        if isinstance(cost, bool) or not isinstance(cost, int) or cost < 0:
            errors.append(f"{label}.cost must be a non-negative integer")

        range_min = raw.get("range_min", 0)
        range_max = raw.get("range_max", range_min)
        for field_name, value in (("range_min", range_min), ("range_max", range_max)):
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                errors.append(
                    f"{label}.{field_name} must be a non-negative integer"
                )
        if (
            isinstance(range_min, int)
            and not isinstance(range_min, bool)
            and isinstance(range_max, int)
            and not isinstance(range_max, bool)
            and range_max < range_min
        ):
            errors.append(f"{label}.range_max cannot be less than range_min")

        for field_name in (
            "requires_los",
            "requires_detection",
            "requires_identification",
            "allows_last_known_position",
            "allows_blind_area_targeting",
        ):
            if field_name in raw and not isinstance(raw[field_name], bool):
                errors.append(f"{label}.{field_name} must be boolean")
        _validate_text_list(raw.get("tags", []), f"{label}.tags", errors)
    return errors


def validate_combat_actor_archetypes(
    archetypes: Any,
    combat_actions: Any,
) -> List[str]:
    """Validate actor archetype identities and their action references."""

    if not isinstance(archetypes, Mapping):
        return ["combat_actor_archetypes must be an object"]
    action_ids = set(combat_actions) if isinstance(combat_actions, Mapping) else set()
    errors: List[str] = []
    for archetype_id, raw in archetypes.items():
        _validate_id(archetype_id, "combat actor archetype id", errors)
        label = f"combat_actor_archetypes.{archetype_id}"
        if not isinstance(raw, Mapping):
            errors.append(f"{label} must be an object")
            continue
        errors.extend(_unknown_field_errors(raw, _COMBAT_ARCHETYPE_FIELDS, label))
        if raw.get("archetype_id") != archetype_id:
            errors.append(
                f"{label}.archetype_id must equal mapping key {archetype_id}"
            )
        footprint = raw.get("footprint", 1)
        if isinstance(footprint, bool) or not isinstance(footprint, int):
            errors.append(f"{label}.footprint must be integer 1 for Phase 1")
        elif footprint != 1:
            errors.append(f"{label}.footprint must be 1 for Phase 1")
        for action_id in _validate_text_list(
            raw.get("action_ids", []),
            f"{label}.action_ids",
            errors,
        ):
            _validate_id(action_id, f"{label}.action_ids", errors)
            if action_id not in action_ids:
                errors.append(
                    f"{label} references unknown combat action {action_id!r}"
                )
        _validate_text_list(raw.get("tags", []), f"{label}.tags", errors)
        metadata = raw.get("metadata", {})
        if not isinstance(metadata, Mapping):
            errors.append(f"{label}.metadata must be an object")
    return errors


def _valid_tactical_map_lookup(tactical_maps: Any) -> Dict[str, Any]:
    from .combat_schema import parse_tactical_map_definition

    result: Dict[str, Any] = {}
    if not isinstance(tactical_maps, Mapping):
        return result
    for map_id, definition in tactical_maps.items():
        if not isinstance(map_id, str):
            continue
        try:
            result[map_id] = parse_tactical_map_definition(map_id, definition)
        except ValueError:
            pass
    return result


def validate_encounters(
    encounters: Any,
    tactical_maps: Any,
    combat_actions: Any,
    combat_actor_archetypes: Any,
    world_map: Any = None,
) -> List[str]:
    """Validate encounter shells and cross-references owned by D-069."""

    if not isinstance(encounters, Mapping):
        return ["encounters must be an object"]

    map_ids = set(tactical_maps) if isinstance(tactical_maps, Mapping) else set()
    action_ids = set(combat_actions) if isinstance(combat_actions, Mapping) else set()
    archetype_ids = (
        set(combat_actor_archetypes)
        if isinstance(combat_actor_archetypes, Mapping)
        else set()
    )
    parsed_maps = _valid_tactical_map_lookup(tactical_maps)
    world_nodes: Set[str] = set()
    if isinstance(world_map, Mapping):
        nodes = world_map.get("nodes", {})
        if isinstance(nodes, Mapping):
            world_nodes = set(nodes)

    errors: List[str] = []
    required = {
        "encounter_id",
        "map_id",
        "location_id",
        "trigger",
        "participants",
        "deployment",
        "objective_set",
        "retreat_policy",
        "ai_profiles",
        "aftermath_profile",
        "time_cost_minutes",
        "canon_status",
    }

    for encounter_id, raw in encounters.items():
        _validate_id(encounter_id, "encounter id", errors)
        label = f"encounters.{encounter_id}"
        if not isinstance(raw, Mapping):
            errors.append(f"{label} must be an object")
            continue

        errors.extend(_unknown_field_errors(raw, _ENCOUNTER_FIELDS, label))
        missing = sorted(required - set(raw))
        if missing:
            errors.append(
                f"{label} missing required fields: {', '.join(missing)}"
            )
        if raw.get("encounter_id") != encounter_id:
            errors.append(
                f"{label}.encounter_id must equal mapping key {encounter_id}"
            )

        map_id = raw.get("map_id")
        _validate_id(map_id, f"{label}.map_id", errors)
        if isinstance(map_id, str) and map_id not in map_ids:
            errors.append(f"{label} references unknown tactical map {map_id!r}")

        location_id = raw.get("location_id")
        _validate_id(location_id, f"{label}.location_id", errors)
        if world_nodes and isinstance(location_id, str) and location_id not in world_nodes:
            errors.append(f"{label} references unknown world location {location_id!r}")

        for field_name in (
            "trigger",
            "deployment",
            "objective_set",
            "retreat_policy",
            "ai_profiles",
            "aftermath_profile",
            "metadata",
        ):
            if field_name in raw and not isinstance(raw[field_name], Mapping):
                errors.append(f"{label}.{field_name} must be an object")

        minutes = raw.get("time_cost_minutes")
        if isinstance(minutes, bool) or not isinstance(minutes, int) or minutes < 0:
            errors.append(
                f"{label}.time_cost_minutes must be a non-negative integer"
            )
        canon_status = raw.get("canon_status")
        if not isinstance(canon_status, str) or not canon_status:
            errors.append(f"{label}.canon_status must be non-empty text")
        if "title" in raw and (
            not isinstance(raw["title"], str) or not raw["title"].strip()
        ):
            errors.append(f"{label}.title must be non-empty text")

        for action_id in _validate_text_list(
            raw.get("action_ids", []),
            f"{label}.action_ids",
            errors,
        ):
            _validate_id(action_id, f"{label}.action_ids", errors)
            if action_id not in action_ids:
                errors.append(
                    f"{label} references unknown combat action {action_id!r}"
                )
        for archetype_id in _validate_text_list(
            raw.get("archetype_ids", []),
            f"{label}.archetype_ids",
            errors,
        ):
            _validate_id(archetype_id, f"{label}.archetype_ids", errors)
            if archetype_id not in archetype_ids:
                errors.append(
                    f"{label} references unknown combat archetype {archetype_id!r}"
                )

        participants = raw.get("participants")
        if not isinstance(participants, list):
            errors.append(f"{label}.participants must be a list")
            continue

        seen_actor_ids: Set[str] = set()
        for index, participant in enumerate(participants):
            item_label = f"{label}.participants[{index}]"
            if not isinstance(participant, Mapping):
                errors.append(f"{item_label} must be an object")
                continue
            errors.extend(
                _unknown_field_errors(
                    participant,
                    _ENCOUNTER_PARTICIPANT_FIELDS,
                    item_label,
                )
            )
            actor_id = participant.get("actor_id")
            _validate_id(actor_id, f"{item_label}.actor_id", errors)
            if isinstance(actor_id, str):
                if actor_id in seen_actor_ids:
                    errors.append(
                        f"{label} has duplicate participant actor_id {actor_id}"
                    )
                seen_actor_ids.add(actor_id)

            archetype_id = participant.get("archetype_id")
            if archetype_id is not None:
                _validate_id(archetype_id, f"{item_label}.archetype_id", errors)
                if isinstance(archetype_id, str) and archetype_id not in archetype_ids:
                    errors.append(
                        f"{item_label} references unknown combat archetype "
                        f"{archetype_id!r}"
                    )
            persistent_ref = participant.get("persistent_ref")
            if persistent_ref is not None:
                _validate_id(
                    persistent_ref,
                    f"{item_label}.persistent_ref",
                    errors,
                )
            faction_id = participant.get("faction_id")
            if faction_id is not None:
                _validate_id(faction_id, f"{item_label}.faction_id", errors)
            if "required" in participant and not isinstance(
                participant["required"], bool
            ):
                errors.append(f"{item_label}.required must be boolean")

            for action_id in _validate_text_list(
                participant.get("action_ids", []),
                f"{item_label}.action_ids",
                errors,
            ):
                _validate_id(action_id, f"{item_label}.action_ids", errors)
                if action_id not in action_ids:
                    errors.append(
                        f"{item_label} references unknown combat action "
                        f"{action_id!r}"
                    )
            _validate_text_list(
                participant.get("tags", []),
                f"{item_label}.tags",
                errors,
            )

            zone_id = participant.get("deployment_zone")
            if zone_id is not None:
                _validate_id(zone_id, f"{item_label}.deployment_zone", errors)
                parsed_map = parsed_maps.get(map_id)
                if (
                    parsed_map is not None
                    and isinstance(zone_id, str)
                    and zone_id
                    not in {zone.zone_id for zone in parsed_map.deployment_zones}
                ):
                    errors.append(
                        f"{item_label} references unknown deployment zone "
                        f"{zone_id!r}"
                    )

    return errors


def validate_tactical_content(
    tactical_maps: Any,
    combat_actions: Any,
    combat_actor_archetypes: Any,
    encounters: Any,
    world_map: Any = None,
) -> List[str]:
    """Validate optional D-069 tactical authored sections as one cross-ref set."""

    errors: List[str] = []
    errors.extend(validate_tactical_maps(tactical_maps))
    errors.extend(validate_combat_actions(combat_actions))
    errors.extend(
        validate_combat_actor_archetypes(
            combat_actor_archetypes,
            combat_actions,
        )
    )
    errors.extend(
        validate_encounters(
            encounters,
            tactical_maps,
            combat_actions,
            combat_actor_archetypes,
            world_map,
        )
    )
    return errors


def validate_content_pack(
    scenes: Mapping[str, Dict[str, Any]],
    quests: Mapping[str, Mapping[str, Any]] | None = None,
    powers: Mapping[str, Mapping[str, Any]] | None = None,
    registries: Mapping[str, Mapping[str, Any]] | None = None,
    world_map: Mapping[str, Any] | None = None,
    *,
    tactical_maps: Mapping[str, Mapping[str, Any]] | None = None,
    combat_actions: Mapping[str, Mapping[str, Any]] | None = None,
    combat_actor_archetypes: Mapping[str, Mapping[str, Any]] | None = None,
    encounters: Mapping[str, Mapping[str, Any]] | None = None,
) -> List[str]:
    """Validate scenes, quest/power definitions, and authored cross-references."""
    from .powers import validate_power_definitions
    from .quests import validate_quest_definitions

    quest_definitions = {} if quests is None else quests
    power_definitions = {} if powers is None else powers
    errors = list(validate_scenes(scenes))
    errors.extend(validate_quest_definitions(quest_definitions))
    errors.extend(validate_power_definitions(power_definitions))
    errors.extend(validate_world_map(world_map, scenes))
    errors.extend(
        validate_tactical_content(
            {} if tactical_maps is None else tactical_maps,
            {} if combat_actions is None else combat_actions,
            {} if combat_actor_archetypes is None else combat_actor_archetypes,
            {} if encounters is None else encounters,
            world_map,
        )
    )

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
    world_map: Mapping[str, Any] | None = None,
    *,
    tactical_maps: Mapping[str, Mapping[str, Any]] | None = None,
    combat_actions: Mapping[str, Mapping[str, Any]] | None = None,
    combat_actor_archetypes: Mapping[str, Mapping[str, Any]] | None = None,
    encounters: Mapping[str, Mapping[str, Any]] | None = None,
) -> None:
    errors = validate_content_pack(
        scenes,
        quests,
        powers,
        registries,
        world_map,
        tactical_maps=tactical_maps,
        combat_actions=combat_actions,
        combat_actor_archetypes=combat_actor_archetypes,
        encounters=encounters,
    )
    if errors:
        raise RuleError("Invalid authored content pack:\n- " + "\n- ".join(errors))
