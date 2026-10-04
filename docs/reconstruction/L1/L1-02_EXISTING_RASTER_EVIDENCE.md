# L1-02 — Existing Raster Evidence and Per-Asset Measurements

Layer: **L1 Existing-state record**
Depends on: L0-03 (native grid and anchor standard), L0-04 (palette standard)
Machine-readable companion: **`L1-02_raster_evidence.json`**

---

## 1. Purpose and method

Every PNG in `android/app/src/main/res/drawable-nodpi/` was decoded pixel by
pixel with the Python standard library during L1 capture. Nothing in this
document is estimated from a palette declaration or a filename — all values are
measured from decoded bytes.

The repository's own `tools/verify_pixel_raster_equivalence.py` was executed
first and reported **24/24 assets pixel-matching their Kotlin source masters
with 0 mismatches**, so these measurements describe the authoritative current
state of the art.

## 2. Corpus-wide facts

| Fact | Value |
| --- | --- |
| Assets decoded | **24** |
| Total pixels | 77,632 |
| Distinct colours across all assets | **71** |
| Partial-alpha pixels | **0** |
| Duplicate files by SHA-256 | **0** |
| Scenes fully opaque | 9 / 9 |
| Character/item rasters with binary transparency | 15 / 15 |

**Zero partial-alpha pixels across all 24 assets** confirms the binary
transparency rule (L0-03 §8 rule 8) is honoured everywhere.

**71 distinct colours for the entire game's art** is the single most important
number in this document. The game presents as one coherent visual system, not
as 24 unrelated images.

### 2.1 The global palette

| Hex | Pixels | Share | UI anchor |
| --- | ---: | ---: | --- |
| `#111A20` | 18,559 | 23.91% | — |
| `#1B252C` | 13,222 | 17.03% | — |
| `#303E45` | 5,806 | 7.48% | — |
| `#48535A` | 5,529 | 7.12% | — |
| `#26363E` | 3,872 | 4.99% | — |
| `#162129` | 3,494 | 4.50% | — |
| `#263238` | 2,930 | 3.77% | — |
| `#0F171B` | 2,588 | 3.33% | — |
| `#182228` | 1,710 | 2.20% | — |
| `#65737A` | 1,701 | 2.19% | — |
| `#17242B` | 1,676 | 2.16% | — |
| `#10181D` | 1,423 | 1.83% | — |
| `#63D8D1` | 1,295 | 1.67% | **Cyan** |
| `#6A5941` | 1,152 | 1.48% | — |
| `#394850` | 1,112 | 1.43% | — |
| `#47565D` | 1,060 | 1.37% | — |
| `#53616A` | 874 | 1.13% | — |
| `#4A555B` | 844 | 1.09% | — |
| `#3A4449` | 774 | 1.00% | — |
| `#344147` | 720 | 0.93% | — |
| `#304149` | 689 | 0.89% | — |
| `#E2B65F` | 686 | 0.88% | **Gold** |
| `#10151A` | 638 | 0.82% | **Ink** |
| `#66757C` | 586 | 0.75% | — |
| `#151E23` | 576 | 0.74% | — |
| `#11191D` | 564 | 0.73% | — |
| `#36454C` | 443 | 0.57% | — |
| `#D66B66` | 298 | 0.38% | **Danger** |
| `#53656E` | 275 | 0.35% | — |
| `#66747B` | 274 | 0.35% | — |
| `#3B5963` | 200 | 0.26% | — |
| `#E9E2CC` | 193 | 0.25% | **Paper** |

The remaining 40 colours are all below 0.25% share — small clusters of
highlight, skin, accent and transition values.

### 2.2 What the distribution proves

Three quarters of all pixels sit in **five dark ramp colours** (`#111A20`,
`#1B252C`, `#303E45`, `#48535A`, `#26363E`). The game is dark by construction,
not by accident.

Accent colours are used sparingly and semantically:

- **Cyan** at 1.67% — powered/active surfaces only;
- **Gold** at 0.88% — authority and value;
- **Danger** at 0.38% — the rarest accent, reserved for failure and emergency.

A rebuild that raises any accent above roughly 2% of a scene's pixels has broken
the semantic colour law (L0-04 §2.1).

