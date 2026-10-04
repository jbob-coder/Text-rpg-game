# THE GAME — Documentation Cross-Reference Matrix

Status: **ACTIVE INDEX**  
Parent authority: `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`

This file answers: **what does each major document own, what does it reference, what must be added next, and which implementation consumes it?**

---

## 1. Authority order

| Document | Owns | Must not own |
| --- | --- | --- |
| `MASTER_GAME_DEVELOPMENT_PROGRAM.md` | repository priority, program scope, permissions, documentation sequence | low-level implementation details |
| `MASTER_DOCUMENTATION_RECORD.md` | consolidated documentation status: exists / done / partial / missing / blocked / next | detailed domain design or runtime facts not supported by source/evidence |
| `THE_GAME_MASTER_TASK_REGISTER.md` | operational task state | gameplay canon |
| `IMPLEMENTATION_STATUS.md` | verified current implementation snapshot | future design treated as implemented |
| `GAME_CONTEXT_LOGS/*` | durable user decisions/context | overriding live source/evidence |
| domain master docs | design contracts | hidden runtime facts not represented in source |

---

## 1.1 Parallel execution authorities

Two program-level companions now govern breadth and playable integration:

### `docs/FIRST_PASS_DOMAIN_DOCUMENTATION_QUOTAS.md`
Owns:
- first-pass minimum canonical documentation quotas by V00–V12;
- anti-filler counting rules;
- breadth-before-extreme-depth direction;
- later quota recalibration gate.

### `docs/PHASE_1_SOLO_PLAYABLE_PARALLEL_TRACK.md`
Owns:
- bounded Gate Twelve solo-playable requirements;
- Track A / Track B / Track C synchronization model;
- Phase 1 implementation gate and exit criteria;
- task-completion impact/update requirements.

Every domain master should feed one or both of these authorities when its maturity changes.

## 2. Existing core documents

### `docs/systems/CAMERA_AND_TACTICAL_PRESENTATION_STANDARD.md`
Purpose:
- lock the primary three-quarter 2D/2.5D camera language;
- define exploration, tactical-combat and map framing relationships;
- lock square-grid, turn-based, action-budget tactical direction;
- define tap-first phone interaction, directional cover, LOS/detection/knowledge separation, companion control direction and persistent aftermath;
- establish Galaxy A02-class hardware as a product target requirement without claiming current device verification.

Consumes:
- tactical combat master;
- application UX master;
- pixel-art runtime composition;
- authoritative player-safe state rules.

Feeds:
- future tactical coordinate/schema work;
- combat UI/projection work;
- combat asset specifications;
- performance-budget documentation;
- bounded combat prototypes.


### `docs/MASTER_DOCUMENTATION_RECORD.md`
Purpose:
- one canonical control record for what documentation exists;
- separate completed contract layers from incomplete content/runtime work;
- list missing work, blockers, authority links and next execution order;
- preserve exact audited path-count context without treating counts as semantic completion.

Maintenance:
- update whenever a major documentation area's state, blocker, authority or next action changes;
- reconcile stale task-register NEXT text when newer repository files materially change the state;
- do not absorb full domain content that belongs in the linked master/child documents.

### `docs/DEEP_SOURCE_EXISTING_STATE_AUDIT_2026-10-04.md`
Purpose:
- exact current-head source inventory for Python engine modules, Android application/runtime files, authored content, durable save fields, raster assets, tests and build/workflow surfaces;
- attach current KEEP / EXTEND / REWORK / replacement-direction dispositions without treating them as deletion permission.

Consumes:
- existing-state decision matrix;
- live repository audit;
- Android consumer map;
- asset provenance work.

Still needs:
- field-level consumer mapping;
- cross-branch survivor reconciliation;
- final zero-consumer/deprecation evidence;
- exact runtime execution evidence when implementation changes resume.

