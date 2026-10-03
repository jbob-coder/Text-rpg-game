# UI, FX, Held-Prop, and Animation Asset Provenance — 2026-10-03

Status: **ACTIVE / D-029 CHILD LEDGER / SOURCE-GROUNDED PARTIAL**  
Repository: `jbob-coder/Text-rpg-game`  
Inspected implementation baseline: `docs/master-game-development-program@2ad50d7aff6f153b90036f8e0f61043242a09765`  
Parent: [Asset Family Provenance Index](ASSET_FAMILY_PROVENANCE_INDEX_2026-10-03.md)

## 1. Scope

This ledger covers presentation families that are neither base environment art nor player/equipment raster families:

- UI chrome;
- UI icons;
- UI utility art;
- Trace ambient/signal/directional FX;
- Trace strain avatar/portrait effects;
- divergent diagnostic-reader held-prop masters;
- divergent Service Tunnel ambient-animation masters.

The families here remain presentation-only. They may visualize projected state but do not own gameplay rules, hidden NPC state, route legality, quest logic, or ability consequences.

## 2. UI chrome family

Source:

`android/app/src/main/java/com/thegame/rpg/ui/PixelUiChromeCatalog.kt`  
Current blob: `8defc127e424c953cac9bf9e95f4562e2b72664d`

Current IDs:

- `UI_PANEL_STORY_FRAME`
- `UI_PANEL_CHARACTER_FRAME`
- `UI_PANEL_STATS_FRAME`
- `UI_PANEL_INVENTORY_FRAME`
- `UI_PANEL_QUEST_FRAME`
- `UI_PANEL_MAP_FRAME`
- `UI_PANEL_SETTINGS_FRAME`
- `UI_PANEL_DEVELOPER_FRAME`
- `UI_MODAL_FRAME`
- `UI_CHOICE_CARD_ENABLED`
- `UI_CHOICE_CARD_DISABLED`
- `UI_CHOICE_CARD_SELECTED`
- `UI_BUTTON_PRIMARY`
- `UI_BUTTON_SECONDARY`
- `UI_BUTTON_DANGER`
- `UI_TAB_ACTIVE`
- `UI_TAB_INACTIVE`

### Provenance

Inherited runtime expansion root:

PR #16 `feature/pixel-assets-runtime-expansion@ddbb5f4250e26b99765999d0a8e81f59cb1ea26c`.

### Runtime consumers

- `PixelComponents.kt`;
- `CharacterSection.kt`;
- `GameScreen.kt`.

The current family is procedural Kotlin code; no PNG export is required/present on the inspected program branch.

### QA

`PixelUiChromeCatalogTest.kt` — blob `e12a6f88c6dc6f0bfdad595451040f06015afd89`.

Tests verify:

- stable unique IDs;
- panel-kind mapping;
- distinct enabled/disabled/tab presentation masters.

### Stage

`SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED`

Not `CANON_APPROVED` solely because it renders.

### Reuse/migration rules

- reuse chrome by semantic UI role, not by superficial shape;
- danger/disabled/selected semantics must not be interchanged;
- final APK/UI rework may replace visual treatment while preserving player-safe action boundaries and accessibility state;
- Android chrome must never become gameplay authority.

## 3. UI icon family

Source:

`PixelUiIconCatalog.kt` — blob `625e4136240c9a1673eda8c47adfdf56c25f6c3f`.

Current IDs include:

Navigation:

- `UI_NAV_STORY_ICON`
- `UI_NAV_CHARACTER_ICON`
- `UI_NAV_STATS_ICON`
- `UI_NAV_INVENTORY_ICON`
- `UI_NAV_QUESTS_ICON`
- `UI_NAV_MAP_ICON`
- `UI_NAV_MORE_SETTINGS_ICON`

Resources:

- `UI_RESOURCE_HEALTH_ICON`
- `UI_RESOURCE_STAMINA_ICON`
- `UI_RESOURCE_FOCUS_ICON`
- `UI_RESOURCE_RESOLVE_ICON`

Quest categories:

- `UI_QUEST_MAIN_ICON`
- `UI_QUEST_SIDE_ICON`
- `UI_QUEST_OPTIONAL_ICON`
- `UI_QUEST_LORE_ICON`

### Provenance

Historical root: PR #7 `feature/pixel-asset-wave-a@a3970de6597c77939afccb5f30d6040bdf3d608d`.

### Consumers

`GameScreen.kt` and `PixelComponents.kt` use the catalog as presentation mappings.

### QA

`PixelUiIconCatalogTest.kt` — blob `851e3d6dfff4adfdef71dee96d4148f887ec5842`.

Tests verify:

- planned native dimensions/palette keys;
- stable presentation-only navigation mapping;
- resource/quest mapping from projected IDs.

### Stage

`SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED`

No current raster export family was found for these icons.

