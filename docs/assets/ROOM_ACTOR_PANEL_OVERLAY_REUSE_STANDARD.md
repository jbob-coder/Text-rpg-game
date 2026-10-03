# THE GAME — Room Actor, Character Panel, Overlay & Reuse Packet Standard

Status: **ACTIVE / VISUAL CHILD STANDARD**  
Parent: `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`

## 1. Purpose

This standard defines how a room/area packet combines environment art, player character, NPC actors, portraits/panels, props, text/signage, overlays, equipment, FX, and reusable assets without making the scene look assembled from unrelated sources.

It is a child contract. Identity rules still come from character blueprints/references; gameplay presence still comes from player-safe projected state.

## 2. Required area packet

Each player-facing area should eventually have:
- area ID;
- parent location ID;
- environment source master;
- material/palette signature;
- perspective;
- native pixel density;
- lighting direction;
- actor ground line;
- actor scale range;
- prop anchors;
- foreground occluders;
- signage/text anchors;
- state-overlay anchors;
- FX anchors;
- portrait/panel-safe UI zone;
- map/arrival-preview asset;
- animation list;
- runtime consumer;
- QA screenshots.

## 3. Actor presence

A character is shown in the room only when authoritative player-safe projection says that actor is present.

The visual layer does not infer presence from:
- hidden quest flags;
- private NPC goals;
- raw scene metadata;
- developer-only state.

## 4. Character representation layers

A named actor may have three simultaneous representations:

### Room actor
Small gameplay sprite composited into environment.

### Portrait
Higher-information identity asset used in dialogue or inspection.

### Focus panel
UI container holding portrait, name, player-safe relationship/status, dialogue/actions, and context.

All three must share identity anchors:
- face/hair;
- silhouette;
- outfit/equipment;
- role markers;
- permanent marks;
- palette family.

## 5. Player character

Jack's final player identity uses:
- approved identity reference;
- source-native gameplay master;
- paper-doll/equipment overlays;
- portrait/focus asset;
- action/pose variants;
- status overlays separated from identity art.

Equipment overlays must preserve the established 32x48 paper-doll contract until an explicit rig migration replaces it.

## 6. Reuse compatibility signature

An asset can be reused directly only when compatible in:
- pixel density;
- perspective;
- scale;
- light direction;
- value range;
- palette family;
- material language;
- anchor/pivot;
- occlusion;
- semantic state.

If one or more dimensions fail, use one of:
- adapt;
- recolor;
- redraw;
- re-anchor;
- split into reusable module;
- reject for that area.

Do not force reuse merely because an asset exists.

## 7. Text and signage

World signage belongs to environment/prop art and follows the area's perspective/pixel density.

UI text remains crisp UI typography and is not rasterized into world art unless the world object itself contains text.

Reusable sign frames may be shared; sign content must remain semantically correct for the location.

## 8. Overlay classes

Reusable overlays include:
- power state;
- damage;
- weather;
- emergency light;
- access/lock;
- Trace/signal effect;
- smoke/steam;
- selection/current/reachable map state.

Overlays must not permanently mutate the source master when architecture is unchanged.

## 9. Animation

Animation is layered by ownership:
- environment ambient loop;
- prop mechanical loop;
- actor animation;
- equipment-attached animation;
- state overlay;
- transient FX.

Do not flatten every animation into a whole-scene video.

## 10. Visual cohesion test

Before reuse/integration, compare the candidate asset against the area packet:
- does edge density match?
- does scale match actors/doors?
- does light come from the same family?
- does palette/value range clash?
- does the material look like the same world?
- does the asset compete with the focal landmark?
- can overlays still read?
- can UI panels open without covering the only important landmark?

If the answers are poor, adapt or reject the asset.

## 11. Runtime composition order

Default:
1. environment;
2. structural modules;
3. static props;
4. state overlays behind actors;
5. player;
6. NPC room actors;
7. held/equipment overlays;
8. foreground occluders;
9. FX;
10. UI focus/panel layer.

A specific area may override ordering only when documented.

## 12. Area status states

Each packet tracks:
- PLANNED;
- BLUEPRINTED;
- SOURCE_MASTER_READY;
- RASTER_READY;
- INTEGRATED;
- VERIFIED;
- REFINEMENT_OPEN;
- SUPERSEDED.

“Created” and “finished” are not synonyms.

## 13. Per-character panel packet

For each named actor:
- actor ID;
- room sprite;
- portrait;
- focus-panel portrait/crop;
- emotion/pose set;
- outfit variants;
- equipment overlays;
- permanent marks;
- forbidden deviations;
- dialogue UI hooks;
- visibility/state rules;
- runtime asset IDs;
- QA references.

