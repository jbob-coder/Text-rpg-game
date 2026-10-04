# THE GAME — World / Simulation Time & Duration Standard

Status: **ACTIVE TARGET-GAME DESIGN / CURRENT-REALITY MAPPED / NUMERIC BALANCE PARTIAL / IMPLEMENTATION MIGRATION DEFERRED**

Parents:
- `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`
- `docs/systems/GAMEPLAY_SYSTEM_REBUILD_MATRIX.md`
- `docs/systems/PROGRESSION_CLASSES_RANKS_EVOLVED_GAME_DESIGN.md`
- `docs/systems/status/TIME_CAUSAL_STATE_AND_SNAPSHOT_STANDARD.md`
- `docs/systems/status/PASSIVE_CANONICAL_RESOLVER_RANGE_FIXTURE_ELIGIBILITY_AUDIT_WAVE_001.md`

Purpose: define the authoritative time domains used by world simulation, activities, recovery, travel, conditions, NPC schedules, tactical encounters, temporal abilities, save/load, and future numeric calibration.

This document deliberately separates **CURRENT REALITY** from the **EVOLVED TARGET**.

---

# 1. CURRENT REALITY — durable time state

Current `GameState` stores:

- `turn: int = 0`;
- `time_minutes: int = 0`.

Current validation requires both to be:
- integers;
- non-boolean;
- non-negative.

Current save schema version 1 serializes `time_minutes` and `turn` as durable authoritative state.

No current durable field defines:
- calendar date;
- hour-of-day;
- day index;
- season;
- timezone;
- sub-minute world time;
- NPC schedule clock;
- tactical elapsed seconds.

These are not current implementation facts and must not be inferred.

# 2. CURRENT REALITY — time advancement

Current `advance_time(state, minutes)`:
- accepts integer minutes >= 0;
- validates current `state.time_minutes`;
- validates timed-condition records before mutation;
- increments `state.time_minutes` atomically after preflight;
- decrements condition `duration_minutes`;
- removes timed conditions whose remaining duration reaches zero;
- returns the IDs of expired conditions.

Current `validate_time_advance` performs the same temporal preflight without mutating state.

Current `advance_time` does **not** by itself:
- move NPCs;
- advance quests;
- run schedules;
- regenerate resources;
- simulate economy;
- execute travel;
- create encounters;
- update weather;
- advance combat initiative.

Those systems would need explicit integration.

# 3. CURRENT REALITY — authored choice time

Current authored choices may contain:

`time_cost_minutes`

Current rules:
- default is 0;
- value must be a non-negative integer;
- time advance is preflighted before mutation;
- outcome effects are applied;
- then authored time cost is advanced;
- then `turn` increments;
- history records resulting `time_minutes`.

Therefore current `turn` and `time_minutes` are distinct:
- a zero-minute choice can increment `turn`;
- elapsed minutes can increase by different amounts per choice.

Do not treat `turn` as elapsed time.

# 4. CURRENT REALITY — timed conditions

Current condition records may contain:
- `duration_minutes`;
- `applied_at = state.time_minutes`.

Current durations:
- are integer minutes;
- may be absent for non-timed conditions;
- count down only when authoritative time advancement runs.

Current edge case:
a condition can currently be authored with `duration_minutes = 0` and exists until a time-advance operation processes it.

Target design should not rely on that ambiguity.

# 5. CURRENT REALITY — training and recovery

Current simulation uses minutes directly.

Current skill training:
- requires >= 1 minute;
- spends Stamina and Focus according to current implementation formulas;
- advances `time_minutes`.

Current attribute training:
- requires >= 120 minutes;
- advances `time_minutes`.

Current recovery:
- accepts integer minutes >= 0;
- calculates current resource recovery from elapsed hours and quality;
- then advances `time_minutes`.

These formulas are current implementation evidence, not automatically final target balance.

# 6. CURRENT REALITY — persistence

Schema-v1 save/load persists `time_minutes`.

Validation rejects:
- negative values;
- booleans;
- non-integers.

