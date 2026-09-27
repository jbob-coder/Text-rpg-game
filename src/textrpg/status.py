from __future__ import annotations

from math import isfinite
from typing import Any, Dict, Mapping

from .core import GameState, RuleError, RulesEngine
from .powers import ability_player_view
from .schema import ATTRIBUTE_SPECS, DERIVED_STAT_SPECS, RESOURCE_KEYS, SKILL_CATALOG


_IDENTITY_FIELDS = (
    "name",
    "origin",
    "background",
    "path",
    "level",
    "exp",
    "condition",
)

_RESOURCE_MAX_DERIVED = {
    "health": "max_health",
    "stamina": "max_stamina",
    "focus": "max_focus",
    "resolve": "max_resolve",
}


def _finite_number(value: Any, label: str) -> float:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not isfinite(float(value))
    ):
        raise RuleError(f"{label} must be a finite number")
    return float(value)


def _safe_identity_value(value: Any, label: str) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        if isinstance(value, float) and not isfinite(value):
            raise RuleError(f"{label} cannot be NaN or infinity")
        return value
    raise RuleError(f"{label} must be a scalar player-visible value")


def _attribute_view(
    state: GameState,
    engine: RulesEngine,
) -> list[Dict[str, Any]]:
    attributes = state.player.get("attributes", {})
    if attributes is None:
        attributes = {}
    if not isinstance(attributes, Mapping):
        raise RuleError("player.attributes must be an object")

    output: list[Dict[str, Any]] = []
    for attribute_id, spec in ATTRIBUTE_SPECS.items():
        base = _finite_number(
            attributes.get(attribute_id, 0),
            f"attribute {attribute_id}",
        )
        explanation = engine.explain_player_value(
            state,
            f"attributes.{attribute_id}",
        )
        effective = _finite_number(
            explanation["total"],
            f"effective attribute {attribute_id}",
        )
        output.append(
            {
                "id": attribute_id,
                "name": attribute_id.replace("_", " ").title(),
                "role": spec.get("role"),
                "base": base,
                "effective": effective,
                "delta": round(effective - base, 4),
                "modified": effective != base,
            }
        )
    return output


def _skill_view(
    state: GameState,
    engine: RulesEngine,
) -> Dict[str, list[Dict[str, Any]]]:
    skills = state.player.get("skills", {})
    if skills is None:
        skills = {}
    if not isinstance(skills, Mapping):
        raise RuleError("player.skills must be an object")

    grouped: Dict[str, list[Dict[str, Any]]] = {}
    for skill_id, category in SKILL_CATALOG.items():
        base = _finite_number(skills.get(skill_id, 0), f"skill {skill_id}")
        explanation = engine.explain_player_value(
            state,
            f"skills.{skill_id}",
        )
        effective = _finite_number(
            explanation["total"],
            f"effective skill {skill_id}",
        )
        grouped.setdefault(category, []).append(
            {
                "id": skill_id,
                "name": skill_id.replace("_", " ").title(),
                "base": base,
                "effective": effective,
                "delta": round(effective - base, 4),
                "modified": effective != base,
            }
        )
    return grouped


def _resource_view(
    state: GameState,
    engine: RulesEngine,
) -> list[Dict[str, Any]]:
    resources = state.player.get("resources", {})
    if resources is None:
        resources = {}
    if not isinstance(resources, Mapping):
        raise RuleError("player.resources must be an object")

    output: list[Dict[str, Any]] = []
    for resource_id in RESOURCE_KEYS:
        derived_id = _RESOURCE_MAX_DERIVED[resource_id]
        maximum = _finite_number(
            engine.explain_player_value(
                state,
                f"derived.{derived_id}",
            )["total"],
            f"resource maximum {resource_id}",
        )
        current = _finite_number(
            resources.get(resource_id, 0),
            f"resource {resource_id}",
        )
        output.append(
            {
                "id": resource_id,
                "name": resource_id.title(),
                "current": current,
                "max": maximum,
                "empty": current <= 0,
                "full": current >= maximum if maximum > 0 else current == 0,
                "over_cap": current > maximum,
            }
        )
    return output


