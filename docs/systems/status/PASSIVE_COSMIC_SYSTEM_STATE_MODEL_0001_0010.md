# THE GAME — Cosmic / System Passive State Model 0001–0010

Status: **PHASE-C CALIBRATION / NOT CANON / NOT IMPLEMENTED**

Shared state:
`qualification_state`, `ownership_state`, `system_event_id`, `status_confirmation_state`, `known_prompt_state`, `system_signature_state`, `system_anomaly_state`, `projection_state`.

Rules:
- qualification requires an authored system event plus Status confirmation;
- hidden content remains hidden;
- recognition is not repair/control authority;
- system event IDs cannot be farmed or duplicated;
- public projection never reconstructs hidden system state from the passive;
- save/load preserves event qualification exactly once.

| ID range | Main state | Hard cap |
|---|---|---|
| COS_0001–0002 | visible Status/prompt interpretation | hidden contents remain hidden |
| COS_0003–0004 | response to abnormal system/Level events | no immunity to consequences |
| COS_0005–0007 | discrepancy/revelation/threshold recognition | no automatic secret-data reveal |
| COS_0008 | anomaly recognition | no repair/admin authority |
| COS_0009–0010 | specific system/cosmic signatures | no universal cosmic sensitivity |

Required tests: hidden-data non-leakage, event-ID uniqueness, Status-confirmation validation, save/load exactness, no admin escalation, and Witness placeholder isolation.
