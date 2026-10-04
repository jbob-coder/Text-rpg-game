# THE GAME — Cryo Sink Thermal Transfer & Reserve Standard

Status: **PROVISIONAL CHILD STANDARD / NOT CANON UNTIL OWNER REVIEW / NOT IMPLEMENTED**

Parents:
- `ABILITY_ENERGY_RESERVE_ACCOUNTING_STANDARD.md`
- `calibration/PRIMARY_ABILITY_DETAIL_RARE_001_005.md`
- `calibration/ABILITY_TECHNIQUE_DETAIL_RARE_001_010.md`
- `RARE_ABILITY_RARITY_OVERLAP_AUDIT_001_010.md`

Scope:
- `ABILITY_RAR_004 Cryo Sink`
- techniques `TECH_RAR_004_T1`–`T4`

Purpose: resolve the non-numeric structure for thermal extraction, transfer geometry, thermal-reserve accounting, saturation, conduction/spillover, thermal shock, and reserve lifecycle boundaries.

## 1. Core law

Cryo Sink removes thermal energy from one valid bounded target region and transfers an accepted portion into a finite personal `THERMAL_RESERVE`.

It does not:
- create an independent “cold” substance;
- set arbitrary temperature directly;
- remove unlimited heat instantly;
- ignore insulation/material/geometry;
- create net usable energy;
- automatically release stored heat as an attack;
- become Heat Shaping.

## 2. Thermal source state

A valid extraction target needs enough authoritative thermal state to evaluate:
- target region/volume or bounded surface/body region;
- material/state class;
- current thermal condition;
- surrounding environment;
- transfer boundary/contact geometry;
- insulation/barrier state;
- current extraction transaction;
- safety/condition constraints where applicable.

Exact physical temperature/energy units remain a parent physics/numeric decision.

The game may use physical units or a validated abstract thermal model, but the chosen model must conserve the same conceptual accounting.

## 3. Extraction accounting

Required invariant:

`accepted_thermal_input <= thermal_energy_removed_from_target`

and

`thermal_reserve_gain <= accepted_thermal_input`.

If capture/transfer efficiency is below 100%, the difference is a modeled loss, not a second usable reserve.

The target's thermal state changes only by the amount actually resolved through the extraction transaction.

## 4. Temperature versus stored energy

Cryo Sink should not store “degrees of cold.”

The reserve represents thermal-energy-equivalent removed from targets.

Why:
- equal temperature changes can require different energy for different materials/masses;
- a small metal component and a large body of water cannot be treated as identical merely because both change by the same temperature amount;
- thermal mass matters to transfer.

Final formula remains `TBD`.

## 5. Transfer path

Extraction requires a valid ability-mediated thermal transfer relationship between user and target.

A future transaction must identify:
- target;
- bounded extraction region;
- effective transfer geometry;
- transfer-rate limit;
- target/material transfer limit;
- insulation/barrier effect;
- reserve free capacity;
- technique envelope;
- requested extraction;
- accepted extraction.

The ability may mediate the transfer without ordinary direct contact if its final range permits, but it does not make material/insulation irrelevant.

Exact range remains `TBD`.

## 6. Material / thermal-mass behavior

Different target materials/states may respond differently due to:
- thermal mass;
- conductivity;
- phase/state;
- geometry;
- surrounding heat flow;
- insulation.

The ability's control does not eliminate those distinctions.

A future parent thermal model must define enough categories or physical values to make those differences deterministic.

## 7. Insulation

Insulation is a transfer-rate/eligibility factor.

A sufficiently insulating boundary may:
- reduce extraction rate;
- require more Focus/control;
- prevent the desired region from being targeted effectively;
- force extraction from an accessible outer region instead.

Cryo Sink does not automatically bypass every insulating layer.

## 8. Environmental refill / conduction

Cooling one region creates a thermal gradient.

After or during extraction, ordinary world thermal behavior may cause:
- heat flow from neighboring material;
- ambient warming;
- convection;
- conduction;
- phase/state changes.

Cryo Sink does not freeze surrounding heat flow unless a technique explicitly maintains extraction.

This is especially important for `Sustained Extraction`.

## 9. Precision Sink — T2

`TECH_RAR_004_T2 Precision Sink` reduces the intended extraction region.

It improves spatial/thermal control; it does not disable ordinary heat conduction.

Required behavior:
- target region is smaller/more selective;
- spillover from the ability's own target selection is reduced;
- subsequent natural conduction may still spread cooling effects;
- hidden/internal target structure cannot be selected without legitimate targeting knowledge/perception.

Precision is not omniscient internal targeting.

## 10. Sustained Extraction — T3

`TECH_RAR_004_T3 Sustained Extraction` maintains repeated/continuous extraction while:
- the target remains valid;
- transfer path remains valid;
- reserve capacity remains;
- user resources/control remain;
- no hard safety/failure condition terminates it.

The resolver must re-evaluate changing thermal state over time.

As the target cools, extraction conditions may change.

The technique cannot assume a constant transfer rate indefinitely.

## 11. Emergency Heat Pull — T4

`TECH_RAR_004_T4 Emergency Heat Pull` permits a higher short-duration extraction-rate envelope.

It increases risk from:
- thermal shock;
- brittle/fracture behavior in susceptible materials;
- rapid phase/state changes where modeled;
- reserve overload/saturation;
- user strain/injury;
- unintended nearby thermal gradients.

It does not bypass reserve capacity or target physics.

## 12. Thermal shock

Rapid temperature change can be hazardous independently of final temperature.

A future thermal-shock check may depend on:
- extraction rate;
- material/tissue type;
- target geometry;
- existing damage;
- current temperature/state;
- technique envelope.

Exact thresholds remain `TBD`.

