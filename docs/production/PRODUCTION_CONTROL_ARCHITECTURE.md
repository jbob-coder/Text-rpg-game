# Documentation Production Control Architecture

Status: **ACTIVE / NORMATIVE**
Repository: `jbob-coder/Text-rpg-game`
Authority class: `OWNER_DECISION + CONFIRMED_DOCUMENTED`
Program owner: Documentation / Coordination

## Purpose
Control production of the owner's long-horizon target of **2,000,000 separate documentation files** without losing authority, traceability, resumability, or quality. This control layer coordinates existing domain documents; it does not duplicate them.

## Production hierarchy
- 1 file = one justified documentation unit.
- 100 files = one sub-batch.
- 10 sub-batches = one 1,000-file batch.
- 2,000 batches = 2,000,000 files.
- Global namespace: `DOC_0000001` through `DOC_2000000`.

## Anti-filler
A numbered file must have a unique ownership role: authority, requirement, decision, schema, entity, system, guide, migration, test/verification contract, risk, evidence, content record, asset record, world record, or implementation handoff. A file with no unique ownership is not created.

## Existing documentation
Existing useful documents are mapped, linked, and classified as KEEP / UPDATE / REWRITE / SUPERSEDE / MERGE / DELETE. They are not copied into the numbered corpus merely to raise file count.

## Immutable IDs
Assigned IDs are never reused. Renaming does not change the ID. Retired/superseded IDs remain reserved forever.

## Naming
`DOC_NNNNNNN_SHORT_NAME.md`

## Status
RESERVED, PLANNED, DRAFT, STRUCTURED, REVIEWABLE, IMPLEMENTATION_READY, VERIFIED_IMPLEMENTATION, BLOCKED, SUPERSEDED, RETIRED.

## Dependency edges
depends_on, constrains, supersedes, references, specifies, implemented_by, verified_by, consumed_by, blocks, belongs_to.

## Resume/checkpoint
Each sub-batch manifest records exact range, plan, completed/blocked files, last verified ID, next ID, dependencies, unresolved decisions, files changed, and verification performed. A future session resumes from the manifest, not chat memory.

## Sub-batch completion
A 100-file sub-batch completes only when every ID is accounted for, no duplicates/skips exist, created docs pass documentation QA, references are checked, relevant gap/coverage registers are updated, and a handoff identifies the next sub-batch.

## Scale risk
Two million physical files create real Git/filesystem/search/CI risks. Scale-up is empirical. Periodically measure repository size, checkout/index/search performance, CI traversal cost, and tooling compatibility. Operational problems must be documented before changing the owner's file-count requirement.

## First proof
`BATCH_0001-SB01 = DOC_0000001–DOC_0000100`.
Its manifest is `docs/production/BATCH_0001/SB01_MANIFEST.md`.
