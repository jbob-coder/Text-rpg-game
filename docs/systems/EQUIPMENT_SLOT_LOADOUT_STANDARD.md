# THE GAME — Equipment Slot & Loadout Standard

Status: **APPROVED FIRST-PASS V07 CONTRACT / CURRENT RUNTIME FOUNDATION EXISTS**
Parent:
- docs/systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md
Current source:
- src/textrpg/equipment.py
- src/textrpg/modifiers.py
- src/textrpg/android_bridge.py

## 1. Purpose

Define equip legality, slot ownership, modifiers, set hooks and visual/loadout boundaries.

## 2. Current slot authority

Current DEFAULT_SLOTS:
- head;
- body;
- hands;
- legs;
- feet;
- main_hand;
- off_hand;
- ring_1;
- ring_2;
- neck;
- accessory_1;
- accessory_2.

The first-pass target preserves these slots.

## 3. Current equip behavior

equip_item currently validates:
- item mapping;
- item_id;
- supported slot;
- inventory presence when consume_inventory=true;
- modifier mapping;
- base attribute requirements;
- base skill requirements;
- set_id;
- tags;
- passive_perks.

It writes equipped record with:
- item_id;
- slot;
- quality;
- modifiers;
- tags;
- set_id;
- active_ability;
- passive_perks;
- source.

This is authoritative current behavior.

## 4. Requirement rule

Equipment requirements use permanent/base player values.

Equipped bonuses do not qualify another item.

Reason:
- prevents circular/order-dependent builds.

Keep this rule.

## 5. Slot conflicts

One record per slot.

Equipping into an occupied slot returns/replaces the previous record according to the caller's inventory transaction.

Two-handed weapons, linked accessory slots and mutually exclusive gear are future explicit rules, not inferred from tags.

## 6. Sets

Current set hooks exist.

Set bonuses remain an equipment/modifier rule and must not be reimplemented by UI.

A set definition must use stable IDs and deterministic piece counts.

## 7. Active/passive grants

Equipment may reference:
- active ability;
- passive perks.

Availability must be derived from equipped authoritative state and relevant ability/perk rules.

Removing gear removes gear-sourced grants unless another source still grants them.

## 8. Quality and condition

Current equipped records store quality.

Quality is not durability.

No durability/repair state is added here until V07 adopts it explicitly.

## 9. Visual integration

Equipment slot state may drive:
- paper-doll layers;
- held sprite;
- portrait/accessory overlays.

Visual absence must not change gameplay equipment state.

## 10. Tactical integration

Combat actor adapters read equipment-derived authoritative modifiers.

Combat must not copy item stats into tactical authored maps.

## 11. Player-safe projection

Android may show:
- equipped slot;
- item;
- quality;
- modifiers/contributions according to status visibility;
- legal equip/unequip actions.

## 12. Tests

Required:
- all current slots;
- invalid slot rejection;
- base requirement behavior;
- occupied-slot replacement;
- inventory consume atomicity;
- set bonus interaction;
- passive/active grant removal;
- save/load;
- visual consumer does not own rules.
