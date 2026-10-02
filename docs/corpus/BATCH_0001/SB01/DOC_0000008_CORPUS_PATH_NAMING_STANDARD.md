# DOC_0000008 — Corpus Path and Naming Standard

Status: **REVIEWABLE**
Domain/program owner: D-07 Documentation / Coordination
Authority/evidence class: CONFIRMED_DOCUMENTED
Stable ID: DOC_0000008

Upstream: DOC_0000006; DOC_0000007; EXISTING::docs/production/GLOBAL_DOCUMENT_NAMESPACE.md
Downstream: all numbered files, manifest generators, reference validators.

## Canonical path
docs/corpus/BATCH_NNNN/SBXX/DOC_NNNNNNN_SHORT_NAME.md

## Naming grammar
- batch: four digits, e.g. BATCH_0001;
- sub-batch: two digits, e.g. SB01;
- document ID: seven digits, e.g. DOC_0000008;
- short name: uppercase snake case;
- default extension: .md unless another corpus class is formally introduced.

## Short-name rule
The short name describes ownership, not sequence. Prefer PROGRAM_AUTHORITY_MAP over PART_1, NOTES, MISC, or MORE_INFO.

## Path ownership
The path encodes production allocation, not domain canon. Reclassification of domain does not permit changing an immutable DOC ID.

## Rename behavior
Preserve the ID, update the filename and manifest, update inbound references, and verify no duplicate path exists.

## Acceptance
ID, filename, path, batch range, sub-batch range, and manifest row all agree.

## Revision trigger
Corpus storage layout changes or a formally supported new file format is introduced.

## Next action
Apply this standard to every numbered file in BATCH_0001-SB01.