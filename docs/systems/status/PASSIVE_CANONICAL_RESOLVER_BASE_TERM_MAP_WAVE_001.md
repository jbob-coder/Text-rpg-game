# THE GAME — Passive Canonical Resolver Base-Term Map — Wave 001

Status: **PHASE-C NUMERIC PREPARATION / BASE TERMS IDENTIFIED / VALUES TBD / NOT CANON / NOT IMPLEMENTED**

Parents:
- `PASSIVE_SHARED_RESOLVER_CAP_SEMANTICS_WAVE_001.md`
- `STATUS_BASE_RESOLUTION_TERM_UNIT_TAXONOMY.md`

Purpose: identify the underlying base term and abstract unit class required by each of the 20 canonical shared passive resolver families.

| Resolver | Base term that must exist | Unit class | Required upstream system | Numeric blocker |
|---|---|---|---|---|
| RESOLVER_KNOWN_INFORMATION_RECALL | retrieval burden/error for one already-acquired datum | ERROR_BURDEN | knowledge provenance + recall model | final recall resolution model |
| RESOLVER_AUDITORY_SOURCE_SEPARATION | source-separation error for available auditory input | ERROR_BURDEN / INTERPRETATION_CONFIDENCE | sensory signal model | signal/noise and confidence scale |
| RESOLVER_ENGAGEMENT_DISTANCE_JUDGMENT | spacing-estimation error for observed target/equipment geometry | ERROR_BURDEN / DISTANCE | spatial + equipment reach model | world distance unit and error model |
| RESOLVER_IMMEDIATE_THREAT_PRIORITIZATION | prioritization error/burden across already recognized threats | ERROR_BURDEN | threat observation + decision model | decision difficulty model |
| RESOLVER_PROCEDURE_COMPLIANCE_ERROR | omission/error burden for one known authorized procedure step/check | ERROR_BURDEN | procedure/version/authorization model | procedural error resolution |
| RESOLVER_PROLONGED_FOCUS_DRAIN | base Focus loss over eligible sustained task interval | RESOURCE_RATE | Focus + authoritative time/task windows | Focus scale and time unit |
| RESOLVER_PRACTICED_PROCEDURE_OVERHEAD | avoidable setup/transition burden inside a practiced procedure | PROCEDURE_OVERHEAD / TIME_INTERVAL | procedure/action model | action timing representation |
| RESOLVER_ANALYTICAL_CHECK_DISCIPLINE | avoidable analytical-check omission/error burden | ERROR_BURDEN | evidence/decision model | analytical resolution model |
| RESOLVER_SYSTEM_ANOMALY_RECOGNITION | recognition error for legitimately observable Status/system anomaly | ERROR_BURDEN / INTERPRETATION_CONFIDENCE | Status event/evidence model | confidence and anomaly-observation model |
| RESOLVER_EQUIPMENT_RETENTION | base handling contribution to a valid retention contest | CONTEST_MODIFIER | equipment + action contest model | contest scale |
| RESOLVER_COMMAND_STRUCTURE_FAMILIARITY | procedural error burden inside a known command workflow | ERROR_BURDEN | institution/role/protocol model | institutional procedure resolver |
| RESOLVER_FINE_MOTOR_STEADINESS | execution variance around a valid precision action | EXECUTION_VARIANCE | physical action/tool model | precision/variance representation |
| RESOLVER_TRAVEL_EFFICIENCY | avoidable cost/pace inefficiency over travel interval | DIMENSIONLESS_PENALTY / RESOURCE_RATE | movement/travel/environment model | distance, time, stamina travel model |
| RESOLVER_FATIGUE_PERFORMANCE_DECAY | performance penalty produced by eligible accumulated fatigue | PERFORMANCE_DECAY | exertion/fatigue model | fatigue accumulation and recovery model |
| RESOLVER_OBSERVED_AUDIENCE_CLIENT_CUE_INTERPRETATION | interpretation error for available social/group cues | ERROR_BURDEN / INTERPRETATION_CONFIDENCE | social observation/evidence model | social cue/confidence resolver |
| RESOLVER_STAMINA_RECOVERY_OPPORTUNITY | base Stamina restored during one valid recovery transaction | RECOVERY_EFFECT / RESOURCE_AMOUNT | Stamina + recovery-window model | Stamina scale and recovery rates |
| RESOLVER_SLEEP_RESTORATION | base resource/state restoration from one valid adequate-sleep interval | RECOVERY_EFFECT / RESOURCE_AMOUNT | sleep/rest + resource recovery model | sleep quality/duration and resource scales |
| RESOLVER_HEAT_PERFORMANCE_PENALTY | non-injury performance penalty from current heat exposure | DIMENSIONLESS_PENALTY | environment/temperature/exposure model | heat bands and performance curve |
| RESOLVER_COLD_PERFORMANCE_PENALTY | non-injury performance penalty from current cold exposure | DIMENSIONLESS_PENALTY | environment/temperature/exposure model | cold bands and performance curve |
| RESOLVER_POST_EVENT_EMOTIONAL_RECOVERY | recovery toward functional baseline after resolved emotional event | RECOVERY_EFFECT / PERFORMANCE_DECAY | mental pressure/recovery model | baseline, recovery timing, Resolve interaction |

## Calibration-readiness tiers

### Tier 0 — parent model absent

Do not assign passive coefficients yet when the parent base term itself is undefined.

Current examples:
- social-cue interpretation;
- command-workflow error;
- detailed fatigue curve;
- environmental heat/cold performance curve.

### Tier 1 — state concept exists, unit/scale open

Safe next step:
define ranges/scenario anchors without locking coefficients.

Current examples:
- Stamina/Focus resources;
- known-information recall;
- procedure overhead;
- equipment retention.

### Tier 2 — executable base resolver exists

Only after runtime implementation or a formal numeric simulation exists may final candidate coefficients be tested.

No current Wave-001 shared passive resolver is certified Tier 2 by this document.

## Dependency order

Recommended numeric-design order:

1. authoritative simulation-time representation;
2. core resource scales and ordinary spend/recovery ranges;
3. action timing/contest representation;
4. environment/fatigue penalty representation;
5. evidence/error/confidence representation;
6. procedure/workflow error representation;
7. passive coefficients and caps.

This prevents passive numbers from defining the base systems backwards.

## Acceptance gate

A resolver may receive candidate numeric values only when:
- its base term is defined;
- its unit class is selected;
- base scenario ranges exist;
- cap/floor meaning is explicit;
- save/rounding behavior is understood.

No final value is assigned by this map.
