# WORLD_HISTORY_AND_REFERENCE_MASTER_BUILD_PLAN

Status: ACTIVE_EXECUTION_PLAN
Authority: USER_DIRECTION_2026-09-29
Repository: jbob-coder/Text-rpg-game
Branch: context/shared-game-context
Scope: World history book + technical world reference encyclopedia
Live-game clock effect: NONE

## 1. Purpose

This document exists to prevent the world-history project from being attempted as one massive write.

The project will be built in controlled phases so that:
- canon remains internally consistent;
- older files are not silently contradicted;
- protagonist mysteries remain protected;
- every historical era has enough social, ecological, technological, political, and cultural depth to feel lived-in;
- creatures, powers, crystals, portals, factions, institutions, and locations become reusable reference systems for later scenario generation;
- future sessions can resume work from repository state without depending on chat memory;
- game scenes can query world history and reference material to select era-appropriate threats, species, institutions, technologies, laws, and social conditions.

The final result is not intended to be a thin timeline.

It is intended to function as:
1. a complete history of the setting;
2. an author reference bible;
3. a gameplay/worldbuilding encyclopedia;
4. a scenario-generation reference system;
5. a continuity source of truth.

---

## 2. Core creative direction

### 2.1 History must feel lived-in

Do not write history as:
- "this happened";
- "then this happened";
- "then war happened";
- "then society changed".

Every major era must answer:
- what ordinary people experienced;
- how institutions reacted;
- how technology changed daily life;
- what food, medicine, work, education, law, religion, travel, family life, crime, and military service looked like;
- how ecosystems changed;
- what people feared;
- what people misunderstood;
- what information governments or institutions hid;
- what was publicly believed;
- what actually happened.

History must contain causal continuity.

Every large transition should show:
CAUSE -> PRESSURE -> EVENT -> RESPONSE -> CONSEQUENCE -> LONG-TERM EFFECT.

---

## 3. Protected protagonist mystery rule

The world may be documented in extreme detail.

Jack, Elias, and other principal player-character mysteries must remain deliberately incomplete.

Protected areas include, where applicable:
- parent identities or true roles;
- unexplained disappearances;
- classified family history;
- exact origin of unique abilities;
- hidden institutional relationships;
- secret experiments;
- unknown benefactors/enemies;
- sealed operations tied directly to protagonist backstory.

Use the state:
PROTAGONIST_MYSTERY

A PROTAGONIST_MYSTERY may contain:
- known public facts;
- known inconsistencies;
- missing records;
- sealed files;
- witness contradictions;
- unexplained events;
- evidence fragments.

It must not automatically contain the final answer.

World history should create hooks around these mysteries without resolving them prematurely.

---

## 4. Immediate canon correction gate

Before extending the historical chronology beyond the current boundary, perform a canon reconciliation pass.

### 4.1 Homunculi correction

USER-DIRECTED CANON:
- Homunculi are not the cause of the First Interworld War.
- The First Interworld War must have an independent geopolitical/interworld cause.
- Homunculi exist as a hidden hostile or anti-human society/factional network.
- They are opposed to human survival as a broad strategic objective unless later factional distinctions are explicitly created.
- Human cooperation with hostile Homunculus groups can be treated as an extreme offense against humanity under applicable human law.
- Discovery of active collaboration may lead to severe criminal prosecution, potentially including capital punishment where that jurisdiction and historical period permit it.
- Homunculi must not be treated as the central cause of every major conflict.
- Their existence should remain one dangerous layer of the world rather than the single explanation behind the setting.

### 4.2 Files requiring reconciliation

Review and revise as necessary:
- docs/world_history/WORLD_HISTORY_MASTER_INDEX.md
- docs/world_history/species/SPECIES_HOMUNCULUS_001.md
- docs/world_history/species/HOMUNCULUS_HISTORICAL_DEVELOPMENT_2556_2602.md
- docs/world_history/eras/ERA_050_PORTAL_EXPANSION_2559_2605.md
- any future law/faction/event file referencing the Homunculus Rebellion as the dominant historical driver.

Do not delete useful material automatically.
Preserve compatible biology, ecology, technology, or faction concepts where they still fit.
Mark superseded historical claims explicitly.

---

## 5. Deliverable architecture

The project will be developed as two synchronized products.

# PRODUCT A — WORLD HISTORY BOOK

Purpose:
A readable, detailed historical account from the pre-Crystal world to the opening period of the game.

