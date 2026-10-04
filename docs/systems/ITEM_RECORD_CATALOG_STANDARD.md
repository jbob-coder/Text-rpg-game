# THE GAME — Item Record & Catalog Standard

Status: **APPROVED FIRST-PASS V07 CONTRACT / CURRENT REGISTRY FOUNDATION EXISTS**
Parent:
- docs/systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md
Current source:
- content/vertical_slice_01.json
- src/textrpg/content.py
- src/textrpg/equipment.py

## 1. Purpose

Define one stable item identity/schema used by inventory, equipment, quests, activities, combat, economy, world loot, UI, saves, and assets.

## 2. Current reality

Current authored item registry contains:
- ITEM_MAINTENANCE_SEAL;
- ITEM_DEAD_RELAY;
- ITEM_DEPOT_JACKET;
- ITEM_WORK_GLOVES;
- ITEM_SIGNAL_RING;
- ITEM_COURIER_NECKTAG.

Current metadata already uses label, slot, quality, modifiers, tags and source where applicable.

Current GameState.inventory stores item_id -> integer quantity.

Current equipment state stores equipped item records by slot.

This is a useful foundation but not yet the final item catalog schema.

## 3. Stable identity

Item type IDs:
- prefix ITEM_;
- uppercase semantic ID;
- never encode current quantity, owner or condition;
- never reused for another item type.

A unique physical object may later require an instance ID in addition to its item type ID. Phase 1 does not need general item instances.

## 4. Required catalog fields

First-pass item definition:
- item_id;
- label;
- category;
- description when player-facing;
- tags;
- stack policy;
- slot if equippable;
- requirements;
- modifiers;
- quality;
- source/provenance class;
- quest/key status when applicable;
- legality/ownership class when applicable;
- value/pricing reference when economy exists;
- visual asset references when consumed;
- canon status.

Optional fields are omitted rather than filled with invented defaults.

## 5. Category taxonomy

First-pass categories:
- EQUIPMENT;
- TOOL;
- ACCESSORY;
- CONSUMABLE;
- QUEST;
- KEY_ACCESS;
- MATERIAL;
- RESOURCE;
- DOCUMENT_DATA;
- SALVAGE;
- CURRENCY.

A record may use tags for finer meaning. Do not multiply overlapping top-level categories.

## 6. Definition versus runtime state

Definition owns:
- what the item type is.

Inventory owns:
- quantity/possession.

Equipment owns:
- equipped state.

Future item instance state may own:
- durability;
- unique provenance;
- custom modification;
- serial identity.

Do not put mutable owner/quantity into the static item definition.

## 7. Requirements and modifiers

Equippable items may reference base attribute/skill requirements and validated modifier paths.

Current equipment logic deliberately checks permanent/base values for requirements so equipped items do not circularly qualify each other. Preserve that rule unless explicitly migrated.

## 8. Quest/key items

Quest/key items:
- are ordinary stable item IDs with additional usage/protection rules;
- are not automatically non-removable unless their quest contract says so;
- must have clear source/provenance.

ITEM_DEAD_RELAY is current proof of an item whose story state also drives visual/power/knowledge content.

## 9. Player-safe projection

UI may receive:
- ID when internal UI contract uses stable IDs;
- name;
- quantity;
- category;
- equipped state;
- quality;
- known description/tags;
- legal actions.

UI must not infer hidden origin, secret function or quest future from raw item metadata.

## 10. Validation

Require:
- valid stable ID;
- valid category;
- valid slot if present;
- nonnegative stack/quantity rules;
- valid modifier paths;
- valid requirements;
- valid asset/provenance refs when required;
- no duplicate ID.

## 11. Tests

Required:
- current six item records remain valid after migration;
- invalid slot/modifier rejected;
- item definition separated from quantity;
- hidden metadata redaction;
- save/load inventory references;
- item deletion/migration cannot orphan equipment/quest references.
