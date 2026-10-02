# DOC_0000001 — Program Authority Map

Status: **REVIEWABLE**
Domain/program owner: D-07 Documentation / Coordination
Authority/evidence class: OWNER_DECISION + CONFIRMED_DOCUMENTED
Stable ID: DOC_0000001
Scope: authority resolution for the Text Pixel RPG / THE GAME documentation and implementation program.

Upstream:
- EXISTING::docs/program/00_OWNER_DIRECTIVE_2026-10-02.md
- EXISTING::docs/program/01_DOCUMENTATION_PROGRAM_MASTER.md
- EXISTING::docs/program/09_DECISION_GAP_REGISTER.md
- EXISTING::docs/program/10_EXECUTION_COORDINATION_GRAPH.md
- EXISTING::docs/program/12_DOCUMENT_EXPECTATION_AND_ACCEPTANCE_STANDARD.md
- EXISTING::docs/program/16_SESSION_DECISION_LOG_2026-10-02.md
- EXISTING::docs/assets/GATE_TWELVE_REGION_MASTER_PLAN.md
- EXISTING::docs/production/PRODUCTION_CONTROL_ARCHITECTURE.md
- EXISTING::docs/production/GLOBAL_DOCUMENT_NAMESPACE.md
- EXISTING::docs/production/SUBBATCH_STATUS_SCHEMA.md
- EXISTING::docs/production/EXISTING_DOCUMENT_MAPPING_REGISTER.md

Downstream consumers: every numbered corpus document, domain programs D-01 through D-07, implementation tasks, QA/test evidence, migration/rebuild decisions, and future session handoffs.

## 1. Ownership
This document owns the active authority chain used to decide which source controls when project statements conflict.
It does not own gameplay formulas, world geography, art specifications, APK architecture, or content details.

## 2. Active authority chain
Use this order when evidence conflicts:
1. current repository state on the exact active branch/ref;
2. freshly executed build/test/runtime evidence;
3. explicit owner decisions recorded in active repository documentation;
4. active normative program/control documents;
5. current domain specifications and pilot documents;
6. historical plans still mapped as useful evidence;
7. external references;
8. chat memory or informal recollection.

A lower tier may add context but may not silently override a higher tier.

## 3. Conflict resolution
When active repository documents conflict: compare status/evidence class; identify explicit supersession; check the decision-gap register; preserve useful history; mark losing statements SUPERSEDED, CONFLICTING, or DEFERRED; then update downstream pointers.
Fresh observed runtime evidence overrides documentation that claims behavior the runtime no longer exhibits.

## 4. Current
- jbob-coder/Text-rpg-game is the priority repository.
- Documentation-first development is active.
- Gate Twelve is the current pilot, not the complete world.
- The numbered corpus is controlled by the production architecture and manifests.
- Existing documentation may be updated, rewritten, superseded, merged, or retired when justified.
- Application systems may be reworked/rebuilt when migration and verification are documented.

## 5. Target
Trace meaningful work as: Owner Decision -> Program Authority -> Domain Spec -> Implementation Task -> Test -> Observed Evidence.

## 6. Delta
Still incomplete: stale repository pointers, broad world/system decisions, the machine-readable cross-document index, and the final APK teardown/rebuild matrix.

## 7. Migration
When authority changes: preserve the prior source, record supersession, update indexes/consumers, preserve immutable DOC IDs, and do not claim implementation changed until code/runtime evidence exists.

## 8. Acceptance
Passes when upstream files exist, no higher-authority source contradicts the chain, future documents use explicit authority/evidence labels, and session resume does not require chat memory.

## 9. Revision triggers
Revise if repository priority, authority order, evidence rules, or governance model changes.

## 10. Unknowns
The final machine-readable graph representation remains undecided.

## 11. Next action
Use this map as the parent governance reference for the remainder of BATCH_0001-SB01.