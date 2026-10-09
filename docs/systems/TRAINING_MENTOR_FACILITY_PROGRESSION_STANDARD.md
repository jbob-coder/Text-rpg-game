# THE GAME — Training / Mentor / Facility Progression Standard

Status: **ACTIVE TARGET-GAME DESIGN / D-045 MATERIALIZED CHILD / IMPLEMENTATION DEFERRED**  
Task: **Parallel P12 / D-045**  
Owner: **Veyra / PLAYER_VEYRA**  
Authority boundary: reconstruction-grade progression design. This document does not implement runtime progression, change save schema, create canon institutions, or replace existing activity/training arithmetic.

Read with:

- `docs/systems/PROGRESSION_CLASSES_RANKS_EVOLVED_GAME_DESIGN.md`
- `docs/systems/PROGRESSION_MASTER_PLAN.md`
- `docs/systems/EVOLVED_SKILL_REGISTRY.md`
- `docs/systems/COMBAT_CLASS_CATALOG.md`
- `docs/systems/PROFESSION_RANK_STATUS_NAMESPACE_STANDARD.md`
- `docs/systems/TRAINING_AND_PRACTICE_ACTIVITY_STANDARD.md`
- `docs/systems/ACTIVITY_RECORD_AND_STATE_STANDARD.md`
- `docs/systems/ACTIVITY_TIME_COST_ATOMICITY_STANDARD.md`
- `docs/systems/PHASE_1_PROGRESSION_SCHEMA_API_MIGRATION_PACKET.md`
- `docs/systems/NPC_SCHEDULE_PRESENCE_STANDARD.md`

---

# 1. Purpose

This standard defines how **training opportunities**, **mentors/evaluators**, and **facilities** participate in the evolved progression network without becoming a second progression engine.

It exists to answer five questions future implementation must not guess:

1. What owns the training activity itself?
2. What proves that a mentor can teach or evaluate a subject?
3. What capability does a facility provide independent of its world-facing name or institution?
4. How do skill, class, profession, rank/status, access, schedule, injury, knowledge and world state gate training without collapsing into one universal rank?
5. What may the player safely know about training availability without exposing hidden NPC state, undiscovered facilities or secret progression requirements?

The central rule is:

> **Training is a cross-system qualification and activity network. It is not a universal XP shop and it does not create a second owner for skills, abilities, classes, professions, world access, NPC state or time.**

---

# 2. Authority boundary — CURRENT / TARGET / PROPOSAL

Every statement in this document is interpreted under one of three labels.

## 2.1 CURRENT REALITY

Current repository source/contracts already provide:

- 23 registered skills under `schema.SKILL_CATALOG`;
- skill training through `simulation.train()`;
- slower attribute training through `simulation.train_attribute()`;
- world-time advancement through the current simulation owner;
- stamina/focus and other domain-owned resource costs;
- mentor bonus support in the current training primitive;
- ability/technique practice in the existing powers/progression system;
- diminishing-return behavior in current training;
- `GameState.time_minutes` as current world-time authority;
- activity identity under the existing `ACTIVITY_*` activity standard;
- validation-before-commit and activity rollback expectations;
- player-safe training preview rules in the V10 activity contracts;
- Trace Chamber as the current specialized proof environment for Trace Echo practice/training/recovery;
- schema-v1 persistence for the Phase 1 progression proof, with no new top-level progression owner.

CURRENT does **not** mean the repository already has final mentor catalogs, facility registries, profession training ladders, class training state, certifications or a universal training-opportunity DTO.

## 2.2 TARGET DESIGN

The evolved game should support:

- reusable training paths across skills, classes, professions and abilities;
- persistent mentors/evaluators whose availability depends on real NPC/world state;
- facilities defined by functional capability rather than by UI label alone;
- access gates tied to world discovery, relationships, organizations, credentials, equipment, conditions and schedule where appropriate;
- advanced-training plateaus that require stronger evidence than repeating the easiest activity forever;
- cross-training without erasing previously learned capability;
- player-safe discovery of known training opportunities;
- explicit validation/migration seams before runtime adoption.

TARGET describes intended semantics. It is not evidence that target records already exist in runtime.

## 2.3 PROPOSAL

The stable-ID families and record shapes introduced below are proposal namespaces for future content/runtime design.

They do not become canon because they look final. They require later content, migration and implementation approval before persistence or gameplay use.

