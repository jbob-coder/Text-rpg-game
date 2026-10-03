# PR #33 Live Shared-File Reconciliation — 2026-10-03

Status: **ACTIVE D-044 EVIDENCE / SHARED-FILE SLICE COMPLETE / NO WHOLE-FILE MIGRATION REQUIRED**

Repository: `jbob-coder/Text-rpg-game`

PR: #33 — `Establish master game development and documentation program`

Program branch audited:
`docs/master-game-development-program@ab7c041d6916b2e37b75430523a2183f9483883b`

Live target branch audited by ref:
`docs/settlement-region-build-plan@65d2db8538c1b8302c314f2fbe9eb7a1b585b51d`

Shared merge base:
`c261b2aaf8bd978d27b46f8fea03435c0c5734d0`

Parent evidence:
- `docs/PR33_MOVING_BASE_DRIFT_RECONCILIATION_2026-10-02.md`
- `docs/BASE_BRANCH_DOCUMENT_CROSSWALK_2026-10-02.md`

## 1. Purpose

Close D-044's remaining shared-file question for the live PR target without:

- trusting stale PR-base metadata;
- copying older entrypoint routing back into the program branch;
- replacing the more complete Gate Twelve authority with the moving-base variant;
- silently losing a genuinely unique base-side requirement;
- treating a renamed/reorganized section as missing merely because exact lines differ.

This is a current-state reconciliation record. It does not rewrite or delete the earlier moving-base evidence.

## 2. Live branch topology

### VERIFIED CURRENT REPOSITORY STATE

Direct Git ref resolution produced:

- program ref: `ab7c041d6916b2e37b75430523a2183f9483883b`;
- target ref: `65d2db8538c1b8302c314f2fbe9eb7a1b585b51d`;
- merge base: `c261b2aaf8bd978d27b46f8fea03435c0c5734d0`.

Compared from the shared merge base:

- target branch is **99 commits ahead**;
- program branch is **210 commits ahead**.

Direct branch-to-branch comparison reports:

- status: **diverged**;
- program-only side: 210 commits;
- target-only side: 99 commits;
- merge base: `c261b2aa...`.

The target-side delta still contains **65 changed paths**. The program-side delta contains **90 changed paths**.

### PR metadata discrepancy

The PR object reported:

- base ref: `docs/settlement-region-build-plan`;
- base SHA: `c261b2aaf8bd978d27b46f8fea03435c0c5734d0`;
- `mergeable = false`;
- `mergeable_state = dirty`;
- `rebaseable = false`.

However, direct ref resolution proves the named target branch currently points to:

`65d2db8538c1b8302c314f2fbe9eb7a1b585b51d`.

Therefore D-044 must not use the PR object's `base.sha` alone as the live moving-base head.

Operational rule:

`resolve target branch ref -> compare exact refs -> then assess PR state`

The current `dirty` mergeability state is consistent with live branch divergence. No merge/rebase is authorized by this document.

## 3. Audit method

For each shared active file this audit recorded:

- exact blob on the live target head;
- exact blob on the program head;
- line counts;
- exact normalized base-only lines;
- heading differences;
- authority/reconstruction implications.

For Gate Twelve, exact-line differences were supplemented with:

- section-heading comparison;
- section-level overlap analysis;
- targeted preservation checks for numeric geometry, node anchors, route anchors, expansion rules and migration constraints;
- verification against the newer D-030 actor-projection contract where the older Gate Twelve plan's first implementation slice moved into a dedicated authority.

This is an authority/migration audit, not a claim that the two Gate Twelve files are textually identical.

## 4. Shared-file summary

