# THE GAME — Core Resource Scale & Transaction Standard

Status: **ACTIVE TARGET-GAME DESIGN / CURRENT-REALITY MAPPED / FINAL BALANCE RANGES OPEN / IMPLEMENTATION MIGRATION DEFERRED**

Parents:
- `PROGRESSION_CLASSES_RANKS_EVOLVED_GAME_DESIGN.md`
- `STATUS_BASE_RESOLUTION_TERM_UNIT_TAXONOMY.md`
- `STATUS_CORE_RESOURCE_PARENT_FIXTURE_BATCH_001_STAMINA_FOCUS.md`
- `WORLD_SIMULATION_TIME_AND_DURATION_STANDARD.md`

Scope:
- Health;
- Stamina;
- Focus;
- Resolve.

Purpose: define resource ownership, scale semantics, effective maxima, spend/recovery transactions, max-change behavior, current reference formulas, and the remaining calibration work.

---

# 1. CURRENT REALITY — resource identities

Current registered resource keys:
- `health`;
- `stamina`;
- `focus`;
- `resolve`.

Current runtime stores:
- current value under the resource name;
- effective maximum under `max_<resource>`.

Current resources are numeric and are normalized against authoritative derived maxima.

# 2. CURRENT REALITY — effective maximum formulas

Current schema defines:

`max_health = 50 + 2.0*Endurance + 0.5*Will`

`max_stamina = 40 + 1.5*Endurance + 0.5*Athletics`

`max_focus = 30 + 0.8*Intellect + 0.7*Will`

`max_resolve = 25 + 1.1*Will + 0.35*Presence + 0.15*Leadership`

These are current implementation facts.

Attributes and skills are authored on 0–100 ranges before modifier effects.

Ignoring all modifiers, the raw formula envelopes are therefore:

| Resource | Raw authored-input formula minimum | Raw authored-input formula maximum |
|---|---:|---:|
| Health | 50 | 300 |
| Stamina | 40 | 240 |
| Focus | 30 | 180 |
| Resolve | 25 | 185 |

These are **reference implementation envelopes**, not locked target balance ranges.

Effective modifiers can change inputs and/or derived values, so actual runtime maxima are not universally capped by the table above.

# 3. CURRENT REALITY — floors and normalization

Current derived resource maxima have hard minimum 0.

Current initialization/normalization:
- recomputes effective maxima;
- records `max_<resource>`;
- refills to maximum only when explicitly requested or when a current resource is absent;
- otherwise clamps current resource to `0 <= current <= effective maximum`.

Therefore current max increase does **not** automatically refill the newly available amount.

Current max decrease clamps current resource downward if necessary.

This behavior is a strong target compatibility rule.

# 4. CURRENT REALITY — provisional Dead Relay values

Current provisional starting content uses:
- Health 100;
- Stamina 70;
- Focus 60;
- Resolve 50.

These are starting **current values**, not universal maxima.

They must not be used to infer:
- universal 100-point Health;
- universal Stamina/Focus/Resolve caps;
- percentage-based resource semantics.

# 5. CURRENT REALITY — recovery

Current recovery implementation uses the current effective maximum as its reference and calculates hourly recovery using provisional coefficients:

- Health: 0.04 × max per hour;
- Stamina: 0.30 × max per hour;
- Focus: 0.22 × max per hour;
- Resolve: 0.15 × max per hour;

then multiplies by recovery quality and elapsed hours.

Recovery clamps to effective maximum.

These are implementation facts and regression evidence, not final target balance.

# 6. CURRENT REALITY — training spend examples

Current skill training consumes, per hour at intensity 1.0:
- 8 Stamina;
- 5 Focus.

Intensity currently scales those costs.

These are current implementation values, not universal target activity costs.

# 7. EVOLVED TARGET — resource scale semantics

The target game preserves **absolute resource amounts with dynamic effective maxima**.

It does **not** redefine all resources as normalized 0–100 percentages.

