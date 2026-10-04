# THE GAME — Pixel Asset Master Production Plan v1

Status: documentation-first; no generated image is canon or production-ready merely because it exists.

## 1. Objective

Build a reusable, inspectable pixel-art asset system for the Android narrative RPG. Assets must support the existing authoritative game state rather than becoming a second source of truth.

Current grounded content includes:

- player-visible layered avatar and equipment;
- NPC_TAMSIN;
- current items: Maintenance Seal, Dead Municipal Relay, Depot Utility Jacket, Insulated Work Gloves, Signal Ring, Courier Neck Tag;
- current locations: Platform Nine, Relay Workbench, Service Gate Twelve, Service Tunnel, Quiet Stair, Trace Chamber, Depot Plaza, Municipal Archive, Workshop Row;
- current quest categories: main, side, optional, lore;
- current core resources: health, stamina, focus, resolve;
- Trace Echo / Signal Pulse / Directional Trace presentation needs.

This plan is deliberately broader than the current procedural Compose drawings, but it does not silently invent new gameplay rules.

## 2. Non-negotiable production rule

Generated images are **reference material**, not drop-in game assets.

The production chain is:

`game requirement -> written visual contract -> reference generation -> review -> pixel reconstruction blueprint -> native pixel asset -> metadata -> integration -> runtime verification`

A generated reference may suggest silhouette, material, lighting, or composition. It may not bypass the reconstruction step.

## 2.1 Assistant-owned generation/extraction workflow

The intended source of newly created visual art for the evolved game is the project workflow itself: the assistant determines requirements from the documentation, generates the needed source/reference art, extracts or decomposes reusable visual pieces, and promotes cleaned native-grid pixel assets into the repository.

This does **not** authorize untreated generated imagery as production art. The production artifact remains the native pixel asset after extraction/reconstruction, cleanup, palette control, transparency cleanup, anchor/layer definition, metadata, state binding and QA.

Preferred production chain:

`game/design requirement -> assistant-generated source or extraction board -> asset extraction/decomposition -> native pixel reconstruction/cleanup -> metadata/provenance -> integration -> runtime/phone QA -> canon approval`

Generated boards should be deliberately composed to make extraction practical. Character, prop, building, tile, icon, portrait, FX and UI families should use separated subjects, clear silhouettes, consistent scale, minimal background contamination, and known target grids whenever feasible.

This workflow is the default for new visual production unless a repository-approved existing asset already satisfies the requirement.

## 3. Pixel resolution hierarchy

Use fixed native grids. Scale in the UI with integer or nearest-neighbor presentation.

| Family | Native master | Typical use |
| --- | ---: | --- |
| Micro icon | 16x16 | map markers, status marks |
| Standard icon | 24x24 | navigation, compact HUD |
| Item icon | 32x32 | inventory/equipment |
| Gameplay character | 32x48 | paper-doll and character sprite |
| Character portrait | 64x64 | dialogue/character inspection |
| FX cell | 64x64 | ability/status effects |
| Scene illustration | 128x64 | narrative location image |
| Map master | 256x144 minimum | district/world map |
| Reference board | 1024px+ | concept only; never shipped directly |

Compatibility note: the current Android prototype uses an 18x30 logical avatar and 64x32 procedural scene grid. Those are implementation placeholders, not the final source-art resolution. The replacement system must preserve UI readability while moving source art to the grids above.

## 4. Global pixel rules

1. No anti-aliasing inside shipped raster assets.
2. No fractional-pixel placement.
3. Do not scale source art with bilinear/bicubic filtering.
4. Maximum local palette:
   - icon: 4–8 colors;
   - item: 6–12 colors;
   - gameplay character/layer: 8–16 colors;
   - portrait: 12–24 colors;
   - scene: 16–32 colors.
5. One dominant light direction per location set.
6. Silhouette must remain readable at 1x native size.
7. Materials require distinct value ramps; metal, cloth, skin, glass and powered surfaces must not share identical ramps.
8. Transparency is binary for ordinary sprite edges unless a documented FX layer requires graded alpha.
9. Dithering is deliberate and sparse; never use noise as a substitute for material design.
10. Pixel clusters should be designed, not produced by applying a pixelation filter to smooth art.

