from __future__ import annotations

import re
from math import isfinite
from typing import Any, Dict, Mapping, MutableMapping

from .core import GameState, RuleError
from .modifiers import validate_modifier_mapping
from .progression import gain_ability_mastery, technique_available
from .schema import ATTRIBUTE_SPECS, SKILL_CATALOG
from .simulation import advance_time, apply_condition, validate_time_advance
from .stats import effective_player_value


TECHNIQUE_STAGES = (
    (0, "discovered"),
    (10, "unstable"),
    (40, "learned"),
    (120, "practiced"),
    (300, "mastered"),
)

_STAGE_ORDER = {
    "unknown": -1,
    "discovered": 0,
    "unstable": 1,
    "learned": 2,
    "practiced": 3,
    "mastered": 4,
}


_STABLE_ID = re.compile(r"^[A-Z][A-Z0-9_]*$")


def _validate_power_resource_path(path: Any, label: str) -> str:
    if not isinstance(path, str) or not path:
        raise RuleError(f"{label} must be a non-empty string")
    parts = path.split(".")
    if len(parts) != 2 or parts[0] != "power_resources" or not parts[1]:
        raise RuleError(f"{label} must use power_resources.<id>")
    return path


def validate_power_definitions(
    definitions: Mapping[str, Mapping[str, Any]],
) -> list[str]:
    """Validate complete authored ability/resource/technique definitions."""
    errors: list[str] = []
    if not isinstance(definitions, Mapping):
        return ["power definitions must be an object"]

    for ability_id, definition in definitions.items():
        if not isinstance(ability_id, str) or not _STABLE_ID.fullmatch(ability_id):
            errors.append(f"ability_id must be a stable uppercase ID: {ability_id!r}")
            continue
        if not isinstance(definition, Mapping):
            errors.append(f"{ability_id} power definition must be an object")
            continue

        family = definition.get("family")
        if family is not None and (not isinstance(family, str) or not family):
            errors.append(f"{ability_id}.family must be a non-empty string")
        form = definition.get("form")
        if form is not None and (not isinstance(form, str) or not form):
            errors.append(f"{ability_id}.form must be null or a non-empty string")
        tags = definition.get("tags", [])
        if not isinstance(tags, list) or not all(
            isinstance(tag, str) and tag for tag in tags
        ):
            errors.append(f"{ability_id}.tags must be a list of non-empty strings")

        resource = definition.get("resource")
        if resource is not None:
            if not isinstance(resource, Mapping):
                errors.append(f"{ability_id}.resource must be an object")
            else:
                try:
                    _validate_power_resource_path(
                        resource.get("path"),
                        f"{ability_id}.resource.path",
                    )
                except RuleError as exc:
                    errors.append(str(exc))

                maximum = resource.get("maximum")
                starting = resource.get("starting", maximum)
                recovery = resource.get("recovery_per_hour", 0)
                parsed: Dict[str, float] = {}
                for field, value in (
                    ("maximum", maximum),
                    ("starting", starting),
                    ("recovery_per_hour", recovery),
                ):
                    if (
                        isinstance(value, bool)
                        or not isinstance(value, (int, float))
                        or not isfinite(float(value))
                    ):
                        errors.append(
                            f"{ability_id}.resource.{field} must be a finite number"
                        )
                    else:
                        parsed[field] = float(value)

                if "maximum" in parsed and parsed["maximum"] <= 0:
                    errors.append(f"{ability_id}.resource.maximum must be positive")
                if "starting" in parsed and "maximum" in parsed:
                    if parsed["starting"] < 0 or parsed["starting"] > parsed["maximum"]:
                        errors.append(
                            f"{ability_id}.resource.starting must be in range 0..maximum"
                        )
                if "recovery_per_hour" in parsed and parsed["recovery_per_hour"] < 0:
                    errors.append(
                        f"{ability_id}.resource.recovery_per_hour cannot be negative"
                    )

        techniques = definition.get("techniques", {})
        if not isinstance(techniques, Mapping):
            errors.append(f"{ability_id}.techniques must be an object")
        else:
            for technique_id, technique in techniques.items():
                if (
                    not isinstance(technique_id, str)
                    or not _STABLE_ID.fullmatch(technique_id)
                ):
                    errors.append(
                        f"{ability_id} technique_id must be a stable uppercase ID: "
                        f"{technique_id!r}"
                    )
                    continue
                technique_errors = validate_technique_definition(technique)
                errors.extend(
                    f"{ability_id}.{technique_id}: {error}"
                    for error in technique_errors
                )

        evolutions = definition.get("evolutions", {})
        if not isinstance(evolutions, Mapping):
            errors.append(f"{ability_id}.evolutions must be an object")
        else:
            for evolution_id, evolution in evolutions.items():
                if (
                    not isinstance(evolution_id, str)
                    or not _STABLE_ID.fullmatch(evolution_id)
                ):
                    errors.append(
                        f"{ability_id} evolution_id must be a stable uppercase ID: "
                        f"{evolution_id!r}"
                    )
                    continue
                evolution_errors = validate_evolution_definition(evolution)
                errors.extend(
                    f"{ability_id}.{evolution_id}: {error}"
                    for error in evolution_errors
                )

    return errors


def assert_valid_power_definitions(
    definitions: Mapping[str, Mapping[str, Any]],
) -> None:
    errors = validate_power_definitions(definitions)
    if errors:
        raise RuleError("Invalid power definitions:\n- " + "\n- ".join(errors))


def technique_stage(xp: float) -> str:
    if isinstance(xp, bool) or not isinstance(xp, (int, float)) or not isfinite(float(xp)):
        raise RuleError("Technique mastery XP must be a finite number")
    if xp < 0:
        raise RuleError("Technique mastery XP cannot be negative")
    stage = "unknown"
    for threshold, name in TECHNIQUE_STAGES:
        if xp >= threshold:
            stage = name
        else:
            break
    return stage


def _player_path(state: GameState, path: str) -> Any:
    current: Any = state.player
    for part in path.split("."):
        if not isinstance(current, Mapping) or part not in current:
            return None
        current = current[part]
    return current


def _mutable_player_path_slot(
    state: GameState,
    path: str,
) -> tuple[MutableMapping[str, Any], str]:
    parts = path.split(".")
    if not parts or any(not part for part in parts):
        raise RuleError(f"Invalid mutable player path: {path!r}")
    if not isinstance(state.player, MutableMapping):
        raise RuleError("player state must be mutable")

    current: MutableMapping[str, Any] = state.player
    for part in parts[:-1]:
        node = current.get(part)
        if not isinstance(node, MutableMapping):
            raise RuleError(f"Player path is not mutable: {path}")
        current = node

    leaf = parts[-1]
    if leaf not in current:
        raise RuleError(f"Player path is missing: {path}")
    return current, leaf


def _set_player_path(state: GameState, path: str, value: Any) -> None:
    current, leaf = _mutable_player_path_slot(state, path)
    current[leaf] = value


def _validate_spendable_resource_path(path: Any, label: str) -> str:
    if not isinstance(path, str) or not path:
        raise RuleError(f"{label} must be a non-empty string")
    parts = path.split(".")
    if len(parts) != 2 or parts[0] not in {"resources", "power_resources"} or not parts[1]:
        raise RuleError(
            f"{label} must use resources.<id> or power_resources.<id>"
        )
    return path