def _derived_view(
    state: GameState,
    engine: RulesEngine,
) -> list[Dict[str, Any]]:
    output: list[Dict[str, Any]] = []
    for derived_id, spec in DERIVED_STAT_SPECS.items():
        total = _finite_number(
            engine.explain_player_value(
                state,
                f"derived.{derived_id}",
            )["total"],
            f"derived stat {derived_id}",
        )
        output.append(
            {
                "id": derived_id,
                "name": derived_id.replace("_", " ").title(),
                "value": total,
                "role": spec.get("role"),
            }
        )
    return output


def _condition_view(
    state: GameState,
    definitions: Mapping[str, Mapping[str, Any]],
) -> list[Dict[str, Any]]:
    conditions = state.player.get("conditions", {})
    if conditions is None:
        conditions = {}
    if not isinstance(conditions, Mapping):
        raise RuleError("player.conditions must be an object")

    output: list[Dict[str, Any]] = []
    for condition_id, record in conditions.items():
        if not isinstance(condition_id, str) or not condition_id:
            raise RuleError("Condition IDs must be non-empty strings")
        if not isinstance(record, Mapping):
            raise RuleError(f"Condition record must be an object: {condition_id}")

        definition = definitions.get(condition_id, {})
        if not isinstance(definition, Mapping):
            raise RuleError(f"Condition definition must be an object: {condition_id}")

        if record.get("visible", True) is False:
            continue
        if definition.get("player_visible", True) is False:
            continue

        severity = record.get("severity", 1)
        if isinstance(severity, bool) or not isinstance(severity, int):
            raise RuleError(f"Condition severity must be an integer: {condition_id}")

        duration = record.get("duration_minutes")
        if duration is not None and (
            isinstance(duration, bool)
            or not isinstance(duration, int)
            or duration < 0
        ):
            raise RuleError(
                f"Condition duration must be null or a non-negative integer: {condition_id}"
            )

        tags = record.get("tags", [])
        if not isinstance(tags, list) or not all(
            isinstance(tag, str) and tag for tag in tags
        ):
            raise RuleError(f"Condition tags must be a list of strings: {condition_id}")

        fallback_id = (
            condition_id.removeprefix("COND_")
            if condition_id.startswith("COND_")
            else condition_id
        )
        display_name = definition.get(
            "name",
            fallback_id.replace("_", " ").title(),
        )
        if not isinstance(display_name, str) or not display_name:
            raise RuleError(f"Condition name must be a non-empty string: {condition_id}")

        output.append(
            {
                "id": condition_id,
                "name": display_name,
                "severity": severity,
                "duration_minutes": duration,
                "tags": list(tags),
            }
        )
    return output


def build_status_view(
    state: GameState,
    engine: RulesEngine,
    *,
    ability_definitions: Mapping[str, Mapping[str, Any]] | None = None,
    condition_definitions: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, Any]:
    """Build a non-mutating player-facing status projection.

    The projection deliberately excludes raw modifier maps, hidden quest/NPC state,
    and undiscovered ability evolution requirements. The rules layer owns all
    arithmetic; this module only organizes already-authoritative values.
    """
    if not isinstance(engine, RulesEngine):
        raise RuleError("build_status_view requires the active RulesEngine")

    ability_definitions = ability_definitions or {}
    condition_definitions = condition_definitions or {}
    if not isinstance(ability_definitions, Mapping):
        raise RuleError("ability_definitions must be an object")
    if not isinstance(condition_definitions, Mapping):
        raise RuleError("condition_definitions must be an object")

    identity: Dict[str, Any] = {}
    for field in _IDENTITY_FIELDS:
        if field in state.player:
            identity[field] = _safe_identity_value(
                state.player[field],
                f"player.{field}",
            )

    abilities: list[Dict[str, Any]] = []
    for ability_id in sorted(state.abilities):
        definition = ability_definitions.get(ability_id, {})
        if not isinstance(definition, Mapping):
            raise RuleError(f"Ability definition must be an object: {ability_id}")
        abilities.append(
            ability_player_view(
                state,
                ability_id,
                definition,
            )
        )

    return {
        "identity": identity,
        "attributes": _attribute_view(state, engine),
        "resources": _resource_view(state, engine),
        "derived": _derived_view(state, engine),
        "skills": _skill_view(state, engine),
        "abilities": abilities,
        "conditions": _condition_view(state, condition_definitions),
    }
