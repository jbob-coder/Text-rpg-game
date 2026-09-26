from __future__ import annotations

from typing import Any, Dict, Mapping

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
        if isinstance(minimum, bool) or not isinstance(minimum, (int, float)):
            raise RuleError(f"Equipment attribute requirement must be numeric: {key}")
        validated_attrs[key] = float(minimum)

    validated_skills: Dict[str, float] = {}
    for key, minimum in skill_requirements.items():
        if key not in SKILL_CATALOG:
            raise RuleError(f"Unknown equipment skill requirement: {key}")
        if isinstance(minimum, bool) or not isinstance(minimum, (int, float)):
            raise RuleError(f"Equipment skill requirement must be numeric: {key}")
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
    item_id = item.get("item_id")
    slot = item.get("slot")
    if not isinstance(item_id, str) or not item_id:
        raise RuleError("Equipment item requires item_id")
    if slot not in DEFAULT_SLOTS:
        raise RuleError(f"Unsupported equipment slot: {slot}")
    if consume_inventory and state.inventory.get(item_id, 0) < 1:
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
    attrs = state.player.get("attributes", {})
    skills = state.player.get("skills", {})
    for key, minimum in attr_requirements.items():
        if float(attrs.get(key, 0)) < minimum:
            raise RuleError(f"Attribute requirement not met: {key} >= {minimum}")
    for key, minimum in skill_requirements.items():
        if float(skills.get(key, 0)) < minimum:
            raise RuleError(f"Skill requirement not met: {key} >= {minimum}")

    previous = state.equipment.get(slot)
    state.equipment[slot] = {
        "item_id": item_id,
        "slot": slot,
        "quality": item.get("quality", "standard"),
        "modifiers": modifiers,
        "tags": list(item.get("tags", [])),
        "set_id": item.get("set_id"),
        "active_ability": item.get("active_ability"),
        "passive_perks": list(item.get("passive_perks", [])),
        "source": item.get("source", "unknown"),
    }
    if consume_inventory:
        state.inventory[item_id] -= 1
        if state.inventory[item_id] <= 0:
            del state.inventory[item_id]
    return previous
