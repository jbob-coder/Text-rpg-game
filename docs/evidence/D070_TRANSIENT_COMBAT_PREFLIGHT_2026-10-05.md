# D-070 — Transient Combat Session / Turn Engine Preflight

**Status:** READ-ONLY PREPARATION / DO NOT CLAIM BEFORE D-069 DONE  
**Prepared by:** AXIOM  
**Observed authority HEAD:** `bc9668a07656b2ad7f76b89601c7133f75471df8` — re-fetch after D-069 completion.  
**Task:** D-070 — Tactical transient state, turn and action engine  
**Dependency:** D-069 DONE

This packet exists so the D-069 -> D-070 handoff does not require another repository-wide architecture pass.

It is not a task claim and does not authorize early D-070 implementation.

## 1. Authority

Read in this order after D-069 closes:

1. live D-070 Bulletin entry;
2. this preflight;
3. `docs/systems/PHASE_1_COMBAT_SCHEMA_API_MIGRATION_PACKET.md`;
4. `docs/systems/TURN_INITIATIVE_ACTION_BUDGET_STANDARD.md`;
5. `docs/systems/TACTICAL_COORDINATE_OCCUPANCY_STANDARD.md`;
6. D-069 final evidence + Learning Ledger record;
7. current `combat_schema.py` / `combat_grid.py`.

Only then inspect broader combat documents if an acceptance gap genuinely requires them.

## 2. Locked D-070 responsibility

D-070 implements **transient authoritative encounter execution**.

It owns:
- `CombatSession` / equivalent transient encounter state;
- `TacticalActorState` or equivalent encounter-local mutable actor state;
- round index;
- initiative snapshot/order;
- activation index/state;
- active actor;
- four-unit Phase-1 action budget;
- encounter-local actor coordinates/occupancy;
- movement commit using the D-069 authoritative path/grid query;
- authored action-cost legality at the transient session boundary;
- deterministic committed event index/log;
- rollback when a committed action transaction fails;
- end activation and round advance;
- incapacitated activation skip as a state-engine rule;
- deterministic replay/transcript primitives required for D-070-B.

D-070 must not add tactical fields to durable `GameState` schema v1.

## 3. Explicitly outside D-070 first seam

Do not absorb:
- awareness/detection/identification logic;
- hidden-information projection;
- directional-cover attack modifiers;
- objectives/retreat runtime;
- bounded combat AI;
- persistent injury/aftermath commits;
- Gate Twelve authored encounter content;
- Android bridge/DTO/ViewModel/Compose tactical UI;
- save-schema v2 or mid-combat persistence.

Those remain downstream D-071+ responsibilities.

### Attack/damage boundary

No current task authority explicitly requires D-070 to implement the full attack/damage formula.

The first D-070 proof should establish the deterministic action transaction/event engine on bounded action types such as:
- movement;
- end activation;
- authored budget-cost action with legality/commit semantics that does not require D-071 awareness/cover logic.

Do not invent attack/damage tuning merely to make D-070 feel complete.

D-071 can consume the D-070 transaction engine when it adds awareness/cover/objective/retreat/AI decision semantics.

If exact post-D-069 authority demonstrates that a minimal attack action is required for D-070 acceptance, record the evidence and update this boundary before implementation.

## 4. Transient state shape

A minimal session should conceptually own:

```text
CombatSession
- encounter_id
- map_id / tactical map reference
- seed / deterministic source identity
- round_index
- activation_index
- event_index
- initiative_order
- active_actor_id
- actors
- committed_events
- encounter_status
```

A minimal actor state should conceptually own:

```text
TacticalActorState
- actor_id
- faction_id
- coord
- facing
- action_budget
- activation_state
- alive/incapacitated state
- encounter-local temporary fields only when required
```

Do not copy full GameState/player/NPC records into combat state.

Adapters/query functions read durable state and authored archetypes; encounter state stores only the transient values needed to execute combat.

## 5. Initiative / round rules

From the approved standard:

- `round_index` starts at 1;
- snapshot eligible actors at round start;
- higher resolved initiative first;
- ties: stable `actor_id` ascending;
- each eligible actor gets at most one normal activation per round;
- mid-round initiative changes affect the next round, not current snapshot;
- actor incapacitated before activation is skipped;
- normal reinforcements join next round;
- no unordered container iteration may decide order.

D-070 does not need free-form delay/reinsert.

## 6. Action budget

Phase-1 default:
- **4 budget units per activation**.

Baseline authored costs come from action definitions; UI will not own costs.

The D-070 engine must prove:
- reset to 4 at activation start;
- no overspending;
- cost paid only after legality;
- zero-cost End Activation does not create budget underflow;
- unused normal budget expires at activation end;
- action budget remains transient.

Reserved-budget reaction mechanics may be represented only to the degree required by the approved state machine, but full reaction triggers/AI should not expand D-070 beyond acceptance.

### CPR-005 / OR-033 deterministic reaction ordering

The Phase-1 scheduler contract is now resolved:
- runtime candidates use encounter-local integer `trigger_priority`;
- omitted priority defaults to `0`;
- higher numeric priority resolves first;
- remaining ties use higher round initiative, then `actor_id` ascending, then `reaction_id` ascending;
- D-070 owns validation/scheduling only; D-071 owns trigger-generation/awareness/AI policy;
- no durable GameState/save-schema field is introduced.

## 7. Movement transaction

