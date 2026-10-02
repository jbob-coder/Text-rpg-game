# THE GAME — Pixel Art & Contextual Presentation Integration Contract

Status: **STAGE 1 / INITIAL NORMATIVE CONTRACT**
Parent: `docs/DOCUMENTATION_MASTER_PROGRAM.md`
Depends on:
- `docs/VISUAL_BIBLE.md`
- `docs/assets/PIXEL_ASSET_MASTER_PLAN.md`
- `docs/assets/CHARACTER_PIXEL_BLUEPRINTS.md`
- `docs/assets/REFERENCE_TO_BLUEPRINT_PIPELINE.md`
- `docs/assets/ASSET_MANIFEST_SCHEMA.md`

Purpose: define how world art, character art, equipment, effects, text/UI, contextual panels, and reusable overlays combine inside the actual game without becoming visually inconsistent or leaking hidden gameplay state.

---

## 1. Existing contracts retained

The following current production contracts are retained:

- gameplay character master: 32x48;
- item/equipment icon: 32x32;
- map/UI micro icon: 16x16;
- portrait/FX family: 64x64 unless a more specific child contract exists;
- location scene preview: 128x64;
- district/map master: 256x144 minimum;
- pixel-art scaling must remain crisp/integer-aligned;
- generated/reference boards are not production-ready by default;
- paper-doll equipment is state-driven;
- manifests record provenance, native size, anchors, state bindings, QA, and checksums.

These values are production defaults, not a requirement that every future asset use the same canvas.

---

## 2. Visual-reference decisions

### Adopt
- character turnarounds and body anchors;
- layered clothing/equipment concept;
- expression families for recurring characters;
- separate item icons and worn/held layers;
- reusable environment props;
- dedicated location previews;
- district map markers;
- separate ability/interaction FX;
- coherent dark-panel UI framing;
- consistent visual scale references.

### Adapt
- the reference palette becomes guidance, not a global immutable palette;
- settlement sectioning becomes modular loading/authoring logic, not a fixed number of areas;
- location previews may reuse the same architecture with state overlays;
- character panels adapt dynamically to party/scene presence.

### Reject as automatic authority
- exact external settlement dimensions;
- exact five-section/twelve-area counts;
- medieval architecture identity;
- exact reference colors where they conflict with current project palette;
- one flattened scene image per narrative state;
- a unique one-off character drawing for each equipment combination.

---

## 3. Scene composition stack

Default z/composition order:

1. far background / sky / distant architecture;
2. world base / permanent architecture;
3. permanent environment modules;
4. stateful environment overlay;
5. floor/path/foreground occlusion;
6. world props;
7. interactable props;
8. NPC/player rear accessories;
9. NPC/player body sprite;
10. equipment paper-doll layers;
11. held objects;
12. injury/status overlays;
13. ability/interaction FX;
14. player-safe world markers;
15. scene vignette/frame;
16. contextual character panels;
17. narrative text;
18. choices/actions;
19. navigation/system UI.

Exceptions must be documented because incorrect z-order can make an asset appear detached or hide critical state.

---

## 4. Asset-reuse compatibility test

An asset may be reused in another scene only if all relevant conditions pass:

- pixel density compatible;
- perspective compatible;
- camera angle compatible;
- light direction compatible or intentionally neutral;
- palette/value range compatible;
- material language compatible;
- scale compatible;
- ground/pivot alignment compatible;
- silhouette still readable;
- occlusion behavior known;
- state binding still valid;
- no location-specific symbol contradicts the new context.

If one condition fails, choose one of:
- create a variant;
- palette remap through an approved authored variant;
- use a location-specific overlay;
- rebuild the asset;
- reject reuse.

Do not stretch, blur, arbitrarily recolor, or paste an asset merely to save production time.

---

## 5. Character presence -> panel contract

The UI must derive visible character panels from a **player-safe scene presence projection**.

Minimum safe panel input per character:
- stable character ID;
- display name if known;
- presence = true/false;
- role in scene: player / speaker / party / nearby / remote-contact;
- portrait asset ID;
- expression/state tag;
- visible equipment tags when needed;
- visible condition tag when needed;
- dialogue focus priority;
- whether panel interaction is available.

The UI must never infer presence from:
- raw future scene definitions;
- hidden NPC registry entries;
- secret observers;
- hidden relationship states;
- raw quest authoring metadata.

### Layout behavior

One character:
- one focused panel;
- unused panel space returns to scene/narrative.

Two characters:
- player + primary interlocutor or two dialogue participants;
- focus indicates speaker without removing the other.

Three or more:
- compact group strip, stack, or carousel;
- primary speaker receives emphasis;
- party presence remains discoverable;
- never reduce narrative/choice touch targets below usability.

No character present:
- no fake portrait frame;
- scene/location art gets more space.

---

## 6. Player avatar usage

The player avatar is persistent identity, not decoration.

Required contexts:
- primary gameplay;
- Character screen;
- Equipment screen;
- selected map/party contexts when useful;
- major status/injury views;
- tactical combat if/when that client exists.

The same authoritative equipment state should resolve to the same visible equipment layers across these contexts, subject to scale-specific asset variants.

Avoid:
- redrawing the player as a different person in each screen;
- showing logically unequipped gear;
- hiding equipped visual gear simply because the narrative panel changed;
- forcing tiny accessories at scales where they become noise.

---

## 7. NPC visual identity

