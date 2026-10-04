# L0-02 — Angle Standard

Layer: **L0 Foundation**
Depends on: L0-01 (canon digest), `docs/assets/PIXEL_ASSET_MASTER_PLAN.md`
Governs: every view specification in L2, L3 and L4

> **Authority note.** This document expands, it does not replace. The six-view
> character turnaround originates in `docs/assets/PIXEL_ASSET_MASTER_PLAN.md` §7
> and `docs/assets/CHARACTER_PIXEL_BLUEPRINTS.md` §1.11. The view numbering here
> matches those sources exactly.

---

## 1. Why angles get their own standard

A pixel asset reconstructed from a description is usually correct in proportion
and wrong in *presence* — it looks like the thing in one pose and like nothing at
all when turned. Angle documentation exists to prevent that failure by fixing
the observation conditions before any artistic choice is made.

Three properties make an angle specification reproducible:

1. **Named camera position.** Not "a side view" but `L_PROFILE`, with a defined
   camera axis and a defined rotation from front.
2. **Invariants across views.** Height, head size, shoulder span, hand scale and
   pivot do not change when the camera moves. Anything that changes them is a
   reconstruction error, not a stylistic choice.
3. **Per-view asymmetry ledger.** Every asymmetric feature is assigned an
   anatomical side once and checked in every view.

## 2. Camera position definitions

The canonical angles are named relative to the **subject's own body**, never to
the viewer's left/right. This is the rule that prevents mirrored art.

| Code | Name | Camera axis | Rotation from front | Notes |
| --- | --- | --- | ---: | --- |
| `FRONT` | front | camera on subject's anterior, at subject's eye height | 0° | Symmetry reference. Most detailed face information. |
| `F3Q` | front three-quarter | camera offset toward subject's left, 30–45° | 30–45° | Shows both silhouette and a partial second face plane. |
| `L_PROFILE` | left profile | camera on subject's left side, at subject's eye height | 90° | Shows true anterior-posterior depth. **Authored separately.** |
| `R_PROFILE` | right profile | camera on subject's right side | 90° (opposite) | **Authored separately.** Never a mirror of `L_PROFILE`. |
| `R3Q` | rear three-quarter | camera offset toward subject's right rear, 30–45° | 135–150° | Back plane plus one side. |
| `BACK` | back | camera on subject's posterior | 180° | Back hair, rear equipment, pack/belt occlusion. |

### 2.1 The mirroring prohibition

`L_PROFILE` and `R_PROFILE` are **separate authored assets**. Mirroring is
forbidden whenever any of the following exist:

- asymmetric hairstyle or fringe;
- a rolled, pushed-up or torn sleeve;
- a scar, notch, tattoo, birthmark or other body mark;
- a badge, patch, emblem or asymmetric fastener;
- a satchel, bag, scabbard or asymmetric tool;
- a weapon or held item in one hand only;
- a belt buckle, holster or asymmetric pocket;
- handedness-dependent pose.

For a subject with none of these, `R_PROFILE` may legitimately be a horizontal
flip of `L_PROFILE` — but this must be **declared explicitly in the asset's
symmetry ledger**, never assumed.

### 2.2 Which side is which

For every view, this mapping must be applied before describing any feature:

| View | Subject LEFT appears | Subject RIGHT appears |
| --- | --- | --- |
| `FRONT` | viewer's **right** | viewer's **left** |
| `F3Q` | viewer's right-rear (far side) | viewer's left-front (near side) |
| `L_PROFILE` | near the camera (visible) | hidden behind body |
| `R_PROFILE` | hidden behind body | near the camera (visible) |
| `R3Q` | hidden / far | near the camera |
| `BACK` | viewer's **left** | viewer's **right** |

The `FRONT` inversion is the single most common error in character pixel art.
It is restated in every character specification in L4 without exception.

## 3. The six-view reference board

The non-shipping reference board shows all six views. Requirements:

### 3.1 Board layout

- overall canvas 1536x1024 or larger;
- six equal view panels in the order `FRONT, F3Q, L_PROFILE, R_PROFILE, R3Q, BACK`;
- flat neutral background;
- orthographic/turnaround presentation;
- no dramatic perspective;
- consistent ground line across all six panels;
- the subject's apparent height identical in all six panels.

### 3.2 Board invariants

