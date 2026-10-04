# THE GAME — Evolved Skill Registry

Status: **ACTIVE TARGET-GAME DESIGN / CHILD OF PROGRESSION AUTHORITY**  
Parent:
- `docs/systems/PROGRESSION_CLASSES_RANKS_EVOLVED_GAME_DESIGN.md`
- `docs/systems/PROGRESSION_MASTER_PLAN.md`

Purpose: turn the current 23-skill runtime catalog into a reconstruction-grade game-design registry for the evolved game.

This document does not claim that all target uses, training activities, mentors, facilities, checks, class links, profession links, or UI are implemented.

---

# 1. Current reality

The current runtime defines exactly 23 registered skills in five families:

## Combat
- unarmed
- blades
- ranged
- defense
- tactics

## Physical
- athletics
- stealth
- traversal
- survival

## Technical
- engineering
- technical_systems
- medicine
- crafting

## Social
- persuasion
- deception
- intimidation
- empathy
- leadership

## Knowledge
- investigation
- history
- factions
- powers
- creatures

Current skill values use a 0–100 scale. Current training already supports time cost, stamina/focus consumption, mentor bonus, and diminishing returns.

This registry preserves those IDs as the first evolved-game skill foundation.

---

# 2. Registry design rules

Each skill must answer:

- what competence it represents;
- which attributes commonly support it;
- how the player practices it;
- what world activities consume it;
- what tactical/combat situations consume it;
- which classes commonly value it;
- which professions commonly value it;
- what equipment/facility dependencies may matter;
- what advanced progression gates can exist;
- what authored content must be created so the skill is more than a number.

Attribute relationships below are **design relationships**, not fixed formulas unless a future rules document explicitly defines one. A scene may reasonably pair the same skill with different attributes depending on the action.

Example:

- forcing open a warped hatch may use Might + Engineering;
- diagnosing why the hatch failed may use Intellect + Engineering;
- noticing a dangerous structural load may use Perception + Engineering.

The skill defines learned competence. The attribute defines how the character is applying that competence.

---

# 3. Combat skills

## 3.1 Unarmed

**Current family:** Combat

### Target identity
Practical fighting without a dedicated weapon, including striking, clinch control, escapes, basic grappling, restraint, and close-quarters body control.

### Supporting attributes
Common:
- Might;
- Agility;
- Endurance.

Situational:
- Perception for timing/reading;
- Will for maintaining control under pressure.

### Training
- supervised drills;
- sparring;
- conditioning;
- defensive escape practice;
- controlled restraint practice;
- live combat experience.

### World uses
- nonlethal restraint;
- breaking or escaping holds;
- self-defense in places where weapons are unavailable or restricted;
- physical contest scenes;
- training/fitness activities.

### Tactical uses
- close-range attacks;
- shove/reposition;
- grapple/control;
- disarm attempts where rules permit;
- nonlethal takedown;
- escape from adjacent enemy control.

### Class affinity
Strong:
- Vanguard;
- Skirmisher.

Useful:
- Field Specialist;
- Envoy where security/bodyguard play exists.

### Profession affinity
- security;
- military/law-enforcement equivalents where canon supports them;
- field work;
- some civic/emergency professions.

### Advanced gates
- qualified instructor;
- live sparring;
- specialized restraint doctrine;
- high-risk field proof.

### Required content
- training scenes;
- sparring NPCs;
- nonlethal encounter options;
- restraint outcomes;
- unarmed animation/pose assets.

---

## 3.2 Blades

**Current family:** Combat

### Target identity
Competence with cutting/thrusting melee weapons and similar edged tools used as weapons.

### Supporting attributes
Common:
- Agility;
- Might;
- Perception.

Situational:
- Endurance for sustained fighting;
- Will under pressure.

### Training
- stance/footwork drills;
- target practice;
- supervised sparring;
- weapon maintenance and handling;
- live combat.

### World uses
- weapon familiarity;
- safe handling;
- judging blade condition;
- threatening display only where socially/legal appropriate;
- cutting tasks when a tool use overlaps.