Every recurring NPC should have:
- stable ID;
- canonical body proportions;
- turnaround;
- palette;
- hairstyle/identity anchors;
- permanent marks;
- default equipment;
- asymmetry notes;
- expression set;
- pose/animation set as needed;
- allowed state variants;
- forbidden deviations.

A one-scene background NPC may use a typed archetype, but must not accidentally reuse a unique recurring-character identity.

---

## 8. Equipment overlay contract

A wearable/held visual requires:
- source item ID;
- slot;
- body rig version;
- native canvas;
- anchor;
- z-order;
- front/rear split if required;
- occlusion mask;
- directional variants if required;
- animation compatibility;
- state variants;
- fallback behavior if art is missing.

Fallback rule:
authoritative equipment can remain logically equipped even when a visual layer is unavailable. UI must label or gracefully omit the visual rather than invent geometry.

---

## 9. Environment modularity

Environment production should favor reusable families:

- wall/floor/path tiles;
- doors/gates;
- windows;
- railings/fences;
- lights;
- benches;
- signs;
- crates/storage;
- workstations;
- vegetation;
- water/terrain edges;
- structural columns;
- industrial/depot modules;
- civic modules;
- underground/service modules.

A location's identity should emerge from:
- layout;
- landmark;
- material family;
- prop mix;
- lighting;
- state;
not from inventing an entirely separate asset library for every room.

---

## 10. Text-art and UI overlays

Text/UI may overlay scene art only inside defined safe regions.

Each scene/location master should declare:
- no-text region;
- safe text region;
- character-panel safe region;
- choice-panel safe region;
- marker-safe region;
- focal landmark bounding box;
- crop-safe bounds.

Rules:
- never cover the primary interaction landmark with persistent UI;
- never cover a speaking character's face with a panel that could be relocated;
- narrative text readability outranks decorative background detail;
- accessibility font scaling may expand panels; art must tolerate this;
- pixel frames can surround text while font rendering remains accessibility-compatible.

---

## 11. Stateful location art

Preferred model:

`LOCATION_BASE + STATE_OVERLAYS + ACTORS + UI`

Examples of overlay-capable state:
- blackout/power restored;
- alarm/emergency light;
- door/gate opened/closed;
- damage;
- weather;
- Trace/ability residue;
- faction signage;
- temporary barricade;
- fire/smoke;
- quest/event marker.

A state needs a flattened alternate scene only when geometry/composition changes enough that overlays are no longer credible.

---

## 12. Map representation

The map must use:
- authoritative stable location IDs;
- player position;
- discovery;
- reachability;
- route visibility;
- event/quest markers;
- locked states;
- selected destination;
- local/world hierarchy.

The map art can imply streets, terrain, walls, gates, districts, and depth, but route legality comes from engine state.

Future global map levels:
1. world;
2. region/kingdom;
3. city/settlement;
4. district;
5. local/interior as needed.

---

## 13. Asset creation list — immediate

Existing/partially defined families:
- player base 32x48;
- player equipment overlays;
- Tamsin identity/turnaround;
- Depot Jacket;
- current item icons;
- Gate Twelve location set;
- map/UI icons;
- Trace FX;
- environment props.

Immediate documentation/production gaps:
- canonical player identity decision;
- contextual character-panel visual frame;
- panel speaker-focus states;
- group-panel layout;
- location safe-area metadata;
- environment module manifests;
- global map icon hierarchy;
- location-specific palette/material sheets;
- equipment fallback visual state;
- held-object anchor contract integration;
- status/injury overlay catalog;
- additional recurring NPC identity sheets;
- loading/transition art rules;
- tactical-combat sprite requirements once combat contract exists.

---

## 14. What may be rebuilt

Presentation may be replaced if necessary:
- current procedural placeholder avatar;
- procedural scene drawings;
- screen composition;
- navigation layout;
- map rendering;
- contextual panels;
- visual asset loader;
- asset registry;
- Compose presentation components.

Do not rebuild merely for novelty.

The replacement must preserve or deliberately migrate:
- player-safe projection boundary;
- authoritative engine state;
- save compatibility;
- stable IDs;
- equipment truth;
- quest truth;
- relationship/knowledge secrecy;
- accessibility;
- narration controls.

---

## 15. Verification gates

Before an art/UI system is considered integrated:

1. native-size review;
2. nearest-neighbor/integer scaling check;
3. anchor alignment check;
4. z-order/occlusion check;
5. palette/material consistency check;
6. player-safe state-binding review;
7. scene safe-area review;
8. smallest supported phone-width review;
9. accessibility text-scale review;
10. representative Android runtime screenshot/interaction test;
11. save/load state restoration check when visual state depends on saves;
12. no hidden-state leakage.

---

## 16. Handoff

CONFIRMED:
- pixel art is mandatory;
- existing native-size and paper-doll contracts are retained;
- reference boards are not automatically production assets;
- UI may be redesigned;
- engine remains authoritative;
- panels depend on actual player-safe scene presence.

ADOPTED:
- layered scene composition;
- compatibility gate for asset reuse;
- contextual panel model;
- safe-area metadata;
- stateful overlays before flattened duplicates.

UNKNOWN / NEXT:
- final player fixed identity vs configurable identity;
- full recurring NPC roster;
- global world palette families;
- tactical-combat sprite requirements;
- exact final screen compositions;
- exact global map hierarchy content.

NEXT ACTION:
Create the global world/map schema, then map each current Gate Twelve asset and location into that schema before expanding geography.
