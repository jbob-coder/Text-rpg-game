# PR #19 Raster Exporter Provenance Audit — 2026-10-04

**Status:** VERIFIED HISTORICAL PROVENANCE / D-029 PARALLEL SLICE  
**Agent:** Kestrel  
**Task:** D-029 — Exactize asset provenance and production stage  
**Claim head:** `dd2e28e35c0946f8baa86fb3513cebf431dcf73b`  
**Historical subject:** PR #19 / `feature/png-pixel-art-runtime-a@c11133122d47009abc71e8c6e91c08aedbe91ae2`

## Question closed

Existing D-029 records said the historical PR #19 raster exporter was "not persisted/found." That wording left one technical ambiguity: whether an exporter might actually be committed somewhere on the PR #19 head but had simply not been located by the earlier audit.

This audit closes that ambiguity for the committed PR #19 repository state.

## Exact evidence inspected

1. GitHub PR #19 changed-file inventory contains 31 paths. The change set includes:
   - Android workflow/UI/runtime raster-consumer changes;
   - `PixelRasterCatalog.kt`;
   - 24 PNG files under `android/app/src/main/res/drawable-nodpi/`;
   - `PixelRasterCatalogTest.kt`.
2. The PR #19 changed-file inventory contains **no exporter/generator/tool/script path**.
3. The exact PR #19 head root at `c11133122d47009abc71e8c6e91c08aedbe91ae2` contains `.github`, `android`, `content`, `docs`, `src`, and `tests` plus root metadata files. It contains **no `tools/` directory**.
4. An exact contents lookup for `tools` at that head returns `404 Not Found`.
5. The PR #19 head commit itself (`c11133122d47009abc71e8c6e91c08aedbe91ae2`) changes only the Android screenshot-evidence workflow to include Relay Workbench. It does not add or modify an exporter.

## Disposition

### CURRENT VERIFIED HISTORICAL FACT

No raster exporter is committed in the exact PR #19 head tree, and no exporter/generator/script is part of PR #19's changed-file set.

Therefore D-029 should no longer treat the PR #19 exporter as a potentially recoverable repository artifact that merely remains undiscovered on that branch. For reconstruction purposes its disposition is:

`HISTORICAL GENERATION PROCESS NOT PERSISTED IN PR19 COMMITTED TREE`

The 24 delivered PNGs and their committed Kotlin source masters remain historical/current lineage evidence. They do **not** prove that the original generation mechanism can be reproduced from PR #19 alone.

### UNKNOWN

This audit cannot prove whether an uncommitted local script, external tool, manual process, or discarded working-tree file was used before the PNGs were committed. No such mechanism is claimed.

## Reconstruction consequence

The repository-owned `tools/verify_pixel_raster_equivalence.py` must remain the reconstruction/verification authority for future deterministic reproduction. It is a replacement reconstruction tool, not evidence that the original PR #19 exporter was recovered.

No runtime asset, raster, source master, visual canon state, or owner promotion decision is changed by this audit.

## Acceptance impact

This closes one real D-029 provenance ambiguity with exact branch/head evidence:

`PR #19 exporter status: not committed / not recoverable from the PR #19 tree`

Remaining D-029 work still includes fresh exact-checkout raster-equivalence execution, owner visual promotion decisions, future portrait/actor production, destination visual QA, and physical-device QA. Those are not claimed complete here.
