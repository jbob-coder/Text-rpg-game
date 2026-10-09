# THE GAME — Android Consumer & Player-Safe Projection Map

Status: **ACTIVE / FIRST-PASS SOURCE-GROUNDED CONSUMER CONTRACT**  
Repository: `jbob-coder/Text-rpg-game`  
Program branch: `docs/master-game-development-program`  
Parents:
- `docs/android/APPLICATION_UX_MASTER_PLAN.md`
- `docs/android/APK_REBUILD_AND_EVOLUTION_MASTER_PLAN.md`
- `docs/android/APK_FINAL_RECONSTRUCTION_MATRIX.md`

## 1. Purpose

Map Android presentation consumers to the player-safe data/actions they are allowed to consume.

This is the bridge between:
- Python/domain state;
- Android bridge projection;
- Compose screens;
- pixel assets;
- tests.

It prevents the final APK rebuild from moving gameplay authority into UI code.

## 2. Current Android projection contract

Current Kotlin `GameSnapshot` exposes:

- `sceneId`;
- `title`;
- `body`;
- `choices`;
- `resources`;
- `attributes`;
- `derived`;
- `skills`;
- `conditions`;
- `identity`;
- `inventory`;
- `quests`;
- `worldMap`;
- `room`;
- `visuals`;
- `turn`;
- `timeMinutes`;
- `location`;
- `contentId`;
- `canonStatus`;
- `abilities`.

Current public `GameEngine` actions expose:
- start;
- choose;
- save;
- load;
- applyCheat;
- equip;
- unequip;
- travel;
- inspectStatus.

These are current implementation facts at the audited program branch.

## 3. Core boundary

Target remains:

`GameState -> domain/rules/world -> player-safe projection -> Android bridge -> Compose UI`

Compose may:
- select;
- request;
- render;
- animate;
- filter already-safe presentation fields;
- manage ephemeral UI state.

Compose may not:
- decide quest truth;
- calculate authoritative stats/damage;
- decide route legality;
- read hidden NPC goals;
- infer actor presence from private flags;
- mutate inventory directly;
- create undiscovered map nodes;
- grant skills/abilities/items.

## 4. Story/current-location consumer

Current/target inputs:
- scene ID;
- title/body;
- choices;
- resources;
- location;
- safe visual state;
- current actor presence when added;
- current room/state overlays.

Current actions:
- choose.

Target asset packet:
- environment base;
- props/modules;
- room actors;
- equipment/held-object layers;
- state overlays;
- FX;
- optional portrait/focus panel.

Decision:
- **REWORK presentation / KEEP authority boundary**.

## 5. Choice cards

Consume:
- choice ID;
- player-visible text;
- enabled;
- disabled reason.

Must not receive:
- raw requirements;
- hidden checks;
- future outcomes;
- secret next-scene IDs unless intentionally player-facing.

Action:
- `choose(choiceId)`.

Decision:
- **KEEP safe semantics / REWORK visual treatment as needed**.

## 6. Story resource HUD

Consume:
- `resources[].id/current/max`.

May calculate only visual ratios from already-projected current/max.

Must not calculate authoritative maximum values.

Decision:
- **KEEP projection / REWORK styling/layout as needed**.

## 7. Map consumer

Current `GameWorldMap` exposes:
- title;
- currentLocation;
- nodes;
- edges.

Each node exposes:
- ID;
- title;
- description;
- X/Y;
- current;
- reachable.

Map may:
- render nodes/edges;
- render current/reachable state;
- select a safe node;
- show player-safe description;
- request travel.

Map may not:
- invent edges;
- mark a node reachable itself;
- reveal hidden nodes not projected;
- alter travel time/risk.

Action:
- `travel(locationId)`.

Decision:
- **KEEP semantic projection / REWORK or partially replace visual presentation**.

## 8. Future hierarchical map requirement

Current `GameWorldMap` is district-scale.

Final world navigation needs a future projection capable of:
- world;
- macroregion;
- region;
- settlement;
- district;
- site/interior.

Do not overload current node X/Y to silently become universal world coordinates.

Required migration:
- new hierarchical place/map projection;
- backward-compatible Gate Twelve adapter or explicit migration.

## 9. Character consumer

Current inputs:
- identity;
- equipment slots;
- conditions;
- attributes;
- skills;
- resources;
- inventory candidates.

Current actions:
- equip;
- unequip.

Visual contract:
- 32x48 paper-doll;
- equipment layers;
- canonical Jack identity;
- status overlays;
- future portrait.

Decision:
- **KEEP state contract / REWORK visual identity**.

## 10. Stats consumer

Current inputs:
- resources;
- attributes;
- derived;
- skills;
- conditions;
- projected contribution summaries.

Current action:
- `inspectStatus(path)`.

Inspection returns:
- path;
- kind;
- total;
- player-safe contribution sources/values.

UI may label safe contribution sources.

It must not reconstruct hidden modifier provenance.

Decision:
- **KEEP safe inspection / EXTEND after progression migration**.

## 11. Skills consumer

Current skills are exposed in `GameSnapshot.skills`.

