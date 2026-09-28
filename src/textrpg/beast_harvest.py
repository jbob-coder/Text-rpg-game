from __future__ import annotations

from copy import deepcopy
from math import isfinite
from typing import Any, Dict, List, Mapping

from .core import RuleError
from .medieval import DAMAGE_TYPES, validate_beast_runtime_state, validate_crystal_instance


def _stable_id(value: Any) -> bool:
    return (
        isinstance(value, str)
        and bool(value)
        and value[0].isalpha()
        and all(char.isupper() or char.isdigit() or char == "_" for char in value)
    )


def _finite_number(
    value: Any,
    *,
    minimum: float | None = None,
    maximum: float | None = None,
) -> bool:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    numeric = float(value)
    if not isfinite(numeric):
        return False
    if minimum is not None and numeric < minimum:
        return False
    if maximum is not None and numeric > maximum:
        return False
    return True


def validate_crystal_definition(definition: Any) -> List[str]:
    if not isinstance(definition, Mapping):
        return ["crystal definition must be an object"]

    errors: List[str] = []
    for field_name in ("crystal_id", "core_zone_id"):
        if not _stable_id(definition.get(field_name)):
            errors.append(f"crystal_definition.{field_name} must be a stable uppercase ID")

    grade = definition.get("base_grade")
    if isinstance(grade, bool) or not isinstance(grade, int) or grade < 1:
        errors.append("crystal_definition.base_grade must be an integer >= 1")

    for field_name in ("base_purity", "base_stability"):
        if not _finite_number(definition.get(field_name), minimum=0.0, maximum=100.0):
            errors.append(
                f"crystal_definition.{field_name} must be finite numeric in range 0..100"
            )

    if not _finite_number(definition.get("size"), minimum=0.000001):
        errors.append("crystal_definition.size must be finite numeric > 0")

    if not _finite_number(
        definition.get("core_damage_sensitivity", 1.0), minimum=0.0, maximum=2.0
    ):
        errors.append(
            "crystal_definition.core_damage_sensitivity must be finite numeric in range 0..2"
        )

    if not _finite_number(
        definition.get("decay_per_hour", 0.0), minimum=0.0, maximum=100.0
    ):
        errors.append(
            "crystal_definition.decay_per_hour must be finite numeric in range 0..100"
        )

    tags = definition.get("resonance_tags", [])
    if not isinstance(tags, list) or not all(isinstance(tag, str) and tag for tag in tags):
        errors.append(
            "crystal_definition.resonance_tags must be a list of non-empty strings"
        )
    elif len(tags) != len(set(tags)):
        errors.append("crystal_definition.resonance_tags must not contain duplicates")

    effects = definition.get("effects", {})
    if not isinstance(effects, Mapping):
        errors.append("crystal_definition.effects must be an object")
    else:
        for effect_id, value in effects.items():
            if not _stable_id(effect_id):
                errors.append(
                    f"crystal_definition effect ID must be stable uppercase: {effect_id!r}"
                )
            if not _finite_number(value, minimum=0.0):
                errors.append(
                    f"crystal_definition.effects.{effect_id} must be finite non-negative numeric"
                )

    return errors


def validate_body_zone_runtime(zone_state: Any) -> List[str]:
    if not isinstance(zone_state, Mapping):
        return ["body zone runtime state must be an object"]

    errors: List[str] = []
    if not _stable_id(zone_state.get("zone_id")):
        errors.append("body_zone.zone_id must be a stable uppercase ID")

    maximum = zone_state.get("max_integrity")
    damage = zone_state.get("damage_taken")
    if not _finite_number(maximum, minimum=0.000001):
        errors.append("body_zone.max_integrity must be finite numeric > 0")
    if not _finite_number(damage, minimum=0.0):
        errors.append("body_zone.damage_taken must be finite non-negative numeric")
    if (
        _finite_number(maximum, minimum=0.000001)
        and _finite_number(damage, minimum=0.0)
        and float(damage) > float(maximum)
    ):
        errors.append("body_zone.damage_taken cannot exceed max_integrity")

    hits = zone_state.get("hits", 0)
    if isinstance(hits, bool) or not isinstance(hits, int) or hits < 0:
        errors.append("body_zone.hits must be a non-negative integer")

    breakdown = zone_state.get("damage_by_type", {})
    if not isinstance(breakdown, Mapping):
        errors.append("body_zone.damage_by_type must be an object")
    else:
        for damage_type, amount in breakdown.items():
            if damage_type not in DAMAGE_TYPES:
                errors.append(
                    f"body_zone.damage_by_type has unsupported type: {damage_type!r}"
                )
            elif not _finite_number(amount, minimum=0.0):
                errors.append(
                    f"body_zone.damage_by_type.{damage_type} must be finite non-negative numeric"
                )
    return errors


