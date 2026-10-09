# THE GAME — Progression, Classes & Ranks: Evolved Game Design

Status: **ACTIVE TARGET-GAME DESIGN / RECONSTRUCTION-GRADE / IMPLEMENTATION DEFERRED**  
Repository: `jbob-coder/Text-rpg-game`  
Program branch: `docs/master-game-development-program`  
Parent authorities:
- `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`
- `docs/FINAL_GAME_RECONSTRUCTION_BLUEPRINT.md`
- `docs/systems/PROGRESSION_MASTER_PLAN.md`
- `docs/systems/GAMEPLAY_SYSTEM_REBUILD_MATRIX.md`

Purpose: define how the progression layer of the existing game evolves into the intended full game. This document is a **game-design authority**, not a migration task and not a claim that the target systems are already implemented.

---

## 0. Design interpretation

The current repository is the **reference game**.

The objective is not to preserve every current limitation and it is not to rebuild the current implementation one-for-one. The objective is to understand what the game already is, preserve the parts that define its identity, and deliberately evolve those foundations into a larger, deeper, more coherent game.

For this domain, the working sequence is:

`CURRENT REALITY -> PRESERVE IDENTITY -> EVOLVE DESIGN -> DEFINE CREATION REQUIREMENTS -> IMPLEMENT LATER`

Every section below therefore distinguishes between:

- **CURRENT REALITY** — facts supported by current repository source/content;
- **PRESERVE** — current ideas that remain part of the evolved game's identity;
- **EVOLVED TARGET** — the intended fuller game design;
- **CREATION REQUIREMENTS** — content, records, UI, balancing, assets, and future implementation needed to realize the target.

Where exact balance values are not yet justified, the system behavior is defined while numeric tuning remains provisional.

---

# 1. CURRENT REALITY — progression foundation already present

## 1.1 Core attributes

Current source defines seven authoritative player attributes on a 0–100 authored range:

- **Might** — raw physical force;
- **Agility** — movement, coordination, reaction;
- **Endurance** — fatigue tolerance and resilience;
- **Intellect** — reasoning and technical learning;
- **Will** — mental resistance and discipline;
- **Perception** — awareness, danger detection, tells;
- **Presence** — social force and leadership.

Current validation rejects unknown attribute IDs and non-finite values.

### Current design significance

This is already a broad enough foundation to support combat, exploration, technical activity, social play, survival, powers, and professions without requiring a replacement attribute set.

The evolved game therefore treats the seven attributes as a recognizable foundation rather than disposable prototype data.

---

## 1.2 Skills

Current source registers 23 skills:

### Combat
- unarmed;
- blades;
- ranged;
- defense;
- tactics.

### Physical
- athletics;
- stealth;
- traversal;
- survival.

### Technical
- engineering;
- technical_systems;
- medicine;
- crafting.

### Social
- persuasion;
- deception;
- intimidation;
- empathy;
- leadership.

### Knowledge
- investigation;
- history;
- factions;
- powers;
- creatures.

Current skill values are validated in the 0–100 range.

Current training can improve registered skills over world time, consumes stamina/focus, supports training intensity and mentor bonus, and applies diminishing returns at higher skill values.

### Current design significance

The game already treats competence as **domain-specific** rather than deriving every action directly from attributes. That is a strong identity feature and should be expanded rather than flattened into a generic character level.

---

## 1.3 Derived values

Current source calculates nine derived values:

- max health;
- max stamina;
- max focus;
- max resolve;
- initiative;
- accuracy;
- evasion;
- guard;
- carry capacity.

These values are built from authoritative attributes/skills and modifier sources instead of being independently owned by the UI.

Current equipment, perks, conditions, and equipment-set effects can modify inputs or derived values.

### Current design significance

The evolved game should preserve the rule that derived combat/survival values are **consequences of the player's build and state**, not arbitrary parallel stats that drift away from the underlying character.

---

## 1.4 Core resources

Current authoritative resources are:

- health;
- stamina;
- focus;
- resolve.

Their maxima are derived from the stat system. Current state initialization clamps resources to valid maxima and supports bounded recovery.

### Current design significance

These four resources provide a useful split:

- health = physical survival;
- stamina = physical exertion;
- focus = precision, concentration, technical/power exertion;
- resolve = mental/social resistance and sustained will.

The evolved design keeps these as the core universal resources. Specific powers or special systems may own additional dedicated resources without replacing them.

---

## 1.5 Ability progression

Current ability state supports:

- ability ID;
- rank;
- mastery XP;
- mastery stage;
- technique records;
- power-specific data.

Current ability mastery stages are:

1. discovered;
2. unstable;
3. learned;
4. practiced;
5. mastered.

Current default ability-rank thresholds derive rank from accumulated mastery XP.

Current technique discovery can require combinations of:

- ability rank;
- mastery XP;
- attributes;
- skills;
- flags;
- items;
- knowledge;
- perks;
- other techniques.

### Current design significance

The game already supports progression through **use, discovery, requirements, and mastery**, rather than only through a level-up menu. This should become one of the defining systems of the full game.

---

## 1.6 Training and world time

Current source already supports:

- time advancement;
- skill training;
- slow attribute training;
- resource expenditure;
- recovery;
- timed conditions;
- mentor bonus;
- diminishing returns.

