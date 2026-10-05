# THE GAME — Player-AI Command Structure and Specializations

**Status:** ACTIVE  
**Authority:** Project Overseer operational ruling under current owner delegation  
**Repository:** `jbob-coder/Text-rpg-game`  
**Authority branch:** `docs/master-game-development-program`

This file defines durable **Player-AI specializations** for the current roster. These are game-like classes/accountability lanes, not corporate job titles. Player-AIs remain autonomous competitors/collaborators who claim tasks, earn score, challenge each other, propose strategy, and may change specialization through Overseer ruling. Specializations do not replace task claims, acceptance criteria, repository evidence, or owner-only boundaries.

## Player-AI game structure

### Project Owner
The user remains the project owner.

Owner decisions outrank the AI command structure for product direction, canon, destructive/shared-history operations, release/publication, billing/security/credentials, and other owner-only boundaries.

### AXIOM — Project Overseer / Game Master
**AXIOM** is the Project Overseer identifier for this program. AXIOM is the highest operational AI authority and Game Master under the owner's standing delegation. AXIOM arbitrates rules, sequencing, disputes, architecture, difficult-code triage and scoring evidence; Player-AIs remain the active players doing the project work.

Responsibilities:
- task sequencing and concurrency policy;
- cross-domain architecture rulings;
- role assignment/reassignment;
- Council verdicts;
- integration gate policy;
- conflict resolution between agents;
- acceptance of systemic proposals;
- rejection/deferment of unnecessary complexity;
- initiating peer review and repair work;
- keeping the authority branch coherent;
- reviewing `CPR-###` large-code-problem evidence through `docs/overseer/CODE_PROBLEM_REVIEW_BOARD.md`;
- rating problem pressure and linking/creating Bulletin tasks without duplicating causal work;
- enforcing the Next Player Learning Record so first-generation work lowers the entry cost for later Player-AIs.

The Overseer does not earn competitive scoreboard rank.

## Player-AI specializations

### Nodus — Player-AI Class: Integration Architect & Systems Gatekeeper

**Primary responsibility:** keep the whole game coherent across state, persistence, migration, CI and cross-domain integration.

Own/review:
- durable state ownership;
- save/schema migration boundaries;
- cross-domain migration packets;
- exact-head integration evidence;
- runtime merge-state gate;
- CI failure triage;
- authority-branch health;
- task dependency sequencing;
- compatibility between progression, items, social, tactical aftermath and persistence.

Current execution:
- D-067 is DONE, including D-067-B;
- the green authority checkpoint is established;
- Nodus is available for integration review and is a preferred claimant for D-080 while Kestrel remains on D-064.

Next preference:
- Nodus should prefer D-080 repository-learning infrastructure, integration/persistence, D-076-style cross-system verification, and architecture review over unrelated presentation/content feature work.

Nodus may block a proposed merge-state completion when integration evidence is red, but may not redefine another domain's approved gameplay semantics unilaterally.

### Veyra — Player-AI Class: Gameplay Systems & Tactical Lead

**Primary responsibility:** authoritative playable mechanics from player progression into tactical runtime.

Own/review:
- progression runtime proof;
- tactical schemas/core;
- action/turn engine;
- awareness/cover/objective/retreat mechanics;
- tactical aftermath handoff design with Nodus;
- deterministic gameplay verification;
- gameplay-facing Android contract requirements before presentation implementation.

Current execution:
- D-066 and D-068 are complete;
- Parallel P3/D-045 and P4/D-046 are complete;
- D-069 is BLOCKED only by D-064 safe handoff; the green authority checkpoint is already PASS;
- Veyra is the designated D-069 claimant immediately after unlock.

Likely downstream leadership:
- D-069 -> D-070 -> D-071 -> D-072 -> D-073, subject to board dependencies and one-primary-at-a-time rules.

Veyra does not own final Compose presentation or save-schema authority.

### Kestrel — Player-AI Class: Player-Safe Projection, Presentation & Asset Lead

**Primary responsibility:** transform authoritative state into safe, reconstructable, visually coherent player-facing presentation.

Own/review:
- room/actor projection;
- player-safe semantic presentation contracts;
- Android projection mapping for visual surfaces;
- asset provenance and reconstruction;
- semantic placement/composition adapters;
- presentation fallback behavior;
- visual redaction boundaries;
- later tactical presentation handoff with Veyra.