## 4. UI utility family

Source:

`PixelUiUtilityCatalog.kt` — blob `48fc74e267fa1249aca82cd60a7100521b7ccc6f`.

IDs:

- `UI_SCROLL_MARKER`
- `ACCESS_AUDIO_NARRATION_ICON`

Provenance:

PR #16 `feature/pixel-assets-runtime-expansion@ddbb5f4250e26b99765999d0a8e81f59cb1ea26c`.

Current consumer:

`GameScreen.kt`.

QA:

`PixelUiUtilityCatalogTest.kt` — blob `a9a29c3fee053198f3cb8735c16c2fdf36f23b9a`.

Tests verify exact scroll-marker and narration-icon native masters.

Stage:

`SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED`

Migration risk:

Narration iconography is a control affordance only. Narration/audio behavior must remain owned by application/service logic, not encoded as visual state.

## 5. Trace FX family

Source:

`PixelTraceFxCatalog.kt` — blob `093617194e5761494b6649ef3704c794dd5b0137`.

Base IDs:

- `FX_TRACE_ECHO_AMBIENT`
- `FX_SIGNAL_PULSE`
- `FX_DIRECTIONAL_TRACE`

Frame IDs are generated from those stable family IDs.

Current functions provide:

- ambient trace frames;
- six-frame signal pulse;
- six-frame directional trace;
- explicit player-facing scene mappings.

### Provenance

Historical root: PR #7.

### Consumer

`SceneIllustration.kt` selects:

`directionalTraceForScene(sceneId) ?: signalPulseForScene(sceneId) ?: forScene(sceneId)`

and advances the selected frame family inside the Compose scene surface.

### QA

`PixelTraceFxCatalogTest.kt` — blob `0c87022798a31e6bfadce86903e89f36f7582567`.

Tests verify:

- exact 64x64 transparent grids;
- supported mappings;
- six-frame pulse/directional sets;
- player-facing scene boundaries.

### Stage

`SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED`

### Reuse rule

Trace FX may be reused only when the semantic effect matches. Do not use a directional-discovery visual to imply ability success, hidden state, or damage unless the authoritative engine projection explicitly supplies that player-visible meaning.

## 6. Trace strain avatar/portrait effect family

Source:

`PixelTraceStrainCatalog.kt` — blob `cc06b89f5d22992fd140b43160fd7d2f6efba38b`.

Base IDs/state:

- `FX_TRACE_STRAIN`
- projected condition key `COND_ECHO_STRAIN`

Generated frame families include:

- `FX_TRACE_STRAIN_AVATAR_FRAME_*`
- `FX_TRACE_STRAIN_PORTRAIT_FRAME_*`

### Important classification

The `PORTRAIT_FRAME` names here are **effect frames**, not canonical character portrait masters.

This family does not satisfy the planned Jack/Tamsin portrait requirement.

### Consumers

- avatar strain effect: `PlayerAvatarPanel`;
- portrait-compatible strain effect is available from the catalog for a future/current portrait surface consumer.

### QA

`PixelTraceStrainCatalogTest.kt` — blob `f56c7ad8377932daa670d5988474d8d9d8fab1e1`.

Tests verify exact avatar/portrait effect canvases and that the effect maps only from projected `COND_ECHO_STRAIN`.

### Stage

`SOURCE_MASTER_PRESENT + CODE_PRESENT + INTEGRATED`

Migration risk:

Never infer a hidden ability/condition from art. The effect must remain downstream of player-safe projected condition state.

## 7. Diagnostic-reader held-prop candidate — PR #9

### 7.1 Current program branch

`PixelHeldPropCatalog.kt` is **not present** on the inspected program branch.

Therefore this family is not current integrated runtime state.

### 7.2 Verified branch evidence

PR #9:

`feature/pixel-asset-wave-m-diagnostic-reader@063d5879413b81656cc5c7304be0afd02402f2fd`

Source:

`android/app/src/main/java/com/thegame/rpg/ui/PixelHeldPropCatalog.kt`

Blob:

`f8f909016e24a2a05cefe0617db391df6cf1dcfa`

IDs:

- `PROP_DIAGNOSTIC_READER`
- `PROP_DIAGNOSTIC_READER_ICON_MASTER`
- `PROP_DIAGNOSTIC_READER_HELD_FRONT_MASTER`

Test:

`PixelHeldPropCatalogTest.kt` — blob `ffccdd1e66d6078cbfd9b2af048d9a008098e927`

Tests verify documented native dimensions/palette keys and transparency outside held-reader geometry.

Historical workflow run 36778591342 succeeded for PR #9.

### 7.3 Integration state

The PR #7–#31 reconciliation already determined that this production evidence remains deferred unless a real typed runtime consumer exists.

Current stage:

`DEFERRED_INTEGRATION`

Not:

