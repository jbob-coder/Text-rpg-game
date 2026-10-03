# Raster Export and Source Correspondence — 2026-10-03

Status: **ACTIVE / D-029 EXACT LINEAGE EVIDENCE / CURRENT 24-PNG BASELINE**  
Repository: `jbob-coder/Text-rpg-game`  
Audit start HEAD: `docs/master-game-development-program@2161ed51a06462353b4621ac67bb4e2f5bb62f23`

Parent authorities:

- [Asset provenance registry](ASSET_PROVENANCE_REGISTRY.md)
- [Asset family provenance index](ASSET_FAMILY_PROVENANCE_INDEX_2026-10-03.md)
- [Raster delivery evidence](RASTER_DELIVERY_EVIDENCE_2026-10-02.md)
- [Source/raster branch reconciliation](SOURCE_RASTER_RECONCILIATION_2026-10-02.md)

Machine-readable evidence:

- `docs/evidence/raster_export_lineage_2026-10-03.json`

## 1. Purpose

D-029 previously knew:

- which 24 PNGs exist;
- their dimensions;
- SHA-256 values;
- Git blobs;
- runtime bindings;
- that PNG delivery wins over Kotlin fallback when a raster is bound.

This record adds the missing historical source-to-raster chain.

For each current PNG, the machine-readable evidence now records:

`source file -> source revision -> initial export commit -> later refresh/refinement commit when any -> current raster blob -> runtime binding`

The remaining limitation is the actual exporter implementation/tool invocation. That tooling is not presently reconstructable from repository evidence.

## 2. Confirmed source authority

Commit `9390a0456618a5835a3a6339e9c9e4c459080e39` created `PixelAssetCatalog.kt` with an explicit source comment:

- text-based native-pixel definitions are the production source of truth;
- every pixel change should remain reviewable in Git;
- they are intended to be exportable to PNG later.

PR #19 then states that it:

- exported real PNG pixel art;
- kept the original `PixelSprite` definitions as exact fallback and reviewable source;
- made runtime prefer the exported PNGs;
- did not invent new canonical geometry or art direction.

Therefore, for the current 24-PNG lineage, the repository-supported production relationship is:

`Kotlin PixelSprite source master -> exported PNG delivery -> PixelRasterCatalog binding -> runtime raster preference`

This does **not** mean every current visual family in the project must use PNG. Other D-029 ledgers identify many procedural Kotlin families whose active production form remains code-native.

## 3. Initial PR #19 export sequence

PR #19: **Use real PNG pixel art for opening scene and player**

Base parent:

`feature/story-scene-first-pixel-art@5a8151a56265e0b0b4a39fcb6f62aa1c4d8e4102`

At that parent, the source blobs were:

- `PixelAssetCatalog.kt`: `61b435ae1407c3cd0ebb156b3f7307b2cf05e540`
- `PixelSceneCatalog.kt`: `529231483cf1147cbb276fb45c9bbd9925b11efb`

Those source blobs remained unchanged through the initial PNG export commits.

### PR #19 commit order

| Commit | Purpose | Provenance significance |
| --- | --- | --- |
| `9b2e2108` | Add raster pixel art for opening scene and player loadout | first PNG delivery for player/base hair, current loadout slice and Platform Nine |
| `b1954ceb` | Add raster-backed pixel asset delivery layer | introduces raster-delivery infrastructure |
| `49abe616` | Render exported player pixel PNGs at runtime | establishes player raster consumption |
| `cbcf05eb` | Prefer raster pixel art for exported scenes | establishes scene PNG preference |
| `8683bc01` | Test raster pixel art coverage and fallback | locks coverage/fallback contract |
| `d2f529c4` | Export remaining loadout relay and early scene PNGs | exports courier/relay/maintenance plus Gate Twelve and Relay Workbench |
| `c7f03fad` | Export remaining named scene PNGs | completes raster delivery for the other named scenes |
| `51eb33fe` | Map all exported pixel PNGs into runtime | completes runtime mapping |
| `86960345` | Cover complete raster asset mapping | verifies the 24-raster mapping set |
| `f283b659` | Refine Platform Nine pixel scene fidelity | changes Platform Nine source and PNG together |
| `dea77b1c` | Refine Relay Workbench pixel scene fidelity | changes Relay Workbench source and PNG together |
| `c1113312` | Include Relay Workbench in UI QA evidence set | final PR #19 head |

