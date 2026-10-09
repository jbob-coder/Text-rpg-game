# Veyra D-072 Durable-Owner Transaction Acceptance Review — 2026-10-08

Status: **NON-OWNING SOURCE/CONTRACT REVIEW — NOT D-072 ACCEPTANCE**  
Reviewer: **Veyra / PLAYER_VEYRA / SESSION_VEYRA_20261007T1140-0400_S02**  
Observed authority HEAD: `8cdb1f29bb741cfc5caeba7bad54e9205a8529e4`  
Live ownership at review: **D-072 IN_PROGRESS / Silex**  
Execution evidence from this review: **NONE — no Python/Android/CI/emulator/device tests run**

## 1. Purpose

This review does not claim D-072, edit Silex implementation, define Gate Twelve canon, or mark any tactical gate complete.

It closes one acceptance-analysis gap that is separate from the existing Quorix temporal-condition review:

> How should D-072 compose current durable GameState owners whose helpers have different mutation and history behavior while still satisfying one outer atomic aftermath transaction?

The governing contract is:

- `docs/systems/INJURY_CONDITION_AFTERMATH_STANDARD.md`;
- `docs/systems/PHASE_1_COMBAT_SCHEMA_API_MIGRATION_PACKET.md`.

The relevant current source owners inspected are:

- `src/textrpg/core.py`;
- `src/textrpg/simulation.py`;
- `src/textrpg/quests.py`;
- `src/textrpg/social.py`;
- `src/textrpg/equipment.py`.

This review complements, and does not replace:

- `docs/reviews/QUORIX_D072_TEMPORAL_CONDITION_ACCEPTANCE_REVIEW_2026-10-08.md`;
- Veyr's separate NPC/social D-072/D-073 review evidence where available;
- the live D-072 owner implementation and CI.

## 2. Contract facts that constrain D-072

The aftermath standard requires:

1. validate planned writes;
2. take a **deep** snapshot;
3. apply the plan;
4. validate the resulting state;
5. append one aftermath history record;
6. commit;
7. rollback **all** durable changes on failure.

Partial aftermath is forbidden.

The combat migration packet additionally states:

- GameState remains the durable RPG/world owner;
- CombatSession stays transient for Phase 1;
- aftermath is a validated CombatSession -> GameState transaction;
- current GameState fields must be reused where semantically correct;
- quest consequences go through quest functions;
- social/NPC consequences use current durable social owners;
- history contains **one durable aftermath summary plus existing social/quest events as appropriate**;
- the entire tactical log/transcript must **not** be copied into GameState history;
- save schema remains version 1;
- persistent NPC/player references must resolve to existing authoritative IDs.

These requirements mean D-072 cannot treat every durable field as an equivalent raw dictionary assignment.

## 3. Current helper behavior is heterogeneous

### 3.1 Inventory

`core.adjust_inventory()` validates:

- non-empty item ID through `inventory_quantity()`;
- non-zero integer delta;
- non-negative resulting quantity.

It then mutates `state.inventory`.

It does **not** append `state.history`.

Implication: inventory is a semantic helper, but D-072 must decide whether loot/resource provenance is represented only in the single aftermath summary or by another already-authorized event. Do not invent a duplicate tactical-log history stream.

### 3.2 Equipment

`equipment.equip_item()` validates the item, slot, requirements, modifier map, passive/tag shape and optional inventory quantity before writing `state.equipment` and optional inventory consumption.

It does **not** append `state.history`.

Implication: equipment changes can participate in the outer transaction, but the outer transaction still owns rollback across equipment plus every other domain.

### 3.3 Conditions and world time

`simulation.apply_condition()` validates condition metadata and modifier paths before adding/replacing the durable player condition. It stamps:

`applied_at = state.time_minutes`.

`simulation.validate_time_advance()` provides a non-mutating time preflight.

`simulation.advance_time()` precomputes timed-condition effects, then updates `time_minutes`, decrements durations and removes expired conditions.

