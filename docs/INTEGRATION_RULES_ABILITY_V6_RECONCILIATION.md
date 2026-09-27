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


## Additional atomicity hardening

A second static integration defect was found in direct `simulation.train()` usage.

Before this pass, `train()` called `initialize_resources()` before checking whether current Stamina/Focus were sufficient. Resource initialization is internally atomic, but it can still normalize current values and write `max_*` fields. If training then failed for insufficient resources, those normalization writes could remain even though the training action itself failed.

V6 now treats resource normalization as part of the training transaction:
- snapshot existing resource state;
- normalize against the authoritative derived/set-aware maxima;
- check training affordability;
- if affordability fails, restore the exact prior resource state;
- only then proceed to skill/resource/time/history mutation.

A regression test now verifies that failed direct training leaves:
- resources unchanged;
- skills unchanged;
- world time unchanged;
- history unchanged.

The static authored-test count is now **208** across 17 test files.

This remains source/test hardening only. Exact runtime execution is still required before any green claim.


## Social-state purity and atomicity hardening

A targeted review of public social APIs found several failure paths that could change durable state even when an operation was only being queried or ultimately rejected.

V6 now hardens these paths:

- `eligible_leak_targets()` is now a read-only query. It no longer creates missing NPC shells, relationship entries, or knowledge containers merely by evaluating leak eligibility.
- `adjust_relationship()` validates every requested axis/value and plans the resulting values before mutating any relationship axis. An invalid later axis can no longer leave an earlier axis partially changed.
- `share_knowledge()` now preflights speaker knowledge and recipient containers before writing recipient knowledge or memories. A missing speaker no longer creates an empty NPC shell as a side effect of failure.
- `update_goal_progress()` now rejects missing/invalid goals without calling `ensure_npc()`; failed progress attempts no longer create empty NPC/relationship state.
- `transition_story_state()` now checks the existing/implicit previous state and `allowed_from` guard before creating or mutating an NPC.
- `execute_leak_event()` now snapshots NPC/relationship/history state and rolls the full event back if any later recipient transfer fails. Multi-recipient leak execution is therefore transactional.

Regression coverage was added for:
- leak-eligibility query purity;
- relationship multi-axis failure atomicity;
- missing-speaker share purity;
- unknown-goal progress purity;
- rejected story-transition purity;
- multi-recipient leak rollback when a later recipient is corrupt.

The static authored-test count is now **208** across 17 test files.

This remains a static/source hardening result. Exact execution of the complete V6 suite is still required.


## Quest and technique-discovery failure atomicity hardening

A further static mutation audit found two additional areas where rejected direct API operations could leave durable state changed.

### Quest mutations

Direct quest APIs now preflight mutable runtime containers before changing quest state.

Hardening added to:
- `start_quest()`
- `complete_objective()`
- `fail_objective()`
- `fail_quest()`

Changes include:
- require mutable `state.quests` for quest creation;
- require list-backed global history before quest mutation;
- require mutable quest records and list-backed completed/failed/history containers;
- validate the authored quest definition before objective completion/failure mutation;
- reject malformed quest runtime state before appending objectives or closing a quest.

Regression coverage verifies:
- corrupt global history cannot create a partially-started quest;
- corrupt quest history cannot leave an objective marked complete;
- malformed authored quest graphs are rejected before objective mutation;
- a failed manual quest-close does not change active quest status.

### Technique discovery

`discover_technique()` previously created an empty `ability["techniques"]` container before discovery requirements were evaluated when an older/partial ability state lacked that container.

If discovery then failed, the rejected operation still changed persistent ability state.

V6 now plans a missing technique container locally and attaches it only after discovery requirements pass.

A regression verifies a failed technique discovery leaves:
- ability state unchanged;
- history unchanged;
- no empty `techniques` container created.

The static authored-test count is now **213** across 17 test files.

These are source/test hardening results only. Exact V6 runtime execution remains the promotion gate.