def _numeric_player_path(state: GameState, path: str) -> float:
    value = _player_path(state, path)
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not isfinite(float(value))
    ):
        raise RuleError(f"Power resource path is missing or non-finite numeric: {path}")
    return float(value)


def _power_resource_plan(
    state: GameState,
    ability_id: str,
    definition: Mapping[str, Any],
) -> Dict[str, Any] | None:
    """Validate and plan one authored power resource without mutating state."""
    errors = validate_power_definitions({ability_id: definition})
    if errors:
        raise RuleError("Invalid power definition:\n- " + "\n- ".join(errors))

    resource = definition.get("resource")
    if resource is None:
        return None
    if not isinstance(resource, Mapping):
        raise RuleError(f"Power resource definition must be an object: {ability_id}")

    path = _validate_power_resource_path(
        resource.get("path"),
        f"{ability_id}.resource.path",
    )
    maximum = float(resource["maximum"])
    starting = float(resource.get("starting", maximum))
    recovery_per_hour = float(resource.get("recovery_per_hour", 0))

    if not isinstance(state.player, MutableMapping):
        raise RuleError("player state must be mutable")

    resource_id = path.split(".", 1)[1]
    existing_container = state.player.get("power_resources")
    if existing_container is None:
        container: MutableMapping[str, Any] = {}
        create_container = True
    elif not isinstance(existing_container, MutableMapping):
        raise RuleError("player.power_resources must be a mutable object")
    else:
        container = existing_container
        create_container = False

    missing = resource_id not in container
    if missing:
        current = starting
    else:
        raw = container[resource_id]
        if (
            isinstance(raw, bool)
            or not isinstance(raw, (int, float))
            or not isfinite(float(raw))
        ):
            raise RuleError(f"Power resource must be a finite number: {path}")
        current = float(raw)
        if current < 0 or current > maximum:
            raise RuleError(
                f"Power resource must be in range 0..{maximum}: {path}={current}"
            )

    return {
        "path": path,
        "resource_id": resource_id,
        "container": container,
        "create_container": create_container,
        "missing": missing,
        "current": current,
        "maximum": maximum,
        "starting": starting,
        "recovery_per_hour": recovery_per_hour,
    }


def _commit_power_resource_plan(state: GameState, plan: Mapping[str, Any], value: float) -> None:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not isfinite(float(value))
    ):
        raise RuleError("Power resource commit value must be finite numeric")
    maximum = float(plan["maximum"])
    value = float(value)
    if value < 0 or value > maximum:
        raise RuleError(
            f"Power resource commit value must be in range 0..{maximum}: {value}"
        )

    container = plan["container"]
    if not isinstance(container, MutableMapping):
        raise RuleError("Power resource container must be mutable")
    if plan["create_container"]:
        state.player["power_resources"] = container
    container[str(plan["resource_id"])] = value


def initialize_power_resource(
    state: GameState,
    ability_id: str,
    definition: Mapping[str, Any],
) -> Dict[str, float | str] | None:
    """Initialize an ability-specific resource from an authored definition."""
    plan = _power_resource_plan(state, ability_id, definition)
    if plan is None:
        return None

    if plan["missing"]:
        _commit_power_resource_plan(state, plan, float(plan["starting"]))

    return {
        "path": str(plan["path"]),
        "current": float(plan["current"]),
        "maximum": float(plan["maximum"]),
        "recovery_per_hour": float(plan["recovery_per_hour"]),
    }


def recover_power_resource(
    state: GameState,
    ability_id: str,
    definition: Mapping[str, Any],
    *,
    minutes: int,
    quality: float = 1.0,
) -> Dict[str, Any]:
    """Recover one authored power resource through the shared world clock."""
    if isinstance(minutes, bool) or not isinstance(minutes, int) or minutes <= 0:
        raise RuleError("Power recovery minutes must be a positive integer")
    if (
        isinstance(quality, bool)
        or not isinstance(quality, (int, float))
        or not isfinite(float(quality))
        or float(quality) < 0
    ):
        raise RuleError("Power recovery quality must be a finite non-negative number")

    ability = state.abilities.get(ability_id)
    if ability is None:
        raise RuleError(f"Unknown ability: {ability_id}")
    _ability_progression_state(ability, ability_id)
    _validate_history_container(state)
    validate_time_advance(state, minutes)

    plan = _power_resource_plan(state, ability_id, definition)
    if plan is None:
        raise RuleError(f"Ability has no recoverable power resource: {ability_id}")

    before = float(plan["current"])
    rate = float(plan["recovery_per_hour"])
    maximum = float(plan["maximum"])
    amount = rate * (minutes / 60.0) * float(quality)
    after = min(maximum, before + amount)

    event = {
        "type": "power_resource_recovery",
        "ability_id": ability_id,
        "resource_path": str(plan["path"]),
        "before": round(before, 3),
        "after": round(after, 3),
        "gained": round(after - before, 3),
        "minutes": minutes,
        "quality": float(quality),
        "time_minutes": state.time_minutes + minutes,
    }

    # All state/definition/time validation is complete before persistent mutation.
    _commit_power_resource_plan(state, plan, after)
    advance_time(state, minutes)
    state.history.append(event)
    return event


def discover_ability(
    state: GameState,
    ability_id: str,
    *,
    family: str = "unknown",
    form: str | None = None,
    tags: tuple[str, ...] | list[str] = (),
    data: Mapping[str, Any] | None = None,
) -> Dict[str, Any]:
    """Create a persistent ability shell without granting free mastery."""
    if not isinstance(ability_id, str) or not ability_id:
        raise RuleError("Ability ID must be a non-empty string")
    if not isinstance(family, str) or not family:
        raise RuleError("Ability family must be a non-empty string")
    if form is not None and (not isinstance(form, str) or not form):
        raise RuleError("Ability form must be null or a non-empty string")
    if not isinstance(tags, (tuple, list)) or not all(
        isinstance(tag, str) and tag for tag in tags
    ):
        raise RuleError("Ability tags must be a list/tuple of non-empty strings")
    if data is not None and not isinstance(data, Mapping):
        raise RuleError("Ability data must be an object")
    if not isinstance(state.abilities, MutableMapping):
        raise RuleError("state.abilities must be mutable")
    _validate_history_container(state)

    existing = state.abilities.get(ability_id)
    if existing is not None:
        if not isinstance(existing, MutableMapping):
            raise RuleError(f"Ability state must be an object: {ability_id}")
        _ability_progression_state(existing, ability_id)

        existing_tags = existing.get("tags", [])
        if not isinstance(existing_tags, list) or not all(
            isinstance(tag, str) and tag for tag in existing_tags
        ):
            raise RuleError(f"Ability tags state is invalid: {ability_id}")
        existing_data = existing.get("data", {})
        if not isinstance(existing_data, Mapping):
            raise RuleError(f"Ability data state is invalid: {ability_id}")
        existing_techniques = existing.get("techniques", {})
        if not isinstance(existing_techniques, MutableMapping):
            raise RuleError(f"Ability techniques state is invalid: {ability_id}")

        existing.setdefault("family", family)
        existing.setdefault("form", form)
        existing.setdefault("tags", list(tags))
        existing.setdefault("data", dict(data or {}))
        existing.setdefault("techniques", {})
        return existing

    ability: Dict[str, Any] = {
        "rank": 0,
        "mastery_xp": 0.0,
        "mastery_stage": "discovered",
        "family": family,
        "form": form,
        "tags": list(tags),
        "data": dict(data or {}),
        "techniques": {},
    }
    state.abilities[ability_id] = ability
    state.history.append(
        {
            "type": "ability_discovered",
            "ability_id": ability_id,
            "family": family,
            "form": form,
            "turn": state.turn,
            "time_minutes": state.time_minutes,
        }
    )
    return ability


