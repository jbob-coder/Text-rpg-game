# THE GAME — Resistance Passive Scaling & State Model 0001–0010

Status: **PHASE-C CALIBRATION / NOT CANON / NOT IMPLEMENTED**

Shared state:
`qualification_state`, `ownership_state`, `hazard_type`, `exposure_state`, `adaptation_state`, `recovery_state`, `injury_state`, `projection_state`.

| ID | Effect input | Scaling direction | Hard cap |
|---|---|---|---|
| RES_0001 | bounded heat penalty | safe heat-adaptation history | severe heat remains dangerous |
| RES_0002 | bounded cold penalty | safe cold-adaptation history | severe cold remains dangerous |
| RES_0003 | low-level electrical disruption | legitimate conditioning history | no high-energy immunity |
| RES_0004 | pressure-change impairment | trained pressure exposure | no unsafe pressure immunity |
| RES_0005 | one toxin-family effect | documented family-specific adaptation | no cross-family universal resistance |
| RES_0006 | loud-noise impairment | safe acoustic adaptation | hearing injury remains possible |
| RES_0007 | flash recovery burden | valid visual recovery history | injury thresholds remain |
| RES_0008 | familiar fear disruption | reviewed legitimate exposure | threat awareness remains |
| RES_0009 | ordinary fatigue performance penalty | long conditioning history | recovery remains mandatory |
| RES_0010 | reorientation burden | familiar non-injury motion history | injury/neurological conditions remain separate |

Qualification requires safe/controlled exposure, recovery, stable event IDs, no duplicate credit, and hidden progress.

Required tests:
- type specificity;
- no immunity drift;
- no duplicate exposure credit;
- safe-limit requirements enforced;
- save/load exactness;
- hidden thresholds absent from player-safe projection.
