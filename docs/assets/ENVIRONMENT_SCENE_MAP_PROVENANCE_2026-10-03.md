# Environment, Scene, and Map Asset Provenance — 2026-10-03

Status: **ACTIVE / D-029 CHILD LEDGER / SOURCE-GROUNDED PARTIAL**  
Repository: `jbob-coder/Text-rpg-game`  
Inspected implementation baseline: `docs/master-game-development-program@58a61eb202bbb9443e01f8689e18e8ef0e99d3c7`  
Runtime/content delta from prior D-029 baseline `2ad50d7aff6f153b90036f8e0f61043242a09765`: **none**; intervening changes are documentation/evidence only.  
Parent: [Asset Family Provenance Index](ASSET_FAMILY_PROVENANCE_INDEX_2026-10-03.md)

## 1. Scope

This ledger covers the current environment and navigation-facing visual families:

- nine named-location scene masters;
- nine current named-location PNG rasters;
- environment modules;
- infrastructure atlas;
- environment props;
- environment decals;
- environment overlays;
- scene/state overlays;
- Gate Twelve district map art;
- map markers;
- map travel transition;
- divergent Service Tunnel / Quiet Stair refinement branches;
- environment/map reuse and migration risk.

Gameplay/world authority remains outside these presentation assets. Art never grants route legality, discovery, actor presence, quest state, or hidden state.

## 2. Current scene chain and raster precedence

Verified source files:

- `PixelSceneCatalog.kt` — blob `b6126ddcab09d1005baa0352299ec57b301bf3d2`;
- `PixelRasterCatalog.kt` — blob `6bfc11c88df1d2edb473ed8b3cd3293e7f2822d8`;
- `SceneIllustration.kt` — blob `619c9cf5f6610f9ab9e118b8cab3ab3a875031f4`.

`SceneIllustration` computes the source-native scene layout from `PixelSceneCatalog.scene(locationId)`, then:

1. resolves `sceneRaster = rememberPixelRaster(PixelRasterCatalog.scene(locationId))`;
2. draws the PNG if `sceneRaster != null`;
3. otherwise draws the Kotlin `PixelSprite`.

Therefore current named scenes are dual-form assets:

`Kotlin source-native scene/fallback + preferred PNG runtime raster`

A source-only refinement can be hidden by an older raster.

## 3. Named-location scene family

### 3.1 Stable scene IDs

Current `PixelSceneCatalog` defines:

- `PLATFORM_NINE_BLACKOUT_SCENE`
- `RELAY_WORKBENCH_DEFAULT_SCENE`
- `GATE_TWELVE_SEALED_SCENE`
- `SERVICE_TUNNEL_DEFAULT_SCENE`
- `EVAC_STAIR_DEFAULT_SCENE`
- `TRACE_CHAMBER_IDLE_SCENE`
- `DISTRICT_PLAZA_OPEN_SCENE`
- `DISTRICT_ARCHIVE_DEFAULT_SCENE`
- `WORKSHOP_ROW_DEFAULT_SCENE`

The current production grid is 128x64 for these scene masters.

### 3.2 Branch provenance

Historical broad scene/code root:

PR #7 `feature/pixel-asset-wave-a@a3970de6597c77939afccb5f30d6040bdf3d608d`.

Inherited PNG raster delivery:

PR #19 `feature/png-pixel-art-runtime-a@c11133122d47009abc71e8c6e91c08aedbe91ae2`.

At PR #19:

- `PixelSceneCatalog.kt` blob already equals the current inspected `b6126ddc...`;
- `PixelRasterCatalog.kt` blob already equals current `6bfc11c8...`.

### 3.3 Current raster exports

