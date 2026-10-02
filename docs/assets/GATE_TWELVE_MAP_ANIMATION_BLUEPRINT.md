# Gate Twelve District — Pixel Animation Blueprint

Status: production-planning companion to `GATE_TWELVE_MAP_PIXEL_ASSET_BLUEPRINT.md`.

## 1. Purpose

This document defines how the already-authored Gate Twelve district assets may animate without changing map geometry or moving gameplay authority into presentation code.

Animation is divided into three classes:

- **STATIC** — architecture/material that should not animate.
- **AMBIENT LOOP** — visual life that can repeat continuously without implying gameplay state.
- **STATE-DRIVEN** — animation that may only run when player-safe authoritative state permits it.

The rule is simple:

`geometry stays fixed -> animated layers move inside that geometry`

## 2. Global animation rules

1. No smooth interpolation that destroys pixel alignment.
2. Prefer integer-pixel movement.
3. Keep loops short, restrained and readable at phone scale.
4. Environmental animation must not make every surface move.
5. Static architecture remains the visual anchor.
6. Ambient loops may not imply danger, reachability, quest availability or interaction.
7. State-driven loops require an existing player-safe state, scene or visual projection.
8. Do not animate hidden or inferred game information.
9. Reuse animation families instead of creating a unique timing system for every location.
10. Animation may be omitted at reduced-motion/accessibility settings.

## 3. Timing families

Recommended reusable timing classes:

| Class | Typical frames | Frame duration | Use |
| --- | ---: | ---: | --- |
| Indicator blink | 2-3 | 350-700 ms | small status lamps, terminal idle lights |
| Utility pulse | 3-4 | 180-300 ms | powered panels, controlled signal indicators |
| Mechanical idle | 4-6 | 180-260 ms | fan/vent cycle, small machinery |
| Light flicker | 3-5 | 90-220 ms, irregular sequence | damaged/emergency light only |
| Steam/drip | 4-6 | 180-300 ms | tunnel ambient detail |
| Sign/arrow pulse | 2-4 | 300-500 ms | evacuation/emergency state |
| Trace FX | 6-8 | 80-160 ms | Signal/Trace state-driven effects |
| Travel transition | 6-10 | 70-130 ms | successful map travel only |

Exact timing should remain centralized when implementation begins.

## 4. Region animation contracts

### 4.1 Workshop Row

**STATIC**
- shop shells;
- shutters/awning geometry unless a specific state supports movement;
- repair apron and paving.

**AMBIENT LOOP**
- one or two workshop indicator lamps: 2 frames, slow asynchronous blink;
- optional tiny exhaust/fan cycle on selected bay: 4 frames;
- hanging cable/tool sway only if silhouette remains stable and movement is <=1 px.

**STATE-DRIVEN**
- rumor/active-information emphasis: localized lamp/figure/prop emphasis;
- do not animate every storefront when one interaction becomes relevant.

### 4.2 Depot Plaza

**STATIC**
- paving;
- depot facade;
- permanent trees/planters;
- path geometry.

**AMBIENT LOOP**
- warm lamp shimmer: 2 frames;
- restrained tree-leaf cluster shift: 2-3 frames, <=1 px and very sparse.

**STATE-DRIVEN**
- blackout/emergency light sequence;
- evacuation signage pulse;
- temporary barrier/warning animation if visible state supports it.

### 4.3 Municipal Archive

**STATIC**
- archive facade;
- courtyard;
- shelving architecture.

**AMBIENT LOOP**
- backup-power indicator: 2 frames;
- terminal idle cursor/status pulse: 2-3 frames.

**STATE-DRIVEN**
- terminal active/read state;
- records-access highlight in close-up;
- do not animate readable text inside pixel art; actual record text remains UI.

### 4.4 Platform Nine

**STATIC**
- depot structure;
- platform;
- track geometry.

**AMBIENT LOOP**
- distant utility indicators;
- restrained tram/track signal blink if not tied to a gameplay lock.

**STATE-DRIVEN**
- blackout emergency strips;
- crowd movement in scene composition;
- injury/courier staging;
- evacuation pressure;
- powered/unpowered door states.

A crowd loop should use staggered 2-4 frame silhouettes, not synchronized bouncing figures.

### 4.5 Relay Workbench

**STATIC**
- bench;
- tool rail;
- room shell.

**AMBIENT LOOP**
- one diagnostic indicator: 2-3 frames.

**STATE-DRIVEN**
- relay pulse;
- opened relay internal indicator;
- signal-loss transition;
- diagnostic reader activity.

Relay animation must reflect the visible relay state and must not predict an unopened state.

### 4.6 Service Gate Twelve

**STATIC**
- reinforced frame;
- door panels;
- center seam.

**AMBIENT LOOP**
- tiny maintenance indicator: 2 frames, slow.

