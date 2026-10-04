# L1-01 — Branch and Runtime Surface Inventory

Layer: **L1 Existing-state record**  
Depends on: L1-00 (preservation priority)  
Machine-readable companion: `L1-01_branch_inventory.json`

---

## 1. Purpose

Records the branch topology and the runtime surface that exist today, so a
rebuild knows what was in flight and what the client actually contained. This
is captured **before** the branch breakdown, per L1-00 §1.

## 2. Branch count

**61 branches** (the ref count including `HEAD -> main` is 61).

| Group | Count |
| --- | ---: |
| `feature` | 33 |
| `docs` | 7 |
| `integration` | 7 |
| `fix` | 3 |
| `review` | 3 |
| `prototype` | 2 |
| `shared` | 2 |
| `HEAD -> main` | 1 |
| `context` | 1 |
| `foundation` | 1 |
| `main` | 1 |
| **total** | **61** |

## 3. Governing rules already in force

- `main` is **not** the canonical implementation branch.
- Historical V6 and Android branches are **evidence sources**, not product authority.
- Do not infer that the newest PR number is automatically canonical.
- Branch/HEAD awareness is required for every production-stage claim (`ASSET_PROVENANCE_REGISTRY.md` §8).
- The canonical tip is `docs/master-game-development-program`.

## 4. The full branch table

`files` is the total tracked file count at that branch head.

| Branch | Head SHA | Date | Files | Category |
| --- | --- | --- | ---: | --- |
| `docs/master-game-development-program` | `2111addc1` | 2026-10-03 | 354 | Documentation program |
| `docs/text-pixel-rpg-master-program` | `8bc462dfb` | 2026-10-02 | 199 | Documentation program |
| `docs/settlement-region-build-plan` | `65d2db853` | 2026-10-02 | 256 | Documentation program |
| `feature/story-pixel-resource-hud` | `d80aee802` | 2026-10-01 | 187 | Feature — art / client / systems |
| `feature/service-tunnel-scene-art-pass` | `d19e6edba` | 2026-10-01 | 191 | Feature — art / client / systems |
| `feature/service-tunnel-atlas-detail` | `b5cb51040` | 2026-10-01 | 191 | Feature — art / client / systems |
| `feature/service-tunnel-arrival-pixel-art` | `2f7f77d79` | 2026-10-01 | 191 | Feature — art / client / systems |
| `feature/service-tunnel-ambient-animation-stack` | `19807863e` | 2026-10-01 | 198 | Feature — art / client / systems |
| `feature/service-tunnel-ambient-animation` | `2f7f77d79` | 2026-10-01 | 191 | Feature — art / client / systems |
| `feature/quiet-stair-scene-art-pass` | `7adacd474` | 2026-10-01 | 191 | Feature — art / client / systems |
| `feature/player-base-art-pass` | `59a193096` | 2026-10-01 | 189 | Feature — art / client / systems |
| `feature/player-avatar-art-pass` | `494f2b3f0` | 2026-10-01 | 190 | Feature — art / client / systems |
| `feature/pixel-map-art-pass` | `59a193096` | 2026-10-01 | 189 | Feature — art / client / systems |
| `feature/opening-story-actor-pixel-art` | `9f3cf1936` | 2026-10-01 | 191 | Feature — art / client / systems |
| `feature/mobile-skills-pixel-layout` | `141192bbd` | 2026-10-01 | 191 | Feature — art / client / systems |
| `feature/mobile-bag-pixel-art` | `f4f8d4c81` | 2026-10-01 | 191 | Feature — art / client / systems |
| `feature/gate-twelve-map-surface-texture` | `b0e22782a` | 2026-10-01 | 195 | Feature — art / client / systems |
| `docs/visual-integration-recovery-plan` | `fe83ad845` | 2026-10-01 | 188 | Documentation program |
| `docs/master-documentation-program` | `9a7609521` | 2026-10-01 | 204 | Documentation program |
| `docs/gate-twelve-map-pixel-asset-blueprint` | `b6e2d97c3` | 2026-10-01 | 195 | Documentation program |
| `fix/player-hub-runtime-recovery` | `93f8be13d` | 2026-09-30 | 153 | Hardening / review |
| `fix/avatar-overlay-rig-contract` | `7d4558ea5` | 2026-09-30 | 142 | Hardening / review |
| `feature/story-scene-first-pixel-art` | `5a8151a56` | 2026-09-30 | 161 | Feature — art / client / systems |
| `feature/png-pixel-art-runtime-a` | `c11133122` | 2026-09-30 | 187 | Feature — art / client / systems |
| `feature/player-safe-stat-inspection` | `7cba26a4c` | 2026-09-30 | 142 | Feature — art / client / systems |
| `feature/player-safe-skills-ui` | `2f50abe77` | 2026-09-30 | 142 | Feature — art / client / systems |
| `feature/pixel-assets-runtime-expansion` | `ddbb5f425` | 2026-09-30 | 161 | Feature — art / client / systems |
| `feature/pixel-assets-existing-reuse-b` | `623cf9bb9` | 2026-09-30 | 161 | Feature — art / client / systems |
| `feature/pixel-asset-wave-m-diagnostic-reader` | `063d58794` | 2026-09-30 | 145 | Feature — art / client / systems |
| `feature/pixel-asset-wave-l-environment-modules` | `54a40bb5a` | 2026-09-30 | 145 | Feature — art / client / systems |
| `feature/pixel-asset-wave-a` | `a3970de65` | 2026-09-30 | 142 | Feature — art / client / systems |
| `feature/character-stats-inspection` | `791a839b2` | 2026-09-30 | 151 | Feature — art / client / systems |
| `feature/character-equipment-paperdoll-ui` | `40c95ec2e` | 2026-09-30 | 142 | Feature — art / client / systems |
| `context/shared-game-context` | `817b957ba` | 2026-09-30 | 369 | Shared context |
| `shared/game-context` | `76d5b3056` | 2026-09-27 | 44 | Shared context |
| `prototype/medieval-crystal-contracts` | `ed3d8744e` | 2026-09-27 | 60 | Prototype / foundation |
| `prototype/medieval-crystal-combat-contracts` | `29c69788b` | 2026-09-27 | 71 | Prototype / foundation |
| `integration/rules-ability-v6-reconcile` | `7f5f104fb` | 2026-09-27 | 45 | Integration |
| `integration/android-open-world-v1-reconcile` | `444063731` | 2026-09-27 | 89 | Integration |
| `fix/v6-runtime-boundaries` | `7be1adef2` | 2026-09-27 | 60 | Hardening / review |
| `feature/android-runtime-bootstrap-v1` | `6a68b960e` | 2026-09-27 | 75 | Feature — art / client / systems |
| `feature/android-pixel-client-v1` | `17aac1474` | 2026-09-27 | 87 | Feature — art / client / systems |
| `feature/android-open-world-v1` | `3faec5d44` | 2026-09-27 | 87 | Feature — art / client / systems |
| `docs/pixel-asset-production-plan-v1` | `a997a3b25` | 2026-09-27 | 111 | Documentation program |
| `shared/game-context-ui-sync` | `1090c9204` | 2026-09-26 | 35 | Shared context |
| `review/effective-stat-contract-hardening-v3` | `7212193c0` | 2026-09-26 | 40 | Hardening / review |
| `review/effective-stat-contract-hardening-v2` | `eec7ca8a9` | 2026-09-26 | 38 | Hardening / review |
| `review/effective-stat-contract-hardening` | `08a4ff863` | 2026-09-26 | 29 | Hardening / review |
| `main` | `6f8d9c5bf` | 2026-09-26 | 1 | main (empty) |
| `integration/rules-ability-v5` | `fd36b9f1d` | 2026-09-26 | 44 | Integration |
| `integration/rules-ability-v4` | `f7a2a6851` | 2026-09-26 | 43 | Integration |
| `integration/rules-ability-v3` | `f7a2a6851` | 2026-09-26 | 43 | Integration |
| `integration/rules-ability-v2` | `46deba017` | 2026-09-26 | 44 | Integration |
| `integration/rules-ability-v1` | `7bb7b519b` | 2026-09-26 | 42 | Integration |
| `foundation/text-rpg-systems` | `b3340bc38` | 2026-09-26 | 38 | Prototype / foundation |
| `feature/effective-stat-pipeline` | `1f9afb4e4` | 2026-09-26 | 27 | Feature — art / client / systems |
| `feature/ability-progression-v4` | `932bd74c4` | 2026-09-26 | 37 | Feature — art / client / systems |
| `feature/ability-progression-v3` | `767949472` | 2026-09-26 | 37 | Feature — art / client / systems |
| `feature/ability-progression-v2` | `36aadb4be` | 2026-09-26 | 34 | Feature — art / client / systems |
| `feature/ability-progression-v1` | `535a5d63e` | 2026-09-26 | 29 | Feature — art / client / systems |
| `HEAD -> main` | `origin/HE` |  | 1 | Other |

