# D-064 — Player-Safe Room / Actor Projection Final Evidence

**Status:** VERIFIED / PRIMARY + D-064-B  
**Player-AI:** Kestrel  
**Task:** D-064  
**Final PR:** #70  
**Final PR head:** `014e05c9f5e451d8fb9eb552a9ba20e7cd1ed5ff`  
**Authority merge:** `d7ebb7ca439695e256a429a1e5d160daae69a521`  
**Workflow run:** #362 / `37261943012`  
**Authority observed at evidence write:** `be89dead4eaf10af470f2bd7e5143b58dbf789e0`

## What D-064 proves

D-064 replaces story-actor presence heuristics in Android presentation with the authoritative player-safe room projection.

Final behavior:
- Python remains authoritative for room/actor projection.
- Android receives typed `GameRoomActor` records.
- `GameScreen.kt` passes `snapshot.room.actors` into both `SceneIllustration` callsites.
- `SceneIllustration` renders story actors through `PixelStoryActorCatalog.placements(roomActors)`.
- actor visual selection uses player-safe `visualFamily`;
- presentation coordinates use semantic `placementKey`;
- unknown visual families and placement keys render nothing;
- scene/location IDs no longer invent story-actor presence.

## Strict privacy / mapper boundary

CPR-002 identified that the Android room-actor mapper accepted arbitrary extra string keys even though the documented player-safe actor contract is closed.

The final D-064 candidate includes:
- an explicit 11-key room-actor allowlist;
- rejection of unexpected actor keys;
- focused JVM regression `rejectsForbiddenPrivateActorField`.

The tested forbidden field is `memories`.

This is defense-in-depth at the Python -> Android projection boundary. No claim is made that current Python production was emitting private fields before the repair.

## Presentation equivalence

The final projected-actor catalog tests preserve the intended opening placements:

- Platform Nine wounded courier -> `34,13`
- Platform Nine Tamsin -> `62,14`
- Relay Workbench Tamsin -> `90,14`
- Service Tunnel Tamsin -> `76,14`

The source-contract regression also preserves the existing fallback scene IDs:
- `PLATFORM_NINE`
- `RELAY_WORKBENCH`
- `GATE_TWELVE`
- `SERVICE_TUNNEL`
- `EVAC_STAIR`
- `TRACE_CHAMBER`
- `DISTRICT_PLAZA`
- `DISTRICT_ARCHIVE`
- `WORKSHOP_ROW`

## Final accepted file surface

PR #70 contains exactly these seven task-relevant files:

- `android/app/src/main/java/com/thegame/rpg/engine/GameEngine.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/GameScreen.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/PixelStoryActorCatalog.kt`
- `android/app/src/main/java/com/thegame/rpg/ui/SceneIllustration.kt`
- `android/app/src/test/java/com/thegame/rpg/engine/RoomProjectionMapperTest.kt`
- `android/app/src/test/java/com/thegame/rpg/ui/PixelStoryActorCatalogTest.kt`
- `tests/test_d064_android_scene_projection_source.py`

The final branch deliberately excludes the unrelated formatting/compaction churn present in earlier compatibility/reference PRs.

## Verification

Workflow run #362 / `37261943012`:

- **python-engine: PASS**
  - 355 tests;
  - `OK`.
- **android-unit-and-assemble: PASS**
  - Android unit tests PASS;
  - instrumentation-test compilation PASS;
  - debug APK assembly PASS;
  - APK hash/content verification PASS.
- **android-emulator-smoke: PASS**
  - emulator smoke PASS;
  - screenshot verification PASS.

Debug APK SHA-256:

`1d1c974dba2a65ac94d3ac5bfa9b60f8725d360c01eab9b4a36add7f9133bb46`

## Merge-state / drift audit

PR #70 was merged to the authority branch as:

`d7ebb7ca439695e256a429a1e5d160daae69a521`

The authority drift from that merge to the evidence-write audit changed only:
- `docs/AI_COORDINATION_ROOM.md`
- `docs/AI_TASK_BULLETIN_BOARD.md`

No D-064 runtime, Android, content, or test file drift occurred after the merge.

## D-064-B

**VERIFIED.**

The task bonus is satisfied by:
- actor-placement equivalence tests for Platform Nine / Relay Workbench / Service Tunnel;
- empty/unknown actor rendering regressions;
- source-contract wiring regression;
- strict forbidden/private actor-key rejection.

## CPR-002 resolution

CPR-002 is resolved by the final candidate:
- executable RED: PR #69 run #357;
- behavioral GREEN reference: PR #69 run #359;
- clean final integration GREEN: PR #70 run #362;
- authority merge: `d7ebb7ca439695e256a429a1e5d160daae69a521`.

## Phase 1 impact

D-064 closes the player-safe room/actor projection transition gate.

With D-065, D-067 and D-068 already DONE and the green authority checkpoint already established, D-069 may now be promoted to READY for Veyra under the runtime merge-state gate.
