# THE GAME — Technical / Craft Passive Scaling & State Model 0001–0010

Status: **PHASE-C CALIBRATION / NOT CANON / NOT IMPLEMENTED**

Purpose: define bounded scaling and authoritative state categories for `PASSIVE_TEC_0001`–`PASSIVE_TEC_0010`.

## Shared state

Future implementation should distinguish:
- `qualification_state`;
- `ownership_state`;
- `tool_identity`;
- `tool_familiarity_state`;
- `technical_task_state`;
- `procedure_state`;
- `material_observation_state`;
- `diagnostic_evidence_state`;
- `quality_review_state`;
- `projection_state`.

## Per-record model

| ID | Effect input | Scaling direction | Hard cap |
|---|---|---|---|
| TEC_0001 | tool setup/reorientation overhead | repeated validated use of same/related tools | unfamiliar tools receive limited/no benefit |
| TEC_0002 | fine-motor execution variance | reviewed precision-task history | cannot exceed physical/tool precision limits |
| TEC_0003 | diagnostic-sequence omission/error | verified diagnostic task history | no automatic correct diagnosis |
| TEC_0004 | failure-signature recognition burden | confirmed prior failure encounters | novel failures remain uncertain |
| TEC_0005 | familiar-material discrimination error | confirmed inspection history | no hidden composition revelation |
| TEC_0006 | avoidable consumable waste | familiar repair history with quality review | cannot create missing parts/materials |
| TEC_0007 | assembly error from routine handling | validated assembly/cleanliness practice | design defects and bad parts remain possible |
| TEC_0008 | temporary-repair reliability | varied valid field-repair experience | unsuitable materials remain unsuitable |
| TEC_0009 | Focus loss during long calibration | legitimate calibration history | no free Focus or instant calibration |
| TEC_0010 | workshop-procedure adherence error | sustained reviewed workshop practice | unfamiliar facilities/protocols receive reduced/no benefit |

## Qualification rules

The compact records require:
- technical tasks;
- verified repairs/outputs;
- quality review.

Future qualification must:
1. use stable task/output IDs;
2. count valid output once;
3. require quality review where specified;
4. reject trivial repetitive setup loops;
5. distinguish task completion from successful quality;
6. keep hidden progress out of ordinary Status projection.

## Cross-family overlap watchlist

- Tool Memory ↔ Procedural Chunking;
- Fine Motor Calibration ↔ weapon/medical precision passives;
- Diagnostic Habit ↔ Analytical Habit;
- Failure Pattern Library ↔ Error Memory;
- Material Sense ↔ sensory/crafting knowledge;
- Repair Economy ↔ profession/logistics passives;
- Calibration Patience ↔ Patience Engine / Cognitive Endurance;
- Workshop Discipline ↔ profession/faction institutional routines.

Same-resolver effects use one capped composition path.

## Required tests

- unfamiliar tools/materials do not receive unjustified full familiarity;
- diagnostic outputs remain evidence-based and uncertain where appropriate;
- duplicate task/output IDs do not double-count;
- low-quality outputs cannot satisfy a quality gate merely by completion;
- no passive fabricates materials, parts, or technical facts;
- save/load preserves qualification and ownership exactly once;
- player-safe projection omits hidden thresholds.

No runtime module is claimed here.
