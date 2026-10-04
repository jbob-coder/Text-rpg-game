# THE GAME — Deep Source Existing-State Audit — 2026-10-04

Status: **ACTIVE / CURRENT-HEAD SOURCE INVENTORY COMPLETE / CROSS-BRANCH RECONCILIATION REMAINS**  
Repository: `jbob-coder/Text-rpg-game`  
Branch: `docs/master-game-development-program`  
Audited HEAD: `d0382aaf6cca2920a7f315d08153ac6b0dddc5dd`  
Parents:
- `docs/EXISTING_STATE_REWORK_DECISION_MATRIX.md`
- `docs/LIVE_REPOSITORY_STATE_AUDIT_2026-10-02.md`
- `docs/MASTER_DOCUMENTATION_RECORD.md`

## 1. Purpose

This document advances D-006 / D-042 from high-level subsystem classification to an exact current-head inventory of:

- Python engine modules;
- Android runtime/application components;
- authored content packs;
- durable save/state fields;
- raster assets;
- test-source files;
- build/workflow surfaces.

The dispositions below apply to the **current source responsibility**. They are not permission to delete files. Cross-branch survivor migration, line-by-line Android consumer mapping, and final teardown decisions remain separate work.

## 2. Exact current-head structure

At the audited HEAD:

| Area | Exact count |
| --- | ---: |
| Python engine modules under `src/textrpg/` | 19 |
| Python test files under `tests/` | 21 |
| authored JSON files under `content/` | 2 |
| Android main Kotlin files | 35 |
| Android JVM/unit-test Kotlin files | 27 |
| Android instrumented-test Kotlin files | 3 |
| Android runtime PNGs in `drawable-nodpi` | 24 |
| GitHub workflow files | 2 |
| Android Gradle/manifest configuration files | 5 |

No runtime tests were executed by this audit. These are source/path counts and source inspections.

## 3. Python engine module inventory

| File | Current responsibility observed from source | Disposition |
| --- | --- | --- |
| `src/textrpg/__init__.py` | package/export surface | **KEEP**, update exports only with controlled API evolution |
| `src/textrpg/android_bridge.py` | player-safe Android session façade; scene/status/inventory/quest/map/visual projection; choose/travel/equip/save/load/cheat actions | **KEEP + EXTEND**, preserve player-safe boundary; evolve projection contracts rather than bypassing them |
| `src/textrpg/cli.py` | local development terminal client | **KEEP as development client**, not final presentation authority |
| `src/textrpg/content.py` | authored content-pack loading into engine/state | **KEEP + EXTEND** |
| `src/textrpg/core.py` | `GameState`, `RulesEngine`, choice/scene execution, checks/effects, player-safe scene projection | **KEEP + EXTEND**, high-authority runtime |
| `src/textrpg/equipment.py` | equipment requirement validation and equip mutation | **KEEP + EXTEND**; slot/schema migration requires explicit contract |
| `src/textrpg/json_contract.py` | strict finite JSON decoding | **KEEP** |
| `src/textrpg/modifiers.py` | equipment/perk/condition/set modifier validation and effective-value breakdown | **KEEP + EXTEND** |
| `src/textrpg/persistence.py` | schema-versioned JSON save/load with transactional file replacement | **KEEP / HIGH-RISK**; migration only |
| `src/textrpg/powers.py` | ability discovery, resources, technique use/mastery/practice/evolution and player view | **KEEP FOUNDATION + REWORK/EXTEND** into final ability taxonomy |
| `src/textrpg/progression.py` | ability mastery stages and technique availability | **KEEP NOW / MIGRATION-CONTROLLED EXTEND** |
| `src/textrpg/quests.py` | quest graph validation, start/objective/failure/terminal resolution | **KEEP + EXTEND** |
| `src/textrpg/schema.py` | current attribute/resource/derived-stat specifications | **KEEP CURRENT CONTRACT**; final progression changes require migration |
| `src/textrpg/simulation.py` | time advance, conditions, recovery and training | **KEEP + EXTEND** toward activity/life-loop contract |
| `src/textrpg/social.py` | NPC memory/knowledge/sharing/leaks/relationships/goals/story transitions | **KEEP + EXTEND** toward schedules/factions/rival system |
| `src/textrpg/stats.py` | player stat validation, derived stats and resource initialization | **KEEP CURRENT CONTRACT / EXTEND THROUGH PROGRESSION MIGRATION** |
| `src/textrpg/status.py` | player-safe status projection and inspected contribution view with hidden-state redaction | **KEEP + EXTEND**, privacy boundary is high-risk |
| `src/textrpg/validation.py` | registry, scene, world-map and content-pack validation | **KEEP + EXTEND** |
| `src/textrpg/visuals.py` | recurring-character visual identity validation/generation contract | **KEEP + EXTEND** into final provenance/identity pipeline |

