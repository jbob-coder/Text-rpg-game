# Service Tunnel Ambient Animation Migration Contract — 2026-10-03

Status: **ACTIVE TARGET CONTRACT / D-029 PROVENANCE DECISION / RUNTIME NOT IMPLEMENTED**  
Repository: `jbob-coder/Text-rpg-game`  
Program branch: `docs/master-game-development-program`  
Source-audit baseline before this document: `97be95849a4b3af10af441da145a90f92a9ad4f6`

Parents:

- [Asset provenance registry](ASSET_PROVENANCE_REGISTRY.md)
- [UI, FX, Held-Prop, and Animation Asset Provenance](UI_FX_ANIMATION_PROVENANCE_2026-10-03.md)
- [Environment, Scene, and Map Asset Provenance](ENVIRONMENT_SCENE_MAP_PROVENANCE_2026-10-03.md)
- [Application UX master plan](../android/APPLICATION_UX_MASTER_PLAN.md)
- [Gate Twelve map/art/animation context](../GAME_CONTEXT_LOGS/2026-10-01_GATE_TWELVE_MAP_ART_ANIMATION.md)

Related implementation candidate:

PR #31 — `feature/service-tunnel-ambient-animation-stack@19807863e3d68cd3ffad0e627ad19130da9bdbed`

## 1. Purpose

Define exactly how the existing PR #31 ambient-animation work may be reconstructed or selectively migrated without:

- treating its divergent branch as current authority;
- coupling presentation animation to gameplay state;
- bypassing reduced-motion accessibility;
- binding animation to the wrong Service Tunnel static-art revision;
- creating hidden-state leakage;
- wasting mobile resources when animation should not run.

This is a migration contract. It does **not** claim ambient animation is present on the current program branch.

## 2. Evidence classes used here

- **VERIFIED CURRENT IMPLEMENTATION** — directly inspected on the current program branch.
- **VERIFIED BRANCH EVIDENCE** — directly inspected on PR #31's exact head.
- **ESTABLISHED DESIGN** — required by current active documentation.
- **PROPOSED MIGRATION** — target implementation path, not current behavior.
- **UNKNOWN** — repository evidence does not currently establish the detail.
- **BLOCKED** — promotion cannot proceed until a named prerequisite is satisfied.

## 3. Current program-branch state

### VERIFIED CURRENT IMPLEMENTATION

The current program branch does not contain:

`android/app/src/main/java/com/thegame/rpg/ui/PixelAmbientAnimationCatalog.kt`

The current `SceneIllustration.kt` is not PR #31's ambient-animation implementation.

No current Android source field/control matching:

- `reduceMotion`;
- `reducedMotion`;
- `ambientAnimationEnabled`

was found in the inspected:

- `MainActivity.kt`;
- `GameViewModel.kt`;
- `GameScreen.kt`;
- `GameEngine.kt`.

Therefore current runtime status is:

`NOT INTEGRATED`

### Current presentation-setting ownership

`MainActivity.kt` currently owns presentation preferences such as:

- `autoReadNarration`;
- `narrationRate`;
- `textDelayMs`;

using Compose `rememberSaveable` state.

Those values are passed into the UI rather than Python gameplay state.

No `DataStore` or `SharedPreferences` persistence was found in the inspected current setting path.

This establishes a current architectural precedent:

`Android presentation preference -> UI rendering behavior`

not:

`Python gameplay state -> accessibility preference`

## 4. Established accessibility requirement

`docs/android/APPLICATION_UX_MASTER_PLAN.md` already requires:

- scalable text;
- contrast;
- **reduced motion**;
- touch sizes;
- non-color-only states;
- narration;
- haptic/sound alternatives if used.

Therefore reduced motion is not invented by this migration document. It is an existing target requirement whose runtime path remains unimplemented.

## 5. PR #31 exact branch evidence

### Branch identity

Head:

`19807863e3d68cd3ffad0e627ad19130da9bdbed`

Base:

`docs/gate-twelve-map-pixel-asset-blueprint@b6e2d97c3675813c53f03460342d875a1bdc750e`

Changed files:

- `PixelAmbientAnimationCatalog.kt`;
- `SceneIllustration.kt`;
- `PixelAmbientAnimationCatalogTest.kt`;
- `SceneIllustrationAmbientAnimationTest.kt`;
- Gate Twelve animation/context documentation;
- task-register documentation.

It does not change gameplay/content state.

### Historical verification

Exact PR #31 head has:

- workflow: Android Pixel Client;
- run number: 285;
- run ID: `36952192376`;
- status: completed;
- conclusion: success.

This is historical exact-head evidence only. It is not proof for a future rebased implementation.

## 6. Candidate animation assets

PR #31 source:

`PixelAmbientAnimationCatalog.kt`

Git blob:

`e53f39319ff5a8b2c547c132fe5cc527f997573a`

Candidate track IDs:

