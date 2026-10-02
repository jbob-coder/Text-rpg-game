# PR #33 moving-base drift reconciliation — 2026-10-02

Repository: `jbob-coder/Text-rpg-game`  
PR: #33  
Program branch: `docs/master-game-development-program`  
Program head inspected: `de6b10e8c79103ce34b853234e9d917685b5268d`  
PR base branch: `docs/settlement-region-build-plan`  
Base head inspected: `de6b10e8c79103ce34b853234e9d917685b5268d`  
Merge base: `c261b2aaf8bd978d27b46f8fea03435c0c5734d0`  
Status: **P0 / DO NOT BLIND-MERGE**

## 1. Verified branch state

The PR base moved after PR #33 was opened.

At this inspection:

- the base branch is **99 commits ahead** of the shared merge base;
- the program branch is **140 commits ahead** of the shared merge base;
- the branches are therefore **diverged** rather than a simple fast-forward;
- GitHub currently reports PR #33 as non-mergeable;
- the base-side comparison exposes 65 changed paths.

This explains the PR conflict state. It does not prove every changed path conflicts textually.

## 2. Authority rule for this reconciliation

Do not merge the base branch wholesale into the documentation-program branch.

Reasons:

1. both branches now contain documentation-program authorities;
2. some base-side files duplicate responsibilities already owned by the program branch;
3. one base-side owner-directive statement conflicts with the current handoff;
4. the current program branch contains a substantially larger Gate Twelve master and a newer task authority;
5. merging without a crosswalk would create two active sources of truth.

The safe operation is **classify -> compare -> selectively migrate -> supersede/archive duplicates -> verify links/indexes**.

## 3. Direct instruction conflict: numerical target units

The current owner handoff states:

> the large numerical targets remain recorded with units unresolved; they are not marked complete.

The moving base adds `docs/program/00_OWNER_DIRECTIVE_2026-10-02.md`, which states that the 2,000,000 target means **2,000,000 separate documentation files** and defines 100-file sub-batches / 1,000-file batches.

These two instructions are incompatible.

Current decision:

- preserve **UNITS UNRESOLVED** on the program branch;
- do not activate the two-million-file production mandate;
- do not import corpus automation/production targets that depend on that interpretation;
- classify the base-side statement as **CONFLICTING / REQUIRES EXPLICIT OWNER SUPERSESSION**.

No amount of repetition in derived documentation may turn the conflicting base statement into confirmed owner direction.

## 4. Overlapping active authorities

### 4.1 Gate Twelve master

Program branch:
- `docs/assets/GATE_TWELVE_REGION_MASTER_PLAN.md`
- 4,831 lines at inspected head
- blob `0d9e14f323b8d9d7ee9f57d63ef85c4186af3609`

Moving base:
- same path
- 3,378 lines
- blob `fa07bfdf7aa378d6ea66dfbd497c8ecb3cb1d8d2`

Decision:
- program-branch version remains active authority;
- do not replace it with the shorter moving-base version;
- later section-level diff may extract unique base-only details, but only with explicit ownership and no regression of Steps 1–14 or later continuation material.

### 4.2 Master task register

Program branch:
- 799 lines;
- contains D-000 through D-043 continuation tasks and current reconciliation work.

Moving base:
- 503 lines;
- introduces a smaller `DOC-001` program task structure.

Decision:
- program task register remains active;
- do not create a second master task namespace;
- unique base-side tasks may be mapped into existing D-* tasks or a new non-colliding continuation ID only after review.

### 4.3 Repository entrypoints

`AGENTS.md`, `README.md`, and `docs/IMPLEMENTATION_STATUS.md` differ on both branches.

Decision:
- program-branch entrypoints remain active for PR #33;
- base-side edits must be diffed as candidate additions, not overwritten wholesale;
- stale historical pointers may be migrated only when they do not undo current program routing.

## 5. Base-side material classification

### CLASS A — BLOCKED BY OWNER-DIRECTIVE CONFLICT

Do not migrate as active authority until the units question is explicitly resolved:

- `docs/program/00_OWNER_DIRECTIVE_2026-10-02.md` section 4;
- `docs/corpus/BATCH_0001/SB01/DOC_0000004_TWO_MILLION_FILE_MANDATE.md`;
- production/corpus controls whose numerical batching depends on 2,000,000 separate files;
- any completion/progress metric derived from that unit assumption.

The documents may remain evidence on the base branch.

### CLASS B — DUPLICATE / NEEDS CROSSWALK

These overlap responsibilities already owned by the program branch and must not become parallel authorities:

- `docs/program/01_DOCUMENTATION_PROGRAM_MASTER.md`;
- `docs/program/02_WORLD_MAP_REGIONS_PROGRAM.md`;
- `docs/program/03_PIXEL_ART_ASSET_UI_PROGRAM.md`;
- `docs/program/04_CHARACTERS_NPCS_SOCIAL_PROGRAM.md`;
- `docs/program/05_PROGRESSION_COMBAT_SYSTEMS_PROGRAM.md`;
- `docs/program/06_ECONOMY_ITEMS_ECOSYSTEM_PROGRAM.md`;
- `docs/program/07_ANDROID_APK_REBUILD_PROGRAM.md`;
- `docs/program/08_DOCUMENTATION_GUIDE_SCALE_PROGRAM.md`;
- `docs/program/09_DECISION_GAP_REGISTER.md`;
- `docs/program/10_EXECUTION_COORDINATION_GRAPH.md`;
- `docs/program/11_CONTEXTUAL_VISUAL_COMPOSITION_CONTRACT.md`;
- `docs/program/12_DOCUMENT_EXPECTATION_AND_ACCEPTANCE_STANDARD.md`;
- `docs/program/14_DOCUMENTATION_COVERAGE_AND_EXPECTATION_MATRIX.md`;
- `docs/program/16_SESSION_DECISION_LOG_2026-10-02.md`.

