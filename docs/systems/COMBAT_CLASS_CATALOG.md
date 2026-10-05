# THE GAME — Combat Class Catalog

Status: **ACTIVE TARGET-GAME DESIGN / D-045 CHILD / RUNTIME NOT IMPLEMENTED**  
Parent authorities:
- `docs/systems/PROGRESSION_CLASSES_RANKS_EVOLVED_GAME_DESIGN.md`
- `docs/systems/PROGRESSION_MASTER_PLAN.md`
- `docs/systems/EVOLVED_SKILL_REGISTRY.md`

Integration authorities:
- `docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md`
- `docs/systems/TRAINING_AND_PRACTICE_ACTIVITY_STANDARD.md`
- `docs/systems/PHASE_1_PROGRESSION_SCHEMA_API_MIGRATION_PACKET.md`
- `docs/systems/STATUS_UI_ABILITIES_AND_PASSIVES_MASTER_PLAN.md`

Task:
- D-045 — evolved progression/classes reconstruction;
- Parallel P3 bounded child — combat class catalog.

This document defines the first reconstruction-grade combat/adventure class catalog for THE GAME.

It does **not** claim:
- that class state exists in the current runtime;
- that the proposed class IDs are already save-compatible canon IDs;
- that class features are implemented;
- that final balance thresholds are selected;
- that any proposed specialization name is canon;
- that profession, faction rank, institutional authority, global Level, ability rank, or social status are the same thing as combat class.

---

# 1. Authority boundary — CURRENT / TARGET / PROPOSAL

## 1.1 CURRENT REALITY

The current authoritative game already has:
- seven core attributes: Might, Agility, Endurance, Intellect, Will, Perception, Presence;
- 23 registered skills;
- derived combat/status values;
- ordinary player resources;
- ability and technique mastery;
- time-bound skill training;
- player-safe progression projection;
- save-schema-v1 persistence for current progression state.

The current `GameState` does **not** have a durable combat-class record.

The current Phase 1 progression migration packet explicitly says not to add a second top-level progression owner merely to support the bounded Gate Twelve proof.

Therefore:
- no runtime class container is created by this catalog;
- no save migration is implied by file existence;
- current skill/ability state remains authoritative where it already exists;
- future class implementation requires its own accepted schema/API/save migration decision.

## 1.2 TARGET DESIGN

The evolved game uses seven functional combat/adventure class families:
1. Vanguard;
2. Skirmisher;
3. Operator;
4. Field Specialist;
5. Investigator;
6. Envoy;
7. Ability Specialist.

A class is an **earned discipline** expressing how a character applies existing attributes, skills, abilities, equipment, knowledge, training, and field experience.

A class is not selected as a permanent identity at character creation.

Class advancement is built from four evidence dimensions already established by the parent authority:
- Foundation;
- Practice;
- Field Proof;
- Specialization.

Classes must integrate with world activities and tactical play without becoming an isolated XP ladder.

## 1.3 PROPOSAL-ONLY CONTENT

The following items in this catalog are proposals until accepted by later canon/balance/migration work:
- target class IDs such as `CLASS_VANGUARD`;
- exact class unlock thresholds;
- exact feature names;
- exact specialization names/counts;
- numeric feature values;
- final mentor/facility requirements;
- final world-facing class terminology;
- final class icons/insignia;
- any persistent class-state schema.

Where this document uses a proposed ID or feature label, it is a design handle, not proof of runtime or canon adoption.

---

# 2. Class design principles

## 2.1 Class is a discipline, not a replacement character sheet

Class mechanics consume existing systems.

A class may:
- unlock new legal tactical actions;
- improve access to discipline-specific training;
- unlock reactions or interaction options;
- expose class-specific explanations or progression goals;
- qualify the character for specialization training;
- make certain combinations of existing capabilities more effective.

A class must not:
- erase base attributes;
- replace current skills with class-only copies;
- create a second inventory;
- create a second ability system;
- create a second injury system;
- create a second tactical rules engine;
- make profession/faction/institution rank synonymous with combat power.

## 2.2 Demonstrated competence over menu selection

Class acquisition should be inferred from persistent evidence such as:
- registered skill competence;
- completed training;
- relevant techniques;
- equipment familiarity where meaningful;
- knowledge;
- mentor/facility access;
- field-use history;
- class-relevant proof events.

The exact numeric thresholds remain a later balance packet.

## 2.3 No universal combat superiority

Each family must produce a distinct problem-solving profile.

A class feature should generally create:
- a new option;
- better reliability in its discipline;
- better information;
- better action economy in a narrowly defined context;
- better recovery/control;
- stronger integration between existing systems.

Avoid universal flat bonuses that make one class strictly better in all encounters.

## 2.4 Opportunity cost owns build limits

Cross-training is allowed.

The evolved game discourages effortless completion of every class through:
- world-time cost;
- mentor availability;
- facility access;
- competing activities;
- specialization depth;
- field-proof requirements;
- knowledge/equipment dependencies.

The limit is opportunity cost rather than arbitrary hard lockout.

## 2.5 Player and NPC parity

Persistent NPCs may use the same class semantics where appropriate.

NPC classes must not grant hidden exceptions to:
- equipment requirements;
- injury persistence;
- ability costs;
- tactical legality;
- knowledge limits.

Encounter-only NPC templates may use compressed authoring, but their visible behavior must remain compatible with the same tactical/world rules.

---

# 3. Target class-definition record

A future class definition should be able to answer these fields.

This is a semantic target record, not a committed runtime schema.

