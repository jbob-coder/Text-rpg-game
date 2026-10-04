# L1-00 — Preservation Priority and Perishable Evidence Register

Layer: **L1 Existing-state record**
Depends on: L0-08 (layer index and build log)
Purpose: record what exists **right now**, before it changes.

---

## 1. Why this document is first in L1

The owner has stated that:

- the game is being **evolved**, not merely preserved;
- the current beta APK will be **broken down**, and only some of it will remain;
- the reference photos and the APK are the material this reconstruction is
  being planned from;
- **this corpus is documentation only** — no pixel art will be produced here.

That combination makes some evidence perishable. Reference images held on an
external drive, and a working client whose UI surface is spread across 64
branches, are both at risk. If they are not recorded now, the rebuild loses
information that cannot be recovered from the repository later.

So L1 leads with capture, not with analysis.

**Ordering rule for L1:** capture raw state first, interpret it second. A
document that records *what exists* without deciding *what it means* is
recoverable; a document that interprets before capturing loses the raw fact.

## 2. What is perishable, ranked by urgency

| Rank | Item | Where it lives now | Risk | Captured in |
| ---: | --- | --- | --- | --- |
| 1 | Jack Wilson approved reference image | Google Drive file ID `1OrLsw_mvbZ5HipFObfX8wdvA7vAPa-Ve` | **HIGH** — external, auth-gated | §3.1, L1-02 |
| 2 | Batch 001 concept board | Google Drive file ID `1JDvlmF_Mfy93rs_Llq5rB444EOUF5Gzr` | **HIGH** — external, auth-gated | §3.2, L1-02 |
| 3 | Pixel RPG visual reference originals | Google Drive IDs `1IcZDQAEPUVpSpvJsvaVZsLqAA0RJmaxp`, `1NYHm1Y_CPQOb22ZQsF9e45T5uFV3Mh_b` | **HIGH** — sibling repo notes Drive "required sign-in at the last attempt" | §3.3 |
| 4 | The working Android client UI surface | 8,621 lines across 28 Kotlin files on `docs/master-game-development-program` | **MEDIUM** — branch breakdown may remove it | §4, L1-01 |
| 5 | The Python rules engine | 8,170 lines across 19 modules | **LOW** — on the same branch as everything else | §5 |
| 6 | Pixel raster/text-map masters | 24 PNGs + 9 Kotlin scene maps | **LOW** — committed, hash-verified | L1-02 |

### 2.1 What is NOT at risk

These are committed to the repository with verified hashes and can be
regenerated or re-read at any time:

- all five batch asset catalogs (the 500-unit plan);
- `content/vertical_slice_01.json` (the authored story);
- the 24 PNG rasters and 9 text-map scene masters;
- the corpus itself, once pushed.

## 3. External reference images — preservation register

Three reference images matter to `Text-rpg-game`, all held on Google Drive
rather than in the repository. Each is recorded here with the identity, hash,
scope and permitted use needed to validate it later. Two of the three are the
only sources for canon that cannot be re-derived from any document.

### 3.1 `UI_REFERENCE_CHARACTER_APPROVED_V1` — the highest-value item

| Field | Value |
| --- | --- |
| Reference ID | `UI_REFERENCE_CHARACTER_APPROVED_V1` |
| Status | `REFERENCE_SELECTED / CHARACTER_TAB_APPROVED` |
| Scope | Jack Wilson Character-tab visual identity/presentation |
| Location | Google Drive file ID `1OrLsw_mvbZ5HipFObfX8wdvA7vAPa-Ve` |
| SHA-256 (recorded) | `af453993693ff0447da3a1bf07e0276013f0c87f6a69442f86c5f3192487d867` |
| Durable audit | `docs/assets/references/UI_REFERENCE_CHARACTER_APPROVED_V1.md` |

**Allowed use:** Jack visual identity, human proportions, silhouette, layered
clothing/equipment presentation, character-art alignment across UI scales.

**Rejected use:** gameplay stat authority, hidden state, collision/hitbox
geometry, exact 32x48 anchors, unseen turnaround views, animation timing.

**Why this is the single most important reference in the project.** It is the
only approved source for the player's visual identity. Every player asset in a
rebuild — base, hair, equipment alignment, portraits, animation masters — traces
back to it. If it becomes unreachable, the player character becomes
re-constructible only from prose, which is precisely the failure the corpus
exists to prevent.

**Outstanding action (owner-side, not agent-side).** The recorded SHA-256 means
integrity can be verified *if* the file is retrieved. Retrieval requires Drive
access. The corpus records the identity, hash, scope and permitted use so the
asset can be validated byte-for-byte once obtained.

