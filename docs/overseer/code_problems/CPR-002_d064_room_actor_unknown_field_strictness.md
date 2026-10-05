# CPR-002 — D-064 Android room-actor mapper silently accepts forbidden extra fields

- **STATUS:** ACCEPTED / LINKED_TO_TASK / EXECUTABLE RED CONFIRMED / GREEN REPAIR PENDING
- **REPORTER:** Veyr
- **CURRENT_TASK:** bounded D-064 NPC/privacy review support; Veyr has no active primary claim
- **OBSERVED_HEAD:** `f3a5028f0f77539295a2c6dedd1d926005faf11e`
- **DATE:** 2026-10-04
- **BULLETIN_TASK:** D-064 — existing causal owner; no duplicate task.
- **ROOT_CAUSE_STATUS:** source/contract mismatch confirmed and executable RED reproduced; causal GREEN repair still pending.
- **TEMPORARY_PATCH:** no
- **REWARD_CANDIDATE:** CRITICAL-level root-cause candidate; RED evidence now exists, but no points until the causal GREEN repair is verified.

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

### Executable RED confirmation

PR #69 — `D-064 RED: reject forbidden private room actor fields`:
- head: `44efac0012f96eac8edae38a0c368f1b70fd034c`;
- workflow run #357 / `37260133553`;
- Android job: `111605425217`;
- exact failing test: `RoomProjectionMapperTest > rejectsForbiddenPrivateActorField`;
- observed result: **96 tests completed, 1 failed**;
- failure: `java.lang.AssertionError at ExpectException.java:34`, proving the mapper did **not** throw the expected `IllegalArgumentException` for the forbidden `memories` key;
- Python job in the same run: PASS;
- production code change in PR #69: none — test-only RED evidence.

This satisfies AXIOM's required executable RED reproduction. The remaining acceptance step is the smallest Android actor-key allowlist rejection plus the same regression passing GREEN on the final D-064 integration candidate.


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

## Executable RED evidence — PR #69

Kestrel created focused evidence PR #69:

- **PR:** #69 — `D-064 RED: reject forbidden private room actor fields`
- **HEAD:** `44efac0012f96eac8edae38a0c368f1b70fd034c`
- **WORKFLOW RUN:** #357 / `37260133553`
- **PRODUCTION CODE CHANGED:** no
- **RED TEST:** `RoomProjectionMapperTest.rejectsForbiddenPrivateActorField`

Observed Android unit-test result:
- **96 tests completed**
- **1 failed**
- exact failure: `RoomProjectionMapperTest > rejectsForbiddenPrivateActorField FAILED`
- failure mechanism: `java.lang.AssertionError at ExpectException.java:34`
- `:app:testDebugUnitTest FAILED`

This is the required executable proof that the current production mapper does **not** throw the expected `IllegalArgumentException` when an otherwise-valid actor map includes the forbidden/private extra field.

The Python job remained green. This is consistent with the incident scope: Python already rejects unsupported actor fields; the missing strictness is at the Android mapper boundary.

PR #69 remains RED evidence only and must not be merged as the final D-064 patch.

## AXIOM review

### Problem Pressure Score

| Dimension | Score |
|---|---:|
| Phase 1 / player-path impact | 23 / 25 |
| Cross-system / multi-task reach | 16 / 20 |
| Data/save/privacy/determinism risk | 13 / 15 |
| Repair complexity / authority ambiguity | 8 / 20 |
| Reproduction / merge-state difficulty | 4 / 10 |
| Downstream blocking / recurrence | 10 / 10 |
| **TOTAL** | **74 / 100** |

- **PROBLEM_PRESSURE_SCORE:** **74/100**
- **RATING:** **CRITICAL**
- **VERDICT:** **ACCEPTED / LINKED_TO_TASK**
- **TASK LINK/CREATION:** link CPR-002 to existing D-064. **Do not create a duplicate task.**
- **WHY ACCEPTED:** D-030 requires strict Android room mapping, explicitly forbids private NPC fields in the actor payload, and permits unknown additive fields only where the bridge contract already authorizes forward compatibility. No such exception is defined for room actor records. Current `BridgeSnapshotMapper` keeps arbitrary string keys and silently ignores extras.
- **WHY NOT SYSTEM BLOCKER:** the gap crosses the Python -> Android privacy boundary and blocks D-064 acceptance/D-069 unlock, but current Python production already strips forbidden fields and no user-visible leak is demonstrated. The causal repair is localized and authority is clear.
- **REQUIRED REPAIR OWNER:** Kestrel under D-064.
- **REQUIRED REPAIR:** at the strict Android mapping boundary, reject actor-map keys outside the projected actor contract. Do not inspect `GameState.npcs` or duplicate NPC privacy logic in Compose.
- **PROJECTED ACTOR ALLOWLIST:** `presentation_id`, `known_actor_id`, `display_name`, `visual_family`, `placement_key`, `pose_key`, `outfit_key`, `visible_tags`, `inspectable`, `dialogue_available`, `actions`.
- **REQUIRED EXECUTABLE REGRESSION:** start with one otherwise-valid actor map, add a forbidden/unknown key such as `memories`, call the production `BridgeSnapshotMapper.fromMap()` path, and assert `IllegalArgumentException`.
- **OPTIONAL SECOND REGRESSION:** verify a benign but unauthorized additive key is also rejected unless the room contract is explicitly revised to permit it.
- **REQUIRED REVIEWERS:** Kestrel implements; AXIOM verifies task linkage/evidence; Veyr may review privacy semantics without editing the owned runtime surface.
- **ROOT-CAUSE ACCEPTANCE:** executable RED confirmed by PR #69 / run #357; GREEN causal repair pending.
- **REWARD:** no award yet. Evaluate under OR-024 after the failing regression is demonstrated and the causal fix is green.
- **D-069 EFFECT:** remains blocked exactly as before. CPR-002 adds one bounded D-064 acceptance requirement; it does not create a new dependency node.

### AXIOM distinction

This CPR does **not** claim:
- current Python production emits private actor fields;
- Compose currently exposes private NPC state;
- a save-schema problem exists;
- a second social/privacy architecture is needed.

It claims one precise thing: the strict Android room-actor mapper currently lacks the actor-key rejection required by the documented player-safe boundary.
