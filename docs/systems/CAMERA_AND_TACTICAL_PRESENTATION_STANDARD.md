# THE GAME — Camera, Spatial Presentation & Tactical View Standard

Status: **APPROVED DESIGN DIRECTION / DOCUMENTATION AUTHORITY / IMPLEMENTATION MAY PROCEED IN BOUNDED SLICES**  
Repository: `jbob-coder/Text-rpg-game`  
Parent authorities:
- `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`
- `docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md`
- `docs/android/APPLICATION_UX_MASTER_PLAN.md`
- `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`

Owner decision date: 2026-10-04 AST

## 1. Purpose

Lock the spatial presentation and tactical-combat camera direction for THE GAME so world, combat, UI, map, actor, asset, performance, and Android documentation no longer drift toward incompatible camera models.

This is a design authority. It does not require one rendering engine implementation technique as long as the shipped result preserves the contracts below.

## 2. Product-level camera decision

THE GAME uses a **2D / 2.5D orthographic three-quarter presentation** as its primary in-world visual language.

The camera is:
- oblique / three-quarter rather than first-person or over-the-shoulder third-person;
- authored rather than freely orbiting;
- fixed in orientation for a given presentation space unless a documented exception exists;
- capable of bounded pan/zoom where needed;
- pixel-art compatible and nearest-neighbor safe;
- designed to remain readable on low-end Android hardware.

The final game must not depend on a freely rotating 3D camera to understand navigation, actors, interactables, or combat.

## 3. Exploration / narrative view

Normal world, room, and current-location presentation uses a **closer three-quarter view**.

It should make it possible to read simultaneously:
- the place;
- Jack's position when shown;
- present NPCs;
- meaningful props/interactables;
- entrances/exits;
- visible state changes;
- narrative and interaction UI without the UI consuming the entire screen.

The view should feel spatial without requiring full 3D rendering.

## 4. Tactical-combat view

Entering tactical combat keeps the same visual language but changes framing.

Combat uses:
- a **higher three-quarter orthographic view**;
- more visible floor/tactical space;
- explicit tactical cells;
- readable cover edges, blockers, hazards, interactables, and unit positions;
- bounded pan and zoom;
- no free camera rotation as a core requirement.

The transition should feel like the same place becoming tactically legible, not like switching into a different game.

## 5. Map view

World/region/settlement/district maps may move toward a **top-down or near-top-down** representation when that improves spatial comprehension.

Map presentation is distinct from tactical coordinates and from room/exploration composition.

## 6. Tactical grid decision

The baseline tactical space uses a **square grid**.

Reasons:
- deterministic cell IDs and pathing;
- straightforward directional cover;
- readable phone interaction;
- simpler authored terrain/prop composition;
- easier LOS/path tests;
- lower rendering and simulation complexity than continuous free movement;
- easier save/replay/debugging.

Exact tile dimensions, maximum encounter footprint, diagonal movement policy, and movement-cost formula remain tuning/documentation decisions.

## 7. Turn and action direction

Combat is **turn-based**.

Each activation uses an **action-budget model** rather than a rigid universal "exactly two actions" rule.

Potential budget consumers include:
- move;
- sprint;
- attack;
- ability;
- item;
- interact;
- defend/brace;
- prepare a reaction;
- assist;
- disengage;
- retreat.

The exact initiative ordering and exact numeric action costs remain tunable until encounter prototypes and phone readability tests exist.

## 8. Position, cover, and information

Position is mechanically meaningful.

Combat must distinguish:
- physical position;
- geometric line of sight;
- detection/awareness;
- concealment;
- known last position;
- player/NPC knowledge.

A unit must not become fully known merely because geometry could theoretically connect two cells.

Cover is directional. Flanking or changing angle can change the protection provided by the same object.

The UI must use player-safe projected information and must not reveal hidden enemies, hidden intent, or unknown weaknesses.

## 9. Knowledge as combat gameplay

Existing knowledge systems should matter tactically.

Enemy information may become more precise through:
- prior encounters;
- investigation;
- study;
- NPC instruction;
- equipment/sensors if canon;
- successful observation;
- faction/world knowledge.

The tactical UI should expose only what the player character is entitled to know.

## 10. Party-control direction

Jack is the player's directly authoritative tactical character.

Recurring companions use a **hybrid order + constrained-autonomy model** as the target direction.

The player may issue tactical intent/orders, while companion execution may be influenced by authored state such as:
- personality;
- discipline;
- loyalty/trust;
- fear;
- injury;
- goals;
- faction doctrine;
- relationship state.

This must never become arbitrary runtime improvisation. Companion behavior remains deterministic and inspectable from authoritative state and rules.

Exact command vocabulary and degree of override remain future detailed design work.

## 11. Enemy and beast behavior

Enemies should not reduce to "move toward nearest target."

Tactical decision inputs may include:
- objective;
- faction doctrine;
- memory of prior encounters;
- known player tactics;
- injury;
- fear/morale if adopted;
- territorial rules;
- pack behavior;
- protection priorities;
- retreat/surrender thresholds.

Beasts may use different movement, senses, territorial behavior, body size, and weak-point logic from humanoid actors.

