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

### 20.1 Source-exact Phase 1 activity consumer trace — 2026-10-08

**Bounded unclaimed documentation audit, not a new V10 implementation claim.** Source inspected at `4cdba58d96959e8609800b3100b3a3243067115b`: [D-068 executed activity proof](../evidence/D068_PHASE1_ACTIVITY_PROOF_2026-10-04.md) belongs to an earlier tested merge; the inspection here is source-only. The word *activity* covers two distinct maturity levels: an **implemented atomic authored-choice activity** and an **unimplemented normalized V10 activity record/preview/long-running-state projection**.

| Stage | Exact current source / input | Existing authoritative behavior or Android consumer |
| --- | --- | --- |
| Authored choice | `content/vertical_slice_01.json`: `TRAIN_POWER_FUNDAMENTALS_TWO_HOURS` in `TRACE_STABILIZATION_HUB` (`TRACE_CHAMBER`); `skill_train` of `powers`, 120 minutes, intensity 1 | This is a **choice ID**, not a newly registered `ACTIVITY_*` record. The existing authored route and the requirement checks gate availability. |
| Read-only eligibility | `src/textrpg/core.py::RulesEngine.available_choices`, `build_scene_view`; `AndroidGameSession._view_for` under `scene.choices[]` | Emits public `id`, `text`, `enabled`, conditional `disabled_reason`; no new registry list, hidden requirements, generic duration/cost preview or resumable activity progress. |
| Android selection | `GameEngine.kt::GameChoice` and `BridgeSnapshotMapper.fromMap`; `GameScreen.kt` Story `PixelChoiceCard` -> `onChoice(choice.id)`; `GameViewModel.choose` -> `PythonGameEngine.choose` / `PythonSessionGateway.choose` | Forwards the exact authored ID; ViewModel updates the authoritative mapped snapshot only after engine response, not optimistic gameplay arithmetic. |
| State mutation | `src/textrpg/core.py::RulesEngine.choose` -> `simulation.train`, `advance_time`; `AndroidGameSession.choose` | Python validates authored eligibility and time/resource legality, applies a snapshot-backed atomic transaction, records training and choice history; errors return `CHOICE_ERROR`, not partial Android progress. |
| Post-result data | `AndroidGameSession._view_for` -> `meta.time_minutes`, `status.resources`, `status.skills` -> `BridgeSnapshotMapper.fromMap` -> `GameSnapshot.timeMinutes/resources/skills` | The current Android UI consumes the updated **existing status/time** fields, not an `activity_progress` DTO. The historical D-068 case proved +120 minutes, -16 stamina, -10 focus and Powers base/effective 2.0 for its exact test fixture. |
| Verification owners | `tests/test_phase1_activity.py` (three test methods); `PythonGameEngineContractTest.kt` test `activity choice delegates exact id and maps authoritative progress` | Python proof checks legitimate authored route, full result/save-load, insufficient-resource no-mutation and invalid-time preflight rollback; Kotlin proof checks exact choice ID and returned value mapping. D-068 evidence reports focused tests passed and Android JVM/assemble succeeded in its historical run #341; its **full Python aggregate was not green**, and this audit did not rerun any test. |

**V10 target still missing:** `ACTIVITY_*` stable registry/definition and read-only availability/preview, player-known duration/cost disclosure, activity-specific typed Kotlin model, interruption/cancel state and resumable progress, scheduling/background policy, durable migration and UI/test contracts when genuinely required. See [Activity Record and State](../systems/ACTIVITY_RECORD_AND_STATE_STANDARD.md) §§3–12, [Activity Time/Cost/Atomicity](../systems/ACTIVITY_TIME_COST_ATOMICITY_STANDARD.md) and [Activity Interruption/Concurrency](../systems/ACTIVITY_INTERRUPTION_CONCURRENCY_STANDARD.md). Atomic current actions need no invented `active_activity` save field. Existing `GameState.time_minutes` and domain-owned training arithmetic remain authoritative; the future projection must disclose only player-safe requirements and never silently grant activity access from a UI affordance.

