# DOC_0000020 — Document Acceptance Gate

Status: **REVIEWABLE**
Domain/program owner: D-07 Documentation / Coordination
Authority/evidence class: CONFIRMED_DOCUMENTED
Stable ID: DOC_0000020

Upstream: DOC_0000011; DOC_0000012; DOC_0000013; DOC_0000014; DOC_0000015; DOC_0000016; DOC_0000017; DOC_0000019; EXISTING::docs/program/12_DOCUMENT_EXPECTATION_AND_ACCEPTANCE_STANDARD.md
Downstream: all corpus QA, manifest completion, sub-batch completion gates.

## Gate
A substantive numbered document is not accepted merely because a file exists.

## Minimum acceptance checks
- scope/ownership is explicit;
- authority/evidence class is explicit;
- current versus target is separated when applicable;
- confirmed versus proposed is separated;
- unknowns/conflicts are visible;
- upstream dependencies are identified;
- downstream consumers are identified where practical;
- stable IDs and terms are consistent;
- affected assets/systems/content are identified when applicable;
- migration is addressed when current behavior changes;
- verification/acceptance exists;
- revision trigger exists;
- next action is explicit;
- external reference material is not treated as canon without a decision;
- no stale statement silently contradicts newer active authority.

## Status outcome
Passing this gate normally permits REVIEWABLE. IMPLEMENTATION_READY requires additional domain-specific implementation completeness. VERIFIED_IMPLEMENTATION requires observed evidence.

## Failure behavior
If the gate fails, move the document backward to DRAFT or STRUCTURED, or mark BLOCKED if a missing dependency prevents completion.

## Acceptance
QA can evaluate the document using this checklist without interpreting hidden intent.

## Revision trigger
Change when the normative documentation acceptance standard changes.

## Next action
Use this gate on DOC_0000001–DOC_0000100 before sub-batch completion.