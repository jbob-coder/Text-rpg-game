# THE GAME — Passive Canonical Resolver Parent-Fixture Requirements — Wave 001

Status: **PHASE-C NUMERIC PREPARATION / FIXTURE CONTRACTS ONLY / NO FINAL VALUES / NOT CANON / NOT IMPLEMENTED**

Parents:
- `PASSIVE_CANONICAL_RESOLVER_BASE_TERM_MAP_WAVE_001.md`
- `PASSIVE_CANONICAL_RESOLVER_SCENARIO_ANCHORS_WAVE_001.md`
- `PASSIVE_SHARED_RESOLVER_CAP_SEMANTICS_WAVE_001.md`
- `STATUS_BASE_RESOLUTION_TERM_UNIT_TAXONOMY.md`
- `STATUS_NUMERIC_CALIBRATION_FRAMEWORK.md`
- `STATUS_BALANCE_AND_TEST_MATRIX.md`

Purpose: define the **parent-system fixture/range evidence that must exist before passive coefficients are allowed to receive candidate numeric values**.

This document does not assign final values. It prevents passive balance numbers from silently defining missing base systems backwards.

## 1. Fixture principle

A passive modifier is downstream of a parent resolver.

Before any candidate passive coefficient is authored, the parent resolver must supply enough testable baseline evidence to answer:

- what term is being modified;
- what unit or abstract unit class the term uses;
- what an ordinary no-passive result looks like;
- what favorable/adverse parent conditions do to that term;
- what hard floor/cap cannot be crossed;
- how timing, rounding, and save/load affect the term;
- how the term is represented in a deterministic test fixture.

A prose statement such as “this should be a small bonus” is not sufficient numeric evidence.

## 2. Parent-fixture record schema

Each parent-system fixture set should eventually record:

- `fixture_set_id`;
- canonical resolver key;
- parent system/owner;
- base-term ID;
- unit class;
- formula/resolution version;
- input-state schema;
- no-passive baseline case;
- favorable case;
- adverse case;
- boundary/failure case;
- expected ordering relationships;
- floor/cap semantics;
- rounding/precision rule;
- save/load reconstruction rule;
- provenance/evidence;
- review status.

Exact numeric expectations can remain `TBD` until the parent system itself is ready.

## 3. Readiness states

Use:

- `PARENT_MODEL_MISSING` — base resolver is not defined enough for fixtures.
- `FIXTURE_SCHEMA_READY` — required fixture shape is defined, but parent values/ranges are absent.
- `QUALITATIVE_FIXTURES_READY` — baseline/favorable/adverse/boundary cases exist with ordering but no candidate ranges.
- `RANGE_FIXTURES_READY` — parent system provides candidate ranges/expected outputs sufficient for passive coefficient simulation.
- `EXECUTABLE_FIXTURES_READY` — deterministic runtime or formal simulation can execute the cases.

No passive coefficient should move past conceptual bands before at least `RANGE_FIXTURES_READY`.

---

## 4. RESOLVER_KNOWN_INFORMATION_RECALL

Parent owner:
knowledge provenance + recall model.

Required fixture set:
- one clearly learned/reinforced datum;
- one weakly reinforced but known datum;
- one competing/similar known datum case;
- one unknown datum boundary;
- one unauthorized/compartmented datum boundary;
- ordinary stress/context modifier;
- domain-tag compatibility case.

Required parent decisions:
- whether recall resolves by score, probability, threshold, contest, or hybrid;
- how reinforcement/history contributes;
- how confidence differs from truth;
- whether recall error means failure, partial recall, or degraded confidence.

Numeric gate:
do not assign recall-passive coefficients until a no-passive known-information retrieval range exists.

Current readiness:
`FIXTURE_SCHEMA_READY`.

---

## 5. RESOLVER_AUDITORY_SOURCE_SEPARATION

Parent owner:
sensory signal/evidence model.

Required fixture set:
- two audible separated sources;
- overlapping but detectable sources;
- high-noise adverse case;
- familiar-source favorable case;
- inaudible/absent-signal boundary;
- hearing limitation/equipment-assisted observation case where applicable.

Required parent decisions:
- signal/noise representation;
- interpretation-confidence representation;
- whether errors are categorical, score-based, probabilistic, or hybrid.

Numeric gate:
passive coefficients wait until baseline source-separation error/confidence behavior is measurable.

Current readiness:
`FIXTURE_SCHEMA_READY`.

---

## 6. RESOLVER_ENGAGEMENT_DISTANCE_JUDGMENT

Parent owner:
spatial + equipment reach model.

Required fixture set:
- stationary observed target with familiar reach profile;
- moving target;
- unfamiliar but visible equipment profile;
- elevation/terrain complication;
- actual-out-of-reach boundary;
- obscured/unobserved target boundary.

