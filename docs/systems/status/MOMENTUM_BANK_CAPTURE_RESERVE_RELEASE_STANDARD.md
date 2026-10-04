# THE GAME — Momentum Bank Capture, Reserve & Release Standard

Status: **PROVISIONAL CHILD STANDARD / NOT CANON UNTIL OWNER REVIEW / NOT IMPLEMENTED**

Parents:
- `ABILITY_ENERGY_RESERVE_ACCOUNTING_STANDARD.md`
- `calibration/PRIMARY_ABILITY_DETAIL_RARE_006_010.md`
- `calibration/ABILITY_TECHNIQUE_DETAIL_RARE_001_010.md`
- `RARE_ABILITY_RARITY_OVERLAP_AUDIT_001_010.md`

Scope:
- `ABILITY_RAR_008 Momentum Bank`
- techniques `TECH_RAR_008_T1`–`T4`

Purpose: resolve the non-numeric model for kinetic-event qualification, capture, stored reserve identity, release direction, recoil/counter-force, decay, and anti-loop behavior.

## 1. Core law

Momentum Bank may:
1. accept a bounded portion of kinetic energy from a valid kinetic-transfer event;
2. store the accepted amount in a finite personal `KINETIC_RESERVE`;
3. later spend stored energy through a valid controlled physical release.

It does not create net kinetic energy.

## 2. Qualifying kinetic event

A qualifying event must involve actual relative motion and kinetic-energy transfer at a valid coupling boundary.

Baseline examples:
- an incoming impact against the user;
- collision through a held/controlled object;
- a moving load striking or transferring motion through a valid contact;
- other explicitly authored kinetic-transfer events.

Not qualifying by default:
- static pressure;
- stationary compression;
- ordinary gravity while standing still;
- heat;
- electricity;
- sound merely because it carries energy;
- self-generated motion recaptured only to create a loop.

## 3. Self-generation anti-loop rule

The user cannot create net reserve by:
1. spending bodily/ability energy to create motion;
2. immediately recapturing that same self-generated motion;
3. repeating the loop for positive gain.

If self-generated motion ever becomes partially capturable for a specific technique or world interaction:
- the full source cost must be accounted;
- conversion efficiency must remain below or equal to the original accepted energy;
- losses and bodily cost remain real;
- no positive-energy cycle is permitted.

Current baseline:
**ordinary self-generated motion is not a qualifying deposit source.**

## 4. Capture transaction

A capture attempt must identify:
- kinetic event ID;
- event source;
- contact/coupling point;
- estimated available kinetic-energy-equivalent;
- requested capture;
- input-rate limit;
- remaining reserve capacity;
- accepted capture;
- unaccepted residual event energy;
- Stamina cost;
- failure/overload result.

Required invariant:

`stored_gain <= accepted_kinetic_input <= qualifying_event_energy`

subject to capture efficiency.

## 5. Residual force/event behavior

Momentum Bank does not automatically nullify an impact.

Any portion that is:
- outside input-rate limit;
- outside free capacity;
- rejected by technique limits;
- lost through inefficiency

continues into the ordinary collision/impact resolver.

Therefore:
- the user can still be knocked back;
- tissue/equipment can still be damaged;
- balance can still be lost;
- catastrophic impacts can exceed safe capture.

## 6. Reserve identity

Provisional design decision:

`KINETIC_RESERVE` stores **scalar kinetic-energy-equivalent**, not a persistent vector-momentum record.

Consequences:
- individual deposit direction is not preserved as a mandatory release direction;
- the user may choose a later valid release direction through an approved physical action;
- the reserve still cannot exceed stored energy accounting;
- changing release direction is part of the ability's authored law, not free energy creation.

This choice matches the existing `Controlled Release` technique, which explicitly permits a chosen physical action/direction.

Owner review is still required before canon.

## 7. Why vector momentum is not stored by default

A vector-per-deposit model would require:
- persistent direction per deposit;
- vector cancellation/addition;
- frame transforms;
- multi-deposit vector bookkeeping;
- release restrictions tied to historical directions.

That is possible but conflicts with the current technique wording implying flexible chosen-direction release.

Therefore the scalar-energy model is the preferred provisional baseline.

## 8. Release routes

Baseline valid release requires a controlled physical action by the user.

Examples of route classes:
- direct contact strike/push;
- braced shove;
- movement impulse through the user's body;
- transfer into a held/controlled physical object at contact.

Not authorized by default:
- remote invisible force blast;
- arbitrary ranged kinetic beam;
- telekinetic manipulation;
- persistent force field;
- gravity control.

Any ranged release would require a separately authored technique/evolution.

## 9. Release transaction

A release must identify:
- reserve amount before release;
- requested spend;
- output-rate limit;
- chosen action/route;
- release direction;
- coupling target or movement action;
- release efficiency;
- accepted output;
- loss;
- resulting reserve;
- recoil/strain result.

Invariant:

`delivered_kinetic_output <= reserve_spent`

unless another separately authored energy source contributes.

## 10. Release efficiency

Release efficiency is finite.

Potential loss channels may include:
- poor alignment;
- body/equipment deformation;
- heat;
- sound;
- uncontrolled motion;
- system loss.

Exact coefficients remain `TBD`.

Loss does not automatically become another usable reserve.

## 11. Recoil / counter-force

Control does not imply recoil immunity.

When stored kinetic energy is delivered through a physical action:
- the user's stance/body/equipment must support the release;
- equal/opposing mechanical consequences are resolved through the world physics/action model as applicable;
- excessive release can destabilize or injure the user;
- poor bracing can waste output or redirect consequences.

The ability may manage energy release but does not make the user's tissues infinitely strong.

