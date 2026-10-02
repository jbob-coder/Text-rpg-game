# DOC_0000019 — Document Revision Trigger Rule

Status: **REVIEWABLE**
Domain/program owner: D-07 Documentation / Coordination
Authority/evidence class: CONFIRMED_DOCUMENTED
Stable ID: DOC_0000019

Upstream: DOC_0000011; DOC_0000012; DOC_0000016; DOC_0000017; DOC_0000018
Downstream: every substantive numbered document, audit cadence, QA.

## Rule
Each substantive document should state the conditions that force it to be revisited.

## Common revision triggers
- upstream authority changes;
- runtime evidence contradicts documented behavior;
- owner decision supersedes current direction;
- implementation architecture changes;
- dependency/consumer graph changes materially;
- a previously UNKNOWN decision becomes resolved;
- a conflict is discovered;
- migration or save compatibility changes;
- acceptance criteria become invalid;
- external constraints materially change.

## Non-trigger
Cosmetic wording improvements do not necessarily require a status reset unless meaning or authority changes.

## Review action
When triggered: reassess evidence class, lifecycle status, dependencies, downstream consumers, and acceptance criteria.

## Acceptance
Every implementation-facing document exposes at least one clear revision trigger or explicitly states none beyond upstream change.

## Revision trigger
This rule changes only if the audit/revision model changes.

## Next action
Use revision triggers to drive future automated stale-document checks.