# THE GAME — Items, Economy, Loot & Resource Master Plan

Status: **FIRST-PASS CONTRACT LAYER ESTABLISHED / CURRENT INVENTORY-EQUIPMENT FOUNDATION EXISTS / FULL ECONOMY NOT IMPLEMENTED**
Parents:
- `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`
- `docs/systems/GAMEPLAY_SYSTEM_REBUILD_MATRIX.md`
- `docs/world/WORLD_SCALE_DOCUMENTATION_BLUEPRINT.md`

## 1. Purpose

Create one coherent model for items, equipment, accessories, loot, world resources, ownership, scarcity, and economy.

Current inventory/equipment behavior remains authoritative until migrated.

## 2. Item record

Every persistent item type should eventually define:
- stable item ID;
- name;
- category;
- description;
- tags;
- material;
- quality/rarity if used;
- stack rule;
- weight/encumbrance if used;
- equipment slot if wearable;
- modifiers;
- ability/interaction hooks;
- value;
- legality;
- provenance;
- durability only if adopted;
- repair/crafting relationships only if adopted;
- icon ID;
- paper-doll/held/world asset IDs;
- canon status.

## 3. Item categories

Possible:
- equipment;
- weapon/tool;
- clothing/armor;
- accessory;
- consumable;
- quest item;
- key/access item;
- material;
- beast material;
- resource;
- document/data;
- salvage;
- currency.

Final taxonomy must avoid duplicate categories.

## 4. Equipment

Preserve existing slot semantics until migration.

Future documentation:
- head;
- chest/body;
- hands;
- legs;
- feet;
- main hand;
- off hand;
- rings;
- neck;
- accessories.

Need:
- equip legality;
- conflicts;
- two-hand rules if used;
- visual layer;
- stat modifiers;
- condition;
- quality;
- ownership.

## 5. Accessories

Accessories should have distinct purpose rather than being stat-stick overflow.

Possible roles:
- identity/access;
- social status;
- utility;
- ability interaction;
- protection;
- faction/legal access.

## 6. Quality / rarity

Still undecided.

If adopted, distinguish:
- manufacturing quality;
- scarcity/rarity;
- condition;
- uniqueness.

Do not collapse these into one color tier unless justified.

## 7. Durability / repair

Not currently assumed.

Only add if:
- gameplay benefit outweighs maintenance burden;
- Workshop Row/repair systems are documented;
- economy and item-state UI support it.

## 8. Crafting

Not currently assumed.

If adopted:
- recipes;
- skills;
- tools;
- stations;
- time;
- resource provenance;
- failure/quality;
- NPC economy impact.

Do not add crafting just because generic asset roadmap includes material templates.

## 9. Loot provenance

Every loot source must answer why the item exists there.

Sources:
- NPC inventory;
- beast drop;
- environmental resource;
- storage/ownership;
- salvage;
- quest;
- battlefield;
- shop;
- reward.

Avoid arbitrary chest loot disconnected from world logic.

## 10. Beast loot

Needs:
- species;
- body/material source;
- harvesting rule;
- condition/quality;
- ecological consequences;
- legality;
- economy use.

Loot should reflect beast biology.

## 11. Resource nodes

Each node:
- stable ID;
- resource;
- location;
- ownership;
- abundance;
- regeneration/depletion;
- extraction method;
- risk;
- transport;
- market use.

## 12. Economy

Need decisions on:
- currencies;
- barter;
- wages;
- taxes;
- prices;
- supply/demand;
- scarcity;
- transport cost;
- faction control;
- black market;
- theft/ownership;
- regional price differences.

Current game should not invent economy values before this system is locked.

## 13. Ownership and crime

Item ownership can affect:
- theft;
- reputation;
- guards/law;
- NPC memory;
- resale;
- faction consequences.

Requires law/crime integration.

## 14. Vendors

Vendors are NPC/institution systems, not generic menus.

Each vendor should have:
- inventory source;
- restock rule;
- funds if modeled;
- prices;
- faction/legal access;
- schedule/location.

## 15. Inventory UX

Android presentation should support:
- item icon;
- quantity;
- category;
- equipped state;
- detail;
- legal/quest flags when player-visible;
- compare;
- action buttons from authoritative state.

## 16. Pixel art

Each item may have:
- 32x32 icon;
- world prop;
- paper-doll;
- held sprite;
- inspection/close-up;
- state variants.

Only create required variants.

## 17. Loot/balance integration

Loot must align with:
- region danger;
- enemy/beast rank;
- economy;
- progression;
- class/skill system;
- quest rewards.

No unlimited high-tier farming in low-risk zones unless intentionally designed.

## 18. Open decisions

- currency;
- price scale;
- rarity;
- quality;
- durability;
- crafting;
- encumbrance;
- ammo;
- vendor restock;
- theft;
- random modifiers;
- unique items;
- item level requirements.


## 19. V07 first-pass child contract suite — 2026-10-04

The Items/Economy/Loot first-pass layer now includes:

- ITEM_RECORD_CATALOG_STANDARD.md
- INVENTORY_STACK_CONTAINER_STANDARD.md
- EQUIPMENT_SLOT_LOADOUT_STANDARD.md
- ITEM_QUALITY_RARITY_CONDITION_STANDARD.md
- MATERIAL_RESOURCE_ITEM_PROVENANCE_STANDARD.md
- LOOT_REWARD_DISTRIBUTION_STANDARD.md
- ECONOMY_CURRENCY_PRICING_STANDARD.md
- VENDOR_SERVICE_OWNERSHIP_STANDARD.md
- GATE_TWELVE_PHASE1_ITEM_EQUIPMENT_PACKET.md

Together with this master, V07 has 10 / 10 first-pass canonical units.

What is locked at first-pass level:
- stable item-type identity and definition/runtime separation;
- current flat inventory remains sufficient for Phase 1;
- current equipment slot contract remains authoritative;
- equipment requirements continue using permanent/base stats to avoid circular qualification;
- quality, rarity/scarcity, condition and uniqueness remain separate concepts;
- loot must have world/item provenance;
- economy architecture is defined without inventing a currency or universal price scale;
- vendors/services belong to world/NPC/institution state rather than generic UI menus.

What remains future work:
- complete item/material/resource catalogs;
- final currency and price bands;
- vendor/service population;
- durability/crafting/encumbrance decisions;
- structured loot tables;
- item-instance migration if ever needed;
- final economy UI and balance evidence.

Phase 1 should prove the existing inventory/equipment/use/save loop before adding broader economy scope.