**Boundary:** This trace corrects the impression that *no* activity reaches Android. It does not close the missing normalized V10 activity projection, add a field to the 21-field `GameSnapshot`, mark D-026 DONE, or claim another agent's task. New executable verification and destination-head approval are required for future implementation.

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


## D-030 exact projection child — 2026-10-02 / D-064 runtime update

[Player-safe room actor & context panel projection contract](PLAYER_SAFE_ROOM_ACTOR_PROJECTION_CONTRACT.md) originated as the implementation-target schema for the missing actor-presence projection. D-064 has since implemented and verified that **room-actor presence** slice.

Preserved decisions:
- a top-level versioned `room` projection owns player-safe actor presence rather than visual-only inference;
- raw `state.npcs`, personality, knowledge, memories, goals, story state and raw relationships remain outside Android;
- the four opening actor compositions are preserved through semantic placement keys;
- `sceneId + locationId` no longer decides story-actor presence;
- the wounded courier remains a support presentation unless game design deliberately promotes it to durable NPC state;
- panel focus remains local/transient and out of saves;
- existing scene choices remain authoritative until a separate actor-action mutation API exists.

D-030 documentation is complete and D-064 verifies the room-presence runtime migration. Contextual panel/interaction depth, broader authored actor coverage and later presentation extensions remain separate work and must preserve the D-064 privacy/equivalence boundary.


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

Historical pre-D-064 inference (superseded):
- `PixelStoryActorCatalog` previously chose Tamsin/courier presence from `sceneId + locationId`;
- it did not read raw NPC state;
- D-064 replaced that presence heuristic with the formal player-safe room/actor projection.

Current D-064 path:
- Python projects player-safe room actors;
- Kotlin maps typed `GameRoomActor` records;
- `SceneIllustration` passes projected room actors into `PixelStoryActorCatalog.placements(roomActors)`;
- the catalog still owns presentation placement/art selection, but it no longer invents actor presence from scene/location IDs.

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

1. finish remaining pixel-catalog member-level consumer/provenance and zero-consumer proof where not already closed by bounded audits;
2. finish remaining hardcoded visual/presentation-state classification against player-safe projection ownership;
3. close weak/untested `GameSnapshot` and action contracts with exact tests and later exact-head execution evidence;
4. materialize the normalized V10 activity projection contract beyond the current generic-choice/D-068 trace;
5. implement and verify the already-materialized P8 tactical, P13 hierarchical-map and P17 adversary-intel migration contracts when their domain dependencies authorize runtime work, plus define remaining evolved-status projection deltas;
6. reconcile the current consumer graph against the final APK target architecture;
7. rerun the relevant test/build matrix when implementation changes are made.

The D-030 actor/room migration map and D-064 typed room projection are already complete and must not be reopened as generic discovery work.

## 29. D-026 / D-021 checkpoint

The high-level projection map is no longer only conceptual: the live Python payload, Kotlin mapper, ViewModel action flow, major Compose consumers, current navigation graph and existing test-source coverage are now explicitly mapped.

Status remains **IN_PROGRESS**, not DONE, because residual member-level consumer/provenance work, normalized activity/evolved-status projection design, P8/P13/P17 runtime implementation/acceptance, final APK migration and exact-head execution evidence remain open.


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
| `PixelStoryActorCatalog.kt` | `SceneIllustration.kt` | **KEEP as D-064 semantic presentation-placement consumer / expand authored coverage as needed** |
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

### 30.1B UI icon/utility asset-ID consumer cross-check — 2026-10-08

**Scope:** 17 existing catalog asset IDs (15 UI icons and two utilities), inspected at authority `9a75e1bb7090f9bbca5fa82a807e90028458224c`; source/test text inspection only. Historical roots, art stages and no-raster-export status remain in [UI, FX, Held-Prop, and Animation Provenance](../assets/UI_FX_ANIMATION_PROVENANCE_2026-10-03.md), sections 3–4. This is a **bounded documentation continuation**, not a D-026/D-021 completion, new runtime API, or claim on another player's lane.

