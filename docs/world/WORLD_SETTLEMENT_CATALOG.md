# THE GAME — World Settlement Catalog

Status: **ACTIVE / SCHEMA + PRODUCTION CATALOG**  
Parent: `docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`

## 1. Purpose

This is the catalog contract for cities, towns, villages, outposts, stations, camps, districts, and other persistent inhabited places.

It begins with schema and production rules. Large-scale entries are populated only after geography and political context exist.

## 2. Settlement types

Supported classes may include:
- metropolis;
- city;
- town;
- village;
- hamlet;
- fortress;
- industrial settlement;
- transit settlement;
- research/technical site;
- frontier outpost;
- temporary camp;
- underground settlement;
- district-scale civic complex.

A type describes role/scale, not quality or danger.

## 3. Required settlement record

Each settlement requires:
- `settlement_id`;
- name;
- type;
- parent region;
- political authority;
- coordinate/bounds;
- population band;
- founding/origin;
- water/food supply;
- major routes;
- districts;
- major sites;
- economy;
- resource inputs/outputs;
- institutions;
- housing pattern;
- infrastructure;
- law/security;
- medical/public services;
- education/training;
- social hierarchy;
- factions;
- cultures/languages only if canon establishes them;
- discrimination/access rules where relevant;
- beasts/hazards;
- danger band;
- loot/resource provenance;
- named NPC anchors;
- supporting NPC capacity;
- current world-state modifiers;
- visual asset kit;
- map packet;
- scenes/quests;
- expansion routes.

## 4. Population model

Population records should use bands until exact population matters.

Track:
- residents;
- commuters/transients;
- workers;
- officials/security;
- students/trainees;
- merchants/service workers if economy exists;
- displaced/refugee population if authored;
- faction presence;
- named NPCs.

Do not generate precise demographic numbers without a system that uses them.

## 5. District model

Large settlements divide into districts with:
- district ID;
- function;
- bounds;
- population/activity;
- routes;
- landmarks;
- services;
- hazards;
- local power/faction presence;
- visual kit;
- local map.

Gate Twelve is a proof-region/district model and may later be nested inside a larger settlement once that parent is canonically established.

## 6. Service model

A service is not created because a building sprite exists.

Potential services include:
- administration;
- transit;
- medical;
- training;
- research;
- repair;
- trade;
- lodging;
- food;
- storage;
- law/security.

Each service requires actual gameplay/content authority before the UI exposes it.

## 7. Settlement economy

Each settlement eventually needs:
- imports;
- exports;
- labor;
- scarcity;
- wealth bands;
- major employers/institutions;
- resource dependency;
- route dependency;
- black/illegal market only if authored.

Item prices and vendor inventories remain economy-system outputs.

## 8. Named NPC anchors

Each settlement should identify:
- governance anchors;
- service anchors;
- faction anchors;
- narrative anchors;
- ordinary-life anchors.

Named NPCs use stable IDs and persistent state.

## 9. Visual production packet

Each settlement requires a reusable visual kit rather than one flattened image:
- terrain/surface tiles;
- building families;
- roof/wall/door/window modules;
- roads/paths;
- signage;
- props;
- vegetation;
- lighting;
- weather/state overlays;
- NPC actor families;
- unique landmarks;
- map icons;
- interiors;
- tactical tiles where combat occurs.

## 10. Catalog seed

Current confirmed local region:
- Gate Twelve District — governed by `docs/assets/GATE_TWELVE_REGION_MASTER_PLAN.md`.

Its larger settlement/city parent remains **UNDECIDED** and must not be invented by this catalog.

## 11. Expansion workflow

For every new settlement:
1. geography parent exists;
2. political relation exists or is explicitly independent;
3. route access exists;
4. resource/economic reason exists;
5. functional districts are outlined;
6. population/hierarchy is defined;
7. danger/balance is defined;
8. visual kit is planned;
9. content hooks are added;
10. runtime/map integration follows only after contracts are accepted.
