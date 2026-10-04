# L0-04 — Palette and Material Standard

Layer: **L0 Foundation**
Depends on: L0-01 (canon digest), L0-03 (native grid standard)
Sources: `docs/assets/PIXEL_ASSET_MASTER_PLAN.md` §5, §9; `docs/VISUAL_BIBLE.md`

> **Authority note.** The UI palette anchors below are transcribed from
> `PIXEL_ASSET_MASTER_PLAN.md` §5. Character palette anchors are from
> `CHARACTER_PIXEL_BLUEPRINTS.md` §3.6. Both match their sources exactly.

---

## 1. The palette contract

Pixel art fails on colour before it fails on form. A correctly-proportioned
sprite with an unplanned palette looks amateur; a loosely-proportioned sprite
with a disciplined palette looks deliberate.

Therefore every asset specification declares:

1. **Anchors** — colours that must appear recognisably and may not drift.
2. **A derived ramp** — colours computed from anchors by stated rule.
3. **A budget** — maximum distinct colours, by family (L0-03 §8 rule 4).
4. **A forbidden list** — colours that must not appear.

Reference-generation colours do **not** become palette entries automatically.
An anchor enters a palette because a document says so, not because a generated
image happened to contain it.

## 2. Cross-system UI anchors

These are **interface** anchors. They are not a mandate that every world object
use them literally. World assets may introduce local ramps while preserving
readable relationships with Cyan, Gold and Danger feedback.

| Token | Hex | Role |
| --- | --- | --- |
| Ink | `#10151A` | deepest ground, void, outline core |
| Deep | `#172128` | primary dark surface |
| Panel | `#22303A` | panel fill |
| PanelAlt | `#2D3D48` | raised panel / hover |
| Paper | `#E9E2CC` | text, brightest paper value |
| Muted | `#9FB0B9` | secondary text, low-emphasis metal |
| Cyan | `#63D8D1` | **technical / active / signal** |
| Gold | `#E2B65F` | **authority / current / valuable** |
| Danger | `#D66B66` | **failure / damage / emergency** |
| Disabled | `#59666D` | unavailable state |

### 2.1 Semantic colour law

The three accents are **semantic**, not decorative:

- **Cyan** = a system is powered, active, sensing or signalling.
- **Gold** = authority, the current objective, or value.
- **Danger red** = damage, failure, emergency, or an unpowered state.

Using Cyan decoratively, or Danger red for a non-danger thing, destroys the
game's colour logic across every scene at once. This is one of the strongest
constraints in the corpus.

### 2.2 Emergency lighting is red/orange, Danger is `#D66B66`

These are related but distinct. Platform Nine's emergency floor strips read as
Danger-family red. This is *canon-correct*: in this world, emergency lighting and
danger share a hue because the emergency system is what failed.

## 3. Character palette anchors
Two characters have authored palette anchors (Tamsin fully, Jack only by
reference). The neutral player body base deliberately uses semantic slots
instead of hexes so it can serve any identity.

### 3.1 NPC_TAMSIN (canonical, authored)

| Token | Hex | Notes |
| --- | --- | --- |
| jacket | `#30343B` | charcoal municipal utility |
| shirt | `#C9C7BE` | pale work shirt; **lower value contrast than UI Paper** so it does not read as emissive |
| trousers | `#24272C` | dark neutral |
| skin shadow | `#8B5F4B` | warm brown mid-shadow |

Additional highlight/deep colours may be derived, but these anchors must remain
recognisable in the reconstructed palette.

### 3.2 Jack Wilson (player)

The approved reference is the identity authority; exact hex values are **not
specified in the current documentation** and must be sampled from the approved
reference asset at production time, then recorded in the asset manifest.

This is a documented gap, not an omission by this corpus. See L0-08.

### 3.3 Neutral player body base — semantic slots

The neutral body base must **not** lock one skin tone. It uses semantic colour
slots that a later identity palette maps to approved colours:

- `SKIN_HI`
- `SKIN_BASE`
- `SKIN_MID`
- `SKIN_DEEP`
- `UNDERLAY_BASE`
- `UNDERLAY_SHADOW`
- `OUTLINE_DEEP`

### 3.4 Skin ramp construction

Each skin set uses a minimum of:

- highlight;
- base;
- mid shadow;
- deep shadow;
- optional warm/cool accent.

Skin ramps must be tested against the dark UI background (`Ink`/`Deep`) and
against Cyan/Gold equipment accents. A ramp that only works on white is wrong
for this game.

## 4. Material ramp law

**Metal, cloth, skin, glass and powered surfaces must not share identical
ramps.** This is L0-03 rule 7 and it is the most commonly violated visual rule.

### 4.1 Material signatures

