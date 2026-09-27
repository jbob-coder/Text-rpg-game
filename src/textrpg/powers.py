from __future__ import annotations

import re
from typing import Any, Dict, Mapping, MutableMapping

from .core import GameState, RuleError
from .progression import gain_ability_mastery, technique_available
from .simulation import advance_time, apply_condition


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


def _validate_requirements_definition(
    ability_id: str,
    technique_id: str,
    field_name: str,
    requirements: Any,
    errors: list[str],
) -> None:
    location = f"{ability_id}.{technique_id}.{field_name}"
    if requirements is None:
        return
    if not isinstance(requirements, Mapping):
        errors.append(f"{location} must be an object")
        return

    for numeric_field in ("rank_min", "mastery_xp_min"):
        value = requirements.get(numeric_field, 0)
        if not isinstance(value, (int, float)) or value < 0:
            errors.append(f"{location}.{numeric_field} must be non-negative numeric")

    for list_field in ("knowledge", "perks"):
        values = requirements.get(list_field, [])
        if not isinstance(values, list):
            errors.append(f"{location}.{list_field} must be a list")
            continue
        for value in values:
            if not isinstance(value, str) or not _STABLE_ID.fullmatch(value):
                errors.append(
                    f"{location}.{list_field} contains invalid stable ID: {value!r}"
                )

    for map_field in ("attributes", "skills"):
        values = requirements.get(map_field, {})
        if not isinstance(values, Mapping):
            errors.append(f"{location}.{map_field} must be an object")
            continue
        for key, minimum in values.items():
            if not isinstance(key, str) or not key:
                errors.append(f"{location}.{map_field} has invalid key")
            if not isinstance(minimum, (int, float)):
                errors.append(
                    f"{location}.{map_field}.{key} minimum must be numeric"
                )

    flags = requirements.get("flags", {})
    if not isinstance(flags, Mapping):
        errors.append(f"{location}.flags must be an object")

    items = requirements.get("items", {})
    if not isinstance(items, Mapping):
        errors.append(f"{location}.items must be an object")
    else:
        for item_id, quantity in items.items():
            if not isinstance(item_id, str) or not _STABLE_ID.fullmatch(item_id):
                errors.append(f"{location}.items has invalid item ID: {item_id!r}")
            if not isinstance(quantity, int) or quantity < 1:
                errors.append(
                    f"{location}.items.{item_id} quantity must be integer >= 1"
                )

    techniques = requirements.get("techniques", {})
    if not isinstance(techniques, Mapping):
        errors.append(f"{location}.techniques must be an object")
    else:
        for required_id, stage in techniques.items():
            if not isinstance(required_id, str) or not _STABLE_ID.fullmatch(required_id):
                errors.append(
                    f"{location}.techniques has invalid technique ID: {required_id!r}"
                )
            if stage not in _STAGE_ORDER or stage == "unknown":
                errors.append(
                    f"{location}.techniques.{required_id} has unsupported stage {stage!r}"
                )