Neither helper appends `state.history`.

Implication: D-072 must explicitly choose/test condition-onset versus encounter-time ordering under the separate temporal review. Regardless of that choice, the entire condition+time result belongs inside the same outer rollback boundary.

### 3.4 Quests

Quest mutation APIs such as `start_quest()`, `complete_objective()`, `fail_objective()` and `fail_quest()` mutate quest records and append semantic quest history to both quest-local history and/or `state.history`.

A quest action can also continue into outcome/stage resolution after an earlier mutation/history append.

Implication: D-072 must not assume a quest helper is the whole-aftermath transaction. If a later domain consequence fails after the quest helper succeeds, the **outer** D-072 transaction must restore the prior quest record and global history exactly.

### 3.5 Social/NPC state

`social.add_memory()` and `social.npc_learn()` call `ensure_npc()`, which can materialize missing NPC/relationship containers.

`social.adjust_relationship()` validates axes, calls `ensure_npc()`, mutates relationship state and appends a `relationship_change` event to `state.history`.

Some higher-level social operations, such as leak execution, have their own local rollback, but D-072 cannot assume all social helpers do.

Implication:

- a persistent aftermath reference must be validated as an allowed existing durable identity **before** calling a helper that can create a missing NPC;
- helper-level atomicity is not a substitute for the aftermath-level transaction;
- semantic social events already emitted by accepted helpers should not be duplicated manually.

## 4. Deep snapshot requirement is stricter than `GameState.snapshot()` alone

`GameState.snapshot()` returns a mapping containing the current nested durable containers.

The current rules engine correctly uses a **deep copy** when it needs a transactional baseline.

D-072 therefore must not treat:

`before = state.snapshot()`

as an isolated rollback image.

Acceptance requires the equivalent of a deep durable baseline before any planned mutation, followed by exact restoration if any late validation/application step fails.

`validate_game_state_structure()` is necessary structural validation, but it does not prove every semantic reference:

- authored quest identity;
- authored item provenance;
- allowed persistent NPC identity;
- condition registry/content legality;
- encounter-result binding;
- player-safe visibility.

Those need the relevant domain/content preflight in addition to the top-level structure check.

## 5. History policy for D-072

The source and migration contract together support this policy:

1. preserve semantic quest/social history produced by the accepted owner APIs when those domain mutations legitimately occur;
2. append exactly one durable **aftermath summary** record for the encounter commit;
3. do not manually duplicate a quest/social event already emitted by its owner helper;
4. do not copy the raw CombatSession event log, AI diagnostics, hidden contacts, utility scores, or private tactical transcript into GameState history;
5. a failed aftermath leaves history exactly as it was before the attempted transaction.

“one aftermath history record” therefore does **not** mean “only one total state.history entry may be added” when accepted quest/social APIs produce their own semantic events. The migration packet explicitly allows one summary **plus existing social/quest events as appropriate**.

## 6. Publication and object-identity boundary

D-072 is a durable GameState transaction task, while P11/CPR-006 separately defines Android session load publication semantics.

For a state-level aftermath helper that receives an existing durable `GameState` object, the safest D-072 contract is:

- validate/stage against an isolated deep candidate or deep baseline;
- publish the accepted result into the caller's authoritative durable state boundary atomically;
- on failure restore the caller-visible durable state exactly.

D-072 should not silently replace only one holder of a shared state object and leave another holder stale.

P11 is moving Android session ownership toward a detached `AndroidGameSession.state` owner, which reduces the old `LoadedContentPack.state` alias risk, but D-072 must not assume that P11 completion changes its state-level transaction contract. Session-level replacement/publication belongs to the later integration boundary and must update the authoritative holder deliberately.

## 7. Acceptance checklist for Silex / future D-072 CI

The following checks are review guidance, not executed evidence.

### DA-01 — Terminal-result binding

