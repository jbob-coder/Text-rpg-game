# Pixel Visual Bible — v0.2

## Product rule — non-negotiable

The shipped game presentation is **pixel style**. This applies to the player avatar, recurring characters, equipment layers, scene illustrations, locations, map presentation, icons, HUD ornaments, menus, transitions, and major narrative moments.

The project owner has explicitly authorized creative additions and presentation improvements as long as they preserve the requested game features, remain consistent with the authoritative gameplay architecture, and keep the pixel-art direction intact.

Pixel style is not a temporary prototype treatment. It is a product constraint.

## Goal

The game can use portraits, scene illustrations, equipment callouts, map visuals, character layers, and short UI animations while preserving one coherent pixel-art language. Generated or hand-made assets must follow the same specification before being accepted.

## Baseline style

- Pixel art, readable at mobile size.
- Strong silhouettes before internal detail.
- Limited local palette per character and location.
- No photorealistic rendering mixed into the game UI.
- Avoid inconsistent pseudo-pixel art where a smooth painting is merely overlaid with a pixel filter.
- Lighting direction and scale must be documented per location set.
- Nearest-neighbor or otherwise crisp integer-aligned presentation should be preferred when scaling pixel assets.
- Smooth-vector UI may be used only as invisible layout/interaction infrastructure; the visible presentation must conform to the pixel language.

## Character identity sheet

Every recurring character must have one canonical character spec before scene art is produced:

- stable character ID
- height class and body proportions
- skin tone
- hair shape, length, and palette
- eye color only if visible at target sprite scale
- default outfit and silhouette anchors
- faction or role markers
- equipment attachment points
- permanent scars/marks
- forbidden deviations
- approved emotion set
- approved poses

A generated image is not automatically canon. It becomes canon only after it matches the identity sheet and is explicitly approved.

## Player-avatar rule

The player is not represented only by text or a generic icon. The primary gameplay experience must support a persistent visible player character/avatar.

The player visual system should be designed as a layered paper-doll/sprite composition rather than a sequence of unrelated flattened images. At minimum, the architecture must be able to represent:

- base body / silhouette;
- hair and identity features;
- head equipment;
- chest equipment;
- hands/arm equipment where visible;
- leg equipment;
- footwear;
- main-hand item;
- off-hand item;
- accessory overlays when they materially affect appearance;
- injury/status overlays;
- pose/state variants.

Equipment state remains authoritative in gameplay systems. Visual layers reflect that state; they do not independently decide what is equipped.

## Machine-readable identity contract

The identity-sheet rule is now enforced by `src/textrpg/visuals.py`.

Recurring-character records can be validated before art work begins. The normalized generation contract preserves immutable identity details, approved expressions/poses, palette information, forbidden deviations, and approved reference-asset paths.

The first provisional implementation record is `NPC_TAMSIN` inside `content/vertical_slice_01.json`.

Important distinction:

- the identity record may be provisional with the content slice;
- generated art remains candidate-only;
- an image is not promoted to canon merely because it was generated from a valid record;
- once a design is approved, future assets must use the same record/reference assets rather than reconstructing the character from memory.

## Recommended asset families

For each major character:

- dialogue portrait: neutral
- dialogue portrait: 4–8 approved emotional variants
- full-body front/side/back reference
- exploration/combat sprite or paper-doll layers if used
- major equipment variants
- injury/status overlays

For each important scene/location:

- establishing image
- alternate state images only when the state materially changes what the player should understand
- environmental overlay tags for weather, alarms, damage, darkness, or faction control

For the player/world UI:

- pixel-style map markers with stable semantic roles;
- location tiles/cards with consistent border, icon, and state conventions;
- equipment-slot icons that match the same pixel grid/palette rules;
- quest-state icons for main, side, optional, and lore/world content;
- status/resource icons sized for mobile readability.

## Map and world presentation

The interactive map should feel like part of the game world, not like a generic mobile navigation screen.

Initial direction:

