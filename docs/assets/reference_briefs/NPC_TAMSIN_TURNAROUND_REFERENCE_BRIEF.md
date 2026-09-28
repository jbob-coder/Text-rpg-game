# Dedicated Reference Brief — NPC_TAMSIN_TURNAROUND

Asset: `018 NPC_TAMSIN_TURNAROUND`  
Game identity: `NPC_TAMSIN`  
Target state after acceptable generation: `REFERENCE_SELECTED`

## Purpose

Generate a dedicated six-view Tamsin identity reference that can be reconstructed into consistent 32x48 gameplay sprites and 64x64 portraits.

Unlike the player-body reference, this image **is identity-constrained**.

## Required board

- minimum board size: 1536x1024;
- six full-body views:
  1. front;
  2. front three-quarter;
  3. left profile;
  4. right profile;
  5. rear three-quarter;
  6. back;
- all views on one ground line;
- equal apparent height;
- neutral stance;
- hands visible where practical;
- full shoes/feet visible;
- no cropping;
- no scene background beyond a neutral presentation field.

A small portrait inset may be included only if it does not reduce the six full-body views.

## Locked identity

Tamsin must remain:

- adult;
- average height;
- slim athletic build;
- long forearms;
- compact stance;
- medium warm-brown skin;
- dark brown eyes;
- short angular layered haircut;
- heavy **left-side fringe**;
- near-black hair with muted cool highlights;
- charcoal municipal utility jacket;
- pale work shirt;
- dark work trousers;
- high utility-jacket collar;
- narrow cross-body tool satchel;
- rolled **right sleeve**;
- small municipal systems badge on **left chest**;
- left-hip tool loop;
- small notch through the **right eyebrow**.

## Locked palette anchors

The reconstruction must be able to preserve:

- jacket base: `#30343B`;
- shirt: `#C9C7BE`;
- trousers: `#24272C`;
- skin shadow: `#8B5F4B`.

The generated reference may add compatible highlight/deep values but must not shift Tamsin into saturated neon colors.

## Critical asymmetry map

Generation must preserve the subject's left/right consistently across every view:

- fringe heavier on Tamsin's left;
- eyebrow notch on Tamsin's right eyebrow;
- right sleeve rolled;
- badge on left chest;
- left-hip tool loop;
- satchel strap follows one consistent shoulder-to-opposite-hip route;
- satchel remains a compact hip bag, not a backpack.

These asymmetries are identity anchors. A candidate failing even one should not be selected without explicit correction.


## FRONT-VIEW LEFT/RIGHT CHECK

For a **front-facing** Tamsin, use anatomical sides, not image-layout sides:

- Tamsin's **LEFT** appears on the **viewer RIGHT**.
  - heavy left-side fringe must occupy the viewer-right side;
  - left-chest badge must be on viewer-right;
  - left-hip tool loop must be on viewer-right.

- Tamsin's **RIGHT** appears on the **viewer LEFT**.
  - right-eyebrow notch must be on viewer-left;
  - the **right sleeve only** must be rolled on viewer-left.

The **left sleeve must remain visibly unrolled/full-length** enough that the asymmetry is unmistakable at 32x48. Do not roll both sleeves.

This anatomical/viewer mapping must remain consistent in the three-quarter and back views as the body rotates.

## Silhouette priorities

At gameplay scale, Tamsin should be identifiable through:

1. angular asymmetric hair;
2. high jacket collar;
3. narrow diagonal satchel strap;
4. compact hip satchel;
5. rolled right sleeve;
6. compact stance with slightly long forearms.

The eyebrow notch is a portrait/close-range identity marker rather than a gameplay-scale silhouette requirement.

## Clothing/material behavior

### Jacket
- practical municipal utility garment;
- charcoal;
- high collar;
- restrained seams/pockets;
- no armor plates;
- no oversized shoulder pads;
- no luminous chest panel;
- no fashionable long coat tail.

### Shirt
- pale work shirt visible at collar/center chest;
- should not look emissive white.

### Trousers
- dark practical work trousers;
- close enough to the body to preserve leg motion;
- no armored greaves.

### Satchel
- narrow cross-body strap;
- compact tool satchel at hip;
- no backpack;
- no oversized messenger bag.

### Badge
- small left-chest systems marker;
- abstract original symbol;
- no unreadable fake text required.

## Pixel-art language

- modern detailed retro pixel art;
- crisp clusters and controlled highlights;
- no smooth painted face;
- no photographic shading;
- no anti-aliasing dependence;
- portrait-level detail may inform the face, but the full-body design must remain reducible to 32x48.

## Lighting

- neutral upper-front light;
- same light on all six views;
- no dramatic colored rim;
- no Trace glow;
- no scene-specific emergency lighting.

## Forbidden deviations

Reject if generated with:

- long hair;
- ponytail/bun;
- backpack;
- neon outfit;
- missing eyebrow notch;
- eyebrow notch on wrong side;
- rolled sleeve on wrong arm;
- badge on wrong side;
- tool loop on wrong hip;
- satchel changing side between views;
- bulky armored silhouette;
- high-fashion redesign;
- different face shape between views;
- different skin tone between views;
- different hair volume between views;
- changed jacket length between views;
- youthful/chibi proportions inconsistent with adult identity.

## Portrait consistency requirement

The selected turnaround must support later 64x64 portraits with:

- identical hair silhouette;
- same right-eyebrow notch;
- same dark-brown eye identity;
- same skin ramp;
- same high collar;
- badge visible when crop permits;
- expressions changing only facial posture, not identity geometry.

## Reconstruction fit

When converted to 32x48:

- Tamsin uses global pivot `(16,47)`;
- shoulder span target x=9..23;
- high collar reaches around y=13;
- satchel bag mass roughly x=9..13, y=27..32 in front-facing reconstruction;
- right sleeve exposes visibly more forearm than left;
- forearms may extend one pixel farther than neutral player-body template;
- feet remain slightly closer together than Bodyframe A.

## Selection record

An accepted candidate must record:

- reference ID;
- Drive file ID;
- SHA-256;
- view-by-view asymmetry verification;
- palette compatibility;
- 32x48 reconstruction feasibility;
- portrait reconstruction feasibility;
- deviations requiring manual blueprint correction.

Only then advance asset 018 to `REFERENCE_SELECTED`.

## Prompt-ready generation specification

Create a dedicated six-view orthographic turnaround reference for NPC_TAMSIN, a recurring adult municipal systems worker in a detailed modern-retro pixel-art text RPG. Show front, front three-quarter, left profile, right profile, rear three-quarter, and back views at equal height on one ground line, neutral stance, full body visible, crisp deliberate pixel clusters, no anti-aliasing or painterly rendering, neutral consistent lighting, plain dark-neutral presentation background. Tamsin is average height with a slim athletic build, slightly long forearms and compact stance; medium warm-brown skin; dark brown eyes; short angular layered near-black hair with muted cool highlights and a heavy fringe on Tamsin's left; a small notch through the right eyebrow; charcoal municipal utility jacket with high collar over a pale work shirt; dark practical work trousers; a narrow cross-body tool satchel; right sleeve rolled **only** while the left sleeve remains visibly unrolled/full-length; small municipal systems badge on left chest; left-hip tool loop. Keep all left/right asymmetries consistent in every view. The satchel must remain a compact cross-body hip bag, never a backpack. No long hair, neon colors, armor, oversized weapons, dramatic pose, Trace effects, environment, invented text, or redesign. This is a canonical identity reference for reconstruction into 32x48 sprites and 64x64 portraits.