### 3.2 `REF_BATCH001_CONCEPT_BOARD_A`

| Field | Value |
| --- | --- |
| Reference ID | `REF_BATCH001_CONCEPT_BOARD_A` |
| Status | `REFERENCE_GENERATED / STYLE_DIRECTION_ACCEPTED / CANON_GEOMETRY_REJECTED` |
| Scope | Broad Batch 001 style probe |
| Location | Google Drive file ID `1JDvlmF_Mfy93rs_Llq5rB444EOUF5Gzr` |
| SHA-256 (recorded) | `2d52f5364cecd1338e3c4cd0eafdbba7d5575e980f4c3d7856db3c6119e83ec8` |
| Durable audit | `docs/assets/references/REF_BATCH001_CONCEPT_BOARD_A.md` |

**Allowed use:** pixel-density direction, modular sheet layout, dark industrial
value language, restrained cyan/gold accents, icon/scene/FX family coherence.

**Rejected use:** canon player face, canon Tamsin geometry, item existence,
courier identity, district architecture, relay state contract.

This is a **style** reference, not a geometry reference. Its invented details
are explicitly rejected as canon. Recording that rejection matters as much as
recording the acceptance: a rebuild that treats this board as geometry would
invent a different game.

### 3.3 Sibling-repository references (`pixel-rpg-goblin-underwater`)

These belong to a **different repository** and are recorded here only to prevent
them being confused with `Text-rpg-game` canon.

| Title | Drive ID | Note |
| --- | --- | --- |
| Pixel RPG — Visual Reference ORIGINAL.png | `1IcZDQAEPUVpSpvJsvaVZsLqAA0RJmaxp` | Byte identity and equivalence to the village concept **not established** |
| Pixel RPG — Visual Reference.jpg | `1NYHm1Y_CPQOb22ZQsF9e45T5uFV3Mh_b` | Smaller working copy |

That repo's own `VISUAL_REFERENCE_ASSETS.md` records that the reported
`voxel_fantasy_village_gate.png` full image **is not supplied**, that the Drive
links required sign-in at the last attempt, and that "Metadata and derivative
crops do not replace the full photo."

**Consequence for this corpus.** Any visual target that exists *only* as a
cross-repository Drive reference is **not currently reconstructible**. This is
recorded as a real gap rather than quietly worked around.

### 3.4 Reference persistence policy (restated)

From `REFERENCE_REGISTRY.md`:

> Persist selected and materially useful references **outside the APK** in a
> durable source store.

Production PNGs and manifests belong in the repository only after
reconstruction and QA. Large concept boards should remain outside the
repository unless there is a specific reason to version them there.

**The corpus follows this.** It records reference identity, hash, scope and
permitted use — never the image bytes.

## 4. The beta APK's UI surface — what "only some will remain" must cover

The APK is built from the Kotlin client. Its visual substance is 8,621 lines
across 28 files in `android/app/src/main/java/com/thegame/rpg/ui/`, containing
**23 pixel catalogs** and **192 distinct asset IDs**.

The 24 PNG rasters are a *subset*. The other 168 IDs exist only as Kotlin
text-map definitions, and would be lost with the branches if they are not
recorded.

### 4.1 Catalog inventory