### 3.1 Important source-scale observations

The largest current Python responsibilities include:

- `powers.py`: 2,061 source lines at the audited version;
- `core.py`: 793 lines;
- `validation.py`: 782 lines;
- `android_bridge.py`: 776 lines;
- `social.py`: 680 lines.

These sizes are not defects by themselves. They identify likely future decomposition pressure if the target systems grow substantially.

## 4. Durable GameState / save contract

Current `GameState` fields observed in `core.py`:

1. `seed`
2. `scene_id`
3. `turn`
4. `time_minutes`
5. `player`
6. `flags`
7. `relationships`
8. `knowledge`
9. `inventory`
10. `quests`
11. `npcs`
12. `party`
13. `abilities`
14. `equipment`
15. `perks`
16. `schema_version`
17. `history`

Current save schema facts from `persistence.py`:

- `CURRENT_SCHEMA_VERSION = 1`;
- saves reject a schema version other than 1;
- loader requires non-empty `seed` and `scene_id`;
- unknown top-level save fields are rejected;
- loaded state is validated through `validate_game_state_structure`;
- save writes use a temporary file followed by replacement.

Disposition:

**KEEP / HIGH-RISK CONTRACT.** No new top-level persistent field, renamed field, changed stable-ID meaning, or schema bump should occur without D-032/save-migration documentation and regression evidence.

## 5. Current authored content inventory

### 5.1 `content/vertical_slice_01.json`

Source SHA at audited branch:
`bd07e2434e42c10ce6776be14734c18d53ac0c56`

Current record counts:

| Record | Count |
| --- | ---: |
| scenes | 19 |
| choices across scenes | 31 |
| quests | 4 |
| characters | 1 |
| powers | 1 |
| knowledge registry entries | 8 |
| perk registry entries | 1 |
| item registry entries | 6 |
| condition registry entries | 1 |
| world-map nodes | 9 |
| world-map edges | 8 |

Declared canon status: `provisional_canon`.

Disposition:

**KEEP AS CURRENT AUTHORED VERTICAL-SLICE EVIDENCE / EXTEND THROUGH CONTROLLED CONTENT MIGRATION.** It is not proof of final world scale.

### 5.2 `content/sample_scene.json`

Current content:
- 2 sample scenes.

Disposition:

**KEEP AS NON-CANON/DEVELOPMENT EXAMPLE** unless later superseded by a more explicit fixture. Do not promote it to world canon.

## 6. Android application/runtime inventory

### 6.1 Core runtime/application files

| File | Responsibility | Disposition |
| --- | --- | --- |
| `GameViewModel.kt` | application UI state/actions and travel transition state | **KEEP + REWORK/EXTEND** as projection contracts grow |
| `MainActivity.kt` | Android activity/bootstrap shell | **KEEP**, change only as final app architecture requires |
| `audio/NarrationController.kt` | narration/TTS application controller | **KEEP + EXTEND** |
| `boot/BootState.kt` | startup state model | **KEEP** |
| `engine/GameEngine.kt` | Kotlin player-safe engine interface and projected data models | **KEEP / HIGH-VALUE CONTRACT**, extend versionably |
| `engine/PythonGameEngine.kt` | Kotlin-to-Python engine bridge and projection mapper | **KEEP + EXTEND**, must stay aligned with Python bridge |
| `save/SaveRepository.kt` | Android-side save repository/slot access | **KEEP**, persistence semantics remain engine-owned |

Observed `GameEngine.kt` includes player-facing models for choices, resources, attributes, derived stats, skills, contributions/inspection, conditions, identity, inventory/equipment, visuals, quests, map nodes/edges/world map, and `GameSnapshot`.

### 6.2 Primary Compose surfaces

| File | Current responsibility | Disposition |
| --- | --- | --- |
| `ui/GameScreen.kt` | root shell and Story/Map/Inventory/Quest/Settings/More navigation/presentation | **REWORK PRESENTATION / KEEP AUTHORITY BOUNDARY** |
| `ui/CharacterSection.kt` | character/equipment presentation | **REWORK VISUALLY / KEEP EQUIPMENT STATE CONTRACT** |
| `ui/StatsSection.kt` | detailed stats/skills presentation | **KEEP SAFE DATA / EXTEND + REWORK VISUAL HIERARCHY** |
| `ui/StatusComponents.kt` | reusable Status UI components | **KEEP + EXTEND** against Status UX contract |
| `ui/SceneIllustration.kt` | scene visual composition surface | **KEEP/REWORK** according to final room composition contract |
| `ui/PixelComponents.kt` | reusable pixel-styled Compose components | **KEEP + REWORK selectively**, no gameplay authority |

