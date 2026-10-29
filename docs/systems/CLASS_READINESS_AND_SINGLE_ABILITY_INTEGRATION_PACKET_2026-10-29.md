# THE GAME — Read-only class readiness and single-principal-ability integration packet

**Status:** IMPLEMENTATION DESIGN / UNAPPROVED CONTRACT / NOT AN IMPLEMENTED CLASS SYSTEM.  
**Date:** 2026-10-29.  
**Scope:** `jbob-coder/Text-rpg-game`, branch `work/story-engine-class-ability-20261029`.  
**Authority:** `COMBAT_CLASS_CATALOG.md`, `PROGRESSION_CLASSES_RANKS_EVOLVED_GAME_DESIGN.md`, `src/textrpg/core.py`, `src/textrpg/powers.py`, `src/textrpg/quests.py`, `src/textrpg/persistence.py`, and creator history H-05/H-06, H-20–H-27. The master D-045 migration packet supersedes this note wherever it differs.

## 1. What source code currently guarantees

- `GameState` is a dataclass holding `player`, `flags`, `relationships`, `knowledge`, `inventory`, `quests`, `npcs`, `party`, `abilities`, `equipment`, `perks`, `history` plus seed, scene, turn and time. **There is no authoritative durable class record.**
- `persistence.py` requires `CURRENT_SCHEMA_VERSION = 1` and rejects unknown top-level fields. Adding `classes` casually would break the contract; **do not do it**.
- `powers.py` implements ability/technique discovery, mastery, evolution and per-technique prerequisites. This is not a class system. On the current working branch it rejects cyclic discovery prerequisite graphs and malformed unhashable stage metadata.
- `quests.py` has quest stages, objectives and state changes. Quest state is not evidence that a particular *individual action* was performed or that competence was demonstrated unless a named result with the required provenance exists.
- The two story proposals (Vol II chapters II–III) have **no** content-pack registrations or world coordinates. Their scene descriptions must not be treated as events in the game.

## 2. Three distinct progression axes

| Axis | What it represents | Source of truth now | Forbidden shortcut |
| --- | --- | --- | --- |
| Principal ability + derived techniques | One randomly assigned exceptional capacity per human, with learnable methods inside it (H-05/H-06) | `GameState.abilities` and technique records; **single-principal enforcement not yet implemented** | Grant a second independent principal ability as a class reward |
| Combat/adventure class | Earned discipline and field competence; seven target families | Design catalog only, no class state | Grant a class automatically for taking one dialogue branch |
| Profession / Smith | Skilled occupation/forging competence, constrained by core properties and Smith experience | Design/H-20–H-27 only | Treat Smith as Operator, create matter properties, or duplicate weapon+wielder modifiers by default |

Even when all three appear in one mission, each must have an independent authority and validated event trail. A hero may be a skilled investigator and an able smith yet have exactly one principal ability.

## 3. Candidate class-readiness query — API proposal, **no code yet**

Future side-effect-free query concept:

`query_class_readiness(state, class_definition, evidence_source) -> {status, visible_reasons, proven_domains, missing_domains}`

**Proposed status semantics:** `not_evaluable` if source provenance is unavailable or the candidate class definition is unapproved; `requirements_not_met` if trustworthy evidence is insufficient; `ready_for_review` if the required evidence exists and an authorized award procedure may review it. None of these statuses **grants** a class or updates saves.

Prerequisites for implementation:

1. Approve catalog IDs and the ownership of a durable class record in an explicit save-schema migration.
2. Define evidence **producers** that actually execute the relevant action and record subject, actor, source revision, event identity, outcome and visibility without leaking hidden lore. Do not count generic `history` strings whose origin cannot be checked.
3. Define evidence deduplication across replay/save-resume; duplicate events must not multiply field proofs. Failed/aborted actions need separate rules; a narrated attempt must not be confused with performed practice.
4. Define required stages Foundation -> Practice -> Field Proof -> Specialization and the threshold/balance table **after** measuring realistic gameplay rates. This document sets no XP/level numbers.
5. Report only player-justifiable evidence, with hidden provenance redacted by the existing projection rules. Unknown evidence is not treated as proof.
6. Specify migration and legacy save behavior. A version-1 save with no class record remains valid and must not silently gain a class from an inferred story event.

