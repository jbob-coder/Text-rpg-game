# THE GAME — NPC Goal & Decision Standard

Status: **APPROVED FIRST-PASS CONTRACT / V05**
Parents:
- docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md
Current runtime:
- src/textrpg/social.py

## 1. Purpose

Define explicit persistent goals and how they influence deterministic NPC decisions.

## 2. Current goal foundation

Current social.py supports:
- goal_id;
- priority 0..100;
- progress 0..100;
- status;
- source;
- created turn/time;
- updated time;
- data payload.

Current statuses:
- active;
- paused;
- completed;
- failed.

Existing goal IDs cannot be silently replaced by set_goal.

## 3. Target extensions

Add only when consumed:
- target entity/location;
- blockers;
- expiration;
- success/failure conditions;
- visibility/privacy;
- parent/child goal;
- faction/quest source reference.

## 4. Goal ownership

A goal belongs to an NPC.

Quests do not automatically become NPC goals. A quest/event may explicitly create or progress one.

## 5. Priority

Priority is relative importance, not action authority.

High-priority goals still obey knowledge, possibility, schedule, injury, doctrine/law, relationships, and encounter rules.

## 6. Progress

Progress is bounded 0..100.

If meaningful percentage progress cannot be defined, use discrete story-state transitions instead of fake precision.

## 7. Decision selection

At a decision point:
1. collect active goals;
2. collect legal candidate actions;
3. filter by knowledge/requirements;
4. score goal contribution;
5. apply personality/relationship/doctrine modifiers;
6. deterministic tie-break.

Developer diagnostics should make selection inspectable.

## 8. Conflicting goals

Losing a decision does not delete the losing goal.

A goal closes only through explicit completion/failure/abandonment rules.

## 9. Story state versus goal

Story state records where an authored narrative track is.

Goal records what the NPC is trying to accomplish.

Current Tamsin uses both TRACK_RELAY_CASE and GOAL_UNDERSTAND_GATE_TWELVE; preserve that separation.

## 10. Visibility

Goals are private by default.

The player may learn intent through dialogue, observation, knowledge, or a specific ability.

## 11. Tests

Required:
- duplicate goal rejection;
- bounds;
- closed-goal progression rejection;
- deterministic conflict resolution;
- no goal bypass of knowledge/legal action;
- save/load;
- private-goal redaction;
- story-state independence.