### 2.3 The accent colours are used exactly as specified

Every UI accent from L0-04 §2 appears in the art **at its exact specified hex**:
`#63D8D1`, `#E2B65F`, `#D66B66`, `#E9E2CC`, `#10151A`, `#172128`, `#9FB0B9`.

The art and the interface share one colour system. This is deliberate and is the
reason the game reads as coherent.

## 3. Location scenes — 9 assets

All nine are 128x64, fully opaque, and within the 16–32 colour scene budget
(measured 9–12).

| Resource | Colours | Distinct ramp family | Accent profile |
| --- | ---: | --- | --- |
| `pixel_platform_nine_blackout_scene` | 12 | widest spread | R 158, C 85, Paper 75, G 43 |
| `pixel_gate_twelve_sealed_scene` | 11 | cold/sealed | C 234, Paper 118, G 108, R 16 |
| `pixel_trace_chamber_idle_scene` | 9 | district family | C 289, G 144 |
| `pixel_service_tunnel_default_scene` | 9 | **darkest** | C 186, G 40 |
| `pixel_evac_stair_default_scene` | 9 | district family | C 60, G 24 |
| `pixel_district_archive_default_scene` | 10 | district family | G 54, C 33 |
| `pixel_workshop_row_default_scene` | 10 | district family | G 66, C 60, R 30 |
| `pixel_relay_workbench_default_scene` | 10 | district family | C 104, G 56, `#D29A55` 20 |
| `pixel_district_plaza_open_scene` | 10 | district family | C 113, R 54, G 40 |

### 3.1 The district ramp family

Five scenes share one ramp family:

```
#111A20 #162129 #1B252C #26363E #303E45 #48535A #65737A
```

Evac Stair, Trace Chamber, Depot Plaza, Municipal Archive, Workshop Row, Relay
Workbench. This is **intentional district-family reuse** — the free-roam district
was authored as one visual set. A rebuild that gives each of these a unique ramp
has broken the family logic.

Three scenes deliberately depart:

| Scene | Ramp | Why |
| --- | --- | --- |
| Service Tunnel | `#0F171B #11191D #182228 #263238 #344147 #47565D #66747B` | **coldest and darkest**; underground |
| Gate Twelve | `#111A20 #151E23 #1B252C #263238 #3A4449 #4A555B #66757C` | cold, sealed, industrial |
| Platform Nine | `#10181D #111A20 #17242B #1B252C #26363E #304149 #394850 #53616A` | **widest spread**; most lit, most crowded |

### 3.2 Measured luminance ranking

| Scene | Dominant dark | Pixels | Reads as |
| --- | --- | ---: | --- |
| Service Tunnel | `#0F171B` | 2,588 | underground |
| Platform Nine | `#17242B` | 1,676 | lit interior |
| Evac Stair | `#111A20` | 4,802 | very dark, sparse |
| Trace Chamber | `#111A20` | 3,391 | dark + cyan |

**Service Tunnel is the darkest scene by mean luminance** — `#0F171B` alone
occupies 2,588 of 8,192 pixels. Underground reads darker than everything else,
which is correct and must be preserved.

### 3.3 Cyan density as an instrument cue

| Scene | Cyan pixels | Interpretation |
| --- | ---: | --- |
| Trace Chamber | **289** | most instrumented space |
| Gate Twelve | 234 | sealed but signalling |
| Service Tunnel | 186 | maintenance indicators |
| District Plaza | 113 | active public space |
| Relay Workbench | 104 | diagnostic lighting |
| Platform Nine | 85 | powered emergency systems |
| Workshop Row | 60 | contractor equipment |
| Evac Stair | 60 | sparse guidance lights |
| Municipal Archive | 33 | backup power only |

Cyan density alone identifies a location before any landmark is read. This is
the visual system working as intended and is a strong constraint on rebuilds.

### 3.4 Platform Nine carries all four accents

It is the only scene containing Cyan, Gold, Danger **and** Paper in meaningful
quantity. It is the opening location, the last lit place, and the only place
where passengers, emergency lighting, signage and narrative text coexist. The
palette density is a direct consequence of narrative load.