- `class_id` — proposed stable target identifier;
- `working_name`;
- `family`;
- `design_status`;
- `identity`;
- `attribute_affinities`;
- `signature_skill_group`;
- `supporting_skill_group`;
- `ability_relationship`;
- `equipment_relationship`;
- `knowledge_relationship`;
- `entry_evidence`;
- `training_modes`;
- `mentor_dependencies`;
- `facility_dependencies`;
- `field_proof_types`;
- `feature_families`;
- `tactical_role_tags`;
- `world_role_tags`;
- `specialization_axes`;
- `cross_training_links`;
- `failure_or_plateau_conditions`;
- `player_safe_preview`;
- `content_requirements`;
- `test_requirements`;
- `provenance`.

A future durable character class record, if approved, must be designed by migration work rather than copied blindly from this definition record.

---

# 4. Acquisition and progression contract

## 4.1 Eligibility query

Class eligibility is read-only.

Checking whether a player qualifies must never:
- spend resources;
- advance time;
- award a class;
- generate rewards;
- mutate skill state;
- mutate social state.

## 4.2 Foundation

Foundation proves the player has a coherent base in the discipline.

Target evidence categories:
- at least one signature competency cluster;
- supporting attribute capability;
- relevant practice history;
- basic knowledge/equipment handling when the class depends on it.

Exact threshold logic is deferred.

## 4.3 Practice

Practice proves sustained training/use rather than one lucky check.

Evidence may come from:
- training activities;
- safe drills;
- field use;
- sparring/simulation;
- mentorship;
- technique practice;
- repeated world interactions.

Practice should consume real world time/resources through the activity system.

## 4.4 Field Proof

Field Proof proves the class can be applied under meaningful consequences.

Examples:
- Vanguard protects another actor under pressure;
- Skirmisher solves a tactical problem through movement/precision;
- Operator safely manipulates a dangerous system;
- Field Specialist preserves life/readiness during an expedition;
- Investigator turns evidence into actionable knowledge;
- Envoy changes a conflict through social leverage;
- Ability Specialist controls exceptional ability behavior under real constraints.

Field Proof is not automatically “win a combat.”

## 4.5 Specialization

Specialization narrows or transforms a class.

It should:
- deepen a play pattern;
- require additional practice/field evidence;
- create distinctive features;
- preserve previously earned baseline competence;
- remain separate from profession and faction rank.

Exact branch names/counts remain proposal-only.

## 4.6 Failure and plateau

Class progression may pause when:
- required skills plateau;
- mentor/facility access is missing;
- relevant injury/condition blocks training;
- required knowledge has not been learned;
- field-proof conditions have not occurred;
- ability control remains unsafe.

A plateau is a progression problem to solve in the world, not a reason for UI-side arbitrary XP injection.

---

# 5. Feature ownership rules

Class features must declare their authoritative owner.

| Feature type | Owning system |
| --- | --- |
| new tactical action permission | tactical combat rules |
| movement/position option | movement/pathing |
| cover/defense interaction | cover/action resolution |
| information reveal | knowledge/LOS/detection |
| ally coordination | tactical + social/party rules |
| injury stabilization | condition/medical rules |
| device/environment interaction | world/technical interaction |
| ability efficiency/control | ability/power authority |
| training efficiency | activity/progression rules |
| equipment handling | equipment rules |
| class unlock/progress | future class progression authority |

A class definition may request behavior from another system, but it does not duplicate that system's formula.

---

# 6. Class family catalog summary

| Working family | Proposed target ID | Primary discipline | Strong current-skill anchors |
| --- | --- | --- | --- |
| Vanguard | `CLASS_VANGUARD` | protection, pressure, close control | Unarmed, Blades, Defense, Tactics, Athletics |
| Skirmisher | `CLASS_SKIRMISHER` | mobility, precision, route control | Unarmed, Blades, Ranged, Tactics, Athletics, Stealth, Traversal |
| Operator | `CLASS_OPERATOR` | systems, devices, environment control | Tactics, Engineering, Technical Systems |
| Field Specialist | `CLASS_FIELD_SPECIALIST` | survival, medicine, logistics | Survival, Medicine |
| Investigator | `CLASS_INVESTIGATOR` | evidence, awareness, actionable knowledge | Stealth, Investigation, Factions |
| Envoy | `CLASS_ENVOY` | negotiation, leadership, coordination | Persuasion, Empathy, Leadership, Factions |
| Ability Specialist | `CLASS_ABILITY_SPECIALIST` | deep exceptional-ability control | Powers |

The IDs are **PROPOSAL**, while the seven working families are established TARGET design.

---

# 7. Vanguard

## 7.1 Status

- **Family:** TARGET.
- **Working name:** Vanguard.
- **Proposed ID:** `CLASS_VANGUARD`.
- **Runtime:** not implemented.

## 7.2 Identity

Vanguard is the discipline of direct engagement, protection, pressure, and controlled staying power.

The class should make a character better at holding dangerous space and protecting a team without turning high health into its only identity.

## 7.3 Attribute affinities

Primary target affinities:
- Might;
- Endurance.

Important situational affinities:
- Agility;
- Will;
- Perception.

These are relationships, not fixed formulas.

## 7.4 Skill anchors from the current 23-skill registry

Strong:
- Unarmed;
- Blades;
- Defense;
- Tactics;
- Athletics.

Useful:
- Intimidation;
- Leadership.

## 7.5 Entry evidence

A future Vanguard entry pattern should require a coherent combination of:
- defensive/close-engagement competence;
- physical conditioning;
- tactical awareness;
- practice under pressure;
- at least one protection/control field proof.

No exact numeric threshold is selected here.