The exact list is preserved in GitHub PR commit history and the machine-readable D-029 evidence file.

## 4. Current 24-PNG correspondence result

The current branch contains 24 PNG runtime assets.

The exact lineage audit classifies them as:

- **17 — INITIAL_EXPORT_REMAINS_CURRENT**
- **7 — SOURCE_REVISED_THEN_RASTER_REFRESHED**

This classification means repository commit/PR evidence supports the source→raster lineage. It does **not** claim this documentation pass independently reproduced each PNG and performed a pixel-for-pixel binary comparison.

### 4.1 Seventeen initial-export rasters still current

These assets have no later raster revision in the current program ancestry after their PR #19 export:

- District Archive scene;
- District Plaza scene;
- Quiet/Evac Stair current baseline scene;
- Gate Twelve scene;
- Courier Neck Tag icon;
- Dead Relay base/opened/damaged/signal-lost assets;
- Depot Jacket icon;
- Maintenance Seal icon;
- Signal Ring icon;
- Signal Ring paper-doll;
- Work Gloves icon;
- Service Tunnel current inherited baseline scene;
- Trace Chamber scene;
- Workshop Row scene.

For these records:

- the source definitions existed before export;
- the export commits added PNGs without changing the relevant source catalogs;
- no later current-ancestry visual revision of those specific asset definitions was found;
- their initial exported PNG blob remains the current program-branch PNG blob.

Exact per-file commit/blob/hash rows are in `raster_export_lineage_2026-10-03.json`.

## 5. Player/loadout refinement and raster refresh

A potentially dangerous source/raster drift existed briefly in PR #22's commit sequence, but the branch repaired it before its verified head.

PR #22 sequence:

1. `d3367eb1` — **art: refine player silhouette and current loadout**
2. `a3f8aa7f` — **fix: keep player art catalog source valid**
3. `f8b681c2` — **art: refresh player raster delivery**
4. `c54c5a90` — test refined player art rig
5. `1e70d071` — align manifest with current rasters
6. `2a1c7f59` — record current loadout raster delivery

PR #22 explicitly states that it:

- refines the neutral player base;
- refines the temporary hair layer;
- reworks the Depot Jacket layer;
- refines glove and Courier Neck Tag paper-doll layers;
- refreshes **all five runtime-preferred PNG rasters**;
- retains exact source-native Kotlin fallbacks.

The five refreshed current PNGs are:

- `pixel_player_gameplay_front_base.png`
- `pixel_player_hair_tech_placeholder.png`
- `pixel_item_depot_jacket_paperdoll.png`
- `pixel_item_work_gloves_paperdoll.png`
- `pixel_item_courier_necktag_paperdoll.png`

At refresh commit `f8b681c239b48ccd4e28be2ec9f5f0520c66f6ee`, the source catalog blob is:

`dc6f1d553dbb8abbccecef728ee67bbf54bad3c2`

That is also the current program-branch `PixelAssetCatalog.kt` blob at this audit.

Current file history shows no later PNG revisions for those five assets.

### Consequence

The current branch is **not** in the specific broken state where PR #22's newer Kotlin player art is hidden by PR #19's old player/loadout PNGs.

The raster refresh exists and is part of the inherited current ancestry.

However, the general failure mode remains real and must stay documented because the runtime still prefers PNG over source fallback.

## 6. Scene refinements and synchronized export

### Platform Nine

Current visual source revision:

`f283b6592ed2342576e2461efa6fc01637bdb965`

That commit changes both:

- `PixelSceneCatalog.kt`
- `pixel_platform_nine_blackout_scene.png`

PR #19's exact-head comment records preservation of:

- the 128x64 source canvas;
- raster-preferred runtime;
- source-native fallback;
- existing overlay placements.

### Relay Workbench

Current visual source revision:

`dea77b1c72686e72f448367784493b2882e5c14e`

That commit changes both:

- `PixelSceneCatalog.kt`
- `pixel_relay_workbench_default_scene.png`

After this commit, `PixelSceneCatalog.kt` is blob:

`b6126ddcab09d1005baa0352299ec57b301bf3d2`

That remains the current program-branch scene-catalog blob at this audit.

### Other current scenes

The scene-catalog path history shows:

