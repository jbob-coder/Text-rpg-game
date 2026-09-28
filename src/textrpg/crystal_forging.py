from __future__ import annotations

from copy import deepcopy
from math import isfinite
from typing import Any, Dict, List, Mapping

from .core import RuleError
from .medieval import CRYSTAL_SOURCE_TYPES, validate_crystal_instance


INTEGRATION_MODES = ("socket", "fusion")


def _stable_id(value: Any) -> bool:
    return (
        isinstance(value, str)
        and bool(value)
        and value[0].isalpha()
        and all(char.isupper() or char.isdigit() or char == "_" for char in value)
    )


def _percent(value: Any) -> bool:
    return (
        not isinstance(value, bool)
        and isinstance(value, (int, float))
        and isfinite(float(value))
        and 0.0 <= float(value) <= 100.0
    )


def validate_equipment_instance(item: Any) -> List[str]:
    if not isinstance(item, Mapping):
        return ["equipment instance must be an object"]

    errors: List[str] = []
    for field_name in ("instance_id", "definition_id", "material_id"):
        if not _stable_id(item.get(field_name)):
            errors.append(f"equipment.{field_name} must be a stable uppercase ID")

    for field_name in ("forge_quality", "condition"):
        if not _percent(item.get(field_name)):
            errors.append(f"equipment.{field_name} must be finite numeric in range 0..100")

    sockets = item.get("crystal_sockets", [])
    if not isinstance(sockets, list):
        errors.append("equipment.crystal_sockets must be a list")
        return errors

    seen_ids: set[str] = set()
    for index, socket in enumerate(sockets):
        label = f"equipment.crystal_sockets[{index}]"
        if not isinstance(socket, Mapping):
            errors.append(f"{label} must be an object")
            continue

        socket_id = socket.get("socket_id")
        if not _stable_id(socket_id):
            errors.append(f"{label}.socket_id must be a stable uppercase ID")
        elif socket_id in seen_ids:
            errors.append(f"duplicate equipment crystal socket ID: {socket_id}")
        else:
            seen_ids.add(socket_id)

        max_grade = socket.get("max_grade")
        if isinstance(max_grade, bool) or not isinstance(max_grade, int) or max_grade < 1:
            errors.append(f"{label}.max_grade must be an integer >= 1")

        allowed_sources = socket.get("allowed_source_types", list(CRYSTAL_SOURCE_TYPES))
        if (
            not isinstance(allowed_sources, list)
            or not allowed_sources
            or not all(source in CRYSTAL_SOURCE_TYPES for source in allowed_sources)
        ):
            errors.append(f"{label}.allowed_source_types must contain supported source types")

        allowed_tags = socket.get("allowed_resonance_tags", [])
        if not isinstance(allowed_tags, list) or not all(
            isinstance(tag, str) and tag for tag in allowed_tags
        ):
            errors.append(f"{label}.allowed_resonance_tags must be a list of non-empty strings")

        allowed_modes = socket.get("allowed_modes", ["socket"])
        if (
            not isinstance(allowed_modes, list)
            or not allowed_modes
            or not all(mode in INTEGRATION_MODES for mode in allowed_modes)
        ):
            errors.append(f"{label}.allowed_modes must contain supported integration modes")

        crystal = socket.get("crystal")
        if crystal is not None:
            crystal_errors = validate_crystal_instance(crystal)
            errors.extend(f"{label}.crystal: {error}" for error in crystal_errors)
            if socket.get("locked") not in (True, False, None):
                errors.append(f"{label}.locked must be boolean when provided")

            integration = socket.get("integration")
            if not isinstance(integration, Mapping):
                errors.append(f"{label}.integration must be an object when occupied")
            else:
                if integration.get("mode") not in INTEGRATION_MODES:
                    errors.append(f"{label}.integration.mode is unsupported")
                if not _percent(integration.get("quality")):
                    errors.append(
                        f"{label}.integration.quality must be finite numeric in range 0..100"
                    )
                smith_id = integration.get("smith_id")
                if smith_id is not None and not _stable_id(smith_id):
                    errors.append(
                        f"{label}.integration.smith_id must be a stable uppercase ID"
                    )
    return errors