## 7.6 Feature families

Target feature families:
- **Brace / Hold:** better discipline-specific use of defensive actions and dangerous positions;
- **Interpose / Protect:** legal ally-protection options when tactical geometry permits;
- **Pressure:** close-range actions that influence enemy positioning without bypassing movement rules;
- **Controlled Force:** shove/restraint/guard-breaking options tied to existing combat skills;
- **Steady Under Pressure:** bounded interactions with conditions/morale only where the owning system supports them.

These are semantic feature families. Exact action costs/modifiers are deferred to tactical implementation/balance.

## 7.7 Tactical role

Common role tags:
- front-line control;
- ally protection;
- close engagement;
- objective holding;
- retreat-cover support.

Vanguard does not guarantee aggro or mind-control enemies.

## 7.8 World/adventure role

Potential non-combat relevance:
- dangerous physical access;
- escort/protection scenes;
- restraint/security interactions;
- emergency extraction;
- intimidating presence where social rules allow it.

## 7.9 Training dependencies

Likely training modes:
- conditioning;
- supervised defensive drills;
- sparring;
- restraint/control practice;
- tactical team drills;
- field protection exercises.

Facility families:
- practice yard;
- safe sparring space;
- conditioning facility;
- tactical drill area.

World-facing facility names remain proposal/canon work.

## 7.10 Specialization axes — PROPOSAL

Possible axes:
- protection / interception / objective defense;
- breach / pressure / forced-position control.

These are direction concepts, not final specialization names.

## 7.11 Cross-training

Natural links:
- Field Specialist for survival/stabilization;
- Envoy for leadership/security;
- Skirmisher for mobility;
- Ability Specialist when an ability supports close control.

---

# 8. Skirmisher

## 8.1 Status

- **Family:** TARGET.
- **Working name:** Skirmisher.
- **Proposed ID:** `CLASS_SKIRMISHER`.
- **Runtime:** not implemented.

## 8.2 Identity

Skirmisher is the discipline of movement, positioning, precision, route exploitation, pursuit, and disengagement.

It should reward solving geometry and visibility problems instead of merely adding ranged damage.

## 8.3 Attribute affinities

Primary:
- Agility;
- Perception.

Situational:
- Endurance;
- Will;
- Might.

## 8.4 Skill anchors

Strong:
- Unarmed;
- Blades;
- Ranged;
- Tactics;
- Athletics;
- Stealth;
- Traversal.

Useful:
- Defense;
- Survival;
- Deception;
- Creatures.

## 8.5 Entry evidence

A future entry pattern should prove:
- mobility/traversal competence;
- one credible attack/engagement skill;
- positioning awareness;
- controlled disengagement or precision field proof.

## 8.6 Feature families

Target feature families:
- **Reposition:** discipline-specific movement options that remain subject to occupancy/path rules;
- **Disengage:** safer withdrawal options where action-budget rules permit;
- **Precision Setup:** better use of aim/known-target information rather than free accuracy;
- **Route Exploit:** traversal/terrain options supported by the map;
- **Scout Pressure:** ability to convert legal observation/positioning into better tactical choices.

No feature reveals an undetected enemy by class ownership alone.

## 8.7 Tactical role

Common tags:
- mobile attacker;
- scout;
- flanker;
- pursuit;
- precision engagement;
- retreat/reposition specialist.

## 8.8 World/adventure role

Potential world uses:
- difficult routes;
- scouting;
- stealth approach;
- chase/escape;
- perimeter observation;
- creature tracking when supported by knowledge.

## 8.9 Training dependencies

Likely:
- movement drills;
- obstacle/traversal training;
- range/precision drills where canon supports ranged weapons;
- stealth exercises;
- pursuit/evasion;
- field route practice.

Facilities:
- obstacle/traversal route;
- controlled range if canon;
- field course;
- wilderness/urban route.

## 8.10 Specialization axes — PROPOSAL

Possible axes:
- precision / observation / ranged control;
- mobility / infiltration / close skirmish.

## 8.11 Cross-training

Natural links:
- Investigator for scouting/intel;
- Operator for device-assisted route control;
- Vanguard for close-combat durability;
- Field Specialist for expedition readiness.

---

# 9. Operator

## 9.1 Status

- **Family:** TARGET.
- **Working name:** Operator.
- **Proposed ID:** `CLASS_OPERATOR`.
- **Runtime:** not implemented.

## 9.2 Identity

Operator is the discipline of technical systems, devices, infrastructure, hazards, and environment manipulation.

This family intentionally grows from THE GAME's existing relay, workbench, Gate Twelve, municipal-system, and technical-skill identity.

It must not make every technical worker a combat Operator automatically.

## 9.3 Attribute affinities

Primary:
- Intellect;
- Perception.

Situational:
- Agility;
- Will;
- Endurance.

## 9.4 Skill anchors

Strong:
- Tactics;
- Engineering;
- Technical Systems.

Useful:
- Ranged;
- Stealth;
- Traversal;
- Crafting;
- Investigation;
- History;
- Powers where exceptional abilities interface with technology.

## 9.5 Entry evidence

A future entry pattern should prove:
- technical diagnosis competence;
- safe manipulation of systems/equipment;
- tactical awareness;
- at least one dangerous-system field proof;
- tool/equipment familiarity where the feature requires it.

## 9.6 Feature families

Target feature families:
- **System Read:** player-safe technical information that the character can legitimately infer;
- **Bypass / Restore:** technical interaction options with infrastructure;
- **Hazard Control:** disable, reroute, isolate, or exploit authored hazards;
- **Device Deployment:** use supported tools without inventing items from class state;
- **Environmental Advantage:** turn legal system interaction into tactical terrain/objective benefit.

