from __future__ import annotations

from typing import Any, Dict, Mapping

from .core import GameState, RuleError
from .modifiers import effective_player_value, modifier_breakdown, resolve_set_context
from .schema import (
    ATTRIBUTE_SPECS,
    DERIVED_FORMULAS,
    DERIVED_STAT_SPECS,
    RESOURCE_KEYS,
    SKILL_CATALOG,
)


def _effective(
    state: GameState,
    path: str,
    set_definitions: Mapping[str, Mapping[str, Any]] | None,
) -> float:
    try:
        return effective_player_value(state, path, set_definitions)
    except ValueError as exc:
        raise RuleError(f"Invalid effective player value for {path}: {exc}") from exc


def validate_player_stats(state: GameState) -> list[str]:
    errors: list[str] = []
    attrs = state.player.get("attributes", {})
    skills = state.player.get("skills", {})
    if not isinstance(attrs, dict):
        return ["player.attributes must be an object"]
    if not isinstance(skills, dict):
        errors.append("player.skills must be an object")
        skills = {}
    for key, value in attrs.items():
        if key not in ATTRIBUTE_SPECS:
            errors.append(f"unknown attribute: {key}")
            continue
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            errors.append(f"attribute {key} must be numeric")
            continue
        spec = ATTRIBUTE_SPECS[key]
        if value < spec["min"] or value > spec["max"]:
            errors.append(f"attribute {key} out of range {spec['min']}..{spec['max']}: {value}")
    for key, value in skills.items():
        if key not in SKILL_CATALOG:
            errors.append(f"unknown skill: {key}")
        if isinstance(value, bool) or not isinstance(value, (int, float)) or value < 0 or value > 100:
            errors.append(f"skill {key} must be numeric in range 0..100")
    return errors


def _bounded_derived(name: str, value: float) -> float:
    spec = DERIVED_STAT_SPECS[name]
    minimum = spec.get("min")
    if minimum is not None:
        value = max(float(minimum), value)
    return round(value, 2)


def derived_stat_breakdown(
    state: GameState,
    name: str,
    set_definitions: Mapping[str, Mapping[str, Any]] | None = None,
    *,
    equipment_sets: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, Any]:
    """Explain one final derived value from formula inputs through modifiers/floor."""
    set_definitions = resolve_set_context(
        set_definitions,
        equipment_sets=equipment_sets,
    )
    if name not in DERIVED_FORMULAS or name not in DERIVED_STAT_SPECS:
        raise RuleError(f"Unknown derived stat: {name}")

    formula = DERIVED_FORMULAS[name]
    base_constant = float(formula.get("base", 0.0))
    inputs: Dict[str, Dict[str, float]] = {}
    formula_total = base_constant

    for path, weight_raw in formula.get("terms", {}).items():
        weight = float(weight_raw)
        effective = _effective(state, path, set_definitions)
        contribution = effective * weight
        inputs[path] = {
            "effective_value": round(effective, 4),
            "weight": weight,
            "contribution": round(contribution, 4),
        }
        formula_total += contribution

    try:
        direct = modifier_breakdown(
            state,
            f"derived.{name}",
            set_definitions,
        )
    except ValueError as exc:
        raise RuleError(f"Invalid direct modifiers for derived.{name}: {exc}") from exc

    direct_total = float(direct["total"])
    raw_total = formula_total + direct_total
    total = _bounded_derived(name, raw_total)
    floor = DERIVED_STAT_SPECS[name].get("min")
    floor_adjustment = total - round(raw_total, 2)

    return {
        "name": name,
        "base_constant": base_constant,
        "inputs": inputs,
        "formula_total": round(formula_total, 2),
        "direct_modifiers": direct,
        "direct_modifier_total": round(direct_total, 2),
        "raw_total": round(raw_total, 2),
        "floor": floor,
        "floor_adjustment": round(floor_adjustment, 2),
        "total": total,
    }


def derived_stats(
    state: GameState,
    set_definitions: Mapping[str, Mapping[str, Any]] | None = None,
    *,
    equipment_sets: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, float]:
    set_definitions = resolve_set_context(
        set_definitions,
        equipment_sets=equipment_sets,
    )
    return {
        name: float(derived_stat_breakdown(state, name, set_definitions)["total"])
        for name in DERIVED_FORMULAS
    }


def initialize_resources(
    state: GameState,
    *,
    refill: bool = False,
    set_definitions: Mapping[str, Mapping[str, Any]] | None = None,
    equipment_sets: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, float]:
    set_definitions = resolve_set_context(
        set_definitions,
        equipment_sets=equipment_sets,
    )
    resources = state.player.setdefault("resources", {})
    derived = derived_stats(state, set_definitions)
    maxima = {
        "health": derived["max_health"],
        "stamina": derived["max_stamina"],
        "focus": derived["max_focus"],
        "resolve": derived["max_resolve"],
    }
    for key, maximum in maxima.items():
        max_key = f"max_{key}"
        resources[max_key] = maximum
        if refill or key not in resources:
            resources[key] = maximum
        else:
            resources[key] = max(0.0, min(float(resources[key]), maximum))
    return maxima