def discover_technique(state: GameState, ability_id: str, technique_id: str) -> Dict[str, Any]:
    if not isinstance(technique_id, str) or not technique_id:
        raise RuleError("Technique ID must be a non-empty string")
    _validate_history_container(state)

    ability = state.abilities.get(ability_id)
    if not isinstance(ability, MutableMapping):
        raise RuleError(f"Unknown or invalid ability state: {ability_id}")
    _ability_progression_state(ability, ability_id)

    techniques = ability.get("techniques")
    if techniques is None:
        techniques = {}
        ability["techniques"] = techniques
    if not isinstance(techniques, MutableMapping):
        raise RuleError(f"Ability techniques must be an object: {ability_id}")
    if technique_id in techniques:
        existing = techniques[technique_id]
        if not isinstance(existing, MutableMapping):
            raise RuleError(f"Technique state must be an object: {technique_id}")
        return existing

    record = {
        "mastery_xp": 0.0,
        "stage": "discovered",
        "uses": 0,
        "ready_at_minutes": state.time_minutes,
        "discovered_at_minutes": state.time_minutes,
    }
    techniques[technique_id] = record
    state.history.append(
        {
            "type": "technique_discovered",
            "ability_id": ability_id,
            "technique_id": technique_id,
            "turn": state.turn,
            "time_minutes": state.time_minutes,
        }
    )
    return record

def gain_technique_mastery(
    state: GameState,
    ability_id: str,
    technique_id: str,
    xp: float,
) -> Dict[str, Any]:
    if isinstance(xp, bool) or not isinstance(xp, (int, float)) or not isfinite(float(xp)):
        raise RuleError("Technique mastery gain must be a finite number")
    if xp < 0:
        raise RuleError("Technique mastery gain cannot be negative")
    ability = state.abilities.get(ability_id)
    if not ability:
        raise RuleError(f"Unknown ability: {ability_id}")
    techniques = ability.get("techniques", {})
    if not isinstance(techniques, Mapping):
        raise RuleError(f"Ability techniques must be an object: {ability_id}")
    technique = techniques.get(technique_id)
    if not isinstance(technique, MutableMapping):
        raise RuleError(f"Technique has not been discovered or is invalid: {technique_id}")

    current_mastery = technique.get("mastery_xp", 0.0)
    if (
        isinstance(current_mastery, bool)
        or not isinstance(current_mastery, (int, float))
        or not isfinite(float(current_mastery))
        or float(current_mastery) < 0
    ):
        raise RuleError(f"Technique mastery state is invalid: {technique_id}")

    next_mastery = float(current_mastery) + float(xp)
    next_stage = technique_stage(next_mastery)
    before = dict(technique)
    technique["mastery_xp"] = next_mastery
    technique["stage"] = next_stage
    return {"before": before, "after": dict(technique)}


def practice_technique(
    state: GameState,
    ability_id: str,
    technique_id: str,
    *,
    minutes: int,
    intensity: float = 1.0,
    mentor_bonus: float = 0.0,
    stamina_per_hour: float = 4.0,
    focus_per_hour: float = 6.0,
) -> Dict[str, Any]:
    """Practice a discovered technique through paid world time and resources."""
    if isinstance(minutes, bool) or not isinstance(minutes, int) or minutes < 30:
        raise RuleError("Technique practice requires integer minutes >= 30")

    def finite_number(
        value: Any,
        label: str,
        *,
        minimum: float | None = None,
        maximum: float | None = None,
    ) -> float:
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or not isfinite(float(value))
        ):
            raise RuleError(f"{label} must be a finite number")
        number = float(value)
        if minimum is not None and number < minimum:
            raise RuleError(f"{label} must be >= {minimum}")
        if maximum is not None and number > maximum:
            raise RuleError(f"{label} must be <= {maximum}")
        return number

    intensity = finite_number(
        intensity,
        "Technique practice intensity",
        minimum=0.0000001,
        maximum=2.0,
    )
    mentor_bonus = finite_number(
        mentor_bonus,
        "Technique mentor bonus",
        minimum=0.0,
        maximum=1.0,
    )
    stamina_per_hour = finite_number(
        stamina_per_hour,
        "Technique stamina rate",
        minimum=0.0,
    )
    focus_per_hour = finite_number(
        focus_per_hour,
        "Technique focus rate",
        minimum=0.0,
    )

    ability = state.abilities.get(ability_id)
    if not isinstance(ability, MutableMapping):
        raise RuleError(f"Unknown or immutable ability state: {ability_id}")
    _ability_progression_state(ability, ability_id)
    validate_time_advance(state, minutes)
    _validate_history_container(state)
    technique = ability.get("techniques", {}).get(technique_id)
    if not isinstance(technique, MutableMapping):
        raise RuleError(f"Technique has not been discovered: {technique_id}")

    ready_at = technique.get("ready_at_minutes", 0)
    if isinstance(ready_at, bool) or not isinstance(ready_at, int) or ready_at < 0:
        raise RuleError(f"Technique ready_at_minutes is invalid: {technique_id}")
    if state.time_minutes < ready_at:
        raise RuleError(
            f"Technique is still recovering for {ready_at - state.time_minutes} minutes"
        )

    hours = minutes / 60.0
    stamina_cost = hours * stamina_per_hour * intensity
    focus_cost = hours * focus_per_hour * intensity

    stamina_before = _numeric_player_path(state, "resources.stamina")
    focus_before = _numeric_player_path(state, "resources.focus")
    _mutable_player_path_slot(state, "resources.stamina")
    _mutable_player_path_slot(state, "resources.focus")
    if stamina_before < stamina_cost or focus_before < focus_cost:
        raise RuleError("Insufficient stamina or focus for technique practice")

    technique_before = technique.get("mastery_xp", 0.0)
    ability_before = ability.get("mastery_xp", 0.0)
    if (
        isinstance(technique_before, bool)
        or not isinstance(technique_before, (int, float))
        or not isfinite(float(technique_before))
        or float(technique_before) < 0
    ):
        raise RuleError("Technique mastery state is invalid")
    if (
        isinstance(ability_before, bool)
        or not isinstance(ability_before, (int, float))
        or not isfinite(float(ability_before))
        or float(ability_before) < 0
    ):
        raise RuleError("Ability mastery state is invalid")

    technique_before = float(technique_before)
    ability_before = float(ability_before)
    learning_factor = max(0.15, 1.0 - technique_before / 450.0)
    technique_gain = (
        hours
        * 8.0
        * intensity
        * learning_factor
        * (1.0 + mentor_bonus)
    )
    ability_gain = technique_gain * 0.35

    # All validation happens above this point. Mutations below are deliberate.
    _set_player_path(state, "resources.stamina", stamina_before - stamina_cost)
    _set_player_path(state, "resources.focus", focus_before - focus_cost)
    gain_technique_mastery(
        state,
        ability_id,
        technique_id,
        technique_gain,
    )
    gain_ability_mastery(
        state,
        ability_id,
        ability_gain,
    )
    advance_time(state, minutes)

    event = {
        "type": "technique_practice",
        "ability_id": ability_id,
        "technique_id": technique_id,
        "minutes": minutes,
        "intensity": intensity,
        "mentor_bonus": mentor_bonus,
        "technique_mastery_before": round(technique_before, 3),
        "technique_mastery_after": round(
            float(technique.get("mastery_xp", 0.0)),
            3,
        ),
        "ability_mastery_before": round(ability_before, 3),
        "ability_mastery_after": round(
            float(ability.get("mastery_xp", 0.0)),
            3,
        ),
        "stamina_spent": round(stamina_cost, 3),
        "focus_spent": round(focus_cost, 3),
        "time_minutes": state.time_minutes,
    }
    state.history.append(event)
    return event