| Location | Runtime raster | Git blob |
| --- | --- | --- |
| PLATFORM_NINE | `pixel_platform_nine_blackout_scene.png` | `591fa56cd17bdf5576774815ed330b3f40af4ccc` |
| RELAY_WORKBENCH | `pixel_relay_workbench_default_scene.png` | `96612e083a9db37a4588049dd2c3a3f2aad304b4` |
| GATE_TWELVE | `pixel_gate_twelve_sealed_scene.png` | `2c2b1838060c66cc794e945fe56bece691cacea6` |
| SERVICE_TUNNEL | `pixel_service_tunnel_default_scene.png` | `aa6e31fa37e3ebcadef84de9ccd47d93b6d065b1` |
| EVAC_STAIR | `pixel_evac_stair_default_scene.png` | `75a985e7cdee6e669b936c3d0a2d2e769939f394` |
| TRACE_CHAMBER | `pixel_trace_chamber_idle_scene.png` | `43f9919fef3e0ae0ad27c4e09e008064068a93ff` |
| DISTRICT_PLAZA | `pixel_district_plaza_open_scene.png` | `215ce07dbf78a15b5d7036c81ca02f3dd0e7ca79` |
| DISTRICT_ARCHIVE | `pixel_district_archive_default_scene.png` | `f511c36c84690c76f39cbf9928b608cc00461d52` |
| WORKSHOP_ROW | `pixel_workshop_row_default_scene.png` | `49a1e0789fcb83d84e872de04c521eb4dee5e1db` |

Per-raster SHA-256/dimensions are authoritative in `docs/evidence/raster_bindings_2026-10-02.json`.

### 3.4 Stage

Current baseline:

`RASTER_PRESENT + CODE_PRESENT + INTEGRATED`

Not established:

- final visual approval;
- exact original authoring-source lineage for every PNG;
- source/raster pixel equivalence;
- canon approval.

### 3.5 QA

- `PixelSceneCatalogTest.kt` blob `b41c0754e1499d4d679b0577ba38b5e34886d775`;
- `PixelRasterCatalogTest.kt` blob `e4f9f4c1b8bd00169ae74a70173fae9503703738`.

Tests cover native grid/current-location mapping and raster delivery/fallback contract.

Historical PR #19 workflow run 36823014708 succeeded. No fresh runtime test is claimed for this documentation slice.

## 4. Environment module / infrastructure atlas family

### 4.1 IDs

Current `PixelEnvironmentModuleCatalog.kt` contains at least:

- `DEPOT_FACADE_EXTERIOR`
- `MAINTENANCE_CORRIDOR_CONNECTOR`
- `MUNICIPAL_ARCHIVE_EXTERIOR`
- `MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS`

The catalog also exposes exact arrival-preview mappings for current locations.

### 4.2 Exact source lineage

Current program-branch source:

- file blob: `440b7d41141d70700d6eba7c84303cbf109c10f2`.

Relevant branch snapshots:

- PR #8 `feature/pixel-asset-wave-l-environment-modules@54a40bb5ad0aeafb428d128be7c1465f3d1a759b`
  - module file blob: `d4cf93e1faa91e535a17aba4bf448e6555bce6b7`
  - relation: divergent historical/candidate source.
- PR #16 `feature/pixel-assets-runtime-expansion@ddbb5f4250e26b99765999d0a8e81f59cb1ea26c`
  - module blob: `3827c2fcaaa720af4cf81aea61e8f2af4691452e`.
- PR #26 `feature/service-tunnel-arrival-pixel-art@2f7f77d7925e94558d219d4ab2340fbb32476717`
  - module blob: `440b7d41141d70700d6eba7c84303cbf109c10f2`.
- current program branch:
  - same blob as PR #26.

Conclusion:

The active program-branch environment-module source is the inherited PR #26 revision, not the older divergent PR #8 file.

### 4.3 Runtime consumers

- `PixelEnvironmentPreview.kt` — blob `c82ecd09a4f84297764dc504bd17c25b3535625e`;
- `GameScreen.kt` — current map/application presentation also references `PixelEnvironmentModuleCatalog`.

No PNG raster export is currently required for this code-master family.

### 4.4 QA/stage