### `docs/android/ANDROID_CONSUMER_FIELD_AUDIT_2026-10-04.md`
Purpose:
- exact current Android field/action/screen consumer map;
- connect Python player-safe payloads to Kotlin mapper, ViewModel actions, Compose consumers, direct pixel-catalog dependencies and test surfaces.

Owns:
- current-source consumer evidence only.

Must not own:
- future domain rules;
- final projection schemas not yet accepted;
- asset canon/provenance decisions.

Still needs:
- per-entry asset consumer/zero-consumer audit;
- remaining navigation/temporary-state audit;
- implementation/equivalence evidence for future projection migrations.

### `docs/IMPLEMENTATION_SURVIVOR_MIGRATION_MATRIX_2026-10-04.md`
Purpose:
- one final D-020 survivor/migration classification for implementation PRs #7–#31;
- distinguish inherited current behavior from superseded historical surfaces and deferred branch-only candidates;
- define the migration rule and owner/technical blocker for every divergent implementation line.

Consumes:
- exact PR #7–#31 reconciliation;
- source/raster provenance;
- Android consumer audit;
- ambient-animation migration contract.

Feeds:
- D-029 asset promotion/provenance;
- D-030 actor/room projection migration;
- D-032 mechanics migration;
- D-033/final APK teardown.

### `docs/assets/CURRENT_ASSET_CONSUMER_ZERO_CONSUMER_AUDIT_2026-10-04.md`
Purpose:
- resolve consumer presence for each of the 24 current runtime PNGs;
- distinguish currently consumed rasters from deferred/noncurrent zero-consumer candidates;
- provide deletion-safety evidence for D-029 and later APK teardown work.

Result:
- 24 / 24 current PNGs have a consumer path;
- 0 current PNGs are zero-consumer deletion candidates.

Must not own:
- canon/visual approval;
- raster-equivalence execution;
- final deletion decisions after future architecture changes.

### `docs/assets/VISUAL_SURVIVOR_OWNER_DECISION_PACKET_2026-10-04.md`
Purpose:
- isolate the two remaining D-029 static-scene owner choices;
- prevent newer divergent branches from being mistaken for automatically preferred art;
- define safe default and post-selection migration/verification gates.

Decision IDs:
- `D029-VIS-001` — Service Tunnel current baseline vs PR #27;
- `D029-VIS-002` — Quiet Stair current baseline vs PR #30.

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
- geometry contract;
- material/visual language;
- asset decomposition;
- Gate Twelve application UX;
- state layers;
- loading/performance;
- implementation order;
- verification;
- migration/removal;
- execution handoff.

Current stage:
- Steps 1–14 complete as the first proof-region planning packet;
- next consumer is exact implementation/asset reconciliation, not another region-planning step.

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

## 5. Original requirements list — domain masters now materialized

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

### Progression evolved target design

`docs/systems/PROGRESSION_CLASSES_RANKS_EVOLVED_GAME_DESIGN.md`

Owns:
- CURRENT REALITY versus EVOLVED GAME DESIGN separation for progression;
- preservation of the current seven-attribute / 23-skill / mastery foundation as reference-game identity;
- target progression network across skills, abilities, techniques, classes, specializations, professions, ranks, knowledge and world access;
- training, mentors, facilities, injury/recovery, equipment, world, NPC and tactical-combat integration;
- Gate Twelve progression proof requirements;
- child-document and content-creation requirements.

Supplements rather than replaces `PROGRESSION_MASTER_PLAN.md`. It is target-game design, not evidence that target features already exist.

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

## 10. Historical initial sequence — superseded by operational continuation

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

## 11. 2026-10-02 expansion documents

### `docs/MASTER_DIRECTIVE_EXECUTION_BREAKDOWN.md`
Owns:
- ordered program phases;
- broad permission interpretation;
- stop rules;
- dependency order.

References:
- Master Development Program;
- task register;
- all domain masters.

### `docs/EXISTING_STATE_REWORK_DECISION_MATRIX.md`
Owns:
- top-level KEEP / EXTEND / REWORK / REPLACE / REMOVE / NEW decisions.