No explicit migration currently exists from `time_minutes` to a richer calendar clock.

Therefore any replacement or reinterpretation requires an explicit save migration.

---

# 7. EVOLVED TARGET — one authoritative durable world clock

THE GAME retains one authoritative monotonic durable world-time axis.

For compatibility, the target design preserves the semantic role of current `time_minutes`:

> elapsed authoritative world-simulation minutes from the campaign/save epoch.

Until an explicit schema migration is approved:
- `time_minutes` remains the durable coarse world-time field;
- it never moves backward through ordinary gameplay;
- UI clocks/calendars derive from it rather than owning time.

A later calendar can project:
- day;
- hour;
- date;
- season;
- local cultural calendar

from the authoritative elapsed-time state plus world calendar rules.

Calendar presentation must not become the underlying authority.

# 8. Time domains

The target game distinguishes at least five time domains.

## 8.1 WORLD_TIME

Durable, monotonic, simulation-wide elapsed time.

Uses:
- training;
- work;
- travel;
- recovery;
- sleep;
- schedules;
- quest deadlines;
- condition duration;
- world events;
- long-form crafting/research;
- persistence.

Current backing field:
`GameState.time_minutes`.

## 8.2 EVENT_ORDER

Stable ordering for multiple authoritative events that can occur at the same world minute.

Purpose:
- remove ambiguity among zero-duration or same-minute events;
- support deterministic history;
- support causal snapshots;
- support save/load deduplication.

The final runtime representation is `TBD`.

It may be:
- monotonic event sequence;
- transaction sequence;
- another deterministic ordering key.

Do not overload `turn` as the universal event-order authority because current `turn` advances on authored choices, not every state transition.

## 8.3 ENCOUNTER_TIME

Local tactical/encounter timing used for:
- action budget;
- initiative;
- movement;
- attacks;
- reactions;
- short ability durations;
- process-rate effects.

Exact tactical time model is still open because the combat turn/activation model is unresolved.

Encounter time:
- must not replace WORLD_TIME;
- may use turns, phases, action units, seconds, ticks, or another tested representation;
- must define how elapsed encounter duration commits back to WORLD_TIME.

## 8.4 PROCESS_TIME

Local duration/progress for one process:
- crafting step;
- channel;
- sustained ability;
- loading operation;
- repair procedure;
- gate startup;
- recovery window.

A process has:
- start authority;
- duration/progress rule;
- interruption behavior;
- completion state.

Process time may be driven by WORLD_TIME or ENCOUNTER_TIME depending context.

## 8.5 SUBJECTIVE_TIME

Character-internal processing experience.

Primary current use:
- Time Partition.

SUBJECTIVE_TIME:
- does not advance WORLD_TIME independently;
- does not create extra world events;
- does not create extra physical actions;
- may change subjective planning/processing according to its ability law.

# 9. Canonical time unit policy

For durable strategic/world simulation:

**one authoritative unit = one integer world minute.**

This is both:
- current implementation reality;
- preserved target compatibility decision.

This does not mean every gameplay action lasts at least one minute.

Sub-minute tactical/action behavior belongs to ENCOUNTER_TIME / PROCESS_TIME and is reconciled into WORLD_TIME through an explicit commit policy.

Benefits:
- save compatibility;
- deterministic activity accounting;
- human-readable schedules;
- no floating-point drift in long world simulation;
- simple deadline and condition arithmetic.

# 10. Sub-minute action policy

The target game may contain actions shorter than one minute.

Rules:
1. do not repeatedly round every short action to one world minute;
2. resolve short actions inside ENCOUNTER_TIME or PROCESS_TIME;
3. accumulate/reconcile elapsed encounter/process duration;
4. commit world-minute advancement through one documented boundary;
5. preserve deterministic rounding/remainder behavior.

Exact remainder/rounding representation is `TBD`.

It must be chosen before tactical encounter duration becomes implementation-ready.

# 11. Zero-duration events

Zero-world-minute events are allowed when they represent:
- bookkeeping;
- instantaneous state acknowledgement;
- UI-independent authoritative choices that legitimately consume no strategic time;
- same-minute event sequencing.

