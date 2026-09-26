from __future__ import annotations

from typing import Any, Dict, Mapping


def _get_path(data: Mapping[str, Any], path: str, default: Any = None) -> Any:
    current: Any = data
    for part in path.split("."):
        if not isinstance(current, Mapping) or part not in current:
            return default
        current = current[part]
    return current


def _numeric(value: Any, *, source: str, path: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"Non-numeric modifier/value at {source}:{path}")
    return float(value)


def set_counts(state: Any) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for record in state.equipment.values():
        set_id = record.get("set_id")
        if set_id:
            counts[set_id] = counts.get(set_id, 0) + 1
    return counts


def active_set_bonuses(
    state: Any,
    set_definitions: Mapping[str, Mapping[str, Any]],
) -> Dict[str, Dict[str, Any]]:
    counts = set_counts(state)
    active: Dict[str, Dict[str, Any]] = {}
    for set_id, count in counts.items():
        definition = set_definitions.get(set_id, {})
        thresholds = definition.get("thresholds", {})
        for pieces_raw, bonus in thresholds.items():
            pieces = int(pieces_raw)
            if count >= pieces:
                active[f"{set_id}:{pieces}"] = dict(bonus)
    return active


def equipment_modifiers(
    state: Any,
    set_definitions: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, float]:
    total: Dict[str, float] = {}
    for slot, record in state.equipment.items():
        for path, value in record.get("modifiers", {}).items():
            total[path] = total.get(path, 0.0) + _numeric(
                value,
                source=f"equipment:{slot}",
                path=path,
            )
    if set_definitions:
        for bonus_id, bonus in active_set_bonuses(state, set_definitions).items():
            for path, value in bonus.get("modifiers", {}).items():
                total[path] = total.get(path, 0.0) + _numeric(
                    value,
                    source=f"set:{bonus_id}",
                    path=path,
                )
    return total


def perk_modifiers(state: Any) -> Dict[str, float]:
    total: Dict[str, float] = {}
    for perk_id, perk in state.perks.items():
        for path, value in perk.get("modifiers", {}).items():
            total[path] = total.get(path, 0.0) + _numeric(
                value,
                source=f"perk:{perk_id}",
                path=path,
            )
    return total


def condition_modifiers(state: Any) -> Dict[str, float]:
    total: Dict[str, float] = {}
    conditions = state.player.get("conditions", {})
    if not isinstance(conditions, Mapping):
        raise ValueError("player.conditions must be an object")
    for condition_id, condition in conditions.items():
        if not isinstance(condition, Mapping):
            raise ValueError(f"Condition must be an object: {condition_id}")
        for path, value in condition.get("modifiers", {}).items():
            total[path] = total.get(path, 0.0) + _numeric(
                value,
                source=f"condition:{condition_id}",
                path=path,
            )
    return total


def modifier_totals(
    state: Any,
    set_definitions: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, float]:
    """Aggregate all additive effective-value modifiers exactly once.

    Canonical modifier paths use player-relative paths such as
    ``attributes.might`` and ``skills.ranged``. Direct derived-stat modifiers use
    ``derived.<name>`` (for example ``derived.max_health``).

    Condition severity is metadata; authored modifier magnitudes are already the
    final values and are not multiplied by severity automatically.
    """
    total: Dict[str, float] = {}
    sources = (
        equipment_modifiers(state, set_definitions),
        perk_modifiers(state),
        condition_modifiers(state),
    )
    for source in sources:
        for path, value in source.items():
            total[path] = total.get(path, 0.0) + value
    return total


def modifier_breakdown(
    state: Any,
    path: str,
    set_definitions: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, float]:
    """Return an inspectable additive breakdown for one player-relative path."""
    breakdown: Dict[str, float] = {}

    base = _get_path(state.player, path, 0)
    breakdown["base"] = _numeric(base, source="player", path=path)

    for slot, record in state.equipment.items():
        if path in record.get("modifiers", {}):
            breakdown[f"equipment:{slot}"] = _numeric(
                record["modifiers"][path],
                source=f"equipment:{slot}",
                path=path,
            )

    if set_definitions:
        for bonus_id, bonus in active_set_bonuses(state, set_definitions).items():
            if path in bonus.get("modifiers", {}):
                breakdown[f"set:{bonus_id}"] = _numeric(
                    bonus["modifiers"][path],
                    source=f"set:{bonus_id}",
                    path=path,
                )

    for perk_id, perk in state.perks.items():
        if path in perk.get("modifiers", {}):
            breakdown[f"perk:{perk_id}"] = _numeric(
                perk["modifiers"][path],
                source=f"perk:{perk_id}",
                path=path,
            )

    conditions = state.player.get("conditions", {})
    if not isinstance(conditions, Mapping):
        raise ValueError("player.conditions must be an object")
    for condition_id, condition in conditions.items():
        if not isinstance(condition, Mapping):
            raise ValueError(f"Condition must be an object: {condition_id}")
        if path in condition.get("modifiers", {}):
            breakdown[f"condition:{condition_id}"] = _numeric(
                condition["modifiers"][path],
                source=f"condition:{condition_id}",
                path=path,
            )

    breakdown["total"] = sum(breakdown.values())
    return breakdown


def effective_player_value(
    state: Any,
    path: str,
    set_definitions: Mapping[str, Mapping[str, Any]] | None = None,
) -> float:
    """Return base player value plus equipment/set/perk/condition modifiers."""
    return modifier_breakdown(state, path, set_definitions)["total"]