## 5. Existing UI palette anchors

The current Android theme provides the cross-system UI anchors:

- Ink: #10151A
- Deep: #172128
- Panel: #22303A
- PanelAlt: #2D3D48
- Paper: #E9E2CC
- Muted: #9FB0B9
- Cyan: #63D8D1
- Gold: #E2B65F
- Danger: #D66B66
- Disabled: #59666D

These colors are interface anchors, not a mandate that every world object use them literally. World assets may introduce local ramps while preserving readable relationships with Cyan, Gold and Danger feedback.

## 6. Character construction standard

Gameplay characters use a 32x48 native body grid.

**Character art must not be geometry-built.** The 32x48 grid, anchors and layer coordinates are alignment contracts for finished pixel sprites. They must not be interpreted as permission to synthesize the visible character from rectangles, circles, polygons, block primitives, vector shapes, or procedural body geometry. Character appearance comes from generated/extracted/cleaned authored pixel-art assets.

### Required anchor points

Coordinates are expressed relative to the 32x48 sprite cell:

- pivot / ground: (16, 47)
- head center: (16, 8)
- neck: (16, 13)
- left shoulder: (10, 15)
- right shoulder: (22, 15)
- left elbow: (7, 24)
- right elbow: (25, 24)
- left wrist: (6, 32)
- right wrist: (26, 32)
- pelvis: (16, 28)
- left knee: (12, 37)
- right knee: (20, 37)
- left foot anchor: (11, 46)
- right foot anchor: (21, 46)
- main-hand attachment: (27, 31)
- off-hand attachment: (5, 31)
- neck item anchor: (16, 14)
- belt/accessory anchor: (16, 28)

These are pipeline defaults. A body-frame variant may move them only through a versioned character rig specification.

### Paper-doll z-order

1. ground shadow
2. back accessory / cape / pack
3. rear hair
4. base legs
5. footwear
6. base torso
7. arm-under layers
8. chest equipment
9. leg equipment
10. neck layer
11. head base
12. hair/front facial features
13. head equipment
14. hands/gloves
15. main-hand item
16. off-hand item
17. front accessory
18. injury/status overlay
19. ability/FX overlay

Gameplay state decides what is equipped. Art only renders that state.

## 7. Character turnaround standard

Every recurring character and every player body-frame master must have a six-view reference:

1. front
2. front three-quarter
3. left profile
4. right profile
5. rear three-quarter
6. back

Asymmetrical details must be authored separately; do not mirror a rolled sleeve, scar, badge, weapon, satchel, hairstyle or injury when mirroring changes identity.

## 8. Animation standard

Animation is modular and state-readable.

Baseline gameplay character sheets:

- idle: 4 frames
- walk: 6 frames per required direction
- run: 8 frames per required direction
- crouch enter/idle/exit: 2 + 2 + 2 frames
- interact/use tool: 4–6 frames
- hurt/recover: 3–4 frames
- ability activation: 6–8 frames
- equipment change feedback: UI/overlay animation, not a new body sheet

The current game is narrative-first, so only animations used by the shipped screen should be integrated immediately. Future movement sheets can be produced without changing the body rig.

## 9. Scene illustration standard

Scene masters use 128x64.

Each scene sheet records:

- location ID;
- dominant perspective;
- horizon/ground line;
- light source and color temperature;
- material palette;
- permanent architecture;
- temporary story-state overlays;
- interactable landmarks;
- safe text/UI crop zones;
- alternate-state triggers.

Do not create a unique flattened image for every minor story branch. Build location masters plus state overlays whenever architecture is unchanged.

## 10. Map asset standard

The map remains a visualization of authoritative location graph state.

Required visual layers:

- base district texture;
- roads/routes;
- discovered node;
- current node;
- reachable node;
- unavailable node;
- quest marker;
- event marker;
- player marker;
- selection ring;
- route preview;
- blackout/danger overlay.

