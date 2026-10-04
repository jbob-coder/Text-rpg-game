# THE GAME — Documentation Progress Ledger

Status: **ACTIVE / METRIC DEFINITION PENDING OWNER CONFIRMATION**  
Parent: `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`

## 1. Why this ledger exists

The owner set very large long-range documentation targets. The numeric units were not fully specified, so this ledger prevents accidental false completion claims.

## 2. Preserved owner targets

- 3,000 “documentation”
- 2,000 guide/planning
- 10,000 map-development scope
- 10,000 final APK/development scope
- 2,000,000 total documentation target

These numbers are preserved exactly as planning targets.

## 3. Metrics tracked separately

Track:
- Markdown/document files;
- documentation words;
- structured world records;
- guide/planning entries;
- decisions;
- implementation tasks;
- map/place records;
- routes;
- assets;
- NPC records;
- item/loot records;
- beast/ecosystem/resource records;
- system specification records;
- test cases;
- QA/evidence records.

No single metric is automatically equivalent to one of the owner's numeric targets.

## 4. Corpus classes

### Authority/governance
Target content:
- project priority;
- permissions;
- prohibitions;
- migration;
- evidence;
- branch rules;
- handoffs.

### Guides/planning
Target content:
- implementation guides;
- art production packets;
- map packets;
- migration guides;
- test plans;
- troubleshooting;
- balancing guides;
- content-authoring guides.

### World/map records
Target content:
- coordinates;
- macroregions;
- political entities;
- cities;
- towns;
- villages;
- districts;
- sites;
- interiors;
- routes;
- resources;
- ecosystems;
- beast zones;
- population;
- loot provenance.

### Systems
Target content:
- progression;
- stats;
- skills;
- abilities;
- passives;
- classes/ranks;
- items;
- economy;
- social;
- NPC;
- tactical combat;
- adversaries;
- activities;
- balance.

### Visual
Target content:
- asset briefs;
- source masters;
- manifests;
- character sheets;
- map kits;
- scene packets;
- overlays;
- FX;
- animation;
- UI art.

### APK/application
Target content:
- screens;
- components;
- projection fields;
- migrations;
- QA;
- release provenance.

## 4.1 First-pass canonical document quotas

The first concrete coverage floor is defined in:
- `docs/FIRST_PASS_DOMAIN_DOCUMENTATION_QUOTAS.md`.

First-pass minimum allocation:
- V00 authority/governance: 8;
- V01 existing-state audit: 10;
- V02 visual/assets: 12;
- V03 Gate Twelve proof region: 10;
- V04 world: 12;
- V05 characters/social: 12;
- V06 progression: 12;
- V07 items/economy/loot: 10;
- V08 tactical combat: 10;
- V09 persistent adversaries/world memory: 8;
- V10 activities/life simulation: 8;
- V11 application UI/UX planning: 8;
- V12 Android/APK reconstruction: 8;
- cross-domain guides/planning: 10;
- cross-domain evidence/QA/migration: 10.

Total first-pass floor: **148 canonical documentation units**.

This is not a claim that 148 files equal completion. Structured records and semantic coverage remain separate metrics, and final quotas will be recalibrated after the first broad pass.

## 4.2 Phase 1 playable progress must be tracked separately

The parallel playable line is:
- `docs/PHASE_1_SOLO_PLAYABLE_PARALLEL_TRACK.md`.

Track its 16 minimum integrated requirements independently from the corpus-size metrics. Documentation can grow without falsely implying Phase 1 is playable, and implementation progress can advance without falsely implying the full corpus is complete.

## 5. Current program milestone

The current documentation branch has established:
- master program;
- cross-reference matrix;
- priority/context log;
- Gate Twelve Steps 1–14;
- pixel runtime composition standard;
- asset status matrix;
- character blueprint work;
- world master index;
- APK rebuild plan;
- master directive breakdown;
- existing-state rework matrix;
- pixel production/reuse ledger;
- world-scale schema blueprint;
- gameplay rebuild matrix;
- final APK reconstruction matrix.

This is a program foundation, not the final corpus.

## 6. Progress rules

A documentation unit is counted only if it:
- has a stable repository path or structured registry ID;
- has a defined owner/parent;
- has a status;
- does not duplicate another unit without reason;
- links to implementation or another required document;
- can be found by the cross-reference system.

## 7. Completion rules