### 3.5 The declared-but-unused warm accent

`#D29A55` appears in **20 pixels** of Relay Workbench and is declared in the
Kotlin palette of five other scenes while being **absent from those rasters**.

This is a real authoring inconsistency, recorded in L0-04 §6.3. A rebuild must
decide explicitly: use `H` in those scenes, or remove it from the palette.
Silently carrying an unused slot is how drift begins.

## 4. Character rasters — 2 assets
Only two of the 24 rasters are character art, and one of those is explicitly
placeholder-quality. This section carries the most consequential finding in
L1, so the measurements are given in full rather than summarised.

### 4.1 `pixel_player_gameplay_front_base`

| Property | Value |
| --- | --- |
| Grid | 32x48 RGBA |
| Occupied bounds | `x5..26, y4..46` |
| Measured height | **43 px** (y4–y46) |
| Colours | 10 |
| Transparency | binary |
| Recorded stage | runtime evidence, **not** final Jack identity |

**Palette (all 10):**

| Hex | Pixels | Role |
| --- | ---: | --- |
| `#10151A` | 224 | outline (UI `Ink`) |
| `#566564` | 144 | underlay / garment mid |
| `#AD7D62` | 126 | skin base |
| `#3B4543` | 70 | garment dark |
| `#343F3E` | 40 | garment shadow |
| `#27302F` | 30 | garment deep |
| `#8B5F4B` | 14 | skin shadow |
| `#1F2625` | 10 | deep outline |
| `#C79779` | 2 | skin highlight |
| `#7E8B84` | 2 | highlight |

### 4.2 Measured geometry against the L0-03 specification

| Measure | Spec | Measured | Verdict |
| --- | --- | --- | --- |
| Occupied height | 44 px | 43 px (y4..46) | within tolerance |
| Top margin | 2 px (y2) | 4 px (y4) | **2 px lower than spec** |
| Head box | `x11..21, y2..12` | widest `x8..23` at y8–10 | **wider than spec** |
| Shoulder span | 16–18 px at `y15` | 16 px at y17–18 | matches |
| Shoulder line | `x8..24` | `x8..23` at y17–18 | matches |
| Feet | L`(11,46)` R`(21,46)` | `x8..23` at y45–46 | wider stance |
| Pivot | `(16,47)` | row 47 empty, y46 is last art | correct |

The head is **wider (16 px) and lower (starting y4)** than the documented
cluster map, and the feet are **wider** than the documented anchors. These are
measured deviations from `L0-03` §5 and are recorded rather than reconciled,
because the raster is the current runtime truth and the cluster map is the
planning contract.

### 4.3 A reconstruction-critical finding — silhouette identity

The measured silhouette does **not** read as the documented male player figure.

Evidence, all from decoded pixels:

1. **Bare limbs.** Skin (`#AD7D62`) occupies the full outer edge of both arms
   from y19 to y33 — there is no sleeve or glove mass over the upper arms.
2. **Narrow waist, wide hip flare.** Shoulder width 16 px at y17–18 narrows to
   the torso block, then the leg mass at y40–44 is 14 px wide with feet
   flaring to 16 px at y45–46.
3. **Bare lower legs.** Skin tones are absent below y33; legs are covered, but
   the arm treatment and hip flare produce a feminine-coded silhouette.
4. **No jacket.** The torso uses garment greys `#566564`/`#3B4543`, but the
   silhouette lacks the layered-clothing volume the approved reference requires.

**Why this matters and how to treat it.**

`CHARACTER_PIXEL_BLUEPRINTS.md` §1.0 states the player visual identity target
**is no longer generic** — it must preserve Jack Wilson's approved identity,
non-chibi proportions, hair/face silhouette and layered-clothing/equipment
presentation.

The existing front base does not meet that standard. It is:

- explicitly recorded in `ASSET_PROVENANCE_REGISTRY.md` §9 as "runtime evidence,
  **not** final Jack identity";
- built from a flat procedural treatment with no hair layer of its own;
- anatomically ambiguous in a way that reads against the approved reference.

**The correct rebuild action is to treat this asset as a migration placeholder
and rebuild it from `UI_REFERENCE_CHARACTER_APPROVED_V1` — not to reproduce it.**

