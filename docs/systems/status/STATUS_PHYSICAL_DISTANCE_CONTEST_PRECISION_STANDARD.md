# THE GAME — Physical Distance, Contest & Precision Standard

Status: **ACTIVE TARGET-GAME DESIGN / CURRENT-REALITY MAPPED / FINAL COMBAT RANGES OPEN / NOT IMPLEMENTED**

Parents:
- `STATUS_BASE_RESOLUTION_TERM_UNIT_TAXONOMY.md`
- `STATUS_ERROR_CONFIDENCE_RESOLUTION_MODE_STANDARD.md`
- `SPATIAL_REFERENCE_FRAME_AND_TRANSIT_STANDARD.md`
- `docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md`
- `STATUS_PARENT_FIXTURE_BATCH_004_SPATIAL_TRAVEL_CONTEST.md`
- `STATUS_PARENT_FIXTURE_BATCH_002_PROCEDURE_ACTION_PRECISION.md`

Purpose: define the common representation for physical distance, reach, range, opposed physical contests, and precision/variance before final combat/travel numbers are chosen.

---

# 1. CURRENT REALITY

Current repository facts:
- no final tactical grid shape/size is selected;
- no final action-budget/turn model is selected;
- no universal physical world-distance unit is implemented in the current text rules;
- Gate Twelve presentation/map coordinates must not be assumed to be meters;
- some authored routes may carry travel-minute costs;
- current derived stats include accuracy, evasion, guard, initiative, and carry capacity;
- current scene checks can resolve a seeded stat/skill margin against difficulty.

Therefore a target physical-unit standard is required before range-heavy combat/travel calibration.

# 2. Canonical physical distance unit

Target design decision:

**authoritative physical world distance uses meters.**

Conventions:
- base stored/validated physical distance unit: meter;
- kilometer is a display/authoring convenience for large travel;
- centimeters/millimeters may be used for precision/material tasks when needed;
- conversions must be deterministic.

This decision applies to physical geometry, not every map coordinate.

# 3. Presentation coordinates are not physical meters

A visual map may use:
- pixels;
- normalized coordinates;
- authored node positions;
- screen-space units.

Those coordinates do not become physical distance unless a map-specific transform explicitly defines that relationship.

Gate Twelve current map positions remain presentation/layout evidence.

# 4. Route distance versus route time

A route may carry both:
- physical distance;
- travel duration/cost.

They are different fields.

Two routes of equal meters may have different time because of:
- terrain;
- access;
- elevation;
- crowding;
- transport;
- hazards;
- load;
- weather.

Authored route minutes must not be reverse-engineered into meters without an explicit route model.

# 5. Tactical coordinates

The tactical layer may use:
- square grid;
- hex grid;
- free position;
- another original tested layout.

Regardless of representation, each tactical position system must define an explicit mapping to physical distance if physical range/reach rules depend on it.

Example principle:
a “cell” is not intrinsically one meter.

Cell physical size remains `TBD` until tactical design selects the coordinate model.

# 6. DISTANCE unit contract

For a physical distance term record:
- value in meters;
- source positions/geometry;
- frame/reference space;
- measurement confidence if character-estimated rather than engine-truth;
- whether value is engine-authoritative or player-observed.

Player-safe UI may display rounded distance only when legitimately known/perceived.

# 7. Reach

Reach is a physical geometry constraint.

Possible contributors:
- body dimensions;
- held equipment;
- stance;
- action;
- technique.

A judgment passive can improve estimation of reach.

It cannot increase actual reach unless another mechanic physically changes body/equipment/action geometry.

# 8. Ability range

Ability range should use physical meters where a natural spatial range exists.

A range record must distinguish:
- targeting range;
- effect radius;
- path length;
- line-of-sight requirement;
- travel/transit distance;
- area geometry.

Do not collapse these into one “range” number.

# 9. Distance estimation

Characters may possess an estimated distance rather than exact engine truth.

Separate:
- `AUTHORITATIVE_DISTANCE`;
- `OBSERVED_DISTANCE_ESTIMATE`;
- `ESTIMATE_ERROR`;
- `CONFIDENCE`.

`RESOLVER_ENGAGEMENT_DISTANCE_JUDGMENT` modifies estimation burden/error, not authoritative geometry.

# 10. Physical contest model

Target physical contests use the general `OPPOSED_CONTEST` resolution mode when two active sides oppose one another.

Conceptual form:

`contest_margin = actor_capability + actor_context - opposition_capability - opposition_context + bounded_variance_if_used`

The final scale and variance are domain-specific.

Hard physical invalidity resolves before the contest.

# 11. Contest outcome

A contest may produce:
- clear actor success;
- marginal actor success;
- marginal opposition success;
- clear opposition success

or another domain-specific degree set.

Exact thresholds remain `TBD`.

A `CONTEST_MODIFIER` cannot guarantee success by itself.

# 12. Equipment retention

Equipment retention is one physical contest.

