# L0-08 — Layer Index and Build Log

Layer: **L0 Foundation**
Purpose: navigation for the corpus, and the record of what this corpus changed,
verified, and deliberately left open.

---

## 1. Corpus state

| Item | Value |
| --- | --- |
| Corpus version | `v1.0` |
| Corpus started | 2026-10-03 |
| Authority branch | `docs/master-game-development-program` |
| Working branch | `docs/hermes-angle-documentation` |
| Baseline HEAD | `2111addc18836c863809eb290f2843fc862cc533` |
| L0 status | **COMPLETE** |
| L1 status | **IN PROGRESS** (3 documents + 3 machine-readable files) |
| L2–L5 status | PENDING |
| Integrity harness | `tools/verify_reconstruction_corpus.py`, 9/9 passing |

## 2. Layer index

| Layer | Directory | Status | Documents |
| --- | --- | --- | ---: |
| L0 | `docs/reconstruction/L0/` | **COMPLETE** | 10 |
| L1 | `docs/reconstruction/L1/` | **IN PROGRESS** | 3 + 3 JSON |
| L2 | `docs/reconstruction/L2/` | PENDING | — |
| L3 | `docs/reconstruction/L3/` | PENDING | — |
| L4 | `docs/reconstruction/L4/` | PENDING | — |
| L5 | `docs/reconstruction/L5/` | PENDING | — |

### 2.1 L0 documents

| # | Document | Purpose |
| ---: | --- | --- |
| 00 | `L0-00_RECONSTRUCTION_OBJECTIVE_AND_PROTOCOL.md` | Objective, fidelity definition, twelve interpretive angles, unit contract, rebuild sequence |
| 01 | `L0-01_CANON_DIGEST.md` | World, story, characters, items, quests, map, visual direction — with authored-state honesty |
| 02 | `L0-02_ANGLE_STANDARD.md` | Camera definitions, six-view set, six view-set families, per-view template, consistency ledger |
| 03 | `L0-03_NATIVE_GRID_AND_ANCHOR_STANDARD.md` | Grid hierarchy, 18 anchors, cluster map, z-order, pixel rules, visual form classification |
| 04 | `L0-04_PALETTE_AND_MATERIAL_STANDARD.md` | UI/character anchors, material ramp law, budgets, verified current palettes |
| 05 | `L0-05_ASSET_UNIT_REGISTRY.md` | All 500 planned units with family, native master, view set, canon class |
| 06 | `L0-06_STABLE_ID_AND_NAMING_STANDARD.md` | ID stability, namespaces, manifest contract, state bindings, supersession |
| 07 | `L0-07_PROHIBITIONS_AND_FAILURE_MODES.md` | Catastrophic failures, 11 prohibition classes, anti-pattern table |
| 08 | `L0-08_LAYER_INDEX_AND_BUILD_LOG.md` | Layer navigation and build log |
| 09 | `L0-09_CORPUS_INTEGRITY_PROTOCOL.md` | Observed failure modes and the post-generation verification step |

## 3. Planned layer contents
Each remaining layer is scoped below with its intended deliverables, so a
subsequent pass can build them without re-deriving intent.

### L1 — Existing-state record

What exists today, with evidence. Delivers:

- the 24 runtime rasters: exact path, dimensions, SHA-256, git blob, bounds,
  colour count, occupied region, catalog binding;
- the 9 text-map scene masters and their palette bindings;
- the code visual catalogs and what each contains;
- the branch/stack history and what is superseded;
- the open reconciliation items inherited from `ASSET_PROVENANCE_REGISTRY.md`;
- a machine-readable `docs/reconstruction/L1/existing_state.json`.

### L2 — Asset angle specifications

Per-unit specifications for all 500 planned units. Delivers:

- per-view reconstruction specs for every `SIX_VIEW` / `SIX_VIEW_DEFERRED` unit
  (114 units);
- presentation-state specs for `PRESENTATION_STATES` units (213);
- prop-angle specs for `PROP_ANGLES` units (61);
- scene-camera specs for `SCENE_CAMERA` units (28);
- tile/axis specs for `TILE_AXES` units (84);
- each with the twelve interpretive angles from L0-00 §4.

### L3 — World angle specifications

Locations, environments, architecture and scene angles. Delivers:

- a scene-camera specification per named location (9 authored, plus the
  documented-but-unbuilt ones);
- architectural axis and crop-safe-zone definitions;
- overlay classes per location;
- Gate Twelve region and district subdivision angle documentation.

### L4 — Character angle specifications

Character identity, turnarounds, layers, portraits, animation. Delivers:

- `PLAYER_BODYFRAME_A_TURNAROUND` six-view spec;
- Jack Wilson identity-layer specs;
- `NPC_TAMSIN_TURNAROUND` six-view spec with full asymmetry ledger;
- player directional bases (front/left/right/back);
- animation sheet frame contracts;
- portrait and emotion-family specs.

