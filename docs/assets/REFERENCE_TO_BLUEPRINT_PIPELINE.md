# THE GAME — Reference Generation to Pixel Blueprint Pipeline v1

## Purpose

This pipeline controls how concept/reference imagery becomes reproducible pixel assets.

The reference is a **design probe**. The blueprint is the authority for reconstruction. The native pixel master is what may enter the game.

## Stage 0 — Requirement lock

Before any image generation, record:

- stable asset ID;
- gameplay system that needs it;
- exact screen/location where it appears;
- authoritative state that controls it;
- native pixel size;
- required views/states;
- palette budget;
- identity/material anchors;
- forbidden deviations;
- spoiler/visibility restrictions;
- dependencies on other assets.

No generation begins from only a loose prose idea.

## Stage 1 — Reference brief

Reference prompt/brief contains:

- "reference only; not final game asset";
- exact subject and stable ID;
- required view count;
- neutral presentation unless a scene mood is specifically being studied;
- silhouette priorities;
- material descriptions;
- canonical colors where locked;
- asymmetry requirements;
- no text/logos unless a documented symbol is required;
- no background clutter for turnaround/item references;
- no motion blur;
- no depth-of-field blur that hides edges;
- enough separation between views to inspect them independently.

## Stage 2 — Reference generation

Generate one tightly scoped family at a time.

Do not generate 100 unrelated assets in one image. For example:

- character turnaround board;
- one item family;
- one location composition;
- one FX study.

A batch may contain multiple candidates for the same brief, but they remain alternatives until one is selected.

## Stage 2A — Extraction-oriented generation

When the goal is to produce game assets rather than only study a composition, generate the source image or sheet so that later extraction is intentional.

Requirements:

- isolate each requested subject or view;
- avoid overlapping unrelated objects;
- use clean or transparent/simple backgrounds where possible;
- preserve consistent subject scale within a family;
- reserve visible spacing between sprites/props/views;
- keep lighting/material decisions consistent with the target area packet;
- avoid baked UI labels and unnecessary text;
- keep asymmetric identity details visible;
- generate families according to known target grids and layer needs;
- identify which parts are expected to become separate runtime assets.

The assistant owns the follow-through: generated source material is inspected, useful components are selected, extracted/decomposed, reconstructed or cleaned on the native pixel grid, named, versioned, bound and QA-checked before integration.

## Stage 3 — Reference review

Score the reference against the written brief.

### Character review

Check:

- silhouette;
- body proportions;
- left/right identity;
- hair volume;
- permanent marks;
- clothing layers;
- equipment attachment feasibility;
- pose neutrality;
- whether identity survives conversion to 32x48.

### Item review

Check:

- recognizable 32x32 silhouette;
- material readability;
- grip/wear feasibility;
- damaged/active state continuity;
- whether tiny detail is doing too much of the recognition work.

### Location review

Check:

- readable architecture;
- dominant landmark;
- depth layers;
- safe crop;
- lighting;
- reuse opportunities;
- overlay/state separation.

Reject references that cannot survive the native pixel budget.

## Stage 4 — Silhouette extraction

Before interior detail:

1. convert the selected concept mentally/analytically into flat masses;
2. identify primary silhouette;
3. identify secondary negative spaces;
4. identify 3–5 unmistakable anchors;
5. reproduce those masses on the native grid.

The blueprint records these shapes using coordinates, rectangles/polygons or a pixel mask.

## Stage 5 — Proportion blueprint

Record measurable ratios.

For characters:

- canvas bounds;
- top/bottom occupied pixel;
- head box;
- shoulder width;
- hip width;
- hand/foot dimensions;
- joint/attachment coordinates.

For items:

- bounding box;
- center/pivot;
- grip point;
- attachment edge;
- orientation.

For locations:

- horizon/ground line;
- major structure boxes;
- focal point;
- foreground/midground/background regions.

## Stage 6 — Palette reconstruction

Do not sample every color from the reference.

Instead:

1. identify material families;
2. define compact ramps;
3. align key accents with project palette;
4. remove redundant near-colors;
5. test grayscale/value separation;
6. test against PixelColors.Ink/Deep/Panel backgrounds.

Record hex/RGBA values in manifest.

## Stage 7 — Pixel-cluster construction

Build in this order:

1. largest silhouette;
2. structural planes;
3. material boundaries;
4. shadow clusters;
5. highlight clusters;
6. identity anchors;
7. one-pixel accents;
8. cleanup isolated noise.