### Tactical uses
- melee attack;
- guard pressure;
- parry-like defensive actions if supported;
- reach/position control;
- precise/nonlethal flat/blunt use only when the weapon permits it.

### Class affinity
Strong:
- Vanguard;
- Skirmisher.

### Profession affinity
Context-dependent:
- security;
- military;
- field protection roles.

### Equipment dependence
Actual blade type matters. The skill does not create a weapon.

### Advanced gates
- instructor;
- weapon-specific doctrine;
- live sparring;
- difficult tactical application.

### Required content
- blade families;
- handling/attack animations;
- training facilities;
- legal/cultural rules by region.

---

## 3.3 Ranged

**Current family:** Combat

### Target identity
Competence with ranged weapons and precision projectile systems supported by the setting.

### Supporting attributes
Common:
- Perception;
- Agility.

Situational:
- Will for composure;
- Endurance for sustained field use.

### Training
- range drills;
- target identification;
- firing/launch discipline;
- reload/handling practice;
- movement-and-fire drills;
- field engagements.

### World uses
- safe handling;
- judging firing lanes;
- identifying poor shooting positions;
- training/certification where institutions require it.

### Tactical uses
- ranged attack accuracy;
- target prioritization;
- precision shots;
- overwatch/reaction-like mechanics if the combat authority uses an original implementation;
- suppression/area denial where supported.

### Class affinity
Strong:
- Skirmisher.

Useful:
- Operator;
- Field Specialist.

### Profession affinity
Context-dependent:
- security;
- military;
- hunting/field roles if world canon supports them.

### Equipment dependence
Weapon family, ammunition/resource, condition, range, and sighting system remain equipment/system concerns.

### Advanced gates
- range qualification;
- moving targets;
- hostile conditions;
- specialized weapon family.

### Required content
- target range/training activity;
- ranged weapon families;
- firing poses;
- tactical sight-line UI.

---

## 3.4 Defense

**Current family:** Combat

### Target identity
Learned defensive combat technique: guarding, blocking, avoiding predictable attacks, protecting vulnerable positions, and maintaining safe structure.

### Supporting attributes
Common:
- Endurance;
- Agility;
- Perception.

Situational:
- Might for hard blocks;
- Will for maintaining discipline.

### Training
- guard drills;
- partner attack-response drills;
- shield/protective equipment practice if supported;
- sparring;
- pressure drills.

### World uses
- protecting another actor during dangerous physical events;
- safely moving through hostile situations;
- bodyguard/security scenes.

### Tactical uses
- guard;
- defensive stance;
- block/parry contributions;
- ally protection;
- reaction defense;
- reduced exposure while repositioning.

### Class affinity
Strong:
- Vanguard.

Useful:
- Field Specialist;
- Skirmisher.

### Profession affinity
- security;
- emergency/escort work;
- military where canon supports it.

### Advanced gates
- sustained pressure;
- protection of another actor;
- specialized defensive equipment;
- elite instructor.

### Required content
- defensive stance/pose assets;
- protection encounters;
- sparring drills;
- tactical defense feedback.

---

## 3.5 Tactics

**Current family:** Combat

### Target identity
Understanding positioning, tempo, objectives, threat priority, team coordination, terrain use, and encounter-level decision making.

### Supporting attributes
Common:
- Intellect;
- Perception.

Situational:
- Presence for command;
- Will for pressure decisions.

### Training
- tactical exercises;
- after-action analysis;
- simulation;
- mentor instruction;
- field leadership;
- studying prior encounters.

### World uses
- planning dangerous routes;
- evaluating defensive positions;
- interpreting security layouts;
- anticipating likely enemy behavior.

### Tactical uses
- initiative/plan advantages where justified;
- better preview of threats;
- coordinated team actions;
- terrain/cover exploitation;
- retreat/engagement planning;
- objective prioritization.

### Class affinity
Strong:
- Vanguard;
- Skirmisher;
- Operator.