The Operator never owns hidden world truth. Information must pass knowledge/privacy rules.

## 9.7 Tactical role

Common tags:
- environment control;
- objective interaction;
- device support;
- hazard management;
- technical support fire where equipment permits.

## 9.8 World/adventure role

Potential uses:
- repair;
- diagnostics;
- bypass;
- infrastructure restoration;
- technical investigation;
- equipment maintenance;
- controlled experimentation.

## 9.9 Training dependencies

Likely:
- workbench diagnostics;
- supervised system repair;
- fault isolation;
- tool drills;
- hazard simulation;
- field maintenance.

Facilities:
- technical workbench;
- diagnostic station;
- controlled systems lab;
- real infrastructure under authorized conditions.

## 9.10 Specialization axes — PROPOSAL

Possible axes:
- infrastructure / bypass / restoration;
- devices / hazards / field-control tools.

## 9.11 Cross-training

Natural links:
- Investigator for technical forensics;
- Field Specialist for expedition logistics;
- Ability Specialist for ability-technology interfaces;
- Skirmisher for mobile deployment.

---

# 10. Field Specialist

## 10.1 Status

- **Family:** TARGET.
- **Working name:** Field Specialist.
- **Proposed ID:** `CLASS_FIELD_SPECIALIST`.
- **Runtime:** not implemented.

## 10.2 Identity

Field Specialist is the discipline of survival, medicine, logistics, recovery, and sustained field readiness.

It is broader than “healer” and should remain useful before, during, and after combat.

## 10.3 Attribute affinities

Primary:
- Endurance;
- Intellect.

Situational:
- Perception;
- Will;
- Agility.

## 10.4 Skill anchors

Strong:
- Survival;
- Medicine.

Useful:
- Unarmed;
- Ranged;
- Defense;
- Athletics;
- Traversal;
- Engineering;
- Crafting;
- Empathy;
- Creatures.

## 10.5 Entry evidence

A future entry pattern should prove:
- survival or medical competence;
- reliable field preparation;
- safe use of required tools/supplies;
- a stabilization/recovery/logistics field proof.

## 10.6 Feature families

Target feature families:
- **Stabilize:** legal medical/condition actions owned by the injury/condition system;
- **Field Readiness:** preparation and support interactions, not free resource refills;
- **Supply Discipline:** better use/management of real inventory where rules permit;
- **Hazard Endurance:** environment-specific mitigation based on knowledge/equipment;
- **Assist Recovery:** improve access/quality of recovery when proper time/facilities/resources exist.

The class cannot conjure medical supplies or erase persistent injuries.

## 10.7 Tactical role

Common tags:
- stabilization;
- support;
- rescue;
- sustainment;
- objective assistance;
- casualty extraction.

## 10.8 World/adventure role

Potential uses:
- expedition planning;
- first aid;
- recovery;
- field camp readiness;
- environmental survival;
- creature-related hazard assessment.

## 10.9 Training dependencies

Likely:
- medical drills;
- supervised treatment;
- survival courses;
- evacuation drills;
- field logistics;
- recovery protocol training.

Facilities:
- clinic/medical station;
- field course;
- survival route;
- supply/logistics area.

## 10.10 Specialization axes — PROPOSAL

Possible axes:
- medical response / stabilization / recovery;
- expedition survival / logistics / environmental readiness.

## 10.11 Cross-training

Natural links:
- Vanguard for protection/rescue;
- Operator for technical field support;
- Investigator for evidence/medical diagnosis;
- Skirmisher for expedition mobility.

---

# 11. Investigator

## 11.1 Status

- **Family:** TARGET.
- **Working name:** Investigator.
- **Proposed ID:** `CLASS_INVESTIGATOR`.
- **Runtime:** not implemented.

## 11.2 Identity

Investigator is the discipline of awareness, deduction, evidence reconstruction, knowledge exploitation, and information control.

It must obey the distinction between:
- what exists in the simulation;
- what the character can perceive;
- what the character knows;
- what the player-safe UI may show.

## 11.3 Attribute affinities

Primary:
- Perception;
- Intellect.

Situational:
- Presence;
- Will;
- Agility.

## 11.4 Skill anchors

Strong:
- Stealth;
- Investigation;
- Factions.

Useful:
- Tactics;
- Survival;
- Engineering;
- Technical Systems;
- Medicine;
- Persuasion;
- Deception;
- Empathy;
- Leadership;
- History;
- Powers;
- Creatures.

This intentionally makes Investigator broad in supporting knowledge, but the class should require depth in an actual evidence/problem-solving pattern rather than treating every useful skill as mandatory.

## 11.5 Entry evidence

A future entry pattern should prove:
- investigative competence;
- evidence/knowledge use;
- observation discipline;
- one actionable reconstruction/weakness-identification field proof.

## 11.6 Feature families

Target feature families:
- **Reconstruct:** connect known evidence into player-safe conclusions;
- **Identify Weakness:** expose a tactical/world vulnerability only when evidence supports it;
- **Contradiction Detection:** unlock alternate dialogue/investigation paths;
- **Known-Intel Marking:** organize already-known facts for tactical use;
- **Prepared Inquiry:** gain better investigative options through prior knowledge.

No class feature may reveal private NPC state, hidden enemies, secret objectives, or undiscovered knowledge merely because the player has the class.

## 11.7 Tactical role

Common tags:
- reconnaissance;
- target analysis;
- known-intel support;
- detection support;
- objective analysis.

## 11.8 World/adventure role

