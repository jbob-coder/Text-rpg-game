# THE GAME — Activity Record & State Standard

Status: **APPROVED FIRST-PASS V10 CONTRACT / LOWER-LEVEL RUNTIME EXISTS**
Parent:
- docs/systems/PLAYER_ACTIVITIES_AND_LIFE_LOOP_MASTER_PLAN.md
Related:
- docs/systems/PROGRESSION_MASTER_PLAN.md
- docs/systems/NPC_SCHEDULE_PRESENCE_STANDARD.md
- docs/systems/SAVE_AND_CONTENT_MIGRATION_MASTER_PLAN.md

## 1. Purpose

Define one reusable activity contract for training, study, research, work, recovery, diagnostics, social actions, and other deliberate time-use without turning every button into a disconnected special case.

## 2. Current reality

The engine already supports:
- GameState.time_minutes;
- authored choice time_cost_minutes;
- deterministic time advancement;
- conditions with durations;
- recover;
- skill/attribute training;
- technique practice/use/recovery;
- quests, knowledge, relationships, inventory, and history.

These are lower-level primitives, not a normalized activity registry.

## 3. Activity identity

Reusable activities use stable IDs:
- prefix ACTIVITY_;
- semantic uppercase snake case;
- ID survives display-name changes;
- never reuse an ID for a different activity contract.

One-off story interactions may remain scene choices if they do not need reusable activity state.

## 4. Activity definition

Required:
- activity_id;
- display_name;
- category;
- execution_class;
- duration model;
- location requirements;
- actor/mentor requirements;
- resource costs;
- prerequisite requirements;
- interruption policy;
- output/effect references;
- repeat policy;
- player-safe preview;
- provenance/canon status.

Optional when consumed:
- schedule window;
- tool/item requirements;
- concurrency groups;
- risk;
- progression cap;
- cooldown;
- diminishing returns;
- participant roles;
- economy outputs;
- quest/world effects.

## 5. Execution classes

Use:
- IMMEDIATE;
- TIMED_ACTIVE;
- SCHEDULED;
- BACKGROUND_BOUNDED.

Phase 1 needs IMMEDIATE and TIMED_ACTIVE only.

SCHEDULED/BACKGROUND_BOUNDED require persistence/interruption contracts before runtime adoption.

## 6. Categories

Initial taxonomy:
- TRAINING;
- PRACTICE;
- STUDY;
- RESEARCH;
- WORK;
- RECOVERY;
- MEDICAL;
- SOCIAL;
- DIAGNOSTIC;
- INVESTIGATION;
- TRAVEL_COMPATIBLE;
- GATHERING only if later approved.

Category does not determine formulas by itself.

## 7. Runtime activity state

Immediate/timed activities that resolve atomically may not need a durable active_activity field.

Long-running/scheduled activity target state:
- activity_id;
- started_at_minutes;
- planned_duration;
- elapsed_minutes;
- actor/participants;
- location_id;
- paid/reserved costs;
- partial progress;
- interruption state;
- deterministic context;
- schema_version.

Do not add this to GameState until a real resumable activity requires it.

## 8. Query vs mutation

Activity availability/preview is read-only.

Starting/resolving is authoritative mutation.

A UI refresh must never:
- spend resources;
- advance time;
- create goals;
- generate rewards;
- mutate activity state.

## 9. Availability pipeline

Validate:
1. definition exists;
2. player/runtime state valid;
3. correct location/access;
4. participants available;
5. schedule window if any;
6. prerequisites;
7. required items/tools;
8. resources;
9. concurrency;
10. interruption blockers;
11. repeat/cooldown;
12. domain-specific legality.

No costs paid on validation failure.

## 10. Outputs

Activity outputs are domain-owned effects such as:
- skill progress;
- technique mastery;
- knowledge;
- recovery;
- quest objective;
- relationship/memory;
- item/resource;
- condition;
- world flag.

The activity layer coordinates; it does not duplicate each domain's rule calculations.

## 11. Repeatability

Definition must say:
- once;
- repeatable;
- limited count;
- cooldown;
- diminishing;
- story-reset.

No unlimited repeatability by default.

## 12. Player-safe projection

UI can receive:
- ID/label/category;
- available/unavailable;
- safe reason;
- duration;
- known costs;
- known broad outcomes;
- participant/location;
- cancelability.

Never expose hidden success thresholds, secret rewards, private NPC goals, or undiscovered knowledge.

## 13. Save/load

Atomic activities only need their committed results persisted.

Any resumable activity requires explicit durable state and migration.

## 14. Tests

Required:
- stable ID validation;
- availability read-only;
- no cost on failure;
- correct duration;
- output routed to owning subsystem;
- repeat rules;
- privacy redaction;
- save/load after completion;
- resumable state only when schema supports it.

## 15. Phase 1

Trace Chamber training/recovery is the first proof family. It already has authored current actions and should be normalized conceptually before new job/crafting activity systems are invented.
