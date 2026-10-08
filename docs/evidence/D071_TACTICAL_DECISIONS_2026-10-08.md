# D-071 — Knowledge-correct tactical decisions

**Owner:** Silex
**Status:** DONE / REQUIRED MERGE-STATE GATE PASS
**Authority base:** `5a36915c6884b68b78687e34f896f2aec70b32c3`
**Claim:** `63d8b4a87912c28a42f45fd6fd404af2f98cbe25`
**Branch:** `agent/silex-d071-tactical-decisions`

## Implemented boundary

- `combat_knowledge.py`: observer-specific UNKNOWN/SUSPECTED/DETECTED/IDENTIFIED
  contacts; explicitly supplied known identity; stale positions; knowledge-safe
  actor/cell targeting and movement previews; directional +0/+10/+20 cover;
  allowlisted player view without raw actor IDs, AI internals or unknown hazards.
- `combat_rules.py`: typed objectives for the eight Phase 1 objective kinds;
  actor loadouts; deterministic detection using resolved perception/stealth inputs;
  objective interaction, movement, round and exit-only retreat transactions.
- `combat_ai.py`: bounded candidate generation, stable utility/tie selection,
  cautious/aggressive/companion/beast doctrine, and HOLD/ADVANCE/FOCUS_TARGET/
  ASSIST/WITHDRAW orders. Orders affect utility, not action legality.
- `combat_state.py`: one transient `withdrawn` flag excludes departed actors from
  occupancy, future initiative and normal/reaction action authority. D-069 geometry,
  durable state/save, content and Android code remain unchanged.

The controller consumes D-069 geometry and D-070 transactions. Integration must
use `EncounterRules.commit_movement` so movement-triggered awareness and objective
updates participate in the same rollback boundary. The lower-level session API
remains available for scheduler work and its existing tests.

## Contract and tuning choices

Authorities: LOS/Detection & Combat Knowledge; Directional Cover & Terrain;
Combat AI/Objectives/Retreat; Turn/Initiative; Phase 1 Combat Migration packet.

Detection is an event-keyed deterministic contest, not geometric LOS alone.
The bounded default is perception - stealth - Manhattan distance - concealment,
plus SHA-256 variance in [-10,+10]. `DetectionStats` accepts already resolved
values, with a configurable sight range (default 6); it does not recompute player
or NPC stats. Movement resolves each live observer's checks under its committed
event identity. An explicitly authored scan may use its own action range/cost.
These are initial tuning defaults, not invented NPC canon or an attack formula.

Known identities must be passed as typed `KnownIdentity` values derived from
existing durable knowledge. Detection alone does not identify a stranger. A lost
contact retains its last known coordinate/round. Blind area targeting returns no
unseen cover detail, and actor targeting never substitutes a hidden current
position for last-known knowledge.

AI considers at most 16 authored actions per actor, prunes movement to 24 visible
destinations by default, and returns at most 64 candidates (configurable downward).
End Activation is retained as a zero-cost fallback. Objective completion scores
+1000, withdrawal progress +800, and useful movement +5 per cell. Known cover
contributes at most +100. Legal target pressure is a simple doctrine heuristic
(40 cautious/companion, 80 aggressive, 50 beast), **not expected damage**. Stable
selection ties use action ID, target key, then path key. There is no Monte Carlo
search or wall-clock random source. D-078 still owns measured handset budgets.

The AI outputs a legal decision package; callers revalidate at commit. Movement,
interaction and retreat have executable commits here. Authored attack/ability
effect sources, balancing and their bridge dispatch remain later integration
work; no playable tactical Android encounter is claimed by this task.

## Executed local verification

`PYTHONPATH=src python -m unittest discover -s tests -v`

**478 tests PASS** on Python 3.12.14, including **36 new D-071 tests**:
10 knowledge, 16 objective/transaction and 10 AI tests. The previous 442 tests are
retained. Tests were added before each new module and the observed defect repairs.

Verified examples:
- LOS alone does not identify/reveal a contact; identities are an explicit
  allowlist; separate observers retain separate knowledge.
- Hidden and nonexistent actor targets fail identically; stale contacts cannot
  reveal a moved actor; hidden occupancy does not alter safe movement previews.
- Unknown enemy locations and unknown hazards do not change AI candidates or
  choices; a focus order cannot make a hidden actor targetable.
- Objective movement, observation + escape, exit-only retreat, survival, protection,
  elimination, disabling and incapacitated capture execute their own conditions.
- Retreat removes occupancy and future action/reaction authority. Ending views
  remain available, and departed observers cannot break later movement.
- Failure after append, or after observation mutation, restores actor/session,
  event sequence, knowledge and objective state. Previews consume no event.
- Enemy movement performs observer-specific detection within the movement event;
  arrived reinforcements do not crash observers without a specialized stat binding.
- Doctrine and orders change ranking without granting illegal candidates; stable
  input permutations keep the decision fixed; the configured candidate cap holds.
- Developer diagnostics and private objectives are absent from the safe view.

The code audit reproduced and repaired an unseen-cover preview leak, two
post-retreat observer/view errors, missing movement-driven detection, a missing
reinforcement stat fallback, and a doctrine field that initially did not change
ranking. These were local implementation defects inside D-071, not a new contract
or a temporary workaround. Committed regressions retain their reproductions.

## Handoff limits

D-072 owns durable aftermath and recovery. D-073 owns canonical/proposed content
materialization and Python bridge dispatch; it must bind action loadouts, resolved
stats and existing knowledge, map contact tokens safely, and consume the explicit
safe view. D-074 owns Android tactical consumers. D-071 does not add tactical save
fields, fabricate canon opponents/weapons, or claim physical-device acceptance.

Developer diagnostics are implemented and excluded from the headless safe view.
**D-071-B is not claimed/scored:** the bonus's final bridge-projection exclusion
proof awaits D-073's actual tactical bridge integration.

Required Python 3.10 / Android unit-build-package / emulator-screenshot PR merge-state CI passed as recorded below.

## Final integration evidence

- Candidate: `87412926c12afd2a37be154913361ecf05a8b84d`; tested base: `5a36915c6884b68b78687e34f896f2aec70b32c3`.
- Tested PR merge: `53e4b90a63b83b77e4b3b0adfcf1f7546e0bf33b`.
- PR #79 / workflow #404 `37774598150`; Python 478/478 PASS; Android unit/build/package PASS; emulator 35/35 PASS; screenshot gate PASS.
- Workflow: https://github.com/jbob-coder/Text-rpg-game/actions/runs/37774598150.
- APK SHA-256: `63d23d717eea3dbf64ecb9adea78b264fff4d5252529494b11f388652d373cbd`; APK artifact `11548967832`; UI-QA artifact `11549083410`.
- CI artifact retention is short; identifiers/hashes remain provenance after expiry.
- Resulting authority merge: `ffea9fcd4e0826b54c766b2e1c06468fb3afcbe7`; completed `2026-10-08T08:16:53-04:00`.
- Fresh merge checks retained the tested base/candidate, and resulting authority tree matched the verified candidate. No compatibility repair or main promotion.

D-071 primary acceptance is complete. D-072 is READY; D-071-B remains unclaimed.
