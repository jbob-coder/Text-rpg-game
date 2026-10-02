# Implementation PR #7–#31 reconciliation — 2026-10-02

Repository: `jbob-coder/Text-rpg-game`  
Authority branch: `docs/master-game-development-program`  
Reconciliation read baseline: `8e34a792d5f9c73c27c5ef1fc82473ef074b4f46`  
Status: **P0 exact-branch reconciliation record**

## Purpose

This record reconciles implementation PRs #7–#31 against the current documentation-program branch without treating an open PR as merged authority.

Definitions used here:

- **INHERITED**: the PR head is an ancestor of the documentation-program head; the compare merge-base equals the PR head.
- **DIVERGED**: the PR head contains commits that are not ancestors of the documentation-program head.
- **PARTIAL**: an earlier commit from that PR line is inherited, but the current PR head contains a later branch-only tail.
- **CI GREEN**: the recorded PR head has a completed successful `Android Pixel Client` workflow.
- Documentation ancestry does **not** mean promotion to `main`, final canon approval, physical-device acceptance, or permission to delete the source branch.

## Exact reconciliation matrix

| PR | Head | Base | Relation to docs head | CI at recorded head | Subsystem / intent | Reconciliation decision |
| --- | --- | --- | --- | --- | --- | --- |
| #7 | `a3970de6` | `integration/android-open-world-v1-reconcile` | INHERITED | run 36773072464 — success | pixel-asset system / loadout visuals | Retain as historical root of the inherited asset line. Do not reopen old presentation choices merely because the PR remains open. |
| #8 | `54a40bb5` | `feature/pixel-asset-wave-a` | DIVERGED (+6 branch-only commits) | run 36773224465 — success | reusable environment modules / infrastructure atlas | Preserve as candidate source material. Compare exact assets/consumers against #16, #26 and #28 before any selective migration. No automatic merge. |
| #9 | `063d5879` | `feature/pixel-asset-wave-a` | DIVERGED (+7) | run 36778591342 — success | diagnostic reader production masters | Preserve production evidence. Integration remains deferred unless a real typed runtime consumer exists; do not fabricate a reader interaction surface. |
| #10 | `7d4558ea` | `feature/pixel-asset-wave-a` | INHERITED | run 36791439179 — success | paper-doll overlay rig contract | Retain rig/orientation contract as inherited baseline. |
| #11 | `7cba26a4` | `fix/avatar-overlay-rig-contract` | INHERITED | run 36792821912 — success | player-safe stat inspection | Retain player-safe inspection boundary; Android must not own modifier arithmetic. |
| #12 | `40c95ec2` | `feature/player-safe-stat-inspection` | INHERITED | run 36793699892 — success | character equipment paper-doll UI | Retain verified slot/paper-doll presentation contract unless replaced by an explicitly migrated final Character surface. |
| #13 | `791a839b` | `feature/character-equipment-paperdoll-ui` | INHERITED | run 36801876404 — success | Character/Stats refinement | Retain inherited contribution/equipment-action behavior. |
| #14 | `2f50abe7` | `feature/character-equipment-paperdoll-ui` | DIVERGED (+6) | run 36794045790 — success | dedicated Skills surface | Preserve as behavior/presentation candidate. Compare with later inherited #25 mobile Skills work; do not maintain two competing final Skills surfaces. |
| #15 | `93f8be13` | `feature/character-stats-inspection` | DIVERGED (+11); PR currently non-mergeable | run 36800913142 — success | player-hub runtime recovery / equipment detail | Treat as fix-extraction source only. Diff the recovery behavior against inherited descendants before cherry-picking; do not merge wholesale while conflict state is unresolved. |
| #16 | `ddbb5f42` | `feature/character-stats-inspection` | INHERITED | run 36808323405 — success | runtime asset expansion | Retain inherited safe runtime bindings and deferred/unbound distinction. |
| #17 | `623cf9bb` | `feature/pixel-assets-runtime-expansion` | INHERITED | run 36808843923 — success | secondary-button asset reuse | Retain where semantic role still matches. |
| #18 | `5a8151a5` | `feature/pixel-assets-existing-reuse-b` | INHERITED | run 36813157344 — success | scene-first Story layout | Retain as inherited presentation baseline subject to final Story rework contract. |
| #19 | `c1113312` | `feature/story-scene-first-pixel-art` | INHERITED | run 36823014708 — success | PNG scene/player raster delivery | Retain as current inherited raster baseline. Later #27/#30 refinements are not automatically present. |
| #20 | `d80aee80` | `feature/png-pixel-art-runtime-a` | INHERITED | run 36884520604 — success | Story resource HUD | Retain only as player-safe presentation; final screen structure may be reworked. |
| #21 | `59a19309` | `feature/story-pixel-resource-hud` | INHERITED | run 36908417976 — success | authored district map art | Retain map semantics and authored-art direction. |
| #22 | `494f2b3f` | `feature/pixel-map-art-pass` | PARTIAL/DIVERGED (+3 from inherited `2a1c7f59`) | run 36957097941 — success | player avatar art refinement | Do not call the current PR head inherited. Compare its three-commit tail against current manifests/references and selectively promote only approved identity-compatible changes. |
| #23 | `9f3cf193` | `feature/player-avatar-art-pass` | INHERITED | run 36944154030 — success | opening story actor art | Retain opening actor equivalence as inherited current behavior. |
| #24 | `f4f8d4c8` | `feature/opening-story-actor-pixel-art` | INHERITED | run 36945408846 — success | mobile Bag pixel layout | Retain as inherited mobile layout baseline; final Bag may be reworked only through APK/UI migration plan. |
| #25 | `141192bb` | `feature/mobile-bag-pixel-art` | INHERITED | run 36947136146 — success | mobile Skills hierarchy/layout | Treat as current inherited Skills presentation baseline; use #14 only as comparison/source evidence. |
| #26 | `2f7f77d7` | `feature/mobile-skills-pixel-layout` | INHERITED | run 36949189946 — success | Service Tunnel arrival art binding | Retain as branch point for tunnel refinements. |
| #27 | `d19e6edb` | `feature/service-tunnel-arrival-pixel-art` | DIVERGED (+6) | run 36950023830 — success | Service Tunnel static scene refinement | Candidate static survivor. Source + raster both change; integrate only after visual/provenance comparison against inherited #19/#26 state. |
| #28 | `b5cb5104` | `feature/service-tunnel-arrival-pixel-art` | DIVERGED (+3) | run 36950528306 — success | Service Tunnel infrastructure-atlas detail | Candidate compositional detail. Compare against #27 and final room packet; do not merge both branches blindly. |
| #29 | `b6e2d97c` | `feature/service-tunnel-arrival-pixel-art` | INHERITED | no commit workflow returned; documentation-only | Gate Twelve map/pixel blueprint | Retain as documentation ancestry and provenance context. Runtime verification is not implied. |
| #30 | `7adacd47` | `feature/service-tunnel-scene-art-pass` | DIVERGED (+11 from #26 branch point) | run 36950951038 — success | Quiet Stair static scene refinement | Candidate static survivor for Quiet Stair. Must be reconciled together with #27 because it carries the refined tunnel raster in its ancestry. |
| #31 | `19807863` | `docs/gate-twelve-map-pixel-asset-blueprint` | DIVERGED (+6) | run 36952192376 — success | Service Tunnel ambient animation | Keep as animation candidate only after the final static Service Tunnel source/raster survivor is selected. Reduced-motion and off-screen-stop requirements remain mandatory. |