Potential uses:
- scene reconstruction;
- records research;
- faction analysis;
- creature/power research;
- interviewing;
- technical/medical clue synthesis.

## 11.9 Training dependencies

Likely:
- archive/research work;
- case reconstruction;
- observation exercises;
- supervised investigation;
- field evidence collection;
- debrief analysis.

Facilities:
- archive;
- research station;
- evidence workspace;
- field investigation site.

## 11.10 Specialization axes — PROPOSAL

Possible axes:
- forensic/evidence reconstruction;
- tactical/field intelligence;
- social/faction analysis as a later branch if it remains distinct from Envoy.

## 11.11 Cross-training

Natural links:
- Operator for technical forensics;
- Envoy for interviews/faction leverage;
- Skirmisher for reconnaissance;
- Ability Specialist for exceptional-phenomena analysis.

---

# 12. Envoy

## 12.1 Status

- **Family:** TARGET.
- **Working name:** Envoy.
- **Proposed ID:** `CLASS_ENVOY`.
- **Runtime:** not implemented.

## 12.2 Identity

Envoy is the discipline of negotiation, leadership, coordination, intimidation, access, and conflict manipulation through social leverage.

It is not a “charisma damage” class.

## 12.3 Attribute affinities

Primary:
- Presence;
- Will.

Situational:
- Perception;
- Intellect;
- Endurance.

## 12.4 Skill anchors

Strong:
- Persuasion;
- Empathy;
- Leadership;
- Factions.

Useful:
- Unarmed where protection/security play exists;
- Tactics;
- Medicine;
- Deception;
- Intimidation;
- Investigation;
- History.

## 12.5 Entry evidence

A future entry pattern should prove:
- credible social competence;
- group/faction awareness;
- coordination or negotiation practice;
- one field proof where social leverage materially changes a conflict/outcome.

## 12.6 Feature families

Target feature families:
- **Coordinate:** ally-facing tactical support that respects party/tactical rules;
- **Negotiate:** alternate conflict-resolution options when actors are willing/able;
- **Rally:** bounded support under pressure without overriding condition/social authority;
- **Leverage:** use known faction/relationship facts to open options;
- **Pressure:** intimidation/coercion options with real consequence and resistance.

Envoy features do not mind-control NPCs and cannot expose private relationship values directly.

## 12.7 Tactical role

Common tags:
- team coordination;
- assist;
- surrender/de-escalation where encounter rules allow;
- morale/retreat support where implemented;
- objective negotiation.

## 12.8 World/adventure role

Potential uses:
- access negotiation;
- mediation;
- recruitment;
- faction communication;
- de-escalation;
- leadership;
- coercive negotiation with consequences.

## 12.9 Training dependencies

Likely:
- supervised negotiation;
- leadership exercises;
- mediation/debrief;
- faction/cultural study;
- team drills;
- real social field proof.

Facilities:
- no mandatory universal building;
- mentor-led instruction;
- institutional training site where canon supports it;
- meeting/debrief context;
- field social encounters.

## 12.10 Specialization axes — PROPOSAL

Possible axes:
- coordination / leadership / team support;
- negotiation / mediation / access;
- pressure / coercion as a distinct risk-heavy direction.

Exact branch count remains open.

## 12.11 Cross-training

Natural links:
- Investigator for evidence-backed negotiation;
- Vanguard for security/leadership;
- Field Specialist for crisis coordination;
- Operator where technical authority/access matters.

---

# 13. Ability Specialist

## 13.1 Status

- **Family:** TARGET.
- **Working name:** Ability Specialist.
- **Proposed ID:** `CLASS_ABILITY_SPECIALIST`.
- **Runtime:** not implemented.

## 13.2 Identity

Ability Specialist is the discipline of deep control, safe mastery, technique integration, and advanced use of an exceptional ability.

It does not create an ability.

A character must still discover and progress an ability through the ability authority.

## 13.3 Attribute affinities

Ability-dependent.

Commonly relevant:
- Will;
- Perception;
- Intellect;
- Endurance.

Exact relationships must come from each ability/technique design rather than one universal class formula.

## 13.4 Skill anchors

Strong:
- Powers.

Useful:
- Technical Systems when an ability interfaces with technology;
- other current skills only when the specific ability contract supports the relationship.

## 13.5 Entry evidence

A future entry pattern should prove:
- a discovered ability;
- meaningful ability/technique mastery;
- safe resource management;
- relevant Powers knowledge;
- one field proof involving controlled exceptional behavior.

No one may unlock this class merely from global Level.

## 13.6 Feature families

Target feature families:
- **Control:** safer or more precise use where the ability contract supports it;
- **Resource Discipline:** bounded efficiency/recovery interactions owned by the ability/resource system;
- **Technique Integration:** access to advanced combinations or context-specific technique options;
- **Drawback Management:** earned mitigation where the ability explicitly permits it;
- **Evolution Preparation:** meet/understand advanced evolution requirements without bypassing them.

Ability Specialist must not grant universal damage scaling across unrelated abilities.

## 13.7 Tactical role

Role is ability-dependent.

Potential tags:
- control;
- sensing;
- mobility;
- support;
- offense;
- defense;
- environment interaction.

The class deepens the actual ability instead of forcing all abilities into one tactical archetype.

## 13.8 World/adventure role

Potential uses:
- controlled ability research;
- specialist diagnostics;
- exceptional-environment interaction;
- technique practice;
- safe recovery;
- ability-related knowledge work.

## 13.9 Training dependencies

Likely:
- technique practice;
- mentor/specialist instruction where available;
- safe controlled facility;
- ability-specific recovery;
- field proof.