| Track | Frame duration | Declared moving bounds |
| --- | ---: | --- |
| `SERVICE_TUNNEL_AMBIENT_FAN` | 220 ms | left 82, top 18, right 88, bottom 24 |
| `SERVICE_TUNNEL_AMBIENT_PANEL` | 450 ms | left 40, top 31, right 44, bottom 33 |
| `SERVICE_TUNNEL_AMBIENT_DRIP` | 260 ms | left 116, top 36, right 118, bottom 41 |

The candidate catalog returns these tracks only for:

`SERVICE_TUNNEL`

The catalog requires frame duration to be at least 80 ms and keeps frames on the scene-native grid.

## 7. Candidate execution model

PR #31 candidate `SceneIllustration.kt` blob:

`5d200ba2b58707863e87114d5669291dcc5d72c3`

Observed model:

1. resolve ambient tracks from `locationId`;
2. initialize per-track frame indices;
3. enter a `LaunchedEffect(locationId, ambientTracks)`;
4. create one coroutine per track;
5. delay by each track's frame duration;
6. advance the corresponding frame index;
7. draw the current frame during scene composition.

This is presentation-only animation.

### What the candidate does not establish

The inspected candidate does not contain an explicit reduced-motion preference check.

It also does not prove, by documentation alone, every future navigation/composition path will stop animation when the scene is no longer visible.

Compose's lifecycle behavior must be validated in the destination implementation rather than used as a substitute for an explicit product contract.

## 8. Candidate QA evidence

PR #31 unit test:

`PixelAmbientAnimationCatalogTest.kt`  
blob: `13f554338e42f900e6e808a267c887e67e0ed542`

It verifies:

- Service Tunnel is the only location with ambient tracks in this slice;
- exact candidate timings;
- native-grid dimensions;
- declared moving bounds;
- non-empty visible frames.

PR #31 instrumentation test:

`SceneIllustrationAmbientAnimationTest.kt`  
blob: `425bfc055a462953a34db8b898287bc12aaaddbe`

It verifies that advancing time changes visible Service Tunnel pixels without changing story state.

Missing from the candidate's verified contract:

- reduced-motion disabled-loop behavior;
- settings-toggle behavior;
- destination-head lifecycle/off-screen cancellation evidence;
- physical-device performance/visual evidence.

## 9. Static-art dependency

Technical branch topology is already resolved in:

`ENVIRONMENT_SCENE_MAP_PROVENANCE_2026-10-03.md`

Service Tunnel has two relevant static states for promotion purposes:

1. current inherited program-branch baseline;
2. PR #27 refined candidate.

PR #31 is not based on the selected final static-art destination.

Therefore:

> PR #31 must not determine which Service Tunnel static art wins.

Animation geometry/bounds must be validated against whichever static source is ultimately selected.

### Blocking owner decision

The static visual promotion remains:

`OWNER DECISION REQUIRED`

between:

- current inherited Service Tunnel baseline;
- PR #27 refined Service Tunnel candidate.

The animation can be technically specified now, but final integration is blocked until its scene geometry is selected.

## 10. Migration decision

### Decision

Do **not** merge PR #31 wholesale.

When the static Service Tunnel survivor is selected:

1. start from the selected current implementation parent;
2. selectively reconstruct/reimplement the three ambient tracks;
3. validate their bounds against the selected 128x64 scene;
4. add reduced-motion gating before promotion;
5. add destination-head tests and visual evidence;
6. preserve all gameplay/state ownership outside the animation code.

PR #31 is therefore classified:

`VERIFIED_BRANCH_EVIDENCE + DEFERRED_INTEGRATION + REIMPLEMENT_ON_SELECTED_STATIC_PARENT`

## 11. Reduced-motion target contract

### Ownership

Reduced motion is an Android/application presentation preference.

It must not become:

- a gameplay stat;
- Python `GameState`;
- a quest flag;
- an NPC/world field;
- a combat modifier;
- part of the gameplay save schema merely to control UI motion.

### Proposed first integration path

The smallest architecture-compatible path is conceptually:

`MainActivity presentation setting`
-> `TheGameRoot`
-> `GameScreen / StorySection`
-> `SceneIllustration`
-> ambient-animation enable/disable decision

A concrete name such as `reducedMotion` is proposed, not current implementation.

### Behavior

When reduced motion is **off**:

- approved ambient tracks may advance using their documented timings.

When reduced motion is **on**:

- ambient track loops do not advance;
- render either no ambient animation layer or a documented neutral/static frame;
- story, choices, map state, actors, overlays and gameplay state remain unchanged.

No gameplay information may be lost when motion is disabled.

### Default

This document does not silently choose a final product default.

The implementation must define and test the default explicitly.

### Persistence

Current presentation settings use `rememberSaveable`, not durable application-preference storage.

For the first bounded migration, reduced motion may follow the same existing presentation-state lifecycle if that is the selected implementation strategy.

Long-term durable accessibility-preference storage remains a separate application-settings decision.

Do not store it in game saves merely because durable app preferences do not yet exist.

## 12. Scene visibility and lifecycle contract

Ambient animation should consume resources only while its rendered surface is active.

Destination implementation must verify:

