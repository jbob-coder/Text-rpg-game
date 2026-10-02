# Economy, Items and Ecosystem Program

Status: ACTIVE / ARCHITECTURE

## Scope

Owns:
- currencies/value exchange;
- resources/materials;
- loot;
- items;
- equipment;
- accessories;
- crafting/repair if adopted;
- vendors/services if adopted;
- scarcity;
- beast resources;
- ecosystems;
- resource extraction;
- production chains;
- local/regional economic differences.

## Existing foundation

Current repository already models items, equipment slots, modifiers, quality concepts and provenance in limited form.

Do not infer a complete economy from those primitives.

## Item taxonomy target

Potential families:
- consumable;
- equipment;
- accessory;
- tool;
- key/quest item;
- material;
- beast-derived material;
- document/knowledge item;
- container;
- trade good;
- currency/token;
- crafting component if crafting is adopted.

Every family needs stable IDs and clear ownership.

## Ecosystem contract

Each ecosystem/biome eventually documents:
- terrain/climate;
- flora;
- beasts;
- predator/prey relationships;
- mutations/evolution if the setting uses them;
- resources;
- hazards;
- settlement pressure;
- harvesting consequences;
- seasonal/time variation where relevant;
- world-state change hooks.

## Beast zones

A beast zone must not be only a level number. Target records include:
- spatial boundary;
- known species;
- threat bands;
- migration behavior;
- resource value;
- faction access/control;
- environmental hazards;
- respawn/repopulation model if any;
- quests/events;
- how overhunting or world events can change it.

## Loot contract

Loot must be derived from authored sources and state, not arbitrary UI generation.

Future design must decide:
- deterministic vs seeded drops;
- body-part/resource-quality dependence;
- rarity;
- preservation/damage;
- player skill contribution;
- equipment/tool contribution;
- market value;
- anti-farming controls.

## Required future documents

- ECONOMY_CORE
- CURRENCY_AND_VALUE
- ITEM_SCHEMA_V2
- EQUIPMENT_ACCESSORY_SYSTEM
- LOOT_GENERATION
- RESOURCE_MATERIAL_CATALOG
- CRAFTING_REPAIR_DECISION
- VENDOR_SERVICE_DECISION
- ECOSYSTEM_SCHEMA
- BEAST_ZONE_SCHEMA
- BEAST_RESOURCE_CHAIN
- REGIONAL_ECONOMIES
