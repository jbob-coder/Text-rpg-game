# Branch Source Audit — context/shared-game-context

Status: **REVIEWABLE / SOURCE RECONCILIATION**
Repository: `jbob-coder/Text-rpg-game`
Source branch: `context/shared-game-context`
Source head at audit: `817b957ba7b6cd2beb9f13b3a268d1bce5e9f096`
Current authority branch: `docs/settlement-region-build-plan`
Purpose: extract usable continuity/world/history material without letting a campaign-specific branch silently override the current full-game program.

## Repository-scale context

Repository branch inventory at audit time:
- total branches: 60;
- non-main branches: 59;
- source branch total files: 369;
- `docs/world_history/**`: 332 files;
- `context/**`: 12 files;
- other `docs/**`: 5 files;
- `src/**`: 9 files;
- `tests/**`: 8 files;
- `content/**`: 1 file.

This source is therefore primarily a world-history/context corpus, not merely a code branch.

## Authority boundary

The source branch contains a campaign-specific authority file:

`BRANCH::context/shared-game-context::context/CURRENT_NARRATIVE_AUTHORITY.md`

That file explicitly limits itself to the narrated Jack/Elias campaign continuity and says Android/APK, open-world Android UI, and pixel-client work are not authoritative for that narrow campaign unless reintroduced.

Current program authority is broader and newer:
- `jbob-coder/Text-rpg-game` is the priority repository;
- the current program explicitly includes world, map, pixel art/assets/UI, gameplay systems, Android/APK, migration and rebuild work;
- repository documentation on `docs/settlement-region-build-plan` governs current documentation production.

Therefore:

> The campaign-specific exclusion boundary remains valid as historical provenance for that campaign, but it does not override the current whole-game documentation program.

Do not merge these two scopes silently.

## Source families

### 1. Campaign authority and continuity

Files:
- `context/CURRENT_NARRATIVE_AUTHORITY.md`
- `context/chats/text-rpg-foundation-chat/GAME_CONTEXT.md`
- `context/chats/text-rpg-foundation-chat/HANDOFF.md`
- `context/chats/text-rpg-foundation-chat/NARRATIVE_CANON_CORRECTION_2026-09-29.md`
- `context/chats/text-rpg-foundation-chat/VERIFIED_WORK.md`

Classification:
**KEEP AS HISTORICAL/CONTINUITY SOURCE + RECONCILE**

Use for:
- Jack Wilson continuity evidence;
- Steal identity continuity;
- provenance for narrative decisions;
- historical conflict records;
- future supersession maps.

Do not use these files to automatically suppress current application/UI/asset work.

### 2. World Director runtime model

Files:
- `context/world_director/WORLD_DIRECTOR_PROTOCOL.md`
- `context/world_director/LIVE_WORLD_STATE.md`
- `context/world_director/OFFSCREEN_SIMULATION.md`
- `context/world_director/WORLD_EVENT_LEDGER.md`
- `context/world_director/ACADEMY_CONTINUITY_ANCHOR.md`
- `context/world_director/README.md`

Classification:
**HIGH-VALUE SYSTEM SOURCE / REWRITE INTO CURRENT SYSTEM ARCHITECTURE**

Reusable concepts:
- multiple independent world clocks;
- causal world-event propagation;
- bounded actor knowledge;
- off-screen simulation;
- player-agency boundary;
- event ledger;
- live world-state persistence;
- Academy integration with wider world pressures.

Required current-program adaptation:
- separate narrated-campaign state from general game-system specification;
- replace campaign-only names/state with reusable schema where appropriate;
- connect NPC/faction/world clocks to D-03, D-04, D-05 and D-01;
- define persistence and save migration before implementation;
- preserve Jack user-agency constraints where still applicable.

### 3. World-history master architecture

Key files:
- `docs/world_history/WORLD_HISTORY_MASTER_INDEX.md`
- `docs/world_history/WORLD_HISTORY_AND_REFERENCE_MASTER_BUILD_PLAN.md`
- `docs/world_history/CANON_RECONCILIATION_REPORT.md`
- `docs/world_history/book/WORLD_HISTORY_BOOK_INDEX.md`
- book chapters under `docs/world_history/book/**`

Classification:
**HIGH-VALUE WORLD/CANON SOURCE / RECONCILE BEFORE PROMOTION**

Strong reusable architecture:
- readable world-history book plus structured reference encyclopedia;
- PUBLIC / CLASSIFIED / TRUE knowledge layers;
- stable historical entities/events;
- causal history rather than event lists;
- Academy derived from world history;
- scenario validation by era/region/biome/threat/species/faction/technology/legal context;
- protected protagonist mysteries;
- separation of First Interworld War causation from Homunculus plotline.

### 4. Historical canon-reconciliation evidence

Primary source:
`docs/world_history/CANON_RECONCILIATION_REPORT.md`

Classification:
**KEEP / HIGH PRIORITY**

Important already-documented conflict:
- older Homunculus species/rebellion/slavery framing conflicts with later owner direction;
- First Interworld War remains Human/Kharvori and must have independent causation;
- old conflicting material was intended to be preserved and superseded, not silently deleted.

Current-program implication:
- do not migrate obsolete Homunculus ontology into new corpus as confirmed canon;
- preserve it as historical evidence and explicit supersession material;
- current world/system documents should inherit only reconciled claims.

### 5. World-history subject registries

