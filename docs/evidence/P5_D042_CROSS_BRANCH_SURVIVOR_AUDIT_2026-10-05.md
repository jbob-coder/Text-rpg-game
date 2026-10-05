# P5 / D-042 — Cross-Branch Survivor Audit — 2026-10-05

**Player-AI:** Quorix  
**Task:** Parallel P5 / D-042 — Cross-branch existing-state source audit  
**Audit authority HEAD:** `f5c3731d0c494dd3948f88481a3d5b2d3d0f4138`  
**Audit tree:** `87f51737160050e5ed7f46b21932c838fd024e41`  
**Machine-readable companion:** `docs/evidence/P5_D042_CROSS_BRANCH_SURVIVOR_MATRIX_2026-10-05.json`

## Purpose

This is a bounded survivor reconciliation, not another whole-repository inventory and not permission to merge historical branches.

The audited slice covers:

- recent completed integration ancestry for D-064, D-065/D-068, and D-067;
- the still-divergent Service Tunnel / Quiet Stair presentation family in PRs #27, #28, #30, and #31;
- current consumer ownership for those candidate behaviors;
- one stale current-audit assumption that should no longer send later Player-AIs back through already-completed D-020/D-044 work.

No gameplay source, Android source, raster asset, content, branch history, or save schema was modified by this audit.

## Recent integration ancestry

At the exact audit head:

| Task | Completion head | Relation to audit head | Disposition |
| --- | --- | --- | --- |
| D-064 | `d7ebb7ca439695e256a429a1e5d160daae69a521` | ancestor; audit head is 31 commits ahead / 0 behind | **INHERITED CURRENT AUTHORITY** |
| D-065 / D-068 | `e883205559c64d2e82614160bd6548c2c9332808` | ancestor; audit head is 317 commits ahead / 0 behind | **INHERITED CURRENT AUTHORITY** |
| D-067 | `0fd843a5ece0f87c74a262c7ecb6739d025b0678` | ancestor; audit head is 271 commits ahead / 0 behind | **INHERITED CURRENT AUTHORITY** |

This means these completed proofs are not stranded only on divergent feature branches. Their recorded completion commits are in authority ancestry. This is ancestry evidence, not a new runtime-pass claim.

## Bounded unresolved survivor family

### PR #27 — Service Tunnel static refinement

**Head:** `d19e6edba4dec5345f1365bb358084b9b77eb7d9`  
**State:** open / divergent.

Unique behavior:

- replaces the Service Tunnel procedural source master with a muted municipal-perspective composition;
- replaces `pixel_service_tunnel_default_scene.png`;
- adds focused scene-shape/palette assertions.

At the audit head, neither the PR's `PixelSceneCatalog.kt` blob nor its Service Tunnel PNG blob matches authority.

Current player-visible ownership is important: `PixelRasterCatalog.scene("SERVICE_TUNNEL")` resolves the raster resource and `SceneIllustration` draws that raster first. `PixelSceneCatalog.serviceTunnelDefault` is the fallback when raster loading is unavailable.

**Disposition:** **DEFERRED MIGRATION CANDIDATE — D-029.**

Do not cherry-pick only the procedural catalog. The visible scene is raster-first. Source master + raster must move as one provenance/equivalence unit after D-029 visual/provenance review.

### PR #28 — Service Tunnel infrastructure-atlas arrival detail

**Head:** `b5cb510408331446ec3fdfbc6ec188b8a5516c15`  
**State:** open / divergent.

Unique behavior:

- adds `arrivalDetailTiles("SERVICE_TUNNEL")`;
- composes the entire municipal infrastructure atlas below the map arrival preview.

Authority currently exposes only `arrivalPreview(locationId)`; `PixelEnvironmentArrivalPreview` does not consume `arrivalDetailTiles`.

**Disposition:** **DEFERRED PRESENTATION CANDIDATE.**

Preserve as evidence. D-029 owns atlas provenance; D-077 or later V11 Android UX may consume the composition only if the arrival-preview surface survives final UX. There is no evidence-based reason to import the strip now.

### PR #30 — Quiet Stair static refinement