Useful:
- Envoy;
- Investigator.

### Profession affinity
- security;
- military;
- logistics;
- emergency coordination.

### Advanced gates
- complex simulations;
- real multi-actor operations;
- command responsibility;
- review of failures/successes.

### Required content
- tactical training exercises;
- after-action review activity;
- encounter intelligence systems;
- team-command interactions.

---

# 4. Physical skills

## 4.1 Athletics

**Current family:** Physical

### Target identity
General physical conditioning and controlled exertion: sprinting, climbing strength, jumping, swimming where applicable, sustained effort, and body control.

### Supporting attributes
Common:
- Endurance;
- Agility;
- Might.

### Training
- running;
- conditioning;
- climbing drills;
- resistance work;
- obstacle courses;
- field exertion.

### World uses
- chase scenes;
- lifting/moving with technique;
- long climbs;
- physical escape;
- maintaining pace under fatigue.

### Tactical uses
- movement efficiency;
- evasion contribution;
- sprint/rapid reposition;
- physical recovery between bursts.

### Class affinity
Strong:
- Skirmisher;
- Vanguard.

Useful:
- Field Specialist.

### Profession affinity
- field work;
- emergency services;
- manual occupations;
- security.

### Advanced gates
- harder terrain;
- higher intensity;
- coached conditioning;
- injury-safe training.

### Required content
- conditioning activities;
- obstacle/training areas;
- fatigue-aware encounters.

---

## 4.2 Stealth

**Current family:** Physical

### Target identity
Avoiding detection through movement discipline, concealment, timing, noise control, and use of environmental cover.

### Supporting attributes
Common:
- Agility;
- Perception.

Situational:
- Will for patience;
- Intellect for planned infiltration.

### Training
- movement drills;
- observation/avoidance exercises;
- low-light practice;
- route planning;
- field use.

### World uses
- bypassing watchers;
- eavesdropping positions;
- avoiding wildlife/beasts;
- infiltration;
- escaping pursuit.

### Tactical uses
- concealed approach;
- opening-position advantage;
- breaking line of sight;
- avoiding reaction fire/attention where rules support it.

### Class affinity
Strong:
- Skirmisher;
- Investigator.

Useful:
- Operator.

### Profession affinity
Context-dependent:
- reconnaissance;
- investigation;
- security testing.

### Advanced gates
- trained observers;
- difficult lighting/noise conditions;
- surveillance systems;
- hostile territory.

### Required content
- concealment states;
- detection logic;
- stealth-capable locations;
- visual/noise feedback.

---

## 4.3 Traversal

**Current family:** Physical

### Target identity
Navigating difficult built and natural environments safely and efficiently.

### Supporting attributes
Common:
- Agility;
- Perception;
- Endurance.

Situational:
- Might for climbs;
- Intellect for technical route interpretation.

### Training
- ladders/scaffolds;
- climbing routes;
- balance;
- controlled drops;
- rope/tool use where supported;
- repeated route practice.

### World uses
- alternative routes;
- vertical access;
- damaged infrastructure;
- tight maintenance spaces;
- environmental shortcuts.

### Tactical uses
- elevation changes;
- vault/climb actions;
- route access;
- flanking through difficult terrain.

### Class affinity
Strong:
- Skirmisher;
- Field Specialist.

Useful:
- Operator.

### Profession affinity
- maintenance;
- infrastructure;
- field survey;
- emergency work.

### Advanced gates
- hazardous routes;
- specialized gear;
- weather/environmental stress;
- high-consequence climbs.

### Required content
- authored traversal anchors/routes;
- climbing/ladder sprites;
- route difficulty metadata;
- fail/safe-recovery outcomes.

---

## 4.4 Survival

**Current family:** Physical

### Target identity
Staying functional outside secure civic support: shelter, field safety, navigation fundamentals, exposure management, resource awareness, and basic expedition discipline.

### Supporting attributes
Common:
- Perception;
- Endurance;
- Intellect.

