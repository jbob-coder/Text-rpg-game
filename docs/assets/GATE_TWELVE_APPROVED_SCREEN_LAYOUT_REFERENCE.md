# THE GAME — Gate Twelve Approved Screen Layout Reference

Status: **OWNER-APPROVED VISUAL DIRECTION / REFERENCE CONTRACT**  
Date: 2026-10-05 AST  
Scope: Gate Twelve Sector 01 exploration/current-location presentation  
Parent authorities:
- `docs/assets/GATE_TWELVE_MAP_PIXEL_ASSET_BLUEPRINT.md`
- `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`
- `docs/android/APPLICATION_UX_MASTER_PLAN.md`

## 1. Owner decision

The owner approved the revised Gate Twelve screen direction after rejecting the earlier steep isometric/city treatment.

The approved reference is a **near-top-down / shallow three-quarter 2D pixel-art gameplay view** with grounded municipal/industrial architecture, clear roads and pedestrian space, restrained vegetation, strong landmark readability and compact HUD overlays.

This reference is a composition target, not a new gameplay-state authority. Runtime state, routes, actors, objectives and reachability remain owned by their authoritative systems.

## 2. Camera and presentation lock

Use:
- near-top-down / shallow three-quarter camera;
- fixed authored orientation;
- low perspective distortion;
- readable building fronts while preserving useful ground/floor area;
- clear north/south/east/west spatial relationships;
- phone-readable silhouettes;
- nearest-neighbor-safe pixel art.

Reject:
- steep isometric camera;
- dramatic diagonal city perspective;
- free-orbit 3D presentation;
- medieval-fantasy city massing;
- dense cyberpunk/neon skyline treatment.

## 3. Reference screen order — back/top to front/bottom

The approved composition is documented in this order so later assets can be reconstructed consistently.

1. **Northern perimeter / continuation** — restrained tree line and the route beyond the sector boundary.
2. **Gate Twelve fortified boundary** — heavy municipal wall, central gate opening/door, flanking structural towers, restrained red municipal banners, practical guards and lamps.
3. **Gate approach road** — broad north/south road leading directly from the district toward Gate Twelve; sparse lane/maintenance markings; no decorative clutter that obscures navigation.
4. **Municipal Archive block — upper-left** — cleaner institutional civic facade, front steps/entry, restrained landscaping, lamps and readable pedestrian apron.
5. **Workshop Row block — upper-right** — linked practical repair bays, shutters/open work fronts, tools/crates only where justified, warmer practical lighting, industrial rather than commercial-luxury identity.
6. **Primary east/west street** — road crossing the gate approach; crosswalk/curb logic must remain spatially coherent.
7. **Jack / current-location focus** — Jack occupies the playable ground plane rather than a detached UI diorama; his sprite must preserve approved identity and paper-doll contracts.
8. **Depot Plaza — lower-center** — open municipal paving with large readable negative space, benches, lamps, planters/trees and one restrained civic focal monument/marker. The plaza is not a market and should not be filled with tents or stalls.
9. **Lower-left civic/service block** — building mass and landscaping may frame the plaza but must preserve walkable/readable routes.
10. **Lower-right neighborhood/service frontage** — grounded low-rise municipal/residential/service architecture; not a forest trail and not a disconnected wilderness biome.
11. **Foreground/lower road continuation** — sector continues beyond the camera; roads and sidewalks must connect logically rather than terminating decoratively.

## 4. Explicit removals from the rejected iterations

Do not reintroduce unless a later authoritative map/world decision requires them:
- waterfront/ocean framing for this approved screen;
- dock or pier occupying the lower-left merely for visual interest;
- boat/ship inserted into the sector without authored transport/water geometry;
- improvised market tents in Depot Plaza;
- isolated forest trail on the lower-right that breaks the urban district fabric;
- oversized fantasy towers/castle massing;
- excessive ornamental banners;
- dense medieval/cyberpunk street clutter.

## 5. Asset decomposition — every visible detail is layered

### 5.1 Ground/surface family
1. gate approach asphalt;
2. east/west road asphalt;
3. lane/maintenance markings;
4. crosswalk markings;
5. civic sidewalk;
6. curb/edge modules;
7. Depot Plaza paving;
8. Archive entrance paving/steps;
9. Workshop service apron;
10. drains/utility seams;
11. localized wear decals.