def validate_power_definitions(
    definitions: Mapping[str, Mapping[str, Any]],
) -> list[str]:
    """Validate authored power/resource/technique definitions before play."""
    errors: list[str] = []
    for ability_id, definition in definitions.items():
        if not isinstance(ability_id, str) or not _STABLE_ID.fullmatch(ability_id):
            errors.append(f"ability_id must be a stable uppercase ID: {ability_id!r}")
            continue
        if not isinstance(definition, Mapping):
            errors.append(f"{ability_id} power definition must be an object")
            continue

        resource = definition.get("resource")
        if resource is not None:
            if not isinstance(resource, Mapping):
                errors.append(f"{ability_id}.resource must be an object")
            else:
                path = resource.get("path")
                if not isinstance(path, str) or not path.startswith("power_resources."):
                    errors.append(
                        f"{ability_id}.resource.path must start with 'power_resources.'"
                    )
                maximum = resource.get("maximum")
                starting = resource.get("starting", maximum)
                recovery = resource.get("recovery_per_hour", 0)
                for field, value in (("maximum", maximum), ("starting", starting), ("recovery_per_hour", recovery)):
                    if not isinstance(value, (int, float)):
                        errors.append(f"{ability_id}.resource.{field} must be numeric")
                if isinstance(maximum, (int, float)) and maximum <= 0:
                    errors.append(f"{ability_id}.resource.maximum must be positive")
                if isinstance(starting, (int, float)) and isinstance(maximum, (int, float)):
                    if starting < 0 or starting > maximum:
                        errors.append(
                            f"{ability_id}.resource.starting must be in range 0..maximum"
                        )
                if isinstance(recovery, (int, float)) and recovery < 0:
                    errors.append(
                        f"{ability_id}.resource.recovery_per_hour cannot be negative"
                    )

        techniques = definition.get("techniques", {})
        if not isinstance(techniques, Mapping):
            errors.append(f"{ability_id}.techniques must be an object")
            continue
        for technique_id, technique in techniques.items():
            if not isinstance(technique_id, str) or not _STABLE_ID.fullmatch(technique_id):
                errors.append(
                    f"{ability_id} technique_id must be a stable uppercase ID: {technique_id!r}"
                )
                continue
            if not isinstance(technique, Mapping):
                errors.append(f"{ability_id}.{technique_id} must be an object")
                continue
            _validate_requirements_definition(
                ability_id,
                technique_id,
                "discovery_requirements",
                technique.get("discovery_requirements", {}),
                errors,
            )
            _validate_requirements_definition(
                ability_id,
                technique_id,
                "requirements",
                technique.get("requirements", {}),
                errors,
            )
            stage_min = technique.get("stage_min", "discovered")
            if stage_min not in _STAGE_ORDER or stage_min == "unknown":
                errors.append(
                    f"{ability_id}.{technique_id}.stage_min is unsupported: {stage_min!r}"
                )
            cooldown = technique.get("cooldown_minutes", 0)
            if not isinstance(cooldown, int) or cooldown < 0:
                errors.append(
                    f"{ability_id}.{technique_id}.cooldown_minutes must be a non-negative integer"
                )
            for path, amount in technique.get("costs", {}).items():
                if not isinstance(path, str) or not path:
                    errors.append(f"{ability_id}.{technique_id} has invalid cost path")
                if not isinstance(amount, (int, float)) or amount < 0:
                    errors.append(
                        f"{ability_id}.{technique_id} cost {path!r} must be non-negative numeric"
                    )
            for drawback in technique.get("drawbacks", []):
                if not isinstance(drawback, Mapping) or drawback.get("type") != "condition":
                    errors.append(
                        f"{ability_id}.{technique_id} drawbacks must be condition records"
                    )
                    continue
                condition_id = drawback.get("condition_id")
                if not isinstance(condition_id, str) or not _STABLE_ID.fullmatch(condition_id):
                    errors.append(
                        f"{ability_id}.{technique_id} drawback condition_id must be stable uppercase ID"
                    )
    return errors


def assert_valid_power_definitions(
    definitions: Mapping[str, Mapping[str, Any]],
) -> None:
    errors = validate_power_definitions(definitions)
    if errors:
        raise RuleError("Invalid power definitions:\n- " + "\n- ".join(errors))


def technique_stage(xp: float) -> str:
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


def _set_player_path(state: GameState, path: str, value: Any) -> None:
    parts = path.split(".")
    current: MutableMapping[str, Any] = state.player
    for part in parts[:-1]:
        node = current.get(part)
        if not isinstance(node, MutableMapping):
            node = {}
            current[part] = node
        current = node
    current[parts[-1]] = value


def _numeric_player_path(state: GameState, path: str) -> float:
    value = _player_path(state, path)
    if not isinstance(value, (int, float)):
        raise RuleError(f"Power resource path is missing or non-numeric: {path}")
    return float(value)


def initialize_power_resource(
    state: GameState,
    ability_id: str,
    definition: Mapping[str, Any],
) -> Dict[str, float | str] | None:
    """Initialize an ability-specific resource without creating a universal mana pool."""
    errors = validate_power_definitions({ability_id: definition})
    if errors:
        raise RuleError("Invalid power definition:\n- " + "\n- ".join(errors))
    resource = definition.get("resource")
    if not resource:
        return None
    path = resource["path"]
    maximum = float(resource["maximum"])
    starting = float(resource.get("starting", maximum))
    current = _player_path(state, path)
    if current is None:
        _set_player_path(state, path, starting)
        current = starting
    elif not isinstance(current, (int, float)):
        raise RuleError(f"Power resource path is non-numeric: {path}")
    return {
        "path": path,
        "current": float(current),
        "maximum": maximum,
        "recovery_per_hour": float(resource.get("recovery_per_hour", 0)),
    }


