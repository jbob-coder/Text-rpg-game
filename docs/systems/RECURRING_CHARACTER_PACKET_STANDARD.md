# THE GAME — Recurring Character Reconstruction Packet Standard

Status: **APPROVED FIRST-PASS V05 CONTRACT / AUTHORING TEMPLATE**
Parent:
- docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md
Consumes:
- NPC_CHARACTER_IDENTITY_PROFILE_STANDARD.md
- NPC_PERSONALITY_BEHAVIOR_STANDARD.md
- NPC_MEMORY_EVENT_STANDARD.md
- NPC_KNOWLEDGE_BELIEF_PRIVACY_STANDARD.md
- NPC_RELATIONSHIP_STATE_STANDARD.md
- NPC_GOALS_DECISION_STANDARD.md
- NPC_SCHEDULE_PRESENCE_STANDARD.md
- FACTION_HIERARCHY_MEMBERSHIP_STANDARD.md

## 1. Purpose

Define the minimum complete packet for a named recurring NPC.

A recurring character is not complete merely because a name, portrait, or dialogue scene exists. The packet must connect identity, runtime state, world placement, social behavior, visuals, privacy, and tests.

## 2. Packet sections

Every recurring-character packet should contain:

1. Identity
2. Canon/provenance
3. World placement
4. Visual identity
5. Personality
6. Starting relationships
7. Knowledge/beliefs
8. Memory baseline
9. Goals
10. Schedule/presence
11. Faction/institution
12. Story-state tracks
13. Quest/content hooks
14. Party/companion behavior if applicable
15. Tactical behavior if applicable
16. Injury/lifecycle
17. Player-safe projection
18. Save/migration
19. Tests
20. Open decisions

## 3. Identity section

Must include:
- stable NPC ID;
- player-facing naming rules;
- role;
- canon state;
- aliases;
- immutable identity vs mutable state boundary.

## 4. Provenance

Record:
- source content file;
- creation/approval context;
- visual source;
- branch/head for implemented assets;
- superseded references.

No character should silently inherit another identity's art.

## 5. World placement

Define:
- home;
- work;
- current starting location;
- valid route/schedule assumptions;
- parent-world unknowns.

If geography is unknown, mark it.

## 6. Visual identity

Link:
- gameplay sprite;
- portrait;
- room actor;
- paper-doll/equipment where applicable;
- permanent anchors;
- allowed temporary variants.

Final visuals require provenance/QA.

## 7. Social state

List:
- personality values;
- starting player relationship;
- important NPC-to-NPC relationships when needed;
- relationship event rules.

Do not create every possible relationship upfront.

## 8. Knowledge

Document:
- what NPC initially knows;
- what they do not know;
- secret/private information;
- how key facts can be learned;
- what can be shared.

## 9. Memories

Define only initial memories that materially affect behavior/story.

Future memories come from events.

## 10. Goals

List active starting goals and creation triggers for later goals.

Each goal needs source, priority, progress policy, privacy, and resolution.

## 11. Schedule/presence

State:
- normal location/activity pattern;
- story overrides;
- party behavior;
- absence/removal behavior.

## 12. Story tracks

For each story_state track:
- track_id;
- allowed states;
- legal transitions;
- transition triggers;
- player-facing consequence.

This prevents impossible jumps.

## 13. Quest hooks

Identify exact quest IDs/objectives/scenes that read or mutate the NPC.

Do not leave hidden string references undocumented.

## 14. Party/companion

If recruitable/temporary party:
- join/leave conditions;
- follow presence;
- order vocabulary;
- autonomy constraints;
- aftermath state.

## 15. Tactical

If combat-capable:
- actor profile;
- action loadout;
- AI/companion profile;
- injury/lifecycle rules;
- combat knowledge;
- retreat/surrender.

A noncombat character does not need fake combat stats.

## 16. Player-safe projection

Specify exactly what can appear:
- name/label;
- portrait;
- visible condition;
- visible role;
- contextual relationship;
- dialogue/interaction actions.

Private goals/memory/knowledge stay out.

## 17. Save/migration

Identify:
- durable fields;
- stable IDs;
- schema impact;
- fallback if optional new fields are missing;
- migration from old content.

## 18. Required tests

At minimum:
- identity lookup;
- starting state;
- relationship gate;
- knowledge gate;
- story-state transitions;
- goal state;
- presence;
- save/load;
- player-safe redaction;
- visual identity binding where implemented.

## 19. Completion levels

DRAFT:
schema filled incompletely.

PROVISIONAL:
sufficient for vertical slice.

RECONSTRUCTION_READY:
all used systems/consumer links/tests documented.

IMPLEMENTED:
runtime exists but not necessarily verified.

VERIFIED:
exact-head tests/runtime evidence exists.

## 20. Phase 1

NPC_TAMSIN receives the first concrete packet under TAMSIN_PHASE1_SOCIAL_PROOF_PACKET.md.
