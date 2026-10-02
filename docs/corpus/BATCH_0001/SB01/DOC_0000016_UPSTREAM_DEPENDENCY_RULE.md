# DOC_0000016 — Upstream Dependency Rule

Status: **REVIEWABLE**
Domain/program owner: D-07 Documentation / Coordination
Authority/evidence class: CONFIRMED_DOCUMENTED
Stable ID: DOC_0000016

Upstream: DOC_0000001; DOC_0000013; DOC_0000015; EXISTING::docs/program/10_EXECUTION_COORDINATION_GRAPH.md
Downstream: all documents declaring upstream constraints.

## Rule
An upstream dependency is a source whose authority, decision, schema, or contract constrains the current document.

## Required behavior
- list material upstream documents;
- use stable DOC IDs for numbered corpus sources;
- use EXISTING::<path> for pre-corpus sources;
- do not cite chat memory as authoritative upstream;
- if an upstream source is superseded, review downstream consumers.

## Missing upstream
If required authority is missing, mark the document BLOCKED or explicitly PROPOSED rather than inventing a dependency.

## Change propagation
When an upstream changes materially, all known downstream consumers must be reviewed for stale assumptions.

## Acceptance
Every material rule in a document can be traced to its upstream authority or identified as a new explicit decision/proposal.

## Revision trigger
Change if dependency semantics or reference syntax changes.

## Next action
Use this rule in graph and stale-reference audits.