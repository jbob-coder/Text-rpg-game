# Branch Source Audit — docs/master-game-development-program

Status: **REVIEWABLE / SOURCE RECONCILIATION**
Repository: `jbob-coder/Text-rpg-game`
Source branch: `docs/master-game-development-program`
Source head at audit: `4d596bcd27b6e2f8ef9ce3a93b9dab22f5f4812e`
Current authority branch: `docs/settlement-region-build-plan`

## Purpose

Audit the former master-development branch as a source for current documentation, implementation archaeology, migration planning and future numbered-corpus ownership.

This branch is not current authority merely because it called itself a master program. Its compatible material must be reconciled into the current program.

## Structural inventory

Source branch total files: **239**

Observed families:
- `docs/**`: 97 files;
- `android/**`: 94 files;
- `src/**`: 19 files;
- `tests/**`: 20 files;
- `content/**`: 2 files.

The branch is therefore a mixed documentation + implementation snapshot, not a documentation-only branch.

## Major source groups

### Program/control documents

High-value sources:
- `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`
- `docs/MASTER_DIRECTIVE_EXECUTION_BREAKDOWN.md`
- `docs/DOCUMENTATION_CORPUS_ARCHITECTURE.md`
- `docs/DOCUMENTATION_CROSS_REFERENCE_MATRIX.md`
- `docs/DOCUMENTATION_PROGRESS_LEDGER.md`
- `docs/EXISTING_STATE_REWORK_DECISION_MATRIX.md`
- `docs/LIVE_REPOSITORY_STATE_AUDIT_2026-10-02.md`
- `docs/REPOSITORY_CORPUS_INVENTORY_SNAPSHOT_2026-10-02.md`

Classification:
**KEEP AS SOURCE / PARTIALLY SUPERSEDED / EXTRACT UNIQUE RULES**

Strong reusable material:
- documentation-before-destruction;
- KEEP / EXTEND / REWORK / REPLACE / REMOVE / UNKNOWN classification;
- explicit source-of-truth hierarchy;
- separation of gameplay authority from Compose/UI;
- stable-ID/save-schema protection;
- domain-volume decomposition;
- cross-reference ownership;
- exact-head evidence discipline;
- final APK reconstruction as late-stage work;
- current-vs-target-vs-migration distinction.

### Critical supersession — 2,000,000 unit

The former master program stated that the unit of “2,000,000 documentation” was undefined and should be tracked across multiple metrics.

That ambiguity is now **SUPERSEDED**.

Current owner directive and production architecture explicitly define:

- target: **2,000,000 separate documentation files**;
- 100 files per sub-batch;
- 1,000 files per batch;
- 2,000 batches total;
- no filler.

Therefore any old branch statement saying the unit is unresolved must not be promoted into current authority.

Secondary metrics such as words, structured records, tests, assets and tasks may still be useful operational telemetry, but they do not replace the file-count mandate.

## World-development sources

High-value files include:
- `docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`
- `docs/world/WORLD_COORDINATE_AND_SCALE_STANDARD.md`
- `docs/world/WORLD_GEOGRAPHY_STANDARD.md`
- `docs/world/WORLD_POLITICAL_ENTITIES.md`
- `docs/world/WORLD_SETTLEMENT_CATALOG.md`
- `docs/world/WORLD_TRAVEL_AND_ROUTES.md`
- `docs/world/WORLD_ECOSYSTEM_AND_RESOURCES.md`
- `docs/world/WORLD_BEAST_ZONE_STANDARD.md`
- `docs/world/WORLD_POPULATION_AND_CITIZEN_HIERARCHY.md`
- `docs/world/WORLD_BALANCE_AND_LEVEL_BANDS.md`
- `docs/world/WORLD_LOOT_PROVENANCE_STANDARD.md`
- `docs/world/WORLD_NPC_POPULATION_STANDARD.md`
- `docs/world/WORLD_SCALE_DOCUMENTATION_BLUEPRINT.md`

Classification:
**HIGH-VALUE D-01/D-05 SOURCE / RECONCILE WITH CURRENT WORLD FOUNDATION**

