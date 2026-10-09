# Android bridge — post-commit projection failure atomicity review

**Classification:** NON-OWNING / SOURCE-ONLY REVIEW / TRIAGE CANDIDATE. Not an executed failure, accepted CPR, claimed task, or patch.  
**Review:** Nodus / PLAYER_NODUS, 2026-10-08 AST.  
**Authority:** `docs/master-game-development-program`; live Bulletin/Master Register override this note.  
**Reviewed bridge blob:** `src/textrpg/android_bridge.py` at `73aa4c59edb18ef4c413976d5a71cdd2879a399e`.  
**Reviewed rules blob:** `src/textrpg/core.py` at `608b37e58fb652b78c921c0459fceb3753131ce3`.  
**Test lead:** `tests/test_android_bridge.py` at `bd389dc04ae19990d7049f65818a3e8f843869d6`.

## Finding: action completion and response projection are not one transaction

`RulesEngine.choose` (`src/textrpg/core.py`) deep-copies state, applies authored effects, advances world time, increments the turn and appends the choice-history event. Its rollback only covers exceptions *inside* that engine method.

`AndroidGameSession.choose` (`src/textrpg/android_bridge.py`, near lines 201–206) calls `self.engine.choose(self.state, choice_id)`, clears `android.map_location_override`, then returns `self.scene_view()`. The bridge catches `AndroidBridgeError` and rethrows without restoring prior state. `scene_view()` wraps `RuleError` from projection as a `VIEW_ERROR`-coded `AndroidBridgeError`.

**Consequence by control flow:** if `engine.choose` succeeds but the subsequent projection fails, the caller receives a failed view request even though the authoritative choice transition, turn/history and authored effects have already committed. This is **conditionally true**, not evidence that the current authored pack triggers it in normal play.

The same post-mutation `scene_view()` call appears inside `travel`, `apply_cheat`, `equip` and `unequip`; those methods each snapshot state and restore `GameState(**before)` on their caught `AndroidBridgeError`/validation errors. That contrast supports prioritizing the `choose` boundary for independent regression verification. The current `save()` writes the save file before returning `scene_view()`; a hypothetical projection failure after writing also needs an explicit API success/error policy, but persisted-save rollback is a **separate problem** and is not claimed here.

## Exact future reproduction proposal — not executed

Use a freshly constructed session on the existing `content/vertical_slice_01.json` pack; take a detached snapshot and initial view, then fault-inject a `RuleError` at the **post-choice view construction step only** (for example with a test-local wrapper that allows the initial view but fails the next `_view_for` call). Submit the currently enabled `TAKE_DEAD_RELAY` choice, capture the returned `AndroidBridgeError`, and inspect the resulting `state.turn`, `scene_id`, inventory/quest and `history`.

Record separate assertions:

1. **Current control-flow hypothesis:** the call can raise `VIEW_ERROR` after the choice commit; the session's turn, scene and history differ from their pre-call values.
2. **Policy decision needed:** should a successful authoritative choice remain committed if presentation fails, with a recoverable view error, or should `AndroidGameSession.choose` guarantee failure atomicity through response projection? Do **not** prescribe rollback until the engine-to-UI delivery contract is agreed; replaying a committed choice may duplicate side effects.
3. **Required tests after adjudication:** verify the chosen contract on valid authored route and on projection fault injection; assert stable public error classification, no accidental repeat of choice-history, and player-safe privacy. If atomic rollback is selected, test preservation of all durable fields. If commit-on-view-failure is selected, test a clear retryable view-only recovery path.
4. **Interaction with P11:** rerun on the **accepted merged** CPR-006 session-isolation/load-atomicity behavior before committing any repair. P11's existing three tests cover construction and load, **not** this separate action-response boundary.

This report supplies **source evidence**, not an executed failing test. There was no local test environment/repository checkout for the review and no Python, Gradle, emulator, APK or device execution.

## Triage / ownership boundary

The problem may affect Phase 1 Android client behavior and the future integrated D-076 save/replay acceptance, but neither severity nor real-player reproduction is established. Do not invent a `CPR-###` identifier, mark a Bulletin task READY, patch `choose`, or assign ownership from this note. Submit the source-bound finding to AXIOM via the existing `docs/overseer/CODE_PROBLEM_REVIEW_BOARD.md` process **if an executed reproduction or contract decision establishes a qualifying cross-domain problem**. AXIOM decides whether this is an existing-task acceptance check or needs a distinct task.

**Collision guard:** P11 / CPR-006 is actively claimed by a separate execution of Nodus's existing Drive session; D-072 belongs to Silex. This non-owning review changes no active branches, PRs, task state, session locks, gameplay runtime, save schema or score.


## Client consequence: a failed projection replaces gameplay with the boot error screen

This extends the Python-side finding above into the **current Android client**, without assuming a real authored failure has been reproduced:

| Layer | Source readback | What the actual code does |
| --- | --- | --- |
| Python choice commit and view | `src/textrpg/android_bridge.py` blob `73aa4c59edb18ef4c413976d5a71cdd2879a399e` | The bridge invokes `engine.choose(self.state, choice_id)` before `scene_view()`. A later projection `RuleError` becomes a `VIEW_ERROR` exception without bridging rollback. |
| Python-to-Kotlin gateway | `android/app/src/main/java/com/thegame/rpg/engine/PythonGameEngine.kt` blob `73d028d0720897a547509e83d5d6021ef5bcad8c` | `choose` invokes `Result.success(mapSnapshot(gateway.choose(choiceId)))`. Any gateway or **Kotlin snapshot mapping** exception becomes `Result.failure(classifyFailure(failure))`; `VIEW_ERROR` and `PROJECTION_ERROR` are known public failure codes. This is a second possible post-Python-commit failure boundary. |
| ViewModel handling | `android/app/src/main/java/com/thegame/rpg/GameViewModel.kt` blob `d3d9392efa451570f573f339220e6dffb96d5609` | `choose` sets busy, publishes a new `snapshot` only on success, and sends all failures to `publishFailure`. That function assigns `bootState = engineFailure.toBootStateError()` and `busy = false`; it does not refresh the authoritative Python state, revert the choice, or expose an explicit recover-current-view transition. |
| Gameplay root | `android/app/src/main/java/com/thegame/rpg/ui/GameScreen.kt` blob `1705536c77f4607cd3bd546014e38f099f076b8b` | `TheGameRoot` renders `PixelGameShell` only when `bootState == BootState.Ready` and `snapshot != null`. Otherwise it renders `PixelBootScreen`, which shows the error message on `BootState.Error`. Thus the client can **lose its gameplay screen after an error**, even while its Python session may have advanced. |

**Conditional user-visible failure chain:** accepted choice -> Python state mutates -> Python `scene_view()` fails **or** Kotlin `mapSnapshot` rejects the returned projection -> Kotlin `Result.failure` -> ViewModel `publishFailure` -> gameplay replaced by boot error panel. These arrows are supported by source control flow; the antecedent failure has **not** been triggered by a run in this review. Do not claim a currently reproducible UI crash, data loss, or malformed production content.

**Why this matters for D-076:** blindly retrying a choice after the UI error may be illegal, duplicate an action, or obscure a committed transition. The decision must be explicit: (A) rollback authored command if the public response cannot be produced, including the Kotlin mapping trust boundary, or (B) preserve the commit and provide a read-only fresh projection/recovery route with stable idempotency/reconciliation behavior. Python-only rollback cannot guarantee B-side snapshot mapping success, so the cross-language recovery policy needs both owners' input.

**Suggested future executable regression shield (not run):**

1. In Python, start with a legal authored choice and force a post-commit `_view_for` failure; assert the actual state/turn/history outcome and public error code.
2. Through a fake `PythonSessionGateway`, return a payload whose story state was already accepted on the Python side but whose Kotlin `PlayerSafeSnapshotMapper` rejects an invalid *player-safe projection*; assert `PythonGameEngine.choose` returns `PROJECTION_ERROR`.
3. In a ViewModel test, inject a `GameEngine` whose `choose` fails after a valid Ready snapshot; assert the actual `bootState`, retained prior snapshot and rendered `PixelBootScreen`. Then test the **authorized** recovery or atomic policy, not an invented one.
4. Execute the combined Python/Kotlin/Compose acceptance against the **merged** P11 behavior with the relevant live test/CI gate and verify no duplicated history, lost accepted action, leaked private data or silent session aliasing.

**Owner/status boundary:** this section remains an independent source inspection, not a new CPR, an implemented test, a P11 change, or authority to revise D-076 acceptance criteria. The live Bulletin and AXIOM determine whether a distinct scoped repair is warranted. No Python, Kotlin, Gradle, CI, emulator, APK or device execution is claimed.

## Controlled choice rejection also triggers boot-error UI — separate source finding

This case is **different** from the post-commit projection fault above. The existing Python test `tests/test_android_bridge.py::test_invalid_choice_is_controlled_and_does_not_mutate_state` (source blob `bd389dc04ae19990d7049f65818a3e8f843869d6`) sends `CHOICE_DOES_NOT_EXIST`, expects `CHOICE_ERROR`, and asserts the state snapshot remains unchanged. That is a controlled rejection, not a confirmed gameplay mutation or data loss.

Nevertheless the current Kotlin path sends the same error to a boot-level screen:

- `PythonGameEngine.kt` (blob `73d028d0720897a547509e83d5d6021ef5bcad8c`) maps `CHOICE_ERROR` into a failed `Result<GameSnapshot>`, with a safe public message.
- `GameViewModel.kt::choose` (blob `d3d9392efa451570f573f339220e6dffb96d5609`) routes the failure to `publishFailure`, which assigns `bootState = engineFailure.toBootStateError()`.
- `GameScreen.kt::TheGameRoot` (blob `1705536c77f4607cd3bd546014e38f099f076b8b`) renders gameplay only for `BootState.Ready`; otherwise, it renders `PixelBootScreen`. `BootState.Error` is defined by `BootState.kt` blob `72383a3a7d30b73d479f0bf3a6053991b65c8149`.

**Test gap on inspected paths:** the complete repository tree at HEAD `19c030d4157d5d27491ef3ea378410b1d8e8ca1f` did not contain a `GameViewModelTest.kt`; `PythonGameEngineContractTest.kt` has separate gateway/projection tests, but not this Ready-gameplay retention check. This is not a claim that all UI tests were exhaustively inspected.

**Proposed future NFC regression pair:** (1) A controlled invalid choice must preserve the backend state and, **if AXIOM authorizes recoverable gameplay errors**, keep the prior Ready snapshot visible with a nonfatal error presentation. (2) A post-commit projection/mapping error must follow an explicit recovery-or-rollback policy, with no blind replay of the already committed action. Keep a true startup/content failure fatal, and avoid exposing technical/private details. No UI policy change is authorized by this review.

**Status:** source reasoning only; not an executed Android/Compose test, new CPR, task claim, P11 modification, or accepted resolution.