| Asset ID(s) | Catalog selector; present consumer | Condition and meaning |
| --- | --- | --- |
| `UI_NAV_STORY_ICON`, `UI_NAV_CHARACTER_ICON`, `UI_NAV_STATS_ICON`, `UI_NAV_INVENTORY_ICON`, `UI_NAV_QUESTS_ICON`, `UI_NAV_MAP_ICON`, `UI_NAV_MORE_SETTINGS_ICON` | `PixelUiIconCatalog.navigation(label)` in `GameScreen.kt::PixelNavButton` (the Inventory icon is also used in the Loadout header). | Seven 24x24 icons, chosen by public application section labels, with `Settings` sharing the More icon. They do not choose a destination or grant navigation access. |
| `UI_RESOURCE_HEALTH_ICON`, `UI_RESOURCE_STAMINA_ICON`, `UI_RESOURCE_FOCUS_ICON`, `UI_RESOURCE_RESOLVE_ICON` | `PixelUiIconCatalog.resource(resource.id)` in `GameScreen.kt::StoryResourceHud`, `ResourcePanel`, and `StatusComponents.kt::StatusResourceGrid`. | Four 16x16 presentation icons mapped from projected public resource IDs. The icon does not calculate resources or change state. |
| `UI_QUEST_MAIN_ICON`, `UI_QUEST_SIDE_ICON`, `UI_QUEST_OPTIONAL_ICON`, `UI_QUEST_LORE_ICON` | `PixelUiIconCatalog.quest(category)` in `GameScreen.kt::QuestSection`. | Four 16x16 icons. The screen groups **only** `snapshot.quests` with matching public category; the icon does not discover or fabricate quests. |
| `UI_SCROLL_MARKER` | `PixelUiUtilityCatalog.scrollMarker` in `GameScreen.kt` Story narrative scroll surface. | Procedural 16x16 affordance displayed while `narrativeScroll.value < narrativeScroll.maxValue`; no authored world-state implication. |
| `ACCESS_AUDIO_NARRATION_ICON` | `PixelUiUtilityCatalog.narrationIcon` in `GameScreen.kt` READ ALOUD button. | Procedural 24x24 affordance for `onNarrate(snapshot.body)`; the callback, not the sprite, owns the action. |

**Renderer versus catalog ownership:** `PixelComponents.kt::PixelUiIcon` is the reusable renderer; it is **not** a direct `PixelUiIconCatalog` selector in the inspected source. `GameScreen.kt` and `StatusComponents.kt` call the catalog, then supply sprites to that renderer. Do not treat a renderer's presence as proof that every catalog asset is displayed in every session.

**Existing test-source evidence:** `PixelUiIconCatalogTest.kt` enumerates all 15 icon IDs, asserts native sizes/palette coverage, checks seven section mappings plus the Settings alias, four public resource lookups, four quest-category lookups, and unknown-name null returns. `PixelUiUtilityCatalogTest.kt` checks the scroll marker and narration master dimensions/palette. These tests do **not** establish end-to-end Compose accessibility, narration service behavior or executed current-head acceptance. **No Gradle, instrumentation, emulator, APK or phone tests were executed in this documentation pass.**

**Disposition:** KEEP as source-defined presentation members pending production QA; no member in these two catalogs is proven wholly unreferenced by this bounded source review. Whether a conditional icon is actually rendered depends on current public state and screen path. No deletion, private-state projection, change of state ownership, or migration to a second asset registry is authorized. Continue the per-member test/provenance/consumer audit for remaining catalogs before treating D-026/D-021 as complete.

### 30.1C Trace FX and strain frame-family consumer matrix — 2026-10-08

**Documentation-only / no new task claim.** Inspected authority `f180f8338987c908cc3cf481c2f75f3852ffff64` and all 29 present `android/app/src/main/java/com/thegame/rpg/ui/*.kt` production source files (27 independent UI files plus these two catalogs), with the two dedicated catalog test sources. This is a bounded per-frame-family consumer audit, **not** global asset-deletion proof or a complete accessibility/animation QA run. Historical asset provenance already lives in [UI/FX provenance](../assets/UI_FX_ANIMATION_PROVENANCE_2026-10-03.md) §§5–6.

