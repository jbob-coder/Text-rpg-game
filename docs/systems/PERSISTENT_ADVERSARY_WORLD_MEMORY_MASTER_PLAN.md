# THE GAME — Persistent Adversary & World Memory Master Plan

Status: **APPROVED FIRST-PASS V09 MASTER / ORIGINAL SYSTEM / RUNTIME NOT IMPLEMENTED**
Parents:
- docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md
- docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md
- docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md
- docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md
Related:
- docs/systems/NPC_MEMORY_EVENT_STANDARD.md
- docs/systems/NPC_KNOWLEDGE_BELIEF_PRIVACY_STANDARD.md
- docs/systems/INJURY_CONDITION_AFTERMATH_STANDARD.md

## 1. Purpose

Define an original persistent-adversary and world-memory layer in which selected recurring opponents can remember meaningful encounters, survive or leave the world, adapt inside authored limits, move through valid world structures, and reappear only when world state supports it.

This system is not a renamed copy of another game's branded hierarchy feature.

Its authority comes from THE GAME's existing:
- stable NPC identity;
- memory;
- knowledge/belief;
- goals;
- relationships;
- faction membership;
- tactical aftermath;
- world routes;
- save/persistence.

## 2. Core principle

Persistence is selective.

Most hostile encounter entities remain encounter-local.

An adversary becomes persistent only when an authored eligibility rule gives the world a reason to remember that individual.

Persistence must add:
- continuity;
- consequence;
- world logic;
- recognizable recurrence.

It must not add:
- arbitrary stat inflation;
- forced recurring cameos;
- omniscient counters;
- endless replacement ladders;
- UI-only rivalry.

## 3. System flow

Preferred flow:

eligible world actor
-> meaningful encounter
-> authoritative encounter aftermath
-> selected durable memories/knowledge/injury/outcome
-> bounded adaptation decision
-> lifecycle/world-location update
-> recurrence eligibility
-> player-safe intel projection
-> later encounter/social/world consequence.

Every transition must be inspectable.

## 4. State ownership

Persistent adversary state belongs in the gameplay/world domain, not Compose.

Target persistent state may include:
- stable NPC/adversary ID;
- eligibility status;
- lifecycle;
- current location/territory;
- faction/role/rank;
- injuries/conditions;
- memories;
- knowledge/beliefs;
- goals;
- relationship/rival dimensions where adopted;
- encounter history summary;
- adaptation records;
- availability/recurrence state;
- succession/role state;
- last-known player-facing intel boundary.

Do not duplicate fields already owned by the ordinary NPC/social system.

## 5. World memory

World memory is broader than one adversary.

Meaningful events may persist through:
- NPC memories;
- faction/institution records;
- location state;
- rumors;
- quest/world flags;
- ownership/control;
- damage/repair;
- deaths/captures/escapes.

The adversary system consumes these records; it is not the only owner.

## 6. Encounter memory

Only significant combat/social events should create adversary memories.

Examples:
- Jack spared/captured/injured the adversary;
- adversary defeated or escaped Jack;
- an ally/leader died;
- a known technique was observed;
- a route or location became dangerous;
- an agreement or betrayal occurred.

The actor can remember only what they perceived or later learned.

## 7. Adaptation

Adaptation must be bounded by:
- actor capabilities;
- equipment access;
- knowledge;
- faction resources;
- injury;
- time;
- location;
- doctrine;
- authored adaptation options.

Adaptation may change:
- preferred tactics;
- equipment selection from valid inventory/access;
- route choice;
- allies;
- engagement/retreat preference;
- preparation for a known player tactic.

It may not silently grant impossible powers or inflate stats merely because the adversary lost.

## 8. Lifecycle

Candidate lifecycle:
- active;
- injured;
- recovering;
- displaced;
- captured;
- retired;
- dead;
- unknown.

Lifecycle transitions are authoritative and save-persistent.

Dead/retired actors do not reappear unless a separate canon mechanism explicitly permits it.

## 9. Recurrence

A persistent adversary may recur only when:
- lifecycle permits;
- world route/location permits;
- time/cooldown permits;
- faction/goal permits;
- quest/story state permits;
- player/adversary knowledge permits the meeting logic.

Recurrence is not a random UI event.

## 10. Hierarchy and succession

Faction role/rank change comes from the world's original faction system.

A successor may inherit:
- office;
- responsibility;
- resources;
- public consequences.

A successor does not inherit private memories or personal relationship history automatically.

## 11. Territory and routing

Adversaries occupy the same world-location/route authority as other actors.

They cannot teleport between unrelated regions to force recurrence.

Movement may be abstracted off-screen, but must remain route/world-state coherent.

## 12. Player-facing intel

Player sees only learned/observable information:
- known identity;
- known affiliation;
- visible injury;
- last known encounter/location;
- observed tactics;
- rumors;
- known status.

Never project hidden goals, exact adaptation score, secret route, internal utility, or unknown abilities.

## 13. Performance

Low-end Android design requires event-driven simulation.

Do not continuously simulate every adversary every frame.

Re-evaluate adversary state on bounded triggers:
- encounter aftermath;
- meaningful time boundary;
- faction/world event;
- route/location event;
- quest transition.

## 14. Save policy

Persistent adversary state must survive save/load once implemented.

Stable references must remain valid through:
- promotion;
- injury;
- capture;
- death;
- displacement;
- succession.

Any new durable container requires explicit save-schema migration.

## 15. Originality boundary

The system must use original:
- terminology;
- hierarchy logic;
- adaptation rules;
- recurrence rules;
- UI;
- content;
- fiction;
- formulas.

Broad genre ideas such as recurring enemies, memory, promotion and retaliation are not enough to justify copying a proprietary combined system.

## 16. First-pass children

This master is implemented by:
- ADVERSARY_ELIGIBILITY_IDENTITY_STANDARD.md
- ADVERSARY_ENCOUNTER_MEMORY_ADAPTATION_STANDARD.md
- ADVERSARY_LIFECYCLE_RECURRENCE_STANDARD.md
- ADVERSARY_HIERARCHY_SUCCESSION_STANDARD.md
- ADVERSARY_TERRITORY_ROUTING_STANDARD.md
- ADVERSARY_PLAYER_SAFE_INTEL_STANDARD.md
- GATE_TWELVE_ADVERSARY_PROOF_PACKET.md

## 17. Implementation order

1. adopt eligibility/state schema;
2. map ordinary NPC fields that can be reused;
3. define durable save migration;
4. implement aftermath memory/adaptation packet;
5. implement lifecycle/availability;
6. implement route/world recurrence query;
7. implement player-safe intel;
8. author one bounded proof adversary;
9. test save/load/removal;
10. expand only after world/faction content supports it.

## 18. Completion boundary

V09 first-pass documentation can be complete while runtime remains absent.

Runtime acceptance later requires one real eligible adversary to:
- persist through encounter;
- remember a significant event;
- adapt inside authored bounds;
- recur only under valid world conditions;
- expose only safe intel;
- survive save/load;
- be removed permanently without broken references.
