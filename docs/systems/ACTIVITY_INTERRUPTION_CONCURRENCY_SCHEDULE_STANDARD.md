# THE GAME — Activity Interruption, Concurrency & Scheduling Standard

Status: **APPROVED FIRST-PASS V10 CONTRACT / LONG-RUNNING ACTIVITY RUNTIME NOT IMPLEMENTED**
Parents:
- docs/systems/PLAYER_ACTIVITIES_AND_LIFE_LOOP_MASTER_PLAN.md
- docs/systems/ACTIVITY_RECORD_AND_STATE_STANDARD.md
- docs/systems/ACTIVITY_TIME_COST_ATOMICITY_STANDARD.md
Related:
- docs/systems/NPC_SCHEDULE_PRESENCE_STANDARD.md
- docs/systems/SAVE_AND_CONTENT_MIGRATION_MASTER_PLAN.md

## 1. Purpose

Define what happens when an activity is interrupted, which activities may overlap, and when scheduled/background activities require durable state.

## 2. Current reality

Current train/recover/choice-time operations resolve atomically in one engine call.

There is no general durable active-activity state.

Therefore Phase 1 should prefer atomic timed activities unless a genuine gameplay need requires resumable scheduling.

## 3. Interruption policy

Every non-immediate activity declares one:
- NOT_INTERRUPTIBLE;
- CANCEL_NO_PROGRESS;
- CANCEL_KEEP_ELAPSED_TIME;
- PARTIAL_PROGRESS;
- PAUSE_RESUMABLE;
- FAIL_WITH_CONSEQUENCE.

The activity definition owns the policy.

## 4. Cost behavior

On interruption, separately define:
- elapsed time retained?;
- resource cost retained?;
- item consumed?;
- partial progression retained?;
- condition/risk event applied?;
- cooldown started?;
- NPC/social consequence?.

Never infer refund policy from UI behavior.

## 5. Atomic Phase 1 default

For short Phase 1 activities:
1. validate;
2. resolve one complete duration;
3. commit all outputs atomically.

If the application is interrupted before authoritative commit, no partial result is kept.

This avoids adding save schema for active activities prematurely.

## 6. Concurrency groups

Target groups:
- BODY;
- ATTENTION;
- SOCIAL;
- TRAVEL;
- PROCESS.

Activities list the groups they occupy.

Two activities overlap only if their groups do not conflict, both definitions explicitly allow overlap, and world logic permits it.

## 7. Examples

Training:
- BODY + ATTENTION;
- normally blocks other active training.

Reading during safe travel:
- ATTENTION + TRAVEL;
- only if route/travel contract allows it.

Machine process:
- PROCESS;
- may continue while player leaves only if persistence/off-screen rules exist.

Conversation:
- SOCIAL + ATTENTION.

## 8. Background activity

Background does not mean offline real-world progression.

A background activity requires:
- start time;
- duration/progress model;
- owning world process;
- interruption rules;
- persistence;
- completion event;
- save/load behavior.

No generic background system is required for Phase 1.

## 9. Scheduled activity

Target record:
- activity_id;
- scheduled_start;
- latest_start/grace window;
- duration;
- participants;
- location;
- absence policy;
- conflict priority;
- cancellation policy.

Calendar/date semantics remain future work.

## 10. Conflict resolution

When scheduled activities conflict:
1. mandatory authored world event;
2. higher explicit schedule priority;
3. player choice when allowed;
4. stable activity ID tie-break for noninteractive resolution.

Do not silently run incompatible activities simultaneously.

## 11. Combat/emergency interruption

Combat may interrupt an activity according to the activity contract.

Tactical combat remains its own state machine.

An activity must not keep granting full progress while the player is in combat unless explicitly designed.

## 12. Save migration gate

A PAUSE_RESUMABLE, background, or future scheduled activity that survives application close requires durable activity state.

That requires an explicit save-schema migration before implementation.

Atomic activities do not.

## 13. NPC schedule integration

Mentor/supervisor presence is validated at activity start.

If a long-running activity depends on an NPC, the interruption policy must define what happens when that NPC leaves or becomes unavailable.

## 14. Android boundary

UI may display duration, conflict, known interruption rule, and cancel/continue controls when supported.

UI does not advance timers or grant progress independently.

## 15. Tests

Required when long-running activities are implemented:
- each interruption mode;
- no double progress;
- concurrency conflict rejection;
- valid overlap;
- combat interruption;
- NPC departure;
- deterministic conflict tie;
- save/load resume;
- no offline progression unless explicitly enabled.