### L5 — Systems and narrative reference

World, systems, progression and story reconstruction reference. Delivers:

- ability and passive corpus structure with exact counts;
- rarity tier semantics;
- level/XP and the Level-100 exception;
- Trace Echo system reference;
- quest graph and scene graph;
- narrative beat reference for the authored 19 scenes.

## 4. Build and verification log

Each entry records what was added, what was verified, and what was found.

### 2026-10-03 — L0 foundation created

**Added**

- `docs/reconstruction/README.md` — corpus root, layer model, angle requirement,
  scope and change protocol.
- `docs/reconstruction/L0/` — nine foundation documents.

**Repository survey performed**

- Repository cloned and inspected. `main` contains one commit (`6f8d9c5 Initial
  commit`) and a two-line README only.
- 60 remote branches enumerated after a full fetch (the initial pre-fetch
  listing showed 64 refs; the authoritative post-fetch count is 60); the
  substantive working tip is
  `docs/master-game-development-program` (354 files, 210 under `docs/`,
  most recent commit 2026-10-03).
- Existing corpus measured: 182 Markdown documents, 2,229,747 characters
  (excluding this corpus).

**Canon extraction performed**

- `content/vertical_slice_01.json` parsed in full: 19 scenes, 4 quests, 9 map
  nodes, 8 map edges, 8 knowledge records, 6 items, 1 ability with 2 techniques,
  1 character record, 7 opening flags, starting attributes/skills/resources and
  Tamsin's relationship and personality axes.
- `docs/world/*` confirmed to be **schema-first with empty catalogs** — no
  kingdoms, factions, settlements or wider geography are authored. Recorded as
  such rather than filled in.
- `docs/systems/status/*` sampled: 102 distinct primary ability IDs across nine
  rarity tiers; 230 passive IDs across five categories; Level-100 exception
  documented as owner-established canon.

**Asset registry built mechanically**

- All five batch catalogs parsed: **500 units, 001–500, no missing numbers, no
  duplicate stable asset IDs.**
- Canon-class column present on batches 002–005 (400 units): 300
  `technical/non-canon framework`, 96 `technical`, 4
  `current/provisional canon + technical`.
- View sets assigned by one rule, ID pattern dominant, family fallback:
  `PRESENTATION_STATES` 167, `TILE_AXES` 146, `PROP_ANGLES` 71,
  `SIX_VIEW_DEFERRED` 69, `SIX_VIEW` 30, `SCENE_CAMERA` 17.
- Registry emitted twice — `L0-05_ASSET_UNIT_REGISTRY.md` (index) and
  `L0-05_ASSET_UNIT_REGISTRY.json` (machine-readable, with an assertable
  integrity claim) — and **verified equal after generation**: 500 rows matched
  500 units on number, ID and view set, with zero mismatches.

### 2026-10-03 — Third self-correction: view-set rule divergence

The first registry generation used a family-first rule; a second pass used an
ID-first rule. A consistency check between the two outputs found **87
per-unit divergences** and **different totals** (e.g. `NPC_ARCHETYPE_*` bases
classified as `SIX_VIEW` by the ID rule but `TILE_AXES` by the family rule;
all 17 location scenes classified `SCENE_CAMERA` by family and `TILE_AXES` by
ID pattern).

Resolution: adopted the **ID-first** rule as the single authority, because the
stable ID is the stable identity (L0-06 §1) and the family label is a
descriptive annotation that varies between catalogs. Both files were
regenerated from one parse and re-verified equal.

This is the third time a check caught an error before it reached a document
(§4 below lists the first two). The pattern is deliberate: generate, verify,
and only then write. A registry whose stated counts disagree with its own rows
is worse than no registry, because a rebuilder cannot tell which is wrong.

**Pixel evidence gathered (fresh, by decoding every existing raster)**

All 24 PNGs in `android/app/src/main/res/drawable-nodpi/` were decoded at pixel
level. Findings recorded in L0-03 §8.1 and L0-04 §6:

- **Zero partial-alpha pixels across all 24 files** — the binary-transparency
  rule is currently honoured.
- All 24 files are **unique by SHA-256** — no placeholder duplication.
- Palette usage is within every family budget: scenes 9–12 colours (budget
  16–32), item icons 4–8 (budget 6–12), character/paper-doll 2–10 (budget
  8–16).
- Per-location ramp families identified, including four locations sharing one
  district-outdoor family by intent (L0-04 §6.2).
- `pixel_item_signal_ring_paperdoll` occupies **2 pixels** — correct behaviour
  for a ring micro-layer, not a broken asset.
