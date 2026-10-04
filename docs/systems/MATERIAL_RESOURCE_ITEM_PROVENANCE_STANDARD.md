# THE GAME — Material, Resource & Item Provenance Standard

Status: **APPROVED FIRST-PASS V07 CONTRACT / WORLD CATALOGS PENDING**
Parents:
- docs/systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md
- docs/world/WORLD_ECOSYSTEM_AND_RESOURCES.md
- docs/world/WORLD_LOOT_PROVENANCE_STANDARD.md
Related:
- docs/assets/ASSET_PROVENANCE_REGISTRY.md

## 1. Purpose

Define where materials/resources/items come from so loot, crafting if later adopted, economy, ecology and world state remain causally connected.

## 2. Provenance layers

Distinguish:
- asset provenance: where the visual/source file came from;
- item provenance: how the in-world item entered circulation;
- material provenance: biological/geological/manufactured origin;
- ownership provenance: who legally/actually possessed it;
- loot-event provenance: why the player can obtain it now.

These must not be conflated.

## 3. Item source classes

Controlled first-pass source classes:
- starting_loadout;
- quest/event;
- NPC inventory;
- vendor/institution;
- manufactured;
- salvage;
- world resource;
- beast material;
- recovered storage;
- reward;
- unknown/legacy only when source genuinely has not been reconstructed.

## 4. Material record

Target material fields:
- material_id;
- name;
- class;
- source region/resource/species/process;
- properties relevant to gameplay;
- legality;
- scarcity;
- uses;
- canon status.

Do not invent pseudo-scientific composition when gameplay does not consume it.

## 5. Resource record

Target:
- resource_id;
- source zone;
- abundance;
- depletion/renewal;
- extraction method;
- ownership/law;
- risk;
- transport;
- item outputs.

Resource extraction is not automatically a Phase 1 mechanic.

## 6. Manufactured items

Manufactured provenance may reference:
- maker/facility class;
- material inputs;
- institution/faction;
- production era/batch only when meaningful.

Crafting recipes are a separate system and remain optional.

## 7. Beast materials

Must reference:
- species/anatomy;
- harvesting condition;
- ecological/legal consequences;
- quality influences.

No generic “monster drop table” detached from biology/world.

## 8. Current Gate Twelve items

Current loadout source metadata already marks multiple items as opening_loadout.

The Dead Relay comes from a current story event and courier context.

These should be normalized into provenance categories later without changing current gameplay IDs.

## 9. Loot integration

Every obtainable item source should answer:
- where was it before?;
- why is it available?;
- who owned it?;
- what state made transfer legal/possible?;
- does obtaining it change world/social state?.

## 10. Economy integration

Supply and scarcity derive from provenance/resource/production networks, not arbitrary price multipliers alone.

## 11. Tests

Required when structured provenance is implemented:
- valid source refs;
- no impossible beast/material linkage;
- quest item source;
- ownership transfer;
- save/load of instance provenance if later used;
- no UI leak of hidden source history.