### Training
- field exercises;
- route planning;
- shelter practice;
- environmental identification;
- mentor-led expeditions.

### World uses
- dangerous-region travel;
- resource planning;
- hazard recognition;
- exposure mitigation;
- camp/rest quality;
- avoiding environmental mistakes.

### Tactical uses
Indirect:
- better pre-encounter preparation;
- hazard awareness;
- terrain exploitation;
- retreat route judgment.

### Class affinity
Strong:
- Field Specialist.

Useful:
- Skirmisher;
- Investigator.

### Profession affinity
- field work;
- survey;
- expedition/logistics;
- resource professions.

### Advanced gates
- harsh climate;
- long expeditions;
- unfamiliar ecosystem;
- beast-zone exposure.

### Required content
- field travel events;
- environmental hazards;
- expedition activities;
- survival mentors/facilities.

---

# 5. Technical skills

## 5.1 Engineering

**Current family:** Technical

### Target identity
Understanding and manipulating physical systems, structures, mechanisms, power/mechanical assemblies, and designed infrastructure.

### Supporting attributes
Common:
- Intellect;
- Perception.

Situational:
- Might for heavy physical work;
- Agility for delicate assembly.

### Training
- supervised repair;
- technical study;
- workshop practice;
- diagnostics;
- component teardown/rebuild;
- field repair.

### World uses
- structural diagnosis;
- repair;
- safe bypass;
- mechanism construction;
- interpreting infrastructure;
- evaluating damage.

### Tactical uses
- environmental manipulation;
- disabling/repairing devices;
- creating routes;
- restoring cover or machinery where combat design permits.

### Class affinity
Strong:
- Operator.

Useful:
- Field Specialist;
- Investigator.

### Profession affinity
- infrastructure;
- maintenance;
- engineering;
- municipal technical work;
- research support.

### Advanced gates
- specialist tools;
- advanced workshop;
- rare system knowledge;
- dangerous live repair.

### Required content
- workbenches;
- repair activities;
- component/structure records;
- technical mentors;
- equipment/tool assets.

---

## 5.2 Technical Systems

**Current family:** Technical

### Target identity
Operating, diagnosing, configuring, and interacting with electronic/digital/control systems and other setting-specific technical interfaces.

### Supporting attributes
Common:
- Intellect;
- Perception.

Situational:
- Will under time pressure;
- Agility for delicate physical interface work.

### Training
- terminals;
- diagnostics;
- control-panel exercises;
- supervised system work;
- troubleshooting;
- real maintenance incidents.

### World uses
- relay diagnostics;
- terminal access;
- municipal system operation;
- sensor/control interpretation;
- safe system restart;
- fault tracing.

### Tactical uses
- interact with powered terrain/devices;
- disable or redirect systems;
- use sensors;
- support team information.

### Class affinity
Strong:
- Operator.

Useful:
- Investigator;
- Ability Specialist where powers interface with technology.

### Profession affinity
- municipal systems;
- technical operations;
- maintenance;
- research;
- communications/control work.

### Advanced gates
- protected systems;
- live infrastructure;
- incomplete diagnostics;
- unfamiliar architecture;
- authorization requirements.

### Required content
- terminals/panels;
- diagnostic tools;
- fault states;
- technical mini-scenarios;
- player-safe system readouts.

---

## 5.3 Medicine

**Current family:** Technical

### Target identity
Assessment, stabilization, treatment, recovery planning, injury management, and practical medical knowledge within the game's setting.

### Supporting attributes
Common:
- Intellect;
- Perception.

Situational:
- Empathy via social skill interaction;
- Will under emergency pressure;
- Agility for precise procedures.

### Training
- study;
- clinic practice;
- supervised treatment;
- simulation;
- field stabilization;
- recovery care.

### World uses
- diagnose visible injury;
- stabilize NPCs;
- improve recovery;
- determine treatment needs;
- identify unsafe activity;
- support rehabilitation.

### Tactical uses
- stabilize wounded actors;
- treat conditions;
- reduce persistent consequences;
- triage.