### 6.3 Exact current pixel/UI catalog files

The following source files are present and remain under consumer/provenance audit:

- `PixelAssetCatalog.kt`
- `PixelCharacterStagingCatalog.kt`
- `PixelEnvironmentDecalCatalog.kt`
- `PixelEnvironmentModuleCatalog.kt`
- `PixelEnvironmentOverlayCatalog.kt`
- `PixelEnvironmentPreview.kt`
- `PixelEnvironmentPropCatalog.kt`
- `PixelEquipmentSlotCatalog.kt`
- `PixelItemQualityFrameCatalog.kt`
- `PixelMapArtCatalog.kt`
- `PixelMapMarkerCatalog.kt`
- `PixelMapTravelTransition.kt`
- `PixelRasterCatalog.kt`
- `PixelSceneCatalog.kt`
- `PixelSceneOverlayCatalog.kt`
- `PixelStoryActorCatalog.kt`
- `PixelTheme.kt`
- `PixelTraceFxCatalog.kt`
- `PixelTraceStrainCatalog.kt`
- `PixelUiChromeCatalog.kt`
- `PixelUiIconCatalog.kt`
- `PixelUiUtilityCatalog.kt`

Group disposition:

**KEEP CURRENT SEMANTIC BINDINGS + RECONCILE / REWORK PRESENTATION ASSET-BY-ASSET.**

Do not bulk-delete these catalogs. D-020/D-026/D-029 must establish consumers, survivor implementation, provenance, and replacement evidence first.

The current `PixelStoryActorCatalog` remains transitional; D-030's player-safe room projection is the documented replacement direction for scene/location actor inference.

## 7. Runtime raster inventory

Exactly 24 PNG files are present under `android/app/src/main/res/drawable-nodpi/`:

### Scene/environment rasters
- `pixel_district_archive_default_scene.png`
- `pixel_district_plaza_open_scene.png`
- `pixel_evac_stair_default_scene.png`
- `pixel_gate_twelve_sealed_scene.png`
- `pixel_platform_nine_blackout_scene.png`
- `pixel_relay_workbench_default_scene.png`
- `pixel_service_tunnel_default_scene.png`
- `pixel_trace_chamber_idle_scene.png`
- `pixel_workshop_row_default_scene.png`

### Player rasters
- `pixel_player_gameplay_front_base.png`
- `pixel_player_hair_tech_placeholder.png`

### Item/equipment rasters
- `pixel_item_courier_necktag_icon.png`
- `pixel_item_courier_necktag_paperdoll.png`
- `pixel_item_dead_relay_damaged.png`
- `pixel_item_dead_relay_icon.png`
- `pixel_item_dead_relay_opened.png`
- `pixel_item_dead_relay_signal_lost.png`
- `pixel_item_depot_jacket_icon.png`
- `pixel_item_depot_jacket_paperdoll.png`
- `pixel_item_maintenance_seal_icon.png`
- `pixel_item_signal_ring_icon.png`
- `pixel_item_signal_ring_paperdoll.png`
- `pixel_item_work_gloves_icon.png`
- `pixel_item_work_gloves_paperdoll.png`

Disposition:

- preserve all 24 as current-head evidence;
- production/canon status is **not inferred from file existence**;
- canonical stage belongs to D-029 provenance authority;
- generic/provisional player identity remains replacement-target art while the 32x48 rig/state contract is preserved unless explicitly migrated.

## 8. Test-source inventory

### 8.1 Python tests — 21 files

- `test_android_bridge.py`
- `test_android_stat_contributions.py`
- `test_cli.py`
- `test_content.py`
- `test_core.py`
- `test_equipment.py`
- `test_modifiers.py`
- `test_persistence.py`
- `test_pixel_raster_equivalence_tool.py`
- `test_powers.py`
- `test_progression.py`
- `test_quests.py`
- `test_save_resume_routes.py`
- `test_scene_projection.py`
- `test_simulation.py`
- `test_social.py`
- `test_stats.py`
- `test_status.py`
- `test_validation.py`
- `test_vertical_slice.py`
- `test_visuals.py`

### 8.2 Android JVM/unit tests — 27 files

