# THE GAME — Android Consumer Field & Action Audit — 2026-10-04

Status: **ACTIVE / CURRENT-HEAD FIELD-ACTION MAP COMPLETE / CATALOG-DEPRECATION AUDIT REMAINS**  
Repository: `jbob-coder/Text-rpg-game`  
Branch: `docs/master-game-development-program`  
Audited source HEAD: `f906f83f778ac9f96a159365a96431ce26320bc3`

Parents:
- `docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md`
- `docs/android/APPLICATION_UX_MASTER_PLAN.md`
- `docs/DEEP_SOURCE_EXISTING_STATE_AUDIT_2026-10-04.md`

## 1. Purpose

This document advances D-026 / D-021 from a first-pass screen contract to a source-grounded map of:

`Python player-safe projection -> Kotlin bridge mapping -> GameSnapshot field/action -> ViewModel -> Compose consumer -> test surface`

It records what the current Android client actually consumes. It does not add new projection fields or claim future systems are implemented.

## 2. Current projection pipeline

Current source boundary:

`GameState -> RulesEngine/status/content -> AndroidGameSession._view_for() -> PythonSessionGateway -> BridgeSnapshotMapper -> GameSnapshot -> GameViewModel -> Compose`

Current Python top-level player-facing payload keys from `android_bridge.py`:

- `scene`
- `status`
- `inventory`
- `quests`
- `map`
- `visuals`
- `meta`

Current `meta` keys:

- `content_id`
- `canon_status`
- `turn`
- `time_minutes`
- `schema_version`
- `location`

Kotlin `BridgeSnapshotMapper.fromMap` maps this payload into `GameSnapshot`.

## 3. GameSnapshot field inventory and current consumers

| GameSnapshot field | Current semantic owner | Current Android consumers | Decision |
| --- | --- | --- | --- |
| `sceneId` | scene projection | root scene-change reset, NarrativePanel state/reveal key, SceneIllustration, Settings session info | **KEEP** |
| `title` | scene projection | NarrativePanel | **KEEP** |
| `body` | scene projection | narration trigger, NarrativePanel text reveal | **KEEP** |
| `choices` | scene projection | NarrativePanel -> choice cards -> `onChoice` | **KEEP SAFE SEMANTICS** |
| `resources` | status projection | StoryResourceHud, ResourcePanel, status components | **KEEP** |
| `attributes` | status projection | CharacterSection, StatsSection | **KEEP NOW / EXTEND THROUGH PROGRESSION MIGRATION** |
| `derived` | status projection | StatsSection | **KEEP + EXTEND** |
| `skills` | status projection | CharacterSection, StatsSection/SkillsMatrix | **KEEP + EXTEND** |
| `conditions` | status projection | Story avatar overlays, CharacterSection, StatsSection | **KEEP PLAYER-SAFE PROJECTION** |
| `identity` | status/identity projection | Story PlayerAvatarPanel, CharacterSection, PlayerStatusSummary | **KEEP; REWORK ART ONLY** |
| `inventory` | inventory/equipment projection | Story paper-doll equipment, CharacterSection, InventorySection, StatsSection equipment/contribution context | **KEEP STATE CONTRACT / REWORK PRESENTATION** |
| `quests` | quest projection | QuestSection | **KEEP + EXTEND** |
| `worldMap` | world-map projection | MapSection | **KEEP DISTRICT SEMANTICS / FUTURE HIERARCHICAL EXTENSION** |
| `visuals` | safe visual-state projection | SceneIllustration; current relay-state selection | **KEEP + EXTEND VERSIONABLY** |
| `turn` | meta | TopStatusBar, Settings session panel | **KEEP** |
| `timeMinutes` | meta | TopStatusBar formatted display | **KEEP** |
| `location` | meta/map state | TopStatusBar, SceneIllustration, ViewModel travel transition | **KEEP** |
| `contentId` | content metadata | Settings session panel | **KEEP** |
| `canonStatus` | content metadata | Settings session panel | **KEEP** |

No current `GameSnapshot` field is classified REMOVE by this audit.

## 4. Current action map

