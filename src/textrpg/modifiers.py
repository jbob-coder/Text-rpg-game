from __future__ import annotations

from typing import Any, Dict, Mapping

from .schema import ATTRIBUTE_SPECS, DERIVED_STAT_SPECS, SKILL_CATALOG


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


def validate_modifier_path(path: Any) -> str:
    """Validate one canonical effective-value path and return it unchanged."""
    if not isinstance(path, str) or not path:
        raise ValueError(f"Modifier path must be a non-empty string: {path!r}")

    namespace, separator, key = path.partition(".")
    if not separator or not key or "." in key:
        raise ValueError(f"Invalid modifier path format: {path!r}")

    if namespace == "attributes":
        if key not in ATTRIBUTE_SPECS:
            raise ValueError(f"Unknown attribute modifier path: {path}")
    elif namespace == "skills":
        if key not in SKILL_CATALOG:
            raise ValueError(f"Unknown skill modifier path: {path}")
    elif namespace == "derived":
        if key not in DERIVED_STAT_SPECS:
            raise ValueError(f"Unknown derived modifier path: {path}")
    else:
        raise ValueError(f"Unsupported modifier namespace: {namespace!r}")

    return path


def validate_modifier_mapping(
    modifiers: Any,
    *,
    source: str = "modifier",
) -> Dict[str, float]:
    """Validate modifier keys and values without mutating authored input."""
    if modifiers is None:
        return {}
    if not isinstance(modifiers, Mapping):
        raise ValueError(f"{source}.modifiers must be an object")

    validated: Dict[str, float] = {}
    for path, value in modifiers.items():
        canonical = validate_modifier_path(path)
        validated[canonical] = _numeric(value, source=source, path=canonical)
    return validated


def validate_set_definitions(set_definitions: Any) -> None:
    """Validate every authored set threshold and modifier map."""
    if not isinstance(set_definitions, Mapping):
        raise ValueError("set_definitions must be an object")
    for set_id, definition in set_definitions.items():
        if not isinstance(definition, Mapping):
            raise ValueError(f"Set definition must be an object: {set_id}")
        thresholds = definition.get("thresholds", {})
        if not isinstance(thresholds, Mapping):
            raise ValueError(f"Set thresholds must be an object: {set_id}")
        for pieces_raw, bonus in thresholds.items():
            try:
                pieces = int(pieces_raw)
            except (TypeError, ValueError) as exc:
                raise ValueError(
                    f"Invalid set threshold for {set_id}: {pieces_raw!r}"
                ) from exc
            if pieces <= 0:
                raise ValueError(f"Set threshold must be positive for {set_id}: {pieces}")
            if not isinstance(bonus, Mapping):
                raise ValueError(f"Set bonus must be an object: {set_id}:{pieces}")
            validate_modifier_mapping(
                bonus.get("modifiers", {}),
                source=f"set:{set_id}:{pieces}",
            )


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
    validate_set_definitions(set_definitions)
    counts = set_counts(state)
    active: Dict[str, Dict[str, Any]] = {}
    for set_id, count in counts.items():
        definition = set_definitions.get(set_id, {})
        thresholds = definition.get("thresholds", {})
        if not isinstance(thresholds, Mapping):
            raise ValueError(f"Set thresholds must be an object: {set_id}")
        for pieces_raw, bonus in thresholds.items():
            try:
                pieces = int(pieces_raw)
            except (TypeError, ValueError) as exc:
                raise ValueError(f"Invalid set threshold for {set_id}: {pieces_raw!r}") from exc
            if pieces <= 0:
                raise ValueError(f"Set threshold must be positive for {set_id}: {pieces}")
            if not isinstance(bonus, Mapping):
                raise ValueError(f"Set bonus must be an object: {set_id}:{pieces}")
            validate_modifier_mapping(
                bonus.get("modifiers", {}),
                source=f"set:{set_id}:{pieces}",
            )
            if count >= pieces:
                active[f"{set_id}:{pieces}"] = dict(bonus)
    return active


