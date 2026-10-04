# THE GAME — Cognitive Passive Scaling & State Model 0001–0010

Status: **PHASE-C CALIBRATION / NOT CANON / NOT IMPLEMENTED**

Purpose: define state ownership and hard boundaries for PASSIVE_COG_0001 through PASSIVE_COG_0010.

## Shared state
Future implementation should separate `qualification_state`, `ownership_state`, `study_context`, `domain_familiarity`, `knowledge_provenance`, `practice_history`, `error_review_state`, `mentor_instruction_state`, and player-safe `projection_state`.

## Per-record model

| ID | Effect input | Scaling direction | Hard cap |
|---|---|---|---|
| COG_0001 | pattern-recognition burden | repeated valid domain exposure | no facts from absent evidence |
| COG_0002 | unfamiliarity penalty | related-task exposure | no skipped prerequisite |
| COG_0003 | reviewed-correction retention | verified correction history | no guaranteed future success |
| COG_0004 | transfer friction | approved shared-principle history | unrelated domains receive none |
| COG_0005 | retrieval burden | deliberate study/reinforcement | no information never acquired |
| COG_0006 | procedure transition overhead | valid routine practice | required steps remain required |
| COG_0007 | assumption-check consistency | reviewed analytical work | no automatic truth discovery |
| COG_0008 | study restart Focus cost | continuity in one valid program | no permanent zero-cost restart |
| COG_0009 | instruction retention | qualified instruction plus practice | no copying full instructor skill |
| COG_0010 | theory/application integration | confirmed field application | uncertain observations stay uncertain |

## Global rules
- Level does not directly scale these passives by default.
- Raw Intellect, skill values, knowledge, familiarity, and passive modifiers remain separate.
- Cross-domain transfer requires an explicit relationship record.
- Same-resolver bonuses use capped composition.
- Duplicate ownership does not stack.
- Hidden progress remains absent from ordinary player projection.
- Exact numeric coefficients remain TBD.

## Required tests
- unrelated domains receive no transfer;
- absent knowledge is not fabricated;
- invalid/trivial study does not advance hidden qualification;
- mentor benefit requires both valid instruction and practice;
- save/load does not duplicate qualification evidence;
- study restart benefits respect continuity windows;
- UI does not reveal hidden thresholds.

No runtime module is claimed here.