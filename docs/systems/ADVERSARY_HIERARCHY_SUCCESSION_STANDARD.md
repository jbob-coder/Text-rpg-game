# THE GAME — Adversary Hierarchy, Promotion & Succession Standard

Status: **APPROVED FIRST-PASS V09 CONTRACT / ORIGINAL WORLD-LOGICAL MODEL**
Parent:
- docs/systems/PERSISTENT_ADVERSARY_WORLD_MEMORY_MASTER_PLAN.md
Related:
- docs/systems/FACTION_HIERARCHY_MEMBERSHIP_STANDARD.md
- docs/world/WORLD_POLITICAL_ENTITIES.md

## 1. Purpose

Define how a persistent adversary's formal role can change and how a world organization replaces a removed member without copying a branded fixed promotion ladder.

## 2. Hierarchy authority

Adversary hierarchy is not a separate magical rank system.

It consumes the faction/institution hierarchy owned by the world/social domains.

An adversary can hold:
- faction membership;
- role;
- rank when that faction uses rank;
- territory/assignment;
- responsibilities;
- subordinates only when authored.

## 3. Promotion/demotion causes

Valid causes may include:
- mission success/failure;
- appointment;
- vacancy;
- leader decision;
- disciplinary action;
- political event;
- resource/control change;
- proven competence;
- player-caused world consequences.

Combat victory/loss alone does not guarantee promotion/demotion.

## 4. Promotion transaction

A role/rank transition should record:
- event_id;
- actor_id;
- faction_id;
- old role/rank;
- new role/rank;
- cause;
- authority/source;
- world time;
- resource/responsibility changes;
- player visibility.

The faction record must support the target role.

## 5. Demotion

Demotion may affect:
- authority;
- resources;
- assignment;
- access;
- goals;
- reputation within faction.

It does not erase memories, personality or injuries.

## 6. Succession

When a role becomes vacant, a successor may be selected from valid world candidates.

Selection inputs may include:
- faction rules;
- candidate role/rank;
- availability;
- competence;
- relationships/politics;
- location;
- authored succession rules.

Stable deterministic tie-break is required when multiple equivalent candidates exist.

## 7. No memory inheritance

Successor may inherit:
- office;
- public responsibilities;
- equipment/resources owned by the role when world rules allow;
- known institutional records.

Successor does not inherit:
- predecessor's personal memories;
- private relationship axes;
- private grudges;
- personal injuries;
- hidden player knowledge not stored institutionally.

## 8. Vacancies

The system must support a role remaining vacant.

Do not spawn a replacement solely to preserve a hierarchy shape.

A vacancy may create:
- power vacuum;
- reduced capability;
- faction goal/event;
- later appointment.

## 9. Player consequence

Player action may indirectly cause:
- promotion;
- demotion;
- vacancy;
- succession;
- faction instability.

The player-facing UI shows only known consequences.

## 10. Persistent adversary status

Promotion does not automatically make a nonpersistent NPC an adversary.

Adversary eligibility and faction role are separate concepts.

## 11. Tests

Required:
- role transition references valid faction hierarchy;
- combat loss alone does not force demotion;
- successor gets new stable ID/identity;
- no personal memory inheritance;
- vacancy allowed;
- deterministic candidate selection;
- save/load;
- secret promotion redaction where applicable.