### Class affinity
Strong:
- Field Specialist.

Useful:
- Investigator;
- Envoy.

### Profession affinity
- medical;
- emergency response;
- clinic/support work.

### Advanced gates
- supervised clinical practice;
- complex injury;
- scarce equipment;
- high-pressure treatment.

### Required content
- clinics;
- medical mentors;
- treatment items/tools;
- injury states;
- recovery activities;
- medical poses/animations.

---

## 5.4 Crafting

**Current family:** Technical

### Target identity
Fabricating, modifying, maintaining, and repairing useful objects from available materials when the relevant recipe/knowledge/tools exist.

### Supporting attributes
Common:
- Intellect;
- Agility.

Situational:
- Might for heavy fabrication;
- Perception for quality inspection.

### Training
- workshop practice;
- apprenticeship;
- repair work;
- prototype building;
- recipe/manual study.

### World uses
- repair;
- fabrication;
- modifications;
- consumable/tool preparation;
- equipment upkeep if durability systems are approved.

### Tactical uses
Mostly pre/post encounter:
- prepare tools;
- field repairs;
- deployable utility items where approved.

### Class affinity
Useful:
- Operator;
- Field Specialist.

### Profession affinity
- craft;
- maintenance;
- technical trades;
- workshop employment.

### Advanced gates
- specialized bench;
- rare materials;
- advanced patterns;
- mentor;
- quality-control challenge.

### Required content
- recipes/patterns;
- material provenance;
- workstations;
- crafting animations/UI;
- quality rules only if approved by economy/item authority.

---

# 6. Social skills

## 6.1 Persuasion

**Current family:** Social

### Target identity
Convincing another actor through credible argument, negotiation, framing, incentives, and relationship-aware communication.

### Supporting attributes
Common:
- Presence;
- Intellect.

Situational:
- Empathy as a separate skill interaction;
- Factions/History knowledge for credible context.

### Training
- negotiation practice;
- public interaction;
- mentorship;
- professional work;
- repeated social problem solving.

### World uses
- negotiate access;
- reduce conflict;
- secure cooperation;
- bargain where economy permits;
- persuade NPCs toward an action they can plausibly accept.

### Tactical uses
Potential nonviolent encounter options:
- surrender;
- ceasefire;
- coordination;
- hostage/nonlethal negotiation where authored.

### Class affinity
Strong:
- Envoy.

Useful:
- Investigator.

### Profession affinity
- trade;
- administration;
- leadership;
- civic/public-facing work.

### Advanced gates
- resistant audiences;
- high stakes;
- faction conflict;
- weak leverage.

### Required content
- negotiation scenes;
- NPC motive data;
- social consequence tracking;
- dialogue variants.

---

## 6.2 Deception

**Current family:** Social

### Target identity
Creating or maintaining false impressions through controlled statements, omissions, misdirection, disguise behavior, and consistency.

### Supporting attributes
Common:
- Presence;
- Intellect.

Situational:
- Will for pressure;
- Empathy for reading suspicion;
- Factions/History for believable cover stories.

### Training
- role practice;
- controlled social exercises;
- field deception;
- studying institutional procedures.

### World uses
- cover identity;
- conceal intent;
- misdirect questioning;
- bluff access;
- protect secrets.

### Tactical uses
Limited and contextual:
- feint intent;
- manipulate hostile attention;
- buy time.

### Class affinity
Useful:
- Envoy;
- Investigator;
- Skirmisher.

### Profession affinity
Context-dependent:
- intelligence/investigative roles;
- negotiation;
- undercover/security work if canon supports it.

### Advanced gates
- informed interrogators;
- evidence consistency;
- repeated lie continuity;
- high-suspicion targets.

### Required content
- suspicion/memory consequences;
- cover-story state;
- fact consistency checks.

---

## 6.3 Intimidation

**Current family:** Social

### Target identity
Applying credible pressure, threat, dominance, or consequence awareness to alter behavior.

### Supporting attributes
Common:
- Presence;
- Will.