Do not declare the 2,000,000 target complete until:
- target units are defined or accepted;
- counts are reproducible;
- stale/duplicate material is excluded or marked;
- cross-reference coverage is audited;
- the owner accepts the measurement method.

## 8. Next action

After the repository existing-state audit, add a reproducible corpus inventory script or report capable of counting:
- docs;
- words;
- records;
- tasks;
- assets;
- tests;
- world records.

Until then, all exact corpus totals remain **UNKNOWN** rather than estimated.

## 2026-10-02 system-master expansion

New documentation units now present on the master-program branch:
- tactical combat master;
- NPC/social/persistent-adversary master;
- items/economy/loot master;
- world balance integration plan;
- save/content migration master;
- Android application UX master.

This advances the systems/application contract layer. It does not change the numeric-target interpretation and does not claim implementation completion.

Next high-value documentation:
1. complete exact existing-state audit against live implementation heads;
2. deepen progression/class/rank details;
3. define world political/settlement/ecology child catalogs;
4. audit exact runtime/source state against the rework matrix;
5. create reproducible corpus/asset-status inventory.


## 2026-10-02 corpus architecture + world child standards

Added active documentation units:
- `docs/DOCUMENTATION_CORPUS_ARCHITECTURE.md`;
- `docs/world/WORLD_GEOGRAPHY_STANDARD.md`;
- `docs/world/WORLD_POLITICAL_ENTITIES.md`;
- `docs/world/WORLD_SETTLEMENT_CATALOG.md`;
- `docs/world/WORLD_TRAVEL_AND_ROUTES.md`;
- `docs/assets/ROOM_ACTOR_PANEL_OVERLAY_REUSE_STANDARD.md`.

These additions materially advance:
- corpus/branch planning;
- world coordinate/geography structure;
- political hierarchy;
- settlement authoring;
- routes/travel;
- per-area pixel-art/actor/panel/reuse composition.

No numeric target is declared complete. Reproducible inventory remains the next P0 measurement task.


## 2026-10-02 world-standard completion batch

Added:
- ecosystem/resources;
- beast zones;
- population/citizen hierarchy;
- world balance/level bands;
- loot provenance;
- world NPC population.

The world schema layer now has materialized child standards for geography, political entities, settlements, routes, ecosystems/resources, beast zones, population/hierarchy, balance, loot provenance and NPC distribution.

This does **not** mean the world itself has been populated. Large-scale canon records for macroregions, kingdoms/states, cities/villages, ecosystems, beasts and NPCs remain future authoring work.


## 2026-10-02 Gate Twelve Step 8 continuation

Completed on the master-program branch:
- Gate Twelve Step 8 application UX contract;
- Story/current-location composition ownership;
- player-safe room-actor and focus-panel behavior;
- district-map selection/travel contract;
- overlay/text-art/fallback rules;
- phone-first accessibility and loading behavior;
- explicit KEEP / REWORK presentation boundaries for the proof region.

Next regional documentation: Step 9 state-layer plan.


## 2026-10-02 Gate Twelve Steps 9–14 completion batch

The first proof-region plan is now complete through Step 14:
- state-layer ownership;
- performance/section-loading strategy;
- implementation/dependency order;
- documentation/engine/Android/pixel/privacy/performance/handset verification gates;
- KEEP / EXTEND / REWORK / REPLACE / REMOVE / ARCHIVE migration policy;
- exact execution handoff and first implementation dependency.

This is documentation completion only. It does not claim the runtime, final pixel art, map, actor projection, connector migration, APK or physical handset acceptance is complete.

Next P0 measurement/control work:
1. exact existing-state repository audit;
2. reproducible documentation/world/asset inventory;
3. Gate Twelve refinement/provenance reconciliation.


## 2026-10-02 live-repository audit and inventory-control batch

Added:
- `docs/LIVE_REPOSITORY_STATE_AUDIT_2026-10-02.md`;
- `docs/REPOSITORY_CORPUS_INVENTORY_SNAPSHOT_2026-10-02.md`;
- `tools/documentation_inventory.py`.

Verified structural snapshot for `docs/master-game-development-program@f9981cdcd4d82c8eced330a2da081e60ee2ed510` before these additions:
- 231 tracked files;
- 90 files under `docs/`;
- 69 Markdown files repository-wide;
- 67 Markdown files under `docs/`;
- 24 PNGs;
- 39 Python files;
- 65 Kotlin files;
- 18 JSON files;
- 50 Python/Kotlin source files with `test` in their path;
- 12 world Markdown documents;
- 8 systems Markdown documents;
- 22 asset Markdown documents;
- 3 Android Markdown documents;
- 3 Game Context Log Markdown documents.