| Catalog | File | Lines | Stable IDs | PixelSprites |
| --- | --- | ---: | ---: | ---: |
| `PixelAssetCatalog` | PixelAssetCatalog.kt | 963 | 15 | 16 |
| `PixelSceneCatalog` | PixelSceneCatalog.kt | 824 | 9 | 9 |
| `PixelUiIconCatalog` | PixelUiIconCatalog.kt | 512 | 15 | 15 |
| `PixelEquipmentSlotCatalog` | PixelEquipmentSlotCatalog.kt | 456 | 12 | 12 |
| `PixelEnvironmentPropCatalog` | PixelEnvironmentPropCatalog.kt | 422 | 10 | 10 |
| `PixelComponents` | PixelComponents.kt | 356 | 0 | 9 |
| `PixelSceneOverlayCatalog` | PixelSceneOverlayCatalog.kt | 336 | 5 | 4 |
| `PixelStatsSection` | StatsSection.kt | 329 | 0 | 0 |
| `PixelUiChromeCatalog` | PixelUiChromeCatalog.kt | 306 | 17 | 0 |
| `PixelSceneIllustration` | SceneIllustration.kt | 289 | 0 | 8 |
| `PixelMapArtCatalog` | PixelMapArtCatalog.kt | 288 | 1 | 1 |
| `PixelTraceFxCatalog` | PixelTraceFxCatalog.kt | 207 | 3 | 3 |
| `PixelStoryActorCatalog` | PixelStoryActorCatalog.kt | 198 | 2 | 2 |
| `PixelEnvironmentModuleCatalog` | PixelEnvironmentModuleCatalog.kt | 190 | 4 | 2 |
| `PixelMapTravelTransitionCatalog` | PixelMapTravelTransition.kt | 169 | 1 | 2 |
| `PixelMapMarkerCatalog` | PixelMapMarkerCatalog.kt | 167 | 5 | 5 |
| `PixelEnvironmentDecalCatalog` | PixelEnvironmentDecalCatalog.kt | 129 | 2 | 2 |
| `PixelEnvironmentOverlayCatalog` | PixelEnvironmentOverlayCatalog.kt | 125 | 2 | 3 |
| `PixelRasterCatalog` | PixelRasterCatalog.kt | 110 | 0 | 0 |
| `StatusComponents` | StatusComponents.kt | 107 | 0 | 0 |
| `PixelTraceStrainCatalog` | PixelTraceStrainCatalog.kt | 97 | 2 | 2 |
| `PixelUiUtilityCatalog` | PixelUiUtilityCatalog.kt | 88 | 0 | 2 |
| `PixelItemQualityFrameCatalog` | PixelItemQualityFrameCatalog.kt | 76 | 2 | 1 |
| `PixelColors` | PixelTheme.kt | 62 | 0 | 0 |
| `PixelCharacterStagingCatalog` | PixelCharacterStagingCatalog.kt | 51 | 1 | 1 |
| `PixelEnvironmentPreview` | PixelEnvironmentPreview.kt | 44 | 0 | 1 |
| `GameScreen` | GameScreen.kt | 1473 | 0 | 4 |
| `CharacterSection` | CharacterSection.kt | 247 | 0 | 0 |

**Reading.** `PixelUiChromeCatalog` has 17 IDs but zero PixelSprites — its art is
defined structurally, not as pixel rows. `PixelRasterCatalog` has zero IDs and
zero sprites — it is the binding table that maps asset symbols to Android
drawables. Both are recorded because a rebuild needs to know they exist and what
they do, even though neither is art.

### 4.2 What this means for the rebuild

The APK's presentation is not "24 PNGs". It is **24 PNGs plus 168 Kotlin-defined
pixel assets plus the structural chrome**. The corpus must therefore treat the
Kotlin catalogs as **source masters in their own right**, not as throwaway
implementation. `PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md` §8 already classifies
them as **Type B — source-native PixelSprite/text-map definition**, explicitly
"acceptable production form if intentionally authored and visually approved."

### 4.3 Navigation surface

Seven bottom-navigation identities, each a stable asset ID:

| Nav slot | Asset ID |
| --- | --- |
| Story | `UI_NAV_STORY_ICON` |
| Character | `UI_NAV_CHARACTER_ICON` |
| Stats | `UI_NAV_STATS_ICON` |
| Inventory | `UI_NAV_INVENTORY_ICON` |
| Quests | `UI_NAV_QUESTS_ICON` |
| Map | `UI_NAV_MAP_ICON` |
| More/Settings | `UI_NAV_MORE_SETTINGS_ICON` |

Active colour is applied by UI state, **not** baked into a duplicate icon.

## 5. The Python rules engine

8,170 lines across 19 modules under `src/textrpg/`, plus 6,959 lines across 21
test files.

| Module | Lines | Responsibility |
| --- | ---: | --- |
| `powers.py` | 2061 | ability/technique/mastery system |
| `validation.py` | 782 | content and state validation |
| `android_bridge.py` | 776 | engine ↔ client boundary |
| `core.py` | 793 | authoritative `GameState`, checks, effects |
| `social.py` | 680 | NPC personality, relationships, knowledge |
| `quests.py` | 471 | quest graph and stages |
| `status.py` | 460 | conditions and status effects |
| `modifiers.py` | 348 | modifier resolution |
| `simulation.py` | 339 | resolution and determinism |
| `equipment.py` | 182 | equipment slots and legality |
| `stats.py` | 216 | attributes, skills, derived stats |
| `progression.py` | 194 | XP and advancement |
| `visuals.py` | 180 | machine-readable identity contract |
| `cli.py` | 156 | command interface |
| `content.py` | 139 | content loading |
| `schema.py` | 114 | schema and derived-value formulas |
| `persistence.py` | 88 | save/load and migrations |
| `json_contract.py` | 24 | JSON contract |
| `__init__.py` | 167 | package surface |

