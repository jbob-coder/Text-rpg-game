# THE GAME — AI Brag Room

**Status:** ACTIVE  
**Purpose:** evidence-backed accomplishment log and cross-agent handoff channel.

This is the repository-native "chat room" where AI agents record what they actually shipped. It is intentionally more informal than the master task register, but it may never contradict repository evidence.

## Rules

1. Brag only after a primary task is genuinely complete or after a meaningful verified bonus.
2. Every claim must point to evidence: commit/HEAD, files, tests, build/run IDs, artifact hashes, or documented audit output as applicable.
3. Never claim a test/build/device result that was not executed and observed.
4. Never turn proposal into canon in a brag entry.
5. Keep hidden/private game state out of player-facing screenshots or prose.
6. Before taking the next primary task, append the completed task's Brag Card here.
7. If the agent is running inside an interactive ChatGPT conversation, also post a concise version of the Brag Card in the active chat so the user and later AI agents can see the accomplishment. If the agent has no chat-posting capability, this repository entry is sufficient and remains canonical.
8. A bonus gets its own line/card but cannot disguise an incomplete primary task.
9. Other agents may respond by appending a short `CHALLENGE ACCEPTED` note when they claim the next task; never edit another agent's historical brag entry.

## Brag score

- P0-CRITICAL primary complete: 100
- P0 primary complete: 90
- P0/P1 primary complete: 75
- P1 primary complete: 60
- Verified bonus: +20

Score has no authority. Evidence and correctness outrank score.

## Brag Card template

### BRAG — <TASK_REF> — <short title>
- **AGENT:** <agent/session identifier>
- **CLAIM_HEAD:** <sha>
- **COMPLETION_HEAD:** <sha>
- **SCORE:** <base + optional bonus>
- **WHAT I SHIPPED:** <concise factual summary>
- **BUGS / GAPS I KILLED:** <what was actually resolved>
- **PROOF FLEX:** <tests/builds/audits and exact results>
- **FILES / ARTIFACTS:** <key paths / artifact hashes>
- **PHASE 1 / PROGRAM IMPACT:** <requirements/dependencies changed>
- **BONUS:** <done/not done + evidence>
- **UNVERIFIED / STILL BLOCKED:** <honest remaining boundary>
- **NEXT AI UNLOCK:** <next eligible task(s)>
- **MESSAGE TO NEXT AI:** <short challenge/handoff>

## Challenge claim template

### CHALLENGE ACCEPTED — <TASK_REF>
- **AGENT:** <agent/session identifier>
- **CLAIM_HEAD:** <sha>
- **WHY THIS TASK:** <dependency/rank reason>
- **I WILL PROVE:** <acceptance criteria summary>

## Hall of verified wins

No campaign brag entries recorded yet. Add entries; do not rewrite history.

### BRAG — D-060 — Exact-revision corpus control
- **AGENT:** Nodus
- **CLAIM_HEAD:** `8d3d5e80c2c3a346575b3f12e156ee77a649a421`
- **COMPLETION_HEAD:** `3507f2b1e0087bf41c3d6ed41f44aa0770a10591`
- **SCORE:** 100
- **WHAT I SHIPPED:** revision-bound corpus inventory tooling, contamination regression coverage, fresh immutable structural evidence, and a second-pass documentation recalibration that replaces quota-filler growth with closure gates.
- **BUGS / GAPS I KILLED:** the inventory tool no longer counts mutable working-tree/untracked state as revision evidence; source SHA is explicit; D-058/D-019 drift is reconciled.
- **PROOF FLEX:** `PYTHONPATH=. python -m unittest tests.test_documentation_inventory_tool -v` -> 2 tests passed, 0 failures/errors in isolated temporary Git repositories using the exact file bytes later committed. Executed local blob hashes match committed tool/test blob SHAs. Exact Git-tree evidence at `4570005b4d544f56db1222623955139a3b23c01a` records 561 tracked files and 387 Markdown files.
- **FILES / ARTIFACTS:** `tools/documentation_inventory.py`; `tests/test_documentation_inventory_tool.py`; `docs/evidence/repository_inventory_d060_exact_revision_2026-10-04.json`; `docs/SECOND_PASS_DOCUMENTATION_RECALIBRATION_2026-10-04.md`.
- **PHASE 1 / PROGRAM IMPACT:** removes the D-060 control dependency so migration/proof tasks with satisfied direct contracts can proceed; no playable requirement is falsely claimed complete.
- **BONUS:** not done; D-060-B is not claimed.
- **UNVERIFIED / STILL BLOCKED:** full-checkout execution for current Markdown word/heading totals remains D-019 work; no full engine suite, Android build, physical-device acceptance, or APK claim.
- **NEXT AI UNLOCK:** D-061 is the highest-ranked next task; D-062/D-063 and other dependency-satisfied D-060 children can be exposed for parallel work.
- **MESSAGE TO NEXT AI:** Control surface is clean. Beat the migration packets with source-grounded state/save/projection evidence, not prose volume.

### BRAG — D-029 — PR #19 exporter provenance ambiguity closed
- **AGENT:** Kestrel
- **CLAIM_HEAD:** `dd2e28e35c0946f8baa86fb3513cebf431dcf73b`
- **COMPLETION_HEAD:** `b4694ab7a103a729780825c40807fba346ffd026`
- **SCORE:** 90
- **WHAT I SHIPPED:** exact historical provenance audit proving the PR #19 committed tree contains the delivered raster consumer set but no persisted exporter/generator/tool/script.
- **BUGS / GAPS I KILLED:** replaced the ambiguous `not persisted/found` wording with an exact disposition: `HISTORICAL GENERATION PROCESS NOT PERSISTED IN PR19 COMMITTED TREE`.
- **PROOF FLEX:** inspected PR #19's 31 changed paths, exact head `c11133122d47009abc71e8c6e91c08aedbe91ae2`, root tree and `tools` lookup; no exporter path or `tools/` directory exists in that committed head. This is a repository audit, not a runtime/build test.
- **FILES / ARTIFACTS:** `docs/assets/PR19_RASTER_EXPORTER_PROVENANCE_AUDIT_2026-10-04.md`.
- **PHASE 1 / PROGRAM IMPACT:** removes a reconstruction ambiguity without changing runtime assets or visual canon; future deterministic reconstruction continues to use the repository-owned equivalence verifier as a replacement tool rather than falsely treating it as recovered historical tooling.
- **BONUS:** not done; zero-to-runtime asset-family checklist remains optional.
- **UNVERIFIED / STILL BLOCKED:** fresh exact-checkout raster-equivalence execution, owner visual promotion choices, destination visual QA and physical-device QA remain open; no build/device result is claimed.
- **NEXT AI UNLOCK:** D-029 parallel slice acceptance is satisfied; D-029 global asset program remains IN_PROGRESS under its documented production/owner gates. Remaining READY parallel lanes may proceed independently.
- **MESSAGE TO NEXT AI:** Historical absence is now proven at the PR head. Do not resurrect the old exporter as a repository artifact; verify reconstruction with current tooling and exact-head evidence.
