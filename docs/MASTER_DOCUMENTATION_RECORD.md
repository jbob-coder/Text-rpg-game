# THE GAME — Master Documentation Record

Status: **ACTIVE / CANONICAL DOCUMENTATION STATUS INDEX**  
Repository: `jbob-coder/Text-rpg-game`  
Working branch: `docs/master-game-development-program`  
Created: 2026-10-04 AST  
Source audit HEAD used to establish this record: `28809b7abdaf6f7f05ccd58cf0d5e71efacf5e22`

---

## 0. Purpose

This file is the master record requested by the owner for the documentation program.

Its job is not to duplicate every design document. Its job is to answer, from one durable repository location:

1. **What documentation exists?**
2. **What has actually been completed?**
3. **What is only partially documented?**
4. **What is still missing?**
5. **What is blocked and why?**
6. **Which document is authoritative for each subject?**
7. **What should be worked on next?**
8. **What evidence supports a completion claim?**

A future developer or AI agent should be able to open this file, follow its links, and reconstruct the current documentation state without depending on chat memory.

This is a living control document. It must be updated whenever a major documentation area changes state.

---

## 1. Authority and interpretation rules

### 1.1 Evidence order

When this record conflicts with newer repository evidence, use this order:

1. exact repository files at the current branch/HEAD;
2. fresh test/build/runtime evidence for implementation claims;
3. `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`;
4. this master documentation record;
5. `docs/THE_GAME_MASTER_TASK_REGISTER.md`;
6. current domain master documents;
7. current context logs;
8. historical handoffs and older branch snapshots;
9. chat memory.

### 1.2 Status vocabulary

This record uses the following documentation statuses:

- **ESTABLISHED** — the governing/master contract exists and is usable as authority.
- **PARTIAL** — meaningful documentation exists, but the area is not reconstruction-complete.
- **IN_PROGRESS** — active work is still adding/reconciling required documentation.
- **PENDING** — required documentation has not yet been produced at sufficient depth.
- **BLOCKED** — work is intentionally waiting on another contract, decision, execution environment, or evidence gate.
- **PROPOSAL** — written design exists but is not canon/approved authority yet.
- **HISTORICAL** — useful evidence, but not current top-level authority.
- **SUPERSEDED** — retained only for traceability after a newer authority replaces it.

A file merely existing does **not** mean its domain is complete.

### 1.3 Two different kinds of completion

Every area must distinguish:

- **documentation/contract completion** — the intended behavior, ownership, constraints, migrations, and verification rules are written;
- **content/runtime completion** — the actual world records, assets, implementation, migrations, tests, builds, and device acceptance exist.

This prevents a master-plan file from being mistaken for a finished game system.

---

## 2. Exact repository snapshot used for this record

At source audit HEAD `28809b7abdaf6f7f05ccd58cf0d5e71efacf5e22`:

- tracked repository files: **489**;
- paths in documentation scope (`AGENTS.md`, `README.md`, and `docs/**`): **347**;
- Markdown documentation paths: **319**;
- structured documentation paths under that scope (JSON/YAML/CSV class): **21**;
- paths under `docs/systems/`: **216**;
- paths under `docs/systems/status/`: **204** of those 216;
- paths under `docs/world/`: **18**;
- paths under `docs/assets/`: **46**;
- paths under `docs/android/`: **5**;
- paths under `docs/GAME_CONTEXT_LOGS/`: **13**;
- paths under `docs/evidence/`: **5**;
- paths under `docs/verification/`: **10**.

These are **path counts**, not semantic completion percentages.

The separate all-branch snapshot `docs/ALL_BRANCH_DOCUMENT_INDEX_2026-10-04.md` recorded **432 unique document-like paths** across eight audited documentation branches at the SHAs captured by that snapshot. Its canonical-branch SHA was older than the source audit HEAD above, so it must be treated as a branch-reconciliation snapshot rather than the live count for the current working branch.

Exact current word counts and structured record counts remain governed by D-019 and must be reproduced from a complete checkout before being treated as current totals.

---

## 2.1 Latest D-019 inventory checkpoint

A newer bounded inventory checkpoint now exists for source HEAD `991cd9b29ea0752fa1c303a19e8f210713efe4b5`:

