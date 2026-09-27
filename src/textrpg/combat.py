from __future__ import annotations

from math import isfinite
from typing import Any, Dict, Iterable, Mapping, Sequence

from .core import RuleError


RANGE_BANDS = ("grapple", "close", "reach", "ranged")
FACINGS = ("front", "left_flank", "right_flank", "rear")
ELEVATION_RELATIONS = ("lower", "level", "higher")
POSTURES = (
    "standing",
    "crouched",
    "prone",
    "grounded",
    "airborne",
    "climbing",
    "pinned",
)


def _non_empty_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise RuleError(f"{label} must be a non-empty string")
    return value


def _string_set(value: Any, label: str) -> set[str]:
    if value is None:
        return set()
    if isinstance(value, (str, bytes)) or not isinstance(value, Iterable):
        raise RuleError(f"{label} must be a list of non-empty strings")
    result = set(value)
    if not all(isinstance(item, str) and item for item in result):
        raise RuleError(f"{label} must be a list of non-empty strings")
    return result


def _enum_set(
    value: Any,
    label: str,
    allowed: Sequence[str],
    *,
    default_all: bool = False,
) -> set[str]:
    if value is None:
        return set(allowed) if default_all else set()
    result = _string_set(value, label)
    unknown = result.difference(allowed)
    if unknown:
        raise RuleError(f"{label} contains unsupported values: {sorted(unknown)}")
    return result


def _finite_number(value: Any, label: str) -> float:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not isfinite(float(value))
    ):
        raise RuleError(f"{label} must be a finite number")
    return float(value)


def validate_combat_state(combat_state: Mapping[str, Any]) -> None:
    if not isinstance(combat_state, Mapping):
        raise RuleError("combat_state must be an object")

    range_band = combat_state.get("range_band")
    if range_band not in RANGE_BANDS:
        raise RuleError(f"Unsupported combat range_band: {range_band}")

    facing = combat_state.get("relative_facing")
    if facing not in FACINGS:
        raise RuleError(f"Unsupported combat relative_facing: {facing}")

    elevation = combat_state.get("relative_elevation", "level")
    if elevation not in ELEVATION_RELATIONS:
        raise RuleError(f"Unsupported combat relative_elevation: {elevation}")

    posture = combat_state.get("defender_posture", "standing")
    if posture not in POSTURES:
        raise RuleError(f"Unsupported combat defender_posture: {posture}")

    _string_set(combat_state.get("state_tags", []), "combat_state.state_tags")
    _string_set(combat_state.get("blocked_zones", []), "combat_state.blocked_zones")

    distance = combat_state.get("distance")
    if distance is not None:
        _finite_number(distance, "combat_state.distance")


def validate_weapon_targeting(weapon: Mapping[str, Any]) -> None:
    if not isinstance(weapon, Mapping):
        raise RuleError("weapon must be an object")

    weapon_id = weapon.get("weapon_id", weapon.get("item_id"))
    _non_empty_string(weapon_id, "weapon.weapon_id")

    _enum_set(
        weapon.get("range_bands"),
        "weapon.range_bands",
        RANGE_BANDS,
    )
    _string_set(weapon.get("targeting_tags", []), "weapon.targeting_tags")


def validate_body_zone_definitions(
    body_zones: Mapping[str, Mapping[str, Any]],
) -> None:
    if not isinstance(body_zones, Mapping) or not body_zones:
        raise RuleError("body_zones must be a non-empty object")

    for zone_id, definition in body_zones.items():
        _non_empty_string(zone_id, "body zone ID")
        if not isinstance(definition, Mapping):
            raise RuleError(f"Body zone definition must be an object: {zone_id}")

        name = definition.get("name", zone_id.replace("_", " ").title())
        _non_empty_string(name, f"body zone name: {zone_id}")

        _enum_set(
            definition.get("allowed_facings"),
            f"{zone_id}.allowed_facings",
            FACINGS,
            default_all=True,
        )
        _enum_set(
            definition.get("allowed_range_bands"),
            f"{zone_id}.allowed_range_bands",
            RANGE_BANDS,
            default_all=True,
        )
        _enum_set(
            definition.get("allowed_elevation_relations"),
            f"{zone_id}.allowed_elevation_relations",
            ELEVATION_RELATIONS,
            default_all=True,
        )
        _enum_set(
            definition.get("allowed_postures"),
            f"{zone_id}.allowed_postures",
            POSTURES,
            default_all=True,
        )
        _string_set(
            definition.get("requires_all_state_tags", []),
            f"{zone_id}.requires_all_state_tags",
        )
        _string_set(
            definition.get("requires_any_state_tags", []),
            f"{zone_id}.requires_any_state_tags",
        )
        _string_set(
            definition.get("blocked_state_tags", []),
            f"{zone_id}.blocked_state_tags",
        )
        _string_set(
            definition.get("required_weapon_tags", []),
            f"{zone_id}.required_weapon_tags",
        )
        _string_set(
            definition.get("forbidden_weapon_tags", []),
            f"{zone_id}.forbidden_weapon_tags",
        )

        visible = definition.get("player_visible", True)
        if not isinstance(visible, bool):
            raise RuleError(f"{zone_id}.player_visible must be boolean")