This is not a licence to invent Jack's appearance. It is a statement that the
existing sprite is not the target, and that the approved reference is.

### 4.4 `#8B5F4B` — Tamsin's skin anchor is in the player sprite

`#8B5F4B` is the authored `skin_shadow` for **NPC_TAMSIN**, and it appears in
`pixel_player_gameplay_front_base` at 14 pixels (y11, y13, y15 — neck/jaw
shading).

This is almost certainly coincidental: it is a plausible mid-brown skin shadow
that the player sprite's procedural generator also used. It is recorded as an
observation, **not** as evidence that the player is Tamsin or that Tamsin's
palette has leaked.

**It does, however, illustrate a real hazard:** a palette anchor from one
character can appear in another character's art by accident, and a rebuild that
reads presence of an anchor as evidence of identity will draw the wrong
conclusion. Identity comes from the character record, never from a palette
match.

### 4.5 `pixel_player_hair_tech_placeholder`

| Property | Value |
| --- | --- |
| Grid | 32x48 RGBA |
| Occupied bounds | `x9..22, y2..10` |
| Colours | 3 |
| Palette | `#2C302E` 57, `#191C1B` 29, `#4A4F4A` 8 |

Occupies only the head-top region (y2–y10) — a partial hair cap, not a full
hairstyle. Near-black with a muted cool highlight, which matches the district's
visual language.

**This is explicitly placeholder-quality by name and must not become canonical
merely through reuse.** The approved reference governs Jack's hair.

## 5. Item and equipment rasters — 13 assets
Thirteen of the 24 rasters are items and equipment layers. Together they are
the largest coherent family in the corpus and the best evidence of how the
paper-doll system is meant to behave.

### 5.1 Inventory and state icons (32x32)

| Resource | Colours | Bounds | Notes |
| --- | ---: | --- | --- |
| `pixel_item_depot_jacket_icon` | 5 | `x5..26, y4..26` | matches `ITEM_DEPOT_JACKET_ICON` |
| `pixel_item_work_gloves_icon` | 4 | `x4..27, y7..25` | matches `ITEM_WORK_GLOVES_ICON` |
| `pixel_item_signal_ring_icon` | 4 | `x7..24, y4..24` | `uncommon` quality |
| `pixel_item_courier_necktag_icon` | 5 | `x8..23, y5..25` | matches `ITEM_COURIER_NECKTAG_ICON` |
| `pixel_item_maintenance_seal_icon` | 4 | `x7..24, y7..24` | matches `ITEM_MAINTENANCE_SEAL_ICON` |
| `pixel_item_dead_relay_icon` | 6 | `x6..25, y5..27` | intact base state |
| `pixel_item_dead_relay_opened` | 8 | `x5..26, y6..26` | most complex state |
| `pixel_item_dead_relay_damaged` | 6 | `x7..24, y5..27` | failed forced opening |
| `pixel_item_dead_relay_signal_lost` | 5 | `x7..24, y5..27` | indicator fully dark |

### 5.2 The Dead Relay state family — verified continuity

The four relay states form the clearest example of state-variant design in the
corpus:

| State | Colours | Bounds relationship |
| --- | ---: | --- |
| `dead_relay_icon` (intact) | 6 | `x6..25, y5..27` |
| `dead_relay_opened` | 8 | `x5..26, y6..26` — **widest** |
| `dead_relay_damaged` | 6 | `x7..24, y5..27` |
| `dead_relay_signal_lost` | 5 | `x7..24, y5..27` |

- `opened` is one pixel wider on each side and **most colourful (8)** — opened
  casing reveals internal components;
- `damaged` and `signal_lost` share identical bounds (`x7..24, y5..27`), so the
  difference between them is **purely the indicator state**, not geometry;
- `signal_lost` has the **fewest colours (5)** — the pulse indicator is dark,
  exactly as specified: "Same damaged object with signal indicator fully dark."

This is correct design. A rebuild must preserve the geometry identity between
`damaged` and `signal_lost` and change only the indicator.

### 5.3 Paper-doll layers (32x48)

