# Gate Twelve District — Map Geometry to Pixel Asset Blueprint

Status: production-planning document.  
Source branch: `feature/service-tunnel-arrival-pixel-art@2f7f77d7925e94558d219d4ab2340fbb32476717`  
Map master: `MAP_GATE_TWELVE_DISTRICT_BASE`, 256x144 native pixels.

## 1. Purpose

This document converts the already-authored Gate Twelve district geometry into a stable visual production map.

The goal is to avoid repeatedly redesigning the district whenever new pixel art is produced. The geometry remains fixed unless an explicit map-design change is approved. New art should be generated or reconstructed to fit the existing blocks, routes and landmarks.

The intended workflow is:

`confirmed geometry -> written visual specification -> asset brief -> reference/pixel construction -> integration -> mobile QA`

This document is not a second gameplay-state system. It does not decide discovery, reachability, travel, quests, hazards, interactions or story state.

## 2. Authority and terminology

Three evidence classes are used below:

- **CONFIRMED GEOMETRY** — directly represented in `PixelMapArtCatalog.kt`.
- **CODE-PRESENT ASSET** — a matching stable asset ID exists in the current Android visual catalogs on the source branch. This does not by itself mean final canon art is approved.
- **PROPOSED VISUAL SPEC** — production guidance derived from the confirmed geometry, Visual Bible and Pixel Asset Master Plan. This may be refined without changing the map layout.

The map master uses a 256x144 coordinate grid. These coordinates describe the presentation texture only. Authoritative world-map nodes continue to use the engine's percentage coordinates and route graph.

## 3. Global district composition

### 3.1 Confirmed horizontal bands

| Map band | Confirmed geometry | Role | Proposed visual treatment |
| --- | --- | --- | --- |
| Surface civic district | y=0..47 | Workshop Row, Depot Plaza and Municipal Archive | Muted civic stone, worn concrete, restrained vegetation, public-lighting fixtures. Slightly brighter value range than the maintenance belt. |
| Depot/service belt | y=48..94 | Platform Nine, Relay Workbench, Gate Twelve and service routes | Industrial concrete, tram/depot surfacing, embedded service channels, practical metal trim. |
| Lower maintenance infrastructure | y=95..143 | Quiet Stair and lower service infrastructure | Darker municipal concrete, maintenance flooring, vents, rails, drains and service markings. |

The visual language must remain grounded municipal infrastructure. Do not turn the district into neon/cyberpunk scenery.

### 3.2 Confirmed perimeter streets

- Upper perimeter street: approximately y=5..11 across the map.
- Lower perimeter street: approximately y=126..133 across the map.
- Both use a road band plus a lighter center/edge treatment.

**Proposed asset treatment**

Use a repeatable civic-road surface family rather than one giant unique texture:
- worn road/asphalt tile;
- concrete curb tile;
- narrow utility seam/drain tile;
- sparse painted municipal lane mark;
- localized wear decals.

Do not bake gameplay routes into the road texture. Route lines remain a separate presentation layer driven by the map graph.

## 4. Named geometry regions

### 4.1 Workshop Row

**CONFIRMED GEOMETRY**
- Main block: x=49..102, y=8..29.
- Four attached shop/stall forms begin around x=53, 65, 77 and 89.
- Front service edge is near y=28..30.

**Identity**
Practical repair shops and municipal contractors, not luxury storefronts.

**PROPOSED VISUAL SPEC**
- Exterior shell: warm-gray/brown industrial masonry and sheet metal.
- Individual bays: distinguish through shutters, awnings, open repair apertures and tool silhouettes rather than radically different architecture.
- Ground edge: worn repair apron, drain marks and small salvage clusters.
- Windows/indicators: restrained amber/gold practical lighting.
- Optional prop layer: benches, scrap bins, tool carts and contractor signs using symbol shapes rather than unreadable text.
- Avoid large glowing signs, holograms or saturated neon.

