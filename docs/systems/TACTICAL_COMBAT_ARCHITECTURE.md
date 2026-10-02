# Tactical Combat Architecture

Status: **REVIEWABLE / SYSTEM ARCHITECTURE**
Domain: Combat
Requirement: `P-COMBAT-001`

## 1. Design goal

Create an original tactical combat system with readable positional decision-making, action economy, party roles, environmental interaction and persistent consequences.

The design may use general turn-based squad-tactics principles, but it must not copy protected UI, terminology, characters, maps, exact rule tables, or presentation from another game.

## 2. Combat authority

Combat state belongs to the rules engine.

UI may:
- display combatants;
- display valid actions;
- show range/cover/target previews;
- submit action intent;
- animate results.

UI may not decide hit chance, damage, legal movement, status application, or enemy AI outcomes.

## 3. Combat entity model

Combat-capable entities may include:
- player;
- party NPC;
- allied NPC;
- hostile human/NPC;
- bestia;
- persistent adversary;
- environmental hazard/object.

Each combatant should expose a common combat projection while preserving category-specific rules.

## 4. Encounter phases

Target high-level phases:

1. encounter initialization;
2. awareness/initiative setup;
3. alternating or ordered turns;
4. movement/action resolution;
5. reactions/interrupts;
6. status/environment update;
7. objective check;
8. encounter end;
9. persistent consequence resolution.

Exact turn-order algorithm remains unresolved.

## 5. Action economy

Candidate structure:
- movement allowance or movement action;
- primary action;
- limited reaction/interrupt resource;
- free/contextual actions only when explicitly authored.

The final economy must avoid:
- unlimited action chaining;
- hidden UI-only costs;
- inconsistent NPC/player rules without justification.

## 6. Position

Combat positioning may use:
- discrete cells;
- zones/lanes;
- graph nodes;
- measured local coordinates.

Final representation is unresolved.

Selection must support:
- cover;
- line of sight;
- range;
- movement cost;
- environmental hazards;
- mobile-readable UI.

## 7. Cover

Cover is an authored/environment-derived combat property.

Potential states:
- none;
- partial;
- strong;
- directional.

Exact bonuses/formulas remain unresolved.

Cover should not be a cosmetic icon disconnected from geometry/state.

## 8. Line of sight and range

Rules must define:
- visibility;
- obstruction;
- weapon/ability ranges;
- minimum range where relevant;
- elevated/blocked states if adopted.

Do not expose targets that authoritative combat state marks unseen unless a detection/knowledge rule permits it.

## 9. Accuracy and defense

Accuracy/evasion/guard may derive from:
- attributes;
- skills;
- equipment;
- position;
- cover;
- status;
- range;
- ability effects;
- knowledge/surprise.

Exact formula remains unresolved.

## 10. Damage and body interaction

Baseline combat supports health/status consequences.

Potential future body-part targeting for beasts or specific enemies is allowed, but requires a separate body-part contract defining:
- targetable parts;
- hit effects;
- break/sever rules if used;
- resource consequences;
- visual overlays;
- balance.

Do not assume body-part combat is global for every enemy.

## 11. Objectives

Encounters should support goals beyond “defeat everything.”

Potential objective types:
- escape;
- survive;
- protect;
- capture;
- retrieve;
- hold position;
- disable device;
- reach location;
- investigate;
- force retreat.

Objective state remains engine-owned.

## 12. Reactions

Reaction mechanics may include original equivalents of:
- defensive response;
- intercept;
- guarded shot/action;
- counter;
- assistance.

Names and exact behavior must be original project design.

## 13. Party/NPC autonomy

Party members are not necessarily direct puppets.

Future modes may support:
- direct player command;
- command with personality/relationship constraints;
- autonomous tactical choice;
- refusal/override in special circumstances.

Final control model remains unresolved.

## 14. Beast combat

Bestias use the shared combat framework plus species-specific rules.

Potential additions:
- movement type;
- pack behavior;
- anatomy;
- territorial behavior;
- flee/pursue;
- environmental interaction;
- persistent injury;
- learned behavior for persistent adversaries.

## 15. Terrain/environment

Combat maps/scenes can expose:
- cover;
- hazard;
- destructible/interactive object;
- elevation if adopted;
- doors/gates;
- choke points;
- environmental resource/effect.

Environment state must remain compatible with world/location state.

## 16. Persistence

After combat, persist relevant:
- health/injury;
- conditions;
- ammunition/resources if used;
- equipment damage if used;
- deaths/absence;
- quest outcomes;
- beast injury/escape;
- adversary memory;
- world-state changes;
- loot/resource eligibility.

## 17. Determinism

The existing project values deterministic/reproducible rules.

Combat randomness, if used, must be seedable/reproducible from authoritative state so tests/save analysis remain possible.

## 18. UI projection

Player-safe combat projection should eventually include:
- visible combatants;
- player-known identity;
- current turn/phase;
- legal actions;
- movement/range preview;
- visible statuses;
- objective;
- player-known cover/terrain;
- projected action cost.

Hidden AI intent/hidden stats remain hidden unless intentionally revealed.

## 19. Failure/recovery

Combat action resolution should be transactional where practical.

Invalid action:
- no partial state mutation;
- return player-safe reason.

Runtime interruption/save:
- define safe save boundaries before final implementation.

## 20. Implementation readiness gaps

Still required:
- position model;
- turn order;
- action economy exact values;
- hit/damage formulas;
- cover values;
- movement costs;
- reaction rules;
- party-control model;
- AI architecture;
- combat UI;
- body-part scope;
- encounter generation.

## 21. Acceptance expectation

Implementation-ready when one bounded encounter can be fully specified with:
- map/position;
- participants;
- initiative;
- legal actions;
- movement;
- targeting;
- damage/status;
- objective;
- AI;
- persistence;
- deterministic tests;
- mobile UI projection.
