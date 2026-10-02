# THE GAME — NPC, Social Hierarchy & Persistent Adversary Master Plan

Status: **FOUNDATIONAL / IMPLEMENTATION PARTIAL AT LOWER SCOPE**
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
