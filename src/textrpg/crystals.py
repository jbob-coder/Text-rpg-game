from __future__ import annotations

from math import isfinite
from typing import Any, Dict, Iterable, Mapping

from .core import RuleError


CRYSTAL_SOURCE_TYPES = ("mine", "beast")
APPRAISAL_STATES = ("unknown", "partial", "known")


def _string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise RuleError(f"{label} must be a non-empty string")
    return value


def _finite(
    value: Any,
    label: str,
    *,
    minimum: float | None = None,
    maximum: float | None = None,
) -> float:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not isfinite(float(value))
    ):
        raise RuleError(f"{label} must be a finite number")
    number = float(value)
    if minimum is not None and number < minimum:
        raise RuleError(f"{label} must be >= {minimum}")
    if maximum is not None and number > maximum:
        raise RuleError(f"{label} must be <= {maximum}")
    return number


def _string_list(value: Any, label: str) -> list[str]:
    if value is None:
        return []
    if isinstance(value, (str, bytes)) or not isinstance(value, Iterable):
        raise RuleError(f"{label} must be a list of non-empty strings")
    result = list(value)
    if not all(isinstance(item, str) and item for item in result):
        raise RuleError(f"{label} must be a list of non-empty strings")
    if len(set(result)) != len(result):
        raise RuleError(f"{label} must not contain duplicates")
    return result


def validate_crystal_definitions(
    definitions: Mapping[str, Mapping[str, Any]],
) -> None:
    if not isinstance(definitions, Mapping):
        raise RuleError("crystal definitions must be an object")

    for crystal_id, definition in definitions.items():
        _string(crystal_id, "crystal ID")
        if not isinstance(definition, Mapping):
            raise RuleError(f"Crystal definition must be an object: {crystal_id}")

        _string(
            definition.get("name", crystal_id.replace("_", " ").title()),
            f"crystal name: {crystal_id}",
        )
        _string_list(
            definition.get("affinities", []),
            f"{crystal_id}.affinities",
        )
        _string_list(
            definition.get("tags", []),
            f"{crystal_id}.tags",
        )

        allowed_sources = definition.get(
            "allowed_source_types",
            list(CRYSTAL_SOURCE_TYPES),
        )
        allowed_sources = _string_list(
            allowed_sources,
            f"{crystal_id}.allowed_source_types",
        )
        unknown = set(allowed_sources).difference(CRYSTAL_SOURCE_TYPES)
        if unknown:
            raise RuleError(
                f"{crystal_id}.allowed_source_types contains unsupported values: "
                f"{sorted(unknown)}"
            )

        visible = definition.get("player_visible", True)
        if not isinstance(visible, bool):
            raise RuleError(f"{crystal_id}.player_visible must be boolean")


def validate_crystal_instance(
    instance: Mapping[str, Any],
    definitions: Mapping[str, Mapping[str, Any]],
) -> None:
    if not isinstance(instance, Mapping):
        raise RuleError("crystal instance must be an object")
    validate_crystal_definitions(definitions)

    instance_id = _string(instance.get("instance_id"), "crystal.instance_id")
    crystal_id = _string(instance.get("crystal_id"), f"{instance_id}.crystal_id")
    if crystal_id not in definitions:
        raise RuleError(f"Unknown crystal definition: {crystal_id}")

    source_type = instance.get("source_type")
    if source_type not in CRYSTAL_SOURCE_TYPES:
        raise RuleError(f"Unsupported crystal source_type: {source_type}")

    allowed_sources = definitions[crystal_id].get(
        "allowed_source_types",
        list(CRYSTAL_SOURCE_TYPES),
    )
    if source_type not in allowed_sources:
        raise RuleError(
            f"Crystal {crystal_id} cannot originate from source_type {source_type}"
        )

    _string(instance.get("source_id"), f"{instance_id}.source_id")

    grade = instance.get("grade", 1)
    if isinstance(grade, bool) or not isinstance(grade, int) or grade < 1:
        raise RuleError(f"{instance_id}.grade must be an integer >= 1")

    _finite(instance.get("purity", 1.0), f"{instance_id}.purity", minimum=0.0, maximum=1.0)
    _finite(
        instance.get("stability", 1.0),
        f"{instance_id}.stability",
        minimum=0.0,
        maximum=1.0,
    )
    _finite(
        instance.get("integrity", 1.0),
        f"{instance_id}.integrity",
        minimum=0.0,
        maximum=1.0,
    )
    _finite(instance.get("size", 1.0), f"{instance_id}.size", minimum=0.0000001)
    _finite(instance.get("resonance", 0.0), f"{instance_id}.resonance", minimum=0.0)
    _finite(
        instance.get("harvest_damage", 0.0),
        f"{instance_id}.harvest_damage",
        minimum=0.0,
        maximum=1.0,
    )

    appraisal_state = instance.get("appraisal_state", "unknown")
    if appraisal_state not in APPRAISAL_STATES:
        raise RuleError(
            f"{instance_id}.appraisal_state must be one of {APPRAISAL_STATES}"
        )

    _string_list(instance.get("traits", []), f"{instance_id}.traits")

    if source_type == "beast":
        _string(instance.get("beast_id"), f"{instance_id}.beast_id")
    elif source_type == "mine":
        _string(instance.get("deposit_id"), f"{instance_id}.deposit_id")


def crystal_player_view(
    instance: Mapping[str, Any],
    definitions: Mapping[str, Mapping[str, Any]],
) -> Dict[str, Any]:
    """Return a player-safe crystal projection based on appraisal state."""
    validate_crystal_instance(instance, definitions)
    crystal_id = instance["crystal_id"]
    definition = definitions[crystal_id]
    appraisal_state = instance.get("appraisal_state", "unknown")

    if definition.get("player_visible", True) is False:
        return {
            "instance_id": instance["instance_id"],
            "appraisal_state": "unknown",
            "name": "Unknown Crystal",
        }

    base: Dict[str, Any] = {
        "instance_id": instance["instance_id"],
        "appraisal_state": appraisal_state,
        "integrity": float(instance.get("integrity", 1.0)),
    }

    if appraisal_state == "unknown":
        base["name"] = "Unknown Crystal"
        base["size"] = float(instance.get("size", 1.0))
        return base

    base["name"] = definition.get(
        "name",
        crystal_id.replace("_", " ").title(),
    )
    base["grade"] = int(instance.get("grade", 1))
    base["source_type"] = instance["source_type"]

    if appraisal_state == "partial":
        return base

    base.update(
        {
            "crystal_id": crystal_id,
            "source_id": instance["source_id"],
            "purity": float(instance.get("purity", 1.0)),
            "stability": float(instance.get("stability", 1.0)),
            "size": float(instance.get("size", 1.0)),
            "resonance": float(instance.get("resonance", 0.0)),
            "harvest_damage": float(instance.get("harvest_damage", 0.0)),
            "affinities": list(definition.get("affinities", [])),
            "traits": list(instance.get("traits", [])),
        }
    )
    return base


def effective_crystal_integrity(instance: Mapping[str, Any]) -> float:
    """Return physical integrity after harvest damage without mutating state."""
    if not isinstance(instance, Mapping):
        raise RuleError("crystal instance must be an object")
    integrity = _finite(
        instance.get("integrity", 1.0),
        "crystal.integrity",
        minimum=0.0,
        maximum=1.0,
    )
    harvest_damage = _finite(
        instance.get("harvest_damage", 0.0),
        "crystal.harvest_damage",
        minimum=0.0,
        maximum=1.0,
    )
    return round(max(0.0, integrity * (1.0 - harvest_damage)), 4)