- `TravelTransitionContractTest.kt`
- `BootStateTest.kt`
- `BridgeStatusMapperTest.kt`
- `PythonGameEngineContractTest.kt`
- `StatContributionMapperTest.kt`
- `SaveRepositoryTest.kt`
- `PixelAssetCatalogTest.kt`
- `PixelCharacterStagingCatalogTest.kt`
- `PixelEnvironmentDecalCatalogTest.kt`
- `PixelEnvironmentModuleCatalogTest.kt`
- `PixelEnvironmentOverlayCatalogTest.kt`
- `PixelEnvironmentPropCatalogTest.kt`
- `PixelEquipmentSlotCatalogTest.kt`
- `PixelItemQualityFrameCatalogTest.kt`
- `PixelMapArtCatalogTest.kt`
- `PixelMapMarkerCatalogTest.kt`
- `PixelMapTravelTransitionCatalogTest.kt`
- `PixelRasterCatalogTest.kt`
- `PixelSceneCatalogTest.kt`
- `PixelSceneOverlayCatalogTest.kt`
- `PixelStoryActorCatalogTest.kt`
- `PixelTraceFxCatalogTest.kt`
- `PixelTraceStrainCatalogTest.kt`
- `PixelUiChromeCatalogTest.kt`
- `PixelUiIconCatalogTest.kt`
- `PixelUiUtilityCatalogTest.kt`
- `StatusComponentsTest.kt`

### 8.3 Android instrumented tests — 3 files

- `ActivityBootSmokeTest.kt`
- `CharacterStatsSectionTest.kt`
- `GameScreenTest.kt`

Test disposition:

**KEEP + EXTEND.** Test-source presence does not mean current-head tests passed. Historical green runs remain evidence only for their exact implementation heads. Any runtime migration must rerun relevant Python, Android JVM, Compose/instrumented, and asset-equivalence checks.

## 9. Build and workflow surfaces

Current workflow files:

- `.github/workflows/android-apk-artifact.yml`
- `.github/workflows/android-pixel-client.yml`

Current Android configuration surfaces:

- `android/build.gradle.kts`
- `android/settings.gradle.kts`
- `android/gradle.properties`
- `android/app/build.gradle.kts`
- `android/app/src/main/AndroidManifest.xml`

Disposition:

**KEEP + VERIFY BEFORE RELEASE CHANGES.** Documentation-branch existence does not prove a workflow executed for the current HEAD.

## 10. Current-head disposition summary

| Area | Disposition |
| --- | --- |
| deterministic Python engine/state boundary | **KEEP + EXTEND** |
| save schema v1 | **KEEP / MIGRATION ONLY** |
| authored vertical slice | **KEEP EVIDENCE + EXTEND THROUGH CONTENT MIGRATION** |
| player-safe projection boundary | **KEEP / HIGH-RISK** |
| Android engine bridge | **KEEP + EXTEND** |
| Compose shell/screens | **REWORK PRESENTATION**, not wholesale discard |
| current pixel catalogs | **KEEP/RECONCILE**, replace only with consumer/provenance evidence |
| current 24 PNGs | **PRESERVE/CLASSIFY PER ASSET** |
| generic player visual | **REPLACE ART**, preserve rig/state contract unless migrated |
| Python/Android tests | **KEEP + EXTEND / RERUN ON CHANGES** |
| workflows/build config | **KEEP + VERIFY** |
| final tactical combat | **NEW TARGET SYSTEM** |
| final classes/ranks/professions | **NEW/EXTEND TARGET SYSTEM** |
| persistent adversary system | **NEW ORIGINAL SYSTEM** on social foundation |
| full world population | **NEW CONTENT**, standards already documented |

## 11. What this audit closes

This pass closes the **current-HEAD path inventory** portion of D-042 for:

- engine modules;
- application components;
- authored content;
- save fields/schema;
- current runtime rasters;
- test-source files;
- workflow/build surfaces.

It also attaches a disposition to each major responsibility without silently deleting or promoting anything.

## 12. What remains for D-006 / D-042

D-042 is not fully DONE yet because the following still require reconciliation:

1. exact field-to-composable/ViewModel/bridge consumer map — D-026/D-021;
2. per-catalog consumer map and temporary/hardcoded visual-state audit;
3. exact asset source-master/raster/runtime lineage completion — D-029;
4. cross-branch survivor/migration matrix — D-020;
5. remaining PR #33 Class-C unique requirement extraction — D-044;
6. deprecated/zero-consumer proof before any final REMOVE classification;
7. current-head execution of relevant tests/builds when implementation changes begin.

## 13. Verification boundary

No gameplay source, Android source, content, save schema, stable ID, raster, workflow, or test file was changed by this audit.

No tests/builds were executed.

All source facts above were read from the exact audited branch/HEAD. Runtime correctness remains governed by exact-head execution evidence, not this documentation pass.