These must hold across all six panels or the board is rejected:

| Invariant | Requirement |
| --- | --- |
| Apparent height | identical within reconstruction tolerance |
| Head size | identical |
| Shoulder span | identical |
| Hip span | identical |
| Hair volume | identical |
| Equipment anchor heights | identical |
| Foot length | identical |
| Hand scale | identical |
| Head-to-body ratio | ~1:4 adult |
| Ground line | shared |

### 3.3 What a board may decide

- subtle neutral anatomy transitions;
- elbow and knee volume;
- side-profile chest and back depth;
- natural hand and foot silhouette inside the fixed envelope;
- how clothing falls on the body from each side.

### 3.4 What a board may never decide

- permanent identity (for a neutral player body base);
- hair, scars or clothing (for a neutral body base);
- equipment selection;
- role, faction or story background;
- ability effects;
- any hidden game state.

## 4. View sets by asset family

The view set is fixed by family, never chosen per-asset. Six families:

### 4.1 `SIX_VIEW` — mandatory

**Applies to:** player body bases (FRONT/BACK/profiles), every recurring NPC,
every canonical named-character turnaround.

Assets: `PLAYER_BODYFRAME_A_TURNAROUND`, `NPC_TAMSIN_TURNAROUND`,
`PLAYER_GAMEPLAY_FRONT_BASE`, `PLAYER_GAMEPLAY_LEFT_PROFILE_BASE`,
`PLAYER_GAMEPLAY_RIGHT_PROFILE_BASE`, `PLAYER_GAMEPLAY_BACK_BASE`, and every
Batch 002 NPC body base.

### 4.2 `SIX_VIEW_DEFERRED` — full set specified, subset shipped

**Applies to:** character equipment layers whose first integration is
front-only.

All six views are **specified**. Views not yet built are marked `DEFERRED` with
the reason "movement renderer does not request this direction yet". This is the
Wave A pattern for `ITEM_DEPOT_JACKET_PAPERDOLL`, which requires front for first
production integration and back/left/right/three-quarter before directional
movement assets ship.

### 4.3 `PROP_ANGLES` — presentation angle set

**Applies to:** held props and interactive props.

Default set: `FRONT`, `F3Q`, `L_PROFILE`, `TOP` (where the prop is operated from
above or read from above). Plus a `GRIP_IN_CONTEXT` view showing the prop
attached to the hand anchor rather than isolated.

Held props such as `PROP_DIAGNOSTIC_READER` additionally require a
`TWO_HAND_OPERATE` view matching the canonical diagnostic pose.

### 4.4 `SCENE_CAMERA` — single camera plus state variants

**Applies to:** all 128x64 location scenes.

A scene is **not** a turnaround subject. Its angle documentation covers:

- one primary camera position and framing;
- architectural axes (which direction the space "faces");
- the crop-safe zone for UI text;
- documented state variants (`BLACKOUT`, `OPENED`, `AFTershock`, `TRAINING`,
  `ECHO_ACTIVE`) that reuse the same camera;
- forbidden re-angles — a rebuild must not redraw a scene from a new angle,
  because scene identity is camera-bound.

**Hard rule:** identical architecture, different state. A state variant that
changes architecture is a different location, not a state.

### 4.5 `TILE_AXES` — seam behaviour, not camera

**Applies to:** tiles, atlases, environment modules.

Documents: the axes the tile repeats along, seam pixels that must match,
edge-constrained modules, and how modules join. Camera angles are NOT
applicable and must be marked `NOT APPLICABLE — TILE_AXES`.

### 4.6 `PRESENTATION_STATES` — no camera angle

**Applies to:** UI icons, HUD icons, frames, chrome, FX cells.

Documents: each presentation state and the authoritative condition that selects
it. View angles are `NOT APPLICABLE — PRESENTATION_STATES`.

## 5. The view specification template

Every view in L2/L3/L4 is specified with this block:

```markdown
### View: <CODE> — <Name>

**Camera.** <axis, rotation, elevation>
**Subject-side mapping.** <which side is near/far, explicit>
**Visible features.** <what must be legible in this view>
**Hidden features.** <what must NOT be visible or is occluded>
**Silhouette delta.** <how the outline differs from FRONT>
**Internal planes.** <how many depth planes read>
**Asymmetry check.** <each asymmetric feature and its expected position here>
**Palette use.** <which colours dominate; any state-specific colour>
**Light.** <how the light interacts from this angle>
**Anchor visibility.** <which anchors are observable; which are occluded>
**Reconstruction notes.** <specific things to get right>
**Acceptance.** <observable checks that prove the view is correct>
```

