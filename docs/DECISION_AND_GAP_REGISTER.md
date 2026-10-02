# THE GAME — Decision & Gap Register

Status: **ACTIVE / MUST BE UPDATED WITH MAJOR DESIGN CHANGES**

## Decision states

- `LOCKED` — accepted and used as a downstream dependency.
- `ACTIVE` — current direction; may still receive detail.
- `PROPOSED` — documented candidate, not implementation authority.
- `UNKNOWN` — intentionally undecided.
- `BLOCKED` — cannot be decided without another dependency.
- `SUPERSEDED` — retained for history but no longer current.

## Project decisions

| Domain | Decision | State |
| --- | --- | --- |
| Active repository | `jbob-coder/Text-rpg-game` | LOCKED |
| Product | narrative/text RPG with Android pixel-art presentation | LOCKED |
| Main branch | placeholder, not implementation authority | LOCKED |
| Engine/UI ownership | gameplay state -> player-safe projection -> Android UI | LOCKED |
| Final visuals | real pixel assets, not final code geometry/boxes | LOCKED |
| Rendering | nearest-neighbor/source-native pixel presentation | LOCKED |
| Pixel references | reference-only until lifecycle promotion | LOCKED |
| Player asset rig | 32x48 production character grid | ACTIVE |
| Portrait target | 64x64 | ACTIVE |
| Item icon target | 32x32 | ACTIVE |
| Scene target | 128x64 | ACTIVE |
| Map master minimum/current Gate Twelve | 256x144 | ACTIVE |
| Bulk asset roadmap | 500 planned v1 units | ACTIVE |
| Gate Twelve macrozones | Surface Civic / Depot-Gate Core / Lower Maintenance | LOCKED |
| Gate Twelve connector | Depot Plaza <-> Platform Nine required in target circulation, not yet gameplay-authored | ACTIVE |
| Documentation-first final rebuild | required before destructive app reconstruction | LOCKED |

## Pixel-art decisions still required

- canonical player body/identity reference details not yet locked;
- all recurring NPC turnarounds;
- room-specific character panel layouts;
- multiple-character room priority/order;
- full animation direction/frame budget by screen;
- full environment tile atlas families;
- final material palettes by world region;
- map zoom/LOD behavior;
- large-world atlas segmentation;
- final overlay budget and blending rules;
- final pixel-art accessibility rules.

## World decisions still required

- planet/world shape and global map extent;
- coordinate system;
- kingdoms/states;
- settlements;
- political borders;
- languages/cultures if authored;
- population model;
- species/beast taxonomy;
- global resource distribution;
- ecology;
- climate/biomes;
- travel network;
- danger zones;
- world-level bands;
- settlement hierarchy;
- faction hierarchy.

## Mechanics decisions still required

- final level/progression system;
- class/rank structure;
- skill-tree structure;
- full passive system;
- combat grid and action economy;
- hit/damage/armor formulas;
- cover/LOS/elevation;
- tactical AI;
- persistent rival/adversary memory model;
- enemy/beast rank balance;
- economy;
- loot;
- item quality;
- crafting/repair, if any;
- crime/law;
- reputation;
- social discrimination mechanics, if included;
- NPC schedules and simulation depth.

## App decisions still required

- final navigation architecture;
- whether Story and Map become one integrated world screen or remain separate surfaces;
- room/character panel placement;
- map pan/zoom;
- scene-to-map transition;
- asset streaming;
- low-memory strategy;
- save migration;
- final developer panel;
- release packaging;
- physical-device performance target.

## Rebuild candidates

Candidates that may be intentionally broken/replaced after target contracts exist:
- geometric map presentation;
- procedural/code-drawn scene placeholders;
- placeholder player avatar art;
- old panel layouts;
- redundant state/view glue;
- duplicated UI calculations;
- old navigation structure if it blocks world-centric play;
- any visual implementation that cannot consume approved production assets cleanly.

No candidate is deleted merely because this register names it. Deletion requires an implementation/migration slice with evidence.