Required parent decisions:
- authoritative world distance unit;
- equipment/body reach representation;
- observation-to-distance-estimate error model;
- movement timing relationship.

Numeric gate:
no passive spacing coefficient before distance and reach use compatible authoritative units.

Current readiness:
`PARENT_MODEL_MISSING` for final numeric work because final world distance representation is still open.

---

## 7. RESOLVER_IMMEDIATE_THREAT_PRIORITIZATION

Parent owner:
threat observation + decision model.

Required fixture set:
- two recognized threats with clearly different urgency;
- multiple recognized threats with close urgency;
- conflicting objective case;
- time-pressure adverse case;
- hidden-threat boundary;
- false/ambiguous observed cue case.

Required parent decisions:
- threat candidate representation;
- prioritization difficulty/error representation;
- separation of observation from decision;
- whether tactical skill contributes before/inside/after this resolver.

Numeric gate:
no passive coefficient until ordinary prioritization burden has a parent resolution rule.

Current readiness:
`FIXTURE_SCHEMA_READY`.

---

## 8. RESOLVER_PROCEDURE_COMPLIANCE_ERROR

Parent owner:
procedure/version/authorization model.

Required fixture set:
- known valid procedure with ordinary steps;
- familiar repeated procedure;
- long/multi-check procedure;
- interruption-pressure case;
- stale procedure-version boundary;
- unauthorized procedure boundary;
- missing-required-step/material boundary.

Required parent decisions:
- procedure-step representation;
- omission/error resolution;
- versioning;
- authorization check order;
- mandatory versus avoidable overhead.

Gate Twelve local evidence:
maintenance, Workshop Row, Municipal Archive, and restricted infrastructure can later provide content contexts, but do not yet define exact procedure fixtures.

Numeric gate:
no coefficient until a procedure can fail/omit deterministically or through an explicitly chosen error model.

Current readiness:
`FIXTURE_SCHEMA_READY`.

---

## 9. RESOLVER_PROLONGED_FOCUS_DRAIN

Parent owner:
Focus + authoritative time/task-window model.

Required fixture set:
- ordinary sustained reasoning task;
- sustained calibration/precision task;
- prolonged social/negotiation task;
- high-distraction adverse case;
- rested/familiar favorable case;
- zero-Focus / insufficient-Focus boundary;
- task-ending/interruption boundary.

Required parent decisions:
- Focus min/max scale;
- authoritative time interval;
- ordinary sustained-task drain range;
- whether drain is continuous, stepped, event-based, or hybrid;
- recovery interaction.

Numeric gate:
requires parent Focus scale plus time-window semantics.

Current readiness:
`PARENT_MODEL_MISSING` for ranges; the resource concept exists but universal scale/time semantics are not locked.

---

## 10. RESOLVER_PRACTICED_PROCEDURE_OVERHEAD

Parent owner:
procedure/action timing model.

Required fixture set:
- known multi-step routine;
- highly practiced routine;
- valid unfamiliar configuration;
- interruption/context-switch case;
- mandatory-step boundary;
- missing-tool/material boundary.

Required parent decisions:
- action/procedure timing representation;
- which overhead is avoidable versus mandatory;
- whether transitions are time, action cost, cognitive cost, or composite.

Numeric gate:
requires an authoritative action-time/procedure-overhead representation.

Current readiness:
`FIXTURE_SCHEMA_READY`.

---

## 11. RESOLVER_ANALYTICAL_CHECK_DISCIPLINE

Parent owner:
evidence + decision model.

Required fixture set:
- sufficient evidence with ordinary review;
- conflicting evidence;
- noisy/incomplete evidence;
- time-pressure review;
- hidden-truth boundary;
- unsupported-conclusion boundary.

Required parent decisions:
- evidence quality representation;
- analytical omission/error term;
- confidence semantics;
- relation to Investigation/domain skills.

Numeric gate:
do not assign modifier magnitude until base analytical-check omission/error has a formal resolution form.

Current readiness:
`FIXTURE_SCHEMA_READY`.

---

## 12. RESOLVER_SYSTEM_ANOMALY_RECOGNITION

Parent owner:
Status event/evidence model.

Required fixture set:
- legitimately visible normal Status event;
- legitimately visible anomalous event;
- repeated/familiar anomaly signature;
- ambiguous anomaly;
- hidden prompt-content boundary;
- protected/root system-state boundary.

Required parent decisions:
- observable Status-event schema;
- anomaly classification;
- confidence/confirmation states;
- disclosure/projection rules.

Numeric gate:
requires actual observable anomaly fields and recognition model; hidden architecture cannot be used as fixture input.

Current readiness:
`PARENT_MODEL_MISSING` for numeric calibration.