Training is not free: it consumes character resources and advances world time.

### Current design significance

This establishes a crucial target principle:

> Character growth happens inside the world and costs something inside the world.

The evolved game should make training locations, teachers, schedules, injuries, money, access, faction membership, equipment, and world events meaningful to progression.

---

## 1.7 Player-facing progression projection

Current player-safe status projection exposes:

- identity;
- attributes;
- resources;
- derived values;
- skills;
- abilities;
- visible conditions.

Current inspection APIs deliberately redact hidden perk/condition provenance where required.

### Current design significance

The evolved progression UI must remain a **projection of authoritative game state**. The Android client may organize, explain, filter, and visualize progression, but it must not become the owner of progression rules.

---

## 1.8 Current playable baseline

The current provisional vertical slice, **The Dead Relay**, starts with:

Attributes:
- Might 30;
- Agility 35;
- Endurance 35;
- Intellect 45;
- Will 40;
- Perception 40;
- Presence 30.

Initial authored skills:
- Athletics 20;
- Technical Systems 25;
- Investigation 20;
- Persuasion 15.

Initial resources:
- Health 100;
- Stamina 70;
- Focus 60;
- Resolve 50.

This is current provisional content evidence, not a universal final starting build.

---

# 2. PRESERVE — progression identity of THE GAME

The evolved game preserves these principles.

## 2.1 Independent growth

A player does not become better at everything because one global number increased.

Someone who spends weeks repairing municipal systems should become better at technical work. Someone who repeatedly survives dangerous field operations should grow in relevant physical, combat, tactical, survival, and ability competencies. Someone who builds relationships, studies institutions, or works inside a faction should gain different advantages.

Progression must reflect **what the character actually does**.

## 2.2 Stable character foundation

The seven attributes remain the core physical/mental/social foundation unless a later explicit redesign proves a replacement is superior.

They should change slowly relative to skills.

## 2.3 Skills represent learned competence

Skills grow faster than attributes and are the main expression of learnable capability.

## 2.4 Abilities are discovered and mastered

Abilities and techniques are not ordinary inventory unlocks. Their growth can require practice, knowledge, story circumstances, teachers, equipment, conditions, risk, or repeated use.

## 2.5 Time matters

Training, work, recovery, research, travel, and study consume world time.

Time is therefore part of progression balance.

## 2.6 World access matters

Who teaches the player, what facilities are available, which regions are reachable, which factions trust the player, and what the player knows can all change what progression routes exist.

## 2.7 Builds remain legible

The player should be able to understand why Jack is good or bad at something and what actions could improve him.

Complexity belongs in the system, not in unexplained numbers.

---

# 3. EVOLVED TARGET — progression is a network, not one ladder

The full game uses the following progression layers:

1. **Attributes** — slow-changing foundational capability.
2. **Skills** — trainable learned competency.
3. **Derived values** — calculated practical capability.
4. **Resources** — current expendable capacity.
5. **Abilities** — exceptional/special capability families.
6. **Techniques** — concrete methods inside abilities.
7. **Passives and perks** — persistent learned, earned, or situational traits.
8. **Combat class** — a developed combat/adventure discipline.
9. **Specialization** — a narrower direction inside a class or capability family.
10. **Profession** — civilian/economic/technical occupation.
11. **Institutional rank** — formal authority inside an organization.
12. **Faction rank** — standing inside a faction.
13. **Social/legal status** — world-recognized civic position.
14. **Reputation** — how specific groups/people view the player.
15. **Knowledge** — facts, secrets, technical understanding, cultural understanding.
16. **Equipment proficiency** — familiarity with classes of equipment where meaningful.
17. **World access** — locations, services, mentors, licenses, contacts, and opportunities opened by the above systems.

No single layer replaces the others.

---

# 4. Attributes — evolved design

## 4.1 Attribute role

Attributes describe **capacity**, not expertise.

Examples:

- high Might can make heavy physical tasks easier but does not teach sword technique;
- high Intellect can accelerate understanding but does not automatically grant Engineering;
- high Presence can strengthen social pressure but does not substitute for Empathy or Factions knowledge;
- high Agility can support weapon handling but does not automatically make the player an expert marksman.

## 4.2 Growth rate

Attribute growth is intentionally slow.

Target sources include:

- sustained physical conditioning;
- long-term study/mental discipline;
- major recovery or rehabilitation;
- rare transformative events;
- exceptional ability effects where explicitly authored;
- permanent injuries that may reduce or constrain capacity.

Routine quest completion should not award arbitrary attribute points.

## 4.3 Attribute ceilings

The current 0–100 representation is retained as the design scale.

The evolved game should distinguish:

- ordinary starting capability;
- trained adult capability;
- exceptional human capability;
- extreme capability;
- supernatural/special enhancement where the setting permits it.

Exact boundaries are a balance task, but the game should avoid casually filling multiple attributes to 100.

## 4.4 Creation requirement

Create a future **Attribute Calibration Table** that defines:

- starting ranges;
- population reference bands;
- long-term training rates;
- injury effects;
- enhancement rules;
- world NPC comparison bands;
- checks against current derived-stat formulas.

---

# 5. Skills — evolved design

## 5.1 Skill architecture

The current 23 skills remain the base catalog for the first evolved design pass.

They should become part of a structured registry containing, for every skill:

- stable ID;
- display name;
- family;
- description;
- governing attribute relationships;
- common training methods;
- world activities that grant practice;
- mentors/facilities;
- equipment dependencies;
- opposed-use rules;
- check usage;
- passive benefits if any;
- tactical-combat use;
- noncombat use;
- related professions;
- related classes;
- UI icon/category;
- visibility/discovery policy.

## 5.2 Skill growth sources

Skill growth can come from:

- deliberate training;
- successful practical use;
- failed practical use where learning is plausible;
- formal education;
- mentorship;
- books/manuals/data;
- work;
- combat;
- quests only when the quest actually exercises or teaches the skill.

Quest rewards should usually unlock **opportunities**, knowledge, resources, teachers, equipment, or access rather than handing out unrelated skill XP.

## 5.3 Practice quality

Not all practice is equal.

Target training calculation should eventually account for:

- duration;
- intensity;
- teacher quality;
- facility quality;
- equipment quality;
- character fatigue;
- injury;
- relevant attributes;
- current skill;
- novelty;
- repeated-drill diminishing returns;
- danger/stress when learning in live conditions.

## 5.4 Skill plateaus

Higher skill values should increasingly require better practice conditions.

A player should not reach elite technical or combat mastery by repeating a trivial beginner action indefinitely.

Target progression introduces **plateau gates** such as:

- advanced teacher;
- advanced facility;
- live practice;
- certification/exam;
- special knowledge;
- dangerous field experience;
- specialized equipment;
- technique challenge.

These gates are contextual, not identical for every skill.

---

# 6. Mastery descriptors

The game should present numeric skill values internally but also communicate meaningful qualitative bands.

Working target bands:

- **Unfamiliar** — little or no practical competence;
- **Novice** — understands basics;
- **Trained** — reliable routine competence;
- **Skilled** — strong practical ability;
- **Expert** — advanced professional/field performance;
- **Master** — exceptional command;
- **Exceptional** — rare top-end capability.

Exact numeric thresholds remain a balancing task.

These descriptors must never replace the underlying numeric state; they exist to make progression understandable.

---

# 7. Derived values and resources — evolved design

## 7.1 Preserve calculated ownership

Derived values continue to be calculated from authoritative inputs.

The target game may add additional derived values only where they represent a useful reusable rule.

Potential future values include:

- movement allowance;
- reaction capacity;
- stability;
- resistance categories;
- medical recovery rate;
- concealment capability;
- technical handling;
- social composure.

Do not create a derived value merely because a UI screen has space.

## 7.2 Resource model

Universal resources remain:

- Health;
- Stamina;
- Focus;
- Resolve.

Ability families may define their own resource where their fiction and mechanics require it.

Class features should generally **interact with** resources rather than create dozens of new universal bars.

---

# 8. Abilities and techniques — evolved design

## 8.1 Ability

An ability is a coherent exceptional capability family.

An ability record should eventually describe:

- origin/source;
- family;
- discovery state;
- rank;
- mastery;
- resource model;
- known techniques;
- hidden discoverable techniques;
- passive effects;
- drawbacks;
- failure states;
- counters;
- evolutions;
- training methods;
- teachers/research sources;
- legal/social implications where applicable.

## 8.2 Technique

A technique is a learned executable method inside an ability.

Techniques should have their own mastery because knowing an ability does not mean mastering every use of it.

Technique improvement can affect:

- reliability;
- resource cost;
- speed;
- range;
- precision;
- control;
- secondary effects;
- failure chance;
- recovery burden.

## 8.3 Discovery

Techniques can be discovered through:

- experimentation;
- mentor instruction;
- observation;
- records/manuals;
- story events;
- combat insight;
- environmental interaction;
- combining prior techniques;
- reaching a mastery threshold.

Discovery must feel connected to player behavior and world knowledge.

## 8.4 Ability evolution

Ability evolution is not a generic level-up choice.

An evolution should be caused by a combination of:

- mastery;
- repeated use pattern;
- learned knowledge;
- meaningful decisions;
- physiological/mental adaptation;
- rare materials or equipment where appropriate;
- critical story/world conditions.

The player may see partial hints without exposing hidden requirements prematurely.

---

# 9. Passives and perks — evolved design

Passives/perks represent persistent effects that do not belong in base attributes or ordinary skills.

Every passive/perk must have a recorded source.

Sources include:

- background;
- class;
- specialization;
- profession;
- training;
- faction;
- institutional rank;
- equipment;
- injury/scar;
- ability;
- discovery;
- relationship;
- world event.

Each record needs:

- stacking rule;
- visibility;
- modifier/effect ownership;
- removal policy if removable;
- source provenance.

Hidden perks may affect rules while remaining redacted through player-safe projections where the game intentionally withholds the cause.

---

# 10. Combat classes — evolved design

## 10.1 What a class means

A class is the character's developed **combat/adventure discipline**.

It is not:

- the player's job;
- social class;
- legal status;
- faction membership;
- total character identity.

A player can change jobs without losing combat training. A player can leave a faction without forgetting how to fight. A doctor can be a highly trained combatant. A technically focused character can become dangerous without being renamed as a different profession.

## 10.2 Acquisition

Classes are **earned**, not selected from a permanent menu at character creation.

A class becomes available when the player's demonstrated competencies satisfy its entry pattern.