def _stage_at_least(actual: str, minimum: str) -> bool:
    if actual not in _STAGE_ORDER:
        raise RuleError(f"Unknown technique stage: {actual}")
    if minimum not in _STAGE_ORDER:
        raise RuleError(f"Unknown required technique stage: {minimum}")
    return _STAGE_ORDER[actual] >= _STAGE_ORDER[minimum]


def _extra_requirements_met(
    state: GameState,
    requirements: Mapping[str, Any],
    *,
    equipment_sets: Mapping[str, Mapping[str, Any]] | None = None,
) -> list[str]:
    reasons: list[str] = []

    for key, minimum in requirements.get("attributes", {}).items():
        actual = effective_player_value(
            state,
            f"attributes.{key}",
            equipment_sets=equipment_sets,
        )
        if actual < float(minimum):
            reasons.append(f"attribute:{key}")

    for key, minimum in requirements.get("skills", {}).items():
        actual = effective_player_value(
            state,
            f"skills.{key}",
            equipment_sets=equipment_sets,
        )
        if actual < float(minimum):
            reasons.append(f"skill:{key}")

    for key, expected in requirements.get("flags", {}).items():
        if state.flags.get(key) != expected:
            reasons.append(f"flag:{key}")

    for item_id, quantity in requirements.get("items", {}).items():
        if state.inventory.get(item_id, 0) < int(quantity):
            reasons.append(f"item:{item_id}")

    return reasons


def _number(value: Any, label: str, errors: list[str], *, minimum: float | None = None) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        errors.append(f"{label} must be numeric")
        return None
    number = float(value)
    if not isfinite(number):
        errors.append(f"{label} must be finite")
        return None
    if minimum is not None and number < minimum:
        errors.append(f"{label} must be >= {minimum}")
    return number


def _integer(value: Any, label: str, errors: list[str], *, minimum: int | None = None) -> int | None:
    if isinstance(value, bool) or not isinstance(value, int):
        errors.append(f"{label} must be an integer")
        return None
    if minimum is not None and value < minimum:
        errors.append(f"{label} must be >= {minimum}")
    return value


def _validate_history_container(state: GameState) -> None:
    if not isinstance(state.history, list):
        raise RuleError("state.history must be a list")


def _validate_condition_container(state: GameState) -> None:
    if not isinstance(state.player, MutableMapping):
        raise RuleError("player state must be mutable")
    conditions = state.player.get("conditions")
    if conditions is not None and not isinstance(conditions, dict):
        raise RuleError("player.conditions must be an object")


def _ability_progression_state(
    ability: Any,
    ability_id: str,
) -> tuple[int, float, int]:
    if not isinstance(ability, Mapping):
        raise RuleError(f"Ability state must be an object: {ability_id}")

    rank = ability.get("rank", 0)
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 0:
        raise RuleError(f"Ability rank state is invalid: {ability_id}")

    mastery = ability.get("mastery_xp", 0.0)
    if (
        isinstance(mastery, bool)
        or not isinstance(mastery, (int, float))
        or not isfinite(float(mastery))
        or float(mastery) < 0
    ):
        raise RuleError(f"Ability mastery state is invalid: {ability_id}")

    rank_floor = ability.get("rank_floor", 0)
    if (
        isinstance(rank_floor, bool)
        or not isinstance(rank_floor, int)
        or rank_floor < 0
    ):
        raise RuleError(f"Ability rank_floor state is invalid: {ability_id}")

    return rank, float(mastery), rank_floor


def validate_technique_definition(definition: Any) -> list[str]:
    """Validate one authored technique definition without mutating game state."""
    errors: list[str] = []
    if not isinstance(definition, Mapping):
        return ["technique definition must be an object"]

    stage_min = definition.get("stage_min", "discovered")
    if stage_min not in _STAGE_ORDER:
        errors.append(f"stage_min has unsupported value {stage_min!r}")

    requirements = definition.get("requirements", {})
    if not isinstance(requirements, Mapping):
        errors.append("requirements must be an object")
        requirements = {}

    for section in ("attributes", "skills", "flags", "items"):
        value = requirements.get(section, {})
        if not isinstance(value, Mapping):
            errors.append(f"requirements.{section} must be an object")

    if "rank_min" in requirements:
        _integer(requirements["rank_min"], "requirements.rank_min", errors, minimum=0)
    if "mastery_xp_min" in requirements:
        _number(
            requirements["mastery_xp_min"],
            "requirements.mastery_xp_min",
            errors,
            minimum=0.0,
        )

    for section in ("attributes", "skills"):
        values = requirements.get(section, {})
        if isinstance(values, Mapping):
            catalog = ATTRIBUTE_SPECS if section == "attributes" else SKILL_CATALOG
            for key, minimum in values.items():
                if key not in catalog:
                    errors.append(f"requirements.{section} has unknown ID {key!r}")
                _number(
                    minimum,
                    f"requirements.{section}.{key}",
                    errors,
                    minimum=0.0,
                )

    item_requirements = requirements.get("items", {})
    if isinstance(item_requirements, Mapping):
        for item_id, quantity in item_requirements.items():
            _integer(
                quantity,
                f"requirements.items.{item_id}",
                errors,
                minimum=0,
            )

    for section in ("knowledge", "perks"):
        values = requirements.get(section, [])
        if not isinstance(values, list) or not all(isinstance(v, str) and v for v in values):
            errors.append(f"requirements.{section} must be a list of non-empty IDs")

    costs = definition.get("costs", {})
    if not isinstance(costs, Mapping):
        errors.append("costs must be an object")
    else:
        for path, amount in costs.items():
            try:
                _validate_spendable_resource_path(path, "Technique cost path")
            except RuleError as exc:
                errors.append(str(exc))
                continue
            _number(amount, f"costs.{path}", errors, minimum=0.0)

    if "cooldown_minutes" in definition:
        cooldown = definition["cooldown_minutes"]
        if isinstance(cooldown, bool) or not isinstance(cooldown, int):
            errors.append("cooldown_minutes must be an integer")
        elif cooldown < 0:
            errors.append("cooldown_minutes must be >= 0")

    for key in ("mastery_gain", "ability_mastery_gain"):
        if key in definition:
            _number(definition[key], key, errors, minimum=0.0)

    drawbacks = definition.get("drawbacks", [])
    if not isinstance(drawbacks, list):
        errors.append("drawbacks must be a list")
    else:
        for index, drawback in enumerate(drawbacks):
            location = f"drawbacks[{index}]"
            if not isinstance(drawback, Mapping):
                errors.append(f"{location} must be an object")
                continue
            if drawback.get("type") != "condition":
                errors.append(
                    f"{location}.type has unsupported value {drawback.get('type')!r}"
                )
                continue
            condition_id = drawback.get("condition_id")
            if not isinstance(condition_id, str) or not condition_id:
                errors.append(f"{location}.condition_id must be a non-empty string")
            severity = drawback.get("severity", 1)
            if isinstance(severity, bool) or not isinstance(severity, int):
                errors.append(f"{location}.severity must be an integer")
            elif severity < 1 or severity > 5:
                errors.append(f"{location}.severity must be in range 1..5")
            duration = drawback.get("duration_minutes")
            if duration is not None:
                if isinstance(duration, bool) or not isinstance(duration, int):
                    errors.append(f"{location}.duration_minutes must be an integer or null")
                elif duration < 0:
                    errors.append(f"{location}.duration_minutes must be >= 0")
            tags = drawback.get("tags", [])
            if isinstance(tags, (str, bytes)) or not isinstance(tags, (list, tuple)):
                errors.append(f"{location}.tags must be a list/tuple of non-empty strings")
            elif not all(isinstance(tag, str) and tag for tag in tags):
                errors.append(f"{location}.tags must be a list/tuple of non-empty strings")
            modifiers = drawback.get("modifiers")
            if modifiers is not None:
                try:
                    validate_modifier_mapping(
                        modifiers,
                        source=f"technique.{location}",
                    )
                except ValueError as exc:
                    errors.append(f"{location}.modifiers invalid: {exc}")

    return errors