Situational:
- Might where physical credibility matters;
- Factions/Reputation where authority matters.

### Training
- command/security experience;
- controlled confrontation;
- field exposure;
- institutional authority roles.

### World uses
- force compliance;
- deter aggression;
- pressure information;
- establish boundaries.

### Tactical uses
- morale pressure;
- force retreat/surrender where plausible;
- interrupt weak-willed opponents.

### Class affinity
Useful:
- Vanguard;
- Envoy.

### Profession affinity
- security;
- command;
- enforcement roles where canon supports them.

### Advanced gates
- fearless targets;
- superior enemy position;
- weak credibility;
- consequences for abuse.

### Required content
- fear/suspicion/reputation reactions;
- nonlethal confrontation outcomes;
- social backlash.

---

## 6.4 Empathy

**Current family:** Social

### Target identity
Reading emotional state, perspective, interpersonal tension, and likely social needs without automatically knowing hidden facts.

### Supporting attributes
Common:
- Perception;
- Presence.

Situational:
- Intellect for structured analysis;
- Will for emotional control.

### Training
- counseling-like practice;
- social observation;
- mentorship;
- repeated relationship interaction;
- reflective activities.

### World uses
- detect discomfort;
- choose better dialogue approach;
- recognize grief/fear/anger;
- support relationships;
- identify when pressure would backfire.

### Tactical uses
Indirect:
- assess morale;
- recognize panic;
- support ally stabilization.

### Class affinity
Strong:
- Envoy.

Useful:
- Investigator;
- Field Specialist.

### Profession affinity
- medical;
- social/civic;
- leadership;
- negotiation.

### Advanced gates
- concealed emotion;
- cultural differences;
- trauma;
- conflicting incentives.

### Required content
- richer NPC emotional state;
- player-safe tells;
- relationship consequences;
- supportive dialogue.

---

## 6.5 Leadership

**Current family:** Social

### Target identity
Coordinating people toward a shared objective through clarity, confidence, planning, responsibility, and trust.

### Supporting attributes
Common:
- Presence;
- Will.

Situational:
- Intellect for planning;
- Tactics for combat command;
- Empathy for morale.

### Training
- team responsibility;
- supervision;
- command exercises;
- crisis management;
- faction/institution duties.

### World uses
- organize workers;
- coordinate evacuations;
- lead expeditions;
- manage group tasks;
- delegate.

### Tactical uses
- team coordination;
- morale support;
- synchronized actions;
- command bonuses only where explicit combat rules support them.

### Class affinity
Strong:
- Envoy.

Useful:
- Vanguard;
- Investigator.

### Profession affinity
- management;
- civic administration;
- security command;
- logistics.

### Advanced gates
- larger groups;
- crisis conditions;
- divided loyalties;
- responsibility for failure.

### Required content
- party/group systems;
- command events;
- delegated tasks;
- leadership consequences.

---

# 7. Knowledge skills

## 7.1 Investigation

**Current family:** Knowledge

### Target identity
Systematically finding, evaluating, connecting, and testing evidence.

### Supporting attributes
Common:
- Perception;
- Intellect.

### Training
- case review;
- evidence exercises;
- archive work;
- field investigation;
- mentor critique.

### World uses
- inspect scenes;
- connect clues;
- identify contradictions;
- reconstruct events;
- locate hidden but discoverable information.

### Tactical uses
- identify encounter clues;
- recognize weak points only when evidence supports it;
- improve preparation.

### Class affinity
Strong:
- Investigator.

Useful:
- Operator;
- Envoy.

### Profession affinity
- investigation;
- records;
- research;
- security.

### Advanced gates
- incomplete evidence;
- deception;
- contaminated scene;
- multi-step causal reconstruction.

### Required content
- evidence records;
- clue graph;
- inspection interactions;
- archive/research support.

---

## 7.2 History

**Current family:** Knowledge

### Target identity
Knowledge of past events, institutions, conflicts, technologies, places, cultural developments, and historical context.

