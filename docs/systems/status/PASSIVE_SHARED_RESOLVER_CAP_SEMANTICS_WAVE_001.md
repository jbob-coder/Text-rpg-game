# THE GAME — Passive Shared Resolver & Cap Semantics — Wave 001

Status: **PHASE-C RESOLVER NORMALIZATION / PROVISIONAL / NOT CANON / NOT IMPLEMENTED**

Parents:
- `PASSIVE_OVERLAP_EDGE_ADJUDICATION_WAVE_001.md`
- `PASSIVE_CROSS_FAMILY_COMPOSITION_STANDARD.md`
- `STATUS_NUMERIC_CALIBRATION_FRAMEWORK.md`

Purpose: convert the 38 `SAME_TERM_CAPPED` overlap edges into canonical shared resolver families so the same gameplay term cannot receive duplicate numeric treatment through parallel passive systems.

## 1. Resolver consolidation result

The overlap adjudication introduced 24 provisional resolver keys.

This standard consolidates them to **20 canonical resolver families**.

### Merge A — recall

Provisional:
- `RESOLVER_KNOWN_INFORMATION_RECALL`
- `RESOLVER_KNOWN_PROTOCOL_RECALL`

Canonical:
- `RESOLVER_KNOWN_INFORMATION_RECALL`

Protocol recall becomes a domain-tagged case:
- `domain=protocol`;
- `domain=team`;
- `domain=species`;
- `domain=route`;
- `domain=injury_pattern`;
- `domain=classified_compartment`;
- etc.

Reason:
one fact-retrieval attempt must not receive one bonus for “general recall” and a second bonus merely because the fact is also a protocol.

### Merge B — prolonged Focus drain

Provisional:
- `RESOLVER_LONG_TASK_FOCUS_DRAIN`
- `RESOLVER_PROLONGED_FOCUS_DRAIN`

Canonical:
- `RESOLVER_PROLONGED_FOCUS_DRAIN`

Scope tags distinguish:
- calibration;
- professional work;
- negotiation;
- vigilance/reasoning;
- sanctioned isolation/testing.

Reason:
all modify Focus degradation over a prolonged eligible task window.

### Merge C — procedure compliance

Provisional:
- `RESOLVER_SECURITY_SECRECY_PROTOCOL_COMPLIANCE`
- `RESOLVER_SECURITY_SAFETY_PROCEDURE_COMPLIANCE`
- `RESOLVER_WORKPLACE_PROCEDURE_COMPLIANCE`

Canonical:
- `RESOLVER_PROCEDURE_COMPLIANCE_ERROR`

Scope tags:
- `workplace_safety`;
- `information_security`;
- `secrecy_compartment`;
- `workshop`;
- other explicitly authored procedure domains.

Reason:
one procedural check should have one final omission/error term even if several domain-specific passives are eligible.

## 2. Canonical resolver families

| Canonical resolver | Shared term | Composition shape | Non-negotiable cap/floor |
|---|---|---|---|
| RESOLVER_KNOWN_INFORMATION_RECALL | retrieval error/burden for already acquired information | capped penalty reduction | unknown information remains unavailable; certainty not guaranteed |
| RESOLVER_AUDITORY_SOURCE_SEPARATION | auditory source-separation error | capped error reduction | absent/inaudible signal stays absent |
| RESOLVER_ENGAGEMENT_DISTANCE_JUDGMENT | spacing/range judgment error | capped error reduction | physical reach, movement, and geometry stay authoritative |
| RESOLVER_IMMEDIATE_THREAT_PRIORITIZATION | ordering error among already recognized immediate threats | capped decision-error reduction | hidden threats stay hidden; priority can still be wrong |
| RESOLVER_PROCEDURE_COMPLIANCE_ERROR | omission/error probability in a known valid procedure | capped error reduction | cannot grant authorization, knowledge, or perfect compliance |
| RESOLVER_PROLONGED_FOCUS_DRAIN | Focus degradation during an eligible prolonged task | capped drain reduction | drain cannot become negative; no Focus creation |
| RESOLVER_PRACTICED_PROCEDURE_OVERHEAD | avoidable transition/cognitive overhead in a practiced procedure | capped overhead reduction | mandatory steps/time remain |
| RESOLVER_ANALYTICAL_CHECK_DISCIPLINE | avoidable conclusion/checking error | capped error reduction | does not reveal hidden truth |
| RESOLVER_SYSTEM_ANOMALY_RECOGNITION | recognition error for legitimately observable Status/system anomalies | capped recognition-error reduction | hidden prompt/system content remains hidden |
| RESOLVER_EQUIPMENT_RETENTION | handling/retention modifier in a valid equipment-control contest | capped contest modifier | no absolute immunity to disarm/loss |
| RESOLVER_COMMAND_STRUCTURE_FAMILIARITY | procedural error inside a known command structure | capped error reduction | does not create rank or authority |
| RESOLVER_FINE_MOTOR_STEADINESS | execution variance in an eligible precision task | capped variance reduction | tool/body precision floor remains |
| RESOLVER_TRAVEL_EFFICIENCY | avoidable travel cost/pace inefficiency | capped inefficiency reduction | terrain, load, injury, and distance remain |
| RESOLVER_FATIGUE_PERFORMANCE_DECAY | performance loss from eligible ordinary fatigue/repetition | capped penalty reduction | fatigue and recovery needs remain real |
| RESOLVER_OBSERVED_AUDIENCE_CLIENT_CUE_INTERPRETATION | interpretation error for observable group/client cues | capped interpretation-error reduction | no mind reading or hidden intent access |
| RESOLVER_STAMINA_RECOVERY_OPPORTUNITY | recovery improvement during a valid Stamina-recovery opportunity | capped recovery bonus | no opportunity creation; resource cap remains |
| RESOLVER_SLEEP_RESTORATION | restorative value of valid adequate sleep | capped recovery-efficiency increase | sleep deprivation does not become safe |
| RESOLVER_HEAT_PERFORMANCE_PENALTY | non-critical heat performance penalty | capped penalty reduction | heat injury state remains separate |
| RESOLVER_COLD_PERFORMANCE_PENALTY | non-critical cold performance penalty | capped penalty reduction | cold injury state remains separate |
| RESOLVER_POST_EVENT_EMOTIONAL_RECOVERY | recovery toward functional emotional baseline after a resolved event | capped recovery-rate/penalty improvement | no instant reset or emotion deletion |

