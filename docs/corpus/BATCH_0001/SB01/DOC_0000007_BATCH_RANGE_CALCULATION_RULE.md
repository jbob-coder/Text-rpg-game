# DOC_0000007 — Batch Range Calculation Rule

Status: **REVIEWABLE**
Domain/program owner: D-07 Documentation / Coordination
Authority/evidence class: CONFIRMED_DOCUMENTED
Stable ID: DOC_0000007

Upstream: DOC_0000004; EXISTING::docs/production/GLOBAL_DOCUMENT_NAMESPACE.md
Downstream: batch manifests, range validators, next-ID selection.

## Batch formula
For batch N, where 1 <= N <= 2000:
- batch_start = ((N - 1) * 1000) + 1
- batch_end = N * 1000

## Sub-batch formula
For sub-batch S, where 1 <= S <= 10:
- subbatch_start = batch_start + ((S - 1) * 100)
- subbatch_end = subbatch_start + 99

## Canonical examples
- BATCH_0001-SB01 = DOC_0000001–DOC_0000100
- BATCH_0001-SB10 = DOC_0000901–DOC_0001000
- BATCH_0002-SB01 = DOC_0001001–DOC_0001100
- BATCH_2000-SB10 = DOC_1999901–DOC_2000000

## Boundary checks
Each sub-batch must contain exactly 100 IDs, each batch exactly 1,000 IDs, adjacent ranges must not overlap, and no ID may fall outside DOC_0000001–DOC_2000000.

## Current evidence
BATCH_0001-SB01 is the proof range. A prior 101-entry planning error was detected before manifest finalization, so arithmetic validation remains mandatory.

## Acceptance
A manifest may enter authoring only after its range count is verified mathematically and entries map one-to-one to reserved IDs.

## Revision trigger
Only a change to the global file-count or batch-size mandate.

## Next action
Apply range validation to every future batch/sub-batch manifest.