Final UI must later incorporate:
- skill families;
- class/profession links;
- ranks/mastery;
- prerequisites;
- training opportunities.

These fields do not yet all exist in current projection.

Decision:
- **EXTEND projection after progression contract**.

## 12. Inventory/Bag consumer

Current inputs:
- inventory items;
- item ID/name/quantity;
- equippable;
- slot;
- quality;
- equipment state.

Current actions may include equip/unequip through engine.

Future additions may require:
- item detail;
- provenance-known effects;
- categories;
- weight/encumbrance only if implemented;
- ownership/legal status only if implemented.

Decision:
- **KEEP inventory authority / REWORK presentation / EXTEND schema carefully**.

## 13. Equipment consumer

Current inputs:
- equipment slots;
- item identity;
- quality;
- contribution summaries.

Must preserve slot semantics.

Paper-doll visual layers consume item IDs through the asset system.

Decision:
- **KEEP mechanics / REWORK art/alignment**.

## 14. Quests consumer

Current `GameQuest` exposes:
- ID;
- title;
- description;
- category;
- status;
- stage;
- objectives.

Objectives expose:
- ID;
- title;
- required;
- status.

Must not expose hidden future objectives/stages unless projected.

Decision:
- **KEEP/EXTEND**.

## 15. Save/load consumer

Actions:
- save;
- load.

UI owns:
- buttons;
- confirmation;
- error display;
- slot presentation if slots later exist.

Engine/persistence owns:
- serialization;
- schema;
- migration;
- correctness.

Decision:
- **KEEP authority / REWORK UX if needed**.

## 16. Settings

Settings may own application-only preferences:
- audio;
- narration;
- text reveal;
- accessibility;
- display;
- input behavior.

Gameplay settings that affect rules must route through domain authority.

Decision:
- **EXTEND**.

## 17. Developer/cheat consumer

Current engine exposes `applyCheat`.

Developer tools must remain:
- visually separated;
- unavailable from normal player flow unless explicitly enabled;
- non-canonical for ordinary play evidence.

Decision:
- **KEEP separate / EXTEND developer tooling**.

## 18. Room actor-presence projection — implemented D-064

Current `GameSnapshot.room` is a typed `GameRoomProjection` with projection version, location ID, player-safe actor records and optional active-speaker presentation ID.

Current `GameRoomActor` exposes only the typed presentation contract:
- `presentationId`;
- optional `knownActorId`;
- `displayName`;
- `visualFamily`;
- `placementKey`;
- optional `poseKey`;
- optional `outfitKey`;
- `visibleTags`;
- `inspectable`;
- `dialogueAvailable`;
- safe `actions`.

The mapper rejects unsupported actor fields, including private data that is not part of the allowlist. `RoomProjectionMapperTest` covers versioned mapping, migration-compatible absence, private-field rejection, room/location consistency, duplicate actors and active-speaker validity.

This closes the former missing actor-presence projection gap. Later presentation work may extend rendering/accessibility behavior, but must preserve the current player-safe room contract rather than recreating actor presence from raw state.

## 19. Missing world-state notification projection

Future app may need safe notifications such as:
- location changed;
- new route discovered;
- activity complete;
- quest updated;
- relationship visibly changed;
- item obtained;
- condition changed.

Do not infer notifications by diffing raw hidden state in Compose.

## 20. Missing activity projection

Future activity system should expose:
- activity ID/name;
- safe requirements;
- duration;
- known costs;
- availability;
- current progress;
- interruption/cancel status.

Implementation waits on activity master/schema.

## 21. Missing tactical combat projection

Future combat needs a separate player-safe model for:
- visible units;
- positions;
- legal actions;
- known cover/LOS;
- resources;
- objectives;
- visible status;
- combat log.

Do not overload ordinary `GameSnapshot` until a combat projection contract is selected.

## 22. Missing persistent-adversary intel projection

Future rival/adversary UI may show only:
- known identity;
- known faction/status;
- remembered encounter history;
- known traits;
- known injuries/status;
- player relationship/rivalry information that is intentionally visible.

No omniscient hierarchy.

## 23. Pixel asset ownership

Android screen code requests assets by stable visual ID/state.

Asset catalogs/manifests own:
- raster/fallback mapping;
- compatibility;
- state variants.

Engine owns:
- which semantic state is true.

UI owns:
- how the selected safe asset is displayed.

## 24. Current source consumers to keep under audit

Known major presentation/runtime files include:
- `GameViewModel.kt`;
- `GameEngine.kt`;
- `PythonGameEngine.kt`;
- `GameScreen.kt`;
- `CharacterSection.kt`;
- `StatsSection.kt`;
- `StatusComponents.kt`;
- `SceneIllustration.kt`;
- pixel catalogs;
- save repository;
- boot state;
- narration controller.

Each must receive a final KEEP/EXTEND/REWORK/REPLACE/REMOVE classification before the final APK rebuild.

## 25. Consumer test requirements

For every new projection field/action:
- bridge mapper unit test;
- engine contract test;
- Compose consumer test where visible;
- privacy/hidden-state regression;
- save/load test if persistent;
- emulator screenshot if visual;
- physical handset QA when required for final acceptance.

