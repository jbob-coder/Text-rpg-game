from __future__ import annotations

from math import isfinite
from typing import Any, Dict, Iterable

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

    ability = state.abilities.setdefault(
        ability_id,
        {"rank": 0, "mastery_xp": 0.0, "mastery_stage": "discovered", "techniques": {}},
    )
    before = dict(ability)
    ability["mastery_xp"] = float(ability.get("mastery_xp", 0.0)) + float(xp)
    ability["mastery_stage"] = mastery_stage(ability["mastery_xp"])

    rank = 0
    for index, threshold in enumerate(rank_thresholds):
        if ability["mastery_xp"] >= threshold:
            rank = index
    derived_rank = min(rank, max_rank)
    rank_floor = int(ability.get("rank_floor", 0))
    ability["rank"] = max(derived_rank, rank_floor)

    return {"before": before, "after": dict(ability)}


def technique_available(state: GameState, ability_id: str, requirements: Dict[str, Any]) -> bool:
    ability = state.abilities.get(ability_id)
    if not ability:
        return False
    if ability.get("rank", 0) < requirements.get("rank_min", 0):
        return False
    if ability.get("mastery_xp", 0) < requirements.get("mastery_xp_min", 0):
        return False
    for knowledge_id in requirements.get("knowledge", []):
        if knowledge_id not in state.knowledge:
            return False
    for perk_id in requirements.get("perks", []):
        if perk_id not in state.perks:
            return False
    return True
