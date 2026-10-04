# THE GAME — Profession Passive Scaling & State Model 0001–0010

Status: **PHASE-C CALIBRATION / NOT CANON / NOT IMPLEMENTED**

Shared state:
`qualification_state`, `ownership_state`, `profession_id`, `work_shift_state`, `task_familiarity`, `competency_review_state`, `workplace_context`, `projection_state`.

| ID | Effect input | Scaling direction | Hard cap |
|---|---|---|---|
| PRO_0001 | long-shift performance decay | legitimate shift history | rest needs remain |
| PRO_0002 | pacing inefficiency | repeated professional task history | no infinite throughput |
| PRO_0003 | explicit-cue interpretation | reviewed client interaction history | no mind reading |
| PRO_0004 | route/location recall burden | repeated work-route use | unknown routes remain unknown |
| PRO_0005 | routine inventory error | reviewed inventory work | missing stock is not created |
| PRO_0006 | safety-procedure omission | validated workplace practice | procedure cannot prevent every hazard |
| PRO_0007 | routine negotiation inconsistency | professional negotiation history | no automatic agreement |
| PRO_0008 | documentation omission | recurring reviewed documentation | bad source data remains bad |
| PRO_0009 | issued-equipment tracking error | accountable work history | no remote item detection |
| PRO_0010 | distraction during familiar duty | sustained role-specific practice | unrelated duties receive limited/no benefit |

Qualification requires profession shifts, competency review, repeated relevant tasks, stable event IDs, no duplicate credit, and hidden progress.

Tests: profession specificity, no authority fabrication, no resource creation, competency review enforcement, save/load exactness, player-safe projection filtering.