- leaving `SERVICE_TUNNEL` stops Service Tunnel ambient loops;
- changing to a location with no tracks leaves no orphaned track loop;
- removing the Story/scene composable from composition stops its work;
- reopening the scene starts from the defined initial animation state;
- rapid location changes do not accumulate coroutines.

This must be demonstrated by destination-head tests or inspectable runtime evidence.

## 13. State and privacy boundary

Ambient animation may depend on:

- public location/presentation identity;
- explicit player-safe visual-state projection if a future track requires it;
- Android presentation settings such as reduced motion.

It must not infer animation from:

- hidden quest flags;
- NPC goals;
- private memories;
- hidden relationships;
- undiscovered state;
- future scene state;
- raw private AI intent.

The current PR #31 three-track slice does not require hidden state.

## 14. Layering order

Ambient motion is not a base-scene replacement.

Target scene order remains conceptually:

`base scene raster/source`
-> permanent environment composition
-> state overlays
-> props/decals as defined
-> room actors
-> approved ambient animation layer at documented z-order
-> transient Trace/event FX
-> panels/text/UI

Exact z-order must be checked against the selected static scene and existing `SceneIllustration` layer sequence before integration.

Do not flatten ambient frames into the preferred base PNG merely to simplify rendering.

## 15. Performance contract

The candidate is deliberately small:

- three tracks;
- bounded moving regions;
- low frame cadence relative to full-frame animation.

Destination requirements:

- no full-scene bitmap regeneration each animation tick when a bounded layer is sufficient;
- no unbounded coroutine creation;
- no hidden background loop for an inactive scene;
- reduced motion must eliminate continuous track advancement;
- retain integer/native pixel rendering;
- measure representative low-end-device behavior before final approval.

Galaxy A03-class physical-device evidence remains separate from emulator evidence.

## 16. Required unit tests after migration

At minimum:

1. only Service Tunnel maps to these three tracks;
2. stable track IDs remain unchanged unless explicitly migrated;
3. frame durations remain valid and bounded;
4. frames stay inside declared animation bounds;
5. no frame is empty unless intentionally documented;
6. unknown location returns no tracks;
7. reduced motion disables track advancement;
8. disabling motion does not mutate gameplay/story state;
9. re-enabling motion follows the documented restart/resume rule;
10. selected static-scene geometry still contains the declared moving regions.

## 17. Required Compose/instrumentation tests

At minimum:

- Service Tunnel animation visibly advances when enabled;
- Service Tunnel does not advance when reduced motion is enabled;
- another location does not create Service Tunnel track motion;
- changing away from Service Tunnel stops its track updates;
- changing back does not duplicate running loops;
- story choice state remains unchanged by animation time;
- overlay/actor composition remains visible and correctly layered;
- 320dp/narrow-phone rendering remains stable.

## 18. Required destination-head verification

After code migration:

- Kotlin unit tests;
- instrumentation compile/tests;
- Android assemble/package gates;
- screenshot evidence for Service Tunnel with motion-capable state;
- screenshot/static evidence for reduced-motion state;
- exact destination commit recorded;
- static source/raster survivor recorded;
- asset/candidate provenance updated;
- physical-device performance/visual QA when available.

Historical PR #31 success cannot substitute for this destination-head verification.

## 19. Failure handling

If the candidate bounds no longer align to the selected static scene:

- do not move the static scene solely to satisfy stale animation coordinates;
- update/re-author the animation bounds/frames against the selected scene;
- preserve track semantic IDs if the same visual concept survives;
- record the migration.

If reduced-motion integration cannot be implemented safely in the same slice:

- keep ambient animation deferred;
- do not ship continuous motion without the required accessibility path.

## 20. Reconstruction instructions

If PR #31 disappeared, reconstruct from this evidence:

1. create three Service Tunnel presentation-only track records using the stable IDs above;
2. recreate their documented cadence and bounded regions;
3. use the selected 128x64 static Service Tunnel source as the spatial authority;
4. implement track rendering as separate layers, not base art;
5. expose an Android reduced-motion preference to the scene renderer;
6. suppress continuous advancement when reduced motion is active;
7. keep all gameplay/state authority unchanged;
8. test location scoping/lifecycle;
9. capture exact-head QA;
10. record final provenance and supersession state.

Do not reconstruct from a video/screenshot alone when exact track IDs, bounds, timings and source evidence are available.

## 21. Final classification

PR #31 ambient animation:

- source master: **VERIFIED BRANCH EVIDENCE**
- historical CI: **VERIFIED AT PR #31 HEAD**
- current program integration: **NO**
- static scene dependency: **BLOCKED BY OWNER VISUAL PROMOTION DECISION**
- reduced-motion design requirement: **ESTABLISHED**
- reduced-motion runtime path: **MIGRATION REQUIRED**
- migration strategy: **REIMPLEMENT SELECTIVELY**
- canon approval: **NOT ESTABLISHED**
- physical-device QA: **NOT ESTABLISHED**

This closes the D-029 question of *how* PR #31 should be migrated. It does not implement the migration.
