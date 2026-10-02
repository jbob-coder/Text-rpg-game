# Global Documentation Namespace

Status: **ACTIVE / NORMATIVE**
Authority: `OWNER_DECISION`

## Range
`DOC_0000001` … `DOC_2000000`.

## Batch arithmetic
For batch N (1–2000):
- start = `((N - 1) * 1000) + 1`
- end = `N * 1000`

For sub-batch S (1–10):
- start = `batch_start + ((S - 1) * 100)`
- end = `start + 99`

Examples:
- BATCH_0001-SB01 = DOC_0000001–DOC_0000100
- BATCH_0001-SB10 = DOC_0000901–DOC_0001000
- BATCH_0002-SB01 = DOC_0001001–DOC_0001100
- BATCH_2000-SB10 = DOC_1999901–DOC_2000000

## Paths
Corpus:
`docs/corpus/BATCH_NNNN/SBXX/DOC_NNNNNNN_SHORT_NAME.md`

Production control:
`docs/production/BATCH_NNNN/`

## Existing docs
Existing valid docs use `EXISTING::<path>` references until an explicit migration assigns a numbered document.

## Collision prevention
Before creating a numbered file:
1. verify manifest reservation;
2. verify path does not already exist;
3. verify ID is not already issued;
4. create once;
5. read back;
6. update manifest.

## Naming
Use uppercase snake-case ownership names. Avoid meaningless PART/NOTES labels.
