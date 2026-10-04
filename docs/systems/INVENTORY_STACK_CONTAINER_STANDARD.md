# THE GAME — Inventory, Stack & Container Standard

Status: **APPROVED FIRST-PASS V07 CONTRACT / CURRENT FLAT INVENTORY EXISTS**
Parent:
- docs/systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md
Current source:
- src/textrpg/core.py
- src/textrpg/android_bridge.py

## 1. Purpose

Define item possession, quantities, transfers and future containers without replacing the current simple inventory before the game needs more complexity.

## 2. Current reality

GameState.inventory is:
- mapping item_id -> integer quantity.

Current Android projection:
- filters nonpositive/invalid quantities;
- resolves item definitions;
- reports name, quantity, equippable, slot and quality.

This flat model is adequate for Phase 1.

## 3. Phase 1 inventory model

Keep:
- one player inventory;
- integer stack quantities;
- stable item IDs;
- no nested containers required;
- no weight/encumbrance requirement;
- no item-instance durability requirement.

This minimizes save/runtime complexity.

## 4. Stack policy

Each item definition eventually declares:
- STACKABLE;
- SINGLETON_TYPE;
- INSTANCE_REQUIRED.

Phase 1 current items can use integer quantities even when normal gameplay supplies one.

If instance-specific state is later required, migrate deliberately rather than encoding serialized objects inside the quantity map.

## 5. Inventory mutation

All mutations validate before commit.

Operations:
- add;
- remove;
- transfer;
- consume;
- equip-from-inventory;
- return unequipped item where the ownership model requires it.

Quantity:
- integer;
- cannot be negative;
- zero removes the key.

## 6. Atomicity

A transaction such as equip-from-inventory must not:
- consume the item and then fail to equip;
- duplicate the previous equipped item;
- leave negative quantity.

Snapshot/rollback or preflight is required.

## 7. Capacity

No inventory capacity/encumbrance system is approved for Phase 1.

Future capacity may use:
- slots;
- weight;
- volume;
- container limits.

Do not add burden until item/world/activity systems justify it.

## 8. Containers

Future containers require:
- container_id;
- owner/location;
- access rule;
- contents;
- persistence;
- theft/ownership;
- capacity when used.

World containers must not be arbitrary loot chests detached from provenance.

## 9. Transfers

Transfers between player/NPC/world/vendor require explicit ownership and source/destination.

A transfer event should record enough provenance to explain where an important item came from.

## 10. Player-safe projection

UI may show only player-accessible inventory/containers.

Do not reveal hidden NPC inventories or unopened container contents unless the game state allows it.

## 11. Save compatibility

Phase 1 flat inventory remains schema-v1 compatible.

A future item-instance/container migration requires save versioning if durable shape changes.

## 12. Tests

Required:
- add/remove boundary;
- no negative quantities;
- equip atomicity;
- consume atomicity;
- save/load;
- hidden container redaction;
- current item loop regression.