| UI / ViewModel action | Current path | Mutation authority | Notes |
| --- | --- | --- | --- |
| start | `GameViewModel.startIfNeeded -> GameEngine.start -> PythonGameEngine.start` | Python/domain session | boot stages are application state |
| choose | `GameViewModel.choose -> engine.choose(choiceId)` | RulesEngine through bridge | resets stat-inspection UI state after success |
| save | `GameViewModel.save -> engine.save` | Python persistence | UI does not serialize state |
| load/continue | `GameViewModel.load -> SaveRepository.continueGame -> engine.load` | Python persistence | SaveRepository checks that failed load does not alter original save bytes |
| cheat | `GameViewModel.applyCheat -> engine.applyCheat` | Python bridge/domain | developer-only path; keep separate from normal play |
| equip | `GameViewModel.equip -> engine.equip(itemId)` | equipment/domain | UI supplies item ID only |
| unequip | `GameViewModel.unequip -> engine.unequip(slot)` | equipment/domain | UI supplies slot only |
| travel | `MapSection -> GameViewModel.travel -> engine.travel(locationId)` | Python/domain route legality | ViewModel creates only transient confirmed travel animation state after authoritative location change |
| inspect status | `Stats/Character -> GameViewModel.inspectStatus -> engine.inspectStatus(path)` | status/domain | returns player-safe contribution detail |
| finish travel animation | `GameViewModel.finishTravelTransition(token)` | application-only ephemeral state | does not mutate game location |

This preserves the intended authority rule: Compose requests actions; it does not decide gameplay truth.

## 5. Current screen/component ownership

### Story

Primary implementation:
- `ui/GameScreen.kt` -> `StorySection`, `NarrativePanel`, `StoryResourceHud`;
- `ui/SceneIllustration.kt` -> room/scene composition.

Consumes:
- scene ID/title/body/choices;
- location;
- resources;
- identity/equipped gear/conditions;
- current safe `visuals` state.

Disposition:
**REWORK PRESENTATION / KEEP PROJECTION BOUNDARY.**

### Map

Primary implementation:
- `GameScreen.kt -> MapSection`.

Consumes:
- `worldMap.title`;
- current location;
- projected nodes/edges;
- node current/reachable flags.

Action:
- `travel(locationId)`.

Disposition:
**KEEP SEMANTICS / REWORK OR PARTIALLY REPLACE VISUAL PRESENTATION.**

### Character / Equipment

Primary implementation:
- `ui/CharacterSection.kt`.

Consumes:
- identity;
- attributes;
- skills;
- conditions;
- inventory/equipment.

Actions:
- equip;
- unequip.

Disposition:
**KEEP STATE CONTRACT / REWORK FINAL JACK PRESENTATION.**

### Stats / Skills

Primary implementation:
- `ui/StatsSection.kt`;
- `ui/StatusComponents.kt`.

Consumes:
- attributes;
- derived stats;
- skills;
- conditions;
- identity/resources where shared components are used;
- inventory/equipment contribution context.

Action:
- `inspectStatus(path)`.

Disposition:
**KEEP SAFE INSPECTION / EXTEND AFTER PROGRESSION CONTRACT.**

### Inventory

Primary implementation:
- `GameScreen.kt -> InventorySection`.

Consumes:
- item identity/quantity/equippable/slot/quality;
- equipment slots and current equipped state.

Actions:
- equip;
- unequip.

Disposition:
**KEEP AUTHORITY / REWORK PRESENTATION.**

### Quests

Primary implementation:
- `GameScreen.kt -> QuestSection`.

Consumes:
- quest ID/title/description/category/status/stage/objectives.

Disposition:
**KEEP + EXTEND.**

### Settings / save / narration / developer

Primary implementation:
- `GameScreen.kt -> SettingsPanel`;
- `NarrationController.kt`;
- `SaveRepository.kt`.

Consumes:
- content/canon/session meta;
- current snapshot for session display only.

Actions:
- save/load;
- narration controls;
- developer cheat path.

Disposition:
**KEEP SEPARATION / EXTEND ACCESSIBILITY AND SETTINGS.**

## 6. Current asset-catalog consumers

### `GameScreen.kt`

Direct catalog dependencies observed:
- `PixelAssetCatalog`
- `PixelEnvironmentModuleCatalog`
- `PixelEquipmentSlotCatalog`
- `PixelMapArtCatalog`
- `PixelMapMarkerCatalog`
- `PixelUiChromeCatalog`
- `PixelUiIconCatalog`
- `PixelUiUtilityCatalog`

### `CharacterSection.kt`

Direct catalog dependencies:
- `PixelAssetCatalog`
- `PixelEquipmentSlotCatalog`
- `PixelUiChromeCatalog`

### `StatusComponents.kt`