## 12. Encounter objectives

Elimination is only one possible objective.

Supported design space includes:
- escape;
- survive;
- rescue;
- protect;
- retrieve;
- capture;
- disable;
- hold;
- investigate;
- reach an exit;
- delay;
- force withdrawal;
- nonlethal resolution.

The objective must be authoritative encounter/quest state.

## 13. Injury and body-part direction

Localized injury is retained as a meaningful system, but universal micro-targeting of many body parts is **not** the baseline for every ordinary combatant.

Baseline:
- localized injuries may affect movement, actions, accuracy, stamina, equipment use, or recovery;
- body zones should be limited enough to remain readable on phone;
- large beasts, bosses, or anatomically important special encounters may use deeper weak-point / body-part targeting;
- persistent injuries must write back to world/NPC/player state.

Exact zones and formulas remain future combat-detail work.

## 14. Persistent aftermath

Combat is not a detached minigame.

Aftermath may persist:
- health/injury;
- resources;
- consumed items/ammunition if adopted;
- equipment condition if adopted;
- death/capture/escape;
- NPC memory;
- relationships;
- reputation;
- rival/adversary state;
- quest progress;
- loot;
- local/world control;
- elapsed time;
- discovered knowledge.

## 15. Mobile interaction contract

Combat interaction should be primarily tap-driven:
- tap unit;
- tap legal cell;
- tap action;
- tap target;
- explicit confirmation only where needed;
- drag/pan tactical view;
- pinch/controlled zoom if supported.

A virtual movement joystick is **not** the baseline tactical-combat control.

Touch targets, text, overlays, and tactical cells must remain readable on phone.

## 16. Low-end Android target

The design must be capable of shipping on **Galaxy A02-class hardware** as a low-end target.

This is a product requirement, not a claim of current verified compatibility.

Design implications:
- prefer 2D/2.5D compositing over a required fully dynamic 3D world;
- bound simultaneously active tactical units and effects;
- use deterministic lightweight rules;
- avoid mandatory real-time physics for tactical resolution;
- constrain animation/effect complexity;
- support low-memory asset handling;
- preserve reduced-motion and accessibility paths;
- profile actual builds before claiming acceptance.

Historical Galaxy A03 emulator/device references remain evidence about their recorded targets only and do not prove Galaxy A02 compatibility.

## 17. Visual continuity

The same identity/art system should flow through:
- exploration room actor;
- tactical unit;
- portrait/focus panel;
- equipment layers;
- condition/injury overlays.

Combat should not require redesigning a character into a visually unrelated unit.

## 18. Performance-budget documentation required before implementation scale-up

Before large combat implementation, document:
- target encounter unit count;
- maximum visible tactical cells;
- sprite/effect budget;
- animation frame/cadence budget;
- memory/cache policy;
- target frame-time / responsiveness policy;
- low-end Android profiling procedure;
- fallback/reduced-effects behavior.

## 19. Decisions now locked

Locked design direction:
1. primary in-world camera = orthographic three-quarter 2D/2.5D;
2. exploration = closer three-quarter framing;
3. combat = higher three-quarter tactical framing;
4. map = top-down / near-top-down where appropriate;
5. no free-rotation 3D camera as core requirement;
6. square tactical grid;
7. turn-based combat;
8. action-budget activations;
9. directional cover;
10. LOS, detection, and knowledge are distinct;
11. player-safe information boundary applies in combat;
12. Jack direct control + companion order/constrained-autonomy target;
13. multiple encounter objective types;
14. localized persistent injuries, with deeper body-part systems reserved for suitable encounters;
15. tap-first mobile tactical controls;
16. Galaxy A02-class hardware is a target requirement.

## 20. Decisions still open

Not yet locked:
- exact projection angle/pixel ratio;
- exact tactical tile size;
- diagonal movement rule;
- exact initiative ordering;
- exact action-budget numbers;
- exact cover names/modifiers;
- exact hit/impact prediction presentation;
- exact damage/armor formulas;
- exact companion command vocabulary;
- morale adoption/formula;
- ammunition policy;
- destructibility scope;
- exact body-zone schema;
- encounter generation policy;
- maximum encounter size;
- orientation support;
- exact camera pan/zoom limits.

These must be resolved through later documentation and bounded prototypes rather than silently hardcoded.

## 21. Implementation sequencing

When implementation begins or continues:
1. tactical coordinate/grid model;
2. camera/presentation prototype using placeholder-safe existing art only unless asset production is separately required;
3. pathing/occupancy;
4. LOS/detection/knowledge projection;
5. directional cover;
6. activation/action-budget model;
7. attack/ability legality and resolution;
8. injury/condition integration;
9. companion order/autonomy rules;
10. enemy/beast AI;
11. encounter objectives;
12. persistent aftermath;
13. player-safe combat projection;
14. Android tactical surface;
15. low-end performance profiling;
16. bounded authored test encounter;
17. expand only after evidence.

## 22. Authority and change control

This standard is an approved design direction.

A future implementation may tune numbers and unresolved details, but it should not silently replace the camera model, grid model, tactical-information boundary, or persistent-combat philosophy.

Any major reversal should be documented as an explicit design migration.
