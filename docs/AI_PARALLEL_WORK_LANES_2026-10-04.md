# THE GAME — Parallel AI Work Lanes

**Status:** HISTORICAL FIRST-WAVE LANE DESIGN / NOT LIVE CLAIM AUTHORITY  
**Purpose:** preserve the original P1–P5 parallel-lane decomposition that kept multiple AI agents productive while the D-060 -> D-079 dependency chain advanced.  
**Observed activation HEAD:** 4570005b4d544f56db1222623955139a3b23c01a — historical only; every claimant must fetch live HEAD.

**Current authority note — 2026-10-08 AST:** the original P1–P5 lanes described below are completed historical lanes. Later P6–P18 waves were published and tracked directly in `docs/AI_TASK_BULLETIN_BOARD.md`. Do **not** claim work from this file merely because a lane description exists here. The Bulletin owns live READY/IN_PROGRESS/BLOCKED/DONE state and claim ownership; the Master Task Register owns task semantic scope.

These lanes use existing master-register tasks. They do not replace the ranked D-060 -> D-079 campaign.

## Historical parallel scheduling rule

At activation time, when the highest-ranked main-campaign task was already IN_PROGRESS by another agent, an unassigned agent could claim the highest-priority READY lane only after that lane was published as READY in the live Bulletin.

Parallel lanes are intentionally scoped to different authority/file families. Agents must stay inside their lane unless a required synchronization write is unavoidable.

After completion:
1. synchronize the existing master task;
2. append a Brag Card;
3. create or refresh the next evidence-backed task or lane;
4. release or unlock any dependent work;
5. claim a different eligible task.

## Lane P1 — D-021 Android consumer/test contract audit

**Priority:** P0 PARALLEL  
**Domain:** Android / player-safe projection / test mapping  
**Master task:** D-021  
**Status at activation:** existing task IN_PROGRESS; bulletin lane may be claimed independently of D-060.

### Scope
- continue exact current screen/component -> projection field -> engine owner -> action -> test/evidence mapping;
- close currently documented consumer/test-map gaps where this can be done by inspection/documentation;
- reconcile QuestSection, contentId, canonStatus, derived-stat, identity, activity/hierarchical-map/adversary future-consumer requirements;
- preserve Python/engine authority and hidden-state boundaries.

### Do not
- implement D-064 room/actor runtime projection;
- implement tactical Android runtime;
- redesign final UI;
- duplicate D-049 architecture work.

### Acceptance
- current consumer/test coverage map is materially deeper and exact-source-grounded;
- remaining implementation gaps are explicit and non-duplicative;
- D-021/D-026 records are synchronized where necessary.

### Bonus
Produce a machine-readable current screen -> field/action -> engine owner -> test-status matrix without changing runtime.

## Lane P2 — D-029 Asset provenance/reconstruction audit

**Priority:** P0 PARALLEL  
**Domain:** visual assets / provenance / reconstruction  
**Master task:** D-029

### Scope
- continue source-master -> raster/export -> branch/head -> runtime consumer -> reuse signature -> QA -> canonical-state tracing;
- reconcile remaining provenance gaps that do not require owner visual promotion decisions;
- improve reconstruction instructions for current asset families;
- use existing raster-verifier evidence accurately if now available.

### Do not
- generate, modify, regenerate, export, integrate, promote, replace or delete runtime assets;
- decide Service Tunnel/Quiet Stair owner visual choices;
- claim physical-device QA.

### Acceptance
- at least one real remaining provenance/reconstruction ambiguity is closed with exact evidence;
- family ledgers/registry remain internally consistent;
- owner-only visual choices remain clearly separated.

### Bonus
Create a concise "rebuild this asset family from zero" reconstruction checklist for one fully evidenced current family.

## Lane P3 — D-045 Evolved progression/classes design

**Priority:** P0 PARALLEL  
**Domain:** full-game progression / classes / professions / ranks  
**Master task:** D-045

### Scope
Continue the documented D-045 NEXT sequence:
1. combat class catalog;
2. profession/rank/status packet;
3. training/mentor/facility standard;
4. Gate Twelve proof packet;
5. progression UX contract.

Work one bounded semantic unit at a time. Preserve the current seven-attribute/23-skill foundation unless live evidence or authority says otherwise.

### Do not
- implement runtime progression;
- edit the D-046 ability/passive corpus except cross-reference links;
- invent canon world institutions where only proposals are allowed;
- override D-061 migration work.

### Acceptance
- one next D-045 child is reconstruction-grade, cross-referenced, and clearly separates CURRENT / TARGET / PROPOSAL;
- master/task/index direction is synchronized.

### Bonus
Add a dependency map showing how the new class/profession/rank unit consumes current skills, training, world facilities and future tactical roles.

## Lane P4 — D-046 Status / ability / passive Phase-C refinement

**Priority:** P0 PARALLEL  
**Domain:** abilities / passives / Status reconstruction corpus  
**Master task:** D-046

