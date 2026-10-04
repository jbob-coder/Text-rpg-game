# THE GAME — World-Time Parent Fixture Batch 001

Status: **PHASE-C PARENT-SCALE PREPARATION / TIME SEMANTICS READY / NO FINAL ACTIVITY RANGES / NOT IMPLEMENTED**

Parent:
- `WORLD_SIMULATION_TIME_AND_DURATION_STANDARD.md`

Purpose: provide deterministic qualitative fixtures for the authoritative world-time layer so resource, activity, travel, schedule, condition, and temporal-ability systems can depend on one time contract.

## Readiness result

World-time semantics:
`SEMANTIC_AUTHORITY_READY`.

Durable strategic time unit:
integer world minute.

Still open:
- tactical/sub-minute remainder representation;
- final activity duration ranges;
- travel speeds;
- sleep duration bands;
- combat encounter elapsed-time mapping.

These open values do not invalidate the clock semantics.

## FIX_TIME_001 — Monotonic advance

Start:
`WORLD_TIME = T`.

Apply valid duration `D >= 0`.

Required:
`WORLD_TIME_after = T + D`.

Ordinary gameplay must never produce:
`WORLD_TIME_after < T`.

## FIX_TIME_002 — Zero-duration authoritative event

Start:
`WORLD_TIME = T`.

Commit two valid zero-duration events.

Required:
- both events remain at world minute `T`;
- deterministic EVENT_ORDER distinguishes them;
- no cooldown/window/qualification system may use identical minute alone as proof that they are the same event.

## FIX_TIME_003 — Invalid advance preflight

Given corrupt timed state or invalid duration:

Required:
- transaction rejects;
- WORLD_TIME unchanged;
- timed conditions unchanged;
- resource/activity outputs unchanged.

This preserves the current atomic preflight behavior as a target principle.

## FIX_TIME_004 — Timed-condition expiry

Condition begins with valid duration `D`.

Advance by `D-1` where valid:
- condition remains active.

Advance remaining minute:
- condition expires exactly once;
- expiry consequence commits once.

## FIX_TIME_005 — Same-minute ordering

Two authoritative transactions occur with zero elapsed minutes between them.

Required:
- history/event ordering is deterministic;
- snapshots/evidence can identify which occurred first;
- save/load preserves that order.

Final EVENT_ORDER representation remains open.

## FIX_TIME_006 — Choice/action with elapsed time

An authored world action has duration `D`.

Required:
- prerequisite/time preflight occurs before commit;
- state outcome and elapsed time commit as one logical transaction;
- world time advances once;
- history records end time.

## FIX_TIME_007 — Activity interruption

A planned activity duration is longer than actual completed time.

Required:
- only authoritative elapsed duration advances WORLD_TIME;
- output reflects completed portion according to activity law;
- no full-duration reward from an interrupted short session unless explicitly authored.

## FIX_TIME_008 — Recovery transaction

A valid recovery action consumes elapsed world time.

Required:
- recovery resolves against the correct pre/post resource state;
- time advances once;
- reload does not repeat recovery.

## FIX_TIME_009 — Deadline

Deadline is anchored to absolute WORLD_TIME.

Required:
- ordinary time advancement approaches/passes deadline deterministically;
- save/load preserves deadline;
- app/device wall-clock does not move it.

## FIX_TIME_010 — NPC schedule projection

Given schedule data and WORLD_TIME:

Required:
- schedule state derives from authoritative simulation time;
- reopening UI produces same NPC schedule state for unchanged game state;
- device clock has no authority.

## FIX_TIME_011 — Travel

Travel transaction has an authoritative duration from the travel system.

Required:
- world time advances exactly by accepted travel duration;
- map animation length does not determine game time;
- repeated UI transition cannot duplicate elapsed time.

## FIX_TIME_012 — Tactical encounter reconciliation

Encounter starts at WORLD_TIME `T`.

Local encounter uses its own timing domain.

Required:
- encounter does not mutate WORLD_TIME per visual frame;
- final elapsed encounter duration commits according to one explicit policy;
- same encounter cannot commit elapsed time twice.

## FIX_TIME_013 — Time Partition

Activate Time Partition.

Required:
- subjective processing changes according to its ability state;
- WORLD_TIME remains governed only by external authoritative elapsed time;
- no extra world minutes or physical actions are created by subjective acceleration.

## FIX_TIME_014 — Temporal Drag

Activate local process-rate modification.

Required:
- affected process progress can differ from unaffected process progress;
- WORLD_TIME remains monotonic;
- no global clock reversal occurs.

## FIX_TIME_015 — Event Reversal

Restore one valid physical snapshot at current time `T2`, where snapshot was captured at `T1 < T2`.

Required:
- eligible physical state can restore according to Event Reversal law;
- WORLD_TIME remains `T2`;
- world history/knowledge/progression outside restore scope is not automatically rewound.

## FIX_TIME_016 — Save/load deduplication

Commit a time-advancing transaction, save, load.

Required:
- stored WORLD_TIME equals committed value;
- transaction is not replayed;
- condition expiries/recovery/travel/deadlines do not apply twice.

## FIX_TIME_017 — Device-clock manipulation

Change real device time while save state is unchanged.

Required:
- WORLD_TIME unchanged;
- no automatic resource gain/loss;
- no schedule/deadline shift;
- no passive qualification.

## FIX_TIME_018 — Calendar projection

Given WORLD_TIME and a future calendar definition:

Required:
- calendar display derives deterministically;
- changing display/calendar formatting does not mutate WORLD_TIME;
- if calendar definition is unavailable, elapsed minutes remain sufficient authority.

## Numeric gate effect

This batch closes the **general clock-semantics** prerequisite.

It does not by itself move passive resolvers to `RANGE_FIXTURES_READY`.

Remaining numeric dependencies include:
- actual action/activity ranges;
- core resource ranges;
- travel speed/cost ranges;
- fatigue/sleep/environment ranges;
- tactical elapsed-time mapping.

No runtime implementation or numeric balance is established here.