- 490 tracked files;
- 320 Markdown files repository-wide;
- 318 Markdown files under `docs/`;
- 21 structured documentation paths;
- 24 PNG files;
- 42 Python files;
- 68 Kotlin/KTS files;
- 51 Python/Kotlin test-source paths;
- 104 asset-manifest rows resolving to 95 unique asset IDs;
- repository-owned Status Wave-001 audit: 1,019 structured records;
- Gate Twelve baseline: 9 nodes / 8 edges.

Authorities:

- `docs/REPOSITORY_CORPUS_INVENTORY_SNAPSHOT_2026-10-04.md`
- `docs/evidence/repository_inventory_2026-10-04.json`

This advances D-019 but does not complete it. Current-head Markdown word counts, generalized world/domain extractors, provenance-normalized asset-stage counts, and executed-test evidence remain open.

## 2.3 D-044 moving-base reconciliation closure

D-044 is now **DONE**.

The seven selective Class-C migrations are present in current authorities, duplicate `docs/program/*` authority was not imported wholesale, and the conflicting numeric-unit interpretation remains blocked.

Final recheck recorded:

- program ref: `de8c76cc08da20099671b5cd8fc5d7d7acca1920`;
- target ref: `65d2db8538c1b8302c314f2fbe9eb7a1b585b51d`;
- merge base: `c261b2aaf8bd978d27b46f8fea03435c0c5734d0`;
- branch comparison: diverged, program ahead 651 / behind 99;
- PR #33: open, draft, mergeable false.

This closes documentation extraction only. It does not authorize a blind merge/rebase or promotion.

## 2.2 Latest D-042 source-state checkpoint

`docs/DEEP_SOURCE_EXISTING_STATE_AUDIT_2026-10-04.md` now records the exact current-head implementation surface at audited source HEAD `d0382aaf6cca2920a7f315d08153ac6b0dddc5dd`.

Current-head inventory includes:

- 19 Python engine modules;
- 35 Android main Kotlin files;
- 2 authored content JSON files;
- GameState's 17 durable top-level fields and save schema v1 boundary;
- 24 runtime PNGs;
- 21 Python tests;
- 27 Android JVM/unit tests;
- 3 Android instrumented tests;
- 2 GitHub workflows;
- 5 Android build/manifest configuration files.

This closes basic current-head source discovery. D-006/D-042 remain open for cross-branch survivor, consumer, deprecation and exact-execution reconciliation.

## 2.2 Deep current-head source audit checkpoint

`docs/DEEP_SOURCE_EXISTING_STATE_AUDIT_2026-10-04.md` now records a source-grounded D-042 checkpoint for audited HEAD `d0382aaf6cca2920a7f315d08153ac6b0dddc5dd`.

Exact audited source inventory:

- 19 Python engine modules;
- 21 Python test files;
- 2 authored content JSON files;
- 35 Android main Kotlin files;
- 27 Android JVM/unit-test files;
- 3 Android instrumented-test files;
- 24 runtime PNGs;
- 2 GitHub workflows;
- 5 Android Gradle/manifest configuration files.

The audit also records:
- all 17 durable `GameState` fields;
- save schema version 1 boundaries;
- current vertical-slice counts: 19 scenes, 31 choices, 4 quests, 1 character, 1 power, 9 map nodes and 8 edges;
- current responsibility/disposition for every Python engine module and the principal Android/application surfaces.

This closes the current-head path/source inventory portion of D-042. D-042 remains **IN_PROGRESS** because line-by-line consumer mapping, catalog consumers, asset lineage, cross-branch survivor reconciliation and zero-consumer evidence remain open.

## 3. Master documentation map

