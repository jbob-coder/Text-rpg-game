# THE GAME — Momentum Bank Reserve & Release Standard

Status: **PROVISIONAL CHILD STANDARD / NOT CANON UNTIL OWNER REVIEW / NOT IMPLEMENTED**

Parents:
- `ABILITY_ENERGY_RESERVE_ACCOUNTING_STANDARD.md`
- `calibration/PRIMARY_ABILITY_DETAIL_RARE_006_010.md`
- `calibration/ABILITY_TECHNIQUE_DETAIL_RARE_001_010.md`

Scope:
- `ABILITY_RAR_008 Momentum Bank`
- techniques `TECH_RAR_008_T1`–`T4`

Purpose: resolve the non-numeric structural rules for kinetic capture, reserve metadata, release, recoil/counter-force, and decay.

## 1. Core law

Momentum Bank captures a bounded portion of kinetic energy from a qualifying motion event, stores that captured amount in a personal kinetic reserve, and later releases stored energy through a valid physical action.

It does not:
- absorb static pressure;
- absorb arbitrary force with no qualifying motion;
- erase residual impact automatically;
- create net kinetic energy;
- become a universal force reserve.

## 2. Qualifying kinetic event

A candidate deposit event needs:
- stable event ID;
- moving source/object/body;
- relative motion at the interaction;
- available kinetic-energy-equivalent;
- direction/vector context;
- contact/coupling context;
- amount requested for capture;
- amount accepted;
- residual event after capture.

The normal impact/motion resolver remains responsible for unaccepted energy.

## 3. Capture accounting

Required invariant:

`stored_gain <= accepted_kinetic_input`

and

`accepted_kinetic_input <= qualifying_event_available_input`.

Capture efficiency may be below 100%.

The ability can reduce the kinetic energy remaining in the qualifying event only by the amount actually accepted into the reserve plus explicitly modeled loss.

No hidden dissipation is assumed.

## 4. Direction metadata

Provisional structural decision:

The reserve stores **energy amount plus provenance metadata**, but not a mandatory single global direction vector.

Each deposit may record:
- source event;
- accepted amount;
- incoming direction;
- contact point or body/action context;
- capture time.

Why:
- multi-deposit banking can combine events from different directions;
- forcing the entire reserve to one vector would make later deposits ambiguous;
- allowing directionless universal force would be too broad.

Release direction is therefore chosen by a valid release action, subject to control and recoil rules.

## 5. Reserve representation

A future reserve record should support:
- current total stored amount;
- hard capacity;
- input-rate/event acceptance limit;
- output-rate limit;
- deposit ledger;
- decay state;
- overload/saturation state;
- last committed transaction ID.

The deposit ledger may be compacted later if deterministic accounting can be preserved.

## 6. Multi-deposit rule

`TECH_RAR_008_T3 Multi-Deposit Bank` allows several qualifying events to contribute to one bounded reserve.

Rules:
- each deposit is accounted once;
- total reserve cannot exceed capacity;
- a later deposit does not erase prior provenance automatically;
- saturation does not make residual incoming force disappear;
- duplicate save/load replay cannot re-credit a deposit.

## 7. Release action

Stored kinetic energy may only be released through an explicitly valid physical action or authored delivery interface.

Current baseline supports:
- body-driven strike/push/launch-like action;
- another technique-specific mechanical delivery action if separately authored.

It does not automatically support:
- remote telekinetic blasts;
- arbitrary omnidirectional force;
- electricity/heat conversion;
- direct core-resource restoration.

## 8. Controlled Release

`TECH_RAR_008_T2 Controlled Release`:
- selects a bounded release amount;
- selects a valid physical action/direction;
- applies release efficiency;
- validates body/equipment/contact capability;
- commits reserve expenditure;
- resolves recoil/counter-force;
- resolves target/world effect.

If alignment or delivery is invalid, some or all requested release may fail or be wasted according to the future numeric model.

## 9. Reserve Burst

`TECH_RAR_008_T4 Reserve Burst` permits a much larger fraction of the reserve to be released in one action.