### Supporting attributes
Common:
- Intellect.

Situational:
- Perception for recognizing artifacts;
- Factions as complementary knowledge.

### Training
- study;
- archives;
- oral history;
- museums/records;
- expert mentors.

### World uses
- identify old structures;
- understand precedent;
- recognize symbols;
- interpret documents;
- unlock historically informed dialogue.

### Tactical uses
Indirect:
- recognize old fortifications/equipment/doctrine where relevant.

### Class affinity
Useful:
- Investigator;
- Envoy;
- Operator.

### Profession affinity
- research;
- archives;
- administration;
- education.

### Advanced gates
- restricted archives;
- disputed records;
- specialist language/context;
- rare primary sources.

### Required content
- historical records;
- archive locations;
- lore sources;
- knowledge provenance.

---

## 7.3 Factions

**Current family:** Knowledge

### Target identity
Understanding organizations, their structure, leadership, customs, interests, alliances, rivalries, rank systems, and public behavior.

### Supporting attributes
Common:
- Intellect;
- Perception.

Situational:
- Presence for using the knowledge socially.

### Training
- study;
- direct faction exposure;
- interviews;
- observation;
- institutional work.

### World uses
- recognize rank/insignia;
- predict protocol;
- understand jurisdiction;
- identify likely allies/conflicts;
- avoid social mistakes.

### Tactical uses
- infer doctrine/behavior of organized opponents;
- identify command relationships.

### Class affinity
Strong:
- Investigator;
- Envoy.

Useful:
- Tactics-oriented builds.

### Profession affinity
- administration;
- security;
- diplomacy/trade;
- research.

### Advanced gates
- secret structures;
- internal politics;
- misinformation;
- splinter groups.

### Required content
- faction records;
- rank insignia assets;
- doctrine/protocol data;
- player-safe faction knowledge.

---

## 7.4 Powers

**Current family:** Knowledge

### Target identity
Understanding the setting's exceptional abilities, their observable behavior, known theory, risks, counters, training traditions, and documented phenomena.

### Supporting attributes
Common:
- Intellect;
- Perception.

Situational:
- Will for controlled practical study;
- ability-specific attributes.

### Training
- study;
- supervised observation;
- controlled experimentation;
- mentor instruction;
- direct ability experience.

### World uses
- identify phenomena;
- interpret ability residue/effects;
- recognize danger;
- understand training material;
- support technique discovery.

### Tactical uses
- identify known counters;
- interpret enemy ability behavior;
- improve informed response.

### Class affinity
Strong:
- Ability Specialist.

Useful:
- Investigator;
- Operator.

### Profession affinity
- research;
- specialist medical/technical roles if canon supports them.

### Advanced gates
- rare phenomena;
- restricted knowledge;
- dangerous experimentation;
- conflicting theories.

### Required content
- power codex;
- research facilities;
- mentors;
- observation events;
- hidden vs known requirement handling.

---

## 7.5 Creatures

**Current family:** Knowledge

### Target identity
Knowledge of nonhuman/hostile creature biology, behavior, habitat, signs, threat patterns, and resource provenance.

### Supporting attributes
Common:
- Intellect;
- Perception.

Situational:
- Survival for field interpretation.

### Training
- field observation;
- study;
- specimen records;
- hunter/researcher mentors where canon supports them;
- encounter analysis.

### World uses
- identify tracks/signs;
- estimate threat;
- predict habitat;
- understand behavior;
- identify safe handling and valuable materials.

### Tactical uses
- recognize attack patterns;
- identify vulnerable/armored regions when known;
- choose safer engagement or avoidance strategy.

### Class affinity
Useful:
- Field Specialist;
- Investigator;
- Skirmisher.

### Profession affinity
- research;
- field survey;
- medical/biological specialties;
- resource work.

### Advanced gates
- rare species;
- incomplete records;
- altered behavior;
- elite/beast-zone variants.

### Required content
- creature codex;
- habitat records;
- encounter observations;
- loot/material provenance links.

---

