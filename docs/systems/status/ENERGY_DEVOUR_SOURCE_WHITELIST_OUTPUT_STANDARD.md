# THE GAME — Energy Devour Source Whitelist & Output Authorization Standard

Status: **PROVISIONAL CHILD STANDARD / NOT CANON UNTIL OWNER REVIEW / NOT IMPLEMENTED**

Parents:
- `ABILITY_ENERGY_RESERVE_ACCOUNTING_STANDARD.md`
- `calibration/PRIMARY_ABILITY_DETAIL_SUPER_RARE_001_006.md`
- `calibration/ABILITY_TECHNIQUE_DETAIL_SUPER_RARE_001_006.md`

Scope:
- `ABILITY_SRR_006 Energy Devour`
- techniques `TECH_SRR_006_T1`–`T4`

Purpose: define how energy-type compatibility is whitelisted, how incompatible sources are rejected, how conversion enters a generalized reserve, and which reserve outputs are authorized by default.

## 1. Core law

Energy Devour may absorb only explicitly compatible **non-biological** energy inputs and convert part of accepted input into a finite `GENERAL_ENERGY_RESERVE`.

It is not universal energy negation.

Required invariant:

`general_reserve_gain <= accepted_input_energy`

subject to conversion efficiency.

## 2. Compatibility-state vocabulary

Every source class uses one of these states:

- `PROVISIONALLY_COMPATIBLE` — coherent with the current ability identity, still awaiting owner/numeric review;
- `REQUIRES_CHILD_REVIEW` — not usable until a dedicated interaction model exists;
- `EXCLUDED` — outside the current ability law by default.

No unlisted type is implicitly compatible.

## 3. Provisional input whitelist

### ELECTRICAL_ENERGY
Status: `PROVISIONALLY_COMPATIBLE`.

Requirements:
- actual electrical source/charge flow;
- valid coupling;
- finite input rate;
- reserve capacity;
- conversion loss.

Boundary:
Energy Devour removes/converts electrical energy rather than routing it like Lightning Conduit.

### THERMAL_ENERGY
Status: `PROVISIONALLY_COMPATIBLE`.

Requirements:
- actual transferable heat/thermal flux;
- valid contact/range/coupling rule;
- finite extraction/conversion rate;
- reserve capacity.

Boundary:
Energy Devour does not gain Cryo Sink's precise thermal-domain control or thermal-specific reserve behavior merely because heat is compatible.

### NON_IONIZING_RADIANT_ENERGY
Status: `PROVISIONALLY_COMPATIBLE`.

Candidate scope:
- visible/infrared/microwave or other explicitly modeled non-ionizing radiant input once the world physics/content model distinguishes them.

Boundary:
absorption does not grant light-path control, invisibility, imaging, or arbitrary electromagnetic manipulation.

## 4. Inputs requiring dedicated child review

### KINETIC_MECHANICAL_ENERGY
Status: `REQUIRES_CHILD_REVIEW`.

Reason:
Momentum Bank already owns a specific kinetic capture/storage identity.

Energy Devour must not absorb kinetic impacts by default until cross-tier overlap, coupling, recoil, and world-physics consequences are separately approved.

### ACOUSTIC_ENERGY
Status: `REQUIRES_CHILD_REVIEW`.

Reason:
requires an authored sound-energy measurement/coupling model and overlap review with sound-domain abilities.

### IONIZING_RADIATION
Status: `REQUIRES_CHILD_REVIEW`.

Reason:
requires radiation injury, shielding, measurement, conversion, and world-safety rules.

### CHEMICAL_POTENTIAL_ENERGY
Status: `REQUIRES_CHILD_REVIEW`.

Reason:
extracting usable energy from matter/fuel may imply chemical transformation rather than direct energy absorption.

A separate matter/chemistry interface is required.

## 5. Excluded input classes

Current default `EXCLUDED` classes:

- biological life force;
- Health;
- Stamina;
- Focus;
- Resolve;
- memories;
- emotions;
- souls/identity;
- Status effects;
- Level/XP;
- primary abilities;
- passives;
- time;
- space;
- gravity as an abstract field quantity;
- causal state;
- probability;
- laws/concepts;
- information;
- nuclear binding energy simply because matter exists;
- arbitrary mass-energy conversion.

Any future exception requires explicit higher-order design review.

## 6. Biological boundary

The ability may interact with non-biological energy physically present near living targets, but it does not drain biological vitality by default.

