from __future__ import annotations

from typing import Any, Dict, Mapping

from .core import GameState, RuleError
from .modifiers import active_set_bonuses, equipment_modifiers, set_counts


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

    # Equipment requirements deliberately use permanent/base values. Allowing one
    # equipped item to qualify another can create circular or order-dependent builds.
    requirements = item.get("requirements", {})
    attrs = state.player.get("attributes", {})
    skills = state.player.get("skills", {})
    for key, minimum in requirements.get("attributes", {}).items():
        if float(attrs.get(key, 0)) < float(minimum):
            raise RuleError(f"Attribute requirement not met: {key} >= {minimum}")
    for key, minimum in requirements.get("skills", {}).items():
        if float(skills.get(key, 0)) < float(minimum):
            raise RuleError(f"Skill requirement not met: {key} >= {minimum}")

    previous = state.equipment.get(slot)
    state.equipment[slot] = {
        "item_id": item_id,
        "slot": slot,
        "quality": item.get("quality", "standard"),
        "modifiers": dict(item.get("modifiers", {})),
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
