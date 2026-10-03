# Player-Safe Room Actor & Context Panel Projection Contract

Status: **ACTIVE TARGET CONTRACT / IMPLEMENTATION PENDING**  
Repository: `jbob-coder/Text-rpg-game`  
Program branch: `docs/master-game-development-program`  
Source-audit baseline: `7703d67e7c6a80a0b2394312e8ad8895d2d88ae6`

Parents:
- `docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md`
- `docs/assets/ROOM_COMPOSITION_IMPLEMENTATION_CONTRACT.md`
- `docs/assets/ROOM_ACTOR_PANEL_OVERLAY_REUSE_STANDARD.md`
- `docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md`

Task: D-030.

## 1. Purpose

Define the exact player-safe projection boundary required to replace Android scene/location actor inference with engine/content-owned room presence while preserving the current opening-story visuals.

This document specifies an API target. It does **not** claim the API is implemented.

## 2. Verified current source state

At the audited baseline:

### Python authoritative state

`src/textrpg/core.py` `GameState` already stores:
- `relationships`;
- `knowledge`;
- `npcs`;
- `party`;
- quests, flags, inventory, equipment, perks and history.

`state.npcs` is durable authoritative state. It is not a player-facing projection.

`src/textrpg/social.py` NPC shells may contain private/internal structures including:
- personality;
- knowledge;
- memories;
- goals;
- story state.

These structures must never be serialized wholesale to Android.

### Current bridge

`AndroidGameSession._view_for()` currently returns exactly these top-level player-facing groups:

- `scene`;
- `status`;
- `inventory`;
- `quests`;
- `map`;
- `visuals`;
- `meta`.

`_visuals_view_for()` currently projects only `relay_state` and explicitly avoids raw flags/private records.

This existing redaction style is the model for actor projection.

### Current Kotlin snapshot

`GameSnapshot` currently contains:
- scene/text/choices;
- status;
- identity;
- inventory;
- quests;
- world map;
- `GameVisuals(relayState)`;
- turn/time/location/content metadata.

There is no room actor record.

### Current Android actor behavior

`SceneIllustration` receives:
- `snapshot.location`;
- `snapshot.sceneId`;
- `snapshot.visuals.relayState`.

It then calls:

`PixelStoryActorCatalog.placements(locationId, sceneId)`

The current actor catalog hard-codes:

| Scene | Location | Current presentation |
| --- | --- | --- |
| `OPENING_DEPOT_BLACKOUT` | `PLATFORM_NINE` | wounded courier at 34,13; Tamsin at 62,14 |
| `OPENING_DECISION` | `PLATFORM_NINE` | Tamsin at 62,14 |
| `OPENING_RECOVERY` | `RELAY_WORKBENCH` | Tamsin at 90,14 |
| `OPENING_TUNNEL` | `SERVICE_TUNNEL` | Tamsin at 76,14 |

Those coordinates are 128x64 scene-canvas sprite origins. They are presentation coordinates, not world coordinates and not authoritative NPC location.

### Current content facts

`content/vertical_slice_01.json` currently defines:
- durable `NPC_TAMSIN` in `initial_state.npcs`;
- a player relationship to `NPC_TAMSIN`;
- one canonical character-visual identity record for `NPC_TAMSIN`;
- no general room-presence field in scene records;
- scene records with `location_id`.

The wounded courier is currently a visual/story support actor, not a durable NPC record in `initial_state.npcs`.

## 3. Ownership decision

### Engine/content owns

The authoritative layer decides:
- whether a person/support actor is currently present;
- whether the player is allowed to perceive that presence;
- whether identity/name is known;
- public presentation role;
- safe visible condition tags;
- safe pose/presentation variant;
- whether inspection/dialogue is allowed;
- which public presentation record identifies this visible actor.

### Android owns

Android decides:
- pixel-space x/y;
- z-order and occlusion resolution;
- portrait/panel layout;
- responsive panel sizing;
- focus/selection animation;
- local transient selected actor;
- which approved asset corresponds to a safe presentation key.

### Asset catalogs own

