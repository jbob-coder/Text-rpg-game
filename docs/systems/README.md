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


## V05 character/NPC/social first-pass closure — 2026-10-04

V05 now has 12 / 12 minimum first-pass canonical units: the existing NPC/Social/Rival master plus eleven child standards/packets covering identity, personality, memory, knowledge/privacy, relationships, goals, schedule/presence, faction membership, rumor/social consequence, recurring-character authoring, and the Tamsin Phase 1 proof packet.

The first-pass quota is satisfied; runtime expansion remains separate. Persistent-adversary depth continues under V09 rather than being treated as complete by this V05 closure.


## V10 activities/life-simulation first-pass closure — 2026-10-04

V10 now has 8 / 8 first-pass canonical units: the activity master plus seven child standards/packets covering activity records, time/cost atomicity, training/practice, recovery/treatment, work/study/research, interruption/concurrency, and the Trace Chamber Phase 1 proof.

The current train/recover/technique-practice runtime is preserved as foundation. Full professions, scheduled/background activity, calendar, offline progression and final Activity UI remain future work.


## V07 items/economy/loot first-pass closure — 2026-10-04

V07 now has 10 / 10 first-pass canonical units: the item/economy master plus nine child standards/packets covering item records, inventory/stacks, equipment/loadouts, quality/rarity/condition, material/resource provenance, loot/rewards, economy/pricing architecture, vendors/services/ownership, and the Gate Twelve Phase 1 item/equipment proof.

The current flat inventory and equipment runtime remain the Phase 1 foundation. Currency, vendors, crafting, durability, encumbrance and broad loot generation are not required for the first playable slice.


## V09 persistent-adversary/world-memory first-pass closure — 2026-10-04

V09 now has 8 / 8 first-pass canonical units: a dedicated original persistent-adversary/world-memory master plus seven child contracts covering eligibility/identity, encounter memory/adaptation, lifecycle/recurrence, hierarchy/succession, territory/routing, player-safe intel, and a Gate Twelve bounded proof packet.

The system is explicitly knowledge-driven and world-logical. It does not use arbitrary post-defeat stat inflation, forced cameos, memory inheritance across successors, or omniscient counter-preparation.

The Gate Twelve proof intentionally does not promote the current unidentified Service Tunnel contacts into canon recurring enemies.


## Persistent-adversary implementation migration — 2026-10-04

- `PERSISTENT_ADVERSARY_SCHEMA_API_MIGRATION_PACKET.md` — D-032 implementation mapping for the V09 contract layer.

The first runtime target extends the existing per-NPC durable record rather than creating a second actor registry. The packet keeps top-level save schema v1 only behind explicit nested-record validation and round-trip tests; any new top-level adversary field requires a later schema migration.

No runtime or canonical recurring enemy is created by this document.