These are exact structural counts for that Git tree, not completion percentages and not a chosen interpretation of the owner's 3,000 / 2,000 / 10,000 / 10,000 / 2,000,000 targets.

The deterministic inventory tool has been added, but a persisted exact-checkout execution plus structured domain/asset-stage extraction remains P0 work.


## 2026-10-02 owner-directive traceability + missing-child closure batch

Added:
- `docs/OWNER_DIRECTIVE_TRACEABILITY_MATRIX_2026-10-02.md`;
- `docs/systems/PLAYER_ACTIVITIES_AND_LIFE_LOOP_MASTER_PLAN.md`;
- `docs/world/WORLD_COORDINATE_AND_SCALE_STANDARD.md`;
- `docs/assets/ASSET_PROVENANCE_REGISTRY.md`;
- `docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md`.

This batch closes four documentation gaps detected by the directive traceability pass:
- passive/active player activities and life-loop ownership;
- operational coordinate/scale rules;
- branch-aware visual provenance requirements;
- Android screen/projection consumer mapping.

The new documents are contracts, not claims that their target runtime systems are complete.


## Executed baseline inventory — 2026-10-02 15:06 AST

Exact baseline `4d596bcd27b6e2f8ef9ce3a93b9dab22f5f4812e`: 239 tracked files; 76 Markdown files; 74 under docs; 123,707 repository Markdown words; 122,028 docs Markdown words; 24 PNGs; 13 world, 9 systems, 23 asset and 4 Android Markdown files. Command actually executed: `python tools/documentation_inventory.py --root .`. No unreadable Markdown reported.

These measured quantities are baseline inventory, not completion of the owner's ambiguous numeric targets. New continuation files are excluded from the baseline snapshot. Full file-content catalog and 24 raster binding records are now stored under docs/evidence. World map baseline contains nine nodes and eight edge records. No 10,000-place or 2,000,000-unit completion is claimed.


## 2026-10-02 final reconstruction integration update

Added integration authority:
- `docs/FINAL_GAME_RECONSTRUCTION_BLUEPRINT.md`.

This is counted as a new durable documentation unit but does **not** resolve the owner's numeric-unit ambiguity and does not justify a completion percentage.

The new blueprint adds structured decision coverage for:
- change authority;
- pixel asset stages and required creation families;
- area packet composition;
- actor/panel projection;
- decided vs undecided world canon;
- mechanics migration depth;
- final APK teardown/rebuild order.

Next measurable work remains branch-aware asset/implementation reconciliation and exact inventory execution.


## 2026-10-04 master documentation record control layer

Added:
- `docs/MASTER_DOCUMENTATION_RECORD.md`.

Purpose:
- provide one durable repository-native record of what documentation exists;
- separate contract completion from runtime/content completion;
- list completed areas, partial areas, missing work, blockers, authorities and next execution order;
- prevent older task-register NEXT text and historical count snapshots from being mistaken for live state.

Source audit used to establish the record:
- `docs/master-game-development-program@28809b7abdaf6f7f05ccd58cf0d5e71efacf5e22`;
- 489 tracked files;
- 347 documentation-scope paths;
- 319 Markdown documentation paths;
- 21 structured documentation paths;
- 216 paths under `docs/systems/`, including 204 under `docs/systems/status/`;
- 18 world paths;
- 46 asset paths;
- 5 Android paths.

These are structural path counts, not semantic-completion percentages and not a resolution of the owner's ambiguous numeric units.

Control reconciliation performed in the same continuation:
- repository entry points now route through the master documentation record;
- cross-reference authority now includes the master record;
- TASK D-047 records creation/maintenance of the master record;
- D-020 moved from pending to in-progress because PR-level reconciliation exists through D-028 while survivor migration remains;
- D-021 moved from pending to in-progress because D-026 already materialized the high-level Android consumer/projection map;
- D-046 was reconciled to the live Status corpus: Phase A complete, Wave 001 structurally complete at 1,019 records, primary-ability detail coverage 47/47, passive family baseline 23/23, while Phase-C refinement/canon/runtime mapping remains active.

