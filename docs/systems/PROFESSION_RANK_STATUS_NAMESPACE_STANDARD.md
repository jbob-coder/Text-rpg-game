# THE GAME — Profession / Rank / Status Namespace Standard

Status: **ACTIVE TARGET-GAME DESIGN / D-045 MATERIALIZED CHILD / IMPLEMENTATION DEFERRED**  
Parent authorities:
- `docs/systems/PROGRESSION_CLASSES_RANKS_EVOLVED_GAME_DESIGN.md`
- `docs/systems/PROGRESSION_MASTER_PLAN.md`
- `docs/systems/COMBAT_CLASS_CATALOG.md`
- `docs/systems/EVOLVED_SKILL_REGISTRY.md`
- `docs/systems/FACTION_HIERARCHY_MEMBERSHIP_STANDARD.md`
- `docs/systems/STATUS_UI_ABILITIES_AND_PASSIVES_MASTER_PLAN.md`
- `docs/systems/PHASE_1_PROGRESSION_SCHEMA_API_MIGRATION_PACKET.md`

Task authority: **D-045 / Parallel P7**.

Purpose: define reconstruction-grade namespace, ownership, stable-ID, migration, projection and cross-system rules for **profession**, **profession grade**, **institutional rank**, **faction rank**, **civic/social status**, and **reputation** without collapsing them into global Level, class progression, ability rank, technique mastery, a current job assignment, or personal relationship state.

This document is a design contract. It does **not** claim that profession/rank/status runtime state already exists.

---

# 0. Interpretation rule — CURRENT / TARGET / PROPOSAL

Every statement in this packet belongs to one of three states.

- **CURRENT** — directly supported by current source/content or an already-approved repository contract.
- **TARGET** — approved evolved-game design direction to preserve during future implementation.
- **PROPOSAL** — naming, prefix, catalog, balance or representation guidance that still requires implementation/content approval before becoming runtime or canon.

No PROPOSAL in this packet becomes canon merely because it has a stable-looking ID.

---

# 1. CURRENT reality

## 1.1 Current authoritative player state

**CURRENT:** `src/textrpg/core.py::GameState` currently owns:
- `player`;
- `flags`;
- `relationships`;
- `knowledge`;
- `inventory`;
- `quests`;
- `npcs`;
- `party`;
- `abilities`;
- `equipment`;
- `perks`;
- `time_minutes`;
- `history`;
- schema version 1.

There is currently no top-level `profession`, `class`, `institutional_rank`, `faction_rank`, or `civic_status` field.

Therefore this packet must not describe any of those target concepts as already implemented.

## 1.2 Current progression foundation

**CURRENT:** the runtime has seven attributes and exactly 23 registered skills.

Combat:
- `unarmed`
- `blades`
- `ranged`
- `defense`
- `tactics`

Physical:
- `athletics`
- `stealth`
- `traversal`
- `survival`

Technical:
- `engineering`
- `technical_systems`
- `medicine`
- `crafting`

Social:
- `persuasion`
- `deception`
- `intimidation`
- `empathy`
- `leadership`

Knowledge:
- `investigation`
- `history`
- `factions`
- `powers`
- `creatures`

**CURRENT:** D-061 keeps the bounded Phase 1 progression proof inside existing schema-v1 state and explicitly does not create a new top-level progression owner.

## 1.3 Current ability namespace

**CURRENT:** abilities and techniques already use stable authored identities such as `ABILITY_TRACE_ECHO` and `TECHNIQUE_SIGNAL_PULSE`.

Ability rank and technique mastery are therefore real current progression concepts.

They are not profession grade, organization rank, civic status, or reputation.

## 1.4 Current social/faction boundary

**CURRENT CONTRACT:** `FACTION_HIERARCHY_MEMBERSHIP_STANDARD.md` separates:
- political entity;
- institution;
- faction;
- profession;
- job/occupation;
- internal rank;
- legal/citizenship status;
- social class;
- reputation;
- individual relationship.

It also requires organization-specific rank, distinct role vs rank, and player-safe privacy for secret membership/clearance.

## 1.5 Global Level

**TARGET / OWNER-LOCKED CANON DESIGN:** the Status authority defines a real in-universe global **Level**, obtained through the Status system and related to kill progression.

**CURRENT RUNTIME LIMIT:** this target Level system is still documented as implementation-deferred. This packet does not invent a current `GameState.level` field or a save representation for it.

