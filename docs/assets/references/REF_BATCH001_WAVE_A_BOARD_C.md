# Reference Audit — REF_BATCH001_WAVE_A_BOARD_C

Status: `REFERENCE_GENERATED`  
Selection result: **REJECTED for asset 001 and asset 018**  
Use: style/detail study only

## Persisted reference

- Google Drive file: `REF_BATCH001_WAVE_A_BOARD_C.png`
- Drive file ID: `1Id6tO2-2Mte6L2W9nVE7qRKoL9qVnoCW`
- Resolution: 1536 x 1024 RGB PNG
- SHA-256: `31de936c8e091decfbeb91f0a3321ffcc85885dc2f57f65eeca3fe51efd3e909`

## Asset 001 — PLAYER_BODYFRAME_A_TURNAROUND

Decision: **REJECT**

### What passed

- six labeled body views are present;
- equal-height presentation is broadly usable;
- the 32x48 scale idea is visually coherent;
- hands/feet remain readable;
- the separate body-proportion inset is useful as a supporting anatomy reference;
- the pose is neutral enough for rig study.

### What failed

The locked player brief requires an identity-neutral construction model. The candidate instead introduces:

- a distinctive dark hairstyle;
- a specific face;
- a visible eye/face identity;
- a fixed shirt/shorts visual identity rather than a purely neutral construction underlayer;
- animation examples that reinforce that invented identity.

These details would bias a supposedly reusable player rig toward one permanent character design.

### Reuse boundary

Allowed:
- proportional study;
- general 32x48 silhouette density;
- hand/foot readability;
- turnaround spacing;
- body-proportion inset as an anatomy aid.

Rejected:
- player hair;
- face;
- outfit identity;
- any claim that this is the canonical player appearance.

Asset 001 remains `BRIEF_LOCKED`.

---

## Asset 018 — NPC_TAMSIN_TURNAROUND

Decision: **REJECT**

The candidate is visually strong but fails locked asymmetry requirements. Identity constraints outrank polish.

### What passed

- six full-body views are present;
- apparent height/build is consistent;
- slim athletic silhouette is appropriate;
- skin tone is within the intended warm-brown family;
- dark hair / charcoal jacket / pale shirt / dark trousers are directionally correct;
- high collar is clear;
- left-chest badge placement appears broadly correct;
- cross-body satchel is present and remains a compact hip bag rather than a backpack;
- utility-worker silhouette is strong;
- portrait/expression family is internally coherent;
- the overall design is reconstructable at 32x48.

### Critical failures

#### 1. Heavy fringe is on the wrong anatomical side

Locked requirement:
- heavy fringe on **Tamsin's anatomical left**.

Front-view rule:
- Tamsin's anatomical left appears on the **viewer-right** side of a front-facing reference.

Candidate:
- the heavy fringe mass falls primarily on the **viewer-left**, which corresponds to Tamsin's anatomical right.

This is a direct identity inversion and cannot be selected.

#### 2. Sleeve asymmetry is wrong

Locked requirement:
- **right sleeve rolled**;
- left sleeve remains the non-rolled comparison side.

Candidate:
- front and three-quarter views make **both sleeves read as rolled/shortened**, destroying the required asymmetry.

This is also a direct identity failure.

### Additional caution

- the right-eyebrow notch is presented in the detail panel, but the small full-body views do not prove consistent placement across directions;
- satchel routing is broadly useful, but it must be rechecked after correcting left/right body semantics;
- expression portraits may be used only as mood studies, not as the selected identity source because the underlying turnaround fails.

### Reuse boundary

Allowed:
- body build;
- utility-jacket material language;
- high collar;
- badge scale;
- satchel scale;
- palette direction;
- overall 32x48 detail density;
- expression intensity/mood range as a secondary study.

Rejected:
- fringe side;
- sleeve treatment;
- any direct pixel reconstruction of Tamsin from this board;
- any promotion to `REFERENCE_SELECTED`.

Asset 018 remains `BRIEF_LOCKED`.

---

## Generation correction required

Future Tamsin prompts must state the asymmetry twice: anatomically and from the viewer's perspective.

For a front-facing Tamsin:

- **Tamsin's LEFT / viewer RIGHT:** heavy fringe, left-chest badge, left-hip tool loop.
- **Tamsin's RIGHT / viewer LEFT:** eyebrow notch and rolled right sleeve.

The left sleeve must remain visibly full-length/unrolled enough that the right-sleeve asymmetry survives at 32x48.

## Classification

`REFERENCE_GENERATED -> STYLE_DIRECTION_ACCEPTED -> DETAIL_LANGUAGE_ACCEPTED -> PLAYER_SELECTION_REJECTED -> TAMSIN_SELECTION_REJECTED`

No manifest asset is advanced to `REFERENCE_SELECTED` from Board C.