| Generated asset ID family | Defined members / grid | Actual direct production consumer and selector |
| --- | --- | --- |
| `FX_TRACE_ECHO_AMBIENT_FRAME_1..4` | 4 procedural 64×64 frames in `PixelTraceFxCatalog.kt::frames` | `SceneIllustration.kt` falls back to `PixelTraceFxCatalog.forScene(sceneId)` for the seven listed player-facing scene IDs; unknown scenes return null. |
| `FX_SIGNAL_PULSE_FRAME_1..6` | 6 procedural 64×64 frames, `signalPulseFrames` | `SceneIllustration.kt` uses `signalPulseForScene` for **exactly** `POWER_FIRST_LIVE_USE`, ahead of the ambient fallback. |
| `FX_DIRECTIONAL_TRACE_FRAME_1..6` | 6 procedural 64×64 frames, `directionalTraceFrames` | `SceneIllustration.kt` uses `directionalTraceForScene` for **exactly** `TRACE_DIRECTIONAL_DISCOVERY_RESULT`, ahead of both pulse and ambient. |
| `FX_TRACE_STRAIN_AVATAR_FRAME_1..4` | 4 procedural 32×48 frames in `PixelTraceStrainCatalog.kt::avatarFrames` | `PixelComponents.kt::PlayerAvatarPanel` calls `avatarForConditions(conditions.map { it.id }.toSet())`; only projected `COND_ECHO_STRAIN` yields frames, overlaid on the avatar canvas. |
| `FX_TRACE_STRAIN_PORTRAIT_FRAME_1..4` | 4 procedural 64×64 frames in `PixelTraceStrainCatalog.kt::portraitFrames` | **No direct production call to `portraitForConditions` in the 29 audited Kotlin UI files.** The catalog and `PixelTraceStrainCatalogTest.kt` define/test the frames, but that is not current runtime portrait display proof. Keep as **DEFINED / TEST-REFERENCED / NO UI CONSUMER VERIFIED**; not a canonical portrait master or deletion authorization. |

**Actual precedence and state boundary:** `SceneIllustration` selects `directionalTraceForScene ?: signalPulseForScene ?: forScene` and cycles only the chosen frames at 180 ms; scene IDs come from the player-facing snapshot. This visual rule does not expose hidden trace strength, target selection or engine state. Strain uses already projected condition IDs, not private condition registries. An absent recognized scene/condition yields no corresponding effect and must not be interpreted as a hidden gameplay verdict.

**Existing test-source scope:** `PixelTraceFxCatalogTest.kt` asserts 4/6/6 frame counts, unique frame IDs, 64×64 size, palette coverage, known-scene mapping and null for unsupported scenes. `PixelTraceStrainCatalogTest.kt` asserts both 4-frame sets and 32×48 avatar/64×64 portrait sizes, palette keys and `COND_ECHO_STRAIN` gating. These are defined tests, **not executed** in this pass. Neither unit test demonstrates a live Compose portrait caller, performance on a low-end phone or full accessibility/reduced-motion behavior.

**Retention decision:** KEEP used scene/strain-avatar members; RETAIN unused-for-UI portrait effect masters as possible future source art, but label **NO CURRENT PRODUCTION UI CONSUMER FOUND** rather than claiming the portrait feature is integrated. Before any removal, consult non-UI consumers, approved asset provenance/owner, planned portrait surfaces and real build/render test evidence. Do not create private-state-driven effects merely to turn test-only assets into UI assets.

### 30.1D Procedural UI chrome member/consumer matrix — 2026-10-08

**Documentation-only / no task claim.** At inspected authority HEAD `63cf6705888b8da2a8681b0ed9243586b9d3a6f1`, this review compared all 17 `PixelUiChromeCatalog.kt::produced` members with production references across all 29 Kotlin files under `android/app/src/main/java/com/thegame/rpg/ui/`, plus `GameViewModel.kt` and `MainActivity.kt`, and read `PixelUiChromeCatalogTest.kt`. This is source-reference evidence, **not** a compiled/runtime coverage claim, a repo-wide removal decision or completion of D-026/D-021. Historical provenance stays in [UI/FX provenance](../assets/UI_FX_ANIMATION_PROVENANCE_2026-10-03.md), section 2.