Does not replace:
- the deeper source-file audit still required by task D-006.

### `docs/DOCUMENTATION_PROGRESS_LEDGER.md`
Owns:
- numeric target preservation;
- separate corpus metrics;
- completion-count rules.

### `docs/assets/PIXEL_ART_PRODUCTION_AND_REUSE_LEDGER.md`
Owns:
- production stages;
- current-vs-required asset lists;
- room actor/portrait/panel relationship;
- reuse classes;
- area packet requirements;
- text/overlay rules.

References:
- runtime composition standard;
- character blueprints;
- Gate Twelve asset matrix;
- manifests.

### `docs/world/WORLD_SCALE_DOCUMENTATION_BLUEPRINT.md`
Owns:
- world coordinate layers;
- place/political/settlement/resource/ecosystem/beast-zone/population schemas;
- map-record tracking rules.

References:
- world master index;
- future world child catalogs.

### `docs/systems/GAMEPLAY_SYSTEM_REBUILD_MATRIX.md`
Owns:
- current system disposition;
- target systems;
- implementation dependency order.

Defers detailed authority to future:
- progression;
- economy/items;
- NPC/social/adversary;
- tactical combat;
- balance;
- save migration masters.

### `docs/android/APK_FINAL_RECONSTRUCTION_MATRIX.md`
Owns:
- late-stage screen/component disposition;
- final rebuild sequence;
- removal gates;
- APK acceptance.

References:
- APK rebuild/evolution master;
- final domain contracts.

## 12. Historical expansion sequence — superseded by operational continuation

1. Gate Twelve Steps 8–14;
2. deep existing-state source audit;
3. progression/class/rank master;
4. NPC/social/adversary master;
5. item/economy/loot master;
6. tactical combat master;
7. world child schemas/catalogs;
8. application UX master;
9. save/content migration master;
10. final APK execution plan;
11. broad implementation only after required contracts.

## Newly materialized domain masters — 2026-10-02

### `docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md`
Owns the original tactical-combat contract: encounter state, tactical coordinates, turn/action model decision space, movement, cover, LOS, damage/injury, AI, beasts, party control, aftermath, Android tactical surface, pixel-art dependencies and verification.

### `docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md`
Owns NPC memory/knowledge/goals/schedules, social hierarchy, institutions, fictional discrimination modeling, faction structure, and the original persistent-adversary framework.

### `docs/systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md`
Owns item schema, equipment/accessories, quality/rarity decisions, durability/crafting gates, loot provenance, beast materials, resources, economy, ownership/crime integration and visual requirements.

### `docs/systems/WORLD_BALANCE_INTEGRATION_PLAN.md`
Owns regional danger bands, progression/world integration, anti-snowball policy, encounter/loot/economy/training/rival/beast balance and future validation requirements.

### `docs/systems/SAVE_AND_CONTENT_MIGRATION_MASTER_PLAN.md`
Owns high-risk migration governance for stable IDs, save versions, quests, NPCs, items, map routes, visual IDs and rollback.

### `docs/android/APPLICATION_UX_MASTER_PLAN.md`
Owns the future Android information architecture, Story/current-location surface, room character panels, Map hierarchy, Character/Stats/Skills/Equipment/Inventory/Quests, tactical mode, narration, accessibility and responsive behavior.

All six are subordinate to `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`. Implementation remains gated by their unresolved decisions and exact live-source audits.


---

## 2026-10-02 corpus/world/visual child expansion

### `docs/DOCUMENTATION_CORPUS_ARCHITECTURE.md`
Owns:
- long-range documentation volume structure;
- unit types;
- branch families;
- cross-reference rules;
- record-scale strategy;
- ambiguous numeric-target tracking;
- documentation-before-destruction gate.

References:
- master program;
- directive breakdown;
- progress ledger;
- domain master documents.

