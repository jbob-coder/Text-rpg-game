# THE GAME — Injury / Scar Adaptation Passive Scaling & State Model 0001–0010

Status: **PHASE-C CALIBRATION / NOT CANON / NOT IMPLEMENTED**

Shared state:
`qualification_state`, `ownership_state`, `documented_injury_id`, `medical_stability_state`, `rehabilitation_plan_state`, `functional_limit_state`, `adaptation_state`, `projection_state`.

| ID | Effect input | Scaling direction | Hard cap |
|---|---|---|---|
| INJ_0001 | healed-scar mobility penalty | completed rehab history | active injury remains separate |
| INJ_0002 | gait inefficiency from stable limitation | reviewed adaptation history | no benefit beyond documented limitation |
| INJ_0003 | one-hand task penalty | practiced eligible tasks | no automatic skill transfer |
| INJ_0004 | self-recognition of known pain patterns | documented symptom history | no diagnosis creation |
| INJ_0005 | reinjury-risk movement habit | authorized rehab/practice | no invulnerability |
| INJ_0006 | cue-use inefficiency after visual limitation | documented adaptation practice | lost sensory input is not recreated |
| INJ_0007 | cue-use inefficiency after hearing limitation | documented adaptation practice | lost sensory input is not recreated |
| INJ_0008 | pacing inefficiency around stable respiratory limit | authorized adaptation history | underlying condition remains |
| INJ_0009 | missed familiar warning sensations | documented long-term injury history | novel symptoms remain uncertain |
| INJ_0010 | rehab-specific rebuilding inefficiency | authorized program history | no unlimited strength gain |

Qualification requires a documented injury, medical stability, legitimate rehabilitation sessions, stable event IDs, and explicit exclusion of reinjury farming.

Tests:
no benefit without matching documented limitation; no hidden diagnosis; no sensory restoration; no duplicate rehab credit; save/load exactness; hidden thresholds absent from normal projection.