def validate_evolution_definition(definition: Any) -> list[str]:
    """Validate one authored evolution definition before any state mutation."""
    errors: list[str] = []
    if not isinstance(definition, Mapping):
        return ["evolution definition must be an object"]

    requirements = definition.get("requirements", {})
    if not isinstance(requirements, Mapping):
        errors.append("requirements must be an object")
        requirements = {}

    if "rank_min" in requirements:
        _integer(requirements["rank_min"], "requirements.rank_min", errors, minimum=0)
    if "mastery_xp_min" in requirements:
        _number(
            requirements["mastery_xp_min"],
            "requirements.mastery_xp_min",
            errors,
            minimum=0.0,
        )

    for section in ("attributes", "skills", "items", "flags", "techniques"):
        value = requirements.get(section, {})
        if not isinstance(value, Mapping):
            errors.append(f"requirements.{section} must be an object")

    for section in ("attributes", "skills"):
        values = requirements.get(section, {})
        if isinstance(values, Mapping):
            catalog = ATTRIBUTE_SPECS if section == "attributes" else SKILL_CATALOG
            for key, minimum in values.items():
                if key not in catalog:
                    errors.append(f"requirements.{section} has unknown ID {key!r}")
                _number(
                    minimum,
                    f"requirements.{section}.{key}",
                    errors,
                    minimum=0.0,
                )

    item_requirements = requirements.get("items", {})
    if isinstance(item_requirements, Mapping):
        for item_id, quantity in item_requirements.items():
            _integer(
                quantity,
                f"requirements.items.{item_id}",
                errors,
                minimum=0,
            )

    for section in ("knowledge", "perks"):
        values = requirements.get(section, [])
        if not isinstance(values, list) or not all(isinstance(v, str) and v for v in values):
            errors.append(f"requirements.{section} must be a list of non-empty IDs")

    techniques = requirements.get("techniques", {})
    if isinstance(techniques, Mapping):
        for technique_id, stage in techniques.items():
            if not isinstance(technique_id, str) or not technique_id:
                errors.append("requirements.techniques keys must be non-empty IDs")
            if stage not in _STAGE_ORDER:
                errors.append(
                    f"requirements.techniques.{technique_id} has unsupported stage {stage!r}"
                )

    result = definition.get("result", {})
    if not isinstance(result, Mapping):
        errors.append("result must be an object")
        return errors

    if "form" in result:
        form = result["form"]
        if not isinstance(form, str) or not form:
            errors.append("result.form must be a non-empty string")

    if "rank_floor" in result:
        value = result["rank_floor"]
        if isinstance(value, bool) or not isinstance(value, int):
            errors.append("result.rank_floor must be an integer")
        elif value < 0:
            errors.append("result.rank_floor must be >= 0")

    tags = result.get("tags", [])
    if not isinstance(tags, list) or not all(isinstance(v, str) and v for v in tags):
        errors.append("result.tags must be a list of non-empty strings")

    consume_items = result.get("consume_items", {})
    if not isinstance(consume_items, Mapping):
        errors.append("result.consume_items must be an object")
    else:
        for item_id, quantity in consume_items.items():
            if not isinstance(item_id, str) or not item_id:
                errors.append("result.consume_items keys must be non-empty IDs")
                continue
            if isinstance(quantity, bool) or not isinstance(quantity, int):
                errors.append(f"result.consume_items.{item_id} must be an integer")
            elif quantity < 0:
                errors.append(f"result.consume_items.{item_id} must be >= 0")

    grant_perks = result.get("grant_perks", {})
    if not isinstance(grant_perks, Mapping):
        errors.append("result.grant_perks must be an object")
    else:
        for perk_id, perk in grant_perks.items():
            location = f"result.grant_perks.{perk_id}"
            if not isinstance(perk_id, str) or not perk_id:
                errors.append("result.grant_perks keys must be non-empty IDs")
            if not isinstance(perk, Mapping):
                errors.append(f"{location} must be an object")
                continue
            modifiers = perk.get("modifiers", {})
            try:
                validate_modifier_mapping(
                    modifiers,
                    source=location,
                )
            except ValueError as exc:
                errors.append(f"{location}.modifiers invalid: {exc}")
            perk_tags = perk.get("tags", [])
            if not isinstance(perk_tags, list) or not all(
                isinstance(v, str) and v for v in perk_tags
            ):
                errors.append(f"{location}.tags must be a list of non-empty strings")

    return errors


