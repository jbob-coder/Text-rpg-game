# Foundation -> V5 Reconciliation Inventory

Status: [VERIFIED STATIC INVENTORY] / NO IMPLEMENTATION CHANGE APPLIED

Repository: `jbob-coder/Text-rpg-game`

Authoritative workstream state at inventory time:

- Foundation: `foundation/text-rpg-systems` @ `b3340bc38e63e916c6cc7a8538ed1e8a34011112`
- Integration checkpoint: `integration/rules-ability-v5` @ `fd36b9f1d14528f3dc5eb37e20e9120af25af036`
- Architecture/context: `shared/game-context`
- Context to preserve later: `context/shared-game-context`
- Merge base between V5 and current foundation: `3ff37588f3ee9c0900e2e048387503c97cf9ed97`
- Foundation-only commits since merge base: **19**
- V5-only commits relative to current foundation: **28**

## Purpose

Do not merge the 19 foundation-only commits blindly.

Each commit is classified before any source reconciliation into:

- **A — DIRECT CARRY CANDIDATE**: isolated intent that can be carried with little/no semantic ambiguity after V6 is created. Still review the exact diff before application.
- **B — SEMANTIC RECONCILIATION**: overlaps V5-hardened source/tests or is already represented in evolved form. Do not cherry-pick blindly; preserve V5 invariants and port only missing intent.
- **C — DOCUMENTATION / CONTENT INDEPENDENT**: authored content or documentation that should be recovered separately from source reconciliation. Documentation claiming verification/counts must be regenerated from the reconciled branch rather than copied as current truth.

Additional per-commit status:

- **PRESENT** — equivalent intent already exists in V5.
- **MISSING** — intent is absent in V5.
- **PARTIAL** — some intent exists, but current foundation contains additional behavior/data.
- **STALE-AS-STATUS** — useful history, but verification/current-state wording cannot be copied forward as present truth.

## Executive result

The 19 commits are much narrower than a blind ahead/behind count suggests.

### Already semantically present in V5

The following foundation-only work is already represented in V5, usually in a more hardened form:

- negative-perk gate
- technique-stage gate
- authored skill training effect
- authored normal-resource recovery effect
- validation for those authored rules
- effective attribute/skill prerequisites for powers
- earned Trace Echo stabilization route through Directional Trace discovery
- related integration/unit tests
- save/resume coverage through Directional Trace discovery

These must **not** be re-applied from old foundation patches over V5.

### Actually missing from V5

Two substantive deltas remain:

1. **Power-definition cross-reference validation**
   - reject a technique requiring itself
   - reject prerequisite technique IDs that do not exist in the same ability definition

2. **Post-discovery Directional Trace content**
   - first live Directional Trace use
   - stronger Echo Strain consequence
   - deeper-route knowledge result
   - one-hour recovery scene
   - final first-use-complete flag
   - corresponding route/save-resume regression coverage

Foundation documentation describing these deltas is also newer than V5, but it must be regenerated after reconciliation.

---

# Commit-by-commit inventory

## 01 — `a3f89abbbe53362e2cb0c94bea0ab77c49f929ce`
**Message:** Add technique-stage gates and authored training recovery effects  
**Files:** `src/textrpg/core.py`  
**Class:** B — SEMANTIC RECONCILIATION  
**V5 status:** PRESENT

Foundation intent:
- add `not_has_perk`
- add `technique_stage_min`
- add `skill_train`
- add `recover_resources`

V5 already contains all four behaviors.

Important V5 evolution to preserve:
- RulesEngine has broader transactional/preflight/rollback hardening.
- Reapplying this older core patch risks overwriting newer mutation-safety behavior.

**Action:** no cherry-pick; mark satisfied by V5.

---

## 02 — `9d80ea6b4f3362d497747d4433a8b4680d06878e`
**Message:** Validate training recovery and technique-stage authored rules  
**Files:** `src/textrpg/validation.py`  
**Class:** B — SEMANTIC RECONCILIATION  
**V5 status:** PRESENT

Foundation intent:
- register `not_has_perk` and `technique_stage_min`
- register `skill_train` and `recover_resources`
- validate technique stage values
- validate training/recovery durations
- validate skill identifier presence