| Existing asset ID(s) | Direct current source consumer | Member-level disposition |
| --- | --- | --- |
| `UI_PANEL_STORY_FRAME` | `PixelUiChromeCatalog.panel(PixelPanelChrome.STORY)` via `PixelComponents.kt::PixelPanel` default; story panels/avatar variants use that default. | KEEP — live panel path. |
| `UI_PANEL_CHARACTER_FRAME` | `CharacterSection.kt` passes `PixelPanelChrome.CHARACTER` through `PixelPanel`, `PlayerStatusSummary`, `StatusResourceGrid` and avatar panel paths. | KEEP — live panel path. |
| `UI_PANEL_STATS_FRAME` | `StatsSection.kt` and `StatusComponents.kt` select `PixelPanelChrome.STATS`; `GameScreen.kt` also calls `PixelUiChromeCatalog.statsFrame` for one direct chrome. | KEEP — live panel path. |
| `UI_PANEL_INVENTORY_FRAME` | `GameScreen.kt` selects `PixelPanelChrome.INVENTORY` for Loadout/Bag. | KEEP — live panel path. |
| `UI_PANEL_QUEST_FRAME` | `GameScreen.kt` selects `PixelPanelChrome.QUEST` for quest/category panels. | KEEP — live panel path. |
| `UI_PANEL_MAP_FRAME` | `GameScreen.kt` selects `PixelPanelChrome.MAP` for the public map panel. | KEEP — live panel path. |
| `UI_PANEL_SETTINGS_FRAME` | `GameScreen.kt` selects `PixelPanelChrome.SETTINGS` for Settings/Narration/Session/More panels. | KEEP — live panel path. |
| `UI_PANEL_DEVELOPER_FRAME` | `GameScreen.kt` selects `PixelPanelChrome.DEVELOPER` for the developer section. | KEEP — live, section-gated panel path. |
| `UI_MODAL_FRAME` | `CharacterSection.kt` selects `PixelPanelChrome.MODAL`; the `PixelPanel` mapper resolves the modal frame. | KEEP — live modal-styled panel path. |
| `UI_CHOICE_CARD_ENABLED`, `UI_CHOICE_CARD_DISABLED` | `PixelComponents.kt::PixelChoiceCard` uses public `choice.enabled && !busy` to pick one asset before applying `.clickable(enabled = enabled)`. | KEEP — direct public-state conditional consumer. |
| `UI_CHOICE_CARD_SELECTED` | **No direct production reference found** to `choiceSelected` among audited UI source files; appears in catalog definition/`produced` list. | RETAIN / **DEFINED, NO PRESENT UI CONSUMER VERIFIED**; do not claim a selected-choice visual currently ships. |
| `UI_BUTTON_PRIMARY` | `GameScreen.kt` and `CharacterSection.kt` apply `buttonPrimary` via `.pixelChrome` / their button components. | KEEP — live button path. |
| `UI_BUTTON_SECONDARY` | `CharacterSection.kt` supplies `buttonSecondary` to its button chrome parameter. | KEEP — live button path. |
| `UI_BUTTON_DANGER` | **No direct production reference found** to `buttonDanger` among audited UI source files; appears in catalog definition/`produced` list and `PixelUiChromeCatalogTest.kt` distinction assertion. | RETAIN / **DEFINED, TEST-REFERENCED, NO PRESENT UI CONSUMER VERIFIED**; not evidence of a destructive-action button on screen. |
| `UI_TAB_ACTIVE`, `UI_TAB_INACTIVE` | `GameScreen.kt` selects `tabActive` or `tabInactive` from the `active` flag in its navigation-tab chrome. | KEEP — live presentation-selection path, not navigation authority. |

**Implementation boundary:** `PixelUiChromeCatalog.panel` maps nine `PixelPanelChrome` variants. `PixelComponents.kt::PixelPanel` feeds that asset into `Modifier.pixelChrome`; the modifier draws hard-edged frames with Compose `drawBehind` and uses no required PNG/9-slice raster export. Screen selection and click/choice legality remain separate from these color/frame definitions. `choiceSelected` and `buttonDanger` being enumerated in `produced` is an asset-existence assertion, not proof of active-screen usage.