| Material | Ramp behaviour | Highlight placement | Edge |
| --- | --- | --- | --- |
| Painted metal | broad, even steps; slight cool cast | long straight runs along edges | hard, 1px dark outline |
| Bare/worn metal | high contrast, irregular | scattered, clustered | hard, broken |
| Cloth | narrow, close steps; matte | minimal; follows fold lines | soft within cluster |
| Skin | narrow, warm ramp; smooth | broad soft areas | no outline; body contour only |
| Glass | very few steps; high transparency logic | single sharp specular pixel | hard |
| Powered surface | flat emissive field + dark surround | saturated core | hard, plus outer glow cluster |
| Rubber/cable | very dark, low contrast | rare tiny specular | soft |

### 4.2 Powered-surface rule

A powered surface (cyan indicator, live display) is drawn as a **flat saturated
core inside a dark surround**, not as a gradient. Adding a glow that bleeds into
neighbouring materials converts a technical asset into an emissive one and
breaks the material distinction the game depends on.

### 4.3 Cluster discipline

Pixel clusters are designed, not produced by applying a pixelation filter.
Dithering is deliberate and sparse; never noise as a substitute for material
design.

Cables must be **clustered** — "clustered cables avoid 1px spaghetti noise"
(`PROP_TUNNEL_CABLE_SET`). A run of single-pixel alternating colours reads as
corruption, not as cable.

## 5. Palette budgets

| Family | Max distinct colours |
| --- | ---: |
| Micro icon | 4–8 |
| Standard icon | 4–8 |
| Item icon | 6–12 |
| Gameplay character / layer | 8–16 |
| Portrait | 12–24 |
| Scene | 16–32 |

Icon art is especially tight. `ITEM_DEPOT_JACKET_ICON` specifies a maximum
target of **6 colours plus transparency**, with a five-colour working set.

## 6. Verified current palette evidence

Measured during corpus construction from the 24 existing runtime rasters.

### 6.1 Scene rasters — actual hexes and pixel counts

Every scene is fully opaque (no transparency) and well inside the 16–32 scene
budget.

| Raster | Colours | Dominant ramp (count) | Accents |
| --- | ---: | --- | --- |
| `pixel_gate_twelve_sealed_scene` | 11 | `#263238` 1880, `#1B252C` 1636, `#111A20` 1420, `#4A555B` 844, `#3A4449` 774 | C 234, Paper 118, G 108, R 16 |
| `pixel_platform_nine_blackout_scene` | 12 | `#17242B` 1676, `#10181D` 1423, `#394850` 1112, `#53616A` 874 | R 158, C 85, Paper 75, G 43 |
| `pixel_service_tunnel_default_scene` | 9 | `#0F171B` 2588, `#182228` 1710, `#47565D` 1060, `#263238` 1050 | C 186, G 40 |
| `pixel_evac_stair_default_scene` | 9 | `#111A20` 4802, `#1B252C` 1536, `#65737A` 465 | C 60, G 24 |
| `pixel_trace_chamber_idle_scene` | 9 | `#111A20` 3391, `#1B252C` 1792, `#162129` 1062 | C 289, G 144 |
| `pixel_district_archive_default_scene` | 10 | `#111A20` 2953, `#48535A` 1900, `#1B252C` 1664, `#6A5941` 720 | G 54, C 33 |
| `pixel_workshop_row_default_scene` | 10 | `#111A20` 2947, `#303E45` 2105, `#1B252C` 1678, `#6A5941` 432 | G 66, C 60, R 30 |
| `pixel_relay_workbench_default_scene` | 10 | `#1B252C` 2193, `#303E45` 1536, `#162129` 1415, `#48535A` 1196 | C 104, G 56, `#D29A55` 20 |
| `pixel_district_plaza_open_scene` | 10 | `#111A20` 2285, `#1B252C` 1967, `#303E45` 1075 | C 113, R 54, G 40 |

### 6.2 Per-location ramp families

The scenes deliberately use **distinct dark ramp families** so locations are
recognisable before any landmark is read:

| Location | Ramp family | Character |
| --- | --- | --- |
| Service Tunnel | `#0F171B #11191D #182228 #263238 #344147 #47565D #66747B` | coldest, deepest — underground |
| Gate Twelve | `#111A20 #151E23 #1B252C #263238 #3A4449 #4A555B #66757C` | cold, sealed, industrial |
| Platform Nine | `#10181D #111A20 #17242B #1B252C #26363E #304149 #394850 #53616A` | widest spread — most lit, most crowded |
| Evac Stair | `#111A20 #162129 #1B252C #26363E #303E45 #48535A #65737A` | dark, quiet, sparse |
| Trace Chamber | `#111A20 #162129 #1B252C #26363E #303E45 #48535A #65737A` | same family as Stair, but highest C density |
| District Archive / Workshop Row / Plaza / Relay Workbench | `#111A20 #162129 #1B252C #26363E #303E45 #48535A #65737A` | **shared district-outdoor family** |

Two observations a rebuilder must not undo:

1. **Service Tunnel is the darkest scene by mean luminance** — `#0F171B` alone
   occupies 2588 of 8192 pixels. Underground should read darker.
2. **Trace Chamber has the highest cyan density relative to size** (289 cyan
   pixels) — it is the most instrumented space, and that is legible before any
   prop is read.
