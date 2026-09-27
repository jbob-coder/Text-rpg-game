from __future__ import annotations

from math import isfinite
from typing import Any, Dict, Mapping, MutableMapping, Sequence

from .beasts import validate_beast_state
from .core import RuleError


def _finite(value: Any, label: str, *, minimum: float | None = None, maximum: float | None = None) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not isfinite(float(value)):
        raise RuleError(f"{label} must be a finite number")
    number = float(value)
    if minimum is not None and number < minimum:
        raise RuleError(f"{label} must be >= {minimum}")
    if maximum is not None and number > maximum:
        raise RuleError(f"{label} must be <= {maximum}")
    return number


def validate_level_thresholds(thresholds: Sequence[Any]) -> list[float]:
    """Validate cumulative XP required for levels 1..N.

    Index 0 is level 1 and must be exactly zero. A sequence is used instead of
    integer-keyed JSON objects so authored content round-trips without key coercion.
    """
    if isinstance(thresholds, (str, bytes)) or not isinstance(thresholds, Sequence) or not thresholds:
        raise RuleError("level_thresholds must be a non-empty list")

    validated: list[float] = []
    previous: float | None = None
    for index, raw in enumerate(thresholds):
        value = _finite(raw, f"level_thresholds[{index}]", minimum=0.0)
        if index == 0 and value != 0.0:
            raise RuleError("level 1 threshold must be exactly 0")
        if previous is not None and value <= previous:
            raise RuleError("level thresholds must increase strictly")
        validated.append(value)
        previous = value
    return validated


def validate_development_rules(rules: Mapping[str, Mapping[str, Any]]) -> None:
    if not isinstance(rules, Mapping):
        raise RuleError("development rules must be an object")
    for event_type, rule in rules.items():
        if not isinstance(event_type, str) or not event_type:
            raise RuleError("development event IDs must be non-empty strings")
        if not isinstance(rule, Mapping):
            raise RuleError(f"Development rule must be an object: {event_type}")
        _finite(rule.get("base_xp", 0.0), f"{event_type}.base_xp", minimum=0.0)
        enabled = rule.get("enabled", True)
        if not isinstance(enabled, bool):
            raise RuleError(f"{event_type}.enabled must be boolean")


def level_for_xp(total_xp: float, thresholds: Sequence[Any]) -> int:
    total_xp = _finite(total_xp, "total_xp", minimum=0.0)
    validated = validate_level_thresholds(thresholds)
    level = 1
    for index, threshold in enumerate(validated, start=1):
        if total_xp >= threshold:
            level = index
        else:
            break
    return level


def preview_development_event(
    beast: Mapping[str, Any],
    *,
    event_type: str,
    significance: float,
    novelty: float,
    rules: Mapping[str, Mapping[str, Any]],
    level_thresholds: Sequence[Any],
) -> Dict[str, Any]:
    """Preview earned beast development without mutating state.

    `novelty` is an explicit anti-farm input: repeating an already-mastered low-risk
    event can remain meaningful but yields progressively less development.
    """
    validate_beast_state(beast)
    validate_development_rules(rules)
    thresholds = validate_level_thresholds(level_thresholds)
    if not isinstance(event_type, str) or not event_type:
        raise RuleError("event_type must be a non-empty string")
    if event_type not in rules:
        raise RuleError(f"Unknown development event type: {event_type}")

    significance = _finite(significance, "significance", minimum=0.0, maximum=1.0)
    novelty = _finite(novelty, "novelty", minimum=0.0, maximum=1.0)

    before_xp = _finite(beast.get("development_xp", 0.0), "beast.development_xp", minimum=0.0)
    before_level = beast.get("level", 1)
    expected_level = level_for_xp(before_xp, thresholds)
    if before_level != expected_level:
        raise RuleError(
            f"beast.level {before_level} does not match development_xp level {expected_level}"
        )

    rule = rules[event_type]
    base_xp = float(rule.get("base_xp", 0.0))
    gain = 0.0 if rule.get("enabled", True) is False else base_xp * significance * novelty
    gain = round(gain, 4)
    after_xp = round(before_xp + gain, 4)
    after_level = level_for_xp(after_xp, thresholds)

    return {
        "event_type": event_type,
        "significance": significance,
        "novelty": novelty,
        "before_xp": before_xp,
        "xp_gain": gain,
        "after_xp": after_xp,
        "before_level": before_level,
        "after_level": after_level,
        "levels_gained": after_level - before_level,
    }


def apply_development_event(
    beast: MutableMapping[str, Any],
    *,
    event_type: str,
    significance: float,
    novelty: float,
    rules: Mapping[str, Mapping[str, Any]],
    level_thresholds: Sequence[Any],
) -> Dict[str, Any]:
    if not isinstance(beast, MutableMapping):
        raise RuleError("beast state must be mutable")
    result = preview_development_event(
        beast,
        event_type=event_type,
        significance=significance,
        novelty=novelty,
        rules=rules,
        level_thresholds=level_thresholds,
    )
    beast["development_xp"] = result["after_xp"]
    beast["level"] = result["after_level"]
    return result