**Relevant planned/current assets**
- `WORKSHOP_ROW_DEFAULT_SCENE` — CODE-PRESENT ASSET.
- `WORKSHOP_ROW_RUMOR_SCENE` — planned in Batch 001, not found in current code.
- `PROP_WORKSHOP_BENCH` — CODE-PRESENT ASSET.
- `DISTRICT_AMBIENT_DECAL_SET` — CODE-PRESENT ASSET.

**Map application rule**
The map should show the row as a linked group of practical bays. Scene art may show one selected stall in detail, but the map identity remains the full row.

### 4.2 Depot Plaza

**CONFIRMED GEOMETRY**
- Plaza/paving field: approximately x=105..143, y=8..39.
- Civic/depot frontage: approximately x=108..140, y=31..43.
- Trees and lamps already occupy the upper plaza composition.

**Identity**
Primary public/free-roam hub adjacent to depot infrastructure.

**PROPOSED VISUAL SPEC**
- Paving: large municipal slab pattern with restrained value variation.
- Depot frontage: robust public-service facade, practical doors/windows, municipal trim.
- Plaza furniture: lamp posts, utility planters/trees, notice board, barriers only where justified by the scene.
- Emergency readability: red/orange strip overlays may appear during blackout states, but the base plaza should not permanently look like an alarm zone.
- Keep paths visually obvious toward Workshop Row, Archive and depot/service routes.

**Relevant planned/current assets**
- `DISTRICT_PLAZA_OPEN_SCENE` — CODE-PRESENT ASSET.
- `DISTRICT_PLAZA_BLACKOUT_SCENE` — planned in Batch 001, not found in current code.
- `DEPOT_FACADE_EXTERIOR` — CODE-PRESENT ASSET.
- `PROP_DISTRICT_NOTICE_BOARD` — CODE-PRESENT ASSET.
- `EVACUATION_SIGNAGE_SET` — CODE-PRESENT ASSET.
- `DISTRICT_AMBIENT_DECAL_SET` — CODE-PRESENT ASSET.

**Map application rule**
Use facade/paving/furniture modules as separate reusable layers. Do not flatten every state into a unique map master.

### 4.3 Municipal Archive

**CONFIRMED GEOMETRY**
- Main block: approximately x=151..196, y=6..33.
- Frontage/courtyard and trees occupy the same upper-right civic zone.

**Identity**
Municipal records building with institutional storage and backup-power motifs.

**PROPOSED VISUAL SPEC**
- Exterior: institutional masonry/metal panels, narrow vertical windows and a clean civic silhouette.
- Courtyard: sparse paving, restrained trees and utility lighting.
- Interior scene language: tall shelving, record storage, public terminal, warm backup lamps.
- Signage: use symbols/plates; actual written records remain UI text.
- Material distinction: archive surfaces should read cleaner and more institutional than Workshop Row.

**Relevant planned/current assets**
- `DISTRICT_ARCHIVE_DEFAULT_SCENE` — CODE-PRESENT ASSET.
- `DISTRICT_ARCHIVE_TERMINAL_CLOSEUP` — planned in Batch 001, not found in current code.
- `MUNICIPAL_ARCHIVE_EXTERIOR` — CODE-PRESENT ASSET.
- `PROP_ARCHIVE_SHELF` — CODE-PRESENT ASSET.
- `PROP_ARCHIVE_TERMINAL` — CODE-PRESENT ASSET.

**Map application rule**
The map uses the exterior identity only. Interior shelving/terminal assets belong to scene composition, not the district map surface.

### 4.4 Platform Nine depot

**CONFIRMED GEOMETRY**
- Main depot block: approximately x=20..83, y=37..72.
- Platform/depot roof and facade are embedded in this block.
- Tram/maintenance tracks run approximately x=18..85 around y=69..78.

**Identity**
Municipal tram/depot evacuation platform and opening location.

**PROPOSED VISUAL SPEC**
- Architecture: heavy depot framing, broad service roof, practical windows and access doors.
- Tracks: dark rail steel, sleepers/maintenance crossbars and worn track bed.
- Platform edge: high-contrast safety strip used sparingly.
- Blackout state: emergency floor strips and shadow overlays, while keeping major silhouettes readable.
- Crowd/evacuation figures belong to scene art, not permanent map texture.