**Test-source limits:** `PixelUiChromeCatalogTest.kt` checks 17 unique `UI_` IDs, all nine panel-kind mappings and distinct IDs for enabled/disabled choices, active/inactive tabs and primary/danger buttons. It does not assert any production call to `choiceSelected` or `buttonDanger`; it does not cover rendered contrast, touch targeting, state accessibility, animation or screenshot fidelity. **No Gradle, instrumentation, emulator, device or APK tests were executed in this review.**

**Follow-up:** If a selected-choice or danger-button variant is later required, introduce a deliberate and tested source consumer while keeping choice legality and destructive-action confirmation outside the chrome catalog. Before deleting either unused-for-UI member, check non-UI/transitive consumers, the asset owner/provenance plan and rebuild acceptance evidence. Remaining catalog-member inventory, final APK and accessibility QA are still open.

### 30.1E Equipment-slot icon and item-quality frame consumer matrix — 2026-10-08

**Documentation-only / no task claim.** Inspected authority HEAD `170c9e9351cfed1bb129d1461397f08b8bf3f59a` for `PixelEquipmentSlotCatalog.kt`, `PixelItemQualityFrameCatalog.kt`, `PixelComponents.kt`, `CharacterSection.kt`, `GameScreen.kt` and the dedicated Kotlin catalog unit-test sources. This checks **12 equipment-slot IDs and two quality-frame IDs** against their runtime selectors, not final APK accessibility or a complete member-level zero-consumer inventory. Historical roots/stages remain in [Character, Equipment, Item, and Actor Asset Provenance](../assets/CHARACTER_EQUIPMENT_ITEM_ACTOR_PROVENANCE_2026-10-03.md), §§6–7.

| Existing asset ID(s) | Explicit source selector | Actual consumer path and rendering condition |
| --- | --- | --- |
| `UI_EQUIPMENT_SLOT_HEAD`, `UI_EQUIPMENT_SLOT_CHEST`, `UI_EQUIPMENT_SLOT_HANDS`, `UI_EQUIPMENT_SLOT_LEGS`, `UI_EQUIPMENT_SLOT_FEET` | `PixelEquipmentSlotCatalog.slot` maps `head`, `body`, `hands`, `legs`, `feet` respectively. | `CharacterSection.kt::CharacterSlotCard`, `GameScreen.kt` Loadout detail/slot tile and generic slot icon paths call the selector on **projected** `slot.slot`; icons substitute for an absent/undisplayable equipped item sprite, not the item state. |
| `UI_EQUIPMENT_SLOT_MAIN_HAND`, `UI_EQUIPMENT_SLOT_OFF_HAND` | `slot("main_hand")`, `slot("off_hand")`. | Same semantic slot placeholders; they do not enforce handedness, equipment compatibility or combat loadout authority. |
| `UI_EQUIPMENT_SLOT_RING_1`, `UI_EQUIPMENT_SLOT_RING_2`, `UI_EQUIPMENT_SLOT_NECK` | `slot("ring_1")`, `slot("ring_2")`, `slot("neck")`. | Separate slot IDs are preserved even where visible art could look related; the catalog does not combine, invent or infer occupied slots. |
| `UI_EQUIPMENT_SLOT_ACCESSORY_1`, `UI_EQUIPMENT_SLOT_ACCESSORY_2` | `slot("accessory_1")`, `slot("accessory_2")`. | Both mapped to distinct 24×24 icons; unknown `slotId` returns null rather than inventing an icon. |
| `UI_ITEM_QUALITY_FRAME_STANDARD` | `PixelItemQualityFrameCatalog.forQuality("standard")` maps to `standardFrame`. | `PixelComponents.kt::PixelItemIcon` draws the separate 32×32 decoration **only if** an item sprite exists and a recognized projected quality is supplied. |
| `UI_ITEM_QUALITY_FRAME_UNCOMMON` | `forQuality("uncommon")` (case-insensitive via lowercase) maps to `uncommonFrame`. | Same optional decoration; includes shape ornament for differentiation beyond color; unknown, absent or unrecognized quality yields **no quality frame**. |

