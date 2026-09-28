from __future__ import annotations

from copy import deepcopy
from math import isfinite
from typing import Any, Dict, List, Mapping

from .core import RuleError
from .medieval import validate_beast_runtime_state


DEVELOPMENT_EVENT_TYPES = (
    "survival",
    "hunt",
    "rival_victory",
    "territory_defense",
    "territory_expansion",
    "training",
    "resource_gain",
    "maturation",
    "evolution",
)


def _stable_id(value: Any) -> bool:
    return (
        isinstance(value, str)
        and bool(value)
        and value[0].isalpha()
        and all(char.isupper() or char.isdigit() or char == "_" for char in value)
    )


def _finite(value: Any, *, minimum: float | None = None, maximum: float | None = None) -> bool:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    numeric = float(value)
    if not isfinite(numeric):
        return False
    if minimum is not None and numeric < minimum:
        return False
    if maximum is not None and numeric > maximum:
        return False
    return True


def validate_progression_definition(definition: Any) -> List[str]:
    if not isinstance(definition, Mapping):
        return ["beast progression definition must be an object"]
    errors: List[str] = []
    if not _finite(definition.get("base_level_xp"), minimum=0.000001):
        errors.append("progression.base_level_xp must be finite numeric > 0")
    if not _finite(definition.get("growth_factor"), minimum=1.0):
        errors.append("progression.growth_factor must be finite numeric >= 1")
    if not _finite(definition.get("repeat_decay"), minimum=0.0, maximum=1.0):
        errors.append("progression.repeat_decay must be finite numeric in range 0..1")
    if not _finite(definition.get("min_repeat_factor"), minimum=0.0, maximum=1.0):
        errors.append("progression.min_repeat_factor must be finite numeric in range 0..1")
    if not _finite(definition.get("max_xp_per_event"), minimum=0.000001):
        errors.append("progression.max_xp_per_event must be finite numeric > 0")
    max_level = definition.get("max_level")
    if isinstance(max_level, bool) or not isinstance(max_level, int) or max_level < 1:
        errors.append("progression.max_level must be an integer >= 1")
    return errors


def total_xp_required_for_level(level: int, definition: Mapping[str, Any]) -> float:
    errors = validate_progression_definition(definition)
    if errors:
        raise RuleError("Invalid beast progression definition:\n- " + "\n- ".join(errors))
    if isinstance(level, bool) or not isinstance(level, int) or level < 1:
        raise RuleError("level must be an integer >= 1")
    if level <= 1:
        return 0.0

    base = float(definition["base_level_xp"])
    growth = float(definition["growth_factor"])
    total = 0.0
    for current_level in range(1, level):
        total += base * (growth ** (current_level - 1))
    return round(total, 4)


def level_for_total_xp(total_xp: float, definition: Mapping[str, Any]) -> int:
    errors = validate_progression_definition(definition)
    if errors:
        raise RuleError("Invalid beast progression definition:\n- " + "\n- ".join(errors))
    if not _finite(total_xp, minimum=0.0):
        raise RuleError("total_xp must be finite non-negative numeric")

    max_level = int(definition["max_level"])
    level = 1
    while level < max_level:
        next_level = level + 1
        if float(total_xp) < total_xp_required_for_level(next_level, definition):
            break
        level = next_level
    return level


def award_beast_development(
    beast_state: Mapping[str, Any],
    event: Mapping[str, Any],
    progression_definition: Mapping[str, Any],
) -> Dict[str, Any]:
    """Apply one meaningful development event with deterministic repeat decay."""
    beast_errors = validate_beast_runtime_state(beast_state)
    definition_errors = validate_progression_definition(progression_definition)
    if beast_errors or definition_errors:
        raise RuleError(
            "Invalid beast development contract:\n- "
            + "\n- ".join(beast_errors + definition_errors)
        )
    if not isinstance(event, Mapping):
        raise RuleError("development event must be an object")

    event_id = event.get("event_id")
    repeat_key = event.get("repeat_key")
    event_type = event.get("type")
    meaningful = event.get("meaningful")
    base_xp = event.get("base_xp")
    significance = event.get("significance", 1.0)

    if not _stable_id(event_id):
        raise RuleError("development event_id must be a stable uppercase ID")
    if not _stable_id(repeat_key):
        raise RuleError("development repeat_key must be a stable uppercase ID")
    if event_type not in DEVELOPMENT_EVENT_TYPES:
        raise RuleError(f"unsupported beast development event type: {event_type!r}")
    if not isinstance(meaningful, bool):
        raise RuleError("development event meaningful must be boolean")
    if not _finite(base_xp, minimum=0.0):
        raise RuleError("development base_xp must be finite non-negative numeric")
    if not _finite(significance, minimum=0.0, maximum=1.0):
        raise RuleError("development significance must be finite numeric in range 0..1")

    updated = deepcopy(dict(beast_state))
    history = dict(updated.get("development_history", {}))
    prior_count = history.get(repeat_key, 0)
    if isinstance(prior_count, bool) or not isinstance(prior_count, int) or prior_count < 0:
        raise RuleError(f"development history count is invalid: {repeat_key}")

    repeat_factor = max(
        float(progression_definition["min_repeat_factor"]),
        float(progression_definition["repeat_decay"]) ** prior_count,
    )
    if meaningful:
        awarded = min(
            float(progression_definition["max_xp_per_event"]),
            float(base_xp) * float(significance) * repeat_factor,
        )
    else:
        awarded = 0.0

    old_xp = float(updated["development_xp"])
    old_level = int(updated["level"])
    new_xp = round(old_xp + awarded, 4)
    computed_level = level_for_total_xp(new_xp, progression_definition)
    new_level = min(
        int(progression_definition["max_level"]),
        max(old_level, computed_level),
    )

    updated["development_xp"] = new_xp
    updated["level"] = new_level
    if meaningful:
        history[repeat_key] = prior_count + 1
    updated["development_history"] = history

    log = list(updated.get("development_log", []))
    log.append(
        {
            "event_id": event_id,
            "type": event_type,
            "meaningful": meaningful,
            "base_xp": float(base_xp),
            "significance": float(significance),
            "repeat_factor": round(repeat_factor, 4),
            "awarded_xp": round(awarded, 4),
            "level_before": old_level,
            "level_after": new_level,
        }
    )
    updated["development_log"] = log
    return updated
