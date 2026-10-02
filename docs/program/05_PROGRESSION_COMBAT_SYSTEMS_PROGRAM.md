# Progression, Combat and Systems Program

Status: ACTIVE / ARCHITECTURE

## Scope

Owns:
- attributes;
- derived stats;
- skills;
- classes;
- ranks;
- abilities;
- techniques;
- passives;
- perks;
- status conditions;
- activities/training;
- tactical combat;
- enemy/rival persistence;
- encounter balance;
- world level/scaling.

## Existing foundation

Current repository documentation/code already contains:
- seven core attributes;
- skills;
- resources;
- derived stats;
- equipment modifiers;
- perks/conditions;
- abilities/techniques;
- mastery/prerequisites/costs/cooldowns/drawbacks;
- deterministic choice checks;
- quest progression.

These are the starting point, not proof that the final system is locked.

## Classes and ranks

Owner request adds formal class/rank development.

Open design questions:
- classless vs class-assisted progression;
- whether classes gate abilities or organize them;
- multiclass/specialization rules;
- civilian/professional ranks versus combat ranks;
- faction ranks versus character classes;
- how ranks interact with social hierarchy;
- whether class progression is reversible.

## Tactical combat direction

Requirement P-COMBAT-001:
Combat should capture principles of readable turn-based squad tactics without copying another game's protected UI, terminology, maps, characters or exact rule expression.

Candidate original principles:
- discrete action economy;
- cover/position;
- line of sight;
- range;
- movement cost;
- overwatch/reaction-style authored mechanics under original naming/rules;
- environment interactions;
- status effects;
- body/target zones only if supported by balance and UI;
- party/NPC autonomy;
- deterministic or seeded resolution compatible with saves/tests.

Exact combat rules remain UNDECIDED.

## Persistent rival/adversary direction

Requirement P-RIVAL-001:
Create an original persistent adversary system using general systemic ideas—memory, promotion/demotion, grudges, traits, injuries, relationships, territory, re-encounters—without copying proprietary names, presentation, hierarchy, dialogue structure or one-to-one mechanics.

Potential original entities:
- adversary record;
- encounter memory;
- rivalry score;
- scars/injuries;
- learned counters;
- faction standing;
- territory/role;
- nemesis-like recurrence under original project terminology to be chosen later.

Do not use another game's trademarked branding as the shipped system name.

## World level and balance

Must define:
- how regions signal danger;
- whether enemies scale, partially scale, or remain fixed;
- minimum/maximum encounter bands;
- gear contribution;
- ability contribution;
- party-size contribution;
- encounter objectives beyond defeat-all;
- retreat/failure recovery;
- anti-grind controls;
- progression ceilings.

## Required future documents

- STAT_SCHEMA_FINAL
- DERIVED_STATS_FINAL
- SKILL_TREE_ARCHITECTURE
- CLASS_AND_SPECIALIZATION_SYSTEM
- RANK_SYSTEM
- ABILITY_PASSIVE_PERK_MATRIX
- ACTIVITY_TRAINING_SYSTEM
- TACTICAL_COMBAT_CORE
- TACTICAL_AI
- PERSISTENT_ADVERSARY_SYSTEM
- WORLD_LEVEL_AND_BALANCE
- ENCOUNTER_GENERATION_RULES
- COMBAT_UI_PROJECTION