**Member consumer interpretation:** all 12 defined equipment icons are reachable through the shared `slot(slotId)` selector and all 12 slot IDs are explicitly exercised by `PixelEquipmentSlotCatalogTest.kt`; this is **conditional direct consumer coverage**, not evidence that every icon appears in every session or that all hypothetical equipment-slot identifiers are supported. `CharacterSlotCard` shows item art when `slot.equipped` and its item icon is known, else the semantic slot icon. `GameScreen.kt` follows comparable conditional rendering, with its detail panel showing `PixelItemIcon` for a non-null equipped item ID. These visual choices do not change `GameEquipmentSlot` truth.

**Quality fallback distinction:** `PixelItemIcon` first resolves the item itself with `PixelAssetCatalog.itemIcon(itemId)` and optionally a raster; it draws `qualityFrame` only inside the recognized-item branch. An **unknown item ID** renders `?`, not a quality frame over a nonexistent item. A **known item ID with unknown quality** still renders its item art without a quality frame. `"legendary"` is currently an unsupported visual lookup, **not** a finding about the authoritative item-quality taxonomy or a request to silently add a rare tier.

**Existing test-source evidence:** `PixelEquipmentSlotCatalogTest.kt` checks 12 unique IDs, exact 24×24 grids/palette keys, the 12 known slot-name mappings and null for an unknown slot. `PixelItemQualityFrameCatalogTest.kt` checks both unique 32×32 transparent masters, palette keys, `standard`/`UNCOMMON` lookup and null for null/`legendary`/empty quality. Neither test exercises actual Compose slot-card fallback, rendered frame/testTag visibility, color accessibility or a device. **No tests, Android build, CI, emulator or phone run were executed in this documentation pass.**

**Disposition:** KEEP all 14 source members; no zero-consumer claim is supported for these selectors. Do not replace slot IDs with item art IDs, infer hidden equipment, migrate quality legality to Compose or delete members based on a conditional absence in one screenshot. Future source-to-render regression tests should check the two distinct fallback paths and conditional quality frame visibility.


### 30.1F Environment decals and composited overlay consumers

**Bounded source-only audit, no task claim.** Four environment member IDs and their transitive consumers were compared against the existing provenance registry. This supplements, not replaces, [environment provenance](../assets/ENVIRONMENT_SCENE_MAP_PROVENANCE_2026-10-03.md) and the historical [member audit](PIXEL_MEMBER_ASSET_ID_CONSUMER_AUDIT_2026-10-04.md).

| Asset ID | Selection and live consumer |
| --- | --- |
| `EVACUATION_SIGNAGE_SET` (24x24) | `PixelEnvironmentDecalCatalog.placements(locationId)` returns this for `PLATFORM_NINE`, `EVAC_STAIR`, `DISTRICT_PLAZA`; `SceneIllustration.kt` draws the returned sprite and position. |
| `DISTRICT_AMBIENT_DECAL_SET` (32x32) | Same selector and renderer, for `PLATFORM_NINE`, `SERVICE_TUNNEL`, `DISTRICT_PLAZA`; unknown locations yield no decals. |
| `BLACKOUT_SHADOW_OVERLAY` (128x64) | `PixelEnvironmentOverlayCatalog.blackoutShadows` is the first input to `PixelSceneOverlayCatalog.districtPlazaBlackout` via `compose(...)`. It is a used composite input, not a standalone scene selector. |
| `EMERGENCY_LIGHT_OVERLAY` (128x64) | `PixelEnvironmentOverlayCatalog.emergencyLights` is the second input to the same composite; later nontransparent pixels overwrite earlier pixels. |

`PixelSceneOverlayCatalog.forScene("DISTRICT_HUB")` returns the composite `DISTRICT_PLAZA_BLACKOUT` and `SceneIllustration.kt` draws it over the base scene, followed by visual-state overlay, decals and props. `DISTRICT_PLAZA` is a decal **location** selector whereas `DISTRICT_HUB` is a scene-overlay **scene** selector; neither key alone proves both render together. The catalog reads public location/scene keys, not hidden route/hazard legality. Visual emergency signage and light strips do not independently authorize travel or indicate that a hazard is safe.