Current concrete anchor:
- `TRACE_CHAMBER` is already the first specialist facility for Trace Echo practice/training/recovery.

That current location does not imply every ability uses Trace Chamber.

## 13.10 Specialization axes — PROPOSAL

Possible axes:
- control / efficiency / safe sustained use;
- technique depth / interaction / evolution preparation.

Specific ability families may need bespoke branches instead of one shared list.

## 13.11 Cross-training

Ability Specialist can pair with any other family when the ability supports that style.

Strong conceptual links:
- Operator for ability/technology interaction;
- Investigator for perception/knowledge-heavy abilities;
- Vanguard or Skirmisher for combat-form abilities;
- Field Specialist for recovery/support abilities;
- Envoy for social/coordination abilities.

---

# 14. All-23-skill class dependency matrix

Legend:
- **S** = Strong affinity in the current Evolved Skill Registry;
- **U** = Useful affinity in the current Evolved Skill Registry;
- blank = no explicit affinity recorded there.

| Current skill | Vanguard | Skirmisher | Operator | Field Specialist | Investigator | Envoy | Ability Specialist |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Unarmed | S | S |  | U |  | U |  |
| Blades | S | S |  |  |  |  |  |
| Ranged |  | S | U | U |  |  |  |
| Defense | S | U |  | U |  |  |  |
| Tactics | S | S | S |  | U | U |  |
| Athletics | S | S |  | U |  |  |  |
| Stealth |  | S | U |  | S |  |  |
| Traversal |  | S | U | S |  |  |  |
| Survival |  | U |  | S | U |  |  |
| Engineering |  |  | S | U | U |  |  |
| Technical Systems |  |  | S |  | U |  | U* |
| Medicine |  |  |  | S | U | U |  |
| Crafting |  |  | U | U |  |  |  |
| Persuasion |  |  |  |  | U | S |  |
| Deception |  | U |  |  | U | U |  |
| Intimidation | U |  |  |  |  | U |  |
| Empathy |  |  |  | U | U | S |  |
| Leadership | U |  |  |  | U | S |  |
| Investigation |  |  | U |  | S | U |  |
| History |  |  | U |  | U | U |  |
| Factions |  |  |  |  | S | S |  |
| Powers |  |  | U |  | U |  | S |
| Creatures |  | U |  | U | U |  |  |

`U*` for Ability Specialist means Technical Systems is useful specifically where an ability interfaces with technology, matching the skill-registry qualifier.

This matrix is evidence synchronization, not a new formula.

---

# 15. Training / facility / tactical dependency map

This section satisfies the D-045 P3 bonus requirement by making class dependencies explicit.

| Class | Current skill foundation | Target training families | Facility/mentor dependencies | Tactical role dependencies |
| --- | --- | --- | --- | --- |
| Vanguard | combat + Athletics/Tactics | conditioning, defense, sparring, team drill | practice/sparring space; qualified combat mentor where needed | defend/brace, assist/protect, close action resolution, forced movement if implemented |
| Skirmisher | Ranged/Unarmed/Blades + Athletics/Stealth/Traversal/Tactics | movement, precision, route, stealth | field route; range where canon; mobility mentor | move/sprint/disengage, LOS/detection, ranged/close attacks, terrain |
| Operator | Engineering + Technical Systems + Tactics | diagnostics, repair, tool/hazard drills | workbench/lab/infrastructure access; technical mentor | interact, device/item use, hazards, terrain/objectives |
| Field Specialist | Survival + Medicine | treatment, survival, evacuation, logistics | clinic/field course/supply context; medical/field mentor | assist, item use, stabilization, aftermath, extraction |
| Investigator | Investigation + Stealth/Factions + broad knowledge | research, observation, reconstruction, evidence | archive/research/evidence site; specialist mentor | detection/knowledge, target info, objective analysis, player-safe intel |
| Envoy | Persuasion + Empathy + Leadership + Factions | negotiation, coordination, mediation, team drill | mentor/social context; institution only if canon | assist/coordination, retreat/surrender/de-escalation hooks, party/social rules |
| Ability Specialist | Powers + ability-specific competence | technique practice, control, recovery, research | ability-specific safe facility/mentor; Trace Chamber is current Trace Echo anchor | ability action, cooldown/resource, technique legality, drawback/condition rules |

Dependency rule:
- the class layer asks these systems for authoritative results;
- it does not own their calculations.

---

# 16. Tactical integration contract

The V08 tactical system remains the authority for:
- coordinate/occupancy;
- pathing;
- turn/action budget;
- LOS/detection;
- cover;
- targeting;
- damage/injury;
- AI/objectives/retreat.

Classes may add legal options inside that framework.

Examples:
- Vanguard may gain a protection action, but tactical geometry decides whether the protected ally is reachable/adjacent as required;
- Skirmisher may gain reposition options, but pathing and occupancy decide legal destinations;
- Operator may manipulate a hazard, but the encounter/world definition decides whether that hazard exists;
- Field Specialist may stabilize an injury, but the condition system owns the injury and treatment result;
- Investigator may expose known tactical information, but detection/knowledge/privacy rules own what can be known;
- Envoy may attempt de-escalation, but NPC/social/encounter rules own whether the opponent can be influenced;
- Ability Specialist may use advanced techniques, but ability resources/cooldowns/mastery own legality.

No class feature may create an Android-only tactical truth.

---

# 17. Equipment relationship

Class does not grant equipment into inventory.

