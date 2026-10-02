# Source/raster branch reconciliation — 2026-10-02

Repository: `jbob-coder/Text-rpg-game`  
Documentation read baseline: `8e34a792d5f9c73c27c5ef1fc82473ef074b4f46`  
Status: **P0 provenance and delivery reconciliation**

## Runtime precedence confirmed

At the inspected implementation lineage:

- `PixelSceneCatalog.kt` owns source-native 128x64 scene masters/fallbacks.
- `PixelRasterCatalog.scene(locationId)` binds nine named locations to PNG resources.
- `SceneIllustration` decodes the bound PNG and renders it when available; it falls back to the source-native `PixelSprite` only when the raster is unavailable.
- Therefore a Kotlin source edit without a synchronized preferred PNG can be visually hidden at runtime.

This record does not claim pixel equality. It records exact Git blob identity and branch relationships so later render comparison can be reproducible.

## Inherited PR #19 raster baseline

PR #19 head: `c11133122d47009abc71e8c6e91c08aedbe91ae2`  
Workflow: Android Pixel Client run 36823014708 — success.  
`PixelSceneCatalog.kt` blob: `b6126ddcab09d1005baa0352299ec57b301bf3d2`.  
`PixelRasterCatalog.kt` blob: `6bfc11c88df1d2edb473ed8b3cd3293e7f2822d8`.

| Runtime raster | PR #19 blob | Bytes |
| --- | --- | ---: |
| `pixel_platform_nine_blackout_scene.png` | `591fa56cd17bdf5576774815ed330b3f40af4ccc` | 1,255 |
| `pixel_relay_workbench_default_scene.png` | `96612e083a9db37a4588049dd2c3a3f2aad304b4` | 1,182 |
| `pixel_gate_twelve_sealed_scene.png` | `2c2b1838060c66cc794e945fe56bece691cacea6` | 32,900 |
| `pixel_service_tunnel_default_scene.png` | `aa6e31fa37e3ebcadef84de9ccd47d93b6d065b1` | 32,900 |
| `pixel_evac_stair_default_scene.png` | `75a985e7cdee6e669b936c3d0a2d2e769939f394` | 32,900 |
| `pixel_trace_chamber_idle_scene.png` | `43f9919fef3e0ae0ad27c4e09e008064068a93ff` | 32,900 |
| `pixel_district_plaza_open_scene.png` | `215ce07dbf78a15b5d7036c81ca02f3dd0e7ca79` | 32,900 |
| `pixel_district_archive_default_scene.png` | `f511c36c84690c76f39cbf9928b608cc00461d52` | 32,900 |
| `pixel_workshop_row_default_scene.png` | `49a1e0789fcb83d84e872de04c521eb4dee5e1db` | 32,900 |

## Service Tunnel refinement — PR #27

PR #27 head: `d19e6edba4dec5345f1365bb358084b9b77eb7d9`  
Workflow: run 36950023830 — success.  
Relation to documentation head: **DIVERGED**, six branch-only commits from inherited #26.  

Observed changes:

- `PixelSceneCatalog.kt` blob becomes `b9124a02cac75abd6c84aaa93c090fdd0b846f9f`.
- `pixel_service_tunnel_default_scene.png` becomes `50543eb0316c98ffd2a93c0976849af985ccdf74`, 1,529 bytes.
- `PixelRasterCatalog.kt` remains `6bfc11c88df1d2edb473ed8b3cd3293e7f2822d8`; the runtime binding still prefers the same resource name.
- All other nine-scene raster blobs inspected remain unchanged from PR #19 at this branch head.

Conclusion: source and preferred raster both changed on #27, so this is not the specific failure case of “source changed, raster stayed old.” It is still **not yet canon-integrated**, because the branch diverges from the documentation/runtime ancestry and no cross-branch render comparison has selected it as survivor.

## Quiet Stair refinement — PR #30

PR #30 head: `7adacd474ae22908bba2fc72247f500312ea7483`  
Workflow: run 36950951038 — success.  
Relation to documentation head: **DIVERGED**.

Observed changes:

- `PixelSceneCatalog.kt` blob becomes `ade70ece1394b89b35bc67e9af8813107cdcffdb`.
- `pixel_evac_stair_default_scene.png` becomes `c4759aeb1a917cb31ccb1465c4f1b26d9f1de220`, 1,411 bytes.
- The refined Service Tunnel raster from #27 remains present at blob `50543eb0316c98ffd2a93c0976849af985ccdf74`.
- `PixelRasterCatalog.kt` remains unchanged at `6bfc11c88df1d2edb473ed8b3cd3293e7f2822d8`.

Conclusion: #30 carries both the #27 tunnel static refinement and a later Quiet Stair source/raster refinement. Selecting #30 as a source of Quiet Stair work therefore requires deliberate file-level integration, not a blind branch merge.

## PR #28 and PR #31 relationship

PR #28 (`b5cb5104`) changes environment-module/catalog preview code but not the named Service Tunnel scene PNG. Its useful atlas/detail work must be compared against the chosen static tunnel scene composition.

PR #31 (`19807863`) changes ambient-animation catalog, `SceneIllustration`, tests and documentation but not the static named scene PNG. Its animation must be rebased/reimplemented after the static source/raster survivor is chosen.

## Current authority decision

Until a bounded implementation integration is performed:

- inherited #19 PNGs remain the current documentation-branch raster baseline;
- #27 Service Tunnel static art is a **CANDIDATE_SURVIVOR**;
- #30 Quiet Stair static art is a **CANDIDATE_SURVIVOR**;
- #28 atlas detail is a **CANDIDATE_COMPOSITION_LAYER**;
- #31 ambient animation is a **DEFERRED_CANDIDATE**;
- none of these divergent candidates should be marked integrated merely because their historical CI passed.

## Required promotion procedure

For each candidate location:

1. compare source-native scene rows/palette at inherited and candidate heads;
2. compare PNG dimensions, alpha, exact blob/hash and rendered appearance;
3. confirm the PNG corresponds to the intended source revision rather than an unrelated export;
4. inspect Story/arrival-preview/map consumers;
5. check actor/prop/overlay anchors against changed geometry;
6. integrate by file-level migration onto the chosen implementation parent;
7. run Kotlin/unit/instrumentation/build/package gates;
8. capture phone-width screenshots;
9. record final source blob + raster blob + destination commit;
10. only then mark `INTEGRATED` / `VERIFIED`.

## Explicit defect rule

A future edit is a blocking visual-delivery defect when:

- `PixelSceneCatalog` changes a bound location,
- the corresponding preferred PNG remains at an older visual revision,
- and the runtime still resolves that PNG through `PixelRasterCatalog.scene()`.

The correct fix is to update/re-export the preferred raster or deliberately alter/remove its binding with documented fallback intent. Do not rely on fallback source art while an older preferred raster silently wins.