- `pixel_player_hair_tech_placeholder` is a 3-colour head-top region and is
  explicitly placeholder-named; recorded as **not** Jack's hair.

### 2026-10-03 — Repository equivalence verifier executed

The repository ships its own tool, `tools/verify_pixel_raster_equivalence.py`,
whose recorded status was `IMPLEMENTED_HARDENED_EXECUTION_BLOCKED_BY_ENVIRONMENT`
with fresh 24/24 equivalence `NOT YET VERIFIED`. **It was executed.**

**Result: `24/24` assets pixel-match their Kotlin source masters,
`total_pixel_mismatches: 0`.**

Checks passing: `all_pixels_match_source`, `all_dimensions_match`,
`all_binding_dimensions_match`, `all_runtime_bindings_match`,
`all_sha256_match_evidence`, `all_git_blobs_match_evidence`,
`asset_count_is_24`, `all_lineage_metadata_match`,
`binding_lineage_path_sets_match`, `lineage_paths_are_unique`,
`runtime_binding_set_matches`.

One check fails: `all_lineage_source_blobs_match` (24/24 sub-checks false).

**Root cause — diagnosed, and it is a tool defect, not art drift.**

The tool computes a per-asset source blob from raw file bytes:

```python
source_bytes = (root / source_path).read_bytes()
source_blob = git_blob_sha1(source_bytes)
```

Git, when hashing a working-tree file, normalises line endings (CRLF → LF) per
`.gitattributes`/core.autocrlf. Verified on `PixelSceneCatalog.kt`:

| Hashing method | Result |
| --- | --- |
| raw bytes (what the tool does) | `1e2019297ec92cbe0238a6bcbb827fdfaa60eca2` |
| `git hash-object <file>` | `b6126ddcab09d1005baa0352299ec57b301bf3d2` |
| raw bytes with CRLF→LF normalised | `b6126ddcab09d1005baa0352299ec57b301bf3d2` |

The file on disk has 823 CRLF line endings. Line-ending normalisation makes the
two hashes agree exactly. The lineage evidence records the whole-file
normalised blob (`b6126dd…`), which matches `current_source_files` in the
lineage JSON and matches `git hash-object`.

**Conclusion.** This is a **Windows-only false failure** in the verifier. The
art is correct and current; the evidence file is correct; the tool's hashing
does not apply git's line-ending normalisation. Recorded as a corpus finding,
**not** acted on — fixing the tool is an implementation change outside this
corpus's documentation-only scope. Logged here and in L1 so the next
implementation pass picks it up.

**Independent confirmation.** A separate check in this corpus comparing every
lineage `current_source_blob` against `git hash-object` for the corresponding
source file returned **0 mismatches across all 24 records** (9 scene assets +
15 character/item assets, sourced from `PixelSceneCatalog.kt` and
`PixelAssetCatalog.kt`).

### 2026-10-03 — Two false findings self-corrected

Recorded because the method matters more than the conclusion.

1. **Scene row-width "defect".** An initial parse suggested
   `workshopRowDefault` had malformed rows of length 33–38 instead of 128.
   On inspection this was a **regex over-capture**: the pattern matched a node
   list (`"PLATFORM_NINE"`, `"RELAY_WORKBENCH"`, …) adjacent to the row block.
   All 9 scene masters are valid 64x128. No defect exists.
2. **Raster/text-map palette mismatch.** An initial comparison reported all 9
   scenes as palette-mismatched. This was an **off-by-one in the slicing
   arithmetic** producing 6-character hex values with a stray `F` prefix.
   Corrected comparison confirms Gate Twelve, Platform Nine and Service Tunnel
   match exactly, and the remaining six differ only by **declared-but-unused
   palette slots** — a real (minor) authoring observation now recorded at
   L0-04 §6.3, not a raster/source mismatch.

Both were caught by verifying rather than reporting. Neither reached a document
as a false claim.

## 5. Open items inherited from existing authority

These are recorded, not resolved, because they are owned elsewhere.

| Item | Owner |
| --- | --- |
| Verifier line-ending normalisation defect | `tools/` (implementation) |
| Stale verifier status evidence (`execution pending`) | `docs/evidence/` |
| Declared-but-unused palette slots in 6 scene masters | asset production |
| Jack Wilson identity hex values not recorded in canon | asset production |
| D-029 provenance reconciliation still `IN_PROGRESS` | `ASSET_PROVENANCE_REGISTRY.md` |
| Native-scale art review pending | QA |
| Physical Galaxy A03 visual QA pending | QA |
| Source-master lineage for many exports | provenance |

## 6. Gaps this corpus has deliberately not filled

