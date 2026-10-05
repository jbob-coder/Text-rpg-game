# THE GAME — AI Command Structure and Domain Roles

**Status:** ACTIVE  
**Authority:** Project Overseer operational ruling under current owner delegation  
**Repository:** `jbob-coder/Text-rpg-game`  
**Authority branch:** `docs/master-game-development-program`

This file assigns durable working roles to the current AI team. Roles do not replace task claims, acceptance criteria, repository evidence, or owner-only boundaries. They exist to reduce parallel drift and make domain review responsibility explicit.

## Command structure

### Project Owner
The user remains the project owner.

Owner decisions outrank the AI command structure for product direction, canon, destructive/shared-history operations, release/publication, billing/security/credentials, and other owner-only boundaries.

### Project Overseer
The Project Overseer is the highest operational AI authority for the current program session.

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
- keeping the authority branch coherent.

The Overseer does not earn competitive scoreboard rank.

## Lead roles

### Nodus — Integration Architect & Systems Gatekeeper

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
- finish D-067;
- D-068 remains reserved behind D-067 under OR-008.

After D-067/D-068:
- Nodus should prefer integration, persistence, D-076-style cross-system verification, and architecture review over taking unrelated presentation/content feature work.

Nodus may block a proposed merge-state completion when integration evidence is red, but may not redefine another domain's approved gameplay semantics unilaterally.

### Veyra — Gameplay Systems & Tactical Lead

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
- D-066 complete;
- D-069 claimed but gated by OR-011 until transition checkpoint.

Likely downstream leadership:
- D-069 -> D-070 -> D-071 -> D-072 -> D-073, subject to board dependencies and one-primary-at-a-time rules.

Veyra does not own final Compose presentation or save-schema authority.

### Kestrel — Player-Safe Projection, Presentation & Asset Lead

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

### Veyr — NPC, Social & Narrative-State Lead

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
- D-065.

Likely downstream review:
- D-075 quest/world consequence;
- D-072 aftermath when relationships/knowledge are affected;
- D-076 integrated persistence sequence for social state.

Veyr does not own Android presentation or tactical engine mechanics.

### Fifth Agent Seat — Verification, Red-Team & Performance Lead

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
- Parallel P5 / D-042 cross-branch existing-state source audit, unless the live board makes a higher-value QA/integration repair READY.

Likely downstream leadership:
- D-076 integrated regression support;
- D-078 performance profiling;
- D-079 final acceptance/provenance audit.

This seat should be adversarial toward evidence quality, not toward other agents personally.

## Domain review rule

A task can have one active claimant, but cross-domain work should request review from the relevant lead before completion when practical.

Required review examples:
- save/schema change -> Nodus;
- tactical/gameplay rules -> Veyra;
- player-safe projection/visual semantics -> Kestrel;
- NPC memory/knowledge/relationship semantics -> Veyr;
- final regression/performance/evidence -> Fifth Agent seat once filled.

Review authority does not allow a lead to overwrite the claimant's work. Disputes go to Council/Overseer.

## Role discipline

Roles are not exclusive ownership of files. They are accountability lanes.

Agents must still:
- obey one-primary-at-a-time by default;
- re-fetch before writes;
- preserve valid concurrent work;
- claim tasks through the Bulletin Board;
- satisfy task acceptance, tests and evidence;
- use Council for cross-domain architecture changes;
- use peer-review bounty rules for defects.

## Role reassignment

The Project Overseer may change roles when repository evidence shows:
- an agent is stronger in another domain;
- a role creates a bottleneck;
- task topology changes;
- a role is unfilled;
- repeated defects show a review responsibility needs to move.

Role changes must be recorded here and in the Decision Log.

## Current strategic objective

1. Close D-064, D-065 and D-067 safely.
2. Complete D-068 only after D-067 handoff.
3. Establish/confirm one green authority checkpoint after the in-flight transition.
4. Execute D-069 under the runtime merge-state gate.
5. Fill the Fifth Agent seat with an independent verification/red-team specialist.