Level remains semantically separate from every namespace defined below.

---

# 2. Non-negotiable namespace separation

The evolved game must be able to answer these questions independently.

| Concept | Question answered | Must NOT mean |
| --- | --- | --- |
| Global Level | How far has the Status-level progression axis advanced? | job qualification, faction authority, class mastery |
| Ability rank | How far has one primary ability family advanced? | Level, profession grade |
| Technique mastery | How practiced is one technique? | ability rank, class progression |
| Combat class | What combat/adventure discipline has been developed? | occupation, institution |
| Class progression | How far has that discipline developed? | profession grade, organization rank |
| Profession | What sustained civilian/economic/technical occupation is the character qualified for or practicing? | combat class, current shift, faction |
| Profession grade | What qualification/responsibility grade exists inside that profession? | global Level, faction rank |
| Institution rank | What formal authority does the character hold inside one institution? | personal trust, universal law |
| Faction rank | What formal position/standing does the character hold inside one faction? | reputation, profession |
| Civic/legal status | What status does a society/law recognize? | faction rank, social relationship |
| Reputation | How is the character regarded by a person/group/settlement/institution? | membership/rank |
| Job/assignment | What work is the character currently doing? | profession identity |
| Organization role | What function does the member perform? | rank |
| Relationship | How does one NPC relate to the player across authored relationship axes? | faction reputation |

No implementation may infer one of these merely because another is high.

Examples:
- Level 40 does not create a profession grade.
- a Master-level skill does not automatically award an institution rank.
- a Vanguard class does not make the player a security officer.
- a medical profession does not automatically grant Field Specialist class progression.
- high faction reputation does not make the player a faction officer.
- a faction officer does not automatically trust Jack personally.
- an active job shift does not make the job itself a permanent profession identity.

---

# 3. Stable-ID policy

## 3.1 General rules

All future durable or cross-document records must follow these rules.

1. IDs identify semantics, not display text.
2. display names may change without changing stable IDs.
3. IDs are not reused for a different meaning.
4. a rename of an implemented stable ID requires an explicit migration/alias record.
5. IDs do not encode numeric balance values.
6. IDs do not encode temporary UI order.
7. IDs do not encode player-local progression numbers.
8. scoped child records must resolve to their parent definition.
9. current stable runtime IDs are never renamed just to match a new target prefix.
10. PROPOSAL prefixes below guide new target records; they do not retroactively rewrite current content.

## 3.2 Proposed target ID families

The following are **PROPOSAL namespace prefixes**, not proof that records already exist.

| Record kind | Proposed pattern | Scope rule |
| --- | --- | --- |
| profession definition | `PROF_<IDENTITY>` | one semantic profession family/occupation definition |
| profession grade | `PROF_GRADE_<IDENTITY>` | must reference exactly one profession definition |
| job/work opportunity | `JOB_<IDENTITY>` | concrete work/assignment content; not profession identity |
| organization role | `ORG_ROLE_<IDENTITY>` | function inside one organization context |
| institution rank | `INST_RANK_<IDENTITY>` | valid only inside its owning institution/rank ladder |
| faction rank | `FACTION_RANK_<IDENTITY>` | valid only inside its owning faction/rank ladder |
| civic/legal status | `CIVIC_STATUS_<IDENTITY>` | world-law/society-recognized status |
| social-status category | `SOCIAL_STATUS_<IDENTITY>` | create only if world design needs a formal durable category |
| class definition | existing proposal family `CLASS_<IDENTITY>` | retained from Combat Class Catalog |
| ability | current `ABILITY_<IDENTITY>` family | existing runtime/content authority |
| technique | current `TECHNIQUE_<IDENTITY>` family | existing runtime/content authority |

If the future world organization registry standardizes all institution/faction identities under a shared `ORG_*` identity, that does not erase the semantic distinction between **institutional rank** and **faction rank**.

## 3.3 IDs that should usually NOT be persisted

Reputation display bands such as “trusted”, “hostile”, or “respected” should normally be **derived presentation labels** over the authoritative reputation/relationship owner unless a future rule proves that a band itself has independent gameplay identity.

Do not persist `REPUTATION_RANK_7` merely because a UI wants a badge.

Likewise:
- skill mastery descriptors are display/interpretation unless the owning skill system explicitly persists them;
- UI section names are not stable game IDs;
- generic “status” text is not automatically a `SOCIAL_STATUS_*` record.

