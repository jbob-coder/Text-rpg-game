# Asset Family Provenance Index — 2026-10-03

Status: **ACTIVE / D-029 FAMILY-LEVEL INDEX / PARTIAL SLICE**  
Repository: `jbob-coder/Text-rpg-game`  
Inspected implementation baseline: `docs/master-game-development-program@58a61eb202bbb9443e01f8689e18e8ef0e99d3c7`  
Runtime/content delta from prior D-029 baseline `2ad50d7aff6f153b90036f8e0f61043242a09765`: **none**; intervening changes are documentation/evidence only.  
Task: **D-029 — Exactize asset provenance and production stage**

Parent authorities:

- [Asset provenance registry](ASSET_PROVENANCE_REGISTRY.md)
- [Pixel-art runtime composition standard](PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md)
- [Pixel-art production and reuse ledger](PIXEL_ART_PRODUCTION_AND_REUSE_LEDGER.md)
- [Global asset reuse/occlusion matrix](GLOBAL_ASSET_REUSE_OCCLUSION_MATRIX.md)
- [Source/raster branch reconciliation](SOURCE_RASTER_RECONCILIATION_2026-10-02.md)
- [Raster delivery evidence](RASTER_DELIVERY_EVIDENCE_2026-10-02.md)

## 1. Purpose

This index turns D-029 from a single raster list into a family-level provenance system.

It records the evidence chain required for reconstruction:

`asset family -> IDs -> source/code master -> raster/export when present -> branch/head -> runtime consumer -> precedence/override -> QA evidence -> production stage -> missing work -> migration risk`

This document is an index. Detailed family records are intentionally split into child ledgers so the provenance registry does not become an unreadable monolith.

## 2. Evidence classification

Every statement in the child ledgers uses one of these meanings:

- **VERIFIED CURRENT IMPLEMENTATION** — inspected directly on the program branch at the baseline above.
- **VERIFIED BRANCH EVIDENCE** — inspected on an exact open-PR head, but not necessarily integrated into the program branch.
- **ESTABLISHED DESIGN/CANON** — owned by an existing active authority document.
- **PROPOSED DESIGN** — intended direction, not current implementation.
- **UNKNOWN** — repository evidence does not establish the fact.
- **BLOCKED** — cannot be promoted until a named prerequisite is satisfied.
- **DEPRECATED / SUPERSEDED** — retained for history but not the preferred current candidate.
- **MIGRATION REQUIRED** — a replacement cannot safely become current without consumer/state/art migration.
- **OWNER DECISION REQUIRED** — artistic/canon approval cannot be inferred from implementation or CI.

Historical CI proves only the recorded branch/head. Documentation-only work in this slice does not re-run Android/Python runtime tests.

## 3. Runtime precedence rule that controls provenance

The inspected implementation confirms a critical rule:

1. `PixelSceneCatalog` supplies source-native scene sprites/fallbacks.
2. `PixelRasterCatalog.scene(locationId)` binds nine current locations to PNG drawables.
3. `SceneIllustration` renders the bound PNG when the raster resolves.
4. Only if no raster resolves does `SceneIllustration` render the source-native scene sprite.

The player/equipment/item path follows the same pattern through `PixelRasterCatalog.sprite(assetId)`: PNG-backed player, equipment, and item assets are preferred and source-native Kotlin sprites are fallback geometry.

Therefore:

> A newer Kotlin source master can be visually hidden by an older bound PNG.

D-029 must always reconcile source and raster together for any raster-bound family.

## 4. Child ledgers

### 4.1 Character / equipment / item / actor provenance

[Character, Equipment, Item, and Actor Asset Provenance](CHARACTER_EQUIPMENT_ITEM_ACTOR_PROVENANCE_2026-10-03.md)

Covers:

- player base sprite;
- technical hair placeholder;
- character staging shadow;
- item icons;
- equipment paper-doll layers;
- equipment slot assets;
- item-quality frames;
- opening-story actors;
- Jack approved reference relationship;
- portrait status;
- PR #22 reference-only tail;
- raster/source precedence for player/equipment/item assets.

