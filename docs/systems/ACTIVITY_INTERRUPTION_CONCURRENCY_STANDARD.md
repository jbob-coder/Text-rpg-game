# THE GAME — Activity Interruption, Concurrency & Scheduling Standard

Status: **APPROVED FIRST-PASS V10 CONTRACT / ADVANCED RUNTIME DEFERRED**
Parent:
- docs/systems/PLAYER_ACTIVITIES_AND_LIFE_LOOP_MASTER_PLAN.md
Related:
- docs/systems/NPC_SCHEDULE_PRESENCE_STANDARD.md
- docs/systems/ACTIVITY_TIME_COST_ATOMICITY_STANDARD.md

## 1. Purpose

Define when activities can overlap, how they are interrupted, and what state survives interruption without requiring a high-frequency life simulator.

## 2. Phase 1 scope

Phase 1 primarily uses atomic timed activities.

It does not require:
- multiple simultaneous player activity slots;
- offline progression;
- a full calendar;
- resumable multi-day work.

The schema is designed now so later expansion does not force incompatible state.

## 3. Concurrency groups

Candidate groups:
- BODY;
- ATTENTION;
- SOCIAL;
- TRAVEL;
- MACHINE_PROCESS;
- PASSIVE_RECOVERY.

An activity declares groups it occupies.

Default:
- two foreground activities cannot share BODY or ATTENTION;
- SOCIAL usually consumes ATTENTION;
- travel compatibility is explicit;
- machine process may continue if it truly operates independently.

## 4. Concurrency policy

Each activity says:
- EXCLUSIVE;
- COMPATIBLE_WITH listed groups/activities;
- BACKGROUND_ONLY;
- PASSIVE.

No UI heuristic decides compatibility.

## 5. Interruption causes

Potential:
- player cancel;
- combat;
- emergency/world event;
- required NPC leaves;
- access revoked;
- resource depletion;
- schedule window closes;
- travel begins/ends;
- injury/condition;
- save/load policy;
- application/process interruption.

## 6. Interruption policy

Each non-immediate activity defines:
- INTERRUPT_CANCEL_NO_PROGRESS;
- INTERRUPT_KEEP_PARTIAL;
- INTERRUPT_PAUSE_RESUMABLE;
- INTERRUPT_COMPLETE_CURRENT_STEP.

The policy also defines:
- time spent;
- resources consumed/refunded;
- partial output;
- cooldown;
- history event.

## 7. Atomic current activities

Current train/recover/practice actions behave as bounded atomic resolutions.

For those:
- preflight;
- commit full duration/effect;
- or fail with no mutation.

Do not retrofit resumable state into them unless product UX needs it.

## 8. Scheduled activities

Future scheduled activity needs:
- scheduled start/end;
- location;
- participant availability;
- grace/late policy;
- missed-event consequence;
- persistence.

It should be evaluated at relevant world-time boundaries, not every frame.

## 9. Background activity

Background progress is not real-world offline progress by default.

If allowed later:
- cap elapsed time;
- validate world events during interval;
- prevent duplicated rewards;
- record deterministic catch-up;
- explicitly handle clock tampering if device time is used.

The safest default is no offline progression.

## 10. Combat interruption

Entering tactical combat:
- cancels or pauses current activity according to its contract;
- never lets training/recovery silently continue at full rate during combat;
- preserves already committed atomic activities.

## 11. Travel concurrency

Travel-compatible activities require route/mode support.

Examples later:
- conversation;
- reading;
- light recovery.

Walking through dangerous terrain should not automatically allow full focused study.

## 12. NPC schedule interaction

Mentor/supervisor availability is a hard activity input.

If the NPC schedule changes before start, activity becomes unavailable.

If interruption occurs mid-session, the activity policy decides partial progress.

## 13. Save/load

Resumable activities require durable:
- activity ID;
- state;
- elapsed/planned duration;
- participants;
- location;
- paid costs;
- schema version.

Atomic activities need no active record after commit.

## 14. Player-safe UI

UI can show:
- activity in progress;
- time remaining if known;
- pause/cancel availability;
- interruption warning;
- concurrency conflict reason.

It must not create local timers that become authoritative.

## 15. Determinism

Same state, schedule boundary, and interruption event produces the same state transition.

No background completion based solely on Compose lifecycle timing.

## 16. Tests

Required:
- exclusive group conflict;
- compatible groups;
- cancel/no-progress;
- keep-partial;
- pause/resume when implemented;
- combat interruption;
- NPC departure;
- save/load resumable state;
- no offline progress by default;
- no duplicate reward after resume.

## 17. Phase 1

For the first playable slice:
- Trace Chamber training is atomic;
- combat cannot overlap training;
- recovery is atomic;
- no background slots;
- no offline progression.

This is intentionally simple and robust.
