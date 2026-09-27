from __future__ import annotations

import hashlib
from math import isfinite
from typing import Any, Dict, Mapping

from .beasts import validate_beast_state
from .core import RuleError


_SCORE_KEYS = (
    "level",
    "combat_power",
    "intelligence",
    "followers",
    "terrain_affinity",
    "morale",
    "resource_score",
    "injury_penalty",
    "exhaustion_penalty",
)


def _string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise RuleError(f"{label} must be a non-empty string")
    return value


def _finite(value: Any, label: str, *, minimum: float | None = None, maximum: float | None = None) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not isfinite(float(value)):
        raise RuleError(f"{label} must be a finite number")
    number = float(value)
    if minimum is not None and number < minimum:
        raise RuleError(f"{label} must be >= {minimum}")
    if maximum is not None and number > maximum:
        raise RuleError(f"{label} must be <= {maximum}")
    return number


def validate_region_state(region: Mapping[str, Any]) -> None:
    if not isinstance(region, Mapping):
        raise RuleError("region state must be an object")
    region_id = _string(region.get("region_id"), "region.region_id")
    beast_ids = region.get("beast_ids", [])
    if not isinstance(beast_ids, list) or not all(isinstance(item, str) and item for item in beast_ids):
        raise RuleError(f"{region_id}.beast_ids must be a list of non-empty strings")
    if len(set(beast_ids)) != len(beast_ids):
        raise RuleError(f"{region_id}.beast_ids must not contain duplicates")
    capacity = region.get("carrying_capacity", 0)
    if isinstance(capacity, bool) or not isinstance(capacity, int) or capacity < 0:
        raise RuleError(f"{region_id}.carrying_capacity must be a non-negative integer")
    _finite(region.get("resource_score", 0.0), f"{region_id}.resource_score", minimum=0.0, maximum=1.0)
    controller = region.get("territory_controller")
    if controller is not None:
        _string(controller, f"{region_id}.territory_controller")
    last = region.get("last_simulated_minutes", 0)
    if isinstance(last, bool) or not isinstance(last, int) or last < 0:
        raise RuleError(f"{region_id}.last_simulated_minutes must be a non-negative integer")


def validate_conflict_profile(profile: Mapping[str, Any], beast_id: str) -> None:
    if not isinstance(profile, Mapping):
        raise RuleError(f"Conflict profile must be an object: {beast_id}")
    _finite(profile.get("combat_power", 0.0), f"{beast_id}.combat_power", minimum=0.0)
    for key in ("terrain_affinity", "morale", "resource_score", "injury_burden", "exhaustion"):
        _finite(profile.get(key, 0.0), f"{beast_id}.{key}", minimum=0.0, maximum=1.0)


def validate_ecology_rules(rules: Mapping[str, Any]) -> None:
    if not isinstance(rules, Mapping):
        raise RuleError("ecology rules must be an object")
    weights = rules.get("weights")
    if not isinstance(weights, Mapping):
        raise RuleError("ecology rules.weights must be an object")
    unknown = set(weights).difference(_SCORE_KEYS)
    missing = set(_SCORE_KEYS).difference(weights)
    if unknown or missing:
        raise RuleError(f"ecology rules.weights mismatch; missing={sorted(missing)} unknown={sorted(unknown)}")
    for key in _SCORE_KEYS:
        _finite(weights[key], f"ecology weight {key}", minimum=0.0)
    _finite(rules.get("deterministic_variance", 0.0), "deterministic_variance", minimum=0.0)


def region_simulation_steps(region: Mapping[str, Any], *, now_minutes: int, cadence_minutes: int) -> int:
    validate_region_state(region)
    if isinstance(now_minutes, bool) or not isinstance(now_minutes, int) or now_minutes < 0:
        raise RuleError("now_minutes must be a non-negative integer")
    if isinstance(cadence_minutes, bool) or not isinstance(cadence_minutes, int) or cadence_minutes < 1:
        raise RuleError("cadence_minutes must be an integer >= 1")
    last = int(region.get("last_simulated_minutes", 0))
    if now_minutes < last:
        raise RuleError("now_minutes cannot be earlier than last_simulated_minutes")
    return (now_minutes - last) // cadence_minutes