Direct catalog dependency:
- `PixelUiIconCatalog`

### `SceneIllustration.kt`

Direct catalog dependencies:
- `PixelAssetCatalog`
- `PixelEnvironmentDecalCatalog`
- `PixelEnvironmentPropCatalog`
- `PixelRasterCatalog`
- `PixelSceneCatalog`
- `PixelSceneOverlayCatalog`
- `PixelStoryActorCatalog`
- `PixelTraceFxCatalog`

This proves these catalogs have current consumers at the audited source state. It does not prove every individual asset entry inside each catalog is consumed.

## 7. Transitional/hardcoded presentation state found

### Scene/location actor inference

`PixelStoryActorCatalog` remains a current presentation dependency in `SceneIllustration.kt`.

Disposition:
**KEEP TEMPORARILY / REWORK toward D-030 player-safe room projection.**

Do not remove it before the semantic actor-presence adapter is implemented and equivalence-tested.

### Relay visual state

Current `GameVisuals` carries `relayState`.

The Kotlin mapper explicitly accepts only:
- `intact`
- `opened`
- `damaged`
- `signal_lost`

Disposition:
**KEEP current bounded safe visual state.** Future visual projection must remain explicit/versioned rather than exposing raw flags.

### Travel transition

`TravelTransitionUiState` is created only after `engine.travel` returns a snapshot whose projected location confirms a real change.

Disposition:
**KEEP as presentation-only ephemeral state.**

## 8. Test/evidence mapping

Current source tests that directly support this consumer boundary include:

### Mapper / engine contract

- `BridgeStatusMapperTest.kt`
  - player-safe stats mapping;
  - stat-inspection contribution mapping;
  - unsupported relay visual state rejection.
- `PythonGameEngineContractTest.kt`
  - Python gateway / Kotlin engine contract coverage.
- `StatContributionMapperTest.kt`
  - contribution mapping.
- Python:
  - `tests/test_android_bridge.py`;
  - `tests/test_android_stat_contributions.py`;
  - `tests/test_scene_projection.py`;
  - `tests/test_status.py`.

### Save boundary

- `SaveRepositoryTest.kt`
  - missing save does not load;
  - valid save loads;
  - corrupt save failure preserves original bytes;
  - unsupported schema failure preserves original bytes.
- Python:
  - `tests/test_persistence.py`;
  - `tests/test_save_resume_routes.py`.

### Compose/instrumented consumers

`GameScreenTest.kt` covers, among other current behaviors:
- gameplay shell/narrative/choices/avatar/navigation;
- Stats inspection request and safe equipment contribution;
- UI/equipment/catalog rendering;
- relay visual projection;
- named scene masters and state overlays;
- equipped/unmapped gear behavior;
- character unequip routing;
- visible condition FX;
- confirmed travel transition;
- inventory quality frame.

`CharacterStatsSectionTest.kt` covers phone-size evidence for:
- story/scene/avatar;
- Tamsin/courier art;
- map;
- inventory;
- equipment slots;
- projected attributes;
- skills matrix;
- large-text width behavior.

These are **test-source mappings**. This audit does not claim those tests executed at the audited documentation HEAD.

## 9. Projection gaps still open

The current `GameSnapshot` does not yet implement final target projections for:

1. D-030 semantic room actor/panel presence;
2. hierarchical world-map/place levels beyond the current district model;
3. activities/life-loop state;
4. tactical combat state/actions;
5. persistent-adversary player-safe intel;
6. general player-safe world notification/event feed;
7. target class/profession/rank/ability/passive progression detail required by the evolved design.

These additions require domain/schema contracts before Kotlin fields are added.

## 10. D-026 / D-021 result

The current-head **field/action/screen/bridge map is complete at first exact-source pass**.

Still open:
- per-entry asset-catalog consumer/zero-consumer audit;
- complete navigation graph and temporary/hardcoded presentation inventory beyond the identified actor/relay/travel cases;
- future projection schemas that do not yet exist;
- exact test execution after implementation changes;
- final APK teardown decisions.

Therefore:
- D-026 remains **IN_PROGRESS**, but its line-of-responsibility mapping is materially advanced;
- D-021 remains **IN_PROGRESS**, with current screens/components now mapped to player-safe projection/domain ownership at field/action level.

## 11. Verification boundary

No Kotlin, Python, content, save, asset or runtime behavior was modified by this audit.

No tests/builds were executed.

The audit is documentation derived from inspected source at the recorded source head.