V5 validation already contains these rule/effect types and has stricter structural validation.

**Action:** no cherry-pick; preserve V5 validator.

---

## 03 — `1aebf8250dd57079114045e269b5324edc07e62f`
**Message:** Use effective stats for power prerequisites  
**Files:** `src/textrpg/powers.py`  
**Class:** B — SEMANTIC RECONCILIATION  
**V5 status:** PRESENT / EVOLVED

Foundation intent:
- evaluate power attribute/skill prerequisites using effective values rather than raw base values.

V5 already does this through `effective_player_value(..., equipment_sets=...)`, retaining equipment-set context and the hardened modifier contract.

The old patch calls an earlier effective-value surface and must not replace the V5 implementation.

**Action:** no cherry-pick; V5 behavior is the stronger implementation.

---

## 04 — `e11a857b44870baf0bcbc0d65b85cfd1c154c9e0`
**Message:** Add earned Trace Echo stabilization and Directional Trace route  
**Files:** `content/vertical_slice_01.json`  
**Class:** C — DOCUMENTATION / CONTENT INDEPENDENT  
**V5 status:** PRESENT

Foundation intent:
- add `QUEST_TRACE_STABILIZATION`
- add repeatable stabilization hub
- add Signal Pulse practice
- add Powers training
- add recovery
- earn stable-pattern knowledge
- earn Trace Tolerance
- discover Directional Trace through gameplay

V5 already contains this route. V5 currently has 14 scenes / 23 choices and reaches Directional Trace discovery.

**Action:** no content transplant needed for this commit; use it as provenance.

---

## 05 — `42d1d676cac73f72b82ddbf44e6742c9f3c65988`
**Message:** Validate perk negation and technique-stage cross references  
**Files:** `src/textrpg/validation.py`  
**Class:** B — SEMANTIC RECONCILIATION  
**V5 status:** PRESENT

Foundation intent:
- registry cross-validation for `not_has_perk`
- cross-reference `technique_stage_min` ability/technique references alongside `technique_discoverable`

V5's current validation layer already includes these authored types within its broader validation system.

**Action:** do not reapply old validator patch; verify equivalent coverage remains after V6 reconciliation.

---

## 06 — `4f5458dc07f78cc44d2e17d8217e6bf9c0561ec8`
**Message:** Test earned Directional Trace research and training route  
**Files:** `tests/test_vertical_slice.py`  
**Class:** B — SEMANTIC RECONCILIATION / TEST  
**V5 status:** PRESENT

V5 already contains:
`test_directional_trace_is_earned_through_training_research_and_tolerance`

The test lives in a file that has additional integration changes, so the old patch should not be replayed.

**Action:** retain V5 test; later extend it with the missing first-use assertions from commit 14.

---

## 07 — `a4443582c3f8edf752ddd8e4456892a1d757270f`
**Message:** Test technique-stage gates training and recovery effects  
**Files:** `tests/test_core.py`  
**Class:** B — SEMANTIC RECONCILIATION / TEST  
**V5 status:** PRESENT

V5 contains:
- `test_technique_stage_and_negative_perk_conditions`
- `test_scene_effects_can_train_skill_and_recover_resources`

**Action:** no replay; preserve evolved V5 tests.

---

## 08 — `0a725b7b546603dcc1a0a7f4fe4b610669956102`
**Message:** Carry save-resume route into Trace stabilization plan  
**Files:** `tests/test_save_resume_routes.py`  
**Class:** B — SEMANTIC RECONCILIATION / TEST  
**V5 status:** PRESENT

V5's save/resume suite already enters the stabilization plan.

**Action:** no replay.

---

## 09 — `177412b3a9d0aefb0eea5687c0d82b41b5a0d251`
**Message:** Add save-resume coverage for earned Directional Trace unlock  
**Files:** `tests/test_save_resume_routes.py`  
**Class:** B — SEMANTIC RECONCILIATION / TEST  
**V5 status:** PRESENT

V5 contains:
`test_directional_trace_unlock_survives_save_resume`

At V5 this covers discovery/unlock, but not the newer first-use/recovery tail.

**Action:** keep V5 test and extend semantically using commit 15 after new content is recovered.

---

