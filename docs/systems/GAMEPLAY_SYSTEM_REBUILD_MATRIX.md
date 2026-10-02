# THE GAME — Gameplay System Rebuild Matrix

Status: **ACTIVE / DESIGN AUTHORITY PRECURSOR**  
Parent: `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`  
Purpose: decide which gameplay foundations are preserved, expanded, redesigned, or created before implementation.

## 1. Core architecture

Target authority flow remains:

`GameState -> World/Quest/Narrative -> Rules/Stats/Abilities/Equipment -> Player-safe projection -> Android UI`

Rules:
- UI presents state; it does not own it.
- persistent systems require stable IDs.
- hidden knowledge stays hidden until projected.
- deterministic/seedable behavior is preferred for testability where applicable.

## 2. Attributes and derived stats

Current base attributes:
- might;
- agility;
- endurance;
- intellect;
- will;
- perception;
- presence.

Decision:
- KEEP for current content/save compatibility.
- Final progression design may EXTEND or MIGRATE only through explicit schema/version migration.

Required progression master decisions:
- numeric scale;
- soft/hard caps;
- growth curve;
- derived-stat formulas;
- temporary modifiers;
- injury/status effects;
- equipment contribution;
- class/rank contribution;
- world-level expectations.

## 3. Skills

Decision: KEEP existing skill engine foundation, REWORK/EXTEND taxonomy.

Need:
- category hierarchy;
- general vs specialist skills;
- training rules;
- checks;
- opposed checks;
- combat skill integration;
- profession/class interaction;
- knowledge gating;
- UI representation;
- XP/mastery curve.

## 4. Abilities / powers / techniques / passives

Decision: KEEP current ability/technique progression foundation; EXTEND into one final taxonomy.

Need distinction:
- innate ability;
- learned ability;
- technique;
- passive;
- perk;
- condition-derived modifier;
- equipment-granted effect;
- class feature;
- temporary buff/debuff.

Each needs:
- ID;
- source;
- prerequisites;
- costs;
- cooldown;
- range/targeting where applicable;
- mastery;
- progression/evolution;
- failure/drawback;
- visibility;
- save representation.

## 5. Classes, professions and ranks

Target scope: NEW.

Must decide separately:
- combat/class archetype;
- profession/job;
- institutional rank;
- citizen/social rank;
- faction rank;
- mastery rank.

Do not overload one “class” field with all forms of status.

## 6. Citizen hierarchy

Target scope: NEW world/social system.

Possible dimensions:
- legal status;
- wealth;
- occupation;
- education/training;
- citizenship/residency;
- faction membership;
- noble/official/military status if the setting establishes it;
- criminal status;
- reputation.

Each dimension needs effects on:
- access;
- prices/economy if implemented;
- dialogue;
- law/security;
- quests;
- housing/work;
- NPC behavior.

## 7. Prejudice/discrimination system

Target: nuanced social simulation.

Model separately:
- institution policy;
- local culture;
- faction doctrine;
- individual NPC belief;
- player reputation/identity;
- current conflict/event pressure.

Consequences can affect:
- access;
- trust/suspicion;
- dialogue;
- legal treatment;
- employment;
- faction response;
- violence risk where authored.

Avoid a single global “racism meter.”

## 8. Activities and life simulation

Target: EXTEND current time/training/recovery systems.

Potential activity classes:
- training;
- work;
- research;
- rest;
- travel;
- social interaction;
- shopping only if economy is approved;
- maintenance/repair only if system exists;
- exploration;
- crafting only if approved;
- medical recovery;
- faction duties;
- study/education.

Every activity needs:
- location;
- duration;
- prerequisites;
- resource cost;
- outputs;
- risk;
- interruption policy;
- NPC/world-state effects.

## 9. Items, equipment and accessories

Decision:
- KEEP stable item/equipment foundations.
- EXTEND taxonomy.

Need:
- item type;
- equipment slot;
- quality;
- condition/durability only if approved;
- modifiers;
- active use;
- legality;
- provenance;
- value;
- crafting/repair links;
- loot source;
- visual asset ID;
- paper-doll/held-object mapping;
- storage/weight only if approved.

## 10. Loot system

Target: NEW/EXTEND.

Principles:
- provenance first;
- enemy/beast/resource source;
- location logic;
- scarcity;
- quality;
- condition;
- faction ownership;
- quest protection;
- anti-farming rules if necessary;
- economy balance.