They still require deterministic EVENT_ORDER.

A zero-duration event must not:
- bypass cooldowns by repeated spam;
- farm passive qualification;
- reset activity windows;
- duplicate rewards;
- avoid schedule/deadline consequences that should require elapsed time.

# 12. Time transaction

Every authoritative time-advancing operation should eventually resolve as one transaction containing:

- transaction/event ID;
- source action/activity;
- start WORLD_TIME;
- requested duration;
- accepted duration;
- end WORLD_TIME;
- affected timed processes/conditions;
- interruption/failure state;
- resulting world events;
- save/schema version.

The current implementation already preflights timed-condition validity before time mutation.

The evolved target generalizes this discipline to all world-time consumers.

# 13. Atomicity

A failed time-advancing transaction must not partially advance the world.

Required pattern:
1. validate requested duration;
2. validate dependent time-sensitive state;
3. validate costs/prerequisites;
4. capture rollback/transaction state where needed;
5. commit authoritative effects;
6. advance/process time;
7. run scheduled consequences;
8. persist event/history state.

Exact ordering can vary by activity, but partial time mutation followed by failed action commit is not acceptable.

# 14. Timed-condition target rule

Target timed conditions should use one of two explicit forms:

### REMAINING_DURATION
Store bounded remaining duration and decrement through time processing.

### EXPIRY_TIME
Store absolute expiry WORLD_TIME.

A final implementation may choose one as canonical.

Do not mix both without a reconciliation rule.

For reconstruction, every timed condition must define:
- start time;
- duration or expiry;
- pause behavior if any;
- encounter/world-time domain;
- expiration event;
- save/load behavior.

# 15. Zero-duration condition rule

Target rule:

A timed condition with zero duration should not persist ambiguously.

Before implementation, choose one explicit behavior:
- reject zero-duration timed conditions; or
- treat them as immediate event effects and never persist them as active timed conditions.

Current schema behavior is preserved as a documented legacy edge case, not a target feature.

# 16. Activity duration

Every time-consuming activity eventually needs:
- activity ID;
- start location;
- start WORLD_TIME;
- requested/planned duration;
- minimum valid duration;
- interruption policy;
- costs;
- outputs;
- schedule/world consequences;
- completion state.

Examples:
- training;
- work;
- study;
- repair;
- research;
- sleep;
- medical recovery;
- travel.

Duration is not merely flavor text; it is an authoritative balance input.

# 17. Training-time rule

Training keeps world-time cost as a defining design principle.

Target training must:
- consume WORLD_TIME;
- obey activity minimums where authored;
- consume resources through authoritative resource transactions;
- interact with schedules/locations/mentors/facilities;
- support interruption;
- not grant full completion output if the required duration did not occur.

Current 1-minute skill minimum and 120-minute attribute-training minimum are implementation facts, not locked final balance.

# 18. Recovery-time rule

Recovery is time-dependent.

Target recovery must:
- use authoritative elapsed duration;
- respect core-resource maxima;
- respect blocking conditions;
- support sleep/rest/environment/medical context;
- avoid duplicate recovery on save/load;
- distinguish opportunity, rate, and cap.

Current linear hourly recovery coefficients are implementation facts, not locked target values.

# 19. Travel-time rule

Travel must consume WORLD_TIME when the world model says travel takes time.

Travel time may depend on:
- authored route cost;
- movement/travel system;
- terrain;
- load;
- conditions;
- interruptions;
- transport.

Existing Gate Twelve route-minute content can serve as content-specific regression evidence.

Map/presentation coordinates are not automatically physical distance units.

# 20. NPC schedule rule

Future NPC schedules require WORLD_TIME-derived schedule position.

A schedule system must define:
- schedule period;
- location/action entries;
- travel transitions;
- exceptions;
- injury/emergency overrides;
- quest/faction overrides;
- off-screen simulation granularity.

NPC schedules must not use device wall-clock time as gameplay authority.

# 21. Quest and event deadlines