Possible requirements:

- attribute minimums;
- relevant skills;
- learned techniques;
- training history;
- mentor;
- field experience;
- equipment familiarity;
- knowledge;
- institutional access.

## 10.3 Working class families

The first target class architecture uses seven functional families. Names are working design names; functionality is more authoritative than final world-facing terminology.

### Vanguard

Identity:
direct engagement, protection, pressure, staying power.

Likely foundations:
- Might;
- Endurance;
- Defense;
- Unarmed or Blades;
- Resolve.

Gameplay direction:
- hold dangerous positions;
- protect allies;
- force enemy movement;
- endure pressure;
- close-range control.

### Skirmisher

Identity:
mobility, positioning, ranged or agile engagement.

Likely foundations:
- Agility;
- Perception;
- Ranged;
- Athletics;
- Traversal or Stealth.

Gameplay direction:
- reposition;
- exploit sight lines;
- precision attacks;
- disengage;
- pursue;
- scout dangerous routes.

### Operator

Identity:
technical systems, devices, battlefield/environment control.

Likely foundations:
- Intellect;
- Perception;
- Technical Systems;
- Engineering;
- Investigation.

Gameplay direction:
- manipulate infrastructure;
- deploy/use technical tools;
- analyze systems;
- disable hazards;
- create tactical environmental advantages.

This family connects naturally to the existing Gate Twelve municipal/relay/technical gameplay without making the entire game a technical class game.

### Field Specialist

Identity:
survival, medicine, logistics, recovery, field support.

Likely foundations:
- Endurance;
- Intellect;
- Medicine;
- Survival;
- Crafting or Engineering.

Gameplay direction:
- stabilize injuries;
- improve recovery;
- maintain field readiness;
- handle dangerous environments;
- support long expeditions.

### Investigator

Identity:
awareness, deduction, knowledge exploitation, information control.

Likely foundations:
- Perception;
- Intellect;
- Investigation;
- Factions;
- History or Creatures.

Gameplay direction:
- reveal options;
- detect contradictions;
- identify weaknesses;
- reconstruct events;
- expose hidden routes or motives when knowledge supports it.

### Envoy

Identity:
leadership, negotiation, intimidation, social coordination.

Likely foundations:
- Presence;
- Will;
- Persuasion;
- Empathy;
- Leadership, Deception, or Intimidation.

Gameplay direction:
- negotiate;
- coordinate allies;
- influence group morale;
- gain access;
- manipulate or resolve conflicts;
- create social options unavailable to purely combat-focused builds.

### Ability Specialist

Identity:
deep mastery of exceptional abilities and their techniques.

Likely foundations:
- varies by ability;
- Powers knowledge;
- Focus/Resolve;
- ability mastery;
- technique mastery.

Gameplay direction:
- higher control;
- specialized technique interactions;
- reduced drawbacks through mastery;
- advanced evolution paths.

An Ability Specialist is not automatically a stronger character in every situation. It trades breadth for deep exceptional capability.

---

# 11. Specializations

Each combat class may later branch into specializations.

Specialization rules:

- a specialization narrows or transforms a class's play pattern;
- it should not erase previously learned capability;
- it may unlock class features, techniques, reactions, training efficiencies, or equipment handling;
- specialization should emerge from demonstrated play rather than arbitrary menu selection where practical;
- cross-class competence remains possible.

Example structure:

`class family -> class progression -> specialization -> advanced features`

Exact specialization names and counts are a later class-content packet.

---

# 12. Multiclass / cross-training model

The target game allows cross-training.

It should be possible to build, for example:

- a technical Operator who learns Skirmisher mobility;
- an Investigator with Envoy social tools;
- a Vanguard with strong Medicine;
- an Ability Specialist whose profession remains municipal technician.

However, cross-training costs time and opportunity.

The design should discourage effortless completion of every class tree in one playthrough through:

- world-time cost;
- mentor availability;
- training requirements;
- conflicting schedules;
- faction/institution access;
- difficult advanced prerequisites;
- specialization depth.

The limit is **opportunity cost**, not arbitrary hard lockouts.

---

# 13. Profession — separate from class

Profession describes sustained work/economic/social function.

Target profession families include:

- technical/infrastructure;
- medical;
- logistics;
- municipal/civic;
- security/military where world canon supports it;
- research;
- trade;
- field work;
- craft/maintenance;
- information/records;
- other world-specific occupations created during settlement design.

Profession affects:

- income;
- schedule;
- legal/work access;
- social network;
- equipment familiarity;
- practical skill use;
- institutional reputation;
- training opportunity;
- housing/services where relevant;
- quests/events.

Profession advancement should involve actual work, qualification, reputation, and organizational conditions—not only XP.

---

# 14. Rank namespaces

The evolved game explicitly separates rank systems.

## 14.1 Ability rank

Measures progression of one ability family.

## 14.2 Technique mastery

Measures practical mastery of a specific technique.

## 14.3 Class progression

Measures development inside a combat/adventure discipline.

## 14.4 Profession grade

Measures professional qualification or responsibility.

## 14.5 Institutional rank

Formal authority inside an institution.

## 14.6 Faction rank

Standing/position inside a faction.

## 14.7 Citizen/social status

Civic/legal/social position recognized by a society.

