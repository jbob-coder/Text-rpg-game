# L0-03 — Native Grid and Anchor Standard

Layer: **L0 Foundation**
Depends on: L0-02 (angle standard)
Sources: `docs/assets/PIXEL_ASSET_MASTER_PLAN.md` §3, §6; `docs/assets/CHARACTER_PIXEL_BLUEPRINTS.md` §1.2, §1.9

> **Authority note.** The anchor table below is transcribed from
> `PIXEL_ASSET_MASTER_PLAN.md` §6 and is numerically identical. It is restated
> here so that every asset specification in this corpus can reference one table.

---

## 1. Native grid hierarchy

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

### 1.1 Compatibility note

The existing Android client uses an **18x30 logical avatar** and a **64x32
procedural scene grid**. These are implementation placeholders, not final
source-art resolution. The replacement system preserves UI readability while
moving source art to the grids above.

This means a rebuild must **not** assume 18x30 is the character grid. 18x30 is a
rendering compromise of a previous attempt; 32x48 is the contract.

## 2. The 32x48 character cell
The 32x48 cell is the most-used grid in the game: it carries the player base,
every NPC body, every equipment paper-doll layer and every character overlay.
Getting it right once here makes hundreds of downstream assets correct; getting
it wrong makes hundreds of assets consistently wrong.

### 2.1 Canvas

- canvas: 32 wide x 48 high pixels;
- format: RGBA;
- background: transparent;
- coordinates: zero-based `x,y`, `x` rightward, `y` downward, origin at
  **top-left**;
- occupied bounds target: `x=3..28`, `y=2..46`;
- minimum 2-pixel breathing room around the ordinary silhouette;
- weapons/FX may extend into a documented overscan cell rather than changing
  body proportions.

### 2.2 Ground pivot

`pivot = (16, 47)`

This is the point that touches the ground line. It is **not** the bottom of the
art. Pixel row 47 is the ground contact; art occupies up to roughly row 46.

## 3. The canonical anchor table

These are the pipeline-default anchors. A body-frame variant may move them only
through a versioned character rig specification.

| # | Anchor | Coordinate |
| ---: | --- | --- |
| 1 | pivot / ground | `(16, 47)` |
| 2 | head center | `(16, 8)` |
| 3 | neck | `(16, 13)` |
| 4 | left shoulder | `(10, 15)` |
| 5 | right shoulder | `(22, 15)` |
| 6 | left elbow | `(7, 24)` |
| 7 | right elbow | `(25, 24)` |
| 8 | left wrist | `(6, 32)` |
| 9 | right wrist | `(26, 32)` |
| 10 | pelvis | `(16, 28)` |
| 11 | left knee | `(12, 37)` |
| 12 | right knee | `(20, 37)` |
| 13 | left foot anchor | `(11, 46)` |
| 14 | right foot anchor | `(21, 46)` |
| 15 | main-hand attachment | `(27, 31)` |
| 16 | off-hand attachment | `(5, 31)` |
| 17 | neck item anchor | `(16, 14)` |
| 18 | belt/accessory anchor | `(16, 28)` |

### 3.1 Naming convention trap

`left shoulder = (10,15)` means the **subject's** left shoulder. Because the
front view is inverted relative to the viewer, in a front-facing sprite the
subject's left shoulder appears at the **viewer's right**, i.e. at greater x.

This is the mechanical reason behind the L0-02 §2.2 inversion rule. Confusing
subject-side with screen-side is the most common anchor bug.

### 3.2 Anchor visibility

Not every anchor is observable in every view. For `L_PROFILE` and `R_PROFILE`,
the shoulder and hip anchors collapse toward the body centreline and the
wrist/hand anchors project to the visible edge. An anchor being *occluded* in a
profile view is correct and must not be "fixed" by moving it.

## 4. Body proportion contract (body-frame A)

Target proportions when reduced to 32x48:

| Measure | Target |
| --- | --- |
| total visible height | 44 px |
| head | 11–12 px high |
| neck | 2 px |
| shoulder span | 16–18 px |
| torso | 14–15 px high |
| pelvis | 5–6 px high |
| upper leg | 8–9 px |
| lower leg/foot | 8–9 px |
| hand mass | 3–4 px |
| forearm | 7–8 px |
| head-to-height ratio | **~1:4** |
| top empty margin | 2 px |
| head box target | `x=11..21`, `y=2..12` |
| shoulder span target | `x=8..24` around `y=15` |
| torso mass | `y=14..28` |
| pelvis center | `(16,28)` |
| knees | left `(12,37)`, right `(20,37)` |
| feet | left `(11,46)`, right `(21,46)` |

### 4.1 Proportion prohibitions

- no chibi head enlargement;
- no hyper-muscular or fashion-model exaggeration;
- no smooth-painting miniature treatment;
- the body must read as an **adult human**.

