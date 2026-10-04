# THE GAME — Implementation Survivor & Migration Matrix — 2026-10-04

Status: **ACTIVE / D-020 BRANCH RECONCILIATION COMPLETE / SELECTED MIGRATIONS MAY REMAIN DEFERRED**  
Repository: `jbob-coder/Text-rpg-game`  
Program branch: `docs/master-game-development-program`  
Documentation head at creation: `5db72c09716c2621e7c905834837dae9be300485`

Parents:
- `docs/IMPLEMENTATION_PR_7_31_RECONCILIATION_2026-10-02.md`
- `docs/assets/ASSET_FAMILY_PROVENANCE_INDEX_2026-10-03.md`
- `docs/assets/SOURCE_RASTER_RECONCILIATION_2026-10-02.md`
- `docs/assets/SERVICE_TUNNEL_AMBIENT_ANIMATION_MIGRATION_CONTRACT_2026-10-03.md`
- `docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md`

## 1. Purpose

This document closes D-020's documentation requirement by converting the PR #7–#31 history into one survivor/migration decision matrix.

It answers:

- which implementation line is already inherited by the current program branch;
- which divergent branch is superseded by a later inherited/current implementation;
- which branch remains useful only as provenance/reference;
- which branch contains a candidate that still requires selective migration;
- which candidate is blocked by owner visual/canon approval or another documented dependency.

This matrix does **not** merge branches, promote `main`, change runtime code, choose art on the owner's behalf, or delete historical branches.

## 2. Decision vocabulary

- **CURRENT / INHERITED** — implementation responsibility already survives in the current program lineage.
- **CURRENT CONTRACT / REWORK LATER** — behavior survives, but final presentation may be reworked under later contracts.
- **SUPERSEDED AS FINAL SURFACE** — historical implementation remains evidence, but a later inherited/current surface owns the final-current baseline.
- **NO SEPARATE MIGRATION REQUIRED** — useful branch content has already survived through later current source or has been fully reconciled as non-unique.
- **DEFERRED SELECTIVE MIGRATION** — branch-only work remains useful, but must be reimplemented/cherry-picked by file/behavior after prerequisites.
- **OWNER DECISION REQUIRED** — technical provenance is resolved, but visual/canon promotion cannot be inferred.
- **HISTORICAL / FIX-EXTRACTION ONLY** — do not merge wholesale; consult only if the specific behavior is needed.
- **DOCUMENTATION ONLY** — useful planning/provenance ancestry; no runtime promotion implied.

## 3. PR #7–#31 survivor matrix

| PR | Subsystem | Final reconciliation | Destination / migration rule |
| --- | --- | --- | --- |
| #7 | first broad pixel-asset/runtime line | **CURRENT / HISTORICAL ROOT** | Current branch inherits descendants. Keep provenance; no separate migration. |
| #8 | environment modules + infrastructure atlas | **NO SEPARATE MODULE MIGRATION REQUIRED / ATLAS DEFERRED** | Three 128x64 modules have current exact Map arrival-preview consumers. Infrastructure atlas remains produced/deferred; PR #28 is optional composition evidence. |
| #9 | diagnostic reader icon/held prop | **DEFERRED SELECTIVE MIGRATION** | Held prop belongs to Tamsin actor presentation, not player inventory. Blocked on D-030 actor projection + verified hand/wrist anchors. Icon has no authorized current inventory consumer. |
| #10 | avatar overlay rig | **CURRENT / INHERITED** | Preserve rig/orientation contract unless a deliberate rig migration replaces it. |
| #11 | player-safe stat inspection | **CURRENT / INHERITED** | Preserve engine-owned arithmetic and player-safe inspection boundary. |
| #12 | Character/Equipment paper-doll UI | **CURRENT CONTRACT / REWORK LATER** | Keep slot/paper-doll state behavior; presentation may evolve under final Character UX. |
| #13 | Character/Stats contribution refinement | **CURRENT / INHERITED** | Keep contribution/equipment-action behavior. |
| #14 | earlier dedicated Skills surface | **SUPERSEDED AS FINAL CURRENT SURFACE** | Retain as comparison evidence; PR #25 inherited mobile Skills hierarchy/layout is current baseline. |
| #15 | player-hub recovery/equipment-detail fix line | **HISTORICAL / FIX-EXTRACTION ONLY** | Do not merge wholesale. Consult exact diff only if current inherited descendants lack a required recovery/detail behavior. |
| #16 | runtime asset expansion | **CURRENT / INHERITED** | Preserve safe bindings and explicit integrated/deferred distinction. |
| #17 | secondary-button asset reuse | **CURRENT / INHERITED** | Keep where semantic role still matches. |
| #18 | scene-first Story layout | **CURRENT CONTRACT / REWORK LATER** | Current Story presentation baseline; later Story redesign must preserve safe state boundaries. |
| #19 | PNG scene/player raster delivery | **CURRENT / INHERITED RASTER BASELINE** | Current raster precedence baseline. Candidate scene refinements must migrate source+raster together. |
| #20 | Story resource HUD | **CURRENT CONTRACT / REWORK LATER** | Preserve projected resource semantics; final HUD layout may change. |
| #21 | authored district map art | **CURRENT / INHERITED** | Keep map semantics/authored-art direction. |
| #22 | avatar-art-pass tail | **NO RUNTIME MIGRATION REQUIRED FOR TAIL** | Exact reconciliation found tail reference/docs-only relative to inherited ancestor. Keep approved-reference provenance; final Jack production remains D-029 work. |
| #23 | opening Story actor art | **CURRENT / INHERITED TRANSITIONAL ACTOR PRESENTATION** | Preserve current visible behavior until D-030 room-actor projection replaces scene/location inference. |
| #24 | mobile Bag pixel layout | **CURRENT CONTRACT / REWORK LATER** | Current inherited Bag baseline; final Bag can rework only through UX/APK migration. |
| #25 | mobile Skills hierarchy/layout | **CURRENT / INHERITED CURRENT SKILLS BASELINE** | Supersedes #14 as current surface baseline. |
| #26 | Service Tunnel arrival/module binding | **CURRENT / INHERITED BRANCH POINT** | Current arrival-preview/module binding survives; static-scene refinement decisions remain separate. |
| #27 | Service Tunnel static scene refinement | **OWNER DECISION REQUIRED / CANDIDATE SURVIVOR** | If selected, migrate source master + PNG together, recheck actors/props/overlays and run destination-head QA. |
| #28 | infrastructure-atlas Service Tunnel composition | **OPTIONAL DEFERRED SELECTIVE MIGRATION** | No new scene master geometry. Reimplement only if selected after final static Service Tunnel visual decision. |
| #29 | Gate Twelve map/pixel blueprint | **DOCUMENTATION ONLY / INHERITED** | Keep as documentation/provenance ancestry. No runtime verification implied. |
| #30 | Quiet Stair static scene refinement | **OWNER DECISION REQUIRED / CANDIDATE SURVIVOR** | Carries #27 tunnel refinement in ancestry; selectively migrate Quiet Stair source+raster onto destination rather than merging branch wholesale. |
| #31 | Service Tunnel ambient animation | **DEFERRED SELECTIVE MIGRATION** | Migration contract exists. Reimplement on selected static Service Tunnel parent with reduced-motion/off-screen lifecycle behavior and destination-head verification. |