def recover_power_resource(
    state: GameState,
    ability_id: str,
    definition: Mapping[str, Any],
    *,
    minutes: int,
    quality: float = 1.0,
) -> Dict[str, Any]:
    """Recover one authored power resource while advancing shared world time."""
    if minutes <= 0:
        raise RuleError("Power recovery time must be positive")
    if quality < 0:
        raise RuleError("Power recovery quality cannot be negative")
    if ability_id not in state.abilities:
        raise RuleError(f"Unknown ability: {ability_id}")
    resource = initialize_power_resource(state, ability_id, definition)
    if resource is None:
        raise RuleError(f"Ability has no recoverable power resource: {ability_id}")

    path = str(resource["path"])
    before = _numeric_player_path(state, path)
    maximum = float(resource["maximum"])
    rate = float(resource["recovery_per_hour"])
    amount = rate * (minutes / 60.0) * quality
    after = min(maximum, before + amount)
    _set_player_path(state, path, after)
    advance_time(state, minutes)

    event = {
        "type": "power_resource_recovery",
        "ability_id": ability_id,
        "resource_path": path,
        "before": round(before, 3),
        "after": round(after, 3),
        "gained": round(after - before, 3),
        "minutes": minutes,
        "quality": quality,
        "time_minutes": state.time_minutes,
    }
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
    definition: Mapping[str, Any] | None = None,
) -> Dict[str, Any]:
    """Create the persistent shell of an ability without granting mastery."""
    is_new = ability_id not in state.abilities
    ability = state.abilities.setdefault(
        ability_id,
        {
            "rank": 0,
            "mastery_xp": 0.0,
            "mastery_stage": "discovered",
            "techniques": {},
        },
    )
    ability.setdefault("family", family)
    ability.setdefault("form", form)
    ability.setdefault("tags", list(tags))
    ability.setdefault("data", dict(data or {}))
    ability.setdefault("techniques", {})

    if definition is not None:
        initialize_power_resource(state, ability_id, definition)

    if is_new:
        state.history.append(
            {
                "type": "ability_discovered",
                "ability_id": ability_id,
                "family": ability.get("family"),
                "form": ability.get("form"),
                "turn": state.turn,
                "time_minutes": state.time_minutes,
            }
        )
    return ability


def technique_discovery_status(
    state: GameState,
    ability_id: str,
    technique_id: str,
    definition: Mapping[str, Any] | None = None,
) -> Dict[str, Any]:
    """Report whether an authored technique may be discovered now."""
    ability = state.abilities.get(ability_id)
    if not ability:
        return {"available": False, "reasons": ["ability_missing"]}

    if technique_id in ability.get("techniques", {}):
        return {"available": True, "reasons": [], "already_discovered": True}

    requirements = (definition or {}).get("discovery_requirements", {})
    reasons: list[str] = []

    if float(ability.get("rank", 0)) < float(requirements.get("rank_min", 0)):
        reasons.append("rank")
    if float(ability.get("mastery_xp", 0)) < float(
        requirements.get("mastery_xp_min", 0)
    ):
        reasons.append("mastery_xp")

    for knowledge_id in requirements.get("knowledge", []):
        if knowledge_id not in state.knowledge:
            reasons.append(f"knowledge:{knowledge_id}")
    for perk_id in requirements.get("perks", []):
        if perk_id not in state.perks:
            reasons.append(f"perk:{perk_id}")

    reasons.extend(_extra_requirements_met(state, requirements))

    techniques = ability.get("techniques", {})
    for required_id, stage_min in requirements.get("techniques", {}).items():
        record = techniques.get(required_id)
        if not record or not _stage_at_least(record.get("stage", "unknown"), stage_min):
            reasons.append(f"technique:{required_id}:{stage_min}")

    return {"available": not reasons, "reasons": reasons, "already_discovered": False}


