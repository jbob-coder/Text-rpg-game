# THE GAME — Memory Echo Impression, Contamination & Evidence Standard

Status: **PROVISIONAL CHILD STANDARD / NOT CANON UNTIL OWNER REVIEW / NOT IMPLEMENTED**

Parents:
- `KNOWLEDGE_EVIDENCE_CONFIDENCE_STANDARD.md`
- `calibration/PRIMARY_ABILITY_DETAIL_RARE_006_010.md`
- `calibration/ABILITY_TECHNIQUE_DETAIL_RARE_001_010.md`
- `RARE_ABILITY_RARITY_OVERLAP_AUDIT_001_010.md`

Scope:
- `ABILITY_RAR_007 Memory Echo`
- techniques `TECH_RAR_007_T1`–`T4`

Purpose: define how residual impressions are created, decay, overlap, contaminate, and become evidence without turning Memory Echo into objective historical playback or mind reading.

## 1. Core interpretation

Memory Echo reads a residual impression associated with emotionally intense past contact on a valid object or location.

An Echo is:
- an extraordinary observation source;
- fragmentary;
- context-sensitive;
- potentially contaminated;
- potentially biased;
- not objective truth by default.

The engine's hidden world truth remains separate.

## 2. Echo-source record

A future authoritative echo-source record should identify:
- `echo_source_id`;
- source object/location stable ID;
- originating event ID if known to the engine;
- creation world time;
- emotional/intensity band;
- sensory-channel tags;
- persistence/decay class;
- contamination state;
- overlap group;
- integrity state.

Player-facing projection does not automatically reveal originating event ID or hidden truth fields.

## 3. What may be encoded

A residual impression may contain bounded fragments such as:
- visual shapes/colors/light;
- sounds/voices without guaranteed identification;
- tactile/temperature sensations;
- motion/direction;
- emotional tone;
- pain/fear/urgency intensity;
- spatial context;
- short sequence relationships.

A fragment is not required to contain every category.

## 4. What is not automatically encoded

Memory Echo does not automatically provide:
- exact names;
- verified identities;
- precise timestamps;
- complete conversations;
- full memories;
- private thoughts;
- motives;
- objective causation;
- hidden Status data;
- information absent from the residual impression.

If the character later infers identity or causation, that becomes an interpretation/claim with its own confidence.

## 5. Emotional intensity

Emotionally intense contact increases the chance or persistence of an Echo, but emotional intensity is not truth quality.

A strong Echo can still be:
- incomplete;
- misleading without context;
- contaminated by overlap;
- dominated by one participant's emotional state;
- difficult to date.

Do not equate "strong emotion" with "accurate history."

## 6. Decay

Echo persistence decreases over world time according to a future decay model.

Decay may reduce:
- accessible channels;
- detail;
- sequence coherence;
- separability from background residue;
- confidence.

Decay must not reveal exact event age unless the ability or other evidence legitimately supports that estimate.

Exact decay coefficients remain `TBD`.

## 7. Overlap

An object/location can hold multiple Echoes.

Overlapping Echoes should preserve separate source records where the simulation has them, even if the user cannot distinguish them.

Observed results may include:
- blended sensory fragments;
- conflicting emotional tones;
- misordered fragments;
- partial dominance by the stronger Echo;
- ambiguous source attribution.

The engine must not merge world truth merely because the character perceives overlap.

## 8. Contamination

Contamination means the observed Echo cannot be assumed to cleanly represent one historical event.

Potential contamination sources:
- multiple intense events at the same source;
- later emotionally intense contact;
- deliberate staged/decoy events;
- ability interference;
- damaged/altered object or location state;
- user interpretation bias.

Contamination is an evidence-state problem, not automatic proof of falsification.

## 9. Deliberate decoys

A person can potentially create misleading residual context by causing a separate intense event around a source.

A decoy:
- does not rewrite the true past event;
- can add competing residue;
- can make isolation more difficult;
- can encourage false inference if the user lacks corroboration.

Memory Echo therefore cannot be treated as an unspoofable forensic system.

## 10. User bias

The ability supplies impressions.

The user's interpretation remains subject to:
- expectations;
- prior beliefs;
- incomplete knowledge;
- emotional reaction;
- anchoring on a vivid fragment.

The authoritative record should distinguish:
- raw impression;
- user interpretation;
- later corroboration/contradiction.

## 11. Technique model

