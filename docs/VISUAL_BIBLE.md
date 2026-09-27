# Pixel Visual Bible — v0.1

## Goal

The game can use portraits, scene illustrations, equipment callouts, and short UI animations while preserving one coherent pixel-art language. Generated or hand-made assets must follow the same specification before being accepted.

## Baseline style

- Pixel art, readable at mobile size.
- Strong silhouettes before internal detail.
- Limited local palette per character and location.
- No photorealistic rendering mixed into the game UI.
- Avoid inconsistent pseudo-pixel art where a smooth painting is merely overlaid with a pixel filter.
- Lighting direction and scale must be documented per location set.

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

## Consistency rule

Do not regenerate a character from a prose prompt alone after the first approved design. Future generation prompts must reference the canonical visual spec and approved reference assets.

## Animation rule

Animation should communicate game state, not exist only as decoration. Examples:

- stat gain: restrained meter movement, not a giant reward explosion for +1
- technique discovery: new icon silhouette becomes visible
- mastery: animation becomes cleaner/faster than the unstable version
- relationship shift: subtle portrait/emote change where appropriate
- injury: persistent status marker and visual overlay
- major evolution: bespoke sequence reserved for true milestone changes

## Scene composition

Text remains primary. Art supports comprehension and atmosphere.

Recommended mobile composition:

1. compact scene header
2. scene illustration/portrait region
3. readable narrative text
4. optional state chips (time, location, party)
5. choice list
6. expandable character/stats/inventory panels

Avoid permanently displaying every statistic. Detailed sheets should be one action away so the narrative screen stays readable.