def _zone_access_reason(
    combat_state: Mapping[str, Any],
    weapon: Mapping[str, Any],
    zone_id: str,
    definition: Mapping[str, Any],
) -> tuple[bool, str | None]:
    range_band = combat_state["range_band"]
    facing = combat_state["relative_facing"]
    elevation = combat_state.get("relative_elevation", "level")
    posture = combat_state.get("defender_posture", "standing")
    state_tags = _string_set(combat_state.get("state_tags", []), "combat_state.state_tags")
    blocked_zones = _string_set(
        combat_state.get("blocked_zones", []),
        "combat_state.blocked_zones",
    )
    weapon_ranges = _enum_set(
        weapon.get("range_bands"),
        "weapon.range_bands",
        RANGE_BANDS,
    )
    weapon_tags = _string_set(weapon.get("targeting_tags", []), "weapon.targeting_tags")

    if range_band not in weapon_ranges:
        return False, "weapon_out_of_range"
    if zone_id in blocked_zones:
        return False, "zone_blocked"

    allowed_facings = _enum_set(
        definition.get("allowed_facings"),
        f"{zone_id}.allowed_facings",
        FACINGS,
        default_all=True,
    )
    if facing not in allowed_facings:
        return False, "facing"

    allowed_ranges = _enum_set(
        definition.get("allowed_range_bands"),
        f"{zone_id}.allowed_range_bands",
        RANGE_BANDS,
        default_all=True,
    )
    if range_band not in allowed_ranges:
        return False, "range"

    allowed_elevation = _enum_set(
        definition.get("allowed_elevation_relations"),
        f"{zone_id}.allowed_elevation_relations",
        ELEVATION_RELATIONS,
        default_all=True,
    )
    if elevation not in allowed_elevation:
        return False, "elevation"

    allowed_postures = _enum_set(
        definition.get("allowed_postures"),
        f"{zone_id}.allowed_postures",
        POSTURES,
        default_all=True,
    )
    if posture not in allowed_postures:
        return False, "posture"

    requires_all = _string_set(
        definition.get("requires_all_state_tags", []),
        f"{zone_id}.requires_all_state_tags",
    )
    if not requires_all.issubset(state_tags):
        return False, "missing_state_requirement"

    requires_any = _string_set(
        definition.get("requires_any_state_tags", []),
        f"{zone_id}.requires_any_state_tags",
    )
    if requires_any and not requires_any.intersection(state_tags):
        return False, "missing_state_alternative"

    blocked_tags = _string_set(
        definition.get("blocked_state_tags", []),
        f"{zone_id}.blocked_state_tags",
    )
    if blocked_tags.intersection(state_tags):
        return False, "state_blocked"

    required_weapon = _string_set(
        definition.get("required_weapon_tags", []),
        f"{zone_id}.required_weapon_tags",
    )
    if not required_weapon.issubset(weapon_tags):
        return False, "weapon_requirement"

    forbidden_weapon = _string_set(
        definition.get("forbidden_weapon_tags", []),
        f"{zone_id}.forbidden_weapon_tags",
    )
    if forbidden_weapon.intersection(weapon_tags):
        return False, "weapon_forbidden"

    return True, None


def reachable_target_zone_ids(
    combat_state: Mapping[str, Any],
    weapon: Mapping[str, Any],
    body_zones: Mapping[str, Mapping[str, Any]],
) -> list[str]:
    """Return only zones currently reachable under authoritative combat geometry.

    The function is deterministic and non-mutating. It intentionally does not
    calculate damage or reveal hidden anatomy/weakness data.
    """
    validate_combat_state(combat_state)
    validate_weapon_targeting(weapon)
    validate_body_zone_definitions(body_zones)

    output: list[str] = []
    for zone_id, definition in body_zones.items():
        accessible, _ = _zone_access_reason(
            combat_state,
            weapon,
            zone_id,
            definition,
        )
        if accessible:
            output.append(zone_id)
    return output


def explain_target_zone_access(
    combat_state: Mapping[str, Any],
    weapon: Mapping[str, Any],
    body_zones: Mapping[str, Mapping[str, Any]],
    zone_id: str,
) -> Dict[str, Any]:
    """Rules/debug explanation; not a player-facing projection."""
    validate_combat_state(combat_state)
    validate_weapon_targeting(weapon)
    validate_body_zone_definitions(body_zones)
    _non_empty_string(zone_id, "zone_id")
    if zone_id not in body_zones:
        raise RuleError(f"Unknown body zone: {zone_id}")

    accessible, reason = _zone_access_reason(
        combat_state,
        weapon,
        zone_id,
        body_zones[zone_id],
    )
    return {
        "zone_id": zone_id,
        "reachable": accessible,
        "blocked_reason": reason,
    }


def build_targeting_view(
    combat_state: Mapping[str, Any],
    weapon: Mapping[str, Any],
    body_zones: Mapping[str, Mapping[str, Any]],
) -> Dict[str, Any]:
    """Build a player-safe targeting projection.

    Only currently reachable, player-visible zones are returned. Internal
    weakness/effect metadata and inaccessible anatomy are not exposed.
    """
    reachable = set(reachable_target_zone_ids(combat_state, weapon, body_zones))
    zones: list[Dict[str, Any]] = []

    for zone_id, definition in body_zones.items():
        if zone_id not in reachable:
            continue
        if definition.get("player_visible", True) is False:
            continue

        zone_view: Dict[str, Any] = {
            "id": zone_id,
            "name": definition.get("name", zone_id.replace("_", " ").title()),
        }
        description = definition.get("description")
        if description is not None:
            zone_view["description"] = _non_empty_string(
                description,
                f"{zone_id}.description",
            )
        zones.append(zone_view)

    weapon_id = weapon.get("weapon_id", weapon.get("item_id"))
    return {
        "range_band": combat_state["range_band"],
        "relative_facing": combat_state["relative_facing"],
        "relative_elevation": combat_state.get("relative_elevation", "level"),
        "defender_posture": combat_state.get("defender_posture", "standing"),
        "weapon_id": weapon_id,
        "target_zones": zones,
    }
