# THE GAME — Error, Confidence & Resolution-Mode Standard

Status: **ACTIVE TARGET-GAME DESIGN / CURRENT-REALITY MAPPED / DOMAIN RANGES OPEN / IMPLEMENTATION MIGRATION DEFERRED**

Parents:
- `KNOWLEDGE_EVIDENCE_CONFIDENCE_STANDARD.md`
- `STATUS_BASE_RESOLUTION_TERM_UNIT_TAXONOMY.md`
- `STATUS_PARENT_FIXTURE_BATCH_003_KNOWLEDGE_EVIDENCE_INTERPRETATION.md`
- `PASSIVE_CANONICAL_RESOLVER_RANGE_FIXTURE_ELIGIBILITY_AUDIT_WAVE_001.md`

Purpose: define how THE GAME represents uncertain checks, avoidable error, evidence confidence, seeded variance, and the separation between outcome uncertainty and truth.

---

# 1. CURRENT REALITY — authored checks

Current scene-choice checks use a seeded margin model:

`score = effective_stat + effective_skill * skill_weight + seeded_roll`

`margin = score - difficulty`

Current default:
- difficulty = 50;
- variance = 10;
- skill weight = 0.5.

Current deterministic roll seed uses:
- save/game seed;
- turn;
- scene ID;
- choice ID.

The current roll is deterministic for identical authoritative inputs.

Current default degree thresholds:
- critical_success >= margin 20;
- success >= 0;
- failure >= -20;
- critical_failure below that.

These are current implementation facts and are not automatically final target balance.

# 2. CURRENT REALITY — knowledge confidence

Current NPC knowledge code validates numeric confidence in:

`0.0 <= confidence <= 1.0`.

Current knowledge records may also include:
- source;
- truth label;
- secrecy;
- turn learned.

Current knowledge transfer copies the source knowledge record and changes provenance to the speaker.

Current code does not establish that confidence is objective probability of truth.

# 3. EVOLVED TARGET — separate four concepts

The target game separates:

1. **task resolution** — did an attempted action/check succeed?
2. **error burden** — how much avoidable error pressure exists before resolution?
3. **confidence** — how justified a character's belief/interpretation is.
4. **truth** — objective world state.

These are never interchangeable.

# 4. Resolution modes

Every uncertain parent resolver should declare one mode.

## DETERMINISTIC_RULE
Outcome follows directly from state/rules.

Examples:
- missing authorization;
- impossible physical requirement;
- absent source energy;
- no known datum.

No random roll should override a hard rule.

## MARGIN_CHECK
Capability/context compared with difficulty using a margin.

May be fully deterministic.

## SEEDED_VARIANCE_MARGIN
Margin check with bounded deterministic seeded variance.

This generalizes the current authored-choice check pattern.

## OPPOSED_CONTEST
Two authoritative sides contribute to one contest.

## WEIGHTED_OUTCOME
A bounded unresolved event has an explicit plausible outcome set and weights.

Primary special use:
Probability Tilt-compatible parent events.

A subsystem must not switch resolution mode silently.

# 5. Hard-rule precedence

Before any uncertainty is resolved:
1. validate target/domain;
2. validate authorization;
3. validate required knowledge/evidence;
4. validate physical/system possibility;
5. validate resources;
6. then resolve uncertainty.

A passive cannot roll past a hard invalid state.

# 6. Resolution margin

Where margin-based resolution is used:

`margin = capability + context_modifiers - effective_difficulty + bounded_variance`

Exact domain scales can differ.

The current stat/skill check system provides a reference pattern, not a universal formula requirement.

Positive/negative margin means:
- above/below the parent difficulty threshold.

Degree bands are domain-owned unless a shared system explicitly adopts common thresholds.

# 7. ERROR_BURDEN

`ERROR_BURDEN` is **not automatically a probability**.

It represents avoidable error pressure attributable to:
- omission;
- confusion;
- poor interpretation;
- execution inconsistency;
- unfamiliar procedure;
- another documented source.

A parent resolver must map ERROR_BURDEN into exactly one authorized place, such as:
- difficulty delta;
- margin delta;
- variance envelope;
- failure-state severity;
- deterministic threshold.

A passive modifying ERROR_BURDEN does not directly edit hidden truth.

# 8. No universal error percentage

Do not display or store “15% error chance” unless that parent resolver genuinely uses probability and has a calibrated statistical model.

Many systems are better represented as:
- deterministic difficulty;
- margin;
- contest;
- confidence band.

This prevents false precision.

# 9. INTERPRETATION_CONFIDENCE

The target preserves current compatible normalized internal confidence:

`0.0 <= confidence <= 1.0`

for knowledge/evidence records where a numeric confidence field is useful.

Important:
confidence is a **justification strength**, not objective truth probability.

A confidence value may reflect:
- source reliability;
- corroboration;
- directness;
- contamination;
- memory age;
- interpretation quality.

The exact aggregation formula remains domain-specific.

# 10. SYSTEM_CONFIRMED

`SYSTEM_CONFIRMED` is a provenance/authority state, not merely confidence = 1.0.

A record can have high confidence without Status confirmation.

A Status-confirmed field means:
- Status explicitly confirmed that exact datum.

It does not confirm adjacent facts.

# 11. Player-facing confidence bands

Player-safe presentation may use qualitative bands:
- LOW;
- MODERATE;
- HIGH;
- SYSTEM_CONFIRMED where applicable.