def discover_technique(
    state: GameState,
    ability_id: str,
    technique_id: str,
    definition: Mapping[str, Any] | None = None,
) -> Dict[str, Any]:
    ability = state.abilities.get(ability_id)
    if not ability:
        raise RuleError(f"Unknown ability: {ability_id}")
    techniques = ability.setdefault("techniques", {})
    if technique_id in techniques:
        return techniques[technique_id]

    status = technique_discovery_status(
        state, ability_id, technique_id, definition
    )
    if not status["available"]:
        raise RuleError(
            f"Technique cannot be discovered: {technique_id} "
            f"({', '.join(status['reasons'])})"
        )

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
    if xp < 0:
        raise RuleError("Technique mastery gain cannot be negative")
    ability = state.abilities.get(ability_id)
    if not ability:
        raise RuleError(f"Unknown ability: {ability_id}")
    technique = ability.get("techniques", {}).get(technique_id)
    if not technique:
        raise RuleError(f"Technique has not been discovered: {technique_id}")

    before = dict(technique)
    technique["mastery_xp"] = float(technique.get("mastery_xp", 0.0)) + float(xp)
    technique["stage"] = technique_stage(technique["mastery_xp"])
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
    """Practice an already-discovered technique through paid world time.

    Practice is intentionally gradual: it consumes stamina/focus, advances the
    simulation clock, uses diminishing returns, and grants less overall ability
    mastery than technique-specific mastery.
    """
    if minutes < 30:
        raise RuleError("Technique practice requires at least 30 minutes")
    if intensity <= 0 or intensity > 2.0:
        raise RuleError("Technique practice intensity must be in range (0, 2]")
    if mentor_bonus < 0 or mentor_bonus > 1.0:
        raise RuleError("Technique mentor bonus must be in range 0..1")
    if stamina_per_hour < 0 or focus_per_hour < 0:
        raise RuleError("Technique practice resource rates cannot be negative")

    ability = state.abilities.get(ability_id)
    if not ability:
        raise RuleError(f"Unknown ability: {ability_id}")
    technique = ability.get("techniques", {}).get(technique_id)
    if not technique:
        raise RuleError(f"Technique has not been discovered: {technique_id}")

    ready_at = int(technique.get("ready_at_minutes", 0))
    if state.time_minutes < ready_at:
        raise RuleError(
            f"Technique is still recovering for {ready_at - state.time_minutes} minutes"
        )

    hours = minutes / 60.0
    stamina_cost = hours * float(stamina_per_hour) * intensity
    focus_cost = hours * float(focus_per_hour) * intensity

    stamina_before = _numeric_player_path(state, "resources.stamina")
    focus_before = _numeric_player_path(state, "resources.focus")
    if stamina_before < stamina_cost or focus_before < focus_cost:
        raise RuleError("Insufficient stamina or focus for technique practice")

    technique_before = float(technique.get("mastery_xp", 0.0))
    ability_before = float(ability.get("mastery_xp", 0.0))
    learning_factor = max(0.15, 1.0 - technique_before / 450.0)
    technique_gain = (
        hours
        * 8.0
        * intensity
        * learning_factor
        * (1.0 + mentor_bonus)
    )
    ability_gain = technique_gain * 0.35

    # Validate everything above before spending resources or advancing time.
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
) -> list[str]:
    reasons: list[str] = []

    attributes = state.player.get("attributes", {})
    for key, minimum in requirements.get("attributes", {}).items():
        if float(attributes.get(key, 0)) < float(minimum):
            reasons.append(f"attribute:{key}")

    skills = state.player.get("skills", {})
    for key, minimum in requirements.get("skills", {}).items():
        if float(skills.get(key, 0)) < float(minimum):
            reasons.append(f"skill:{key}")

    for key, expected in requirements.get("flags", {}).items():
        if state.flags.get(key) != expected:
            reasons.append(f"flag:{key}")

    for item_id, quantity in requirements.get("items", {}).items():
        if state.inventory.get(item_id, 0) < int(quantity):
            reasons.append(f"item:{item_id}")

    return reasons