## Equipment and persistence boundary hardening

A subsequent static review covered equipment mutation and save deserialization.

### Equipment preflight

`equip_item()` now validates all failure-prone state before replacing an equipped slot or consuming inventory.

Hardening includes:
- require the item payload to be an object;
- require mutable equipment state;
- require `consume_inventory` to be boolean;
- when consuming inventory, require a mutable inventory container and a positive integer quantity;
- require attribute/skill source containers to be mappings;
- reject boolean/non-numeric/non-finite requirement source stats instead of allowing invalid values through comparisons;
- require equipment `tags` and `passive_perks` to be lists of non-empty strings;
- compute remaining inventory quantity before the equipment commit.

Regression coverage verifies:
- immutable inventory is rejected before equipment mutation;
- corrupt/non-finite requirement source stats do not equip the item;
- malformed tag metadata is rejected before slot mutation.

### Save deserialization

`loads_state()` previously assumed the JSON root was an object and silently dropped unknown top-level fields that were not members of `GameState`.

That behavior could turn a malformed/current-schema save into a partially loaded state without surfacing potential data loss.

V6 now:
- wraps invalid JSON as `RuleError`;
- rejects non-object JSON roots;
- rejects boolean/non-integer schema versions;
- requires non-empty string `seed` and `scene_id`;
- rejects unknown top-level fields for the current schema instead of silently discarding them.

Regression coverage verifies each of those boundaries.

The static authored-test count is now **221** across 17 test files.

This remains static/source validation only. The exact V6 suite still has not been executed.


## Durable GameState boundary validation

A later pass found that both content loading and save deserialization could construct a `GameState` whose top-level containers had the wrong runtime types.

Examples included:
- `player=[]`
- `knowledge=[]`
- non-list `party`
- non-list `history`
- boolean turn/time/schema values

Several downstream systems assume those containers are mutable mappings/lists and would otherwise fail later with implementation exceptions or partial behavior.

V6 now defines a shared top-level `validate_game_state_structure()` contract in `core.py`.

It validates:
- non-empty string `seed` and `scene_id`;
- non-negative integer `turn`, `time_minutes`, and `schema_version` with booleans rejected;
- mutable mapping containers for player/flags/relationships/knowledge/inventory/quests/NPCs/abilities/equipment/perks;
- list-backed party with non-empty string member IDs;
- list-backed history whose entries are mapping objects.

The validator is now used:
- immediately after authored `initial_state` becomes a `GameState`;
- after a save payload is converted to `GameState`;
- before serializing a runtime state through `dumps_state()`.

Six regressions were added for malformed initial-state containers, invalid turn type, corrupt save containers/party entries, and invalid runtime history during save.

The static authored-test count is now **227** across 17 test files.

This remains source/test hardening only; exact runtime execution is still pending.


## Player-safe status provenance redaction

A disclosure review against `docs/context/STATUS_SCREEN_DATA_CONTRACT.md` found that `inspect_status_value()` returned the raw modifier provenance emitted by the rules engine.

That meant a mechanically active but player-hidden condition could still leak its stable condition ID through keys such as:

`condition:COND_HIDDEN`

even though the normal condition list correctly filtered that condition.

V6 now preserves the authoritative numeric total while sanitizing player-facing modifier provenance:
- conditions hidden by runtime `visible: false` are redacted;
- conditions hidden by authored `player_visible: false` are redacted when condition definitions are supplied;
- hidden condition IDs are not returned in the player-facing breakdown;
- their aggregate contribution is represented only as `unidentified_modifier`, preserving arithmetic explainability without exposing the hidden stable ID;
- nested derived-stat `direct_modifiers` are sanitized by the same rule.

Two regressions verify runtime-hidden and definition-hidden condition provenance cannot expose the hidden condition identifier.

The static authored-test count is now **229** across 17 test files.

This is still a static/source result. Exact execution of the V6 suite remains pending.