Observed source families include:
- eras;
- events;
- factions;
- organizations;
- laws;
- economy;
- ecology/ecosystems;
- education;
- medicine;
- military;
- labor;
- environment;
- crystals;
- contact;
- Kharvori;
- lineages;
- Academy/institutional history.

Classification:
**DOMAIN SOURCE / PER-FILE RECONCILIATION REQUIRED**

Target domains:
- D-01 World/Map/Regions;
- D-03 Characters/NPC/Social;
- D-04 Progression/Combat/Systems;
- D-05 Economy/Items/Ecosystem;
- later history/canon domain allocation within the numbered corpus.

### 6. Planning-round corpus

The branch contains a very large planning-round family covering at least:
- 001–100 initial world-history planning;
- 101–1000 expansion into spatial, cultural, economic, military, ecology, transport, institutions and scenario systems;
- 1011–1110 living-world simulation/causality;
- 1111–1210 runtime world-director integration;
- 1211–1510 deeper spatial/material/geography/place-history work.

Classification:
**PLANNING SOURCE, NOT COMPLETION EVIDENCE**

Important rule already present in the source:
a planning round records a design target/constraint; it does not mean the corresponding content or implementation exists.

Current-program handling:
- never convert “round complete” into “system implemented”;
- extract unique decisions/requirements;
- map those requirements to current domains;
- reject repetitive planning text that adds no unique ownership;
- use planning rounds as source nodes for future numbered documents rather than copying all files one-for-one.

## High-value reusable decisions

The following concepts are strong migration candidates, subject to current authority review:

1. World changes should follow causal chains rather than arbitrary plot movement.
2. Off-screen systems continue only according to elapsed in-game time and causal state.
3. NPCs/factions require goals, resources, knowledge, constraints and decision triggers.
4. World state should distinguish true/classified/public/player/NPC knowledge.
5. Maps and scenarios should be validated against time, location, access, ecology, law, technology and current state.
6. History should explain ordinary life, institutions, economy, ecology, technology, law and culture—not only major events.
7. Academy/world integration should be causal rather than isolated.
8. Creature/beast ecology should be a real ecosystem model rather than encounter inventory.
9. First Interworld War causation remains separate from the Homunculus network.
10. Protagonist mysteries should be explicitly protected rather than accidentally “completed” by omniscient worldbuilding.

## Known conflict/hold areas

Do not promote without explicit reconciliation:
- old `SPECIES_HOMUNCULUS_001` meaning;
- old Homunculus rebellion/slavery/custodial-order framing;
- any obsolete claim tying Homunculi directly to First Interworld War causation;
- campaign-specific Elias runtime state as general game canon;
- campaign-specific time anchors as universal application state;
- narrow campaign rule excluding Android/pixel work from current whole-game authority;
- any planning-round proposal that was never promoted to canon.

## Current domain mapping

| Source family | Current domain | Action |
|---|---|---|
| world history / eras / events | D-01 + future canon/history allocation | RECONCILE + INDEX |
| world director / clocks | D-03 / D-04 / D-05 / D-01 | REWRITE AS GENERAL SYSTEM CONTRACTS |
| Academy historical integration | D-01 / D-03 | RECONCILE |
| ecosystems / beasts | D-05 + D-01 | RECONCILE WITH CURRENT BEAST SCHEMA |
| economy / labor / services | D-05 | EXTRACT UNIQUE RULES |
| laws / social conflict | D-03 / D-01 | EXTRACT + VERIFY CURRENT DIRECTION |
| abilities | D-04 | COMPARE WITH RULES/ABILITY INTEGRATION BRANCHES |
| spatial atlases / routes / travel | D-01 | HIGH PRIORITY FOR LARGE WORLD MAP |
| runtime scenario/world director | D-07 + D-03/D-04/D-05 | GENERALIZE + SPECIFY |
| source Python/tests | implementation evidence | COMPARE, DO NOT AUTO-PROMOTE |

## Deep-audit work units generated from this branch

The branch justifies future bounded audit units for:
- WH-AUTH — authority/canon reconciliation;
- WH-HISTORY — historical eras/events/book;
- WH-WORLD — geography/regions/settlements/routes;
- WH-ECO — ecosystems/beasts/resources;
- WH-SOCIETY — law/culture/class/institutions;
- WH-ECON — economy/labor/services;
- WH-ABILITY — abilities/crystals/technology;
- WH-CONTACT — Kharvori/contact/interworld/war;
- WH-ACADEMY — institutional ancestry/present integration;
- WH-SIM — living-world simulation;
- WH-RUNTIME — runtime world director/scenario selection;
- WH-QA — scenario/canon/temporal/spatial validation.

These are audit families, not automatic numbered-document reservations.

## Verification completed

- source branch enumerated recursively;
- file-family counts recorded;
- campaign authority boundary read;
- world-director protocol read;
- live-world state read;
- off-screen simulation contract read;
- world-history master index reviewed;
- canon reconciliation report reviewed;
- master build plan reviewed;
- representative planning-round indexes reviewed.

## Current result

This branch contains a large amount of reusable world/history/simulation design, but it must not be copied wholesale.

The correct migration strategy is:
`source branch -> family audit -> reconcile -> deduplicate -> current-domain decision -> numbered ownership document -> implementation/test trace`.

## Next action

Continue BR-1 by auditing `docs/master-game-development-program` and compare its unique documentation against the current program and this source audit.