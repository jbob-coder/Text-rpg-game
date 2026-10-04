# THE GAME — Faction, Institution & Hierarchy Membership Standard

Status: **APPROVED FIRST-PASS V05 CONTRACT / LARGE CATALOG PENDING**
Parents:
- docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md
- docs/world/WORLD_POLITICAL_ENTITIES.md

## 1. Purpose

Define how NPCs belong to factions/institutions and how rank/status is represented without collapsing political authority, profession, citizenship, reputation, and personal relationships into one hierarchy.

## 2. Current reality

The social master defines target faction concepts, but current vertical-slice content does not yet provide a complete faction registry.

Tamsin is described through municipal systems/work identity and a municipal systems badge, but this document does not infer a final faction ID from that visual/context clue.

## 3. Distinct concepts

Keep separate:
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

One NPC may participate in several simultaneously.

## 4. Membership record

Target membership fields:
- membership_id;
- npc_id;
- organization_id;
- organization_type;
- role_id;
- rank_id;
- status;
- joined_at;
- ended_at;
- public_visibility;
- clearance/access tags;
- duties;
- current assignment;
- provenance.

Status examples:
- active;
- suspended;
- probation;
- retired;
- expelled;
- undercover;
- former.

Undercover/secret membership is private state.

## 5. Organization hierarchy

Organization definition may include:
- stable organization ID;
- parent organization;
- purpose;
- jurisdiction/territory;
- rank ladder;
- roles;
- rules/laws;
- resources;
- leadership;
- succession policy;
- allied/opposed organizations;
- reputation relation;
- access/clearance model;
- combat doctrine.

Do not force all organizations into identical rank ladders.

## 6. Rank

Rank is organization-specific.

Rank does not automatically grant:
- personal trust;
- combat power;
- wealth;
- universal legal authority.

Any granted capability must be explicit.

## 7. Role vs rank

Role answers what the person does.
Rank answers position in that organization's hierarchy.

Examples may eventually include technician role at a certain municipal grade, but no concrete new Gate Twelve ranks are canonized here.

## 8. Membership changes

Membership may change through:
- appointment;
- promotion;
- demotion;
- transfer;
- suspension;
- expulsion;
- retirement;
- death;
- faction split;
- story event.

Every transition should record:
- cause;
- before/after;
- world time;
- authority/source;
- player-visible consequence if any.

## 9. Reputation

Player/faction reputation is separate from NPC membership.

An NPC may react to Jack's faction reputation through authored rules, but that does not rewrite their personal relationship automatically.

## 10. Access

Membership/rank may grant access to:
- locations;
- records;
- equipment;
- services;
- dialogue;
- tactical orders.

Access checks must be engine-owned and may also depend on credentials, knowledge, quest state, or law.

## 11. Orders and duties

Organization orders may create:
- goals;
- schedule overrides;
- tactical doctrine;
- travel assignments.

An order still cannot grant knowledge the organization has not communicated to that NPC.

## 12. Persistent adversary integration

Adversary promotion/demotion must use the world's actual organization hierarchy.

Do not create a separate branded-style enemy ladder disconnected from faction state.

Successors may inherit role/authority but not private memories.

## 13. Privacy

Secret membership, clearance, and internal assignments remain private until discovered.

Android receives only player-known organization/rank labels.

## 14. Validation

Required:
- organization IDs stable;
- rank belongs to organization;
- role/rank references valid;
- dates/state transitions coherent;
- one active membership record per same organization/role unless explicitly multi-role;
- secret membership not projected;
- no implicit social/relationship effects.

## 15. Phase 1

Phase 1 does not require a full faction catalog.

For Tamsin:
- preserve municipal role clues;
- do not invent a final institution/rank before world canon settles it;
- use PROPOSED/UNKNOWN references where needed.

For the Service Fork encounter:
- provisional contacts remain encounter-local and unassigned to a canon faction until owner/content review.
