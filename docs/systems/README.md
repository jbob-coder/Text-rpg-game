# THE GAME — Systems Documentation Index

Parent authority: `../MASTER_GAME_DEVELOPMENT_PROGRAM.md`

## Current system planning

- [Gameplay System Rebuild Matrix](GAMEPLAY_SYSTEM_REBUILD_MATRIX.md) — current KEEP/EXTEND/REWORK/NEW decisions and dependency order.

## Required master documents

Planned:
- `PROGRESSION_MASTER_PLAN.md`
- `ITEM_ECONOMY_LOOT_MASTER_PLAN.md`
- `NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md`
- `TACTICAL_COMBAT_MASTER_PLAN.md`
- `WORLD_BALANCE_INTEGRATION_PLAN.md`
- `SAVE_AND_CONTENT_MIGRATION_MASTER_PLAN.md`

## Authority rule

Current repository source and exact-head verification outrank planning documents.

Do not implement target-scale classes, ranks, tactical combat, persistent adversary systems, or economy expansion until their master contracts are written and linked here.

## Materialized master plans — 2026-10-02

The following previously planned system masters now exist:

- `PROGRESSION_MASTER_PLAN.md`
- `TACTICAL_COMBAT_MASTER_PLAN.md`
- `NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md`
- `ITEM_ECONOMY_LOOT_MASTER_PLAN.md`
- `WORLD_BALANCE_INTEGRATION_PLAN.md`
- `SAVE_AND_CONTENT_MIGRATION_MASTER_PLAN.md`

These remain documentation contracts. Their existence does not claim runtime implementation.


## Activity / life loop
- `PLAYER_ACTIVITIES_AND_LIFE_LOOP_MASTER_PLAN.md` — player time-use, training, study, work, recovery, social, diagnostics, scheduled/background activity, interruption/concurrency and safe UI projection.


## Evolved target-game design — 2026-10-03

- [Progression, Classes & Ranks: Evolved Game Design](PROGRESSION_CLASSES_RANKS_EVOLVED_GAME_DESIGN.md) — reconstruction-grade target design that uses the current game as reference evidence and defines the larger progression/class/profession/rank/training system to create before implementation.

Working rule: current runtime facts and evolved target design stay explicitly separated. Migration/API work is downstream of target-game design.

- [Evolved Skill Registry](EVOLVED_SKILL_REGISTRY.md) — full 23-skill target-game registry with training, world/tactical uses, class/profession affinities, content requirements and pixel-art presentation requirements.


## Status UI / abilities / passives

- [Status UI, Abilities & Passives Master Plan](STATUS_UI_ABILITIES_AND_PASSIVES_MASTER_PLAN.md) — target-game authority for age-18 awakening, global Level, one-primary-ability rule, rarity, Level-100 exception, scalable passive acquisition, hidden requirements, knowledge asymmetry and catalog architecture.
- [Status subsystem index](status/README.md) — child contracts, registries, visibility rules and future catalog navigation.

This program supplements the broader progression authority and owns the Status-specific rules.


## Tactical combat first-pass contract layer — 2026-10-04

The V08 first-pass tactical documentation floor is now materialized through ten canonical units: the master plan, camera/presentation standard, and eight implementation-detail standards.

- TACTICAL_COORDINATE_OCCUPANCY_STANDARD.md
- TURN_INITIATIVE_ACTION_BUDGET_STANDARD.md
- MOVEMENT_PATHING_AND_POSITIONING_STANDARD.md
- LOS_DETECTION_AND_COMBAT_KNOWLEDGE_STANDARD.md
- DIRECTIONAL_COVER_TERRAIN_STANDARD.md
- COMBAT_ACTION_TARGETING_RESOLUTION_STANDARD.md
- INJURY_CONDITION_AFTERMATH_STANDARD.md
- COMBAT_AI_OBJECTIVES_RETREAT_STANDARD.md

This closes the first-pass documentation quota for V08 only. Tactical runtime remains unimplemented. The next combat document should be a bounded Gate Twelve Phase 1 encounter packet rather than more generic combat theory.