| Volume / area | Current documentation state | Runtime/content state | Primary authorities | What is still missing |
|---|---|---|---|---|
| **V00 — Program authority / governance** | **ESTABLISHED** | N/A | `MASTER_GAME_DEVELOPMENT_PROGRAM.md`, this record, `THE_GAME_MASTER_TASK_REGISTER.md`, `DOCUMENTATION_CROSS_REFERENCE_MATRIX.md`, `DOCUMENTATION_CORPUS_ARCHITECTURE.md` | Ongoing synchronization; eliminate stale status text when later files overtake older task entries. |
| **V01 — Existing-state audit** | **IN_PROGRESS / CURRENT-HEAD SOURCE INVENTORY COMPLETE** | Current program HEAD is now inventoried at module/component/content/save/asset/test/build level; historical/feature lines are not yet fully reconciled | `DEEP_SOURCE_EXISTING_STATE_AUDIT_2026-10-04.md`, `LIVE_REPOSITORY_STATE_AUDIT_2026-10-02.md`, `EXISTING_STATE_REWORK_DECISION_MATRIX.md`, `IMPLEMENTATION_PR_7_31_RECONCILIATION_2026-10-02.md` | Finish field/consumer mapping, per-catalog consumer audit, cross-branch survivor migration, asset lineage/equivalence, zero-consumer proof, D-044 Class-C extraction is now complete. |
| **V02 — Pixel-art / visual production** | **PARTIAL / IN_PROGRESS** | Many assets and runtime bindings exist, but canonical production/provenance/QA is not complete | `PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`, `PIXEL_ART_PRODUCTION_AND_REUSE_LEDGER.md`, `ASSET_PROVENANCE_REGISTRY.md`, provenance family indexes | Finish D-029 provenance; execute deterministic raster equivalence tooling; resolve remaining visual promotion decisions; finish Jack/portrait production and device QA. |
| **V03 — Gate Twelve proof region** | **ESTABLISHED FIRST-PASS CONTRACT** | Implementation/acceptance remains incomplete | `GATE_TWELVE_REGION_MASTER_PLAN.md`, map/animation blueprints, asset status matrix, room composition contract | Parent-world proposal still requires owner canon decision; bounded runtime migration and physical-device acceptance remain future work. |
| **V04 — World development** | **ESTABLISHED STANDARDS / PARTIAL POPULATION** | World is not populated at final scale | `WORLD_DEVELOPMENT_MASTER_INDEX.md`, geography/politics/settlement/routes/ecology/beast/population/balance/loot/NPC standards | Canon macroregions, sovereign entities, settlements, routes, ecosystems, populations, institutions, and large-scale structured records. |
| **V05 — Characters / NPC / social / rivals** | **PARTIAL** | Existing engine has social/memory concepts; target corpus is not exhaustive | `NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md`, population/hierarchy standards, player-safe actor contract | Full character catalog, recurring-NPC packets, schedules/goals/factions, dynamic-rival hierarchy/evolution records, world integration and migration mapping. |
| **V06 — Progression / stats / skills / abilities / passives / classes / ranks** | **LARGE ACTIVE CORPUS / IN_PROGRESS** | Target design substantially exceeds current runtime | `PROGRESSION_MASTER_PLAN.md`, `PROGRESSION_CLASSES_RANKS_EVOLVED_GAME_DESIGN.md`, `EVOLVED_SKILL_REGISTRY.md`, `STATUS_UI_ABILITIES_AND_PASSIVES_MASTER_PLAN.md`, `docs/systems/status/**` | Status Phase A is complete; Wave 001 has 1,019 structurally audited records; primary-ability detail coverage is 47/47 and passive family baseline coverage is 23/23. Still missing: combat-class catalog; profession/rank/status packet; training/mentor/facility standard; progression Gate Twelve proof packet; progression UX contract; numeric/range fixtures; world/canon promotion; target-schema/API migration. |
| **V07 — Items / economy / loot** | **MASTER CONTRACT ESTABLISHED / CONTENT PARTIAL** | Existing equipment/items are not the final target economy | `ITEM_ECONOMY_LOOT_MASTER_PLAN.md`, world loot provenance standard, asset/item provenance docs | Full item taxonomy/catalog, economy source/sink model, vendor/services rules where approved, resource-to-item chains, loot tables, migration to existing IDs/save consumers. |
| **V08 — Tactical combat** | **MASTER CONTRACT ESTABLISHED / DETAIL PARTIAL** | Final tactical runtime not implemented | `TACTICAL_COMBAT_MASTER_PLAN.md`, balance integration docs | Combat class/archetype catalog, encounter/tactical-map standards, AI detail, action-economy calibration, progression/item/status integration, schema/API migration and tests. |
| **V09 — Persistent adversaries / world memory** | **PARTIAL** | Concepts exist; target system is not reconstruction-complete | `NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md`, social engine evidence, world integration standards | Dedicated adversary/rival records, hierarchy changes, memory consequences, promotion/demotion rules, world event integration, save/state migration contract. |
| **V10 — Activities / life simulation** | **MASTER CONTRACT ESTABLISHED / CONTENT PARTIAL** | Current simulation is narrower than target design | `PLAYER_ACTIVITIES_AND_LIFE_LOOP_MASTER_PLAN.md` | Activity catalog, training/work/study/recovery content, concurrency/interruption fixtures, facility links, world schedules, progression/economy/social integration. |
| **V11 — Application UX / projection** | **PARTIAL / IN_PROGRESS** | Current Android client exists but is not final target UX | `APPLICATION_UX_MASTER_PLAN.md`, `ANDROID_CONSUMER_AND_PROJECTION_MAP.md`, `PLAYER_SAFE_ROOM_ACTOR_PROJECTION_CONTRACT.md`, status UI contracts | Finish line-by-line consumer/ViewModel/bridge mapping, complete missing player-safe projections, progression/status UX integration, migration and QA mapping. |
| **V12 — Android / final APK reconstruction** | **PLANNED / BLOCKED FOR EXECUTION** | Final rebuild intentionally not started as a destructive rewrite | `APK_REBUILD_AND_EVOLUTION_MASTER_PLAN.md`, `APK_FINAL_RECONSTRUCTION_MATRIX.md`, final reconstruction blueprint | Mechanics migration packets, completed consumer map, teardown manifest, zero-consumer deletion evidence, final rebuild, exact-head CI, APK provenance and physical handset validation. |