No gameplay runtime, save schema, stable IDs, Android implementation, pixel raster, or final APK behavior changed in this control-layer batch.

Next measurement priority remains D-019: execute and persist a reproducible exact-current-head inventory with words, structured records, asset stages, test-source counts and executed-test evidence kept distinct.


## 2026-10-04 D-019 exact structural inventory refresh

Source HEAD:
- `docs/master-game-development-program@991cd9b29ea0752fa1c303a19e8f210713efe4b5`.

New persisted evidence:
- `docs/REPOSITORY_CORPUS_INVENTORY_SNAPSHOT_2026-10-04.md`;
- `docs/evidence/repository_inventory_2026-10-04.json`.

Exact structural source-head counts:
- 490 tracked files;
- 5,203,664 tracked blob bytes;
- 320 Markdown files repository-wide;
- 318 Markdown files under `docs/`;
- 21 structured documentation paths;
- 24 PNGs;
- 42 Python files;
- 68 Kotlin/KTS files;
- 51 Python/Kotlin test-source paths;
- 18 world Markdown files;
- 216 systems Markdown files, including 204 Status-system Markdown files;
- 33 asset Markdown files;
- 5 Android Markdown files.

Bounded structured counts added:
- 13 asset manifests;
- 104 manifest rows;
- 95 unique asset IDs;
- Status Wave 001: 1,019 structurally audited records from the repository-owned audit;
- Gate Twelve baseline: 9 nodes and 8 edges.

D-019 remains **IN_PROGRESS**. No current-head word count was fabricated. Complete-checkout word/heading counts, generalized domain extractors, provenance-normalized asset stages and executed-test evidence remain open.


## 2026-10-04 D-042 deep current-head source audit

Added:
- `docs/DEEP_SOURCE_EXISTING_STATE_AUDIT_2026-10-04.md`.

Audited source HEAD:
- `docs/master-game-development-program@d0382aaf6cca2920a7f315d08153ac6b0dddc5dd`.

Current-head inventory now explicitly covers:
- 19 Python engine modules;
- 35 Android main Kotlin files;
- 2 authored content JSON files;
- exact GameState/save schema v1 top-level fields and persistence boundary;
- 24 runtime PNGs;
- 21 Python test files;
- 27 Android JVM/unit-test files;
- 3 Android instrumented-test files;
- 2 GitHub workflow files;
- 5 Android Gradle/manifest configuration files.

The audit records KEEP / EXTEND / REWORK / replacement-direction dispositions while preserving the no-deletion-before-consumer/migration-evidence rule.

D-006/D-042 remain in progress because cross-branch survivor reconciliation, field-level Android consumer mapping, per-catalog consumer/deprecation proof, D-029 asset equivalence/provenance and D-044 remaining Class-C extraction are still open.

No runtime or content files changed and no tests/builds were executed by this documentation pass.


## 2026-10-04 D-042 deep source audit checkpoint

Added:
- `docs/DEEP_SOURCE_EXISTING_STATE_AUDIT_2026-10-04.md`.

Audited source HEAD:
- `docs/master-game-development-program@d0382aaf6cca2920a7f315d08153ac6b0dddc5dd`.

Current-head source inventory captured:
- 19 Python engine modules;
- 21 Python test files;
- 2 authored content JSON files;
- 35 Android main Kotlin files;
- 27 Android JVM/unit-test files;
- 3 Android instrumented-test files;
- 24 runtime PNGs;
- 2 workflows;
- 5 Android build/manifest configuration files.

The audit records the 17-field durable GameState/save boundary, schema v1 behavior, current vertical-slice record counts, and source-level disposition guidance.

D-042 remains **IN_PROGRESS** because line-by-line Android consumer mapping, catalog consumers, full asset lineage, cross-branch survivor migration and zero-consumer/deprecation proof remain open.

No runtime tests/builds were executed and no gameplay/application source was changed by this audit.


## 2026-10-04 D-044 moving-base reconciliation closure

D-044 is complete.

All seven Class-C selective extraction actions are now represented in current authorities:
- documentation expectation/acceptance;
- decision-gap closure;
- graph/failure-handoff semantics;
- beast scene presence;
- beast-zone density/repopulation/pressure/readiness;
- bounded persistent-adversary adaptation/recurrence/lifecycle;
- L0-L4 map-detail production gate.

