# THE GAME — Defensive Adaptation Passive Scaling & State Model 0001–0010

Status: **PHASE-C CALIBRATION / NOT CANON / NOT IMPLEMENTED**

Purpose: define bounded scaling and authoritative state categories for `PASSIVE_DEF_0001`–`PASSIVE_DEF_0010`.

## Shared state

Future implementation should distinguish:
- `qualification_state`;
- `ownership_state`;
- `defensive_event_context`;
- `recognized_threat_state`;
- `guard_state`;
- `balance_state`;
- `cover_state`;
- `equipment_state`;
- `protected_target_state`;
- `projection_state`.

## Per-record model

| ID | Effect input | Scaling direction | Hard cap |
|---|---|---|---|
| DEF_0001 | avoidable reaction disruption | validated controlled exposure/history | cannot remove all disruption |
| DEF_0002 | time/overhead to enter practiced brace | successful anticipated-response history | no benefit without recognized cue |
| DEF_0003 | cover-choice overhead/error | reviewed cover-selection history | only known nearby cover can be selected |
| DEF_0004 | alignment error against known direction | validated directional-response practice | no immunity to underlying force |
| DEF_0005 | guard-form degradation | repeated successful guarded actions | guard can still fail |
| DEF_0006 | post-evasion recovery overhead | valid trained evasion history | does not create free movement/actions |
| DEF_0007 | balance-loss component of survivable impact | validated recovery history | underlying damage remains unchanged |
| DEF_0008 | practiced shield handling overhead | equipment-specific familiarity | no benefit without valid shield system |
| DEF_0009 | protective posture response after recognized cue | reviewed cue-response history | no blast immunity |
| DEF_0010 | positioning error relative to a protected ally | validated escort/protection history | does not redirect danger automatically |

## Qualification rules

The compact records currently require:
- meaningful defensive events;
- correct-response performance;
- exclusion of reckless farming.

Future qualification must:
1. use stable event IDs;
2. count each event once;
3. reject trivial/repeated staged loops;
4. preserve hidden progress;
5. separate actual outcome from the quality of the defensive decision.

## Cross-family overlap watchlist

- Flinch Control ↔ Mental/Will stress passives;
- Brace Reflex ↔ Physical Core Bracing;
- Cover Instinct ↔ Sensory/Crisis Clarity;
- Guard Integrity ↔ combat skill and equipment durability;
- Evasion Recovery ↔ Movement family;
- Stagger Resistance ↔ Physical balance/joint passives;
- Shield Habit ↔ Weapon Familiarity;
- Protective Positioning ↔ Leadership/coordination.

Same-resolver effects use one capped composition path.

## Required tests

- hidden threat information is never created;
- damage/injury stays authoritative;
- duplicate event IDs do not advance qualification twice;
- successful decision and successful outcome are tracked separately where needed;
- equipment-specific effects require compatible equipment;
- save/load preserves ownership/progress exactly once;
- normal Status projection omits hidden qualification thresholds.

No runtime module is claimed here.