### `docs/world/WORLD_GEOGRAPHY_STANDARD.md`
Owns:
- spatial containment hierarchy;
- W0–W4 coordinate roles;
- geography boundaries;
- terrain/water/climate placement logic;
- resource/beast/political geography relationships;
- scale policy.

Must not invent final world size or missing Gate Twelve parent geography.

### `docs/world/WORLD_POLITICAL_ENTITIES.md`
Owns:
- political entity schema;
- government/institution layers;
- territorial-control states;
- social hierarchy and discrimination-policy documentation;
- conflict/political-economy links.

Current world-scale catalog remains unpopulated until canon is authored.

### `docs/world/WORLD_SETTLEMENT_CATALOG.md`
Owns:
- settlement/district record schema;
- population/service/economy/visual-packet requirements;
- settlement production workflow.

Gate Twelve is the current local proof region; its larger settlement parent remains undecided.

### `docs/world/WORLD_TRAVEL_AND_ROUTES.md`
Owns:
- route classes;
- endpoint/access/discovery/travel/risk record;
- hierarchical travel;
- route migration;
- map-art versus route-authority separation.

### `docs/assets/ROOM_ACTOR_PANEL_OVERLAY_REUSE_STANDARD.md`
Owns:
- per-area art packet;
- actor-in-room contract;
- room sprite/portrait/focus-panel identity consistency;
- text/signage separation;
- overlay classes;
- animation ownership;
- reuse compatibility signature;
- visual QA.

This child standard does not own NPC presence. Player-safe projected engine state does.


---

## 2026-10-02 live audit and inventory controls

### `docs/LIVE_REPOSITORY_STATE_AUDIT_2026-10-02.md`
Owns:
- exact audited program HEAD;
- live open-PR/branch landscape snapshot;
- current repository structural counts;
- current implementation/pixel/world/system state;
- what may change versus what remains protected;
- immediate reconciliation controls.

Consumes:
- master program;
- rework decision matrix;
- task register;
- live GitHub metadata/tree.

Feeds:
- branch/provenance reconciliation;
- Android consumer map;
- Gate Twelve implementation restart;
- final APK reconstruction.

### `docs/REPOSITORY_CORPUS_INVENTORY_SNAPSHOT_2026-10-02.md`
Owns:
- exact structural counts for the audited program Git tree;
- distinction between measurable repository quantities and ambiguous owner numeric targets;
- inventory expansion requirements.

### `tools/documentation_inventory.py`
Owns:
- deterministic local structural/documentation inventory;
- Markdown word counting in a complete checkout;
- extension/document-family/test-source counts.

It does **not** own:
- canon;
- asset production status;
- executed-test results;
- target-unit interpretation.


---

## 2026-10-02 directive child-contract expansion

### `docs/OWNER_DIRECTIVE_TRACEABILITY_MATRIX_2026-10-02.md`
Owns:
- requirement-by-requirement mapping of the expanded owner directive;
- current document owner;
- current state;
- next action;
- missing child-contract detection.

### `docs/systems/PLAYER_ACTIVITIES_AND_LIFE_LOOP_MASTER_PLAN.md`
Owns:
- active/timed/scheduled/background activity classes;
- time, interruption, concurrency, training, study, work, recovery, social, diagnostics and future gathering boundaries;
- NPC/activity integration;
- persistence and player-safe activity projection requirements.

### `docs/world/WORLD_COORDINATE_AND_SCALE_STANDARD.md`
Owns:
- operational coordinate-space IDs;
- units/origins/axes/bounds;
- parent-child transforms;
- logical versus presentation coordinates;
- route anchors/distance types;
- elevation/depth;
- W0–W4 separation;
- coordinate versioning/validation.

### `docs/assets/ASSET_PROVENANCE_REGISTRY.md`
Owns:
- source/reference/raster/fallback provenance fields;
- production stage;
- branch/HEAD;
- hashes/dimensions;
- reuse compatibility;
- supersession;
- initial runtime-raster reconciliation queue.

