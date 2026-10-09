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