Target rules:
- equipment remains independently owned;
- skill/class may affect handling legality or available techniques;
- class may create recommended loadout categories, not mandatory identity;
- equipment quality/condition/provenance remain item/economy concerns;
- a player may keep class training after changing equipment;
- a class must remain playable through more than one exact item unless its feature explicitly depends on that tool type.

Examples:
- Vanguard can function unarmed or with supported melee/defensive gear;
- Skirmisher may use ranged or agile close engagement;
- Operator needs actual tools/devices for tool-specific actions;
- Field Specialist needs actual medical/survival supplies for supply-consuming actions;
- Ability Specialist cannot use equipment as a substitute for undiscovered ability state.

---

# 18. Knowledge and privacy relationship

Classes can consume knowledge but cannot bypass knowledge ownership.

Target rules:
- known facts may unlock class options;
- undiscovered facts remain undiscovered;
- Investigator/Operator/Ability Specialist can improve interpretation only through legal checks/evidence;
- Envoy cannot read private relationship maps;
- hidden enemy state remains hidden until detection/knowledge rules expose it;
- mentor hidden requirements may remain partially undisclosed when the design calls for discovery.

Player-safe class UI should show:
- known requirements;
- met/unmet status where intended;
- broad next steps;
- earned features;
- visible specialization direction.

It should not expose:
- hidden canon flags;
- secret NPC goals;
- exact hidden AI thresholds;
- undiscovered ability evolution requirements.

---

# 19. Global Level, rank, profession, and class separation

The Status authority includes a real global Level.

This catalog preserves the namespace separation established by the parent progression design.

Combat class is not:
- global Level;
- ability rank;
- technique mastery;
- profession grade;
- institutional rank;
- faction rank;
- citizen/social status;
- reputation.

A high-Level character may be broadly experienced without having completed a specific class field proof.

A class-trained character may hold no institutional authority.

A professional doctor may or may not be a Field Specialist.

A faction officer may or may not be an Envoy.

Implementation must not infer one namespace from another unless an explicit rule says so.

---

# 20. Cross-training matrix

Cross-training is TARGET behavior.

| Primary class | High-value cross-training | Why it works | Primary tradeoff |
| --- | --- | --- | --- |
| Vanguard | Field Specialist | protection + rescue/sustainment | less time for deep control specialization |
| Vanguard | Envoy | protection + leadership | social training competes with combat depth |
| Vanguard | Skirmisher | durability + mobility | broader skill demands |
| Skirmisher | Investigator | scout + evidence/intel | knowledge investment |
| Skirmisher | Operator | mobility + devices/environment | tool/training burden |
| Operator | Investigator | technical systems + forensics | broad knowledge requirements |
| Operator | Field Specialist | systems + expedition logistics | facility/mentor breadth |
| Operator | Ability Specialist | technology + exceptional systems | ability-specific dependency |
| Field Specialist | Investigator | diagnosis + evidence | reduced pure survival/medical depth |
| Field Specialist | Vanguard | rescue + protection | physical training load |
| Investigator | Envoy | evidence + social leverage | requires real social competence |
| Investigator | Ability Specialist | exceptional phenomena analysis | depends on discovered ability |
| Envoy | Vanguard | leadership + protection | combat time cost |
| Envoy | Field Specialist | crisis coordination | broad support training |
| Ability Specialist | any compatible family | ability deepens an existing play style | high technique/resource/mentor opportunity cost |

The game should not assign “multiclass penalties” solely for having two class records. The cost is earned time, access, practice, and specialization opportunity.

---

# 21. Proposed specialization direction matrix

These are **PROPOSAL axes**, not final specialization names.

| Class | Axis A | Axis B | Optional later axis |
| --- | --- | --- | --- |
| Vanguard | protection/interception | breach/pressure/control | command/formation only if distinct from Envoy |
| Skirmisher | precision/observation | mobility/infiltration | pursuit/route control |
| Operator | infrastructure/bypass | devices/hazards | technical support/logistics |
| Field Specialist | medical stabilization/recovery | survival/logistics | creature/environment specialization |
| Investigator | forensic reconstruction | tactical/field intelligence | social/faction analysis |
| Envoy | coordination/leadership | negotiation/mediation | coercion/pressure |
| Ability Specialist | control/efficiency | technique depth/evolution | ability-family-specific branch |

Later specialization authoring must avoid role collapse:
- Envoy should not absorb Investigator;
- Operator should not absorb all Crafting;
- Field Specialist should not become the only usable Medicine path;
- Ability Specialist should not become mandatory for every power user.

---

# 22. Content requirements per class

Each implemented class eventually needs more than a definition record.

Minimum content package:
- at least one discoverable/understandable entry route;
- training activity set;
- practice feedback;
- field-proof opportunity;
- mentor/facility where required;
- at least one failure/plateau explanation;
- baseline feature set;
- specialization hook;
- cross-training hooks;
- world usage outside combat;
- tactical usage if the class is combat relevant;
- NPC example;
- player-safe UI strings;
- tests;
- save/migration fixture when runtime state is introduced.

A class must not exist only as a Status-screen label.

---

# 23. Visual and UI requirements

Final character presentation remains authored pixel art.

Class visuals should use:
- small class-family iconography;
- optional training/feature icons;
- player-safe progression markers;
- contextual animation/pose requirements when a feature creates a new visible action.

Class should **not** automatically determine:
- uniform;
- faction insignia;
- profession clothing;
- social rank markings.

Those belong to their respective world/equipment/institution systems.

Accessibility:
- do not encode class state only by color;
- provide readable labels;
- explain why a feature is locked using player-safe reasons;
- support text equivalents for icon-only indicators.

No visual asset is generated or promoted by this catalog.