def equipment_modifiers(
    state: Any,
    set_definitions: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, float]:
    total: Dict[str, float] = {}
    for slot, record in state.equipment.items():
        modifiers = validate_modifier_mapping(
            record.get("modifiers", {}),
            source=f"equipment:{slot}",
        )
        for path, value in modifiers.items():
            total[path] = total.get(path, 0.0) + value
    if set_definitions:
        for bonus_id, bonus in active_set_bonuses(state, set_definitions).items():
            modifiers = validate_modifier_mapping(
                bonus.get("modifiers", {}),
                source=f"set:{bonus_id}",
            )
            for path, value in modifiers.items():
                total[path] = total.get(path, 0.0) + value
    return total


def perk_modifiers(state: Any) -> Dict[str, float]:
    total: Dict[str, float] = {}
    for perk_id, perk in state.perks.items():
        modifiers = validate_modifier_mapping(
            perk.get("modifiers", {}),
            source=f"perk:{perk_id}",
        )
        for path, value in modifiers.items():
            total[path] = total.get(path, 0.0) + value
    return total


def condition_modifiers(state: Any) -> Dict[str, float]:
    total: Dict[str, float] = {}
    conditions = state.player.get("conditions", {})
    if not isinstance(conditions, Mapping):
        raise ValueError("player.conditions must be an object")
    for condition_id, condition in conditions.items():
        if not isinstance(condition, Mapping):
            raise ValueError(f"Condition must be an object: {condition_id}")
        modifiers = validate_modifier_mapping(
            condition.get("modifiers", {}),
            source=f"condition:{condition_id}",
        )
        for path, value in modifiers.items():
            total[path] = total.get(path, 0.0) + value
    return total


def modifier_totals(
    state: Any,
    set_definitions: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, float]:
    """Aggregate all additive effective-value modifiers exactly once.

    Canonical modifier paths use player-relative paths such as
    attributes.might and skills.ranged. Direct derived-stat modifiers use
    derived.<name>, for example derived.max_health.

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
    """Return an inspectable additive breakdown for one canonical path.

    For derived.* this function explains direct modifiers only; the formula
    contribution is calculated by derived_stats and is intentionally not
    represented as a fake player-base field.
    """
    validate_modifier_path(path)
    breakdown: Dict[str, float] = {}

    if path.startswith("derived."):
        breakdown["base"] = 0.0
    else:
        base = _get_path(state.player, path, 0)
        breakdown["base"] = _numeric(base, source="player", path=path)

    for slot, record in state.equipment.items():
        modifiers = validate_modifier_mapping(
            record.get("modifiers", {}),
            source=f"equipment:{slot}",
        )
        if path in modifiers:
            breakdown[f"equipment:{slot}"] = modifiers[path]

    if set_definitions:
        for bonus_id, bonus in active_set_bonuses(state, set_definitions).items():
            modifiers = validate_modifier_mapping(
                bonus.get("modifiers", {}),
                source=f"set:{bonus_id}",
            )
            if path in modifiers:
                breakdown[f"set:{bonus_id}"] = modifiers[path]

    for perk_id, perk in state.perks.items():
        modifiers = validate_modifier_mapping(
            perk.get("modifiers", {}),
            source=f"perk:{perk_id}",
        )
        if path in modifiers:
            breakdown[f"perk:{perk_id}"] = modifiers[path]

    conditions = state.player.get("conditions", {})
    if not isinstance(conditions, Mapping):
        raise ValueError("player.conditions must be an object")
    for condition_id, condition in conditions.items():
        if not isinstance(condition, Mapping):
            raise ValueError(f"Condition must be an object: {condition_id}")
        modifiers = validate_modifier_mapping(
            condition.get("modifiers", {}),
            source=f"condition:{condition_id}",
        )
        if path in modifiers:
            breakdown[f"condition:{condition_id}"] = modifiers[path]

    breakdown["total"] = sum(breakdown.values())
    return breakdown


def effective_player_value(
    state: Any,
    path: str,
    set_definitions: Mapping[str, Mapping[str, Any]] | None = None,
) -> float:
    """Return base player value plus equipment/set/perk/condition modifiers."""
    if path.startswith("derived."):
        # Local import keeps schema/modifier modules independent during import.
        from .stats import derived_stat_breakdown

        key = path.removeprefix("derived.")
        return float(derived_stat_breakdown(state, key, set_definitions)["total"])
    return modifier_breakdown(state, path, set_definitions)["total"]