## 26. Final rebuild rule

The final APK is rebuilt from this mapping plus domain contracts.

A screen is not rewritten simply because it looks old.

A screen is rewritten when:
- required domain information cannot be represented cleanly;
- presentation architecture blocks final UX;
- current asset pipeline cannot scale;
- accessibility/performance requires change;
- duplicate/hardcoded state would cause divergence.

## 27. Open audit work

Still required:
- exact field consumer map for every composable;
- exact ViewModel flow/action mapping;
- exact bridge payload keys from Python;
- all test coverage by field/action;
- all asset catalog consumers;
- all temporary/hardcoded visual state;
- final navigation graph.

This document is the first-pass contract, not a completed line-by-line Android audit.


## D-030 exact projection child — 2026-10-02

[Player-safe room actor & context panel projection contract](PLAYER_SAFE_ROOM_ACTOR_PROJECTION_CONTRACT.md) now owns the implementation-target schema for the missing actor-presence projection.

Key decisions:
- add a top-level versioned `room` projection rather than hiding actor presence inside visual-only state;
- keep raw `state.npcs`, personality, knowledge, memories, goals, story state and raw relationships out of Android;
- preserve current four opening actor compositions through semantic placement keys before removing `sceneId + locationId` inference;
- keep the wounded courier as a support presentation unless game design deliberately promotes it to durable NPC state;
- keep panel focus local/transient and out of saves;
- keep existing scene choices authoritative until a separate actor-action mutation API exists.

This closes the documentation requirement for D-030. Runtime migration remains separate and must pass the Python/Kotlin/Compose equivalence and redaction gates in that contract.


## 28. Exact current consumer audit — 2026-10-04

Audited against the live documentation-program branch after the D-042 source inventory.

This section advances the previously-open requirement for exact field/action consumer mapping. It does not claim the final APK architecture is complete.

### 28.1 Projection envelope from Python

Current Python Android bridge returns one player-safe root object with:

- `scene`;
- `status`;
- `inventory`;
- `quests`;
- `map`;
- `visuals`;
- `meta`.

Observed child keys currently consumed by Kotlin:

#### `scene`
- `id`;
- `title`;
- `body`;
- `choices[].id`;
- `choices[].text`;
- `choices[].enabled`;
- optional `choices[].disabled_reason`.

#### `status`
- `resources[].id/current/max`;
- `attributes[].id/name/base/effective/delta/modified/role/contributions`;
- `derived[].id/name/value/role`;
- grouped `skills.<category>[]` with id/name/base/effective/delta/modified/contributions;
- `conditions[].id/name/severity/duration_minutes/tags`;
- `identity.name/origin/background/path/level`.

#### `inventory`
- `items[].id/name/quantity/equippable/slot/quality`;
- `equipment[].slot/equipped/item_id/name/quality`.

#### `quests`
- quest id/title/description/category/status/stage;
- objective id/title/required/status.

#### `map`
- `title`;
- `current_location`;
- nodes: id/title/description/x/y/current/reachable;
- edges: from/to.

#### `visuals`
- `relay_state`, restricted by the Kotlin mapper to:
  - `intact`;
  - `opened`;
  - `damaged`;
  - `signal_lost`.

#### `meta`
- `turn`;
- `time_minutes`;
- optional `location`;
- optional `content_id`;
- optional `canon_status`.

The Python bridge also exposes `schema_version` in meta, but the current Kotlin `GameSnapshot` mapper does not retain it as a player-facing field. Save compatibility remains owned by persistence rather than by Compose.

### 28.2 Kotlin projection boundary

`BridgeSnapshotMapper.fromMap` converts the safe payload into `GameSnapshot`.

Current `GameSnapshot` fields:

- `sceneId`;
- `title`;
- `body`;
- `choices`;
- `resources`;
- `attributes`;
- `derived`;
- `skills`;
- `conditions`;
- `identity`;
- `inventory`;
- `quests`;
- `worldMap`;
- `room`;
- `visuals`;
- `turn`;
- `timeMinutes`;
- `location`;
- `contentId`;
- `canonStatus`;
- `abilities`.

Unknown root/scene/status fields are not copied into `GameSnapshot`. Current unit evidence explicitly checks that secret authoring data and hidden modifier fields do not survive the mapper.

### 28.3 Exact GameViewModel action flow

`GameViewModel` currently owns the Android-side request flow:

| UI request | Engine operation | Snapshot/result handling |
| --- | --- | --- |
| start | `engine.start(...)` | publishes full `GameUiState` with `BootState.Ready` |
| choice | `engine.choose(choiceId)` | replaces snapshot; clears stat-inspection transient state |
| save | `engine.save()` | no snapshot replacement |
| load | `SaveRepository.continueGame()` -> engine load | replaces snapshot; clears stat-inspection transient state |
| cheat | `engine.applyCheat(code)` | replaces snapshot; clears stat-inspection transient state |
| equip | `engine.equip(itemId)` | replaces snapshot; clears stat-inspection transient state |
| unequip | `engine.unequip(slot)` | replaces snapshot; clears stat-inspection transient state |
| travel | `engine.travel(locationId)` | replaces snapshot and creates presentation-only travel transition if confirmed location changed |
| stat inspection | `engine.inspectStatus(path)` | stores transient `GameStatInspection`; does not mutate gameplay snapshot |
| travel animation complete | local ViewModel state only | clears transient travel-transition overlay |

