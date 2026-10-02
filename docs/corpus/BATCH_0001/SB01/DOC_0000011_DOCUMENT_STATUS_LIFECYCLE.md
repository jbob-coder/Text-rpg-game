# DOC_0000011 — Document Status Lifecycle

Status: **REVIEWABLE**
Domain/program owner: D-07 Documentation / Coordination
Authority/evidence class: CONFIRMED_DOCUMENTED
Stable ID: DOC_0000011

Upstream: DOC_0000001; DOC_0000005; DOC_0000010; EXISTING::docs/production/SUBBATCH_STATUS_SCHEMA.md
Downstream: every numbered corpus document, manifests, QA, checkpoint logic.

## Ownership
This document owns the valid lifecycle states of numbered documentation and the allowed meaning of each state.
It does not define gameplay or implementation lifecycle states.

## Normal lifecycle
RESERVED -> PLANNED -> DRAFT -> STRUCTURED -> REVIEWABLE -> IMPLEMENTATION_READY -> VERIFIED_IMPLEMENTATION

## Exceptional states
- BLOCKED: work cannot progress without an unresolved dependency or decision.
- SUPERSEDED: a newer authority replaces the document while the old record remains preserved.
- RETIRED: the document remains historically traceable but is no longer active.

## Transition rules
- RESERVED means only an ID/range allocation exists.
- PLANNED means filename, purpose, and ownership are defined in a manifest.
- DRAFT means substantive authoring has started but required sections are incomplete.
- STRUCTURED means required sections exist but evidence/decisions may still be incomplete.
- REVIEWABLE means scope, authority, current/target/delta, unknowns, dependencies, and acceptance are clear enough for review.
- IMPLEMENTATION_READY means a developer can implement the owned scope without guessing material rules.
- VERIFIED_IMPLEMENTATION requires matching observed implementation evidence; documentation alone cannot grant it.

## Backward movement
QA may move a document backward if evidence becomes incomplete, conflicts appear, or a previously assumed dependency changes.

## Acceptance
Every manifest row must use one of these states and its status must match the actual document quality.

## Revision trigger
Change only if the program adopts a new documentation lifecycle model.

## Next action
Apply the lifecycle consistently to SB01 and future manifests.