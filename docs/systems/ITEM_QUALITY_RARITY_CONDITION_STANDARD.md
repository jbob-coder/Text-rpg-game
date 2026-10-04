# THE GAME — Item Quality, Rarity & Condition Standard

Status: **APPROVED FIRST-PASS V07 CONTRACT / TAXONOMY LOCKED, FINAL TIERS PARTIAL**
Parent:
- docs/systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md
Related:
- docs/systems/status/ABILITY_RARITY_STANDARD.md

## 1. Purpose

Keep manufacturing quality, world rarity/scarcity, physical condition and uniqueness as distinct concepts.

Item rarity must not copy ability rarity automatically.

## 2. Current reality

Current items/equipment use quality strings including:
- standard;
- uncommon.

Current runtime does not implement a full item-rarity or durability system.

Do not reinterpret current “uncommon” as proof of a global tier ladder.

## 3. Quality

Quality describes construction/performance grade.

Target concept:
- item-specific or controlled quality vocabulary;
- may affect modifiers/value/reliability only through explicit formulas.

Current values remain accepted legacy/current content until a final quality catalog is chosen.

## 4. Rarity/scarcity

Rarity answers how common the item is in the world.

It may derive from:
- production volume;
- region;
- legal restriction;
- historical loss;
- unique creator;
- resource scarcity.

It does not inherently make the item stronger.

## 5. Condition

Condition answers current physical state.

Possible future values:
- pristine;
- serviceable;
- worn;
- damaged;
- broken.

No condition/durability runtime is adopted yet.

## 6. Uniqueness

Uniqueness is separate:
- generic;
- named pattern;
- limited issue;
- unique artifact.

Unique items require instance/provenance decisions if multiple copies must be impossible.

## 7. UI

Do not rely on color alone to communicate any quality/rarity dimension.

If both quality and rarity are shown, label them distinctly.

## 8. Loot/economy

Loot tables and prices may use scarcity/quality/condition as separate inputs.

No one color tier controls drop chance, power and price simultaneously unless later design explicitly chooses it.

## 9. Migration

Before replacing current quality strings:
- inventory/equipment save implications;
- Android mapper/display;
- asset variants;
- tests;
must be audited.

## 10. Tests

Required when expanded:
- current strings preserved or migrated;
- rarity independent of power;
- condition independent of rarity;
- unique constraints;
- player-safe display;
- save/load migration.