It increases:
- delivery stress;
- recoil/counter-force risk;
- collateral risk;
- control difficulty;
- chance of reserve/ability instability.

It does not bypass:
- reserve amount;
- output-rate envelope;
- body/equipment limits;
- conservation;
- valid delivery action.

## 10. Recoil / counter-force

Structural baseline:

A release does not grant automatic recoil immunity.

The resolver must account for how the release couples to:
- user's body;
- ground/support;
- held equipment;
- target;
- environment.

Possible outcomes:
- support absorbs expected reaction;
- user is displaced/staggered;
- equipment fails/slips;
- release is capped by safe coupling;
- injury occurs;
- some requested output is rejected.

Exact mechanics remain numeric/physics calibration.

## 11. Defensive capture interaction

Momentum Bank is not a total defensive shield.

During an incoming impact:
1. normal event determines available kinetic input;
2. ability attempts bounded capture;
3. accepted capture reduces only that accepted portion;
4. residual impact continues through the normal defensive/injury system.

This preserves the boundary with `Impact Cushion`, which dissipates rather than stores.

## 12. Static pressure boundary

Static or quasi-static loading is not a valid deposit merely because force exists.

Examples that do not qualify by default:
- standing under a constant heavy load;
- sustained hydraulic pressure with no authored qualifying motion event;
- being pinned against a wall after motion has already ended.

A moving compression/impact event may contain a qualifying kinetic portion, but only that portion is eligible.

## 13. Decay

Structural proposal:
the reserve is not assumed perfectly permanent.

A future decay model may be:
- time-based leakage;
- strain-based instability;
- no decay inside a short active window followed by later decay;
- another explicitly authored bounded model.

Until selected, decay is `TBD`.

Save/load must preserve whatever decay clock/state is eventually chosen.

## 14. Capacity and overflow

When a deposit exceeds remaining capacity:
- only the accepted amount enters reserve;
- excess kinetic input remains in the original event unless another authorized resolver handles it;
- capacity cannot be bypassed by splitting one event into repeated UI actions.

Over-capacity storage is not allowed by default.

## 15. Cross-ability interaction

Default:
- Impact Cushion cannot automatically transfer dissipated energy into Momentum Bank;
- Energy Devour cannot automatically consume the kinetic reserve;
- Weight Shift cannot multiply stored energy;
- no other ability can read/write the reserve without explicit compatibility.

Any cross-ability conversion requires its own accounting rule.

## 16. Save/load

Persist:
- reserve total;
- capacity if dynamic;
- deposit transaction IDs or deterministic equivalent;
- decay state;
- saturation/lockout;
- active release transaction if mid-action saves are legal.

A deposit or release cannot execute twice after reload.

## 17. Player-safe projection

The player may see reserve information only if the ability legitimately provides reserve awareness.

Potential visible fields:
- broad reserve amount/band;
- saturation warning;
- known decay warning;
- current release readiness.

Hidden event vectors, exact physics calculations, or unseen incoming-event data must not leak through UI.

## 18. Required future tests

- static pressure cannot deposit;
- one impact deposits at most once;
- accepted capture never exceeds available kinetic input;
- residual force remains after partial capture;
- multi-deposit total respects capacity;
- opposite-direction deposits do not corrupt reserve accounting;
- Controlled Release spends reserve exactly once;
- release cannot exceed stored amount;
- recoil/counter-force is not silently ignored;
- Reserve Burst respects output and coupling limits;
- save/load cannot duplicate deposit/release;
- no automatic cross-ability reserve conversion.

## 19. Remaining blockers

Resolved structurally:
- qualifying event definition;
- deposit accounting;
- direction/provenance model;
- multi-deposit behavior;
- valid release concept;
- recoil/counter-force requirement;
- static-pressure exclusion;
- capacity/overflow behavior;
- save/load transaction invariants.

Still open:
- numeric capacity;
- capture efficiency;
- input/output rate;
- release efficiency;
- safe body/equipment coupling;
- recoil equations;
- decay model/value;
- world training/regulation.

No canon promotion occurs through this standard.
