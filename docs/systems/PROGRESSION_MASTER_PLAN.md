# THE GAME — Progression / Class / Rank Master Plan v0

Status: **IN_PROGRESS / DESIGN CONTRACT**  
Parent: `GAMEPLAY_SYSTEM_REBUILD_MATRIX.md`

## 1. Existing implementation baseline

Current source supports:
- seven attributes on a 0–100 authored scale;
- skills on 0–100;
- derived stats from weighted effective values;
- equipment/perk/condition modifiers;
- health/stamina/focus/resolve maxima from derived formulas;
- ability mastery XP;
- mastery stages;
- ability ranks;
- technique prerequisites;
- training and recovery time.

Current seven attributes:
- might;
- agility;
- endurance;
- intellect;
- will;
- perception;
- presence.

Current ability mastery stages:
- discovered at 0;
- unstable at 20;
- learned at 60;
- practiced at 150;
- mastered at 350.

Current default ability-rank thresholds:
- 0;
- 100;
- 300;
- 700;
- 1500;
with current default maximum rank index 4.

These are implementation facts, not automatically final balance.

## 2. Progression design principle

Progress is earned through:
- practice;
- use;
- study;
- mentors;
- equipment;
- discovery;
- quests;
- injuries/recovery;
- social/faction access;
- world opportunities.

Avoid:
- unexplained instant level jumps;
- one generic XP bar controlling every competency;
- class choice erasing prior learned capability;
- grinding loops with no world/time/resource cost.

## 3. Progression layers

Separate:
1. core attributes;
2. skills;
3. abilities;
4. techniques;
5. passives/perks;
6. classes/archetypes;
7. professions/jobs;
8. institutional ranks;
9. faction ranks;
10. citizen/social status;
11. equipment proficiency;
12. reputation/knowledge.

No one layer should substitute for all others.

## 4. Attributes

Current schema stays stable for compatibility until migration is approved.

Final decisions still required:
- base creation ranges;
- normal adult range;
- exceptional range;
- soft cap;
- hard cap;
- permanent growth cadence;
- age/injury effects;
- training ceilings;
- class/equipment interaction;
- world-level calibration.

## 5. Skills

Final skill taxonomy should use families.

Candidate families:
- combat;
- physical;
- technical;
- social;
- knowledge;
- powers;
- survival/exploration;
- profession/craft if approved.

Each skill record needs:
- ID;
- family;
- governing attribute candidates;
- training methods;
- practical use;
- check formula;
- cap/soft cap;
- prerequisites;
- known mentors/locations;
- UI category;
- combat/noncombat tags.

## 6. Ability taxonomy

Each ability:
- stable ID;
- family;
- source;
- rank;
- mastery XP;
- stage;
- techniques;
- passives;
- resource;
- prerequisites;
- costs;
- cooldown;
- drawbacks;
- counters;
- evolution paths;
- visibility.

Technique stages may keep current stage names unless later testing shows a better model.

## 7. Passives/perks

Every passive/perk must record source:
- background;
- training;
- class;
- profession;
- faction;
- equipment;
- injury/scar;
- ability;
- discovery;
- relationship;
- world event.

Duplicate effects must have stacking rules.

## 8. Class system

Target class is not a fixed “job.”

A class should represent a combat/adventure method.

Required decisions:
- class acquisition;
- multiclass or specialization;
- class prerequisites;
- class features;
- class skill affinities;
- class technique access;
- class progression;
- class switching/respec policy;
- interaction with learned skills.

Classes must not invalidate freeform skill development.

## 9. Profession system

Profession is separate from class.

Examples of function categories, not final content:
- technical;
- medical;
- logistics;
- municipal;
- military/security;
- research;
- trade;
- field work.

Profession can affect:
- income/economy;
- access;
- training;
- social status;
- schedule;
- NPC network;
- equipment familiarity.

## 10. Rank systems

Use distinct rank namespaces:
- ability rank;
- technique mastery;
- class rank;
- profession grade;
- faction rank;
- military/institutional rank;
- citizen/social status.

Never display them all as one “level.”

## 11. Player level

Final decision pending.

Options:
- no global level;
- global progression summary plus independent systems;
- level only for broad content-band guidance.

Current recommendation:
use independent progression as authority and treat any global level as a summary/unlock helper, not the sole power measure.

## 12. Training

Current engine already supports time-based training with intensity and resource costs.

Final training contract should include:
- duration;
- location;
- mentor;
- facilities;
- intensity;
- stamina/focus cost;
- injury risk;
- diminishing returns;
- skill ceiling;
- attribute influence;
- schedule/world-time consequence.

## 13. World progression

The world should not fully scale to the player.

Use:
- safe civic bands;
- low-risk field bands;
- dangerous regions;
- elite/endgame bands;
- unique exceptions.

Players may enter over-tier areas and retreat/avoid.

## 14. UI requirements

Stats/Skills must distinguish:
- base;
- effective;
- modifier source;
- mastery;
- prerequisites;
- next meaningful milestone.

Do not overwhelm phone UI with every internal formula by default.

## 15. Save migration

Any change to:
- attribute IDs;
- skill IDs;
- ability representation;
- class/rank fields;
- resource schema

requires save schema migration.

Current schema version remains 1 until migration implementation exists.

## 16. Next documents/decisions

Need:
- final skill catalog;
- class families;
- profession families;
- rank scales;
- world balance bands;
- player creation rules;
- XP/training curves;
- save migration mapping.

This v0 document is a design contract starter, not final balance.


## 17. Evolved target-game child

The current reference-game facts and starter constraints in this master feed the reconstruction-grade target design in:

- `PROGRESSION_CLASSES_RANKS_EVOLVED_GAME_DESIGN.md`

That child owns the deliberate evolution of this domain: how the current seven attributes, 23-skill foundation, derived values, resources, training, abilities and mastery expand into the intended class, specialization, profession, rank, mentor, facility, world-access and progression-content systems.

This master remains a baseline authority. The evolved child does not claim its target features are implemented.
