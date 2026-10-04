# THE GAME — NPC, Social Hierarchy & Persistent Adversary Master Plan

Status: **V05 FIRST-PASS CONTRACT LAYER ESTABLISHED / IMPLEMENTATION PARTIAL / V09 ADVERSARY DETAIL STILL PARTIAL**
Parents:
- `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`
- `docs/systems/GAMEPLAY_SYSTEM_REBUILD_MATRIX.md`
- `docs/world/WORLD_SCALE_DOCUMENTATION_BLUEPRINT.md`

## 1. Purpose

Expand the current NPC relationship/knowledge/memory foundation into a persistent world-social simulation and an original persistent adversary system.

The design may use the broad genre idea that recurring enemies remember encounters and evolve. It must not copy protected names, hierarchy UI, dialogue patterns, archetypes, branded progression, or proprietary implementation from another game.

## 2. NPC authority model

Each persistent NPC should eventually have:
- stable ID;
- identity;
- location/home/work;
- faction;
- social/legal status;
- attributes/skills/abilities where needed;
- equipment/inventory where needed;
- relationships;
- knowledge;
- memories;
- goals;
- schedule;
- current condition;
- world-state flags;
- portrait/sprite/provenance.

The engine owns these. The Android UI receives player-safe projections.

## 3. NPC memory

Memory entries need:
- event ID;
- timestamp/world time;
- participants;
- location;
- perception source;
- confidence;
- emotional/relationship impact;
- public/private status;
- decay/persistence policy;
- consequences.

Not every world event becomes a detailed memory.

## 4. Knowledge

Separate:
- world truth;
- NPC knowledge;
- player knowledge;
- rumor;
- false belief;
- uncertain inference.

NPCs should act on what they know/believe, not omniscient truth.

## 5. Goals

Goal record:
- stable goal ID;
- owner NPC;
- priority;
- progress;
- source;
- target;
- blockers;
- expiration;
- success/failure;
- hidden/player-visible state.

Goals may conflict.

## 6. Relationships

Potential axes:
- trust;
- respect;
- affection;
- fear;
- suspicion;
- debt;
- loyalty;
- hostility;
- rivalry.

Do not add axes casually. The current system already has relationship dimensions; final taxonomy needs migration review.

## 7. Schedules

NPC schedule model should support:
- home;
- work;
- travel;
- social;
- sleep/rest;
- emergencies;
- faction orders;
- quest overrides;
- injury/recovery;
- combat/rival pursuit.

Off-screen simulation needs a bounded update budget.

## 8. Social hierarchy

Model distinct dimensions rather than one universal social score:
- legal citizenship/status;
- wealth;
- profession;
- institutional rank;
- military rank;
- guild/faction rank;
- reputation;
- ability/combat rank if culturally relevant;
- criminal status;
- residency;
- lineage/culture/species only if canonically authored.

## 9. Prejudice / discrimination / racism in fictional worldbuilding

If included, separate:
- institutional law/policy;
- regional cultural norm;
- faction ideology;
- individual NPC belief;
- player reputation/identity;
- economic/access consequence.

Do not model a universal "racism stat."

Documentation must define:
- targets;
- causes/history;
- regional variation;
- legal consequences;
- social consequences;
- resistance/mobility;
- exceptions;
- how NPC individuality prevents stereotypes.

## 10. Factions and institutions

Each faction:
- stable ID;
- purpose;
- leadership;
- territory;
- resources;
- laws/rules;
- ranks;
- allies/enemies;
- reputation;
- NPC membership;
- goals;
- succession;
- economy;
- combat doctrine;
- world events.

## 11. Persistent adversary system — working original model

Working generic name: **Persistent Adversary Network**.

This name is internal and may change.

Each adversary is a persistent NPC with additional rival state.

### Rival state may include
- rivalry intensity;
- fear;
- respect;
- hostility;
- obsession/priority;
- confidence;
- known player tactics;
- injuries/scars;
- wins/losses;
- escapes;
- allies;
- subordinates if faction structure supports it;
- ambitions;
- current hunt/avoidance behavior.