Movement commit must reuse D-069 grid/path authority.

Required pattern:
1. validate active actor;
2. validate requested path/end cell against the same authoritative grid query used by preview;
3. snapshot transient state;
4. pay movement action budget cost;
5. update encounter-local coord/occupancy;
6. append one deterministic committed event;
7. on exception/failure, restore the transient snapshot and append no event.

Do not write tactical coordinates to world-map state or GameState.

Preview path queries must:
- be read-only;
- not consume `event_index`;
- use the same legality/path authority as commit.

## 8. Deterministic event key

Approved digest inputs:

```text
state.seed
| encounter_id
| round_index
| activation_index
| event_index
| actor_id
| action_id
| target_key
```

Rules:
- SHA-256 deterministic philosophy;
- `event_index` increments only for committed authoritative resolution events;
- preview queries do not consume event index;
- failed/rolled-back actions do not consume a committed event index;
- identical seed/state/action sequence must yield identical committed event sequence.

D-070-B should hash/normalize the committed transcript from two identical runs and prove equality.

## 9. Activation state machine

Approved states:
- pending;
- active;
- resolving_action;
- waiting_reaction;
- complete;
- skipped.

For the first D-070 slice:
- only active actor initiates normal action;
- end activation explicitly completes actor;
- zero remaining budget may auto-complete when no legal zero-cost action remains;
- incapacitation may skip/end activation;
- after last eligible actor, advance round and snapshot next initiative order.

Do not implement UI state here.

## 10. GameState / persistence boundary

D-070 is transient.

Must prove:
- starting/advancing a combat session does not add tactical fields to GameState;
- previews do not mutate GameState;
- committed transient movement/action events do not mutate durable world state;
- no mid-combat save schema is introduced.

Durable consequences belong to D-072 aftermath.

Bridge/session ownership and save-interruption behavior belong to later integration tasks unless D-070 tests need a minimal pure-Python session owner.

## 11. Recommended implementation surface

Preferred new files:
- `src/textrpg/combat_state.py`
- `src/textrpg/combat_rules.py` only for the bounded turn/action transaction seam if needed;
- `tests/test_combat_state.py`
- `tests/test_combat_turns.py` or equivalent.

Reuse:
- `combat_schema.py`;
- `combat_grid.py`;
- authored action definitions loaded by D-069.

Avoid touching:
- Android/Kotlin;
- persistence schema;
- quest/social aftermath;
- AI modules;
- combat projection;
unless exact D-070 acceptance evidence requires a bounded compatibility change.

## 12. Minimum test matrix

Before D-070 completion prove:

### Session / setup
- deterministic actor initialization;
- duplicate actor IDs reject;
- invalid spawn/occupancy rejects using D-069 authority;
- GameState snapshot unchanged by session construction.

### Initiative / rounds
- initiative descending;
- actor-ID stable tie;
- one normal activation per eligible actor;
- mid-round initiative mutation does not reorder current round;
- incapacitated actor skips;
- round increments after final activation.

### Budget
- activation starts at 4;
- legal action spends exact authored cost;
- insufficient budget rejects without mutation;
- End Activation works with unused budget;
- next actor starts with its own correct budget.

### Movement / action transaction
- legal movement commits authoritative path endpoint;
- illegal movement/path rejects without state mutation;
- preview returns same legal path/decision surface without consuming event index;
- forced failure after snapshot rolls back transient state and event log.

### Determinism
- committed event indices are monotonic;
- preview/failure does not advance committed event index;
- same seed + same initial state + same action sequence => same transcript/events;
- different committed sequence yields appropriately different transcript.

### Durable-state boundary
- no D-070 action adds tactical state to GameState;
- GameState remains unchanged during headless transient proof.

## 13. D-070-B

**Deterministic combat transcript / replay hash**

Recommended normalized transcript fields:
- encounter ID;
- round;
- activation index;
- event index;
- actor ID;
- action ID;
- normalized target key;
- budget before/after;
- coordinate before/after when relevant;
- deterministic event digest.

Run the same scripted encounter twice from identical seed/state and assert:
- exact event sequence equality;
- exact transcript hash equality;
- no preview call changes the hash.

## 14. First commit sequence

After D-069 is truly DONE and D-070 claim is won:

**Commit 1 — transient state**
- session/actor dataclasses;
- setup validation;
- round/initiative snapshot;
- basic state tests.

**Commit 2 — activation/budget**
- activation progression;
- budget legality;
- end activation;
- skip/round advance tests.

**Commit 3 — movement/event transaction**
- reuse D-069 pathing;
- preview vs commit;
- event-index/digest;
- rollback tests.

**Commit 4 — deterministic transcript bonus**
- only after primary acceptance is coherent.

## 15. Exit gate

D-070 is DONE only when:
- D-069 authority merge is the implementation base;
- headless encounter can run deterministic rounds/activations/actions;
- previews do not consume committed event indices;
- failed actions roll back transient state;
- GameState has no tactical schema expansion/mutation;
- full required Python gate is green;
- runtime merge-state policy is satisfied;
- evidence + Learning Record + Coordination FINISH exist.

## 16. Do not start early

Until D-069 is marked DONE:
- do not claim D-070;
- do not create combat_state/runtime code;
- do not modify Veyra's D-069 branch;
- read-only review/preflight is allowed.

When D-069 closes, re-fetch live authority and audit this packet against the merged D-069 API before implementation.
