from __future__ import annotations

from math import isfinite
from typing import Any, Dict, Iterable, Mapping, MutableMapping

from .core import GameState, RuleError


MASTERY_STAGES = (
    (0, "discovered"),
    (20, "unstable"),
    (60, "learned"),
    (150, "practiced"),
    (350, "mastered"),
)


def mastery_stage(xp: float, stages: Iterable[tuple[float, str]] = MASTERY_STAGES) -> str:
    if isinstance(xp, bool) or not isinstance(xp, (int, float)) or not isfinite(float(xp)):
        raise RuleError("Ability mastery XP must be a finite number")
    if xp < 0:
        raise RuleError("Ability mastery XP cannot be negative")
    stage = "unknown"
    for threshold, name in stages:
        if xp >= threshold:
            stage = name
        else:
            break
    return stage


def gain_ability_mastery(
    state: GameState,
    ability_id: str,
    xp: float,
    *,
    rank_thresholds: tuple[float, ...] = (0, 100, 300, 700, 1500),
    max_rank: int = 4,
) -> Dict[str, Any]:
    """Advance an ability through use/training without instant unlock buttons.

    Rank is derived from accumulated mastery XP. Story prerequisites for techniques
    should remain authored conditions rather than being silently granted here.
    """
    if not isinstance(ability_id, str) or not ability_id:
        raise RuleError("Ability ID must be a non-empty string")
    if not isinstance(state.abilities, MutableMapping):
        raise RuleError("state.abilities must be mutable")
    if isinstance(xp, bool) or not isinstance(xp, (int, float)) or not isfinite(float(xp)):
        raise RuleError("Ability mastery gain must be a finite number")
    if xp < 0:
        raise RuleError("Ability mastery gain cannot be negative")
    if isinstance(max_rank, bool) or not isinstance(max_rank, int) or max_rank < 0:
        raise RuleError("Ability max_rank must be a non-negative integer")
    if not rank_thresholds:
        raise RuleError("Ability rank_thresholds cannot be empty")
    previous_threshold = -1.0
    for threshold in rank_thresholds:
        if (
            isinstance(threshold, bool)
            or not isinstance(threshold, (int, float))
            or not isfinite(float(threshold))
            or float(threshold) < 0
        ):
            raise RuleError("Ability rank thresholds must be finite non-negative numbers")
        if float(threshold) < previous_threshold:
            raise RuleError("Ability rank thresholds must be sorted ascending")
        previous_threshold = float(threshold)

    existing = state.abilities.get(ability_id)
    if existing is None:
        existing = {
            "rank": 0,
            "mastery_xp": 0.0,
            "mastery_stage": "discovered",
            "techniques": {},
        }
    if not isinstance(existing, MutableMapping):
        raise RuleError(f"Ability state must be mutable: {ability_id}")

    current_rank = existing.get("rank", 0)
    if (
        isinstance(current_rank, bool)
        or not isinstance(current_rank, int)
        or current_rank < 0
    ):
        raise RuleError(f"Ability rank state is invalid: {ability_id}")

    current_mastery = existing.get("mastery_xp", 0.0)
    if (
        isinstance(current_mastery, bool)
        or not isinstance(current_mastery, (int, float))
        or not isfinite(float(current_mastery))
        or float(current_mastery) < 0
    ):
        raise RuleError(f"Ability mastery state is invalid: {ability_id}")

    rank_floor_raw = existing.get("rank_floor", 0)
    if (
        isinstance(rank_floor_raw, bool)
        or not isinstance(rank_floor_raw, int)
        or rank_floor_raw < 0
    ):
        raise RuleError(f"Ability rank_floor state is invalid: {ability_id}")

    next_mastery = float(current_mastery) + float(xp)
    next_stage = mastery_stage(next_mastery)

    rank = 0
    for index, threshold in enumerate(rank_thresholds):
        if next_mastery >= threshold:
            rank = index
    derived_rank = min(rank, max_rank)
    next_rank = max(derived_rank, rank_floor_raw)

    before = dict(existing)
    ability = state.abilities.setdefault(ability_id, existing)
    ability["mastery_xp"] = next_mastery
    ability["mastery_stage"] = next_stage
    ability["rank"] = next_rank

    return {"before": before, "after": dict(ability)}


def technique_available(
    state: GameState,
    ability_id: str,
    requirements: Mapping[str, Any],
) -> bool:
    """Evaluate basic technique requirements without mutating state."""
    if not isinstance(ability_id, str) or not ability_id:
        raise RuleError("Ability ID must be a non-empty string")
    if not isinstance(requirements, Mapping):
        raise RuleError("Technique requirements must be an object")
    if not isinstance(state.abilities, Mapping):
        raise RuleError("state.abilities must be an object")
    if not isinstance(state.knowledge, Mapping):
        raise RuleError("state.knowledge must be an object")
    if not isinstance(state.perks, Mapping):
        raise RuleError("state.perks must be an object")

    ability = state.abilities.get(ability_id)
    if ability is None:
        return False
    if not isinstance(ability, Mapping):
        raise RuleError(f"Ability state must be an object: {ability_id}")

    rank = ability.get("rank", 0)
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 0:
        raise RuleError(f"Ability rank state is invalid: {ability_id}")
    mastery = ability.get("mastery_xp", 0.0)
    if (
        isinstance(mastery, bool)
        or not isinstance(mastery, (int, float))
        or not isfinite(float(mastery))
        or float(mastery) < 0
    ):
        raise RuleError(f"Ability mastery state is invalid: {ability_id}")

    rank_min = requirements.get("rank_min", 0)
    if isinstance(rank_min, bool) or not isinstance(rank_min, int) or rank_min < 0:
        raise RuleError("Technique rank_min must be a non-negative integer")
    mastery_min = requirements.get("mastery_xp_min", 0)
    if (
        isinstance(mastery_min, bool)
        or not isinstance(mastery_min, (int, float))
        or not isfinite(float(mastery_min))
        or float(mastery_min) < 0
    ):
        raise RuleError("Technique mastery_xp_min must be finite non-negative numeric")

    knowledge = requirements.get("knowledge", [])
    perks = requirements.get("perks", [])
    if not isinstance(knowledge, list) or not all(
        isinstance(value, str) and value for value in knowledge
    ):
        raise RuleError("Technique knowledge requirements must be a list of non-empty IDs")
    if not isinstance(perks, list) or not all(
        isinstance(value, str) and value for value in perks
    ):
        raise RuleError("Technique perk requirements must be a list of non-empty IDs")

    if rank < rank_min:
        return False
    if float(mastery) < float(mastery_min):
        return False
    for knowledge_id in knowledge:
        if knowledge_id not in state.knowledge:
            return False
    for perk_id in perks:
        if perk_id not in state.perks:
            return False
    return True
