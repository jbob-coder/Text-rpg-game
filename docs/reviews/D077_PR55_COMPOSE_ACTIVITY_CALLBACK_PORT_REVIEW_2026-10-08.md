# D-077 / D-021 — Trace Chamber Compose Activity Callback Port Review

**State:** NON-OWNING / SOURCE-ONLY / NOT IMPLEMENTED OR ACCEPTED.  
**Prepared:** 2026-10-08 AST.  
**Authority:** live Bulletin and Master Task Register. Do not use this document as a task claim or as permission to change PR #55.

## Exact source evidence

- PR #55 is OPEN, unmerged; source HEAD `2bb38f556d2870202e3a66109fec237b3bb98b28`. Changed paths: `android/app/src/androidTest/java/com/thegame/rpg/ui/Phase1ActivityChoiceTest.kt`, `android/app/src/test/java/com/thegame/rpg/engine/Phase1ActivityChoiceContractTest.kt`, `tests/test_phase1_activity_proof.py`.
- Old instrumentation test: `Phase1ActivityChoiceTest.kt` blob `45c2ea4aa65c259614e551010e1b290e12cb8dbe`. It sets up the enabled `TRAIN_POWER_FUNDAMENTALS_TWO_HOURS` choice in `TRACE_STABILIZATION_HUB`, taps the UI and captures `onChoice` to assert that exact stable ID.
- Current UI: `PixelComponents.kt` blob `c07a0cc784b9b49171bc44ce16485d0f3348c17a`; `GameScreen.kt` blob `1705536c77f4607cd3bd546014e38f099f076b8b`. The latter invokes `PixelChoiceCard(choice, busy) { onChoice(choice.id) }`.
- Current model: `GameEngine.kt` blob `36c4c20825d000c41741052b6069026c8a79a415` still defines `GameChoice(id, text, enabled, disabledReason)` and compatible `GameSnapshot` required constructor fields, with defaults for added fields.
- Existing UI test: `GameScreenTest.kt` blob `0759909527fff5456f4e42c9a851b9367da345ab` checks generic choice affordances using `onChoice = {}`; no training-specific captured callback was found. P15 preserves PR #55 on HOLD for a future D-077/D-021 consumer test port.

## Concrete compatibility problem

The **old** test locates an element by the exact unprefixed visible text `Train two hours of controlled power fundamentals and measurement.`. The **current** `PixelChoiceCard` constructs an enabled label by prefixing `> ` to `choice.text`, and a disabled label by prefixing `× `. Consequently, the old exact-text selector is no longer aligned with the current implementation. This is a **source-level incompatibility risk**, not an executed failing test.

The durable action selector already exists: `testTag("choice-${choice.id}")`, while the enabled gate is `choice.enabled && !busy`, and the card's clickable action forwards `choice.id`. Port the instrumentation test to **select the stable `choice-TRAIN_POWER_FUNDAMENTALS_TWO_HOURS` tag**, scroll/display/click it when enabled, and assert the captured callback equals `TRAIN_POWER_FUNDAMENTALS_TWO_HOURS` exactly. Do not tie action identity to visible punctuation.

## Suggested future acceptance

1. **Enabled:** the activity-tagged choice exists, is interactive, and one tap emits the exact stable ID.
2. **Disabled by authoring:** a `GameChoice` with `enabled=false` cannot dispatch; verify appropriate Compose disabled semantics and unchanged callback.
3. **Busy UI:** `busy=true` suppresses otherwise enabled choice dispatch.
4. **Regression:** existing generic `GameScreenTest.kt` remains green, and accepted D-068 Python/Kotlin bridge/authoritative training tests remain intact.
5. **Executable evidence:** compile and run the new test under the current Compose Android instrumentation workflow; record exact candidate SHA, PR/merge-state, emulator job and resulting acceptance evidence. Source compatibility does not establish such a result.

## Boundaries and handoff

The future authorized D-077/D-021 owner should reuse the old 70-line test as provenance, adapt the stale text lookup to the current stable-tag UI contract, compile/execute the new test, and only then disposition PR #55 with provenance retained. No stale three-test diff should be merged wholesale merely to recover one callback assertion. The test's responsibility is **UI tap to ID**, not training resource/time calculation.

At this source-inspection checkpoint, P11/CPR-006 remains Nodus-owned, D-072 is Silex-owned, and D-077 remains dependency-gated. No code, runtime, schema, claims, locks, PRs or scores are changed by this review. No tests, emulator, CI, APK or device runs were performed here.