Important overlap with current active docs:
- current `WORLD_SPATIAL_HIERARCHY_AND_COORDINATES.md`;
- current `WORLD_ENTITY_ID_AND_REFERENCE_STANDARD.md`;
- current `REGION_SETTLEMENT_DOCUMENTATION_TEMPLATE.md`;
- current `WORLD_MAP_PRODUCTION_SEQUENCE.md`;
- current `BEAST_ZONE_AND_ECOSYSTEM_SCHEMA.md`;
- current Gate Twelve external-connections register.

Do not duplicate old world standards one-for-one. Compare fields and migrate unique constraints.

## Gameplay-system sources

High-value files:
- `docs/systems/PROGRESSION_MASTER_PLAN.md`
- `docs/systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md`
- `docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md`
- `docs/systems/PLAYER_ACTIVITIES_AND_LIFE_LOOP_MASTER_PLAN.md`
- `docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md`
- `docs/systems/WORLD_BALANCE_INTEGRATION_PLAN.md`
- `docs/systems/SAVE_AND_CONTENT_MIGRATION_MASTER_PLAN.md`
- `docs/systems/GAMEPLAY_SYSTEM_REBUILD_MATRIX.md`

Classification:
**HIGH-VALUE D-03/D-04/D-05 SOURCE**

Strong current-compatible decisions include:
- existing deterministic Python engine remains gameplay authority until migrated;
- stats/abilities/persistence/quests/social foundations are valuable existing contracts;
- classes/professions/ranks need explicit layered meanings;
- social hierarchy should not collapse into one global discrimination scalar;
- tactical combat must be original and state-driven;
- persistent adversary design must use original terminology/UI/data;
- save and stable IDs are high-risk migration boundaries;
- NPC autonomy must not require hosted AI for base functionality.

Every system file still requires comparison with later integration branches before it can be treated as implementation-ready authority.

## Android/APK sources

High-value files:
- `docs/android/APK_REBUILD_AND_EVOLUTION_MASTER_PLAN.md`
- `docs/android/APK_FINAL_RECONSTRUCTION_MATRIX.md`
- `docs/android/APPLICATION_UX_MASTER_PLAN.md`
- `docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md`
- `docs/ANDROID_PIXEL_CLIENT_VALIDATION.md`

Classification:
**HIGH-VALUE D-06 SOURCE / IMPLEMENTATION ARCHAEOLOGY**

Reusable boundaries:
- UI consumes player-safe projections;
- Compose does not own authoritative gameplay state;
- final APK rebuild is late-stage;
- component changes require migration/consumer audit;
- physical-device evidence must not be fabricated from emulator-only evidence;
- navigation/screens may be reworked or replaced while persistent contracts require stronger migration discipline.

## Pixel-art / visual-production sources

Observed documentation includes:
- 500-unit asset roadmaps/batches;
- asset provenance;
- character pixel blueprints;
- Gate Twelve map/scene/animation blueprints;
- room actor/panel/overlay reuse standard;
- runtime pixel composition standard;
- reference-to-blueprint pipeline;
- production manifests and wave packets.

Classification:
**HIGH-VALUE D-02 SOURCE / ASSET LINEAGE**

Current handling:
- preserve stable asset provenance;
- distinguish production assets from references;
- retain base-art vs overlay state separation;
- map asset consumer relationships;
- reconcile Jack visual reference and overlay rig lineage against later branches;
- do not assume every planned asset was actually produced.

## Observed implementation snapshot

This branch contains substantial Android and Python implementation:
- 94 Android files;
- 19 Python source files;
- 20 Python/Android test files;
- content/vertical-slice data;
- verification logs and manifests.

Classification:
**EVIDENCE SOURCE, NOT AUTOMATIC CURRENT IMPLEMENTATION**

A source file existing on this historical branch proves only that it existed at this branch head. It does not prove:
- current active branch contains it;
- tests still pass now;
- later branches did not replace it;
- final architecture should retain it.

## Existing-state rework matrix

