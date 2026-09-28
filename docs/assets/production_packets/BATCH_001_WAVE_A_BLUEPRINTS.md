# Batch 001 — Production Wave A Reconstruction Pack

Wave: `B001-WAVE-A`  
Assets: `001, 002, 018, 021, 022`  
Purpose: validate the complete reference -> blueprint -> native pixel master -> paper-doll integration pipeline before mass asset production.

## Shared rules

- Reference imagery is not shipped.
- Native masters use hard pixel edges and transparent backgrounds where applicable.
- No anti-aliasing.
- No fractional placement.
- All coordinates use zero-based `x,y` inside the declared canvas.
- Character paper-doll layers share the 32x48 rig and pivot `(16,47)`.
- Equipment state comes from the authoritative player-safe equipment projection.
- Any generated result that conflicts with this packet is rejected rather than silently changing the packet.

---

# 001 — PLAYER_BODYFRAME_A_TURNAROUND

Status target after first generation: `REFERENCE_SELECTED`

## Function

This is the neutral six-view construction reference for the reusable player body system. It does not define a permanent player face, hairstyle, skin tone or outfit.

## Reference-board canvas

Recommended generation board:

- overall: 1536x1024 or larger;
- six equal view panels;
- flat neutral background;
- orthographic/turnaround presentation;
- no dramatic perspective;
- no weapon;
- no equipment;
- close-fitting neutral underlayer only so anatomy can be reconstructed.

## Required views

1. front;
2. front three-quarter;
3. left profile;
4. right profile;
5. rear three-quarter;
6. back.

## Locked proportion contract

When reduced to 32x48:

- occupied height: 44 px target;
- top empty margin: 2 px;
- bottom/pivot: y=47;
- head box target: x=11..21, y=2..12;
- shoulder span target: x=8..24 around y=15;
- torso mass: y=14..28;
- pelvis center: `(16,28)`;
- knees: left `(12,37)`, right `(20,37)`;
- feet: left anchor `(11,46)`, right `(21,46)`;
- adult readable proportion near 1 head : 4 total body height;
- no chibi head enlargement;
- no hyper-muscular or fashion-model exaggeration.

## What the reference is allowed to decide

- subtle neutral anatomy transitions;
- elbow/knee volume;
- side-profile chest/back depth;
- natural hand/foot silhouette inside the fixed envelope.

## What the reference is not allowed to decide

- permanent player identity;
- hair;
- scars;
- clothing;
- equipment;
- role/faction;
- story background;
- ability effects.

## Selection test

Reject if any of the six views:

- changes apparent height by more than a small reconstruction tolerance;
- changes shoulder/hip proportions;
- uses perspective foreshortening;
- relies on anti-aliased anatomy that cannot be represented at 32x48;
- creates inconsistent hand/foot scale.

---

# 002 — PLAYER_GAMEPLAY_FRONT_BASE

Status target after reconstruction: `PIXEL_MASTER_BUILT`

## Canvas

- 32x48 RGBA
- transparent background
- pivot: `(16,47)`
- occupied target bounds: x=6..25, y=2..46

## Semantic palette

The base master should use semantic color slots rather than locking one player skin tone:

- `SKIN_HI`
- `SKIN_BASE`
- `SKIN_MID`
- `SKIN_DEEP`
- `UNDERLAY_BASE`
- `UNDERLAY_SHADOW`
- `OUTLINE_DEEP`

A later identity palette maps the skin tokens to approved colors.

## Reconstructable cluster map

The following boxes define the first-pass silhouette. Edge pixels may be sculpted inside these envelopes, but the anchor geometry must remain stable.

### Head / neck

- head main envelope: x=11..20, y=3..11
- forehead/temple allowance: x=10..21, y=4..8
- left ear envelope: x=9..10, y=6..9
- right ear envelope: x=21..22, y=6..9
- neck: x=14..17, y=12..14

### Torso

- shoulder line envelope: x=8..23, y=14..17
- upper torso: x=10..21, y=15..22
- lower torso: x=11..20, y=22..28
- pelvis: x=11..20, y=27..31

### Arms

Left:
- upper arm: x=7..10, y=16..23
- forearm: x=6..9, y=23..31
- hand: x=5..8, y=31..34

Right:
- upper arm: x=21..24, y=16..23
- forearm: x=22..25, y=23..31
- hand: x=23..26, y=31..34

### Legs / feet

Left:
- thigh: x=11..15, y=30..37
- lower leg: x=10..14, y=37..44
- foot: x=8..14, y=44..46

