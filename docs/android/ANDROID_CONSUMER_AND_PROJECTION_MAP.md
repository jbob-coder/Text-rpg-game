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
- `visuals`;
- `turn`;
- `timeMinutes`;
- `location`;
- `contentId`;
- `canonStatus`.

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

## 18. Missing actor-presence projection

Current `GameSnapshot` does not provide a formal room-actor list.

Target new safe record should eventually expose only player-known/currently visible actors, for example:

- actor ID;
- display name;
- portrait/visual identity key;
- room anchor/pose key;
- visible condition;
- known role/faction;
- available safe interactions.

It must not expose:
- private goals;
- secret knowledge;
- hidden disposition;
- off-screen position if not known;
- future story state.

This is a required dependency for dynamic room actors and character panels.

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
- `visuals`;
- `turn`;
- `timeMinutes`;
- `location`;
- `contentId`;
- `canonStatus`.

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