def technique_use_status(
    state: GameState,
    ability_id: str,
    technique_id: str,
    definition: Mapping[str, Any],
) -> Dict[str, Any]:
    reasons: list[str] = []
    ability = state.abilities.get(ability_id)
    if not ability:
        return {"available": False, "reasons": ["ability_missing"]}

    technique = ability.get("techniques", {}).get(technique_id)
    if not technique:
        return {"available": False, "reasons": ["technique_undiscovered"]}

    requirements = definition.get("requirements", {})
    if not technique_available(state, ability_id, dict(requirements)):
        reasons.append("ability_requirements")

    reasons.extend(_extra_requirements_met(state, requirements))

    minimum_stage = definition.get("stage_min", "discovered")
    if not _stage_at_least(technique.get("stage", "unknown"), minimum_stage):
        reasons.append(f"stage:{minimum_stage}")

    ready_at = int(technique.get("ready_at_minutes", 0))
    if state.time_minutes < ready_at:
        reasons.append(f"cooldown:{ready_at - state.time_minutes}")

    for path, amount_raw in definition.get("costs", {}).items():
        amount = float(amount_raw)
        if amount < 0:
            raise RuleError(f"Technique cost cannot be negative: {path}")
        current = _numeric_player_path(state, path)
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
) -> Dict[str, Any]:
    status = technique_use_status(state, ability_id, technique_id, definition)
    if not status["available"]:
        raise RuleError(
            f"Technique cannot be used: {technique_id} ({', '.join(status['reasons'])})"
        )

    ability = state.abilities[ability_id]
    technique = ability["techniques"][technique_id]

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
) -> Dict[str, Any]:
    ability = state.abilities.get(ability_id)
    if not ability:
        return {"available": False, "reasons": ["ability_missing"]}

    if evolution_id in {
        record.get("evolution_id") for record in ability.get("evolutions", [])
    }:
        return {"available": False, "reasons": ["already_evolved"]}

    requirements = definition.get("requirements", {})
    reasons: list[str] = []

    if ability.get("rank", 0) < int(requirements.get("rank_min", 0)):
        reasons.append("rank")
    if float(ability.get("mastery_xp", 0)) < float(
        requirements.get("mastery_xp_min", 0)
    ):
        reasons.append("mastery_xp")

    for knowledge_id in requirements.get("knowledge", []):
        if knowledge_id not in state.knowledge:
            reasons.append(f"knowledge:{knowledge_id}")

    for perk_id in requirements.get("perks", []):
        if perk_id not in state.perks:
            reasons.append(f"perk:{perk_id}")

    reasons.extend(_extra_requirements_met(state, requirements))

    techniques = ability.get("techniques", {})
    for required_id, stage_min in requirements.get("techniques", {}).items():
        record = techniques.get(required_id)
        if not record or not _stage_at_least(record.get("stage", "unknown"), stage_min):
            reasons.append(f"technique:{required_id}:{stage_min}")

    result = definition.get("result", {})
    for item_id, quantity in result.get("consume_items", {}).items():
        if int(quantity) < 0:
            raise RuleError(f"Evolution item consumption cannot be negative: {item_id}")
        if state.inventory.get(item_id, 0) < int(quantity):
            reasons.append(f"consume_item:{item_id}")

    for perk_id in result.get("grant_perks", {}):
        if perk_id in state.perks:
            reasons.append(f"perk_exists:{perk_id}")

    if "rank_floor" in result and int(result["rank_floor"]) < 0:
        raise RuleError("Evolution rank floor cannot be negative")

    return {"available": not reasons, "reasons": reasons}


def evolve_ability(
    state: GameState,
    ability_id: str,
    evolution_id: str,
    definition: Mapping[str, Any],
) -> Dict[str, Any]:
    status = ability_evolution_status(state, ability_id, evolution_id, definition)
    if not status["available"]:
        raise RuleError(
            f"Ability cannot evolve: {evolution_id} ({', '.join(status['reasons'])})"
        )

    ability = state.abilities[ability_id]
    result = definition.get("result", {})
    previous_form = ability.get("form")
    if "form" in result:
        ability["form"] = result["form"]
    if "rank_floor" in result:
        rank_floor = int(result["rank_floor"])
        ability["rank_floor"] = max(int(ability.get("rank_floor", 0)), rank_floor)
        ability["rank"] = max(int(ability.get("rank", 0)), ability["rank_floor"])

    if "tags" in result:
        tags = list(dict.fromkeys([*ability.get("tags", []), *result["tags"]]))
        ability["tags"] = tags

    consumed_items: Dict[str, int] = {}
    for item_id, quantity_raw in result.get("consume_items", {}).items():
        quantity = int(quantity_raw)
        if quantity:
            state.inventory[item_id] -= quantity
            consumed_items[item_id] = quantity
            if state.inventory[item_id] <= 0:
                del state.inventory[item_id]

    granted_perks: list[str] = []
    for perk_id, perk in result.get("grant_perks", {}).items():
        state.perks[perk_id] = {
            "source": f"evolution:{ability_id}:{evolution_id}",
            "modifiers": dict(perk.get("modifiers", {})),
            "tags": list(perk.get("tags", [])),
        }
        granted_perks.append(perk_id)

    record = {
        "evolution_id": evolution_id,
        "time_minutes": state.time_minutes,
        "previous_form": previous_form,
        "form": ability.get("form"),
    }
    ability.setdefault("evolutions", []).append(record)

    event = {
        "type": "ability_evolution",
        "ability_id": ability_id,
        "evolution_id": evolution_id,
        "time_minutes": state.time_minutes,
        "previous_form": previous_form,
        "form": ability.get("form"),
        "granted_perks": granted_perks,
        "consumed_items": consumed_items,
    }
    state.history.append(event)
    return event