## 11. World level and balance

Target: NEW master balance layer.

Define:
- regional danger bands;
- NPC civilian/combat bands;
- beast threat bands;
- gear quality bands;
- class/rank expectations;
- resource/economy band;
- encounter escape/avoidance options.

Do not make all enemies scale exactly to the player unless a specific mode requires it.

## 12. Tactical combat — original squad tactics

Target: NEW.

Broad design inspiration may include turn-based squad tactics, but implementation must be original.

Required components:
- initiative/turn order;
- action points or equivalent original action budget;
- movement cost;
- cover;
- stance;
- line of sight;
- range;
- accuracy;
- reaction/overwatch-like behavior only if expressed originally;
- abilities;
- status/injury;
- destructible/interactive terrain if approved;
- morale/fear if approved;
- body-part targeting only if final combat design supports it;
- AI roles;
- retreat/surrender;
- nonlethal outcomes;
- persistent aftermath.

Do not copy XCOM UI, terminology, maps, class names, enemy designs, narrative, percentages presentation, or proprietary encounter structure.

## 13. Persistent adversary network — original design

Working generic description: **Persistent Adversary Network**.

Target: NEW, built on current NPC memory/social state.

Potential components:
- stable adversary identity;
- memory of encounters;
- perceived player traits;
- injuries/recovery;
- wins/losses;
- promotion/demotion;
- faction standing;
- rivals/allies;
- grudges/fear/respect;
- ambitions;
- succession;
- generated missions/events;
- retirement/death/capture outcomes;
- scars/titles only from original vocabulary;
- world-map movement/schedules.

Do not copy branded hierarchy screens, named ranks, character archetypes, dialogue cadence, or presentation from another game.

## 14. NPC simulation

Decision: EXTEND current social foundation.

Need:
- schedules;
- needs/goals;
- location;
- jobs;
- family/social ties if authored;
- memory;
- knowledge;
- rumors;
- relationships;
- faction;
- resources/inventory if relevant;
- travel;
- reactions to world events;
- persistence;
- off-screen update budget.

NPC autonomy must not require hosted AI to keep the base game functional.

## 15. Quest/narrative system

Decision: KEEP + EXTEND.

Need:
- main;
- side;
- optional;
- lore;
- faction;
- dynamic/event;
- adversary;
- world-state.

Preserve:
- prerequisites;
- branching;
- failure;
- consequences;
- knowledge;
- NPC memory;
- time.

## 16. Save/persistence

Decision: KEEP as high-risk authority.

Before new world scale:
- define registry versioning;
- map stable IDs;
- migration functions;
- deprecated fields;
- unknown/forward compatibility;
- save integrity;
- deterministic reconstruction where possible.

## 17. Implementation sequence

1. progression/class/rank contract;
2. items/economy/loot contract;
3. NPC/social/hierarchy contract;
4. world balance bands;
5. tactical combat contract;
6. persistent adversary contract;
7. save migration design;
8. prototype each system separately;
9. integrate with vertical slice;
10. expand world content.

## 18. Required future documents

- `PROGRESSION_MASTER_PLAN.md`
- `ITEM_ECONOMY_LOOT_MASTER_PLAN.md`
- `NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md`
- `TACTICAL_COMBAT_MASTER_PLAN.md`
- `WORLD_BALANCE_INTEGRATION_PLAN.md`
- `SAVE_AND_CONTENT_MIGRATION_MASTER_PLAN.md`

This matrix is the decision bridge; those documents own the full specifications.


## 2026-10-02 final reconstruction integration update

The integration blueprint converts the system matrix into four migration depths:

**Depth 0 — Preserve contract:** save/load, stable IDs, hidden-state boundary, deterministic engine ownership, existing quest/equipment/stat authority.

**Depth 1 — Extend:** NPC memory/relationships/goals, quests, activities, abilities/techniques, validation, player-safe inspection.

**Depth 2 — Rework with migration:** progression taxonomy, class/profession/rank/citizen-status layers, skill taxonomy, item/economy/loot depth, world-balance formulas, richer schedules/factions, actor-presence projection.

**Depth 3 — New subsystem:** tactical positional combat, persistent adversary network, world-scale registries/population and tactical encounter terrain/AI.

No Depth 2/3 change may silently mutate save fields or Android-visible contracts. Each must define schema/API owner, stable IDs, save migration, player-safe projection, tests and rollback before integration.