### 4.2 Environment / scene / map provenance

[Environment, Scene, and Map Asset Provenance](ENVIRONMENT_SCENE_MAP_PROVENANCE_2026-10-03.md)

Covers:

- named scene source masters;
- current nine-scene raster baseline;
- environment modules;
- reusable infrastructure atlas;
- environment props;
- decals;
- environment overlays;
- scene/state overlays;
- map base artwork;
- map markers;
- map travel transition;
- divergent Service Tunnel / Quiet Stair static candidates;
- scene-raster occlusion and migration risk.

### 4.3 UI / FX / held-prop / animation provenance

[UI, FX, Held-Prop, and Animation Asset Provenance](UI_FX_ANIMATION_PROVENANCE_2026-10-03.md)

Covers:

- UI chrome;
- UI icons;
- UI utilities;
- Trace FX;
- Trace strain avatar/portrait effects;
- divergent diagnostic-reader held-prop masters;
- divergent Service Tunnel ambient animation;
- integration and reduced-motion risks.

## 5. Current family coverage summary

| Family | Current program-branch form | Raster/export | Runtime integrated? | Current stage |
| --- | --- | --- | --- | --- |
| Player base / hair | Kotlin fallback + PNG binding | yes | yes | `RASTER_PRESENT + CODE_PRESENT + INTEGRATED`; canon approval not established |
| Equipment/item icons and paper-doll layers | Kotlin fallback + PNG binding for current authored set | yes | yes | `RASTER_PRESENT + CODE_PRESENT + INTEGRATED`; expansion incomplete |
| Character staging | Kotlin code master | no | yes | `SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED` |
| Equipment slots | Kotlin code master | no | yes | `SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED` |
| Item quality frames | Kotlin code master | no | yes | `SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED` |
| Opening story actors | Kotlin code master | no | yes | `SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED`; actor-presence migration pending D-030 implementation |
| Canonical portraits | no dedicated production family found on inspected program branch | no | no | `PLANNED / UNKNOWN SOURCE` |
| Named scenes | Kotlin fallback + nine PNG bindings | yes | yes | `RASTER_PRESENT + CODE_PRESENT + INTEGRATED`; later divergent refinements unresolved |
| Environment modules / infrastructure atlas | Kotlin code masters | no | 3 modules: yes; atlas: no | three modules: `SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED`; atlas: `SOURCE_MASTER_PRESENT + CODE_PRESENT + DEFERRED_INTEGRATION` |
| Environment props | Kotlin code master | no | yes | `SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED` |
| Environment decals | Kotlin code master | no | yes | `SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED` |
| Environment overlays | Kotlin code master | no | yes | `SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED` |
| Scene/state overlays | Kotlin code master | no | yes | `SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED` |
| Gate Twelve district map art | Kotlin code master | no | yes | `SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED` |
| Map markers | Kotlin code master | no | yes | `SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED` |
| Map travel transition | Kotlin frame code | no | yes | `SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED` |
| UI chrome | Kotlin code master | no | yes | `SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED` |
| UI icons | Kotlin code master | no | yes | `SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED` |
| UI utilities | Kotlin code master | no | yes | `SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED` |
| Trace FX | Kotlin frame code | no | yes | `SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED` |
| Trace strain visuals | Kotlin frame code | no | yes | `SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED` |
| Diagnostic-reader held prop | divergent PR #9 code master | no | no | `DEFERRED_INTEGRATION / BLOCKED_BY_D-030_RUNTIME_AND_TAMSIN_ANCHOR` |
| Service Tunnel ambient animation | divergent PR #31 code/frame master | no | no | `VERIFIED_BRANCH_EVIDENCE + DEFERRED_INTEGRATION + MIGRATION_CONTRACT_DOCUMENTED` |

`CANON_APPROVED` is deliberately not assigned merely because code or raster exists.

## 6. Branch provenance roots used by the ledgers

Exact open-PR evidence inspected for this slice:

- PR #7 `feature/pixel-asset-wave-a@a3970de6597c77939afccb5f30d6040bdf3d608d` — historical root for the first broad pixel-asset catalogs.
- PR #8 `feature/pixel-asset-wave-l-environment-modules@54a40bb5ad0aeafb428d128be7c1465f3d1a759b` — divergent historical Wave-L provenance. Its four visual definitions survive in current source. Current runtime later integrates all three 128x64 modules as exact Map arrival previews, while `MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS` remains deferred with no main-UI consumer found.
- PR #9 `feature/pixel-asset-wave-m-diagnostic-reader@063d5879413b81656cc5c7304be0afd02402f2fd` — divergent diagnostic-reader masters. Consumer ownership is resolved: the 32x48 held master is Tamsin actor-presentation art under D-030's player-safe pose/visual-family boundary, not player inventory/equipment. Runtime remains blocked on D-030 projection plus verified Tamsin hand/wrist anchors; the 32x32 icon has no authorized current inventory consumer.
- PR #16 `feature/pixel-assets-runtime-expansion@ddbb5f4250e26b99765999d0a8e81f59cb1ea26c` — inherited runtime asset expansion.
- PR #19 `feature/png-pixel-art-runtime-a@c11133122d47009abc71e8c6e91c08aedbe91ae2` — inherited PNG raster delivery baseline.
- PR #21 `feature/pixel-map-art-pass@59a1930961ae5fc961acab5624dcbfcc2f7e66cb` — inherited map-art implementation.
- PR #22 `feature/player-avatar-art-pass@494f2b3f0dedbcb90c202aab7380694c4daf33f3` — three-commit tail is reference/documentation-only relative to inherited ancestor `2a1c7f59843f0ff248daba97781ca99279829b6c`.
- PR #23 `feature/opening-story-actor-pixel-art@9f3cf193619e1db3845c1bc71f4592c7ac62db76` — inherited story-actor implementation.
- PR #26 `feature/service-tunnel-arrival-pixel-art@2f7f77d7925e94558d219d4ab2340fbb32476717` — inherited Service Tunnel arrival/module branch point.
- PR #31 `feature/service-tunnel-ambient-animation-stack@19807863e3d68cd3ffad0e627ad19130da9bdbed` — divergent ambient-animation candidate.

For PR #27/#28/#30 static refinement lineage, use the existing source/raster reconciliation record rather than duplicating its exact per-raster evidence here.

## 7. QA interpretation

Current family catalogs have dedicated unit-test sources in the program branch for:

- asset dimensions/palette/rig mapping;
- staging;
- modules;
- props;
- decals;
- overlays;
- equipment slots;
- quality frames;
- map art;
- markers;
- travel transition;
- raster delivery;
- scenes;
- scene overlays;
- story actors;
- Trace FX;
- Trace strain;
- UI chrome;
- UI icons;
- UI utilities.

Those tests are evidence that contracts exist. They are **not a fresh pass result for this documentation commit**.

