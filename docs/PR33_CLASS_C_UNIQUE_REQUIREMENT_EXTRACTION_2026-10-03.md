# PR #33 Class-C Unique-Requirement Extraction — 2026-10-03

Status: **ACTIVE D-044 EVIDENCE / EXTRACTION PLAN / NO WHOLE-HIERARCHY MIGRATION**

Repository: `jbob-coder/Text-rpg-game`

Program branch source-audit head:
`docs/master-game-development-program@835a028d7c84bfcdced4e954d9f0acbcb492480e`

Moving target branch audited:
`docs/settlement-region-build-plan@65d2db8538c1b8302c314f2fbe9eb7a1b585b51d`

Merge base:
`c261b2aaf8bd978d27b46f8fea03435c0c5734d0`

Parents:
- [PR #33 moving-base drift reconciliation](PR33_MOVING_BASE_DRIFT_RECONCILIATION_2026-10-02.md)
- [Moving-base document crosswalk](BASE_BRANCH_DOCUMENT_CROSSWALK_2026-10-02.md)
- [Live shared-file reconciliation](PR33_LIVE_SHARED_FILE_RECONCILIATION_2026-10-03.md)

## 1. Purpose

Resolve D-044's remaining Class-C / `EXTRACT UNIQUE` work without importing the moving branch's duplicate `docs/program/*` authority hierarchy.

The extraction rule is:

`inspect exact base source -> compare current owner -> keep unique non-conflicting requirement -> adapt to current authority vocabulary -> link provenance -> leave stale status/history behind`

A requirement is not promoted to gameplay canon merely because it is useful.

Game/system proposals remain labeled as proposed or unresolved where the current program has not already established them.

## 2. Source set audited

| Moving-base source | Blob | Current disposition |
| --- | --- | --- |
| `docs/program/09_DECISION_GAP_REGISTER.md` | `8129f57d3d9458970c4c41c1dac5da9018534b83` | **EXTRACT CLOSURE RULE ONLY** |
| `docs/program/10_EXECUTION_COORDINATION_GRAPH.md` | `22318ac60cad6164d2b8cc670e6d5dbd0a66c466` | **EXTRACT GRAPH SEMANTICS / FAILURE-HANDOFF RULES** |
| `docs/program/12_DOCUMENT_EXPECTATION_AND_ACCEPTANCE_STANDARD.md` | `0f952e7faf2f92f9a0315d8f5a81341abcf5c6c2` | **EXTRACT SUBSTANTIAL UNIQUE QA CONTRACT** |
| `docs/program/13_BEAST_ENTITY_ECOSYSTEM_AND_SCENE_PRESENCE_STANDARD.md` | `96fcb08649c5d5564bf27fca5b754ada5479ae23` | **EXTRACT BEAST PRESENCE / MIXED-SCENE REQUIREMENTS** |
| `docs/program/14_DOCUMENTATION_COVERAGE_AND_EXPECTATION_MATRIX.md` | `0b984f95d91d2e0f33863edc9b2098ceff8c8bc1` | **HISTORICAL STATUS MATRIX / NO ACTIVE IMPORT** |
| `docs/program/15_CONTEXTUAL_BEAST_PRESENCE_ADDENDUM.md` | `d1708154489f7320f75f285e4763acb79b3ac662` | **MERGE UNIQUE PRESENCE RULES INTO CURRENT VISUAL OWNER** |
| `docs/systems/PERSISTENT_ADVERSARY_SYSTEM.md` | `d32d31a5f0f8243ae4d400270f7ec807fe6aecdf` | **EXTRACT BOUNDED ADVERSARY MECHANICS** |
| `docs/world/BEAST_ZONE_AND_ECOSYSTEM_SCHEMA.md` | `edfb5dc7fcf9d43216932bf698a37e2b5d3bda98` | **EXTRACT DENSITY / REPOPULATION / PRESSURE / READINESS** |
| `docs/world/WORLD_MAP_PRODUCTION_SEQUENCE.md` | `dc309869f89a2f555266cc3b5bbc59c16240e89e` | **MOSTLY COVERED; EXTRACT MAP-LEVEL PRODUCTION GATE ONLY** |

## 3. Decision-gap register

### Current owner

- `docs/world/WORLD_CANON_DECISION_QUEUE.md`
- `docs/THE_GAME_MASTER_TASK_REGISTER.md`
- `docs/DECISION_AND_REBUILD_EXECUTION_REGISTER.md`

### Base material that is stale

The GAP-001 through GAP-024 status table is a 2026-10-02 snapshot.

Many statuses have already changed:

- Gate Twelve Steps 1-14 are complete as documentation;
- D-030 projection contract exists;
- asset provenance has advanced;
- D-029/D-044 have later evidence.

Do not import that table as a second active gap registry.

### Unique rule to preserve

A gap closes only when:

1. the decision is durable in repository documentation;
2. conflicts/superseded alternatives are reconciled;
3. downstream owners are updated;
4. implementation-facing gaps include acceptance/verification criteria.

A chat statement by itself is not repository closure.

Disposition:

`EXTRACT -> DECISION_AND_REBUILD_EXECUTION_REGISTER`

## 4. Execution coordination graph

### Current owners

- `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`
- `docs/MASTER_DIRECTIVE_EXECUTION_BREAKDOWN.md`
- `docs/DOCUMENTATION_CROSS_REFERENCE_MATRIX.md`
- `docs/THE_GAME_MASTER_TASK_REGISTER.md`

The current program already contains execution phases, dependency graphs, cross-references, rollback boundaries and task continuity.

### Unique requirement

The moving-base document contributes an explicit relationship vocabulary:

`G = (V, E)`

Useful node classes:

- requirement;
- decision;
- document;
- world entity;
- system;
- repository file;
- implementation task;
- asset;
- test;
- risk;
- evidence.

Useful edge semantics:

- Decision -> constrains -> Document;
- Document -> specifies -> System;
- System -> implemented_by -> File;
- Test -> verifies -> Behavior;
- Asset -> renders -> State;
- Location -> belongs_to -> Region;
- Route -> connects -> Location;
- Gap -> blocks -> Task;
- Decision -> supersedes -> Decision.

This is a documentation/reconstruction model, not a runtime database requirement.

Also retain the failure/recovery expectation for consequential work:

- failure mode;
- detection;
- state/data preserved;
- rollback or compensating action;
- exact evidence required before success.

Disposition:

`EXTRACT -> DOCUMENTATION_CROSS_REFERENCE_MATRIX / reconstruction graph guidance`

Do not activate the old `docs/program/*` graph as a second task system.

## 5. Documentation expectation and acceptance standard

### Current owners

- `docs/DOCUMENTATION_CORPUS_ARCHITECTURE.md`
- `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`
- `docs/DOCUMENTATION_CROSS_REFERENCE_MATRIX.md`

The current corpus architecture already owns unit types, metadata, hierarchy, no-filler intent, supersession and reconstruction use.

### Materially unique requirements

The moving-base standard adds a concise per-document QA contract that is not fully expressed in one current active standard:

- mandatory ownership/non-ownership questions;
- current/target/delta/migration/acceptance separation;
- decision-completeness record;
- domain-specific expectations for assets/world/systems;
- explicit upstream/downstream references;
- document quality states;
- anti-filler acceptance;
- batch audit cadence.

The evidence labels in the moving-base standard are **not** copied verbatim because the owner's current handoff defines the active classification vocabulary:

- VERIFIED CURRENT IMPLEMENTATION;
- ESTABLISHED DESIGN/CANON;
- PROPOSED DESIGN;
- INFERENCE;
- UNKNOWN;
- BLOCKED;
- DEPRECATED;
- MIGRATION REQUIRED;
- OWNER DECISION REQUIRED.

Disposition:

`EXTRACT -> new top-level DOCUMENTATION_EXPECTATION_AND_ACCEPTANCE_STANDARD.md subordinate to corpus/master authority`

## 6. Beast entity/ecosystem/scene-presence standards

### Current owners

- `docs/world/WORLD_BEAST_ZONE_STANDARD.md`
- `docs/world/WORLD_ECOSYSTEM_AND_RESOURCES.md`
- `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`
- `docs/assets/ROOM_ACTOR_PANEL_OVERLAY_REUSE_STANDARD.md`

Current world owners already cover:

- beast species records;
- beast zones;
- ecology;
- threat dimensions;
- body-part/resource conditions;
- encounter inputs;
- human interaction;
- originality boundaries.

### Unique presence requirements

The moving-base beast documents add visual/presentation requirements currently absent from the active composition standards:

- presentation may render a beast only from authoritative/player-safe presence;
- mixed scenes must support characters and beasts simultaneously;
- beast focus must expose only observed/learned information;
- absent beasts must not render merely because art exists;
- missing beast art must not substitute another species;
- pack/group scenes must preserve identities when gameplay distinguishes individuals;
- ordinary character social models must not be reused as beast truth;
- beast rendering participates in the same environment/actor/overlay/FX stack while keeping separate state ownership.

The B0-B4 labels in the moving branch are useful descriptive modes, but they are not required as permanent runtime enum names.

Disposition:

`EXTRACT -> current room/composition standard as PROPOSED TARGET BEAST-PRESENCE EXTENSION`

## 7. Beast-zone/ecosystem schema

### Current owners

- `docs/world/WORLD_BEAST_ZONE_STANDARD.md`
- `docs/world/WORLD_ECOSYSTEM_AND_RESOURCES.md`

### Already covered

Current owners already contain:

- stable beast/zone identities;
- parent region/ecosystem;
- habitat;
- species;
- migration;
- population;
- threat;
- resources;
- human/faction pressure;
- ecosystem predator/prey relationships;
- extraction pressure;
- persistence principles.

### Unique schema detail to preserve

The moving-base schema adds:

**Planning density vocabulary**
- absent;
- trace;
- sparse;
- ordinary;
- dense;
- concentrated;
- migration surge;
- displaced.

**Migration boundary**
- beast migration routes are not player travel routes;
- map visualization remains player-knowledge gated.

**Repopulation model options**
- authored reset;
- time-based recovery;
- resource-driven recovery;
- migration-driven refill;
- persistent depletion;
- event-driven change.

No model is selected globally.

**Hunting/harvesting pressure consequences**
- local density;
- behavior;
- resource quality;
- migration;
- settlement economy;
- quests/events;
- faction reaction.

**Readiness gate**
A concrete beast zone is not implementation-ready until identity, parent, space/boundary, species, threat/density meaning, encounter relationship, resource relationship, discovery/map behavior, persistence and runtime-required unknowns are resolved.

Disposition:

`EXTRACT -> WORLD_BEAST_ZONE_STANDARD / WORLD_ECOSYSTEM_AND_RESOURCES`

These are schema capabilities, not claims that simulation depth is already implemented.

## 8. Persistent adversary architecture

### Current owner

`docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md`

The current master already includes:

- persistent NPC rival state;
- encounter memory;
- injuries/scars;
- faction rank/status evolution;
- succession/replacement;
- rival events;
- player-safe rival intel;
- social/economic integration;
- pixel-art integration;
- originality/patent-review caution.

### Unique bounded mechanics to preserve

The moving-base architecture contributes:

- not every hostile entity becomes persistent;
- possible persistent category may include a beast where the beast/world design supports it;
- adaptation may affect tactics/equipment/resistance/route/allies/territory/retreat behavior but must stay within authored bounds;
- adaptation must not become arbitrary stat inflation;
- recurrence selection should depend on territory/location, world state, availability, player history, faction/pack state, authored timing/cooldown and quest/event conditions;
- do not force a rival into unrelated scenes merely to show the system;
- persistent lifecycle needs explicit authoritative states such as active/injured/recovering/displaced/captured/retired/dead/unknown;
- selection/adaptation may use seeded deterministic variation but state transitions must remain inspectable/testable;
- acceptance should prove promotion, memory, consequence-driven change, valid recurrence, player-safe projection, save/load and clean retirement/removal.

Disposition:

`EXTRACT -> NPC_SOCIAL_AND_RIVAL_MASTER_PLAN as PROPOSED TARGET DETAIL`

No exact counts, formulas, recurrence timer or death policy are selected.

## 9. Documentation coverage matrix

The moving-base coverage matrix is primarily a status snapshot.

Its useful quality legend is already part of the acceptance-standard extraction.

Its domain statuses are stale relative to the current task register and newer masters.

Disposition:

`HISTORICAL / NO ACTIVE STATUS MIGRATION`

Do not create a second coverage authority from this file.

## 10. World-map production sequence

### Current owner

`docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`

Current section 24 already defines a hierarchy-first map-development production program:

- lock schemas;
- finish the Gate Twelve pilot;
- establish parent settlement/city;
- expand surrounding routes/districts;
- establish political/ecological context;
- expand outward.

### Unique process detail

The moving-base process contributes a reusable map-detail hierarchy:

- L0 world;
- L1 region;
- L2 settlement;
- L3 district;
- L4 location/interior.

Each level may use its own coordinate space.

The production gate requires before map art:

- stable entity IDs;
- clear parent/child hierarchy;
- authored/proposed routes;
- declared coordinate space;
- visible major gaps;
- documented visual language.

Also preserve:

- do not draw detailed city blocks before city/region purpose exists;
- do not create route art before route entity/endpoints exist;
- do not reveal hidden destinations in art before discovery rules exist.

Disposition:

`EXTRACT SMALL PROCESS GATE -> WORLD_DEVELOPMENT_MASTER_INDEX`

No separate active `WORLD_MAP_PRODUCTION_SEQUENCE.md` is needed on the program branch.

## 11. Migration queue

The following extraction actions are authorized by D-044's selective-migration rule:

1. create current top-level documentation expectation/acceptance standard;
2. add gap-closure rule to current decision/rebuild register;
3. add graph node/edge semantics to current cross-reference guidance;
4. add beast-presence extension to current composition/room standard;
5. add beast density/repopulation/pressure/readiness detail to current world owner;
6. add bounded adversary adaptation/recurrence/lifecycle detail to current rival master;
7. add L0-L4 map-production gate to current world master index.

Each extraction must:

- identify moving-base provenance;
- remain subordinate to the current owner;
- avoid creating duplicate active authority;
- preserve proposals/unknowns as proposals/unknowns;
- not claim implementation.

## 12. Files intentionally not migrated wholesale

Do not copy these complete files onto the program branch as parallel active authorities:

- `docs/program/09_DECISION_GAP_REGISTER.md`;
- `docs/program/10_EXECUTION_COORDINATION_GRAPH.md`;
- `docs/program/12_DOCUMENT_EXPECTATION_AND_ACCEPTANCE_STANDARD.md`;
- `docs/program/13_BEAST_ENTITY_ECOSYSTEM_AND_SCENE_PRESENCE_STANDARD.md`;
- `docs/program/14_DOCUMENTATION_COVERAGE_AND_EXPECTATION_MATRIX.md`;
- `docs/program/15_CONTEXTUAL_BEAST_PRESENCE_ADDENDUM.md`;
- `docs/systems/PERSISTENT_ADVERSARY_SYSTEM.md`;
- `docs/world/BEAST_ZONE_AND_ECOSYSTEM_SCHEMA.md`;
- `docs/world/WORLD_MAP_PRODUCTION_SEQUENCE.md`.

Their exact blobs remain historical evidence through this extraction record.

## 13. Completion definition

This Class-C slice becomes complete when:

- the seven migration actions above are written into current owners;
- indexes/cross-references point to the current owners, not `docs/program/*`;
- no numerical-unit-dependent corpus machinery is activated;
- both branch refs are re-resolved;
- PR #33 mergeability is reassessed.

Until then:

`D-044 CLASS-C EXTRACTION = IN_PROGRESS`.
