# THE GAME — Status UI, Abilities & Passives Master Plan

Status: **ACTIVE TARGET-GAME DESIGN / RECONSTRUCTION-GRADE / IMPLEMENTATION DEFERRED**  
Parent authorities:
- `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`
- `docs/FINAL_GAME_RECONSTRUCTION_BLUEPRINT.md`
- `docs/systems/PROGRESSION_CLASSES_RANKS_EVOLVED_GAME_DESIGN.md`

Purpose: define the target-game structure for the human Status UI, awakening, ability rarity, level progression, one-primary-ability rule, passive acquisition, hidden requirements, discovery state, and documentation scale.

This is a design authority. It does not claim these systems are already implemented in runtime code.

---

# 1. Owner-locked canon

## 1.1 Human Status UI

All humans receive access to the Status UI at age 18.

Awakening is socially formalized through a public event in which schools gather and present their students for identification and classification.

The awakening event publicly establishes at minimum:
- that the person awakened;
- their primary ability identity or recognized classification;
- the ability rarity/classification that society is permitted to know;
- other public-facing classification data defined by future social/institutional documentation.

The exact degree of privacy, governmental access, falsification, concealment, and classified handling remains a child-document decision.

## 1.2 One primary ability per human

A human awakens exactly **one primary ability**.

That primary ability defines a coherent family of powers, techniques, evolutions, and applications available to that person.

A human cannot normally replace the awakened primary ability.

### Level-100 exception

Changing or replacing the primary ability becomes possible only after reaching **Level 100**.

Historical fact currently locked by owner direction:
- only **two humans** in known history have reached Level 100 so far.

The exact mechanics, cost, risks, permanence, and public knowledge surrounding the Level-100 ability-change event remain to be designed.

## 1.3 Ability rarity hierarchy

Working canonical rarity order:

1. Common
2. Uncommon
3. Rare
4. Super Rare
5. Epic
6. Super Epic
7. Legendary
8. Prime Legendary
9. Unique

### Unique

A Unique ability is **1/1 in the universe** for that ability identity.

This does not mean every Unique ability is automatically omnipotent. It means that specific ability exists only once across the known universe unless later canon explicitly establishes succession, inheritance, destruction/rebirth, or another exception.

## 1.4 Ability superiority

Some abilities are objectively superior to others.

The game must not pretend that all awakenings have identical raw potential.

Balance comes from the total character:
- level;
- stats;
- training;
- technique;
- knowledge;
- equipment;
- passives;
- matchup;
- environment;
- experience;
- preparation;
- injuries;
- team support;
- ability mastery.

A lower-rarity ability can still be dangerous, highly optimized, or strategically superior in a specific situation without erasing genuine rarity/potential differences.

---

# 2. Level system

## 2.1 Canon role

Global Level is real in-universe Status data.

It is not merely a UI summary.

Humans gain level progress through kills, currently including:
- beast kills;
- PK / killing another person.

The exact XP formula, contribution rules, assists, party split, anti-exploit rules, level curve, and whether all valid lifeforms award XP remain calibration tasks.

## 2.2 Relationship to other progression

Level does **not** replace:
- attributes;
- learned skills;
- ability mastery;
- techniques;
- passives;
- profession;
- combat class;
- institutional rank;
- faction rank;
- reputation;
- knowledge;
- equipment proficiency.

The evolved game therefore uses Level as one progression axis inside a larger progression network.

## 2.3 Level-100 significance

Level 100 is an extreme historical threshold.

Because only two humans are known to have reached it, any content involving Level 100 must treat it as a civilization-scale rarity, not a normal endgame expectation.

---

# 3. Primary ability model

Every primary ability record must eventually define:

- stable ability ID;
- display name;
- rarity;
- public classification;
- true classification if different;
- conceptual domain;
- core law/rule;
- allowed power family;
- forbidden/unrelated effects;
- initial awakening manifestation;
- base techniques;
- advanced techniques;
- mastery states;
- evolution branches;
- level interactions;
- stat interactions;
- skill interactions;
- resource costs;
- drawbacks;
- counters;
- environmental interactions;
- equipment interactions;
- passive synergies;
- known users;
- historical users;
- secrecy level;
- institution/faction interest;
- legal/social consequences;
- visual/FX requirements;
- hidden properties;
- discovery conditions;
- balance notes;
- test requirements.

The goal is to prevent “ability drift,” where an ability gradually acquires unrelated powers because individual scenes need convenient solutions.

