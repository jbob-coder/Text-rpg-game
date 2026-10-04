# THE GAME — Probability Tilt Event-Resolution & Evidence Standard

Status: **PROVISIONAL CHILD STANDARD / NOT CANON UNTIL OWNER REVIEW / NOT IMPLEMENTED**

Parents:
- `KNOWLEDGE_EVIDENCE_CONFIDENCE_STANDARD.md`
- `TIME_CAUSAL_STATE_AND_SNAPSHOT_STANDARD.md`
- `calibration/PRIMARY_ABILITY_DETAIL_SUPER_EPIC_001_003.md`
- `calibration/ABILITY_TECHNIQUE_DETAIL_SUPER_EPIC_001_003.md`

Scope:
- `ABILITY_SEP_003 Probability Tilt`
- techniques `TECH_SEP_003_T1`–`T4`

Purpose: define the non-numeric semantics for eligible uncertain events, plausible outcome sets, probability weighting, bounded context, observability, causation evidence, chained resolutions, and save/load determinism.

## 1. Core law

Probability Tilt modifies the weighting among **already plausible unresolved outcomes** inside one bounded eligible context.

It does not:
- make impossible outcomes possible;
- guarantee an outcome;
- rewrite an event after resolution;
- create hidden new outcomes;
- create matter/energy;
- expose exact hidden probabilities by default;
- prove that a favorable outcome was caused by the ability.

## 2. Eligible resolution event

A future probability-sensitive event should identify:
- stable event/resolution ID;
- event type/domain;
- candidate plausible outcome set;
- baseline weighting model;
- eligibility for probability modification;
- current unresolved/resolved state;
- context boundary;
- relevant hidden/public evidence;
- deterministic seed/state if the simulation uses seeded stochastic resolution.

Probability Tilt cannot act on an event that has already authoritatively committed.

## 3. Plausible outcome set

Before the ability applies, the parent event resolver defines which outcomes are genuinely possible.

The ability may reweight only members of that set.

If an outcome has zero eligibility under the parent event law, Probability Tilt cannot raise it above zero.

Examples:
- an unlocked door may plausibly swing several ways under a noisy physical model;
- a physically impossible teleport outcome is not a candidate;
- a social decision cannot include knowledge/choices the NPC does not possess unless another system adds them.

## 4. Near-equivalent requirement

The current ability identity is strongest when competing outcomes are already close enough that a bounded bias can matter.

A future resolver must define a non-numeric or numeric eligibility test for:
- near-equivalent outcomes;
- large-gap outcomes;
- effectively deterministic outcomes.

The ability must weaken or become ineligible as the baseline gap grows beyond its approved envelope.

Exact threshold remains `TBD`.

## 5. Weighting, not selection

The ability changes relative weighting.

It does not directly set:
`chosen_outcome = desired_outcome`.

A successful activation can still end with:
- undesired outcome;
- neutral outcome;
- another plausible outcome.

This uncertainty is part of the Super Epic identity.

## 6. Bounded context

Each activation must define a bounded target context, such as:
- one resolution event;
- one outcome family;
- a short linked sequence;
- a technique-defined field/context.

The context should identify:
- start;
- end;
- included resolution domains;
- owner;
- technique;
- resource/strain state.

Unbounded “make everything lucky” behavior is prohibited.

## 7. Observability

The user does not automatically know:
- baseline probabilities;
- exact modified probabilities;
- hidden candidate outcomes;
- whether the final result differed because of the ability.

The player may know:
- they activated the ability;
- intended target/context;
- observed outcome;
- any Status-confirmed activation/failure information explicitly provided.

Hidden weight values remain authoritative-only unless another mechanic exposes them.

## 8. Evidence and causation

One favorable outcome is not proof of causal success.

World/research evidence may require:
- repeated controlled observations;
- comparison groups;
- known activation records;
- sufficient sample size;
- elimination of confounding factors;
- another authored proof standard.

Even strong statistical evidence remains evidence, not direct exposure of hidden probability state unless Status confirms it.

## 9. Edge Bias — T1

`TECH_SEP_003_T1 Edge Bias`:
- one bounded unresolved event;
- several already plausible near-equivalent outcomes;
- small weighting shift;
- no guarantee.

It should fail cleanly when there is no eligible uncertain resolution.

## 10. Outcome Weight — T2

`TECH_SEP_003_T2 Outcome Weight`:
- selects one **outcome family**, not one exact hidden micro-outcome;
- increases relative weighting of eligible members of that family;
- cannot include impossible family members.

The family definition must be explicit enough to prevent “anything beneficial” as an unbounded target.

## 11. Probability Field — T3

`TECH_SEP_003_T3 Probability Field`:
- maintains a bounded bias across a linked sequence of eligible events;
- each event still resolves separately;
- context growth and event count increase strain/control burden;
- ineligible events ignore the field.

The field cannot retroactively modify events already committed.

## 12. Narrow Fate — T4

`TECH_SEP_003_T4 Narrow Fate`:
- permits the strongest approved short-duration bias;
- only among close plausible outcomes;
- retains nonzero failure/alternate-outcome possibility unless the parent event was already deterministic.

It does not become certainty.

## 13. Deterministic parent events

If a parent event is deterministic by design and has one valid outcome:
- Probability Tilt has nothing to reweight;
- activation should be rejected, wasted, or otherwise resolved by a future explicit rule;
- the ability cannot invent randomness merely to create leverage.