This should be readable as a coherent history book rather than only as a database.

Primary structure:
- Book 0 — Foundations of Earth and Humanity
- Book 1 — Hidden Anomalous Humanity
- Book 2 — The Last Pre-Crystal Centuries
- Book 3 — Veinfall
- Book 4 — The Early Crystal Era
- Book 5 — Crystal Industrialization
- Book 6 — Portal Expansion
- Book 7 — Interworld Expansion
- Book 8 — First Contact and Escalation
- Book 9 — First Interworld War
- Book 10 — Concord and Reconstruction
- Book 11 — The World of 2670
- Book 12 — Academy Historical Development
- Appendix — unresolved protagonist-adjacent historical gaps

Each Book may be split into Chapters when needed.

# PRODUCT B — WORLD REFERENCE ENCYCLOPEDIA

Purpose:
A structured reference system for use while creating scenarios.

Major reference volumes:
- Creature / Beast Codex
- Creature Threat Classification
- Creature Ability Registry
- Human Ability Classification
- Crystal Classification and Uses
- Portal Types and Hazards
- Ecosystem Registry
- Disease / Contamination Registry
- Technology Registry
- Weapon / Defense Technology Registry
- Faction Registry
- Government / Nation Registry
- Organization Registry
- Law and Crime Registry
- Academy Reference
- Economy and Resource Registry
- Profession Registry
- Religion / Culture Registry
- Planet / Region / Biome Registry
- Historical Event Registry
- War and Military Doctrine Registry

The encyclopedia must allow scenario construction by filtering:
ERA + REGION + BIOME + THREAT_LEVEL + SPECIES + FACTION + TECHNOLOGY_LEVEL + LEGAL_CONTEXT.

---

## 6. Creature / monster reference requirements

The creature system must not be a random monster list.

Each creature entry should eventually support:

- stable ID;
- common name;
- scientific or institutional name;
- origin type;
- first known historical appearance;
- eras in which it exists;
- native worlds/regions;
- biome;
- trophic role;
- diet;
- prey;
- predators;
- reproduction;
- migration;
- activity cycle;
- social behavior;
- intelligence;
- aggression triggers;
- territorial behavior;
- crystal interaction;
- portal interaction;
- diseases/parasites;
- physical anatomy;
- sensory capabilities;
- natural defenses;
- abilities;
- weaknesses;
- environmental vulnerabilities;
- threat classification;
- recommended response doctrine;
- known variants;
- age stages;
- historical population changes;
- economic value;
- harvested materials;
- legal protection/restriction;
- domestication status;
- use by factions;
- notable historical incidents;
- gameplay encounter notes;
- scenario suitability by era.

---

## 7. Creature threat-level system

Threat level must represent operational danger, not only raw combat strength.

Threat rating should consider:
- individual lethality;
- group behavior;
- intelligence;
- mobility;
- resilience;
- reproduction rate;
- stealth;
- environmental spread;
- disease/toxin potential;
- portal mobility;
- ability use;
- infrastructure damage;
- resistance to conventional weapons;
- strategic threat.

Initial design task:
create a threat-classification system before populating large numbers of creatures.

Possible structure to evaluate later:
- nuisance/local hazard;
- dangerous fauna;
- specialist response threat;
- settlement-level threat;
- regional catastrophe;
- strategic/national threat;
- civilization-level threat;
- anomalous/unclassifiable threat.

Exact names and thresholds must be designed and tested before promotion to canon.

---

## 8. Power and ability reference requirements

Abilities require two separate systems:

### 8.1 Human natural abilities
Existing high-level families:
- PHYSICAL
- SENSORY
- BIOLOGICAL
- ENERGY
- MENTAL
- SPATIAL
- TRANSFORMATION
- MATERIAL
- FIELD
- ANOMALOUS

Each ability should track:
- ID;
- family;
- biological mechanism or best current theory;
- manifestation conditions;
- inheritance tendency;
- range;
- cost;
- limitations;
- side effects;
- training curve;
- counters;
- legal classification;
- military classification;
- medical risks;
- historical first record;
- public knowledge state.

### 8.2 Creature / nonhuman abilities

Do not force every creature ability into the human system.

Creature abilities may be:
- anatomical;
- biochemical;
- sensory;
- neurological;
- crystal-adapted;
- environmental;
- portal-derived;
- swarm/cooperative;
- anomalous.

Each ability must be tied to a plausible organism, ecology, or setting rule.