**Relevant planned/current assets**
- `PLATFORM_NINE_BLACKOUT_SCENE` — CODE-PRESENT ASSET.
- `PLATFORM_NINE_EVACUATED_SCENE` — planned in Batch 001, not found in current code.
- `PROP_DEPOT_DOOR` — CODE-PRESENT ASSET.
- `EMERGENCY_LIGHT_OVERLAY` — CODE-PRESENT ASSET.
- `BLACKOUT_SHADOW_OVERLAY` — CODE-PRESENT ASSET.
- `EVACUATION_SIGNAGE_SET` — CODE-PRESENT ASSET.

**Map application rule**
Tracks and depot mass are permanent. Emergency lighting, crowds and story-state damage are overlays or scene-state assets.

### 4.5 Relay Workbench annex

**CONFIRMED GEOMETRY**
- Annex block: approximately x=75..105, y=31..58.

**Identity**
Small technical maintenance annex attached to the depot/service zone.

**PROPOSED VISUAL SPEC**
- Exterior/map mass: compact utility room or annex footprint.
- Interior scene: maintenance bench, tool rail, storage, diagnostic light and relay focal area.
- Materials: darker steel/painted utility surfaces than the public plaza; still clean enough to read as maintained infrastructure.
- Relay object/state should remain a swappable prop, not painted permanently into the room texture.

**Relevant planned/current assets**
- `RELAY_WORKBENCH_DEFAULT_SCENE` — CODE-PRESENT ASSET.
- `RELAY_WORKBENCH_RELAY_OPEN_SCENE` — planned in Batch 001, not found in current code.
- `PROP_RELAY_WORKBENCH` — CODE-PRESENT ASSET.

**Map application rule**
The map only needs a readable annex footprint and service identity. Detailed relay state is reserved for scene/close-up presentation.

### 4.6 Service Gate Twelve

**CONFIRMED GEOMETRY**
- Main block: approximately x=119..154, y=56..85.
- Door/gate center mass sits inside that block.

**Identity**
Heavy municipal maintenance entrance separating normal district space from restricted infrastructure.

**PROPOSED VISUAL SPEC**
- Door: twin heavy panels, strong center seam, service hardware and restrained technical indicators.
- Surround: reinforced concrete/metal frame with visible maintenance wear.
- Signal/Trace effects: separate overlay; never bake active Echo state into the base door.
- Maintain a strong central silhouette so the gate remains readable at phone scale.

**Relevant planned/current assets**
- `GATE_TWELVE_SEALED_SCENE` — CODE-PRESENT ASSET.
- `GATE_TWELVE_ECHO_ACTIVE_SCENE` — planned in Batch 001, not found in current code.
- `PROP_GATE_TWELVE_DOOR` — CODE-PRESENT ASSET.

**Map application rule**
The map shows the gate landmark and surrounding service block. Locked/reachable state comes from map markers/UI, not from changing the underlying gate geometry.

### 4.7 Quiet Stair / Evac Stair

**CONFIRMED GEOMETRY**
- Utility/stair shaft block: approximately x=88..118, y=89..123.

**Identity**
Sparse maintenance stair used as a quieter branch/exit route.

**PROPOSED VISUAL SPEC**
- Angular stair silhouette with dark landings and narrow guidance lights.
- Utility shaft walls: darker municipal concrete than the public district.
- Railings: muted metal with strong pixel clusters, not 1-pixel visual noise.
- Signage: directional evacuation symbols only.
- Keep open negative space so the stair route remains legible.

**Relevant planned/current assets**
- `EVAC_STAIR_DEFAULT_SCENE` — CODE-PRESENT ASSET.
- `EVACUATION_SIGNAGE_SET` — CODE-PRESENT ASSET.
- `MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS` — CODE-PRESENT ASSET.

