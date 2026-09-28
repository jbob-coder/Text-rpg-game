from __future__ import annotations

from copy import deepcopy
from math import isfinite
from typing import Any, Dict, List, Mapping

from .core import RuleError
from .medieval import validate_beast_runtime_state


def _finite_probability(value: Any) -> bool:
    return (
        not isinstance(value, bool)
        and isinstance(value, (int, float))
        and isfinite(float(value))
        and 0.0 <= float(value) <= 1.0
    )


def _stable_observation_id(value: Any) -> bool:
    if not isinstance(value, str) or not value.startswith("OBS_"):
        return False
    return all(char.isupper() or char.isdigit() or char == "_" for char in value)


def validate_encounter_memory(memory: Any) -> List[str]:
    if not isinstance(memory, Mapping):
        return ["encounter memory must be an object"]

    errors: List[str] = []
    for field_name in ("memory_id", "opponent_id"):
        value = memory.get(field_name)
        if not isinstance(value, str) or not value or not all(
            char.isupper() or char.isdigit() or char == "_" for char in value
        ):
            errors.append(f"memory.{field_name} must be a stable uppercase ID")

    encounter_count = memory.get("encounter_count", 0)
    if (
        isinstance(encounter_count, bool)
        or not isinstance(encounter_count, int)
        or encounter_count < 0
    ):
        errors.append("memory.encounter_count must be a non-negative integer")

    last_seen = memory.get("last_seen_time_minutes", 0)
    if isinstance(last_seen, bool) or not isinstance(last_seen, int) or last_seen < 0:
        errors.append("memory.last_seen_time_minutes must be a non-negative integer")

    observations = memory.get("observations", {})
    if not isinstance(observations, Mapping):
        errors.append("memory.observations must be an object")
        return errors

    for observation_id, record in observations.items():
        if not _stable_observation_id(observation_id):
            errors.append(f"memory observation ID is invalid: {observation_id!r}")
            continue
        if not isinstance(record, Mapping):
            errors.append(f"memory.observations.{observation_id} must be an object")
            continue
        count = record.get("count")
        confidence = record.get("confidence")
        if isinstance(count, bool) or not isinstance(count, int) or count < 1:
            errors.append(
                f"memory.observations.{observation_id}.count must be an integer >= 1"
            )
        if not _finite_probability(confidence):
            errors.append(
                f"memory.observations.{observation_id}.confidence must be finite numeric in range 0..1"
            )
    return errors


def record_encounter_observations(
    memory: Mapping[str, Any],
    observations: Mapping[str, Any],
    *,
    occurred_at_minutes: int,
) -> Dict[str, Any]:
    """Return an updated memory without mutating the caller's existing durable state."""
    errors = validate_encounter_memory(memory)
    if errors:
        raise RuleError("Invalid encounter memory:\n- " + "\n- ".join(errors))
    if not isinstance(observations, Mapping):
        raise RuleError("observations must be an object")
    if (
        isinstance(occurred_at_minutes, bool)
        or not isinstance(occurred_at_minutes, int)
        or occurred_at_minutes < 0
    ):
        raise RuleError("occurred_at_minutes must be a non-negative integer")
    if occurred_at_minutes < memory.get("last_seen_time_minutes", 0):
        raise RuleError("occurred_at_minutes cannot precede the previous encounter time")

    for observation_id, confidence in observations.items():
        if not _stable_observation_id(observation_id):
            raise RuleError(f"invalid observation ID: {observation_id!r}")
        if not _finite_probability(confidence):
            raise RuleError(
                f"observation confidence must be finite numeric in range 0..1: {observation_id}"
            )

    updated = deepcopy(dict(memory))
    existing_observations = updated.setdefault("observations", {})
    for observation_id, confidence in observations.items():
        existing = existing_observations.get(observation_id)
        if existing is None:
            existing_observations[observation_id] = {
                "count": 1,
                "confidence": round(float(confidence), 4),
            }
            continue

        count = int(existing["count"])
        old_confidence = float(existing["confidence"])
        next_count = count + 1
        averaged = ((old_confidence * count) + float(confidence)) / next_count
        existing_observations[observation_id] = {
            "count": next_count,
            "confidence": round(averaged, 4),
        }

    updated["encounter_count"] = int(updated.get("encounter_count", 0)) + 1
    updated["last_seen_time_minutes"] = occurred_at_minutes
    return updated


