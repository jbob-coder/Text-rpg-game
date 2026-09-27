from __future__ import annotations

from math import isfinite
from typing import Any, Dict, Iterable, Mapping

from .combat import RANGE_BANDS
from .core import RuleError


WEAPON_FAMILIES = (
    "sword",
    "dagger",
    "axe",
    "hammer",
    "mace",
    "spear",
    "polearm",
    "staff",
    "bow",
    "crossbow",
    "shield",
    "improvised",
)
DAMAGE_TYPES = ("cutting", "piercing", "blunt")


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


def validate_weapon_definition(definition: Mapping[str, Any]) -> None:
    if not isinstance(definition, Mapping):
        raise RuleError("weapon definition must be an object")

    weapon_id = _string(definition.get("weapon_id"), "weapon.weapon_id")
    _string(
        definition.get("name", weapon_id.replace("_", " ").title()),
        f"{weapon_id}.name",
    )

    family = definition.get("family")
    if family not in WEAPON_FAMILIES:
        raise RuleError(f"Unsupported weapon family: {family}")

    range_bands = _string_list(definition.get("range_bands"), f"{weapon_id}.range_bands")
    if not range_bands:
        raise RuleError(f"{weapon_id}.range_bands must not be empty")
    unknown_ranges = set(range_bands).difference(RANGE_BANDS)
    if unknown_ranges:
        raise RuleError(
            f"{weapon_id}.range_bands contains unsupported values: {sorted(unknown_ranges)}"
        )

    _finite(definition.get("weight"), f"{weapon_id}.weight", minimum=0.0000001)
    _finite(definition.get("reach"), f"{weapon_id}.reach", minimum=0.0)
    _finite(
        definition.get("handling"),
        f"{weapon_id}.handling",
        minimum=0.0,
        maximum=100.0,
    )
    _finite(
        definition.get("balance"),
        f"{weapon_id}.balance",
        minimum=0.0,
        maximum=1.0,
    )
    _finite(definition.get("momentum"), f"{weapon_id}.momentum", minimum=0.0)
    _finite(definition.get("guard"), f"{weapon_id}.guard", minimum=0.0)
    _finite(definition.get("penetration"), f"{weapon_id}.penetration", minimum=0.0)
    _finite(
        definition.get("recovery"),
        f"{weapon_id}.recovery",
        minimum=0.0,
    )
    _finite(
        definition.get("stamina_burden"),
        f"{weapon_id}.stamina_burden",
        minimum=0.0,
    )

    max_durability = definition.get("max_durability")
    if (
        isinstance(max_durability, bool)
        or not isinstance(max_durability, int)
        or max_durability < 1
    ):
        raise RuleError(f"{weapon_id}.max_durability must be an integer >= 1")

    socket_count = definition.get("crystal_socket_count", 0)
    if isinstance(socket_count, bool) or not isinstance(socket_count, int) or socket_count < 0:
        raise RuleError(
            f"{weapon_id}.crystal_socket_count must be a non-negative integer"
        )

    damage_profile = definition.get("damage_profile")
    if not isinstance(damage_profile, Mapping):
        raise RuleError(f"{weapon_id}.damage_profile must be an object")

    total_profile = 0.0
    for damage_type, value in damage_profile.items():
        if damage_type not in DAMAGE_TYPES:
            raise RuleError(f"Unsupported weapon damage type: {damage_type}")
        total_profile += _finite(
            value,
            f"{weapon_id}.damage_profile.{damage_type}",
            minimum=0.0,
        )
    if total_profile <= 0:
        raise RuleError(f"{weapon_id}.damage_profile must contain positive damage")

    _string_list(
        definition.get("targeting_tags", []),
        f"{weapon_id}.targeting_tags",
    )
    _string_list(
        definition.get("armor_interaction_tags", []),
        f"{weapon_id}.armor_interaction_tags",
    )
    _string_list(
        definition.get("allowed_crystal_tags", []),
        f"{weapon_id}.allowed_crystal_tags",
    )

    visible = definition.get("player_visible", True)
    if not isinstance(visible, bool):
        raise RuleError(f"{weapon_id}.player_visible must be boolean")


