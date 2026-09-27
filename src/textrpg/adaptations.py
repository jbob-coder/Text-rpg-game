from __future__ import annotations

from typing import Any, Dict, Mapping, MutableMapping

from .beasts import (
    ADAPTATION_TYPES,
    OBSERVATION_KINDS,
    adaptation_readiness,
    validate_beast_state,
)
from .core import RuleError


def _string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise RuleError(f"{label} must be a non-empty string")
    return value


def _string_list(value: Any, label: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
        raise RuleError(f"{label} must be a list of non-empty strings")
    if len(set(value)) != len(value):
        raise RuleError(f"{label} must not contain duplicates")
    return list(value)


def validate_adaptation_definitions(definitions: Mapping[str, Mapping[str, Any]]) -> None:
    if not isinstance(definitions, Mapping):
        raise RuleError("adaptation definitions must be an object")
    for adaptation_id, definition in definitions.items():
        _string(adaptation_id, "adaptation ID")
        if not isinstance(definition, Mapping):
            raise RuleError(f"Adaptation definition must be an object: {adaptation_id}")
        _string(definition.get("name", adaptation_id.replace("_", " ").title()), f"{adaptation_id}.name")
        kind = definition.get("observation_kind")
        if kind not in OBSERVATION_KINDS:
            raise RuleError(f"Unsupported adaptation observation_kind: {kind}")
        _string(definition.get("observation_value"), f"{adaptation_id}.observation_value")
        adaptation_type = definition.get("adaptation_type")
        if adaptation_type not in ADAPTATION_TYPES:
            raise RuleError(f"Unsupported adaptation type: {adaptation_type}")
        _string_list(definition.get("granted_tags", []), f"{adaptation_id}.granted_tags")
        priority = definition.get("priority", 0)
        if isinstance(priority, bool) or not isinstance(priority, int):
            raise RuleError(f"{adaptation_id}.priority must be an integer")
        visible = definition.get("player_visible", True)
        if not isinstance(visible, bool):
            raise RuleError(f"{adaptation_id}.player_visible must be boolean")


def eligible_adaptations(
    beast: Mapping[str, Any],
    definitions: Mapping[str, Mapping[str, Any]],
    *,
    elapsed_minutes: int = 0,
    resource_score: float = 0.0,
) -> list[Dict[str, Any]]:
    validate_beast_state(beast)
    validate_adaptation_definitions(definitions)
    existing = set(beast.get("adaptations", []))
    results: list[Dict[str, Any]] = []

    for adaptation_id, definition in definitions.items():
        if adaptation_id in existing:
            continue
        readiness = adaptation_readiness(
            beast,
            kind=definition["observation_kind"],
            value=definition["observation_value"],
            adaptation_type=definition["adaptation_type"],
            elapsed_minutes=elapsed_minutes,
            resource_score=resource_score,
        )
        if not readiness["ready"]:
            continue
        results.append({
            "adaptation_id": adaptation_id,
            "priority": definition.get("priority", 0),
            "readiness": readiness,
        })

    results.sort(key=lambda entry: (-entry["priority"], entry["adaptation_id"]))
    return results


def apply_adaptation(
    beast: MutableMapping[str, Any],
    definitions: Mapping[str, Mapping[str, Any]],
    adaptation_id: str,
    *,
    elapsed_minutes: int = 0,
    resource_score: float = 0.0,
) -> Dict[str, Any]:
    if not isinstance(beast, MutableMapping):
        raise RuleError("beast state must be mutable")
    validate_beast_state(beast)
    validate_adaptation_definitions(definitions)
    adaptation_id = _string(adaptation_id, "adaptation_id")
    if adaptation_id not in definitions:
        raise RuleError(f"Unknown adaptation: {adaptation_id}")
    if adaptation_id in beast.get("adaptations", []):
        raise RuleError(f"Adaptation already applied: {adaptation_id}")

    definition = definitions[adaptation_id]
    readiness = adaptation_readiness(
        beast,
        kind=definition["observation_kind"],
        value=definition["observation_value"],
        adaptation_type=definition["adaptation_type"],
        elapsed_minutes=elapsed_minutes,
        resource_score=resource_score,
    )
    if not readiness["ready"]:
        raise RuleError(
            f"Adaptation is not ready: {adaptation_id}; reasons={readiness['reasons']}"
        )

    adaptations = beast.get("adaptations")
    if not isinstance(adaptations, list):
        raise RuleError("beast.adaptations must be a list")
    tags = beast.get("adaptation_tags")
    if tags is None:
        tags = []
        beast["adaptation_tags"] = tags
    if not isinstance(tags, list) or not all(isinstance(tag, str) and tag for tag in tags):
        raise RuleError("beast.adaptation_tags must be a list of non-empty strings")

    adaptations.append(adaptation_id)
    for tag in definition.get("granted_tags", []):
        if tag not in tags:
            tags.append(tag)

    return {
        "adaptation_id": adaptation_id,
        "adaptation_type": definition["adaptation_type"],
        "granted_tags": list(definition.get("granted_tags", [])),
        "readiness": readiness,
    }


def adaptation_player_view(
    beast: Mapping[str, Any],
    definitions: Mapping[str, Mapping[str, Any]],
) -> list[Dict[str, Any]]:
    validate_beast_state(beast)
    validate_adaptation_definitions(definitions)
    output: list[Dict[str, Any]] = []
    for adaptation_id in beast.get("adaptations", []):
        definition = definitions.get(adaptation_id)
        if definition is None or definition.get("player_visible", True) is False:
            continue
        output.append({
            "id": adaptation_id,
            "name": definition.get("name", adaptation_id.replace("_", " ").title()),
            "type": definition["adaptation_type"],
        })
    return output
