# Batch / Sub-batch Status Schema

Status: **ACTIVE / NORMATIVE**

## Manifest fields
batch_id, sub_batch_id, id_start, id_end, title, purpose, authority, status, created_at, last_updated, upstream, downstream, last_verified_id, next_id, blockers, open_decisions.

## File row fields
ID, filename, purpose, domain, status, upstream, downstream, evidence, notes.

## Normal lifecycle
`RESERVED -> PLANNED -> DRAFT -> STRUCTURED -> REVIEWABLE -> IMPLEMENTATION_READY -> VERIFIED_IMPLEMENTATION`

Exceptional states:
- BLOCKED
- SUPERSEDED
- RETIRED

Audit may move a document backward when evidence is incomplete.

## Checkpoint rule
After each work group update:
- last_verified_id
- next_id
- completed count
- blocked count
- files changed
- checks/tests
- unresolved issues

## Documentation verification
Check path existence, readback, ID/manifest match, required metadata where applicable, no duplicate ID, and reference validity where checkable. Documentation completion does not imply runtime implementation success.
