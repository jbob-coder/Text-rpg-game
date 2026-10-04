# THE GAME — Trace Chamber Phase 1 Activity Proof Packet

Status: **CURRENT-FACT AUDIT + PHASE 1 ACTIVITY PROOF / NO RUNTIME CHANGE**
Parent:
- docs/systems/PLAYER_ACTIVITIES_AND_LIFE_LOOP_MASTER_PLAN.md
Current source:
- content/vertical_slice_01.json
- src/textrpg/simulation.py
- src/textrpg/powers.py

## 1. Purpose

Identify the existing Trace Chamber activity loop as the first Phase 1 proof for requirement #8: one life/activity action that consumes time/resources, creates persistent progress, and integrates with another domain.

No new activity is invented for this proof.

## 2. Current location

Current location:
- TRACE_CHAMBER.

Current description:
- controlled space used to reproduce and stabilize Trace Echo.

The location already has a coherent specialist function: training/research/recovery.

## 3. Current proof action

Preferred Phase 1 activity proof:
- choice ID TRAIN_POWER_FUNDAMENTALS_TWO_HOURS.

Current authored effect:
- skill_train;
- skill = powers;
- minutes = 120;
- intensity = 1.

This routes into the current authoritative training primitive.

## 4. Why this satisfies the activity concept

The action:
- occurs at an authored specialist location;
- consumes two world hours;
- uses authoritative skill training;
- consumes authoritative training resources through simulation rules;
- advances a persistent skill;
- interacts with progression;
- is not UI-owned.

It is therefore a stronger Phase 1 proof than inventing a new job/work mechanic.

## 5. Other current Trace activities

Current content also includes:
- PRACTICE_SIGNAL_PULSE_ONE_HOUR;
- PRACTICE_SIGNAL_PULSE_TWO_HOURS;
- RECOVER_EIGHT_HOURS;
- ANALYZE_STABLE_TRACE_PATTERN;
- COMPLETE_TRACE_TOLERANCE_PROTOCOL;
- TRY_DIRECTIONAL_TRACE_ON_SERVICE_FORK;
- Trace Resonance recovery actions.

These provide a small activity family rather than one isolated button.

## 6. Current training source behavior

simulation.train validates:
- known skill;
- integer duration;
- intensity bounds;
- time-advance legality;
- mutable skill/resources state;
- existing skill range;
- resource availability.

It restores resource state when insufficient resource causes failure after normalization.

The final Phase 1 verification should preserve this atomicity.

## 7. Phase 1 acceptance criteria

Requirement #8 is implementation-verified when the selected Phase 1 head proves:

1. Jack reaches Trace Chamber through legitimate content state;
2. TRAIN_POWER_FUNDAMENTALS_TWO_HOURS is available only in the authored context;
3. start skill value is captured;
4. start world time/resources are captured;
5. action executes through authoritative engine;
6. world time advances by the authored/training duration exactly once;
7. stamina/focus/resource costs are applied by the engine;
8. powers skill increases according to current formula/cap;
9. history/state is valid;
10. save;
11. load;
12. skill/time/resources remain identical after load;
13. Android merely presents/request the action and does not duplicate arithmetic.

## 8. Failure fixture

Test an insufficient-resource case:
- training request is rejected;
- world time does not advance;
- skill does not change;
- resource normalization does not leak mutation;
- player receives safe failure reason.

## 9. Condition interaction

Add a regression where a malformed/timed condition state causes preflight failure or expiry according to current time rules.

Do not let activity partially commit before condition/time validation.

## 10. Progression integration

The activity proves the bridge:
location/content -> timed activity -> skill progression -> resource cost -> world time -> save/load.

It does not define:
- class advancement;
- profession;
- rank;
- global Level;
- all progression UI.

Those remain separate authorities.

## 11. Research/practice follow-up

The same Phase 1 region can later prove:
- technique practice;
- knowledge research;
- recovery;
without introducing a new activity scheduler.

These should be added only if they help integrated gameplay rather than quota counting.

## 12. UI relationship

During current planning phase, UI requirements are minimal:
- show activity label;
- show duration;
- show known requirements/cost;
- issue engine request;
- refresh snapshot;
- show safe result.

Final Activity UI refinement remains deferred with V11.

## 13. Performance

Atomic engine resolution is cheap enough for the low-end target.

No background timers, offline simulation, or per-frame training logic are needed.

## 14. Current status

Documentation:
- activity schema: ready;
- time/cost atomicity: ready;
- training/practice: ready;
- recovery: ready;
- interruption/concurrency: ready;
- Trace Chamber proof packet: ready.

Runtime foundation:
- train/recover/power-practice primitives exist;
- current content actions exist.

Remaining:
- exact-head Phase 1 regression execution;
- final migration/consumer map if activity projection is normalized;
- Android proof on target integration branch.

## 15. Phase 1 impact

Requirement #8 moves to:
**CURRENT RUNTIME FOUNDATION EXISTS / DOCUMENTATION-READY / FINAL EXACT-HEAD VERIFICATION PENDING.**

No new gameplay behavior is claimed by this documentation packet.
