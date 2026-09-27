from __future__ import annotations

from typing import Any, Dict, Mapping

from .beasts import BEAST_ROLES, OBSERVATION_KINDS, communication_tier, validate_beast_state
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


def validate_voice_definitions(definitions: Mapping[str, Mapping[str, Any]]) -> None:
    if not isinstance(definitions, Mapping):
        raise RuleError("voice definitions must be an object")
    for bark_id, definition in definitions.items():
        _string(bark_id, "voice bark ID")
        if not isinstance(definition, Mapping):
            raise RuleError(f"Voice definition must be an object: {bark_id}")
        _string(definition.get("text"), f"{bark_id}.text")
        min_tier = definition.get("min_tier", 0)
        max_tier = definition.get("max_tier", 5)
        for label, value in (("min_tier", min_tier), ("max_tier", max_tier)):
            if isinstance(value, bool) or not isinstance(value, int) or value < 0 or value > 5:
                raise RuleError(f"{bark_id}.{label} must be an integer in range 0..5")
        if min_tier > max_tier:
            raise RuleError(f"{bark_id}.min_tier cannot exceed max_tier")
        contexts = _string_list(definition.get("contexts", []), f"{bark_id}.contexts")
        if not contexts:
            raise RuleError(f"{bark_id}.contexts must not be empty")
        roles = _string_list(definition.get("roles", []), f"{bark_id}.roles")
        unknown_roles = set(roles).difference(BEAST_ROLES)
        if unknown_roles:
            raise RuleError(f"{bark_id}.roles contains unsupported values: {sorted(unknown_roles)}")
        _string_list(definition.get("required_adaptation_tags", []), f"{bark_id}.required_adaptation_tags")
        memory = definition.get("memory_requirement")
        if memory is not None:
            if not isinstance(memory, Mapping):
                raise RuleError(f"{bark_id}.memory_requirement must be an object")
            memory_kind = _string(memory.get("kind"), f"{bark_id}.memory_requirement.kind")
            if memory_kind not in OBSERVATION_KINDS:
                raise RuleError(f"Unsupported voice memory observation kind: {memory_kind}")
            _string(memory.get("value"), f"{bark_id}.memory_requirement.value")
        priority = definition.get("priority", 0)
        if isinstance(priority, bool) or not isinstance(priority, int):
            raise RuleError(f"{bark_id}.priority must be an integer")


def _has_memory(beast: Mapping[str, Any], requirement: Mapping[str, Any]) -> bool:
    key = f"{requirement['kind']}:{requirement['value']}"
    return key in beast.get("encounter_memory", {})


def eligible_barks(
    beast: Mapping[str, Any],
    species_definition: Mapping[str, Any],
    definitions: Mapping[str, Mapping[str, Any]],
    *,
    context: str,
) -> list[Dict[str, Any]]:
    validate_beast_state(beast)
    validate_voice_definitions(definitions)
    context = _string(context, "voice context")
    tier = communication_tier(beast, species_definition)
    adaptation_tags = set(beast.get("adaptation_tags", []))
    if not all(isinstance(tag, str) and tag for tag in adaptation_tags):
        raise RuleError("beast.adaptation_tags must contain non-empty strings")

    output: list[Dict[str, Any]] = []
    for bark_id, definition in definitions.items():
        if context not in definition["contexts"]:
            continue
        if tier < definition.get("min_tier", 0) or tier > definition.get("max_tier", 5):
            continue
        roles = definition.get("roles", [])
        if roles and beast.get("role", "solitary") not in roles:
            continue
        required_tags = set(definition.get("required_adaptation_tags", []))
        if not required_tags.issubset(adaptation_tags):
            continue
        memory_requirement = definition.get("memory_requirement")
        if memory_requirement is not None and not _has_memory(beast, memory_requirement):
            continue
        output.append({
            "bark_id": bark_id,
            "text": definition["text"],
            "priority": definition.get("priority", 0),
            "communication_tier": tier,
        })

    output.sort(key=lambda entry: (-entry["priority"], entry["bark_id"]))
    return output


def select_beast_bark(
    beast: Mapping[str, Any],
    species_definition: Mapping[str, Any],
    definitions: Mapping[str, Mapping[str, Any]],
    *,
    context: str,
) -> Dict[str, Any] | None:
    """Select one deterministic authored bark; never invokes generative AI."""
    candidates = eligible_barks(
        beast,
        species_definition,
        definitions,
        context=context,
    )
    if not candidates:
        return None
    chosen = candidates[0]
    return {
        "bark_id": chosen["bark_id"],
        "text": chosen["text"],
        "communication_tier": chosen["communication_tier"],
        "context": context,
    }