def technique_use_status(
    state: GameState,
    ability_id: str,
    technique_id: str,
    definition: Mapping[str, Any],
    *,
    equipment_sets: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, Any]:
    definition_errors = validate_technique_definition(definition)
    if definition_errors:
        raise RuleError(
            "Invalid technique definition: " + "; ".join(definition_errors)
        )

    reasons: list[str] = []
    ability = state.abilities.get(ability_id)
    if ability is None:
        return {"available": False, "reasons": ["ability_missing"]}
    _ability_progression_state(ability, ability_id)

    techniques = ability.get("techniques", {})
    if not isinstance(techniques, Mapping):
        raise RuleError(f"Ability techniques must be an object: {ability_id}")
    technique = techniques.get(technique_id)
    if not technique:
        return {"available": False, "reasons": ["technique_undiscovered"]}
    if not isinstance(technique, Mapping):
        raise RuleError(f"Technique state must be an object: {technique_id}")

    technique_mastery = technique.get("mastery_xp", 0.0)
    if (
        isinstance(technique_mastery, bool)
        or not isinstance(technique_mastery, (int, float))
        or not isfinite(float(technique_mastery))
        or float(technique_mastery) < 0
    ):
        raise RuleError(f"Technique mastery state is invalid: {technique_id}")

    ability_mastery = ability.get("mastery_xp", 0.0)
    if (
        isinstance(ability_mastery, bool)
        or not isinstance(ability_mastery, (int, float))
        or not isfinite(float(ability_mastery))
        or float(ability_mastery) < 0
    ):
        raise RuleError(f"Ability mastery state is invalid: {ability_id}")

    uses = technique.get("uses", 0)
    if isinstance(uses, bool) or not isinstance(uses, int) or uses < 0:
        raise RuleError(f"Technique uses state is invalid: {technique_id}")

    requirements = definition.get("requirements", {})
    if not technique_available(state, ability_id, dict(requirements)):
        reasons.append("ability_requirements")

    reasons.extend(
        _extra_requirements_met(
            state,
            requirements,
            equipment_sets=equipment_sets,
        )
    )

    minimum_stage = definition.get("stage_min", "discovered")
    if not _stage_at_least(technique.get("stage", "unknown"), minimum_stage):
        reasons.append(f"stage:{minimum_stage}")

    ready_at_raw = technique.get("ready_at_minutes", 0)
    if (
        isinstance(ready_at_raw, bool)
        or not isinstance(ready_at_raw, int)
        or ready_at_raw < 0
    ):
        raise RuleError(f"Technique ready_at_minutes is invalid: {technique_id}")
    ready_at = ready_at_raw
    if state.time_minutes < ready_at:
        reasons.append(f"cooldown:{ready_at - state.time_minutes}")

    for path, amount_raw in definition.get("costs", {}).items():
        amount = float(amount_raw)
        if amount < 0:
            raise RuleError(f"Technique cost cannot be negative: {path}")
        current = _numeric_player_path(state, path)
        _mutable_player_path_slot(state, path)
        if current < amount:
            reasons.append(f"resource:{path}")

    cooldown = int(definition.get("cooldown_minutes", 0))
    if cooldown < 0:
        raise RuleError("Technique cooldown cannot be negative")

    mastery_gain = float(definition.get("mastery_gain", 0))
    if mastery_gain < 0:
        raise RuleError("Technique mastery gain cannot be negative")
    ability_mastery_gain = float(definition.get("ability_mastery_gain", 0))
    if ability_mastery_gain < 0:
        raise RuleError("Ability mastery gain cannot be negative")

    for drawback in definition.get("drawbacks", []):
        if drawback.get("type") != "condition":
            raise RuleError(f"Unsupported power drawback type: {drawback.get('type')}")
        severity = int(drawback.get("severity", 1))
        if severity < 1 or severity > 5:
            raise RuleError("Condition severity must be in range 1..5")
        duration = drawback.get("duration_minutes")
        if duration is not None and int(duration) < 0:
            raise RuleError("Condition duration cannot be negative")

    return {
        "available": not reasons,
        "reasons": reasons,
        "ready_at_minutes": ready_at,
    }


def use_technique(
    state: GameState,
    ability_id: str,
    technique_id: str,
    definition: Mapping[str, Any],
    *,
    equipment_sets: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, Any]:
    status = technique_use_status(
        state,
        ability_id,
        technique_id,
        definition,
        equipment_sets=equipment_sets,
    )
    if not status["available"]:
        raise RuleError(
            f"Technique cannot be used: {technique_id} ({', '.join(status['reasons'])})"
        )

    _validate_history_container(state)
    if definition.get("drawbacks"):
        _validate_condition_container(state)

    ability = state.abilities[ability_id]
    if not isinstance(ability, MutableMapping):
        raise RuleError(f"Ability state must be mutable: {ability_id}")
    techniques = ability.get("techniques", {})
    if not isinstance(techniques, MutableMapping):
        raise RuleError(f"Ability techniques must be mutable: {ability_id}")
    technique = techniques.get(technique_id)
    if not isinstance(technique, MutableMapping):
        raise RuleError(f"Technique state must be mutable: {technique_id}")

    spent: Dict[str, float] = {}
    for path, amount_raw in definition.get("costs", {}).items():
        amount = float(amount_raw)
        before = _numeric_player_path(state, path)
        _set_player_path(state, path, before - amount)
        spent[path] = amount

    cooldown = int(definition.get("cooldown_minutes", 0))
    technique["ready_at_minutes"] = state.time_minutes + cooldown
    technique["uses"] = int(technique.get("uses", 0)) + 1

    applied_drawbacks: list[str] = []
    for drawback in definition.get("drawbacks", []):
        condition_id = drawback["condition_id"]
        apply_condition(
            state,
            condition_id,
            severity=int(drawback.get("severity", 1)),
            duration_minutes=drawback.get("duration_minutes"),
            source=f"technique:{ability_id}:{technique_id}",
            tags=drawback.get("tags", ()),
            modifiers=drawback.get("modifiers"),
        )
        applied_drawbacks.append(condition_id)

    mastery_gain = float(definition.get("mastery_gain", 0))
    mastery_result = None
    if mastery_gain:
        mastery_result = gain_technique_mastery(
            state, ability_id, technique_id, mastery_gain
        )

    ability_mastery_gain = float(definition.get("ability_mastery_gain", 0))
    ability_mastery_result = None
    if ability_mastery_gain:
        ability_mastery_result = gain_ability_mastery(
            state, ability_id, ability_mastery_gain
        )

    event = {
        "type": "technique_use",
        "ability_id": ability_id,
        "technique_id": technique_id,
        "time_minutes": state.time_minutes,
        "spent": spent,
        "ready_at_minutes": technique["ready_at_minutes"],
        "drawbacks": applied_drawbacks,
        "mastery": mastery_result,
        "ability_mastery": ability_mastery_result,
    }
    state.history.append(event)
    return event


