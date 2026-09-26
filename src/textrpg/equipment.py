from __future__ import annotations

from typing import Any, Dict, Mapping

from .core import GameState, RuleError


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


def set_counts(state: GameState) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for record in state.equipment.values():
        set_id = record.get("set_id")
        if set_id:
            counts[set_id] = counts.get(set_id, 0) + 1
    return counts


def active_set_bonuses(
    state: GameState,
    set_definitions: Mapping[str, Mapping[str, Any]],
) -> Dict[str, Dict[str, Any]]:
    counts = set_counts(state)
    active: Dict[str, Dict[str, Any]] = {}
    for set_id, count in counts.items():
        definition = set_definitions.get(set_id, {})
        thresholds = definition.get("thresholds", {})
        for pieces_raw, bonus in thresholds.items():
            pieces = int(pieces_raw)
            if count >= pieces:
                active[f"{set_id}:{pieces}"] = dict(bonus)
    return active


def equipment_modifiers(
    state: GameState,
    set_definitions: Mapping[str, Mapping[str, Any]] | None = None,
) -> Dict[str, float]:
    total: Dict[str, float] = {}
    for record in state.equipment.values():
        for path, value in record.get("modifiers", {}).items():
            total[path] = total.get(path, 0.0) + float(value)
    if set_definitions:
        for bonus in active_set_bonuses(state, set_definitions).values():
            for path, value in bonus.get("modifiers", {}).items():
                total[path] = total.get(path, 0.0) + float(value)
    return total
