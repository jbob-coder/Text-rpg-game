# THE GAME — Player Activities & Life-Loop Master Plan

Status: **FOUNDATIONAL / DESIGN CONTRACT / IMPLEMENTATION PARTIAL AT LOWER SCOPE**  
Repository: `jbob-coder/Text-rpg-game`  
Parent authorities:
- `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`
- `docs/systems/PROGRESSION_MASTER_PLAN.md`
- `docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`
- `docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md`

## 1. Purpose

Define how the player spends time outside immediate story-choice resolution and tactical combat.

This contract covers:
- training;
- study;
- work/profession;
- rest/recovery;
- social activity;
- research;
- maintenance/diagnostics;
- travel-time activity;
- gathering/harvesting only if approved by world/economy systems;
- scheduled/background activities;
- location-specific services;
- interruption and failure;
- NPC participation;
- progression/economy/world consequences;
- Android presentation.

It does not invent activities merely to create buttons.

## 2. Existing implementation facts

Current repository implementation already supports lower-level building blocks:

- authoritative `GameState.time_minutes`;
- authored scene-choice `time_cost_minutes`;
- deterministic time advancement;
- timed conditions;
- resource recovery over time;
- skill training with time/intensity/resource cost;
- ability/technique practice;
- quest progression;
- NPC relationships/knowledge/goals;
- world/location state;
- save/load.

These are existing foundations. They are not yet a full activity/life-loop system.

## 3. Core activity principle

Every meaningful activity answers:

1. where can it happen?
2. who can perform or supervise it?
3. how long does it take?
4. what resources does it consume?
5. what state can interrupt it?
6. what does it produce?
7. how is progression capped or diminished?
8. what world/NPC consequences occur?
9. what does the player know before committing?
10. how is it represented in save/load and UI?

No generic “do activity -> gain XP” shortcut becomes the universal model.

## 4. Activity execution classes

### A. Immediate activity

Resolved in one authored interaction.

Examples:
- inspect a relay;
- read a record;
- ask a worker a question;
- use a tool.

### B. Timed active activity

Consumes a defined block of world time and resolves while the player is focused on it.

Examples:
- practice Signal Pulse;
- study records;
- repair a device if that system is later approved;
- train a skill.

### C. Scheduled activity

Player commits to a future/time-blocked task that may complete later.

Possible examples:
- work shift;
- class/training session;
- appointment;
- supervised practice.

This is **not implemented at target scope**.

### D. Background/passive activity

A bounded activity that may progress while another compatible foreground action occurs.

Rules:
- must define whether concurrent progress is logically possible;
- cannot duplicate full-rate active training;
- must have explicit caps and interruption rules;
- cannot silently advance while the app is closed unless an offline-time system is separately approved.

“Passive activity” does not automatically mean real-world offline progression.

### E. Ambient NPC activity

NPC world behavior such as work, travel, sleep or social schedules.

This belongs to NPC/world simulation and is not automatically a player activity.

## 5. Activity record schema

Each reusable activity should eventually define:

- `activity_id`;
- display name;
- category;
- location requirements;
- actor/mentor requirements;
- schedule window if any;
- duration model;
- foreground/background class;
- concurrency group;
- interruption rules;
- resource costs;
- item/tool requirements;
- skill/attribute/ability requirements;
- knowledge requirements;
- legal/faction/access requirements;
- world-state requirements;
- risk;
- deterministic/random resolution contract;
- progression outputs;
- item/resource outputs;
- money/economy outputs if economy exists;
- knowledge outputs;
- relationship outputs;
- condition/injury outputs;
- quest/world effects;
- cooldown/repeat rules;
- diminishing returns;
- player-safe preview;
- hidden resolution data;
- scene/UI presentation;
- save schema;
- validation rules.

## 6. Time model

Current time authority remains `GameState.time_minutes`.

Activity time must use the same world-time authority.

Do not create independent UI timers that mutate gameplay directly.