## 14.8 Reputation

Perception by specific NPCs, groups, settlements, or institutions.

These namespaces remain distinct even though the Status UI now includes a real global **Level**. Level must not be mistaken for profession grade, faction rank, institutional authority, class progression, or reputation.

---

# 15. Global player Level policy — owner-canon update

The evolved target now includes a real in-universe **Level** as part of the human Status UI.

Owner-established rules:

- all humans receive the Status UI at age 18;
- Level progression is tied to kills, including beasts and PK;
- reaching Level 100 is extraordinarily rare;
- only two humans in known history have reached Level 100 so far;
- Level 100 creates the exceptional possibility of changing/replacing the otherwise fixed awakened primary ability.

Level is therefore not merely a UI summary.

However, Level does **not** replace the rest of the progression network and must not automatically determine every capability.

The true character remains the combination of:

- Level;
- attributes;
- skills;
- primary ability;
- ability mastery and techniques;
- passives;
- class development;
- profession;
- equipment;
- conditions;
- knowledge;
- reputation;
- faction/institutional status;
- world access.

The full XP curve, kill-credit rules, assists/party contribution, anti-exploit behavior, level rewards, and exact Level-100 transition are owned by the Status/Abilities/Passives documentation program.

Authority:
- `STATUS_UI_ABILITIES_AND_PASSIVES_MASTER_PLAN.md`

The world still must not automatically scale to Jack's Level.

---

# 16. Class progression structure

Each class should eventually have four kinds of advancement:

1. **Foundation** — entry competency and basic discipline.
2. **Practice** — repeated use and training.
3. **Field proof** — meaningful real-world application.
4. **Specialization** — focused advanced direction.

A class should not advance only by killing enemies.

Examples of class-relevant proof:

- Vanguard: successfully protecting another actor under pressure;
- Skirmisher: solving combat through positioning/precision;
- Operator: restoring or manipulating a dangerous system;
- Field Specialist: preserving lives/resources during an expedition;
- Investigator: uncovering actionable information;
- Envoy: changing a conflict through social leverage;
- Ability Specialist: safely controlling advanced ability behavior.

These examples define the philosophy, not hardcoded achievements.

---

# 17. Training ecosystem

The evolved game turns training into a world system.

Training records should eventually account for:

- activity ID;
- skill/attribute/ability target;
- location;
- facility;
- mentor;
- equipment;
- duration;
- intensity;
- resource cost;
- money/material cost where applicable;
- prerequisites;
- risk;
- interruption;
- world-time consequence;
- learning yield;
- plateau state.

Training locations become meaningful world content.

Examples:

- municipal workbench;
- clinic/medical facility;
- archive/research station;
- practice yard;
- firing/training range where world canon permits;
- wilderness route;
- faction facility;
- private mentor location.

A facility is not merely flavor text if it changes what can be learned there.

---

# 18. Mentors and teachers

Mentors should be persistent NPCs with their own:

- identity;
- location/schedule;
- knowledge;
- teaching specialties;
- relationship requirements;
- faction/institution restrictions;
- price or exchange requirements where appropriate;
- personal goals;
- availability.

A mentor can:

- accelerate learning;
- unlock a plateau;
- teach a technique;
- reveal a hidden requirement;
- evaluate the player;
- refuse instruction;
- provide specialized practice.

Mentorship links progression to the NPC/social game rather than isolating it in menus.

---

# 19. Knowledge as progression

Knowledge is a progression layer in its own right.

Knowing something can:

- expose a dialogue option;
- reveal an enemy weakness;
- unlock a safe technical procedure;
- enable an advanced technique;
- reveal a faction custom;
- reduce uncertainty;
- make a training method available;
- allow the player to recognize valuable materials/items;
- change the interpretation of a scene.

Knowledge should not always increase a numeric stat.

This preserves the existing game's strong knowledge/state architecture and expands its practical importance.

---

# 20. Injury, failure, and recovery

Progression must include setbacks without casually destroying the player's build.

Target rules:

- temporary conditions can reduce effective values;
- injuries can require treatment/rest/rehabilitation;
- severe events may create long-term consequences;
- training while exhausted/injured can be inefficient or dangerous;
- failure can still create learning when plausible;
- permanent losses must be rare, explicit, and narratively/mechanically justified.

Recovery systems create meaningful roles for Medicine, facilities, NPCs, supplies, and time.

---

# 21. Equipment relationship

Equipment should amplify or enable a build, not replace character development.

Equipment may:

- modify attributes/skills/derived values;
- enable techniques;
- reduce costs;
- add utility;
- protect against hazards;
- change tactical options.

Equipment should not automatically teach a skill simply because it is equipped.

Where proficiency matters, poor familiarity can reduce effectiveness until trained.

---

# 22. World integration

Progression and world design must interlock.

Regions and settlements can differ in:

- available professions;
- mentors;
- facilities;
- institutions;
- equipment;
- knowledge;
- legal restrictions;
- faction training;
- danger;
- economic opportunity.

This means travel can change the player's growth possibilities.

The world should **not** scale every challenge to the player. Progression should sometimes allow the player to return to a previously dangerous area with visibly greater capability.

---

# 23. Social and institutional integration

Rank must have concrete consequences.

Institutional/faction/profession status can influence:

- restricted areas;
- services;
- equipment access;
- information access;
- NPC treatment;
- prices only where the economy system supports it;
- responsibilities;
- scheduled duties;
- quests/events;
- legal authority.

Higher rank also creates obligations.

Advancement should not be pure benefit. Authority can produce:

- duties;
- political consequences;
- enemies;
- expectations;
- reduced freedom;
- accountability for failure.

---

# 24. NPC parity

NPCs should use the same conceptual progression vocabulary where appropriate.

Important NPCs can have:

- attributes;
- skills;
- professions;
- class capabilities;
- abilities;
- injuries;
- faction/institution ranks;
- reputation;
- knowledge.

The game does not need to simulate every background citizen at full player fidelity, but important NPC capability should not be invented ad hoc each time a scene needs it.

This supports consistent recurring allies, rivals, mentors, and adversaries.

---

# 25. Tactical combat integration

The tactical-combat system should consume progression state rather than own a separate RPG.

Examples:

- Initiative derives from existing character capability;
- Accuracy and Evasion use authoritative derived values;
- combat skills matter;
- class features create tactical options;
- abilities/techniques use their normal mastery/resources;
- injuries persist back into world state;
- equipment remains the same equipment;
- NPC progression can persist across encounters.

Combat rewards should include contextual learning, loot/provenance, reputation, knowledge, injuries, relationships, and world consequences—not just generic combat XP.

---

# 26. Activities and life-loop integration

The progression system is consumed by the broader activity system.

Activities include:

- work;
- study;
- training;
- research;
- medical recovery;
- exploration;
- social interaction;
- faction duties;
- equipment maintenance;
- travel;
- combat preparation.

A day spent training is a day not spent working, traveling, researching, helping an NPC, or pursuing another opportunity.

This creates strategic character development without requiring artificial energy timers outside the game world.

---

# 27. Player-facing progression UX

The evolved mobile interface should make the system deep but readable.

## 27.1 Character overview

Show:

- identity;
- current condition;
- core resources;
- seven attributes;
- major build summary;
- active profession/class;
- important ranks;
- currently relevant progression goals.

## 27.2 Skills

Group by family.

For each skill show:

- base;
- effective;
- mastery descriptor;
- recent progress;
- next known improvement opportunity;
- relevant modifiers;
- known training options.

## 27.3 Abilities

Show:

- ability identity;
- rank;
- mastery stage;
- resource;
- known techniques;
- technique mastery;
- visible evolution hints;
- drawbacks/cooldowns.

## 27.4 Classes

Show:

- active/developed class families;
- earned features;
- specialization progress;
- demonstrated requirements;
- known unmet requirements where player knowledge allows them to be shown.

## 27.5 Profession/rank

Separate screen/panel group for:

- profession;
- institutional rank;
- faction position;
- civic/social status.

Do not mix these into combat class.

## 27.6 Explanation

The UI should answer:

- Why is this value what it is?
- What changed it?
- What can I do to improve it?
- What does improving it actually affect?

Hidden authored information remains hidden.

---

# 28. Progression feedback

Growth should be visible in the world.

Examples:

- new dialogue acknowledgement;
- easier traversal;
- different technical options;
- better combat handling;
- access to advanced training;
- NPC recognition;
- professional responsibility;
- ability-control changes;
- equipment that becomes practical to use;
- new solutions to old types of problems.

The player should not need to stare at numbers to know that Jack has developed.

---

# 29. Balance philosophy

## 29.1 No mandatory grinding

Routine repetition should eventually produce sharply reduced value.

Meaningful progress comes from new difficulty, better instruction, new environments, and actual application.

## 29.2 Breadth versus depth

Broad characters gain flexibility.

Specialists gain access to difficult high-end actions.

Neither approach should make the other invalid.

## 29.3 Build viability

The game should support multiple strong identities, including:

- combat-heavy;
- technical;
- investigative;
- social;
- survival/support;
- ability-focused;
- hybrid.

Not every route must solve every problem.

## 29.4 World remains dangerous

Progression can make earlier threats easier, but not all danger should become trivial.

Threat also depends on numbers, preparation, environment, information, injuries, equipment, and tactical situation.

---

# 30. Gate Twelve — first evolved progression proof packet

Gate Twelve should become the first region where the evolved progression philosophy is demonstrated.

The first proof packet should exercise:

### Technical route
- Technical Systems;
- Engineering;
- Intellect;
- Perception;
- Operator-oriented development.

### Investigation route
- Investigation;
- Perception;
- relevant knowledge;
- Investigator-oriented development.

### Social route
- Persuasion;
- Empathy;
- Presence;
- relationship state;
- Envoy-oriented development.

### Physical route
- Athletics;
- Traversal;
- Endurance/Agility;
- physical access or risk-management opportunities.

### Ability route
- discovered ability;
- mastery progression;
- technique discovery;
- resource control;
- drawback/recovery.

These routes should overlap rather than create seven isolated versions of the story.

A technically skilled player may uncover information that improves a social route. An Investigator may identify a safer physical route. An NPC relationship may expose a training opportunity.

This interdependence is the target.

---

# 31. Character-development example

A representative evolved play sequence could look like:

1. Jack reaches Gate Twelve with the current generalist baseline.
2. Technical investigation improves Technical Systems through real use.
3. Tamsin becomes a potential mentor/contact based on relationship and events.
4. Repair work opens an Operator-style progression route.
5. Exploration reveals knowledge tied to Trace.
6. Trace use creates ability mastery but also resource/recovery pressure.
7. The player chooses to spend time training control instead of pursuing another immediate opportunity.
8. Improved capability later changes available approaches to a district problem.
9. Continued technical work may produce a profession opportunity independently of combat class.
10. Institutional/faction choices may later create rank or access without rewriting the player's core skills.

The important point is that one story sequence can advance several **distinct but connected** layers.

---

# 32. Creation requirements — documents

To make this system reconstruction-grade, create the following children:

1. **Attribute Calibration Table**
   - population bands;
   - starting ranges;
   - training rate;
   - exceptional ranges;
   - injury/enhancement effects.

2. **Skill Registry**
   - all 23 current skills first;
   - complete functional records;
   - future additions only with clear gameplay purpose.

3. **Skill Training & Plateau Standard**
   - gain model;
   - mentors;
   - facilities;
   - difficulty/novelty;
   - plateau gates.

4. **Combat Class Catalog**
   - class requirements;
   - features;
   - progression;
   - specializations;
   - cross-training.

5. **Profession Catalog**
   - job families;
   - qualification;
   - income/access/schedule;
   - advancement.

6. **Rank & Status Namespace Standard**
   - institutional;
   - faction;
   - profession;
   - civic/social;
   - reputation relationships.

7. **Ability & Technique Design Standard**
   - discovery;
   - mastery;
   - resource;
   - evolution;
   - drawback;
   - visibility.

8. **Progression UX Contract**
   - Android player-safe fields;
   - screen hierarchy;
   - explanations;
   - accessibility.

9. **Progression Balance Calibration Packet**
   - time-to-competence;
   - breadth/depth tradeoffs;
   - starting build;
   - Gate Twelve proof values.

10. **Progression Content Authoring Guide**
   - how scenes, activities, mentors, quests, jobs, combat, and exploration grant progression without arbitrary XP rewards.

---

# 33. Creation requirements — game content

The evolved progression system requires authored content, not only formulas.

Create:

- training activities;
- training locations;
- mentors;
- teachers;
- evaluators/examiners where relevant;
- class entry challenges;
- specialization challenges;
- profession qualification paths;
- jobs/work shifts;
- faction/institution advancement events;
- skill-use opportunities;
- ability discovery situations;
- technique experimentation;
- injury/recovery activities;
- advanced facilities;
- learning items/manuals/records;
- progression-aware dialogue;
- NPC recognition of capability;
- world obstacles with multiple competency solutions.

---

# 34. Creation requirements — visual/UI assets

Eventually create:

- attribute icons;
- skill-family icons;
- mastery-stage indicators;
- class-family icons;
- profession/rank insignia framework;
- ability/technique presentation family;
- progress/plateau states;
- training/facility markers;
- mentor/trainer role markers where appropriate;
- accessibility-safe state distinctions;
- compact mobile progression cards;
- detailed inspection panels.

Visual assets must follow the repository pixel-art and UI composition authorities.

---

# 35. What the evolved design deliberately does NOT do

This design does not:

- reduce character development to one global XP bar;
- make profession and combat class the same field;
- turn faction rank into combat power;
- automatically scale the whole world to Jack;
- award unrelated stats because a quest completed;
- require every build to learn every skill;
- hide all progression logic from the player;
- expose secret requirements that the character has not discovered;
- make Android the owner of progression rules;
- discard the current seven-attribute/skill foundation merely to appear “new.”

The upgrade comes from depth, interaction, content, world integration, and meaningful choice—not from renaming everything.

---

# 36. Target acceptance criteria

This progression domain is reconstruction-grade when a future developer or agent can answer from repository documentation:

- What are the seven attributes and what does each mean?
- What skills exist?
- How are skills trained?
- How do attributes differ from skills?
- How do abilities and techniques progress?
- What is a class?
- What is a profession?
- What kinds of rank exist?
- How does cross-training work?
- How does world time affect growth?
- How do mentors/facilities matter?
- How do injuries/recovery affect progression?
- How does equipment interact with capability?
- How does progression alter story/world options?
- How is progression shown safely on Android?
- What progression content must be authored for Gate Twelve?
- What is implemented now versus target design?
- Which values are balance decisions rather than canon facts?

If the documentation cannot answer these without guessing, this branch is not finished.

---

# 37. Immediate next documentation work

Proceed in this order:

1. **DONE** — build the **Skill Registry** for the 23 current skills;
2. **DONE** — build the **Combat Class Catalog** for the seven working class families;
3. **DONE** — build the **Profession / Rank / Status namespace packet**;
4. **DONE** — build the **Training / Mentor / Facility progression standard**;
5. **DONE** — build the **Gate Twelve Progression Proof Packet**;
6. **NEXT** — build the **Progression UX Contract**;
7. calibrate numbers only after the above structures are coherent.

Implementation follows the completed design; it is not the purpose of this document.



# 38. Materialized child — Skill Registry

The first reconstruction-grade child is now:

- `EVOLVED_SKILL_REGISTRY.md`

It expands all 23 current registered skills into target-game design records while preserving the distinction between current runtime facts and evolved content/system requirements.


# 39. Materialized child — Combat Class Catalog