---

# 4. Profession

## 4.1 Definition

**TARGET:** a profession is a sustained civilian/economic/technical occupation or qualification path.

Profession can influence:
- work eligibility;
- income/economy;
- schedule;
- legal/work access;
- professional equipment familiarity;
- practical skill use;
- mentor/facility access;
- institutional network;
- professional reputation;
- training opportunity;
- quests/events;
- housing/services where world rules support them.

Profession is not a combat class.

## 4.2 Profession record requirements

A future profession definition should provide at minimum:
- stable profession ID;
- display name;
- status: TARGET / PROPOSAL / CANON when applicable;
- profession family;
- description;
- core work functions;
- current-skill anchors;
- optional attribute relationships;
- qualification evidence;
- training/education routes;
- mentor/evaluator requirements;
- facility requirements;
- tool/equipment requirements;
- work activity families;
- legal/license requirements if any;
- organization/institution dependencies if any;
- progression/grade model reference;
- class relationships;
- tactical-role relationships where relevant;
- access/services unlocked;
- privacy/public-visibility policy;
- content provenance;
- migration/implementation owner;
- validation/test requirements.

A profession record does not own the formulas of another system.

## 4.3 Profession vs job

Profession answers:
> What occupational capability/qualification does this character have?

Job/assignment answers:
> What work are they currently doing, for whom, where, and under what schedule?

A qualified technician may be unemployed.
A character may perform a temporary paid task without gaining a full profession.
A professional may change employers without losing all professional competence.
A job shift should be authored as world/activity content rather than silently becoming a permanent profession grade.

---

# 5. Profession-family binding to the current 23-skill foundation

The following families are **TARGET functional families**, not canon institutions or final profession names.

They provide a reconstruction map from all 23 current skills into plausible occupational use without creating a second skill catalog.

| Target profession family | Current skill anchors | Natural class relationships | Training/facility direction |
| --- | --- | --- | --- |
| Technical / infrastructure | Engineering, Technical Systems, Crafting, Investigation | Operator, Investigator | workbench, infrastructure access, diagnostics, repair mentor |
| Medical | Medicine, Empathy, Survival, Investigation | Field Specialist, Investigator | clinic, treatment practice, field care, medical mentor |
| Logistics | Crafting, Survival, Leadership, Technical Systems, Athletics | Field Specialist, Operator, Envoy | supply context, planning, handling, route/field exercises |
| Municipal / civic | Engineering, Technical Systems, Factions, Leadership, Empathy, History | Operator, Envoy, Investigator | civic systems, records, supervised public-service work |
| Security / military — only where canon supports it | Unarmed, Blades, Ranged, Defense, Tactics, Athletics, Intimidation, Leadership | Vanguard, Skirmisher, Envoy | practice yard, controlled range where canon, tactical/team drill |
| Research | Investigation, History, Factions, Powers, Creatures, Engineering, Technical Systems | Investigator, Ability Specialist, Operator | archive, lab/research station, field evidence, specialist mentor |
| Trade / service | Persuasion, Deception, Empathy, Factions, Crafting | Envoy, Investigator | market/service context, negotiation, appraisal/service practice |
| Field work | Athletics, Stealth, Traversal, Survival, Creatures, Investigation | Skirmisher, Field Specialist, Investigator | wilderness/urban route, field course, expedition mentor |
| Information / records | Investigation, History, Factions, Deception, Empathy, Technical Systems | Investigator, Envoy, Operator | archive, records terminal, interviewing, evidence handling |

Coverage check: every one of the 23 current skills appears in at least one row.

This table does **not** state that skill value alone grants a profession. Profession qualification may also require:
- training time;
- work evidence;
- assessment;
- license;
- mentor approval;
- knowledge;
- legal access;
- organization membership;
- safe equipment handling;
- authored world events.

---

# 6. Profession grade

## 6.1 Meaning

**TARGET:** profession grade represents qualification, responsibility, certification, or professional standing **inside one profession**.

It is not a universal character power tier.

## 6.2 Grade rules

A profession grade:
- must belong to one profession;
- may have prerequisites;
- may affect work eligibility/access;
- may affect pay bands where economy rules support them;
- may grant responsibility rather than combat power;
- may require assessment/field evidence;
- may be suspended/revoked if world rules support it;
- must not be inferred solely from global Level.

