# THE GAME — Institution, Role, Credential, Authorization & Protocol Standard

Status: **ACTIVE TARGET-GAME DESIGN / ROLE-CLASS COMPATIBLE / NAMED WORLD ENTITIES STILL OPEN / NOT IMPLEMENTED**

Parents:
- `PASSIVE_FACTION_INSTITUTIONAL_SCALING_STATE_MODEL_0001_0010.md`
- `PASSIVE_EVENT_QUALIFICATION_GOVERNANCE_STANDARD.md`
- `PASSIVE_WORLD_INTEGRATION_ROLE_CLASS_MATRIX_WAVE_001.md`
- `STATUS_GATE_TWELVE_EVIDENCE_BACKED_KNOWLEDGE_WORLD_ADJUDICATION_001.md`
- `STATUS_PARENT_FIXTURE_BATCH_005_FATIGUE_ENVIRONMENT_RECOVERY_INSTITUTION.md`

Purpose: define the parent institutional model required by Faction/Institutional passives, profession access, command workflows, credentials, restricted infrastructure, classified information, and future law/security systems.

This standard creates **system semantics**, not named governments/factions.

---

# 1. Core distinction

Do not collapse these concepts:

- institution membership;
- role;
- rank;
- credential;
- clearance;
- authorization;
- protocol familiarity;
- reputation;
- faction standing;
- profession.

A character can have one without all others.

# 2. Institution record

A future institution requires at least:
- stable `institution_id`;
- institution type/role class;
- name when canonized;
- region/jurisdiction;
- purpose;
- role namespace;
- credential namespace;
- protocol namespace;
- policy/law links;
- membership rules;
- status/version.

Role classes can exist in documentation before named institutions.

# 3. Role

A role describes an authorized organizational function.

Record needs:
- role ID;
- institution ID;
- duties;
- authority scope;
- prerequisites;
- reporting/responsibility relationships;
- active/inactive state.

Role is not reputation.

# 4. Rank

Rank is a position in one institution-specific hierarchy where such a hierarchy exists.

Rules:
- no universal rank scale across all institutions;
- rank does not automatically transfer;
- rank can affect authority but is not identical to authorization;
- a profession grade is not automatically institutional rank.

# 5. Credential

A credential is evidence that an institution recognizes some identity, role, qualification, or permission.

Possible forms:
- badge;
- digital record;
- document;
- token;
- biometric binding;
- another authored form.

The system model should store semantic credential state independent of presentation.

# 6. Credential record

Future credential fields:
- credential ID;
- issuing institution;
- holder stable ID;
- credential type;
- scope;
- issue time;
- expiry if any;
- active/revoked/suspended state;
- version;
- verification method;
- public/private/classified fields.

A passive cannot create a credential.

# 7. Clearance

Clearance is a bounded authorization category for protected access/information.

It is not automatically present in every institution.

Where used, define:
- clearance ID;
- institution;
- scope/domain;
- level/category;
- issue authority;
- expiry/revocation;
- compartment links;
- handling rules.

Do not infer a clearance hierarchy merely because a door is restricted.

# 8. Authorization decision

Authorization is an event-specific decision:

`subject + requested action/resource + institution/context + current credentials/role/policy -> ALLOW / DENY / CONDITIONAL`

The authoritative authorization resolver owns the decision.

Passives may reduce workflow error.

They do not change DENY to ALLOW without an explicit permission-changing mechanic.

# 9. Access object

A protected target may be:
- physical area;
- document;
- system;
- equipment;
- service;
- procedure;
- information compartment.

Every protected target should identify the policy/authority that controls it.

# 10. Protocol

A protocol is an institution-owned procedure/rule set.

Record needs:
- protocol ID;
- institution;
- version;
- effective world time;
- scope;
- steps/checks;
- required roles/credentials;
- superseded version if any;
- secrecy/knowledge scope;
- training/review path.

# 11. Protocol versioning

Familiarity must bind to:
- protocol identity;
- relevant version range.

A character who knows version A does not automatically know materially changed version B.

Migration/transition policy may allow partial familiarity.

# 12. Command / responsibility structure

A command structure is a relationship graph, not a universal ladder.

Possible edges:
- reports_to;
- supervises;
- operational_control;
- temporary_assignment;
- advisory;
- support;
- emergency_authority.

Command familiarity helps navigate known legitimate structure.

It does not create obedience or rank.

# 13. Institutional service event

Qualification/progression can use stable service events.

A service event should identify:
- event ID;
- institution;
- character;
- role;
- task/protocol;
- authorization state;
- start/end WORLD_TIME;
- outcome;
- supervisor/reviewer where applicable;
- competency/quality result;
- duplicate-credit marker.

This prevents vague “served 15 times” farming.

# 14. Credential Navigation passive boundary