**Head:** `7adacd474ae22908bba2fc72247f500312ea7483`  
**State:** open / divergent.

Unique behavior:

- replaces the EVAC_STAIR / Quiet Stair procedural source master;
- replaces `pixel_evac_stair_default_scene.png`;
- adds focused visual-shape assertions.

Neither the PR's `PixelSceneCatalog.kt` blob nor its Quiet Stair PNG blob matches authority.

Current ownership mirrors Service Tunnel: `PixelRasterCatalog.scene("EVAC_STAIR")` supplies the raster rendered first by `SceneIllustration`; the procedural catalog is fallback geometry.

**Disposition:** **DEFERRED MIGRATION CANDIDATE — D-029.**

Treat source + raster as one candidate. Branch recency is not visual/canon approval.

### PR #31 — Service Tunnel ambient fan/panel/drip animation

**Head:** `19807863e3d68cd3ffad0e627ad19130da9bdbed`  
**State:** open / divergent.

Unique behavior:

- adds `PixelAmbientAnimationCatalog`;
- adds fan, panel, and drip tracks;
- adds `SceneIllustration` playback;
- adds JVM and Compose checks for track bounds and visible frame advancement.

The catalog and both dedicated tests are absent from authority.

The current pixel-runtime composition standard explicitly requires **restrained loops** and **reduced-motion behavior**, and also states that open Service Tunnel ambient work is distinct from canonical integration. PR #31's tests prove track geometry and visible advancement, but no reduced-motion path is present in the patch.

**Disposition:** **REIMPLEMENT BEFORE MIGRATION.**

The behavior remains a valid candidate, but do not merge PR #31 as-is. The future implementation should:

1. wait for the selected Service Tunnel static survivor;
2. consume only player-safe visible location/scene state;
3. provide an explicit reduced-motion path;
4. verify lifecycle/off-screen behavior rather than relying on an untested infinite-loop assumption;
5. rerun current merge-state Android/emulator evidence.

Likely integration consumer: `SceneIllustration`; likely task lane: D-077 / later presentation integration, with D-029 supplying the approved static/art provenance base.

## Concrete regression / migration risk

The highest-risk incorrect migration is to treat `PixelSceneCatalog.kt` as the visible scene owner.

That assumption is false on current authority for Service Tunnel and Quiet Stair because `SceneIllustration` uses `PixelRasterCatalog` first. A code-only transplant from #27 or #30 can therefore appear "integrated" in source while leaving the player-visible raster unchanged.

The correct migration unit is the selected source master + raster + catalog binding + tests/provenance evidence.

PR #31 has a separate accessibility risk: merging its infinite ambient loops without a reduced-motion contract would violate the current composition standard.

## Stale D-042 remainder found

`docs/DEEP_SOURCE_EXISTING_STATE_AUDIT_2026-10-04.md` still lists these as remaining:

- D-020 cross-branch survivor/migration matrix;
- D-044 PR #33 Class-C extraction.

Live authority already marks both completed. They should no longer be treated as open D-042 archaeology.

After this P5 slice, the honest remaining D-042/D-006 boundaries are narrower:

- broader field/consumer mapping remains owned by D-021/D-026;
- asset source/raster/canon promotion remains D-029;
- zero-consumer/deprecation proof remains required immediately before destructive REMOVE decisions;
- additional branch families should be audited only when they are still unclassified and materially affect reconstruction.

## Verification boundary

Executed:

- exact PR metadata / changed-file reads for #27, #28, #30, #31, #59, #65, #70;
- exact Git ancestry comparisons for D-064, D-065/D-068, D-067 completion heads;
- exact Git blob comparison for the bounded #27/#28/#30/#31 file surfaces;
- live authority source inspection of `PixelRasterCatalog`, `PixelSceneCatalog`, `PixelEnvironmentModuleCatalog`, `PixelEnvironmentPreview`, and `SceneIllustration`;
- current composition-standard inspection for ambient/reduced-motion requirements.

Not executed:

- no Python/Android test suite;
- no APK build;
- no emulator/device run;
- no raster visual-equivalence execution;
- no physical Galaxy A03 validation.

This evidence classifies branch survivors. It does not promote them.