---

# 3. Non-duplication and ownership rules

The training ecosystem composes existing owners.

| Concern | Authoritative owner | This standard may do | This standard must not do |
|---|---|---|---|
| Activity identity | V10 Activity Record standard / `ACTIVITY_*` | reference training activities | create a competing training-activity ID family |
| Time and resource cost | simulation + Activity Time/Cost/Atomicity | define gating/ownership links | redefine cost arithmetic |
| Skill value | current skill/progression owner | reference skill IDs | persist duplicate skill values |
| Attribute value | current attribute/progression owner | reference attribute IDs | make generic attribute training automatically available |
| Ability/technique mastery | powers/progression owner | reference practice/evidence | create duplicate mastery XP |
| Class identity/progression | Combat Class Catalog target owner | define training dependencies | turn class into profession or skill |
| Profession/grade | P7 profession namespace | define qualification/training links | infer profession from one training activity |
| Institution/faction rank | owning organization/rank system | use rank/access as prerequisite evidence | equate rank with skill or reputation |
| NPC identity/state | NPC/social systems | reference authorized mentor/evaluator NPCs | copy private goals/knowledge into progression |
| NPC schedule/presence | NPC Schedule/Presence owner | require real availability | invent UI-only availability |
| World location/access | world/location owner | reference facility-bearing locations | create hidden map truth in progression |
| Equipment/tools | item/equipment owner | require equipment/tool capability | grant/equip items through training metadata |
| Conditions/injury | condition/aftermath owner | gate or modify legality | heal or remove injury implicitly |
| UI projection | player-safe bridge/Android | project known options | own gameplay truth |

A future implementation that cannot name the real owner for a prerequisite is incomplete.

---

# 4. Stable-ID policy

The P7 stable-ID rules remain in force: IDs identify semantics, are not reused, do not encode balance numbers, and do not become canon merely because they are stable-looking.

## 4.1 Existing ID family retained

Training actions/activities continue to use:

- `ACTIVITY_<IDENTITY>`

This standard does **not** create `TRAINING_ACTIVITY_*` as a competing activity identity.

## 4.2 Proposed new target ID families

The following are **PROPOSAL namespaces**:

| Record | Proposed ID family | Meaning |
|---|---|---|
| training path | `TRAINING_PATH_<IDENTITY>` | reusable cross-system route connecting subject, activity/evidence and gates |
| mentor capability | `MENTOR_CAP_<IDENTITY>` | semantic teaching/coaching capability independent of a specific NPC identity |
| evaluator capability | `EVAL_CAP_<IDENTITY>` | semantic assessment/certification capability independent of a specific evaluator NPC |
| facility capability | `FACILITY_CAP_<IDENTITY>` | functional environmental/tooling capability independent of a specific location name |
| reusable training requirement bundle | `TRAINING_REQ_<IDENTITY>` | named prerequisite bundle only when reuse justifies stable identity |

Rules:

1. A mentor NPC ID is not a `MENTOR_CAP_*` ID.
2. A facility location ID is not a `FACILITY_CAP_*` ID.
3. A class ID is not a training path ID.
4. A profession grade is not an evaluator capability.
5. A relationship threshold is not a mentor capability.
6. Availability results are normally derived query output, not persisted stable records.
7. Hidden requirements may have stable internal identity without being projected to the player.
8. Do not create `TRAINING_REQ_*` records for trivial one-use conditions that are clearer inline.

---

# 5. Core target records

## 5.1 Training path record

A future `TRAINING_PATH_*` definition should describe a reusable route, not perform mutation itself.

Recommended fields:

- `training_path_id`;
- `status`: TARGET / PROPOSAL / implemented later;
- `subject_refs`: skill, attribute, ability, technique, class feature, profession qualification or other accepted progression owner;
- `activity_refs`: one or more `ACTIVITY_*` activities or activity categories;
- `evidence_kinds`: practice, assessment, field proof, study, supervised work, research, other accepted evidence;
- `mentor_capability_refs`;
- `evaluator_capability_refs`;
- `facility_capability_refs`;
- `equipment_tool_requirements`;
- `world_access_requirements`;
- `knowledge_requirements`;
- `relationship_or_membership_requirements` where the owning system supports them;
- `condition_restrictions`;
- `schedule_requirements`;
- `plateau_gate_refs` or owner-defined plateau rule references;
- `cross_training_links`;
- `player_safe_visibility_policy`;
- `future_write_owner`;
- `validation_requirements`.

