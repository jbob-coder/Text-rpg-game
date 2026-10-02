# THE GAME — World Ecosystems and Resources

Status: **ACTIVE / WORLD STANDARD + CATALOG SEED**  
Parent: `docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`

## 1. Purpose

This document defines how ecosystems, natural resources, salvage fields, anomalous resources, and human extraction pressure are authored as connected world systems rather than as disconnected backdrop or arbitrary loot.

## 2. Ecosystem record

Each ecosystem requires:
- `ecosystem_id`;
- parent region/bounds;
- biome;
- climate;
- terrain;
- water;
- dominant flora;
- ordinary fauna;
- beast species;
- predator/prey relations;
- migration;
- reproduction/renewal;
- hazards;
- seasonal/state variation if simulated;
- human settlement pressure;
- extraction pressure;
- resource zones;
- transport routes;
- visual kit;
- danger/balance links.

## 3. Resource record

Each resource requires:
- `resource_id`;
- category;
- source ecosystem/geology/industry;
- spatial bounds/source sites;
- abundance;
- renewable/nonrenewable;
- renewal/depletion rate if simulated;
- extraction method;
- required tools/skills if any;
- hazard;
- ownership/control;
- legal restrictions;
- refinement;
- transport;
- consumers;
- item/material outputs;
- economy link;
- ecological cost;
- faction interest;
- associated beasts;
- quest/event hooks.

## 4. Resource categories

Potential categories:
- biological;
- agricultural;
- mineral;
- crystal/energy only if final lore supports it;
- water;
- timber/fiber;
- salvage;
- manufactured feedstock;
- anomalous;
- beast-derived.

A category does not imply a crafting system.

## 5. Ecology first

Beast and resource placement should normally follow ecology, infrastructure, or an authored anomaly.

Do not:
- scatter high-value materials only to satisfy player progression;
- spawn beasts without habitat/food/territory logic;
- assign resource drops to unrelated creatures;
- make every region contain every resource.

## 6. Extraction pressure

Where simulation depth justifies it, track:
- untouched;
- lightly exploited;
- industrially exploited;
- depleted;
- recovering;
- contaminated/damaged;
- protected.

Effects may propagate into:
- prices;
- migration;
- beast behavior;
- settlement prosperity;
- faction conflict;
- quests;
- route security.

Implementation is deferred until economy/world simulation consumes these states.

## 7. Human/ecosystem interaction

Each inhabited region should eventually document:
- food supply;
- water;
- waste;
- land use;
- dangerous wildlife/beasts;
- resource extraction;
- conservation/protection;
- infrastructure impact.

This grounds settlement placement and economy.

## 8. Resource-to-item provenance

Every material/item derived from a resource should be traceable:
`ecosystem/resource zone -> extraction/drop -> refinement -> item/equipment/consumable`.

The item system owns item stats. This document owns origin and world distribution.

## 9. Gate Twelve status

Gate Twelve currently has municipal/infrastructure salvage context and technical equipment, but its wider natural ecosystem/resource parent remains undecided.

Do not invent surrounding biome/resources until the parent region is authored.

## 10. Catalog production order

1. parent geography;
2. ecosystem;
3. resource zones;
4. ordinary fauna/flora;
5. beast relationships;
6. human extraction/settlement pressure;
7. route/economy links;
8. loot/item provenance;
9. state variants;
10. visual kits.