Target handling:
- map each section to an existing master/cross-reference/domain owner;
- migrate unique requirements only;
- mark the base-side document historical/superseded if later merged into this branch;
- never leave two active documents claiming the same final authority.

### CLASS C — COMPLEMENTARY CANDIDATES

These appear to add a narrower responsibility not fully represented by one current file and are candidates for selective migration:

- `docs/assets/GLOBAL_ASSET_REUSE_OCCLUSION_MATRIX.md`;
- `docs/systems/CLASS_RANK_SKILL_TREE_ARCHITECTURE.md`;
- `docs/systems/PERSISTENT_ADVERSARY_SYSTEM.md`;
- `docs/systems/TACTICAL_COMBAT_ARCHITECTURE.md`;
- `docs/systems/WORLD_LEVEL_AND_BALANCE_ARCHITECTURE.md`;
- `docs/world/BEAST_ZONE_AND_ECOSYSTEM_SCHEMA.md`;
- `docs/world/GATE_TWELVE_EXTERNAL_CONNECTIONS_AND_EXPANSION_REGISTER.md`;
- `docs/world/REGION_SETTLEMENT_DOCUMENTATION_TEMPLATE.md`;
- `docs/world/WORLD_ENTITY_ID_AND_REFERENCE_STANDARD.md`;
- `docs/world/WORLD_MAP_PRODUCTION_SEQUENCE.md`;
- `docs/world/WORLD_SPATIAL_HIERARCHY_AND_COORDINATES.md`.

Migration gate:
- compare against current domain masters;
- retain only unique requirements or more precise schemas;
- preserve current stable-ID, player-safe projection, migration and provenance rules;
- update cross-reference ownership;
- do not lower a current implementation-readiness standard.

### CLASS D — CORPUS/PRODUCTION INFRASTRUCTURE

The base adds:
- `docs/corpus/BATCH_0001/SB01/DOC_0000001...` through `DOC_0000020...`;
- `docs/production/*` control/manifests/checkpoints;
- branch-source audit files;
- global namespace/batch/status machinery.

Current decision:
- do not migrate this production infrastructure yet;
- first resolve whether the numerical target unit is actually “files”;
- then evaluate repository scale, Git performance, indexing cost, checkout/cloning cost and usefulness before adopting a multi-million-file architecture.

This is a scalability gate, not a rejection of structured documentation.

## 6. Base-side material that aligns conceptually

The following ideas are compatible with current program principles and may be migrated without changing core direction once duplicates are resolved:

- evidence classification;
- explicit document ownership/upstream/downstream fields;
- supersession traces;
- revision triggers;
- acceptance gates;
- stable world-entity IDs;
- map production from hierarchy -> entities -> routes -> art rather than giant-image-first;
- contextual visual composition where engine owns actor presence and UI only presents it;
- original tactical combat architecture;
- persistent adversary state with hidden/player-safe separation;
- Gate Twelve external route interfaces that stay UNKNOWN until destination IDs exist.

Compatibility does not mean the base documents themselves become active authority.

## 7. Parent-world proposal interaction

The new program-branch `docs/world/GATE_TWELVE_PARENT_WORLD_PROPOSAL.md` intentionally proposes working parent names and local municipal context while labeling them non-canon.

The base-side external-connection register explicitly says parent settlement/region remains unresolved.

These are compatible only if:
- the proposal remains `PROPOSAL / OWNER CANON DECISION REQUIRED`;
- no base-side UNKNOWN is silently rewritten to CONFIRMED;
- existing local Gate Twelve IDs/routes remain untouched.

## 8. Persistent-adversary safety interaction

The base-side `PERSISTENT_ADVERSARY_SYSTEM.md` is an original-system architecture candidate, but it does not replace the current patent-aware safeguard.

Before commercial implementation:
- retain original terminology/data/rules/presentation;
- perform claim-specific patent review for any mechanic combination materially resembling a protected system;
- do not treat “different art/names” as legal clearance.

This repository documentation is design-risk management, not legal advice.

## 9. Merge/rebase decision

Current result: **NO WHOLE-BRANCH MERGE OR REBASE YET**.

Reason:
- unresolved owner-directive conflict;
- duplicated master authorities;
- large shared-file overlap;
- current PR is non-mergeable;
- selective migration has lower blast radius and clearer provenance.

A later merge/rebase becomes reasonable only after:
1. conflict statement is resolved;
2. duplicate authority crosswalk is complete;
3. candidate unique documents are migrated or intentionally left historical;
4. Gate Twelve shared-file differences are reconciled;
5. entrypoint/task-register differences are reconciled;
6. links and indexes pass.

## 10. Next exact work

1. build a base-document -> current-authority crosswalk;
2. compare Class C candidates against current masters;
3. migrate only unique, non-conflicting requirements;
4. leave Class A/D blocked;
5. update PR #33 conflict notes;
6. then reassess mergeability and whether the base should remain the PR target at all.

## 11. Verification performed

This reconciliation used live GitHub branch/PR state and exact file blobs/line counts.

Runtime tests were not rerun because no runtime code was changed in this reconciliation.