## 3. Generic symbolic cap rules

Exact numeric values remain `TBD`.

### Penalty/error reduction

For resolvers that reduce a penalty/error term:

`eligible_reduction = capped_sum(valid_passive_modifiers)`

`final_penalty = max(context_floor, base_penalty - eligible_reduction)`

Required properties:
- one cap per canonical resolver;
- no duplicate passive ID;
- domain/context eligibility checked before composition;
- floor cannot be crossed.

### Recovery/efficiency increase

For recovery/efficiency resolvers:

`eligible_bonus = capped_sum(valid_passive_modifiers)`

`final_value = min(context_cap, base_value + eligible_bonus)`

Required properties:
- cannot create the underlying opportunity;
- cannot exceed resource/state cap;
- cannot convert one resource into another without a separate rule.

### Contest modifiers

For contest-style resolvers:

`final_modifier = clamp(base_modifier + capped_sum(valid_modifiers), min_modifier, max_modifier)`

The modifier influences a contest; it never guarantees the contest result.

## 4. Scope tags

A passive contributes only when its scope tags match the current resolution.

Required tag classes where applicable:
- domain;
- task/procedure;
- equipment class;
- environment/hazard;
- profession;
- institution;
- species;
- team;
- injury/rehabilitation context;
- primary ability/technique.

A broader passive does not automatically contribute to every narrow domain.

## 5. Specific anti-double-count rules

### Deep Recall + Protocol Memory + Black Ledger

When the current retrieval concerns one authorized protocol:
- all eligible recall passives are gathered once;
- the result is composed through `RESOLVER_KNOWN_INFORMATION_RECALL`;
- protocol/category tags select eligibility;
- the same knowledge fact is resolved once.

### Patience Engine + Calibration Patience + White Room + Cognitive Endurance + Professional Focus + Negotiation Stamina

If several are eligible for one prolonged Focus-drain event:
- all contribute to `RESOLVER_PROLONGED_FOCUS_DRAIN`;
- one shared cap/floor applies;
- task-domain tags determine which passives actually qualify.

### Workshop Discipline + Safety Routine + Security Habit + Closed Hand

For one procedural action:
- only passives whose procedure-domain tags match are eligible;
- all eligible compliance modifiers resolve through `RESOLVER_PROCEDURE_COMPLIANCE_ERROR`;
- the check is not repeated once per passive.

### Second Wind + Recovery Channel

If one recovery opportunity is simultaneously ordinary exertion recovery and valid primary-ability recovery:
- both may be eligible;
- both modify one `RESOLVER_STAMINA_RECOVERY_OPPORTUNITY` transaction;
- one recovery cap applies;
- the opportunity cannot trigger twice.

### Heat/Cold Tolerance + Heat/Cold Resistance

For the shared **performance-penalty** component:
- both may use the heat/cold performance resolver;
- one cap applies.

Injury/harm mitigation remains a separate resolver owned by the resistance/hazard system and is not duplicated by environmental tolerance.

## 6. Domain specialization rule

A specialized passive may be more relevant than a broad passive without creating a second final term.

The future numeric model may use:
- eligibility weighting;
- context-specific modifier magnitude;
- diminishing returns;
- strongest-plus-secondary composition.

The final choice is `TBD`, but it must still end in one canonical resolver result.

## 7. Resolver audit record

Future debug/audit output should support:
- resolver key;
- base term;
- context/scope tags;
- candidate passive IDs;
- eligible passive IDs;
- rejected IDs and reasons;
- each proposed modifier;
- cap/floor;
- final authoritative term.

Player-safe UI does not require access to this internal audit.

## 8. Save/load rule

Passive composition itself should be deterministic from saved authoritative state.

Do not persist a second permanent copy of a derived combined modifier unless performance requires caching and the cache has:
- source-version tracking;
- invalidation rules;
- deterministic rebuild.

Loading must not apply the same passive twice.

## 9. Required tests

For every canonical resolver:
- zero eligible passives returns the base term;
- one eligible passive applies once;
- duplicate ownership does not double-apply;
- two eligible passives respect the shared cap;
- ineligible scope tags reject the modifier;
- floor/cap cannot be crossed;
- save/load produces the same result;
- player-safe projection does not expose hidden qualification state.

Additional required tests:
- protocol recall cannot receive two independent recall finalizations;
- prolonged Focus drain cannot be reduced through two separate resolver keys;
- procedure compliance is checked once per procedure step/check;
- Heat/Cold performance reduction cannot silently reduce injury state;
- Second Wind + Recovery Channel cannot produce two recovery opportunities from one event.

## 10. Remaining numeric blockers

Still `TBD`:
- modifier units;
- per-resolver hard caps/floors;
- individual passive coefficient ranges;
- diminishing-return shape if used;
- context-weighting model;
- base-system units.

These must be calibrated only after the underlying base terms are documented.

No passive is canon-promoted and no final numeric value is established by this standard.