def apply_body_zone_damage(
    zone_state: Mapping[str, Any],
    amount: float,
    damage_type: str,
) -> Dict[str, Any]:
    """Apply already-resolved combat damage without deciding target availability here."""
    errors = validate_body_zone_runtime(zone_state)
    if errors:
        raise RuleError("Invalid body-zone runtime state:\n- " + "\n- ".join(errors))
    if not _finite_number(amount, minimum=0.000001):
        raise RuleError("body-zone damage amount must be finite numeric > 0")
    if damage_type not in DAMAGE_TYPES:
        raise RuleError(f"Unsupported body-zone damage type: {damage_type}")

    updated = deepcopy(dict(zone_state))
    maximum = float(updated["max_integrity"])
    old_damage = float(updated["damage_taken"])
    applied = min(float(amount), maximum - old_damage)
    updated["damage_taken"] = round(old_damage + applied, 4)
    updated["hits"] = int(updated.get("hits", 0)) + 1

    breakdown = dict(updated.get("damage_by_type", {}))
    breakdown[damage_type] = round(float(breakdown.get(damage_type, 0.0)) + applied, 4)
    updated["damage_by_type"] = breakdown
    updated["broken"] = updated["damage_taken"] >= maximum
    return updated


def harvest_beast_crystal(
    beast_state: Mapping[str, Any],
    core_zone_state: Mapping[str, Any],
    crystal_definition: Mapping[str, Any],
    *,
    instance_id: str,
    harvest_skill: float,
    tool_quality: float,
    elapsed_minutes: int = 0,
) -> Dict[str, Any]:
    """Create a beast-crystal instance whose integrity reflects combat and extraction."""
    beast_errors = validate_beast_runtime_state(beast_state)
    zone_errors = validate_body_zone_runtime(core_zone_state)
    crystal_errors = validate_crystal_definition(crystal_definition)
    if beast_errors or zone_errors or crystal_errors:
        raise RuleError(
            "Invalid beast crystal harvest contract:\n- "
            + "\n- ".join(beast_errors + zone_errors + crystal_errors)
        )

    if beast_state.get("life_state") != "dead":
        raise RuleError("beast crystal can only be harvested from a dead beast")
    if core_zone_state["zone_id"] != crystal_definition["core_zone_id"]:
        raise RuleError("core zone does not match crystal definition")
    if not _stable_id(instance_id):
        raise RuleError("crystal instance_id must be a stable uppercase ID")
    if not _finite_number(harvest_skill, minimum=0.0, maximum=100.0):
        raise RuleError("harvest_skill must be finite numeric in range 0..100")
    if not _finite_number(tool_quality, minimum=0.0, maximum=100.0):
        raise RuleError("tool_quality must be finite numeric in range 0..100")
    if isinstance(elapsed_minutes, bool) or not isinstance(elapsed_minutes, int) or elapsed_minutes < 0:
        raise RuleError("elapsed_minutes must be a non-negative integer")

    max_integrity = float(core_zone_state["max_integrity"])
    core_damage_ratio = float(core_zone_state["damage_taken"]) / max_integrity
    sensitivity = float(crystal_definition.get("core_damage_sensitivity", 1.0))
    combat_remaining = max(0.0, 1.0 - core_damage_ratio * sensitivity)

    extraction_quality = (float(harvest_skill) * 0.65) + (float(tool_quality) * 0.35)
    extraction_factor = 0.5 + (extraction_quality / 200.0)

    decay_per_hour = float(crystal_definition.get("decay_per_hour", 0.0))
    decay_penalty = min(100.0, (elapsed_minutes / 60.0) * decay_per_hour)
    time_factor = max(0.0, 1.0 - decay_penalty / 100.0)

    harvest_integrity = round(
        max(0.0, min(100.0, 100.0 * combat_remaining * extraction_factor * time_factor)),
        2,
    )

    # Damage to the core can also reduce crystal stability. Purity represents the
    # authored material itself and is not magically improved by harvesting skill.
    base_stability = float(crystal_definition["base_stability"])
    stability = round(max(0.0, base_stability * combat_remaining), 2)

    crystal = {
        "instance_id": instance_id,
        "crystal_id": crystal_definition["crystal_id"],
        "source_type": "beast",
        "source_beast_id": beast_state["beast_id"],
        "grade": crystal_definition["base_grade"],
        "purity": float(crystal_definition["base_purity"]),
        "stability": stability,
        "harvest_integrity": harvest_integrity,
        "size": float(crystal_definition["size"]),
        "resonance_tags": list(crystal_definition.get("resonance_tags", [])),
        "effects": {
            effect_id: float(value)
            for effect_id, value in crystal_definition.get("effects", {}).items()
        },
        "harvest": {
            "core_zone_id": core_zone_state["zone_id"],
            "core_damage_percent": round(core_damage_ratio * 100.0, 2),
            "extraction_quality": round(extraction_quality, 2),
            "elapsed_minutes": elapsed_minutes,
        },
    }

    errors = validate_crystal_instance(crystal)
    if errors:
        raise RuleError("Harvest produced invalid crystal instance:\n- " + "\n- ".join(errors))
    return crystal
