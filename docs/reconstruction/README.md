# THE GAME — Reconstruction Documentation Corpus

Status: **ACTIVE / LAYERED BUILD IN PROGRESS**
Repository: `jbob-coder/Text-rpg-game`
Authority branch: `docs/master-game-development-program`
Corpus version: `v1.0`
Corpus created: `2026-10-03`

---

## 1. What this corpus is

This directory is the **reconstruction corpus**: the layer of documentation whose
purpose is to make the game rebuildable from text alone.

It exists because the game must eventually be recreated — including its pixel-art
presentation — from documentation rather than from the surviving code of a
previous implementation attempt. The corpus is written so that:

- a coding agent with no access to the current runtime can implement the game;
- a pixel artist (human or AI) with no access to the original artwork can
  reconstruct every asset at its exact native grid;
- every visual asset can be rebuilt **from every angle**, not only from the
  angle that happened to be built first;
- every rule is stated once and referenced everywhere else, so contradictions
  cannot silently accumulate.

The corpus is **documentation only**. No production asset, no runtime change and
no gameplay implementation is created by this corpus. Documentation is
authoritative; code follows it later.

## 2. Layer model

The corpus is built in layers. Each layer depends only on the layers beneath it.
A layer is never weakened to avoid rewriting a lower layer; when a lower layer
changes, the dependent layers are updated and the change is logged.

| Layer | Name | Depends on | Purpose |
| --- | --- | --- | --- |
| **L0** | Foundation | — | Canon digest, angle standard, ID registries, shared vocabulary, rebuild protocol. Defines *how* this corpus documents things. |
| **L1** | Existing-state record | L0 | Every asset, file, branch and runtime binding that currently exists. Defines *what exists today*. |
| **L2** | Asset angle specifications | L0, L1 | Per-view reconstruction specification for every planned asset unit. Defines *how to draw each thing from each angle*. |
| **L3** | World angle specifications | L0, L2 | Location, environment, architecture and scene-angle reconstruction. Defines *what the places look like from every direction*. |
| **L4** | Character angle specifications | L0, L2 | Character identity, turnaround, layer, portrait and animation reconstruction. Defines *how people look from every angle*. |
| **L5** | Systems and narrative reference | L0 | World, systems, progression and story reconstruction reference. Defines *how the game plays and why*. |

### Reading order

Read `L0` first, in full. Everything else is written to be read on demand once
L0 is understood.

1. [L0-00 Reconstruction Objective and Protocol](L0/L0-00_RECONSTRUCTION_OBJECTIVE_AND_PROTOCOL.md)
2. [L0-01 Canon Digest](L0/L0-01_CANON_DIGEST.md)
3. [L0-02 Angle Standard](L0/L0-02_ANGLE_STANDARD.md)
4. [L0-03 Native Grid and Anchor Standard](L0/L0-03_NATIVE_GRID_AND_ANCHOR_STANDARD.md)
5. [L0-04 Palette and Material Standard](L0/L0-04_PALETTE_AND_MATERIAL_STANDARD.md)
6. [L0-05 Asset Unit Registry](L0/L0-05_ASSET_UNIT_REGISTRY.md)
7. [L0-06 Stable ID and Naming Standard](L0/L0-06_STABLE_ID_AND_NAMING_STANDARD.md)
8. [L0-07 Prohibitions and Failure Modes](L0/L0-07_PROHIBITIONS_AND_FAILURE_MODES.md)
9. [L0-08 Layer Index and Build Log](L0/L0-08_LAYER_INDEX_AND_BUILD_LOG.md)
10. [L0-09 Corpus Integrity Protocol](L0/L0-09_CORPUS_INTEGRITY_PROTOCOL.md)
11. [L0-10 Layer Stack Authority and Scene Composition](L0/L0-10_LAYER_STACK_AUTHORITY_AND_SCENE_COMPOSITION.md)

## 3. Relationship to existing documentation

This corpus does **not** replace the existing documentation tree. It is a
reconstruction-oriented sibling layer that references the existing tree as its
evidence base.

| Existing authority | Role relative to this corpus |
| --- | --- |
| `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md` | Top-level project authority. Corpus obeys it. |
| `docs/FINAL_GAME_RECONSTRUCTION_BLUEPRINT.md` | Integration blueprint. Corpus supplies its missing detail layer. |
| `docs/GAME_FOUNDATION.md` | Rules-engine canon. Corpus references, never contradicts. |
| `docs/assets/PIXEL_ASSET_MASTER_PLAN.md` | Native grid, anchor, z-order and lifecycle authority. Corpus is its per-angle expansion. |
| `docs/assets/CHARACTER_PIXEL_BLUEPRINTS.md` | Player and Tamsin identity authority. Corpus expands it into per-view specs. |
| `docs/assets/ASSET_PROVENANCE_REGISTRY.md` | Provenance schema authority. Corpus records provenance for its own documents. |
| `docs/assets/ASSET_MANIFEST_SCHEMA.md` | Machine-readable manifest contract. Corpus emits manifests in that shape. |
| `docs/world/*` | World canon authority. Corpus references it for L3/L5. |
| `docs/systems/*` | Systems canon authority. Corpus references it for L5. |

**Conflict rule.** If this corpus and an existing authority disagree, the
existing authority wins and the corpus is corrected. The corpus records such
corrections in `L0/L0-08_LAYER_INDEX_AND_BUILD_LOG.md`. The corpus never
silently overrides canon.

## 4. The angle requirement

The corpus's distinguishing obligation is **angle completeness**.

"Angle" in this corpus has two related meanings, both required:

1. **View angle** — a specific camera direction for a subject. For characters
   and character equipment this is the canonical six-view set defined in
   `L0-02_ANGLE_STANDARD.md`. For scenes and props it is a defined set of
   presentation angles rather than a character turnaround.
2. **Interpretive angle** — a distinct reading of a subject that a
   reconstruction could get wrong: identity, silhouette, material, light,
   scale, state, palette, occlusion, motion, camera, narrative function,
   accessibility, provenance and rebuild risk.

Every asset unit in L2 receives both: a per-view reconstruction specification
and an interpretive-angle analysis. An asset that has only a front view is
incomplete by construction.

## 5. Scale of the corpus

The corpus targets roughly **1,000,000 characters** of reconstruction-grade
documentation, built incrementally in layers rather than written in one pass.
Large volume is a consequence of the asset count (500 planned units plus the
existing 24 rasters) times the angle count (up to six views times twelve
interpretive angles), not an end in itself.

Density and correctness outrank length. Where a spec cannot be made specific,
it says so explicitly rather than padding.

## 6. What this corpus is not

It is not:

- a place to record conversational decisions (that is `GAME_CONTEXT_LOGS`);
- a place to record work progress (that is `THE_GAME_MASTER_TASK_REGISTER`);
- a place to record implementation evidence (that is `IMPLEMENTATION_STATUS`
  and `docs/evidence/`);
- a place to store generated images as art (references live under
  `docs/assets/references/` and never occupy a production asset path);
- permission to treat generated imagery as production art.

## 7. Change protocol

Any change to this corpus:

1. is made on a working branch, never on `main`;
2. records its intent in `L0/L0-08_LAYER_INDEX_AND_BUILD_LOG.md`;
3. respects the prohibitions in `L0/L0-07_PROHIBITIONS_AND_FAILURE_MODES.md`;
4. preserves stable IDs from `L0/L0-05_ASSET_UNIT_REGISTRY.md`;
5. updates any dependent layer that references the changed fact.

Rebuild progress for the game itself is tracked in
`docs/THE_GAME_MASTER_TASK_REGISTER.md`, not here.