**Map application rule**
Use a shaft/stair iconography in the footprint; the map does not need to render every physical stair step.

### 4.8 Service Tunnel

**CONFIRMED GEOMETRY**
- Main plant/tunnel block: approximately x=161..199, y=78..108.
- Internal vertical ribs are already represented in the base map.

**Identity**
Restricted connective maintenance infrastructure below the evacuation route.

**PROPOSED VISUAL SPEC**
- Base surfaces: dark municipal wall panels, service floor, rails and vents.
- Repeated structure: pipe runs, cable trays, support ribs and access panels.
- Central depth: preserve a darker corridor opening/vanishing area.
- Indicators: cyan only as sparse maintenance status accents.
- Wear: drains, caution paint, maintenance labels and localized grime; no random noise.
- Signal aftershock/distortion must remain a state overlay.

**Relevant planned/current assets**
- `SERVICE_TUNNEL_DEFAULT_SCENE` — CODE-PRESENT ASSET.
- `SERVICE_TUNNEL_AFTERSHOCK_SCENE` — planned in Batch 001, not found in current code.
- `MAINTENANCE_CORRIDOR_CONNECTOR` — CODE-PRESENT ASSET.
- `MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS` — CODE-PRESENT ASSET.
- `PROP_TUNNEL_PIPE_SET` — CODE-PRESENT ASSET.
- `PROP_TUNNEL_CABLE_SET` — CODE-PRESENT ASSET.
- `DISTRICT_AMBIENT_DECAL_SET` — CODE-PRESENT ASSET.

**Map application rule**
The named Service Tunnel keeps its own recognizable geometry. Generic corridor/tile assets may support its visual texture, but must not replace the unique named-location identity.

### 4.9 Trace Chamber

**CONFIRMED GEOMETRY**
- Main block: approximately x=194..237, y=40..71.

**Identity**
Controlled municipal infrastructure space used for Trace practice/measurement.

**PROPOSED VISUAL SPEC**
- Base room: grounded service architecture, not a futuristic laboratory.
- Central apparatus: strong focal silhouette with calibration/measurement framing.
- Floor/walls: infrastructure atlas materials with a cleaner, more controlled arrangement than the Service Tunnel.
- Active state: bounded rings/lines/instrument response supplied by FX and overlays.
- Cyan accents indicate signal activity but should never dominate the room palette.

**Relevant planned/current assets**
- `TRACE_CHAMBER_IDLE_SCENE` — CODE-PRESENT ASSET.
- `TRACE_CHAMBER_TRAINING_SCENE` — planned in Batch 001, not found in current code.
- `PROP_TRACE_CHAMBER_APPARATUS` — CODE-PRESENT ASSET.
- `MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS` — CODE-PRESENT ASSET.

**Map application rule**
Keep the map representation architectural and neutral. Training success/failure and active signal intensity are runtime state, not permanent map texture.

## 5. Shared map infrastructure

### 5.1 Confirmed service-route geometry

The current map master contains the following route segments as presentation geometry:

- (46,52) -> (87,45)
- (46,52) -> (136,69)
- (46,52) -> (102,101)
- (136,69) -> (179,88)
- (136,69) -> (210,56)
- (179,88) -> (210,56)

These lines mirror the authored graph visually but are not the source of truth for travel.

**Production rule**
Do not bake route availability into background textures. Build:
1. neutral underlying service road/path surface;
2. route line overlay;
3. current/reachable/unavailable marker layers;
4. selection/preview state.

### 5.2 Street furniture and vegetation

The base map already establishes sparse tree and lamp placement in civic areas plus small material-breakup clusters.

**PROPOSED VISUAL SPEC**
- Trees: compact municipal/street trees with muted foliage; no lush forest treatment.
- Lamps: industrial-civic posts with warm practical light.
- Barriers/crates/scrap: use only in service/repair zones and keep silhouettes small.
- Do not scatter props uniformly. Preserve large readable negative-space areas.

## 6. Asset families to produce and reuse

### 6.1 Base surface tiles