## Branch topology conclusions

1. None of PRs #7–#31 is merged to `main`; their value is ancestry/evidence, not merge status.
2. The documentation program already inherits the central runtime chain through #26 plus documentation PR #29.
3. The branches requiring explicit survivor review are #8, #9, #14, #15, #22, #27, #28, #30 and #31.
4. #27, #28 and #30 all branch from the Service Tunnel refinement area and must not be stacked by guesswork.
5. #31 is downstream of documentation PR #29 rather than the final static-art branch; animation therefore cannot establish which static tunnel raster should win.
6. #15 is the only PR in this range currently reported non-mergeable. Its successful historical CI does not resolve current conflicts.

## Survivor order for the visual branch family

Use this order:

1. inherited #19 raster baseline;
2. inherited #21 map-art semantics;
3. inherited #22 ancestor at `2a1c7f59` plus explicit review of current #22 tail;
4. inherited #23–#26 runtime/UI progression;
5. choose Service Tunnel static survivor from #27 plus any non-conflicting #28 detail;
6. choose Quiet Stair static survivor from #30;
7. rebase/reimplement #31 ambient animation on the selected static survivor rather than merging stale ancestry;
8. rerun exact-head tests/screenshots after any integration.

## Acceptance gate for a divergent survivor

A divergent PR contributes to the final reconstruction only when all of the following are recorded:

- exact source commit and file list;
- destination branch/head;
- file-level conflict resolution;
- source/raster or code/resource provenance;
- typed consumer mapping;
- player-safe state boundary;
- unit/instrumentation/build checks;
- screenshot/render comparison for presentation work;
- no stable-ID/save-schema regression;
- rollback path.

## Immediate follow-up

- Source/raster reconciliation: `docs/assets/SOURCE_RASTER_RECONCILIATION_2026-10-02.md`.
- Parent-world decision proposal: `docs/world/GATE_TWELVE_PARENT_WORLD_PROPOSAL.md`.
- Do not delete divergent branches after reconciliation; they remain evidence until their useful content is migrated or explicitly rejected.
