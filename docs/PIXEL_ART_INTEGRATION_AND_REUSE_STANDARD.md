# THE GAME — Pixel Art Integration, Character Panels & Reuse Standard

Status: **ACTIVE VISUAL CONTRACT**
Authority roots:
- `docs/MASTER_DOCUMENTATION_PROGRAM.md`
- `docs/assets/PIXEL_ASSET_MASTER_PLAN.md`
- `docs/assets/ASSET_PRODUCTION_ROADMAP_001-500.md`
- `docs/assets/REFERENCE_REGISTRY.md`

## 1. Goal

Pixel art is not decoration added after the game is finished. It is the visual presentation layer for authoritative game state.

The system must support:
- world/map art;
- location/room art;
- player character;
- NPCs;
- paper-doll equipment;
- portraits;
- room character panels;
- item icons;
- props;
- environment tiles;
- state overlays;
- ability/status FX;
- HUD/UI icons;
- animation;
- future combat presentation.

Art must be reusable without making locations look copied, incoherent, or disconnected from the rest of the game.

## 2. Production lifecycle

Every production asset uses the lifecycle:

`PLANNED -> BRIEF_LOCKED -> REFERENCE_GENERATED -> REFERENCE_SELECTED -> BLUEPRINTED -> PIXEL_MASTER_BUILT -> INTEGRATED -> VERIFIED -> CANON_APPROVED`

Important:
- a generated reference is not a shipped asset;
- a text/code pixel map may be a valid production master if it is deliberately authored and visually approved;
- a procedural rectangle/box used to reserve geometry is not final art;
- exact runtime status must be verified before advancing an asset stage.

## 3. Current production baseline

Existing documentation defines 500 v1 planned asset units.

The repository task register records prior integrated work including:
- source-native player sprite work;
- paper-doll starting equipment mappings;
- Maintenance Seal and Dead Relay visual states;
- scene masters for the nine current Gate Twelve locations;
- several story/state overlays;
- UI/map assets in the Batch 001 range.

These are a status starting point, not a blanket statement that all 500 assets are complete or canon-approved.

Before changing any one asset, inspect:
1. stable asset ID;
2. current source master;
3. manifest/state binding;
4. reference provenance;
5. runtime consumer;
6. exact branch/HEAD;
7. latest visual QA.

## 4. Core native sizes

Current production standards:
- micro icon: 16x16;
- standard UI icon: 24x24;
- item/equipment icon: 32x32;
- gameplay character/paper-doll: 32x48;
- portrait: 64x64;
- FX cell: 64x64;
- scene master: 128x64;
- district map master: 256x144 minimum/current Gate Twelve baseline.

Large concept/reference material is never shipped directly merely because it looks better.

## 5. Runtime visual stack

The canonical visual stack is layered.

### Layer 0 — world/map base
Permanent geography, terrain, streets, water, district footprint, room shell.

### Layer 1 — permanent architecture
Walls, floors, roofs, depot structures, civic buildings, doors whose existence is permanent.

### Layer 2 — reusable structural modules
Road tiles, curb, stairs, rails, windows, columns, pipe runs, shelf modules, wall modules, shop bays.

### Layer 3 — permanent props
Benches, shelves, terminals, fixed lamps, notice boards, infrastructure objects.

### Layer 4 — temporary/state props
Dead relay state, movable crates, temporary barricades, dropped items, damage variants.

### Layer 5 — characters
Player and present NPC gameplay sprites.

### Layer 6 — equipment/paper-doll
Character-bound wearable/held layers driven by authoritative equipment state.

### Layer 7 — environmental state overlays
Blackout, emergency lighting, weather, danger haze, Trace distortion, damage, contamination, event dressing.

### Layer 8 — ability/status FX
Trace Echo, conditions, combat/status effects.

### Layer 9 — interaction/navigation markers
Selected, reachable, current, quest/event markers. State-driven only.

### Layer 10 — character/room panels
Portraits, names, dialogue/action affordances, contextual interaction panel.

### Layer 11 — narrative/UI text
Readable UI text. Do not bake changing dialogue, quest state, or player-specific text into environment art.

## 6. Character panels by room presence

Character panels must depend on who is actually present in the current location/room.

The UI must not hardcode:
- "Tamsin panel always visible";
- fixed portrait lists by screen;
- NPCs inferred from raw hidden flags.

Required data flow:

`authoritative world/NPC state -> player-safe room/scene occupant projection -> Android presentation -> character panel`

### Panel priority when multiple characters are present

1. explicitly selected character;
2. current speaker;
3. current interaction target;
4. party member relevant to current action;
5. other visible/present room occupants;
6. no-character state.

### Panel content

Allowed if projected safely:
- portrait;
- display name;
- short role/title;
- visible condition;
- relationship summary if designed to be player-facing;
- current dialogue/action buttons;
- party indicator;
- equipment silhouette if relevant.

Not allowed unless player-safe:
- hidden loyalty;
- secret goals;
- undiscovered faction;
- raw suspicion formulas;
- hidden quest triggers;
- future betrayal state;
- private knowledge.

### Panel visual contract

- portrait master: 64x64 target;
- use character-specific approved references;
- panel frame may reuse common UI frame assets;
- character identity art cannot be recolored arbitrarily to fake a different NPC;
- equipment shown on portrait/sprite must match authoritative equipment when the system supports it;
- room lighting may tint/overlay the portrait only through a documented effect that preserves identity/readability.

## 7. Room composition rules

A room/location scene should be reconstructable from reusable modules.

