# THE GAME — Persistent Adversary Eligibility & Identity Standard

Status: **APPROVED FIRST-PASS V09 CONTRACT**
Parent:
- docs/systems/PERSISTENT_ADVERSARY_WORLD_MEMORY_MASTER_PLAN.md
Related:
- docs/systems/NPC_CHARACTER_IDENTITY_PROFILE_STANDARD.md
- docs/systems/RECURRING_CHARACTER_PACKET_STANDARD.md

## 1. Purpose

Define which hostile or competitive entities are eligible to become persistent adversaries and how their identity remains stable across encounters.

## 2. Eligibility is deliberate

Not every hostile actor becomes persistent.

Potential eligible classes:
- authored hostile NPC;
- faction operative;
- recurring competitor/rival;
- named hunter/pursuer;
- persistent beast when its species/intelligence/world logic supports it;
- another explicitly authored recurring threat.

Disposable spawned units remain encounter-local.

## 3. Eligibility record

Target fields:
- adversary_id or persistent NPC ID;
- source actor/NPC ID;
- eligibility_rule_id;
- eligibility status;
- reason/source event;
- minimum persistence class;
- canon status;
- faction/territory refs when applicable;
- allowed adaptation families;
- allowed recurrence contexts.

## 4. Promotion from encounter-local actor

An encounter-local ACTOR_* does not become persistent merely because it survived.

Promotion requires:
1. explicit eligibility event;
2. new or existing stable persistent NPC ID;
3. identity/profile record;
4. migration of only legitimate durable state;
5. provenance linking encounter-local actor to persistent identity.

Do not retroactively pretend the stable NPC existed before the promotion unless content establishes it.

## 5. Identity invariants

Persistent adversary ID:
- survives display-name discovery;
- survives injury/scars;
- survives rank/faction change;
- survives equipment change;
- survives location change;
- never reused for a successor.

## 6. Known identity

The engine may know the stable ID while the player only sees:
- Unknown Contact;
- faction role;
- nickname/alias;
- full name.

Player-facing identity is knowledge-gated.

## 7. Beast identity

A persistent beast may have:
- species ID;
- individual persistent ID;
- territory;
- injury history;
- pack relation.

Do not force human rank/social fields onto it.

## 8. De-eligibility

Eligibility may end through:
- death;
- retirement;
- narrative removal;
- permanent capture/removal;
- world migration out of supported scope.

Historical records remain for continuity/reference.

## 9. Limits

A future active-adversary cap may exist for performance/content quality, but no numeric cap is locked here.

Selection should prioritize meaningful authored continuity over quantity.

## 10. Tests

Required:
- disposable actor stays nonpersistent;
- explicit promotion creates stable identity;
- no ID reuse;
- hidden name projection;
- beast profile does not require human rank;
- de-eligibility persists;
- save/load after promotion/removal.