Current transient UI state kept outside authoritative saves:

- boot state;
- busy flag;
- travel transition token/from/to;
- selected stat-inspection path/result/busy/error.

This separation should remain.

### 28.4 Exact Compose field consumers

#### Shell / global status

`GameScreen.kt` consumes:

- `snapshot.location` -> top status location;
- `snapshot.turn` -> turn display;
- `snapshot.timeMinutes` -> formatted game-time display;
- `snapshot.sceneId` -> return to Story on scene change and narration/reveal reset;
- `snapshot.body` -> auto-read narration and narrative text.

#### Story surface

`StorySection` consumes:

- `title`;
- `body`;
- `choices`;
- `location`;
- `sceneId`;
- `visuals.relayState`.

`StoryResourceHud` / resource panels consume:
- `resources[].id/current/max`.

Choice selection emits only the projected choice ID through `onChoice`.

#### Story visual composition

`SceneIllustration` consumes:
- projected `locationId`;
- projected `sceneId`;
- projected `relayState`.

It then selects presentation-only assets through:
- `PixelRasterCatalog`;
- `PixelSceneCatalog`;
- `PixelSceneOverlayCatalog`;
- `PixelEnvironmentDecalCatalog`;
- `PixelEnvironmentPropCatalog`;
- `PixelStoryActorCatalog`;
- `PixelTraceFxCatalog`;
- `PixelAssetCatalog`.

Important transitional inference:
- `PixelStoryActorCatalog` chooses Tamsin/courier placements from `sceneId + locationId`;
- it does not read raw NPC state;
- D-030 remains the target replacement for this heuristic through a formal player-safe room/actor projection.

Fallback geometry still exists inside `SceneIllustration` for locations without a selected scene master. This is a presentation fallback, not final authored art authority.

#### Character surface

`CharacterSection.kt` consumes:

- `inventory.equipment`;
- `inventory.items`;
- `identity`;
- `conditions`;
- `attributes`;
- `skills`.

Actions:
- emits `onEquip(itemId)`;
- emits `onUnequip(slot)`.

It does not mutate equipment locally.

#### Stats surface

`StatsSection.kt` consumes:

- `attributes`;
- `skills`;
- `derived`;
- `conditions`;
- `inventory.equipment`;
- transient `GameStatInspection`.

It constructs safe inspection paths only from projected attribute/skill IDs:
- `attributes.<id>`;
- `skills.<id>`.

It requests `onInspect(path)`; authoritative contribution resolution remains in Python.

#### Inventory surface

`InventorySection` consumes:

- `inventory.equipment`;
- `inventory.items`.

Actions:
- equip projected item ID;
- unequip projected slot ID.

#### Quest surface

`QuestSection` consumes:

- quest category/title/description/status/stage;
- objective title/required/status.

No quest mutation occurs in Compose.

#### Map surface

`MapSection` consumes:

- `worldMap.title`;
- `worldMap.currentLocation`;
- node id/title/description/x/y/current/reachable;
- edge from/to.

Local-only UI state:
- selected map-node ID.

Travel is offered only when projected `reachable == true`, and the UI emits only `onTravel(selected.id)`.

The UI renders geometry from projected nodes/edges but does not author route truth.

#### Settings / session surface

`SettingsPanel` consumes:

- `contentId`;
- `canonStatus`;
- `sceneId`;
- `turn`.

It also owns application-only transient controls for:
- narration auto-read;
- narration speed;
- text reveal speed;
- narration stop/replay;
- save/load buttons.

Developer controls emit whitelisted/string cheat requests back to the engine; Compose does not directly mutate game state.

### 28.5 Current navigation graph

Current top-level `GameSection` states:

- Story;
- Character;
- Stats;
- Inventory;
- Quests;
- Map;
- More.

Settings is an overlay/state outside that enum.

`More` currently routes to:
- Character / Equipment;
- Settings / Save / Audio.

A scene-ID change automatically returns the active section to Story and closes Settings.

This navigation is current implementation evidence, not final UX canon.

### 28.6 Test coverage confirmed from source

Current Android unit/instrumentation sources include coverage for:

- safe bridge payload mapping and hidden-field dropping;
- player-safe stats mapping;
- stat-inspection contribution mapping;
- rejection of unsupported relay visual states;
- engine failure classification;
- save repository missing/corrupt/unsupported-schema behavior;
- travel-transition confirmation;
- Story shell/navigation;
- projected map navigation;
- stat-inspection request routing;
- player-safe equipment contribution rendering;
- scene/overlay/raster rendering;
- paper-doll equipment visibility;
- no invented avatar layer for unmapped equipment;
- condition-driven avatar FX;
- travel-transition presentation;
- inventory quality-frame rendering;
- phone-layout evidence for story, map, inventory, character/stats and skills.

