# DOC_0000012 — Evidence Classification Standard

Status: **REVIEWABLE**
Domain/program owner: D-07 Documentation / Coordination
Authority/evidence class: CONFIRMED_DOCUMENTED
Stable ID: DOC_0000012

Upstream: DOC_0000001; DOC_0000011; EXISTING::docs/program/01_DOCUMENTATION_PROGRAM_MASTER.md; EXISTING::docs/program/12_DOCUMENT_EXPECTATION_AND_ACCEPTANCE_STANDARD.md
Downstream: all domain documents, decisions, gap tracking, implementation verification.

## Allowed evidence classes
- CONFIRMED_IMPLEMENTED
- CONFIRMED_DOCUMENTED
- OWNER_DECISION
- PROPOSED
- EXTERNAL_REFERENCE_IDEA
- UNKNOWN
- CONFLICTING
- SUPERSEDED
- DEFERRED
- RETIRED

## Semantics
CONFIRMED_IMPLEMENTED requires observed repository/runtime evidence.
CONFIRMED_DOCUMENTED means the rule or design is explicitly recorded but may not be implemented.
OWNER_DECISION records explicit owner authority.
PROPOSED is not canon and does not become confirmed through repetition.
EXTERNAL_REFERENCE_IDEA is inspiration only.
UNKNOWN means evidence is insufficient.
CONFLICTING means active sources disagree and resolution is pending.
SUPERSEDED preserves old authority after replacement.
DEFERRED is intentionally postponed.
RETIRED is no longer active but remains traceable.

## Promotion rule
Promotion between classes requires new evidence or explicit authority; repetition is not promotion.

## Acceptance
Material claims in substantive documents can be mapped to an appropriate evidence class without ambiguity.

## Revision trigger
Change if program-wide evidence semantics change.

## Next action
Use these labels consistently in all later corpus and domain documents.