---

## 9. Historical era documentation template

Every major era should include:

### Narrative layer
- opening historical situation;
- central tensions;
- major discoveries;
- major disasters;
- turning points;
- representative civilian experiences;
- ending condition.

### Demography
- population;
- migration;
- mortality;
- urbanization;
- displaced populations;
- frontier settlement.

### Politics
- states;
- alliances;
- collapsed states;
- new institutions;
- diplomacy;
- internal political conflict.

### Economy
- dominant industries;
- scarcity;
- trade;
- currency;
- crystal markets;
- offworld resources;
- labor systems.

### Daily life
- housing;
- work;
- education;
- food;
- entertainment;
- family life;
- travel;
- communication.

### Technology
- energy;
- transport;
- medicine;
- weapons;
- communications;
- portal technology;
- crystal technology.

### Ecology
- ecosystems;
- invasive species;
- extinctions;
- mutations/adaptations;
- diseases;
- agriculture;
- ocean and soil changes.

### Military
- force structure;
- doctrine;
- weapons;
- creature-response units;
- portal warfare;
- logistics;
- civil defense.

### Law
- ability regulation;
- crystal regulation;
- portal law;
- wartime emergency law;
- collaboration/treason law;
- creature-control law.

### Culture
- religion;
- language;
- art;
- propaganda;
- memorials;
- myths;
- prejudice;
- social movements.

### Knowledge layers
- PUBLIC
- CLASSIFIED
- TRUE
- PROTAGONIST_MYSTERY where relevant.

---

## 10. Academy integration rule

The Academy must emerge from world history.

It must not appear as an isolated RPG location with no causal foundation.

The Academy historical build must explain:
- what institutions preceded it;
- why governments or societies needed it;
- how early ability users were trained;
- how beast/portal threats changed curriculum;
- how wars changed doctrine;
- why admission standards evolved;
- how military and civilian education separated or overlapped;
- what social class differences exist;
- what students in 2670 believe about its history;
- what the Academy hides;
- what records are classified;
- what parts of its history are mythologized.

The Academy becomes a historical institution first and a gameplay location second.

---

## 11. War construction rule

WAR_FIRST_INTERWORLD_2645_2659 must be constructed separately from the Homunculus plotline.

Before writing the war:
1. build Kharvori history;
2. build Kharvori biology/ecology;
3. define human frontier expansion;
4. define first-contact circumstances;
5. establish conflicting territorial/resource assumptions;
6. establish diplomacy and failed agreements;
7. establish economic and military escalation;
8. document incidents that increase mistrust;
9. define war trigger;
10. define war aims for each major faction;
11. define major theaters;
12. define logistics;
13. define civilian consequences;
14. define technology changes;
15. define beast/ecology effects;
16. define propaganda and public belief;
17. define classified/true causes;
18. define why the war lasts 2645–2659;
19. define why neither side obtains a simple total victory;
20. define the path to EVENT_HALCYON_GATE_CONCORD_2660.

The war must feel historically inevitable in hindsight without being predetermined from the start.

---

## 12. Scenario-reference rule

Every reference entry should eventually answer:

"Can this logically appear in this scene?"

Before using a creature, technology, faction, disease, weapon, or social institution in a scenario, the writer should be able to check:
- Did it exist in this year?
- Did it exist in this region/world?
- Could it survive in this biome?
- Would civilians know about it?
- Would the Academy know about it?
- Is it legal?
- Is it common or rare?
- Is it appropriate for this threat level?
- Would this faction realistically use it?
- Would this encounter contradict ecology or history?

This is a core purpose of the encyclopedia.

---

## 13. Execution phases

### PHASE 00 — Canon audit and contradiction map
Goal:
Identify conflicts before new expansion.

Tasks:
- compare master index against active era/species/law files;
- identify outdated Homunculus assumptions;
- identify duplicate or inconsistent IDs;
- identify undefined historical gaps;
- identify protagonist-sensitive facts;
- produce contradiction report.

Output:
CANON_RECONCILIATION_REPORT.md

Completion gate:
No known high-impact contradiction is silently carried into later phases.

---

### PHASE 01 — Master architecture
Goal:
Freeze document structure.

Tasks:
- establish history-book directory;
- establish encyclopedia directory;
- establish templates;
- establish status labels;
- establish stable-ID rules;
- establish cross-link format.