- integrated;
- canon-approved;
- evidence that a diagnostic-reader gameplay interaction exists.

### 7.4 Promotion requirements

Before integration:

1. identify the authoritative gameplay item/interaction ID;
2. define player-safe held-prop projection;
3. define hand/anchor/orientation contract;
4. reconcile with 32x48 avatar/equipment rig;
5. add consumer without duplicating gameplay state in Compose;
6. run unit/instrumentation/render QA;
7. only then promote.

## 8. Service Tunnel ambient-animation candidate — PR #31

### 8.1 Current program branch

`PixelAmbientAnimationCatalog.kt` is **not present** on the inspected program branch.

Current `SceneIllustration.kt` blob `619c9cf5...` does not contain this candidate ambient-track integration.

Therefore PR #31 is not integrated merely because it has successful historical CI.

### 8.2 Verified branch evidence

PR #31:

`feature/service-tunnel-ambient-animation-stack@19807863e3d68cd3ffad0e627ad19130da9bdbed`

Base:

`docs/gate-twelve-map-pixel-asset-blueprint@b6e2d97c3675813c53f03460342d875a1bdc750e`

Source:

`PixelAmbientAnimationCatalog.kt`  
Blob: `e53f39319ff5a8b2c547c132fe5cc527f997573a`

Track IDs:

- `SERVICE_TUNNEL_AMBIENT_FAN`
- `SERVICE_TUNNEL_AMBIENT_PANEL`
- `SERVICE_TUNNEL_AMBIENT_DRIP`

The catalog returns ambient tracks only for `SERVICE_TUNNEL` in this slice.

Candidate `SceneIllustration.kt` blob:

`5d200ba2b58707863e87114d5669291dcc5d72c3`

It creates per-track frame indices and advances frames with Compose `LaunchedEffect`.

### 8.3 QA evidence

Unit test:

`PixelAmbientAnimationCatalogTest.kt` — blob `13f554338e42f900e6e808a267c887e67e0ed542`

Tests verify:

- Service Tunnel is the only location with tracks in this slice;
- tracks match bounded animation brief;
- frames remain on the scene grid and inside declared moving bounds.

Instrumentation test:

`SceneIllustrationAmbientAnimationTest.kt` — blob `425bfc055a462953a34db8b898287bc12aaaddbe`

It checks that the Service Tunnel ambient loop changes visible pixels without story-state mutation.

Historical workflow run 36952192376 succeeded.

### 8.4 Dependency/precedence risk

PR #31 is based on the documentation/map branch, not on the selected final static Service Tunnel survivor.

Static source/raster selection must happen first.

The candidate animation must then be rebased or reimplemented onto the selected static scene geometry.

### 8.5 Accessibility/performance gap

The project-level reconciliation requires:

- reduced-motion behavior;
- stopping work when the scene is not active/off-screen where applicable;
- bounded mobile cost.

The inspected candidate snippets show per-track `LaunchedEffect` loops, but this provenance pass does not establish a dedicated reduced-motion projection/hook.

Therefore reduced-motion compliance remains **MIGRATION/VERIFICATION REQUIRED**.

### 8.6 Stage

`DEFERRED_INTEGRATION / CANDIDATE`

Do not mark `INTEGRATED` until:

1. static Service Tunnel survivor is selected;
2. animation is rebased/reimplemented;
3. reduced-motion behavior is explicit;
4. unit/instrumentation/build gates pass at the destination head;
5. screenshot/device QA confirms no visual conflict.

## 9. Raster/export status for this ledger

No dedicated PNG raster family was found for the current UI chrome/icon/utility/Trace code-master families.

That is not a defect by itself. Their current authoritative visual form is procedural Kotlin.

If later exported to PNG:

- retain the same stable asset IDs;
- record source blob and export blob;
- record dimensions/hash;
- define precedence;
- ensure the new raster does not silently hide a newer code master.

## 10. Reconstruction instructions

To reconstruct these families:

1. restore stable UI IDs and semantic role mappings;
2. restore procedural chrome/icons/utilities;
3. restore Trace FX and strain frame generators;
4. keep all FX downstream of projected player-visible state;
5. do not treat strain portrait effects as portrait identity masters;
6. do not add the diagnostic-reader family without a typed authoritative consumer;
7. do not add PR #31 ambient animation before static Service Tunnel art is selected;
8. implement reduced-motion/performance controls before final animation promotion;
9. run each catalog test plus destination-head instrumentation/build/render checks;
10. mark canon approval only after visual/UX approval, not because code compiles.

## 11. Remaining gaps

- final UI art approval for chrome/icon families;
- raster/export lineage if procedural families are later exported;
- canonical portrait family;
- typed held-prop projection/consumer;
- Service Tunnel static survivor;
- ambient-animation migration;
- reduced-motion contract implementation;
- physical-device visual/performance QA.