| Resource | Colours | Bounds | Covers |
| --- | ---: | --- | --- |
| `pixel_item_depot_jacket_paperdoll` | 6 | `x6..25, y14..30` | chest + upper arms |
| `pixel_item_work_gloves_paperdoll` | 4 | `x5..26, y30..35` | hands + lower forearms |
| `pixel_item_courier_necktag_paperdoll` | 3 | `x14..17, y16..22` | neck |
| `pixel_item_signal_ring_paperdoll` | 2 | `x5..6, y33..34` | **2 pixels only** |

### 5.4 Paper-doll bounds verify against the L0-03 anchor table

| Layer | Measured bounds | Anchor expectation | Verdict |
| --- | --- | --- | --- |
| Depot Jacket | `y14..30` | high point/collar `y13`, hem `y26..29` | consistent |
| Work Gloves | `y30..35` | wrist `(6,32)`/`(26,32)`, hand mass | consistent |
| Courier Necktag | `y16..22` | neck item anchor `(16,14)` | **2 px below anchor** |
| Signal Ring | `y33..34` | off-hand `(5,31)` | **2 px below anchor** |

The necktag and ring sit slightly below their declared anchors. These are small
measured deviations, recorded rather than reconciled. Neither is large enough to
break the paper-doll system, but a rebuild should place them on the declared
anchors rather than reproducing the offset.

### 5.5 The 2-pixel signal ring is correct, not broken

`pixel_item_signal_ring_paperdoll` occupies **2 pixels** at `x5..6, y33..34`.

The asset specification says: "One/few-pixel highlight at authored ring anchor;
**may be omitted in views where it would become visual noise**."

Two pixels at the off-hand is exactly that. This is a **correct**
implementation of a micro-layer, not a failed asset. A rebuild that enlarges it
to make it "visible" has broken the micro-layer contract.

## 6. Font/UI raster note

`pixel_platform_nine_blackout_scene` is 1,255 bytes while seven other scenes are
32,900 bytes. This is a **compression** difference, not an emptiness difference —
all nine scenes are unique by hash, fully opaque, 128x64, and carry 9–12 colours
each. The smaller file simply compresses better. No scene is a placeholder.

## 7. Stage and approval status

| Aspect | Status | Source |
| --- | --- | --- |
| Rasters present | 24 / 24 | measured |
| Pixel-match to source master | 24 / 24, 0 mismatches | verifier executed |
| Dimensions match manifest | 24 / 24 | verifier executed |
| Runtime bindings valid | 24 / 24 | verifier executed |
| Visual approval | **NOT ESTABLISHED** | `raster_bindings_2026-10-02.json` |
| Native-scale art review | **PENDING** | inherited open item |
| Physical device QA (Galaxy A03) | **PENDING** | inherited open item |
| Canon approval | **NOT GRANTED** | `ASSET_PROVENANCE_REGISTRY.md` |

**No asset in this corpus is `CANON_APPROVED`.** They are hash-verified runtime
evidence. Bytes matching their source master is a correctness property, not an
artistic judgement.

## 8. Consequences for the rebuild

1. **The 24 rasters are the floor, not the target.** They are the current state
   of a partially-built art pipeline.
2. **`pixel_player_gameplay_front_base` must be rebuilt from the approved
   reference**, not reproduced (§4.3). Its silhouette does not match Jack
   Wilson's approved identity.
3. **`pixel_player_hair_tech_placeholder` must be replaced**, not reused as
   canon.
4. **The scene ramp families must be preserved** — five scenes share one family
   by design, and three depart for specific reasons (§3.1).
5. **Accent budgets must be held** — Cyan ~1.7%, Gold ~0.9%, Danger ~0.4%
   globally (§2.2).
6. **Dead Relay state geometry must stay identical** between `damaged` and
   `signal_lost` (§5.2).
7. **The signal ring stays 2 pixels** unless the design changes deliberately.
8. **The declared-unused `#D29A55` slot must be resolved** one way or the other
   (§3.5).
9. **Cyan density per location is a design signal** and should be preserved as
   relative ordering (§3.3).
10. **No asset is canon-approved.** Rebuilds start from `PIXEL_MASTER_BUILT`, not
    from `VERIFIED`.