# 8. Cross-skill interaction

The evolved game should reward combinations rather than isolated maxed values.

Examples:

- **Engineering + Technical Systems** — diagnose both physical and control-layer failure.
- **Medicine + Empathy** — treat an injured person while managing fear/trust.
- **Investigation + Factions** — understand why evidence matters politically.
- **Survival + Creatures** — read field signs correctly.
- **Stealth + Traversal** — reach a concealed route without being detected.
- **Persuasion + History** — make a culturally credible argument.
- **Tactics + Leadership** — coordinate a team instead of merely understanding the battlefield.
- **Powers + Investigation** — distinguish an exceptional phenomenon from an ordinary failure.

Combination checks must remain authored and understandable. The engine should not silently sum unrelated skills.

---

# 9. Training and plateau policy

All 23 skills follow the same high-level growth philosophy:

1. beginner practice can be broadly available;
2. routine repetition gives diminishing returns;
3. advanced competence requires better difficulty, feedback, facilities, mentors, field use, or specialized knowledge;
4. elite competence requires meaningful proof, not idle repetition;
5. failures can teach when the action plausibly provides feedback;
6. catastrophic or trivial spam should not be the optimal progression path.

Future child authority:
`SKILL_TRAINING_MENTOR_FACILITY_STANDARD.md`

---

# 10. Skill visibility

All 23 current skills are registered system concepts, but the UI does not need to overwhelm the player.

Target UX rules:

- group by family;
- show base/effective value;
- show qualitative mastery descriptor;
- show recent meaningful progress;
- show known training opportunities;
- show known dependencies;
- do not expose hidden mentors, secret facilities, or undiscovered progression gates;
- inspection can explain why an effective value differs from base.

---

# 11. Skill-content minimum

A skill should not be considered fully integrated into the evolved game until it has at least:

- one repeatable or reusable training path;
- one meaningful world-use pattern;
- one high-value authored use;
- one progression gate or advanced learning route;
- one UI explanation;
- one test/validation contract when implemented.

Combat skills additionally need tactical consumption.
Social skills need NPC-state consequences.
Knowledge skills need discoverable information content.
Technical skills need tools/facilities/system targets.
Physical skills need environment interactions.

---

# 12. Pixel-art requirements

The skill system requires authored pixel-art presentation, generated and extracted through the project workflow.

Minimum future visual family:

- five skill-family icons;
- one icon per skill if individual icons are retained;
- training/facility markers;
- mentor/trainer markers where appropriate;
- compact progress indicator;
- plateau/advanced-training state indicator;
- skill detail panel accents.

Character training visuals must use authored pixel sprites/poses. Do not build training characters from geometric primitives.

---

# 13. Gate Twelve first-use mapping

Gate Twelve should exercise a representative subset early:

- Technical Systems;
- Engineering;
- Investigation;
- Persuasion;
- Empathy;
- Athletics;
- Traversal;
- Powers.

Secondary opportunities should introduce:

- Factions;
- History;
- Medicine;
- Tactics;
- Stealth.

Combat skills should appear only where the authored Gate Twelve story/encounter design justifies combat or training.

The proof region should demonstrate that skills create different approaches, not separate disconnected stories.

---

# 14. Future expansion rule

A new skill may be added only when:

- its gameplay competence is meaningfully distinct from all existing skills;
- it has repeatable world use;
- it has a viable training path;
- it has enough authored content to justify permanent UI/state weight;
- its relationship to classes/professions is documented.

Do not add skills merely to make the list larger.

---

# 15. Reconstruction checklist

A future developer or AI should be able to answer:

- which 23 skills currently exist;
- what each one means;
- which attributes commonly support each;
- how each can be trained;
- how each changes world interaction;
- how combat skills affect tactical play;
- which classes/professions commonly value each;
- what advanced learning gates exist;
- what content/assets are required for each family;
- how skill combinations create alternative approaches;
- which parts are current runtime facts versus evolved target design.

If those answers require guessing, this registry is incomplete.