Reasons:
- current formulas already produce different natural ranges;
- different character builds legitimately have different capacities;
- abilities/passives can reason about amount, cost, and maximum separately;
- UI can still show a bar/ratio without making percentage the authoritative state.

Player-safe UI may show:
- current amount;
- effective maximum;
- ratio/bar;
- broad warnings.

The authoritative engine owns absolute values.

# 8. Minimum and maximum rule

For every core resource:

`minimum = 0`.

`effective_maximum = authoritative derived maximum after valid modifiers`.

Current value must satisfy:

`0 <= current <= effective_maximum`.

No ordinary transaction may produce:
- negative resource;
- value above effective maximum;
- NaN/infinite resource state.

# 9. Base maximum versus effective maximum

Documentation should distinguish:

`BASE_MAX`
- maximum from the core derived formula before temporary/direct derived modifiers.

`EFFECTIVE_MAX`
- final authoritative maximum after all valid modifiers and floors.

`CURRENT`
- presently available amount.

A future UI may explain contribution sources, but only the engine computes them.

# 10. Maximum-change rule

When EFFECTIVE_MAX changes:

### Increase
Default:
- CURRENT remains unchanged;
- additional capacity becomes empty.

An explicit refill/heal/recovery effect may fill it separately.

### Decrease
Default:
- CURRENT clamps down to the new EFFECTIVE_MAX if necessary.

This preserves current implementation behavior and avoids free resource creation from equipment/modifier swapping.

# 11. Spend transaction

A resource spend should eventually contain:
- transaction ID;
- resource type;
- source action/ability;
- requested amount;
- accepted amount;
- pre-spend current;
- post-spend current;
- cost modifiers;
- minimum/floor;
- world/encounter time;
- commit state.

Default:
- if an action requires full cost and CURRENT < final required cost, action fails before spend;
- partial-spend behavior requires explicit action law;
- spend commits once.

# 12. Cost modifier rule

A passive/ability can modify an authorized cost term.

The final cost:
- cannot become negative;
- cannot generate the same resource through “negative cost”;
- respects shared same-term stacking/cap rules;
- must identify whether reduction is additive, multiplicative, capped, or another explicit form.

No universal cost-reduction formula is locked yet.

# 13. Recovery transaction

A recovery transaction should identify:
- resource;
- valid recovery opportunity;
- base recovery;
- context/quality;
- eligible modifiers;
- active blockers;
- accepted recovery;
- pre/post current;
- maximum;
- event ID;
- elapsed WORLD_TIME.

Recovery:
- cannot exceed maximum;
- cannot create its own opportunity;
- cannot execute twice after reload;
- cannot automatically restore a different resource.

# 14. No universal passive percentage

The target standard does not assume every passive uses:
- +5%;
- +10%;
- multiplicative percentage stacking.

A passive may modify:
- amount;
- rate;
- cost;
- recovery opportunity;
- error burden;
- another authorized term.

The modifier form belongs to its canonical resolver.

# 15. Health semantics

Health represents physical survival/injury capacity at the core-resource layer.

Still unresolved:
- exact relationship between Health and persistent wounds/injury;
- zero-Health outcome;
- incapacitation/death thresholds;
- healing rates;
- medical-treatment interaction.

Passives cannot silently define these parent rules.

# 16. Stamina semantics

Stamina represents immediately available physical exertion capacity.

Uses may include:
- training;
- movement;
- combat actions;
- physical abilities;
- sustained work.

Still unresolved:
- zero-Stamina consequence;
- ordinary action cost bands;
- exertion/fatigue separation;
- combat recovery cadence.

Fatigue remains a distinct potential long-duration state rather than automatically being identical to Stamina.

# 17. Focus semantics

Focus represents immediately available concentration/precision/technical/power exertion capacity.

Uses may include:
- abilities;
- prolonged concentration;
- technical tasks;
- training;
- high-load analysis.