## Social numeric and metadata boundary hardening

A further social-system audit found invalid numeric/metadata values that could either persist non-finite state or raise late implementation exceptions after partial setup.

V6 now hardens:
- `ensure_npc()` against corrupt nested NPC/relationship containers before adding defaults;
- `add_memory()` memory IDs, integer importance, tag collections, and data mappings;
- `npc_learn()` knowledge IDs/source/truth, finite confidence, and integer secrecy;
- `share_knowledge()` secrecy state to require strict integer 0..5 values;
- `eligible_leak_targets()` holder/knowledge/network shape, finite personality inputs, secrecy state, and target IDs;
- `execute_leak_event()` event ID and recipient collection/IDs before any transfer;
- `adjust_relationship()` finite current/delta values;
- `relationship_meets()` mapping shape and finite threshold/current values;
- `set_goal()` stable metadata shape, integer priority, finite progress, source and data mapping;
- `update_goal_progress()` finite threshold/delta/current progress;
- `transition_story_state()` track/reason/data/allowed-from metadata before NPC mutation.

Six regressions were added covering non-finite knowledge confidence, boolean secrecy, non-finite relationship changes, invalid goal numeric metadata, invalid story-transition data, non-finite leak personality state, and malformed leak recipient collections.

The static authored-test count is now **235** across 17 test files.

This remains a static/source hardening result. Exact V6 runtime execution is still pending.


## Condition application and progression boundary hardening

A further static pass found two additional API-boundary classes where malformed caller/state data could either be silently accepted or surface as implementation exceptions rather than rule errors.

### Condition application

`apply_condition()` previously used `modifiers or {}`. A falsey but invalid value such as `[]` was therefore silently converted to an empty modifier mapping instead of being rejected.

The same path attempted `list(tags)` after rejecting strings/bytes only, so a non-iterable tag value could raise a Python `TypeError` instead of a `RuleError`.

V6 now:
- requires non-null condition modifiers to be mappings;
- preserves an explicit empty mapping without coercing invalid falsey objects;
- requires tags to be a non-string iterable before materialization;
- requires mutable player/condition containers;
- attaches a newly-created condition container only after all metadata and structure have passed preflight.

### Ability progression

`gain_ability_mastery()` now:
- requires a non-empty ability ID;
- requires mutable top-level `state.abilities` before changing nested ability state;
- rejects corrupt existing rank state instead of silently overwriting it during a mastery gain.

`technique_available()`, which is also a public query API, now validates:
- ability ID and requirement mapping shape;
- ability/knowledge/perk state containers;
- finite/non-negative rank/mastery state;
- finite/non-negative rank/mastery requirements;
- list-backed non-empty knowledge/perk requirement IDs.

Five regression methods were added covering invalid condition modifiers/tags, immutable ability containers, corrupt rank state, and malformed technique-availability queries.

The static authored-test count is now **240** across 17 test files.

A fresh Codex runtime-environment check during this pass returned no registered environments, so exact suite execution remains unavailable here and no pass claim is made.


## World-time and modifier-source boundary hardening

A further static integrity pass found two additional classes of failure.

### World-time preflight

`advance_time()` validated the requested delta and timed conditions but did not validate the existing `state.time_minutes` value or require mutable player state before committing.

This mattered beyond direct time advancement because recovery and training preflight time before performing other mutations. A corrupt current world-time value could therefore allow resource normalization to happen and only fail later when time was incremented.

V6 now requires, during the shared time-advance plan:
- existing `state.time_minutes` to be a non-negative integer with booleans rejected;
- `state.player` to be mutable before any time/condition commit.

Three regressions verify:
- corrupt current time is rejected without condition mutation;
- immutable player state is rejected before time changes;
- recovery rejects corrupt world time before resource normalization.

### Modifier source structure

The effective-stat pipeline previously assumed nested equipment/perk records and top-level player/equipment/perk containers were mapping-shaped.

