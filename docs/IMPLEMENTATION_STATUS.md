# Implementation Status — V6 Stabilization

> **Scope notice (2026-10-02):** this file remains authoritative historical/runtime evidence for the V6 stabilization work. It is no longer the primary design roadmap. Current full-project documentation authority is `docs/DOCUMENTATION_MASTER_PROGRAM.md`, indexed by `docs/DOCUMENTATION_INDEX.md`.

Updated: 2026-09-27. This record supersedes the foundation-oriented status previously
present here; the earlier history remains at upstream V6 commit
`7f5f104fb839068bdfaf5cec72f37129ae20d463`.

## CURRENT_OBJECTIVE

Finish Stage 3 integration/hardening with an executed, reproducible engine candidate.
Prepare canonicalization separately after reviewing the repaired candidate.

## VERIFIED_STATE

- Repository: `jbob-coder/Text-rpg-game`.
- Candidate branch: `fix/v6-runtime-boundaries`.
- Upstream: `integration/rules-ability-v6-reconcile@7f5f104fb839068bdfaf5cec72f37129ae20d463`.
- Upstream tree: `434d32353f4c5cab192d45298353d4cfbacff9e4`; all 45 files hash-verified.
- Untouched upstream: 258 tests; 245 passed, 1 failed, 12 errored.
- Repaired candidate: 275 tests passed, 0 failures/errors; 18 test files.
- Runtime tested: CPython 3.12.14, Linux. Python 3.10 and other operating systems were not executed.
- Seven attributes and save schema 1 remain; no save migration was performed.
- Content: 16 scenes, 25 choices, 3 quests, 1 power definition.
- `main` remains a placeholder; this repair does not promote or merge branches.

See [V6_STABILIZATION_HANDOFF.md](V6_STABILIZATION_HANDOFF.md) for evidence and API contracts.

## COMPLETED

The candidate retains deterministic checks, transactional choice rollback, persistent
history, NPC knowledge/memory/goals, multiaxis relationships, deterministic secret
propagation, equipment/sets, perks, conditions, effective/derived values, training,
recovery, quest graphs, ability/technique progression, costs, cooldowns, drawbacks,
evolution, save/load, and the local CLI.

This stabilization slice:

1. Executed untouched V6 and captured its real failures.
2. Repaired training gates with validated `resource_min` conditions, preserving the
   restricted modifier namespace and the original resource thresholds.
3. Repaired a missing test import and power prerequisite error handling through the
   existing `RuleError` effective-value adapter.
4. Restricted choice projections to visible fields; added `build_scene_view()` and
   made the CLI consume it while execution retains authored rules.
5. Redacted hidden perk provenance alongside conditions, including direct derived
   modifiers. Registry visibility reaches the engine automatically; scene/evolution
   grants preserve explicit runtime visibility through save/load.
6. Rejected incompatible runtime schema versions before serialization.
7. Shared finite-number JSON decoding between content and saves, rejecting NaN,
   Infinity and overflow literals even in arbitrary metadata.
8. Added 17 regression methods and corrected stale branch/test documentation.

## IN_PROGRESS

Canonical branch selection, promotion review, and shared-context pointer updates.
Runtime execution is no longer an unavailable-environment blocker.

## NEXT_ACTION

1. Review the candidate against its exact V6 parent; do not blind-merge foundation.
2. Establish one canonical implementation branch and refresh shared context pointers.
3. Resolve superseded PRs/branch policy as a separate repository operation.
4. Decide the seven-versus-eight stat schema after canonicalization, with an explicit
   save/content migration if it changes.
5. Isolate later module extraction and subsystem mutation unification from gameplay changes.

## BLOCKERS

The baseline runtime defects and four audited boundary defects are repaired.
Canonical branch governance remains unfinished. The final client and release scope
remain undecided; this is an engine vertical slice, not a finished game.

## ASSUMPTIONS / UNKNOWNS

- This work continues the supplied repository audit, not the separate private campaign.
- Unmarked perks retain prior visible behavior. Authors must mark secrets with runtime
  `visible: false` or registry `player_visible: false`.
- Windows/mobile and the Python 3.10 minimum remain unexecuted.
- No license, release, branch protection, or default-branch policy was selected here.

## DECISIONS / RISKS

- No hosted CI, new story content, stat migration, large refactor, or canon promotion.
- Player projections prevent accidental UI spoilers; raw local files/developer APIs
  remain inspectable and are not a security sandbox.
- `GameState.snapshot()` retains shallow-container semantics. Use `deepcopy` for an
  isolated snapshot until that separate contract is addressed.
- Large modules and some direct effect mutations remain maintenance risks.
- Story and progression balance are still provisional.

## TESTS_RUN / RESULTS

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Untouched baseline: **258 tests, 1 failure, 12 errors**.

Repaired candidate: **275 tests, OK**, including complete Directional Trace progression
and cooperative, solo, recovery, and ability save/resume routes. Focused regressions
failed before the boundary fixes and passed afterward. Evidence is under
`docs/verification/v6/`.

## FILES_CHANGED

Content resource gates; core/CLI projection and perk grants; content/persistence JSON;
power error adapter and perk visibility; status redaction; validation; focused tests;
`.gitignore`; README/status/handoff and verification records.