Each room brief must declare:
- stable location/room ID;
- map parent;
- scene master;
- base material family;
- permanent architecture;
- reusable module list;
- fixed props;
- state props;
- character spawn/presence anchors;
- interaction anchors;
- lighting source;
- overlay slots;
- UI-safe crop area;
- alternate states;
- animation hooks.

Do not flatten all of these into one image if state changes require only a subset to change.

## 8. Asset reuse without looking out of place

Reuse is preferred when identity can be preserved.

### Reuse categories

#### Exact reuse
Same asset, same function:
- common curb;
- standard service door;
- standard municipal lamp;
- generic crate.

#### Variant reuse
Same master with approved variant:
- clean/worn;
- open/closed;
- powered/unpowered;
- damaged/intact.

#### Modular composition reuse
Same modules arranged differently:
- wall + doorway + pipes;
- shop bay shell + different shutters/props;
- archive shelf modules.

#### Palette-family reuse
Shared material ramps without copying full shape:
- civic stone;
- depot steel;
- lower-service concrete.

#### Overlay reuse
Same effect with location-specific masking:
- blackout shadow;
- emergency light;
- rain;
- Trace interference.

### Reuse rejection rules

Do not reuse when:
- silhouette makes two important landmarks indistinguishable;
- perspective conflicts;
- pixel density conflicts;
- light direction conflicts;
- material scale conflicts;
- asset reveals the wrong state;
- character identity would be changed;
- copied composition makes locations feel duplicated;
- the original asset belongs to a different project or incompatible art direction.

## 9. Text-art and text overlays

Text belongs to UI unless it is permanent environmental signage.

### Allowed environmental text-art
- symbols;
- short fixed labels;
- stable numbers/sector marks;
- permanent facility IDs;
- signage whose wording is canon and does not change by player state.

### UI text overlay
Use for:
- dialogue;
- narration;
- action labels;
- changing quest state;
- inventory counts;
- NPC relationship/context;
- travel time;
- warnings;
- tooltips.

UI text overlays must sit above scene/map art and remain readable without forcing the art to reserve excessive blank rectangles.

## 10. Map pixel art

The map uses a permanent base plus state layers.

Permanent:
- terrain;
- streets;
- building footprints;
- public structures;
- stairs/tunnels;
- permanent landmarks.

State-driven:
- current node;
- discovered node;
- reachable node;
- selected node;
- event/quest markers;
- danger;
- blackout;
- temporary obstruction;
- player marker.

The background map may suggest physical paths, but only authoritative graph state decides actual travel.

## 11. Environment asset families to create

Global reusable families:
- terrain/ground tiles;
- road/street tiles;
- curb/edge modules;
- public paving;
- building shells;
- roofs;
- doors;
- windows;
- stairs;
- rails;
- fences;
- pipes;
- vents;
- drains;
- lamps;
- signs;
- vegetation;
- water;
- debris;
- furniture;
- storage;
- workshop props;
- archive props;
- depot props;
- tunnel props;
- hazard props;
- state overlays;
- weather overlays;
- lighting overlays.

Each future biome/kingdom may extend these families but should not reset the entire pipeline.

## 12. Character asset families to create

Per recurring character:
- 32x48 gameplay base;
- front/back/profile/three-quarter reference;
- idle;
- walk when used;
- run when used;
- interact;
- hurt/status if used;
- ability/combat poses if used;
- 64x64 portrait base;
- emotional portrait variants;
- room panel portrait;
- paper-doll compatibility metadata;
- held-item anchors;
- room presence anchor metadata.

Player additionally requires:
- bodyframe master;
- equipment layers by slot;
- customization only if gameplay supports it;
- animation compatible with equipment layers.

## 13. Item/equipment families

Each supported item may require:
- 32x32 icon;
- world prop;
- paper-doll layer;
- held sprite;
- active/damaged variant;
- close-up/inspection art;
- tooltip icon;
- state overlay.

Only create the variants the gameplay actually uses.

## 14. Animation strategy

Animation is phased.

### Phase A
Static environment + state overlays + static character sprites.

### Phase B
Essential character feedback:
- idle;
- simple interaction;
- critical story action.

### Phase C
Movement if/when world traversal presentation requires it.

### Phase D
Tactical combat animation after combat rules are locked.

### Phase E
Ambient environment:
- light flicker;
- water;
- smoke/steam;
- flags/signage;
- machinery;
- weather;
- creature idle loops.

No animation should force gameplay rules to exist.

## 15. Visual consistency checks

Every integrated scene/map must pass:
- perspective consistency;
- pixel-density consistency;
- palette/material consistency;
- light-direction consistency;
- silhouette readability;
- phone-scale readability;
- no anti-aliased halos;
- no accidental cyberpunk/neon drift;
- no unrelated-project asset contamination;
- correct state ownership;
- no hidden-information leak;
- correct character/equipment identity.

## 16. Status reporting

Every asset status report should identify:
- asset ID;
- family;
- source/reference;
- current lifecycle stage;
- branch/commit;
- runtime consumer;
- verified on emulator? yes/no;
- verified on physical handset? yes/no;
- known mismatch;
- next action.

Avoid vague labels like "done" for an asset that only has a reference image.

## 17. Gate Twelve application

Gate Twelve is the first region to apply this standard end-to-end.

Its assets should be built from:
- surface civic family;
- depot/service family;
- lower maintenance family;
- permanent map modules;
- location scene masters;
- state overlays;
- props;
- player/NPC sprites;
- room character panels.

The existing Gate Twelve master plan remains the spatial authority until a later documented migration.