Future time layers may include:
- minute;
- hour;
- day;
- week;
- schedule blocks.

Calendar/date systems are not locked yet.

## 7. Training activities

Training must integrate with:
- attributes;
- skills;
- abilities;
- techniques;
- classes/professions if approved;
- mentors;
- location;
- equipment;
- injuries/conditions;
- stamina/focus/resolve;
- time.

Current training/practice is evidence for the model, not final balance.

Future training must avoid:
- infinite no-cost grinding;
- instant mastery;
- bypassing prerequisites;
- UI-only stat modification.

## 8. Study and research

Study/research activities may consume:
- records;
- books/data;
- experts;
- equipment;
- time;
- focus;
- prior knowledge.

Outputs may include:
- knowledge;
- quest progress;
- technique discovery prerequisites;
- map/world information;
- research progress.

Municipal Archive and Trace Chamber are current proof locations for different research identities.

## 9. Work and profession

A profession system is future scope.

If implemented, work activities require:
- employer/institution;
- role;
- schedule;
- skill/attribute requirements;
- compensation;
- reputation;
- legal/social status;
- risk;
- promotion/rank rules;
- absence/failure consequences.

Do not create generic “work 8 hours = money” before economy, calendar and employment contracts exist.

## 10. Recovery and rest

Current recovery is authoritative lower-level evidence.

Future rest/recovery may distinguish:
- short rest;
- sleep;
- medical recovery;
- ability-specific recovery;
- injury rehabilitation;
- safe/unsafe rest;
- quality modifiers.

Exact categories and rates remain balance decisions.

## 11. Social activities

Potential activities:
- conversation;
- meeting;
- mentoring;
- negotiation;
- recreation;
- faction event;
- relationship-maintenance activity.

Outputs must be authored through:
- relationship axes;
- knowledge;
- memory;
- goals;
- reputation;
- faction/social state.

No relationship is increased merely because the UI displays a social button.

## 12. Maintenance / diagnostics

Relay Workbench is the current proof location.

Potential future activity types:
- inspect device;
- diagnose malfunction;
- compare signal evidence;
- maintain equipment if durability is later approved.

This must remain separate from broad crafting unless crafting becomes a formal system.

## 13. Gathering / harvesting

Not approved as a universal mechanic yet.

If later introduced, it requires:
- resource zone;
- ecology;
- ownership/law;
- tools;
- skill;
- depletion/renewal;
- risk;
- loot provenance;
- time;
- economy linkage.

No arbitrary node farming without world provenance.

## 14. Travel-time activity

Future routes may allow compatible activities during travel, such as:
- reading;
- recovery;
- conversation;
- observation.

Only if:
- route mode permits it;
- risk/interruption permits it;
- travel system exposes the necessary state.

Travel time remains authoritative world state.

## 15. Interruption

Every non-immediate activity must define interruption behavior.

Possible causes:
- combat;
- emergency;
- resource depletion;
- NPC departure;
- schedule conflict;
- quest/world event;
- player cancel;
- invalidated access.

The activity defines:
- whether partial progress is kept;
- whether costs are refunded;
- whether time already spent remains;
- whether new state/consequences occur.

## 16. Concurrency

Concurrency must be explicit.

Each activity gets a concurrency group such as:
- body;
- attention;
- travel;
- social;
- machine/process.

Two activities may overlap only when their groups and logic permit it.

The engine, not UI, decides concurrency legality.

## 17. Diminishing returns and anti-grind

Potential controls:
- fatigue;
- mentor availability;
- resource costs;
- daily/session caps;
- reduced gain after repeated identical training;
- skill ceiling;
- location quality;
- prerequisite knowledge;
- injury/strain.

Final formulas remain balance work.

## 18. Class/profession integration

Activities can:
- train class-relevant skills;
- qualify for class/profession entry;
- satisfy rank requirements;
- unlock techniques;
- build institutional reputation.