No universal numeric grade ladder is approved here.

Examples such as “apprentice”, “licensed”, “senior”, or letter grades remain **PROPOSAL wording** until a profession catalog or world authority defines them.

---

# 7. Institution and faction rank

## 7.1 Institution rank

**TARGET:** formal authority within one institution.

It may influence:
- command authority;
- official duties;
- clearance;
- services;
- records access;
- authorized equipment;
- ability to issue organization-specific orders.

It does not automatically grant:
- personal trust;
- universal legal power;
- wealth;
- combat competence;
- profession qualification outside the institution.

## 7.2 Faction rank

**TARGET:** formal position or structured standing inside a faction.

Faction rank remains separate from:
- faction reputation;
- personal relationship;
- profession;
- civic/legal status.

A faction may have no formal rank ladder at all.

## 7.3 Organization-specific ladders

Rank is organization-specific.

Required future rank-definition fields:
- rank ID;
- owning organization ID;
- organization type;
- display name;
- predecessor/successor or ladder relation if applicable;
- authority scope;
- duties;
- clearance/access grants;
- prerequisites;
- appointment/promotion authority;
- demotion/removal rules;
- public/private visibility;
- provenance.

Do not compare rank numbers across unrelated organizations.

“Rank 3” in one institution must never silently equal “Rank 3” in another.

---

# 8. Role versus rank

Role answers:
> What does this member do?

Rank answers:
> Where does this member sit in the organization's authority structure?

Profession answers:
> What occupational capability/qualification does this character have?

One person can therefore simultaneously be:
- qualified in a profession;
- assigned a particular role;
- hold an organization rank;
- have a separate civic status;
- have positive or negative reputation;
- have personal relationships that disagree with public standing.

No concrete Gate Twelve institution/rank is canonized by this packet.

---

# 9. Civic and social status

## 9.1 Civic/legal status

**TARGET:** civic/legal status represents a position recognized by law, citizenship rules, residency, licensing, legal restriction, public office, or another society-level rule.

Examples are intentionally not canonized here.

A civic status record should define:
- status ID;
- issuing/recognizing jurisdiction;
- eligibility;
- grants/restrictions;
- visibility;
- start/end conditions;
- transition provenance;
- conflicts with other statuses;
- player-safe label.

## 9.2 Social-status category

Do not create a durable social-class hierarchy unless the world actually needs one.

If social status is only an interpretation of:
- wealth;
- reputation;
- profession;
- family;
- rank;
- fame;
- local culture;

then keep those owners separate and derive presentation.

Create `SOCIAL_STATUS_*` records only when the status has independent world rules.

---

# 10. Reputation

Reputation is not rank.

**TARGET:** reputation expresses how a specific person, group, settlement, institution or faction regards the player.

The owning social/reputation system decides:
- axes or score;
- bounded ranges;
- sources;
- decay/persistence if any;
- privacy;
- reaction consequences.

This packet only defines the boundary:
- high reputation may be a prerequisite for appointment;
- appointment does not overwrite reputation;
- faction reputation does not overwrite personal relationship;
- public reputation may differ from private NPC memory;
- reputation labels shown by UI must come from player-safe authority.

---

# 11. Global Level, class and ability separation

The following chains remain independent.

## 11.1 Level

Level is a Status progression axis.
It may become a prerequisite for specific content when explicitly authored.
It does not assign profession, class or rank automatically.

## 11.2 Ability rank

Ability rank belongs to one ability family.
It does not imply profession or class progression.

## 11.3 Technique mastery

Technique mastery belongs to one technique.
It does not create organization authority.

## 11.4 Combat class

The Combat Class Catalog owns seven TARGET class families:
- Vanguard;
- Skirmisher;
- Operator;
- Field Specialist;
- Investigator;
- Envoy;
- Ability Specialist.

Profession may share skills and training routes with a class without being the class.

Examples:
- a technician profession can support Operator development but does not grant Operator features;
- a medical profession can support Field Specialist development but does not grant tactical stabilization actions unless the tactical/medical owner authorizes them;
- security work can train Tactics/Defense without granting Vanguard rank;
- a researcher can study Powers without becoming an Ability Specialist.

---

# 12. Training / mentor / facility integration

D-045's next child will define the full Training / Mentor / Facility progression standard.

This packet establishes only the namespace boundary.