Still unresolved:
- zero-Focus consequence;
- ordinary action cost bands;
- prolonged drain ranges;
- recovery cadence;
- interaction with cognitive strain.

# 18. Resolve semantics

Resolve represents immediately available mental/social resistance and sustained will capacity.

Still unresolved:
- zero-Resolve consequence;
- ordinary pressure/social/ability cost bands;
- relation to fear/morale/emotional recovery;
- recovery cadence.

Resolve is not identical to emotion, loyalty, or confidence.

# 19. Cross-resource isolation

Default:
- Health is not Stamina;
- Stamina is not Focus;
- Focus is not Resolve;
- Resolve is not Health.

No automatic conversion exists.

Any conversion requires:
- explicit mechanic;
- rate;
- efficiency;
- cap;
- ownership;
- exploit review.

# 20. Resource-specific reserves

Ability reserves such as:
- CHARGE_RESERVE;
- THERMAL_RESERVE;
- KINETIC_RESERVE;
- GENERAL_ENERGY_RESERVE

remain separate from core resources.

A UI meter does not make them interchangeable.

# 21. Authoritative time basis

World/life-simulation resource rates use WORLD_TIME minutes as the durable strategic clock.

A rate may be represented per:
- minute;
- hour;
- another exact conversion

as long as conversion to authoritative minutes is deterministic.

Encounter-only spends may use encounter action transactions and reconcile with world time separately.

# 22. Precision and rounding

Current resource code rounds several recovery/training results to 3 decimal places.

That is current implementation behavior, not yet a locked target precision standard.

Before numeric lock, define:
- internal precision;
- serialization precision;
- UI display precision;
- rounding stage;
- repeated-small-transaction exploit behavior.

Rounding must never create repeatable net resource gain.

# 23. Current reference envelope use

The current raw formula envelopes and current recovery/training values may be used as:

`REFERENCE_IMPLEMENTATION_RANGE`

for:
- regression tests;
- migration checks;
- exploratory balancing.

They are not automatically:

`TARGET_CANON_RANGE`.

Any final change must state whether it:
- preserves formula;
- tunes coefficients;
- introduces caps;
- changes modifier behavior;
- changes resource meaning.

# 24. Target calibration bands still needed

For Stamina and Focus, range-fixture readiness still requires:
- representative low/ordinary/trained/elite effective maxima;
- ordinary cheap/moderate/high action costs;
- ordinary recovery-window amounts/rates;
- sustainable activity duration;
- zero-resource consequences;
- interaction with fatigue/strain.

For Health/Resolve, equivalent domain-specific calibration is also required.

# 25. Save/load

Persist:
- CURRENT resource values;
- authoritative inputs needed to reconstruct EFFECTIVE_MAX;
- modifiers/perks/equipment/conditions that change maxima;
- active resource transactions only if mid-transaction saves are legal.

Prefer recomputing derived maxima from authoritative source state rather than treating duplicate stored maxima as independent truth where migration permits.

Current schema stores current/max resource fields inside player state after normalization; any change requires migration review.

# 26. Required tests

- effective maximum recomputes deterministically;
- current clamps after max decrease;
- max increase does not auto-refill;
- full refill happens only when explicitly requested;
- spend cannot underflow;
- recovery cannot overflow;
- cost reduction cannot create resource;
- cross-resource isolation holds;
- save/load cannot duplicate spend/recovery;
- modifier removal cannot preserve illegal current > max;
- rounding cannot be farmed;
- current reference formulas reproduce existing regression values until migration changes them.

# 27. Range-fixture status

This standard closes:
- resource identity;
- absolute-versus-percent semantics;
- min/max ownership;
- base/effective/current distinction;
- max-change behavior;
- spend/recovery transaction shape;
- cross-resource isolation;
- strategic time basis.

Still missing for `RANGE_FIXTURES_READY`:
- target representative maximum bands;
- ordinary spend bands;
- ordinary recovery bands;
- zero-resource consequences;
- final rounding/precision.

No final balance value is canon-promoted here.
