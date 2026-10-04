# THE GAME — Knowledge, Evidence & Confidence Standard

Status: **PROVISIONAL CROSS-SYSTEM DESIGN STANDARD / NOT CANON / NOT IMPLEMENTED**

Purpose: keep objective world truth separate from what a character observes, believes, infers, or can prove. This standard supports Memory Echo, Probability Tilt, Sensory passives, investigation, Status visibility, and future legal/institutional systems.

## State layers
Future authoritative design should distinguish:
- `truth_state` — hidden objective simulation/world state;
- `observation` — information actually available through a valid source;
- `interpretation` — a character/system conclusion drawn from observations;
- `claim` — information asserted by a source;
- `evidence_record` — preserved observation/claim with provenance;
- `confidence` — bounded estimate of reliability, never a replacement for truth.

The player-safe UI must not expose `truth_state` solely because the engine knows it.

## Provenance
An evidence record should eventually support source ID/type, world time, location/context, acquisition method, relevant ability/tool, confidence, known contamination/interference, and chain-of-custody information where the world system requires it.

## Confidence
Confidence is about the character/system's justification, not objective correctness.

Suggested bands for future use: `LOW`, `MODERATE`, `HIGH`, `SYSTEM_CONFIRMED`. These labels should only appear when the character has a legitimate basis for them.

## Memory Echo
Memory Echo produces fragmentary residual impressions. Its output should be stored as an `impression`, not as objective historical truth.

An impression may carry sensory/emotional fragments, approximate sequencing, source context, overlap/contamination flags, and confidence. It does not automatically prove identity, exact chronology, or causation.

## Probability Tilt
A single favorable result does not prove that Probability Tilt caused that result.

Probability-related evidence should distinguish:
- the actual observed outcome;
- the user's intended bounded context;
- any known activation state;
- statistical inference from repeated observations where appropriate.

The system should not expose hidden exact probabilities unless a separate mechanic explicitly authorizes that knowledge.

## Sensory passives
Sensory passives modify signal interpretation, tracking, discrimination, or retention. They do not convert uncertain input into objective truth.

A high-confidence perception can still be incorrect when the source signal is incomplete or misleading.

## Status-confirmed facts
Some facts may be directly confirmed by Status, such as an ability identity or rarity when the relevant Status rule exposes it.

`SYSTEM_CONFIRMED` should mean the Status explicitly confirmed that specific field. It does not imply that every related mechanic, hidden technique, or historical claim is known.

## Investigation/world use
Future investigation, courts, research, schools, security systems, and factions may assign different admissibility or trust to different evidence sources. Those institutions require child rules; this document does not pre-decide them.

## Save/load
Known observations, discovered claims, evidence provenance, and legitimately revealed confidence may need persistence. Hidden truth remains in authoritative world state and is not reconstructed from the player's evidence log.

## Required tests
- hidden truth does not leak into player projection;
- uncertain observation stays uncertain;
- Memory Echo never becomes automatic objective history playback;
- one Probability Tilt outcome is not treated as deterministic proof;
- sensory confidence does not rewrite world truth;
- Status-confirmed fields do not reveal adjacent hidden fields;
- save/load preserves acquired evidence without creating new knowledge.

## Remaining blockers
- final confidence scale and UI language;
- investigation evidence model;
- legal/institutional admissibility;
- Memory Echo contamination/decay rules;
- Probability Tilt statistical-resolution semantics;
- named research and government doctrine;
- player-facing evidence journal design.

No ability or passive is canon-promoted by this standard.