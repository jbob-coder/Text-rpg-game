# CPR-002 — D-064 Android room-actor mapper silently accepts forbidden extra fields

- **STATUS:** REPORTED
- **REPORTER:** Veyr
- **CURRENT_TASK:** bounded D-064 NPC/privacy review support; Veyr has no active primary claim
- **OBSERVED_HEAD:** `f3a5028f0f77539295a2c6dedd1d926005faf11e`
- **DATE:** 2026-10-04
- **BULLETIN_TASK:** candidate existing owner D-064; do not create a duplicate task unless AXIOM finds broader ownership
- **ROOT_CAUSE_STATUS:** hypothesis from exact source/contract audit; no failing runtime test executed
- **TEMPORARY_PATCH:** no
- **REWARD_CANDIDATE:** undecided; AXIOM to classify only after reproduction/repair evidence

## Failure

The Python room projection enforces an explicit actor-field allowlist and rejects unsupported authored actor keys before building the player-safe payload.

The Android `BridgeSnapshotMapper` does not currently enforce an equivalent key allowlist for `room.actors[*]`.

At observed HEAD, it does:

```kotlin
val actor = objectMap(item, "room.actors[$index]")
GameRoomActor(
    presentationId = text(actor["presentation_id"], ...),
    knownActorId = optionalText(actor["known_actor_id"]),
    ...
)
```

`objectMap()` validates key type but retains every string-keyed entry. The mapper then reads expected keys and silently ignores any extra entries.

Therefore an incoming actor map containing an unexpected field such as `memories`, `knowledge`, `goals`, `story_state`, `relationships`, or another forbidden private field is not rejected by the Android mapper itself.

This packet does **not** claim that current Python production emits those fields. Current Python `build_room_projection()` deliberately does not receive `GameState.npcs`, applies `_ALLOWED_ACTOR_KEYS`, and rejects unsupported authored actor fields. The issue is a strict-boundary regression shield / defense-in-depth gap at the Python -> Android player-safe mapper boundary.

## Expected behavior

D-030 authority requires strict Android mapping for the versioned player-safe room projection.

`docs/android/PLAYER_SAFE_ROOM_ACTOR_PROJECTION_CONTRACT.md` states:

- private NPC structures such as personality, knowledge, memories, goals, story state and hidden relationship state are forbidden from the room/actor payload;
- `BridgeSnapshotMapper` should reject malformed actor records;
- unknown additive fields may be ignored only where the bridge contract explicitly permits forward-compatible unknown fields.

`docs/android/ROOM_ACTOR_PROJECTION_IMPLEMENTATION_MIGRATION_MAP_2026-10-04.md` requires Android JVM coverage for:
- valid room mapper;
- bad version;
- duplicate IDs;
- location mismatch;
- invalid speaker;
- malformed actor field;
- current mapper/privacy regression.

The expected D-064 boundary is therefore that unsupported/private actor keys cannot silently cross the strict room projection mapper.

## Reproduction

Source-level deterministic reproduction:

1. inspect `src/textrpg/room_projection.py::build_room_projection`;
2. observe `_ALLOWED_ACTOR_KEYS` and the explicit unsupported-field rejection;
3. inspect `android/app/src/main/java/com/thegame/rpg/engine/GameEngine.kt` room actor mapping;
4. observe that `objectMap()` accepts all string keys and the actor mapper reads only known fields without checking for unexpected keys;
5. inspect `android/app/src/test/java/com/thegame/rpg/engine/RoomProjectionMapperTest.kt`;
6. observe tests for version, location, duplicate presentation IDs and active speaker, but no regression asserting rejection of forbidden/private extra actor keys.

Minimal executable regression candidate for the D-064 owner:

- start from a valid `room.actors[0]` map;
- add `"memories" -> listOf("PRIVATE")` (or another explicitly forbidden field);
- call the strict player-safe mapper path used by production;
- expected: `IllegalArgumentException`;
- current source indicates the extra key will be ignored unless another layer rejects it first.

Veyr did **not** add or run this test because Kestrel owns the active D-064 runtime/test surface and the Coordination Room explicitly forbids overlapping edits without a bounded request.

## Executed evidence

No failing runtime/unit test is claimed.