def validate_weapon_instance(
    instance: Mapping[str, Any],
    definitions: Mapping[str, Mapping[str, Any]],
) -> None:
    if not isinstance(instance, Mapping):
        raise RuleError("weapon instance must be an object")
    if not isinstance(definitions, Mapping):
        raise RuleError("weapon definitions must be an object")

    instance_id = _string(instance.get("instance_id"), "weapon instance_id")
    weapon_id = _string(instance.get("weapon_id"), f"{instance_id}.weapon_id")
    if weapon_id not in definitions:
        raise RuleError(f"Unknown weapon definition: {weapon_id}")
    validate_weapon_definition(definitions[weapon_id])

    _string(instance.get("material_id"), f"{instance_id}.material_id")
    _finite(
        instance.get("forge_quality", 0.5),
        f"{instance_id}.forge_quality",
        minimum=0.0,
        maximum=1.0,
    )
    _finite(
        instance.get("condition", 1.0),
        f"{instance_id}.condition",
        minimum=0.0,
        maximum=1.0,
    )

    durability = instance.get("durability", definitions[weapon_id]["max_durability"])
    if isinstance(durability, bool) or not isinstance(durability, int) or durability < 0:
        raise RuleError(f"{instance_id}.durability must be a non-negative integer")
    if durability > definitions[weapon_id]["max_durability"]:
        raise RuleError(f"{instance_id}.durability exceeds weapon max_durability")

    crystal_ids = _string_list(
        instance.get("integrated_crystal_ids", []),
        f"{instance_id}.integrated_crystal_ids",
    )
    if len(crystal_ids) > definitions[weapon_id].get("crystal_socket_count", 0):
        raise RuleError(f"{instance_id} exceeds crystal socket capacity")

    provenance = instance.get("provenance", {})
    if not isinstance(provenance, Mapping):
        raise RuleError(f"{instance_id}.provenance must be an object")


def weapon_targeting_contract(
    definition: Mapping[str, Any],
) -> Dict[str, Any]:
    """Return the subset consumed by textrpg.combat targeting rules."""
    validate_weapon_definition(definition)
    return {
        "weapon_id": definition["weapon_id"],
        "range_bands": list(definition["range_bands"]),
        "targeting_tags": list(definition.get("targeting_tags", [])),
    }


def weapon_player_view(
    instance: Mapping[str, Any],
    definitions: Mapping[str, Mapping[str, Any]],
) -> Dict[str, Any]:
    """Build a player-safe weapon view without exposing internal tuning metadata."""
    validate_weapon_instance(instance, definitions)
    definition = definitions[instance["weapon_id"]]
    if definition.get("player_visible", True) is False:
        return {
            "instance_id": instance["instance_id"],
            "name": "Unknown Weapon",
        }

    return {
        "instance_id": instance["instance_id"],
        "weapon_id": instance["weapon_id"],
        "name": definition.get(
            "name",
            instance["weapon_id"].replace("_", " ").title(),
        ),
        "family": definition["family"],
        "material_id": instance["material_id"],
        "forge_quality": float(instance.get("forge_quality", 0.5)),
        "condition": float(instance.get("condition", 1.0)),
        "durability": int(
            instance.get("durability", definition["max_durability"])
        ),
        "max_durability": int(definition["max_durability"]),
        "weight": float(definition["weight"]),
        "reach": float(definition["reach"]),
        "handling": float(definition["handling"]),
        "balance": float(definition["balance"]),
        "momentum": float(definition["momentum"]),
        "guard": float(definition["guard"]),
        "penetration": float(definition["penetration"]),
        "recovery": float(definition["recovery"]),
        "stamina_burden": float(definition["stamina_burden"]),
        "range_bands": list(definition["range_bands"]),
        "damage_profile": {
            key: float(value)
            for key, value in definition["damage_profile"].items()
        },
        "armor_interaction_tags": list(
            definition.get("armor_interaction_tags", [])
        ),
        "integrated_crystal_ids": list(
            instance.get("integrated_crystal_ids", [])
        ),
        "crystal_socket_count": int(
            definition.get("crystal_socket_count", 0)
        ),
    }