## 5. The front-base cluster map

The first-pass silhouette envelope for `PLAYER_GAMEPLAY_FRONT_BASE`. Edge pixels
may be sculpted inside these envelopes, but the anchor geometry must remain
stable.

### 5.1 Head / neck

| Region | Box |
| --- | --- |
| head main envelope | `x=11..20, y=3..11` |
| forehead/temple allowance | `x=10..21, y=4..8` |
| left ear envelope | `x=9..10, y=6..9` |
| right ear envelope | `x=21..22, y=6..9` |
| neck | `x=14..17, y=12..14` |

### 5.2 Torso

| Region | Box |
| --- | --- |
| shoulder line envelope | `x=8..23, y=14..17` |
| upper torso | `x=10..21, y=15..22` |
| lower torso | `x=11..20, y=22..28` |
| pelvis | `x=11..20, y=27..31` |

### 5.3 Arms

| Region | Left | Right |
| --- | --- | --- |
| upper arm | `x=7..10, y=16..23` | `x=21..24, y=16..23` |
| forearm | `x=6..9, y=23..31` | `x=22..25, y=23..31` |
| hand | `x=5..8, y=31..34` | `x=23..26, y=31..34` |

### 5.4 Legs / feet

| Region | Left | Right |
| --- | --- | --- |
| thigh | `x=11..15, y=30..37` | `x=17..21, y=30..37` |
| lower leg | `x=10..14, y=37..44` | `x=18..22, y=37..44` |
| foot | `x=8..14, y=44..46` | `x=18..24, y=44..46` |

## 6. Paper-doll z-order

The authoritative layer order. A rebuild composes from bottom of this list up.

| z | Layer |
| ---: | --- |
| 1 | ground shadow |
| 2 | back accessory / cape / pack |
| 3 | rear hair |
| 4 | base legs |
| 5 | footwear |
| 6 | base torso |
| 7 | arm-under layers |
| 8 | chest equipment |
| 9 | leg equipment |
| 10 | neck layer |
| 11 | head base |
| 12 | hair / front facial features |
| 13 | head equipment |
| 14 | hands / gloves |
| 15 | main-hand item |
| 16 | off-hand item |
| 17 | front accessory |
| 18 | injury/status overlay |
| 19 | ability/FX overlay |

### 6.1 Base-body layer order (alternative decomposition)

Where a body-frame master is authored as separate layers rather than one
composited sprite:

1. shadow
2. rear arm
3. rear leg
4. torso/neck
5. front leg
6. front arm
7. head/ears
8. facial pixels
9. rear hair
10. front hair
11. optional skin marks
12. paper-doll occlusion masks

### 6.2 The base body contains no permanent armor

Stated explicitly in `CHARACTER_PIXEL_BLUEPRINTS.md` §1.4. A base body that
bakes in chest, leg or head equipment cannot support the paper-doll system and
is a reconstruction error.

## 7. Non-character native grids
Five grid families cover everything that is not a 32x48 character. Each has its
own density target and its own readability requirement.

### 7.1 Item icons — 32x32

- canvas 32x32 RGBA, transparent;
- target occupied bounds typically `x=4..27, y=4..27`;
- visual centre approximately `(16,16)`;
- maximum 6–8 colours for icons, 6–12 for items;
- icon art must be separable from paper-doll art.

### 7.2 Portraits — 64x64

- canvas 64x64;
- bust crop;
- transparent or location-neutral backdrop;
- head centre around `x=32, y=23`;
- shoulders occupy bottom 20–24 px;
- 12–24 colour budget.

### 7.3 Scenes — 128x64

Each scene sheet records:

- location ID;
- dominant perspective;
- horizon/ground line;
- light source and colour temperature;
- material palette;
- permanent architecture;
- temporary story-state overlays;
- interactable landmarks;
- **safe text/UI crop zones**;
- alternate-state triggers.

The safe crop zone is a hard requirement, not a nicety: narrative UI overlays
the scene and text must stay legible.

### 7.4 Micro icons — 16x16

Map markers, status marks, HUD icons. Must remain readable at micro scale and,
for accessibility icons, must be distinguishable **without relying on colour
alone**.

### 7.5 Navigation icons — 24x24

Bottom navigation identity icons: Story, Character, Stats, Inventory, Quests,
Map, More/Settings.

## 8. Global pixel rules

1. No anti-aliasing inside shipped raster assets.
2. No fractional-pixel placement.
3. Do not scale source art with bilinear/bicubic filtering.
4. Maximum local palette: icon 4–8; item 6–12; gameplay character/layer 8–16;
   portrait 12–24; scene 16–32.
