# L0-07 — Prohibitions and Failure Modes

Layer: **L0 Foundation**
Depends on: L0-00 (protocol), L0-01 (canon digest)

> **Purpose.** A prohibition that is written once and not restated is a
> prohibition that will be violated. This document is the master list; every
> specification in L2–L5 restates the prohibitions that apply to it locally.
> When a rebuilder disagrees with a prohibition, the correct response is to
> raise it here — not to quietly work around it.

---

## 1. The catastrophic failure modes

These destroy the rebuild. They are listed first because they matter most.

### 1.1 Subject-side inversion

**The failure.** Placing a character's left-side features on the viewer's left
in a front-facing sprite.

**Why it is catastrophic.** Every named character's identity flips. Tamsin's
heavy fringe moves to the wrong side, the badge and tool loop swap, the rolled
sleeve switches arms, the eyebrow notch jumps. The character becomes a
different character. This is the single most frequently violated rule in
character pixel art across the entire project history.

**Rule.** In `FRONT`: **subject LEFT = viewer RIGHT**. In `BACK`:
subject LEFT = viewer LEFT. See L0-02 §2.2 for the full mapping.

**Detection.** Render the sprite in pure black. If the heavy detail mass is on
the wrong side, it is wrong.

### 1.2 Geometry-built characters

**The failure.** Constructing a character from rectangles, circles, polygons,
block primitives or procedural drawing logic.

**Why it is catastrophic.** `PIXEL_ASSET_MASTER_PLAN.md` §6 states this
directly: "Character art must not be geometry-built." Rig anchors, pivots and
bounds are **metadata for placement, equipment and animation** — they do not
authorise drawing a human from primitives.

**Rule.** Characters are authored pixel-art sprites produced through the
reference → blueprint → reconstruction pipeline. A historical block avatar may
survive temporarily for debugging/migration safety and is explicitly a
placeholder scheduled for replacement.

**Detection.** Ask: if I delete all the anchor coordinates, could someone still
draw this character from the remaining description? If not, the anchor table
has become a painting guide.

### 1.3 Merging the neutral body base with an identity

**The failure.** Using `PLAYER_BODYFRAME_A_TURNAROUND` (neutral, no identity)
as Jack Wilson's body.

**Why it is catastrophic.** The neutral base must be reusable across identities.
The moment it carries Jack's hair and face it cannot serve anyone else, and the
paper-doll customization system has no neutral base to sit on.

**Rule.** Neutral body base = bald/featureless head, minimal construction face,
no distinct hairstyle, no facial hair, no permanent marks, no equipment.

**Detection.** Ask: can a reviewer describe a stable character identity from
this base? If yes, it has leaked.

### 1.4 Tamsin identity drift

**The failure.** Any of: long hair, saturated neon clothing, removed eyebrow
notch, satchel replaced by backpack, rolled sleeve on the wrong arm, badge on
the wrong chest, satchel strap path broken.

**Why it is catastrophic.** These are the authored `forbidden_deviations`. They
are the difference between Tamsin and a generic NPC.

**Rule.** See L0-01 §5.5. All four forbidden deviations plus the full
asymmetry ledger must hold in every view.

### 1.5 Treating `main` as canonical

**The failure.** Building the rebuild from the default branch.

**Why it is catastrophic.** `main` contains a two-line README and one commit.
All 354 files of substance live on `docs/master-game-development-program`.

**Rule.** `main` is **not** the canonical implementation branch. Do not
promote, rewrite, or merge `main` merely because it is the default branch.

### 1.6 Inventing world canon

**The failure.** Filling empty catalogs with invented kingdoms, factions,
settlements or creatures to make documentation feel complete.

**Why it is catastrophic.** `WORLD_POLITICAL_ENTITIES.md` and
`WORLD_SETTLEMENT_CATALOG.md` explicitly state that nothing is invented to fill
a catalog. An invented faction becomes indistinguishable from authored canon
once written down, and then the game has canon it never decided on.

**Rule.** Empty means empty. Write `NOT SPECIFIED IN DOCS` and move on.

### 1.7 Treating technical framework assets as story canon

**The failure.** Presenting `technical/non-canon framework` units as content.

**Why it is catastrophic.** 300 of the 500 planned units are explicitly
non-canon framework. NPC archetypes, body-frame kits and clothing kits are
*production infrastructure*, not characters.

**Rule.** Generic NPC entries remain technical/non-canon until authored content
assigns a stable named identity. They must never silently become story canon.

## 2. Angle prohibitions

1. Do not mirror an asymmetric asset between `L_PROFILE` and `R_PROFILE`.
2. Do not change apparent height, head size, shoulder span or hand/foot scale
   between views.
3. Do not move an anchor between views.
4. Do not flip light direction between views.
5. Do not invent a view set outside the six families in L0-02 §4.
6. Do not merge a neutral body base with an identity-bearing character.
7. Do not redraw a scene from a new camera to express a state change.
8. Do not mark an asset `VERIFIED` with an undocumented `DEFERRED` view.
9. Do not use anti-aliasing to fake a profile the grid cannot hold.
10. Do not describe an angle as "similar to front" — similarity is the failure.
11. Do not change `R_PROFILE` from `L_PROFILE` by any method other than
    re-authoring, without declaring it in the symmetry ledger.
12. Do not ship a five-view turnaround as "complete". It is five views.

## 3. Pixel prohibitions

1. No anti-aliasing inside shipped raster assets.
2. No fractional-pixel placement.
3. No bilinear/bicubic scaling of source art.
4. Do not exceed the family colour budget (L0-04 §5).
5. Binary transparency on ordinary sprite edges; graded alpha only on a
   documented FX layer.