### Surface Echo
Reads the strongest immediately accessible impression.

Strength does not imply correctness or recency.

### Echo Isolate
Attempts to separate one residual pattern from overlap.

Required future checks:
- distinguishability;
- user contextual knowledge;
- signal integrity;
- contamination.

Failure may return:
- incomplete isolation;
- blended residue;
- no useful result.

### Context Thread
Temporarily holds several related fragments and lets the user infer a probable sequence.

The output is an **interpretation**, not a system-confirmed chronology.

### Deep Resonance
Reads one unusually strong Echo with greater sensory/emotional depth.

Additional risks:
- emotional bleed;
- fixation;
- exhaustion;
- false certainty.

More detail does not remove the evidence uncertainty rule.

## 12. Confidence

Echo confidence must describe reliability of the acquired impression, not objective historical truth.

Suggested contributing factors:
- residue strength;
- decay;
- overlap count;
- contamination;
- technique quality;
- source continuity;
- corroborating evidence.

Even `HIGH` confidence cannot prove an inferred identity or motive unless those specific claims are separately supported.

`SYSTEM_CONFIRMED` is not a normal Memory Echo output state.

## 13. Evidence record

A preserved Echo observation should support:
- evidence ID;
- source object/location ID;
- acquisition time;
- technique ID;
- user ID;
- raw impression fragments;
- contamination/overlap flags;
- confidence band;
- user interpretation;
- corroborating evidence links;
- contradictions;
- chain-of-custody metadata where institutions require it.

Raw impression and interpretation must remain distinct fields.

## 14. Corroboration

Corroboration can raise confidence in a claim when independent sources agree.

Examples:
- physical evidence;
- ordinary witness testimony;
- logs/records;
- other legitimate observations;
- repeated Echo readings from independently related sources.

Repeatedly reading the same Echo is not independent corroboration.

## 15. Contradiction

When an Echo conflicts with other evidence:
- preserve both;
- reduce or revise confidence as appropriate;
- do not silently overwrite one source;
- allow investigation to resolve the conflict later.

The engine's hidden truth remains unchanged.

## 16. Legal/institutional use

This standard does not define a final legal system.

Minimum policy boundary:
no institution should be assumed to treat a Memory Echo as infallible evidence.

Future world/legal records must decide:
- admissibility;
- required corroboration;
- operator qualification;
- privacy limits;
- warrant/consent rules;
- source preservation;
- classified use.

## 17. Privacy boundary

Memory Echo reads residual impressions from objects/locations, not living minds.

Future privacy law may still treat certain readings as sensitive because they can expose past activity.

No privacy policy is canonized here.

## 18. Save/load

Persist enough state to preserve:
- discovered Echo observations;
- raw impression evidence;
- confidence;
- contamination flags;
- interpretation;
- corroboration links;
- resource consequences from the reading.

Loading must not:
- regenerate a cleaner impression from the same event;
- reset contamination;
- duplicate evidence IDs;
- expose hidden source truth.

## 19. Player-safe projection

The player may see:
- experienced sensory/emotional fragments;
- ability-provided uncertainty/caution flags if legitimately available;
- their character's recorded interpretations.

The player must not receive:
- hidden event IDs;
- objective truth labels;
- unseen participant identities;
- exact timeline metadata unless independently known.

## 20. Required tests

Future minimum tests:
- Memory Echo cannot read a living target's thoughts;
- old residue decays according to the final model;
- overlapping Echoes can produce ambiguity;
- Echo Isolate can fail without inventing a clean answer;
- repeated reads of the same Echo are not independent corroboration;
- decoy residue can contaminate interpretation without rewriting history;
- high confidence does not become objective truth;
- raw impression and interpretation persist separately;
- save/load does not clean, duplicate, or truth-upgrade evidence;
- player-safe projection does not leak hidden event identity/chronology.

## 21. Remaining blockers after this standard

Resolved structurally:
- Echo-source identity;
- decay direction;
- overlap;
- contamination;
- deliberate decoys;
- user bias;
- evidence/provenance separation;
- corroboration;
- save/load behavior;
- no-objective-truth boundary.

Still open:
- exact persistence/decay coefficients;
- source eligibility radius/range;
- fidelity thresholds;
- final confidence UI vocabulary;
- institutional/legal admissibility;
- historical/world occurrence examples.

Memory Echo remains `PASS WITH GUARDRAIL` at the design layer and is not canon-promoted by this standard.
