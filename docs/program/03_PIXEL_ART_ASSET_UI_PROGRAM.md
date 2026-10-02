# Pixel Art, Asset and UI Program

Status: ACTIVE / ARCHITECTURE

## Scope

Owns:
- pixel-art rules;
- native grids;
- character paper-doll layers;
- portraits;
- scene masters;
- map art;
- props;
- architecture modules;
- decals;
- overlays;
- icons;
- FX;
- UI chrome;
- contextual panels;
- reuse/occlusion/alignment rules;
- asset lifecycle and verification.

Does not own gameplay truth.

## Existing normative sources

- `docs/VISUAL_BIBLE.md`
- `docs/assets/PIXEL_ASSET_MASTER_PLAN.md`
- `docs/assets/CHARACTER_PIXEL_BLUEPRINTS.md`
- `docs/assets/ASSET_MANIFEST_SCHEMA.md`
- `docs/assets/REFERENCE_TO_BLUEPRINT_PIPELINE.md`
- `docs/assets/GATE_TWELVE_MAP_PIXEL_ASSET_BLUEPRINT.md`

## Reference-derived ideas adopted

The supplied visual references support:
- modular environment pieces rather than flattened whole locations;
- repeatable wall/floor/roof/road/prop families;
- layered equipment over a stable character base;
- consistent inventory/equipment icon families;
- scene-specific panels that react to who is present;
- reusable visual FX/overlays;
- stable silhouettes and palette families.

The references remain non-authoritative for names, exact values, lore, proprietary character designs and one-to-one layouts.

## Layering contract

Preferred rendering families:

### Environment
1. base terrain/surface
2. permanent architecture
3. reusable structure modules
4. permanent props
5. stateful props
6. decals/wear
7. weather/hazard/event overlay
8. characters
9. interaction/quest markers
10. UI selection/feedback

### Character
Use the existing paper-doll z-order unless a versioned rig migration supersedes it.

Gameplay state selects equipped/active content. Art renders it.

## Contextual character/room panels

Requirement P-ART-PANEL-001:
The application may change visible portrait/panel composition based on authoritative scene presence.

The panel may show:
- player;
- one focused speaker;
- multiple present characters;
- party members;
- relationship/emotion/status indicators if player-safe;
- scene/location context;
- actionable interaction affordances.

The panel may not infer that an NPC is present merely because an asset exists.

Presence source must come from engine/scene projection.

## Text-art / raster reuse rule

Reusable text-art/pixel components must declare:
- native grid;
- anchor/pivot;
- z-order;
- occlusion behavior;
- allowed palettes/material family;
- lighting assumption;
- scale policy;
- reusable contexts;
- forbidden contexts.

A component that only fits one scene may remain unique. Reuse is not mandatory when it damages readability or identity.

## Overlay rule

Temporary state must normally be separable:
- blackout;
- emergency light;
- Trace effects;
- damage;
- injuries;
- weather;
- faction control;
- alerts;
- quest/event state.

Do not bake temporary state permanently into a reusable base asset when the same architecture/object can exist without that state.

## Asset lifecycle

`REQUIREMENT -> WRITTEN CONTRACT -> REFERENCE -> SELECT/REJECT -> BLUEPRINT -> NATIVE MASTER -> INTEGRATE -> TEST -> VISUAL QA -> VERIFIED`

No generated reference skips directly to shipped art.

## Required future documents

- CHARACTER_PANEL_CONTEXT_CONTRACT
- ROOM_SCENE_COMPOSITION_CONTRACT
- ASSET_REUSE_MATRIX
- OCCLUSION_AND_ANCHOR_STANDARD
- MAP_OVERLAY_STANDARD
- NPC_PORTRAIT_STATE_STANDARD
- FX_READABILITY_STANDARD
- MOBILE_PIXEL_SCALING_STANDARD
- UI_PANEL_NAVIGATION_STANDARD
- ASSET_RETIREMENT_MIGRATION_LOG