---

# 4. Passive ability model

## 4.1 Core rule

Humans can obtain **multiple passive abilities** in addition to their one primary ability.

Passives are earned through experience, adaptation, repeated behavior, extreme conditions, survival, training, trauma, specialization, or other authored requirements.

## 4.2 Hidden-until-qualified rule

A passive is not visible to the player/person before its requirements are satisfied.

Once the qualifying conditions are met, the Status UI reveals the passive.

Therefore the system requires at least three information states:

1. **UNSEEN** — the passive exists in the game rules but the character does not know it exists.
2. **QUALIFIED / REVEALED** — requirements have been satisfied and the Status UI reveals it.
3. **ACQUIRED / ACTIVE** — the passive is part of the character's state and its effects apply.

If revelation and acquisition are simultaneous for a passive, states 2 and 3 may occur together.

## 4.3 No simple hard cap

The passive system is intended to be broad and large-scale.

There is no current owner-locked small numeric cap on how many passives a character may eventually acquire.

Practical balance should come from:
- difficult prerequisites;
- mutually exclusive adaptations where appropriate;
- risk;
- time;
- opportunity cost;
- physiology;
- build direction;
- diminishing accessibility;
- world knowledge;
- survival requirements;
- rare events.

Do not impose an arbitrary “three passives maximum” rule unless later explicitly approved.

## 4.4 Extreme-experience acquisition

A passive may emerge when a character repeatedly or severely stresses a capability.

Example pattern:

A character undertakes extreme physical conditioning with meaningful danger, recovery cost, and sustained overload. If the authored prerequisites are satisfied, the Status may reveal a passive that benefits that adaptation domain.

The system must not reward meaningless self-harm or trivial input spam. Requirements should represent credible in-world adaptation and must include safeguards against exploitable repetition.

---

# 5. Passive requirement schema

Every passive must have a machine-readable/internal requirement packet eventually containing some combination of:

- minimum level;
- minimum/max attribute;
- skill threshold;
- accumulated activity duration;
- intensity threshold;
- repeated event count;
- unique-event flag;
- survival condition;
- injury/recovery history;
- environmental exposure;
- combat history;
- beast-kill history;
- PK history where canonically relevant;
- ability identity;
- ability rarity;
- ability mastery;
- technique use;
- equipment condition;
- profession/class state;
- location/region;
- mentor/training;
- knowledge;
- faction/institution state;
- time window;
- sequence requirement;
- forbidden conditions;
- mutual exclusion;
- hidden random/seeded factor only if later explicitly approved.

The player-facing UI must never reveal unmet hidden requirements merely because the data exists internally.

---

# 6. Passive families

The first scalable taxonomy should support at least:

- Physical Adaptation
- Endurance / Recovery
- Movement
- Sensory
- Mental / Will
- Cognitive / Learning
- Combat Habit
- Weapon Familiarity
- Defensive Adaptation
- Survival / Environmental
- Social / Behavioral
- Leadership / Coordination
- Technical / Craft
- Medical / Recovery Practice
- Ability Synergy
- Resistance
- Creature / Beast Interaction
- Injury / Scar Adaptation
- Profession
- Faction / Institutional
- Knowledge
- Unique Event
- Cosmic / System
- Unknown / Classified

These are organizational families, not rarity tiers.

A passive may have multiple tags while retaining one primary registry family.

---

# 7. Passive rarity and significance

Passive rarity must be documented separately from primary-ability rarity unless later canon deliberately unifies them.

A passive can be:
- common in principle but difficult for one character to qualify for;
- rare because the requirement is rare;
- secret because institutions suppress knowledge;
- unique because only one historical trigger exists;
- dangerous because its acquisition condition is lethal or destabilizing.

Do not infer rarity only from numerical power.

---

# 8. Knowledge asymmetry

Some passives have already been discovered by people in the world, but their existence or requirements are deliberately kept quiet.

Therefore every passive record needs separate fields for:

- exists in system;
- known to general public;
- known to schools;
- known to government;
- known to military/security;
- known to researchers;
- known to factions;
- classified;
- misinformation/false requirement rumors;
- player knowledge;
- character qualification state.

This supports a world where people can train toward known passives, accidentally discover unknown ones, hide monopolized methods, sell information, or spread false unlock recipes.

---

# 9. Documentation architecture

This system is intentionally large.

