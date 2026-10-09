# Quorix — Android error-screen re-entry review

**Status:** non-owning source inspection and future test design. Not a reproduced runtime fault, task claim, accepted CPR, UI patch, or approved new recovery policy.  
**Player-AI:** `PLAYER_QUORIX`, existing session `SESSION_QUORIX_20261008T1732-0400_S01`; no primary task.  
**Authority:** `jbob-coder/Text-rpg-game`, `docs/master-game-development-program`.  
**Related review:** `docs/reviews/NODUS_BRIDGE_POST_COMMIT_PROJECTION_FAILURE_REVIEW_2026-10-08.md` (Nodus). This packet checks the specific **absence of a UI re-entry action after an error**, rather than reproducing Nodus's Python commit-versus-projection failure hypothesis.

## Verified source-control chain

1. `GameViewModel.choose` calls `engine.choose(choiceId)`; on `Result.failure`, it invokes `publishFailure`. This applies to engine or projection failures. `GameViewModel.save`, `load`, travel and other commands also have error paths that call the same failure publisher.
2. `GameViewModel.publishFailure` sets `bootState = engineFailure.toBootStateError()` and `busy = false`. It retains the previous `snapshot`; it neither invokes `engine.load` nor retrieves a read-only current view on the failure path.
3. `TheGameRoot` displays `PixelGameShell` only when `bootState == BootState.Ready` and `snapshot != null`. Otherwise, it displays `PixelBootScreen(uiState.bootState)`. That screen shows the state code and public message. **No retry/Continue/view-refresh action is passed to or drawn by `PixelBootScreen`.**
4. The passed `onLoad` callback is routed through `PixelGameShell`, which is no longer composed when the state is `BootState.Error`. The existence of LOAD / CONTINUE inside Settings does **not** establish recovery from the error screen.
5. `MainActivity` invokes `gameViewModel.startIfNeeded()` from a `LaunchedEffect(Unit)`, but `GameViewModel.startIfNeeded` returns when `startRequested` is already true. The current error-screen UI therefore offers no explicit way to re-enter a retained session via another tap on the same screen.
6. `GameScreenTest.kt` exercises several `TheGameRoot` cases in `BootState.Ready`, while `BootStateTest.kt` checks error data fields only; these inspected tests do not exercise Error-state retry/Continue controls. This is a **static coverage finding**, not a claim the full test suite fails.

The combined behavior establishes a **conditional UI dead-end**: *if* a command failure changes a live Ready session into `BootState.Error`, the Compose tree hides the gameplay controls while preserving a possibly stale snapshot in ViewModel state, and provides no on-screen action to query or restore the current session. It does **not** prove normal authored content triggers such a failure, that any user data is already lost, or that simply retrying the original gameplay choice is safe.

## Ownership and correctness decision required

A post-command projection error can occur **after** Python has committed the choice (Nodus's separate source-bound hypothesis) or **before** authoritative mutation. The UI cannot infer which happened solely from a generic Result failure. A safe recovery contract must distinguish:

- **Read-only re-projection / reconcile:** query the authoritative Python session without replaying the gameplay command, then publish a fresh player-safe snapshot only if mapping succeeds. Requires a carefully owned, validated bridge/engine entry point and error classification; this review does not add one.
- **Saved-game Continue:** explicit player choice to load an existing checkpoint, with clear possible loss of later unsaved actions; do not silently overwrite a newer in-memory committed state.
- **Restart/repair path:** an explicit boot retry when content/Python initialization truly failed; must not be confused with resubmission of a command that may already have committed.
- **Atomic command contract:** alternatively guarantee rollback on every public response failure across Python and Kotlin mapping. Python alone cannot guarantee Kotlin DTO projection success; ownership and tests are necessary before selecting this policy.

**Recommendation:** AXIOM and future D-076/D-077/Android integration owners choose one recoverability/idempotency contract and add a visible recovery affordance consistent with it. Do not ask Nodus to expand his active P11/CPR-006 **load atomicity** implementation or change Silex D-072 without explicit oversight classification.

## Proposed future verification cases — NOT RUN

| Case | Test setup | Required observation after the selected policy is approved |
| --- | --- | --- |
| ER-01 | Start from Ready snapshot and make one `GameEngine.choose` return an error | Error view remains usable and offers a clearly defined, actionable recovery, rather than text-only dead end |
| ER-02 | Simulate a successful Python action commit followed by Kotlin `mapSnapshot` failure | No automatic replay of that choice; recovery reads actual authoritative turn/scene/history |
| ER-03 | Force a pre-commit action rejection | No phantom turn/history increment; same recovery mechanism handles valid previous playable state |
| ER-04 | Enter Error with no saved checkpoint | Continue is disabled or gives a safe non-destructive result; there is a separate safe boot/re-projection path |
| ER-05 | Enter Error with an older save and a newer in-memory state | A recovery choice does not silently discard unpersisted committed progress |
| ER-06 | Compose semantics under `BootState.Error` | Error panel exposes expected accessible control and state; no technical traceback or private gameplay state leaks |
| ER-07 | Startup failure before a Python session exists | Boot retry is safe, bounded and distinguished from in-session state reconciliation |
| ER-08 | Recover from projection error, then save/reload | Only one committed action is recorded; turn/time/history and legal choices agree with the authoritative state |

**Testability consideration:** `GameViewModel` currently instantiates `PythonGameEngine()` internally, so injecting a fake `GameEngine` for isolated VM tests requires an approved test seam or a higher-level Compose/fake-gateway harness. This is a test-design constraint, not permission to change dependency injection under P11.

## Pinned source blobs (authority inspection)

- `android/app/src/main/java/com/thegame/rpg/GameViewModel.kt`: `d3d9392efa451570f573f339220e6dffb96d5609`
- `android/app/src/main/java/com/thegame/rpg/ui/GameScreen.kt`: `1705536c77f4607cd3bd546014e38f099f076b8b`
- `android/app/src/main/java/com/thegame/rpg/MainActivity.kt`: `2cc00c3ded79dedd1afaf19942e3ce10062ad12b`
- `android/app/src/main/java/com/thegame/rpg/engine/PythonGameEngine.kt`: `73d028d0720897a547509e83d5d6021ef5bcad8c`
- `android/app/src/main/java/com/thegame/rpg/boot/BootState.kt`: review-backed by fetched source; no runtime execution claimed
- `android/app/src/androidTest/java/com/thegame/rpg/ui/GameScreenTest.kt`: `0759909527fff5456f4e42c9a851b9367da345ab`
- `android/app/src/test/java/com/thegame/rpg/boot/BootStateTest.kt`: `8ff02b91ece1d5921d29ca903b30a59446f2bc32`

**Verification scope:** read-only source and test assertions. No Python/Kotlin/Gradle/CI/emulator/handset/APK tests run by Quorix; no code, gameplay, save schema, canon, task status, PR #80, D-072, or score modifications. Re-fetch all source at a future exact merge HEAD before acceptance.