3. Four locations share one ramp family. That is **intentional district-family
   reuse**, not a copy-paste error. The free-roam district was authored as one
   visual set.

### 6.3 Warm accent `#D29A55`

Appears in Relay Workbench (20 px) and is declared in the text-map palette of
Evac Stair, Trace Chamber, Plaza, Archive and Workshop Row, but is **absent
from those five rasters**. It is a *declared but unused* palette slot — warm
counterpoint to Cyan, reserved for workbench lighting and tool-metal warmth.

A rebuild must decide explicitly: either use `H` in those scenes, or remove it
from the palette. Silently carrying an unused slot is how drift starts.

### 6.4 Item and character rasters

| Raster | Grid | Occupied bounds | Colours |
| --- | --- | --- | ---: |
| `pixel_player_gameplay_front_base` | 32x48 | `x5..26, y4..46` | 10 |
| `pixel_player_hair_tech_placeholder` | 32x48 | `x9..22, y2..10` | 3 |
| `pixel_item_depot_jacket_icon` | 32x32 | `x5..26, y4..26` | 5 |
| `pixel_item_depot_jacket_paperdoll` | 32x48 | `x6..25, y14..30` | 6 |
| `pixel_item_work_gloves_icon` | 32x32 | `x4..27, y7..25` | 4 |
| `pixel_item_work_gloves_paperdoll` | 32x48 | `x5..26, y30..35` | 4 |
| `pixel_item_signal_ring_icon` | 32x32 | `x7..24, y4..24` | 4 |
| `pixel_item_signal_ring_paperdoll` | 32x48 | `x5..6, y33..34` | 2 |
| `pixel_item_courier_necktag_icon` | 32x32 | `x8..23, y5..25` | 5 |
| `pixel_item_courier_necktag_paperdoll` | 32x48 | `x14..17, y16..22` | 3 |
| `pixel_item_maintenance_seal_icon` | 32x32 | `x7..24, y7..24` | 4 |
| `pixel_item_dead_relay_icon` | 32x32 | `x6..25, y5..27` | 6 |
| `pixel_item_dead_relay_opened` | 32x32 | `x5..26, y6..26` | 8 |
| `pixel_item_dead_relay_damaged` | 32x32 | `x7..24, y5..27` | 6 |
| `pixel_item_dead_relay_signal_lost` | 32x32 | `x7..24, y5..27` | 5 |

### 6.5 Two reconstruction-critical observations

**`pixel_item_signal_ring_paperdoll` occupies 2 pixels** (`x5..6, y33..34`).
This is the off-hand ring micro-layer behaving exactly as specified: "One/few-pixel
highlight at authored ring anchor; may be omitted in views where it would become
visual noise." It is **not** a broken asset. A rebuild that enlarges it to be
"visible" has broken the micro-layer contract.

**`pixel_player_hair_tech_placeholder` is 3 colours over `x9..22, y2..10`** —
a head-top region only, and explicitly named placeholder. It is **not** Jack's
hair. The existing front base is runtime evidence, **not** final Jack identity.

## 7. Depot Jacket working palette (Wave A reference)

The reference instance for how a palette should be specified:

| Token | Hex |
| --- | --- |
| outline/deep | `#172128` |
| jacket shadow | `#2A414A` |
| jacket base | `#3B5963` |
| jacket highlight | `#53656E` |
| restrained signal/trim accent | `#63D8D1` |
| optional metal fastener highlight | `#9FB0B9` |

Maximum target: **6 colours plus transparency**.

Note this family's base (`#3B5963`) is a **teal-leaning blue-grey** distinct
from Tamsin's charcoal `#30343B`. The Depot Jacket is *the player's* garment and
must stay visually separate from Tamsin's municipal jacket — otherwise the two
characters merge at 32x48.

## 8. Palette derivation rules

When a spec needs a colour it does not name, derive it rather than inventing it:

1. **Ramp step** — move N steps along the declared material ramp. Record N.
2. **Value shift, hue held** — change value only, keep hue. Keeps material
   identity.
3. **Accent reuse** — use Cyan/Gold/Danger only where their semantic role is
   genuinely satisfied.
4. **Neutral mix** — mix a material's shadow toward `Ink`/`Deep` for the deepest
   step.

Never derive a *new hue* to solve a value problem. A third hue in a two-hue ramp
reads as a different material.

## 9. Palette prohibitions

1. Do not exceed the family colour budget.
2. Do not use Cyan/Gold/Danger decoratively.
3. Do not make a material share another material's ramp.
4. Do not bake quality frames into item icons — the icon is quality-neutral and
   `UI_ITEM_QUALITY_FRAMES` renders around it.
5. Do not bake modifier numbers into item icons.
6. Do not bake readable text into pixel art — signage and notices are symbolic
   shapes; actual text stays in UI.
7. Do not recolour a body to show low health — UI feedback first.
8. Do not treat reference-generation colours as palette entries.
9. Do not silently carry unused palette slots (see §6.3).
10. Do not let a world object's ramp converge on the UI anchors so closely that
    object and interface read as the same material.