The training path is orchestration metadata. It does not calculate skill gain, ability mastery, time cost, rank promotion or item effects.

## 5.2 Mentor capability record

A `MENTOR_CAP_*` definition describes **what can be taught or supervised**, not who the mentor is.

Recommended fields:

- `mentor_capability_id`;
- subject families or accepted subject refs;
- permitted activity/training modes;
- teaching stage/ceiling semantics if the owning progression design accepts them;
- whether supervised hazardous practice is supported;
- whether the capability provides instruction, feedback, demonstration or supervised practice;
- required facility capability refs, if any;
- required evaluator capability refs, if separate evaluation is needed;
- condition/safety constraints;
- projection policy;
- validation requirements.

A specific NPC becomes a usable mentor only when:

1. an authorized durable NPC identity exists;
2. that NPC is assigned/references one or more accepted mentor capabilities;
3. current schedule/presence allows participation;
4. the NPC is available under current social/world state;
5. the training path and activity are otherwise legal.

A mentor capability does not reveal the NPC's private goals, memories, hidden knowledge, relationship values or future story state.

## 5.3 Evaluator capability record

An `EVAL_CAP_*` record owns the semantic ability to assess evidence.

It may support:

- skill competency checks;
- profession qualification/grade assessment;
- class progression proof;
- technique/control assessment;
- safety clearance;
- field-proof validation where the domain requires a recognized evaluator.

It does not automatically grant a profession grade, rank, class feature or civic status. The owning domain applies the result.

## 5.4 Facility capability record

A `FACILITY_CAP_*` definition describes **what a location/environment makes possible**, not the location's lore identity.

Recommended fields:

- `facility_capability_id`;
- supported training/activity modes;
- supported subject families;
- safety/containment properties;
- equipment/tool/environment dependencies;
- intensity/difficulty support semantics;
- supervision requirements;
- accessibility constraints;
- player-safe projection policy;
- validation requirements.

A world location may expose zero, one or multiple facility capabilities.

A facility capability must not imply:

- ownership by a faction/institution;
- player membership;
- legal access;
- a discovered map location;
- a specific named building;
- a profession or rank.

Those belong to their respective world/social/organization owners.

---

# 6. Training legality pipeline

Future training availability should be a read-only query before any mutation.

Recommended order:

1. resolve training path and referenced activity;
2. resolve subject owner and stable subject ID;
3. validate current player/runtime state;
4. validate world/location access;
5. validate activity location requirements;
6. validate required facility capabilities;
7. validate mentor/evaluator identity and capability references;
8. validate mentor/evaluator schedule/presence;
9. validate social/membership/rank/access requirements through their owners;
10. validate knowledge/discovery requirements;
11. validate equipment/tool requirements;
12. validate injury/condition restrictions;
13. validate current plateau/entry evidence through the owning progression system;
14. validate time/resource preflight through the activity/simulation owner;
15. return a player-safe availability result;
16. only on explicit player action execute the authoritative activity transaction.

Querying availability does not mutate state.

---

# 7. Evidence classes

Training and progression must distinguish evidence sources.

Target evidence classes include:

- **PRACTICE** — deliberate repeated training/practice;
- **FIELD_USE** — real-world use under accepted conditions;
- **ASSESSMENT** — evaluator-owned test/check;
- **SUPERVISED_WORK** — domain work performed under accepted supervision;
- **STUDY_RESEARCH** — knowledge/study evidence where appropriate;
- **QUEST_WORLD_PROOF** — authored world/quest evidence where the owning system explicitly accepts it;
- **CLASS_FIELD_PROOF** — class-specific proof from the Combat Class Catalog;
- **PROFESSION_QUALIFICATION** — profession-owned qualification evidence.

Forbidden inference examples:

- one successful check ≠ mastery;
- one quest choice ≠ profession;
- NPC trust ≠ public certification;
- faction membership ≠ training completion;
- owning equipment ≠ competence;
- facility access ≠ qualification;
- class eligibility ≠ class acquisition;
- world Level ≠ profession grade;
- repeated UI clicks ≠ valid practice unless the activity owner records legal completion.

---

# 8. Plateau and advanced-training gates