`PixelEnvironmentModuleCatalogTest.kt` blob `1e93c31702846b41ebcf63ae68e3f76a25f4996c` verifies:

- 128x64 scene modules;
- four reusable 32x32 infrastructure tiles;
- explicit location-bound arrival previews.

Current stage must be split by asset rather than assigned to the family as a whole:

| Asset | Current stage | Current consumer evidence |
| --- | --- | --- |
| `DEPOT_FACADE_EXTERIOR` | `SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED` | exact `DISTRICT_PLAZA` Map arrival preview |
| `MAINTENANCE_CORRIDOR_CONNECTOR` | `SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED` | exact `SERVICE_TUNNEL` Map arrival preview |
| `MUNICIPAL_ARCHIVE_EXTERIOR` | `SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED` | exact `DISTRICT_ARCHIVE` Map arrival preview |
| `MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS` | `SOURCE_MASTER_PRESENT + CODE_PRESENT + DEFERRED_INTEGRATION` | no main-UI runtime consumer found |

The older `RUNTIME_EXPANSION_ASSET_WAVE_2026-09-30.json` record is historical evidence for its own snapshot: it still marks `MAINTENANCE_CORRIDOR_CONNECTOR` deferred. Current source is newer and now binds that module through `arrivalPreview("SERVICE_TUNNEL")`. Historical manifest state must not override current runtime inspection.

Exact PR #8 reconciliation:

- PR #8 catalog blob: `d4cf93e1faa91e535a17aba4bf448e6555bce6b7`;
- current catalog blob: `440b7d41141d70700d6eba7c84303cbf109c10f2`;
- a line-level comparison found the four module/atlas visual definitions preserved without PR #8-only geometry loss;
- the current catalog adds only the later player-safe `arrivalPreview(locationId)` mapping block for `DISTRICT_PLAZA`, `DISTRICT_ARCHIVE`, and `SERVICE_TUNNEL`;
- `RUNTIME_EXPANSION_ASSET_WAVE_2026-09-30.json` records all four assets as sourced from `B001-WAVE-L-ENVIRONMENT-MODULES`; its Maintenance Corridor status is now historical because current source later added the exact `SERVICE_TUNNEL` arrival-preview binding. The atlas remains deferred.

Decision:

PR #8 remains historical branch/provenance evidence, but its four visual source definitions do **not** require separate migration into the current program ancestry because those definitions are already preserved in the current catalog. The branch itself still must not be blindly merged.

Remaining:

- legitimate composition/runtime consumer decision for `MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS`;
- final material/palette approval;
- raster export only if the runtime strategy later requires it;
- separate PR #28 detail-candidate reconciliation against the selected Service Tunnel composition.

## 5. Environment prop family

Source:

`PixelEnvironmentPropCatalog.kt` — blob `9340f3d7663e9d5b99a81b7a2542f02432f3a2c8`.

Current asset IDs include:

- `PROP_ARCHIVE_SHELF`
- `PROP_ARCHIVE_TERMINAL`
- `PROP_WORKSHOP_BENCH`
- `PROP_DISTRICT_NOTICE_BOARD`
- `PROP_DEPOT_DOOR`
- `PROP_RELAY_WORKBENCH`
- `PROP_GATE_TWELVE_DOOR`
- `PROP_TUNNEL_PIPE_SET`
- `PROP_TUNNEL_CABLE_SET`
- `PROP_TRACE_CHAMBER_APPARATUS`

Current master form: procedural Kotlin.

Runtime consumer: `SceneIllustration.kt` calls `PixelEnvironmentPropCatalog.placements(locationId, sceneId)`.

QA:

`PixelEnvironmentPropCatalogTest.kt` blob `df9d54f1289bd41946fcf623ed4b33f047925391` verifies documented native canvases/palette keys and placement use of player-facing IDs.

Historical root: PR #7.

Stage:

`SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED`

Reuse rule:

