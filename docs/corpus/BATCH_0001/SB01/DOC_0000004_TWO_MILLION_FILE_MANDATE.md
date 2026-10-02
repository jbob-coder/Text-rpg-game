# DOC_0000004 — Two-Million-File Mandate

Status: **REVIEWABLE**
Domain/program owner: D-07 Documentation / Coordination
Authority/evidence class: OWNER_DECISION
Stable ID: DOC_0000004

Upstream: DOC_0000001; EXISTING::docs/program/00_OWNER_DIRECTIVE_2026-10-02.md; EXISTING::docs/production/PRODUCTION_CONTROL_ARCHITECTURE.md
Downstream: global namespace, batch/sub-batch planning, scale testing, anti-filler enforcement.

## Decision
The long-horizon target is literally 2,000,000 separate documentation files using DOC_0000001 through DOC_2000000.

## Production decomposition
- 1 justified documentation unit = 1 file;
- 100 files = 1 sub-batch;
- 10 sub-batches = 1 batch of 1,000 files;
- 2,000 batches = 2,000,000 files.

## Boundary
The numeric target does not authorize filler, duplication, meaningless fragmentation, or invented facts.

## Current
The production-control layer exists and BATCH_0001-SB01 reserves DOC_0000001 through DOC_0000100. The remaining 1,999 batch allocations are intentionally not all locked.

## Target
Scale while preserving resumability, immutable IDs, dependency traceability, unique ownership, and measured repository/tooling performance.

## Risk
Two million physical files may stress Git index operations, checkout/clone, CI traversal, search, filesystem metadata, editors, and review tooling. These constraints must be measured rather than guessed.

## Acceptance
Every issued ID is manifest-backed and every created file passes anti-filler and documentation QA.

## Revision trigger
Only an explicit owner decision may change the target count or redefine separate file.

## Next action
Continue controlled sub-batch production and establish scale metrics before increasing throughput.