CURRENT training already has diminishing-return behavior. TARGET design adds explicit world/progression gates for advanced competence.

A plateau may require combinations of:

- higher difficulty;
- stronger feedback;
- mentor capability;
- evaluator proof;
- facility capability;
- field use;
- specialized knowledge;
- advanced equipment/tools;
- class/profession evidence;
- injury recovery;
- world access;
- time/opportunity cost.

This document intentionally does **not** assign universal numeric plateau thresholds.

Numeric thresholds remain future balance/implementation work owned by the relevant progression system.

A plateau query must explain only player-known requirements. Hidden gates remain hidden or are presented as an honest unknown requirement according to the eventual UX contract.

---

# 9. Mentor and evaluator world integration

## 9.1 Persistent identity

Mentors/evaluators should be persistent NPCs when they are represented as world characters.

A training record references an NPC only through an authorized durable identity. Do not use encounter-local actors or presentation IDs as durable mentor IDs.

## 9.2 Presence and schedule

Mentor/evaluator availability must consume the NPC Schedule/Presence owner.

Examples of valid reasons for unavailability may include:

- not present at the location;
- unavailable in the current schedule window;
- occupied by authored world state;
- access relationship not satisfied;
- training activity unavailable at this time.

The training system must not create a second NPC schedule.

## 9.3 Social boundary

Relationships may gate access, pricing, willingness or special instruction where an accepted social rule says so.

The training projection must not expose:

- raw relationship axes;
- private NPC memories;
- hidden goals;
- secret knowledge;
- hidden faction state;
- unrevealed future availability.

The player sees only the approved consequence: available, unavailable, known requirement, or an intentionally undisclosed requirement.

## 9.4 Mentor versus evaluator

Teaching and evaluation are separate capabilities.

One NPC may possess both, but the data model must not assume:

- every mentor may certify;
- every evaluator may teach;
- friendship grants evaluator authority;
- organization rank alone proves teaching capability.

---

# 10. Facility world integration

## 10.1 Capability before naming

Design facilities by capability first.

Generic capability families may include:

- conditioning / movement practice;
- close-combat practice;
- controlled ranged practice where world canon permits;
- tactical/team drill;
- stealth/observation environment;
- traversal/field route;
- survival/field course;
- technical diagnostics/workbench;
- fabrication/crafting workspace;
- clinic/treatment practice;
- archive/research/evidence environment;
- social rehearsal/mediation context;
- ability-control/specialist environment.

These are functional design categories, not canon building names.

## 10.2 Current proof anchor

Trace Chamber is CURRENT evidence of a specialized environment for Trace Echo training/practice/recovery.

This does not establish a universal template for every ability or a canon network of similar facilities.

## 10.3 Access

Facility capability and facility access are separate.

A location may have the needed capability while the player still lacks:

- discovery;
- legal access;
- membership;
- permission;
- equipment;
- schedule window;
- safe condition;
- required mentor/supervisor.

The world/access owner decides whether the player may actually use the location.

---

# 11. Full 23-skill training dependency map

The table below is TARGET dependency direction over the **CURRENT** 23 runtime skill IDs. It does not add new skills or final balance values.