Avoid checkerboard noise unless intentional dithering is documented.

## Stage 8 — Layer decomposition

Convert a flattened reference into reusable game layers.

Character example:

- skin/base;
- hair rear;
- hair front;
- shirt/base clothing;
- chest equipment;
- gloves;
- legs;
- footwear;
- neck;
- rings;
- accessory rear/front;
- held items;
- injury;
- FX.

Location example:

- architecture;
- props;
- character/foreground;
- emergency lights;
- blackout mask;
- ability/event overlay.

The goal is to avoid producing a new flattened image for every state combination.

## Stage 9 — View consistency

For multi-view assets:

- align ground line;
- match height;
- match volume;
- match palette;
- check asymmetry;
- check attachment positions.

No view is allowed to invent a different garment, hairstyle or object geometry.

## Stage 10 — Animation derivation

Animation begins only after a static master is approved.

Procedure:

1. duplicate approved static rig;
2. move body masses by planned key poses;
3. update joint/attachment anchors;
4. redraw cloth/gear clusters to preserve volume;
5. test loop at native scale;
6. test equipment following the rig;
7. verify no frame introduces extra colors accidentally.

## Stage 11 — Android presentation test

For player-facing assets:

- render at 1x native;
- render at intended integer scale;
- render inside Story screen;
- render inside Character/Inventory/Map destination;
- check landscape and narrow-width layout;
- inspect on dark panel background;
- verify no smoothing/halo;
- verify text remains readable around art.

The Galaxy A03 physical-device pass remains the final handset evidence when available.

## Stage 12 — Gameplay-state binding

Document the exact state binding.

Examples:

- `ITEM_DEPOT_JACKET_PAPERDOLL` <- equipped `ITEM_DEPOT_JACKET` in body slot;
- `MAP_NODE_REACHABLE` <- player-safe map node `reachable=true`;
- `ITEM_DEAD_RELAY_SIGNAL_LOST` <- visible story state after signal-loss outcome;
- `FX_TRACE_STRAIN` <- visible condition/status projection, not hidden raw state.

Never bind visuals directly to ad hoc UI booleans when authoritative state already exists.

## Stage 13 — Blueprint package

Every approved blueprint package contains:

- written brief;
- selected reference identifier;
- native canvas;
- silhouette map;
- palette;
- anchors;
- layer order;
- states/variants;
- animation frame plan if applicable;
- output filenames;
- integration binding;
- QA checklist.

A future agent must be able to rebuild the native asset from this package without seeing the original generated reference.

## Stage 14 — Production promotion

Promotion sequence:

`REFERENCE_SELECTED -> BLUEPRINTED -> PIXEL_MASTER_BUILT -> INTEGRATED -> VERIFIED -> CANON_APPROVED`

Only `PIXEL_MASTER_BUILT` or later may enter production asset paths.

## Reference rejection conditions

Reject and regenerate/rework if:

- identity depends on smooth gradients;
- silhouette is generic at target scale;
- required asymmetry is missing;
- proportions conflict across views;
- palette cannot be reduced cleanly;
- equipment cannot align to the standard rig;
- location cannot separate architecture from state overlays;
- concept embeds text that would be unreadable;
- reference reveals hidden/spoiler information;
- reference changes an authored identity without an approved design change.

## Practical example — Tamsin

1. Generate six-view neutral reference using locked Tamsin identity.
2. Select candidate whose left fringe, high collar, rolled right sleeve and satchel are clearest.
3. Reduce to silhouette and mark those four anchors.
4. Reconstruct front 32x48 master.
5. Rebuild left/right/back using same proportions, not independent generation.
6. Build 64x64 portrait from the same identity record.
7. Create neutral expression first, then derive focused/concerned/angry/relieved.
8. Add diagnostic-reader prop as separate layer.
9. Test badge/eyebrow notch visibility at native and Android scales.
10. Promote only after identity is consistent across all views.

## Practical example — Platform Nine

1. Generate reference composition for blackout tram depot.
2. Extract depot architecture, emergency floor strips and relay-handoff focal zone.
3. Reconstruct 128x64 base scene.
4. Put red emergency lights in overlay layer.
5. Put temporary figures/courier/Tamsin in foreground layers.
6. Produce evacuated state by changing temporary layers, not architecture.
7. Integrate by `location_id=PLATFORM_NINE` plus visible story-state overlay.