Historical test-source presence is not equivalent to a current-head passing run.

### 28.7 Remaining consumer-audit debt

Still open before D-026/D-021 can be marked DONE:

1. enumerate every pixel catalog's direct Compose consumer and zero-consumer candidates;
2. classify hardcoded visual/presentation state versus safe projection state;
3. map every `GameSnapshot` field to exact tests, including currently weak/untested fields;
4. document the final actor/room projection migration from scene/location inference;
5. define future activity, tactical-combat, hierarchical-map and adversary-intel projection models;
6. reconcile this current consumer graph against the final APK target architecture;
7. rerun the relevant test/build matrix when implementation changes are made.

## 29. D-026 / D-021 checkpoint

The high-level projection map is no longer only conceptual: the live Python payload, Kotlin mapper, ViewModel action flow, major Compose consumers, current navigation graph and existing test-source coverage are now explicitly mapped.

Status remains **IN_PROGRESS**, not DONE, because catalog-level consumers, hardcoded-state audit, future projections and final migration evidence remain open.


## 30. Pixel catalog direct-consumer audit — 2026-10-04

Audited source HEAD: `f906f83f778ac9f96a159365a96431ce26320bc3`.

This is a file-level consumer map for the current Android pixel-presentation sources. It does not yet prove every individual constant/sprite/member is consumed.

| Pixel source | Direct current consumers | Current disposition |
| --- | --- | --- |
| `PixelAssetCatalog.kt` | `CharacterSection.kt`, `GameScreen.kt`, `PixelComponents.kt`, `PixelRasterCatalog.kt`, `SceneIllustration.kt` | **KEEP / RECONCILE PER ASSET** |
| `PixelCharacterStagingCatalog.kt` | `PixelComponents.kt` | **KEEP transitional staging contract / reconcile with final Jack art** |
| `PixelEnvironmentDecalCatalog.kt` | `SceneIllustration.kt` | **KEEP / provenance audit** |
| `PixelEnvironmentModuleCatalog.kt` | `GameScreen.kt`, `PixelEnvironmentPreview.kt` | **KEEP / map-arrival presentation** |
| `PixelEnvironmentOverlayCatalog.kt` | `PixelSceneOverlayCatalog.kt` | **KEEP indirect overlay authority / reconcile provenance** |
| `PixelEnvironmentPreview.kt` | `GameScreen.kt` through `PixelEnvironmentArrivalPreview` | **KEEP presentation-only** |
| `PixelEnvironmentPropCatalog.kt` | `SceneIllustration.kt` | **KEEP / provenance audit** |
| `PixelEquipmentSlotCatalog.kt` | `CharacterSection.kt`, `GameScreen.kt` | **KEEP slot semantics / rework art as needed** |
| `PixelItemQualityFrameCatalog.kt` | `PixelComponents.kt` | **KEEP current quality-frame presentation** |
| `PixelMapArtCatalog.kt` | `GameScreen.kt` | **KEEP semantic viewport/art binding / final map visual may be reworked** |
| `PixelMapMarkerCatalog.kt` | `GameScreen.kt` | **KEEP semantic current/reachable markers / styling may change** |
| `PixelMapTravelTransition.kt` | `GameScreen.kt` through `MapTravelTransitionOverlay` | **KEEP presentation-only / not gameplay route authority** |
| `PixelRasterCatalog.kt` | `PixelComponents.kt`, `SceneIllustration.kt` | **KEEP raster binding / provenance-critical** |
| `PixelSceneCatalog.kt` | `PixelRasterCatalog.kt`, `SceneIllustration.kt` | **KEEP current scene-master lookup / classify each scene asset** |
| `PixelSceneOverlayCatalog.kt` | `SceneIllustration.kt` | **KEEP state-overlay separation** |
| `PixelStoryActorCatalog.kt` | `SceneIllustration.kt` | **TRANSITIONAL / REWORK toward D-030 room actor projection** |
| `PixelTheme.kt` | `MainActivity.kt` | **KEEP / visual tuning allowed** |
| `PixelTraceFxCatalog.kt` | `SceneIllustration.kt` | **KEEP / selective FX provenance and accessibility review** |
| `PixelTraceStrainCatalog.kt` | `PixelComponents.kt` | **KEEP condition-driven presentation** |
| `PixelUiChromeCatalog.kt` | `CharacterSection.kt`, `GameScreen.kt`, `PixelComponents.kt` | **KEEP / presentation may evolve** |
| `PixelUiIconCatalog.kt` | `GameScreen.kt`, `StatusComponents.kt` | **KEEP / presentation asset family** |
| `PixelUiUtilityCatalog.kt` | `GameScreen.kt` | **KEEP / UI utility presentation** |

### 30.1 File-level zero-consumer result

At this audit level, **no listed current pixel presentation file is proven to be wholly zero-consumer**.

That does **not** mean every member within those files is used.

The next deletion-safe audit must operate at member/asset ID level:

- sprite/constant/function symbol;
- direct source consumers;
- manifest/provenance entry;
- test references;
- runtime raster/source binding;
- replacement candidate if any;
- KEEP / MIGRATE / SUPERSEDE / REMOVE decision.

No whole pixel catalog should be removed from the current evidence based only on visual preference.

### 30.1A Bounded map asset-ID consumer cross-check — 2026-10-08

**Documentation-only / non-claiming review.** At inspected authority HEAD `0234bbf8bed4d440e706f1ae3a410f1804bdee2d`, a six-asset map subset has direct source consumers and tests. This is **not** the missing repository-wide, per-member zero-consumer proof; it does not close D-026/D-021 or authorize deletion. Historical provenance and production stages are already recorded in [Environment, Scene, and Map Asset Provenance](../assets/ENVIRONMENT_SCENE_MAP_PROVENANCE_2026-10-03.md), sections 9–10; this section links them to the *exact* Compose consumption behavior rather than making a second asset registry.

| Existing asset ID | Source definition | Exact present consumer / behavior |
| --- | --- | --- |
| `MAP_GATE_TWELVE_DISTRICT_BASE` | `PixelMapArtCatalog.kt::gateTwelveDistrictBase` (256x144) | `GameScreen.kt::MapSection` calls `PixelMapArtCatalog.base(map.title)` and draws it beneath projected edges and markers only for the exact recognized title. |
| `MAP_NODE_DISCOVERED` | `PixelMapMarkerCatalog.kt::discoveredMarker` (16x16) | `MapSection` draws for **each projected** `map.nodes` entry; it does not request additional undiscovered nodes. |
| `MAP_NODE_CURRENT` | `PixelMapMarkerCatalog.kt::currentMarker` | `MapSection` calls `stateOverlay(node.current, node.reachable)`; current takes precedence over reachable. |
| `MAP_NODE_REACHABLE` | `PixelMapMarkerCatalog.kt::reachableMarker` | Overlay when not current and `node.reachable` is true. |
| `MAP_NODE_UNAVAILABLE` | `PixelMapMarkerCatalog.kt::unavailableMarker` | Overlay when neither current nor reachable; the node must already be present in the public map projection. |
| `MAP_PLAYER_MARKER` | `PixelMapMarkerCatalog.kt::playerMarker` | `MapSection` additionally draws it **only** when `node.current` is true. |

**Exact verification boundary:** `PixelMapArtCatalogTest.kt` contains native-grid, exact-title lookup, viewport/coordinate and unknown-map fallback tests; `PixelMapMarkerCatalogTest.kt` contains five asset-ID/grid/palette assertions and four projected-flag overlay cases. This review inspected source and test *text*; **no Gradle, instrumentation, emulator, device or APK tests were executed here**. Existing tests prove their intended coverage only when run at an identified revision.

**Separation of owners:** projected `map.nodes` and `map.edges` determine drawn public locations/routes and `node.reachable` determines travel affordance; `onTravel(selected.id)` delegates via the engine. `PixelMapArtCatalog.base` produces only a background; unknown map titles fall back to a full-canvas viewport without borrowing Gate Twelve art. Local `x/y` are not a world hierarchy or tactical grid (P13 and OR-010).

**Bounded future review question, not a confirmed bug:** `PixelMapArtCatalog.kt` also draws static road-like lines into the Gate Twelve background before projected edges are overlaid. If future discovery design treats an undiscovered route's *visual geometry* as secret, compare partially discovered maps against this fixed backdrop and explicitly decide whether route-like background details require masking or are permissible environment decoration. Do not infer a hidden-route data leak solely from static art.

**Remaining work:** all other pixel catalog members, cross-file/transitive references, test-only assets, per-member provenance/replacement choices and actual runtime screenshots still require independent proof before any removal or promotion.

### 30.2 Hardcoded/transitional state found during consumer audit

Confirmed transitional or presentation-local state includes:

1. `PixelStoryActorCatalog` actor presence inferred from `sceneId + locationId`;
2. `SceneIllustration` location-specific procedural fallback geometry;
3. `SceneIllustration` special-case `RELAY_WORKBENCH` relay placement;
4. `GameScreen` local section/settings/selected-map-node state;
5. `GameViewModel` travel-transition token/from/to presentation state;
6. Settings narration rate, auto-read and text-reveal controls;
7. developer cheat-code text input.

Classification:

- items 4–7 are legitimate application/transient state and should remain outside authoritative saves unless a later product requirement says otherwise;
- items 1–3 are presentation migration debt, not gameplay authority;
- none of these findings justify raw-state access in Compose.

## 31. Updated D-026 audit boundary

The **file-level pixel catalog consumer audit is now complete** for the current source set.

Still required before D-026/D-021 can be considered reconstruction-complete:

1. member/asset-ID level zero-consumer matrix;
2. exact `GameSnapshot` field/action -> test method coverage/gap matrix;
3. D-030 actor projection implementation migration plan at field/consumer level;
4. future activity/combat/hierarchical-map/adversary projection records;
5. final destination APK component migration matrix.


## 32. GameSnapshot field / engine-action test coverage matrix — 2026-10-04