def crystal_socket_compatibility(
    item: Mapping[str, Any],
    crystal: Mapping[str, Any],
    socket_id: str,
    *,
    mode: str = "socket",
) -> Dict[str, Any]:
    item_errors = validate_equipment_instance(item)
    crystal_errors = validate_crystal_instance(crystal)
    if item_errors or crystal_errors:
        raise RuleError(
            "Invalid crystal integration contract:\n- "
            + "\n- ".join(item_errors + crystal_errors)
        )
    if not _stable_id(socket_id):
        raise RuleError("socket_id must be a stable uppercase ID")
    if mode not in INTEGRATION_MODES:
        raise RuleError(f"Unsupported integration mode: {mode}")

    socket = next(
        (entry for entry in item["crystal_sockets"] if entry["socket_id"] == socket_id),
        None,
    )
    if socket is None:
        raise RuleError(f"Unknown crystal socket: {socket_id}")

    reasons: List[str] = []
    if socket.get("crystal") is not None:
        reasons.append("occupied")
    if crystal["grade"] > socket["max_grade"]:
        reasons.append("grade")
    if crystal["source_type"] not in socket.get(
        "allowed_source_types", list(CRYSTAL_SOURCE_TYPES)
    ):
        reasons.append("source_type")
    if mode not in socket.get("allowed_modes", ["socket"]):
        reasons.append("mode")

    allowed_tags = set(socket.get("allowed_resonance_tags", []))
    crystal_tags = set(crystal.get("resonance_tags", []))
    if allowed_tags and not allowed_tags.intersection(crystal_tags):
        reasons.append("resonance")

    return {"compatible": not reasons, "reasons": reasons}


def integrate_crystal(
    item: Mapping[str, Any],
    crystal: Mapping[str, Any],
    socket_id: str,
    *,
    mode: str = "socket",
    integration_quality: float,
    smith_id: str | None = None,
) -> Dict[str, Any]:
    """Return a new equipment instance with one compatible crystal integrated."""
    compatibility = crystal_socket_compatibility(item, crystal, socket_id, mode=mode)
    if not compatibility["compatible"]:
        raise RuleError(
            f"Crystal is incompatible with {socket_id}: "
            + ", ".join(compatibility["reasons"])
        )
    if not _percent(integration_quality):
        raise RuleError("integration_quality must be finite numeric in range 0..100")
    if smith_id is not None and not _stable_id(smith_id):
        raise RuleError("smith_id must be a stable uppercase ID when provided")

    updated = deepcopy(dict(item))
    for socket in updated["crystal_sockets"]:
        if socket["socket_id"] != socket_id:
            continue
        socket["crystal"] = deepcopy(dict(crystal))
        socket["integration"] = {
            "mode": mode,
            "quality": round(float(integration_quality), 2),
            "smith_id": smith_id,
        }
        socket["locked"] = mode == "fusion"
        break
    return updated


def remove_socketed_crystal(
    item: Mapping[str, Any],
    socket_id: str,
) -> Dict[str, Any]:
    """Remove a replaceable crystal; permanent fusion cannot be silently reversed."""
    errors = validate_equipment_instance(item)
    if errors:
        raise RuleError("Invalid equipment instance:\n- " + "\n- ".join(errors))
    if not _stable_id(socket_id):
        raise RuleError("socket_id must be a stable uppercase ID")

    updated = deepcopy(dict(item))
    socket = next(
        (entry for entry in updated["crystal_sockets"] if entry["socket_id"] == socket_id),
        None,
    )
    if socket is None:
        raise RuleError(f"Unknown crystal socket: {socket_id}")
    if socket.get("crystal") is None:
        raise RuleError(f"Crystal socket is empty: {socket_id}")
    if socket.get("locked", False):
        raise RuleError(f"Crystal fusion is permanent without a destructive removal system: {socket_id}")

    socket["crystal"] = None
    socket.pop("integration", None)
    socket["locked"] = False
    return updated


def crystal_effect_output(
    item: Mapping[str, Any],
    socket_id: str,
    effect_id: str,
) -> Dict[str, Any]:
    """Explain effective crystal output after material and craft-quality losses."""
    errors = validate_equipment_instance(item)
    if errors:
        raise RuleError("Invalid equipment instance:\n- " + "\n- ".join(errors))
    if not _stable_id(socket_id):
        raise RuleError("socket_id must be a stable uppercase ID")
    if not _stable_id(effect_id):
        raise RuleError("effect_id must be a stable uppercase ID")

    socket = next(
        (entry for entry in item["crystal_sockets"] if entry["socket_id"] == socket_id),
        None,
    )
    if socket is None:
        raise RuleError(f"Unknown crystal socket: {socket_id}")
    crystal = socket.get("crystal")
    if crystal is None:
        raise RuleError(f"Crystal socket is empty: {socket_id}")

    effects = crystal.get("effects", {})
    if effect_id not in effects:
        raise RuleError(f"Crystal does not provide effect: {effect_id}")

    base_value = float(effects[effect_id])
    purity = float(crystal["purity"])
    stability = float(crystal["stability"])
    harvest_integrity = float(crystal["harvest_integrity"])
    forge_quality = float(item["forge_quality"])
    integration_quality = float(socket["integration"]["quality"])

    material_factor = (purity + stability + harvest_integrity) / 300.0
    craft_factor = (forge_quality + integration_quality) / 200.0
    total = round(base_value * material_factor * craft_factor, 4)

    return {
        "effect_id": effect_id,
        "base_value": base_value,
        "purity": purity,
        "stability": stability,
        "harvest_integrity": harvest_integrity,
        "forge_quality": forge_quality,
        "integration_quality": integration_quality,
        "material_factor": round(material_factor, 4),
        "craft_factor": round(craft_factor, 4),
        "total": total,
    }