---

## 4. What is already done

The following are considered completed documentation deliverables, not completed game implementation:

### 4.1 Program control layer

- master game-development/documentation authority exists;
- corpus architecture exists;
- cross-reference system exists;
- directive execution breakdown exists;
- reconstruction blueprint exists;
- owner-directive traceability matrix exists;
- task register exists;
- baseline documentation catalog and evidence catalog exist;
- all-branch path inventory exists;
- branch reconciliation documents exist for the major documentation program drift already investigated.

### 4.2 Gate Twelve contract layer

- Gate Twelve Steps 1–14 have a first-pass written contract;
- map pixel-asset blueprint exists;
- animation blueprint exists;
- region master plan exists;
- asset status/production matrix exists;
- room composition rules exist;
- player-safe actor/panel projection contract exists;
- external connection/expansion register exists;
- parent-world proposal exists as a **proposal**, not accepted canon.

### 4.3 World standards layer

Written standards currently cover:

- world hierarchy/geography;
- logical coordinate and scale rules;
- stable world entity IDs/references;
- political entities;
- settlement structure;
- travel/routes;
- ecosystem/resources;
- beast zones;
- population/citizen hierarchy;
- world balance/level bands;
- loot provenance;
- NPC population;
- region/settlement documentation templates.

This means the **schema/authoring layer exists**. It does not mean the full world has been authored.

### 4.4 Gameplay-system master layer

Master or major design documents exist for:

- progression;
- evolved skills;
- classes/ranks direction;
- status UI;
- primary abilities;
- passives;
- rarity;
- awakening;
- Level/XP;
- Level-100 exception behavior;
- ability/passive knowledge visibility;
- NPC/social/rival direction;
- tactical combat;
- items/economy/loot;
- world balance integration;
- activities/life loop;
- save/content migration.

The status/ability/passive corpus is currently the deepest documentation area in the repository.

### 4.5 Visual/asset governance layer

Written governance exists for:

- pixel-art runtime composition;
- production/reuse;
- room actor/panel/overlay reuse;
- asset manifests;
- source/raster correspondence;
- asset-family provenance;
- character/equipment/item/actor provenance;
- environment/scene/map provenance;
- UI/FX/animation provenance;
- Gate Twelve visual production.

### 4.6 Android/application layer

Written planning exists for:

- application-wide UX;
- Android consumer/projection ownership;
- player-safe room actor projection;
- final APK evolution;
- final APK keep/rework/replace/remove sequencing.

Execution of the final APK reconstruction remains intentionally gated.

---

## 5. What is not done yet

### 5.1 P0 — Documentation control and reconciliation