## 12. Controlled Release — T2

`TECH_RAR_008_T2 Controlled Release`:
- spends a bounded reserve amount;
- uses one deliberate physical action;
- permits chosen direction within that action;
- respects current output-rate and body/equipment limits.

Failure cases:
- bad alignment;
- weak coupling;
- insufficient reserve;
- excessive requested release;
- unstable footing;
- unsuitable held object.

## 13. Multi-Deposit Bank — T3

`TECH_RAR_008_T3 Multi-Deposit Bank`:
- allows several qualifying external kinetic events to contribute to one scalar reserve;
- does not create separate independent reserve pools by default;
- checks capacity and input rate on every deposit;
- preserves one authoritative reserve amount.

Multiple deposits do not multiply the reserve ceiling.

## 14. Reserve Burst — T4

`TECH_RAR_008_T4 Reserve Burst`:
- spends a large bounded fraction of current reserve in one controlled action;
- remains limited by output rate, bodily/equipment coupling, and safe-control envelope;
- carries increased recoil/collateral/strain risk.

It is not:
- an unlimited explosion;
- a ranged omnidirectional shockwave by default;
- a reserve-cap bypass.

## 15. Impact Cushion interaction

`ABILITY_COM_009 Impact Cushion` dissipates impact and does not store usable energy.

If both effects can interact with one incoming event, the event energy must be partitioned once.

Required rule:

`captured_energy + dissipated_energy + residual_energy + modeled_losses <= incoming_event_energy`

The same joule-equivalent cannot be both banked and dissipated.

Exact priority/order between effects remains implementation/design integration work, but duplication is forbidden.

## 16. Other defensive-system interaction

Armor, bracing, shields, passive resistance, and Momentum Bank can all affect one event at different stages.

Future event resolution must define order.

Baseline principle:
- no stage may re-read the original full event after an earlier stage already removed/redirected a portion;
- every stage receives the current residual state.

This prevents stacked defensive systems from each claiming 100% of one impact.

## 17. Saturation

When reserve capacity is full:
- further deposits cannot increase stored reserve;
- excess kinetic event energy remains in the ordinary event resolver;
- the system may reject capture or enter overload depending on future technique/numeric rules.

Opening UI, splitting events, or save/reload cannot bypass saturation.

## 18. Input-rate overload

A reserve may have free capacity but still be unable to accept one very fast/large event.

Therefore:
- capacity and input rate remain separate;
- huge impact may exceed capture rate;
- residual energy still applies.

This prevents a large empty reserve from automatically making the user safe from any collision.

## 19. Output-rate overload

Likewise, stored energy cannot necessarily be released instantly.

The output-rate limit constrains:
- T2 Controlled Release;
- T4 Reserve Burst;
- any later release technique.

A Burst may have a higher envelope than T2 without removing the ceiling.

## 20. Reserve decay

Provisional preferred baseline:
the reserve is **not assumed perfectly permanent**.

A future decay model should define:
- decay start condition;
- time basis;
- rate/curve;
- whether active stabilization costs Stamina/Focus;
- whether decay becomes harmless system/environmental loss.

Exact decay and even final presence of non-zero passive decay remain owner-review items.

Until approved, documents must not assume indefinite storage.

## 21. Reference-frame boundary

Because stored reserve is scalar energy, deposit direction does not require persistent reference-frame storage.

However:
- incoming-event kinetic calculation still needs the ordinary world physics/reference frame;
- release movement still occurs in the current physical frame;
- vehicle/platform interactions must respect the spatial/reference-frame standard.

The ability does not erase ordinary frame physics.

## 22. Save/load

Persist:
- reserve amount;
- capacity if dynamic;
- saturation/lockout state;
- last authoritative update time needed for decay;
- active release/capture transaction marker if mid-event saving is legal.

Do not persist a fake directional vector under the scalar-reserve baseline.

Loading must not:
- refill reserve;
- duplicate a deposit;
- repeat a release;
- reset saturation;
- skip elapsed decay if the parent world-time/save policy says decay advances.

## 23. Player-safe projection

If the character legitimately senses their reserve, UI may expose:
- current known reserve amount/band;
- saturation warning;
- known release readiness.

UI must not expose:
- hidden incoming-event energy;
- exact enemy attack energy;
- invisible collision data;
- future impact values.

## 24. Required tests

Future minimum tests:
- static pressure cannot be banked;
- self-generated motion loop cannot create net reserve;
- capture never exceeds qualifying event energy;
- capacity and input rate are separate;
- residual impact still resolves;
- multiple deposits share one reserve ceiling;
- release never exceeds reserve spent;
- release direction can differ from deposit direction under scalar model;
- remote force blast is unavailable without a specific technique;
- user can suffer recoil/strain;
- Impact Cushion and Momentum Bank cannot double-claim the same energy;
- save/load cannot duplicate deposit/release;
- saturation cannot be bypassed;
- UI does not reveal hidden kinetic-event values.

## 25. Remaining blockers after this standard

Resolved structurally:
- qualifying-event baseline;
- self-generation anti-loop rule;
- scalar versus vector reserve decision;
- release-route baseline;
- capture/release accounting;
- recoil/counter-force treatment;
- multi-deposit semantics;
- Impact Cushion energy partition;
- saturation/input-output rate separation;
- save/load behavior.

Still open:
- final owner approval of scalar-reserve model;
- reserve capacity;
- input/output rates;
- capture/release efficiency;
- decay rule/coefficients;
- exact bodily/recoil thresholds;
- detailed world/industrial/legal integration.

Momentum Bank remains a coherent Rare calibration record and is not canon-promoted by this standard.