def carrying_pressure(region: Mapping[str, Any]) -> float:
    validate_region_state(region)
    capacity = int(region.get("carrying_capacity", 0))
    population = len(region.get("beast_ids", []))
    if capacity == 0:
        return 1.0 if population else 0.0
    return round(population / capacity, 4)


def _deterministic_variance(seed: str, region_id: str, time_minutes: int, beast_id: str, span: float) -> float:
    seed = _string(seed, "seed")
    payload = f"{seed}|{region_id}|{time_minutes}|{beast_id}".encode("utf-8")
    digest = hashlib.sha256(payload).digest()
    unit = int.from_bytes(digest[:8], "big") / float((1 << 64) - 1)
    return (unit * 2.0 - 1.0) * span


def conflict_score(
    beast: Mapping[str, Any],
    profile: Mapping[str, Any],
    region: Mapping[str, Any],
    rules: Mapping[str, Any],
) -> Dict[str, Any]:
    validate_beast_state(beast)
    validate_region_state(region)
    validate_conflict_profile(profile, beast["beast_id"])
    validate_ecology_rules(rules)
    weights = rules["weights"]

    inputs = {
        "level": float(beast.get("level", 1)),
        "combat_power": float(profile.get("combat_power", 0.0)),
        "intelligence": float(beast.get("intelligence", 0)),
        "followers": float(len(beast.get("followers", []))),
        "terrain_affinity": float(profile.get("terrain_affinity", 0.0)),
        "morale": float(profile.get("morale", 0.0)),
        "resource_score": float(profile.get("resource_score", 0.0)),
        "injury_penalty": float(profile.get("injury_burden", 0.0)),
        "exhaustion_penalty": float(profile.get("exhaustion", 0.0)),
    }
    positive = ("level", "combat_power", "intelligence", "followers", "terrain_affinity", "morale", "resource_score")
    penalties = ("injury_penalty", "exhaustion_penalty")
    contributions = {key: inputs[key] * float(weights[key]) for key in inputs}
    total = sum(contributions[key] for key in positive) - sum(contributions[key] for key in penalties)
    return {
        "beast_id": beast["beast_id"],
        "base_score": round(total, 4),
        "inputs": inputs,
        "contributions": {key: round(value, 4) for key, value in contributions.items()},
    }


def resolve_beast_conflict(
    *,
    seed: str,
    time_minutes: int,
    region: Mapping[str, Any],
    beast_a: Mapping[str, Any],
    profile_a: Mapping[str, Any],
    beast_b: Mapping[str, Any],
    profile_b: Mapping[str, Any],
    rules: Mapping[str, Any],
) -> Dict[str, Any]:
    """Resolve one coarse off-screen conflict deterministically and non-mutatingly."""
    if isinstance(time_minutes, bool) or not isinstance(time_minutes, int) or time_minutes < 0:
        raise RuleError("time_minutes must be a non-negative integer")
    validate_region_state(region)
    if beast_a.get("beast_id") == beast_b.get("beast_id"):
        raise RuleError("A beast cannot resolve a conflict against itself")

    a = conflict_score(beast_a, profile_a, region, rules)
    b = conflict_score(beast_b, profile_b, region, rules)
    span = float(rules.get("deterministic_variance", 0.0))
    a_variance = _deterministic_variance(seed, region["region_id"], time_minutes, a["beast_id"], span)
    b_variance = _deterministic_variance(seed, region["region_id"], time_minutes, b["beast_id"], span)
    a_final = round(a["base_score"] + a_variance, 4)
    b_final = round(b["base_score"] + b_variance, 4)

    if a_final == b_final:
        winner_id, loser_id = sorted((a["beast_id"], b["beast_id"]))
    elif a_final > b_final:
        winner_id, loser_id = a["beast_id"], b["beast_id"]
    else:
        winner_id, loser_id = b["beast_id"], a["beast_id"]

    return {
        "region_id": region["region_id"],
        "time_minutes": time_minutes,
        "winner_id": winner_id,
        "loser_id": loser_id,
        "margin": round(abs(a_final - b_final), 4),
        "scores": {
            a["beast_id"]: {**a, "variance": round(a_variance, 4), "final_score": a_final},
            b["beast_id"]: {**b, "variance": round(b_variance, 4), "final_score": b_final},
        },
    }
