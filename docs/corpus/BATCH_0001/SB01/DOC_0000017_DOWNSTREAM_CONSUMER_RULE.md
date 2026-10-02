# DOC_0000017 — Downstream Consumer Rule

Status: **REVIEWABLE**
Domain/program owner: D-07 Documentation / Coordination
Authority/evidence class: CONFIRMED_DOCUMENTED
Stable ID: DOC_0000017

Upstream: DOC_0000015; DOC_0000016; EXISTING::docs/program/10_EXECUTION_COORDINATION_GRAPH.md
Downstream: domain plans, implementation tasks, tests, assets, migration plans.

## Rule
A downstream consumer is any document, system, asset, task, test, or migration unit whose behavior or interpretation depends on the current document.

## Required behavior
Substantive documents should identify known consumers when practical.
When a document changes materially, downstream consumers must be reviewed before claiming the change is integrated.

## Consumer categories
- document;
- world entity;
- system;
- implementation task;
- repository file;
- asset;
- test;
- migration;
- release evidence.

## Orphan warning
A document with no upstream and no downstream edge requires review; it may be valid, but it risks becoming disconnected documentation debt.

## Acceptance
Important decisions have at least one clear consumer or a documented reason for existing as standalone authority.

## Revision trigger
Change if graph semantics or consumer categories expand.

## Next action
Feed downstream relationships into future machine-readable indexing.