Examples:
- electrical current in external equipment can be a source;
- a person's Health/Stamina is not an energy source;
- metabolic energy is not directly drainable;
- neural electrical activity is not an approved target under this standard.

This prevents drift into life-force absorption or mind disruption.

## 7. Source record

Every intake requires:
- source ID;
- source type;
- compatibility state;
- available energy/supply state;
- source transfer-rate limit;
- coupling state;
- requested intake;
- accepted intake;
- conversion efficiency;
- reserve gain;
- rejected/lost amount;
- overload/failure result.

## 8. Conversion Filter — T2

`TECH_SRR_006_T2 Conversion Filter` improves handling of one known compatible type.

It may:
- validate the expected source type;
- reject/terminate clearly incompatible input;
- reduce conversion instability for a practiced compatible type.

It does not:
- make an excluded type compatible;
- identify every unknown energy source perfectly;
- remove overload risk;
- raise efficiency above future hard limits automatically.

## 9. Sustained Intake — T3

`TECH_SRR_006_T3 Sustained Intake` continuously processes one compatible source while:
- coupling remains valid;
- source remains available;
- input-rate limits are respected;
- reserve capacity remains;
- user control remains stable.

Dynamic source changes require revalidation.

## 10. Multi-Source Devour — T4

`TECH_SRR_006_T4 Multi-Source Devour` may process several simultaneously compatible sources.

Rules:
- every source is independently classified;
- each has its own input-rate limit;
- aggregate conversion remains below total reserve/input envelope;
- mixed-source instability is a real failure mode;
- one unsupported source can force rejection or destabilization according to future rules.

Multiple sources do not create multiple reserve ceilings.

## 11. Generalized reserve identity

`GENERAL_ENERGY_RESERVE` is a normalized ability-specific reserve.

It is not automatically:
- electricity;
- heat;
- kinetic energy;
- Stamina;
- Focus;
- Resolve;
- matter.

The ability's conversion process abstracts compatible inputs into one reserve state.

That abstraction does not authorize arbitrary reconstruction into every input type.

## 12. Output authorization states

Every possible reserve output uses one of:

- `AUTHORIZED_BASELINE`;
- `REQUIRES_OUTPUT_TECHNIQUE`;
- `EXCLUDED`.

## 13. Authorized baseline outputs

### CONTAINMENT / INTAKE SUPPORT
Status: `AUTHORIZED_BASELINE`.

The reserve may exist as the bounded storage state required to continue absorbing until capacity is reached.

This does not create an external effect.

### SAFE_DISSIPATION / EMERGENCY VENT
Status: `AUTHORIZED_BASELINE` as a design safety function.

Purpose:
allow stored reserve to be deliberately discarded into non-usable modeled loss under conditions that do not create a combat output.

This is not:
- a blast;
- an attack;
- a resource transfer;
- free environmental heating/electricity unless a later route explicitly models that consequence.

Exact vent timing/safety remains `TBD`.

## 14. Outputs requiring explicit techniques

### EXTERNAL_DEVICE_OR_INFRASTRUCTURE_TRANSFER
Status: `REQUIRES_OUTPUT_TECHNIQUE`.

Would require:
- target compatibility;
- output type;
- conversion path;
- rate;
- efficiency;
- authorization/safety;
- world-infrastructure rules.

Not available merely because reserve exists.

### CONTROLLED_OFFENSIVE_RELEASE
Status: `REQUIRES_OUTPUT_TECHNIQUE`.

Would require a separately authored technique defining:
- output form;
- range;
- coupling;
- rate;
- recoil/collateral;
- counters.

No generic “energy blast” exists by default.

### OUTPUT_AS_SPECIFIC_ENERGY_TYPE
Status: `REQUIRES_OUTPUT_TECHNIQUE`.

Converting generalized reserve back into:
- electricity;
- heat;
- light;
- kinetic output

requires an explicit authorized route and efficiency.

Input compatibility does not imply output compatibility.

## 15. Excluded outputs

Default `EXCLUDED`:
- restore Health directly;
- restore Stamina directly;
- restore Focus directly;
- restore Resolve directly;
- create matter;
- fuel another primary ability automatically;
- copy another ability;
- produce time/space/gravity effects;
- produce Status/admin effects;
- create unlimited self-sustaining conversion loops.

## 16. Cross-ability transfer

Default:
other abilities cannot read or spend `GENERAL_ENERGY_RESERVE`.