5. One dominant light direction per location set.
6. Silhouette must remain readable at 1x native size.
7. Materials require distinct value ramps — metal, cloth, skin, glass and
   powered surfaces must not share identical ramps.
8. Transparency is binary for ordinary sprite edges unless a documented FX layer
   requires graded alpha.
9. Dithering is deliberate and sparse; never noise as a substitute for material
   design.
10. Pixel clusters are designed, not produced by applying a pixelation filter.

### 8.1 Verified corpus evidence

The 24 existing runtime rasters were decoded and audited during corpus
construction. Every one shows **zero partial-alpha pixels**, confirming the
binary-transparency rule is currently honoured in the repository.

| Class | Files | Alpha profile | Distinct colours |
| --- | ---: | --- | ---: |
| 128x64 scenes | 9 | fully opaque, no transparency | 9–12 |
| 32x32 item icons | 8 | binary | 5–9 |
| 32x48 paper-doll/character | 6 | binary | 3–11 |
| Total | 24 | 0 partial-alpha pixels | — |

Note the scenes are fully opaque and use only 9–12 distinct colours, well inside
the 16–32 scene budget. Two scene rasters (`pixel_relay_workbench_default_scene`,
`pixel_platform_nine_blackout_scene`) are much smaller in file size than the
other seven, which is consistent with sparser/compressible pixel content rather
than placeholder emptiness — all nine are unique by hash and share no duplicate
content.

## 9. Visual form classification

Three visual types coexist during migration. Every asset specification must
declare which one it is.

### Type A — Source-native authored raster
Preferred shipping form when available.

### Type B — Source-native PixelSprite/text-map definition
Acceptable production form **if intentionally authored and visually approved**.
Not inferior merely because pixel rows are represented in code.

### Type C — Procedural geometric fallback
Migration-only fallback for non-character presentation where no authored asset
exists.

### 9.1 Character-specific prohibition

Procedural geometry is **not** an acceptable final rendering path for
characters. Jack, Tamsin, recurring NPCs, supporting actors and other character
identities must use authored pixel-art sprite/portrait assets.

Rig anchors, pivots and bounds are **metadata for sprite placement, equipment and
animation only**. They do not authorise drawing the character from rectangles,
circles, polygons or other primitives.

A historical block avatar may survive temporarily for debugging or migration
safety, but it is explicitly a placeholder scheduled for replacement.

### 9.2 Replacement priority

1. generic block character
2. generic scene geometry
3. flat map blocks
4. technical placeholder icons
5. only then lower-value decorative placeholders

### 9.3 Verified current classification

Audit performed during corpus construction found:

- **24 authored rasters** present as PNG resources (Type A), all in
  `android/app/src/main/res/drawable-nodpi/`;
- **9 named-location scene masters** additionally defined as Type B
  PixelSprite/text-map definitions in `PixelSceneCatalog.kt`, each 128x64 with an
  explicit character-keyed palette and 128-row text rows;
- character presentation partially migrated — the player front base exists as an
  authored raster while hair remains explicitly named
  `pixel_player_hair_tech_placeholder.png`.

Where both Type A and Type B definitions exist for the same location ID, the
precedence rule in `ROOM_COMPOSITION_IMPLEMENTATION_CONTRACT.md` §5 applies and
must be recorded per asset.

## 10. Naming and file layout
Three filename conventions coexist by design: the documentation/planning
pattern for production masters, the `REF_` prefix for references, and the
Android resource convention for shipped drawables.

### 10.1 Filename pattern

```
<stable_id>__<family>__<view_or_state>__vNN.png
```

Examples:

- `NPC_TAMSIN__portrait__focused__v01.png`
- `ITEM_DEPOT_JACKET__paperdoll__front__v01.png`
- `PLATFORM_NINE__scene__blackout__v01.png`
- `TRACE_ECHO__fx__signal_pulse__v01.png`

### 10.2 Reference images

Reference images use the `REF_` prefix and **never occupy a production asset
path**.

### 10.3 Runtime resource naming

Android drawables use lowercase snake case with a `pixel_` prefix, matching the
resource name (for example `pixel_item_depot_jacket_icon`). The runtime
resource filename is **not** sufficient identity — the stable asset ID from
L0-05 governs.

### 10.4 Layer filename convention for Wave A

Wave A uses a `__<layer>__` form:

- `PLAYER_GAMEPLAY_FRONT_BASE__body_mask__v01.png`
- `PLAYER_GAMEPLAY_FRONT_BASE__skin_mask__v01.png`
- `PLAYER_GAMEPLAY_FRONT_BASE__underlay__v01.png`
- `PLAYER_GAMEPLAY_FRONT_BASE__anchors__v01.json`

The body mask lets future palette variants change identity without repainting
equipment. The anchors file makes the L0-03 §3 table machine-readable for the
asset rather than inherited from documentation.