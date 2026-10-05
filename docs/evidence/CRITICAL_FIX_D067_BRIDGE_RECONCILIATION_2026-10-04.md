# Critical Fix Evidence — D-067 Bridge / Transition Baseline Reconciliation

**Status:** VERIFIED CRITICAL ROOT-CAUSE INCIDENT  
**Player-AI:** Nodus  
**Related task:** D-067  
**Critical reward class:** SYSTEM BLOCKER  
**Observed authority HEAD at award review:** `b63b03bad96608b5e7189301e158ac967ad6b3aa`

## Incident

The transition baseline was blocked by a cluster of integration regressions spanning the Python authoritative engine bridge, D-064 room projection acceptance, D-067 inventory/equipment proof and Android-facing compatibility.

Run #341 / `37252547112` showed:
- 341 Python tests discovered;
- 1 failure;
- 12 errors;
- Android JVM/build/package gate otherwise green.

The concrete failures included:
- obsolete third argument passed to `advance_time`;
- obsolete registry-form call to `equip_item`;
- developer cheat whitelist compatibility regression;
- D-064 acceptance importing `pytest` despite the repository's unittest discovery gate;
- old root-shape expectation missing the now-authoritative `room` projection;
- map-only travel producing a scene/location mismatch at the room-projection boundary.

These failures blocked the common green-authority checkpoint and therefore blocked D-069.

## Root cause

The incident was not one isolated assertion failure. It was merge-state/API contract drift across previously independent work:

- bridge callers had regressed away from the current authoritative function signatures;
- compatibility behavior had been partially reconstructed instead of preserved from the established bridge contract;
- the new room projection tightened invariants without map-only travel adapting its projection behavior;
- acceptance tests straddled two different runner/API eras.

The causal repair required reconciling the shared contracts rather than adding catch-all exception handlers or suppressing tests.

## Nodus repair

PR #62 — **D-067: reconcile bridge and establish green Phase 1 checkpoint**

Head: `ab83f80b8047724a17fa141bc15be51585d01da6`.

Relevant repair commits:
- `a4077d39bf1f5520d6e75c53ac91053ba8107a30` — reconcile Android bridge runtime contracts;
- `d4cdbdb7a893c6a18b01d5834e18f8c5fefbd4f2` — align bridge expectations with room projection;
- `7d3fef3eff29042c0beaf930072944d9a2505cd2` — make D-064 acceptance unittest-native;
- `a797fa33c3353b13fb6a9d3b02151c0c6901291a` — complete D-067 exact-head proof;
- `ab83f80b8047724a17fa141bc15be51585d01da6` — shield Android snapshot success path.

The repair:
- restored authoritative travel/equip/cheat bridge contracts;
- preserved current `create_session` compatibility;
- retained D-064 room projection;
- made map-only travel room projection safe instead of leaking stale scene actors;
- aligned D-064 test execution with unittest;
- strengthened D-067 and Android snapshot regression coverage.

## Verification

Workflow: Android Pixel Client  
Run: #345 / `37252981251`

Results:
- **python-engine: PASS**
  - 347 tests;
  - `OK`.
- **android-unit-and-assemble: PASS**
  - Android unit tests PASS;
  - Compose instrumentation-test compile PASS;
  - debug APK assembly PASS;
  - APK contents/hash verification PASS.
- **android-emulator-smoke: PASS**
  - real boot/smoke tests PASS;
  - screenshot verification PASS.

The relevant D-067 proof tests and bridge expectations have been ported into the authority branch. The authority bridge retains the same repaired travel/equip/cheat semantics and map-only room safety, although later concurrent work means D-067 still requires its final exact-authority handoff/checkpoint before the primary task itself is marked DONE.

## Critical reward

Under OR-021:

- SYSTEM BLOCKER: **+175**
- ROOT CAUSE: **+75**
- REGRESSION SHIELD: **+30**
- CROSS-SYSTEM SAVE: **+30**

**TOTAL CRITICAL-FIX BONUS: +310**

Not awarded:
- PATCH-DEBT REMOVAL: not separately evidenced;
- PREVENTION: regression shield already captures the demonstrated prevention work;
- HARD-TO-REPRO PROOF: the failure was merge-state sensitive, but deterministic CI reproduction already existed.

## Important boundary

This +310 rewards the verified critical incident repair.

It does **not** by itself mark D-067 DONE. The normal D-067 +90 remains contingent on the task's own final exact-authority acceptance and handoff.