Props may move only when scale, perspective, anchor, lighting, semantic role, and occlusion order remain compatible. Use `GLOBAL_ASSET_REUSE_OCCLUSION_MATRIX.md`.

## 6. Environment decal family

Source:

`PixelEnvironmentDecalCatalog.kt` — blob `7c3b35a571b519820c357efc411cf4a6617eeee2`.

IDs:

- `EVACUATION_SIGNAGE_SET`
- `DISTRICT_AMBIENT_DECAL_SET`

Master form: procedural Kotlin.

Consumer: `SceneIllustration.kt`.

QA:

`PixelEnvironmentDecalCatalogTest.kt` blob `7eb484d8f8c730236ee91f3c8dc6f71364585dc9`.

Stage:

`SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED`

Migration risk:

Do not bake stateful information or normal UI text into ambient decals. In-world signage remains distinct from UI text.

## 7. Environment overlay family

Source:

`PixelEnvironmentOverlayCatalog.kt` — blob `58c2d3d6a2bb7752eae8115bba317c5e2df946f3`.

IDs:

- `EMERGENCY_LIGHT_OVERLAY`
- `BLACKOUT_SHADOW_OVERLAY`

These are reusable 128x64 transparent environmental layers.

QA:

`PixelEnvironmentOverlayCatalogTest.kt` blob `fe2c22c3d76cb5ceca9985b5d8ad5c9475afcb01`.

Stage:

`SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED`

Rule:

State overlays remain separate from base scene art so the same environment can render multiple player-safe states.

## 8. Scene/state overlay family

Source:

`PixelSceneOverlayCatalog.kt` — blob `3f27dde95dcc0d338b8064de8f4701d0e72f4560`.

Current IDs:

- `GATE_TWELVE_ECHO_ACTIVE_SCENE`
- `SERVICE_TUNNEL_AFTERSHOCK_SCENE`
- `TRACE_CHAMBER_TRAINING_SCENE`
- `DISTRICT_PLAZA_BLACKOUT_SCENE`
- `RELAY_WORKBENCH_RELAY_OPEN_SCENE`

Consumer:

`SceneIllustration.kt`.

The catalog uses player-facing scene IDs and projected relay visual state. It is presentation logic, not hidden-state authority.

QA:

`PixelSceneOverlayCatalogTest.kt` blob `e81027cb6e3e5b6f7f1de383899188adc3c71613` verifies exact transparent grid and explicit scene/state mappings.

Stage:

`SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED`

## 9. Gate Twelve district map-art family

Source:

`PixelMapArtCatalog.kt` — blob `04a958bf3a6809977145aa088791d207d819449e`.

Primary ID:

- `MAP_GATE_TWELVE_DISTRICT_BASE`

Current form:

- procedural Kotlin;
- 256x144 native map presentation master;
- integer-pixel viewport mapping;
- world/node state remains external to artwork.

Branch provenance:

PR #21 `feature/pixel-map-art-pass@59a1930961ae5fc961acab5624dcbfcc2f7e66cb`.

Current consumer:

`MapSection` in `GameScreen.kt`.

QA:

`PixelMapArtCatalogTest.kt` blob `d3d1c3d9ef67ace9e10e98a8c5a6d0b29e1795d9` verifies native grid, viewport, projection behavior and no unrelated-art borrowing.

Stage:

`SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED`

Migration risk:

Map art must not own node discovery, reachability, current location, travel legality, or world hierarchy. Preserve the authored map as presentation beneath projected state overlays.

## 10. Map marker family

Source:

`PixelMapMarkerCatalog.kt` — blob `d6266f05407c4f51433beb9245b38b238b0dd2d0`.

IDs:

- `MAP_PLAYER_MARKER`
- `MAP_NODE_DISCOVERED`
- `MAP_NODE_CURRENT`
- `MAP_NODE_REACHABLE`
- `MAP_NODE_UNAVAILABLE`

Master form: procedural 16x16 Kotlin sprites.

