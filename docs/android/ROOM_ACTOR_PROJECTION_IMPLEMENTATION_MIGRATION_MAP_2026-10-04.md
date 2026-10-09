# THE GAME — Room Actor Projection Implementation Migration Map — 2026-10-04

Status: **IMPLEMENTATION-READY DOCUMENTATION / RUNTIME NOT CHANGED**  
Repository: `jbob-coder/Text-rpg-game`  
Branch: `docs/master-game-development-program`  
Audited source HEAD: `2379608bb7f45c5dd82b929c813670a4c8aef5bf`

Parent contract:

`docs/android/PLAYER_SAFE_ROOM_ACTOR_PROJECTION_CONTRACT.md`

Related current-state evidence:

- `docs/android/ANDROID_CONSUMER_FIELD_AUDIT_2026-10-04.md`
- `docs/android/ANDROID_NAVIGATION_AND_EPHEMERAL_STATE_AUDIT_2026-10-04.md`
- `docs/android/PIXEL_MEMBER_ASSET_ID_CONSUMER_AUDIT_2026-10-04.md`
- `docs/DEEP_SOURCE_EXISTING_STATE_AUDIT_2026-10-04.md`

Task: **D-030 runtime migration planning**.

---

## Current-state supersession note — 2026-10-08

This packet is a **historical pre-implementation migration plan** audited at `2379608bb7f45c5dd82b929c813670a4c8aef5bf`. Its later repeated "current has no room" and `PixelStoryActorCatalog.placements(locationId, sceneId)` descriptions refer to that original baseline, **not** current branch behavior. Do not execute its D-030 room-presence migration as if still outstanding.

