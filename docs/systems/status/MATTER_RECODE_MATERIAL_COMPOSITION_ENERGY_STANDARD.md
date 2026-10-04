# THE GAME — Matter Recode Material, Composition & Energy Standard

Status: **PROVISIONAL CHILD STANDARD / NOT CANON UNTIL OWNER REVIEW / NOT IMPLEMENTED**

Parents:
- `ABILITY_ENERGY_RESERVE_ACCOUNTING_STANDARD.md`
- `KNOWLEDGE_EVIDENCE_CONFIDENCE_STANDARD.md`
- `calibration/PRIMARY_ABILITY_DETAIL_SUPER_EPIC_001_003.md`
- `calibration/ABILITY_TECHNIQUE_DETAIL_SUPER_EPIC_001_003.md`

Scope:
- `ABILITY_SEP_002 Matter Recode`
- techniques `TECH_SEP_002_T1`–`T4`

Purpose: define the non-numeric laws for eligible matter, composition knowledge, mass accounting, transformation models, energy cost, incomplete conversion, contaminants, product validity, and save/load.

## 1. Core law

Matter Recode rearranges **existing nonliving matter** into another permitted nonliving configuration using:
- valid source material;
- sufficiently known composition/model;
- sufficient energy;
- bounded mass/volume/complexity;
- a valid learned target configuration.

It does not:
- create mass from nothing;
- create elements not present in the allowed source model unless a later law explicitly authorizes transmutation;
- alter living organisms by default;
- produce an unknown material from imagination alone;
- bypass energy accounting;
- guarantee that a badly understood design is stable.

## 2. Matter-domain eligibility

Default eligible domain:
`NONLIVING_MATTER`.

Explicitly excluded by default:
- living tissue;
- active biological organisms;
- Status/system state;
- memories/knowledge;
- energy-only phenomena;
- spatial fields;
- ability reserves.

Ambiguous cases such as detached biological material, living cultures, composites containing active biological components, or nanobiological systems require explicit classification before use.

## 3. Source-material record

A future recode transaction should identify:
- source object/material IDs;
- authoritative mass;
- material/composition profile;
- phase/state where relevant;
- contamination/impurity profile;
- structural integrity;
- ownership/access state where world rules require it;
- source location/frame;
- quantity actually committed.

The ability cannot consume the same source mass twice.

## 4. Target-model record

A valid target configuration should eventually identify:
- model ID/version;
- required constituent materials/elements;
- allowed impurities;
- structural/chemical arrangement;
- complexity class;
- tolerances;
- intended scale;
- learned/validated knowledge provenance;
- stability constraints;
- required process energy.

The target model is knowledge, not matter.

Knowing a model does not supply missing material.

## 5. Mass conservation

Baseline invariant:

`accepted_output_mass <= committed_input_mass`

Any difference must be:
- explicitly modeled residual material;
- loss/waste;
- separately conserved byproduct.

No hidden mass generation is permitted through:
- rounding;
- repeated partial conversions;
- save/load;
- combining multiple technique passes.

If future canon permits true mass-energy conversion, that requires a separate upper-tier law and is not part of this standard.

## 6. Composition conservation

Matter Recode may rearrange source constituents but cannot silently introduce unavailable constituent matter.

For each transformation:
- required constituents must be present in valid source material or an explicitly connected source;
- contaminants remain unless separated, transformed within allowed chemistry, or placed into residual/byproduct output;
- purification cannot delete contaminant mass.

This preserves the distinction between restructuring and matter creation.

## 7. Composition knowledge

The user must know the relevant source and target composition to a defined threshold.

Knowledge may come from:
- prior study;
- valid analysis;
- trusted model/library;
- legitimate Status-confirmed information where a rule exposes it;
- another authored evidence source.

The ability does not convert engine truth directly into character knowledge.

Unknown composition can cause:
- rejection;
- partial conversion;
- unstable output;
- unexpected residue;
- excessive energy demand;
- another explicitly authored failure.

Exact thresholds remain `TBD`.

## 8. Model confidence

Composition/model knowledge should distinguish:
- known;
- inferred;
- approximate;
- uncertain;
- unknown.

A high-confidence but incorrect model can still produce a bad result.

Matter Recode does not automatically validate truth merely because activation succeeds.

## 9. Energy budget

Matter Recode uses an `EXTERNAL_ENERGY_BUDGET` or another explicitly approved source.

The transaction must identify:
- source energy ID;
- requested energy;
- accepted energy;
- transfer limit;
- transformation estimate;
- actual committed consumption;
- failure/refund/loss behavior.

No default link to Energy Devour's personal reserve is implied.

## 10. Energy estimate

The future estimator should account for enough information to distinguish:
- simple rearrangement;
- purification/separation;
- bond/structural change;
- phase change;
- high-complexity fabrication;
- multi-material composite work.

Exact physical equations may be abstracted, but relative cost must remain deterministic and cannot hide free transformation.

## 11. Incomplete operation

