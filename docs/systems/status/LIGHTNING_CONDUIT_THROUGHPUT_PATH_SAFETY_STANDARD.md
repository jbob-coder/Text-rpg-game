# THE GAME — Lightning Conduit Throughput, Path & Safety Standard

Status: **PROVISIONAL CHILD STANDARD / NOT CANON UNTIL OWNER REVIEW / NOT IMPLEMENTED**

Parents:
- `ABILITY_ENERGY_RESERVE_ACCOUNTING_STANDARD.md`
- `calibration/PRIMARY_ABILITY_DETAIL_RARE_001_005.md`
- `calibration/ABILITY_TECHNIQUE_DETAIL_RARE_001_010.md`
- `CANON_REVIEW_DRY_RUN_ABILITY_RAR_003.md`

Scope:
- `ABILITY_RAR_003 Lightning Conduit`
- techniques `TECH_RAR_003_T1`–`T4`

Purpose: resolve the non-numeric routing model that blocked Lightning Conduit from advancing beyond its dry canon review.

## 1. Core electrical-routing rule

Lightning Conduit never creates electrical energy.

Every route must identify:
- one valid electrical source;
- one source connection/coupling point;
- one or more permitted conductive path segments;
- one or more destinations/sinks;
- requested transfer;
- accepted transfer;
- modeled losses;
- overload/safety result.

Energy accounting remains governed by the shared reserve standard.

## 2. Source classes

Provisional compatible source classes:
- `STORED_CHARGE` — compatible bounded charge such as Static Reservoir output;
- `LIVE_ELECTRICAL_SOURCE` — powered electrical infrastructure/device;
- `TRANSIENT_ELECTRICAL_EVENT` — an already occurring electrical discharge that can be validly coupled.

A source must already exist.

The ability cannot:
- energize an unpowered network from nothing;
- treat ordinary matter as a power source;
- draw unlimited energy from “the environment.”

## 3. Conductive path graph

The authoritative resolver should represent the candidate route as a conductive graph.

Each segment needs enough conceptual data to evaluate:
- material/conductivity class;
- continuity;
- geometry/length;
- grounding relationship;
- insulation/barrier state;
- current load;
- safe-load envelope if known;
- connection to neighboring segments.

Exact electrical units are deferred.

## 4. Path selection

The user selects a desired route only from paths they can validly target/control under the ability's perception/knowledge rules.

The system validates the route against the actual conductive graph.

The ability may improve routing control, but it does not make a nonconductive path conductive.

## 5. Path ambiguity

When multiple conductive routes exist, path ambiguity becomes a control problem.

Possible results:
- intended path accepted;
- energy divides among valid branches according to the authored routing model;
- route rejected because ambiguity exceeds control;
- unintended conductive branch receives some current;
- overload/arc event occurs if conditions warrant.

Do not assume perfect arbitrary wire-like control through every conductive object.

## 6. Branching rule

Branch Route and later techniques may intentionally select more than one branch.

Conservation requirement:
the sum of accepted branch transfer plus modeled loss cannot exceed accepted source transfer.

Branch count and total throughput are separate parameters.

A higher branch count must not create more total source energy.

## 7. Throughput model

The future numeric resolver requires separate limits for:
- source available transfer rate;
- ability-controlled transfer rate;
- per-path transfer limit;
- total simultaneous transfer limit;
- technique branch count;
- sustain duration.

The effective transfer is constrained by the lowest relevant limit.

Conceptually:

`effective_transfer_rate <= min(source_limit, ability_limit, path_limit, technique_limit)`

Exact units and coefficients remain `TBD`.

## 8. Technique envelopes

### Guided Current
- one valid source;
- one selected conductive route;
- low complexity;
- no intentional branching.

### Branch Route
- one source;
- a small bounded set of explicitly selected branches;
- total transfer still conserved;
- ambiguity and branch imbalance remain possible.

### Sustained Channel
- keeps a validated route active over time;
- topology changes can invalidate the route;
- heating/grounding/load changes can trigger revalidation or collapse.