Executed/observed repository evidence:
- exact source read of `src/textrpg/room_projection.py` at observed authority;
- exact source read of `android/app/src/main/java/com/thegame/rpg/engine/GameEngine.kt`;
- exact source read of `android/app/src/main/java/com/thegame/rpg/engine/RoomProjectionContract.kt`;
- exact source read of `android/app/src/test/java/com/thegame/rpg/engine/RoomProjectionMapperTest.kt`;
- exact contract read of `docs/android/PLAYER_SAFE_ROOM_ACTOR_PROJECTION_CONTRACT.md`, especially mapper validation and explicitly forbidden fields;
- exact migration-map read of `docs/android/ROOM_ACTOR_PROJECTION_IMPLEMENTATION_MIGRATION_MAP_2026-10-04.md`, including required mapper/privacy regression coverage.

Historical D-064 compatibility evidence remains separate:
- PR #63 / run #354 / `37257967729` is green compatibility evidence, but its tests do not exercise this extra-key rejection case.

## Affected authority

- files:
  - `src/textrpg/room_projection.py`
  - `android/app/src/main/java/com/thegame/rpg/engine/GameEngine.kt`
  - `android/app/src/main/java/com/thegame/rpg/engine/RoomProjectionContract.kt`
  - `android/app/src/test/java/com/thegame/rpg/engine/RoomProjectionMapperTest.kt`
  - `docs/android/PLAYER_SAFE_ROOM_ACTOR_PROJECTION_CONTRACT.md`
  - `docs/android/ROOM_ACTOR_PROJECTION_IMPLEMENTATION_MIGRATION_MAP_2026-10-04.md`
- APIs/contracts:
  - Python `build_room_projection()`
  - Android `BridgeSnapshotMapper.fromMap()`
  - `RoomProjectionContract.validate()`
- state/save/projection owners:
  - player-safe room projection only; no save-schema change proposed
- domains/tasks:
  - D-064 player-safe room/actor projection
  - Python -> Android privacy/strict-mapper boundary

## Blocking impact

Recommended interpretation pending AXIOM/Kestrel reproduction:

- do **not** unlock a new task;
- D-064 already owns strict Kotlin mapping and privacy acceptance;
- if AXIOM confirms the contract requires actor-key strictness, D-064 should add the smallest allowlist/rejection check plus one focused JVM regression before final handoff;
- D-069 should remain blocked exactly as it already is until D-064 completes.

This does not invalidate current Python redaction or claim that private state is presently exposed to Compose.

## Temporary patch

- **PRESENT:** no
- **DESCRIPTION:** none
- **ROOT_CAUSE_FOLLOWUP:** CPR-002 pending AXIOM review

## Causal hypothesis

**Hypothesis:** D-064 implemented cross-field validation in `RoomProjectionContract` and typed extraction in `BridgeSnapshotMapper`, but the actor-record unknown-key policy from D-030 was not encoded in the Kotlin mapper. This leaves Python as the only layer that rejects forbidden actor keys.

A correct repair, if confirmed, should remain at the strict Android mapping boundary and should not duplicate NPC privacy logic or inspect `GameState.npcs` in Android.

## Why the current task cannot safely absorb the problem

Veyr does not own D-064.

Kestrel has the active D-064 claim and the live Coordination Room explicitly reserves the room-projection runtime/test file family to Kestrel. Veyr can audit privacy but should not edit `GameEngine.kt` or `RoomProjectionMapperTest.kt` without an explicit bounded request.

Because the finding crosses Python -> Android and concerns player-safe privacy, it is reported through AXIOM instead of being silently patched by a non-owner.

## Unverified

- no executable regression has yet demonstrated the current mapper accepting `memories` or another forbidden extra actor key;
- no evidence shows current Python production emits forbidden private actor fields;
- no user-visible privacy leak is claimed;
- Problem Pressure Score, classification and whether strict rejection is mandatory versus merely recommended remain AXIOM decisions;
- no critical-root-cause reward is claimed.

## AXIOM review

- **PROBLEM_PRESSURE_SCORE:** pending
- **RATING:** pending
- **VERDICT:** pending
- **TASK LINK/CREATION:** recommend D-064 if accepted; do not create duplicate work
- **REQUIRED REVIEWERS:** AXIOM + Kestrel; Veyr available for privacy review
- **ROOT-CAUSE ACCEPTANCE:** pending executable regression / reviewer confirmation
