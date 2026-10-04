# THE GAME — Character Pixel Blueprints v1

This document defines the production blueprints for the visible player-character system and the first recurring NPC, `NPC_TAMSIN`.

The current Compose block avatar is a runtime placeholder. The following specification defines the replacement source-art system.

---

## No-geometric-character-art rule

Character visuals must **not** be constructed from procedural rectangles, circles, polygons, vector primitives, block-figure geometry, or other geometric drawing logic as the final character art.

The production character is an authored pixel-art asset generated through the project art workflow, then extracted/reconstructed, cleaned, layered, and animated as real sprite/portrait assets.

Coordinates, pivots, bounding boxes, body-part anchors, occupied pixel ranges, and attachment points in this document are **measurement and alignment metadata only**. They define where finished pixel-art layers line up; they are not instructions to draw the human figure from geometry.

Temporary historical block/procedural avatars may remain only as migration/debug fallbacks until the authored sprite replacement is integrated. They must never be treated as the final visual method for Jack, Tamsin, supporting NPCs, enemies, or other characters.

# 1. Player Character — Reusable Paper-Doll Master

## 1.0 Player identity authority update — Jack Wilson

The earlier v1 blueprint described the first player master as a technically generic/customizable body-frame because no approved fixed visual identity had yet been available on that branch.

That assumption is now superseded for the current player presentation by the owner-approved reference:

- reference ID: `UI_REFERENCE_CHARACTER_APPROVED_V1`;
- scope: Jack Wilson Character-tab visual identity/presentation;
- durable reference audit: `docs/assets/references/UI_REFERENCE_CHARACTER_APPROVED_V1.md`;
- reference source is not itself a runtime sprite.

### Locked consequence

The 32x48 rig, pivots, equipment anchors, paper-doll separation and source-native pixel rules below remain valid technical contracts.

The **visual identity target is no longer generic**. Future player gameplay sprites, portraits, Character panels, equipment-aligned silhouettes and animation masters must preserve Jack Wilson's approved identity and the approved reference's human-readable non-chibi proportions, hair/face silhouette and layered-clothing/equipment presentation.

### What the approved reference does not decide

It does not define:
- gameplay statistics;
- inventory/equipment legality;
- hidden state;
- collision/hitboxes;
- exact unseen turnaround views;
- exact 32x48 anchor positions;
- animation timing.

Those remain governed by the engine and this technical blueprint.

### Migration rule

Any older generic player placeholder may remain as a fallback until a replacement is integrated and verified, but it must not be treated as the final visual identity. New art must not regenerate Jack from prose memory when the approved reference is available.


## 1.1 Role

The player must remain visually present in the primary gameplay screen and Character screen. The visual is a projection of authoritative identity/equipment/status state.

The player art system must support:

- persistent identity;
- equipment changes without redrawing the whole character;
- future body/hair/skin variants;
- status/injury overlays;
- ability effects;
- idle and future movement animation;
- reuse in portrait, equipment and scene contexts.

## 1.2 Native gameplay grid

- canvas: 32x48 pixels;
- transparent background;
- ground pivot: x=16, y=47;
- recommended occupied bounds: x=3..28, y=2..46;
- minimum 2-pixel breathing room around ordinary silhouette;
- weapons/FX may extend into a documented overscan cell rather than changing body proportions.

## 1.3 Base body proportions

Initial neutral body-frame A:

- total visible height: 44 pixels;
- head: 11–12 px high;
- neck: 2 px;
- shoulder span: 16–18 px;
- torso: 14–15 px high;
- pelvis: 5–6 px high;
- upper leg: 8–9 px;
- lower leg/foot: 8–9 px;
- hand mass: 3–4 px;
- forearm: 7–8 px.

The body must read as an adult human, not chibi and not a smooth-painting miniature. The head-to-height ratio should stay near 1:4 at gameplay scale.

## 1.4 Base-body layers

Required source layers:

1. shadow;
2. rear arm;
3. rear leg;
4. torso/neck;
5. front leg;
6. front arm;
7. head/ears;
8. facial pixels;
9. rear hair;
10. front hair;
11. optional skin marks;
12. paper-doll occlusion masks.

The base body contains no permanent armor.

## 1.5 Identity customization architecture

The current content does not yet define a canonical fixed player face. Therefore the first production player is a **system master**, not a fixed story identity.

Identity-compatible layers:

- body frame;
- skin palette;
- face cluster;
- hair back;
- hair front;
- eyebrow/mark layer;
- optional facial-hair layer;
- identity accessory layer.

Future character creation can swap these layers without changing equipment anchors.

## 1.6 Skin palette construction

Each skin set uses a minimum of:

- highlight;
- base;
- mid shadow;
- deep shadow;
- optional warm/cool accent.

Skin ramps must be tested against the dark UI background and against cyan/gold equipment accents.

## 1.7 Hair construction

Hair is split into rear and front masks.

Requirements:

- silhouette must identify the hairstyle before internal highlight pixels are added;
- highlights occupy coherent clusters, not single-pixel noise;
- front fringe may occlude forehead but not the eye cluster unless explicitly authored;
- helmets can hide front/rear hair through mask metadata;
- asymmetrical hair must receive left/right directional variants.