| Current skill ID | Category | Reusable training direction | Mentor/evaluator direction | Facility capability direction |
|---|---|---|---|---|
| `unarmed` | combat | controlled technique, defense exchange, conditioning, field use | combat instruction / observed competency | close-combat practice; conditioning |
| `blades` | combat | safe handling, forms, controlled exchange, field use | weapon-safety/technique instruction | controlled close-combat practice; safe equipment space |
| `ranged` | combat | handling, precision, target discrimination, field use | ranged instruction/evaluation where canon permits | controlled ranged-practice capability |
| `defense` | combat | guard, movement, protection drill, sparring | defensive feedback/evaluation | close-combat/team drill |
| `tactics` | combat | scenario analysis, team drill, field proof | tactical instruction/debrief | tactical/team simulation or field exercise |
| `athletics` | physical | conditioning, load, sprint/endurance, field activity | conditioning coaching/evaluation | conditioning/movement facility |
| `stealth` | physical | observation avoidance, route discipline, field practice | stealth/observation coaching | stealth/observation environment |
| `traversal` | physical | obstacle, route, climbing/movement, field practice | traversal coaching/safety supervision | traversal route / obstacle environment |
| `survival` | physical | fieldcraft, navigation, resource/shelter practice | field mentor/evaluator | survival/field course |
| `engineering` | technical | diagnostics, repair, systems work, supervised problem-solving | technical mentor/evaluator | diagnostics/workbench/infrastructure capability |
| `technical_systems` | technical | systems operation, diagnostics, controlled lab/work | technical systems mentor | terminal/lab/diagnostics capability |
| `medicine` | technical | treatment procedure, diagnosis, supervised care | medical mentor/evaluator | clinic/treatment-practice capability |
| `crafting` | technical | fabrication, repair, material/tool practice | craft/technical mentor | fabrication/workshop capability |
| `persuasion` | social | negotiation practice, role-play, real social evidence | social coach/evaluator where appropriate | social rehearsal/mediation context |
| `deception` | social | scenario practice, observation, field/social evidence | specialist feedback where ethically/world-appropriate | rehearsal/observation context; no universal institution implied |
| `intimidation` | social | presence/control scenarios, consequence-aware field evidence | social/tactical evaluator where appropriate | controlled scenario/team context |
| `empathy` | social | observation, interviewing, care/social practice | social/medical mentor depending context | interview/care/social context |
| `leadership` | social | coordination, team drill, crisis/field leadership | leadership evaluator/mentor | team drill / supervised group activity |
| `investigation` | knowledge | evidence analysis, reconstruction, observation, field cases | investigator/research mentor | archive/evidence/research environment |
| `history` | knowledge | study, source comparison, archival research | researcher/historian where canon supports | archive/research environment |
| `factions` | knowledge | study, observation, interviews, world evidence | knowledgeable source/mentor with privacy rules | archive/research/social information context |
| `powers` | knowledge | theory, controlled ability practice, research, field evidence | ability specialist/research mentor | ability-control/specialist environment; Trace Chamber is current anchor |
| `creatures` | knowledge | study, field observation, evidence analysis | researcher/field mentor | archive/research/field environment |

Coverage invariant: **23 / 23 current runtime skill IDs are represented exactly once in this matrix.**

The matrix is not a facility catalog. It gives reusable capability direction so future content does not invent incompatible one-off training semantics.

---

# 12. Seven class-family training map

All seven target class families retain their existing Combat Class Catalog identity and skill dependencies.

| Class family | Primary training direction | Mentor/evaluator direction | Facility capability direction | Gate emphasis |
|---|---|---|---|---|
| Vanguard | conditioning, defense, close-action/team drill | combat/team mentor, field evaluator | conditioning + close-combat/team drill | sustained practice + field proof |
| Skirmisher | mobility, precision, stealth, route discipline | mobility/ranged/stealth mentor as appropriate | traversal/field route + controlled precision environment | movement/field evidence |
| Operator | diagnostics, repair, device/tool/hazard drill | technical mentor/evaluator | workbench/lab/infrastructure capability | technical proof + tool/environment access |
| Field Specialist | treatment, survival, evacuation, logistics | medical/field mentor/evaluator | clinic + field-course capability | treatment/field proof |
| Investigator | research, observation, reconstruction, evidence | research/investigation mentor/evaluator | archive/evidence/research environment | knowledge/evidence quality |
| Envoy | negotiation, mediation, coordination, leadership | social/leadership mentor/evaluator | social rehearsal/team context | social evidence + relationship/world context |
| Ability Specialist | technique control, theory, recovery, specialist practice | ability-specific mentor/evaluator | safe ability-control/specialist environment | ability ownership + control evidence + safe access |

Coverage invariant: **7 / 7 target class families are represented exactly once.**

Class training remains distinct from profession qualification. A profession may share activities, mentors or facilities with a class without becoming the class.

---

# 13. Profession, grade, rank and status integration

The P7 namespace standard remains authoritative.

## 13.1 Profession

Profession definitions may reference:

- training paths;
- mentor/evaluator capabilities;
- facility capabilities;
- work/supervised-work evidence;
- class relationships;
- skill evidence.

Training does not automatically grant profession identity.

## 13.2 Profession grade

A profession grade may require:

- prior profession identity;
- defined evidence;
- evaluator capability;
- accepted assessment;
- work history;
- training completion.

The profession owner applies the grade change.

## 13.3 Institution/faction rank

Rank may gate access to training or facilities.

Rank is not training completion, and training completion does not automatically grant rank.

