from __future__ import annotations

import re
from math import isfinite
from typing import Any, Dict, List, Mapping, Sequence

from .core import RuleError


_STABLE_ID = re.compile(r"^[A-Z][A-Z0-9_]*$")

WEAPON_FAMILIES = (
    "sword",
    "dagger",
    "axe",
    "hammer",
    "spear",
    "polearm",
    "staff",
    "bow",
    "crossbow",
    "shield",
    "improvised",
)
DAMAGE_TYPES = ("cut", "pierce", "blunt")
RANGE_BANDS = ("grapple", "close", "reach", "ranged")
FACINGS = ("front", "left_flank", "right_flank", "rear")
POSTURES = (
    "standing",
    "crouched",
    "prone",
    "airborne",
    "climbing",
    "grappled",
    "staggered",
)
ELEVATIONS = ("lower", "level", "higher")
CRYSTAL_SOURCE_TYPES = ("mine", "beast")
BEAST_ROLES = (
    "solitary",
    "pack_member",
    "veteran",
    "guardian",
    "chieftain",
    "commander",
    "territory_ruler",
    "regional_apex",
)


def _stable_id(value: Any) -> bool:
    return isinstance(value, str) and bool(_STABLE_ID.fullmatch(value))


def _finite_number(value: Any, *, minimum: float | None = None, maximum: float | None = None) -> bool:
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


def _validate_string_list(
    value: Any,
    *,
    label: str,
    allowed: Sequence[str] | None = None,
    allow_empty: bool = True,
) -> List[str]:
    errors: List[str] = []
    if not isinstance(value, list):
        return [f"{label} must be a list"]
    if not allow_empty and not value:
        errors.append(f"{label} must not be empty")
    allowed_set = set(allowed or ())
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item:
            errors.append(f"{label}[{index}] must be a non-empty string")
        elif allowed is not None and item not in allowed_set:
            errors.append(f"{label}[{index}] is unsupported: {item}")
    if len(value) != len(set(item for item in value if isinstance(item, str))):
        errors.append(f"{label} must not contain duplicates")
    return errors


def validate_weapon_definition(weapon_id: str, definition: Any) -> List[str]:
    errors: List[str] = []
    if not _stable_id(weapon_id):
        errors.append(f"weapon_id must be a stable uppercase ID: {weapon_id!r}")
    if not isinstance(definition, Mapping):
        return errors + [f"weapon {weapon_id!r} must be an object"]

    family = definition.get("family")
    if family not in WEAPON_FAMILIES:
        errors.append(f"weapon {weapon_id!r}.family is unsupported: {family!r}")

    errors.extend(
        _validate_string_list(
            definition.get("range_bands"),
            label=f"weapon {weapon_id!r}.range_bands",
            allowed=RANGE_BANDS,
            allow_empty=False,
        )
    )
    errors.extend(
        _validate_string_list(
            definition.get("target_tags", []),
            label=f"weapon {weapon_id!r}.target_tags",
        )
    )

    profile = definition.get("damage_profile")
    if not isinstance(profile, Mapping):
        errors.append(f"weapon {weapon_id!r}.damage_profile must be an object")
    else:
        positive = False
        for damage_type, amount in profile.items():
            if damage_type not in DAMAGE_TYPES:
                errors.append(
                    f"weapon {weapon_id!r}.damage_profile has unsupported type: {damage_type!r}"
                )
                continue
            if not _finite_number(amount, minimum=0.0):
                errors.append(
                    f"weapon {weapon_id!r}.damage_profile.{damage_type} must be finite non-negative numeric"
                )
            elif float(amount) > 0:
                positive = True
        if not positive:
            errors.append(f"weapon {weapon_id!r}.damage_profile must contain positive damage")

    for field_name in (
        "weight",
        "reach",
        "handling",
        "momentum",
        "guard",
        "recovery",
        "stamina_burden",
        "durability",
    ):
        if field_name in definition and not _finite_number(definition[field_name], minimum=0.0):
            errors.append(
                f"weapon {weapon_id!r}.{field_name} must be finite non-negative numeric"
            )
    return errors


def validate_crystal_instance(instance: Any) -> List[str]:
    if not isinstance(instance, Mapping):
        return ["crystal instance must be an object"]

    errors: List[str] = []
    for field_name in ("instance_id", "crystal_id"):
        if not _stable_id(instance.get(field_name)):
            errors.append(f"crystal.{field_name} must be a stable uppercase ID")

    source_type = instance.get("source_type")
    if source_type not in CRYSTAL_SOURCE_TYPES:
        errors.append(f"crystal.source_type is unsupported: {source_type!r}")

    grade = instance.get("grade")
    if isinstance(grade, bool) or not isinstance(grade, int) or grade < 1:
        errors.append("crystal.grade must be an integer >= 1")

    for field_name in ("purity", "stability", "harvest_integrity"):
        if not _finite_number(instance.get(field_name), minimum=0.0, maximum=100.0):
            errors.append(f"crystal.{field_name} must be finite numeric in range 0..100")

    if not _finite_number(instance.get("size"), minimum=0.000001):
        errors.append("crystal.size must be finite numeric > 0")

    if source_type == "beast" and not _stable_id(instance.get("source_beast_id")):
        errors.append("beast crystal requires stable source_beast_id")
    if source_type == "mine" and not _stable_id(instance.get("source_location_id")):
        errors.append("mine crystal requires stable source_location_id")

    errors.extend(
        _validate_string_list(
            instance.get("resonance_tags", []),
            label="crystal.resonance_tags",
        )
    )
    return errors


