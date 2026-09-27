from __future__ import annotations

from typing import Any, Dict, Mapping

from .core import RuleError
from .crystals import validate_crystal_instance
from .weapons import validate_weapon_definition, validate_weapon_instance


FORGE_STAGES = (
    "material_selection",
    "shaping",
    "finishing",
    "crystal_housing",
    "crystal_integration",
    "stabilization",
    "inspection",
    "complete",
)


def _string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise RuleError(f"{label} must be a non-empty string")
    return value


def crystal_weapon_compatibility(
    weapon_instance: Mapping[str, Any],
    weapon_definitions: Mapping[str, Mapping[str, Any]],
    crystal_instance: Mapping[str, Any],
    crystal_definitions: Mapping[str, Mapping[str, Any]],
) -> Dict[str, Any]:
    """Evaluate integration compatibility without mutating either item."""
    validate_weapon_instance(weapon_instance, weapon_definitions)
    validate_crystal_instance(crystal_instance, crystal_definitions)

    weapon_definition = weapon_definitions[weapon_instance["weapon_id"]]
    crystal_definition = crystal_definitions[crystal_instance["crystal_id"]]

    reasons: list[str] = []

    socket_count = int(weapon_definition.get("crystal_socket_count", 0))
    integrated = list(weapon_instance.get("integrated_crystal_ids", []))
    if len(integrated) >= socket_count:
        reasons.append("no_open_socket")

    if crystal_instance["instance_id"] in integrated:
        reasons.append("already_integrated")

    allowed_tags = set(weapon_definition.get("allowed_crystal_tags", []))
    crystal_tags = set(crystal_definition.get("tags", []))
    if allowed_tags and not allowed_tags.intersection(crystal_tags):
        reasons.append("incompatible_crystal_tags")

    minimum_stability = weapon_definition.get("min_crystal_stability", 0.0)
    if isinstance(minimum_stability, bool) or not isinstance(
        minimum_stability,
        (int, float),
    ):
        raise RuleError("weapon min_crystal_stability must be numeric")
    minimum_stability = float(minimum_stability)
    if minimum_stability < 0.0 or minimum_stability > 1.0:
        raise RuleError("weapon min_crystal_stability must be in range 0..1")

    stability = float(crystal_instance.get("stability", 1.0))
    if stability < minimum_stability:
        reasons.append("insufficient_crystal_stability")

    if float(crystal_instance.get("integrity", 1.0)) <= 0.0:
        reasons.append("crystal_destroyed")

    return {
        "compatible": not reasons,
        "reasons": reasons,
        "weapon_instance_id": weapon_instance["instance_id"],
        "crystal_instance_id": crystal_instance["instance_id"],
        "open_sockets": max(0, socket_count - len(integrated)),
    }


def preview_crystal_integration(
    weapon_instance: Mapping[str, Any],
    weapon_definitions: Mapping[str, Mapping[str, Any]],
    crystal_instance: Mapping[str, Any],
    crystal_definitions: Mapping[str, Mapping[str, Any]],
) -> Dict[str, Any]:
    """Return the prospective crystal list if compatibility succeeds."""
    compatibility = crystal_weapon_compatibility(
        weapon_instance,
        weapon_definitions,
        crystal_instance,
        crystal_definitions,
    )
    if not compatibility["compatible"]:
        return {
            **compatibility,
            "integrated_crystal_ids": list(
                weapon_instance.get("integrated_crystal_ids", [])
            ),
        }

    return {
        **compatibility,
        "integrated_crystal_ids": [
            *weapon_instance.get("integrated_crystal_ids", []),
            crystal_instance["instance_id"],
        ],
    }


def validate_forge_job(job: Mapping[str, Any]) -> None:
    """Validate a serializable staged forge-work record.

    The prototype does not commit equipment mutations. This contract exists so a
    later transaction can persist work-in-progress safely and resume it.
    """
    if not isinstance(job, Mapping):
        raise RuleError("forge job must be an object")

    job_id = _string(job.get("job_id"), "forge_job.job_id")
    _string(job.get("equipment_instance_id"), f"{job_id}.equipment_instance_id")

    current_stage = job.get("current_stage", FORGE_STAGES[0])
    if current_stage not in FORGE_STAGES:
        raise RuleError(f"Unsupported forge stage: {current_stage}")

    completed = job.get("completed_stages", [])
    if not isinstance(completed, list):
        raise RuleError(f"{job_id}.completed_stages must be a list")
    if not all(isinstance(stage, str) and stage for stage in completed):
        raise RuleError(f"{job_id}.completed_stages must contain non-empty strings")
    if len(set(completed)) != len(completed):
        raise RuleError(f"{job_id}.completed_stages must not contain duplicates")
    unknown = set(completed).difference(FORGE_STAGES)
    if unknown:
        raise RuleError(
            f"{job_id}.completed_stages contains unsupported stages: {sorted(unknown)}"
        )

    expected_prefix = list(FORGE_STAGES[: len(completed)])
    if completed != expected_prefix:
        raise RuleError(
            f"{job_id}.completed_stages must follow canonical forge-stage order"
        )

    expected_current_index = len(completed)
    if expected_current_index >= len(FORGE_STAGES):
        if current_stage != "complete":
            raise RuleError(f"{job_id} completed all stages but is not marked complete")
    elif current_stage != FORGE_STAGES[expected_current_index]:
        raise RuleError(
            f"{job_id}.current_stage does not follow completed_stages"
        )

    minutes_spent = job.get("minutes_spent", 0)
    if (
        isinstance(minutes_spent, bool)
        or not isinstance(minutes_spent, int)
        or minutes_spent < 0
    ):
        raise RuleError(f"{job_id}.minutes_spent must be a non-negative integer")

    quality_inputs = job.get("quality_inputs", {})
    if not isinstance(quality_inputs, Mapping):
        raise RuleError(f"{job_id}.quality_inputs must be an object")

    for key, value in quality_inputs.items():
        _string(key, f"{job_id}.quality_inputs key")
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or float(value) < 0.0
            or float(value) > 1.0
        ):
            raise RuleError(
                f"{job_id}.quality_inputs.{key} must be numeric in range 0..1"
            )
