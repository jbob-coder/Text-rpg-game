# THE GAME — Ability Energy & Reserve Accounting Standard

Status: **PROVISIONAL CROSS-TIER DESIGN STANDARD / NOT CANON UNTIL OWNER REVIEW / NOT IMPLEMENTED**

Parents:
- `STATUS_UI_CORE_CONTRACT.md`
- `PRIMARY_ABILITY_WAVE_001_REFINEMENT_COMPLETENESS_AUDIT.md`
- relevant Common, Rare, Super Rare, Super Epic, and Legendary ability detail packets.

Purpose: define one accounting vocabulary for ability-specific stored quantities, external energy sources, transfer rates, conversion, capacity, and losses.

## 1. Core principle

No ability-specific reserve creates free output merely because a UI meter exists.

Every stored or transferred quantity must identify:
- what physical/system quantity it represents;
- where it came from;
- its capacity;
- transfer or charge rate;
- conversion efficiency where conversion occurs;
- allowed output routes;
- loss/decay behavior;
- authoritative owner.

Exact numeric units remain `TBD`.

## 2. Core Status resources are separate

Health, Stamina, Focus, and Resolve are core Status resources.

Ability-specific reserves are separate unless an explicit ability record says otherwise.

Default rules:
- electrical charge is not Focus;
- thermal reserve is not Stamina;
- kinetic reserve is not Resolve;
- generalized energy reserve is not Health;
- no automatic conversion between core resources and ability reserves.

A later ability may explicitly define a conversion, but it requires its own law, rate, efficiency, and balance review.

## 3. Reserve classes

### CHARGE_RESERVE
Used by Static Reservoir.

Represents bounded stored electrical charge/state.

It must eventually track enough information to distinguish:
- stored charge/capacity;
- safe operating range;
- available discharge path;
- environmental electrical context.

Do not silently treat this as the same thing as a generic energy meter.

### THERMAL_RESERVE
Used by Cryo Sink.

Represents thermal energy removed from another region and held by the ability's bounded storage mechanism.

It may not automatically power unrelated effects.

### KINETIC_RESERVE
Used by Momentum Bank.

Represents captured kinetic-energy-equivalent from qualifying motion events.

The current parent law stores kinetic energy, not a universal force resource.

### GENERAL_ENERGY_RESERVE
Used by Energy Devour.

Represents normalized stored energy produced by conversion from explicitly supported non-biological source types.

This reserve is broader than the domain-specific reserves, but it is still constrained by:
- source whitelist;
- conversion efficiency;
- capacity;
- approved output routes.

### EXTERNAL_ENERGY_BUDGET
Used by systems such as World Gate and potentially Matter Recode.

Represents energy supplied by equipment, infrastructure, prepared sources, or another explicitly connected system.

It is not automatically a personal reserve.

## 4. Source record

A future energy-source record should be able to identify:
- `source_id`;
- `energy_type`;
- authoritative owner/location;
- currently available amount or supply state;
- maximum transfer rate;
- access/connection state;
- compatibility tags;
- depletion/replenishment model;
- measurement confidence where relevant.

## 5. Reserve record

A future reserve state should support:
- `reserve_id`;
- owner entity;
- reserve class;
- current stored amount/state;
- capacity;
- input-rate limit;
- output-rate limit;
- supported input types;
- supported output types/routes;
- conversion efficiency;
- decay/leakage rule;
- lockout/over-capacity state;
- last authoritative update.

No UI component is the owner of these values.

## 6. Accounting invariant

For every transfer or conversion:

`accepted_output <= accepted_input`

unless a separately authored external source supplies the difference.

For conversion:
`stored_gain = accepted_input × conversion_efficiency`

with efficiency normally bounded at or below 100%.

Losses are not required to become another usable reserve. They may be represented as non-recoverable environmental/system loss according to the future physical model.

No record may hide net-positive generation inside rounding, repeated conversion, save/load, or chained abilities.

## 7. Capacity rule

Every reserve has a finite capacity.

When an incoming transfer would exceed capacity, the authoritative resolver must choose a documented outcome, such as:
- clamp/reject excess input;
- terminate transfer;
- enter an overload/lockout state;
- route excess to an allowed sink.

The exact outcome is ability-specific.

Capacity cannot be bypassed by opening multiple UI panels, splitting stacks, reloading, or rapidly toggling techniques.

## 8. Rate rule

Capacity and throughput are different.

A reserve may have unused capacity while still being unable to absorb or release energy faster than its current rate limit.

Required concepts:
- input-rate limit;
- output-rate limit;
- external-source transfer limit;
- technique-specific rate multiplier if later approved.

This prevents “large capacity” from automatically meaning “instant full-power transfer.”

## 9. Static Reservoir

Static Reservoir is storage-limited electrical behavior.

Required future model:
- charge/capacity state;
- recharge source;
- recharge rate;
- discharge route;
- output envelope;
- grounding/conductivity context.

Boundary:
Static Reservoir does not become Lightning Conduit by increasing its meter.