### 5.2 Gate Twelve family
1. wall base module;
2. reinforced pillar/tower module;
3. central twin gate/door;
4. gate service hardware;
5. municipal banner mount;
6. banner cloth variant;
7. guard post/standing anchor;
8. gate lamp;
9. vegetation-at-wall modules;
10. neutral gate sign/label anchor;
11. runtime state overlay anchors for locked/reachable/Trace/Echo states.

### 5.3 Municipal Archive family
1. institutional facade shell;
2. entrance door;
3. window modules;
4. steps;
5. civic trim;
6. archive identity plate/symbol anchor;
7. planters/low shrubs;
8. municipal trees;
9. benches;
10. lamps;
11. optional state overlays.

### 5.4 Workshop Row family
1. linked bay shell;
2. shutter/open-bay variants;
3. workbench;
4. tool rack/tool silhouettes;
5. small storage/crates;
6. utility cabinet;
7. workshop lamps;
8. contractor symbol/sign anchor;
9. service apron wear;
10. restrained salvage/scrap clusters.

### 5.5 Depot Plaza family
1. plaza slab field;
2. central civic monument/marker;
3. monument base;
4. benches;
5. warm civic lamp posts;
6. planters;
7. compact municipal trees;
8. low flower/ground-cover accents;
9. notice-board anchor if required by gameplay;
10. NPC standing/sitting anchors;
11. blackout/emergency overlays.

### 5.6 Lower district family
1. low-rise municipal/service building shell;
2. residential/service door/window modules;
3. roof equipment where justified;
4. utility boxes;
5. small fenced/landscaped edge;
6. sidewalk connectors;
7. road continuation;
8. lamps;
9. sparse vegetation.

### 5.7 Character/NPC family
1. Jack gameplay sprite;
2. Jack equipment layers;
3. guards;
4. municipal workers;
5. workshop workers;
6. civic pedestrians;
7. Tamsin when authoritative projection places her here;
8. interaction/focus markers as UI, not baked into sprites.

### 5.8 HUD/UI family
1. Jack identity/portrait card;
2. level display;
3. HP bar;
4. AP/action-resource bar when contextually valid;
5. primary objective panel;
6. secondary objective list;
7. sector mini-map;
8. current-position marker;
9. objective marker;
10. compass/orientation marker;
11. contextual location labels — debug/reference only unless final UX explicitly retains them.

## 6. Layer order

Render order target:
1. base ground;
2. roads/plaza/sidewalk surfaces;
3. permanent architecture;
4. permanent landscaping;
5. static props;
6. state-dependent environment overlays behind actors;
7. NPCs and Jack according to local ground/occlusion order;
8. held/equipment overlays;
9. foreground occluders;
10. transient FX;
11. interaction/selection markers;
12. HUD and contextual panels.

## 7. Spatial-coherence rules

Every future reconstruction must pass these checks:
- roads connect to roads or authored gates/termini;
- sidewalks connect to entrances and pedestrian areas;
- buildings have plausible access points;
- Depot Plaza remains a public open hub, not a random market;
- vegetation decorates civic space without becoming a forest biome;
- vehicles/boats/large props appear only where supporting infrastructure and authored world state justify them;
- props do not block required routes;
- labels/HUD never compensate for incoherent physical layout;
- each landmark remains recognizable without its floating text label.

## 8. Visual-language rules

Target:
- grounded municipal infrastructure;
- contemporary/near-future practical construction;
- industrial service details where appropriate;
- muted stone/concrete/steel base;
- warm practical lamps;
- restrained green vegetation;
- cyan/blue only as sparse signal/Trace/status accent;
- readable pixel clusters and strong silhouettes.

Avoid:
- neon cyberpunk saturation;
- medieval castle-town styling;
- fantasy harbor styling;
- excessive decorative clutter;
- visual noise at phone scale.

## 9. Reference-image provenance

The approved visual reference was generated during the 2026-10-05 owner review conversation and supplied back by the owner as the preferred direction. The binary image is not embedded by this documentation-only commit. This document records the owner's approved composition and the reconstruction requirements so the visual decision is not lost.

## 10. Next visual outputs required

After this contract is recorded, produce separate reference images for:
1. **Settings UI** — complete Settings screen family showing gameplay, display, audio, accessibility, controls and developer separation where applicable;
2. **Primary gameplay UI** — exploration/current-location screen using this approved Gate Twelve composition, with HUD reduced to player-needed information and no debug-style permanent location labels;
3. later: tactical combat UI using the same spatial/visual language at the approved higher tactical framing.

Those images are visual references. They do not by themselves mark the corresponding runtime UI as implemented or verified.
