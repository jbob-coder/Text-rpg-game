# THE GAME — Repository Corpus Inventory Snapshot — 2026-10-04

Status: **ACTIVE SNAPSHOT / EXACT STRUCTURAL COUNTS / PARTIAL DOMAIN COUNTS**  
Repository: `jbob-coder/Text-rpg-game`  
Branch: `docs/master-game-development-program`  
Audited source HEAD: `991cd9b29ea0752fa1c303a19e8f210713efe4b5`

## 1. Purpose

This is the next reproducible D-019 inventory checkpoint after the 2026-10-02 baseline.

It records exact Git-tree structure for one immutable source HEAD and adds bounded machine-readable counts for asset manifests, the existing Status Wave-001 structural audit, and the preserved Gate Twelve map baseline.

It does **not** claim that the complete local inventory tool was executed at this HEAD. It also does not manufacture a current Markdown word count when that execution evidence is unavailable.

Machine-readable companion:

`docs/evidence/repository_inventory_2026-10-04.json`

## 2. Exact structural counts

The recursive Git tree at `991cd9b29ea0752fa1c303a19e8f210713efe4b5` contained:

| Metric | Count |
| --- | ---: |
| tracked files | 490 |
| tracked blob bytes | 5,203,664 |
| files under `docs/` | 346 |
| documentation-scope paths (`AGENTS.md`, `README.md`, `docs/**`) | 348 |
| Markdown files repository-wide | 320 |
| Markdown files under `docs/` | 318 |
| root documentation Markdown files | 2 |
| structured documentation paths (JSON/YAML/CSV class) | 21 |
| PNG files | 24 |
| Python files | 42 |
| Kotlin/KTS files | 68 |
| JSON files repository-wide | 23 |
| Python/Kotlin source files with `test` in path | 51 |
| world Markdown files | 18 |
| systems Markdown files | 216 |
| Status-system Markdown files | 204 |
| asset Markdown files | 33 |
| Android Markdown files | 5 |
| Game Context Log Markdown files | 13 |
| structured evidence files under `docs/evidence/` | 5 |
| files under `docs/verification/` | 10 |
| files under `tools/` | 2 |

These are structural counts for the exact source HEAD. They are not semantic-completion percentages.

## 3. Structured documentation inventory

The 21 structured documentation paths in documentation scope break down as:

- 13 asset-manifest JSON files;
- 5 JSON evidence files under `docs/evidence/`;
- 3 JSON verification manifests/runtime-source records under `docs/verification/`.

This count excludes non-documentation JSON elsewhere in the repository.

## 4. Asset-manifest inventory

The 13 current asset manifests contain:

- **104 manifest rows**;
- **95 unique asset IDs**.

Using the last manifest occurrence only as an inventory aid, the 95 unique IDs group as:

| Last-seen manifest status | Unique IDs |
| --- | ---: |
| BRIEF_LOCKED | 2 |
| INTEGRATED | 64 |
| CANDIDATE | 5 |
| INTEGRATED_VERIFIED | 19 |
| PRODUCED_DEFERRED_INTEGRATION | 5 |

This is **not** a replacement for the asset provenance authority.

Repeated IDs across manifests are expected, which is why 104 rows resolve to 95 unique IDs. Canonical production stage and promotion decisions remain governed by:

- `docs/assets/ASSET_PROVENANCE_REGISTRY.md`;
- `docs/assets/ASSET_FAMILY_PROVENANCE_INDEX_2026-10-03.md`;
- family-specific provenance documents;
- current exact implementation evidence.

## 5. Status / ability / passive structured corpus

Repository-owned structural audit evidence records Wave 001 as:

| Record class | Count |
| --- | ---: |
| primary abilities | 47 |
| passives | 230 |
| techniques | 188 |
| passive unlock paths | 230 |
| passive knowledge profiles | 230 |
| awakening profiles | 47 |
| counter profiles | 47 |
| **total** | **1,019** |

The existing audit reports:

- 1,019 unique IDs;
- 0 duplicate IDs;
- 0 dangling ability-parent references;
- 0 dangling passive-parent references.

Authority:

`docs/systems/status/STATUS_CORPUS_WAVE_001_AUDIT.md`

This inventory deliberately preserves that audit's warning: **count-complete is not design-complete**. These figures do not mean every record is canon-approved, numerically calibrated, world-integrated, runtime-mapped or implemented.

## 6. Gate Twelve structured baseline

The preserved Gate Twelve map evidence contains:

- **9 nodes**;
- **8 edges**.

Authority:

`docs/evidence/gate_twelve_map_baseline_2026-10-02.json`

This is a proof-region baseline, not a world-scale map completion claim.

## 7. What remains unmeasured at the current HEAD

The following D-019 dimensions are still open:

1. exact current-head Markdown word count from a complete checkout;
2. exact heading/section count;
3. generalized extractors for world/place/route/political/settlement/ecosystem/beast/resource/NPC/item records;
4. asset production-stage counts reconciled against provenance authority rather than simple manifest status;
5. executed-test counts separated from test-source path counts;
6. accepted interpretation of the owner's 3,000 / 2,000 / 10,000 / 10,000 / 2,000,000 numeric targets.

The repository-local tool `tools/documentation_inventory.py` has not been claimed as executed at this exact source HEAD.

## 8. D-019 progress conclusion

D-019 is **IN_PROGRESS**, not DONE.

What is now reproducible for this source HEAD:

- complete Git-tree structural counts;
- documentation-family path counts;
- bounded structured-document breakdown;
- manifest row and unique asset-ID counts;
- repository-owned Status Wave-001 structural counts;
- Gate Twelve node/edge baseline.

What still blocks completion is the broader content extractor layer plus an exact-checkout execution that can produce current word counts and test/evidence separation without inference.

## 9. Snapshot boundary

This report and its JSON evidence were created **after** the audited source HEAD.

Therefore they are intentionally excluded from the 490-file source snapshot. A later inventory run must use its own new exact HEAD rather than silently adding these files to the old count.