## 13.4 Civic/legal status

Legal/licensing status may gate hazardous/sensitive training where world canon later requires it.

Do not invent licensing systems merely to justify a training gate.

## 13.5 Reputation and relationship

Reputation/relationship may affect willingness/access only through their owning systems.

Neither is a universal qualification ladder.

---

# 14. Cross-training

Cross-training is TARGET behavior.

Rules:

1. learned skills are not erased when class/job/profession changes;
2. cross-training consumes real time and opportunity;
3. access may require additional mentors/facilities;
4. advanced cross-training may hit plateaus;
5. class training cannot silently award unrelated profession status;
6. profession training cannot silently grant tactical class features;
7. facility sharing is allowed when capability requirements genuinely overlap;
8. one training activity may produce multiple domain effects only when each effect owner authorizes the transaction.

Cross-training opportunity cost is primarily world time, access, resources and competing opportunities—not arbitrary forgetting.

---

# 15. Player-safe training projection

A future player-safe training query may expose:

- stable public activity/training-path ID where allowed;
- display name;
- known subject;
- known duration;
- known resource/item costs;
- current availability;
- player-safe unavailable reason;
- known location;
- known mentor/evaluator display identity;
- known facility capability/display description;
- known prerequisite/evidence;
- known risk/condition warning;
- known schedule window;
- known expected progression category.

It must not expose:

- private NPC memory/goals;
- raw relationship values;
- hidden faction clearance;
- undiscovered locations;
- secret mentor identities;
- hidden training thresholds;
- unrevealed class/profession requirements;
- private evaluator logic;
- future story state;
- exact hidden gain formulas when the progression UX does not authorize them.

Android/UI remains presentation and interaction, not progression authority.

---

# 16. Current persistence and future migration

## 16.1 Current boundary

D-061 remains authoritative:

- Phase 1 uses save schema v1;
- no new top-level progression field is needed for the bounded current proof;
- current skills/abilities/perks/player state/time/history already have owners.

This P12 document does not change that decision.

## 16.2 Derived opportunity state

Training availability should normally be derived from:

- definitions;
- current player state;
- world/location state;
- NPC presence;
- access;
- knowledge;
- conditions;
- schedule.

Do not persist a duplicate list of "available training" merely for UI convenience.

## 16.3 Future durable state

If future implementation needs durable records such as:

- certification/assessment history;
- mentor relationship to a training path;
- resumable scheduled training;
- explicit plateau/evidence ledger;
- profession qualification state not representable by accepted existing owners;

then migration design must specify:

1. durable owner;
2. stable schema;
3. old/new save behavior;
4. validation;
5. migration fixture;
6. round-trip test;
7. rollback/recovery behavior;
8. player-safe projection.

No such new durable representation is selected by P12.

---

# 17. Validation requirements

Future validators should prove at least:

1. every stable training-path/capability ID is unique within its registry;
2. every skill reference resolves to the current skill catalog;
3. every class reference resolves when class relationships are declared;
4. every profession/rank/status reference resolves to its owner;
5. every `ACTIVITY_*` reference resolves;
6. every mentor NPC reference resolves to an authorized durable NPC when concrete content binds one;
7. every facility location reference resolves when concrete content binds one;
8. mentor capability refs resolve;
9. evaluator capability refs resolve;
10. facility capability refs resolve;
11. capability records do not masquerade as NPC/location identities;
12. no hidden/private NPC fields are projected;
13. unknown/undiscovered facility truth is not exposed;
14. no activity result duplicates skill/ability/profession/class mutation outside the authoritative owner;
15. schedule/presence checks are read from the NPC/world owner;
16. condition restrictions are validated before time/cost commit;
17. stable-ID renames use explicit migration when implemented;
18. no proposal record is reported as CURRENT runtime without implementation evidence;
19. the 23 current skills remain completely mapped;
20. the seven class families remain completely mapped.

---

# 18. Test strategy

P12 is documentation-only. The following are future implementation gates, not tests executed by this task.

## 18.1 Definition/registry tests

- unique IDs;
- unknown skill/class/profession/activity/capability refs rejected;
- circular/invalid training-path links rejected;
- capability/location/NPC semantic separation enforced.

## 18.2 Availability tests