1. **Continue the deep existing-state audit (D-006 / D-042).**  
   The exact current-head path/responsibility slice is now documented in `docs/DEEP_SOURCE_EXISTING_STATE_AUDIT_2026-10-04.md`: 19 Python engine modules, 35 Android main Kotlin files, 2 content packs, exact save fields/schema, 24 runtime PNGs, 51 Android/Python test-source files plus build/workflow surfaces. Remaining work is cross-branch and consumer-level reconciliation rather than basic current-head discovery.

2. **Finish the reproducible current-head inventory (D-019).**  
   The repository has an inventory tool and historical exact snapshots, but current exact word/record/asset-stage/test-evidence totals still need a complete-checkout execution and persisted result.

3. **Finish PR #33 moving-base reconciliation (D-044).**  
   Shared-file reconciliation is complete; remaining Class-C / EXTRACT UNIQUE documents must be inspected for genuinely unique requirements.

4. **Reconcile stale task-register text against the live tree.**  
   Example: D-046's older NEXT text names several standards as future work even though files such as `ABILITY_RARITY_STANDARD.md`, `PRIMARY_ABILITY_REGISTRY_SCHEMA.md`, `PASSIVE_REQUIREMENT_LANGUAGE.md`, `STATUS_KNOWLEDGE_VISIBILITY_STANDARD.md`, `LEVEL_AND_XP_STANDARD.md`, `AWAKENING_EVENT_STANDARD.md`, and `LEVEL_100_EXCEPTION_STANDARD.md` now exist. The task remains in progress, but its next-step list must be refreshed rather than trusted literally.

### 5.2 P0 — Asset and implementation truth

5. **Finish visual/application survivor reconciliation (D-020) and exact asset provenance (D-029).**  
   PR-level reconciliation is complete through D-028, but final migration/reimplementation/supersession decisions still need to be consolidated. Current family-level provenance is strong but incomplete. Deterministic raster equivalence still needs execution and persisted evidence.

6. **Finish Android consumer mapping (D-026 / D-021).**  
   The high-level map exists; line-by-line composable/ViewModel/bridge/test mapping is not complete.

7. **Resolve Gate Twelve parent-world canon (D-031).**  
   A proposal exists. It must remain non-canon until accepted or revised by the owner.

8. **Create mechanics schema/API migration packets (D-032).**  
   Target progression/social/items/combat/adversary designs must be mapped to current engine APIs, saves, projections and tests before broad code migration.

### 5.3 P1 — Reconstruction-depth domain work

9. **Progression continuation (D-045 / D-046).**  
   Current Status/ability/passive work is materially ahead of the older task-register snapshot:
   - Phase A governing standards are complete;
   - Wave 001 structurally contains 1,019 records;
   - primary-ability detail packet coverage is complete for 47 / 47 identities;
   - passive Phase-C family baseline coverage is complete for 23 / 23 families;
   - conceptual passive owner/write-target mapping covers 230 / 230 passive IDs.

   Still missing as reconstruction-grade progression work:
   - combat class catalog;
   - profession/rank/status packet;
   - training/mentor/facility standard;
   - Gate Twelve progression proof packet;
   - progression UX contract;
   - justified parent-system range/test fixtures and numeric envelopes;
   - remaining world/knowledge integration and state-owner/runtime mappings;
   - record-level canon promotion / owner approval;
   - implementation migration packets.

10. **World population.**  
    The standards exist, but final macroregions, political entities, settlements, routes, ecosystems, resource zones, beast populations, citizens, institutions and world events are not authored at target scale.

11. **Character/NPC population.**  
    Full recurring-character packets, schedules, goals, social state, rival evolution, factions and world placement remain incomplete.

12. **Items/economy population.**  
    Full item/resource/equipment/economy records and migration mapping remain incomplete.

13. **Combat reconstruction depth.**  
    Tactical rules need detailed catalogs, calibrated fixtures, encounter standards, AI behaviors and integration packets.

14. **Persistent rival/world-memory reconstruction depth.**  
    The concept has a master direction but needs dedicated operational records and persistence/migration rules.

15. **Activities/life-loop content population.**  
    The contract exists, but concrete activities/facilities/schedules and their cross-system records remain incomplete.

### 5.4 Late-stage blocked work