Final numeric cutoffs between LOW/MODERATE/HIGH remain `TBD`.

The UI must not show exact internal confidence if design chooses qualitative projection.

# 12. Truth labels

Current code accepts free text `truth` on NPC knowledge.

Target design should replace unrestricted semantics with a controlled truth/evidence vocabulary during schema evolution.

Candidate conceptual states:
- UNKNOWN_TO_SYSTEM;
- UNVERIFIED;
- CORRECT;
- PARTIAL;
- FALSE;
- OUTDATED;
- DISPUTED.

This vocabulary is **PROPOSED** until the knowledge schema is migrated.

Do not treat current free-text truth labels as trustworthy authority without validation.

# 13. Evidence provenance

Confidence cannot exist without provenance in reconstruction-grade content.

An evidence/knowledge record should identify enough of:
- source ID/type;
- acquisition time;
- location/context;
- direct/indirect observation;
- chain of transfer;
- known contamination;
- corroboration;
- authorization/classification;
- system confirmation if any.

# 14. Seeded variance

When seeded variance is used:
- seed inputs must be authoritative and stable;
- reloading identical pre-resolution state reproduces the same result;
- UI recomposition does not reroll;
- repeated save/load cannot fish for a new outcome;
- Probability Tilt modifies approved weighting/resolution state before commit rather than manipulating device RNG.

# 15. Commit point

Every uncertain event has one commit point.

Before commit:
- legal modifiers may apply.

After commit:
- outcome is authoritative;
- UI cannot reroll it;
- save/load cannot reroll it;
- passive evaluation cannot reapply to the same event.

Temporal abilities that restore state do not silently erase the event's causal/evidence record unless their own law explicitly owns that state.

# 16. Recall

Known-information recall:
- can only select from legitimately acquired information;
- may suffer retrieval burden;
- may return partial/uncertain recall;
- cannot create an unknown datum.

A high confidence in a recalled false claim remains possible.

# 17. Sensory interpretation

Sensory systems distinguish:
- signal availability;
- perception;
- interpretation;
- confidence.

Improved signal separation does not guarantee correct meaning.

# 18. Analytical checking

Analytical passives can reduce:
- omission;
- unchecked assumption;
- process error.

They cannot:
- manufacture evidence;
- guarantee hidden truth;
- bypass missing domain knowledge.

# 19. Social interpretation

Social cue interpretation may use observation/confidence.

It must not read:
- hidden NPC intent;
- private memory;
- secret relationship state

without an authorized source/mechanic.

# 20. Threat prioritization

Threat prioritization operates only on the recognized candidate set.

A hidden/unrecognized threat cannot receive a priority score merely because the engine knows it exists.

# 21. Status anomaly recognition

Anomaly recognition operates on legitimate Status/system observations.

It cannot expose:
- hidden prompt content;
- root state;
- protected system architecture.

`SYSTEM_CONFIRMED` only applies when Status confirms that exact anomaly fact.

# 22. Probability Tilt boundary

Probability Tilt uses WEIGHTED_OUTCOME parent events.

It does not:
- convert all MARGIN_CHECK systems into probability;
- expose hidden weights;
- let confidence stand in for probability;
- reroll committed events.

# 23. Passive integration

Passive modifiers must identify:
- parent resolver;
- resolution mode;
- authorized error/confidence term;
- scope;
- cap/floor;
- whether modifier affects difficulty, margin, variance, or evidence processing.

No passive may simply say “+X% success” without a parent resolution contract.

# 24. Current-to-target compatibility

Current authored choice checks can continue to operate as a reference `SEEDED_VARIANCE_MARGIN` implementation until migration.

Current NPC confidence 0..1 is compatible with target internal confidence semantics.

Open migration issues:
- current player knowledge records created by some core effects may not validate confidence as strictly as `npc_learn`;
- current free-text truth labels need controlled schema;
- current check difficulty/variance thresholds need content audit before becoming target balance.

# 25. Range-fixture implications

This standard closes the general representation questions:
- confidence internal range = 0..1 where numeric confidence is used;
- confidence != truth probability;
- error burden != automatic probability;
- resolution modes are explicit;
- hard-rule validation precedes uncertainty;
- seeded variance must be deterministic.

Still required before individual passive resolvers become `RANGE_FIXTURES_READY`:
- domain-specific capability/difficulty ranges;
- error-burden mapping range;
- confidence aggregation/band thresholds where player-facing;
- variance/contest ranges;
- content fixtures.

# 26. Required tests

- hard-invalid state cannot be rolled into success;
- identical seeded state resolves identically;
- reload does not reroll committed event;
- confidence outside 0..1 rejected where numeric confidence is used;
- confidence does not mutate truth;
- SYSTEM_CONFIRMED cannot be synthesized from confidence alone;
- unknown information cannot be recalled;
- hidden threat cannot be prioritized;
- hidden NPC intent does not leak through social interpretation;
- probability weighting cannot alter impossible outcomes;
- passive applies to one declared resolution stage only.

# 27. Reconstruction acceptance

A future developer/agent should be able to answer:
- whether a resolver is deterministic, margin-based, contested, or weighted;
- where ERROR_BURDEN enters;
- what confidence means;
- why confidence is not truth;
- how seeded outcomes remain stable;
- why passives cannot bypass hard rules.

No runtime implementation or canon passive promotion occurs through this standard.