Required reusable families:
- civic paving;
- depot/service concrete;
- lower maintenance concrete;
- asphalt/road;
- curb/edge;
- track bed/rail;
- drain/service seam;
- wall panel;
- floor panel;
- rail/vent;
- technical panel.

The current `MUNICIPAL_INFRASTRUCTURE_TILE_ATLAS` already covers wall/floor/panel/rail-vent concepts in code. New surface tiles should extend that family rather than creating a competing visual language.

### 6.2 Building modules

Prefer modular production where architecture repeats:
- municipal door/window families;
- depot facade modules;
- workshop bay modules;
- archive institutional facade modules;
- service wall/support modules;
- stair/shaft modules.

Named locations may combine reusable modules with unique landmarks.

### 6.3 Props

Use current stable prop IDs where available:
- `PROP_DEPOT_DOOR`
- `PROP_RELAY_WORKBENCH`
- `PROP_GATE_TWELVE_DOOR`
- `PROP_TUNNEL_PIPE_SET`
- `PROP_TUNNEL_CABLE_SET`
- `PROP_TRACE_CHAMBER_APPARATUS`
- `PROP_ARCHIVE_SHELF`
- `PROP_ARCHIVE_TERMINAL`
- `PROP_WORKSHOP_BENCH`
- `PROP_DISTRICT_NOTICE_BOARD`

Props should remain separable from architecture when story state can change them.

### 6.4 State overlays

Use separate layers for:
- blackout shadow;
- emergency light;
- Trace Echo / Signal effects;
- damage/wear when supported by visible state;
- event markers;
- quest markers;
- route selection.

Never paint a temporary game state permanently into the base district master.

## 7. Exact scene-master ID presence on the source branch

The checks below test whether the **exact Batch 001 scene/state stable ID** is present in the current Android visual catalogs. Absence of an exact scene-master ID does not prove that no related overlay or alternate visual implementation exists under another ID; related state layers must be audited separately before production.

At the source branch used for this document:

**CODE-PRESENT**
- `PLATFORM_NINE_BLACKOUT_SCENE`
- `RELAY_WORKBENCH_DEFAULT_SCENE`
- `GATE_TWELVE_SEALED_SCENE`
- `SERVICE_TUNNEL_DEFAULT_SCENE`
- `EVAC_STAIR_DEFAULT_SCENE`
- `TRACE_CHAMBER_IDLE_SCENE`
- `DISTRICT_PLAZA_OPEN_SCENE`
- `DISTRICT_ARCHIVE_DEFAULT_SCENE`
- `WORKSHOP_ROW_DEFAULT_SCENE`

**PLANNED IN BATCH 001 BUT NOT FOUND IN CURRENT CODE**
- `PLATFORM_NINE_EVACUATED_SCENE`
- `RELAY_WORKBENCH_RELAY_OPEN_SCENE`
- `GATE_TWELVE_ECHO_ACTIVE_SCENE`
- `SERVICE_TUNNEL_AFTERSHOCK_SCENE`
- `TRACE_CHAMBER_TRAINING_SCENE`
- `DISTRICT_PLAZA_BLACKOUT_SCENE`
- `DISTRICT_ARCHIVE_TERMINAL_CLOSEUP`
- `WORKSHOP_ROW_RUMOR_SCENE`

This distinction is intentional. A planned asset should not be treated as integrated merely because it is named in the asset production catalog.

## 8. Map marker contract

The current Android catalogs contain:
- `MAP_PLAYER_MARKER`
- `MAP_NODE_DISCOVERED`
- `MAP_NODE_CURRENT`
- `MAP_NODE_REACHABLE`
- `MAP_NODE_UNAVAILABLE`

These remain semantic overlays. They should not be merged into location art.

## 9. Production brief template for every future map asset

Before producing a new sprite/tile/module, record:

1. **Stable asset ID**
2. **Map region / location ID**
3. **Geometry target**
   - map bounding box or scene grid;
   - pivot/alignment if applicable.