## 4. Current survivor architecture

The current implementation baseline that should be treated as the working survivor is:

1. inherited engine + Android projection boundary;
2. inherited paper-doll/stat/inventory/Story/Map/Skills application chain through PR #26;
3. current program-branch pixel catalogs and 24-raster family as the baseline evidence set;
4. documentation/provenance overlays from later documentation work;
5. divergent candidates retained only through explicit migration contracts/provenance.

The final target does **not** equal “merge every green PR.”

Historical CI is evidence for exact historical heads only.

## 5. Divergent branch decisions that still require action

### 5.1 PR #9 — diagnostic reader

Technical ownership is resolved.

Still required before runtime adoption:
- D-030 safe actor projection;
- Tamsin pose/hand/wrist anchor confirmation;
- typed held-layer presentation field or equivalent safe visual-family contract;
- destination-head QA.

Current decision: **DEFERRED**.

### 5.2 PR #15 — recovery/equipment-detail fix branch

Do not preserve this branch as a competing runtime authority.

Current decision:
- **HISTORICAL / FIX-EXTRACTION SOURCE ONLY**;
- compare exact behavior against current inherited code only if a known defect/requirement points back to this branch;
- no proactive wholesale merge.

### 5.3 PR #27 — Service Tunnel static art

Technical provenance is resolved.

Remaining decision:
- current inherited baseline versus PR #27 refined candidate.

Current classification: **OWNER DECISION REQUIRED**.

### 5.4 PR #28 — infrastructure atlas composition

The atlas already exists as produced/deferred current source lineage.

PR #28 contributes composition behavior, not a competing source master.

Current classification: **OPTIONAL REIMPLEMENTATION AFTER STATIC ART DECISION**.

### 5.5 PR #30 — Quiet Stair static art

Technical topology is resolved:
- PR #30 stacks on the PR #27 tunnel refinement and adds Quiet Stair.

Remaining decision:
- current Quiet Stair baseline versus PR #30 refined candidate.

Current classification: **OWNER DECISION REQUIRED**.

### 5.6 PR #31 — ambient animation

Migration path is documented.

Current classification:
- **VERIFIED BRANCH EVIDENCE**;
- **DEFERRED INTEGRATION**;
- **REIMPLEMENT ON SELECTED STATIC PARENT**.

## 6. What is superseded

The following historical surfaces should not be maintained as competing final-current authorities:

- PR #14 Skills surface — superseded by current inherited PR #25 Skills baseline;
- PR #15 branch as a whole — retained only for bounded fix extraction;
- divergent branch ancestry for #27/#28/#30/#31 — source evidence only, not a second runtime line;
- duplicate branch UI/pixel implementations that already survive through inherited descendants.

“Superseded” does not mean delete historical branches.

## 7. Migration safety rules

For any deferred candidate that later migrates:

1. select exact source head;
2. identify exact files/symbols/rasters;
3. map current destination consumers;
4. preserve player-safe state boundaries;
5. migrate source+raster pairs together when raster precedence applies;
6. add/update unit and instrumentation coverage;
7. rerun Python/Android/build/package gates;
8. capture visual evidence for presentation changes;
9. record destination commit and rollback path;
10. only then change production/canon status.

## 8. D-020 completion boundary

D-020 branch/provenance **documentation reconciliation is complete** because every PR #7–#31 now has one explicit current disposition and migration rule.

D-020 completion does **not** mean:
- PR #27 or #30 art has been owner-approved;
- PR #31 animation has been implemented;
- PR #9 held-prop runtime has been implemented;
- PR #15 behavior has been cherry-picked;
- final APK reconstruction is complete.

Those actions remain owned by D-029, D-030, D-032, final UX/APK work and future bounded implementation tasks.

## 9. Next consumers

- D-029 — final asset provenance/promotion decisions;
- D-030 — actor/room projection migration;
- D-032 — mechanics/API migration;
- D-033 — late-stage teardown manifest;
- final APK reconstruction after its prerequisites.