Activities must not silently assign a class solely because a threshold was crossed unless that class's acquisition contract says so.

## 19. Citizen/social hierarchy integration

Activity access may depend on:
- citizenship;
- legal status;
- occupation;
- institutional rank;
- faction membership;
- reputation;
- wealth/resources;
- regional law.

If fictional discrimination exists, access restrictions must come from documented institutions/NPC beliefs/world rules rather than one universal identity penalty.

## 20. NPC participation

NPCs may:
- mentor;
- supervise;
- assist;
- oppose;
- interrupt;
- schedule;
- invite;
- remember outcomes.

NPC participation must update authoritative memory/relationship/goal state when relevant.

## 21. Activity risk

Activities may include:
- failure;
- injury;
- condition;
- lost resources;
- legal consequences;
- NPC/social consequences;
- exposure to beasts/hazards.

Risk preview must reveal only player-safe information.

## 22. Rewards

Possible reward classes:
- skill progress;
- ability mastery;
- knowledge;
- items/resources;
- money if economy exists;
- reputation;
- relationship changes;
- quest progress;
- world-state change;
- recovery.

Every reward requires provenance.

## 23. Save/persistence

Persistent activity state may require:
- active activity ID;
- start time;
- planned duration;
- elapsed time;
- participants;
- location;
- paid costs;
- partial progress;
- interruption state;
- deterministic seed/context;
- schema version.

No long-running activity implementation before save migration is defined.

## 24. Android UX

Future activity UI may show:
- name;
- location;
- duration;
- known costs;
- known requirements;
- known risk;
- expected broad outcome;
- participant;
- start/cancel/continue controls.

It must not show:
- hidden roll thresholds;
- secret consequences;
- NPC private goals;
- undiscovered outputs.

Activity UI should be contextual to location and character state rather than one giant menu containing every possible world action.

## 25. Notifications

Potential notifications:
- activity complete;
- interrupted;
- resource too low;
- schedule conflict;
- mentor unavailable;
- world event changed activity.

Notification rules belong to application UX after activity state exists.

## 26. Tactical combat boundary

Combat interrupts or suspends activities according to activity contract.

Combat does not run as an “activity” inside the same generic resolver if doing so would erase tactical state requirements.

## 27. Originality

Life-sim/activity mechanics may use broad genre conventions.

The implementation must use original:
- names;
- formulas;
- UI;
- data;
- progression;
- fiction;
- event structure.

## 28. Existing locations mapped to activity potential

- Depot Plaza: public/state/social activities when authored.
- Workshop Row: practical/contractor activities if systems support them.
- Municipal Archive: research/study.
- Platform Nine: narrative/social/depot state.
- Relay Workbench: diagnostics.
- Gate Twelve: threshold/investigation.
- Quiet Stair: egress/low-frequency events.
- Service Tunnel: investigation/travel.
- Trace Chamber: training/research/recovery.

This mapping does not create new actions by itself.

## 29. Implementation order

1. finalize activity record schema;
2. map existing training/recovery/choice-time actions into the schema;
3. define player-safe activity projection;
4. define persistence migration;
5. add validation;
6. implement one proof activity family;
7. add Android contextual presentation;
8. verify interruption/save/resume;
9. only then add jobs/schedules/background activities.

## 30. Open decisions

- final calendar/date model;
- offline progression yes/no;
- background activity slot count;
- concurrency model;
- profession system scope;
- crafting/repair scope;
- gathering scope;
- economy/pay model;
- fatigue/diminishing-return formulas;
- activity scheduling UI;
- whether any activities continue during fast travel.

Until resolved, UI must not assume answers.

## 31. Completion gate

This master is complete enough for schema prototyping when:
- activity categories and ownership are stable;
- existing lower-level mechanics are mapped;
- persistence requirements are known;
- player-safe projection is designed;
- first proof loop is selected.

Mass activity content remains blocked until world/progression/economy dependencies are ready.