def validate_body_zone_definition(zone_id: str, definition: Any) -> List[str]:
    errors: List[str] = []
    if not _stable_id(zone_id):
        errors.append(f"zone_id must be a stable uppercase ID: {zone_id!r}")
    if not isinstance(definition, Mapping):
        return errors + [f"body zone {zone_id!r} must be an object"]

    label = definition.get("label")
    if not isinstance(label, str) or not label:
        errors.append(f"body zone {zone_id!r}.label must be a non-empty string")

    errors.extend(
        _validate_string_list(
            definition.get("facings"),
            label=f"body zone {zone_id!r}.facings",
            allowed=FACINGS,
            allow_empty=False,
        )
    )
    errors.extend(
        _validate_string_list(
            definition.get("range_bands"),
            label=f"body zone {zone_id!r}.range_bands",
            allowed=RANGE_BANDS,
            allow_empty=False,
        )
    )
    errors.extend(
        _validate_string_list(
            definition.get("tags", []),
            label=f"body zone {zone_id!r}.tags",
        )
    )
    errors.extend(
        _validate_string_list(
            definition.get("requires_exposure_tags", []),
            label=f"body zone {zone_id!r}.requires_exposure_tags",
        )
    )

    for field_name, allowed in (
        ("attacker_postures", POSTURES),
        ("defender_postures", POSTURES),
        ("elevations", ELEVATIONS),
    ):
        if field_name in definition:
            errors.extend(
                _validate_string_list(
                    definition[field_name],
                    label=f"body zone {zone_id!r}.{field_name}",
                    allowed=allowed,
                    allow_empty=False,
                )
            )

    for field_name in ("vital", "crystal_risk"):
        if field_name in definition and not isinstance(definition[field_name], bool):
            errors.append(f"body zone {zone_id!r}.{field_name} must be boolean")
    return errors


def validate_combat_state(state: Any) -> List[str]:
    if not isinstance(state, Mapping):
        return ["combat state must be an object"]
    errors: List[str] = []
    if state.get("facing") not in FACINGS:
        errors.append(f"combat.facing is unsupported: {state.get('facing')!r}")
    if state.get("range_band") not in RANGE_BANDS:
        errors.append(f"combat.range_band is unsupported: {state.get('range_band')!r}")
    if state.get("attacker_posture") not in POSTURES:
        errors.append(f"combat.attacker_posture is unsupported: {state.get('attacker_posture')!r}")
    if state.get("defender_posture") not in POSTURES:
        errors.append(f"combat.defender_posture is unsupported: {state.get('defender_posture')!r}")
    if state.get("elevation") not in ELEVATIONS:
        errors.append(f"combat.elevation is unsupported: {state.get('elevation')!r}")
    errors.extend(_validate_string_list(state.get("exposure_tags", []), label="combat.exposure_tags"))
    errors.extend(_validate_string_list(state.get("blocked_zones", []), label="combat.blocked_zones"))
    for zone_id in state.get("blocked_zones", []) if isinstance(state.get("blocked_zones", []), list) else []:
        if isinstance(zone_id, str) and not _stable_id(zone_id):
            errors.append(f"combat.blocked_zones contains invalid stable ID: {zone_id!r}")
    return errors


def reachable_target_zones(
    combat_state: Mapping[str, Any],
    body_zones: Mapping[str, Mapping[str, Any]],
    weapon_definition: Mapping[str, Any],
) -> List[str]:
    """Return only zones reachable from the current authoritative combat state."""
    errors = validate_combat_state(combat_state)
    errors.extend(validate_weapon_definition("WEAPON_RUNTIME", weapon_definition))
    if not isinstance(body_zones, Mapping):
        errors.append("body_zones must be an object")
    else:
        for zone_id, definition in body_zones.items():
            errors.extend(validate_body_zone_definition(zone_id, definition))
    if errors:
        raise RuleError("Invalid targeting contract:\n- " + "\n- ".join(errors))

    facing = combat_state["facing"]
    range_band = combat_state["range_band"]
    attacker_posture = combat_state["attacker_posture"]
    defender_posture = combat_state["defender_posture"]
    elevation = combat_state["elevation"]
    exposures = set(combat_state.get("exposure_tags", []))
    blocked = set(combat_state.get("blocked_zones", []))
    weapon_ranges = set(weapon_definition["range_bands"])
    weapon_tags = set(weapon_definition.get("target_tags", []))

    if range_band not in weapon_ranges:
        return []

    available: List[str] = []
    for zone_id, zone in body_zones.items():
        if zone_id in blocked:
            continue
        if facing not in zone["facings"]:
            continue
        if range_band not in zone["range_bands"]:
            continue
        if "attacker_postures" in zone and attacker_posture not in zone["attacker_postures"]:
            continue
        if "defender_postures" in zone and defender_posture not in zone["defender_postures"]:
            continue
        if "elevations" in zone and elevation not in zone["elevations"]:
            continue
        required_exposures = set(zone.get("requires_exposure_tags", []))
        if not required_exposures.issubset(exposures):
            continue
        zone_tags = set(zone.get("tags", []))
        if weapon_tags and "*" not in weapon_tags and not weapon_tags.intersection(zone_tags):
            continue
        available.append(zone_id)
    return available