### `docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md`
Owns:
- current `GameSnapshot` and `GameEngine` Android-facing contract;
- screen/component consumer ownership;
- safe actor/activity/world/combat projection gaps;
- final line-by-line Android consumer-audit target.


## 2026-10-02 operational continuation

- [Decision/rebuild execution register](DECISION_AND_REBUILD_EXECUTION_REGISTER.md): decomposed owner requirements, can/will/candidate changes, migration gates and unresolved corpus units.
- [Full baseline document catalog](DOCUMENTATION_CATALOG_2026-10-02.md): every tracked Markdown file, actual headings, words, hashes and literal references; semantic audit remains separate.
- [World canon decision queue](world/WORLD_CANON_DECISION_QUEUE.md): exact nine-node/eight-edge baseline and ordered unresolved geography/politics/ecology/progression decisions.
- [Room composition implementation contract](assets/ROOM_COMPOSITION_IMPLEMENTATION_CONTRACT.md): current actors versus proposed presence projection, focus panels, pixel/text reuse and raster-precedence gates.
- [Raster delivery evidence](assets/RASTER_DELIVERY_EVIDENCE_2026-10-02.md): all 24 baseline PNG dimensions, hashes and catalog bindings.

These supplement existing masters. They do not supersede approved identity references or imply new gameplay APIs.


## 2026-10-02 final reconstruction integration update

### `docs/FINAL_GAME_RECONSTRUCTION_BLUEPRINT.md`
Owns:
- integration across documentation domains;
- change authority vocabulary;
- current/provisional/planned visual-stage summary;
- Gate Twelve area production packet summary;
- decided-versus-undecided world canon snapshot;
- mechanics migration decision summary;
- final APK demolition/rebuild dependency order;
- P0 reconciliation packet.

References/consumes:
- master program;
- live repository audit;
- existing-state decision matrix;
- pixel runtime/reuse/provenance documents;
- Gate Twelve region/asset documents;
- world child standards;
- progression/social/items/combat/activity/migration masters;
- Android UX/consumer/APK masters.

Must not own:
- exact low-level formulas already owned by a domain master;
- implementation facts without exact source/HEAD evidence;
- invented world canon.


## 2026-10-02 branch/raster/parent-world continuation