| File | Live target blob | Program blob | Target lines | Program lines | Disposition |
| --- | --- | --- | ---: | ---: | --- |
| `AGENTS.md` | `f838634bcb9a7dbd98e2a526640211b2c357812b` | `49a9d94c586db5b3f3d47a28af366270d3e72fda` | 97 | 103 | **KEEP PROGRAM / NO UNIQUE REQUIREMENT MIGRATION** |
| `README.md` | `b8cc79eee9deaa21063ed4a450e43445b4cfd0d9` | `24e841245ee544660e719a0d88d373919ef4e430` | 71 | 129 | **KEEP PROGRAM / CURRENT ROUTING SUPERSEDES BASE ROUTING** |
| `docs/IMPLEMENTATION_STATUS.md` | `1e2b7687b55c28a233d3f3593ae4fd88ab2cd924` | `107752d22ad34d1a1996777cef254f996512a67a` | 110 | 111 | **KEEP PROGRAM / HISTORICAL V6 EVIDENCE PRESERVED** |
| `docs/assets/GATE_TWELVE_REGION_MASTER_PLAN.md` | `fa07bfdf7aa378d6ea66dfbd497c8ecb3cb1d8d2` | `0d9e14f323b8d9d7ee9f57d63ef85c4186af3609` | 3,378 | 4,831 | **KEEP PROGRAM / BASE VERSION SUPERSEDED AS ACTIVE AUTHORITY** |

No shared file should be wholesale copied from the live target branch into the program branch.

## 5. `AGENTS.md`

### Exact difference result

The target version has 13 normalized nonblank lines not present verbatim in the program version.

They fall into two groups.

#### A. Older routing

The target entrypoint routes agents first through:

- `docs/program/README.md`;
- `docs/program/00_OWNER_DIRECTIVE_2026-10-02.md`;
- `docs/program/09_DECISION_GAP_REGISTER.md`;
- then the task/status/V6 files.

The program entrypoint instead routes through:

- `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`;
- `docs/FINAL_GAME_RECONSTRUCTION_BLUEPRINT.md`;
- `docs/MASTER_DIRECTIVE_EXECUTION_BREAKDOWN.md`;
- `docs/DOCUMENTATION_CROSS_REFERENCE_MATRIX.md`;
- the master task register;
- implementation status;
- the relevant domain master/source/tests.

Decision:

**Do not migrate the old `docs/program/*` routing.**

Reason:

- that hierarchy is classified by the existing crosswalk as duplicate/partially blocked;
- it contains the disputed two-million-file interpretation;
- the current program routing is more complete and matches the owner's current handoff.

#### B. Historical V6/black-screen baseline

The remaining target-only lines identify:

- old stabilization branch `fix/v6-runtime-boundaries`;
- old parent V6 line;
- the then-open Android black-screen defect.

The program entrypoint already preserves V6 as historical evidence and records that the black-screen incident is historically closed by later Compose/Chaquopy emulator evidence while physical Galaxy A03 evidence remains a separate gate.

Decision:

**Do not restore the stale incident as current status.**

The engineering/safety rules, permission boundaries, task bookkeeping and verification discipline remain present in the program version.

### Disposition

`KEEP PROGRAM / BASE ROUTING HISTORICAL`

No unique active requirement remains to extract from the target `AGENTS.md`.

## 6. `README.md`

### Exact difference result

The target version contains only one normalized nonblank line absent from the program version:

a 2026-10-02 note routing current documentation authority through `docs/program/README.md` and `docs/program/00_OWNER_DIRECTIVE_2026-10-02.md`.

Every other normalized nonblank target line is present in the program README.

The program README additionally contains the active documentation-first routing, reconstruction blueprint, cross-reference matrix, proof-region documents, current operational continuation records and newer domain authorities.

### Disposition

`KEEP PROGRAM / TARGET ROUTING SUPERSEDED`

No unique README requirement requires migration.

## 7. `docs/IMPLEMENTATION_STATUS.md`

### Exact difference result

The target version contains one normalized nonblank line absent from the program version:

a planning-priority note pointing new design work to `docs/program/*`.

The program version replaces that note with a current-priority statement pointing to:

- `MASTER_GAME_DEVELOPMENT_PROGRAM.md`;
- Gate Twelve proof-region completion;
- exact live implementation/asset audit;
- reproducible corpus inventory;
- `DOCUMENTATION_CROSS_REFERENCE_MATRIX.md`;
- `THE_GAME_MASTER_TASK_REGISTER.md`.

The V6 stabilization evidence underneath remains preserved rather than rewritten as current product state.

### Disposition

`KEEP PROGRAM / HISTORICAL IMPLEMENTATION EVIDENCE PRESERVED`

No unique implementation-status requirement requires migration.

## 8. Gate Twelve master-plan relationship

The Gate Twelve files require semantic reconciliation rather than simple line-set comparison.

### 8.1 Shared foundation

Steps 1-4 and the core region model substantially share the same foundation.

The program version retains the same:

- nine current Gate Twelve location IDs;
- region-not-world scope;
- Python/domain authority;
- authored route legality;
- stable-ID principle;
- 256x144 district presentation scaffold;
- player-safe projection boundary;
- modular/source-native pixel-art direction.

### 8.2 Geometry invariants checked

The following target geometry survives in the program version:

- native district map: **256x144**;
- three vertical bands:
  - `0..47`;
  - `48..94`;
  - `95..143`;
- all nine named footprint envelopes, including:
  - Workshop Row `x=49..102`;
  - Depot Plaza `x=105..143`;
  - Municipal Archive `x=151..196`;
  - Platform Nine `x=20..83`;
  - Relay Workbench `x=75..105`;
  - Gate Twelve `x=119..154`;
  - Quiet Stair `x=88..118`;
  - Service Tunnel `x=161..199`;
  - Trace Chamber `x=194..237`;
- authored map-node percentages for all nine nodes;
- presentation anchors:
  - Platform Nine `(~46,52)`;
  - Relay Workbench `(~87,45)`;
  - Gate Twelve `(~136,69)`;
  - Quiet Stair `(~102,101)`;
  - Service Tunnel `(~179,88)`;
  - Trace Chamber `(~210,56)`;
- the six current route presentation segments;
- the planned `DISTRICT_PLAZA <-> PLATFORM_NINE` connector remains a future content migration rather than a UI-only shortcut;
- outward Plaza, Quiet Stair and deeper Service Tunnel expansion capacity remains reserved without inventing destinations.

The current program version makes the coordinate separation more explicit:

- semantic map-node anchor;
- physical scene entrance;
- world-expansion boundary;
- state-overlay anchor.

This is an expansion of the target contract, not loss of the target geometry.

### 8.3 Reusable geometry/material rules

The target file's reusable-module rule is retained and expanded into dedicated:

- civic surface;
- depot/service;
- lower-maintenance;
- municipal-public;
- workshop;
- depot;
- restricted-service;
- prop-anchor families.

The current version also makes explicit that district-map, scene, character and portrait coordinates are different coordinate spaces.

No target-side external-reference dimensions such as a 1-meter tile, five-section or twelve-area subdivision become canon.

### 8.4 Steps 6-10

The current program version is the more detailed authority for:

- material/light language;
- pixel density;
- asset-stage vocabulary and production ordering;
- Story/Map/Character/actor UX;
- portrait/panel behavior;
- text/signage separation;
- base/overlay/actor/equipment/prop/map/UI state layers;
- hidden-state leak prevention;
- loading/caching;
- mobile/low-memory behavior;
- bounded animation and reduced motion.

The target version is useful historical design evidence but does not own a unique active contract in these areas after the program rewrite.

### 8.5 Implementation order

The target implementation sequence used:

`GT-IMP-001` through `GT-IMP-007`.

The program version reorganizes that work into dependency phases A-J:

`exact audit -> safe projection -> asset reconciliation -> Story/Map composition -> missing art -> route/content migration -> animation -> verification`