- wrong location/access rejected without mutation;
- missing facility capability rejected;
- missing mentor capability rejected;
- mentor absent by schedule rejected;
- known versus hidden prerequisite projection correct;
- injury/condition restriction enforced before time passes;
- undiscovered facility not leaked.

## 18.3 Transaction tests

Reuse the V10 activity atomicity owner:

- insufficient resource no mutation;
- invalid prerequisite no mutation;
- time + progression output commit together;
- multi-domain output rollback is atomic;
- condition expiry is preserved correctly;
- deterministic outcome where the underlying training rule is deterministic.

## 18.4 Save/migration tests

Required only when new durable training/qualification state exists:

- schema migration fixture;
- save/load round trip;
- stable-ID migration;
- replay/duplicate evidence protection where relevant;
- resumable activity only after the activity-state schema exists.

## 18.5 Projection tests

- known training option mapped;
- unavailable reason player-safe;
- private mentor state absent;
- hidden requirement absent/redacted;
- unknown facility absent;
- UI action delegates to authoritative engine/activity owner.

---

# 19. Reconstruction checklist

A future agent designing a concrete training route should answer:

- What is the authoritative subject?
- Which `ACTIVITY_*` record executes it?
- Which system owns the gain/effect?
- What evidence class does completion produce?
- Is a mentor required? If yes, what capability—not merely what NPC name?
- Is an evaluator required?
- What facility capability is required?
- Which world location provides that capability?
- Is the location discovered and accessible?
- Is NPC presence/schedule legal now?
- Are relationship/membership/rank requirements owned elsewhere?
- Are conditions/injury legal?
- What is player-known versus hidden?
- What is the atomic transaction owner?
- What persistence is actually needed?
- What future tests prove the route?
- What canon approval is still missing?

If any answer is "the UI decides," the route is architecturally invalid.

---

# 20. Forbidden inference matrix

| Observed fact | Forbidden automatic inference |
|---|---|
| player has high skill | advanced mentor/facility is unnecessary |
| player knows a mentor | mentor is available now |
| NPC likes player | NPC can teach/certify the subject |
| NPC has a profession | NPC automatically has mentor/evaluator capability |
| facility exists | player knows/discovered it |
| player enters facility | player is authorized to train there |
| class uses a skill | class grants the skill |
| profession uses a skill | profession equals class |
| player completes training | profession grade/rank automatically increases |
| player has faction rank | training is complete |
| player has high reputation | evaluator certification exists |
| one successful field event | plateau requirement is satisfied |
| activity button is visible | hidden progression requirement may be exposed |
| UI knows duration/cost | UI owns time/resource mutation |
| current mentor bonus primitive exists | every mentor should have a numeric bonus |
| Trace Chamber exists | every ability has an equivalent canon facility |

---

# 21. P12 completion invariants

This child is complete when repository evidence proves:

- CURRENT / TARGET / PROPOSAL are explicit;
- activity/time/resource arithmetic remains owned by V10/current runtime;
- stable target ID families are defined without colliding with current IDs;
- mentor/evaluator capability is separate from NPC identity;
- facility capability is separate from world location/institution identity;
- access/visibility/qualification/plateau/cross-training gates are defined;
- all **23 / 23** current skills are represented;
- all **7 / 7** class families are represented;
- P7 profession/rank/status namespaces are integrated without collapse;
- schema-v1/current runtime boundaries are preserved;
- player-safe training projection rules are explicit;
- future migration/test seams are explicit;
- no runtime/canon/balance implementation is falsely claimed.

---

# 22. Direct next D-045 child

P16 has now materialized the **Gate Twelve Progression Proof Packet** using:

- the current D-066 Phase 1 progression evidence;
- the 23-skill registry;
- the seven-class catalog;
- the profession/rank/status namespace;
- this training/mentor/facility standard;
- current Trace Chamber activity evidence;
- accepted world/content authority.

That bounded proof preserves CURRENT/TARGET/PROPOSAL separation and does not invent final professions, ranks, mentors, facilities or UI state.

The direct next D-045 child is now the **Progression UX Contract**.

---

# 23. Implementation statement

P12 implements **no runtime gameplay**.

It adds no:

- training formula;
- balance value;
- class/profession/rank runtime state;
- mentor NPC;
- canon institution/faction;
- facility location;
- save field/schema migration;
- Android DTO;
- D-072/D-073 tactical behavior.

It establishes the ownership and reconstruction contract future implementation must satisfy.