For living targets, medical/biological injury authority remains separate from the ability's thermal-control state.

## 13. Living-target boundary

Cryo Sink can only affect living tissue if the parent ability/canon ultimately permits that target class.

If permitted:
- cooling does not become healing by default;
- hypothermia/cold injury remain possible;
- blood flow/metabolism can redistribute heat;
- precise medical use requires relevant knowledge and world policy;
- the ability does not diagnose hidden conditions automatically.

This standard does not by itself approve unrestricted living-target use.

## 14. Reserve capacity

`THERMAL_RESERVE` has a hard finite capacity.

When incoming accepted extraction would exceed remaining capacity:
- only the allowed amount can be stored;
- extraction must clamp/terminate or follow an explicitly authored overload outcome;
- the target does not lose heat that the transaction failed to accept unless another modeled loss route explicitly accounts for it.

UI splitting/repeated toggling cannot bypass capacity.

## 15. Input-rate limit

Capacity and extraction rate are separate.

An empty reserve does not imply the user can absorb arbitrarily large heat flow instantly.

Effective extraction is constrained by:
- ability input-rate envelope;
- technique envelope;
- transfer path/material;
- reserve capacity;
- user control/resources.

## 16. Reserve output prohibition

Current Wave-001 Cryo Sink techniques define extraction/storage but **no active thermal-release technique**.

Therefore current baseline:

**THERMAL_RESERVE has no player-commanded offensive/general-purpose output route.**

It cannot automatically be spent as:
- heat blast;
- fire;
- electricity;
- kinetic force;
- Focus/Stamina/Resolve;
- generic ability power.

A later release/evolution technique would require explicit authoring, accounting, counterplay, and rarity review.

## 17. Reserve lifecycle / unloading

The ability still needs a safe lifecycle for stored thermal energy.

This standard does not silently choose one.

Allowed future design candidates include:
- gradual passive dissipation to environment;
- controlled non-combat venting;
- decay/system loss;
- recovery/rest-mediated emptying;
- another explicitly authored bounded route.

Before implementation one lifecycle rule must define:
- when unloading starts;
- transfer/loss rate;
- environmental consequences if any;
- whether user state affects it;
- save/load behavior;
- whether reserve can remain stored indefinitely.

Until that decision, indefinite storage must not be assumed.

## 18. Overload

Possible overload categories include:
- attempted extraction beyond input rate;
- attempted storage beyond capacity;
- unstable rapid extraction;
- inability to safely contain reserve state;
- user control/resource failure.

Possible consequences may include:
- forced termination;
- rejected extraction;
- reserve lockout;
- user injury/strain;
- uncontrolled safe-loss/vent event if later authored.

Exact outcomes and thresholds remain open.

## 19. Heat Shaping boundary

`ABILITY_UNC_002 Heat Shaping` redistributes existing heat between external regions.

Cryo Sink:
- uses dedicated personal thermal storage;
- supports stronger one-sided extraction;
- is capacity-limited by internal reserve.

Cryo Sink must not gain unrestricted external heat placement merely because the reserve contains thermal energy.

That would erase the rarity/domain boundary unless separately evolved and reviewed.

## 20. Energy Devour boundary

`Energy Devour` cannot automatically consume Cryo Sink's thermal reserve.

Cross-ability transfer requires:
- explicit compatibility;
- source/output authorization;
- rate;
- efficiency;
- accounting transaction.

No universal energy interoperability exists.

## 21. Save/load

Persist enough authoritative state to reconstruct:
- current thermal reserve;
- capacity if dynamic;
- lifecycle/decay state once defined;
- overload/lockout state;
- active sustained-extraction transaction if mid-action saves are legal;
- last committed extraction transaction ID.

Load must not:
- refill reserve;
- duplicate extraction;
- repeat a target cooling transaction;
- reset overload/saturation;
- erase elapsed lifecycle changes if world-time rules say they advance.

## 22. Player-safe projection

If the ability grants reserve awareness, player-safe Status may expose:
- current known reserve amount/band;
- saturation warning;
- extraction readiness;
- known overload/lifecycle warning.

It must not reveal:
- hidden target internal temperature;
- exact unseen material layers;
- hidden health/medical conditions;
- exact environmental thermal values the character cannot sense/measure.

## 23. Required future tests

- extraction cannot exceed target thermal change/accounting;
- reserve gain cannot exceed accepted thermal input;
- empty reserve does not bypass input-rate limit;
- near-full reserve clamps/terminates correctly;
- insulation affects transfer;
- Precision Sink does not disable later ordinary conduction;
- Sustained Extraction re-evaluates changing target state;
- Emergency Heat Pull increases risk rather than bypassing safety;
- thermal shock can remain distinct from final temperature;
- no active reserve-release route exists without explicit technique;
- Heat Shaping and Cryo Sink remain distinct;
- Energy Devour cannot automatically consume the reserve;
- save/load cannot duplicate target cooling or reserve gain;
- UI does not expose hidden thermal/medical state.

## 24. Remaining blockers after this standard

Resolved structurally:
- thermal-energy rather than “cold” storage;
- extraction accounting;
- transfer-path/material/insulation role;
- environmental conduction/refill;
- Precision/Sustained/Emergency technique behavior;
- thermal-shock category;
- capacity/input-rate separation;
- no-current-output-route boundary;
- cross-ability isolation;
- save/load invariants.

Still open:
- thermal/temperature unit model;
- target material/thermal-mass model detail;
- exact range;
- reserve capacity;
- extraction rates;
- capture efficiency;
- reserve lifecycle/unloading decision;
- overload thresholds/outcomes;
- living-target canon/policy;
- world medical/industrial/legal integration.

Cryo Sink remains a coherent Rare calibration record and is not canon-promoted by this standard.
