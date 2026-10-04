# THE GAME — Loot, Reward & Distribution Standard

Status: **APPROVED FIRST-PASS V07 CONTRACT / STRUCTURED TABLES PENDING**
Parents:
- docs/systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md
- docs/world/WORLD_LOOT_PROVENANCE_STANDARD.md
Related:
- docs/systems/WORLD_BALANCE_INTEGRATION_PLAN.md

## 1. Purpose

Define how items/resources become obtainable through encounters, quests, world interaction, salvage, beasts, vendors and rewards without arbitrary disconnected drops.

## 2. Loot source types

First-pass source classes:
- authored quest reward;
- NPC inventory/possession;
- encounter aftermath;
- beast material;
- world resource;
- salvage;
- storage/container;
- vendor purchase;
- institution/faction reward.

Every source must reference item provenance.

## 3. Deterministic versus variable loot

Authored story-critical rewards should normally be deterministic.

Variable loot may exist later when:
- valid source pool exists;
- quantity/chance is balanced;
- deterministic seed inputs are defined;
- save/reload cannot reroll arbitrarily.

No wall-clock RNG.

## 4. Loot table record

Target fields:
- loot_table_id;
- source class/entity;
- entries;
- quantity range;
- eligibility;
- probability/weight if variable;
- scarcity/region constraints;
- ownership/legal state;
- one-time/repeat policy;
- depletion/restock rule;
- provenance reference;
- canon status.

## 5. Quest rewards

Quest rewards may include:
- items;
- knowledge;
- access;
- relationship/reputation;
- progression;
- currency once economy exists.

Do not force every quest to pay currency/items.

## 6. Combat aftermath

Combat may expose loot only after authoritative aftermath says the item is obtainable.

A visible weapon on an enemy does not automatically become a player item unless ownership/condition/item mapping allows it.

## 7. Beast loot

Beast materials must correspond to species/anatomy and harvesting rules.

No generic unrelated item drops.

## 8. World resources

Resource extraction must respect:
- zone;
- abundance;
- ownership;
- method;
- time;
- risk;
- depletion/renewal.

## 9. Containers/storage

Container contents are authored or generated from a valid provenance source.

Unopened contents stay hidden until access/reveal.

## 10. Duplication and farming

Prevent:
- repeated one-time quest reward;
- save/reload reroll abuse;
- unlimited rare resource from nonrenewing node;
- duplicate unique item.

## 11. Player-safe projection

UI may show obtained or currently accessible loot.

Do not show hidden table entries, future rewards or unavailable container contents.

## 12. Tests

Required:
- source provenance;
- one-time reward;
- deterministic variable loot;
- no reroll on reload;
- hidden contents;
- unique item protection;
- combat aftermath integration;
- beast/resource constraints.