Final live ref recheck:
- program `de8c76cc08da20099671b5cd8fc5d7d7acca1920`;
- target `65d2db8538c1b8302c314f2fbe9eb7a1b585b51d`;
- merge base `c261b2aaf8bd978d27b46f8fea03435c0c5734d0`;
- diverged: ahead 651 / behind 99;
- PR #33 remains open, draft and mergeable false.

No blind merge/rebase was performed. Completion is documentation reconciliation, not branch promotion.


## 2026-10-04 D-026 / D-021 Android consumer audit checkpoint

Updated:
- `docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md`.

New source-grounded coverage:
- Python player-safe projection envelope;
- Kotlin snapshot mapper boundary;
- GameViewModel engine-action and transient-state ownership;
- major Compose field consumers;
- current navigation graph;
- functional Android test-source coverage.

This closes the broad field/action mapping gap for the main current UI surfaces, but D-026/D-021 remain **IN_PROGRESS**.

Remaining:
- per-pixel-catalog consumers and zero-consumer candidates;
- hardcoded/temporary presentation-state audit;
- exact field/action-to-test gap matrix;
- future activity/combat/hierarchical-map/adversary projections;
- final APK destination migration map.

No Android implementation or gameplay behavior changed in this documentation pass.


## 2026-10-04 D-026 / D-021 Android consumer exact-source pass

Added:
- `docs/android/ANDROID_CONSUMER_FIELD_AUDIT_2026-10-04.md`.

Current exact-source documentation now maps:
- all 18 `GameSnapshot` fields;
- Python player-safe payload groups;
- Kotlin bridge mapping;
- ViewModel action paths;
- Story/Map/Character/Stats/Inventory/Quests/Settings consumers;
- direct pixel-catalog dependencies in core screens;
- current test-source coverage;
- transitional actor inference, relay visual state and travel transition.

D-026/D-021 remain in progress because future target projections, per-entry asset zero-consumer evidence and complete navigation/temporary-state audit remain open.

No Android/Python runtime files changed and no tests/builds were executed.


## 2026-10-04 Android catalog + field/action test-gap continuation

Updated:
- `docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md`.

Completed documentation slices:
- file-level direct-consumer mapping for all current pixel presentation sources;
- whole-file zero-consumer checkpoint: none proven at current file level;
- transitional/hardcoded presentation-state classification;
- GameSnapshot field -> current test-source coverage/gap matrix;
- GameEngine action -> current test-source coverage matrix.

Documented current test gaps:
- QuestSection projection/rendering;
- contentId;
- canonStatus;
- dedicated derived-stat Compose assertion;
- fuller identity UI contract.

D-026/D-021 remain **IN_PROGRESS**. Member/asset-ID zero-consumer proof, future projections, destination APK mapping and runtime execution evidence remain open.


## 2026-10-04 D-020 implementation survivor reconciliation closure

Added:
- `docs/IMPLEMENTATION_SURVIVOR_MIGRATION_MATRIX_2026-10-04.md`.

D-020 documentation reconciliation is now complete for PRs #7–#31.

The matrix separates:
- inherited/current survivor behavior;
- current contracts that may be visually reworked later;
- superseded historical surfaces;
- branch-only candidate migrations;
- owner-decision-required static art;
- historical fix-extraction sources;
- documentation-only ancestry.

This does not implement PR #9/#27/#28/#30/#31 candidate work and does not make owner art decisions.


## 2026-10-04 D-025 provenance registry seed closure

D-025 is complete at the registry-seed boundary.

The active provenance registry already defines:
- stable asset identity;
- provenance field schema;
- authority/stage vocabularies;
- reuse compatibility;
- runtime layers;
- branch-awareness;
- initial 24-raster seed.

Deep family reconciliation remains D-029 and is not double-counted as unfinished D-025 work.


## 2026-10-04 D-029 current raster consumer / zero-consumer audit

Added:
- `docs/assets/CURRENT_ASSET_CONSUMER_ZERO_CONSUMER_AUDIT_2026-10-04.md`;
- `docs/evidence/current_asset_consumer_audit_2026-10-04.json`.

Result:
- 24 / 24 current drawable-nodpi PNGs have a current source consumer path;
- zero current PNGs qualify for REMOVE on zero-consumer grounds;
- all nine scene PNGs have authored current node/scene reachability;
- all current player/loadout/item raster bindings have avatar/inventory/equipment consumers;
- all four Dead Relay visual states have authored bridge/content reachability.

