# V6 stabilization handoff — 2026-09-27

## CURRENT_OBJECTIVE

Close the exact V6 execution gap and the four boundary defects identified in the
user-supplied audit of `jbob-coder/Text-rpg-game`. This is Stage 3 engine stabilization.

## Prompt reference and scope

`PROMPT_AUDIT_2026_09_27`: the user supplied an audit identifying
`integration/rules-ability-v6-reconcile@7f5f104fb839068bdfaf5cec72f37129ae20d463`
as the implementation candidate, with 258 authored but unexecuted tests. Its requested
next sequence was execution, observed repairs, safe scene/choice projection, hidden-perk
provenance, schema preservation, strict content JSON, then canonicalization.

The attached context-preservation rules were read. No private campaign save or novel
attachment was modified or imported. Repository instructions and source files were
used for this engineering slice; no `AGENTS.md` was present in the V6 source tree.
The final-acceptance/testing policy on `shared/game-context@33e55db…` was also read:
intermediate testing remains an internal responsibility and no hosted CI was added.

## VERIFIED_STATE

| Source / execution | Observed result |
| --- | --- |
| Original V6 commit | `7f5f104fb839068bdfaf5cec72f37129ae20d463` |
| Original V6 Git tree | `434d32353f4c5cab192d45298353d4cfbacff9e4` |
| Source retrieval | 45/45 files, every Git blob hash matched; complete Git tree matched |
| Untouched V6 suite | 258 tests: 245 passed, 1 failure, 12 errors; exit 1 |
| Repair candidate | `fix/v6-runtime-boundaries`, based directly on the original V6 commit |
| Repaired suite | 275 tests across 18 files; 0 failures/errors/skips; exit 0 |
| Runtime | CPython 3.12.14 on Linux; standard library only |
| Content validation | Sample scenes valid; full vertical slice loads and validates |
| Content size | 16 scenes, 25 choices, 3 quests, 1 power definition |
| CLI smoke | New game, first choice, save, restart, load, save again; equivalent state |
| Stat/save model | Seven attributes; schema 1; no migration |

Direct Git transport was unavailable. The source was retrieved through the authenticated
GitHub connection and verified by content identity. A local snapshot commit was used
only for diffs; it was not presented as the upstream commit. The remote repair commit
uses the actual upstream V6 parent, not that local snapshot.

## Runtime defects and repairs

1. **Training resource gates were incompatible with the hardened stat contract.**
   Four requirements used `stat_min` with `stat: resources.*`. Stat conditions require
   `path`, and the modifier pipeline intentionally rejects the `resources` namespace.
   Merely renaming the field did not repair the problem. A separate `resource_min`
   condition now compares the current registered resource pool. The four original
   thresholds remain 8/12 stamina/focus for practice and 16/10 for training. Capacity
   modifiers cannot satisfy a current-resource gate; querying does not spend resources.
2. **A power test omitted its import.** `technique_discovery_status` is now imported;
   the original test assertions are preserved.
3. **Power prerequisite errors escaped the rule boundary.** Powers now use the existing
   core effective-value adapter so malformed modifier state becomes `RuleError` before
   resource/mastery mutation. Arithmetic and set context are unchanged.

All original tests were retained. Three resource-gate regressions brought the first
green runtime checkpoint to 261 tests; the audited boundary regressions bring it to 275.

## Repaired public contracts

### Scene and choice projection

- `engine.build_scene_view(state)` returns `id`, `title`, `body`, and `choices`.
- `engine.available_choices(state)` returns `id`, `text`, `enabled`, plus an authored
  `disabled_reason` only for locked choices.
- Hidden choices, raw requirements/checks/effects/outcomes, future-scene targets, and
  arbitrary metadata are excluded. Visible text fields reject structured objects.
- Results are detached; modifying a returned view cannot change authored rules.
- `choose(state, choice_id)` re-evaluates visibility/eligibility and resolves authored
  checks/effects internally. The CLI renders the projection.
- Raw `get_scene()`, `GameState`, modifier explanations, and resolution events remain
  developer/engine APIs. They are not safe payloads for a future player client.

Compatibility: consumers that relied on extra authored fields from `available_choices`
must move that logic to engine/tooling code. The inspected repository consumers use
only the retained fields. Existing authoring/check/effect behavior remains tested.

### Hidden perks

- Runtime perks may declare boolean `visible`; scene `add_perk` and evolution
  `grant_perks` preserve it. Save/load retains it.
