# THE GAME — Documentation Cross-Reference Matrix

Status: **ACTIVE INDEX**  
Parent authority: `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`

This file answers: **what does each major document own, what does it reference, what must be added next, and which implementation consumes it?**

---

## 1. Authority order

| Document | Owns | Must not own |
| --- | --- | --- |
| `MASTER_GAME_DEVELOPMENT_PROGRAM.md` | repository priority, program scope, permissions, documentation sequence | low-level implementation details |
| `THE_GAME_MASTER_TASK_REGISTER.md` | operational task state | gameplay canon |
| `IMPLEMENTATION_STATUS.md` | verified current implementation snapshot | future design treated as implemented |
| `GAME_CONTEXT_LOGS/*` | durable user decisions/context | overriding live source/evidence |
| domain master docs | design contracts | hidden runtime facts not represented in source |

---

## 2. Existing core documents

### `docs/GAME_FOUNDATION.md`
Purpose:
- core game direction;
- high-level rules-engine philosophy.

Needs:
- audit against current master program;
- link to world/progression/combat/social volumes;
- contradictions logged rather than silently edited.

### `docs/VISUAL_BIBLE.md`
Purpose:
- general visual identity.

Needs:
- reconcile with current pixel-production standards;
- explicitly defer technical grids/anchors to `PIXEL_ASSET_MASTER_PLAN.md`;
- explicitly defer room/actor/overlay composition to `PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`.

### `docs/IMPLEMENTATION_STATUS.md`
Purpose:
- exact verified implementation state.

Current issue:
- still frames V6 stabilization as the current objective.

Required update:
- preserve V6 evidence as historical;
- point current objective to documentation-first master program;
- list current Android/pixel/map branch stack as separate development evidence.

### `docs/V6_STABILIZATION_HANDOFF.md`
Purpose:
- historical evidence for engine stabilization.

Status:
- keep;
- do not rewrite into current project roadmap;
- label as historical engine handoff in higher-level indexes.

### `docs/THE_GAME_MASTER_TASK_REGISTER.md`
Purpose:
- operational queue.

Required update:
- P0 documentation program;
- priority-repository marker;
- Gate Twelve document sequence;
- world master;
- pixel runtime composition;
- final APK rebuild as late-stage task.

---

## 3. Pixel-art documentation

### `docs/assets/PIXEL_ASSET_MASTER_PLAN.md`
Owns:
- native grids;
- global pixel rules;
- character rig;
- scene/map/item standards;
- lifecycle;
- naming;
- quality gates.

References:
- character blueprints;
- production roadmap;
- manifests.

Needs:
- new link to runtime composition standard;
- explicit distinction between source-native master and scene composition;
- current player approved-reference pointer.

### `docs/assets/CHARACTER_PIXEL_BLUEPRINTS.md`
Owns:
- player body rig;
- Tamsin identity;
- anchors;
- equipment layering;
- character animation principles.

Needs:
- reconcile old “customizable generic player master” language with the later owner-approved Jack reference where current branch evidence supports it;
- never overwrite identity reference without provenance;
- add actor-panel/portrait mapping once projected actor contract exists.

### `docs/assets/REFERENCE_TO_BLUEPRINT_PIPELINE.md`
Owns:
- how external/generated reference becomes original source-native pixel art.

Needs:
- continue to prohibit direct smooth-image shipping;
- add exception only for already-valid deliberately authored pixel raster when QA proves it matches the production grid.

### `docs/assets/ASSET_PRODUCTION_ROADMAP_001-500.md`
Owns:
- first 500 planned visual units.

Status:
- planning baseline, not total world asset count.

Needs:
- eventual superseding roadmap for world-scale batches without renumbering or silently repurposing existing IDs.

### `docs/assets/GATE_TWELVE_MAP_PIXEL_ASSET_BLUEPRINT.md`
Owns:
- Gate Twelve visual geometry -> asset specification.

References:
- map master;
- area footprints;
- existing/code-present asset IDs.

Needs:
- remain subordinate to Gate Twelve Region Master Plan for region function/circulation;
- geometry changes require Step 5 geometry-contract update.

### `docs/assets/GATE_TWELVE_MAP_ANIMATION_BLUEPRINT.md`
Owns:
- static/ambient/state-driven animation classes;
- timing families;
- bounded first loops.

Needs:
- keep state-driven animations player-safe;
- later animation implementation must attach to runtime composition layers.

### `docs/assets/GATE_TWELVE_ASSET_STATUS_AND_PRODUCTION_MATRIX.md`
Owns:
- Batch 001 exact-ID/status audit;
- Gate Twelve per-area asset requirements;
- manifest/code drift;
- open-refinement separation;
- production ordering.

Current stage:
- Step 7 evidence source.