- 2D pixel-art city/location map before any heavier 3D implementation;
- clear selectable locations and travel routes;
- discovered/undiscovered states;
- quest/event indicators;
- player-position marker;
- locked/inaccessible locations with readable reasons when appropriate;
- world-state changes reflected visually where practical.

Movement/navigation commands update authoritative world state. The map renders that state and sends intent; it does not become a second world-state owner.

## UI pixel-language rule

Jetpack Compose or another UI toolkit may handle layout, accessibility, text rendering, touch targets, scrolling, safe areas, and navigation. The visible game shell must still read as a coherent pixel RPG.

Use:

- crisp pixel borders and panels;
- consistent corner geometry;
- pixel icons/sprites;
- restrained shadows/lighting consistent with the art direction;
- large readable narrative typography;
- generous mobile touch targets even when the visible button art is pixel-styled;
- clear separation between gameplay HUD and deeper panels such as Stats, Equipment, Inventory, Quests, Map, Saves, Settings, and Developer tools.

Do not sacrifice accessibility or text readability merely to imitate a low-resolution console interface.

## Consistency rule

Do not regenerate a character from a prose prompt alone after the first approved design. Future generation prompts must reference the canonical visual spec and approved reference assets.

Do not introduce isolated visual systems that ignore this bible. New art families should extend the existing visual language rather than reset it.

## Animation rule

Animation should communicate game state, not exist only as decoration. Examples:

- stat gain: restrained meter movement, not a giant reward explosion for +1
- technique discovery: new icon silhouette becomes visible
- mastery: animation becomes cleaner/faster than the unstable version
- relationship shift: subtle portrait/emote change where appropriate
- injury: persistent status marker and visual overlay
- major evolution: bespoke sequence reserved for true milestone changes
- equipment change: concise layer transition or slot feedback rather than a full-screen interruption
- map travel: short readable transition that preserves location context

## Scene composition

Text remains primary, but the player character and world should remain visually present. Art supports comprehension, atmosphere, identity, and spatial context.

Recommended mobile composition:

1. compact scene/location/time header
2. scene/map + visible player-avatar region
3. readable narrative text with tap-to-narrate affordance
4. optional state chips (time, location, party, urgent conditions)
5. choice list/cards
6. bottom or contextual navigation to Character, Inventory, Quests, Map, and More/Settings

Avoid permanently displaying every statistic. Detailed sheets should be one action away so the narrative screen stays readable.

## Acceptance gate for visual additions

A visual addition is acceptable only when it:

1. preserves pixel style at the actual mobile presentation size;
2. uses the canonical character/location identity data where applicable;
3. does not contradict authoritative gameplay/equipment/world state;
4. remains readable and touch-usable on Android;
5. has a repeatable asset/source path rather than existing only as an ephemeral chat image;
6. can be replaced or evolved without rewriting gameplay rules.


## Application integration authority

The visual bible defines the global pixel language. How those assets are composed inside scenes, reused, overlaid, bound to player-safe state, and shown in contextual character panels is defined by:

- `docs/PIXEL_ART_INTEGRATION_CONTRACT.md`

That integration contract may evolve application composition, but it may not weaken this bible's pixel-art, identity, provenance, or gameplay-authority rules.

## Production asset documentation

Detailed production rules live under `docs/assets/` and are normative for new pixel-art work:

- `docs/assets/PIXEL_ASSET_MASTER_PLAN.md` — source resolutions, paper-doll rig, map/scene/item standards, naming, lifecycle and QA.
- `docs/assets/CHARACTER_PIXEL_BLUEPRINTS.md` — player construction and canonical Tamsin blueprint.
- `docs/assets/ASSET_BATCH_001_001-100.md` — first exact 100-unit production batch.
- `docs/assets/REFERENCE_TO_BLUEPRINT_PIPELINE.md` — generated-reference to native-pixel reconstruction process.
- `docs/assets/ASSET_MANIFEST_SCHEMA.md` — state binding, provenance and QA manifest contract.

Generated/reference imagery is never accepted directly as the final shipped asset. It must be reconstructed into a documented native pixel master and pass the visual acceptance gate above.