Consumer: `MapSection` in `GameScreen.kt`.

QA:

`PixelMapMarkerCatalogTest.kt` blob `4167d3995e58580d7fbee83c223ea58621bdfa92` verifies native marker grid and that state overlay mapping uses only projected current/reachable flags.

Historical root: PR #7.

Stage:

`SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED`

## 11. Map travel transition family

Source:

`PixelMapTravelTransition.kt` — blob `3f364a0e7e937e09f45f02f28ee9e78c46d0186e`.

Base ID:

- `UI_MAP_TRAVEL_TRANSITION`

Frame IDs are derived as:

`UI_MAP_TRAVEL_TRANSITION_FRAME_1` through the generated frame sequence.

Current form:

- eight procedural 128x64 frames;
- Compose travel-transition overlay.

QA:

`PixelMapTravelTransitionCatalogTest.kt` blob `c4eaf73f4857db1057ee07bd1f4e3c31993c3322` verifies exact eight-frame dimensions and palette mapping.

Historical root: PR #7.

Stage:

`SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED`

Migration rule:

Travel animation never authorizes travel. It may only visualize an already-authorized transition.

## 12. Divergent static scene candidates

### 12.1 Service Tunnel — PR #27

Branch/head:

`feature/service-tunnel-scene-art-pass@d19e6edba4dec5345f1365bb358084b9b77eb7d9`

Verified branch evidence:

- source scene blob changes to `b9124a02cac75abd6c84aaa93c090fdd0b846f9f`;
- Service Tunnel PNG changes to blob `50543eb0316c98ffd2a93c0976849af985ccdf74`;
- raster binding catalog remains unchanged;
- historical workflow run 36950023830 succeeded.

Stage:

`CANDIDATE_SURVIVOR / NOT INTEGRATED`

### 12.2 Service Tunnel atlas detail — PR #28

Branch/head:

`feature/service-tunnel-atlas-detail@b5cb510408331446ec3fdfbc6ec188b8a5516c15`

Base:

`feature/service-tunnel-arrival-pixel-art@2f7f77d7925e94558d219d4ab2340fbb32476717`

Exact changed files:

- `PixelEnvironmentModuleCatalog.kt`;
- `PixelEnvironmentPreview.kt`;
- `PixelEnvironmentModuleCatalogTest.kt`.

Exact provenance conclusion:

- PR #28 adds **no new module/tile pixel geometry**;
- it adds `arrivalDetailTiles(locationId)`;
- only `SERVICE_TUNNEL` maps to detail tiles;
- the returned detail set is exactly the already-existing `infrastructureTileAtlas.tiles`;
- the preview renderer then lays those existing tiles as a centered decorative strip beneath the existing Service Tunnel arrival preview;
- tests assert that Service Tunnel uses the entire existing atlas and unknown locations receive no detail tiles.

Therefore PR #28 is **not a competing source-master branch for the infrastructure atlas**. The asset source remains the preserved Wave-L/current `MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS`.

Stage:

`CANDIDATE_COMPOSITION_BEHAVIOR / NOT INTEGRATED`

Decision:

Preserve PR #28 as optional composition logic. If adopted later, selectively reimplement the arrival-detail behavior against the current catalog rather than merging the branch to obtain asset geometry. Final use still depends on the Service Tunnel visual/material packet and mobile preview QA.

### 12.3 Quiet Stair — PR #30

Branch/head:

`feature/quiet-stair-scene-art-pass@7adacd474ae22908bba2fc72247f500312ea7483`

Base:

`feature/service-tunnel-scene-art-pass@d19e6edba4dec5345f1365bb358084b9b77eb7d9`

Verified branch evidence:

- scene source blob `ade70ece1394b89b35bc67e9af8813107cdcffdb`;
- `pixel_evac_stair_default_scene.png` blob `c4759aeb1a917cb31ccb1465c4f1b26d9f1de220`;
- branch also carries the PR #27 refined Service Tunnel raster;
- workflow run 36950951038 succeeded.