- Registry metadata may declare boolean `player_visible`. The content loader passes
  the perk registry into `RulesEngine(perk_definitions=...)` automatically.
- Either false value hides perk provenance from `inspect_status_value()`.
- Hidden perks and conditions contribute numerically through `unidentified_modifier`,
  including nested direct-derived breakdowns. Visible sources and totals remain intact.
- Invalid visibility values are rejected. Unmarked perks retain prior visible behavior.
  A manual `RulesEngine` caller must supply its authored perk definitions if visibility
  exists only in those definitions.

### Save schema and JSON

- Serialization requires `state.schema_version == CURRENT_SCHEMA_VERSION` after normal
  structure validation. Unsupported versions require an explicit migration; saving
  cannot relabel them as schema 1 or overwrite an existing save with that payload.
- Content files and saves share finite-number JSON decoding. NaN, Infinity,
  -Infinity, and overflowing float literals such as `1e400` are rejected, including
  inside arbitrary metadata. Ordinary finite values retain their existing behavior.
- `content_pack_from_mapping` remains the trusted in-memory authoring API; JSON parsing
  guarantees apply to file/text loading. This change does not implement save migrations.

## TESTS_RUN / reproducibility

From the candidate repository root:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

The recorded runs also set `PYTHONDONTWRITEBYTECODE=1` to avoid scratch bytecode caches.
No dependency installation, GitHub Actions, or hosted execution was used.

Evidence in `docs/verification/v6/`:

- `baseline-source.json`: original commit/tree and all 45 Git blob identities.
- `baseline-tests.log`: complete failing untouched V6 execution.
- `candidate-runtime.json`: hashes for all 39 source/test/content/config runtime files.
- `candidate-tests.log`: complete 275-test passing candidate execution.
- `*-regressions-before.log`: observed failures before each new contract repair.
- `cli-smoke.log`: real CLI subprocess startup and save/resume verification.

The candidate runtime manifest SHA-256 is
`bc25563aaa67da53b0a0f1ac62aa296301412bee0f20dc21b82c28fa475a0626`.
It identifies runtime inputs independently of documentation-only changes or commit IDs.
The repair PR records the published commit and its final execution result.

## Acceptance checks

| Question | Yes / No | Notes |
| --- | --- | --- |
| Was untouched V6 really executed? | Yes | Full source hash verification preceded the 258-test run |
| Was untouched V6 green? | No | 1 failure and 12 errors; never promote that result as passing |
| Do repaired tests pass? | Yes | 275, including all original tests and 17 additions |
| Do progression/save-resume routes pass? | Yes | Full Directional Trace and existing route tests |
| Are the four audited boundary defects covered? | Yes | Regression failures were observed before repairs |
| Does the CLI start and resume a saved run? | Yes | Separate subprocesses; equal saved state |
| Was the stat schema migrated? | No | Deferred deliberately |
| Was `main` changed? | No | Canonicalization remains separate |
| Were all supported runtimes/platforms tested? | No | Python 3.12/Linux only |
| Is the complete game ready for final acceptance? | No | This scope is the engine stabilization slice |

## NEXT_ACTION / remaining risks

1. Review this repair candidate, then select/promote a canonical implementation branch.
2. Refresh shared-context references and supersede obsolete PRs/branches deliberately.
3. Resolve the seven/eight-stat decision through an isolated migration plan.
4. Address the shallow `snapshot()` contract, large modules, and direct subsystem
   mutations in later focused slices. No broad refactor was mixed into this repair.

No final client, dedicated combat/crafting system, license, release, branch protection,
or complete-game acceptance is claimed. The repository still exposes raw authored
content publicly; player projections prevent accidental UI disclosure, not inspection
of locally available source files.

## Continuity graph

| From | Relationship | To |
| --- | --- | --- |
| User audit, 2026-09-27 | identifies candidate | Original V6 `7f5f104…` |
| Baseline execution | reveals causes | Resource gate mismatch; missing import; exception boundary |
| Repair branch | derives from | Original V6, without foundation merge |
| `test_scene_projection.py` | verifies | Visible scene/choice boundary and unchanged execution |
| `test_status.py` + perk/content tests | verify | Hidden provenance and grant/save propagation |
| `test_persistence.py` + `test_content.py` | verify | Schema preservation and finite JSON |
| Runtime manifest + full test log | identify and verify | Repaired candidate runtime |
| This handoff | supersedes runtime-unknown claim | Earlier V6 reconciliation checkpoints |