## 10 — `2c60436596c1a0991180d7d58907ea17fe4b79fb`
**Message:** Record earned Directional Trace route and verification boundary  
**Files:** `docs/IMPLEMENTATION_STATUS.md`  
**Class:** C — DOCUMENTATION / CONTENT INDEPENDENT  
**V5 status:** STALE-AS-STATUS

Useful historical evidence about the foundation route and its verification boundary.

It must not replace V5/V6 implementation status because:
- branch identity differs
- test counts differ
- V5 has additional systems/tests
- runtime verification provenance differs

**Action:** use as source material only; regenerate V6 status after reconciliation/testing.

---

## 11 — `247f680cfb30502a03dbec09a43fad4327fc7540`
**Message:** Document earned Trace stabilization route and test boundary  
**Files:** `README.md`  
**Class:** C — DOCUMENTATION / CONTENT INDEPENDENT  
**V5 status:** PARTIAL / STALE-AS-STATUS

The gameplay description is newer than V5 README, but the test-status wording belongs to the foundation snapshot.

**Action:** update V6 README only after source/content/test reconciliation; do not copy verification claims blindly.

---

## 12 — `9de43f73644abbffc96ab02d2f7342b17cf73641`
**Message:** Document earned Trace Echo stabilization loop  
**Files:** `docs/SYSTEMS_CATALOG.md`  
**Class:** C — DOCUMENTATION / CONTENT INDEPENDENT  
**V5 status:** MISSING AS DOCUMENTATION; MECHANICS PRESENT

Adds the authored stabilization-loop description and provisional Directional Trace discovery contract.

The underlying route is already in V5; the dedicated catalog section is not.

**Action:** import/rewrite this documentation after V6 source/content reconciliation so terminology matches the integrated runtime.

---

## 13 — `05beafbd97fbfba1cfd8e51e9aae5a58ec379781`
**Message:** Add first live Directional Trace use and recovery consequence  
**Files:** `content/vertical_slice_01.json`  
**Class:** C — DOCUMENTATION / CONTENT INDEPENDENT  
**V5 status:** MISSING

This is the major missing content delta.

Adds:
- `TRY_DIRECTIONAL_TRACE_ON_SERVICE_FORK`
- `TRACE_DIRECTIONAL_AFTERSHOCK`
- `RECOVER_DIRECTIONAL_TRACE_ONE_HOUR`
- `TRACE_DIRECTIONAL_SESSION_END`
- `KNOW_DIRECTIONAL_TRACE_POINTS_DEEPER`
- `trace_echo.directional_first_use`
- `vertical_slice_01.directional_trace_first_use_complete`

The content uses already-supported effect types:
- `technique_use`
- `learn`
- `set_flag`
- `power_recover`

**Action:** recover this authored content into V6 after source contract reconciliation, then validate the complete pack. Do not overwrite V5 content wholesale; apply the content delta against the integrated JSON.

---

## 14 — `6c64791712d2b4663ee60430b354f39e7862f378`
**Message:** Test first Directional Trace use drawback and recovery  
**Files:** `tests/test_vertical_slice.py`  
**Class:** B — SEMANTIC RECONCILIATION / TEST  
**V5 status:** MISSING DELTA

Extends the existing Directional Trace earned-route test with:
- Trace Resonance spend
- +3 Directional Trace mastery
- stage remains `discovered`
- severity-2 Echo Strain
- deeper-route knowledge
- one-hour recovery behavior
- strain expiration
- first-use-complete flag

Because V5 already has an evolved version of the same test function, this is a manual test reconciliation, not a safe commit replay.

**Action:** port assertions into the V6 version of the existing integration test.

---

## 15 — `5a5133fcee2878913adb33753d93d584a85bd0a6`
**Message:** Extend Directional Trace persistence test through first live use  
**Files:** `tests/test_save_resume_routes.py`  
**Class:** B — SEMANTIC RECONCILIATION / TEST  
**V5 status:** MISSING DELTA

Extends the existing V5 save/resume Directional Trace test through:
- first use
- one-hour recovery
- mastery persistence
- knowledge persistence
- condition expiration
- final first-use-complete flag

**Action:** manually extend V5/V6 test; preserve any additional V5 persistence hardening.