It must not live as one giant Markdown file.

Use the following hierarchy:

`docs/systems/status/`
- `README.md` — authority/index.
- `STATUS_UI_CORE_CONTRACT.md` — Status fields, visibility, awakening, level.
- `PRIMARY_ABILITY_REGISTRY_SCHEMA.md` — ability record schema.
- `PASSIVE_REGISTRY_SCHEMA.md` — passive record schema.
- `ABILITY_RARITY_STANDARD.md` — Common -> Unique definitions and calibration.
- `PASSIVE_REQUIREMENT_LANGUAGE.md` — requirement grammar and hidden-condition rules.
- `STATUS_KNOWLEDGE_VISIBILITY_STANDARD.md` — public/classified/player-safe exposure.
- `LEVEL_AND_XP_STANDARD.md` — kills, XP, levels, contribution and anti-exploit.
- `AWAKENING_EVENT_STANDARD.md` — age-18 public school event.
- `LEVEL_100_EXCEPTION_STANDARD.md` — historical/mechanical authority.
- `PASSIVE_CATALOG_INDEX.md` — catalog navigation.
- `PRIMARY_ABILITY_CATALOG_INDEX.md` — catalog navigation.
- `ABILITY_PASSIVE_CROSS_REFERENCE.md` — synergies/conflicts.
- `ABILITY_CONTENT_AUTHORING_GUIDE.md`
- `PASSIVE_CONTENT_AUTHORING_GUIDE.md`
- `STATUS_UI_UX_CONTRACT.md`
- `STATUS_BALANCE_AND_TEST_MATRIX.md`

Large catalogs should later be split by family/range rather than allowing one unbounded file.

---

# 10. Catalog-scale rule

The owner expects a major share of the broader documentation corpus to be devoted to clarifying and mapping abilities/passives and their relationships.

Therefore future catalog work should include:
- primary ability records;
- passive records;
- requirements;
- known/hidden knowledge;
- techniques;
- counters;
- evolutions;
- user examples;
- world institutions;
- training methods;
- discovery routes;
- balance bands;
- visual assets;
- story hooks;
- implementation/test requirements.

No arbitrary claim should be made that a numeric documentation target has been reached unless the unit being counted is explicit and reproducible.

---

# 11. Player-safe Status behavior

The Status UI may show only information the character is allowed to know.

Before passive qualification:
- do not show its name;
- do not show its requirement;
- do not show a locked slot implying exactly what exists;
- do not leak classified catalog membership.

After reveal:
- show the passive name;
- show its known effect;
- show acquired state;
- optionally show discovered provenance/history;
- do not expose hidden future evolutions unless discovered.

The same principle applies to hidden properties of primary abilities.

---

# 12. Content implications

The passive system requires authored world content capable of producing prerequisites:

- gyms/training halls;
- wilderness/environmental extremes;
- combat schools;
- medical recovery;
- work/profession repetition;
- beast zones;
- dangerous expeditions;
- social institutions;
- research;
- classified training;
- faction techniques;
- historical records;
- secret manuals;
- mentors;
- illegal or suppressed methods;
- cosmic/system events.

This is why passive design is a world-content program, not only a stat table.

---

# 13. Pixel-art / presentation implications

Future assets include:
- Status UI awakening presentation;
- rarity frames/icons;
- passive reveal animation;
- level-up feedback;
- hidden/classified visual states;
- ability-family icons;
- technique icons;
- passive-family icons;
- historical Level-100 records;
- awakening-event environment and school representation;
- public classification presentation.

Character art remains authored pixel art. Status effects do not authorize geometry-built character rendering.

---

# 14. Immediate child-document order

1. `STATUS_UI_CORE_CONTRACT.md`
2. `ABILITY_RARITY_STANDARD.md`
3. `PRIMARY_ABILITY_REGISTRY_SCHEMA.md`
4. `PASSIVE_REGISTRY_SCHEMA.md`
5. `PASSIVE_REQUIREMENT_LANGUAGE.md`
6. `STATUS_KNOWLEDGE_VISIBILITY_STANDARD.md`
7. `LEVEL_AND_XP_STANDARD.md`
8. `AWAKENING_EVENT_STANDARD.md`
9. `LEVEL_100_EXCEPTION_STANDARD.md`
10. initial primary-ability catalog seed
11. initial passive catalog seed
12. UX/balance/test packets

The catalog can then scale incrementally without rewriting the governing rules.