## 12. Encounter memory

After encounters, adversaries may remember:
- player spared them;
- player injured them;
- they defeated the player;
- they fled;
- an ally died;
- a technique was observed;
- a location became dangerous;
- player reputation.

Counter-preparation must use knowledge they plausibly have.

## 13. Rank/status evolution

Status change is allowed only through the world's original faction system.

Possible causes:
- mission success/failure;
- leader death;
- political change;
- resource control;
- combat record;
- disciplinary action;
- player action.

Do not recreate a branded fixed ladder merely because another game uses one.

## 14. Succession and replacement

When an adversary dies/leaves:
- faction may fill role;
- successor may inherit responsibilities, not memories;
- rumors/reputation may transfer partially;
- power vacuum may create event.

Replacement must be world-logical.

## 15. Injury/scars

Persistent visual injuries require:
- actual injury record;
- recovery;
- portrait/sprite variant;
- no cosmetic scar solely to imitate external reference.

## 16. Rival events

Potential event categories:
- ambush;
- challenge;
- negotiation;
- intimidation;
- retaliation;
- rescue;
- betrayal;
- alliance shift;
- bounty;
- pursuit;
- retreat;
- faction order.

Events must be generated from state/goals, not arbitrary repetition.

## 17. Player-facing rival intel

Only show known information:
- name if known;
- faction if known;
- last encounter;
- visible injury;
- known abilities;
- known relationship/rival state in qualitative form if designed;
- rumors.

Never show hidden goal trees or omniscient hierarchy.

## 18. Social/economic integration

NPC status affects:
- access;
- prices only if economy supports it;
- legal treatment;
- faction help;
- quest availability;
- housing/work;
- guards;
- travel;
- rumors.

No UI-only social rule.

## 19. Pixel-art integration

Recurring NPC requires:
- gameplay sprite;
- portrait;
- equipment layers if supported;
- expressions;
- injury/status variants only when state supports them;
- room presence anchors;
- character panel mapping.

Named characters must not inherit another NPC's identity art.

## 20. Required future child docs

- NPC schedule simulation;
- faction registry;
- social hierarchy registry;
- reputation system;
- prejudice/discrimination regional matrix if canon;
- persistent adversary event generator;
- rival UI/player-safe projection;
- succession rules.

## 21. Open decisions

- final relationship axes;
- schedule time granularity;
- off-screen simulation frequency;
- procedural NPC scope;
- faction rank models;
- rivalry formulas;
- promotion/succession formulas;
- procedural titles;
- adversary cap per region;
- persistence/performance budget.


## Originality review qualification — 2026-10-02

Original names, art and UI address expression reuse; they do not alone establish patent clearance. US10926179B2 and its linked family are a relevant design-review source: https://patents.google.com/patent/US10926179B2/en . Proposed combined promotion/encounter/traits/hierarchy behavior remains subject to claim-aware review; no legal clearance is asserted. Continue original social-memory/goals design and document alternatives; do not implement a branded system by renaming it.


## 22. Selective persistent-adversary detail extraction — 2026-10-03

Status: **PROPOSED DESIGN / BOUNDED TARGET DETAIL / IMPLEMENTATION NOT CLAIMED**

Source provenance:
- `docs/settlement-region-build-plan@65d2db8538c1b8302c314f2fbe9eb7a1b585b51d`;
- `docs/systems/PERSISTENT_ADVERSARY_SYSTEM.md`;
- source blob `d32d31a5f0f8243ae4d400270f7ec807fe6aecdf`;
- selectively extracted under D-044.

This section supplements the current Persistent Adversary Network design. It does not choose exact formulas, active-rival caps, recurrence timers or death policy.

### 22.1 Eligibility

Not every hostile entity becomes persistent.

A future eligibility policy may admit, when its owning domain supports it:

- hostile NPC;
- faction operative;
- criminal/bandit-type actor if such a category exists in canon;
- rival hunter/competitor;
- persistent beast;
- another explicitly authored recurring adversary.

Eligibility must be deliberate and inspectable.

