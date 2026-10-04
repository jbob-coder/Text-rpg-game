# THE GAME — Status Base Resolution Term & Unit Taxonomy

Status: **PHASE-C NUMERIC PREPARATION / ABSTRACT UNITS ONLY / NOT CANON / NOT IMPLEMENTED**

Parents:
- `STATUS_NUMERIC_CALIBRATION_FRAMEWORK.md`
- `PASSIVE_SHARED_RESOLVER_CAP_SEMANTICS_WAVE_001.md`
- `STATUS_BALANCE_AND_TEST_MATRIX.md`

Purpose: define the kinds of measurable terms the Status system needs before final numeric coefficients are selected.

This standard deliberately does **not** choose final scales, decimal precision, simulation tick duration, or resource curves.

## 1. Unit classes

### RESOURCE_AMOUNT

Used for:
- Health;
- Stamina;
- Focus;
- Resolve;
- any explicitly authored ability-specific reserve.

Properties:
- bounded by an authoritative minimum/maximum;
- unit scale remains system-specific;
- UI may project a formatted value or band.

No universal conversion exists between different resource types.

### RESOURCE_RATE

Represents resource amount gained/lost per authoritative time interval.

Examples:
- Focus drain during prolonged work;
- Stamina recovery during a valid recovery window.

Required parent definitions:
- resource unit;
- authoritative time unit;
- trigger/window semantics.

### TIME_INTERVAL

Represents elapsed authoritative simulation/world time.

Examples:
- action recovery;
- technique duration;
- rest/recovery window;
- passive reset period.

Final implementation may use seconds, ticks, turns, or another authoritative clock representation, but one conversion standard must exist before numeric lock.

### DISTANCE

Represents physical world distance.

Required for:
- engagement spacing;
- ability range;
- travel;
- path length.

Final world-unit representation remains `TBD`.

### DIMENSIONLESS_PENALTY

Represents a bounded gameplay penalty that has no natural physical unit.

Examples:
- fatigue performance loss;
- heat/cold performance loss;
- familiarity friction.

It must have:
- zero/no-penalty meaning;
- ordering;
- hard minimum/maximum;
- conversion rule into the downstream resolver.

No final numeric scale is chosen here.

### ERROR_BURDEN

Represents bounded likelihood/severity of avoidable procedural, interpretation, recall, or execution error.

Examples:
- recall failure;
- protocol omission;
- audience-cue interpretation error;
- diagnostic checking error.

The game may later implement this as:
- probability;
- score checked against difficulty;
- deterministic threshold;
- hybrid contest.

The implementation form remains open.

### EXECUTION_VARIANCE

Represents inconsistency around a technically valid action.

Examples:
- fine-motor steadiness;
- recoil disruption;
- timing variance.

This must remain separate from:
- raw skill;
- equipment physical limits;
- impossible actions.

### CONTEST_MODIFIER

Represents one bounded modifier to an opposed or thresholded contest.

Examples:
- equipment retention;
- displacement resistance;
- some social/defensive interactions.

It cannot itself guarantee success.

### INTERPRETATION_CONFIDENCE

Represents the character/system's justified confidence in an observation or interpretation.

It is not objective truth.

Final UI bands/scales remain governed by the knowledge/evidence standard.

### PROCEDURE_OVERHEAD

Represents avoidable transition, setup, or cognitive burden in a known multi-step procedure.

It is separate from mandatory physical steps/time.

### RECOVERY_EFFECT

Represents bounded improvement toward an existing recovery target.

Required inputs:
- valid recovery opportunity;
- recovery target;
- current state;
- cap;
- active conditions.

It cannot create the opportunity itself.

### PERFORMANCE_DECAY

Represents loss of effective performance over sustained exertion, repetition, or pressure.

It must remain separate from:
- actual resource amount;
- injury;
- long-term skill;
- environment harm.

## 2. Canonical clock requirement

Clock semantics are now defined in:
- `WORLD_SIMULATION_TIME_AND_DURATION_STANDARD.md`;
- `STATUS_WORLD_TIME_PARENT_FIXTURE_BATCH_001.md`.

Resolved:
- durable strategic `WORLD_TIME` uses integer simulation minutes;
- current `GameState.time_minutes` remains the compatibility authority until explicit migration;
- turns are not elapsed time;
- sub-minute tactical/process timing remains a separate local domain;
- device wall-clock time is not gameplay authority by default;
- temporal abilities do not rewind the durable campaign clock under current laws.

Still open before numeric lock:
- tactical/sub-minute remainder representation;
- action duration ranges;
- encounter-to-world-time reconciliation values;
- activity-specific duration ranges.

No passive coefficient should hard-code an unresolved local timing representation.

## 3. Resource-unit requirement

Core resource semantics are now defined in:
- `CORE_RESOURCE_SCALE_AND_TRANSACTION_STANDARD.md`.

Resolved:
- Health, Stamina, Focus, Resolve remain distinct absolute resource amounts;
- minimum is 0;
- effective maxima are authoritative derived values;
- current/base/effective maximum are separate concepts;
- max increase does not automatically refill;
- max decrease clamps current value when required;
- spend/recovery are authoritative deduplicated transactions;
- no default cross-resource conversion exists.

Still open before numeric lock:
- representative target maximum bands;
- ordinary spend ranges;
- ordinary recovery ranges;
- zero-resource consequences;
- final precision/rounding.

Initial content values and current formulas remain reference implementation evidence, not automatic target balance.

## 4. Probability versus deterministic score

General resolution-mode semantics are now defined in:
- `STATUS_ERROR_CONFIDENCE_RESOLUTION_MODE_STANDARD.md`.

Approved target modes:
- `DETERMINISTIC_RULE`;
- `MARGIN_CHECK`;
- `SEEDED_VARIANCE_MARGIN`;
- `OPPOSED_CONTEST`;
- `WEIGHTED_OUTCOME`.

`ERROR_BURDEN` is not automatically a literal probability.

Numeric knowledge/evidence confidence, where used internally, remains bounded 0..1 and is not objective truth probability. `SYSTEM_CONFIRMED` is an authority/provenance state rather than confidence=1.

Domain-specific difficulty/error/variance ranges remain open.

## 5. Physical versus abstract units

Where a natural physical quantity exists, prefer a physical/world unit.

Examples:
- distance;
- elapsed time;
- stored energy if the final physics model uses explicit units;
- mass/temperature if required by an ability law.

Where no natural unit exists, use an explicit abstract unit class rather than pretending it is physical.

## 6. Precision rule

Do not choose decimal precision before:
- expected value range;
- UX display needs;
- deterministic serialization;
- save compatibility;
- rounding behavior

are known.

## 7. Derived-value rule

A derived term should identify:
- source state;
- formula version;
- dependencies;
- clamp/cap;
- whether it is persisted or recomputed;
- player-safe projection.

Avoid persisting duplicated derived values unless required.

## 8. Versioning

Every future locked numeric rule should carry:
- parameter ID;
- unit class;
- version;
- value/range;
- owner;
- migration policy.

A balance change must not silently reinterpret old save values under a new unit meaning.

## 9. Required tests

Future numeric implementation must prove:
- units are not mixed accidentally;
- resource underflow/overflow is controlled;
- timing conversion is deterministic;
- derived terms rebuild identically after save/load;
- caps/floors operate in the correct unit;
- rounding cannot create repeatable value gain;
- UI formatting does not become gameplay authority.

This standard establishes unit classes only. It does not assign final numeric values.