Future deadline records should use:
- absolute WORLD_TIME deadline; or
- explicit remaining duration anchored to a start event.

Deadline state must persist.

Reload cannot extend a deadline unless a deliberate rollback/time-reversal mechanic explicitly owns that state.

# 22. Tactical encounter reconciliation

Combat currently has no final turn/time model.

Future encounters must define:
- local encounter start WORLD_TIME;
- local timing model;
- whether WORLD_TIME is frozen until encounter commit or advanced incrementally;
- how encounter duration maps back to world minutes;
- handling of interruptions/reinforcements/schedules;
- save/load policy.

One encounter must not advance world time once per UI animation.

# 23. Temporal ability boundary

## Temporal Drag
Changes bounded local process rate.

It does not decrement WORLD_TIME or move the global clock backward.

## Time Partition
Changes subjective processing.

It does not grant extra WORLD_TIME.

## Causal Mark
Restores approved property state at current WORLD_TIME.

## Event Reversal
Restores eligible physical snapshot state at current WORLD_TIME.

No current temporal ability rewinds the authoritative campaign clock itself.

# 24. Event Reversal and history

Restoring a physical snapshot does not erase:
- history log by default;
- learned knowledge;
- Status progression;
- world-time passage;
- unrelated quest/faction state.

If a future mechanic can alter world-time history itself, it requires a new upper-level time law and save architecture.

# 25. Save/load

Persist:
- WORLD_TIME;
- enough EVENT_ORDER state to avoid duplicate transactions once implemented;
- active timed conditions/processes;
- activity/travel state;
- schedule-critical state;
- temporal-ability snapshots;
- committed transaction IDs where deduplication is required.

Loading must not:
- rewind elapsed world time unintentionally;
- duplicate recovery/training/travel;
- reset deadlines;
- replay committed expiry events;
- reroll committed stochastic events.

# 26. Offline / real-device time

Device wall-clock time is not gameplay WORLD_TIME by default.

The game must not grant:
- training;
- recovery;
- income;
- NPC schedule progression;
- deadline changes

merely because the app was closed for real-world hours unless an explicit offline-progression feature is later designed.

This preserves deterministic/seedable simulation and prevents clock manipulation.

# 27. Calendar projection

A future calendar may define:
- campaign epoch;
- day length;
- named weekdays/months/seasons if the setting needs them.

Until authored:
- `time_minutes` is elapsed simulation time only;
- no Earth calendar mapping is implied;
- no local timezone is relevant to gameplay state.

# 28. Numeric calibration dependency

This standard resolves the **time-domain semantics prerequisite** for passive range-fixture work.

It does not yet provide:
- core-resource ranges;
- action-time ranges;
- travel speed ranges;
- fatigue curves;
- sleep-duration bands;
- tactical action duration.

Therefore time-dependent passive resolvers remain short of `RANGE_FIXTURES_READY` until their parent systems provide those ranges.

# 29. Required tests

Current-compatibility tests:
- negative/non-integer/bool `time_minutes` rejected;
- `advance_time` expires timed conditions correctly;
- failed preflight does not mutate time;
- training/recovery advance time once;
- save/load round-trips `time_minutes`.

Target tests:
- zero-duration events receive deterministic ordering;
- time transaction cannot commit twice;
- same-minute events are ordered deterministically;
- deadlines survive save/load;
- timed processes resume deterministically;
- tactical encounter commits elapsed world time once;
- device-clock changes do not alter WORLD_TIME;
- Time Partition does not advance world time;
- Temporal Drag does not reverse world time;
- Event Reversal does not rewind campaign WORLD_TIME.

# 30. Reconstruction acceptance

A future developer/agent should be able to answer:
- which clock is durable authority;
- what unit it uses;
- why turns are not time;
- how sub-minute encounters coexist with minute-level world time;
- how timed conditions expire;
- how schedules/deadlines derive from world time;
- how save/load avoids duplicate time consequences;
- how temporal abilities interact with the clock.

This standard changes no runtime code and performs no save migration.
