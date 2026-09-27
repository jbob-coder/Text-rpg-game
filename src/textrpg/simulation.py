from __future__ import annotations

from copy import deepcopy
from math import isfinite
from typing import Any, Dict, Iterable, Mapping, MutableMapping

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


def _time_advance_plan(
    state: GameState,
    minutes: int,
) -> tuple[int, dict[str, Any], bool, Dict[str, int], list[str]]:
    minutes = _minutes(minutes, "Time advance minutes", minimum=0)

    existing_conditions = state.player.get("conditions")
    created_conditions = existing_conditions is None
    if created_conditions:
        conditions: dict[str, Any] = {}
    elif not isinstance(existing_conditions, dict):
        raise RuleError("player.conditions must be an object")
    else:
        conditions = existing_conditions

    duration_updates: Dict[str, int] = {}
    expired: list[str] = []
    for condition_id, record in conditions.items():
        if not isinstance(condition_id, str) or not condition_id:
            raise RuleError("Condition IDs must be non-empty strings")
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

    return minutes, conditions, created_conditions, duration_updates, expired


def validate_time_advance(state: GameState, minutes: int) -> None:
    """Validate that advancing time can commit without mutating state."""
    _time_advance_plan(state, minutes)


def advance_time(state: GameState, minutes: int) -> list[str]:
    """Advance world time atomically after validating all timed conditions."""
    (
        minutes,
        conditions,
        created_conditions,
        duration_updates,
        expired,
    ) = _time_advance_plan(state, minutes)

    state.time_minutes += minutes
    if created_conditions:
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
    validate_time_advance(state, minutes)
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
    validate_time_advance(state, minutes)
    if not isinstance(state.history, list):
        raise RuleError("state.history must be a list")
    if not isinstance(state.player, MutableMapping):
        raise RuleError("player state must be mutable")

    existing_skills = state.player.get("skills")
    if existing_skills is None:
        skills: MutableMapping[str, Any] = {}
        create_skills = True
    elif not isinstance(existing_skills, MutableMapping):
        raise RuleError("player.skills must be a mutable object")
    else:
        skills = existing_skills
        create_skills = False

    current_raw = skills.get(skill, 0)
    current = _finite(
        current_raw,
        f"Skill state {skill}",
        minimum=0.0,
        maximum=100.0,
    )

    had_resources = "resources" in state.player
    resources_before = deepcopy(state.player.get("resources")) if had_resources else None
    initialize_resources(state, set_definitions=set_definitions)
    resources = state.player["resources"]
    stamina_cost = minutes / 60.0 * 8.0 * intensity
    focus_cost = minutes / 60.0 * 5.0 * intensity
    if resources["stamina"] < stamina_cost or resources["focus"] < focus_cost:
        # Resource normalization is part of the training transaction. A failed
        # session must not leave newly written maxima/clamps behind.
        if had_resources:
            state.player["resources"] = resources_before
        else:
            state.player.pop("resources", None)
        raise RuleError("Insufficient stamina or focus for this training session")

    if create_skills:
        state.player["skills"] = skills
    learning_factor = max(0.10, 1.0 - current / 115.0)
    gain = (minutes / 60.0) * intensity * learning_factor * (1.0 + mentor_bonus)
    new_value = min(100.0, current + gain)
    skills[skill] = round(new_value, 3)
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
        "after": skills[skill],
        "gain": round(skills[skill] - current, 3),
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
    validate_time_advance(state, minutes)
    if not isinstance(state.history, list):
        raise RuleError("state.history must be a list")
    if not isinstance(state.player, MutableMapping):
        raise RuleError("player state must be mutable")

    existing_attributes = state.player.get("attributes")
    if existing_attributes is None:
        attributes: MutableMapping[str, Any] = {}
        create_attributes = True
    elif not isinstance(existing_attributes, MutableMapping):
        raise RuleError("player.attributes must be a mutable object")
    else:
        attributes = existing_attributes
        create_attributes = False

    current = _finite(
        attributes.get(attribute, 0),
        f"Attribute state {attribute}",
        minimum=float(ATTRIBUTE_SPECS[attribute]["min"]),
        maximum=float(ATTRIBUTE_SPECS[attribute]["max"]),
    )
    gain = (minutes / 60.0) * 0.08 * intensity * max(0.15, 1.0 - current / 110.0)
    after = min(100.0, current + gain)
    if create_attributes:
        state.player["attributes"] = attributes
    attributes[attribute] = round(after, 3)
    advance_time(state, minutes)
    event = {
        "type": "attribute_training",
        "attribute": attribute,
        "minutes": minutes,
        "before": current,
        "after": attributes[attribute],
        "gain": round(attributes[attribute] - current, 3),
        "time_minutes": state.time_minutes,
    }
    state.history.append(event)
    return event
