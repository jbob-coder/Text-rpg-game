# THE GAME — NPC Goals & Decision Standard

Status: **APPROVED FIRST-PASS V05 CONTRACT / CURRENT GOAL PRIMITIVES EXIST**
Parent:
- docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md
Current source:
- src/textrpg/social.py

## 1. Purpose

Define explicit NPC goals and deterministic decision inputs so behavior can be explained by what an NPC wants, knows, remembers, and is capable of doing.

## 2. Current goal foundation

Current set_goal stores:
- goal_id;
- priority 0..100;
- progress 0..100;
- status;
- source;
- created turn/time;
- updated time;
- data.

Current statuses:
- active;
- paused;
- completed;
- failed.

Existing goal IDs cannot be silently replaced.

## 3. Target goal record

Retain current fields and add only when needed:
- goal type;
- target entity/location;
- success conditions;
- failure conditions;
- blockers;
- deadline/expiry;
- visibility;
- parent/subgoal;
- origin event;
- allowed action domains;
- completion consequence;
- failure consequence.

## 4. Priority

0..100 remains.

Priority is relative urgency/importance, not guaranteed action.

A high-priority goal may still be impossible or illegal.

## 5. Progress

0..100 is valid for gradual goals.

Binary goals may remain 0 until completion.

Progress comes from explicit events/actions, not elapsed time unless the goal definition says so.

## 6. Goal conflicts

Decision resolution considers:
- legality;
- knowledge;
- context;
- goal priority;
- relationship;
- personality;
- orders/faction;
- danger/injury;
- opportunity cost.

A goal never authorizes omniscient behavior.

## 7. Goal creation

Sources may include:
- authored starting state;
- story event;
- faction order;
- relationship/memory consequence;
- discovery/knowledge;
- survival need;
- persistent adversary event.

Creation must record source.

No unbounded runtime AI should invent arbitrary long-term goals without a documented generation rule.

## 8. Goal transitions

Operations:
- create;
- progress;
- pause;
- resume;
- complete;
- fail;
- retire/cancel if later supported.

Each transition should append history.

Terminal goals cannot be progressed unless a dedicated reopen/migration rule exists.

## 9. Decision candidate pipeline

A general NPC decision tick should:
1. identify relevant active goals;
2. reject actions illegal in current state/location;
3. reject actions requiring unknown information;
4. score legal candidates;
5. apply stable deterministic tie-break;
6. execute through the owning domain system.

The goal system does not directly mutate unrelated domains.

## 10. Schedule interaction

Schedule describes normal planned activity.

Goals may override schedule based on priority/emergency.

The schedule standard owns precedence.

## 11. Combat

Encounter objectives have immediate tactical authority.

Long-term goals/personality may modify utility but cannot bypass combat legality.

A goal such as understanding Gate Twelve may favor investigation/survival over reckless elimination.

## 12. Current Tamsin goal

Current content creates:
- GOAL_UNDERSTAND_GATE_TWELVE;
- priority 75;
- progress 10 or 20 depending route;
- later progress +15/+30.

This is a current Phase 1 proof and must remain regression-tested.

## 13. Goal privacy

Goals are private by default.

Player-safe UI may expose a stated/inferred/quest-related goal only when Jack can know it.

Never send the full goals map to Android.

## 14. Off-screen updates

Off-screen goal progress must be bounded.

Named recurring NPCs may receive coarse event-based updates. Aggregate populations should not receive full individual decision ticks.

## 15. Tests

Required:
- priority/progress bounds;
- duplicate goal rejection;
- closed goal cannot progress;
- deterministic candidate tie;
- unknown-information action rejection;
- schedule override;
- privacy redaction;
- save/load;
- Tamsin goal regression.

## 16. Migration

Preserve current goals container and GOAL_UNDERSTAND_GATE_TWELVE.

Add richer fields as optional compatible data until a save-schema migration is justified.