---

## 13. RESOLVER_EQUIPMENT_RETENTION

Parent owner:
equipment + physical action contest model.

Required fixture set:
- ordinary contested hold;
- favorable stance/grip;
- awkward leverage;
- fatigued/injured user;
- overwhelming external-force case;
- equipment-failure/slip case.

Required parent decisions:
- contest representation;
- strength/skill/equipment contribution order;
- grip/contact state;
- deterministic versus probabilistic contest model.

Numeric gate:
requires a parent contest scale or deterministic equivalent.

Current readiness:
`FIXTURE_SCHEMA_READY`.

---

## 14. RESOLVER_COMMAND_STRUCTURE_FAMILIARITY

Parent owner:
institution/role/protocol model.

Required fixture set:
- known organization + known role + current protocol;
- temporary reassignment;
- unfamiliar but related unit;
- stale protocol;
- unauthorized-role boundary;
- unknown organization boundary.

Required parent decisions:
- institution stable IDs;
- role/authority namespace;
- command/responsibility workflow;
- protocol versioning;
- error representation.

Gate Twelve boundary:
local civic/maintenance contexts are confirmed, but no formal credential/command hierarchy is yet established.

Numeric gate:
no coefficient until at least one actual institutional workflow can be represented.

Current readiness:
`PARENT_MODEL_MISSING`.

---

## 15. RESOLVER_FINE_MOTOR_STEADINESS

Parent owner:
physical action/tool model.

Required fixture set:
- ordinary precision action;
- familiar tool/procedure;
- fatigue pressure;
- awkward access;
- mild environment instability;
- physical/tool precision floor;
- injury limitation case.

Required parent decisions:
- execution variance representation;
- tool precision limits;
- body condition contribution;
- skill interaction.

Numeric gate:
requires a measurable precision/variance term or deterministic equivalent.

Current readiness:
`FIXTURE_SCHEMA_READY`.

---

## 16. RESOLVER_TRAVEL_EFFICIENCY

Parent owner:
movement/travel/environment model.

Required fixture set:
- ordinary traversable route;
- familiar route;
- rough terrain;
- load/fatigue case;
- adverse weather/environment case;
- blocked/impassable route boundary;
- route-access boundary.

Required parent decisions:
- authoritative distance unit;
- travel time/cost model;
- Stamina/travel interaction;
- terrain penalties;
- route accessibility semantics.

Gate Twelve boundary:
existing node coordinates are presentation/map values and must not become meters. Existing route minutes on some edges are evidence for authored route cost, not a universal physical-distance scale.

Numeric gate:
requires travel distance/time/Stamina fixtures from the parent travel system.

Current readiness:
`PARENT_MODEL_MISSING` for final ranges.

---

## 17. RESOLVER_FATIGUE_PERFORMANCE_DECAY

Parent owner:
exertion/fatigue model.

Required fixture set:
- ordinary sustained work/exertion;
- well-conditioned/paced favorable case;
- repeated demand;
- inadequate but non-catastrophic recovery;
- sleep-loss interaction;
- injury boundary;
- full-recovery/reset case.

Required parent decisions:
- whether fatigue is a stored state, derived penalty, or hybrid;
- accumulation/recovery curve;
- separation from Stamina;
- separation from injury and sleep deprivation.

Numeric gate:
requires an authoritative fatigue model before passive coefficients.

Current readiness:
`PARENT_MODEL_MISSING`.

---

## 18. RESOLVER_OBSERVED_AUDIENCE_CLIENT_CUE_INTERPRETATION

Parent owner:
social observation/evidence model.

Required fixture set:
- explicit ordinary social cue;
- familiar person/context;
- group with mixed reactions;
- ambiguous/deliberately misleading cue;
- culturally unfamiliar context;
- hidden-intent boundary.

Required parent decisions:
- observable cue representation;
- interpretation-confidence model;
- relation to Empathy/Persuasion/Investigation;
- NPC truth versus observed behavior separation.

Numeric gate:
requires an actual social-cue interpretation resolver, not a hidden NPC-truth lookup.

Current readiness:
`PARENT_MODEL_MISSING`.

---

## 19. RESOLVER_STAMINA_RECOVERY_OPPORTUNITY

Parent owner:
Stamina + recovery-window model.

Required fixture set:
- valid ordinary post-exertion recovery opportunity;
- heavy-exertion recovery;
- favorable safe-rest context;
- constrained recovery context;
- active blocking condition;
- Stamina-cap boundary;
- duplicate/replay event case.

Required parent decisions:
- Stamina min/max logic;
- ordinary spend/recovery ranges;
- recovery-window semantics;
- transaction/reset identity;
- time representation.