| Gap | Why not filled |
| --- | --- |
| Wider world, factions, settlements | Not authored. Empty catalogs are intentional. |
| Beast/creature assets | No canon defines creatures. |
| Jack's exact palette hexes | Must be sampled from the approved reference at production time. |
| Historical exporter identity for PR #19 assets | `UNKNOWN / NOT PERSISTED` — cannot be reconstructed. |
| Turnaround views beyond the front base | Not built. Specification exists; assets do not. |

## 7. Rebuild-readiness statement

**Ready now.** A rebuilder can correctly reconstruct: the full canon of the
authored vertical slice, the angle standard, the 32x48 rig with all 18 anchors,
the palette and material system, the complete 500-unit inventory with view-set
assignment, ID and manifest contracts, and every prohibition.

**Not ready.** The corpus does not yet contain per-unit angle specifications
(L2–L4). Until L2–L4 exist, the art workload is enumerated but not specified
view by view, and a rebuilder would still need to make per-view decisions.

## 8. L1 — existing-state record (in progress)

Deliberately built in the opposite order from the usual: **capture before
interpret**. The owner has stated the beta APK will be broken down and that the
reference photos and APK are what this reconstruction is planned from, so some
evidence is perishable and must be recorded before it changes.

### 2026-10-03 — L1a: preservation and perishable evidence

`L1-00_PRESERVATION_PRIORITY_AND_PERISHABLE_EVIDENCE.md`

Ranks perishable evidence by urgency and records each item's identity, hash,
scope and permitted/rejected use. Key findings:

- **The APK's real art surface is 192 distinct asset IDs**, not 24. 168 of them
  exist only as Kotlin text-map definitions across 23 pixel catalogs in 8,621
  lines, and would be lost with the client branches. These are Type B source
  masters under `PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md` §8.
- The highest-value reference, `UI_REFERENCE_CHARACTER_APPROVED_V1`, is the only
  approved source for Jack Wilson's visual identity and lives on Google Drive
  with a recorded SHA-256.
- Sibling-repo references are recorded but flagged as **not currently
  reconstructible** — that repo's own notes say the full image is not supplied
  and the Drive links required sign-in.
- **60 remote branches**, corrected from the 64 shown by a pre-fetch listing.
  Three branch pairs share a head SHA, so content comparison alone cannot
  separate them.

### 2026-10-03 — L1b: branch, runtime and raster evidence

- `L1-01_BRANCH_AND_RUNTIME_SURFACE.md` + `L1-01_branch_inventory.json` —
  full branch table, duplicate-head analysis, runtime composition.
- `L1-02_EXISTING_RASTER_EVIDENCE.md` + `L1-02_raster_evidence.json` — per-pixel
  measurements for all 24 rasters.

Measured results:

- **71 distinct colours** across the whole 24-asset corpus, with 75% of all
  pixels in five dark ramp values. Accents are sparse and semantic: Cyan 1.67%,
  Gold 0.88%, Danger 0.38%.
- Every UI accent appears in the art **at its exact specified hex**.
- Five scenes deliberately share one ramp family (district reuse); three depart
  for specific reasons. Service Tunnel is the darkest; Trace Chamber has the
  highest cyan density.
- The Dead Relay state family verifies correct design: `damaged` and
  `signal_lost` share **identical bounds** and differ only in indicator state,
  and `signal_lost` has the fewest colours.
- `pixel_item_signal_ring_paperdoll` is **2 pixels** — correct micro-layer
  behaviour, not a broken asset.

**Most consequential finding.** `pixel_player_gameplay_front_base` was measured
pixel by pixel and its silhouette does **not** read as the documented male player
figure: skin occupies the full outer edge of both arms from y19 to y33 with no
sleeve mass, and the waist-to-hip flare reads feminine-coded. This conflicts with
`CHARACTER_PIXEL_BLUEPRINTS.md` §1.0, which locks Jack Wilson's approved
identity as the target. Recorded as a migration placeholder to be rebuilt from
the approved reference — **not** to be reproduced. Measured deviations from the
L0-03 cluster map (head 16 px wide starting y4 rather than 11 px at y2; feet
wider than the declared anchors) are recorded rather than silently reconciled.

Also recorded: `#8B5F4B`, Tamsin's authored skin-shadow anchor, appears in the
*player* sprite at 14 pixels. Recorded as an observation with an explicit warning
that palette-anchor presence is not identity evidence.

### 2026-10-03 — Corpus integrity harness added

`tools/verify_reconstruction_corpus.py` — nine checks, each encoding a defect
actually observed during corpus construction, verified to catch truncation,
unbalanced code fences and unescaped newlines, and verified not to fire on
documents that legitimately describe those defects.

`L0-09_CORPUS_INTEGRITY_PROTOCOL.md` records the seven observed failures, the
reasoning checks the harness cannot perform, and the persistence rule (commit
per layer). Current state: **9/9 checks passing, 224,171 characters**.