### Scope
Advance one current Phase-C gap:
- parent-system range/test fixtures and justified numeric envelopes;
- evidence-backed world/knowledge integration;
- unresolved state-owner/runtime projection mappings;
- normalization/canon-review preparation.

Use the existing 1,019-record Wave-001 corpus and existing 47/47, 23/23, 230/230 milestones; do not regenerate already-complete baseline work.

### Do not
- perform record-by-record canon promotion requiring owner approval;
- implement runtime abilities/passives;
- edit D-045 progression/class design except needed cross-references;
- invent hidden requirements to inflate corpus size.

### Acceptance
- one Phase-C blocker is materially reduced or closed with evidence;
- affected indexes/audits are synchronized;
- no false canon/runtime implication is introduced.

### Bonus
Add automated or machine-readable validation for one currently manual Phase-C consistency rule.

## Lane P5 — D-042 Cross-branch existing-state source audit

**Priority:** P0/P1 PARALLEL  
**Domain:** source archaeology / implementation evidence  
**Master task:** D-042

### Scope
- continue cross-branch reconciliation after the current-head source inventory;
- identify unique implementation behavior on historical/feature branches that is not yet classified as inherited, superseded, deferred, migration candidate, or irrelevant;
- map findings to current authorities/tasks without importing whole divergent architectures;
- prioritize evidence that affects final reconstruction or Phase 1.

### Do not
- merge, rebase, or promote branches;
- copy code merely because it exists on another branch;
- change current runtime during the audit;
- duplicate D-060 corpus inventory counting.

### Acceptance
- a bounded set of previously unresolved cross-branch source differences receives exact disposition and consumer/task mapping;
- D-042 evidence and any affected cross-reference/task records are updated.

### Bonus
Produce a machine-readable branch-survivor table for the audited slice: source branch/commit -> behavior -> current disposition -> migration consumer.

## Collision avoidance

Primary file-family ownership while these lanes run:

- P1 D-021: Android consumer/projection/test mapping docs.
- P2 D-029: asset provenance/evidence ledgers.
- P3 D-045: progression/classes/ranks design children.
- P4 D-046: Status/ability/passive corpus and audits.
- P5 D-042: source-audit/cross-branch evidence documents.

Shared files such as THE_GAME_MASTER_TASK_REGISTER.md, MASTER_DOCUMENTATION_RECORD.md, AI_TASK_BULLETIN_BOARD.md, and AI_BRAG_ROOM.md must always be re-fetched immediately before writes.


## Parallel Wave 2 — active-player unblock lanes

Authority: OR-035 + live Bulletin. The first five bounded lanes above are complete; their historical definitions remain for evidence. Wave 2 reuses unfinished Master Task Register work so active Player-AIs can make progress while D-072 is Silex-owned.

Use the live Bulletin entries P6-P10 for claim state. Detailed intent:
- **P6 / D-019 / Nodus-preferred:** exact-revision inventory refresh and counting-semantics reconciliation.
- **P7 / D-045 / Veyra-preferred:** profession/rank/status namespace packet, the explicit next D-045 child.
- **P8 / D-026 / Kestrel-preferred:** tactical player-safe projection/Android migration contract for the D-073 -> D-074 boundary, documentation only.
- **P9 / D-046 / Veyr-preferred:** one evidence-backed ability/passive world/knowledge/social/privacy Phase-C integration slice.
- **P10 / D-042 / Quorix-preferred:** bounded legacy-open-PR/historical-evidence disposition audit and reversible hygiene where evidence permits.

These lanes do not reserve work by specialty. Claim authority remains the live Bulletin. They must not modify Silex's D-072 implementation without an explicit review request.


## Parallel Wave 3 — completion continuity / blocker removal

Authority: OR-036 + live Bulletin.

Wave 2 is complete. Wave 3 consumes existing unfinished master work and one accepted CPR:
- **P11 / D-076 precondition / CPR-006 / Nodus-preferred:** Android session load validate-before-publish atomicity and state-owner repair.
- **P12 / D-045 / Veyra-preferred:** Training / Mentor / Facility Progression Standard.
- **P13 / D-026 / Kestrel-preferred:** hierarchical world-map player-safe projection migration contract.
- **P14 / D-046 / Veyr-preferred:** social qualification/public-reputation provenance and anti-repeat contract.
- **P15 / D-042 / Quorix-preferred:** exact disposition of open completed-task PRs #62/#57/#55/#45/#41.

Live claim state is owned by the Bulletin. D-072 remains Silex-owned; no Wave-3 lane may bypass D-073/D-074 dependencies.


## Parallel Wave 4 — post-Wave-3 continuation

Authority: OR-037 + live Bulletin.

After P12/P13/P14 completion:
- **P16 / D-045 / Veyra-preferred:** Gate Twelve Progression Proof Packet.
- **P17 / D-026 / Kestrel-preferred:** persistent-adversary intel player-safe projection migration contract.
- **P18 / D-046 / Veyr-preferred:** player-safe passive-list projection/privacy contract.

These lanes remain documentation/design only and do not overlap Nodus P11, Quorix P15, Silex D-072 or downstream D-073/D-074 implementation.