Corrupt state could therefore surface `AttributeError` from calls such as `.get()` instead of a consistent modifier-contract error.

V6 now preflights modifier source containers and records:
- player/equipment/perks must be mappings;
- equipment records must be mappings;
- perk records must be mappings;
- equipment `set_id`, when present, must be a non-empty string.

This keeps direct modifier/stat queries deterministic and lets the higher RulesEngine boundary convert modifier `ValueError` failures into `RuleError` consistently.

Three regressions cover corrupt equipment records, corrupt perk records, and corrupt player containers.

The static authored-test count is now **246** across 17 test files.

These remain static/source hardening results only. Exact V6 runtime execution is still pending.


## Static-validator root and test-harness hardening

A targeted review of the validation layer found that several public validators still assumed mapping-shaped roots and could raise implementation exceptions instead of returning authored validation errors.

V6 now hardens:
- `validate_scenes()` against non-mapping scene roots;
- `validate_quest_definitions()` against non-mapping quest-definition roots;
- `validate_character_visuals()` against non-mapping visual-record roots;
- `validate_content_pack()` so falsey invalid roots such as `quests=[]` or `powers=[]` are no longer silently coerced to `{}`;
- registry cross-reference traversal so malformed scene/choice/condition/effect/power nodes are skipped safely after their structural errors are recorded.

This pass also found an existing test-harness defect: `tests/test_validation.py` called `validate_registries()` without importing it. The missing import is now fixed.

Five regression methods were added covering:
- non-mapping scene roots;
- falsey invalid quest/power roots;
- non-mapping quest roots;
- malformed registry cross-reference traversal;
- non-mapping visual-record roots.

The static authored-test count is now **251** across 17 test files.

This remains static/source verification only. The complete suite still requires exact runtime execution before any green or merge-ready claim.

## Equipment and authored-goal boundary hardening

A further Stage 3 review found two concrete integration gaps.

### Equipment boundary

`equip_item()` validated item requirements and modifier paths, but it still assumed `state.player` was mapping-shaped and allowed malformed non-null `set_id` metadata to be persisted.

That conflicted with the modifier pipeline, where `set_counts()` requires every non-null equipment `set_id` to be a non-empty string. An item could therefore equip successfully and only fail later when effective-stat/set evaluation ran.

V6 now:
- requires mapping-shaped `state.player` before reading equipment requirements;
- rejects non-null equipment `set_id` values unless they are non-empty strings;
- performs both checks before the equipment slot/inventory commit.

Two regression methods cover corrupt player containers and invalid set IDs.

### Authored NPC-goal adapter

The RulesEngine adapter for `npc_goal_create` and `npc_goal_progress` coerced authored values with `int(...)`/`float(...)` before calling the hardened social APIs.

That could silently turn a fractional priority such as `12.5` into `12`, bypassing `set_goal()`'s strict integer contract, and could surface Python conversion errors instead of the social rule boundary.

V6 now passes raw authored goal values into the social APIs so their strict validation remains authoritative.

The static scene validator now also rejects:
- non-integer/out-of-range goal priority;
- non-finite/out-of-range initial goal progress;
- non-finite goal progress deltas;
- invalid completion thresholds;
- malformed goal IDs through the existing stable-ID rule.

Two regression methods cover the RulesEngine no-coercion behavior and the authored validator contract.

[VERIFIED STATIC] V6 now contains **255 authored test methods across 17 test files**.

This is not an executed pass count. Exact runtime execution remains pending.

## Runtime verification boundary

No exact V6 Python suite has been executed from this chat.

Attempted direct repository execution is blocked because the local container cannot reach GitHub and no registered Codex execution environment is available.

No GitHub Actions workflow is being introduced solely to obtain a pass claim.

Therefore:
- historical fully observed foundation evidence remains **103 passed / 0 failed**;
- current foundation has 108 authored test methods;
- V6 has 255 authored test methods;
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
