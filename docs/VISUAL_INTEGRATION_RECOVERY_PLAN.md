# Visual Integration Recovery Plan

Status: planning / documentation only
Repository: jbob-coder/Text-rpg-game
Baseline: PR #19 head c11133122d47009abc71e8c6e91c08aedbe91ae2
Date: 2026-10-01

## Objective

Recover the intended pixel-art presentation of THE GAME without replacing gameplay authority or inventing unsupported canon.

The current problem is not merely missing PNG delivery. Phone evidence and repository history show a broader presentation gap: scenes, the player, and HUD can still read as technical/geometric even though authored pixel masters and earlier approved visual references exist.

## Confirmed constraints

- main is a placeholder and is not implementation authority.
- PR #19 is stacked on PR #18.
- Keep PixelSprite source masters and fallback behavior.
- Prefer mapped PNG raster delivery when present.
- Preserve nearest-neighbor rendering.
- UI consumes player-safe projected state; Compose does not inspect hidden/raw world flags to choose art.
- Preserve established asset IDs and gameplay bindings.
- Preserve paper-doll 32x48 coordinate space, shared origin/pivot, slot and z-order.
- An equipped item without approved mapped geometry remains logically equipped without invented visual geometry.
- Current technical player hair is non-canonical.
- Do not invent final player/NPC anatomy without an approved reference.
- Emulator QA and Galaxy A03 physical-device acceptance are separate gates.

## Visual gap to fix

### 1. Environment / map presentation

Problem: environments can read as geometric diagrams instead of authored game scenes.

Direction:
- Existing legitimate scene art and tiles become visual authority.
- Compose geometry is limited to layout, hit regions, masks, state overlays, and interaction support.
- Reuse existing PixelScene, environment overlay, prop-catalog, sprite-placement, Wave I, and raster assets before creating new art.
- Start with Platform Nine, then major current Story locations.

### 2. Player / equipment presentation

Problem: the base avatar still reads as a technical sprite.

Direction:
- Inventory all existing approved player references before redesign.
- Distinguish canonical references from technical placeholders.
- Preserve current paper-doll contracts.
- Integrate approved base/body/appearance art when found.
- Do not promote technical hair or improvised anatomy to canon.
- Existing equipment layers remain aligned and composable.

### 3. HUD / game display

Problem: current panels/boxes do not yet carry the complete approved pixel-art language.

Direction:
- Recover palette, frames, icon treatment, spacing, panel treatment and hierarchy from approved project references.
- Replace generic-looking presentation incrementally rather than rewriting all Compose UI.
- Add a dynamic HP presentation driven only by projected player-safe values.
- HP display contract: current HP / max HP -> clamped ratio -> visible fill width; retain numeric values where useful for precision.
- Apply the same pattern to Stamina only if current game/state contracts expose it as a player-facing resource.
- Do not invent additional meters/resources.
- Reuse approved Bag/Skills/UI references and Batch 001 boards where applicable.

## Existing reference inventory requiring reconciliation

Drive continuity records identify these Text-rpg-game visual references:
- REF_BATCH001_CONCEPT_BOARD_A.png
- REF_BATCH001_CONCEPT_BOARD_B.png
- REF_BATCH001_WAVE_A_BOARD_C.png
- REF_BATCH001_WAVE_A_BOARD_D.png
- REF_BATCH001_WAVE_A_BOARD_E.png
- UI_REFERENCE_BAG_APPROVED_V1.png
- UI_REFERENCE_SKILLS_APPROVED_V1.png
- UI_REFERENCE_SKILLS_APPROVED_V2.png

Repository/history also records:
- PixelScene environment overlays
- Pixel Environment Prop Catalog
- scene sprite placements
- Wave I environment manifests/coverage
- DISTRICT_PLAZA_BLACKOUT_SCENE
- RELAY_WORKBENCH_RELAY_OPEN_SCENE
- current raster resources in drawable-nodpi

These must be reconciled before new visual assets are authored.

## Execution order

### Phase 0 — Asset recovery and classification
1. Inventory all current PR #19 PNGs, PixelSprite masters, scene catalogs, prop catalogs, manifests, placements and UI assets.
2. Inspect approved Drive references A-E, Bag and Skills.
3. Classify each visual as: runtime-approved, approved-reference-only, source master, technical placeholder, blocked-canonical, obsolete/duplicate, or missing.
4. Build a mapping: gameplay ID -> source master -> approved reference -> raster resource -> runtime consumer.
5. Record gaps; do not fill them speculatively.

Exit gate: every visible opening-screen element has known provenance/status.

### Phase 1 — Platform Nine scene fidelity
1. Reuse approved tiles/scene/prop art first.
2. Make raster scene the dominant presentation.
3. Retain only necessary geometric overlays.
4. Preserve location identity and state-specific overlays.
5. Compare phone-sized before/after QA.

Exit gate: Platform Nine reads as an authored pixel-art scene, not a diagram, with no gameplay/state regression.

### Phase 2 — Player fidelity
1. Locate and review legitimate player references.
2. Replace only geometry supported by approved reference material.
3. Verify paper-doll origin, 32x48 alignment, z-order and equipped layers.
4. Keep unresolved anatomy/appearance explicitly blocked rather than invented.

Exit gate: player presentation uses the strongest approved art available and all equipment remains aligned.

### Phase 3 — HUD visual system
1. Extract approved palette and frame language from project references.
2. Apply shared pixel HUD primitives to Story first.
3. Implement dynamic HP bar from player-safe projected current/max HP.
4. Add Stamina bar only when its current projected contract is confirmed.
5. Retain accessibility/readability and numerical precision.
6. Extend the same language to inventory/skills after Story acceptance.

Exit gate: Story HUD uses coherent approved pixel styling and dynamic resource displays without owning gameplay rules.

### Phase 4 — Major locations
Improve remaining current Story locations one family at a time using the Platform Nine pattern.

### Phase 5 — Inventory / items
Apply approved Bag/Skills references and existing item art consistently.

### Phase 6 — NPCs
Proceed only where canonical visual references exist. Otherwise remain blocked.

### Phase 7 — Secondary UI / FX
Polish secondary panels, transitions, state FX and non-critical presentation after primary gameplay surfaces are coherent.

## Verification for every implementation slice

1. Confirm live branch/PR HEAD immediately before editing.
2. Make one small reversible asset family change.
3. Update source master and raster/export mapping together when the master is authoritative.
4. Add/update tests for mappings, fallback, state projection, dimensions/alignment, and dynamic HUD math as applicable.
5. Run exact-head Python + Android unit/build/package + emulator workflow.
6. Inspect phone-sized QA screenshots/artifacts.
7. Record exact HEAD, workflow run, test counts and artifact IDs.
8. Do not label physical-device acceptance complete until Galaxy A03 QA is observed.

## Immediate next implementation slice

Do not redraw more assets yet.

First produce the Phase 0 provenance matrix. Then use it to decide exactly which existing Platform Nine tiles/scene/props replace geometric presentation and which player/HUD elements already have approved references.

This recovery step is required to prevent duplicate art, accidental canon invention, and further divergence between approved visual work and the APK.