### Field proof opportunities, not awards

| Target family | What a verifiable event could demonstrate | Example negative evidence |
| --- | --- | --- |
| Vanguard | Actual ally protection under valid threat / team coordination | Merely selecting “protect” while no action runs |
| Skirmisher | Legal route choice and movement/precision under geometry checks | Teleportation claimed in prose without map movement |
| Operator | Diagnosis, bounded repair attempt, outcome inspection | Repair description without resource/material consumption and test |
| Field Specialist | Field stabilization, safe extraction or survival with resource/time costs | Claiming recovery without consequence or target record |
| Investigator | Distinguishing observed evidence from rumor with identified sources | NPC rumor rewritten as world truth |
| Envoy | Bounded negotiation/coordination with recorded interlocutors and consequences | Automatically controlling NPC consent |
| Ability Specialist | Authorized technique practice/use of the character's own sole principal ability | Creating an unrelated new principal ability as reward |

`Smith` should have a **separate profession/forging proof**: core identity and inherent properties, material provenance, smith experience, intended output, actual outcome, permitted affected target (weapon or wielder as justified), and later balance checks. No automatic “legendary exception” (H-23 remains undecided).

## 4. Acceptance tests to implement only with approved contract

1. **Pure read:** querying readiness twice returns identical outputs and does not mutate `GameState.snapshot()` or advance world time.
2. **No free class:** completing a quest without performance evidence does not promote a class.
3. **Role-appropriate evidence:** an Investigator proof cannot satisfy a Vanguard protection requirement merely by sharing an event ID.
4. **Source authenticity:** anonymous rumor, unknown actor, stale source revision, hidden NPC secret, or invented event is not accepted as proof.
5. **Replay safety:** re-loading, replaying a cutscene or re-submitting an event does not double-credit practice.
6. **Single primary ability:** character acquisition of an ability-derived technique does not increment the number of principal ability owners; legacy multi-ability saves require analysis, not silent deletion.
7. **Smith physical constraints:** training improves utilization of existing core properties, never invents an absent property or automatically applies identical modifier to both weapon and wielder.
8. **Quest branch honesty:** protect/investigate/repair each validates actions actually performed, with negative outcomes possible and with no implicit reward to unrelated skills.
9. **Persistence:** old version-1 saves load unchanged; changes to durable schema require separately versioned migration and rollback tests.
10. **Android projection:** the client only displays engine-owned decisions, never creates ranks or leaks hidden conditions/knowledge.

## 5. Narrative integration without pretending mechanics exist

- Chapter II `PROPOSED_VOLUME_II_CHAPTER_02_2026-10-29.md`: alternative decisions at an unsafe passage.
- Chapter III `PROPOSED_VOLUME_II_CHAPTER_03_2026-10-29.md`: *one hypothetical investigative continuation*, emphasizing limited knowledge, delayed supply, truthfulness, and no free class/ability.
- A future playable mission would need a new approved content pack, quest graph and stable actor/scene IDs. Gate Twelve / The Dead Relay remains the existing separate vertical-slice baseline and is **not** overwritten by these manuscripts.

## 6. Blockers and next safe implementation boundary

- **Canon:** WD-001 fictional-world/Tierra reconciliation, story protagonist continuity, and timeline are open. Vol II candidates are not owner-approved.
- **Progression:** target classes and Smith are not implemented; IDs, thresholds, save schema and source-of-proof adapter remain unapproved.
- **Code:** only targeted power validator repairs and tests are in the working PR; broader mechanics need a separate designed migration.
- **QA:** run and inspect the exact PR HEAD CI for Python and Android; obtain physical device evidence separately before any release claim.

**Decision:** do not add `GameState.classes`, alter `CURRENT_SCHEMA_VERSION`, award class ranks, or grant a second principal ability in this PR. The smallest safe next implementation is an approved read-only readiness query using evidence producers that already have trustworthy provenance; until then, this packet is a reviewable specification and test checklist only.