## 14. Gate Twelve application

Gate Twelve area packets must eventually exist for:
- Depot Plaza;
- Workshop Row;
- Municipal Archive;
- Platform Nine;
- Relay Workbench;
- Gate Twelve;
- Quiet Stair;
- Service Tunnel;
- Trace Chamber.

Each packet references the region geometry/material/asset plan and this composition standard.

## 15. Acceptance

An area is visually ready only when:
- source master exists;
- runtime art is native/nearest-neighbor compatible;
- actor placement works;
- panels do not destroy scene readability;
- overlays are composable;
- text/signage is coherent;
- no hidden-state visual leak exists;
- phone screenshot QA passes;
- provenance is recorded.


## Operational child

[Room composition implementation contract](ROOM_COMPOSITION_IMPLEMENTATION_CONTRACT.md) records the actual fixed actor lookup, future safe presence/panel contract and raster-precedence acceptance requirements.


## 15. Target beast-presence extension — D-044 selective extraction

Status: **PROPOSED DESIGN / VISUAL-PROJECTION EXTENSION / RUNTIME NOT IMPLEMENTED**

Source provenance:
- `docs/settlement-region-build-plan@65d2db8538c1b8302c314f2fbe9eb7a1b585b51d`;
- `docs/program/13_BEAST_ENTITY_ECOSYSTEM_AND_SCENE_PRESENCE_STANDARD.md` blob `96fcb08649c5d5564bf27fca5b754ada5479ae23`;
- `docs/program/15_CONTEXTUAL_BEAST_PRESENCE_ADDENDUM.md` blob `d1708154489f7320f75f285e4763acb79b3ac662`;
- selectively extracted under D-044.

This extension does not change the current D-030 actor-projection implementation status. It defines how future beast presence must fit the same authority principles when that domain is implemented.

### 15.1 Presence authority

A beast may render in a room/scene only when authoritative game/content state has produced a player-safe presence result for that beast/entity.

Presentation may not invent beast presence from:

- an available sprite;
- a portrait;
- a bestiary entry;
- a location ID;
- a scene ID;
- beast-zone membership alone;
- narrative prose;
- hidden encounter state.

### 15.2 Mixed-scene requirement

The future composition layer must be capable of representing, when authoritative projection requires them:

- player + NPC;
- player + multiple NPCs;
- player + beast;
- player + multiple beasts;
- player + NPCs + beasts;
- party + beasts;
- environment-only scene.

Character and beast truth must not be collapsed into one social-state model merely for UI convenience.

### 15.3 Beast focus information boundary

When a beast is focused, presentation may show only player-safe/observed information such as:

- known identity/species label;
- visible condition;
- visible injury;
- focus/encounter state;
- player-known scan/knowledge;
- range/distance only if an authoritative system exposes it.

Do not expose:

- hidden stats;
- hidden traits;
- unobserved injury;
- future behavior;
- unseen group members;
- secret ecology/population state;
- AI intent;
- unlearned weaknesses;
- undiscovered loot/resource information.

### 15.4 Group/pack identity

When gameplay distinguishes individual persistent beasts, group composition must preserve those stable identities.

When gameplay intentionally models an ordinary aggregate population, the UI must not fabricate individual persistent identities.

### 15.5 Layering relationship

Beast scene composition participates in the existing visual stack.

A typical mixed scene may contain:

1. base environment;
2. architecture;
3. permanent props;
4. stateful props;
5. environment overlays;
6. NPC/story actors;
7. beasts;
8. player where composition requires;
9. injury/status overlays;
10. ability/Trace/other FX;
11. interaction markers;
12. contextual UI.

Local occlusion may change draw order. It must not change state ownership.

### 15.6 Fallback rule

If authoritative projection says a beast is present but its final art is missing:

- use an explicitly approved missing-art/placeholder policy;
- preserve the correct stable identity;
- do not substitute a different species because its sprite happens to exist;
- do not remove the entity from authoritative state merely because presentation lacks art.

### 15.7 Target verification

A future beast-presence implementation should prove:

- absent beasts do not render;
- projected beasts render with the correct identity/family;
- mixed NPC/beast scenes preserve every projected visible entity;
- hidden beast state is not leaked;
- missing art falls back without species substitution;
- save/resume preserves the authoritative state from which presence is derived;
- presentation changes do not mutate beast/world truth.

The moving-base B0-B4 mode labels remain useful design shorthand, but this standard does not require those exact enum names in runtime code.