Historical successful workflow evidence remains tied to the exact PR heads recorded in [Implementation PR #7–#31 reconciliation](../IMPLEMENTATION_PR_7_31_RECONCILIATION_2026-10-02.md).

## 8. What remains incomplete in D-029

This slice is substantial but not the whole task.

Resolved in the current D-029 continuation:

- commit-level export/refresh lineage for all 24 current PNGs is recorded by `RASTER_EXPORT_AND_SOURCE_CORRESPONDENCE_2026-10-03.md` and its JSON evidence;
- PR #8 environment-module source lineage is reconciled; no separate PR #8 geometry migration remains;
- all three 128x64 PR #8-origin modules have current exact Map arrival-preview consumers;
- the infrastructure atlas is explicitly separated as `DEFERRED_INTEGRATION`, with PR #28 retained as optional presentation-only composition logic rather than a new source master;
- PR #9 diagnostic-reader consumer ownership is resolved: held-reader art belongs to Tamsin actor presentation under the D-030-safe pose/held-layer boundary; runtime remains deferred;
- PR #31 migration strategy is documented in `SERVICE_TUNNEL_AMBIENT_ANIMATION_MIGRATION_CONTRACT_2026-10-03.md`; branch evidence survives without promoting the divergent branch.

Still incomplete:

1. execute the repository-owned deterministic raster verifier/exporter on an exact checkout and persist its machine-readable report;
2. confirm fresh 24/24 pixel equivalence or repair/document any mismatch found by that execution;
3. owner visual/canon promotion decision for the Service Tunnel and Quiet Stair static survivors;
4. runtime adoption of the infrastructure-atlas composition if approved, with destination visual QA;
5. D-030 runtime actor-presentation projection plus Tamsin hand/wrist anchor verification for the held diagnostic reader;
6. implementation of the documented PR #31 ambient-animation/reduced-motion contract on the selected Service Tunnel static parent, plus destination-head verification;
7. final Jack production sprite and portrait family;
8. Tamsin/courier portrait production family;
9. per-family owner/canon approval;
10. physical-device visual/performance QA;
11. machine-readable `content/visual/asset_provenance.json` after ID/schema lock.

## 9. Reconstruction rule

If the implementation vanished, reconstruction should proceed in this order:

1. restore stable asset IDs from these ledgers;
2. restore code masters for procedural families;
3. restore current PNG exports from raster evidence;
4. restore `PixelRasterCatalog` bindings;
5. preserve PNG-first/fallback semantics until an explicit migration changes them;
6. restore Compose consumers and layer order;
7. restore player-safe state inputs only;
8. re-run catalog unit tests;
9. render and compare native-scale screenshots;
10. only then approve/supersede assets.

Do not reconstruct from screenshots alone, and do not treat the newest branch as canonical merely because it is newer.


## 10. 2026-10-03 exact raster export continuation

D-029 now also includes:

- [Raster export and source correspondence](RASTER_EXPORT_AND_SOURCE_CORRESPONDENCE_2026-10-03.md)
- `docs/evidence/raster_export_lineage_2026-10-03.json`

This exact-lineage slice establishes, for all 24 current PNG assets:

- the repository Kotlin source family;
- the source revision commit;
- the initial raster-export commit;
- any later source/raster refresh commit;
- the current source blob;
- the current raster Git blob/hash;
- whether the current raster remains from the initial export or was refreshed after a source revision.

Current classification:

- 17 current PNGs retain their initial export lineage;
- 7 current PNGs have later source revisions followed by documented raster refresh/refinement;
- the five PR #22 player/loadout raster refreshes are inherited by the current branch;
- Platform Nine and Relay Workbench source/raster refinements are synchronized in their recorded commits.

The historical PR #19 exporter remains unknown/not persisted. A new repository-owned deterministic verifier/reconstruction exporter now exists at `tools/verify_pixel_raster_equivalence.py`, with repository tests at `tests/test_pixel_raster_equivalence_tool.py`. It has not executed in this work session, so fresh 24/24 pixel equivalence remains unverified until its output is observed and persisted.


## 11. Service Tunnel ambient-animation migration decision

- [Service Tunnel ambient animation migration contract](SERVICE_TUNNEL_AMBIENT_ANIMATION_MIGRATION_CONTRACT_2026-10-03.md) exactizes PR #31's survival/migration path.
- PR #31 remains verified branch evidence, not current implementation.
- Its three track IDs, timing and moving bounds are preserved as candidate source evidence.
- Migration must be selectively reimplemented on the approved Service Tunnel static parent.
- Reduced motion is an established Android/application accessibility requirement; current runtime has no explicit reduced-motion setting path.
- The migration strategy is documented; runtime implementation and destination-head verification remain separate work.


## 12. Raster reconstruction tooling status

- `tools/verify_pixel_raster_equivalence.py` — new standard-library verifier plus safe deterministic reconstruction exporter.
- `tests/test_pixel_raster_equivalence_tool.py` — repository-level 24-binding equality/determinism/safety tests.
- `docs/evidence/raster_equivalence_verifier_status_2026-10-03.json` — machine-readable `IMPLEMENTED_EXECUTION_PENDING` evidence.

This new tool does not retroactively identify the historical PR #19 exporter. It exists to make future reconstruction/equality reproducible.