## 5. Duplicate head SHAs

Three pairs of branches point at the **same commit**. This means work was
duplicated, or merged in a way the commit graph cannot distinguish. It is the
concrete form of the stack-order problem `ASSET_PROVENANCE_REGISTRY.md` §8 warns
about: *do not infer that the newest PR number is automatically canonical.*

| SHA | Branches |
| --- | --- |
| `59a193096` | `feature/pixel-map-art-pass`, `feature/player-base-art-pass` |
| `2f7f77d79` | `feature/service-tunnel-ambient-animation`, `feature/service-tunnel-arrival-pixel-art` |
| `f7a2a6851` | `integration/rules-ability-v3`, `integration/rules-ability-v4` |

Because these pairs share a head, **content comparison alone cannot
separate them**. A rebuild that needs the difference must diff against their
merge bases or compare against `docs/master-game-development-program`.

## 6. Runtime surface — the APK's composition

The APK's substance is a Kotlin/Compose client over a Python engine.

| Component | Files | Lines | Notes |
| --- | ---: | ---: | --- |
| Kotlin UI (`ui/`) | 28 | 8,621 | 23 pixel catalogs, 192 distinct asset IDs |
| Kotlin runtime core | 2 | 375 | `GameViewModel.kt` 309, `MainActivity.kt` 66 |
| Python engine (`src/textrpg/`) | 19 | 8,170 | authoritative game state |
| Python tests | 21 | 6,959 | |
| PNG rasters | 24 | — | binary transparency, unique by hash |
| Text-map scene masters | 9 | 824 | Kotlin `PixelSprite` row definitions |
| Scene overlays (Kotlin) | — | 336 | separate from base scene masters |

### 6.1 The 192-ID surface

24 assets exist as PNG. The remaining **168 IDs exist only as Kotlin text-map
definitions** and would be lost if the client branches are removed. This is the
single strongest argument for L1 existing at all: the APK's real art surface is
roughly seven times larger than its raster count.

Per-catalog detail is in `L1-00` §4.1.

## 7. What this means for the rebuild

1. Do not rebuild from `main`. It is empty.
2. Do not assume 24 assets is the art surface. It is 192 IDs.
3. Treat Kotlin `PixelSprite` text maps as **source masters** (Type B), not
   throwaway implementation.
4. Resolve the three duplicate-head pairs by diffing merge bases, not by
   assuming recency.
5. `powers.py` (2,061 lines) is the largest single module in the project. The
   engine, not the art, is the substantial half.