A future cross-ability route requires:
- explicit compatibility;
- direction;
- rate;
- efficiency;
- ownership;
- save/load behavior;
- exploit review.

This prevents Energy Devour from becoming a universal battery for the entire ability system.

## 17. Capacity and rate

Separate:
- reserve capacity;
- per-source input rate;
- aggregate input rate;
- conversion rate;
- future output rate.

A large reserve does not allow instantaneous absorption of an overwhelming source.

Excess source energy remains in the source/world event and can injure the user.

## 18. Conversion efficiency

For every compatible type:

`reserve_gain = accepted_input × type_conversion_efficiency`

Default design expectation:
efficiency is below 100%.

Exact values remain `TBD`.

Different source types may have different efficiencies and instability risk.

## 19. Mixed-source instability

T4 does not imply all compatible types mix safely at maximum rate.

Future model should consider:
- number of simultaneous sources;
- type combination;
- total conversion load;
- user's mastery/control;
- reserve fill state.

Failure may produce:
- forced termination;
- harmful leakage;
- reserve rupture;
- source-specific injury;
- loss of stored reserve.

## 20. Saturation / overload

At or near capacity:
- new intake is reduced/rejected;
- user cannot hide overflow in another reserve;
- excessive source energy remains dangerous;
- emergency vent may be required.

Save/load cannot reset saturation.

## 21. Source depletion

Absorbed energy is removed from the source according to the authoritative source model.

Examples:
- electrical storage/source loses supplied energy;
- heat source cools only according to accepted thermal transfer;
- radiant input no longer continues past the absorbed amount/path.

The same energy cannot remain fully available to both the source and reserve.

## 22. Boundary with Lightning Conduit

Lightning Conduit:
- routes electrical energy through selected conductive paths;
- does not convert it into a generalized reserve.

Energy Devour:
- absorbs compatible electrical input;
- removes/consumes source energy;
- converts part into generalized reserve;
- loses some through conversion.

Neither subsumes the other.

## 23. Boundary with Cryo Sink

Cryo Sink:
- specializes in strong thermal extraction;
- stores thermal-specific reserve;
- remains a heat-domain ability.

Energy Devour:
- may accept thermal energy as one compatible input;
- converts it into generalized reserve;
- lacks Cryo Sink's specialist thermal control by default.

## 24. Boundary with Momentum Bank

Current baseline:
kinetic/mechanical input is **not approved** for Energy Devour.

Momentum Bank therefore remains the kinetic capture/storage specialist.

Any future kinetic compatibility proposal must pass explicit overlap review.

## 25. Save/load

Persist:
- reserve amount;
- capacity/state if dynamic;
- known compatibility discoveries if progression tracks them;
- active sustained-intake transaction if mid-process save is legal;
- source depletion transaction markers;
- overload/lockout state;
- last committed conversion event.

Loading cannot:
- duplicate source energy;
- refill reserve;
- repeat conversion;
- erase overload.

## 26. Player-safe projection

The character may see:
- known reserve amount/band;
- known compatible types they have legitimately learned;
- saturation/instability warnings if the ability provides them.

UI must not expose:
- hidden source capacity;
- unknown energy type identity;
- future whitelist entries;
- internal conversion coefficients unless legitimately learned.

## 27. Required tests

Future minimum tests:
- excluded biological resource cannot be absorbed;
- unsupported type is rejected;
- compatible source loses accepted energy;
- reserve gain never exceeds accepted input;
- different compatible types can use different efficiencies;
- capacity and input rate are separate;
- T4 validates each source independently;
- mixed-source overload can fail;
- no core-resource restoration;
- no universal ability-fueling;
- no arbitrary external energy blast;
- kinetic input remains rejected under current baseline;
- save/load cannot duplicate source depletion/conversion;
- hidden whitelist information does not leak.

## 28. Remaining blockers after this standard

Resolved structurally:
- whitelist-state vocabulary;
- initial provisional compatible classes;
- dedicated-review classes;
- excluded domains;
- biological boundary;
- generalized reserve identity;
- baseline output authorization;
- cross-ability transfer default;
- source depletion;
- Lightning/Cryo/Momentum boundaries.

Still open:
- owner approval of provisional whitelist;
- exact efficiencies;
- capacity/rates;
- radiant-energy subtypes;
- acoustic/ionizing/chemical review if desired;
- external output techniques, if any;
- overload thresholds;
- world infrastructure/regulation/history.

Energy Devour remains a Super Rare calibration record and is not canon-promoted by this standard.
