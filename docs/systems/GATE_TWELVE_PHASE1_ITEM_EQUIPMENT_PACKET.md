# THE GAME — Gate Twelve Phase 1 Item & Equipment Proof Packet

Status: **CURRENT-STATE GROUNDED / PHASE 1 V07 PROOF / NO NEW ECONOMY REQUIRED**
Parents:
- docs/systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md
- docs/systems/ITEM_RECORD_CATALOG_STANDARD.md
- docs/systems/INVENTORY_STACK_CONTAINER_STANDARD.md
- docs/systems/EQUIPMENT_SLOT_LOADOUT_STANDARD.md
Phase 1:
- docs/PHASE_1_SOLO_PLAYABLE_PARALLEL_TRACK.md
Current source:
- content/vertical_slice_01.json
- src/textrpg/equipment.py
- src/textrpg/android_bridge.py

## 1. Purpose

Use current Gate Twelve loadout/inventory behavior to prove Phase 1 requirement #6 without blocking on currency, vendors, crafting, durability or a large loot catalog.

## 2. Current starting inventory

Current initial items:
- ITEM_MAINTENANCE_SEAL x1;
- ITEM_DEPOT_JACKET x1;
- ITEM_WORK_GLOVES x1;
- ITEM_SIGNAL_RING x1;
- ITEM_COURIER_NECKTAG x1.

ITEM_DEAD_RELAY is obtained during the current opening quest.

## 3. Current equippable records

ITEM_DEPOT_JACKET
- slot: body;
- quality: standard;
- modifier: attributes.endurance +2;
- tags: armor, utility;
- source: opening_loadout.

ITEM_WORK_GLOVES
- slot: hands;
- quality: standard;
- modifier: skills.technical_systems +1;
- tags: utility;
- source: opening_loadout.

ITEM_SIGNAL_RING
- slot: ring_1;
- quality: uncommon;
- modifier: attributes.perception +1;
- tags: accessory, signal;
- source: opening_loadout.

ITEM_COURIER_NECKTAG
- slot: neck;
- quality: standard;
- modifier: attributes.presence +1;
- tags: accessory, identity;
- source: opening_loadout.

These are current authored facts.

## 4. Current non-equipment proof items

ITEM_MAINTENANCE_SEAL
- current key/tool-like story item;
- consumed by a valid relay-opening choice.

ITEM_DEAD_RELAY
- quest/story object;
- obtained through the opening;
- visual state is already projected based on possession/flags/knowledge.

## 5. Phase 1 proof loop

Required player flow:
1. begin with current inventory;
2. inspect inventory projection;
3. equip one current equippable item;
4. authoritative equipment state changes;
5. relevant effective stat/status contribution changes;
6. unequip or replace;
7. state/projection updates;
8. obtain ITEM_DEAD_RELAY through story;
9. consume/use ITEM_MAINTENANCE_SEAL through its authored choice where applicable;
10. save;
11. reload;
12. verify inventory/equipment/story item state persists.

This proves obtain/use/equip/persist without new economy scope.

## 6. No extra reward required

The Phase 1 tactical encounter does not need to drop a new item merely to prove loot.

If its final content later grants loot, the item must use V07 provenance/loot rules.

## 7. Equipment and combat

When tactical combat is implemented:
- current equipped modifiers flow through the player combat-stat adapter;
- combat cannot invent separate jacket/glove/ring bonuses.

Equipment visuals may follow later asset/UI integration.

## 8. Player-safe UI

Inventory/equipment may show:
- item name;
- quantity;
- slot;
- equipped state;
- quality;
- known modifier contribution;
- legal equip/unequip action.

Do not expose hidden story purpose of the Dead Relay beyond player knowledge.

## 9. Phase 1 non-goals

Not required:
- currency;
- vendor;
- crafting;
- durability;
- encumbrance;
- item-instance serialization;
- random loot;
- material harvesting.

## 10. Tests

Required for Phase 1 closure:
- current inventory exact start;
- equip legality;
- inventory consumption where applicable;
- effective modifier contribution;
- unequip/replacement;
- relay acquisition;
- maintenance-seal consumption;
- save/load;
- Android projection;
- no duplication on failed transaction.

## 11. Result

The existing item/equipment loop is sufficient as the Phase 1 V07 proof if validated exact-head.

Broader economy remains separate.
