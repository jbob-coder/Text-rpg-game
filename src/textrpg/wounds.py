from __future__ import annotations

from math import isfinite
from typing import Any, Dict, Iterable, Mapping, MutableMapping

from .core import RuleError


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


def validate_wound_profiles(
    profiles: Mapping[str, Mapping[str, Any]],
) -> None:
    if not isinstance(profiles, Mapping):
        raise RuleError("wound profiles must be an object")

    for zone_id, profile in profiles.items():
        _string(zone_id, "wound profile zone ID")
        if not isinstance(profile, Mapping):
            raise RuleError(f"Wound profile must be an object: {zone_id}")

        thresholds = profile.get("thresholds", [])
        if not isinstance(thresholds, list):
            raise RuleError(f"{zone_id}.thresholds must be a list")

        previous = 1.0000001
        for index, threshold in enumerate(thresholds):
            if not isinstance(threshold, Mapping):
                raise RuleError(
                    f"{zone_id}.thresholds[{index}] must be an object"
                )
            limit = _finite(
                threshold.get("integrity_lte"),
                f"{zone_id}.thresholds[{index}].integrity_lte",
                minimum=0.0,
                maximum=1.0,
            )
            if limit >= previous:
                raise RuleError(
                    f"{zone_id}.thresholds must be ordered from highest to lowest integrity"
                )
            previous = limit
            _string_list(
                threshold.get("tags", []),
                f"{zone_id}.thresholds[{index}].tags",
            )
            _string_list(
                threshold.get("disabled_actions", []),
                f"{zone_id}.thresholds[{index}].disabled_actions",
            )

        crystal_multiplier = profile.get("crystal_damage_multiplier", 0.0)
        _finite(
            crystal_multiplier,
            f"{zone_id}.crystal_damage_multiplier",
            minimum=0.0,
        )


def validate_body_runtime_state(
    body_state: Mapping[str, Mapping[str, Any]],
) -> None:
    if not isinstance(body_state, Mapping):
        raise RuleError("body_state must be an object")

    for zone_id, record in body_state.items():
        _string(zone_id, "body_state zone ID")
        if not isinstance(record, Mapping):
            raise RuleError(f"Body zone runtime state must be an object: {zone_id}")
        _finite(
            record.get("integrity", 1.0),
            f"{zone_id}.integrity",
            minimum=0.0,
            maximum=1.0,
        )
        _string_list(record.get("tags", []), f"{zone_id}.tags")
        _string_list(
            record.get("disabled_actions", []),
            f"{zone_id}.disabled_actions",
        )


def consequence_state_for_integrity(
    zone_id: str,
    integrity: float,
    profiles: Mapping[str, Mapping[str, Any]],
) -> Dict[str, Any]:
    validate_wound_profiles(profiles)
    zone_id = _string(zone_id, "zone_id")
    integrity = _finite(integrity, "integrity", minimum=0.0, maximum=1.0)

    profile = profiles.get(zone_id)
    if profile is None:
        return {
            "zone_id": zone_id,
            "integrity": integrity,
            "tags": [],
            "disabled_actions": [],
        }

    active_tags: list[str] = []
    disabled_actions: list[str] = []
    for threshold in profile.get("thresholds", []):
        if integrity <= float(threshold["integrity_lte"]):
            for tag in threshold.get("tags", []):
                if tag not in active_tags:
                    active_tags.append(tag)
            for action in threshold.get("disabled_actions", []):
                if action not in disabled_actions:
                    disabled_actions.append(action)

    return {
        "zone_id": zone_id,
        "integrity": integrity,
        "tags": active_tags,
        "disabled_actions": disabled_actions,
    }


def apply_zone_damage(
    body_state: MutableMapping[str, Any],
    *,
    zone_id: str,
    damage_fraction: float,
    profiles: Mapping[str, Mapping[str, Any]],
) -> Dict[str, Any]:
    """Apply normalized structural damage to one body zone atomically."""
    if not isinstance(body_state, MutableMapping):
        raise RuleError("body_state must be mutable")
    validate_body_runtime_state(body_state)
    validate_wound_profiles(profiles)

    zone_id = _string(zone_id, "zone_id")
    if zone_id not in body_state:
        raise RuleError(f"Unknown body runtime zone: {zone_id}")
    damage_fraction = _finite(
        damage_fraction,
        "damage_fraction",
        minimum=0.0,
        maximum=1.0,
    )

    record = body_state[zone_id]
    if not isinstance(record, MutableMapping):
        raise RuleError(f"Body runtime zone must be mutable: {zone_id}")

    before = _finite(
        record.get("integrity", 1.0),
        f"{zone_id}.integrity",
        minimum=0.0,
        maximum=1.0,
    )
    after = round(max(0.0, before - damage_fraction), 4)
    consequence = consequence_state_for_integrity(zone_id, after, profiles)

    record["integrity"] = after
    record["tags"] = list(consequence["tags"])
    record["disabled_actions"] = list(consequence["disabled_actions"])

    return {
        "zone_id": zone_id,
        "before_integrity": before,
        "damage_fraction": damage_fraction,
        "after_integrity": after,
        "tags": list(consequence["tags"]),
        "disabled_actions": list(consequence["disabled_actions"]),
    }


def aggregate_body_impairments(
    body_state: Mapping[str, Mapping[str, Any]],
) -> Dict[str, list[str]]:
    validate_body_runtime_state(body_state)
    tags: list[str] = []
    disabled_actions: list[str] = []

    for record in body_state.values():
        for tag in record.get("tags", []):
            if tag not in tags:
                tags.append(tag)
        for action in record.get("disabled_actions", []):
            if action not in disabled_actions:
                disabled_actions.append(action)

    return {
        "tags": tags,
        "disabled_actions": disabled_actions,
    }


def crystal_harvest_damage_from_zone_hit(
    *,
    zone_id: str,
    damage_fraction: float,
    profiles: Mapping[str, Mapping[str, Any]],
) -> float:
    """Translate direct core-zone structural damage into harvest damage.

    A zero multiplier means the zone does not threaten a crystal. This keeps
    combat damage and loot damage related without requiring them to be identical.
    """
    validate_wound_profiles(profiles)
    zone_id = _string(zone_id, "zone_id")
    damage_fraction = _finite(
        damage_fraction,
        "damage_fraction",
        minimum=0.0,
        maximum=1.0,
    )
    profile = profiles.get(zone_id, {})
    multiplier = _finite(
        profile.get("crystal_damage_multiplier", 0.0),
        f"{zone_id}.crystal_damage_multiplier",
        minimum=0.0,
    )
    return round(min(1.0, damage_fraction * multiplier), 4)