## 1.8 Face at gameplay scale

At 32x48, facial design is intentionally minimal:

- eye line: 1–2 pixel clusters;
- brow/mark: 1 px or 2 px cluster;
- nose: optional 1 px shadow;
- mouth: 1–2 px;
- no anti-aliased lips/eyelashes;
- emotion is communicated mainly through brow/eye/mouth placement plus head posture.

Detailed facial acting belongs in 64x64 portraits.

## 1.9 Equipment anchors

All wearable/held layers align to the same 32x48 cell.

Stable anchors:

- head center: (16,8)
- neck: (16,13)
- left shoulder: (10,15)
- right shoulder: (22,15)
- chest center: (16,20)
- waist: (16,28)
- left wrist: (6,32)
- right wrist: (26,32)
- left foot: (11,46)
- right foot: (21,46)
- main hand: (27,31)
- off hand: (5,31)

Wearable art must not move these anchors.

## 1.10 Equipment occlusion rules

- chest armor can cover torso/base shirt but not automatically arms;
- gloves cover hand pixels and may cover lower forearm;
- leg equipment can cover pelvis/upper legs according to mask;
- footwear covers the final 5–7 vertical pixels;
- neck items render over shirt and under most chest armor collars unless metadata says otherwise;
- rings are micro accents and may be represented only when the hand is large enough at the current view;
- accessories may exist behind or in front of the body based on explicit z-layer;
- main/off-hand items never erase the base hand; they use a grip mask.

## 1.11 Player six-view reference board

The non-shipping reference board must show:

1. front;
2. front three-quarter;
3. left profile;
4. right profile;
5. rear three-quarter;
6. back.

Each view must maintain:

- same apparent height;
- same shoulder/hip proportions;
- same hair volume;
- same equipment anchor heights;
- same foot length;
- same hand scale.

This board is used to reverse engineer directional pixel masters.

## 1.12 Gameplay animation blueprint

### Idle — 4 frames
- frame 1: neutral;
- frame 2: chest/shoulder +1 px breathing shift;
- frame 3: neutral;
- frame 4: subtle opposite shift.

No whole-body bob greater than 1 px.

### Walk — 6 frames per direction
- contact;
- down;
- passing;
- opposite contact;
- opposite down;
- opposite passing.

Feet must visibly alternate; equipment follows anchor motion without sliding.

### Run — 8 frames per direction
Stronger lean and arm swing; retain readable paper-doll masks.

### Crouch
- 2-frame entry;
- 2-frame hold loop;
- 2-frame exit.

### Interact/tool use
4–6 frames using stable hand/tool anchors.

### Hurt/recovery
3–4 frames; injury state is not encoded solely in animation because conditions persist.

### Trace Echo activation
6–8 body frames or 4 body frames plus independent FX sheet.

## 1.13 Status overlays

Status art is separate from body/equipment:

- minor injury: small localized mark;
- major injury: stronger overlay and posture modifier;
- Trace strain: cyan-violet edge/pulse layer;
- low health: UI feedback first; do not permanently recolor the body;
- hidden conditions must not get a player-visible visual before the engine makes them visible.

---

# 2. Player Portrait System

## 2.1 Native portrait grid

- 64x64 pixels;
- bust crop;
- transparent or location-neutral backdrop;
- head center around x=32, y=23;
- shoulders occupy bottom 20–24 px.

## 2.2 Approved baseline expression family

For a customizable player, initial expression templates are:

- neutral;
- focused;
- concerned;
- hurt;
- determined;
- surprised.

These are expression/pose layout references, not geometric construction and not a fixed face identity.

## 2.3 Portrait-to-gameplay consistency

Portrait and gameplay sprite must share:

- skin palette family;
- hair silhouette;
- identity marks;
- visible head/neck equipment;
- injury/status state;
- dominant outfit color.

---

# 3. NPC_TAMSIN — Canonical Visual Blueprint

## 3.1 Source-backed identity

Stable ID: `NPC_TAMSIN`

Current authored identity:

- height class: average;
- build: slim athletic adult;
- body proportion anchors: long forearms, compact stance;
- skin: medium warm brown;
- hair: angular layered crop, short, heavy left-side fringe;
- hair palette: near-black with muted cool highlights;
- eyes: dark brown;
- default outfit: charcoal municipal utility jacket, pale work shirt, dark work trousers;
- silhouette anchors:
  - high utility-jacket collar;
  - narrow cross-body tool satchel;
  - rolled right sleeve;
- role marker: small municipal systems badge on left chest;
- attachment points:
  - left hip tool loop;
  - cross-body satchel strap;
- permanent mark: small notch through right eyebrow;
- forbidden deviations:
  - no long hair;
  - no saturated neon clothing;
  - eyebrow notch must remain;
  - satchel must not become a backpack.

Authored palette anchors:

- jacket: #30343B
- shirt: #C9C7BE
- trousers: #24272C
- skin shadow: #8B5F4B

