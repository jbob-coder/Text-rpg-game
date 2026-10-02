# THE GAME — Mechanics Rework & Rebuild Program

Status: **SYSTEM ARCHITECTURE PLANNING**
Rule: mechanics may be broken/replaced only after the replacement contract, migration, tests, and persistence implications are documented.

## 1. Preserve the core state architecture

Target flow remains:

`GameState -> World/Quest/Narrative -> Rules/Stats/Abilities/Equipment -> Player-safe projection -> Android UI`

UI must not become the source of truth.

## 2. System disposition categories

Every mechanic receives one of:
- KEEP;
- EXTEND;
- REWORK;
- REPLACE;
- DEPRECATE;
- DELETE;
- DEFER.

Every REPLACE/DELETE decision needs:
- current behavior;
- reason;
- replacement;
- migration;
- save impact;
- tests;
- rollback.

## 3. Existing systems to preserve unless later migrated

- stable content IDs;
- quest/state model;
- knowledge separation;
- player-safe projection;
- inventory/equipment ownership by engine;
- save persistence;
- authored choice consequences;
- NPC relationship/story state;
- world-map graph as authoritative travel state.

## 4. Systems likely to require expansion/rework

### Stats
Need a full stats bible covering:
- attributes;
- derived stats;
- resources;
- conditions;
- caps;
- modifiers;
- provenance;
- temporary/permanent changes;
- UI explanation;
- balance.

### Abilities
Need:
- ability families;
- techniques;
- passives;
- resource costs;
- cooldowns;
- mastery;
- discovery;
- counters;
- drawbacks;
- progression.

### Skills
Need:
- skill categories;
- training;
- checks;
- diminishing returns;
- prerequisites;
- role in combat/noncombat;
- NPC skill use.

### Classes and ranks
Not yet locked.

Documentation must decide whether "class" means:
- profession;
- combat archetype;
- social rank;
- ability specialization;
- formal institution rank;
or a combination.

Avoid locking a class system merely because RPGs traditionally have one.

### Activities
Need framework for:
- training;
- work;
- research;
- travel;
- rest;
- social interaction;
- crafting/repair only if adopted;
- exploration;
- combat;
- gathering;
- investigation.

## 5. Tactical combat direction

The combat system should become an original turn-based tactical layer.

Genre-level inspiration may include:
- action points;
- grid/position;
- cover;
- line of sight;
- overwatch/reaction concepts;
- squad coordination;
- terrain;
- status effects.

Do not reproduce another game's:
- exact class names;
- UI layout;
- mission templates;
- formulas;
- icons;
- terminology;
- enemy designs;
- progression trees.

### Required combat documentation

#### Encounter setup
- participants;
- teams/factions;
- map;
- objectives;
- retreat;
- surprise;
- starting positions.

#### Turn system
Decide:
- alternating units;
- team turns;
- initiative queue;
- hybrid.

#### Action economy
Define:
- movement;
- attack;
- ability;
- item;
- interact;
- guard/reaction;
- sprint;
- retreat.

#### Accuracy and targeting
Define:
- base accuracy;
- range;
- cover;
- elevation;
- movement penalty;
- status modifiers;
- criticals;
- body/part targeting only if adopted.

#### Damage and defense
Define:
- damage;
- armor;
- penetration;
- shields;
- resistances;
- injury;
- downed/death;
- healing.

#### Terrain
Define:
- cover;
- line-of-sight blockers;
- elevation;
- hazards;
- destructibility only if technically supported;
- doors;
- choke points.

#### AI
Define:
- goals;
- threat assessment;
- morale;
- retreat;
- coordination;
- memory;
- faction doctrine.

## 6. Persistent rival/adversary system

Target: an original persistent enemy-memory system.

Use broad ideas only:
- a surviving enemy remembers the player;
- encounters change relationships;
- enemies develop goals;
- status/rank may change through world events;
- wounds/scars may persist;
- enemies may return.

Do not copy proprietary branded structure, terminology, exact hierarchy UI, or character-generation patterns.

### Original system components

#### Adversary identity
- stable NPC/adversary ID;
- faction;
- rank;
- personality;
- skills;
- equipment;
- goals.

#### Encounter memory
- who won;
- who fled;
- injuries;
- witnesses;
- abilities observed;
- allies lost;
- humiliation/respect;
- debts.

#### Relationship axes
Potential original axes:
- hostility;
- caution;
- respect;
- fear;
- obsession;
- debt;
- rivalry intensity.

Final axes require separate design.

#### World consequence
A rival may:
- change route;
- prepare counters;
- seek allies;
- avoid the player;
- challenge the player;
- rise/fall in faction standing;
- affect rumors/reputation.

All changes must be authored/systemic and persist through saves.

## 7. World-level balance

Avoid full level scaling.

Plan:
- regions have danger ranges;
- beasts/NPCs have intrinsic power ranges;
- player can enter dangerous areas early;
- information/signage/NPC warnings communicate risk;
- events can change local danger;
- elite entities remain exceptional.

Need formulas for:
- level/rank;
- stats per rank;
- equipment quality;
- ability power;
- rewards;
- XP/progression;
- encounter budget;
- death/injury consequences.

## 8. Loot/equipment

Need decision on:
- rarity;
- quality;
- durability;
- repair;
- crafting;
- material tiers;
- slot limits;
- set bonuses;
- random rolls;
- unique items;
- theft;
- ownership.

Do not add systems because the art roadmap contains generic equipment templates.

## 9. Social mechanics

Need:
- relationship axes;
- reputation;
- faction standing;
- social class;
- law/crime;
- discrimination/prejudice if canon;
- persuasion/intimidation;
- memory;
- rumors.

If social prejudice is implemented, it must be regional/stateful and applied through NPC/world rules, not a simplistic global stat bonus/penalty.

## 10. NPC simulation

Need:
- goals;
- schedules;
- needs;
- memory;
- knowledge;
- relationships;
- work/home;
- travel;
- inventory;
- combat willingness;
- fear;
- faction;
- death/absence;
- world event response.

## 11. Mechanics likely to be broken/rebuilt later

Possible rebuild candidates:
- any UI-owned rule calculation;
- duplicated derived-stat calculations;
- flat map travel assumptions incompatible with global world scale;
- placeholder encounter logic;
- one-off scene effects that need reusable systems;
- hardcoded NPC presence;
- hardcoded character panels;
- generic all-purpose location action menus;
- any future combat prototype that bypasses engine state.

## 12. Documentation order before implementation

1. Stats Bible.
2. Skill Bible.
3. Ability/Passive Bible.
4. Class/Rank decision.
5. Progression/level balance.
6. Item/equipment/loot.
7. NPC simulation.
8. Social/faction/law.
9. Tactical combat.
10. Persistent rival system.
11. World integration.
12. Save/migration.
13. UI projection.
14. tests/QA.

## 13. Copyright/originality rule

External games may be cited internally as genre inspiration, but the shipped implementation must use original:
- names;
- formulas;
- data structures where expressive choices matter;
- content;
- visuals;
- UI;
- progression;
- factions;
- enemies;
- narrative.

The goal is similar player-facing depth, not duplication.