The source matrix uses:
- KEEP;
- EXTEND;
- REWORK;
- REPLACE;
- REMOVE;
- UNKNOWN;
- NEW.

This is compatible with the current program's broader classifications, but current active owner documentation also uses:
- UPDATE;
- REWRITE;
- SUPERSEDE;
- MERGE;
- DELETE for documentation;
- KEEP / UPGRADE / REWORK / REPLACE / DELETE / REBUILD for application components.

Current documents control vocabulary where conflicts exist.

## Notable current-compatible world principles

- world hierarchy and coordinate spaces must be explicit;
- missing parent geography around Gate Twelve must remain unknown rather than invented;
- cities/villages must have functional reasons to exist;
- ecology should drive beast/resource placement;
- loot requires provenance;
- political entities should produce gameplay consequences;
- NPC population has persistence/detail tiers;
- world balance should not automatically scale every threat to the player;
- routes/travel and tactical coordinates are distinct coordinate spaces.

## Notable current-compatible visual principles

- source-native pixel art;
- nearest-neighbor presentation;
- player/actor identity distinct from reusable rig;
- equipment overlays remain separate;
- map state overlays remain state overlays;
- scene actors derive from player-safe state;
- provisional geometric presentation may be replaced by authored art;
- final art quality/provenance must be audited asset-by-asset.

## Conflicts / stale assumptions requiring review

1. Old ambiguity about the 2,000,000 unit — **SUPERSEDED**.
2. Old branch self-designation as “primary program” — historical; current branch/program now governs.
3. Statements that specific PR numbers/stack states are current — historical snapshot only.
4. Any claim that a test/build was passing must remain tied to its exact historical head.
5. World schemas in this branch may overlap current world documents and must be merged by ownership, not copied.
6. Any “current” implementation statement dated before later branch evolution requires fresh verification.
7. Any old asset status must be reconciled with later pixel/UI branches and current provenance registers.

## Current-domain mapping

| Source family | Current domain | Handling |
|---|---|---|
| program/control | D-07 | EXTRACT + SUPERSEDE STALE AUTHORITY |
| world | D-01 | FIELD-BY-FIELD RECONCILIATION |
| progression/combat | D-04 | COMPARE WITH RULES/ABILITY LINEAGE |
| NPC/social/rivals | D-03 | GENERALIZE + RECONCILE |
| items/economy/ecology | D-05 | RECONCILE + SPLIT OWNERSHIP |
| pixel/assets/UI | D-02 | ASSET/CONSUMER/PROVENANCE AUDIT |
| Android/APK | D-06 | COMPONENT/MIGRATION AUDIT |
| source/tests | evidence layer | EXACT-HEAD HISTORICAL EVIDENCE |

## Future numbered-document candidates justified by this source

This audit identifies candidate ownership areas but does not reserve IDs automatically:
- branch/source provenance standard;
- source-branch currentness/evidence rule;
- historical test-evidence rule;
- subsystem rework classification contract;
- world-standard reconciliation matrix;
- pixel-asset provenance/consumer reconciliation;
- Android component archaeology/audit;
- implementation lineage map;
- PR/branch historical evidence standard;
- domain-specific migration-from-historical-branch guides.

These should enter manifests only after anti-filler review.

## Verification completed

- branch tree recursively enumerated;
- top-level file-family counts recorded;
- master program reviewed;
- master directive breakdown reviewed;
- corpus architecture reviewed;
- cross-reference matrix reviewed;
- repository/live-state audits reviewed;
- existing-state rework matrix reviewed;
- world development master reviewed;
- Android/system/asset document families enumerated.

## Result

This branch is a major source reservoir. It should be mined aggressively, but not merged wholesale.

The strongest strategy is:
`source file -> current-domain owner -> conflict check -> deduplicate -> migrate unique rule/evidence -> numbered-document ownership -> implementation trace`.

## Next action

Audit the rules/ability lineage next, beginning with:
- `integration/rules-ability-v6-reconcile`;
- `fix/v6-runtime-boundaries`;
and compare them against the current progression/combat/system documentation before issuing system-level corpus files.