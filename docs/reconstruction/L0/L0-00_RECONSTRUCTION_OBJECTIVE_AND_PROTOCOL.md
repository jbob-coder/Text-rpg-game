# L0-00 — Reconstruction Objective and Protocol

Layer: **L0 Foundation**
Depends on: nothing
Governs: every other document in this corpus

---

## 1. The objective

The game will be rebuilt from documentation. This corpus is the material that
makes that possible.

The rebuild has two halves that must both succeed:

**Narrative and systems half.** An agent must be able to read this corpus and
implement the rules engine, content, progression, world and story such that the
result behaves as the intended game, with the same state transitions, the same
determinism guarantees, the same player-visible consequences and the same
player-safety boundaries.

**Presentation half.** An artist or agent must be able to read this corpus and
reconstruct every pixel asset — at its exact native grid, in every required
angle, with correct palette, material, light direction, anchors, occlusion and
state semantics — without seeing any original artwork.

The presentation half is where this corpus does the most work, because pixel
art is the hardest part to recover from prose. A rule can be stated once. An
angle cannot: it must be stated per view.

## 2. Why angle documentation is the core obligation

Consider what "the player character" means as documentation. If it says only
"the player character", a rebuilder must guess. Guessing produces a different
character each time, and the game's identity drifts with every rebuild.

The angle set removes the guess by fixing the observation conditions. Once the
observation conditions are fixed — six named camera positions, a fixed native
grid, fixed anchors, a fixed light direction, a fixed palette — the remaining
freedom is small enough to reconstruct faithfully.

This is why the corpus documents angles first and everything else second.
Angles are the high-information, low-ambiguity part of the specification.

## 3. Reconstruction fidelity definition

An asset is **faithfully reconstructed** when all of the following are true.

### 3.1 Grid fidelity

- Rendered at the declared native grid exactly.
- No scaling to a different native size.
- No fractional pixel placement.
- Pivot/anchor lands on the declared coordinate.

### 3.2 Pixel fidelity

- Hard pixel edges; no anti-aliasing in shipped assets.
- Binary transparency on ordinary sprite edges.
- Palette within the declared colour budget.
- Material ramps distinguishable from one another.

### 3.3 Angle fidelity

- Every declared view exists as a distinct asset, not a mirrored stand-in where
  asymmetry exists.
- Apparent height, head size, shoulder span and hand/foot scale stay consistent
  across all views of one subject.
- Silhouette remains readable at 1x in every view.
- Identity survives in every view, not only the front view.

### 3.4 Identity fidelity

- Named characters are recognisable in black silhouette.
- Asymmetric identity markers appear on the correct anatomical side.
- No identity leaks into a neutral body base that must stay neutral.

### 3.5 Semantic fidelity

- The asset's visibility is driven by authoritative state, never by its own
  pixels.
- Asset state variants correspond to real game states, not arbitrary recolours.
- No asset reveals hidden authored state.
- No asset duplicates a rule the engine owns.

### 3.6 Provenance fidelity

- Reference, blueprint, master, export and runtime stage are distinguishable.
- Hashes identify bytes, not approval.
- Superseded work is preserved and pointed at, not deleted.

## 4. The twelve interpretive angles

Every asset unit in this corpus is documented against twelve interpretive
angles. These are the questions a reconstruction can get wrong that view
direction alone does not constrain.

| # | Angle | The question it answers |
| ---: | --- | --- |
| 1 | **Identity** | What makes this subject recognisably itself, and what must never change? |
| 2 | **Silhouette** | What does the subject read as in pure black at 1x? |
| 3 | **Material** | What is it made of, and how do metal, cloth, skin, glass and powered surfaces differ? |
| 4 | **Light** | Where does light come from, what direction, what colour temperature, what does it occlude? |
| 5 | **Scale and proportion** | How big, relative to what, and by what measured anchor? |
| 6 | **State** | Which real game states change this asset, and how? |
| 7 | **Palette** | Which colours, how many, which are anchors and which are derived? |
| 8 | **Occlusion and layering** | What covers what, in which z-order, with which masks? |
| 9 | **Motion** | How does it move, at what cadence, with what frame contract? |
| 10 | **Camera and presentation** | How is it framed, cropped, scaled and transitioned on device? |
| 11 | **Narrative function** | What story job does it do, and what does its presence tell the player? |
| 12 | **Provenance and rebuild risk** | Where did it come from, and how likely is a rebuild to get it wrong? |