## 3.2 Tamsin gameplay grid

- 32x48;
- same global player rig envelope so shared animation tooling can be reused;
- slightly narrower shoulder silhouette than player body-frame A;
- forearms visually 1 px longer than neutral template;
- stance: feet closer together, center of mass compact.

## 3.3 Tamsin silhouette priorities

A black silhouette should still suggest Tamsin through:

1. asymmetric heavy left fringe;
2. high jacket collar;
3. diagonal narrow satchel strap;
4. small satchel mass near hip;
5. right sleeve ending higher because it is rolled.

The eyebrow notch is a close-range identity marker, not a silhouette feature.

## 3.4 Tamsin hair blueprint

Front:
- asymmetrical top volume;
- left fringe extends 2–3 px lower than right;
- crown remains compact;
- sideburn area short.

Profile:
- angular back contour;
- fringe projects forward;
- no ponytail/bun.

Back:
- cropped nape;
- cool highlight cluster remains sparse.

## 3.5 Tamsin clothing blueprint

Utility jacket:

- charcoal base;
- high collar;
- left chest badge;
- right sleeve rolled;
- subtle seam/pocket clusters;
- no bright fashion trim.

Pale work shirt:

- visible at center collar/upper chest;
- lower value contrast than UI Paper so it does not look emissive.

Trousers:

- dark neutral;
- practical cut;
- no oversized armor silhouette.

Satchel:

- narrow cross-body strap from shoulder to opposite hip;
- compact tool satchel, not backpack;
- strap must remain visible in front/three-quarter views.

## 3.6 Tamsin equipment anchors

- badge anchor: left chest, approximately (12,19) on front sprite;
- satchel shoulder anchor: (21,15);
- satchel hip anchor: (10,29);
- tool loop: left hip, approximately (9,29);
- diagnostic reader held between hands in authored tool pose.

## 3.7 Tamsin portrait master

64x64.

Identity requirements:

- right eyebrow notch visible in neutral/focused/concerned/angry/relieved portraits;
- heavy left fringe consistent in all expressions;
- eye color only represented when pixel budget allows;
- high collar appears at lower portrait edge;
- badge may appear if crop includes left chest;
- no expression changes hairstyle shape.

## 3.8 Tamsin emotion sheet

Five authored expressions:

### Neutral
- level brow except notch;
- closed/relaxed mouth;
- direct but not confrontational gaze.

### Focused
- inner brows slightly lowered;
- eye cluster narrowed by 1 px;
- mouth neutral;
- head angle slightly forward.

### Concerned
- inner brows raised;
- mouth corner slight downturn;
- eyes more open;
- shoulders may lift subtly.

### Angry
- brow angle downward toward center;
- reduced eye opening;
- jaw/mouth line firmer;
- do not exaggerate into cartoon rage.

### Relieved
- brow relaxes;
- eye line softens;
- slight upward mouth corner;
- shoulders lower.

## 3.9 Tamsin pose sheet

Authored poses:

- front;
- profile;
- three-quarter;
- holding diagnostic reader.

Production expands this into six-view turnaround while preserving the authored pose set as the allowed story-facing vocabulary.

## 3.10 Tamsin diagnostic-reader pose

Reader is a separate prop layer.

Pose rules:

- elbows close to torso;
- left hand supports device;
- right hand operates controls;
- satchel strap remains readable;
- badge not covered if possible;
- reader cyan accents may reflect lightly on lower face/hands, but must not recolor skin globally.

---

# 4. Supporting Wounded Courier

The opening scene describes a conscious maintenance courier who cannot carry the relay farther.

This character is a supporting visual, not yet a stable named NPC.

Production rules:

- ID for art pipeline: `SUPPORT_COURIER_01`;
- adult municipal maintenance silhouette;
- workwear distinct from Tamsin;
- visible injury posture without graphic gore;
- relay/courier relationship readable;
- should not accidentally imply a named recurring identity;
- portrait not required in Batch 001 unless dialogue is later added.

---

# 5. Generated Reference Requirements

A generated character reference request must specify:

- exact stable ID;
- reference-only status;
- six required views;
- native pixel target that will be reconstructed;
- body proportions;
- silhouette anchors;
- palette anchors;
- clothing/materials;
- equipment anchors;
- permanent marks;
- forbidden deviations;
- neutral flat lighting;
- no background clutter;
- no perspective lens distortion;
- no text embedded in image;
- no anti-aliased detail relied upon for identity.

The selected reference becomes an input to the pixel blueprint; it does not become the final sprite.

---

# 6. Character Acceptance Checklist

For every player/NPC master:

- [ ] six-view reference complete;
- [ ] silhouette readable at 1x;
- [ ] 32x48 front master complete;
- [ ] left/right asymmetry checked;
- [ ] anchor coordinates verified;
- [ ] equipment masks verified;
- [ ] portrait identity matches gameplay sprite;
- [ ] palette count within budget;
- [ ] no accidental anti-aliasing;
- [ ] nearest-neighbor scaling verified in Android;
- [ ] hidden state is not leaked by art;
- [ ] source/reference/blueprint lineage documented.