Profession/rank/status progression may consume:
- training activities;
- world time;
- mentor/evaluator access;
- facility access;
- equipment/tool access;
- skill evidence;
- knowledge;
- field proof;
- authored work history;
- relationship/faction/institution prerequisites.

It must not duplicate training formulas.

A profession record may say:
> requires an approved medical evaluation activity

It should not reimplement:
- resource cost;
- time advancement;
- injury interaction;
- learning yield;
- interruption logic.

Those belong to activity/progression owners.

---

# 13. Tactical-role integration

Profession, rank and status can affect tactical play only through explicit authorized seams.

Potential TARGET relationships:
- profession may expose legal technical/medical interaction options;
- organization rank may allow an order when command rules and party/organization context permit;
- civic/legal status may affect whether force, access or equipment use is lawful;
- profession may provide equipment familiarity;
- class may provide tactical feature permissions;
- knowledge may reveal tactical information.

But V08 tactical authority continues to own:
- movement;
- occupancy;
- action budget;
- LOS/detection;
- cover;
- targeting;
- damage/injury;
- objectives/retreat.

A profession/rank record may request a tactical option; it cannot redefine geometry or hit resolution.

No D-072/D-073 implementation is changed by this packet.

---

# 14. Access and world consequences

Progression-state records should grant **explicit consequences**, not vague implied power.

Possible target consequences:
- location access;
- records access;
- service eligibility;
- authorized equipment;
- work activities;
- mentor access;
- dialogue;
- legal permissions;
- schedule obligations;
- quest/event eligibility;
- organization duties.

Every grant should identify its owner.

Example:
- institutional rank may grant a records-clearance tag;
- the world/access system validates the actual door/record interaction;
- Android displays only the player-known result;
- the rank itself does not directly mutate a scene into an unlocked state without the world rule.

---

# 15. Persistence and migration boundary

## 15.1 Phase 1

**CURRENT:** D-061 keeps Phase 1 progression on save schema v1.

This packet does not add any save field.

## 15.2 Future durable implementation

Before profession/class/rank/status becomes durable runtime state, the implementing task must define:
- authoritative owner;
- record shape;
- validation;
- content registry;
- legacy/default behavior;
- migration from earlier saves;
- save/load round trip;
- deterministic mutation path;
- rollback;
- player-safe projection;
- Android typed mapping if exposed;
- versioning policy.

The representation is intentionally **not selected here**.

Do not assume:
- a new top-level `professions` field;
- a nested `player.profession` field;
- a generic `ranks` map;
- reuse of `flags`;
- reuse of `perks`;
- reuse of `relationships`.

Those are migration decisions.

## 15.3 Renames

If an implemented stable profession/rank/status ID must change:
1. record old ID;
2. record new ID;
3. define deterministic migration;
4. validate authored references;
5. migrate fixtures;
6. test old-save load;
7. test new-save round trip;
8. preserve player-safe labels independently.

Never migrate from display text.

---

# 16. Mutation and event provenance

Future state changes should be transactional and provenance-rich.

A promotion/qualification/status transition should be able to record:
- source/cause;
- before state;
- after state;
- world time;
- authority/organization;
- relevant stable IDs;
- player-visible consequence;
- private metadata only where the owning privacy contract allows it.

Mutation examples:
- profession qualification awarded;
- grade advanced;
- rank appointed;
- rank demoted;
- membership suspended;
- civic status granted/revoked.

UI must never directly set these fields.

---

# 17. Player-safe projection

Android remains presentation/interaction, not progression authority.

A future player-safe profession/rank/status projection may include:
- stable public ID where allowed;
- display name;
- known grade/rank;
- visible organization;
- visible responsibilities;
- known access;
- next known requirement;
- current qualification/status;
- player-known suspension/restriction.

It must exclude:
- secret membership;
- undercover state;
- hidden clearance;
- undiscovered promotion requirements;
- private NPC opinion;
- hidden faction goals;
- internal AI utility;
- arbitrary raw organization maps.

If a record is not player-known, the client must not infer it from assets or labels.

---

# 18. Validation rules

Future validators must prove at least:

1. every stable ID is unique within its registry;
2. every profession grade references a valid profession;
3. every organization rank references a valid organization and appropriate rank namespace;
4. every role reference is valid for the organization/context where used;
5. civic statuses reference a valid jurisdiction/authority when required;
6. no record depends on an unknown skill ID;
7. all referenced class IDs resolve if class relationships are declared;
8. all referenced mentor/facility/activity IDs resolve when those registries exist;
9. access grants use known target systems/tags;
10. hidden/private fields are not projected;
11. rank transitions are coherent;
12. retired/suspended/ended records do not remain active accidentally;
13. no universal rank comparison is inferred across unrelated organizations;
14. profession and class do not silently mirror one another;
15. reputation mutation is not substituted for rank appointment;
16. no target record is reported as CURRENT runtime without implementation evidence.

---

# 19. Authoring packet shapes

These are TARGET documentation shapes, not runtime schemas.

## 19.1 Profession packet

- profession_id
- display_name
- family
- canon_status
- description
- skill_anchors
- class_relationships
- qualification_routes
- grade_model
- activities
- mentors/evaluators
- facilities
- tools/equipment
- legal_requirements
- organization_dependencies
- access_grants
- schedule/work_patterns
- economy_hooks
- tactical_relationships
- privacy
- provenance
- implementation_owner
- validation

## 19.2 Profession-grade packet

- grade_id
- profession_id
- display_name
- canon_status
- prerequisites
- qualification_evidence
- responsibilities
- access_grants
- renewal/revocation
- next_grade_links
- provenance

## 19.3 Organization-rank packet

- rank_id
- organization_id
- namespace_kind: institution | faction
- display_name
- authority_scope
- duties
- role_relationships
- prerequisites
- appointment_source
- access/clearance
- visibility
- predecessor/successor
- removal/demotion
- provenance

## 19.4 Civic-status packet

- status_id
- jurisdiction_id
- display_name
- legal_effects
- grants
- restrictions
- eligibility
- start/end rules
- visibility
- provenance

---

# 20. Forbidden inference matrix

| Observed fact | Forbidden automatic inference |
| --- | --- |
| high Level | high profession grade |
| high skill | profession qualification |
| profession qualification | combat class |
| combat class | job/employer |
| organization membership | rank |
| rank | personal loyalty/trust |
| faction reputation | faction rank |
| personal relationship | public reputation |
| civic status | combat authority |
| job assignment | permanent profession |
| equipment ownership | profession |
| ability rarity | institutional authority |
| profession grade | universal world tier |
| UI badge/icon | authoritative state |

Any exception requires an explicit authored rule.

---

# 21. Reconstruction acceptance checklist

This child is reconstruction-grade when a future developer can answer without guessing:

- What is a profession?
- How is profession different from class and job?
- What is profession grade?
- How is organization role different from rank?
- How are institution and faction rank separated?
- How is reputation different from rank?
- What does civic/social status mean?
- How do global Level and ability rank fit without replacing these systems?
- Which current runtime fields exist today?
- Why does Phase 1 remain schema v1?
- What ID families should future target records use?
- Which proposed prefixes are not yet canon/runtime?
- How do all 23 current skills connect to profession-family design?
- How do profession families relate to the seven class families?
- How do training, mentors and facilities participate without duplicating their rules?
- How can profession/rank/status affect tactical/world access without taking authority from those systems?
- What privacy must the bridge preserve?
- What future migration evidence is required?
- Which inferences are explicitly forbidden?

---

# 22. D-045 child handoff

The Training / Mentor / Facility Progression Standard named by this P7 packet is now materialized as:

`docs/systems/TRAINING_MENTOR_FACILITY_PROGRESSION_STANDARD.md`

P12 consumed the profession/rank/status namespaces defined here rather than inventing another occupational hierarchy. It preserves existing activity/time/resource owners, separates mentor/evaluator capability from NPC identity and facility capability from world-location identity, and maps all 23 current skills plus all seven target class families.

The direct next D-045 child is now:

**Gate Twelve Progression Proof Packet**

That proof packet should consume P7 + P12 rather than reopening their namespace/ownership work.

---

# 23. Result

This packet materializes D-045's third reconstruction-grade child.

It establishes:
- explicit profession/rank/status separation;
- stable-ID guidance;
- complete 23-skill profession-family coverage;
- class/profession cross-system boundaries;
- training/facility dependency direction;
- future tactical-role seams;
- social/faction/privacy boundaries;
- schema-v1 non-expansion for current Phase 1;
- future migration/validation requirements;
- one direct next D-045 child.

No runtime progression, canon institution, profession catalog, rank ladder, balance value, save-schema change, Android DTO, or D-072/D-073 tactical behavior is implemented by this document.