Deferred/noncurrent zero-consumer candidates remain separate:
- municipal infrastructure atlas;
- PR #9 diagnostic reader icon/held master;
- PR #31 Service Tunnel ambient animation.

D-029 remains in progress because fresh 24/24 pixel-equivalence execution, visual survivor decisions, final character/portrait production, canon approval and physical-device QA remain open.

No runtime/assets were modified and no tests/builds/verifier execution occurred in this audit.


## 2026-10-04 D-029 visual survivor owner-decision gate

Added:
- `docs/assets/VISUAL_SURVIVOR_OWNER_DECISION_PACKET_2026-10-04.md`.

The remaining static-scene ambiguity is now reduced to two explicit owner decisions:
- D029-VIS-001 — current Service Tunnel baseline vs PR #27 refined candidate;
- D029-VIS-002 — current Quiet Stair baseline vs PR #30 refined candidate.

The safe default remains the current integrated baseline. PR #28 composition and PR #31 animation remain downstream/deferred until the Service Tunnel static parent is selected.

No candidate was silently promoted and no runtime/raster migration was performed.


## 2026-10-04 Android navigation and ephemeral-state audit

Added:
- `docs/android/ANDROID_NAVIGATION_AND_EPHEMERAL_STATE_AUDIT_2026-10-04.md`.

Resolved current-source documentation for:
- seven-section production navigation;
- Settings overlay;
- scene-change return-to-Story policy;
- ViewModel transient state;
- inventory/map/stat/local Compose selections;
- narration/text presentation preferences;
- stable test/preview GameScreen navigation surface.

No gameplay authority was moved into UI documentation. No runtime files changed and no tests/builds were executed.


## 2026-10-04 D-026 member asset-ID audit

Added:
- `docs/android/PIXEL_MEMBER_ASSET_ID_CONSUMER_AUDIT_2026-10-04.md`;
- `docs/evidence/pixel_member_consumer_audit_2026-10-04.json`.

Audited source HEAD:
- `docs/master-game-development-program@b79185fd673ff7838ef1b8f2814d1459230052fb`.

Result:
- 110 top-level ID-like constants inspected;
- 109 visual asset IDs;
- one non-visual condition trigger (`COND_ECHO_STRAIN`);
- three top-level visual IDs have no current production consumer:
  - `MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS`;
  - `UI_CHOICE_CARD_SELECTED`;
  - `UI_BUTTON_DANGER`;
- four generated Trace-strain portrait frames also have no current production consumer;
- none are approved for removal by this audit.

D-026/D-021 current-source consumer discovery is now complete at field/action, navigation/transient-state, file, and member/asset-ID levels.

D-006 was updated to remove already-completed D-020/D-044 and already-finished current consumer discovery from its open-work list.

No runtime files changed and no tests/builds were executed.


## 2026-10-04 V08 tactical first-pass documentation batch

Added eight canonical tactical-combat child standards.

V08 first-pass count is now 10 / 10 when the existing tactical master and camera/presentation standard are included.

This is a semantic first-pass quota closure, not runtime completion and not a resolution of the owner's long-range numeric units.

Phase 1 impact:
- tactical mechanical documentation is contract-ready;
- generic persistent injury/aftermath documentation is contract-ready;
- authored encounter packet, Python runtime, Android tactical UI/projection, performance evidence and tests remain pending.

Breadth direction now moves to V05 Characters/NPC/Social while a bounded Gate Twelve encounter packet remains the next combat-specific document.


## 2026-10-04 V05 social first-pass + Phase 1 encounter continuation

Added eleven V05 child standards/packets.

V05 first-pass count is now 12 / 12 when NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md is included.

Semantic coverage now includes:
- stable character identity;
- personality;
- memory;
- knowledge/belief/privacy;
- relationships;
- goals/decision;
- schedules/presence;
- faction/hierarchy membership;
- social consequence/rumor;
- recurring-character packet format;
- Tamsin Phase 1 social proof.

Also added:
- docs/systems/GATE_TWELVE_PHASE1_TACTICAL_ENCOUNTER_PACKET.md.

The encounter packet is proposed content, not canon/runtime completion. It uses existing Service Tunnel and Directional Trace facts and deliberately keeps opponent identity unresolved.

Next breadth area: V10 Activities/Life Simulation.
