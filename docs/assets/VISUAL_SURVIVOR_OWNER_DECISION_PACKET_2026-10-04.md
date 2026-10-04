# THE GAME — Visual Survivor Owner Decision Packet — 2026-10-04

Status: **OWNER DECISION REQUIRED / D-029 VISUAL PROMOTION GATE**  
Repository: `jbob-coder/Text-rpg-game`  
Program branch baseline: `docs/master-game-development-program@3578f8f2b61214c780ea8d6fe4a74efb7c197fdf`

Related authorities:
- `docs/assets/SOURCE_RASTER_RECONCILIATION_2026-10-02.md`
- `docs/assets/ENVIRONMENT_SCENE_MAP_PROVENANCE_2026-10-03.md`
- `docs/IMPLEMENTATION_SURVIVOR_MIGRATION_MATRIX_2026-10-04.md`
- `docs/assets/CURRENT_ASSET_CONSUMER_ZERO_CONSUMER_AUDIT_2026-10-04.md`

## 1. Purpose

This packet isolates the two visual/canon choices that still prevent D-029 from resolving the current static scene survivors.

The owner is **not** being asked to merge branches.

The choices are only:

1. which Service Tunnel static scene should become the target survivor;
2. which Quiet Stair static scene should become the target survivor.

Until the owner chooses, the current integrated baseline remains authoritative by default.

## 2. Decision D029-VIS-001 — Service Tunnel static scene

### Option A — keep current integrated baseline

Current program runtime uses:

- source family: current `PixelSceneCatalog.serviceTunnelDefault`;
- runtime drawable: `pixel_service_tunnel_default_scene.png`;
- current raster binding remains active through `PixelRasterCatalog.scene("SERVICE_TUNNEL")`;
- current asset has a verified source consumer and authored-content reachability.

Advantages:
- no migration required;
- current application consumer and raster-precedence behavior already match;
- lowest compatibility risk;
- PR #28 and PR #31 can remain deferred until a future intentional art revision.

Cost:
- rejects the PR #27 static refinement as the promoted target.

### Option B — promote PR #27 refined Service Tunnel

Exact candidate:

`feature/service-tunnel-scene-art-pass@d19e6edba4dec5345f1365bb358084b9b77eb7d9`

Verified historical evidence:

- source scene changed;
- preferred Service Tunnel PNG changed with it;
- raster resource name/binding contract stayed compatible;
- historical workflow run 36950023830 succeeded on that exact branch head.

Important limitation:

Historical green CI does **not** prove destination-head correctness or owner visual approval.

If selected, migrate only the intended source+raster pair and recheck:
- Story scene composition;
- Tamsin/actor anchors;
- environment props/decals/overlays;
- arrival preview;
- PR #28 optional infrastructure detail;
- PR #31 animation compatibility;
- phone-width visual evidence;
- raster/source equivalence.

### Safe default while undecided

**KEEP CURRENT BASELINE.**

No code/raster migration should occur merely because PR #27 is newer.

## 3. Decision D029-VIS-002 — Quiet Stair static scene

### Option A — keep current integrated baseline

Current program runtime uses:

- current `PixelSceneCatalog.evacStairDefault`;
- `pixel_evac_stair_default_scene.png`;
- current `EVAC_STAIR` raster binding;
- authored `OPENING_SOLO_EXIT` location path.

Advantages:
- no migration required;
- current consumer chain remains unchanged;
- lowest compatibility risk.

Cost:
- PR #30 refined Quiet Stair remains historical/candidate evidence.

### Option B — promote PR #30 refined Quiet Stair

Exact candidate:

`feature/quiet-stair-scene-art-pass@7adacd474ae22908bba2fc72247f500312ea7483`

Verified historical evidence:

- Quiet Stair source changed;
- Quiet Stair preferred PNG changed with it;
- historical workflow run 36950951038 succeeded.

Important topology:

PR #30 is stacked on PR #27 and therefore also carries the refined Service Tunnel in branch ancestry.

If the owner selects **only** the Quiet Stair refinement, migration must be file/symbol/raster selective. Do not merge PR #30 wholesale and accidentally promote the Service Tunnel candidate.

### Safe default while undecided

**KEEP CURRENT BASELINE.**

## 4. Dependent candidates after the Service Tunnel decision

### PR #28 — infrastructure-atlas composition

Exact branch:

`feature/service-tunnel-atlas-detail@b5cb510408331446ec3fdfbc6ec188b8a5516c15`

What it is:
- optional composition behavior;
- reuses the existing `MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS`;
- does not provide a competing atlas source master.

Decision order:

`Service Tunnel static survivor -> optional PR #28 composition decision`

Do not promote PR #28 first.

### PR #31 — Service Tunnel ambient animation

Exact branch:

`feature/service-tunnel-ambient-animation-stack@19807863e3d68cd3ffad0e627ad19130da9bdbed`

Current classification:

`VERIFIED_BRANCH_EVIDENCE + DEFERRED_INTEGRATION + REIMPLEMENT_ON_SELECTED_STATIC_PARENT`

Decision order:

`Service Tunnel static survivor -> reduced-motion/runtime contract -> selective PR #31 reimplementation -> destination QA`

Do not merge PR #31 wholesale.

## 5. What the owner does not need to decide yet

The following remain separate from these two static-scene choices:

- final Jack production sprite;
- Jack portrait family;
- Tamsin/courier portrait family;
- PR #9 diagnostic-reader runtime promotion;
- final raster-equivalence pass;
- final APK reconstruction;
- physical Galaxy A03 acceptance.

## 6. Promotion acceptance gate

A candidate selected by the owner is **SELECTED**, not automatically `INTEGRATED`.

Promotion to `INTEGRATED / VERIFIED` requires:

1. exact source head recorded;
2. exact source symbol/file selected;
3. matching source+raster pair migrated together;
4. current destination consumer compatibility reviewed;
5. current asset IDs/resource names preserved or explicitly migrated;
6. Kotlin/unit/instrumented tests executed;
7. deterministic raster check executed where applicable;
8. phone-width visual evidence captured;
9. source/raster blobs and destination commit recorded;
10. rollback path documented.

## 7. Decision record format

When the owner decides, record one of:

### Service Tunnel
- `D029-VIS-001 = KEEP_CURRENT_BASELINE`
- `D029-VIS-001 = PROMOTE_PR27_REFINED_SERVICE_TUNNEL`

### Quiet Stair
- `D029-VIS-002 = KEEP_CURRENT_BASELINE`
- `D029-VIS-002 = PROMOTE_PR30_REFINED_QUIET_STAIR`

No other interpretation should be inferred from silence.

## 8. Current state

Until an explicit owner decision is recorded:

- current Service Tunnel baseline = **CURRENT AUTHORITY**;
- PR #27 = **CANDIDATE / OWNER DECISION REQUIRED**;
- current Quiet Stair baseline = **CURRENT AUTHORITY**;
- PR #30 = **CANDIDATE / OWNER DECISION REQUIRED**;
- PR #28 = **OPTIONAL AFTER STATIC DECISION**;
- PR #31 = **DEFERRED AFTER STATIC DECISION**.

No runtime migration is authorized by this packet.