def build_targeting_view(
    combat_state: Mapping[str, Any],
    body_zones: Mapping[str, Mapping[str, Any]],
    weapon_definition: Mapping[str, Any],
) -> Dict[str, Any]:
    """Player-safe target projection; authored access rules never leave the rules layer."""
    zone_ids = reachable_target_zones(combat_state, body_zones, weapon_definition)
    return {
        "facing": combat_state["facing"],
        "range_band": combat_state["range_band"],
        "targets": [
            {
                "zone_id": zone_id,
                "label": body_zones[zone_id]["label"],
            }
            for zone_id in zone_ids
        ],
    }


def validate_beast_runtime_state(state: Any) -> List[str]:
    if not isinstance(state, Mapping):
        return ["beast state must be an object"]
    errors: List[str] = []
    for field_name in ("beast_id", "species_id"):
        if not _stable_id(state.get(field_name)):
            errors.append(f"beast.{field_name} must be a stable uppercase ID")

    level = state.get("level")
    if isinstance(level, bool) or not isinstance(level, int) or level < 1:
        errors.append("beast.level must be an integer >= 1")
    if not _finite_number(state.get("development_xp"), minimum=0.0):
        errors.append("beast.development_xp must be finite non-negative numeric")

    intelligence = state.get("intelligence_tier")
    if isinstance(intelligence, bool) or not isinstance(intelligence, int) or not 0 <= intelligence <= 5:
        errors.append("beast.intelligence_tier must be an integer in range 0..5")

    role = state.get("role")
    if role not in BEAST_ROLES:
        errors.append(f"beast.role is unsupported: {role!r}")

    follower_count = state.get("follower_count", 0)
    if isinstance(follower_count, bool) or not isinstance(follower_count, int) or follower_count < 0:
        errors.append("beast.follower_count must be a non-negative integer")

    memories = state.get("memories", [])
    if not isinstance(memories, list) or not all(isinstance(memory, Mapping) for memory in memories):
        errors.append("beast.memories must be a list of objects")
    errors.extend(_validate_string_list(state.get("adaptations", []), label="beast.adaptations"))
    return errors


def beast_role_eligibility(
    beast_state: Mapping[str, Any],
    role_definition: Mapping[str, Any],
) -> Dict[str, Any]:
    """Evaluate an authored role gate; level by itself is never sufficient unless authored so."""
    errors = validate_beast_runtime_state(beast_state)
    if not isinstance(role_definition, Mapping):
        errors.append("role definition must be an object")
    if errors:
        raise RuleError("Invalid beast role contract:\n- " + "\n- ".join(errors))

    reasons: List[str] = []
    minimum_level = role_definition.get("min_level", 1)
    minimum_intelligence = role_definition.get("min_intelligence_tier", 0)
    minimum_followers = role_definition.get("min_followers", 0)
    territory_required = role_definition.get("territory_required", False)

    if isinstance(minimum_level, bool) or not isinstance(minimum_level, int) or minimum_level < 1:
        raise RuleError("role min_level must be an integer >= 1")
    if (
        isinstance(minimum_intelligence, bool)
        or not isinstance(minimum_intelligence, int)
        or not 0 <= minimum_intelligence <= 5
    ):
        raise RuleError("role min_intelligence_tier must be an integer in range 0..5")
    if isinstance(minimum_followers, bool) or not isinstance(minimum_followers, int) or minimum_followers < 0:
        raise RuleError("role min_followers must be a non-negative integer")
    if not isinstance(territory_required, bool):
        raise RuleError("role territory_required must be boolean")

    if beast_state["level"] < minimum_level:
        reasons.append("level")
    if beast_state["intelligence_tier"] < minimum_intelligence:
        reasons.append("intelligence")
    if beast_state.get("follower_count", 0) < minimum_followers:
        reasons.append("followers")
    if territory_required and not _stable_id(beast_state.get("territory_id")):
        reasons.append("territory")

    return {"eligible": not reasons, "missing": reasons}