def adaptation_eligibility(
    beast_state: Mapping[str, Any],
    memory: Mapping[str, Any],
    adaptation_definition: Mapping[str, Any],
    *,
    current_time_minutes: int,
) -> Dict[str, Any]:
    """Check evidence-gated adaptation requirements without mutating beast state."""
    beast_errors = validate_beast_runtime_state(beast_state)
    memory_errors = validate_encounter_memory(memory)
    if beast_errors or memory_errors:
        errors = beast_errors + memory_errors
        raise RuleError("Invalid adaptation state:\n- " + "\n- ".join(errors))
    if not isinstance(adaptation_definition, Mapping):
        raise RuleError("adaptation definition must be an object")
    if (
        isinstance(current_time_minutes, bool)
        or not isinstance(current_time_minutes, int)
        or current_time_minutes < 0
    ):
        raise RuleError("current_time_minutes must be a non-negative integer")
    if current_time_minutes < memory.get("last_seen_time_minutes", 0):
        raise RuleError("current_time_minutes cannot precede the encounter memory")

    minimum_intelligence = adaptation_definition.get("min_intelligence_tier", 0)
    minimum_elapsed = adaptation_definition.get("min_elapsed_minutes", 0)
    required_observations = adaptation_definition.get("required_observations", {})

    if (
        isinstance(minimum_intelligence, bool)
        or not isinstance(minimum_intelligence, int)
        or not 0 <= minimum_intelligence <= 5
    ):
        raise RuleError("adaptation min_intelligence_tier must be an integer in range 0..5")
    if (
        isinstance(minimum_elapsed, bool)
        or not isinstance(minimum_elapsed, int)
        or minimum_elapsed < 0
    ):
        raise RuleError("adaptation min_elapsed_minutes must be a non-negative integer")
    if not isinstance(required_observations, Mapping):
        raise RuleError("adaptation required_observations must be an object")

    missing: List[str] = []
    if beast_state["intelligence_tier"] < minimum_intelligence:
        missing.append("intelligence")

    elapsed = current_time_minutes - memory.get("last_seen_time_minutes", 0)
    if elapsed < minimum_elapsed:
        missing.append("elapsed_time")

    known_observations = memory.get("observations", {})
    for observation_id, requirement in required_observations.items():
        if not _stable_observation_id(observation_id):
            raise RuleError(f"invalid required observation ID: {observation_id!r}")
        if not isinstance(requirement, Mapping):
            raise RuleError(f"required observation {observation_id} must be an object")

        minimum_count = requirement.get("min_count", 1)
        minimum_confidence = requirement.get("min_confidence", 0.0)
        if (
            isinstance(minimum_count, bool)
            or not isinstance(minimum_count, int)
            or minimum_count < 1
        ):
            raise RuleError(
                f"required observation {observation_id}.min_count must be an integer >= 1"
            )
        if not _finite_probability(minimum_confidence):
            raise RuleError(
                f"required observation {observation_id}.min_confidence must be finite numeric in range 0..1"
            )

        observed = known_observations.get(observation_id)
        if observed is None or observed["count"] < minimum_count:
            missing.append(f"observation_count:{observation_id}")
            continue
        if float(observed["confidence"]) < float(minimum_confidence):
            missing.append(f"observation_confidence:{observation_id}")

    return {
        "eligible": not missing,
        "missing": missing,
        "elapsed_minutes": elapsed,
    }
