# THE GAME — Pixel Art Runtime Composition Standard

Status: **ACTIVE VISUAL INTEGRATION CONTRACT**  
Parent: `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`  
Companions:
- `PIXEL_ASSET_MASTER_PLAN.md`
- `CHARACTER_PIXEL_BLUEPRINTS.md`
- `REFERENCE_TO_BLUEPRINT_PIPELINE.md`
- `GATE_TWELVE_MAP_PIXEL_ASSET_BLUEPRINT.md`
- `GATE_TWELVE_MAP_ANIMATION_BLUEPRINT.md`

---

# 1. Purpose

This document defines how pixel-art assets are actually combined in the game.

The problem being solved is not merely “make more pixel art.”

The required result is a coherent system where:
- the map is built from reusable authored art;
- rooms use persistent environment masters;
- characters appear only when the game says they are present;
- equipment changes appearance without redrawing the entire player;
- story-state changes use overlays instead of duplicating whole scenes;
- props can be reused in compatible locations;
- panels can focus on characters who are currently present;
- art from different production waves does not look pasted together;
- no visual layer becomes a second hidden gameplay engine.

---

# 2. Composition stack

A scene should be understood as a composited stack.

Recommended order:

1. base backdrop / room shell;
2. floor / permanent architecture;
3. permanent environment modules;
4. permanent props;
5. state-dependent environment overlays;
6. interaction props;
7. rear character accessories;
8. room actors / NPC sprites;
9. player sprite when the presentation calls for it;
10. held items/equipment;
11. foreground props/occluders;
12. ability/status FX;
13. selection/focus treatment;
14. dialogue/actor panel;
15. narrative/action UI.

This order may vary by scene, but every exception must be explicit.

---

# 3. Asset ownership

## 3.1 Base environment owns
- permanent walls;
- floor;
- fixed doors when their physical state never changes;
- structural supports;
- permanent furniture;
- broad lighting basis.

## 3.2 State overlay owns
- blackout shadow;
- emergency lighting;
- signal response;
- temporary damage;
- quest-safe visible changes;
- powered/unpowered visual state when projected.

## 3.3 Prop owns
- relay;
- diagnostic reader;
- container;
- bench;
- sign;
- terminal;
- door component if separately stateful;
- movable environmental object.

## 3.4 Character actor owns
- body;
- hair;
- identity;
- pose;
- visible clothing/equipment;
- player-safe temporary emotion/condition.

## 3.5 UI owns
- labels;
- dialogue text;
- action buttons;
- interaction affordance;
- status bars;
- actor focus panel;
- map selection state.

UI does not own whether an NPC exists in the room.

---

# 4. Character-in-room contract

## 4.1 Current transitional state

A current implementation line contains `PixelStoryActorCatalog`, with actor placements selected from projected `locationId` and `sceneId`.

Current known actor examples include:
- Tamsin;
- injured maintenance courier.

This is acceptable as a bounded transitional system.

## 4.2 Target state

The target is a player-safe actor projection, conceptually:

`GameSnapshot.actors[]`

Each visible actor record should eventually support:
- stable NPC/actor ID;
- display name;
- location;
- visible pose;
- visible expression;
- visible outfit/equipment identity;
- optional portrait asset ID;
- optional room-sprite asset ID;
- interaction availability;
- player-safe relationship summary if intended;
- panel priority/focus eligibility.

Compose should render the actor list; it should not reconstruct presence by reading raw quest flags.

## 4.3 Panel behavior

When one important actor is present:
- room art remains dominant;
- actor sprite appears in scene;
- optional portrait/name panel can appear near narrative/dialogue UI.

When multiple actors are present:
- do not open every full panel at once;
- use selected/focused actor;
- show compact actor chips/portraits if needed;
- preserve room readability.

When no actor is present:
- no fake portrait panel.

Panel content may show only player-safe state.

---

# 5. Player character contract

The player uses the shared 32x48 gameplay paper-doll system.

Current important rules:
- fixed ground pivot;
- stable attachment anchors;
- equipment layers;
- z-order;
- nearest-neighbor rendering;
- no invented overlay for unmapped equipment.

The later approved character reference for Jack is a visual authority input and must be retained through provenance documentation.

Any older generic-placeholder wording must be reconciled before a final player master is marked CANON_APPROVED.

Do not silently use a generic technical block character when an approved visual reference exists.

---

# 6. Portrait / gameplay / panel identity consistency

A recurring character must share identity across:

- gameplay room sprite;
- portrait;
- character panel;
- dialogue focus;
- equipment/appearance state;
- map/event icon when applicable.

Shared identity fields:
- skin family;
- hair silhouette;
- major facial/identity marks;
- body proportion class;
- clothing identity;
- equipment markers;
- asymmetry;
- role markers.

Different views may simplify detail, but they must not redesign the person.

---

# 7. Reuse compatibility contract

An asset may be reused across locations only if it passes all relevant compatibility checks.

## 7.1 Pixel density
Source grids must be compatible or converted deliberately.

Never scale one asset with smooth interpolation to “make it fit.”

## 7.2 Perspective
A top/three-quarter prop cannot be pasted into a side-on room without a matching view.

## 7.3 Light direction
Major light direction must be compatible.

Local emissive lights may vary, but the object should not imply an impossible global light.

## 7.4 Value range
Dark-area assets and bright civic assets may share materials but need location-appropriate ramps.

## 7.5 Palette family
Exact palette reuse is not mandatory.

Material ramps must harmonize with the destination scene.

## 7.6 Material language
Municipal steel should look like the same industrial family across:
- Platform Nine;
- Relay Workbench;
- Gate Twelve;
- Service Tunnel;
- Trace Chamber.

## 7.7 Scale
Doors, benches, props, characters and environmental modules must preserve relative scale.

## 7.8 Anchor
Reusable objects need stable origin/pivot metadata.

## 7.9 Occlusion
Foreground/background behavior must be known.

## 7.10 State semantics
A powered panel sprite cannot be reused as an idle unpowered panel unless its state is correct.

---

# 8. Text-art / procedural art / authored raster relationship

Three visual types may coexist during migration.

## A. Source-native authored raster
Preferred shipping form when available.

## B. Source-native PixelSprite/text-map definition
Acceptable production form if intentionally authored and visually approved.

It is not inferior merely because its pixel rows are represented in code.

## C. Procedural geometric fallback
Migration-only fallback.

It may:
- preserve layout;
- preserve hit targets;
- keep unsupported locations visible.

It should not dominate final art when authored assets exist.

Replacement priority:
1. generic block character;
2. generic scene geometry;
3. flat map blocks;
4. technical placeholder icons;
5. only then lower-value decorative placeholders.

---

# 9. Overlay strategy

Use overlays when architecture is unchanged.

Examples:
- Gate Twelve Echo-active signal;
- Service Tunnel aftershock;
- Relay Workbench relay-state inspection context;
- Platform Nine blackout;
- Depot Plaza blackout;
- status/ability FX.

Do not make a whole new flattened room image for:
- one changed lamp;
- one open item;
- one NPC entering;
- one temporary effect.

Use a full alternate base only when the physical environment materially changes.

---

# 10. Animation strategy

Animation classes:

- STATIC;
- AMBIENT LOOP;
- STATE-DRIVEN;
- CHARACTER ACTION;
- TRANSITION.

Rules:
- integer-safe motion;
- restrained loops;
- reduced-motion behavior;
- no hidden-state implication;
- actor animation does not change actor identity;
- equipment follows rig anchors;
- ambient loops do not decide hazards.

Current planned/implementation evidence includes a Service Tunnel ambient animation line, but open branch/PR work remains distinct from canonical integration.

---

# 11. Current known production stages

This ledger is evidence-oriented, not a claim that open PR work is merged.

## Planning baseline
- 500 unique planned asset units: COMPLETE as planning.
- Batch 001–005 documents: present.
- asset lifecycle/manifests: present.

## Current scene masters
Current manifests document integrated/provisional scene masters for the nine named Gate Twelve locations and state overlays.

Known examples:
- Platform Nine blackout;
- Relay Workbench default;
- Gate Twelve sealed;
- Service Tunnel default;
- Quiet Stair default;
- Trace Chamber idle;
- Depot Plaza;
- Municipal Archive;
- Workshop Row.

Many automated state-binding gates are green on their recorded exact heads, while native-scale art review and physical handset review remain separate.

## State overlays
Known examples:
- Relay Workbench relay-open/damaged/signal-lost context;
- Gate Twelve Echo active;
- Service Tunnel aftershock;
- Trace Chamber training.

## Player/equipment
A 32x48 paper-doll contract exists.

Current loadout visual work includes:
- Depot Jacket;
- Work Gloves;
- Signal Ring;
- Courier Neck Tag.

The player silhouette/reference line has later branch work and must not be treated as final merely because it exists.