### High-Load Route
- permits a higher controlled transfer envelope through a path network;
- does not remove source/path safety constraints;
- overload and collateral faults remain major risks.

## 9. Dynamic topology

An active route must revalidate when material conditions change materially.

Examples:
- a conductor breaks;
- a switch opens/closes;
- grounding changes;
- water/contact changes conductivity;
- an object enters/leaves contact;
- insulation fails;
- a destination device changes load state.

A sustained route cannot keep using a path that no longer exists.

## 10. Grounding and sinks

Grounding is part of the path graph.

A strong ground path may:
- attract/divert current;
- terminate a route;
- reduce current reaching an intended destination;
- create dangerous current through unexpected connected materials.

The ability may account for a known ground but does not ignore it.

## 11. Insulation

A valid insulating barrier can:
- block a path;
- increase required breakdown/arc conditions beyond the user's safe/control envelope;
- force alternate routing.

Lightning Conduit does not automatically punch through insulation.

Any future arc-jump behavior must be separately authored.

## 12. Overload

Overload may occur when requested/actual transfer exceeds:
- ability control envelope;
- source coupling safety;
- conductor/path safe load;
- destination tolerance;
- user protection/control state.

Possible consequences:
- route collapse;
- uncontrolled diversion;
- equipment damage;
- fire/thermal damage;
- user injury;
- Focus loss/strain;
- temporary lockout.

Exact thresholds remain numeric-calibration work.

## 13. User safety

Control does not imply immunity.

The user may still be endangered by:
- contact voltage/current;
- arc events;
- conductive environment;
- grounding through the body;
- heat;
- equipment failure;
- overload.

Any later defensive technique must be separately authored.

## 14. Technology boundary

Lightning Conduit controls electrical routing, not arbitrary device logic.

It cannot by itself:
- hack software;
- read encrypted data;
- issue digital commands;
- understand an unknown machine;
- bypass locks merely because electricity is present.

Any device effect results from actual electrical consequences.

## 15. Static Reservoir interaction

Static Reservoir may provide a compatible bounded stored-charge source.

Rules:
- the Reservoir's available output rate/capacity remains authoritative;
- Lightning Conduit cannot extract more charge than exists;
- routing does not increase stored charge;
- save/load cannot spend the same stored charge twice.

The two abilities remain distinct.

## 16. Save/load and transaction rules

For any active electrical transaction persist enough state to reconstruct:
- source ID;
- requested/accepted transfer;
- active route IDs/segments;
- branch allocation;
- technique ID;
- transfer time/state;
- overload/lockout state;
- last committed accounting event.

A load cannot duplicate an already committed transfer.

If active sustained routing cannot be deterministically reconstructed, saving mid-route should be disallowed until that proof exists.

## 17. Player-safe projection

The player may see only route/source information they legitimately perceive or know.

The UI must not reveal:
- hidden wiring;
- concealed conductive paths;
- unknown device internals;
- exact secret infrastructure capacity.

Debug route graphs remain separate.

## 18. Required future tests

- no source -> no transfer;
- nonconductive path rejected;
- insulated path rejected/redirected according to model;
- grounding changes the route;
- branch energy is conserved;
- branch-count cap is independent from throughput cap;
- topology change invalidates sustained routing when appropriate;
- overload can collapse/harm;
- Static Reservoir cannot be overdrawn;
- technology logic is not controlled directly;
- save/load does not duplicate transfer;
- hidden infrastructure is not leaked through player-safe projection.

## 19. Remaining blockers after this standard

Resolved at the design-structure level:
- source taxonomy;
- conductive-path graph requirement;
- branching conservation;
- topology revalidation;
- grounding/insulation role;
- overload/safety categories;
- technology boundary.

Still open:
- numeric throughput values;
- branch-count values;
- path distance;
- duration;
- overload thresholds;
- detailed electrical units/loss equations;
- world licensing/infrastructure policy.

Dry canon review remains `RETURN_FOR_REFINEMENT` until those remaining blockers are sufficiently calibrated.