**STATE-DRIVEN**
- Echo/Trace response;
- door powered-state indicator;
- active signal sweep/ring.

The base gate should not pulse continuously. Strong movement is reserved for actual Echo/Trace activity.

### 4.7 Quiet Stair

**STATIC**
- stair geometry;
- shaft walls;
- rails.

**AMBIENT LOOP**
- guidance light blink: 2 frames, slow;
- rare overhead light variation.

**STATE-DRIVEN**
- evacuation guidance pulse if emergency state applies.

Keep this area quieter than Platform Nine and Service Tunnel.

### 4.8 Service Tunnel

**STATIC**
- wall/floor panels;
- support ribs;
- main pipes/cable trays;
- corridor depth.

**AMBIENT LOOP**
- small vent/fan cycle: 4 frames;
- tiny status-light sequence across panels: 3 frames;
- occasional pipe drip: 4-5 frames;
- sparse steam puff only where it does not cover landmarks.

**STATE-DRIVEN**
- aftershock distortion;
- Trace response;
- emergency lighting;
- damaged/flickering system states.

Tunnel ambience should feel alive but mechanically routine. Do not use constant aggressive flicker.

### 4.9 Trace Chamber

**STATIC**
- room shell;
- apparatus body;
- calibration frame.

**AMBIENT LOOP**
- idle apparatus status pulse: 3 frames;
- small instrument light cycle.

**STATE-DRIVEN**
- training rings;
- directional signal lines;
- Trace Echo waveform response;
- apparatus active/calibrating state.

The active loop should read as controlled measurement equipment, not magic neon spectacle.

## 5. Map-level animation

The 256x144 district map should remain mostly static.

Allowed map animation:

- player marker pulse;
- selection ring;
- current/reachable marker feedback;
- route-preview pulse;
- small state overlay on a selected location;
- successful travel transition.

Avoid:
- animated roads;
- constantly moving buildings;
- every lamp blinking simultaneously;
- large looping background motion that competes with map readability.

## 6. First three animation production tasks

### Task A — Service Tunnel ambient infrastructure loop

**Goal**
Make the Service Tunnel feel operational before any special story state is active.

**Layers**
- static corridor master;
- vent/fan 4-frame loop;
- panel indicator 3-frame loop;
- optional drip 5-frame loop.

**Constraints**
- no aftershock/Trace distortion;
- no route or hazard implication;
- <=1 px movement for small mechanical parts;
- loops should have different periods so they do not synchronize visibly.

**Acceptance**
At 320dp, the tunnel must still read first as a corridor, not as an FX screen.

### Task B — Gate Twelve Echo active loop

**Goal**
Animate `GATE_TWELVE_ECHO_ACTIVE_SCENE` as a state-driven overlay over the existing sealed gate geometry.

**Layers**
- static sealed gate;
- 6-8 frame Trace/Echo signal overlay;
- localized indicator response.

**Constraints**
- door geometry does not move unless authoritative state says the door itself changes;
- signal effect stays localized around seam/hardware;
- no hidden destination information.

**Acceptance**
The player can visually distinguish idle Gate Twelve from active Echo state without changing the architecture.

### Task C — Depot Plaza blackout loop

**Goal**
Animate `DISTRICT_PLAZA_BLACKOUT_SCENE` using reusable overlays rather than a new geometry pass.

**Layers**
- static open plaza;
- blackout shadow overlay;
- emergency strip 3-4 frame cycle;
- sparse lamp recovery/failure flicker.

**Constraints**
- paths and silhouettes stay readable;
- emergency lighting is asynchronous and restrained;
- no full-screen strobe.

**Acceptance**
The blackout state must be obvious while the map/plaza remains navigable and readable on mobile.

## 7. Animation asset brief template

Every animated asset should record:

1. stable animation ID;
2. parent static asset ID;
3. region/location ID;
4. animation class: AMBIENT LOOP or STATE-DRIVEN;
5. authoritative trigger, if any;
6. native grid;
7. frame count;
8. frame duration or timing sequence;
9. loop/ping-pong/one-shot behavior;
10. moving pixel bounding box;
11. maximum displacement;
12. palette additions, if any;
13. layers/occlusion order;
14. reduced-motion behavior;
15. 320dp QA screenshot or capture;
16. verification that the animation cannot imply hidden gameplay state.

## 8. Implementation order

1. build one reusable environment animation renderer/timing mechanism;
2. implement Service Tunnel ambient loop;
3. verify phone-scale readability and CPU cost;
4. implement Gate Twelve Echo as state-driven overlay;
5. verify state ownership;
6. implement Plaza blackout;
7. generalize timing classes only after those three cases prove the contract.

Do not build a large animation framework before the first three loops are proven.

## 9. Core rule

Animations decorate or communicate already-authoritative state.

They must never become a second simulation layer.