16. **APK teardown manifest (D-033) remains blocked.**
17. **Final APK reconstruction remains blocked.**
18. **Physical Galaxy A03 acceptance remains unverified unless new physical-device evidence is explicitly recorded.**
19. **Destructive deletion/replacement remains blocked until zero-consumer evidence, migration and rollback boundaries exist.**

---

## 6. Known state mismatches that this record must prevent

### 6.1 Existing file does not equal completed domain

Examples:

- a world settlement standard does not equal a populated world;
- a tactical-combat master does not equal implemented tactical combat;
- an APK reconstruction plan does not equal a rebuilt APK;
- an ability/passive schema does not equal all ability/passive records being canon and balanced;
- a provenance registry seed does not equal every asset being verified.

### 6.2 Historical counts do not equal current counts

The 2026-10-02 baseline inventory and the 2026-10-04 all-branch index remain useful evidence, but neither should silently replace a fresh current-head inventory.

### 6.3 Task-register NEXT fields may drift

When a named future document now exists, update the task entry or this master record rather than continuing to repeat an obsolete NEXT list.

### 6.4 Documentation branch evidence is not runtime verification

PR #33 is primarily a documentation program. Documentation commits do not prove Android runtime behavior, raster pixel equality, physical handset behavior, or gameplay migration unless those checks were actually executed for the relevant implementation head.

---

## 7. Required update protocol

Whenever meaningful documentation work is completed:

1. verify the current branch/HEAD;
2. create or update the domain document;
3. update `docs/THE_GAME_MASTER_TASK_REGISTER.md`;
4. update this master record if the area's state changed;
5. update the cross-reference matrix when authority/dependency relationships changed;
6. update `DOCUMENTATION_PROGRESS_LEDGER.md` when measurable corpus state changed;
7. update evidence/inventory files when counts or verification changed;
8. record blockers explicitly instead of implying completion;
9. preserve superseded material only when it has historical/reconciliation value;
10. never mark a domain complete merely because a master-plan file was created.

For a domain to move to **ESTABLISHED / reconstruction-grade**, the documentation should normally define:

- current reality;
- target design;
- ownership/state boundaries;
- data/schema or record shape;
- dependencies;
- cross-system integrations;
- migration impact;
- content requirements;
- asset/UI requirements when applicable;
- tests/verification;
- unresolved decisions;
- implementation order;
- rollback/recovery boundaries where applicable.

---

## 8. Immediate recommended execution order

The current strongest order is:

1. **Use this file as the master status index.**
2. **Reconcile the task register with the live 2026-10-04 tree**, removing stale NEXT statements without deleting historical evidence.
3. **Complete D-019 current-head inventory** so file/word/record/asset/test totals are reproducible at the current program head.
4. **Complete D-006/D-042 existing-state audit** at file/consumer level.
5. **D-044 moving-base reconciliation is complete.**  
   Shared authority, unique child migrations and all seven Class-C selective extraction actions are reconciled. PR #33 remains divergent/non-mergeable; this is a branch-governance condition, not unfinished Class-C extraction.

6. **
6. **Complete D-029 asset provenance/equivalence evidence.**
7. **Complete D-026/D-021 Android consumer mapping.**
8. **Resolve D-031 Gate Twelve parent-world canon with the owner.**
9. **Continue D-045 progression children**, beginning with the combat class catalog.
10. **Create D-032 migration packets** before broad runtime reconstruction.
11. **Populate world/character/item/combat/life-loop content only against the accepted standards.**
12. **Keep final APK teardown/rebuild late-stage and gated.**

---

## 9. Navigation index

### Program and control

- `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`
- `docs/FINAL_GAME_RECONSTRUCTION_BLUEPRINT.md`
- `docs/MASTER_DIRECTIVE_EXECUTION_BREAKDOWN.md`
- `docs/DOCUMENTATION_CORPUS_ARCHITECTURE.md`
- `docs/DOCUMENTATION_CROSS_REFERENCE_MATRIX.md`
- `docs/DOCUMENTATION_PROGRESS_LEDGER.md`
- `docs/THE_GAME_MASTER_TASK_REGISTER.md`
- `docs/OWNER_DIRECTIVE_TRACEABILITY_MATRIX_2026-10-02.md`

### Audit and branch truth