### `docs/assets/GATE_TWELVE_REGION_MASTER_PLAN.md`
Owns:
- region authority;
- spatial hierarchy;
- circulation;
- per-zone gameplay function;
- next: geometry contract, materials, asset decomposition, UX, state layers, loading, implementation, verification, migration.

Current stage:
- Steps 1–7 complete;
- Step 8 Application UX plan next.

### `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`
Owns:
- how base art, characters, props, overlays, equipment, FX and panels coexist;
- reusable compatibility contract;
- actor-in-room rules;
- current-vs-planned asset-stage ledger.

This is the required bridge between visual documentation and actual Android composition.

---

## 4. World documentation

### `docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`
Owns:
- world hierarchy;
- coordinate hierarchy;
- map-development records;
- political entities;
- settlements;
- ecosystems;
- resource zones;
- beast zones;
- population/NPC distribution;
- progression/world-level interaction.

Required future children:
- `WORLD_GEOGRAPHY_STANDARD.md`
- `WORLD_POLITICAL_ENTITIES.md`
- `WORLD_SETTLEMENT_CATALOG.md`
- `WORLD_ECOSYSTEM_AND_RESOURCES.md`
- `WORLD_BEAST_ZONE_STANDARD.md`
- `WORLD_TRAVEL_AND_ROUTES.md`
- `WORLD_POPULATION_AND_CITIZEN_HIERARCHY.md`
- `WORLD_BALANCE_AND_LEVEL_BANDS.md`

Do not create thousands of fictional records before schemas and Gate Twelve proof are stable.

---

## 5. Gameplay-system documentation still required

### Progression master
Planned:
`docs/systems/PROGRESSION_MASTER_PLAN.md`

Must define:
- attributes;
- derived stats;
- skill taxonomy;
- ability taxonomy;
- passives;
- techniques;
- classes;
- professions;
- ranks;
- mastery;
- training;
- caps;
- resources;
- balance.

### Combat master
Planned:
`docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md`

Must define:
- turn model;
- action economy;
- grid/positioning;
- cover;
- line-of-sight;
- targeting;
- movement;
- abilities;
- status/injury;
- AI;
- encounter persistence;
- tactical UI;
- tests.

### Social/NPC/rival master
Planned:
`docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md`

Must define:
- memory;
- goals;
- schedules;
- social relationships;
- hierarchy;
- recurring rival state;
- rank changes;
- encounter memory;
- faction propagation;
- persistence;
- original-system constraints.

### Economy/items master
Planned:
`docs/systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md`

Must define:
- item taxonomy;
- accessories;
- materials;
- quality;
- loot;
- resources;
- beast drops;
- repair/crafting only if approved;
- economy.

---

## 6. Android / APK documentation

### `docs/android/APK_REBUILD_AND_EVOLUTION_MASTER_PLAN.md`
Owns:
- late-stage audit;
- keep/rework/replace/remove classification;
- screen rebuild order;
- state-projection migration;
- visual integration;
- build/QA;
- APK evidence.

References:
- final world/system/visual contracts.

Rule:
- final APK reconstruction happens after the major design corpus is coherent enough to know what is being rebuilt.

---

## 7. Runtime/source documents

### `content/vertical_slice_01.json`
Owns:
- current provisional playable content.

Does not own:
- future world design;
- map art;
- speculative services.

### Python engine
Owns:
- authoritative gameplay state/rules.

### Android Compose
Owns:
- presentation and permitted actions.

### Asset catalogs/manifests
Own:
- renderable visual masters and their provenance/state binding.

---

## 8. Current implementation branches / PR lines

Repository work is currently distributed across stacked draft PRs.

Important current lines include:
- map authored art;
- player avatar refinement;
- opening story actors;
- mobile Bag;
- mobile Skills;
- Service Tunnel arrival/scene/atlas work;
- Quiet Stair refinement;
- Gate Twelve geometry documentation;
- Service Tunnel ambient animation.

Do not treat “open PR” as “canonical merged implementation.”

Each document that cites implementation must include exact branch/HEAD when it matters.

---

## 9. Required update rule

Whenever a major new document is created:

1. add it here;
2. add it to the relevant domain README/index;
3. add an operational task to the task register if implementation follows;
4. record user-decision context when the change originates from a conversation directive;
5. identify what older document it supplements or supersedes;
6. never erase old evidence solely because the roadmap evolved.

---

## 10. Next documentation sequence

1. finish Gate Twelve Step 5–14;
2. build existing-state audit;
3. build world geography schema;
4. build progression master;
5. build NPC/social/rival master;
6. build tactical combat master;
7. build items/economy/loot master;
8. build application UX master;
9. build final Android migration matrix;
10. only then schedule broad system reconstruction.
