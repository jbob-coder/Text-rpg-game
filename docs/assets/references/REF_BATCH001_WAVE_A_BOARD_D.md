# Reference Audit — REF_BATCH001_WAVE_A_BOARD_D

Status: `REFERENCE_GENERATED`  
Selection result: **REJECTED for asset 001 and asset 018**  
Use: production-layout and detail-language study only

## Persisted reference

- Google Drive file: `REF_BATCH001_WAVE_A_BOARD_D.png`
- Drive file ID: `1KEnFICWT18Jb4SU5P6u-9S1vop56kEcw`
- Resolution: 1536 x 1024 PNG
- SHA-256: `bfe18b3f6a08b34fbb52778cf26bbf89497e63af438efc3c5e3cfcdfd9d6d640`
- File size: 2,536,302 bytes

## Overall result

Board D is useful as a visual-system reference but fails the two dedicated canonical-selection gates.

The repeated failure confirms a pipeline issue rather than a need for more broad mixed sheets: the generation request is carrying too many simultaneous subjects and examples. Canonical turnarounds must therefore move to **one asset per image**.

---

# Asset 001 — PLAYER_BODYFRAME_A_TURNAROUND

Decision: **REJECT**

## Passed

- six directions are presented;
- overall 32x48 body proportions are usable as a study;
- feet/hands are readable;
- the body-structure and anchor panels reinforce the intended rig idea;
- front/profile/back silhouette density is close to the desired gameplay scale.

## Failed

The locked brief requires a neutral technical construction model. Board D again introduces:

- a fixed dark hairstyle;
- a recognizable face;
- fixed eyes and expression;
- a specific shirt/shorts outfit identity;
- repeated animation sprites using the same invented identity.

That makes the reference unsuitable as the neutral reusable body authority.

## Allowed reuse

- proportional comparison;
- body-volume study;
- direction spacing;
- anchor-panel layout;
- native-detail density.

## Rejected reuse

- face;
- hair;
- clothing identity;
- any canonical player appearance.

Asset 001 remains `BRIEF_LOCKED`.

---

# Asset 018 — NPC_TAMSIN_TURNAROUND

Decision: **REJECT**

## Passed

Board D preserves several important Tamsin directions well:

- slim athletic build;
- compact stance;
- warm-brown skin family;
- near-black hair family;
- high utility collar;
- charcoal jacket / pale shirt / dark trousers relationship;
- left-chest badge reads clearly;
- compact cross-body satchel remains a hip bag rather than a backpack;
- left-hip tool-loop concept is visible;
- full-body views are consistently scaled;
- portrait family is internally coherent;
- pixel density is reconstructable.

## Critical identity failures

### A. Heavy fringe remains on the wrong anatomical side

Locked contract:
- heavy fringe = **Tamsin anatomical LEFT**.

For a front-facing Tamsin:
- anatomical LEFT = **viewer RIGHT**.

Board D:
- dominant fringe mass again falls on **viewer LEFT** in the front view;
- viewer LEFT corresponds to Tamsin anatomical RIGHT.

Result:
- direct left/right identity inversion.

### B. Sleeve asymmetry is still not clean enough

Locked contract:
- Tamsin anatomical RIGHT sleeve is rolled;
- anatomical LEFT sleeve remains visibly unrolled/full-length.

For a front-facing Tamsin:
- right sleeve = **viewer LEFT**;
- left sleeve = **viewer RIGHT**.

Board D:
- both sleeves read as shortened/rolled in the front-facing presentation;
- the required one-sleeve asymmetry is therefore lost.

Result:
- direct identity-anchor failure.

## Supporting caution

The detail panel labels the intended features correctly, but labels do not override the pixels. Selection is based on what the character actually depicts.

## Allowed reuse

- jacket material/value language;
- collar;
- badge scale;
- satchel scale;
- trouser/boot density;
- expression intensity;
- overall full-body pixel density.

## Rejected reuse

- fringe geometry;
- sleeve geometry;
- direct canonical pixel reconstruction;
- promotion to `REFERENCE_SELECTED`.

Asset 018 remains `BRIEF_LOCKED`.

---

# Pipeline conclusion

Broad atlas-style generation is no longer acceptable for canonical character selection.

Starting with the next candidate:

1. generate **PLAYER_BODYFRAME_A_TURNAROUND alone**;
2. review/select/reject it;
3. separately generate **NPC_TAMSIN_TURNAROUND alone**;
4. review/select/reject it;
5. do not request animations, expressions, items, locations, UI or effects in the same image;
6. only after a turnaround passes may derivative animation/portrait/equipment references be generated.

This reduces prompt competition and makes left/right consistency measurable.

## Classification

`REFERENCE_GENERATED -> PRODUCTION_LAYOUT_ACCEPTED -> DETAIL_LANGUAGE_ACCEPTED -> PLAYER_SELECTION_REJECTED -> TAMSIN_SELECTION_REJECTED`

No Wave A turnaround asset advances state from Board D.