---

# 24. Save/schema migration boundary

CURRENT:
- no durable class state exists;
- schema v1 does not need a class field for the completed Phase 1 progression/activity proofs.

TARGET:
- the evolved game will eventually need persistent class progress if classes are implemented.

Before implementation, a dedicated migration decision must answer:
- whether class definitions are content-only or versioned registry records;
- where per-character class progress lives;
- stable ID policy;
- old-save defaults;
- specialization persistence;
- NPC class persistence;
- rollback/migration behavior;
- Android projection versioning.

Do not add `state.classes` or another top-level progression container merely because this catalog exists.

This preserves D-061's migration boundary.

---

# 25. Testing requirements for future implementation

When class runtime exists, tests must cover:

## Definition validation
- stable/valid ID;
- existing skill references;
- existing feature/effect references;
- no duplicate class IDs;
- valid specialization parent;
- valid player-safe strings.

## Eligibility
- read-only query;
- legal unlock;
- unmet requirement;
- hidden requirement redaction;
- no accidental unlock from global Level alone.

## Progression
- practice evidence;
- field proof;
- specialization eligibility;
- cross-training;
- plateau;
- deterministic replay.

## Integration
- training time/resource cost;
- equipment prerequisite;
- knowledge prerequisite;
- tactical legal action;
- injury/condition restriction;
- ability resource/cooldown;
- NPC parity.

## Persistence
- save/load;
- migration from older save;
- stable class/specialization IDs;
- no duplicate reward/unlock after load.

## Android
- player-safe projection;
- no class arithmetic in Compose;
- no hidden requirements leaked;
- clear locked/unlocked explanation.

---

# 26. Low-end performance direction

Class logic should be event/query driven.

Do not:
- evaluate every class rule every frame;
- scan every class/skill/mentor continuously;
- recompute entire progression graphs during rendering.

Preferred:
- validate on relevant activity/choice/combat boundaries;
- cache immutable definition indexes;
- project only player-relevant class records;
- use stable IDs and bounded lists.

This aligns with the project's low-end Android target.

---

# 27. Reconstruction dependency graph

```text
CURRENT_ATTRIBUTES
  -> support -> CLASS_ELIGIBILITY

CURRENT_23_SKILLS
  -> evidence -> CLASS_FOUNDATION
  -> practice -> CLASS_PROGRESS

ABILITY_AND_TECHNIQUE_STATE
  -> qualifies/deepens -> ABILITY_SPECIALIST
  -> remains_owned_by -> ABILITY_SYSTEM

TRAINING_ACTIVITIES
  -> create_evidence -> CLASS_PRACTICE
  -> consume -> WORLD_TIME + RESOURCES

MENTORS + FACILITIES
  -> gate/accelerate -> CLASS_TRAINING

KNOWLEDGE
  -> gates -> INVESTIGATOR / OPERATOR / ENVOY / ABILITY_SPECIALIST_OPTIONS

EQUIPMENT
  -> enables -> TOOL_OR_WEAPON_SPECIFIC_CLASS_FEATURES

TACTICAL_RULES
  -> own_legality -> CLASS_TACTICAL_FEATURES

FIELD_EVENTS
  -> prove -> CLASS_FIELD_PROOF

CLASS_FOUNDATION + PRACTICE + FIELD_PROOF
  -> unlocks -> SPECIALIZATION_ELIGIBILITY

PROFESSION / FACTION_RANK / INSTITUTION_RANK / GLOBAL_LEVEL
  -x-> are_not -> COMBAT_CLASS

FUTURE_CLASS_STATE
  -> requires -> EXPLICIT_SAVE_SCHEMA_AND_API_MIGRATION
```

---

# 28. Seven-family coverage audit

This catalog is considered reconstruction-grade for the bounded D-045 child because every current working class family now defines:
- identity;
- CURRENT/TARGET/PROPOSAL status;
- attribute relationships;
- current-skill anchors;
- acquisition evidence;
- feature families;
- tactical role;
- world role;
- training dependencies;
- facility dependencies;
- specialization direction;
- cross-training;
- equipment/knowledge boundaries;
- future test expectations.

Coverage:
- Vanguard: complete first catalog pass;
- Skirmisher: complete first catalog pass;
- Operator: complete first catalog pass;
- Field Specialist: complete first catalog pass;
- Investigator: complete first catalog pass;
- Envoy: complete first catalog pass;
- Ability Specialist: complete first catalog pass.

This is design completion for the catalog child, not runtime completion or final balance.

---

# 29. Explicit open questions

Later work must decide:
- exact class unlock thresholds;
- whether class progress is numeric, milestone-based, or hybrid;
- exact specialization names/counts;
- which class features consume action-budget units and at what cost;
- whether some class features are techniques, perks/passives, or class-only unlocks;
- final mentor/facility population;
- class-to-global-Level relationship, if any beyond display/reference;
- class player-safe projection schema;
- save schema/version;
- balance time-to-foundation and time-to-specialization;
- final world-facing terminology/canon.

None of these unknowns block this catalog from serving as the semantic source for the next D-045 children.

---

# 30. Next D-045 sequence

With the Combat Class Catalog materialized, the D-045 reconstruction sequence advances to:

1. **Profession / Rank / Status namespace packet**;
2. **Training / Mentor / Facility standard**;
3. **Gate Twelve evolved-progression proof packet**;
4. **Progression UX contract**;
5. later balance/migration/runtime work after the target contracts are coherent.

The Profession/Rank/Status packet must preserve the namespace separation in section 19 and must not turn profession or faction authority into hidden combat class progression.