Stage:

`CANDIDATE_SURVIVOR / NOT INTEGRATED`

Do not merge the branch wholesale merely to obtain Quiet Stair art.



## 13. Static survivor decision boundary

The exact PR topology and changed-file sets reduce the earlier survivor ambiguity.

### Service Tunnel

Current inherited baseline:

- source/raster lineage remains the PR #19/current program version.

Refined candidate:

- PR #27 `feature/service-tunnel-scene-art-pass@d19e6edba4dec5345f1365bb358084b9b77eb7d9`;
- changes exactly the Service Tunnel scene source, Service Tunnel PNG, related scene test, Story screenshot test/workflow evidence;
- PR description states the PNG was refreshed from the same 128x64 source-native design;
- exact-head run `36950023830` succeeded;
- physical Galaxy A03 approval remains separate.

PR #30 is stacked on PR #27 and changes only Quiet Stair-specific files plus shared scene/test files for that additional stair revision. It does **not** provide a second Service Tunnel PNG revision.

Therefore the Service Tunnel static choice is:

`CURRENT INHERITED BASELINE`
vs
`PR #27 REFINED CANDIDATE`

not PR #27 vs PR #28 vs PR #30.

### Quiet Stair / EVAC_STAIR

Current inherited baseline:

- current program-branch source/raster.

Refined candidate:

- PR #30 `feature/quiet-stair-scene-art-pass@7adacd474ae22908bba2fc72247f500312ea7483`;
- stacked on PR #27;
- changes the Quiet Stair scene source and preferred PNG plus its tests/evidence;
- PR description states the PNG was refreshed from the same deterministic source-native 128x64 design;
- historical workflow run `36950951038` succeeded;
- physical Galaxy A03 approval remains separate.

Therefore the Quiet Stair static choice is:

`CURRENT INHERITED BASELINE`
vs
`PR #30 REFINED CANDIDATE`.

### PR #28 relationship

PR #28 does not participate as a static-scene survivor. It adds optional Service Tunnel arrival-preview composition using the already-existing infrastructure atlas and does not change the named Service Tunnel PNG.

### Decision status

Technical branch/survivor lineage: **RESOLVED**.

Artistic promotion:

- Service Tunnel PR #27: `OWNER DECISION REQUIRED / VISUAL PROMOTION PENDING`;
- Quiet Stair PR #30: `OWNER DECISION REQUIRED / VISUAL PROMOTION PENDING`.

No documentation agent should silently choose the refined candidate merely because its CI passed. CI verifies implementation integrity, not canon/art approval.

If a refined candidate is approved, integrate it by file-level migration onto the selected implementation parent and re-run destination-head tests/screenshots rather than merging the divergent branch wholesale.

## 14. Reconstruction sequence

If these visual systems were lost:

1. recreate `PixelSceneCatalog` IDs and 128x64 source-native masters;
2. restore all nine raster files and `PixelRasterCatalog.scene` bindings;
3. restore the PNG-first fallback behavior;
4. restore module/atlas code and arrival-preview mappings;
5. restore props, decals, environmental overlays, then state overlays in layer order;
6. restore map base art independently from map state;
7. restore map markers and travel transition;
8. restore player-safe state inputs;
9. do not adopt PR #27/#28/#30 until file-level survivor selection is recorded;
10. run unit tests, native-scale render comparison, emulator screenshots and required device QA.

## 15. Remaining gaps

- current 24-PNG commit-level export/refresh lineage is documented, but the deterministic exporter/tool invocation is not persisted/found;
- fresh pixel-for-pixel source/raster equivalence has not been reproduced;
- `MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS` still lacks a legitimate runtime/composition consumer;
- Service Tunnel static survivor;
- Quiet Stair static survivor;
- per-area asset packets for later Gate Twelve rooms;
- final material/lighting/palette approval;
- canon approval;
- physical-device visual QA.