`Acceptance` must be checkable by eye against the rendered asset, not by
judgment. "The left hand must be visible" is checkable. "The view should feel
dynamic" is not.

## 6. Cross-view consistency ledger

Every multi-view asset carries a ledger that states what is **constant** and
what is **permitted to vary**. Without this, per-view descriptions drift apart.

### 6.1 Constant across all views (unless the asset spec says otherwise)

- native grid dimensions;
- pivot coordinate;
- ground line;
- apparent height;
- head size;
- shoulder and hip span;
- hand and foot scale;
- palette identity (the ramp families, not their distribution);
- material assignment;
- light direction **in world space**;
- equipment anchor coordinates.

### 6.2 Permitted to vary

- silhouette outline detail;
- internal depth-plane count;
- which features are occluded;
- the visible portion of any asymmetric feature;
- highlight/shadow distribution consistent with the same light direction;
- for 3/4 views, a modest foreshortening allowance of the near side.

### 6.3 Forbidden variation

- height, head size, shoulder span, hand/foot scale changing between views;
- palette identity changing between views;
- light direction flipping between views;
- an anchor moving between views;
- a feature changing anatomical side between views;
- equipment appearing in one view and not another for no documented reason.

## 7. Asymmetric side ledger

For any asset with asymmetric features, the specification must contain a table
of this shape. Tamsin's is given as the worked example.

| Feature | Anatomical side | FRONT viewer side | L_PROFILE | R_PROFILE | BACK viewer side |
| --- | --- | --- | --- | --- | --- |
| Heavy fringe | left | right | near | far | n/a |
| High collar | both | both | near | near | both |
| Rolled sleeve | right | left | far | near | right |
| Systems badge | left chest | right | far | near | n/a |
| Satchel strap | left shoulder → right hip | right shoulder → left hip | near | far | left shoulder → right hip |
| Tool loop | left hip | right | far | near | n/a |
| Eyebrow notch | right | left | n/a (profile) | n/a | n/a |

An asset with an asymmetric side ledger is `ASYMMETRIC = YES` and **fails
reconstruction if any view contradicts the ledger**.

## 8. Neutral-body rule

A reusable player body base that will be shared across identities must not leak
a stable identity. It fails if a reviewer can describe a character from it.

The neutral player turnaround therefore has:

- bald or featureless head;
- minimal construction face;
- no distinct hairstyle;
- no facial hair;
- no permanent scars, marks or jewellery;
- no equipment.

This is what separates `PLAYER_BODYFRAME_A_TURNAROUND` (neutral, six-view,
reference-only) from Jack Wilson's identity layer set (specific, canonical,
owner-approved). They are **different assets with different rules**, and merging
them is a prohibited error.

## 9. Angle coverage requirements by production stage

| Stage | Angle requirement |
| --- | --- |
| `REFERENCE_SELECTED` | Board exists and passes the §3.2 invariant check. |
| `BLUEPRINTED` | Every view in the set has a written specification. |
| `PIXEL_MASTER_BUILT` | Every **non-DEFERRED** view exists as a native asset. |
| `INTEGRATED` | Views the current renderer requests are wired and render correctly. |
| `VERIFIED` | Every view passes its acceptance list at 1x and at target scale. |
| `CANON_APPROVED` | All six views built and verified, or the deferral is permanent and documented as such. |

An asset may not reach `CANON_APPROVED` with an undocumented angle gap.

## 10. Prohibitions restated

1. Do not mirror an asymmetric asset between profiles.
2. Do not change apparent height, head size or shoulder span between views.
3. Do not move an anchor between views.
4. Do not flip light direction between views.
5. Do not invent a view set outside the six families in §4.
6. Do not merge a neutral body base with an identity-bearing character.
7. Do not redraw a scene from a new camera to express a state change.
8. Do not mark an asset VERIFIED with an undocumented DEFERRED view.
9. Do not use anti-aliasing to fake a profile that the grid cannot hold.
10. Do not describe an angle as "similar to front" — similarity is the failure.