This matrix is based on current Android test source, not a claim that the tests passed at the documentation HEAD.

### 32.1 Snapshot fields

| Field / group | Direct current test-source evidence | Coverage assessment |
| --- | --- | --- |
| `sceneId` | `PythonGameEngineContractTest`; `GameScreenTest`; `CharacterStatsSectionTest` | **COVERED** mapper + presentation |
| `title` | `PythonGameEngineContractTest`; `BridgeStatusMapperTest`; UI instrumentation fixtures | **COVERED** |
| `body` | `PythonGameEngineContractTest`; UI shell/narrative instrumentation; real-activity smoke | **COVERED** |
| `choices` | `PythonGameEngineContractTest`; `GameScreenTest`; phone UI fixtures | **COVERED** |
| `resources` | `PythonGameEngineContractTest`; `BridgeStatusMapperTest`; UI instrumentation fixtures | **COVERED** |
| `attributes` | `BridgeStatusMapperTest`; `StatContributionMapperTest`; Stats/Character instrumentation | **COVERED** |
| `derived` | `BridgeStatusMapperTest.playerSafeStatsAreMappedForDedicatedStatsScreen` | **PARTIAL** — mapper coverage exists; no dedicated current Compose assertion identified for derived-stat rendering |
| `skills` | `BridgeStatusMapperTest`; `StatContributionMapperTest`; `CharacterStatsSectionTest.skillsMatrixUsesAuthoritativeCategoriesAndPhoneReadableCards` | **COVERED** |
| `conditions` | `BridgeStatusMapperTest`; `GameScreenTest.projectedEchoStrainConditionActivatesVisibleAvatarFx` | **COVERED** for mapper + one visible condition path |
| `identity` | `BridgeStatusMapperTest.playerSafeStatsAreMappedForDedicatedStatsScreen` | **PARTIAL** — mapper identity name/level checked; broader Character identity presentation lacks a dedicated field-by-field contract test |
| `inventory` / equipment | GameScreen inventory/character tests; CharacterStats equipment/inventory tests; real-activity equipment smoke | **COVERED** |
| `quests` | no direct current field-level or dedicated QuestSection test identified in the audited Android test sources | **GAP** |
| `worldMap` | CharacterStats map instrumentation; map marker/art/module tests; travel request tests | **COVERED** for current district-map presentation |
| `room` | `RoomProjectionMapperTest` mapping, unsupported-private-field rejection and room-contract tests | **COVERED** mapper/privacy/contract; presentation coverage remains a separate concern |
| `visuals.relayState` | `BridgeStatusMapperTest`; `GameScreenTest.projectedRelayStateRendersThroughNarrativeScene` | **COVERED** |
| `turn` | `PythonGameEngineContractTest`; UI fixtures | **COVERED** |
| `timeMinutes` | `PythonGameEngineContractTest`; UI fixtures | **COVERED** |
| `location` | `PythonGameEngineContractTest`; travel transition and scene/map UI evidence | **COVERED** |
| `contentId` | no direct assertion identified | **GAP** |
| `canonStatus` | no direct assertion identified | **GAP** |
| `abilities` | `BridgeStatusMapperTest.playerSafeAbilityProgressionMapsIntoTypedSnapshot`; malformed/private-authoring rejection tests | **COVERED** typed mapper + validation/privacy boundary; dedicated Compose presentation remains separate |

### 32.2 Player-safe mapper/privacy tests

Confirmed current unit-test boundaries include:

- `PythonGameEngineContractTest.safe bridge payload maps to snapshot and ignores unknown fields`:
  - checks safe scene/resource/meta mapping;
  - checks unknown root/scene/status secret fields are not retained by `GameSnapshot`.
- `BridgeStatusMapperTest.playerSafeStatsAreMappedForDedicatedStatsScreen`:
  - checks identity, attribute, skill, derived and relay-state mapping.
- `BridgeStatusMapperTest.playerSafeStatInspectionMapsContributionSources`:
  - checks the player-safe contribution payload.
- `BridgeStatusMapperTest.unsupportedRelayVisualStateIsRejected`:
  - checks visual-state whitelist enforcement.

### 32.3 Engine action test-source matrix

| Engine action | Current test-source evidence | Assessment |
| --- | --- | --- |
| `start` | `ActivityBootSmokeTest.realActivityBootsAndAppliesFirstPythonChoice`; Python engine error-classification tests | **COVERED** |
| `choose` | real-activity first-choice smoke; Story UI choice routing | **COVERED** |
| `save` | `SaveRepositoryTest`; `ActivityBootSmokeTest.realActivitySaveLoadRoundTripRestoresPythonScene` | **COVERED** |
| `load` | `SaveRepositoryTest`; real-activity save/load round trip | **COVERED** |
| `applyCheat` | `ActivityBootSmokeTest.realActivityDeveloperDistrictCheatAndMapTravelOpenNarrativeScene`; failure classification | **COVERED** for current developer path |
| `equip` | Character/Inventory UI tests; real-activity equipment smoke | **COVERED** |
| `unequip` | `GameScreenTest.characterScreenSelectsAuthoredPaperDollSlotAndRoutesUnequip`; CharacterStats fresh-snapshot test | **COVERED** |
| `travel` | map navigation test; `TravelTransitionContractTest`; real-activity district travel | **COVERED** |
| `inspectStatus` | Stats request test; mapper inspection test; failure classification | **COVERED** |

