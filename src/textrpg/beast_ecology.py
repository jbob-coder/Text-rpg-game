from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
from math import isfinite
from typing import Any, Dict, List, Mapping

from .core import RuleError
from .medieval import validate_beast_runtime_state


COMMAND_ROLES = {"chieftain", "commander", "territory_ruler", "regional_apex"}


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
    number = float(value)
    if not isfinite(number):
        return False
    if minimum is not None and number < minimum:
        return False
    if maximum is not None and number > maximum:
        return False
    return True


def validate_ecology_profile(profile: Any) -> List[str]:
    if not isinstance(profile, Mapping):
        return ["ecology combat profile must be an object"]
    errors: List[str] = []
    for field_name in ("offense", "defense", "mobility", "tactics", "morale"):
        if not _finite(profile.get(field_name), minimum=0.0, maximum=100.0):
            errors.append(f"ecology_profile.{field_name} must be finite numeric in range 0..100")
    if not _finite(profile.get("injury_penalty", 0.0), minimum=0.0, maximum=100.0):
        errors.append("ecology_profile.injury_penalty must be finite numeric in range 0..100")
    return errors


def validate_territory_state(territory: Any) -> List[str]:
    if not isinstance(territory, Mapping):
        return ["territory state must be an object"]
    errors: List[str] = []
    if not _stable_id(territory.get("territory_id")):
        errors.append("territory.territory_id must be a stable uppercase ID")
    controller = territory.get("controller_beast_id")
    if controller is not None and not _stable_id(controller):
        errors.append("territory.controller_beast_id must be null or a stable uppercase ID")
    if not _finite(territory.get("defense_bonus", 0.0), minimum=0.0, maximum=100.0):
        errors.append("territory.defense_bonus must be finite numeric in range 0..100")
    if not _finite(territory.get("resource_value", 0.0), minimum=0.0, maximum=100.0):
        errors.append("territory.resource_value must be finite numeric in range 0..100")
    return errors


def ecology_combat_score(
    beast_state: Mapping[str, Any],
    profile: Mapping[str, Any],
    *,
    territory_defense_bonus: float = 0.0,
) -> Dict[str, float]:
    beast_errors = validate_beast_runtime_state(beast_state)
    profile_errors = validate_ecology_profile(profile)
    if beast_errors or profile_errors:
        raise RuleError(
            "Invalid ecology combatant:\n- " + "\n- ".join(beast_errors + profile_errors)
        )
    if not _finite(territory_defense_bonus, minimum=0.0, maximum=100.0):
        raise RuleError("territory_defense_bonus must be finite numeric in range 0..100")

    intelligence = int(beast_state["intelligence_tier"])
    followers = int(beast_state.get("follower_count", 0))
    role = beast_state["role"]

    physical = (
        float(profile["offense"]) * 0.30
        + float(profile["defense"]) * 0.25
        + float(profile["mobility"]) * 0.15
        + float(profile["morale"]) * 0.10
    )
    tactics = float(profile["tactics"]) * (0.10 + intelligence * 0.02)
    experience = float(beast_state["level"]) * 0.40
    command = 0.0
    if role in COMMAND_ROLES and followers > 0:
        command = min(30.0, followers * (0.35 + intelligence * 0.13))

    injury_penalty = float(profile.get("injury_penalty", 0.0)) * 0.40
    territory = float(territory_defense_bonus) * 0.25
    total = max(0.0, physical + tactics + experience + command + territory - injury_penalty)
    return {
        "physical": round(physical, 4),
        "tactics": round(tactics, 4),
        "experience": round(experience, 4),
        "command": round(command, 4),
        "territory": round(territory, 4),
        "injury_penalty": round(injury_penalty, 4),
        "total": round(total, 4),
    }


def resolve_beast_conflict(
    attacker: Mapping[str, Any],
    defender: Mapping[str, Any],
    attacker_profile: Mapping[str, Any],
    defender_profile: Mapping[str, Any],
    territory: Mapping[str, Any],
    *,
    event_id: str,
    seed: str,
    variance: float = 10.0,
    claim_margin: float = 10.0,
) -> Dict[str, Any]:
    """Resolve a coarse off-screen conflict without simulating turn-by-turn combat."""
    territory_errors = validate_territory_state(territory)
    if territory_errors:
        raise RuleError("Invalid territory state:\n- " + "\n- ".join(territory_errors))
    if not _stable_id(event_id):
        raise RuleError("ecology event_id must be a stable uppercase ID")
    if not isinstance(seed, str) or not seed:
        raise RuleError("ecology seed must be a non-empty string")
    if not _finite(variance, minimum=0.0):
        raise RuleError("ecology variance must be finite non-negative numeric")
    if not _finite(claim_margin, minimum=0.0):
        raise RuleError("ecology claim_margin must be finite non-negative numeric")
    if attacker.get("beast_id") == defender.get("beast_id"):
        raise RuleError("a beast cannot resolve an ecology conflict against itself")

    defender_bonus = (
        float(territory.get("defense_bonus", 0.0))
        if territory.get("controller_beast_id") == defender.get("beast_id")
        else 0.0
    )
    attacker_score = ecology_combat_score(attacker, attacker_profile)
    defender_score = ecology_combat_score(
        defender,
        defender_profile,
        territory_defense_bonus=defender_bonus,
    )

    digest = sha256(
        f"{seed}|{event_id}|{attacker['beast_id']}|{defender['beast_id']}|{territory['territory_id']}".encode(
            "utf-8"
        )
    ).digest()
    normalized = int.from_bytes(digest[:8], "big") / float(2**64 - 1)
    swing = (normalized * 2.0 - 1.0) * float(variance)
    margin = round(attacker_score["total"] - defender_score["total"] + swing, 4)

    attacker_won = margin > 0
    winner_id = attacker["beast_id"] if attacker_won else defender["beast_id"]
    loser_id = defender["beast_id"] if attacker_won else attacker["beast_id"]
    severity = round(min(100.0, 10.0 + abs(margin) * 1.5), 2)

    updated_territory = deepcopy(dict(territory))
    territory_changed = False
    if attacker_won and margin >= float(claim_margin):
        if updated_territory.get("controller_beast_id") != attacker["beast_id"]:
            updated_territory["controller_beast_id"] = attacker["beast_id"]
            territory_changed = True

    return {
        "event_id": event_id,
        "winner_beast_id": winner_id,
        "loser_beast_id": loser_id,
        "margin": margin,
        "injury_severity": severity,
        "territory_changed": territory_changed,
        "territory": updated_territory,
        "attacker_score": attacker_score,
        "defender_score": defender_score,
        "random_swing": round(swing, 4),
    }
