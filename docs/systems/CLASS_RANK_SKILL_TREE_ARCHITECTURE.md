# Class, Rank and Skill-Tree Architecture

Status: **REVIEWABLE / SYSTEM ARCHITECTURE**
Domain: Progression / Character Development
Authority: `docs/program/05_PROGRESSION_COMBAT_SYSTEMS_PROGRAM.md`

## 1. Purpose

Define how classes, ranks, skills, abilities, passives, professions and social/faction ranks coexist without collapsing every kind of progression into one level number.

## 2. Progression layers

The game should distinguish:

- core attributes;
- skills;
- abilities/techniques;
- passives/perks;
- class/archetype;
- specialization;
- profession/civilian role;
- faction rank;
- social/citizen status;
- equipment qualification;
- titles/reputation.

These layers may interact but must not become aliases for one another.

## 3. Class model

Target direction: **class-assisted, not fully class-locked**.

A class organizes:
- recommended skill families;
- progression identity;
- access to some class techniques/passives;
- specialization routes;
- training expectations.

A class should not automatically prevent all off-class learning unless a specific system requires it.

## 4. Class record

Each authored class eventually needs:

- stable `CLASS_*` ID;
- display name;
- role fantasy;
- primary attribute relationships;
- primary skill families;
- entry requirements;
- unlock conditions;
- class-specific techniques;
- class-specific passives;
- equipment affinities/restrictions if used;
- specializations;
- progression milestones;
- conflicts/incompatibilities;
- social/faction consequences if any;
- visual/UI representation;
- respec/change rules;
- unresolved decisions.

## 5. Specialization

A specialization refines a class rather than creating an entirely separate progression system.

Each specialization may alter:
- technique availability;
- passive weighting;
- tactical role;
- resource use;
- equipment preferences;
- training routes.

Specializations must use stable IDs and explicit prerequisites.

## 6. Rank separation

The term **rank** must always identify which system it belongs to.

Potential rank namespaces:

- `CLASS_RANK`
- `ABILITY_RANK`
- `SKILL_RANK`
- `FACTION_RANK`
- `PROFESSION_RANK`
- `CITIZEN_STATUS`
- `THREAT_RANK` for beasts/encounters if adopted.

Never store a generic `rank=5` without namespace/context.

## 7. Skill-tree structure

Skill trees should be graphs, not necessarily strict trees.

Node types may include:
- technique unlock;
- passive unlock;
- modifier;
- utility action;
- resource efficiency;
- combo/synergy unlock;
- specialization gateway;
- mastery milestone.

A node record needs:
- stable ID;
- prerequisites;
- cost/training requirement;
- mutually exclusive branches if any;
- effects;
- UI position only as presentation data.

## 8. Progression sources

Advancement may come from:
- use/practice;
- training time;
- mentors/instruction;
- quests;
- discoveries;
- equipment;
- faction access;
- environmental experiences;
- beast encounters;
- knowledge;
- class milestones.

No single source should automatically dominate every progression path.

## 9. Respec/change

Global respec policy remains unresolved.

Possible future models:
- no full respec;
- limited retraining;
- specialization swap;
- cost/time-based class shift;
- story-gated change.

Any respec system must define what happens to:
- learned techniques;
- passives;
- equipment requirements;
- quest conditions;
- save compatibility.

## 10. Class versus profession

Combat/adventure class and civilian profession are separate concepts.

Examples of profession layers could include:
- technician;
- medic;
- courier;
- archivist;
- hunter;
- crafter.

A profession may grant skills, access, income or social status without defining combat identity.

## 11. Class versus citizen/social status

Social hierarchy is not a combat class.

Citizen/legal/social status can affect:
- access;
- law;
- prices;
- dialogue;
- faction treatment;
- services;
- quests.

It must not automatically grant combat power.

## 12. Beast interaction

Beasts do not need human-style classes.

Beast progression may instead use:
- species;
- age/stage;
- variant;
- adaptation;
- mutation/evolution;
- learned behavior;
- persistent adversary traits.

If a future beast class system is introduced, it requires its own explicit decision.

## 13. Current repository compatibility

Existing:
- attributes;
- skills;
- abilities;
- techniques;
- perks;
- conditions;
- equipment;
- mastery/prerequisites.

The class/rank architecture must extend these systems rather than duplicate them.

## 14. Implementation delta

Before implementation:
- lock final class philosophy;
- decide whether class is optional or mandatory;
- define initial class catalog;
- define specialization count/depth;
- define rank scales;
- define tree node schema;
- define migration from existing progression records.

## 15. Acceptance expectation

Implementation-ready when:
- at least one real class exists;
- stable class/specialization IDs exist;
- rank namespaces are fixed;
- skill-tree graph schema is fixed;
- prerequisites/effects are deterministic;
- persistence/migration is defined;
- UI projection is defined;
- tests can verify unlock and incompatibility rules.

## 16. Unknowns

- final class count;
- initial player class;
- mandatory versus optional class selection;
- level cap if any;
- respec model;
- exact rank scales;
- exact specialization depth;
- point/currency/training costs.
