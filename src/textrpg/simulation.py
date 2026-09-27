from __future__ import annotations

from math import isfinite
from typing import Any, Dict, Iterable, Mapping

from .core import GameState, RuleError
from .modifiers import validate_modifier_mapping
from .stats import ATTRIBUTE_SPECS, SKILL_CATALOG, initialize_resources


def _minutes(value: Any, label: str, *, minimum: int = 0) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise RuleError(f"{label} must be an integer")
    if value < minimum:
        raise RuleError(f"{label} must be >= {minimum}")
    return value


def _finite(value: Any, label: str, *, minimum: float | None = None, maximum: float | None = None) -> float:
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


def apply_condition(
    state: GameState,
    condition_id: str,
    *,
    severity: int = 1,
    duration_minutes: int | None = None,
    source: str = "unknown",
    tags: Iterable[str] = (),
    modifiers: Mapping[str, float] | None = None,
) -> Dict[str, Any]:
    if not isinstance(condition_id, str) or not condition_id:
        raise RuleError("Condition ID must be a non-empty string")
    if isinstance(severity, bool) or not isinstance(severity, int) or severity < 1 or severity > 5:
        raise RuleError("Condition severity must be an integer in range 1..5")
    if duration_minutes is not None:
        _minutes(duration_minutes, "Condition duration_minutes", minimum=0)
    if not isinstance(source, str) or not source:
        raise RuleError("Condition source must be a non-empty string")
    if isinstance(tags, (str, bytes)):
        raise RuleError("Condition tags must be an iterable of non-empty strings")
    tag_list = list(tags)
    if not all(isinstance(tag, str) and tag for tag in tag_list):
        raise RuleError("Condition tags must be an iterable of non-empty strings")
    try:
        validated_modifiers = validate_modifier_mapping(
            modifiers or {},
            source=f"condition:{condition_id}",
        )
    except ValueError as exc:
        raise RuleError(f"Invalid condition modifiers for {condition_id}: {exc}") from exc

    conditions = state.player.setdefault("conditions", {})
    if not isinstance(conditions, dict):
        raise RuleError("player.conditions must be an object")
    record = {
        "severity": severity,
        "duration_minutes": duration_minutes,
        "source": source,
        "tags": tag_list,
        "modifiers": validated_modifiers,
        "applied_at": state.time_minutes,
    }
    conditions[condition_id] = record
    return record


def advance_time(state: GameState, minutes: int) -> list[str]:
    """Advance world time atomically after validating all timed conditions."""
    minutes = _minutes(minutes, "Time advance minutes", minimum=0)

    existing_conditions = state.player.get("conditions")
    if existing_conditions is None:
        conditions: dict[str, Any] = {}
    elif not isinstance(existing_conditions, dict):
        raise RuleError("player.conditions must be an object")
    else:
        conditions = existing_conditions

    duration_updates: Dict[str, int] = {}
    expired: list[str] = []
    for condition_id, record in conditions.items():
        if not isinstance(record, Mapping):
            raise RuleError(f"Condition record must be an object: {condition_id}")
        duration = record.get("duration_minutes")
        if duration is None:
            continue
        if not isinstance(record, dict):
            raise RuleError(f"Timed condition record must be mutable: {condition_id}")
        next_duration = max(
            0,
            _minutes(
                duration,
                f"Condition duration_minutes {condition_id}",
                minimum=0,
            )
            - minutes,
        )
        if next_duration == 0:
            expired.append(condition_id)
        else:
            duration_updates[condition_id] = next_duration

    # Validation is complete. Commit time and condition-duration changes together.
    state.time_minutes += minutes
    if existing_conditions is None:
        state.player["conditions"] = conditions

    for condition_id, next_duration in duration_updates.items():
        conditions[condition_id]["duration_minutes"] = next_duration

    for condition_id in expired:
        del conditions[condition_id]

    return expired


def recover(
    state: GameState,
    minutes: int,
    *,
    quality: float = 1.0,
    set_definitions: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, float]:
    minutes = _minutes(minutes, "Recovery minutes", minimum=0)
    quality = _finite(quality, "Recovery quality", minimum=0.0)
    maxima = initialize_resources(state, set_definitions=set_definitions)
    resources = state.player["resources"]
    hours = minutes / 60.0
    rates = {"health": 0.04, "stamina": 0.30, "focus": 0.22, "resolve": 0.15}
    gained: Dict[str, float] = {}
    for key, rate in rates.items():
        before = float(resources.get(key, 0))
        amount = maxima[key] * rate * hours * quality
        after = min(maxima[key], before + amount)
        resources[key] = round(max(0.0, after), 3)
        gained[key] = round(resources[key] - before, 3)
    advance_time(state, minutes)
    return gained


def train(
    state: GameState,
    *,
    skill: str,
    minutes: int,
    intensity: float = 1.0,
    mentor_bonus: float = 0.0,
    set_definitions: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, Any]:
    if skill not in SKILL_CATALOG:
        raise RuleError(f"Unknown skill: {skill}")
    minutes = _minutes(minutes, "Training minutes", minimum=1)
    intensity = _finite(
        intensity,
        "Training intensity",
        minimum=0.0000001,
        maximum=2.0,
    )
    mentor_bonus = _finite(mentor_bonus, "Mentor bonus", minimum=0.0)

    initialize_resources(state, set_definitions=set_definitions)
    resources = state.player["resources"]
    stamina_cost = minutes / 60.0 * 8.0 * intensity
    focus_cost = minutes / 60.0 * 5.0 * intensity
    if resources["stamina"] < stamina_cost or resources["focus"] < focus_cost:
        raise RuleError("Insufficient stamina or focus for this training session")

    current = float(state.player.setdefault("skills", {}).get(skill, 0))
    learning_factor = max(0.10, 1.0 - current / 115.0)
    gain = (minutes / 60.0) * intensity * learning_factor * (1.0 + mentor_bonus)
    new_value = min(100.0, current + gain)
    state.player["skills"][skill] = round(new_value, 3)
    resources["stamina"] = round(resources["stamina"] - stamina_cost, 3)
    resources["focus"] = round(resources["focus"] - focus_cost, 3)
    advance_time(state, minutes)

    event = {
        "type": "training",
        "skill": skill,
        "minutes": minutes,
        "intensity": intensity,
        "mentor_bonus": mentor_bonus,
        "before": current,
        "after": state.player["skills"][skill],
        "gain": round(state.player["skills"][skill] - current, 3),
        "time_minutes": state.time_minutes,
    }
    state.history.append(event)
    return event


def train_attribute(
    state: GameState,
    *,
    attribute: str,
    minutes: int,
    intensity: float = 1.0,
) -> Dict[str, Any]:
    if attribute not in ATTRIBUTE_SPECS:
        raise RuleError(f"Unknown attribute: {attribute}")
    minutes = _minutes(minutes, "Attribute training minutes", minimum=120)
    intensity = _finite(
        intensity,
        "Attribute training intensity",
        minimum=0.0000001,
        maximum=2.0,
    )
    current = float(state.player.setdefault("attributes", {}).get(attribute, 0))
    gain = (minutes / 60.0) * 0.08 * intensity * max(0.15, 1.0 - current / 110.0)
    after = min(100.0, current + gain)
    state.player["attributes"][attribute] = round(after, 3)
    advance_time(state, minutes)
    event = {
        "type": "attribute_training",
        "attribute": attribute,
        "minutes": minutes,
        "before": current,
        "after": state.player["attributes"][attribute],
        "gain": round(state.player["attributes"][attribute] - current, 3),
        "time_minutes": state.time_minutes,
    }
    state.history.append(event)
    return event