## Story actors
A later branch includes:
- Tamsin room actor;
- wounded courier room actor;
- scene/location placement logic.

## UI reference adaptations
Later open branch work includes:
- phone Bag layout;
- Skills hierarchy/layout.

## Map
Later open branch work includes authored district art under projected nodes and Gate Twelve map-asset planning.

---

# 12. Required assets by Gate Twelve area

This list is a production checklist, not a claim they are all missing.

## Depot Plaza
- plaza base;
- depot facade;
- paving modules;
- civic lamps;
- notice board;
- tree/planter modules;
- blackout overlay;
- emergency-light loop;
- crowd/NPC actor slots where authored;
- route/entrance visual anchors.

## Workshop Row
- linked workshop exterior modules;
- shutters;
- workbench;
- tool cart;
- scrap bins;
- repair props;
- worker actor families;
- practical signage;
- optional state variants.

## Municipal Archive
- exterior;
- courtyard;
- shelving;
- public terminal;
- backup lamps;
- clerk/visitor actors if authored;
- records interaction close-up;
- conditional research indicator only when projected.

## Platform Nine
- depot shell;
- platform;
- track modules;
- service roof;
- depot door;
- evacuation signage;
- blackout overlay;
- emergency strips;
- evacuee actors;
- Tamsin actor;
- courier actor;
- future post-evacuation state.

## Relay Workbench
- room shell;
- workbench;
- tools;
- relay props by state;
- diagnostic lighting;
- Tamsin technical pose;
- optional diagnostic reader;
- interaction close-up.

## Gate Twelve
- reinforced frame;
- twin gate panels;
- service hardware;
- idle indicators;
- Echo-active overlay;
- future door-state variants only when authoritative;
- investigation actor slots.

## Quiet Stair
- stair/shaft base;
- rails;
- landings;
- evacuation signs;
- guidance lights;
- ambient low-frequency motion only if justified;
- future egress connection art.

## Service Tunnel
- corridor shell;
- ribs/supports;
- pipe/cable modules;
- vents;
- drains;
- indicator lamps;
- access panels;
- ambient steam/drip/fan loops;
- aftershock overlay;
- deep-route visual stub;
- Tamsin actor where present.

## Trace Chamber
- chamber shell;
- test apparatus;
- floor/service marks;
- training markers;
- Trace FX;
- diagnostic/measurement props;
- actor training poses;
- controlled recovery presentation.

---

# 13. World-scale asset families still required

Before mass production, define data ownership for:

- city architecture;
- village architecture;
- kingdom/faction architecture;
- wilderness biomes;
- roads;
- transit;
- water;
- caves;
- beast habitats;
- resources;
- plants;
- beasts;
- civilian archetypes;
- guards;
- workers;
- officials;
- merchants if economy is authored;
- class/rank clothing;
- weapons/tools if authored;
- tactical terrain;
- tactical cover;
- loot;
- accessories;
- class/skill icons;
- faction icons.

---

# 14. Visual acceptance tests

Every major visual integration should answer:

- Is the correct stable ID used?
- Is the source stage known?
- Is the asset source-native?
- Is nearest-neighbor rendering preserved?
- Does it fit the native grid?
- Does it match perspective?
- Does it match scale?
- Does it match material family?
- Does it match scene lighting?
- Does it preserve actor identity?
- Does equipment align?
- Does it reveal hidden state?
- Does the UI still fit 320dp?
- Does it remain readable with larger text?
- Does reduced motion work if animated?
- Is exact-head emulator evidence captured?
- Is physical Galaxy A03 evidence separately identified?

---

# 15. What may be replaced

Visual replacements are explicitly allowed for:
- geometric placeholder rooms;
- generic block avatar;
- poor-quality generated-look assets;
- mismatched perspective assets;
- weak map background;
- non-cohesive UI decoration.

Replacement must:
- preserve authoritative bindings;
- preserve IDs or migrate them;
- preserve hit targets unless intentionally redesigned;
- keep old asset available until new asset passes integration where practical.

---

# 16. Next visual-document tasks

1. finish Gate Twelve geometry contract;
2. reconcile player identity reference with character blueprint;
3. create actor-projection data contract;
4. build provenance matrix mapping every currently visible asset to:
   - ID;
   - source;
   - stage;
   - runtime consumer;
   - replacement need;
5. create Gate Twelve per-area asset production packets;
6. create room-panel UI contract;
7. create world-scale tile/material families only after Gate Twelve proves the pipeline.
