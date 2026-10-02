# DOC_0000015 — Document Scope Boundary Rule

Status: **REVIEWABLE**
Domain/program owner: D-07 Documentation / Coordination
Authority/evidence class: CONFIRMED_DOCUMENTED
Stable ID: DOC_0000015

Upstream: DOC_0000013; DOC_0000014
Downstream: all corpus documents, domain decomposition, cross-document graph.

## Rule
Each document must define what it owns and what it explicitly does not own.

## Boundary principle
A file may reference adjacent systems without becoming their source of truth.
Example: a combat document may reference inventory costs, but inventory ownership remains with economy/items documentation unless explicitly migrated.

## Split criteria
Split scope when ownership, state owner, implementation consumer, revision trigger, or verification path materially differs.

## Merge criteria
Merge scopes when separation creates circular repetition without independent ownership.

## Conflict rule
If two active documents claim the same authority, classify the overlap as CONFLICTING and resolve it explicitly; do not let both remain silently canonical.

## Acceptance
Another developer can state in one sentence what this file controls and what it delegates.

## Revision trigger
Change when system ownership boundaries are re-architected.

## Next action
Use scope boundaries as graph edges in later cross-document indexing.