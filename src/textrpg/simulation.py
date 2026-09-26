from __future__ import annotations

from typing import Any, Dict, Iterable, Mapping

from .core import GameState, RuleError
from .modifiers import validate_modifier_mapping
from .stats import ATTRIBUTE_SPECS, SKILL_CATALOG, initialize_resources


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
    if severity < 1 or severity > 5:
        raise RuleError("Condition severity must be in range 1..5")
    try:
        validated_modifiers = validate_modifier_mapping(
            modifiers or {},
            source=f"condition:{condition_id}",
        )
    except ValueError as exc:
        raise RuleError(f"Invalid condition modifiers for {condition_id}: {exc}") from exc

    conditions = state.player.setdefault("conditions", {})
    record = {
        "severity": severity,
        "duration_minutes": duration_minutes,
        "source": source,
        "tags": list(tags),
        "modifiers": validated_modifiers,
        "applied_at": state.time_minutes,
    }
    conditions[condition_id] = record
    return record


def advance_time(state: GameState, minutes: int) -> list[str]:
    if minutes < 0:
        raise RuleError("Cannot advance time by a negative amount")
    state.time_minutes += minutes
    expired: list[str] = []
    conditions = state.player.setdefault("conditions", {})
    for condition_id, record in list(conditions.items()):
        duration = record.get("duration_minutes")
        if duration is None:
            continue
        duration = max(0, int(duration) - minutes)
        record["duration_minutes"] = duration
        if duration == 0:
            expired.append(condition_id)
            del conditions[condition_id]
    return expired


def recover(
    state: GameState,
    minutes: int,
    *,
    quality: float = 1.0,
    set_definitions: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, float]:
    if minutes < 0 or quality < 0:
        raise RuleError("Recovery time and quality must be non-negative")
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
    if minutes <= 0:
        raise RuleError("Training time must be positive")
    if intensity <= 0 or intensity > 2.0:
        raise RuleError("Training intensity must be in range (0, 2]")
    if mentor_bonus < 0:
        raise RuleError("Mentor bonus cannot be negative")

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
    if minutes < 120:
        raise RuleError("Core attributes require at least 120 minutes of focused training")
    if intensity <= 0 or intensity > 2.0:
        raise RuleError("Attribute training intensity must be in range (0, 2]")
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
