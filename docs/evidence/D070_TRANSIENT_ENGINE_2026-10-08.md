# D-070 — Transient tactical engine continuation

**Owner:** Silex
**Status:** LOCAL PASS / PR MERGE-STATE GATE PENDING
**Authority base:** `8125406c69e2b89f720628d91cb2e067ab3496b5`
**Task branch:** `agent/silex-d070-transient-engine`
**Preserved predecessor:** Veyra PR #77 / `05c0886f45e8acd6bdd9a1a32c938adbd087eb1f`

## Scope and provenance

Retained the predecessor's transient actor/session, activation budget, movement,
reserve lifecycle, reinforcement and transcript implementation, plus its 28 tests.
Only its five D-070 files were carried onto current authority. The preflight was
reconciled with live CPR-005 / OR-033; old ownership text was not retained.

Silex completed reaction scheduling and repaired evidenced lifecycle, seed,
round-transition and transcript defects. Production changes are limited to
`src/textrpg/combat_state.py` and its exports in `src/textrpg/__init__.py`.
D-069 grid/schema, durable GameState, persistence, content and Android are unchanged.

## Reproduced problems and repairs

| Problem observed in preserved code | Causal repair and regression |
| --- | --- |
| No reaction candidate/scheduler despite resolved OR-033 | Frozen `ReactionCandidate` validates integer priority (excluding bool); `order_reactions` sorts by descending priority, frozen round initiative, actor ID, reaction ID. All 120 permutations produce the same queue. |
| Active incapacitated actors could move, prepare and end; advancement could stall | Action boundaries reject incapacitation. The next activation transition skips the actor, expires normal/reserved budget and proceeds without a phantom event. |
| Stale reactions could consume reserves after incapacitation | Consumption rechecks live incapacity, round membership and matching reserve. Queue ordering does not grant permission to fire. |
| Resolved encounters still accepted mutations | Common active-encounter guard covers actions, reaction consumption, activation/round progression and reinforcements. |
| Combat constructor rejected canonical `GameState.seed: str` | Accept nonempty string seeds directly, retaining integer fixtures; exact digest uses the supplied source seed. |
| Invalid mid-round initiative poisoned the next snapshot or partially advanced the round | Validate and build the next initiative snapshot before committing round/state changes. |
| Movement after preparing a reaction logged reserve 0 -> 0 while reserve remained 1 | Movement events record the actual unchanged reserve. |

The first added regression run was RED: 74 tactical tests, 12 failing subtests and
6 errors (missing APIs, rejected canonical seed, lifecycle violations). The second
transaction-focused RED run reproduced 4 failures and 1 error for reserve reporting
and invalid next-round initiative. The final full suite passes with the repairs.

## Executed local verification

- Preserved baseline: `PYTHONPATH=src python -m unittest discover -s tests -v` — **430 PASS**.
- Final complete suite, same command — **442 PASS**, Python 3.12.14.
- The 40 D-070 tests include the 28 preserved tests and 12 continuation tests.
- Fault injection raises **after** event append for Move, Sprint, prepare, consume
  and End Activation; actor state, budget, reserves, event log and index roll back.
- Sprint accepts 10 traversal points and rejects 11 without a commit.
- Scripted runs use the durable string seed, movement, prepare/end/consume,
  reinforcement and a second round. Extra previews leave events and transcript
  hash identical; serialized GameState remains byte-for-byte unchanged.

Local logs are session evidence; the committed regressions and PR workflow are
reproducible durable proof. CI must still verify Python 3.10 and the existing
Android build/unit/emulator/screenshot gates before this task is marked DONE.

## API handoff and limits

`order_reactions(candidates)` returns a read-only ordered tuple, rejecting actors
outside the current round snapshot. It does not generate triggers or execute
attack effects. D-071 must recheck trigger-specific legality before calling
`consume_reaction`; that commit independently rechecks live session/actor/reserve
legality. Multiple proposals for one actor cannot spend its reserve twice.

Initiative updates take effect next round. Incapacitation set by a later effect
immediately prevents further actions; `begin_next_activation` cleans up the ended
turn. Normal reinforcements enter the next round, with occupancy rechecked before
round advancement. The public `complete_active_activation` is a low-level scheduler
operation; authored End Activation should use `commit_end_activation` to log it.

D-070-B supplies normalized event transcripts and SHA-256 replay comparison, not
mid-combat persistence or a transcript deserializer. D-071 owns awareness, cover,
objectives, retreat and AI; D-072 owns durable aftermath; later tasks own bridge/UI.
No physical-device or playable tactical Android encounter claim is made here.