Asset registries/catalogs decide:
- sprite ID;
- portrait ID when one exists;
- equipment/held-object layers;
- pose art;
- missing-art fallback.

### UI must not infer

Android/Compose must not infer actor presence from:
- scene ID;
- location ID alone;
- narrative prose;
- raw quest flags;
- `state.npcs`;
- NPC goals/memories;
- relationships;
- hidden story state.

## 4. Target bridge payload

Add a new top-level player-facing object named `room`.

Do not place actor presence inside `visuals`; presence is domain/player-knowledge state, not merely artwork state.

Target shape:

```json
{
  "room": {
    "projection_version": 1,
    "location_id": "PLATFORM_NINE",
    "actors": [
      {
        "presentation_id": "NPC_TAMSIN",
        "known_actor_id": "NPC_TAMSIN",
        "display_name": "Tamsin",
        "visual_family": "NPC_TAMSIN",
        "placement_key": "PLATFORM_NINE_TAMSIN_RIGHT",
        "pose_key": "front",
        "outfit_key": "default",
        "visible_tags": [],
        "inspectable": true,
        "dialogue_available": false,
        "actions": []
      }
    ],
    "active_speaker_presentation_id": null
  }
}
```

The example is schema illustration, not proof that those exact placement strings already exist in runtime content.

## 5. Room projection fields

### `projection_version`

Integer. Start at 1.

Purpose:
- permit schema evolution;
- let Kotlin reject unsupported incompatible payload versions.

It is not the save schema version.

### `location_id`

Required non-empty string.

Must equal the bridge's projected current location for the same snapshot.

Mismatch is a projection error, not a UI condition.

### `actors`

Ordered list of currently visible/player-perceivable actor presentation records.

Ordering must be deterministic.

Ordering is not pixel z-order. Android placement/area packets own z-order.

### `active_speaker_presentation_id`

Optional.

Use only when the narrative system explicitly knows a player-visible current speaker.

Current prose-only scenes do not justify inferring this field from text, therefore phase-one opening equivalence may leave it null.

## 6. Actor projection fields

### `presentation_id` — required

Player-safe stable identity for one visible presentation entry.

It must be unique inside the room projection.

It may equal a known domain actor ID when exposing that ID is safe.

For an anonymous/unidentified/support actor, use a public presentation identity that does not reveal hidden domain identity.

### `known_actor_id` — optional

Expose only when the player is allowed to know the durable actor identity.

Never expose a hidden NPC stable ID solely so Android can find art.

### `display_name` — required

Player-authorized display label.

Examples of valid classes:
- known name;
- observed role such as “Wounded courier”;
- neutral unknown label.

Do not derive it from an internal stable ID if that would reveal undiscovered identity.

### `visual_family` — required

Player-safe asset-family lookup key.

It identifies the approved visual family, not a raw NPC state object.

It must not leak an undiscovered identity. Unknown actors use an anonymous/support visual family.

### `placement_key` — required for current static 128x64 scenes

Semantic presentation-slot key.

Engine/content may select the safe slot identity; Android area composition maps the key to x/y/z/occlusion.

The bridge must not emit raw 128x64 pixel coordinates.

Long-term simulated NPC positioning may later use a separate player-safe spatial record, but that is outside phase one.

### `pose_key`

Optional player-safe approved pose key.

It must resolve against the actor visual family/identity contract.

Unknown pose falls back safely; Android does not invent a pose from mood/goals.

### `outfit_key`

Optional player-safe visible outfit/presentation variant.

It does not grant or alter equipment.

If no authored visual variant exists, logical state remains unchanged and UI uses the documented missing-art path.

### `visible_tags`

List of explicitly player-visible condition/presentation tags.

Examples may include an authored visible injury state, but never hidden diagnoses, secret status IDs or future consequences.

The bridge owns redaction.

### `inspectable`

Boolean.

Controls whether the UI may open a contextual focus panel.

It does not itself expose extra NPC state.

### `dialogue_available`

Boolean.

Presentation capability only.

The existing scene-choice system remains authoritative for actual current choice execution until a dedicated actor-action API is implemented.

### `actions`

Phase-one value: empty list.

Reserve for a later player-safe actor-action projection with explicit engine mutation routing.