def ability_evolution_status(
    state: GameState,
    ability_id: str,
    evolution_id: str,
    definition: Mapping[str, Any],
    *,
    equipment_sets: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, Any]:
    if not isinstance(evolution_id, str) or not evolution_id:
        raise RuleError("Evolution ID must be a non-empty string")

    definition_errors = validate_evolution_definition(definition)
    if definition_errors:
        raise RuleError(
            "Invalid evolution definition: " + "; ".join(definition_errors)
        )

    ability = state.abilities.get(ability_id)
    if ability is None:
        return {"available": False, "reasons": ["ability_missing"]}
    rank, mastery_xp, _rank_floor = _ability_progression_state(
        ability,
        ability_id,
    )

    evolutions = ability.get("evolutions", [])
    if not isinstance(evolutions, list):
        raise RuleError(f"Ability evolutions must be a list: {ability_id}")
    completed_ids: set[str] = set()
    for index, record in enumerate(evolutions):
        if not isinstance(record, Mapping):
            raise RuleError(
                f"Ability evolution record must be an object: {ability_id}[{index}]"
            )
        completed_id = record.get("evolution_id")
        if completed_id is not None:
            if not isinstance(completed_id, str) or not completed_id:
                raise RuleError(
                    f"Ability evolution record ID is invalid: {ability_id}[{index}]"
                )
            completed_ids.add(completed_id)
    if evolution_id in completed_ids:
        return {"available": False, "reasons": ["already_evolved"]}

    if not isinstance(state.knowledge, Mapping):
        raise RuleError("state.knowledge must be an object")
    if not isinstance(state.perks, Mapping):
        raise RuleError("state.perks must be an object")
    if not isinstance(state.inventory, Mapping):
        raise RuleError("state.inventory must be an object")

    requirements = definition.get("requirements", {})
    reasons: list[str] = []

    if rank < int(requirements.get("rank_min", 0)):
        reasons.append("rank")
    if mastery_xp < float(requirements.get("mastery_xp_min", 0)):
        reasons.append("mastery_xp")

    for knowledge_id in requirements.get("knowledge", []):
        if knowledge_id not in state.knowledge:
            reasons.append(f"knowledge:{knowledge_id}")

    for perk_id in requirements.get("perks", []):
        if perk_id not in state.perks:
            reasons.append(f"perk:{perk_id}")

    reasons.extend(
        _extra_requirements_met(
            state,
            requirements,
            equipment_sets=equipment_sets,
        )
    )

    techniques = ability.get("techniques", {})
    if not isinstance(techniques, Mapping):
        raise RuleError(f"Ability techniques must be an object: {ability_id}")
    for required_id, stage_min in requirements.get("techniques", {}).items():
        record = techniques.get(required_id)
        if record is None:
            reasons.append(f"technique:{required_id}:{stage_min}")
            continue
        if not isinstance(record, Mapping):
            raise RuleError(f"Technique state must be an object: {required_id}")
        if not _stage_at_least(record.get("stage", "unknown"), stage_min):
            reasons.append(f"technique:{required_id}:{stage_min}")

    result = definition.get("result", {})
    for item_id, quantity in result.get("consume_items", {}).items():
        current_quantity = state.inventory.get(item_id, 0)
        if (
            isinstance(current_quantity, bool)
            or not isinstance(current_quantity, int)
            or current_quantity < 0
        ):
            raise RuleError(f"Inventory quantity is invalid: {item_id}")
        if current_quantity < quantity:
            reasons.append(f"consume_item:{item_id}")

    for perk_id in result.get("grant_perks", {}):
        if perk_id in state.perks:
            reasons.append(f"perk_exists:{perk_id}")

    return {"available": not reasons, "reasons": reasons}

def evolve_ability(
    state: GameState,
    ability_id: str,
    evolution_id: str,
    definition: Mapping[str, Any],
    *,
    equipment_sets: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, Any]:
    status = ability_evolution_status(
        state,
        ability_id,
        evolution_id,
        definition,
        equipment_sets=equipment_sets,
    )
    if not status["available"]:
        raise RuleError(
            f"Ability cannot evolve: {evolution_id} ({', '.join(status['reasons'])})"
        )

    _validate_history_container(state)

    ability = state.abilities[ability_id]
    if not isinstance(ability, MutableMapping):
        raise RuleError(f"Ability state must be mutable: {ability_id}")
    current_rank, _mastery_xp, current_rank_floor = _ability_progression_state(
        ability,
        ability_id,
    )

    if not isinstance(state.inventory, MutableMapping):
        raise RuleError("state.inventory must be mutable")
    if not isinstance(state.perks, MutableMapping):
        raise RuleError("state.perks must be mutable")

    existing_tags = ability.get("tags", [])
    if not isinstance(existing_tags, list) or not all(
        isinstance(tag, str) and tag for tag in existing_tags
    ):
        raise RuleError(f"Ability tags state is invalid: {ability_id}")

    existing_evolutions = ability.get("evolutions")
    if existing_evolutions is None:
        evolution_records: list[Dict[str, Any]] = []
        evolutions_were_missing = True
    elif not isinstance(existing_evolutions, list):
        raise RuleError(f"Ability evolutions must be a list: {ability_id}")
    else:
        evolution_records = existing_evolutions
        evolutions_were_missing = False

    result = definition.get("result", {})
    previous_form = ability.get("form")
    next_form = result.get("form", previous_form)

    incoming_rank_floor = result.get("rank_floor")
    next_rank_floor = current_rank_floor
    if incoming_rank_floor is not None:
        next_rank_floor = max(current_rank_floor, incoming_rank_floor)
    next_rank = max(current_rank, next_rank_floor)

    incoming_tags = result.get("tags", [])
    next_tags = list(dict.fromkeys([*existing_tags, *incoming_tags]))

    inventory_after: Dict[str, int] = {}
    consumed_items: Dict[str, int] = {}
    for item_id, quantity in result.get("consume_items", {}).items():
        current_quantity = state.inventory.get(item_id, 0)
        if (
            isinstance(current_quantity, bool)
            or not isinstance(current_quantity, int)
            or current_quantity < quantity
        ):
            raise RuleError(f"Inventory changed or is invalid before evolution: {item_id}")
        inventory_after[item_id] = current_quantity - quantity
        if quantity:
            consumed_items[item_id] = quantity

    perk_records: Dict[str, Dict[str, Any]] = {}
    for perk_id, perk in result.get("grant_perks", {}).items():
        if perk_id in state.perks:
            raise RuleError(f"Perk already exists before evolution commit: {perk_id}")
        perk_records[perk_id] = {
            "source": f"evolution:{ability_id}:{evolution_id}",
            "modifiers": dict(perk.get("modifiers", {})),
            "tags": list(perk.get("tags", [])),
        }

    record = {
        "evolution_id": evolution_id,
        "time_minutes": state.time_minutes,
        "previous_form": previous_form,
        "form": next_form,
    }
    event = {
        "type": "ability_evolution",
        "ability_id": ability_id,
        "evolution_id": evolution_id,
        "time_minutes": state.time_minutes,
        "previous_form": previous_form,
        "form": next_form,
        "granted_perks": list(perk_records),
        "consumed_items": dict(consumed_items),
    }

    # All validation/planning is complete. Commit persistent state.
    if "form" in result:
        ability["form"] = next_form
    if incoming_rank_floor is not None:
        ability["rank_floor"] = next_rank_floor
        ability["rank"] = next_rank
    if "tags" in result:
        ability["tags"] = next_tags

    for item_id, remaining in inventory_after.items():
        if remaining <= 0:
            state.inventory.pop(item_id, None)
        else:
            state.inventory[item_id] = remaining

    for perk_id, perk_record in perk_records.items():
        state.perks[perk_id] = perk_record

    if evolutions_were_missing:
        ability["evolutions"] = evolution_records
    evolution_records.append(record)
    state.history.append(event)
    return event

def _visible_text(value: Any, label: str, *, default: str | None = None) -> str:
    if value is None and default is not None:
        return default
    if not isinstance(value, str) or not value:
        raise RuleError(f"{label} must be a non-empty string")
    return value


def _visible_resource_path(path: Any, label: str) -> str:
    return _validate_spendable_resource_path(path, label)


