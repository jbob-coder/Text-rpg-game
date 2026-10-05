# CPR-001 — D-067 bridge transition contract drift

- **STATUS:** RESOLVED
- **REPORTER:** Project Overseer backfill from committed evidence
- **CURRENT_TASK:** D-067
- **OBSERVED_HEAD:** failure state documented in D-067 transition evidence before PR #62 repair
- **DATE:** 2026-10-04
- **BULLETIN_TASK:** D-067
- **ROOT_CAUSE_STATUS:** proven
- **TEMPORARY_PATCH:** no surviving workaround required
- **REWARD_CANDIDATE:** already resolved/scored under OR-024 as Nodus +310 critical root-cause award

## Failure

The common transition baseline contained a cluster of integration failures spanning:
- Android bridge travel;
- equipment bridge calls;
- developer cheat compatibility;
- room projection/map-only travel;
- D-064 acceptance runner compatibility;
- D-067 inventory/equipment proof expectations.

The aggregate transition run had 1 failure and 12 errors and blocked the green authority checkpoint required before D-069.

## Expected behavior

The existing authoritative Python/Android contracts should remain mutually compatible across:
- current simulation function signatures;
- equipment API signatures;
- player-safe room projection;
- map-only travel;
- repository unittest discovery;
- D-067 inventory/equipment proof.

## Reproduction / executed evidence

Historical failing evidence:
- workflow run #341 / `37252547112`;
- aggregate Python transition state: 1 failure / 12 errors.

Root-cause repair:
- PR #62;
- head `ab83f80b8047724a17fa141bc15be51585d01da6`;
- repair commits listed in `docs/evidence/CRITICAL_FIX_D067_BRIDGE_RECONCILIATION_2026-10-04.md`.

Verified green evidence:
- workflow run #345 / `37252981251`;
- Python: 347 tests, OK;
- Android unit/build/package: PASS;
- emulator smoke/screenshots: PASS.

Final authority checkpoint:
- PR #65 / run #351 / `37253975755`;
- Python PASS;
- Android unit/build/package PASS;
- emulator smoke/screenshots PASS.

## Affected authority

- `src/textrpg/android_bridge.py`
- bridge travel/equip/cheat call contracts
- room-projection compatibility during map-only travel
- D-064 unittest-native acceptance
- D-067 inventory/equipment proof
- Android snapshot regression boundary

## Blocking impact

The incident blocked:
- D-067 completion;
- the common green authority checkpoint;
- downstream D-069 tactical unlock;
- integration confidence across D-064/D-067.

## Causal explanation

The failure was not one isolated test bug.

The causal incident was merge-state/API contract drift:
- callers regressed to obsolete API signatures;
- compatibility behavior was reconstructed inconsistently;
- room projection tightened an invariant without map-only travel adapting;
- acceptance tests crossed runner/API eras.

The correct repair was to reconcile the authoritative contracts and preserve the new projection boundary, not suppress failures or add duplicate presentation-side logic.

## AXIOM review

### Problem Pressure Score

| Dimension | Score |
|---|---:|
| Phase 1 / player-path impact | 24 / 25 |
| Cross-system / multi-task reach | 19 / 20 |
| Data/save/privacy/determinism risk | 10 / 15 |
| Repair complexity / authority ambiguity | 18 / 20 |
| Reproduction / merge-state difficulty | 9 / 10 |
| Downstream blocking / recurrence | 10 / 10 |
| **TOTAL** | **90 / 100** |

**RATING:** SYSTEM BLOCKER

### Verdict

**ACCEPTED / LINKED_TO_TASK / RESOLVED**

D-067 already owned the causal integration proof, so AXIOM would not create a duplicate task.

The correct task action is:
- `CPR-001 -> D-067`;
- preserve the incident evidence;
- score the root-cause repair separately;
- leave the normal D-067 acceptance score independent.

## Resolution evidence

- `docs/evidence/CRITICAL_FIX_D067_BRIDGE_RECONCILIATION_2026-10-04.md`
- `docs/evidence/D067_PHASE1_INVENTORY_EQUIPMENT_PROOF_2026-10-04.md`
- PR #62 / run #345
- PR #65 / run #351

## Next-player lesson

When many failures appear after concurrent integration, do not assume there are many unrelated bugs.

First compare the failing callers/tests against the current authoritative API contracts. A single contract-drift incident can present as many downstream failures.