D-064 implemented and verified Python `AndroidGameSession._room_view_for` -> typed `GameRoomProjection` / `GameRoomActor` -> `GameScreen.kt` -> `SceneIllustration(roomActors)` -> `PixelStoryActorCatalog.placements(roomActors)` with safe `visualFamily` and semantic `placementKey`. See [D-064 final evidence](../evidence/D064_PLAYER_SAFE_ROOM_ACTOR_PROJECTION_FINAL_2026-10-05.md) (PR #70, workflow run #362), [active room projection contract](PLAYER_SAFE_ROOM_ACTOR_PROJECTION_CONTRACT.md), and [current asset provenance addendum](../assets/CHARACTER_EQUIPMENT_ITEM_ACTOR_PROVENANCE_2026-10-03.md#96-post-d-064-current-state-addendum--2026-10-08). The historical plan and requirement fixtures below remain valuable provenance; implementation status must follow current code and Bulletin/Master. Context/focus-panel, art/pose/outfit expansion is not automatically completed by D-064. No new code or runtime tests executed for this note.

## 1. Purpose

The D-030 contract already defines the target player-safe `room` projection.

This document converts that target into an exact bounded implementation sequence against the current repository.

The objective is to replace:

`sceneId + locationId -> PixelStoryActorCatalog.placements(...)`

with:

`engine/content-visible actor presence -> player-safe room projection -> Kotlin typed room -> semantic placement resolver -> existing actor art`

without changing save schema, leaking private NPC state, breaking the opening story, or discarding existing Tamsin/courier art.

No runtime code is changed by this document.

---

## 2. Verified current implementation path

### Python/content

Current authored source:

`content/vertical_slice_01.json`

Current opening actor presentation is **not** authored as room presence records.

Current bridge:

`src/textrpg/android_bridge.py`

`AndroidGameSession._view_for()` currently emits:

- `scene`;
- `status`;
- `inventory`;
- `quests`;
- `map`;
- `visuals`;
- `meta`.

It does not emit `room`.

Current content validation:

`src/textrpg/validation.py`

`validate_scenes()` validates scene/choice structure, but there is no dedicated player-visible actor-presence validation contract yet.

### Kotlin bridge

Current model:

`android/app/src/main/java/com/thegame/rpg/engine/GameEngine.kt`

`GameSnapshot` has no `room` field.

`BridgeSnapshotMapper.fromMap()` has no room mapper.

### Compose

Current scene renderer:

`android/app/src/main/java/com/thegame/rpg/ui/SceneIllustration.kt`

Current signature:

`SceneIllustration(locationId, sceneId, relayState, modifier)`

Current actor-presence decision:

`PixelStoryActorCatalog.placements(locationId, sceneId)`

Current caller:

`android/app/src/main/java/com/thegame/rpg/ui/GameScreen.kt`

Both Story scene-rendering call sites pass only location, scene ID and relay state.

---

## 3. Required opening equivalence records

The first migration must preserve the exact currently visible actor compositions.

### OPENING_DEPOT_BLACKOUT / PLATFORM_NINE

Required projected actors:

1. support courier;
2. Tamsin.

Existing presentation positions that must be preserved through semantic placement keys:

- courier: x=34, y=13;
- Tamsin: x=62, y=14.

### OPENING_DECISION / PLATFORM_NINE

Required:

- Tamsin only;
- x=62, y=14.

### OPENING_RECOVERY / RELAY_WORKBENCH

Required:

- Tamsin only;
- x=90, y=14.

### OPENING_TUNNEL / SERVICE_TUNNEL

Required:

- Tamsin only;
- x=76, y=14.

### All other current scene/location pairs

Required:

- no actor projection unless explicitly authored/evaluated by the engine/content layer.

No actor may be inferred from narrative prose.

---

## 4. File-level implementation map

| Order | File | Required bounded change | Save/runtime risk |
| --- | --- | --- | --- |
| 1 | `content/vertical_slice_01.json` | add player-safe authored actor-presence records to the four opening scenes | low if additive and validated |
| 2 | `src/textrpg/validation.py` | validate optional scene actor-presence records and reject malformed/duplicate presentation identities | medium: malformed content must fail closed |
| 3 | `src/textrpg/android_bridge.py` | add `_room_view_for(state)` and top-level `room` projection | high privacy boundary; must redact |
| 4 | `tests/test_android_bridge.py` and/or focused room test | add equivalence, redaction and non-mutation tests | required before UI switch |
| 5 | `android/.../engine/GameEngine.kt` | add typed `GameRoom` / `GameRoomActor`, defaulted `GameSnapshot.room`, strict mapper validation | medium compatibility risk |
| 6 | Android mapper tests | validate room mapping/version/location/duplicates/speaker references | required |
| 7 | new semantic placement catalog or refactored actor catalog | map `locationId + placementKey` to x/y/z while keeping existing actor sprite masters | presentation-only |
| 8 | `PixelStoryActorCatalog.kt` | retain visual-family/sprite ownership; stop owning presence decision after cutover | migration-sensitive |
| 9 | `SceneIllustration.kt` | consume projected room actors instead of `placements(sceneId, locationId)` | visible-equivalence risk |
| 10 | `GameScreen.kt` | pass `snapshot.room` into both Story scene-rendering call sites | low once model exists |
| 11 | Compose/instrumented tests | prove opening actor equivalence, zero/one/multiple actor behavior and narrow-phone behavior | required |
| 12 | contextual actor panel slice | add Android-local selected presentation ID and panel shell only after room projection is stable | UI-only, not save state |
| 13 | old heuristic removal | remove scene/location actor-presence decision only after equivalence gates pass | irreversible behavior change unless rollback preserved |

---

## 5. Content record migration

Phase one should add optional scene-level actor records rather than inventing durable NPC location state.

Recommended current-content shape remains subordinate to the D-030 contract:

```json
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
```

The support courier uses a public support presentation identity and must **not** be promoted to durable `state.npcs` merely to satisfy the Android API.

Suggested semantic placement keys for equivalence:

- `PLATFORM_NINE_COURIER_LEFT`;
- `PLATFORM_NINE_TAMSIN_RIGHT`;
- `RELAY_WORKBENCH_TAMSIN_RIGHT`;
- `SERVICE_TUNNEL_TAMSIN_RIGHT`.

Names may be adjusted before implementation, but raw pixel coordinates must remain Android presentation data rather than bridge payload fields.

---

## 6. Validation migration

`validate_scenes()` should gain a focused helper for optional actor records.

Minimum validation:

- `actors` must be a list when present;
- each entry must be an object;
- `presentation_id` non-empty;
- unique `presentation_id` per scene;
- `public_name` non-empty;
- `visual_family` non-empty;
- `placement_key` non-empty;
- optional `actor_id`, `pose_key`, `outfit_key` must be non-empty strings when present;
- `inspectable` must be boolean when present;
- no raw pixel x/y fields in the player-safe authored record;
- malformed records fail content loading rather than being silently normalized.

Conditional authored presence, if added, stays internal and must be evaluated before projection.

---

## 7. Python projection migration

Add:

`AndroidGameSession._room_view_for(state)`

It should:

1. resolve current authoritative scene;
2. obtain optional authored actor-presence records;
3. evaluate only approved internal visibility conditions;
4. produce a detached player-safe actor list;
5. redact private NPC data;
6. verify projected room location equals the same current location used by `meta.location`;
7. emit deterministic ordering;
8. emit `active_speaker_presentation_id = null` unless explicit player-visible speaker state exists.

Then extend `_view_for()` additively:

```python
"room": self._room_view_for(state),
```

Do not place room actors under `visuals`.

### Privacy invariant

The projection must never serialize whole `state.npcs` entries.

Forbidden leakage includes:

- personality;
- NPC knowledge;
- memories;
- goals;
- private story state;
- relationship maps;
- hidden flags;
- future schedule;
- secret identity;
- undiscovered equipment;
- AI intent.

---

## 8. Python test gate before Kotlin cutover

Required tests:

1. initial depot scene -> courier + Tamsin;
2. opening decision -> Tamsin only;
3. recovery -> Tamsin only;
4. tunnel -> Tamsin only;
5. unrelated current scene -> empty actors;
6. support courier has no fabricated durable NPC identity;
7. projected Tamsin record does not expose private NPC structures;
8. duplicate authored presentation IDs fail validation;
9. malformed actor record fails safely;
10. room projection is detached;
11. projection does not mutate `GameState`;
12. room/meta location mismatch cannot be emitted.

Do not change Compose actor rendering before these pass on the implementation head.

---

## 9. Kotlin model migration

Add model types conceptually equivalent to the existing contract:

`GameRoomActor`

and:

`GameRoom`.

Then add to `GameSnapshot`:

`val room: GameRoom = GameRoom()`

Migration compatibility:

- absent `room` -> default empty room only during the controlled migration window;
- present `room` -> strict validation;
- unsupported projection version -> mapper failure;
- duplicate presentation ID -> mapper failure;
- room location != meta location -> mapper failure;
- active speaker ID not present in room actor IDs -> mapper failure.

This is player-safe view state and is not serialized into the Python save.

---

## 10. Android placement architecture

Do not make the bridge emit x/y.

Create or refactor a presentation-owned placement resolver with a contract like:

`resolve(locationId, placementKey) -> x/y/z/occlusion packet`.

Initial equivalence mapping:

| Location | Placement key | Existing x/y |
| --- | --- | ---: |
| PLATFORM_NINE | PLATFORM_NINE_COURIER_LEFT | 34,13 |
| PLATFORM_NINE | PLATFORM_NINE_TAMSIN_RIGHT | 62,14 |
| RELAY_WORKBENCH | RELAY_WORKBENCH_TAMSIN_RIGHT | 90,14 |
| SERVICE_TUNNEL | SERVICE_TUNNEL_TAMSIN_RIGHT | 76,14 |

The resolver is Android presentation authority.

The engine chooses safe semantic placement identity; Android chooses actual scene-canvas coordinates.

---

## 11. Actor visual resolver

Current sprite work must survive.

`PixelStoryActorCatalog` should be refactored from:

`presence + placement + visual`

toward:

`visual family + pose -> sprite/layers`.

Initial mappings:

- `NPC_TAMSIN + front` -> existing Tamsin sprite;
- support courier visual family + wounded/guarded pose -> existing courier sprite.

Do not delete current actor sprites during migration.

PR #9 held diagnostic-reader art remains downstream:
- it becomes eligible only after Tamsin projection can safely emit an approved pose/held-layer key;
- Tamsin hand/wrist anchors must be verified separately.

---

## 12. SceneIllustration cutover

Target signature should accept the room projection or actor list.

Example direction:

`SceneIllustration(locationId, sceneId, relayState, roomActors, modifier)`

During the migration window:

- scene ID may continue driving scene overlays and Trace FX;
- relay state continues driving relay presentation;
- location continues selecting scene/map presentation;
- **roomActors becomes the only actor-presence source after cutover**.

Cutover step:

remove:

`PixelStoryActorCatalog.placements(locationId, sceneId)`

only after projected-actor equivalence passes.

Do not retain a silent fallback to old scene-ID actor inference after the final cutover, because that would reintroduce duplicate truth.

---

## 13. GameScreen changes

Both current `SceneIllustration` call sites in Story must pass the same authoritative `snapshot.room` data.

No separate actor inference should exist between wide and narrow layouts.

The Story layout remains presentation-only.

---

## 14. Context panel implementation slice

Do this **after** actor rendering equivalence.

Android-local state:

`selectedActorPresentationId: String?`

Lifecycle:

- default null;
- set only from an inspectable projected actor;
- clear when actor disappears;
- clear on location change;
- clear on loaded/replaced snapshot if no longer valid;
- never save it.

Panel content may use only:
- projected public fields;
- approved visual/portrait assets.

Do not add relationship meters under D-030.

---

## 15. Save boundary

No save schema change is required for phase one.

Do not persist:

- `GameRoom`;
- room actors;
- semantic placement keys as runtime state;
- selected actor;
- pixel coordinates;
- panel open state.

Existing durable `GameState.npcs` remains authoritative where applicable.

A future durable schedule/location system would require a separate schema migration.

---

## 16. Rollback design

Before final heuristic removal, preserve one commit boundary where:

- new room projection is fully implemented;
- old actor placement path still exists but is not the selected production path;
- equivalence tests can compare both outputs.

If post-cutover failures appear:

1. revert the SceneIllustration consumer switch;
2. leave additive room projection/model code intact if safe;
3. restore old presentation path temporarily;
4. fix projection/placement mismatch;
5. rerun equivalence gates;
6. cut over again.

Do not roll back by exposing raw NPC state to Compose.

---

## 17. Required verification matrix

### Python

- content validation;
- room projection equivalence;
- privacy/redaction;
- no mutation;
- current Android bridge tests;
- save/load regression.

### Android JVM

- valid room mapper;
- absent room migration default;
- bad version;
- duplicate IDs;
- location mismatch;
- invalid speaker;
- malformed actor field;
- current mapper/privacy regression.

### Compose/instrumentation

- zero actors;
- one actor;
- multiple actors;
- support actor;
- opening four equivalence compositions;
- actor disappearance;
- location change;
- non-inspectable actor;
- missing-art fallback;
- phone width;
- large text;
- Story choice behavior unchanged;
- relay overlay independent from room projection.

### Build/package

- Android JVM test task;
- instrumented/emulator gate when available;
- APK build;
- exact-head artifact provenance.

Physical Galaxy A03 visual acceptance remains a later gate.

---

## 18. Completion boundaries

### Documentation migration map complete when

- every touched file/responsibility is identified;
- compatibility sequence is explicit;
- test gates are explicit;
- rollback path is explicit;
- save/privacy boundaries are explicit.

This document satisfies that documentation boundary.

### Runtime D-030 complete only when

- room projection is implemented;
- current opening visible actors are equivalent;
- Android no longer infers actor presence from scene/location;
- hidden NPC state remains redacted;
- typed mapper/failure tests pass;
- selected actor remains transient;
- save schema remains compatible;
- exact-head build/test/evidence gates pass.

Runtime D-030 remains **PENDING** after this document.