Outputs:
- WORLD_HISTORY_BOOK_INDEX.md
- WORLD_REFERENCE_ENCYCLOPEDIA_INDEX.md
- templates/

Completion gate:
A new session can understand where every future fact belongs.

---

### PHASE 02 — Pre-Crystal world expansion
Goal:
Turn existing foundations into real history.

Tasks:
- expand human civilizations;
- hidden anomalous humans;
- ancient myths with partial truth;
- early organizations;
- scientific precursors;
- modern pre-Veinfall society;
- precursor anomalies;
- ordinary life before the change.

Completion gate:
The reader understands what humanity is about to lose when Veinfall occurs.

---

### PHASE 03 — Veinfall deep history
Goal:
Make Veinfall a fully realized historical event.

Tasks:
- pre-event warning signs;
- 11-day primary cascade;
- regional differences;
- government response;
- infrastructure collapse;
- first creature incidents;
- first ecological effects;
- human ability manifestations;
- media/public reaction;
- casualties/displacement model;
- scientific confusion;
- classified knowledge;
- 18-month instability.

Completion gate:
Veinfall can support multiple stories without contradicting itself.

---

### PHASE 04 — Early Crystal Era
Goal:
Explain survival and normalization.

Tasks:
- emergency governance;
- refugee systems;
- first beast-control professions;
- early ability law;
- quarantine;
- crystal research;
- food systems;
- medicine;
- early Academy predecessors;
- new economies.

---

### PHASE 05 — Crystal Industrialization
Goal:
Show crystals becoming civilization-scale infrastructure.

Tasks:
- extraction;
- grading;
- industry;
- corporate power;
- energy;
- medicine;
- weaponization;
- labor;
- environmental cost;
- black markets;
- new professions;
- social inequality.

---

### PHASE 06 — Portal Expansion
Goal:
Deepen existing 2559–2605 material.

Tasks:
- research history;
- failures;
- accidents;
- travel law;
- frontier culture;
- quarantine;
- settlements;
- offworld agriculture;
- portal economics;
- smuggling;
- rescue operations;
- early creature migration through portals.

---

### PHASE 07 — Homunculus canon rebuild
Goal:
Align all Homunculus material with current user direction.

Tasks:
- determine origin elements worth preserving;
- remove Homunculus causation from First Interworld War;
- build hidden anti-human society/network;
- define cells/factions if useful;
- define recruitment/infiltration;
- define human collaborators;
- define anti-human strategic goals;
- define legal treatment of collaboration;
- define what is PUBLIC vs CLASSIFIED vs TRUE;
- prevent species/faction terminology from becoming ambiguous.

Important:
Do not assume every biological Homunculus individual must automatically behave identically unless canon explicitly makes "Homunculus" a faction rather than a species.
Resolve terminology during this phase.

---

### PHASE 08 — Creature classification foundation
Goal:
Create a reusable threat and ecology system.

Tasks:
- threat classes;
- taxonomy;
- ability tags;
- ecology fields;
- encounter suitability;
- historical availability;
- biome rules;
- response doctrine.

Output:
CREATURE_CLASSIFICATION_STANDARD_V1.md

---

### PHASE 09 — Core Creature Codex
Goal:
Create first robust creature set.

Build by ecological niche, not arbitrary quantity:
- microbe/pathogen threats;
- herbivores;
- scavengers;
- small predators;
- pack predators;
- apex predators;
- ambush species;
- aerial species;
- aquatic species;
- subterranean species;
- crystal-specialist species;
- portal-associated species;
- parasitic species;
- swarm species;
- intelligent/nonhuman edge cases.

Each entry must follow the full creature template.

---

### PHASE 10 — Human and nonhuman ability encyclopedia
Goal:
Make powers reusable and bounded.

Tasks:
- human natural ability registry;
- induced/crystal-linked effects;
- creature abilities;
- counters;
- costs;
- medical consequences;
- legal/military classification.

---

### PHASE 11 — Interworld Expansion 2606–2644
Goal:
Build the missing historical bridge.

Tasks:
- expansion frontier;
- new settlements;
- resource competition;
- new worlds;
- creature/ecology transfer;
- Kharvori pre-contact history;
- first contact;
- trade;
- misunderstandings;
- diplomacy;
- border disputes;
- militarization.

---

### PHASE 12 — First Interworld War 2645–2659
Goal:
Construct the war in full historical depth.

