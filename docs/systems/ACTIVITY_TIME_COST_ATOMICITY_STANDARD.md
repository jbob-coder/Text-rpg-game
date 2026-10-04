# THE GAME — Activity Time, Cost & Atomicity Standard

Status: **APPROVED FIRST-PASS V10 CONTRACT / CURRENT PRIMITIVES EXIST**
Parent:
- docs/systems/PLAYER_ACTIVITIES_AND_LIFE_LOOP_MASTER_PLAN.md
Current source:
- src/textrpg/simulation.py
- src/textrpg/core.py

## 1. Purpose

Define how activities consume world time/resources and guarantee that failed activity resolution cannot leave partial mutation.

## 2. Time authority

GameState.time_minutes remains the authoritative world-time scalar for current scope.

No UI timer owns gameplay time.

Calendar/date layers may later derive from this authority.

## 3. Duration

Activity duration is an integer number of world minutes for Phase 1.

Reject:
- booleans;
- negative values;
- non-integers.

Immediate activities may use zero minutes only when design explicitly allows it.

## 4. Cost classes

Possible costs:
- world time;
- stamina;
- focus;
- resolve;
- ability-specific resource;
- item quantity;
- currency when economy exists;
- durability when approved;
- opportunity/schedule slot.

Every cost must have an owning system.

## 5. Validation-before-commit

Before mutating:
1. validate activity definition;
2. validate time advance;
3. validate resource containers;
4. validate resource/item sufficiency;
5. validate output destination;
6. snapshot touched durable state;
7. resolve;
8. validate resulting state;
9. append history;
10. commit.

On failure restore the snapshot.

## 6. Current transaction evidence

Current simulation.train already protects against leaving resource normalization behind when training fails from insufficient resources.

Current time advancement preflights timed-condition structure before committing.

These patterns should be generalized rather than replaced.

## 7. Time already spent

For an atomic activity:
- either the activity completes and full time/cost commits;
- or it fails before commit and no time/cost commits.

For interruptible/resumable activities:
- elapsed time may remain spent;
- partial costs/progress follow explicit interruption policy.

Do not mix the two models implicitly.

## 8. Resource clamping

Resource costs cannot produce invalid negative resources.

Recovery cannot exceed authoritative maxima.

Modifiers/maxima come from rules layer, not UI.

## 9. History event

Each completed meaningful activity should be able to record:
- activity_id/type;
- start/end time;
- location;
- participants;
- costs;
- major outputs;
- source/content ID.

History is audit/reconstruction evidence, not a substitute for domain state.

## 10. Deterministic variance

If an activity uses uncertainty:
- seed it from stable state/event identity;
- never use wall-clock randomness;
- store enough event context for test replay.

Many training/recovery activities should remain deterministic.

## 11. Conditions

Advancing time may expire timed conditions.

The activity transaction must account for condition expiry and must not lose expiry events silently.

If an activity is illegal under a condition, validate before time passes.

## 12. Cross-domain outputs

If one activity affects multiple domains, either:
- use one atomic transaction;
- or use an explicit saga/compensating design with safe checkpoints.

Phase 1 should prefer one atomic transaction.

## 13. Android behavior

UI:
- asks for availability;
- displays duration/cost;
- requests start;
- waits for authoritative result;
- renders new snapshot.

UI never decrements resources optimistically as gameplay truth.

## 14. Tests

Required:
- invalid duration;
- insufficient resource no mutation;
- time + output commit together;
- condition expiry;
- resource floor/cap;
- deterministic uncertainty;
- rollback across multi-domain effect;
- history record;
- save/load after activity.

## 15. Phase 1 defaults

Trace Chamber practice/training/recovery should use existing current durations/costs where authored.

Do not retune current values merely to fit a generic activity abstraction.