The second reconstruction-grade D-045 child is now:

- `COMBAT_CLASS_CATALOG.md`

It expands the seven established target class families — Vanguard, Skirmisher, Operator, Field Specialist, Investigator, Envoy and Ability Specialist — into reconstruction-grade records covering acquisition evidence, current-skill dependencies, feature ownership, tactical/world roles, training/facility requirements, specialization axes, cross-training, equipment/knowledge boundaries, future save/migration constraints and test requirements.

The catalog explicitly preserves:
- CURRENT / TARGET / PROPOSAL separation;
- all 23 current skill IDs and their existing class-affinity evidence;
- class/profession/rank/global-Level namespace separation;
- D-061's rule that current Phase 1 does not gain a new top-level progression owner;
- V08 tactical authority over movement, action budget, LOS, cover, targeting, injury and encounter rules;
- Python/game-engine authority over future class legality and mutation.

Its dependency matrix covers all 23 current skills exactly once as matrix rows and maps each class to training/facility/tactical dependencies.

No class runtime, save migration, numeric unlock threshold, canon institution, final specialization name or final class visual asset is claimed by this materialized child.

The Profession / Rank / Status namespace packet is now materialized; see section 40.


# 40. Materialized child — Profession / Rank / Status Namespace Standard

The third reconstruction-grade D-045 child is now:

- `PROFESSION_RANK_STATUS_NAMESPACE_STANDARD.md`

It separates profession, profession grade, institutional rank, faction rank, civic/social status, reputation, job/assignment, organization role, combat class, global Level, ability rank and technique mastery instead of collapsing them into one ladder.

The child provides:
- CURRENT / TARGET / PROPOSAL separation;
- stable-ID guidance without retroactively renaming current runtime IDs;
- profession-family coverage across all 23 current skills;
- explicit links to all seven target class families;
- training/mentor/facility and tactical-role dependency boundaries;
- faction/institution/privacy and player-safe projection rules;
- D-061-compatible schema-v1 non-expansion for current Phase 1;
- future save/content migration and validation requirements;
- the handoff into the now-materialized **Training / Mentor / Facility Progression Standard**.

No profession catalog, canon institution, rank ladder, runtime progression state, save-schema change, Android DTO, or tactical runtime behavior is implemented by this materialized child.

# 41. Materialized child — Training / Mentor / Facility Progression Standard

The fourth reconstruction-grade D-045 child is now:

- `TRAINING_MENTOR_FACILITY_PROGRESSION_STANDARD.md`

It preserves existing V10 activity/time/resource owners while defining the target ownership network for training paths, mentor/evaluator capabilities and facility capabilities.

Verified scope:
- all 23 current runtime skill IDs are mapped;
- all seven target class families are mapped;
- mentor/evaluator capability is distinct from NPC identity;
- facility capability is distinct from location/institution identity;
- profession/rank/status namespaces are consumed rather than duplicated;
- access, visibility, schedule, injury/condition, plateau and cross-training gates are explicit;
- D-061 schema-v1/no-new-top-level-progression-owner boundary remains intact;
- player-safe projection and future migration/test seams are defined.

Evidence: `docs/evidence/P12_D045_TRAINING_MENTOR_FACILITY_2026-10-08.md`.

No runtime training formula, balance value, mentor NPC, canon institution/faction, facility location, save field, Android DTO or tactical behavior is implemented by this child.

The Gate Twelve Progression Proof Packet is now materialized; see section 42. The direct next D-045 child is the **Progression UX Contract**.


# 42. Materialized child — Gate Twelve Progression Proof Packet

The fifth reconstruction-grade D-045 child is now:

- `GATE_TWELVE_PROGRESSION_PROOF_PACKET.md`

P16 consumes the current D-066 Trace Echo / Signal Pulse progression proof and D-068 Trace Chamber Powers-training proof, then maps that evidence into the evolved skill/class/profession/training contracts without promoting target records to runtime or canon.

Verified documentation result:
- the current 23-skill foundation is preserved; the bounded scenario directly exercises the current `powers` skill;
- all seven target class families remain intact, with Ability Specialist selected only as the explicit target relationship relevant to this route;
- `ABILITY_TRACE_ECHO`, `TECHNIQUE_SIGNAL_PULSE`, `PRACTICE_SIGNAL_PULSE_ONE_HOUR`, `TRAIN_POWER_FUNDAMENTALS_TWO_HOURS`, `TRACE_STABILIZATION_HUB` and `TRACE_CHAMBER` are source-bound current identities;
- `CLASS_ABILITY_SPECIALIST` remains TARGET/PROPOSAL and runtime-not-implemented;
- no profession, profession grade, institution/faction rank, mentor/evaluator, training-path or facility-capability record is inferred from current practice evidence;
- D-061 save-schema-v1/current-owner boundaries remain unchanged;
- player-safe visibility and future migration/test seams are explicit.

Evidence: `docs/evidence/P16_D045_GATE_TWELVE_PROGRESSION_PROOF_2026-10-08.md`.

No Python/Android/Gradle/CI/emulator/device/APK test execution is claimed by P16. No runtime, save schema, canon institution/mentor/facility, class/profession/rank state, or D-072/D-073 tactical behavior is changed.

The direct next D-045 child is the **Progression UX Contract**.
