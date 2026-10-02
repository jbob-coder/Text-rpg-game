# THE GAME — World Loot Provenance Standard

Status: **ACTIVE / WORLD-ITEM INTEGRATION STANDARD**  
Parents:
- `docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`
- `docs/systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md`

## 1. Purpose

This standard ensures that loot, equipment, accessories, materials and rewards have a plausible source in the world.

Loot is not a disconnected random chest table.

## 2. Provenance chain

Every important item should be traceable through one or more chains:

`resource -> extraction/drop -> refinement/manufacture -> owner/location -> acquisition`

or

`institution/faction -> manufacture/issue -> carrier/storage -> acquisition`

or

`quest/event -> authored reward -> acquisition`.

## 3. Loot source classes

- beast anatomy/drop;
- natural resource;
- salvage;
- manufactured goods;
- institutional issue;
- personal inventory;
- secured storage;
- trade;
- quest reward;
- event aftermath;
- criminal/contraband only if authored.

## 4. Item-world fields

World provenance may record:
- item ID;
- source place/entity;
- manufacturer/creator if known;
- owner/controller;
- legality;
- scarcity;
- condition;
- quality source;
- renewable/nonrenewable;
- restock logic if any;
- transport route;
- economy relation;
- quest protection;
- visual asset pointer.

Stats/effects remain item-system authority.

## 5. Container rule

A container requires a reason to hold its contents.

Avoid:
- random weapons in ordinary trash;
- rare materials in unrelated civilian drawers;
- infinite respawning quest-critical items.

## 6. Beast loot

Beast drops must match anatomy/ecology.

If body-part preservation is supported:
- damage method can affect condition/quality;
- broken parts can reduce yield;
- precise targeting may change outputs.

This remains conditional on final combat/loot implementation.

## 7. Accessory provenance

Accessories such as rings, tags, badges, trinkets, necklaces or ability-focus objects should have:
- maker/source;
- social/faction meaning if any;
- legality;
- gameplay/narrative reason.

Avoid meaningless accessory spam.

## 8. Economy relation

Price is not stored as world truth unless the economy contract says so.

World provenance supplies:
- scarcity;
- origin;
- transport difficulty;
- legality;
- demand context;
- faction control.

Economy computes market effects.

## 9. Gate Twelve examples

Current authored items such as the maintenance seal, dead relay, depot jacket, work gloves, signal ring and courier neck tag already provide seeds for provenance documentation.

Their exact deeper manufacturing/economic chains are not yet fully authored and must not be invented merely to populate this standard.

## 10. Catalog requirement

Future structured item/world catalogs should validate:
- every persistent item ID;
- source/provenance;
- visual asset;
- equipment mapping where relevant;
- quest protection;
- orphan/unused item detection.