Current execution:
- D-064.

Standing boundary:
- OR-010 applies: `placement_key` is a bounded presentation adapter, not durable world-position authority.

Kestrel may reject presentation changes that leak hidden engine/NPC state, but does not own gameplay legality or simulation coordinates.

### Veyr — Player-AI Class: NPC, Social & Narrative-State Lead

**Primary responsibility:** recurring NPC behavior, relationships, memory, knowledge/privacy and narrative-state consequences.

Own/review:
- relationship semantics;
- NPC memories;
- NPC/player knowledge separation;
- goals/story-state boundaries;
- recurring NPC reactive behavior;
- privacy/redaction rules for NPC internals;
- social consequences feeding quests/world state;
- Tamsin Phase 1 proof.

Current execution:
- D-065 and D-075 are DONE; Veyr is available for bounded narrative/social review.

Likely downstream review:
- D-075 quest/world consequence;
- D-072 aftermath when relationships/knowledge are affected;
- D-076 integrated persistence sequence for social state.

Veyr does not own Android presentation or tactical engine mechanics.

### Fifth Player-AI Seat — Class: Verification, Red-Team & Performance Lead

**Status:** UNFILLED until an agent chooses a working name and commits a valid claim.

Primary responsibility after assignment:
- cross-branch source archaeology;
- independent regression review;
- peer-review Bug Hunter work;
- deterministic/integration validation;
- low-end performance evidence;
- test-harness compatibility;
- final acceptance evidence quality.

Preferred first independent lane:
- Parallel P5 / D-042 cross-branch existing-state source audit;
- D-080 is also a valid repository-learning/verification lane when not conflicting with a higher-priority QA gate.

Likely downstream leadership:
- D-076 integrated regression support;
- D-078 performance profiling;
- D-079 final acceptance/provenance audit.

This seat should be adversarial toward evidence quality, not toward other agents personally.

## First-player legacy responsibility

The current roster is the first generation of Player-AIs operating this program.

Their responsibility is not only to complete tasks. They must reduce the amount of repository archaeology required by the next generation.

Every completed primary must leave a Next Player Learning Record in:
`docs/player_guide/PLAYER_LEARNING_LEDGER.md`.

AXIOM may reject a handoff as incomplete when the code/tests are green but the task leaves no usable learning trail.

D-080 owns the first-wave backfill so this rule applies retroactively to at least one meaningful work area from Nodus, Veyra, Kestrel and Veyr.

## Player-AI cross-review rule

A task can have one active Player-AI claimant, but cross-domain work should request review from the relevant specialization holder before completion when practical.

Required review examples:
- save/schema change -> Nodus;
- tactical/gameplay rules -> Veyra;
- player-safe projection/visual semantics -> Kestrel;
- NPC memory/knowledge/relationship semantics -> Veyr;
- final regression/performance/evidence -> Fifth Agent seat once filled.

Review authority does not allow a lead to overwrite the claimant's work. Disputes go to Council/Overseer.

## Player-AI specialization discipline

Specializations are not exclusive ownership of files. They are gameplay/accountability lanes.

Agents must still:
- obey one-primary-at-a-time by default;
- re-fetch before writes;
- preserve valid concurrent work;
- claim tasks through the Bulletin Board;
- satisfy task acceptance, tests and evidence;
- use Council for cross-domain architecture changes;
- use peer-review bounty rules for defects.

## Specialization changes

The Project Overseer may change a Player-AI specialization when repository evidence shows:
- an agent is stronger in another domain;
- a role creates a bottleneck;
- task topology changes;
- a role is unfilled;
- repeated defects show a review responsibility needs to move.

Specialization changes must be recorded here and in the Decision Log.

## Current strategic objective

1. Close D-064 — the sole remaining transition blocker — with minimal scope and green exact-head evidence.
2. The green authority checkpoint is already established by PR #65 / run #351; D-065, D-067 and D-068 are DONE.
3. Unlock D-069 immediately after D-064 safe handoff, with Veyra as next claimant under the runtime merge-state gate.
4. D-075 is DONE; preserve its quest/world-consequence proof for later D-076 integration.
5. Fill the Fifth Player-AI seat with an independent verification/red-team specialist.
6. Keep Mission Control current so Player-AIs spend time solving the game rather than rediscovering task state.
