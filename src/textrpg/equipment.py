from __future__ import annotations

from math import isfinite
from typing import Any, Dict, Mapping, MutableMapping

from .core import GameState, RuleError
from .modifiers import (
    active_set_bonuses,
    equipment_modifiers,
    set_counts,
    validate_modifier_mapping,
)
from .schema import ATTRIBUTE_SPECS, SKILL_CATALOG


def _validate_requirements(item_id: str, requirements: Any) -> tuple[Dict[str, float], Dict[str, float]]:
    if requirements is None:
        return {}, {}
    if not isinstance(requirements, Mapping):
        raise RuleError(f"Equipment requirements must be an object: {item_id}")

    attr_requirements = requirements.get("attributes", {})
    skill_requirements = requirements.get("skills", {})
    if not isinstance(attr_requirements, Mapping):
        raise RuleError(f"Equipment attribute requirements must be an object: {item_id}")
    if not isinstance(skill_requirements, Mapping):
        raise RuleError(f"Equipment skill requirements must be an object: {item_id}")

    validated_attrs: Dict[str, float] = {}
    for key, minimum in attr_requirements.items():
        if key not in ATTRIBUTE_SPECS:
            raise RuleError(f"Unknown equipment attribute requirement: {key}")
        if (
            isinstance(minimum, bool)
            or not isinstance(minimum, (int, float))
            or not isfinite(float(minimum))
        ):
            raise RuleError(f"Equipment attribute requirement must be finite numeric: {key}")
        validated_attrs[key] = float(minimum)

    validated_skills: Dict[str, float] = {}
    for key, minimum in skill_requirements.items():
        if key not in SKILL_CATALOG:
            raise RuleError(f"Unknown equipment skill requirement: {key}")
        if (
            isinstance(minimum, bool)
            or not isinstance(minimum, (int, float))
            or not isfinite(float(minimum))
        ):
            raise RuleError(f"Equipment skill requirement must be finite numeric: {key}")
        validated_skills[key] = float(minimum)

    return validated_attrs, validated_skills


DEFAULT_SLOTS = (
    "head",
    "body",
    "hands",
    "legs",
    "feet",
    "main_hand",
    "off_hand",
    "accessory_1",
    "accessory_2",
)


def equip_item(
    state: GameState,
    item: Mapping[str, Any],
    *,
    consume_inventory: bool = False,
) -> Dict[str, Any] | None:
    if not isinstance(item, Mapping):
        raise RuleError("Equipment item must be an object")
    if not isinstance(state.equipment, MutableMapping):
        raise RuleError("state.equipment must be mutable")
    if not isinstance(consume_inventory, bool):
        raise RuleError("consume_inventory must be boolean")

    item_id = item.get("item_id")
    slot = item.get("slot")
    if not isinstance(item_id, str) or not item_id:
        raise RuleError("Equipment item requires item_id")
    if slot not in DEFAULT_SLOTS:
        raise RuleError(f"Unsupported equipment slot: {slot}")

    inventory_quantity = None
    if consume_inventory:
        if not isinstance(state.inventory, MutableMapping):
            raise RuleError("state.inventory must be mutable")
        inventory_quantity = state.inventory.get(item_id, 0)
        if (
            isinstance(inventory_quantity, bool)
            or not isinstance(inventory_quantity, int)
            or inventory_quantity < 1
        ):
            raise RuleError(f"Item not present in inventory: {item_id}")

    try:
        modifiers = validate_modifier_mapping(
            item.get("modifiers", {}),
            source=f"equipment:{item_id}",
        )
    except ValueError as exc:
        raise RuleError(f"Invalid equipment modifiers for {item_id}: {exc}") from exc

    # Equipment requirements deliberately use permanent/base values. Allowing one
    # equipped item to qualify another can create circular or order-dependent builds.
    attr_requirements, skill_requirements = _validate_requirements(
        item_id,
        item.get("requirements", {}),
    )
    if not isinstance(state.player, Mapping):
        raise RuleError("state.player must be an object")
    attrs = state.player.get("attributes", {})
    skills = state.player.get("skills", {})
    if not isinstance(attrs, Mapping):
        raise RuleError("player.attributes must be an object")
    if not isinstance(skills, Mapping):
        raise RuleError("player.skills must be an object")

    for key, minimum in attr_requirements.items():
        current = attrs.get(key, 0)
        if (
            isinstance(current, bool)
            or not isinstance(current, (int, float))
            or not isfinite(float(current))
        ):
            raise RuleError(f"Equipment attribute state must be finite numeric: {key}")
        if float(current) < minimum:
            raise RuleError(f"Attribute requirement not met: {key} >= {minimum}")
    for key, minimum in skill_requirements.items():
        current = skills.get(key, 0)
        if (
            isinstance(current, bool)
            or not isinstance(current, (int, float))
            or not isfinite(float(current))
        ):
            raise RuleError(f"Equipment skill state must be finite numeric: {key}")
        if float(current) < minimum:
            raise RuleError(f"Skill requirement not met: {key} >= {minimum}")

    set_id = item.get("set_id")
    if set_id is not None and (not isinstance(set_id, str) or not set_id):
        raise RuleError(f"Equipment set_id must be a non-empty string: {item_id}")

    tags = item.get("tags", [])
    passive_perks = item.get("passive_perks", [])
    if not isinstance(tags, list) or not all(isinstance(tag, str) and tag for tag in tags):
        raise RuleError(f"Equipment tags must be a list of non-empty strings: {item_id}")
    if not isinstance(passive_perks, list) or not all(
        isinstance(perk_id, str) and perk_id for perk_id in passive_perks
    ):
        raise RuleError(
            f"Equipment passive_perks must be a list of non-empty strings: {item_id}"
        )

    previous = state.equipment.get(slot)
    state.equipment[slot] = {
        "item_id": item_id,
        "slot": slot,
        "quality": item.get("quality", "standard"),
        "modifiers": modifiers,
        "tags": list(tags),
        "set_id": set_id,
        "active_ability": item.get("active_ability"),
        "passive_perks": list(passive_perks),
        "source": item.get("source", "unknown"),
    }
    if consume_inventory:
        remaining = int(inventory_quantity) - 1
        if remaining <= 0:
            del state.inventory[item_id]
        else:
            state.inventory[item_id] = remaining
    return previous