---

## 16 — `060fb9b273adea516000abdcc5b04d896de355b2`
**Message:** Validate prerequisite technique references  
**Files:** `src/textrpg/powers.py`  
**Class:** B — SEMANTIC RECONCILIATION  
**V5 status:** MISSING

This is the main missing source invariant.

Foundation adds same-ability cross-reference checks after reading technique definitions:
- a technique cannot require itself
- a prerequisite technique must exist in the ability's `techniques` mapping
- applies to both `discovery_requirements` and normal `requirements`

V5 already has a substantially stricter `validate_power_definitions()` and `_validate_requirements_block()`. The missing cross-reference check must be inserted into that hardened structure without replacing it.

**Action:** implement the invariant manually in V6; do not cherry-pick the old function body.

---

## 17 — `5a920f0dfaab57c6a02dda762bc5b45ac069137b`
**Message:** Test prerequisite technique cross-reference validation  
**Files:** `tests/test_powers.py`  
**Class:** A — DIRECT CARRY CANDIDATE / TEST  
**V5 status:** MISSING

Adds an isolated regression proving both:
- self-dependency rejection
- unknown prerequisite technique rejection

The test intent is compatible with V5's stricter validator.

**Action:** carry the regression into V6, adapting only naming/error substrings if V5's hardened diagnostics require it.

---

## 18 — `4c8ee4ac8261d0bd9c341e3710d41a9b208aaa18`
**Message:** Record Directional Trace first use and current verification boundary  
**Files:** `docs/IMPLEMENTATION_STATUS.md`  
**Class:** C — DOCUMENTATION / CONTENT INDEPENDENT  
**V5 status:** MISSING CONTENT FACTS / STALE-AS-STATUS

Records:
- first live use costs/consequence
- new validation invariant
- 16 scenes / 25 choices
- 103 remains the latest fully executed foundation suite
- five newer tests authored

These are valid foundation-history facts but not a V6 verification report.

**Action:** preserve provenance; regenerate V6 status only after exact V6 tests run.

---

## 19 — `b3340bc38e63e916c6cc7a8538ed1e8a34011112`
**Message:** Document first Directional Trace use consequences  
**Files:** `docs/SYSTEMS_CATALOG.md`  
**Class:** C — DOCUMENTATION / CONTENT INDEPENDENT  
**V5 status:** MISSING AS DOCUMENTATION

Documents the first-use contract:
- 5 Focus
- 4 Trace Resonance
- 30-minute cooldown
- +3 technique XP
- +2 overall Trace Echo mastery
- severity-2 Echo Strain for 35 minutes
- deeper-route knowledge
- one-hour recovery restores 2 Trace Resonance
- discovery does not imply mastery

**Action:** carry this systems-contract information after the V6 content/test reconciliation confirms the contract.

---

# Classification summary

## A — Direct carry candidate

1 commit:

- `5a920f0dfaab...` — isolated regression for prerequisite technique self/unknown cross-references

Even this should be applied only after the corresponding V6 source invariant exists.

## B — Semantic reconciliation

11 commits:

- `a3f89abbbe53...` — core authored gates/effects — already present
- `9d80ea6b4f33...` — validation — already present
- `1aebf8250dd5...` — effective power prerequisites — present/evolved
- `42d1d676cac7...` — registry/cross-reference validation — present
- `4f5458dc07f7...` — earned route test — present
- `a4443582c3f8...` — core tests — present
- `0a725b7b5466...` — stabilization save/resume adaptation — present
- `177412b3a9d0...` — Directional unlock persistence — present
- `6c64791712d2...` — first-use route test delta — missing, reconcile into evolved test
- `5a5133fcee28...` — first-use save/resume delta — missing, reconcile into evolved test
- `060fb9b273ad...` — prerequisite-technique cross-reference source invariant — missing, reconcile into hardened validator

## C — Documentation/content independent

7 commits:

- `e11a857b4487...` — stabilization/Directional discovery content — already present
- `2c60436596c1...` — implementation-status history
- `247f680cfb30...` — README history/status
- `9de43f73644a...` — stabilization systems documentation
- `05beafbd97fb...` — **missing first-use/recovery content delta**
- `4c8ee4ac8261...` — first-use implementation-status history
- `b3340bc38e63...` — first-use systems documentation

