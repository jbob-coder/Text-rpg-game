from __future__ import annotations

from math import isfinite
from typing import Any, Dict, Mapping, MutableMapping

from .core import GameState, RuleError
from .modifiers import validate_modifier_mapping
from .progression import gain_ability_mastery, technique_available
from .simulation import advance_time, apply_condition
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
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not isfinite(float(value))
    ):
        raise RuleError(f"Power resource path is missing or non-finite numeric: {path}")
    return float(value)


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
    if isinstance(tags, (str, bytes)) or not all(
        isinstance(tag, str) and tag for tag in tags
    ):
        raise RuleError("Ability tags must be an iterable of non-empty strings")
    if data is not None and not isinstance(data, Mapping):
        raise RuleError("Ability data must be an object")

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
    if not isinstance(ability, MutableMapping):
        raise RuleError(f"Ability state must be an object: {ability_id}")

    ability.setdefault("family", family)
    ability.setdefault("form", form)
    ability.setdefault("tags", list(tags))
    ability.setdefault("data", dict(data or {}))
    ability.setdefault("techniques", {})

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


def discover_technique(state: GameState, ability_id: str, technique_id: str) -> Dict[str, Any]:
    ability = state.abilities.get(ability_id)
    if not ability:
        raise RuleError(f"Unknown ability: {ability_id}")
    techniques = ability.setdefault("techniques", {})
    if technique_id in techniques:
        return techniques[technique_id]
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
    if not isinstance(ability, Mapping):
        raise RuleError(f"Unknown ability: {ability_id}")
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
            for key, minimum in values.items():
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
            if not isinstance(path, str) or not path:
                errors.append("cost paths must be non-empty strings")
                continue
            parts = path.split(".")
            if (
                len(parts) != 2
                or parts[0] not in {"resources", "power_resources"}
                or not parts[1]
            ):
                errors.append(
                    f"costs.{path} must use resources.<id> or power_resources.<id>"
                )
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
            if (
                not isinstance(tags, (list, tuple))
                or not all(isinstance(tag, str) and tag for tag in tags)
            ):
                errors.append(
                    f"{location}.tags must be a list/tuple of non-empty strings"
                )

            modifiers = drawback.get("modifiers")
            if modifiers is not None:
                try:
                    validate_modifier_mapping(
                        modifiers,
                        source=f"technique:{location}",
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
            for key, minimum in values.items():
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
                    source=f"evolution:{location}",
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
    if not ability:
        return {"available": False, "reasons": ["ability_missing"]}

    technique = ability.get("techniques", {}).get(technique_id)
    if not technique:
        return {"available": False, "reasons": ["technique_undiscovered"]}

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
    *,
    equipment_sets: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, Any]:
    definition_errors = validate_evolution_definition(definition)
    if definition_errors:
        raise RuleError(
            "Invalid evolution definition: " + "; ".join(definition_errors)
        )

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

    reasons.extend(
        _extra_requirements_met(
            state,
            requirements,
            equipment_sets=equipment_sets,
        )
    )

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



def _fallback_display_name(value: str, *prefixes: str) -> str:
    if not isinstance(value, str) or not value:
        raise RuleError("Display fallback ID must be a non-empty string")
    display = value
    for prefix in prefixes:
        if display.startswith(prefix):
            display = display[len(prefix):]
            break
    return display.replace("_", " ").title()


def _visible_text(value: Any, label: str, *, default: str | None = None) -> str:
    if value is None and default is not None:
        return default
    if not isinstance(value, str) or not value:
        raise RuleError(f"{label} must be a non-empty string")
    return value


def _visible_resource_path(path: Any, label: str) -> str:
    if not isinstance(path, str) or not path:
        raise RuleError(f"{label} must be a non-empty string")
    parts = path.split(".")
    if len(parts) != 2 or parts[0] not in {"resources", "power_resources"} or not parts[1]:
        raise RuleError(
            f"{label} must use resources.<id> or power_resources.<id>"
        )
    return path


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
            default=_fallback_display_name(ability_id, "ABILITY_"),
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
                    default=_fallback_display_name(technique_id, "TECHNIQUE_"),
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
                default=_fallback_display_name(evolution_id, "EVOLUTION_"),
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