An asset that answers all twelve has a complete specification. An asset that
answers only views has an incomplete one, regardless of how many views it has.

## 5. Documentation unit contract

Every asset specification in this corpus follows the same structure.

```markdown
# <ASSET_ID> — <Display Label>

## Identity record          (interpretive angle 1)
## View set declaration     (which views exist, which do not, and why)
## Per-view specification   (one block per view)
## Silhouette analysis      (angle 2)
## Material specification   (angle 3)
## Light specification     (angle 4)
## Scale and proportion     (angle 5)
## State model              (angle 6)
## Palette specification    (angle 7)
## Occlusion and layering   (angle 8)
## Motion contract          (angle 9)
## Camera and presentation  (angle 10)
## Narrative function       (angle 11)
## Provenance and rebuild risk (angle 12)
## Reconstruction checklist (verifiable acceptance list)
## Known gaps and prohibitions
```

Sections may be marked `NOT APPLICABLE` with a reason. They may never be
silently omitted — an omitted section is indistinguishable from a forgotten
one, and a rebuilder cannot tell which it is.

## 6. View angle determination

The view set for an asset family is fixed by L0-02, not chosen per asset. The
determination rules are:

1. **Directional character bodies** (player bases, NPCs) use the full six-view
   turnaround. This is mandatory.
2. **Character equipment layers** use the six-view set only for the views the
   movement renderer can request. Wave A equipment may ship front-only, but the
   specification must define the full set and mark the unshipped views `DEFERRED`
   with the reason.
3. **Held props and interactive props** use a presentation-angle set: the views
   the story and interaction model can present.
4. **Location scenes** are single-camera and use one primary angle plus
   documented state variants. A location scene is not a turnaround subject; its
   "angles" are camera framings and architectural axes.
5. **Tiles, modules and atlases** document the axes they tile along and the
   seam behaviour, not view angles.
6. **UI icons, frames and FX** document presentation states rather than camera
   angles.

A family that does not match any of these has no defined view set and must be
assigned one in L0-02 before it is documented. Inventing a view set ad hoc is a
prohibition (see L0-07).

## 7. Determinism and inspectability

The corpus is written for deterministic reconstruction.

- Same corpus + same rules engine version = same game state transitions.
- Same corpus + same asset masters = same bytes in the shipped assets.
- Same save state + same seed + same action = same resolution.

This means the corpus must avoid describing outcomes in prose alone where a rule
is intended. A rule that can be computed must be written so it can be computed.

## 8. The player-safe boundary

Every asset specification carries a visibility contract. The corpus restates the
boundary because it is the most frequently violated rule in visual work:

- Visual assets may depend only on player-safe projection.
- Hidden authored state must never drive a player-visible asset.
- Spoiler risk is recorded per asset.
- A visual never asserts a fact the engine has not made visible.

This applies to UI icons, map markers, scene state variants, item quality frames,
FX, status overlays and equipment layers alike.

## 9. Verification

A specification is verified when:

- every declared view has a written specification, or is explicitly deferred
  with a reason;
- every anchor referenced is declared in L0-03;
- every palette colour referenced is declared in L0-04 or locally justified;
- every asset ID referenced exists in L0-05;
- every prohibition that applies is restated locally;
- no section is empty;
- a second reader could reconstruct the asset without asking a question that
  the corpus does not answer.

## 10. How to use this corpus to rebuild the game

The intended rebuild sequence is:

1. Read all of L0.
2. Read L1 to learn the existing state and its evidence.
3. Read L2 for the asset masters you need, and produce native pixel assets.
4. Read L3 for locations and L4 for characters.
5. Read L5 for world, systems and narrative.
6. Implement the rules engine from L5 and the systems authorities.
7. Implement presentation from L2–L4.
8. Verify against the reconstruction fidelity definition in this document.

Steps 3 and 6 may proceed in parallel. Neither may proceed before step 1.