Right:
- thigh: x=17..21, y=30..37
- lower leg: x=18..22, y=37..44
- foot: x=18..24, y=44..46

## Required anchors

- ground: `(16,47)`
- head center: `(16,8)`
- neck: `(16,13)`
- left shoulder: `(10,15)`
- right shoulder: `(22,15)`
- left elbow: `(7,24)`
- right elbow: `(25,24)`
- left wrist: `(6,32)`
- right wrist: `(26,32)`
- waist: `(16,28)`
- left knee: `(12,37)`
- right knee: `(20,37)`
- left foot: `(11,46)`
- right foot: `(21,46)`
- main hand: `(27,31)`
- off hand: `(5,31)`

## Base-body layer output

Required outputs:

- `PLAYER_GAMEPLAY_FRONT_BASE__body_mask__v01.png`
- `PLAYER_GAMEPLAY_FRONT_BASE__skin_mask__v01.png`
- `PLAYER_GAMEPLAY_FRONT_BASE__underlay__v01.png`
- `PLAYER_GAMEPLAY_FRONT_BASE__anchors__v01.json`

The body mask lets future palette variants change identity without repainting equipment.

## Native-scale QA

At 1x:

- head must remain human-readable;
- hands must be distinct from forearms;
- left/right feet must not merge;
- torso must leave enough room for chest equipment;
- shoulder/hand anchors must line up with paper-doll templates;
- silhouette must remain clear against `PixelColors.Deep`.

---

# 018 — NPC_TAMSIN_TURNAROUND

Status target after first Tamsin generation: `REFERENCE_SELECTED`

## Canon authority

This asset must follow the authored `NPC_TAMSIN` record, not the broad Batch 001 concept board.

## Six views

1. front;
2. front three-quarter;
3. left profile;
4. right profile;
5. rear three-quarter;
6. back.

## Locked identity

- average height;
- slim athletic adult;
- long forearms;
- compact stance;
- medium warm-brown skin;
- dark brown eyes;
- short angular layered crop;
- heavy **left-side** fringe;
- near-black hair with muted cool highlights;
- charcoal municipal utility jacket;
- pale work shirt;
- dark work trousers;
- high utility-jacket collar;
- narrow cross-body tool satchel;
- rolled **right** sleeve;
- small municipal systems badge on **left chest**;
- left hip tool loop;
- small notch through **right eyebrow**.

## Locked palette anchors

- jacket: `#30343B`
- shirt: `#C9C7BE`
- trousers: `#24272C`
- skin shadow: `#8B5F4B`

Additional highlight/deep colors may be derived, but these anchors must remain recognizable in the reconstructed palette.

## Asymmetry contract

Never mirror these details incorrectly:

- fringe is heavier on Tamsin's left;
- right sleeve is rolled;
- eyebrow notch is on Tamsin's right eyebrow;
- badge is on left chest;
- satchel strap and hip bag must follow a consistent shoulder-to-opposite-hip path;
- left hip tool loop remains distinct from satchel mass.

## Forbidden deviations

- no long hair;
- no backpack;
- no neon-saturated outfit;
- no removal of eyebrow notch;
- no switching rolled sleeve side;
- no changing badge side;
- no bulky armored silhouette;
- no glamour/fashion redesign that removes utility-worker readability.

## 32x48 reconstruction targets

Tamsin uses the same global rig envelope but modifies silhouette:

- shoulder span target: x=9..23;
- forearms visually extend one pixel farther than neutral body-frame A where silhouette permits;
- feet closer together than Bodyframe A;
- high collar reaches y=13 around neck;
- satchel strap crosses torso diagonally;
- satchel bag mass sits around x=9..13, y=27..32 in front-oriented views;
- rolled right sleeve exposes more forearm pixels than left.

## Portrait linkage

The turnaround must support a 64x64 portrait with:

- same hair volume;
- same eyebrow notch;
- same skin ramp;
- same collar;
- same badge when crop permits;
- no expression-induced identity changes.

---

# 021 — ITEM_DEPOT_JACKET_ICON

Status target after reconstruction: `PIXEL_MASTER_BUILT`

## Authority

Game item: `ITEM_DEPOT_JACKET`  
Label: Depot utility jacket  
Slot: `body`  
Quality: `standard`  
Current modifier: `attributes.endurance +2`

The icon must not depict modifier numbers.

## Canvas

- 32x32 RGBA
- transparent
- target occupied bounds: x=4..27, y=4..27
- center: approximately `(16,16)`

## Palette

