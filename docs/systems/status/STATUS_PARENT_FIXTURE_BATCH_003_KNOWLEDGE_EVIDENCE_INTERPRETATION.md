# THE GAME — Parent Fixture Batch 003: Knowledge, Evidence, Recognition & Interpretation

Status: **PHASE-C NUMERIC PREPARATION / QUALITATIVE PARENT FIXTURES / NO FINAL VALUES / NOT CANON / NOT IMPLEMENTED**

Parents:
- `PASSIVE_CANONICAL_RESOLVER_PARENT_FIXTURE_REQUIREMENTS_WAVE_001.md`
- `PASSIVE_CANONICAL_RESOLVER_SCENARIO_ANCHORS_WAVE_001.md`
- `KNOWLEDGE_EVIDENCE_CONFIDENCE_STANDARD.md`
- `STATUS_KNOWLEDGE_VISIBILITY_STANDARD.md`
- `STATUS_NUMERIC_CALIBRATION_FRAMEWORK.md`

Scope:
- `RESOLVER_KNOWN_INFORMATION_RECALL`;
- `RESOLVER_AUDITORY_SOURCE_SEPARATION`;
- `RESOLVER_IMMEDIATE_THREAT_PRIORITIZATION`;
- `RESOLVER_ANALYTICAL_CHECK_DISCIPLINE`;
- `RESOLVER_SYSTEM_ANOMALY_RECOGNITION`;
- `RESOLVER_OBSERVED_AUDIENCE_CLIENT_CUE_INTERPRETATION`.

Purpose: define qualitative parent fixtures that preserve the separation between hidden truth, available observation, interpretation, evidence, and confidence.

## 1. Shared evidence pipeline

The parent system must preserve:

`TRUTH_STATE -> AVAILABLE_SIGNAL/CLAIM -> OBSERVATION -> INTERPRETATION -> EVIDENCE/CONFIDENCE -> DECISION`

Not every gameplay event uses every stage.

Rules:
- hidden truth does not become an observation merely because the engine knows it;
- an observation can be incomplete or misleading;
- interpretation can be wrong;
- confidence is not truth;
- a passive can only modify its authorized stage.

# Part A — Known-information recall

## 2. FIX_RECALL_001 — Strongly known datum

Preconditions:
- datum was legitimately acquired;
- provenance exists;
- character retains valid knowledge state.

Expectation:
- recall attempt can resolve using the known datum;
- passive may reduce retrieval burden;
- output remains bounded by what was actually learned.

Current readiness:
`QUALITATIVE_FIXTURES_READY`.

## 3. FIX_RECALL_002 — Weakly reinforced known datum

Preconditions:
- datum exists in character knowledge;
- weak reinforcement/old context.

Expectation:
- recall is harder or less confident than matched strongly reinforced case;
- passive may improve retrieval but cannot create missing precision never learned.

## 4. FIX_RECALL_003 — Competing memories

Preconditions:
- multiple similar known records could be confused.

Expectation:
- parent model can represent retrieval/selection error;
- wrong-but-known candidate remains possible until corroborated.

## 5. FIX_RECALL_004 — Unknown datum boundary

Preconditions:
- datum was never acquired.

Expectation:
- no recall passive creates it;
- result is unavailable/unknown rather than guessed from hidden truth.

## 6. FIX_RECALL_005 — Authorized compartment boundary

Preconditions:
- related information exists in world state;
- character does not possess the protected datum.

Expectation:
- protected information remains unavailable;
- broad recall does not bypass authorization/knowledge acquisition.

# Part B — Auditory source separation

## 7. FIX_AUD_001 — Two available audible sources

Expectation:
- both sources are physically/sensorily available;
- parent system may resolve separation quality/error;
- passive changes separation, not source existence.

Current readiness:
`QUALITATIVE_FIXTURES_READY`.

## 8. FIX_AUD_002 — Masking-noise adverse case

Preconditions:
- target source remains audible but overlaps stronger noise.

Expectation:
- separation burden is no better than matched clear-audio case;
- confidence may fall without changing objective truth.

## 9. FIX_AUD_003 — Absent signal boundary

Preconditions:
- target source is not available to the character's sensory channel.

Expectation:
- passive cannot reconstruct exact absent audio;
- no hidden dialogue/data leaks.

## 10. FIX_AUD_004 — Misleading source

Preconditions:
- available sound is genuine but intentionally deceptive/misidentified.

Expectation:
- source separation may succeed while interpretation remains wrong;
- sensory passive must not become deception detection.

# Part C — Immediate threat prioritization

## 11. FIX_THR_001 — Recognized unequal threats

Preconditions:
- two or more threats are already legitimately recognized.

Expectation:
- parent system can order/prioritize among the candidate set;
- passive may reduce decision burden.

Current readiness:
`QUALITATIVE_FIXTURES_READY`.

## 12. FIX_THR_002 — Near-equal threats

Expectation:
- prioritization remains uncertain/difficult;
- passive does not guarantee globally optimal choice.

## 13. FIX_THR_003 — Hidden threat boundary