## 14. Seeded simulation

If THE GAME uses deterministic/seeded randomness:
- the authoritative event seed/state remains engine-owned;
- Probability Tilt modifies the approved resolution weights/input before commit;
- loading the same saved pre-resolution state must reproduce the same result if all authoritative state is identical;
- reloading cannot reroll until a preferred result appears.

Save-scumming through repeated RNG reconstruction is prohibited.

## 15. Commit point

Every eligible event needs an authoritative commit boundary.

Before commit:
- weighting may be modified if activation/context allows.

At/after commit:
- outcome is fixed;
- Probability Tilt cannot revise it;
- Event Reversal/Causal Mark remain separate systems with different laws.

## 16. Multiple modifiers

If several probability-modifying effects ever exist:
- one authoritative probability-resolution stage must collect them;
- duplicate effect IDs do not double-apply;
- stacking/caps must be explicit;
- final weights remain valid/non-negative;
- impossible outcomes stay impossible.

Current Wave-001 does not assume another such effect exists.

## 17. Unintended adjacent outcome

Current design permits failure modes where a nearby plausible outcome receives unintended benefit.

A future model may represent:
- imprecise family targeting;
- context leakage within the bounded set;
- reduced control under strain.

This must remain bounded and cannot become arbitrary world chaos.

## 18. Resource and strain model

Current cost:
- Focus;
- Resolve.

Structural interpretation:
- Focus supports precise event/context targeting;
- Resolve supports maintaining intended bias under uncertainty.

A dedicated strain/control state may also be needed for sustained/multiple-event techniques.

Exact costs remain `TBD`.

## 19. Probability versus prediction

Probability Tilt is not precognition.

It does not tell the user:
- which outcome would have happened without activation;
- what all future branches contain;
- exact success percentages;
- the opponent's hidden decision tree.

Prediction remains a separate knowledge/modeling task.

## 20. Probability versus social agency

When a social outcome includes another character's decision:
- that character's knowledge, motives, agency, and allowed decisions remain part of the parent resolver;
- Probability Tilt may only reweight already plausible parent outcomes if that domain is explicitly eligible;
- it cannot force an impossible choice or erase agency constraints.

Exact social eligibility remains a future world/design decision.

## 21. Probability versus physical law

Probability Tilt cannot select an outcome that violates established physical/system law.

Examples:
- an intact object does not spontaneously appear elsewhere;
- conserved resources do not multiply;
- a projectile cannot pass through an absolute barrier unless that result was already physically plausible under the parent system.

## 22. Interaction with Time Partition

Time Partition can improve planning/analysis.

Probability Tilt can modify eligible outcome weighting.

Time Partition does not expose hidden weights.
Probability Tilt does not provide extra subjective time.

The two effects remain separate.

## 23. Interaction with Causal Mark / Event Reversal

Causal Mark and Event Reversal operate after a valid recorded state exists.

Probability Tilt operates before unresolved-event commit.

It cannot:
- alter a historical snapshot;
- make a previous event “more likely” after it occurred;
- rewrite evidence of a committed event.

## 24. Save/load

Persist enough state for active contexts:
- activation ID;
- bounded context ID;
- technique;
- affected unresolved event IDs or eligibility scope;
- resource/strain state;
- already committed event IDs;
- seed/resolution state required for determinism.

Loading cannot:
- reroll a committed result;
- reapply bias to the same event;
- reset cost/strain;
- expose hidden weights.

## 25. Player-safe projection

Potential visible data:
- active technique/context;
- broad control/strain warning;
- intended outcome-family label if character knows it;
- observed results.

Do not expose:
- baseline exact percentages;
- final hidden percentages;
- hidden candidate outcomes;
- counterfactual “what would have happened” truth.

## 26. World/research consequences

Plausible role classes:
- research/statistics;
- strategy;
- navigation;
- negotiations;
- high-stakes operations.

But final world treatment requires doctrine for:
- detectability;
- evidence/admissibility;
- gambling/economic regulation if relevant;
- military/security use;
- scientific verification.

No named institution is established here.

## 27. Required future tests

- impossible outcome remains impossible;
- deterministic event cannot be made uncertain merely for activation;
- near-equivalent event can be reweighted without guarantee;
- event commits once;
- post-commit activation cannot change outcome;
- one favorable outcome does not expose causation;
- hidden probability values remain hidden;
- T2 outcome family cannot expand into “anything beneficial”;
- T3 affects only eligible events inside context;
- T4 still preserves alternate outcomes where parent law allows them;
- save/load cannot reroll or reapply bias;
- seeded resolution remains deterministic from saved authoritative state;
- no matter/energy/resource creation;
- social/physical parent laws remain authoritative.

## 28. Remaining blockers

Resolved structurally:
- eligible unresolved event model;
- plausible-outcome-set boundary;
- near-equivalent concept;
- weighting rather than selection;
- bounded context;
- observability/evidence boundary;
- technique semantics;
- commit point;
- seeded save/load anti-reroll rule;
- parent-law/agency/conservation boundaries.

Still open:
- exact probability representation;
- near-equivalent threshold;
- maximum bias;
- field duration/event count;
- detectability;
- resource/strain values;
- eligible parent resolver domains;
- world legal/economic/scientific treatment;
- owner approval.

Probability Tilt remains a Super Epic calibration record and is not canon-promoted by this standard.