Tasks:
- causes;
- trigger;
- factions;
- war aims;
- theaters;
- campaigns;
- weapons;
- portals;
- creatures;
- logistics;
- intelligence;
- civilian life;
- economy;
- propaganda;
- Academy role;
- casualties;
- ecological damage;
- political changes;
- war crimes;
- collaboration cases;
- turning points;
- exhaustion;
- failed peace efforts;
- end conditions.

---

### PHASE 13 — Halcyon Gate Concord and Reconstruction
Goal:
Explain why the war ends and how society changes.

Tasks:
- negotiations;
- concessions;
- unresolved disputes;
- demobilization;
- destroyed regions;
- veterans;
- refugees;
- reconstruction economy;
- memorial culture;
- new security doctrine;
- border controls;
- Academy reform;
- lingering hostile networks.

---

### PHASE 14 — World of 2670
Goal:
Create the immediate pre-game reference state.

Tasks:
- nations;
- cities;
- economy;
- culture;
- laws;
- technology;
- portals;
- bestiary distribution;
- Academy;
- military;
- major factions;
- public fears;
- current unresolved crises.

Do not advance Jack/Elias live gameplay.

---

### PHASE 15 — Scenario query layer
Goal:
Make the documentation operational for game writing.

Create lookup tables or structured indexes for:
- year;
- region;
- biome;
- creature threat;
- faction;
- technology;
- law;
- knowledge level;
- Academy relevance.

Target use:
A future writer can ask:
"2670, temperate forest near human settlement, medium threat, Academy student encounter"
and locate only creatures/events/factions that logically fit.

---

### PHASE 16 — Narrative compilation pass
Goal:
Convert completed history material into a readable history book.

Tasks:
- remove database tone from narrative volumes;
- preserve factual links to encyclopedia files;
- add human-scale examples;
- improve transitions;
- preserve uncertainty where intended;
- verify chronology;
- verify no protagonist mystery was accidentally resolved.

---

## 14. Per-phase workflow

Every phase follows:

READ STATE
-> IDENTIFY AUTHORITY
-> MAP CONTRADICTIONS
-> WRITE SMALL UNIT
-> CROSS-LINK
-> VERIFY
-> UPDATE INDEX
-> RECORD WHAT REMAINS
-> MOVE TO NEXT UNIT

Never write an entire era blindly in one pass.

Preferred unit size:
- one era section;
- one institution;
- one species family;
- one law framework;
- one event cluster;
- one reference standard.

---

## 15. Verification rules

Before marking a unit complete:
- reread the file after write;
- check IDs;
- check date consistency;
- check predecessor/successor era;
- check knowledge layer;
- check protagonist mystery protection;
- check cross-references;
- check that no creature appears before its historical emergence;
- check that no technology appears before invention/adoption;
- check that laws exist before they are enforced;
- check geography/ecology fit;
- check Homunculus material against current direction;
- update master indexes.

Do not claim "verified" without reading the resulting repository state.

---

## 16. Continuity record

At the end of each completed phase, record:
- CURRENT_OBJECTIVE
- VERIFIED_STATE
- COMPLETED
- IN_PROGRESS
- NEXT_ACTION
- BLOCKERS
- ASSUMPTIONS
- UNKNOWNS
- DECISIONS
- RISKS
- FILES_CHANGED
- VERIFICATION_PERFORMED

This allows another session to resume safely.

---

## 17. Current starting point

CONFIRMED existing historical coverage:
- prehuman baseline;
- pre-Crystal human history;
- Veinfall;
- Early Crystal Era;
- Crystal Industrialization;
- Portal Expansion through 2605;
- initial crystal, ecology, law, portal, economy, and Homunculus files.

PRIMARY NEXT ACTION:
PHASE 00 — Canon audit and contradiction map.

Reason:
Current Homunculus documentation contains historical assumptions that conflict with the latest user direction.
Those conflicts must be resolved before building Interworld Expansion and the First Interworld War.

---

## 18. Success condition

This project is complete only when the repository can answer, with traceable canon:

- what happened;
- when it happened;
- why it happened;
- who knew;
- who lied;
- who benefited;
- what ordinary people experienced;
- what changed biologically;
- what changed ecologically;
- what changed technologically;
- what changed legally;
- what creatures existed;
- what powers existed;
- where they existed;
- how dangerous they were;
- which institutions existed;
- what the Academy inherited from history;
- what is still unknown;
- what the protagonists still do not know.

The world should be detailed enough that future scenarios are selected from an existing living world rather than invented from nothing every time.