Preconditions:
- threat exists in truth state but has not been observed/recognized.

Expectation:
- it is absent from the prioritization candidate set;
- passive does not reveal it.

## 14. FIX_THR_004 — False/ambiguous cue

Preconditions:
- character recognizes a possible threat from ambiguous evidence.

Expectation:
- prioritization may legitimately act on perceived threat state;
- later evidence may show the interpretation was wrong;
- world truth is not rewritten.

# Part D — Analytical check discipline

## 15. FIX_ANALYTIC_001 — Sufficient evidence ordinary review

Expectation:
- character can run a known analytical/checking process;
- passive may reduce avoidable omission/check error.

Current readiness:
`QUALITATIVE_FIXTURES_READY`.

## 16. FIX_ANALYTIC_002 — Conflicting evidence

Expectation:
- analysis remains uncertain;
- passive may improve checking discipline but not force a correct hidden conclusion.

## 17. FIX_ANALYTIC_003 — Missing evidence boundary

Expectation:
- unavailable evidence stays unavailable;
- no passive manufactures proof.

## 18. FIX_ANALYTIC_004 — Deliberate false evidence

Expectation:
- high-quality checking may detect inconsistency if evidence permits;
- forged/misleading evidence can still succeed;
- confidence and truth remain separate.

# Part E — Status/system anomaly recognition

## 19. FIX_SYS_001 — Observable known anomaly signature

Preconditions:
- anomaly produces a player/character-legitimate observable signal.

Expectation:
- recognition can improve with familiarity;
- only the exposed signal is eligible.

Current readiness:
`QUALITATIVE_FIXTURES_READY`.

## 20. FIX_SYS_002 — Ambiguous observable anomaly

Expectation:
- recognition may remain partial/uncertain;
- confidence does not become `SYSTEM_CONFIRMED` unless Status explicitly confirms the field.

## 21. FIX_SYS_003 — Hidden prompt/root-state boundary

Preconditions:
- engine has protected/root data with no legitimate observable projection.

Expectation:
- recognition passive returns no hidden content;
- no prompt enumeration;
- no root architecture disclosure.

## 22. FIX_SYS_004 — Ordinary event mistaken for anomaly

Expectation:
- false positive remains possible unless parent evidence rules rule it out;
- passive is not objective-truth access.

# Part F — Audience/client cue interpretation

## 23. FIX_SOC_001 — Clear observable cue

Preconditions:
- behavior/statement is actually observable.

Expectation:
- parent system produces an interpretation burden/confidence;
- passive may reduce interpretation error.

Current readiness:
`QUALITATIVE_FIXTURES_READY`.

## 24. FIX_SOC_002 — Mixed group reactions

Expectation:
- one group cannot be collapsed to a single hidden “true mood” unless the world model explicitly supports it;
- conflicting cues remain conflicting.

## 25. FIX_SOC_003 — Deliberate social deception

Expectation:
- observable cue is processed as presented;
- interpretation can be wrong;
- no mind reading.

## 26. FIX_SOC_004 — Hidden intent boundary

Preconditions:
- NPC intention exists only in hidden state and has no legitimate cue.

Expectation:
- passive cannot expose the intention.

## 27. Cross-stage integration fixture

One investigation/social/security scene may involve:
1. an available observation;
2. auditory/sensory separation;
3. recall of known information;
4. analytical checking;
5. social or anomaly interpretation;
6. decision/threat prioritization.

Required rule:
each stage consumes only the state legitimately produced upstream.

A downstream resolver never requests `truth_state` merely because it would improve accuracy.

## 28. Confidence fixture rule

Where confidence exists:
- `LOW < MODERATE < HIGH < SYSTEM_CONFIRMED` may be used as provisional qualitative bands;
- higher confidence must be justified by available evidence/provenance;
- confidence is not success probability by default;
- `SYSTEM_CONFIRMED` is reserved for explicit Status confirmation of that specific fact.

## 29. Save/load and provenance

For persistent observations/evidence:
- stable evidence ID;
- acquisition source;
- world time/context;
- known contamination/interference;
- character-known confidence;
- discovery state

must reconstruct without duplication.

Reload cannot create a new observation or improve confidence by itself.

## 30. Gate Twelve candidate fixtures

Confirmed local contexts can later instantiate these parent fixtures:
- Municipal Archive — recall/evidence/document interpretation;
- Relay Workbench / Trace Chamber — technical/anomaly evidence if content actually exposes it;
- Depot Plaza — observable social/group cues;
- restricted infrastructure — threat/procedure evidence where authored.

The locations themselves do not grant hidden truth.

## 31. Range-fixture blockers

Before these resolvers become `RANGE_FIXTURES_READY`, the game must choose:
- deterministic score, probability, contest, or hybrid forms where relevant;
- error/confidence scale;
- sensory signal/noise representation;
- threat-candidate difficulty representation;
- social-cue interpretation representation;
- observable Status-anomaly schema.

## 32. Acceptance

This batch establishes qualitative parent fixtures for **6 canonical resolver families**.

No hidden truth access, probability percentage, error coefficient, or canon promotion is established.
