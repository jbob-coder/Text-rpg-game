from __future__ import annotations

from math import isfinite
from typing import Any, Dict, Iterable, Mapping

from .core import RuleError
from .weapons import DAMAGE_TYPES


ARMOR_SLOTS = ("head", "body", "hands", "legs", "feet")


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


def validate_armor_definition(definition: Mapping[str, Any]) -> None:
    if not isinstance(definition, Mapping):
        raise RuleError("armor definition must be an object")

    armor_id = _string(definition.get("armor_id"), "armor.armor_id")
    _string(
        definition.get("name", armor_id.replace("_", " ").title()),
        f"{armor_id}.name",
    )

    slot = definition.get("slot")
    if slot not in ARMOR_SLOTS:
        raise RuleError(f"Unsupported armor slot: {slot}")

    covered_zones = _string_list(
        definition.get("covered_zones"),
        f"{armor_id}.covered_zones",
    )
    if not covered_zones:
        raise RuleError(f"{armor_id}.covered_zones must not be empty")

    _finite(definition.get("weight"), f"{armor_id}.weight", minimum=0.0000001)
    _finite(
        definition.get("flexibility"),
        f"{armor_id}.flexibility",
        minimum=0.0,
        maximum=1.0,
    )
    _finite(
        definition.get("noise"),
        f"{armor_id}.noise",
        minimum=0.0,
        maximum=1.0,
    )
    _finite(
        definition.get("fatigue_burden"),
        f"{armor_id}.fatigue_burden",
        minimum=0.0,
    )

    max_durability = definition.get("max_durability")
    if (
        isinstance(max_durability, bool)
        or not isinstance(max_durability, int)
        or max_durability < 1
    ):
        raise RuleError(f"{armor_id}.max_durability must be an integer >= 1")

    socket_count = definition.get("crystal_socket_count", 0)
    if isinstance(socket_count, bool) or not isinstance(socket_count, int) or socket_count < 0:
        raise RuleError(
            f"{armor_id}.crystal_socket_count must be a non-negative integer"
        )

    resistances = definition.get("resistances")
    if not isinstance(resistances, Mapping):
        raise RuleError(f"{armor_id}.resistances must be an object")
    for damage_type, value in resistances.items():
        if damage_type not in DAMAGE_TYPES:
            raise RuleError(f"Unsupported armor resistance type: {damage_type}")
        _finite(
            value,
            f"{armor_id}.resistances.{damage_type}",
            minimum=0.0,
        )

    _string_list(definition.get("tags", []), f"{armor_id}.tags")
    _string_list(
        definition.get("allowed_crystal_tags", []),
        f"{armor_id}.allowed_crystal_tags",
    )

    visible = definition.get("player_visible", True)
    if not isinstance(visible, bool):
        raise RuleError(f"{armor_id}.player_visible must be boolean")


def validate_armor_instance(
    instance: Mapping[str, Any],
    definitions: Mapping[str, Mapping[str, Any]],
) -> None:
    if not isinstance(instance, Mapping):
        raise RuleError("armor instance must be an object")
    if not isinstance(definitions, Mapping):
        raise RuleError("armor definitions must be an object")

    instance_id = _string(instance.get("instance_id"), "armor instance_id")
    armor_id = _string(instance.get("armor_id"), f"{instance_id}.armor_id")
    if armor_id not in definitions:
        raise RuleError(f"Unknown armor definition: {armor_id}")
    validate_armor_definition(definitions[armor_id])

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

    durability = instance.get("durability", definitions[armor_id]["max_durability"])
    if isinstance(durability, bool) or not isinstance(durability, int) or durability < 0:
        raise RuleError(f"{instance_id}.durability must be a non-negative integer")
    if durability > definitions[armor_id]["max_durability"]:
        raise RuleError(f"{instance_id}.durability exceeds armor max_durability")

    crystal_ids = _string_list(
        instance.get("integrated_crystal_ids", []),
        f"{instance_id}.integrated_crystal_ids",
    )
    if len(crystal_ids) > definitions[armor_id].get("crystal_socket_count", 0):
        raise RuleError(f"{instance_id} exceeds crystal socket capacity")

    provenance = instance.get("provenance", {})
    if not isinstance(provenance, Mapping):
        raise RuleError(f"{instance_id}.provenance must be an object")


def armor_layers_for_zone(
    equipped_armor: Mapping[str, Mapping[str, Any]],
    definitions: Mapping[str, Mapping[str, Any]],
    zone_id: str,
) -> list[Dict[str, Any]]:
    """Return protective layers covering a body zone without resolving damage."""
    if not isinstance(equipped_armor, Mapping):
        raise RuleError("equipped_armor must be an object")
    zone_id = _string(zone_id, "zone_id")

    layers: list[Dict[str, Any]] = []
    for slot, instance in equipped_armor.items():
        if slot not in ARMOR_SLOTS:
            raise RuleError(f"Unsupported equipped armor slot: {slot}")
        validate_armor_instance(instance, definitions)
        definition = definitions[instance["armor_id"]]
        if definition["slot"] != slot:
            raise RuleError(
                f"Armor instance {instance['instance_id']} is in wrong slot: {slot}"
            )
        if zone_id not in definition["covered_zones"]:
            continue

        layers.append(
            {
                "slot": slot,
                "instance_id": instance["instance_id"],
                "armor_id": instance["armor_id"],
                "condition": float(instance.get("condition", 1.0)),
                "durability": int(
                    instance.get("durability", definition["max_durability"])
                ),
                "resistances": {
                    damage_type: float(value)
                    for damage_type, value in definition["resistances"].items()
                },
                "tags": list(definition.get("tags", [])),
            }
        )
    return layers


def armor_player_view(
    instance: Mapping[str, Any],
    definitions: Mapping[str, Mapping[str, Any]],
) -> Dict[str, Any]:
    validate_armor_instance(instance, definitions)
    definition = definitions[instance["armor_id"]]
    if definition.get("player_visible", True) is False:
        return {
            "instance_id": instance["instance_id"],
            "name": "Unknown Armor",
        }

    return {
        "instance_id": instance["instance_id"],
        "armor_id": instance["armor_id"],
        "name": definition.get(
            "name",
            instance["armor_id"].replace("_", " ").title(),
        ),
        "slot": definition["slot"],
        "material_id": instance["material_id"],
        "forge_quality": float(instance.get("forge_quality", 0.5)),
        "condition": float(instance.get("condition", 1.0)),
        "durability": int(
            instance.get("durability", definition["max_durability"])
        ),
        "max_durability": int(definition["max_durability"]),
        "covered_zones": list(definition["covered_zones"]),
        "resistances": {
            damage_type: float(value)
            for damage_type, value in definition["resistances"].items()
        },
        "weight": float(definition["weight"]),
        "flexibility": float(definition["flexibility"]),
        "noise": float(definition["noise"]),
        "fatigue_burden": float(definition["fatigue_burden"]),
        "integrated_crystal_ids": list(
            instance.get("integrated_crystal_ids", [])
        ),
        "crystal_socket_count": int(
            definition.get("crystal_socket_count", 0)
        ),
    }
