# DOC_0000006 — Global ID Immutability Rule

Status: **REVIEWABLE**
Domain/program owner: D-07 Documentation / Coordination
Authority/evidence class: CONFIRMED_DOCUMENTED
Stable ID: DOC_0000006

Upstream: DOC_0000004; EXISTING::docs/production/GLOBAL_DOCUMENT_NAMESPACE.md; EXISTING::docs/production/PRODUCTION_CONTROL_ARCHITECTURE.md
Downstream: all manifests, supersession/retirement rules, reference validation, migration tooling.

## Rule
Once a DOC_NNNNNNN ID is issued, it is permanent and may never be reassigned to a different documentation unit.
Renaming a file does not change its stable ID.

## Lifecycle behavior
An ID may become active, superseded, retired, or tombstoned after controlled deletion. It never returns to the free pool.

## Rename rule
If ownership remains the same but the short name improves: keep the ID, update the filename and references, and preserve rename history where practical.

## Supersession rule
If a new document replaces an older authority: issue a new ID for the new ownership unit, mark the old ID SUPERSEDED, link the relationship, and preserve historical traceability.

## Prohibited behavior
- recycling retired IDs;
- changing IDs merely to close numbering gaps;
- using one ID in multiple files;
- silently repurposing an existing ID.

## Acceptance
One ID maps to at most one active ownership record; manifest and filename agree; retired and superseded IDs remain reserved.

## Revision trigger
Only a formal governance change to the global namespace.

## Next action
Use this rule in collision checks and corpus audits.