- `docs/LIVE_REPOSITORY_STATE_AUDIT_2026-10-02.md`
- `docs/REPOSITORY_CORPUS_INVENTORY_SNAPSHOT_2026-10-02.md`
- `docs/DOCUMENTATION_CATALOG_2026-10-02.md`
- `docs/ALL_BRANCH_DOCUMENT_INDEX_2026-10-04.md`
- `docs/IMPLEMENTATION_PR_7_31_RECONCILIATION_2026-10-02.md`
- `docs/PR33_MOVING_BASE_DRIFT_RECONCILIATION_2026-10-02.md`
- `docs/PR33_LIVE_SHARED_FILE_RECONCILIATION_2026-10-03.md`
- `docs/PR33_CLASS_C_UNIQUE_REQUIREMENT_EXTRACTION_2026-10-03.md`

### World

- `docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`
- `docs/world/WORLD_GEOGRAPHY_STANDARD.md`
- `docs/world/WORLD_COORDINATE_AND_SCALE_STANDARD.md`
- `docs/world/WORLD_ENTITY_ID_AND_REFERENCE_STANDARD.md`
- `docs/world/WORLD_POLITICAL_ENTITIES.md`
- `docs/world/WORLD_SETTLEMENT_CATALOG.md`
- `docs/world/WORLD_TRAVEL_AND_ROUTES.md`
- `docs/world/WORLD_ECOSYSTEM_AND_RESOURCES.md`
- `docs/world/WORLD_BEAST_ZONE_STANDARD.md`
- `docs/world/WORLD_POPULATION_AND_CITIZEN_HIERARCHY.md`
- `docs/world/WORLD_BALANCE_AND_LEVEL_BANDS.md`
- `docs/world/WORLD_LOOT_PROVENANCE_STANDARD.md`
- `docs/world/WORLD_NPC_POPULATION_STANDARD.md`

### Systems

- `docs/systems/PROGRESSION_MASTER_PLAN.md`
- `docs/systems/PROGRESSION_CLASSES_RANKS_EVOLVED_GAME_DESIGN.md`
- `docs/systems/EVOLVED_SKILL_REGISTRY.md`
- `docs/systems/STATUS_UI_ABILITIES_AND_PASSIVES_MASTER_PLAN.md`
- `docs/systems/status/README.md`
- `docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md`
- `docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md`
- `docs/systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md`
- `docs/systems/PLAYER_ACTIVITIES_AND_LIFE_LOOP_MASTER_PLAN.md`
- `docs/systems/WORLD_BALANCE_INTEGRATION_PLAN.md`
- `docs/systems/SAVE_AND_CONTENT_MIGRATION_MASTER_PLAN.md`

### Visual/assets

- `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`
- `docs/assets/PIXEL_ART_PRODUCTION_AND_REUSE_LEDGER.md`
- `docs/assets/ASSET_PROVENANCE_REGISTRY.md`
- `docs/assets/ASSET_FAMILY_PROVENANCE_INDEX_2026-10-03.md`
- `docs/assets/GATE_TWELVE_REGION_MASTER_PLAN.md`
- `docs/assets/GATE_TWELVE_ASSET_STATUS_AND_PRODUCTION_MATRIX.md`
- `docs/assets/ROOM_COMPOSITION_IMPLEMENTATION_CONTRACT.md`
- `docs/assets/ROOM_ACTOR_PANEL_OVERLAY_REUSE_STANDARD.md`

### Android/application

- `docs/android/APPLICATION_UX_MASTER_PLAN.md`
- `docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md`
- `docs/android/PLAYER_SAFE_ROOM_ACTOR_PROJECTION_CONTRACT.md`
- `docs/android/APK_REBUILD_AND_EVOLUTION_MASTER_PLAN.md`
- `docs/android/APK_FINAL_RECONSTRUCTION_MATRIX.md`

---

## 10. Definition of success for this master record

This record is successful when a new developer or AI agent can answer all of the following without asking the owner to repeat prior work:

- what the documentation program is trying to build;
- what the current repository authority is;
- what documentation areas exist;
- which areas are complete only at the contract level;
- which areas are still partial;
- what is missing;
- what is blocked;
- what decisions require the owner;
- which documents contain the detail;
- which task should be done next;
- which completion claims are backed by evidence.

The record must remain shorter than the full corpus and must point outward rather than absorb every detail into one unmaintainable file.