Credential Navigation may reduce avoidable workflow error in a known valid credential/access process.

It cannot:
- invent credentials;
- reveal hidden credentials;
- bypass denied access;
- transfer knowledge between unrelated institutions automatically.

# 15. Clearance Awareness passive boundary

Clearance Awareness may improve understanding of the user's own legitimately known boundaries/handling rules.

It cannot:
- enumerate hidden clearance levels;
- reveal another person's clearance;
- reveal protected targets;
- turn denial responses into a probing oracle.

# 16. Protocol Memory boundary

Protocol Memory improves recall of legitimately learned institutional procedure.

It cannot:
- recall unknown protocol;
- bypass version change;
- reveal classified steps not learned.

# 17. Institutional Language boundary

Institutional Language concerns vocabulary/format/procedure familiarity.

It does not create:
- authority;
- membership;
- credibility;
- trust.

# 18. Chain Familiarity boundary

Institutional Chain Familiarity should be scoped to:
**institution-specific responsibility routing/procedure**.

Leadership `Chain-of-Command Fluency` should be scoped to:
**execution/coordination under a legitimate formal command relationship**.

This split resolves their potential-duplicate risk conceptually.

Both still need record-specific canon review.

# 19. Secrecy and classification

Classification attaches to a specific datum/protocol/object.

A classification record should identify:
- owning authority;
- protected datum;
- reason;
- authorized roles/clearances;
- handling rules;
- declassification/expiry if any.

“Government classified” without a named authority/domain is not reconstruction-grade final world data.

# 20. Knowledge versus permission

A character may know:
- a restricted area exists;
- a protocol exists;
- a clearance level exists

without being authorized to use/access it.

Conversely, a credential can authorize an action without exposing all underlying policy details.

# 21. Reputation

Reputation influences social/institutional reactions.

It is not a credential.

High reputation cannot automatically open a protected system unless policy explicitly allows reputation/discretion to affect authorization.

# 22. Profession

Profession can provide:
- training;
- legitimate task history;
- organizational access;
- credential prerequisites.

Profession is not automatically membership in one institution.

# 23. Gate Twelve boundary

Confirmed Gate Twelve evidence supports:
- controlled/restricted maintenance infrastructure;
- civic/maintenance work contexts;
- archive/records context;
- contractor/workshop context.

It does **not** yet establish:
- a named issuing authority;
- credential technology;
- clearance levels;
- command hierarchy;
- formal protocol IDs.

Therefore Gate Twelve can instantiate this model only after parent-world entities are approved.

# 24. Authorization sequence

Target order:
1. identify institution/context;
2. identify requested action/object;
3. load subject role/credential state;
4. validate credential status/version/expiry;
5. apply policy/clearance/compartment rules;
6. produce authorization decision;
7. only then apply familiarity/passive workflow modifiers to allowed process stages.

A passive does not run before authorization merely to discover hidden requirements.

# 25. Player-safe projection

The player may see:
- their own known role;
- visible credential;
- known clearance category;
- known protocol;
- an allowed/denied result with authored reason if world rules reveal it.

Do not expose:
- hidden clearance taxonomy;
- undiscovered protected targets;
- other users' credentials;
- internal policy tree;
- classified protocol steps.

# 26. Save/load

Persist:
- institution membership;
- roles;
- credentials;
- revocation/expiry;
- clearance/compartment membership;
- known protocol versions;
- service events;
- authorization-relevant world changes.

Save/load cannot:
- reactivate revoked credential;
- duplicate service credit;
- reveal hidden access;
- reset expiry unless world time was legitimately restored by a mechanic that owns it.

# 27. Parent fixture for command familiarity

A future `RESOLVER_COMMAND_STRUCTURE_FAMILIARITY` range fixture can exist only after at least one approved institution defines:
- role graph;
- protocol;
- ordinary workflow error/overhead;
- reassignment case;
- stale-version case;
- unauthorized boundary.

This standard supplies the schema, not the named fixture.

# 28. Required tests

- no credential => no credential-derived authorization;
- revoked/expired credential fails;
- passive cannot convert DENY to ALLOW;
- wrong institution credential does not transfer automatically;
- old protocol version can produce mismatch;
- hidden clearance is not enumerable through repeated checks;
- service event counts once;
- save/load preserves credential/revocation state;
- reputation does not act as credential unless policy explicitly says so;
- institutional/passive knowledge does not leak classified protocol content.

# 29. Remaining world blockers

Still open:
- named institutions;
- actual role/rank taxonomies;
- credential technology/presentation;
- clearance schemes where needed;
- law/policy documents;
- Gate Twelve issuing/operating authority;
- institutional history;
- numeric workflow error ranges.

No named institution, credential, or passive is canon-promoted by this standard.