If the transaction stops before full completion:
- committed source mass remains accounted;
- transformed output remains only where the operation actually completed;
- unresolved input remains input/residual;
- spent energy remains spent unless a specific reversible step allows recovery;
- product validity is reevaluated.

Interruption cannot duplicate source or reset consumed energy.

## 12. Material Rewrite — T1

`TECH_SEP_002_T1 Material Rewrite`:
- small bounded quantity;
- one known source material;
- one approved target structural configuration;
- low complexity.

It is the baseline proof that the ability changes configuration without free mass creation.

## 13. Purity Pass — T2

`TECH_SEP_002_T2 Purity Pass`:
- separates/rearranges known constituents toward a cleaner approved composition;
- requires contaminant/component knowledge;
- produces residual/byproduct mass where contaminants are removed;
- cannot make impurities vanish.

Purity is bounded by source knowledge and separation capability.

## 14. Fabrication Recode — T3

`TECH_SEP_002_T3 Fabrication Recode`:
- constructs a more complex known nonliving structure;
- may require repeated local transformations;
- uses one validated target model/version;
- remains limited by mass, composition, energy, precision, and scale.

It does not substitute for unknown engineering knowledge.

## 15. Composite Rewrite — T4

`TECH_SEP_002_T4 Composite Rewrite`:
- combines several known compatible source components into one approved learned composite structure;
- tracks constituent provenance;
- respects each component's mass contribution;
- requires compatibility/stability knowledge.

This is not unrestricted synthesis of exotic fictional materials without a world-defined model.

## 16. Precision/tolerance

A recoded product is not automatically perfect.

Future output quality may depend on:
- target-model precision;
- composition confidence;
- energy sufficiency;
- user control;
- scale;
- contamination;
- environmental conditions;
- interruption.

The parent craft/technical system may evaluate whether the final output meets tolerance.

## 17. Structural validity

A recoded object must satisfy the world's normal structural rules after commit.

The ability cannot declare:
- an unsupported bridge stable;
- a weak material stronger than its modeled properties;
- an unsafe pressure vessel safe;
- a device functional without correct design.

Matter Recode changes matter configuration; it does not override engineering reality.

## 18. Living-material boundary

Default:
living organisms are invalid targets.

If detached or biologically derived material exists, its eligibility must be classified explicitly.

No interpretation of this standard grants:
- biological redesign;
- healing;
- regeneration;
- living-body transformation.

Those remain owned by biological ability standards.

## 19. Ownership / legal boundary

Physical ownership and law are world systems.

The ability may be physically capable of transforming an object while world rules treat the act as:
- theft;
- sabotage;
- regulated manufacturing;
- evidence destruction;
- hazardous work.

No legality is implied by mechanical capability.

## 20. Save/load

Persist enough state to reconstruct any legal mid-operation transaction:
- transaction ID;
- source material IDs/amounts committed;
- target model/version;
- energy source and committed energy;
- completed transformation fraction/state;
- residual/byproduct state;
- output IDs;
- failure/lockout state.

Loading cannot:
- restore consumed input;
- duplicate output;
- refund already consumed energy;
- rerun completed conversion.

## 21. Player-safe projection

The UI may show only material/composition information the character legitimately knows.

Do not expose:
- hidden constituent data;
- exact unknown impurity;
- unseen internal structure;
- hidden product defects;
- secret material identity.

Debug material truth remains separate.

## 22. Cross-ability boundaries

### Adaptive Arsenal
Adaptive Arsenal transforms the user's biological body using learned biological templates.
Matter Recode remains external nonliving material transformation.

### Energy Devour
No automatic reserve interoperability.

### Crystal Resonance
No crystal-specific material ontology is inferred unless THE GAME authors it independently.

### Law Silence
Law Silence cannot be treated as a shortcut that removes Matter Recode's conservation/knowledge rules unless an explicit protected-rule review permits it.

## 23. Required future tests

- input/output mass balances;
- impurity removal produces residual/byproduct mass;
- missing constituent blocks/reduces valid output;
- unknown composition does not become known automatically;
- wrong model can produce flawed/failed output;
- energy is consumed once;
- interruption cannot duplicate matter;
- T1–T4 remain within learned target models;
- living target is rejected by default;
- product must pass normal structural/technical validity;
- save/load cannot duplicate input/output;
- UI does not expose hidden composition.

## 24. Remaining blockers

Resolved structurally:
- nonliving domain boundary;
- source/target-model separation;
- mass/composition conservation;
- composition-knowledge requirement;
- energy accounting;
- incomplete conversion;
- impurity/byproduct handling;
- technique envelopes;
- product validity;
- save/load/projection boundaries.

Still open:
- authoritative material taxonomy;
- composition representation;
- physical versus abstract energy estimator;
- scale/mass/precision caps;
- output-quality model;
- legal/industrial world integration;
- numeric cost/rate/duration;
- owner approval.

Matter Recode remains a Super Epic calibration record and is not canon-promoted by this standard.
