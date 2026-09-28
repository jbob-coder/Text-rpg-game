# Canonical Turnaround Generation Protocol v1

## Purpose

Stop reference drift before pixel reconstruction.

This protocol applies to any character turnaround that can influence canon identity, equipment anchors, or the reusable player rig.

## Rule 1 — One canonical asset per generated image

Do **not** generate a mixed atlas when selecting a canonical turnaround.

A canonical selection image may target exactly one of:

- `PLAYER_BODYFRAME_A_TURNAROUND`;
- `NPC_TAMSIN_TURNAROUND`;
- another future named-character turnaround with its own locked brief.

Do not include:

- other characters;
- animations;
- expression sheets;
- item icons;
- equipment breakdowns;
- locations;
- maps;
- UI;
- FX;
- props.

Those can be generated after the turnaround is selected.

## Rule 2 — Selection image is a test fixture

Treat generation as a constrained test against the brief.

The candidate passes only if every hard constraint passes.

Visual attractiveness cannot compensate for:

- wrong anatomical side;
- wrong equipment side;
- missing identity mark;
- inconsistent proportions;
- identity leakage into a neutral base;
- mismatched view heights;
- missing required view.

## Rule 3 — Anatomical side verification

For front-facing characters, remember:

- subject LEFT = viewer RIGHT;
- subject RIGHT = viewer LEFT.

For every asymmetric named-character asset, the audit must explicitly record both anatomical and viewer-side position.

Example for Tamsin front view:

| Feature | Anatomical side | Front-view side |
| --- | --- | --- |
| Heavy fringe | Tamsin left | viewer right |
| Badge | Tamsin left chest | viewer right |
| Tool loop | Tamsin left hip | viewer right |
| Eyebrow notch | Tamsin right eyebrow | viewer left |
| Rolled sleeve | Tamsin right arm | viewer left |

If the image contradicts this table, reject it.

## Rule 4 — Neutral-base identity test

A reusable player body base fails if a reviewer can reasonably describe a stable character identity from it.

The player neutral turnaround should therefore have:

- bald/featureless head;
- minimal construction face;
- no distinct hairstyle;
- no facial hair;
- no scars/tattoos;
- no jewelry;
- no faction or role marker;
- plain close-fitting underlayer;
- no distinctive shoes;
- no weapon/bag/equipment.

If the candidate looks like a finished protagonist, reject it.

## Rule 5 — Six-view consistency test

Required:

1. front;
2. front three-quarter;
3. left profile;
4. right profile;
5. rear three-quarter;
6. back.

Check:

- equal apparent height;
- same shoulder width;
- same hip width;
- same head size;
- same hand size;
- same foot size;
- same clothing length;
- same hair volume;
- same accessory location;
- same ground line.

## Rule 6 — Native-grid survivability

Before selection, ask whether the design can survive reconstruction at the target grid.

For 32x48:

- silhouette must carry most identity;
- small identity marks can be portrait-only;
- no critical feature should rely on smooth anti-aliasing;
- no important garment seam should require subpixel geometry;
- left/right asymmetry must remain visible with 1–2 pixel differences.

## Rule 7 — Reference status vocabulary

- `REFERENCE_GENERATED`: exists, not approved.
- `REFERENCE_REJECTED`: failed at least one hard constraint.
- `REFERENCE_SELECTED`: passed all hard constraints for one exact asset.
- `STYLE_DIRECTION_ACCEPTED`: useful only for broad visual language.
- `CANON_GEOMETRY_REJECTED`: cannot be used as geometry authority.

A mixed sheet may be useful but cannot be `REFERENCE_SELECTED` for a canonical turnaround unless it was explicitly generated and audited as that single asset.

## Rule 8 — Failure feedback must change the next prompt

Do not simply regenerate the same prompt.

After each rejection:

1. name every failed hard constraint;
2. convert each failure into explicit positive/negative prompt language;
3. remove unrelated prompt content;
4. generate only the failed asset;
5. re-audit from zero.

## Current Wave A lesson

Boards A–D established useful style language, but the mixed-sheet approach repeatedly caused:

- player identity leakage into the neutral rig;
- Tamsin left/right fringe inversion;
- Tamsin sleeve asymmetry loss.

Therefore all future Wave A turnaround generation is single-asset only until assets 001 and 018 are selected.