## 10. Lightning Conduit

Lightning Conduit is primarily a routing/throughput ability.

It requires an existing electrical source or compatible stored charge.

It should track:
- source energy/charge availability;
- source-to-path coupling;
- path throughput;
- branch count;
- transfer duration;
- path losses where modeled.

It does not need a generalized personal energy reserve by default.

## 11. Cryo Sink

Cryo Sink transfers thermal energy out of a target region into a bounded THERMAL_RESERVE.

Required relation:
`thermal_stored_gain <= thermal_removed_from_target`

subject to capture efficiency.

The reserve cannot silently become:
- electricity;
- kinetic output;
- Focus;
- generic ability power.

A later thermal-release route must be explicitly authored.

## 12. Momentum Bank

Momentum Bank accepts a bounded portion of qualifying kinetic energy.

Required relation:
`kinetic_stored_gain <= kinetic_energy_accepted_from_event`

The normal event resolver still handles any unaccepted portion.

The reserve stores usable kinetic-energy-equivalent according to the parent law.

Still open:
- whether stored state carries directional metadata;
- release efficiency;
- recoil/counter-force treatment;
- decay.

These are child decisions, not implementation assumptions.

## 13. Energy Devour

Energy Devour requires an explicit input whitelist.

Proposed source categories may only be added through review.

For each allowed category define:
- source type;
- measurement model;
- conversion efficiency;
- input-rate limit;
- special incompatibilities;
- resulting generalized-reserve gain.

The generalized reserve still needs explicit output routes.

“Stored energy” alone does not authorize:
- arbitrary electricity;
- arbitrary heat;
- arbitrary kinetic force;
- matter creation;
- core-resource restoration.

## 14. Matter Recode

Matter Recode requires an energy budget appropriate to the requested molecular/material transformation.

This standard does not assume its budget is the same reserve owned by Energy Devour.

Before implementation define:
- valid source classes;
- required energy estimate model;
- transfer/consumption timing;
- incomplete-operation behavior;
- whether energy can come from prepared infrastructure.

Mass conservation remains governed by the Matter Recode ability law.

## 15. World Gate

World Gate uses major EXTERNAL_ENERGY_BUDGET rather than a default personal reserve.

A gate operation eventually needs:
- energy-source identity;
- available supply;
- startup cost;
- sustain cost;
- aperture/throughput relationship;
- endpoint/frame energy correction from the spatial standard;
- shutdown margin;
- accounting when opening fails.

Gate infrastructure cannot spend the same stored external energy twice.

## 16. Cross-ability transfer

Default:
One ability's reserve is not automatically readable, writable, drainable, or shareable by another ability.

Cross-ability reserve interaction requires:
- explicit compatibility;
- ownership rule;
- transfer direction;
- rate;
- efficiency;
- consent/targeting rule where applicable;
- save/state handling.

This prevents accidental universal energy interoperability.

## 17. Ledger events

Future authoritative accounting should be reconstructable through events containing:
- event ID;
- source ID;
- destination reserve/system;
- energy/reserve type;
- requested amount;
- accepted amount;
- efficiency;
- resulting stored amount;
- reason for rejected amount;
- ability/technique ID;
- world time;
- save transaction/version.

This can be implemented as events, state transitions, or another deterministic form; the exact runtime architecture is deferred.

## 18. Save/load invariants

Save/load must preserve:
- reserve current values;
- capacities if dynamic;
- lockout/overload state;
- active transfer state if saving mid-transfer is legal;
- external-source depletion;
- gate infrastructure energy state;
- last processed accounting transaction where needed for deduplication.

A transfer may not execute twice because a save is loaded.

## 19. Projection rule

Player-safe Status may show an ability-specific reserve only if:
- the character legitimately knows/senses it;
- the projection contract permits it.

The UI must not infer reserve capacity or hidden source state from effects.

Debug/accounting views must remain separate.

## 20. Required tests

Minimum future tests:
- capacity clamp/rejection is deterministic;
- rate limit works independently from capacity;
- conversion never creates net-positive output without an external source;
- Static Reservoir cannot become a generic reserve;
- Lightning Conduit fails without a valid source/path;
- Cryo Sink cannot spend thermal reserve through an unauthored output type;
- Momentum Bank cannot capture static/non-qualifying force as kinetic reserve;
- Energy Devour rejects unsupported source types;
- generalized energy reserve cannot restore core resources without an explicit rule;
- Matter Recode cannot consume the same source energy twice;
- World Gate startup/sustain costs reconcile with its infrastructure source;
- save/load cannot duplicate transfers or refill reserves.

## 21. Remaining design gates

This standard resolves the shared accounting vocabulary.

Still open:
- numeric units and capacities;
- per-ability efficiencies;
- exact reserve decay;
- overload outcomes;
- Momentum Bank directional/release model;
- Energy Devour whitelist/output routes;
- Matter Recode energy estimator;
- World Gate startup/sustain formula;
- spatial-frame energy correction.

No ability is canon-promoted by this standard.