The underlying dependency remains the same: safe actor presence must precede presentation logic that depends on it.

### 8.6 `GT-IMP-001` preservation check

The target Gate Twelve plan required player-safe scene-presence projection and exact opening-story equivalence.

Its acceptance cases included:

- `OPENING_DEPOT_BLACKOUT` -> wounded courier + Tamsin;
- `OPENING_DECISION` -> Tamsin;
- `OPENING_RECOVERY` -> Tamsin;
- `OPENING_TUNNEL` -> Tamsin;
- no projected visible actor -> no story actor;
- Android no longer owns presence from scene ID;
- hidden relationship/knowledge/internal flags stay private;
- Python/Android verification and visual equivalence evidence.

Those requirements are not lost.

They are now owned in greater detail by:

`docs/android/PLAYER_SAFE_ROOM_ACTOR_PROJECTION_CONTRACT.md`

That contract records the current hard-coded placements, exact opening equivalence fixtures, support-courier identity rule, hidden-field prohibition, semantic placement migration and verification gates.

Therefore the target `GT-IMP-001` block is **SUPERSEDED BY D-030 CONTRACT**, not a unique missing requirement.

### 8.7 Verification/migration rules

The program Gate Twelve version preserves or strengthens the target rules that:

- exact-head evidence is required;
- historical CI does not prove a later head;
- Python tests alone do not verify Android behavior;
- screenshots/native-scale QA are required for visual work;
- emulator and physical-device evidence are separate;
- stable IDs/gameplay authority are KEEP by default;
- presentation may be reworked substantially;
- deletions wait for consumer audit and verified replacement;
- save/content changes require explicit migration;
- Git/provenance history remains evidence after supersession.

### Gate Twelve disposition

`KEEP PROGRAM / TARGET VERSION HISTORICAL-SUPERSEDED FOR ACTIVE AUTHORITY`

No whole-file migration is allowed.

This audit found no remaining target-only Gate Twelve requirement that requires copying the 3,378-line version over or alongside the 4,831-line current authority.

## 9. Shared-file migration result

For the four shared active paths audited here:

- **0 whole-file migrations required**;
- **0 target entrypoint requirements require extraction**;
- **0 target Gate Twelve requirements require a parallel active authority**;
- target-specific `docs/program/*` routing remains intentionally non-authoritative on the program branch;
- `GT-IMP-001` is already preserved under the dedicated D-030 projection contract.

D-044's **shared-file diff requirement is complete for these active shared authorities**.

## 10. What this does not close

D-044 still has separate work:

1. inspect remaining live target-only Class C / `EXTRACT UNIQUE` documents;
2. migrate only requirements that are genuinely absent from current program authorities;
3. keep the disputed numerical-unit-dependent corpus machinery blocked;
4. re-resolve both branch refs after further concurrent commits;
5. reassess PR mergeability after selective reconciliation;
6. do not retarget, merge, rebase, force-push or delete branches without explicit owner direction.

## 11. Reconstruction rule

If this reconciliation disappeared, reproduce it by:

1. resolve `refs/heads/docs/master-game-development-program`;
2. resolve `refs/heads/docs/settlement-region-build-plan`;
3. determine their merge base;
4. never substitute the PR object's stored `base.sha` for the live named ref without checking;
5. fetch both versions of each shared active path;
6. compare exact blobs, normalized lines and headings;
7. for rewritten master documents, compare stable IDs, numeric invariants, authority rules, migration gates and downstream dedicated contracts;
8. retain one active authority per responsibility;
9. migrate unique requirements only;
10. preserve historical evidence rather than overwriting it.

## 12. Current decision

**Shared-file reconciliation result: KEEP PROGRAM.**

The moving target branch remains a historical/complementary source for selective unique-requirement extraction.

It is not authorized to overwrite:

- program entrypoint routing;
- current task authority;
- current Gate Twelve master;
- current numerical-target interpretation;
- current D-030 projection contract.