- `e711fa26` — adds Platform Nine and Relay Workbench masters;
- `500db3cb` — adds Gate Twelve and Service Tunnel masters;
- `a7fe6d26` — adds the remaining current location masters;
- `f283b659` — later Platform Nine refinement;
- `dea77b1c` — later Relay Workbench refinement.

No later current-ancestry `PixelSceneCatalog.kt` commit exists after the Relay Workbench refinement.

Therefore the seven non-refined current baseline scene rasters retain their original export lineage, while Platform Nine and Relay Workbench retain synchronized later source+raster refinement lineage.

This says nothing about divergent PR #27/#30 candidates; those remain separate survivor work under `SOURCE_RASTER_RECONCILIATION_2026-10-02.md`.

## 7. Export tooling status

### VERIFIED

The current recursive repository tree contains:

- `PixelRasterCatalog.kt`;
- the 24 PNG files;
- raster tests;
- raster evidence documents.

PR #19's PNG-export commits add the exported PNGs, but no dedicated exporter/generator script is part of those export commits.

A current-tree path search for export/raster/pixel tooling found no separate persisted source-to-PNG exporter utility.

### UNKNOWN / NOT PERSISTED

Repository evidence does not currently establish:

- the exact command used to generate the PNGs;
- the implementation language/tool used for export;
- whether the exporter was ephemeral/local;
- whether all exports used one identical tool version.

Therefore:

`Kotlin source -> PNG` lineage is source-controlled and commit-supported, but the **transformation tooling is not reconstructable yet**.

This is a D-029 gap, not a reason to invent an exporter history.

## 8. Pixel-equality limitation

This audit did not independently:

- execute a historical exporter;
- decode each PNG and compare it against a freshly rendered Kotlin `PixelSprite`;
- prove per-pixel equality through a reproducible current tool.

Accordingly, the evidence file uses correspondence language rather than claiming fresh pixel-equality verification.

To upgrade this to independently reproducible equality, create a repository-owned deterministic exporter/checker that:

1. consumes the same `PixelSprite` palette/rows;
2. emits deterministic RGBA PNG bytes or a canonical decoded pixel matrix;
3. compares decoded PNG pixels to source rows;
4. reports dimensions, alpha and palette mismatches;
5. can run against all raster-bound assets;
6. is covered by tests and CI;
7. does not change runtime art merely to make hashes match.

That would convert lineage evidence into reproducible transformation evidence.

## 9. Runtime migration hazard

Current runtime behavior still means:

`bound raster exists -> raster draws`

`no raster -> Kotlin source-native fallback draws`

Therefore any future change to a raster-bound source master must do one of three things:

1. regenerate/update the matching preferred PNG;
2. deliberately remove/change the raster binding with documented migration intent;
3. explicitly retain the older raster as a separate approved visual revision.

What is forbidden:

- edit only the Kotlin source;
- leave an older PNG bound;
- assume the visible game now contains the source edit.

## 10. Reconstruction procedure

If the raster delivery layer were lost:

1. restore stable source-native Kotlin masters first;
2. restore the 24 raster records from `raster_bindings_2026-10-02.json`;
3. use `raster_export_lineage_2026-10-03.json` to identify the relevant source and export revision;
4. preserve PR #22's five-asset refined source/raster relationship;
5. preserve Platform Nine and Relay Workbench's paired refinement relationship;
6. restore `PixelRasterCatalog` mappings;
7. preserve nearest-neighbor rendering and fallback semantics;
8. compare decoded raster pixels to source before declaring a regenerated raster equivalent;
9. run unit/instrumentation/render QA;
10. keep physical-device approval separate.

Do not regenerate from screenshots, concept art, or memory when reviewable source-native pixel maps exist.

## 11. D-029 impact

This closes a major part of the earlier “exact authoring-source lineage for exported rasters” gap:

### Now established

- production source class for the current raster lineage;
- initial export source blobs;
- exact export commits;
- exact later source revisions;
- exact later raster refresh/refinement commits;
- current raster blobs/hashes;
- current source blobs;
- runtime binding relationship.

### Still incomplete

- persisted/reproducible exporter implementation;
- fresh pixel-for-pixel source/raster equivalence execution;
- divergent Service Tunnel/Quiet Stair survivor selection;
- final Jack production art/portrait lineage;
- owner/canon approval;
- final destination-head/device visual QA.

D-029 therefore remains **IN_PROGRESS**.