An aftermath plan is accepted only for the authoritative completed/retreated encounter result and correct pre-combat checkpoint/session identity. A caller-supplied copied flag or raw transcript is insufficient.

### DA-02 — Deep durable baseline

Before the first durable mutation, capture a deep baseline covering all GameState fields that D-072 can affect, including nested:

- player/resources/conditions;
- inventory/equipment;
- quests and quest-local history;
- NPCs/memories/knowledge/goals/story state;
- relationships;
- flags/knowledge;
- time;
- global history.

### DA-03 — Semantic reference preflight

Before apply:

- persistent NPC refs already resolve to authorized durable IDs;
- quest refs/objectives are legal for the current quest definition/state;
- item/loot IDs and provenance are valid;
- condition IDs/modifier paths are allowed for the selected integration content status;
- numeric resource/time values are finite and valid;
- no proposed canon is silently promoted.

### DA-04 — Mixed-helper late-fault rollback

Inject a failure **after** at least one helper with durable history has succeeded, then assert exact pre-transaction restoration of:

- quest state/history;
- NPC/social state;
- relationships;
- inventory/equipment;
- conditions/resources;
- time;
- global history.

This is stronger than proving each helper's local validation.

### DA-05 — History cardinality/provenance

On successful commit assert:

- exactly one aftermath-summary event;
- only the expected semantic quest/social events in addition;
- no duplicated manually-replayed domain event;
- no raw tactical transcript/private AI event in durable history.

### DA-06 — Existing-NPC guard

A plan targeting an unknown persistent NPC ID fails before `ensure_npc()` can materialize a new durable NPC/relationship accidentally.

Encounter-local provisional contacts may remain transient under D-073's later integration contract; they must not become persistent NPC canon through D-072.

### DA-07 — Inventory/equipment rollback

A late failure after loot/equipment mutation restores both containers, including consumed quantity and previous equipped slot state.

### DA-08 — Quest rollback after emitted history

A late failure after `complete_objective()` or another quest mutation restores:

- completed/failed objective lists;
- stage/status;
- quest-local history;
- global history;
- any downstream outcome mutation.

### DA-09 — Social rollback after emitted history

A late failure after a relationship or other social consequence restores the prior NPC/relationship/history state exactly.

### DA-10 — Time/condition consistency

Consume the separate temporal-condition review and prove the chosen onset rule explicitly. World time is charged exactly once; preexisting timed conditions and newly incurred injury behave according to the documented rule.

### DA-11 — Schema-v1 round trip

After a successful aftermath, save/load preserves only approved durable consequences and does not introduce a tactical top-level save field.

### DA-12 — Replay/stale-plan rejection

Re-applying the same accepted aftermath plan, or applying one bound to a stale encounter/checkpoint, must not duplicate loot, quest/social events, time, injury, or the aftermath summary.

If D-072 has no explicit replay-binding mechanism, that is an integration risk to resolve before claiming durable exactly-once behavior.

## 8. Non-defect findings / boundaries

This review does **not** report a confirmed implementation defect because no D-072 implementation branch/PR was available on authority at review time.

It identifies acceptance risks inherent in composing the current owner APIs:

- mixed history behavior;
- helper-local versus whole-aftermath atomicity;
- helpers that can create missing NPC state;
- shallow `snapshot()` unless explicitly deep-copied;
- structural validation versus semantic reference validation;
- exactly-once replay behavior.

These are requirements to test against the eventual implementation, not proof that Silex's implementation is wrong.

## 9. Disposition

**REVIEW SUPPORT ONLY. D-072 ownership remains Silex.**

Recommended owner response when a D-072 candidate is visible:

- link each DA-01..DA-12 check to source/tests or mark it intentionally out of scope with contract evidence;
- add focused fault injection around at least quest/social history-producing helpers;
- show the exact history policy and replay policy;
- run the normal current-authority merge-state gate before DONE.

No task state, score, canon status, save schema, runtime code, Android surface, or test result is changed by this review.