Do not invent Android-only TALK/GIVE/ATTACK actions merely because an actor is visible.

## 7. Explicitly forbidden fields

The room/actor payload must not include raw:

- `personality`;
- `knowledge`;
- `memories`;
- `goals`;
- `story_state`;
- relationship maps or hidden relationship axes;
- quest prerequisites;
- hidden flags;
- future schedule;
- future appearance scene;
- hidden injury/status;
- AI intent;
- secret faction membership;
- undiscovered equipment;
- internal authored `visible_if` / `requires` expressions;
- raw scene actor conditions;
- raw pixel coordinates if a semantic placement key can express the current need.

## 8. Phase-one authoritative source strategy

The current engine does not yet have NPC position/schedule state sufficient to derive general room presence.

Therefore phase one should use **authored scene presence records evaluated by the engine/content layer**, not Android heuristics.

Recommended source shape in content:

```json
{
  "actors": [
    {
      "presentation_id": "NPC_TAMSIN",
      "actor_id": "NPC_TAMSIN",
      "public_name": "Tamsin",
      "visual_family": "NPC_TAMSIN",
      "placement_key": "PLATFORM_NINE_TAMSIN_RIGHT",
      "pose_key": "front",
      "inspectable": true
    }
  ]
}
```

If conditional presence is required, conditions remain authored/internal and are evaluated before projection. Android receives only the resulting visible list.

Long-term NPC schedules/location simulation may later replace or supplement scene-authored presence behind the same player-safe projection schema.

## 9. Opening-story equivalence migration

The first implementation must reproduce current visible actor behavior before deleting any scene-ID placement heuristic.

Required equivalence fixtures:

### `OPENING_DEPOT_BLACKOUT / PLATFORM_NINE`
Projected:
- support courier presentation;
- Tamsin presentation.

Android placement catalog must reproduce existing visual positions 34,13 and 62,14 through semantic placement keys.

### `OPENING_DECISION / PLATFORM_NINE`
Projected:
- Tamsin only.

Existing position 62,14 preserved through the placement catalog.

### `OPENING_RECOVERY / RELAY_WORKBENCH`
Projected:
- Tamsin only.

Existing position 90,14 preserved.

### `OPENING_TUNNEL / SERVICE_TUNNEL`
Projected:
- Tamsin only.

Existing position 76,14 preserved.

### All other current scene/location pairs
No actor is projected unless content/domain state explicitly says otherwise.

Do not infer people from prose.

## 10. Support courier identity rule

The current wounded courier is not a durable `state.npcs` record.

Phase one must not create a persistent NPC merely to satisfy the visual API.

Use a player-safe support presentation record unless/until game design deliberately promotes that character to a durable NPC.

This preserves current behavior and avoids manufacturing persistence.

## 11. Tamsin identity rule

`NPC_TAMSIN` already has:
- durable NPC state;
- relationship state;
- canonical visual identity data.

The projection may expose `known_actor_id = NPC_TAMSIN` only when current authored player knowledge permits the name/identity.

The bridge still must not expose Tamsin's personality, knowledge, memories, goals, private story state or raw relationship map.

## 12. Kotlin target model

Add types conceptually equivalent to:

```kotlin
data class GameRoomActor(
    val presentationId: String,
    val knownActorId: String? = null,
    val displayName: String,
    val visualFamily: String,
    val placementKey: String,
    val poseKey: String? = null,
    val outfitKey: String? = null,
    val visibleTags: List<String> = emptyList(),
    val inspectable: Boolean = false,
    val dialogueAvailable: Boolean = false,
)

data class GameRoom(
    val projectionVersion: Int = 1,
    val locationId: String = "",
    val actors: List<GameRoomActor> = emptyList(),
    val activeSpeakerPresentationId: String? = null,
)
```

Then extend `GameSnapshot` with a defaulted `room: GameRoom = GameRoom()`.

These are target signatures, not implemented code.

## 13. Mapper validation

`BridgeSnapshotMapper` should:

- treat absent `room` as empty for controlled migration compatibility;
- require supported `projection_version` when `room` exists;
- require non-empty `location_id`;
- reject room/meta location mismatch;
- reject duplicate `presentation_id`;
- reject invalid/empty required strings;
- reject unsupported payload types;
- require `active_speaker_presentation_id`, when non-null, to reference a projected actor;
- ignore unknown additive fields only where the bridge contract already permits forward-compatible unknown fields;
- never normalize malformed actor records into apparently valid actors.

## 14. Android presentation migration

### Before migration

`SceneIllustration(locationId, sceneId, relayState)`
-> `PixelStoryActorCatalog.placements(locationId, sceneId)`
-> fixed actor sprites + fixed x/y.

### Target

`GameSnapshot.room.actors`
-> actor visual-family resolver
-> area/placement-key resolver
-> approved sprite/pose/outfit layers
-> scene composition.

`sceneId` may continue to drive scene overlays/Trace FX where those contracts still require it. It must stop being the source of actor presence.

## 15. Pixel catalog refactor boundary

Do not discard the existing Tamsin/courier sprite work.

Refactor responsibilities:

- keep sprite/visual definitions;
- remove presence decision from `PixelStoryActorCatalog.placements(sceneId, locationId)`;
- move x/y placement to an area placement catalog keyed by location + semantic placement key;
- resolve visual family + pose to the existing sprite assets;
- preserve source/raster/actor provenance.

Only remove the old heuristic after projection equivalence tests pass.

## 16. Context panel behavior

Selection is Android-local transient UI state.

Suggested lifecycle:
- initial selection: none;
- tapping/choosing an inspectable actor selects its `presentation_id`;
- selection remains only while that actor remains in the current room projection;
- clear on actor disappearance;
- clear on location change;
- clear on new game/load replacement;
- clear on invalid/malformed ID;
- do not persist selected actor in save data.

Panel may display only projected/public fields plus asset-derived portrait presentation.

Missing portrait:
- text-only or neutral missing-art treatment;
- never substitute another character.

No visible actors:
- no actor panel.

Multiple actors:
- one focus panel at a time.

## 17. Relationship display boundary

Do not expose the full current relationship map merely because the panel exists.

A future relationship projection must separately define which relationship facts are player-observable.

Until then D-030 does not authorize relationship meters in the actor panel.

## 18. Interaction boundary

Existing scene choices remain the only implemented general narrative action path.

D-030 does not add an actor-action mutation API.

A later actor-action contract must define:
- safe action ID/label;
- enabled state;
- disabled reason;
- engine mutation method;
- transaction/rollback;
- persistence;
- tests.

Compose must never mutate NPC state directly.

## 19. Required Python tests

Extend `tests/test_android_bridge.py` or a focused projection suite with:

1. room root exists after implementation;
2. initial opening projects exactly courier + Tamsin;
3. decision scene projects Tamsin only;
4. recovery scene projects Tamsin only;
5. tunnel scene projects Tamsin only;
6. unrelated scene projects zero actors;
7. projection is detached from authoritative state;
8. raw NPC personality/knowledge/memories/goals/story_state do not appear anywhere in the payload;
9. hidden relationship data does not leak;
10. anonymous/support actor does not expose a durable hidden actor ID;
11. invalid authored presence data fails safely;
12. actor projection does not mutate `GameState`.

## 20. Required Kotlin unit tests

Extend `PythonGameEngineContractTest.kt` or a focused mapper test:

1. valid room payload maps to typed `GameRoom`;
2. absent room maps to empty/default room during migration;
3. duplicate presentation IDs are rejected;
4. unsupported projection version is rejected;
5. location mismatch is rejected;
6. invalid speaker reference is rejected;
7. malformed required strings are rejected;
8. unknown additive root fields remain harmless according to existing mapper policy.

## 21. Required Compose/instrumentation tests

Add cases for:

- zero actors;
- one actor;
- multiple actors;
- support/anonymous actor;
- actor focus open/close;
- actor disappears after choice;
- location changes;
- missing portrait fallback;
- non-inspectable actor;
- large text;
- narrow phone width;
- existing opening actor positions remain visually equivalent;
- Story choices remain functional;
- relay visual projection still renders independently.

## 22. Save/migration impact