### 32.4 High-value test gaps to close during implementation work

The current documentation audit identifies these concrete Android test gaps:

1. dedicated `QuestSection` projection/render test for quest status/stage/objectives and hidden-future-objective boundary;
2. direct `contentId` session-display mapping/render assertion;
3. direct `canonStatus` session-display mapping/render assertion;
4. dedicated derived-stat Compose presentation assertion;
5. fuller identity projection/UI contract test for origin/background/path/level rather than only mapper name/level coverage;
6. room-actor Compose rendering/accessibility coverage beyond the implemented mapper/privacy/contract regressions;
7. future hierarchical-map/activity/combat/adversary projection tests when those contracts materialize.

These are **documented gaps**, not current runtime failures.

## 33. D-026 checkpoint after test-gap audit

The exact current `GameSnapshot` field and `GameEngine` action test-source matrix is now documented.

Remaining D-026/D-021 reconstruction work is reduced to:

1. member/asset-ID level consumer/zero-consumer matrix;
2. D-030 actor projection implementation migration map;
3. future projection contracts;
4. final destination APK migration mapping;
5. runtime execution evidence when code changes begin.

## 34. Wave-2 P8 / D-026 — Tactical projection migration boundary

**Status:** FILE/FIELD/ACTION/TEST DOCUMENTATION MAP COMPLETE FOR P8, implementation and runtime evidence still gated on D-073/D-074. **Owner:** Kestrel. **Authority:** OR-015 (typed domain projection), OR-034 (provisional fixture), OR-035 (parallel Wave 2).

**Canonical child:** [D026 tactical player-safe projection migration map](D026_TACTICAL_PLAYER_SAFE_PROJECTION_MIGRATION_MAP_2026-10-08.md). It records:
- exact existing `CombatKnowledge.player_view` and `EncounterRules.player_view` source fields, with an explicit boundary between D-071 source and the **not-yet-implemented** D-073 bridge;
- the Python bridge -> narrow Kotlin `GameEngine` gateway -> typed `GameSnapshot` DTO/mapper -> ViewModel -> Compose path, without transferring tactical legality into Android;
- proposed domain-version manifest, legacy snapshot handling, type/privacy/unknown-required-version failure, observed versus last-known contact semantics;
- named future test owners/paths, accessibility and hidden-contact screenshot/semantics gates, and merge-state/build evidence requirements;
- OR-010 static room placement versus tactical geometry and OR-034 non-canonical contact/visual fixture limits.

This is a **documentation-only D-026 child**, not D-073/D-074 completion, not a produced `combat` wire schema, not a new save field and not an Android runtime result. Retain the remaining D-026 activity, hierarchical-map, adversary-intel, evolved status and final-APK consumer work in the Master Task Register. Any future bridge JSON field name or action signature must be sourced from the completed D-073 contract before Kotlin implementation.

## 35. Wave-3 P13 / D-026 — Hierarchical world-map projection migration

**Status:** **DOCUMENTATION-ONLY MIGRATION CHILD DELIVERED**, not a shipped hierarchical world runtime, Kotlin mapper, UI, gameplay map, canon or save migration. **Owner:** Kestrel under OR-036 / Wave-3 P13.

[Canonical P13 migration contract](P13_D026_HIERARCHICAL_WORLD_MAP_PROJECTION_MIGRATION_2026-10-08.md) maps the current `AndroidGameSession._map_view_for` discovered flat nodes/edges, `travel(locationId)` authoritative Python rules, Kotlin `GameWorldMap`, mapper, ViewModel and `MapSection` to a proposed independently versioned and typed world-scale hierarchy. It preserves the legacy flat view, the current **21-field** Kotlin `GameSnapshot`, schema-v1 saves, separation of world-scale geography from Gate Twelve's local `REGION -> MACROZONE -> NAMED SUBZONE` art plan, and the D-073/D-074 tactical coordinate separation.

- **Privacy:** no hidden node names, parent IDs, route endpoints, breadcrumb counts, asset metadata, map labels or accessibility leaks.
- **Ownership:** hierarchy expand/select/zoom is presentation-only. Actual travel, reachability, time and location remain Python-owned; no Compose pathfinding/route synthesis.
- **Version:** suggested future `hierarchical_map` is a *proposal*, not live wire API; unknown required versions and malformed references must fail closed without compromising historical flat maps.
- **Tests:** existing Python bridge map discovery/adjacency and Android consumer/gateway paths are identified; new cross-domain redaction, mapper, phone UI and merge-state execution are **planned only**.
- **Master boundary:** D-026 remains IN_PROGRESS for activity, adversary intel, evolved status, final APK, actual tactical/hierarchy consumers and executed runtime/build evidence; P13 does not mark those complete.
