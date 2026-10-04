# THE GAME — Human Status UI Core Contract

Status: **ACTIVE TARGET-GAME DESIGN**

## 1. Canon purpose

The Status UI is an in-universe system granted to humanity through the intervention of the cosmic being currently known provisionally as **The Witness / El Testigo**.

It is not merely a game HUD metaphor.

It provides humans with structured access to progression information and is one of the main reasons humanity could resist the first interworld conquest.

## 2. Activation age

Every human receives/activates the Status UI at age **18**.

The exact biological/cosmic mechanism remains unresolved.

## 3. Public awakening event

At age 18, students participate in a large public awakening/classification event involving schools.

Target consequences:
- students are presented publicly;
- awakening is socially significant;
- ability identity/classification can affect reputation and opportunity;
- schools are publicly compared or represented;
- institutions may recruit, monitor, classify, protect, exploit, or suppress talent;
- rare awakenings can become national/international events.

Future child:
- `AWAKENING_EVENT_STANDARD.md`

## 4. Primary ability slot

Every human awakens exactly **one primary ability**.

The primary ability:
- has one stable identity;
- has a rarity;
- defines a coherent capability family;
- can develop techniques and evolutions;
- cannot normally be replaced.

Changing it is reserved for the Level-100 exception.

## 5. Ability rarity sequence

Canonical order:

1. Common
2. Uncommon
3. Rare
4. Super Rare
5. Epic
6. Super Epic
7. Legendary
8. Prime Legendary
9. Unique

Unique = one instance of that ability identity in the universe, subject only to future explicit succession/rebirth rules if ever approved.

## 6. Level

Level is real Status data.

Known owner rule:
- kills can grant progression toward Level;
- beast kills count;
- PK counts.

The exact XP model remains open.

Level must coexist with:
- attributes;
- learned skills;
- ability mastery;
- techniques;
- passives;
- class;
- profession;
- equipment;
- knowledge;
- ranks;
- reputation.

## 7. Level 100

Level 100 is historically extraordinary.

Known history:
- only two humans have reached Level 100 so far.

At Level 100, the otherwise fixed primary ability can become changeable/replacable through a special process not yet designed.

Do not normalize Level 100 as an ordinary late-game milestone.

## 8. Passives

A human can hold many passive abilities in addition to the single primary ability.

Passives may arise from:
- adaptation;
- extreme training;
- survival;
- repeated behavior;
- combat history;
- environmental exposure;
- profession;
- knowledge;
- ability interaction;
- rare events;
- other authored requirement packets.

A passive remains completely hidden from the character before qualification.

Once requirements are satisfied, Status can reveal it.

## 9. Hidden-information principle

The Status UI does not expose everything that exists in the system.

Before discovery/qualification, it must not reveal:
- passive names;
- passive requirements;
- secret evolution branches;
- classified system knowledge;
- hidden future techniques;
- undiscovered ability properties.

Therefore internal authoritative data and player-safe Status projection must remain separate.

## 10. Status fields — target families

The final Status should support at least:

### Identity
- name;
- age;
- public identity;
- relevant titles.

### Global progression
- Level;
- Level XP/progress when the rules allow it to be shown.

### Attributes
- current/base/effective values.

### Skills
- learned competencies and effective values.

### Primary ability
- name;
- rarity;
- known description;
- mastery/rank;
- known techniques;
- known drawbacks.

### Passives
- revealed/acquired passives only.

### Resources
- health;
- stamina;
- focus;
- resolve;
- ability-specific resources where applicable.

### Conditions
- player-visible conditions only.

### Other progression
- class;
- profession;
- recognized ranks;
- player-known reputation/status summaries where designed.

## 11. Security / secrecy rule

The person's own Status does not imply the public automatically has full access to it.

Future documentation must define:
- what the individual alone can see;
- what the public awakening reveals;
- what schools can record;
- what governments can access;
- what can be concealed/falsified;
- classified ability handling;
- criminal/legal consequences of forged records;
- whether inspection abilities exist.

## 12. Required implementation boundary

When implemented:
- engine owns authoritative Status state;
- Android/presentation consumes player-safe projection;
- UI must not reconstruct hidden passives from prerequisites;
- no client-side secret registry should accidentally expose hidden content;
- deterministic save/load must preserve Status state.

## 13. Open decisions

Still unresolved:
- exact Status visual manifestation;
- whether other people can see another person's UI directly;
- exact XP curve;
- kill credit/assist rules;
- party XP;
- anti-farming/anti-abuse;
- stat gains per level;
- whether Level itself grants stat points or mainly gates growth;
- exact Level-100 replacement process;
- legal privacy of awakening data;
- cosmic entity's exact identity/name/motive.
