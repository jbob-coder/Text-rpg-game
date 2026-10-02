# THE GAME — World Political Entities

Status: **ACTIVE / STANDARD + EMPTY CATALOG SEED**  
Parent: `docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`

## 1. Purpose

This document defines how kingdoms, states, city-states, federations, autonomous territories, factions with territorial authority, and other political entities are documented.

No kingdom or government is invented here solely to fill the catalog. The schema is established first; entries are added only when world canon is authored.

## 2. Political entity record

Each entity requires:
- `political_id`;
- official name;
- common name;
- entity type;
- founding/formation status;
- claimed territory;
- controlled territory;
- capital/administrative center;
- major settlements;
- governing structure;
- succession/leadership model;
- legal system;
- military/security institutions;
- economic base;
- resource dependencies;
- external relations;
- internal factions;
- citizenship/residency rules;
- social hierarchy;
- languages/cultures if canon establishes them;
- discrimination/prejudice policies where relevant;
- beast-zone policy;
- travel/border rules;
- current conflicts;
- player-facing known state;
- hidden/developer state;
- map/document pointers.

## 3. Government structure

Represent institutions separately:
- executive/leader;
- council/legislature;
- courts;
- bureaucracy;
- military;
- policing;
- local government;
- guild/merchant power;
- religious authority if present;
- emergency authority.

Do not flatten an entire society into one ruler personality.

## 4. Social hierarchy

Political records may reference:
- legal status;
- citizenship;
- residency;
- wealth class;
- occupation/profession;
- institutional rank;
- military rank;
- faction standing;
- lineage/culture/species only where canon establishes them.

Effects belong in social/legal systems, not in a single universal “class” integer.

## 5. Discrimination and prejudice

When the world includes racism, species prejudice, caste discrimination, xenophobia, classism, or comparable systems, document separately:
- law/policy;
- institutional enforcement;
- local cultural norm;
- faction doctrine;
- individual NPC belief;
- historical cause;
- economic incentive;
- propaganda;
- resistance/activism;
- player-access consequences;
- change over time.

Do not use one global “racism meter.”

## 6. Territorial control

Every territory claim should distinguish:
- claimed;
- controlled;
- occupied;
- disputed;
- autonomous;
- frontier/unadministered.

Map UI exposes only what the player is allowed to know.

## 7. Conflict record

A conflict requires:
- conflict ID;
- participants;
- cause;
- start/status;
- geography;
- objectives;
- civilian effects;
- economic effects;
- route effects;
- beast/ecosystem effects;
- faction/NPC effects;
- quest hooks;
- resolution states.

## 8. Economy relationship

Political entities do not directly define item prices. They provide factors:
- taxes;
- tariffs;
- legal restrictions;
- monopolies;
- resource ownership;
- labor rules;
- currency policy if a currency system exists;
- infrastructure.

Economy systems consume those factors.

## 9. Military/security scale

Record:
- institution;
- rank structure;
- recruitment;
- training;
- equipment bands;
- deployment geography;
- command relations;
- legal authority;
- threat response;
- beast-response doctrine.

Exact combat stats belong to balance/combat documents.

## 10. Catalog status

Current canon entries: **not yet populated at world scale**.

Gate Twelve's municipal institutions demonstrate local civic infrastructure but do not by themselves establish a kingdom/state model.

## 11. Entry acceptance

A new political entity is accepted only when:
- its territory fits geography;
- settlements/routes can reference it;
- its institutions are distinguishable;
- its social hierarchy is documented;
- its resources/economy have plausible support;
- its conflicts do not contradict existing canon;
- it has stable IDs and cross-links.