Phase-one room projection is derived player-safe view data.

Do not persist:
- room actor projection;
- selected actor;
- portrait panel state;
- pixel placement.

Existing durable NPC state remains in `GameState.npcs`.

If future NPC location/schedule becomes durable, that is a separate save-schema migration and must not be smuggled into this presentation task.

## 23. Failure behavior

If actor projection cannot be built safely:
- bridge returns the existing player-facing view error boundary rather than leaking raw data;
- Android must not fall back to scene-ID actor inference once the old heuristic is retired;
- a missing art mapping should omit/fallback presentation safely without falsifying domain presence;
- presence truth outranks art availability.

## 24. Implementation order

1. add authored opening-scene presence records;
2. add Python player-safe room projection;
3. add Python redaction/equivalence tests;
4. add Kotlin `GameRoom` / `GameRoomActor`;
5. extend mapper validation;
6. add mapper tests;
7. create semantic placement-key -> scene x/y/z catalog;
8. change `SceneIllustration` to consume projected actors;
9. preserve existing opening coordinates through placement keys;
10. add local transient focus-panel selection;
11. add contextual panel shell;
12. run Python + Android + emulator screenshot gates;
13. only then delete the old scene/location presence heuristic.

## 25. Completion definition

D-030 documentation is complete when this contract is indexed.

Runtime implementation is complete only when:
- Android no longer decides actor presence from scene/location;
- the four current opening actor compositions are equivalent;
- hidden NPC state remains absent from bridge payloads;
- typed mapping and failure cases pass;
- panel selection is transient;
- save compatibility is unchanged;
- exact-head Android workflow and screenshot evidence pass.

Physical Galaxy A03 acceptance remains a separate later gate.


## 24. Held-prop presentation boundary

This section is a compatible clarification of the existing target contract. It does not claim implementation.

### Verified current evidence

`content/vertical_slice_01.json` currently includes:

- a Tamsin visual-identity pose labelled `holding diagnostic reader`;
- later player-facing narrative that explicitly describes Tamsin's diagnostic reader.

Divergent PR #9 contains technical source masters:

- `PROP_DIAGNOSTIC_READER_ICON_MASTER` — 32x32;
- `PROP_DIAGNOSTIC_READER_HELD_FRONT_MASTER` — 32x48.

Its manifest explicitly states that:

- the icon is not currently exposed as inventory state;
- the held master has no runtime character binding;
- prop art cannot infer possession, pose, relay interaction, quest progress or story state;
- integration was deferred until character anchors or an explicit player-safe held-prop presentation state exists.

### Target ownership

The existing D-030 model already provides the required authority boundary:

- engine/content decides the safe visible pose/presentation variant;
- asset catalogs own held-object layers;
- Android resolves approved art from the safe actor presentation record.

Therefore a diagnostic reader shown in Tamsin's hand must be driven by an explicit player-safe actor presentation key, not by:

- narrative-text matching;
- scene ID alone;
- location ID alone;
- raw NPC equipment/private state;
- hidden quest flags;
- Android-local possession inference.

### Target resolution path

Conceptually:

`GameSnapshot.room.actors[].poseKey`
-> Tamsin visual-family resolver
-> approved pose/layer mapping
-> `PROP_DIAGNOSTIC_READER_HELD_FRONT_MASTER`
-> scene composition

The exact stable machine key for the authored pose is not locked by this clarification. If `holding diagnostic reader` is normalized to a machine key such as snake_case, the mapping must be explicit and migration-tested.

The 32x32 diagnostic-reader icon is not authorized as a player inventory icon merely because it exists.

### Implementation gate

Do not integrate PR #9's held-prop source until:

1. D-030 room actor projection is implemented or an equivalent approved safe presentation projection exists;
2. Tamsin's selected sprite/turnaround has a verified hand/wrist anchor;
3. the pose-to-held-layer mapping is explicit;
4. hidden/private NPC state is absent from the payload;
5. Compose consumes rather than owns the presentation choice;
6. tests cover unknown pose fallback and no-prose/no-hidden-state inference.

Until then the held-prop family remains `DEFERRED_INTEGRATION`.