Potential actor inputs:
- Might;
- Agility;
- relevant skill/familiarity;
- grip;
- stance;
- body condition;
- equipment geometry;
- passive retention modifier.

Potential opposition inputs:
- opposing force/capability;
- leverage;
- direction;
- environmental force;
- equipment failure state.

One contested hold resolves once.

# 13. Equipment failure precedence

If equipment physically fails:
- a retention contest cannot restore it;
- damaged strap/handle/component state is authoritative.

Contest resolution applies only when a valid contested hold still exists.

# 14. Overwhelming-force rule

No ordinary retention/evasion/guard modifier creates absolute immunity.

The parent system may define situations where opposition exceeds the contestable envelope.

That state can:
- auto-fail;
- impose a hard cap;
- use another damage/displacement resolver.

Exact thresholds remain open.

# 15. Precision representation

Where a natural physical error unit exists, prefer it.

Examples:
- linear placement error in mm/cm;
- angular aim error;
- timing error in local encounter/process time;
- alignment error.

Where no natural unit is practical, use explicit `EXECUTION_VARIANCE`.

Do not call an abstract variance “centimeters” unless the parent action actually measures spatial deviation.

# 16. Fine-motor steadiness

Fine-motor passives can reduce eligible execution variance.

They cannot:
- provide missing skill;
- exceed tool precision;
- exceed body/injury limits;
- solve unknown procedure;
- bypass unstable environment.

A hard precision floor always remains.

# 17. Tool precision floor

Every precision-sensitive tool/process may define:
- nominal precision;
- calibration state;
- damage/wear state if modeled;
- minimum achievable variance;
- environmental sensitivity.

Character steadiness cannot produce output more precise than the combined physical process permits unless an ability explicitly changes that process.

# 18. Accuracy versus precision

Accuracy and precision are not identical.

Accuracy:
closeness to intended/valid target outcome.

Precision:
repeatability/variance around execution.

Current derived `accuracy` can be an input to future combat resolution.

It should not automatically become the universal `EXECUTION_VARIANCE` scale.

# 19. Evasion and guard

Current derived `evasion` and `guard` are reference-game values.

Future tactical combat must decide:
- whether they enter opposed contests;
- difficulty adjustments;
- deterministic thresholds;
- another original resolver.

This standard does not pre-lock that formula.

# 20. Seeded physical variance

If a physical contest uses uncertainty:
- variance is seeded/deterministic;
- save/load does not reroll;
- UI cannot request repeated rolls;
- variance remains bounded.

A purely deterministic physical contest is also valid where appropriate.

# 21. Collision / occupancy authority

Physical location and occupancy are world/tactical state.

A distance/contest passive cannot:
- move an occupied entity into invalid geometry;
- ignore walls;
- ignore collision;
- pass through blocked terrain.

Spatial rules resolve before the contest where applicable.

# 22. Knockback / forced movement

Forced movement requires:
- valid source force/effect;
- direction;
- distance or displacement model;
- collision result;
- body/equipment/environment interaction.

A resistance contest may reduce/avoid forced movement.

It must not erase the physical source from history.

# 23. Player-safe projection

UI may show:
- known distance;
- legal range;
- qualitative contest estimate;
- known precision band;
- known cover/geometry.

UI must not expose:
- hidden exact enemy stats;
- unseen geometry;
- hidden collision;
- exact seeded roll before commit;
- private target state.

# 24. Save/load

Persist authoritative position/contest state needed to reconstruct legal mid-encounter saves.

Committed contest results:
- resolve once;
- cannot reroll on load.

Distance is recomputed from authoritative geometry where possible rather than duplicated as independent mutable truth.

# 25. Parent range requirements

Before affected passive resolvers become `RANGE_FIXTURES_READY`, define:

### Engagement distance
- common body/equipment reach bands;
- typical encounter distances;
- distance-estimation error bands.

### Equipment retention
- contest capability scale;
- leverage/context contribution;
- bounded variance or deterministic thresholds.

### Fine motor
- parent precision/variance scale;
- example tool precision floors;
- fatigue/injury penalty ranges.

# 26. Range-fixture effect

This standard closes the representation prerequisite for:
- `RESOLVER_ENGAGEMENT_DISTANCE_JUDGMENT`;
- `RESOLVER_EQUIPMENT_RETENTION`;
- `RESOLVER_FINE_MOTOR_STEADINESS`.

It does not yet provide their target numeric ranges.

Therefore they remain `QUALITATIVE_FIXTURES_READY` until range fixtures are authored.

# 27. Required tests

- map pixel coordinates are not treated as meters without transform;
- meter conversions are deterministic;
- out-of-reach target remains out of reach;
- distance-estimation passive cannot extend reach;
- one equipment-retention contest finalizes once;
- failed equipment remains failed;
- overwhelming physical cases can still defeat modifiers;
- fine-motor modifier cannot exceed tool/body precision floor;
- seeded physical contest reproduces after load;
- hidden geometry/stats remain hidden.

No runtime implementation or final combat balance is established by this standard.