4. **Asset family**
   - base tile, facade, prop, overlay, decal, marker, scene master, state variant.
5. **Permanent or temporary**
6. **Material definition**
   - concrete, painted metal, rail steel, glass, wood, cloth, vegetation, etc.
7. **Palette target**
   - local ramps plus compatibility with Paper/Cyan/Gold/Danger UI anchors.
8. **Lighting**
   - direction, intensity and whether baked or overlay-driven.
9. **Unique landmark**
10. **Reusable elements**
11. **Forbidden deviations**
12. **State owner**
   - engine/world state, scene ID, visual-only static identity.
13. **Integration target**
   - map base, scene catalog, prop placement, overlay catalog, decal catalog.
14. **QA**
   - native 1x silhouette;
   - integer scaling;
   - 320dp phone screenshot;
   - no hidden-state leakage;
   - no route/reachability ownership.

## 10. Recommended production order

Do not redraw the whole map.

### Pass 1 — Surface/material vocabulary
Produce/review:
- civic paving;
- road/curb;
- service concrete;
- maintenance wall/floor;
- track/rail;
- vents/drains/panels.

Goal: establish reusable material language.

### Pass 2 — Major landmark silhouettes
Produce/refine:
- Platform Nine/depot mass;
- Gate Twelve;
- Archive facade;
- Workshop Row bay family;
- Trace Chamber apparatus footprint;
- Quiet Stair shaft;
- Service Tunnel support/rib language.

Goal: make every region identifiable before small decoration.

### Pass 3 — Props and furniture
Apply existing prop families and only create missing variants after the base silhouettes work.

### Pass 4 — State overlays
Blackout, emergency, Trace effects and other temporary states.

### Pass 5 — Decals and wear
Add signage, drains, caution marks and controlled surface breakup last.

This order minimizes rework because detail does not determine geometry.

## 11. Integration protocol

When applying an asset to the map:

1. Read the current `PixelMapArtCatalog` geometry first.
2. Match the asset to an existing region or approved new geometry.
3. Reuse an existing stable asset ID if it already represents that object.
4. Keep static architecture separate from dynamic state.
5. Keep routes and reachability controlled by authoritative map projection.
6. Integrate the smallest visual slice.
7. Add/update a unit contract for the stable binding.
8. Capture the 320dp map screenshot.
9. Inspect clipping, readability, palette drift and landmark identity.
10. Only then move to the next region.

## 12. Change-control rule

If a future asset appears not to fit the current geometry, do not silently move the building or rewrite the map.

Choose one of:
- adapt the asset to the confirmed bounding box;
- create a modular crop/variant;
- document an explicit geometry-change proposal with affected routes/nodes;
- reject the asset.

Geometry changes are map-design decisions, not incidental art adjustments.

## 13. Immediate next asset-production targets

Based on the current geometry and Batch 001 gaps, the highest-value textual briefs to produce next are:

1. `SERVICE_TUNNEL_AFTERSHOCK_SCENE` — state variant over existing tunnel geometry.
2. `GATE_TWELVE_ECHO_ACTIVE_SCENE` — state variant over existing gate geometry.
3. `DISTRICT_PLAZA_BLACKOUT_SCENE` — overlay-driven state variant.
4. `TRACE_CHAMBER_TRAINING_SCENE` — active-state composition over the existing chamber.
5. `WORKSHOP_ROW_RUMOR_SCENE` — localized emphasis without changing the row geometry.
6. `DISTRICT_ARCHIVE_TERMINAL_CLOSEUP` — close-up scene, no map geometry change.
7. `RELAY_WORKBENCH_RELAY_OPEN_SCENE` — prop/state swap on existing workbench.
8. `PLATFORM_NINE_EVACUATED_SCENE` — same depot geometry with population/light-state change.

These should be specified and produced as state variants, not as redesigned locations.

## 14. Core rule

The map geometry is the scaffold. Pixel art supplies identity, material, atmosphere and readable landmarks.

**Do not rebuild the scaffold every time a new sprite is generated.**
