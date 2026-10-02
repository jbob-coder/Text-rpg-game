# DOC_0000010 — Document Collision Prevention

Status: **REVIEWABLE**
Domain/program owner: D-07 Documentation / Coordination
Authority/evidence class: CONFIRMED_DOCUMENTED
Stable ID: DOC_0000010

Upstream: DOC_0000006; DOC_0000007; DOC_0000008; DOC_0000009; EXISTING::docs/production/GLOBAL_DOCUMENT_NAMESPACE.md; EXISTING::docs/production/SUBBATCH_STATUS_SCHEMA.md
Downstream: authoring automation, manifests, corpus QA, resume/checkpoint logic.

## Goal
Prevent ID collisions and path collisions.

## Mandatory pre-create checks
1. manifest reserves the ID;
2. ID belongs to the manifest range;
3. planned filename matches the manifest;
4. target path does not already exist;
5. no other corpus path already contains the same DOC ID;
6. ID is not retired/superseded and being reused improperly;
7. proposed ownership passes anti-filler review.

## Write rule
Create the file once on the intended working branch. Do not perform competing writes to the same path.

## Post-create checks
Read back the file; verify content ID against filename; verify path/range; confirm manifest purpose matches ownership; check references; update manifest status only after successful readback.

## Collision response
Stop issuance for the affected ID, do not overwrite automatically, inspect provenance, preserve already-issued IDs, repair the plan, and record a blocker when resolution is not immediate.

## Resume safety
A checkpoint records last verified ID, next ID, completed count, blocked count, and partial attempts. A resumed session reads that checkpoint before issuing more IDs.

## Acceptance
The work group has unique IDs, unique paths, successful readback, manifest alignment, and no unaccounted hole before the next ID.

## Revision trigger
Automated indexing or storage architecture creates a new collision domain.

## Next action
After DOC_0000001–DOC_0000010 verify successfully, update SB01_MANIFEST.md to last_verified_id DOC_0000010 and next_id DOC_0000011.