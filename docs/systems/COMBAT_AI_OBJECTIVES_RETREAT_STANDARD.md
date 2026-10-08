# THE GAME — Combat AI, Objectives, Retreat & Companion Orders Standard

Status: **APPROVED FIRST-PASS CONTRACT / D-071 HEADLESS IMPLEMENTATION VERIFIED**
Parents:
- docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md
- docs/systems/LOS_DETECTION_AND_COMBAT_KNOWLEDGE_STANDARD.md
- docs/systems/TURN_INITIATIVE_ACTION_BUDGET_STANDARD.md
Related:
- docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md
- docs/systems/WORLD_BALANCE_INTEGRATION_PLAN.md

## 1. Purpose

Define deterministic tactical decision-making that respects objectives, doctrine, personality, knowledge, injury, and retreat instead of nearest-target pursuit.

## 2. AI authority

AI receives authoritative tactical state, actor-safe knowledge, traits/doctrine, legal-action query, and objective state. It outputs one selected legal action package.

UI never chooses enemy actions.

## 3. No-cheating rule

AI cannot target undetected actors, avoid unknown hazards without a knowledge basis, inspect secret cooldowns/inventory, or use global omniscient state unless the actor is explicitly granted that information.

Hidden-state trap tests are mandatory.

## 4. Candidate generation

1. collect legal actions;
2. collect legal known targets/cells;
3. create candidates;
4. reject invalid;
5. score;
6. choose highest;
7. tie-break by action_id, target key, then cell/path key.

End Activation is always valid if encounter remains active.

## 5. Phase 1 utility defaults

Recommended scoring:
- immediate objective completion: +1000;
- prevent immediate objective failure: +400;
- mandatory retreat satisfied: +800;
- survival/strong-cover improvement: up to +100;
- protect assigned ally/objective: up to +150;
- expected damage: +10 per expected health point;
- meaningful condition: +40 base;
- objective-forward movement: +5 per useful cell;
- hazardous/self-defeating move: strong negative;
- doctrine/order violation: strong negative or illegal.

These are tuning weights.

Expected damage uses preview math without consuming authoritative event variance.

## 6. Personality/doctrine

Inputs may include aggression, caution, discipline, loyalty, fear, faction doctrine, mission role, injury, and scarcity.

Current social.py already defines aggression, caution, loyalty, and discipline personality axes. Reuse compatible values rather than duplicating them.

## 7. Objective model

Phase 1 types:
- ELIMINATE;
- ESCAPE;
- SURVIVE_ROUNDS;
- REACH_CELL;
- PROTECT_ACTOR;
- INTERACT_RETRIEVE;
- DISABLE_OBJECT;
- CAPTURE_ACTOR.

The first Gate Twelve encounter should support a non-elimination or retreat-capable resolution.

## 8. Objective ownership

Encounter/quest rules own completion/failure. AI cannot mark objectives complete without the authoritative validator.

## 9. Retreat

Retreat motivation may come from objective, low health, severe injury, isolation, doctrine, fear/morale, leader loss, or explicit order.

Phase 1 retreat requires reaching a valid exit cell, then leaving occupancy. Durable escape is written in aftermath.

No teleport-off-map retreat.

## 10. Surrender

Optional in Phase 1 but schema-compatible. Surrender is distinct from death and has aftermath consequences.

## 11. Beast AI

Beast doctrine profiles may be territorial, pack, ambush predator, prey/flee, or nest-defense, while obeying the same legality/knowledge rules.

## 12. Companion orders

Phase 1 vocabulary:
- HOLD;
- ADVANCE;
- FOCUS_TARGET;
- ASSIST;
- WITHDRAW.

These modify utility rather than directly possessing the companion.

Personality, discipline, loyalty, fear, injury, and impossible conditions may constrain execution.

## 13. Developer diagnostics

Developer-only logs may include candidates, rejection reasons, utility components, selected action, and tie-break.

Enemy utility internals never enter player projection.

## 14. Performance

For Galaxy A02-class target:
- small bounded unit count;
- candidate pruning;
- reuse reachable-cell query;
- no Monte Carlo search;
- AI computes only on decision points.

## 15. Tests

Required:
- cannot target hidden actor;
- deterministic tie;
- objective priority;
- retreat legality;
- no off-map escape;
- companion order changes utility not legality;
- beast legality;
- diagnostics redaction;
- bounded candidate-count fixture.

## 16. Next combat artifact

The framework is implementable, but Phase 1 still needs one Gate Twelve encounter packet specifying map, actors, objective, exits, AI profiles, action loadouts, injury/aftermath hook, and success/failure consequences.

Implementation evidence: `docs/evidence/D071_TACTICAL_DECISIONS_2026-10-08.md`. Durable aftermath and bridge/UI integration remain D-072/D-073/D-074.