6. Do not use noise dithering as a substitute for material design.
7. Do not produce pixel clusters by applying a pixelation filter to smooth art.
8. Do not bake readable text into pixel art — signage and notices are symbolic
   shapes; actual text stays in UI.
9. Do not bake modifier numbers into item icons.
10. Do not bake quality frames into item icons.

## 4. Palette prohibitions

1. Do not use Cyan/Gold/Danger decoratively.
2. Do not let metal, cloth, skin, glass and powered surfaces share a ramp.
3. Do not recolour a body to show low health.
4. Do not treat reference-generation colours as palette entries.
5. Do not silently carry unused palette slots.
6. Do not derive a new hue to solve a value problem.
7. Do not let a world object's ramp converge on the UI anchors so closely that
   object and interface read as the same material.

## 5. Occlusion and layer prohibitions

1. Do not duplicate stat/equipment/rules calculations inside UI code.
2. Do not let art decide what is equipped, reachable, discovered or damaged.
3. Do not flatten a state overlay into a base scene.
4. Do not build unique flattened location images when a master plus overlay is
   sufficient.
5. Do not erase the base hand when adding a held item — use a grip mask.
6. Do not let a chest layer move the shoulder anchors.
7. Do not let equipment follow a static position instead of frame anchors
   (causes sliding).
8. Do not hide interactable silhouettes with a blackout overlay.
9. Do not reveal hidden authored state through a player-visible asset.

## 6. State and boundary prohibitions

1. Do not expose hidden authored rules or secret provenance through
   player-facing projections.
2. Do not let a visual assert a fact the engine has not made visible.
3. Do not create a map marker that implies reachability the engine did not
   provide.
4. Do not use a scene state variant before the story state occurs.
5. Do not use an FX overlay to communicate a hazard the engine has not
   declared.
6. UI does not own whether an NPC exists in the room.
7. Ambient loops do not decide hazards.

## 7. Provenance prohibitions

1. Do not paste a smooth generated image into the game and call it pixel art.
2. Do not regenerate an approved character from memory when a reference exists.
3. Do not mark an asset `VERIFIED` without checking its real integration.
4. Do not conflate a PNG export with a source master.
5. Do not conflate a hash match with artistic approval.
6. Do not infer canon from branch recency or PR number.
7. Do not delete superseded work; mark it and point forward.
8. Do not register external copyrighted art as a runtime source.
9. Do not create `content/visual/asset_provenance.json` until ID naming is
   locked, current assets are reconciled, and a validation schema exists.

## 8. Story and tone prohibitions

These are as binding as the technical rules, because the game fails if its
rebuild reads as a different game.

1. Do not make Trace Echo a voice, a message or prophecy. It is a **spatial
   afterimage** — a personal perception of residual energy in structure.
2. Do not grant ability power on first acquisition. Every milestone is framed
   as baseline, not upgrade.
3. Do not make the Archive reveal supernatural truth. It reveals
   **administrative decisions**.
4. Do not warm Tamsin's starting disposition. She starts trust 15, suspicion 5
   — suspicious and barely trusting.
5. Do not invent a wider world, kingdoms, or political entities.
6. Do not assume beasts/creatures exist. No canon defines them.
7. Do not make the world post-apocalyptic-grim. It is fatigued civic
   infrastructure, not ruin porn.
8. Do not make the supernatural loud. Restraint is the tone.
9. Do not remove the `QUEST_DEAD_RELAY` solo/together fork or the failure branch.
10. Do not let progress be granted by a single button. Progress is earned.

## 9. Anti-pattern table

| Anti-pattern | Why it is wrong | Correct approach |
| --- | --- | --- |
| Mirrored profile on an asymmetric character | flips identity | author separately |
| Block/rect character art | geometry-built character | authored sprite pipeline |
| Reusing the neutral base as Jack | breaks paper-doll system | neutral base + identity layers |
| Recreating Tamsin from memory | drifts forbidden deviations | use `NPC_TAMSIN` record |
| Building from `main` | no content there | build from program branch |
| Inventing factions to fill a catalog | false canon | `NOT SPECIFIED IN DOCS` |
| Treating framework assets as NPCs | false canon | keep technical/non-canon |
| Icon that decides equipped state | duplicates engine logic | state binding in manifest |
| Anti-aliased edges | breaks pixel language | hard edges, binary alpha |
| Baked text in pixel art | illegible + unscalable | symbolic shapes, UI text |
| Cyan used decoratively | breaks colour semantics | Cyan = powered/active |
| Item icon with quality border baked in | wrong system | `UI_ITEM_QUALITY_FRAMES` |
| New scene for one changed lamp | wasted asset + drift | master + overlay |
| Hash match treated as approval | bytes ≠ art | visual QA required |
| Deleting superseded branches | destroys provenance | mark `SUPERSEDED` |

## 10. Documentation prohibitions

1. Do not silently override an existing authority document.
2. Do not omit a specification section — mark it `NOT APPLICABLE` with a reason.
3. Do not invent a value and present it as canon. Write
   `NOT SPECIFIED IN DOCS`.
4. Do not duplicate a rule in many places without marking the single authority.
5. Do not record conversational decisions here — that is `GAME_CONTEXT_LOGS`.
6. Do not record work progress here — that is `THE_GAME_MASTER_TASK_REGISTER`.
7. Do not store generated images as art in this corpus.
8. Do not let the corpus's angle documentation drift from the batch catalogs;
   the registry must remain mechanically verifiable against them.

## 11. How to challenge a prohibition

If a rebuild genuinely requires breaking a rule:

1. State which rule and why.
2. Propose the smallest change that satisfies the underlying need.
3. Update the rule here with the new wording and a reason.
4. Update every dependent layer that references it.
5. Log it in L0-08.

Never work around a prohibition silently. Silent workarounds are how a corpus
loses the ability to be trusted as an authority.