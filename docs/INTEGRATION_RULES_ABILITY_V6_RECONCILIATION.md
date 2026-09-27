# Rules + Ability Integration V6 Reconciliation

Status: **IN PROGRESS — STATIC RECONCILIATION COMPLETE, RUNTIME VERIFICATION PENDING**

Repository: `jbob-coder/Text-rpg-game`

Branch: `integration/rules-ability-v6-reconcile`

Created from exact V5 checkpoint:

`integration/rules-ability-v5@fd36b9f1d14528f3dc5eb37e20e9120af25af036`

Frozen foundation reviewed for this reconciliation:

`foundation/text-rpg-systems@b3340bc38e63e916c6cc7a8538ed1e8a34011112`

Merge base:

`3ff37588f3ee9c0900e2e048387503c97cf9ed97`

## Objective

Converge current foundation behavior/content with the V5 hardened rules/ability/status implementation without blind-merging the 19 foundation-only commits and without introducing the separate seven-to-eight stat migration.

## Inventory-first rule

Before the first V6 source change, all 19 foundation-only commits since the merge base were inspected and classified.

The durable inventory lives on `shared/game-context`:

`docs/context/FOUNDATION_V5_RECONCILIATION_INVENTORY.md`

Result:
- most source intent was already present in V5 in evolved form;
- one source invariant was genuinely missing;
- the latest post-discovery Directional Trace content tail was genuinely missing;
- several newer foundation documentation commits describe state that must be regenerated for V6 rather than copied as verification truth.

## Source reconciliation performed

### Preserved from V5

V6 retains V5's hardened implementations for:
- `not_has_perk`
- `technique_stage_min`
- authored `skill_train`
- authored `recover_resources`
- canonical effective-value calculations
- equipment-set-aware power prerequisites
- transactional RulesEngine behavior
- modifier/path validation
- ability mutation hardening
- player-safe status/ability projection

Older foundation source patches for these behaviors were not replayed.

### Added missing invariant

`src/textrpg/powers.py` now validates prerequisite technique references across the full technique mapping after structural validation.

For both:
- `discovery_requirements.techniques`
- `requirements.techniques`

V6 rejects:
- self dependency;
- references to unknown techniques in the same ability definition.

This was ported semantically into V5's hardened validator rather than replacing the validator with the older foundation implementation.

## Content reconciliation performed

The missing latest foundation content tail was recovered into:

`content/vertical_slice_01.json`

The V6 authored content now matches the frozen foundation content object exactly for that file.

Current structural target:
- 16 scenes
- 25 choices
- 25 unique choice IDs
- 3 quests
- 1 power definition
- 6 knowledge registry entries
- 1 perk registry entry
- 2 item registry entries
- 1 condition registry entry

Recovered post-discovery route:
- controlled first Directional Trace use;
- 5 Focus + 4 Trace Resonance cost through the existing technique definition;
- severity-2 Echo Strain for 35 minutes;
- deeper-route knowledge;
- one-hour recovery;
- final first-use completion flag.

## Test reconciliation performed

V6 retains all V5 integration tests and adds/reconciles the missing foundation test intent.

Added:
- prerequisite-technique self/unknown cross-reference regression.

Extended existing V5 tests:
- Directional Trace earned route now verifies first use, resource spend, mastery, strain, knowledge, recovery, and final flag;
- save/resume route now continues through first use and recovery.

Current static count:
- **200 authored `test_*` methods**
- 17 test files

This is an authored-test count, not a pass claim.

## Static content audit

A fresh V6 structural audit was performed against the current content object.

Observed:
- JSON parse: OK
- scenes: 16
- choices: 25
- unique choices: 25
- quests: 3
- powers: 1
- knowledge registry: 6
- perks registry: 1
- items registry: 2
- conditions registry: 1
- duplicate choice IDs: none
- missing next-scene targets: none
- missing quest/objective references in audited effects: none
- missing power/technique references in audited gates/effects: none
- missing registry references in audited categories: none
- prerequisite technique self/unknown references in current authored power content: none
- static audit errors: 0
- static audit warnings: 0

This static audit does not replace execution of the Python validator/tests.


## Additional integration defect found during static plumbing review

After the initial reconciliation, a cross-system context propagation defect was found in `RulesEngine._apply_effects()`.

The authored effects:
- `skill_train`
- `recover_resources`

called `simulation.train()` / `simulation.recover()` without forwarding the engine's resolved equipment-set definitions.

Those simulation functions already accept `set_definitions` and use it when recalculating resource maxima. Omitting the context meant an authored scene-driven training/recovery action could calculate different Health/Stamina/Focus/Resolve maxima from the rest of the same RulesEngine when active set bonuses modified derived resource maxima.

V6 now forwards:

`set_definitions=self.equipment_sets`

for both authored effect paths.

A regression test was added that equips two pieces of a set with direct `derived.max_stamina` and `derived.max_focus` bonuses, executes authored training and recovery choices, and verifies the resource maxima continue to match the set-aware derived values.

This changes the static authored-test count from 200 to **201**.

Runtime execution is still pending; this is a source-level fix plus authored regression, not a pass claim.

## Runtime verification boundary

No exact V6 Python suite has been executed from this chat.

Attempted direct repository execution is blocked because the local container cannot reach GitHub and no registered Codex execution environment is available.

No GitHub Actions workflow is being introduced solely to obtain a pass claim.

Therefore:
- historical fully observed foundation evidence remains **103 passed / 0 failed**;
- current foundation has 108 authored test methods;
- V6 has 200 authored test methods;
- V6 runtime result remains **UNKNOWN / NOT EXECUTED**.

Do not call V6 green, merge-ready, complete, or verified as a whole until the exact branch is executed.

## Deliberate exclusions

V6 reconciliation does not include:
- seven-to-eight stat migration;
- Dexterity bootstrap/save migration;
- final client/runtime selection;
- UI visual redesign;
- canon promotion;
- broad balance retuning;
- new story expansion beyond recovering the already-authored foundation delta.

## Remaining gate

1. Obtain an authorized exact runtime for the V6 branch.
2. Execute:
   `PYTHONPATH=src python -m unittest discover -s tests -v`
3. Fix only observed integration regressions.
4. Re-run until green.
5. Verify save/resume and hidden-data/status boundaries.
6. Record exact V6 SHA and observed result.
7. Only after that, consolidate duplicate context histories.
8. Keep seven-to-eight stat migration as a later isolated migration.