Numeric gate:
candidate passive coefficients require no-passive recovery transaction fixtures.

Current readiness:
`FIXTURE_SCHEMA_READY` but not `RANGE_FIXTURES_READY`.

---

## 20. RESOLVER_SLEEP_RESTORATION

Parent owner:
sleep/rest + resource recovery model.

Required fixture set:
- valid adequate uninterrupted sleep;
- valid interrupted but still restorative sleep;
- poor environment;
- heavy prior exertion;
- inadequate-sleep boundary;
- sleep-deprivation harm case;
- save/load crossing sleep interval.

Required parent decisions:
- adequate-sleep semantics;
- sleep quality representation;
- resource recovery targets;
- world-time progression;
- interruption rules.

Numeric gate:
requires sleep-duration/quality plus core-resource recovery ranges.

Current readiness:
`PARENT_MODEL_MISSING` for numeric ranges.

---

## 21. RESOLVER_HEAT_PERFORMANCE_PENALTY

Parent owner:
environment/temperature/exposure model.

Required fixture set:
- comfortable/no-penalty baseline;
- non-critical heat penalty;
- acclimated favorable case;
- heavy-work/load adverse case;
- dehydration interaction;
- heat-injury boundary;
- catastrophic environment boundary.

Required parent decisions:
- temperature/exposure bands or equivalent physical model;
- duration effect;
- performance-penalty representation;
- separation from injury/hydration state.

Numeric gate:
requires a parent environmental heat curve or deterministic band model.

Current readiness:
`PARENT_MODEL_MISSING`.

---

## 22. RESOLVER_COLD_PERFORMANCE_PENALTY

Parent owner:
environment/temperature/exposure model.

Required fixture set:
- comfortable/no-penalty baseline;
- non-critical cold penalty;
- acclimated/prepared favorable case;
- wet/fatigued adverse case if wetness is later modeled;
- cold-injury boundary;
- catastrophic environment boundary.

Required parent decisions:
- temperature/exposure bands or equivalent physical model;
- duration effect;
- performance-penalty representation;
- separation from injury.

Numeric gate:
requires a parent environmental cold curve or deterministic band model.

Current readiness:
`PARENT_MODEL_MISSING`.

---

## 23. RESOLVER_POST_EVENT_EMOTIONAL_RECOVERY

Parent owner:
mental pressure/recovery model.

Required fixture set:
- meaningful resolved emotional event;
- safe/supportive recovery context;
- repeated recent stress;
- high-intensity but resolved event;
- still-active threat/event boundary;
- relationship/memory persistence case;
- Resolve interaction case.

Required parent decisions:
- functional-baseline representation;
- emotional-event severity/context;
- recovery time/state;
- relationship with Resolve;
- what remains narrative/qualitative rather than numeric.

Numeric gate:
requires a parent emotional-recovery state model before coefficient assignment.

Current readiness:
`PARENT_MODEL_MISSING`.

---

## 24. Cross-resolver fixture requirements

Before passive numeric simulation, also create shared fixtures for:

### Same-term stacking
For each canonical resolver:
- zero eligible passives;
- one eligible passive;
- two eligible passives;
- duplicate passive ID;
- scope mismatch;
- cap boundary.

### Ordered-stage composition
At least one case where:
- upstream observation/decision/familiarity changes;
- downstream execution/recovery resolves afterward;
- the original full base term is not re-applied at every stage.

### Save/load
For any stateful recovery, fatigue, sleep, event, or resource resolver:
- save before event;
- save after committed event;
- reload;
- verify no duplicate application.

### Hidden-information projection
For evidence/knowledge/social/system resolvers:
- authority can hold hidden truth;
- player-safe projection receives only legitimate observations/results.

## 25. Readiness summary

Current qualitative preparation:
- canonical resolver identities: **20 / 20**;
- base-term/unit-class mapping: **20 / 20**;
- BASELINE/FAVORABLE/ADVERSE/BOUNDARY scenario anchors: **20 / 20**;
- parent-fixture requirement contracts: **20 / 20**.

Still intentionally absent:
- final parent-system scales;
- final parent-system ranges;
- passive coefficient values;
- final cap values;
- final rounding/precision;
- executable runtime fixtures.

## 26. Next numeric-design action

Do **not** jump directly to passive percentages.

Next:
1. choose parent-system fixture batches in dependency order;
2. materialize base-system ranges/test cases where the parent design is sufficiently mature;
3. mark resolvers `RANGE_FIXTURES_READY` only when supported;
4. only then simulate candidate passive coefficients.

Recommended first parent batches:
- core Stamina/Focus resource transactions;
- action/procedure timing;
- knowledge/evidence error representation;
- then travel/fatigue/environment/social systems.

No passive or numeric value is canon-promoted by this document.