Do not persist every disposable encounter entity merely to make the system visible.

### 22.2 Bounded adaptation

After authoritative encounter memory exists, an adversary adaptation may affect:

- tactics;
- equipment where the entity can own equipment;
- resistance/behavior within authored capability;
- route choice;
- allies/pack behavior;
- territory;
- retreat/engagement preference;
- dialogue/presentation for characters where applicable.

Hard rule:

**adaptation must remain inside authored bounds and must not become arbitrary AI stat inflation.**

The source event/memory that justifies an adaptation should be traceable.

### 22.3 Beast adversaries

A persistent beast may participate without being forced into a human social/rank model.

Potential persistent beast state may include:

- injury;
- territory;
- pack status;
- fear/aggression toward the player;
- learned response;
- migration change;
- response to hunting pressure.

Exact beast intelligence/learning limits come from the beast species/world authority.

### 22.4 Recurrence selection

A recurring adversary should reappear only when the world state supports it.

Candidate selection inputs include:

- current location/territory;
- world state;
- availability/lifecycle state;
- player/adversary encounter history;
- faction/pack state;
- authored cooldown/timing rule if adopted;
- quest/event conditions.

Do not inject a rival into unrelated scenes merely to keep the feature visible.

Recurrence is subordinate to world/quest authority.

### 22.5 Lifecycle states

The system needs an explicit authoritative lifecycle rather than an implicit “exists/does not exist” flag.

Candidate vocabulary:

- `active`;
- `injured`;
- `recovering`;
- `displaced`;
- `captured`;
- `retired`;
- `dead`;
- `unknown`.

This vocabulary is **PROPOSED DESIGN** until the final schema is adopted.

Permanent removal/death must remain authoritative and persistent.

Replacement/succession may inherit a role/responsibility, but must not silently inherit private memories.

### 22.6 Determinism and inspectability

Selection/adaptation may use seeded deterministic variation if the final implementation needs variety.

Regardless of randomization strategy:

- state transitions must be inspectable;
- the triggering input/event must be testable;
- save/load must reproduce the authoritative state;
- retries/reloads must not generate arbitrary contradictory outcomes merely because UI recomposed.

### 22.7 Minimum implementation acceptance scenario

A bounded first implementation is not accepted until one real eligible adversary can:

1. enter persistent state through an authored rule;
2. record one significant encounter;
3. change in a traceable bounded way because of that encounter;
4. become eligible to reappear only under valid world conditions;
5. expose only player-safe learned/visible information;
6. preserve authoritative rival state through save/load;
7. retire/die/be removed without corrupting references;
8. leave unrelated scenes unaffected.

This is an acceptance target, not evidence that the system exists today.


## 23. V05 first-pass child contract suite — 2026-10-04

The character/NPC/social first-pass layer now includes:

- NPC_CHARACTER_IDENTITY_PROFILE_STANDARD.md
- NPC_PERSONALITY_BEHAVIOR_STANDARD.md
- NPC_MEMORY_EVENT_STANDARD.md
- NPC_KNOWLEDGE_BELIEF_PRIVACY_STANDARD.md
- NPC_RELATIONSHIP_STATE_STANDARD.md
- NPC_GOALS_DECISION_STANDARD.md
- NPC_SCHEDULE_PRESENCE_STANDARD.md
- FACTION_HIERARCHY_MEMBERSHIP_STANDARD.md
- SOCIAL_CONSEQUENCE_RUMOR_PROPAGATION_STANDARD.md
- RECURRING_CHARACTER_PACKET_STANDARD.md
- TAMSIN_PHASE1_SOCIAL_PROOF_PACKET.md

Together with this master, V05 has 12 / 12 first-pass canonical units.

This closes the V05 breadth floor only. It does not complete:
- world-scale NPC population;
- final faction catalog;
- final daily schedules;
- full rumor network;
- persistent adversary V09 implementation;
- final social UI;
- runtime migration of normalized identity/schedule/memory fields.

Phase 1 social proof should use NPC_TAMSIN rather than inventing a new recurring character.