def ability_player_view(
    state: GameState,
    ability_id: str,
    definition: Mapping[str, Any] | None = None,
) -> Dict[str, Any]:
    """Return a player-safe projection of one known ability.

    This intentionally does not dump the raw authored definition. Only techniques
    already present in persistent ability state and evolution entries explicitly
    marked visible in persistent state are projected. Hidden requirements remain
    inaccessible to a normal status UI.
    """
    ability = state.abilities.get(ability_id)
    if not ability:
        raise RuleError(f"Unknown ability: {ability_id}")

    definition = definition or {}
    rank_value = ability.get("rank", 0)
    if isinstance(rank_value, bool) or not isinstance(rank_value, int) or rank_value < 0:
        raise RuleError(f"Ability rank must be a non-negative integer: {ability_id}")
    mastery_value = ability.get("mastery_xp", 0.0)
    if (
        isinstance(mastery_value, bool)
        or not isinstance(mastery_value, (int, float))
        or not isfinite(float(mastery_value))
        or float(mastery_value) < 0
    ):
        raise RuleError(f"Ability mastery_xp must be a finite non-negative number: {ability_id}")

    output: Dict[str, Any] = {
        "name": _visible_text(
            definition.get("name", ability.get("name")),
            "ability display name",
            default=ability_id,
        ),
        "rank": rank_value,
        "mastery_stage": _visible_text(
            ability.get("mastery_stage"),
            "ability mastery_stage",
            default="discovered",
        ),
        "mastery_xp": float(mastery_value),
        "form": ability.get("form"),
        "state": _visible_text(
            ability.get("state"),
            "ability state",
            default="ready",
        ),
        "techniques": [],
        "evolutions": [],
    }

    for optional_key in ("control", "efficiency"):
        if optional_key in ability:
            value = ability[optional_key]
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not isfinite(float(value))
            ):
                raise RuleError(
                    f"Ability {optional_key} must be a finite number: {ability_id}"
                )
            output[optional_key] = float(value)

    resource_definition = definition.get("resource")
    if resource_definition is not None:
        if not isinstance(resource_definition, Mapping):
            raise RuleError("Ability resource definition must be an object")
        current_path = _visible_resource_path(
            resource_definition.get("current_path"),
            "Ability resource current_path",
        )
        max_path = resource_definition.get("max_path")
        current = _numeric_player_path(state, current_path)
        resource_view: Dict[str, Any] = {
            "label": resource_definition.get("label", "Resource"),
            "current": current,
        }
        if max_path is not None:
            max_path = _visible_resource_path(
                max_path,
                "Ability resource max_path",
            )
            resource_view["max"] = _numeric_player_path(state, max_path)
        output["resource"] = resource_view

    technique_definitions = definition.get("techniques", {})
    if technique_definitions is not None and not isinstance(technique_definitions, Mapping):
        raise RuleError("Ability technique definitions must be an object")

    for technique_id, record in ability.get("techniques", {}).items():
        if not isinstance(technique_id, str) or not technique_id:
            raise RuleError("Technique state keys must be non-empty IDs")
        if not isinstance(record, Mapping):
            raise RuleError(f"Technique state must be an object: {technique_id}")
        technique_mastery = record.get("mastery_xp", 0.0)
        if (
            isinstance(technique_mastery, bool)
            or not isinstance(technique_mastery, (int, float))
            or not isfinite(float(technique_mastery))
            or float(technique_mastery) < 0
        ):
            raise RuleError(
                f"Technique mastery_xp must be a finite non-negative number: {technique_id}"
            )
        uses_value = record.get("uses", 0)
        if isinstance(uses_value, bool) or not isinstance(uses_value, int) or uses_value < 0:
            raise RuleError(f"Technique uses must be a non-negative integer: {technique_id}")
        ready_at_value = record.get("ready_at_minutes", 0)
        if (
            isinstance(ready_at_value, bool)
            or not isinstance(ready_at_value, int)
            or ready_at_value < 0
        ):
            raise RuleError(
                f"Technique ready_at_minutes must be a non-negative integer: {technique_id}"
            )
        authored = (
            technique_definitions.get(technique_id, {})
            if isinstance(technique_definitions, Mapping)
            else {}
        )
        if authored is not None and not isinstance(authored, Mapping):
            raise RuleError(f"Technique definition must be an object: {technique_id}")
        authored = authored or {}
        ready_at = ready_at_value
        output["techniques"].append(
            {
                "technique_id": technique_id,
                "name": _visible_text(
                    authored.get("name"),
                    f"Technique display name {technique_id}",
                    default=technique_id,
                ),
                "stage": _visible_text(
                    record.get("stage"),
                    f"Technique stage {technique_id}",
                    default="discovered",
                ),
                "mastery_xp": float(technique_mastery),
                "uses": uses_value,
                "ready": state.time_minutes >= ready_at,
                "cooldown_remaining_minutes": max(0, ready_at - state.time_minutes),
            }
        )

    evolution_definitions = definition.get("evolutions", {})
    if evolution_definitions is not None and not isinstance(evolution_definitions, Mapping):
        raise RuleError("Ability evolution definitions must be an object")

    visibility = ability.get("evolution_visibility", {})
    if visibility is not None and not isinstance(visibility, Mapping):
        raise RuleError("Ability evolution_visibility must be an object")

    for evolution_id, knowledge in (visibility or {}).items():
        if not isinstance(knowledge, Mapping):
            raise RuleError(
                f"Evolution visibility state must be an object: {evolution_id}"
            )
        disclosure = knowledge.get("state", "hidden")
        if disclosure == "hidden":
            continue
        if disclosure not in {"hinted", "partial", "known", "satisfied"}:
            raise RuleError(
                f"Unsupported evolution disclosure state: {evolution_id}:{disclosure}"
            )
        authored = (
            evolution_definitions.get(evolution_id, {})
            if isinstance(evolution_definitions, Mapping)
            else {}
        )
        if authored is not None and not isinstance(authored, Mapping):
            raise RuleError(f"Evolution definition must be an object: {evolution_id}")
        authored = authored or {}

        if not isinstance(evolution_id, str) or not evolution_id:
            raise RuleError("Evolution visibility keys must be non-empty IDs")
        if disclosure in {"known", "satisfied"}:
            name = _visible_text(
                authored.get("name"),
                f"Evolution display name {evolution_id}",
                default=evolution_id,
            )
        else:
            name = _visible_text(
                knowledge.get("label"),
                f"Evolution visible label {evolution_id}",
                default="Unknown evolution",
            )
        item: Dict[str, Any] = {
            "evolution_id": evolution_id,
            "state": disclosure,
            "name": name,
        }
        hint = knowledge.get("hint")
        if hint is not None:
            item["hint"] = _visible_text(
                hint,
                f"Evolution hint {evolution_id}",
            )
        known_requirements = knowledge.get("known_requirements")
        if known_requirements is not None:
            if (
                not isinstance(known_requirements, list)
                or not all(isinstance(value, str) and value for value in known_requirements)
            ):
                raise RuleError(
                    f"known_requirements must be a list of non-empty strings: {evolution_id}"
                )
            item["known_requirements"] = list(known_requirements)
        output["evolutions"].append(item)

    completed_evolutions = [
        record.get("evolution_id")
        for record in ability.get("evolutions", [])
        if isinstance(record, Mapping) and record.get("evolution_id")
    ]
    output["completed_evolutions"] = completed_evolutions
    return output