- [Implementation PR #7–#31 reconciliation](IMPLEMENTATION_PR_7_31_RECONCILIATION_2026-10-02.md): exact branch heads/bases, ancestry to the documentation program, workflow evidence, divergent survivor set and migration order.
- [Source/raster branch reconciliation](assets/SOURCE_RASTER_RECONCILIATION_2026-10-02.md): inherited nine-scene raster baseline, Service Tunnel/Quiet Stair divergent source+raster revisions, runtime raster precedence and promotion gates.
- [Gate Twelve parent-world proposal](world/GATE_TWELVE_PARENT_WORLD_PROPOSAL.md): proposed minimum settlement/region/municipal/route/terrain-climate parent chain; working names remain non-canon pending owner decision.

These records narrow D-028/D-029/D-031. They do not promote divergent implementation branches, change runtime state, or convert proposed world names into canon.


## 2026-10-02 moving-base crosswalk

- [PR #33 moving-base drift reconciliation](PR33_MOVING_BASE_DRIFT_RECONCILIATION_2026-10-02.md): historical branch-divergence snapshot, conflicting numerical-unit claim, duplicate-authority classification and no-blind-merge decision.
- [PR #33 live shared-file reconciliation](PR33_LIVE_SHARED_FILE_RECONCILIATION_2026-10-03.md): live-ref revalidation and exact shared-file decisions for `AGENTS.md`, `README.md`, `docs/IMPLEMENTATION_STATUS.md`, and the Gate Twelve master; all remain `KEEP PROGRAM`, with GT-IMP-001 preserved under the current D-030 contract.
- [Moving-base document crosswalk](BASE_BRANCH_DOCUMENT_CROSSWALK_2026-10-02.md): maps base-side program/system/world documents to current owners and dispositions.
- [Global asset reuse and occlusion matrix](assets/GLOBAL_ASSET_REUSE_OCCLUSION_MATRIX.md): operational R0–R5 reuse taxonomy and explicit scene occlusion stack under current pixel/reuse parents.
- [World entity ID/reference standard](world/WORLD_ENTITY_ID_AND_REFERENCE_STANDARD.md): semantic-ID lifetime, rename, merge/split and cross-reference rules.
- [Region/settlement authoring template](world/REGION_SETTLEMENT_DOCUMENTATION_TEMPLATE.md): execution template subordinate to geography/settlement standards.
- [Gate Twelve external connection register](world/GATE_TWELVE_EXTERNAL_CONNECTIONS_AND_EXPANSION_REGISTER.md): outward-edge unknown/proposal register compatible with the parent-world proposal.

The moving-base `docs/program/*` hierarchy is not activated by these migrations.


## D-030 player-safe actor projection

- [Player-safe room actor & context panel projection contract](android/PLAYER_SAFE_ROOM_ACTOR_PROJECTION_CONTRACT.md): exact current Python/Kotlin/Compose gap, versioned room payload, hidden-state redaction, opening actor equivalence, support-actor identity rule, semantic placement migration, contextual panel lifecycle and verification gates.

This document is an implementation target, not evidence that room-actor projection already exists at runtime.


## D-029 family-level asset provenance continuation

- [Asset provenance registry](assets/ASSET_PROVENANCE_REGISTRY.md): master provenance schema, stage vocabulary, branch awareness and supersession rules.
- [Asset family provenance index](assets/ASSET_FAMILY_PROVENANCE_INDEX_2026-10-03.md): operational navigation from current asset families to source/code master, raster/export, branch/head, runtime consumer, QA, production stage, migration risk and reconstruction sequence.
- [Character, equipment, item, and actor provenance](assets/CHARACTER_EQUIPMENT_ITEM_ACTOR_PROVENANCE_2026-10-03.md): player/item/equipment/staging/actor family evidence, raster precedence, Jack-reference distinction and portrait gaps.
- [Environment, scene, and map provenance](assets/ENVIRONMENT_SCENE_MAP_PROVENANCE_2026-10-03.md): nine-scene source/raster lineage, environment composition families, map families and divergent static-art candidates; also owns PR #8 source preservation, the current exact arrival-preview consumers, and the integrated-module versus deferred-infrastructure-atlas stage split.
- [UI, FX, held-prop, and animation provenance](assets/UI_FX_ANIMATION_PROVENANCE_2026-10-03.md): UI/Trace families plus deferred PR #9 held-prop and PR #31 ambient-animation candidates; PR #9 consumer ownership is resolved as Tamsin actor-presentation art blocked on D-030 runtime projection and hand/wrist anchor verification.

Authority classification:

- **master:** `ASSET_PROVENANCE_REGISTRY.md`;
- **operational child index:** `ASSET_FAMILY_PROVENANCE_INDEX_2026-10-03.md`;
- **complementary evidence children:** the three family ledgers;
- **exact raster evidence:** `assets/RASTER_DELIVERY_EVIDENCE_2026-10-02.md` + `evidence/raster_bindings_2026-10-02.json`;
- **exact static source/raster divergence evidence:** `assets/SOURCE_RASTER_RECONCILIATION_2026-10-02.md`.

The family ledgers do not promote branch candidates, grant canon approval, or replace runtime/source authority. D-029 remains incomplete until the remaining source lineage, survivor, approval and QA gaps are closed.


## D-029 exact raster export lineage

- [Raster export and source correspondence](assets/RASTER_EXPORT_AND_SOURCE_CORRESPONDENCE_2026-10-03.md): exact current source revision -> export/refresh commit -> runtime raster relationship for all 24 current PNGs.
- `docs/evidence/raster_export_lineage_2026-10-03.json`: machine-readable per-raster lineage, current source/raster blobs and correspondence class.

Authority classification:

- **master schema:** `assets/ASSET_PROVENANCE_REGISTRY.md`;
- **exact static raster identity:** `assets/RASTER_DELIVERY_EVIDENCE_2026-10-02.md` + `evidence/raster_bindings_2026-10-02.json`;
- **export/history correspondence:** `assets/RASTER_EXPORT_AND_SOURCE_CORRESPONDENCE_2026-10-03.md` + `evidence/raster_export_lineage_2026-10-03.json`;
- **divergent static survivor evidence:** `assets/SOURCE_RASTER_RECONCILIATION_2026-10-02.md`.

The historical PR #19 exporter remains unknown/not persisted. A new reconstruction verifier/exporter now exists, but pixel equality is not considered freshly reproduced until that tool executes and its report is inspected.


## D-029 raster reconstruction tooling

- `tools/verify_pixel_raster_equivalence.py`: deterministic standard-library current-source/PNG verifier and safe separate-tree reconstruction exporter.
- `tests/test_pixel_raster_equivalence_tool.py`: 24-binding pixel/identity/lineage equality plus deterministic export and overwrite-safety tests.
- `docs/evidence/raster_equivalence_verifier_status_2026-10-03.json`: machine-readable implementation status; currently `IMPLEMENTED_EXECUTION_PENDING`.

This is reconstruction tooling, not evidence of the historical PR #19 exporter implementation.

## D-029 ambient-animation migration child

- [Service Tunnel ambient animation migration contract](assets/SERVICE_TUNNEL_AMBIENT_ANIMATION_MIGRATION_CONTRACT_2026-10-03.md): PR #31 exact branch evidence, stable track IDs/timing/bounds, static-art dependency, reduced-motion ownership, selective reimplementation sequence, lifecycle/performance rules and destination-head verification gates.
- [Application UX master plan](android/APPLICATION_UX_MASTER_PLAN.md): parent accessibility authority; reduced motion is required and remains presentation/application state, not gameplay authority.

This child resolves the provenance/migration strategy but does not claim the animation or reduced-motion path is implemented.


## Reconstruction dependency-graph semantics — D-044 extraction

Source provenance:
- `docs/settlement-region-build-plan@65d2db8538c1b8302c314f2fbe9eb7a1b585b51d`
- `docs/program/10_EXECUTION_COORDINATION_GRAPH.md`
- source blob `22318ac60cad6164d2b8cc670e6d5dbd0a66c466`.

This section preserves the useful graph vocabulary without activating the moving `docs/program/*` hierarchy as a second execution system.

Conceptual documentation graph:

`G = (V, E)`

Useful node classes include:

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

Preferred relationship semantics include:

- `Decision -> constrains -> Document`;
- `Document -> specifies -> System`;
- `System -> implemented_by -> File`;
- `Test -> verifies -> Behavior`;
- `Asset -> renders -> State`;
- `Location -> belongs_to -> Region`;
- `Route -> connects -> Location`;
- `Gap -> blocks -> Task`;
- `Decision -> supersedes -> Decision`.

These are reconstruction/reference relationships. They do **not** require a graph database or runtime implementation.

For consequential changes, graph/task handoff should also identify:

- failure mode;
- detection;
- state/data that must survive;
- rollback or compensating action;
- evidence required before success.

The active task register, current domain authorities and this cross-reference matrix remain the repository owners. This graph vocabulary is a way to express their relationships, not a replacement authority.


## 2026-10-03 Status UI / ability / passive program

### `docs/systems/STATUS_UI_ABILITIES_AND_PASSIVES_MASTER_PLAN.md`
Owns:
- human age-18 Status awakening;
- one-primary-ability rule;
- ability rarity hierarchy;
- global Level as in-universe progression;
- Level-100 ability-change exception;
- passive acquisition and hidden-until-qualified behavior;
- scalable documentation/catalog architecture;
- knowledge asymmetry and classified unlock methods.

### `docs/systems/status/STATUS_UI_CORE_CONTRACT.md`
Owns the target player/world contract for Status fields, awakening, Level, primary ability, passives, hidden information and future privacy/access rules.

### `docs/systems/status/PASSIVE_REGISTRY_SCHEMA.md`
Owns the reconstruction-grade record structure for large passive catalogs, including requirements, secrecy, world knowledge, evolution, validation and player-safe visibility.

These documents supplement `PROGRESSION_CLASSES_RANKS_EVOLVED_GAME_DESIGN.md`. They do not claim runtime implementation.


## V08 tactical-combat first-pass child suite — 2026-10-04

Parent:
- docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md

Presentation:
- docs/systems/CAMERA_AND_TACTICAL_PRESENTATION_STANDARD.md

Implementation-detail children:
- docs/systems/TACTICAL_COORDINATE_OCCUPANCY_STANDARD.md — cells, topology, occupancy, cardinal adjacency, deterministic pathing boundaries;
- docs/systems/TURN_INITIATIVE_ACTION_BUDGET_STANDARD.md — rounds, initiative, four-unit budget, reactions, reinforcement timing;
- docs/systems/MOVEMENT_PATHING_AND_POSITIONING_STANDARD.md — movement-point costs, move/sprint, interruption, forced movement;
- docs/systems/LOS_DETECTION_AND_COMBAT_KNOWLEDGE_STANDARD.md — supercover LOS, awareness, last-known position, hidden-state redaction;
- docs/systems/DIRECTIONAL_COVER_TERRAIN_STANDARD.md — edge cover, terrain, concealment, hazards;
- docs/systems/COMBAT_ACTION_TARGETING_RESOLUTION_STANDARD.md — action schema, legality, deterministic contest, damage/protection transaction;
- docs/systems/INJURY_CONDITION_AFTERMATH_STANDARD.md — injury generation, condition reuse, persistent atomic aftermath, save boundary;
- docs/systems/COMBAT_AI_OBJECTIVES_RETREAT_STANDARD.md — no-cheat deterministic AI, objectives, retreat, companion orders.

Feeds:
- Gate Twelve Phase 1 authored tactical encounter packet;
- D-032 combat schema/API migration;
- future player-safe combat projection;
- final V11 tactical UI refinement;
- combat asset specifications;
- low-end performance/test packets.

V08 first-pass minimum quota is satisfied. Runtime implementation remains separate.


## V05 character/NPC/social first-pass child suite — 2026-10-04

Parent:
- docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md

Children:
- docs/systems/NPC_CHARACTER_IDENTITY_PROFILE_STANDARD.md
- docs/systems/NPC_PERSONALITY_BEHAVIOR_STANDARD.md
- docs/systems/NPC_MEMORY_EVENT_STANDARD.md
- docs/systems/NPC_KNOWLEDGE_BELIEF_PRIVACY_STANDARD.md
- docs/systems/NPC_RELATIONSHIP_STATE_STANDARD.md
- docs/systems/NPC_GOALS_DECISION_STANDARD.md
- docs/systems/NPC_SCHEDULE_PRESENCE_STANDARD.md
- docs/systems/FACTION_HIERARCHY_MEMBERSHIP_STANDARD.md
- docs/systems/SOCIAL_CONSEQUENCE_RUMOR_PROPAGATION_STANDARD.md
- docs/systems/RECURRING_CHARACTER_PACKET_STANDARD.md
- docs/systems/TAMSIN_PHASE1_SOCIAL_PROOF_PACKET.md

V05 first-pass quota: 12 / 12 including the parent master.

Feeds:
- Phase 1 relationship/knowledge proof;
- player-safe room actor migration;
- future relationship/People UI;
- V09 persistent adversaries;
- tactical companion behavior;
- world NPC population and schedules.

Track-B combat packet:
- docs/systems/GATE_TWELVE_PHASE1_TACTICAL_ENCOUNTER_PACKET.md consumes V08 rules and current Gate Twelve facts, but remains proposed content until canon review.
