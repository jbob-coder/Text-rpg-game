# THE GAME — Unique Event Passive State Model 0001–0010

Status: **PHASE-C CALIBRATION / NOT CANON / NOT IMPLEMENTED**

Shared state:
`qualification_state`, `ownership_state`, `unique_event_id`, `participant_or_witness_state`, `event_outcome_state`, `event_signature_state`, `knowledge_state`, `projection_state`.

Rules:
1. one authored event ID is the qualification authority;
2. duplicate credit is impossible;
3. participation/witness/survival requirements are record-specific;
4. save/load preserves the one-time event completion exactly;
5. deleting/replaying a scene does not generate a second qualification;
6. effects match documented event cues only;
7. no event is canon merely because a placeholder `authored_event_XX` exists.

| ID range | State emphasis | Hard cap |
|---|---|---|
| UEV_0001–0003 | survivor/context recognition | no general trauma/combat immunity |
| UEV_0004–0005 | environmental/system event cues | no universal gateway/storm immunity |
| UEV_0006 | structural emergency pattern | no guaranteed escape |
| UEV_0007–0008 | witnessed exceptional event pattern | no hidden future-event prediction |
| UEV_0009 | expedition-risk pattern | no omniscient exploration knowledge |
| UEV_0010 | one cosmic/system signature | no general cosmic perception |

Required tests: event-ID uniqueness, duplicate prevention, participant/witness validation, save/load persistence, hidden-event data filtering, and placeholder-not-canon enforcement.