`powers.py` alone is 2,061 lines — larger than any UI catalog. The engine, not
the art, is the substantial half of this project.

**Preservation status.** These modules live on the same branch as the docs, so
they are not individually perishable. But their *behaviour* is what L5 must
document, and behaviour cannot be recovered from branch history once rewritten.

## 6. Branch stack — recorded before breakdown

**60 remote branches** (61 refs including the `HEAD -> main` symref), measured
mechanically during L1 capture. The rebuild must know which content is settled
and which is stacked work.

The earlier corpus survey recorded "64 branches" from a pre-fetch listing; the
authoritative post-fetch count is **60**. Corrected here.

| Branch group | Count | Nature |
| --- | ---: | --- |
| `feature/*` | 33 | visual asset production, ability iterations, Android client |
| `docs/*` | 7 | documentation programs and plans |
| `integration/*` | 7 | ability-system reconciliation, Android open world |
| `fix/*`, `review/*` | 6 | contract hardening, runtime recovery |
| `prototype/*`, `shared/*` | 4 | combat contracts, shared game context |
| `context/*`, `foundation/*` | 2 | shared context, text-rpg systems |
| `main` | 1 | **empty** — 2-line README, 1 commit |

**Governing rules already recorded in the repository:**

- `main` is **not** the canonical implementation branch;
- historical V6 and Android branches are **evidence sources**, not product
  authority;
- do not infer that the newest PR number is automatically canonical;
- branch/HEAD awareness is required for every production stage claim.

### 6.1 Most recent activity

| Date | Files | Branch |
| --- | ---: | --- |
| 2026-10-03 | 354 | `docs/master-game-development-program` ← **canonical tip** |
| 2026-10-02 | 256 | `docs/settlement-region-build-plan` |
| 2026-10-02 | 199 | `docs/text-pixel-rpg-master-program` |
| 2026-10-01 | 204 | `docs/master-documentation-program` |
| 2026-10-01 | 195 | `feature/gate-twelve-map-surface-texture` |
| 2026-10-01 | 190 | `feature/player-avatar-art-pass` |

The last two entries show that **visual asset branches were still landing after
the documentation branches**. Documentation-first did not mean art-finished.

### 6.2 The stack-order problem

The newest branch is not automatically the most complete. Several distinct
branches share the same commit SHA, which means work was duplicated or merged
in ways that commit-graph inspection alone cannot resolve:

- `feature/pixel-map-art-pass` and `feature/player-base-art-pass` → both `59a1930961ae5fc961acab5624dcbfcc2f7e66cbcc`;
- `feature/service-tunnel-ambient-animation` and `...-arrival-pixel-art` → both `2f7f77d7925e94558d219d4ab2340fbb32476717`;
- `integration/rules-ability-v3` and `v4` → both `f7a2a685105ed06255d856afee1a9eee5390eecd`.

`ASSET_PROVENANCE_REGISTRY.md` §8 requires every promoted asset to record the
branch where it was authored and the branch where it was integrated, and states
that later refinement existence and supersession must be recorded. That
requirement stands. L1 records the observed state; it does not resolve it.

## 7. What "documentation only" means for this corpus

Stated explicitly so a later pass cannot drift:

| The corpus does | The corpus does not |
| --- | --- |
| specify assets view by view | produce any pixel art |
| record reference identity and hash | store reference image bytes |
| record palettes, anchors, silhouettes as specification | render or export PNGs |
| document the engine's behaviour | modify engine code |
| document the client's UI surface | modify client code |
| record existing raster evidence | regenerate or replace rasters |
| define acceptance criteria | claim QA that was not performed |

The one machine artefact L1 writes is a **JSON evidence file describing existing
assets**. It contains no image data. This keeps the corpus inside its
documentation-only boundary while still making the existing state machine-
readable.

## 8. Preservation checklist

For each perishable item, the corpus records enough that the item can be
restored or verified later:

| Item | Identity | Hash | Scope | Permitted use | Rejected use | Audit note |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| Jack Wilson reference | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Batch 001 concept board | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Pixel RPG originals | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ |
| APK UI catalogs | ✅ | ✅ | ✅ | ✅ | ✅ | this document |
| Python engine | ✅ | ✅ | ✅ | ✅ | ✅ | §5 |
| 24 rasters | ✅ | ✅ | ✅ | ✅ | ✅ | L1-02 |

**Everything perishable is now identified, hashed where a hash exists, and
scoped.** What remains genuinely unavailable is the *image bytes* of the Drive
references, which requires owner-side retrieval. That is recorded as an open
action, not as a completed task.