---

# V6 reconciliation plan derived from the inventory

No 7 -> 8 stat migration is part of this cycle.

## Step 0 — Preserve checkpoint

Create V6 from the exact V5 checkpoint:

`integration/rules-ability-v5@fd36b9f1d14528f3dc5eb37e20e9120af25af036`

V5 remains untouched.

## Step 1 — Source reconciliation

Do **not** replay old source commits.

Only port the source intent missing from V5:

- prerequisite-technique self-reference rejection
- prerequisite-technique unknown-reference rejection

Then inspect foundation-only source changes again to ensure every other source intent is already represented in V5's evolved/hardened code.

## Step 2 — Content recovery

Apply the missing post-discovery Directional Trace content delta from `05beafbd97fb...` against the V6 content file.

Expected integrated content target:

- 16 scenes
- 25 unique choices
- 3 quests
- 1 power
- 6 knowledge registry entries
- first Directional Trace use + aftershock + recovery + final first-use flag

These counts are structural expectations, not runtime verification.

## Step 3 — Test reconciliation

Retain all V5 integration tests.

Add/adapt:
- prerequisite-technique cross-reference regression
- first Directional Trace use/recovery assertions
- save/resume through first use/recovery/final flags

Do not replace evolved V5 test files with foundation versions.

## Step 4 — Static validation

Before runtime execution:
- JSON parse
- content-pack validation
- stable-ID registry cross-references
- scene references
- quest references
- power/technique references
- no duplicate choice IDs
- modifier-path validation
- hidden-data/status projection inspection
- diff review against both V5 and frozen foundation SHA

## Step 5 — Exact runtime verification

Execute the complete V6 suite on the exact V6 checkout.

Until observed:
- 103 remains historical executed foundation evidence
- 108 foundation tests are authored, not all currently verified
- approximately 199 V5 tests are authored, not an executed V5 claim
- V6 has no green claim

## Step 6 — Corrections

Fix only observed V6 regressions. Do not combine stat-schema migration into regression repair.

## Step 7 — Checkpoint

Record:
- exact V6 SHA
- exact frozen foundation SHA
- exact V5 parent SHA
- commands
- pass/fail count
- content counts
- any reconciled semantic decisions

## Step 8 — Context consolidation later

Only after V6 is reproducible and verified:
- retain `shared/game-context` as canonical architecture/context branch
- import exclusive history from `context/shared-game-context`
- preserve per-chat/workstream provenance
- do not flatten conflicting histories
- only then retire/supersede duplicate context paths

---

# Explicit exclusions from V6 reconciliation

Do not include:

- seven -> eight stat migration
- save-schema migration for new Dexterity
- client/runtime technology selection
- UI redesign
- story canon promotion
- broad balance retuning
- new content beyond recovering the already-authored current foundation delta

The goal of V6 is **convergence**, not expansion.

---

# Authoritative stage after inventory

`CURRENT_OBJECTIVE`: converge current foundation + V5 into one reproducible implementation.

`ACTIVE_IMPLEMENTATION`: `foundation/text-rpg-systems`.

`ACTIVE_INTEGRATION_CHECKPOINT`: `integration/rules-ability-v5`.

`ACTIVE_ARCHITECTURE`: `shared/game-context`.

`CONTEXT_TO_PRESERVE`: `context/shared-game-context`.

`MERGE_BASE`: `3ff37588f3ee9c0900e2e048387503c97cf9ed97`.

`FOUNDATION_ONLY_COMMITS`: 19, individually inventoried above.

`PRIMARY_MISSING_SOURCE_DELTA`: prerequisite-technique cross-reference validation.

`PRIMARY_MISSING_CONTENT_DELTA`: first Directional Trace use/recovery tail.

`RUNTIME_STATUS`: exact reconciled HEAD not executed.

`STAT_MIGRATION`: explicitly out of scope until an integrated green seven-stat baseline exists.

`NEXT_SAFE_ACTION`: create `integration/rules-ability-v6-reconcile` from exact V5 HEAD, then reconcile source beginning with the single missing source invariant rather than merging foundation wholesale.