**Existing test-source evidence:** `PixelEnvironmentDecalCatalogTest.kt` covers both exact assets and four location lookups; `PixelEnvironmentOverlayCatalogTest.kt` covers both native masters and the two-layer composite; `PixelSceneOverlayCatalogTest.kt` defines scene-overlay selector assertions. These test files were read but **not run**. No Compose stacking screenshot, accessibility, performance, CI, Android build, emulator or phone verification was performed.

**Disposition:** KEEP all four current source members; a source layer used in composition is not unused. Retain current owners, provenance and layer order. Any future removal or merge requires rendered replacement evidence and rollback review. This subsection does not close Master D-026/D-021 or create a new state owner.

### 30.2 Hardcoded/transitional state found during consumer audit

The original audit found scene/location-derived actor presence. **D-064 resolved that item.** Current transitional or presentation-local state includes:

1. `SceneIllustration` location-specific procedural fallback geometry;
2. `SceneIllustration` special-case `RELAY_WORKBENCH` relay placement;
3. `GameScreen` local section/settings/selected-map-node state;
4. `GameViewModel` travel-transition token/from/to presentation state;
5. Settings narration rate, auto-read and text-reveal controls;
6. developer cheat-code text input.

Classification:

- items 3–6 are legitimate application/transient state and should remain outside authoritative saves unless a later product requirement says otherwise;
- items 1–2 are presentation migration debt, not gameplay authority;
- room-actor **presence** is no longer part of this debt because D-064 moved it to the player-safe room projection;
- none of these findings justify raw-state access in Compose.

## 31. Updated D-026 audit boundary

The **file-level pixel catalog consumer audit is now complete** for the current source set.

Still required before D-026/D-021 can be considered reconstruction-complete:

1. member/asset-ID level zero-consumer matrix;
2. exact `GameSnapshot` field/action -> test method coverage/gap matrix;
3. broader D-064 room-actor coverage plus remaining D-030 contextual-panel/interaction consumer mapping;
4. future activity/combat/hierarchical-map/adversary/evolved-status projection records and their implementation acceptance;
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
2. D-064 actor-coverage/contextual-panel follow-through rather than re-implementing room presence projection;
3. future projection contracts and implementation acceptance;
4. final destination APK migration mapping;
5. runtime execution evidence for future code-changing slices.

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

## 36. Wave-4 P17 / D-026 — Persistent-adversary intel migration

**Status:** OR-037 bounded documentation child delivered; V09 persistent-adversary runtime and Android intel projection NOT implemented. **Owner:** Kestrel / P17. The exact CURRENT/PROPOSED split, V09 social/NPC knowledge provenance, optional Python `adversary_intel` domain, typed Android consumer, player-safe allowlist/denylist, OR-015 projection version/error and legacy compatibility, action delegation and future test matrix are in the [P17 adversary-intel projection migration contract](P17_D026_PERSISTENT_ADVERSARY_INTEL_PROJECTION_MIGRATION_2026-10-08.md).

- **Present:** `GameState.npcs` and `social.py` ordinary NPC memory/knowledge owners; `AndroidGameSession._view_for` and current 21-field Kotlin `GameSnapshot` have **no** adversary-intel domain or action.
- **Proposed:** V09 nested adversary-specific state (not a second actor registry), public observer-knowledge-filtered intel, additive independent domain version, strict typed Kotlin mapper, no raw private memory/adaptation/hidden-location exposure in UI or accessibility.
- **Canon:** OR-034 temporary combat contacts are not persistent V09 identities; Gate Twelve adversary proof remains proposed and non-Phase-1-required.
- **Verification:** [P17 evidence](../evidence/P17_D026_ADVERSARY_INTEL_PROJECTION_2026-10-08.md): 7/7 relative document links and 11/11 named source/test paths verified on a non-truncated exact Git tree; no executable tests/CI/emulator/device.
- **Remaining:** Master D-026 IN_PROGRESS for activity, evolved-status, final APK consumer migration, future V09/tactical/hierarchy implementation and runtime/build acceptance. P17 closes only the bounded **documentation** slice.