Grounded in the current procedural player-equipment treatment:

- outline/deep: `#172128`
- jacket shadow: `#2A414A`
- jacket base: `#3B5963`
- jacket highlight: `#53656E`
- restrained signal/trim accent: `#63D8D1`
- optional metal fastener highlight: `#9FB0B9`

Maximum target: 6 colors plus transparency.

## Silhouette

- open/visible neck opening;
- practical utility collar;
- shoulders broad enough to read as chest equipment;
- compact sleeves;
- two small utility/pocket masses;
- no long coat tail;
- no armor plates;
- no Tamsin-specific badge/satchel/rolled-sleeve asymmetry.

## Cluster plan

- collar/opening: x=13..18, y=4..8
- shoulders: x=7..24, y=8..12
- torso: x=9..22, y=10..25
- left sleeve: x=5..9, y=10..20
- right sleeve: x=22..26, y=10..20
- hem: x=9..22, y=24..27
- utility pocket accents: around x=10..13 and x=18..21, y=16..20

## State/quality separation

The `standard` quality frame is not baked into the icon. `UI_ITEM_QUALITY_FRAMES` renders around it.

## Output

`ITEM_DEPOT_JACKET__icon__v01.png`

---

# 022 — ITEM_DEPOT_JACKET_PAPERDOLL

Status target after reconstruction: `PIXEL_MASTER_BUILT`, then `INTEGRATED`

## Authority binding

Show only when player-safe equipment projection contains:

- `item_id = ITEM_DEPOT_JACKET`
- `slot = body`
- `equipped = true`

The art never decides that the jacket is equipped.

## Canvas

- 32x48 RGBA
- same origin and pivot as player base;
- transparent outside jacket pixels.

## Palette

Same as 021:

- deep `#172128`
- shadow `#2A414A`
- base `#3B5963`
- highlight `#53656E`
- accent `#63D8D1`

## Paper-doll envelope

- high point/collar: y=13
- shoulders: x=8..23, y=15..18
- chest: x=9..22, y=17..27
- waist/hem: x=10..21, y=26..29
- upper sleeve overlays: left x=7..10, right x=21..24, y=17..24
- lower arms remain mostly body/glove territory.

## Occlusion

Default behavior:

- covers `base_torso`;
- partially covers `arm_under` at upper arms;
- stays below neck-item/front-accessory layers when those are defined as front layers;
- stays below held-item layers;
- does not erase hands;
- does not erase legs;
- does not hide hair/head.

## Trim/accent rule

The current procedural avatar uses a cyan chest accent. The reconstructed jacket may retain a restrained 1–2 px trim/utility accent so long as it reads as the same equipment family and not an emissive armor plate.

## Required views in Wave A

First production integration requires front view only.

Before directional movement assets ship, add:

- back;
- left;
- right;
- three-quarter compatibility as demanded by the movement renderer.

## Required output

- `ITEM_DEPOT_JACKET__paperdoll__front__v01.png`
- `ITEM_DEPOT_JACKET__paperdoll__front_mask__v01.png`
- `ITEM_DEPOT_JACKET__paperdoll__anchors__v01.json`

## Integration replacement target

The current `PlayerAvatarPanel` procedurally draws a body-equipment block when the `body` slot is equipped.

Final integration should replace the hard-coded jacket rectangles with an asset-layer renderer while preserving:

- authoritative `GameEquipmentSlot` input;
- existing test tags;
- Story/Character screen visibility;
- no duplicated equipment logic in Compose.

---

# Wave A acceptance matrix

| Asset | Reference | Blueprint | Native master | Integration | Runtime QA |
| --- | --- | --- | --- | --- | --- |
| 001 | required | this packet + selected ref notes | n/a (reference family) | n/a | reference consistency |
| 002 | derives from 001 | complete initial geometry here | required | player avatar | Android visual QA |
| 018 | required | canonical constraints complete here | later sprite/portrait derivatives | NPC presentation later | identity QA |
| 021 | optional item reference | complete initial geometry here | required | inventory | Android visual QA |
| 022 | may inherit 021/player ref | complete initial geometry here | required | paper-doll body slot | equip/unequip QA |

## Stop conditions

Do not mass-produce Batch 001 if Wave A reveals:

- equipment anchor mismatch;
- unreadable 32x48 anatomy;
- Tamsin identity drift;
- icon/paper-doll palette inconsistency;
- smoothing/halo in Android;
- need to duplicate equipment rules in UI;
- inability to trace a production master back to blueprint/reference.

Repair the pipeline first.
