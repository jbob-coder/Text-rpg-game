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