Map art must never decide reachability. The engine projection remains authoritative.

## 11. Item and equipment standard

Every item asset receives:

- stable item ID;
- 32x32 inventory icon;
- material definition;
- primary/secondary silhouette;
- rarity/quality frame association;
- paper-doll layer if wearable/held;
- attachment slot and anchor;
- occlusion mask if it covers body/hair;
- damaged/active variant only when gameplay state supports it.

Paper-doll art must be separable from inventory icon art.

## 12. Naming and repository layout

Proposed paths:

```
assets/
  pixel/
    characters/
      player/
      npc_tamsin/
      supporting/
    equipment/
    items/
    locations/
    props/
    fx/
    ui/
    map/
    palettes/
    manifests/
  references/
    generated/
    approved/
  blueprints/
    characters/
    equipment/
    locations/
    ui/
```

Filename pattern:

`<stable_id>__<family>__<view_or_state>__vNN.png`

Examples:

- `NPC_TAMSIN__portrait__focused__v01.png`
- `ITEM_DEPOT_JACKET__paperdoll__front__v01.png`
- `PLATFORM_NINE__scene__blackout__v01.png`
- `TRACE_ECHO__fx__signal_pulse__v01.png`

Reference images use `REF_` prefix and never occupy the production asset path.

## 13. Reverse-engineering blueprint rule

For each generated reference:

1. identify 3–5 silhouette anchors;
2. identify major negative spaces;
3. define a limited palette;
4. map body/object proportions to native grid;
5. reconstruct large clusters first;
6. reconstruct material break lines;
7. add identity markers;
8. add one-pixel accents only after silhouette validation;
9. create layer masks and anchor points;
10. compare at 1x, 2x and target phone scale;
11. reject if identity depends on anti-aliased detail that cannot survive the native grid.

The blueprint must be sufficient for another artist or coding agent to recreate the asset without needing the original generated image.

## 14. Asset lifecycle states

Every asset moves through:

- PLANNED
- BRIEF_LOCKED
- REFERENCE_GENERATED
- REFERENCE_SELECTED
- BLUEPRINTED
- PIXEL_MASTER_BUILT
- INTEGRATED
- VERIFIED
- CANON_APPROVED

A generated reference is never later than `REFERENCE_SELECTED`.

## 15. Quality gates

An asset is production-ready only when:

- stable ID matches game/domain terminology;
- grid and palette limits are respected;
- required view/state exists;
- silhouette passes 1x inspection;
- anchor metadata is present when needed;
- paper-doll overlap is correct;
- transparent bounds contain no accidental halo;
- Android presentation uses nearest-neighbor/integer-safe scaling where applicable;
- asset does not expose hidden game information;
- visual state is driven by authoritative state;
- source/reference/blueprint lineage is documented.

## 16. Batch strategy

Production is organized into numbered batches of exactly 100 planned asset units.

Batch 001 establishes the reusable visual language for the current playable content. Batches 002–005 complete the v1 production baseline across character/NPC frameworks, equipment/items, world/environment construction, UI/FX/accessibility and developer QA. The complete roadmap is `ASSET_PRODUCTION_ROADMAP_001-500.md`. Future batches must inherit this master standard rather than resetting it.

Do not begin bulk image generation until:

- this master plan exists;
- character blueprints exist;
- the 100-item Batch 001 catalog exists;
- reference-to-blueprint rules exist;
- manifest schema exists.



## 17. V1 planning completion record

The documented v1 baseline contains exactly **500 unique production units**:

- Batch 001: 001–100
- Batch 002: 101–200
- Batch 003: 201–300
- Batch 004: 301–400
- Batch 005: 401–500

Mechanical catalog verification found:

- 500 total entries;
- no missing numbers;
- no duplicate numbers;
- no duplicate stable asset IDs.

This satisfies the planning prerequisite for beginning reference generation. It does **not** mark any asset generated, reconstructed, integrated or verified.
