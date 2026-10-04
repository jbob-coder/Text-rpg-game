# THE GAME — Passive Event Qualification Governance Standard

Status: **PROVISIONAL PHASE-C STANDARD / NOT CANON / NOT IMPLEMENTED**

Scope:
- Unique Event passives (`PASSIVE_UEV_*`);
- Cosmic / System passives (`PASSIVE_COS_*`);
- Unknown / Classified passives (`PASSIVE_CLS_*`) where qualification is packet/event based.

Purpose: define stable one-time qualification behavior so event-bound passives cannot be duplicated, farmed, inferred from UI, or detached from their authored world evidence.

## 1. Stable qualification authority

Every event-bound qualification requires a stable authoritative identifier.

Classes:
- `WORLD_EVENT_ID`;
- `SYSTEM_EVENT_ID`;
- `CLASSIFIED_REQUIREMENT_PACKET_ID`.

Placeholder IDs such as `authored_event_01` are calibration placeholders and are not canon world events.

## 2. Qualification ledger entry

A future authoritative entry should include:
- qualification source ID;
- passive ID;
- character stable ID;
- participation role;
- event time;
- event version;
- required outcome state;
- evidence/provenance;
- qualification result;
- duplicate-credit marker;
- reveal state;
- audit status.

## 3. Participation roles

Possible roles must be explicit:
- participant;
- survivor;
- direct witness;
- authorized operator;
- protected subject;
- investigator/recorder;
- other authored role.

A witness-only passive cannot be earned from secondhand media unless its own requirement explicitly allows that.

## 4. One-time transaction

Qualification is an atomic transaction:
1. event/packet is validated;
2. character participation is validated;
3. record-specific outcome requirements are validated;
4. prior credit is checked;
5. qualification is committed once;
6. passive ownership/reveal state is updated;
7. audit entry is persisted.

Reloading or replaying presentation cannot issue a second credit.

## 5. Event replay versus world history

A gameplay scene may be replayable for testing or presentation.

The authoritative world event is not re-created merely because the scene is replayed.

Only a new stable world event ID can represent a genuinely distinct event occurrence.

## 6. Unique Event knowledge

Knowledge derives from:
- event participants;
- witnesses;
- surviving records;
- public reporting;
- institutional records;
- classified records.

The passive itself does not make the event publicly known.

## 7. Cosmic / System confirmation

A Cosmic/System passive may require explicit Status/system confirmation.

System confirmation:
- applies only to the specified event/field;
- does not validate adjacent rumors;
- does not grant admin/root access;
- does not expose hidden prompt content by default.

## 8. Classified requirement packets

A classified packet requires:
- packet ID;
- owning authority;
- authorization rule;
- qualification condition;
- redaction policy;
- audit policy;
- declassification/discovery behavior if any.

The client/player-safe projection receives only authorized fields.

## 9. Save/load

Persist:
- source event/packet ID;
- qualification result;
- ownership;
- reveal state;
- one-time transaction marker;
- knowledge/discovery state where relevant.

Save/load must not:
- duplicate qualification;
- re-run a one-time event grant;
- expose redacted requirement data;
- erase already committed event history without explicit migration/recovery logic.

## 10. Branching outcomes

An authored event may have multiple possible outcomes.

A passive requirement must reference the exact qualifying outcome or predicate.

Merely entering the event is not enough unless the passive explicitly requires presence only.

## 11. Death/reset policy

If THE GAME later supports irreversible death, timeline recovery, rollback, or other reset mechanisms, event-bound qualification needs an explicit persistence policy.

Do not infer whether qualification survives a timeline/state reset.

That decision belongs to the parent save/world-history design.

## 12. Anti-farm rules

Disallow:
- reload-credit loops;
- duplicate scene-instance IDs;
- scripted re-entry into the same event record;
- alternate UI path re-triggering;
- client-side ownership assertions;
- repeated classified-packet submission without a new authorized state.

## 13. Required tests

Future minimum tests:
- identical event ID grants at most once;
- invalid participant role fails;
- unmet outcome predicate fails;
- save/load cannot duplicate the grant;
- scene replay cannot create a second event occurrence;
- system confirmation is field-scoped;
- classified packets remain redacted;
- stale client projection cannot grant ownership;
- event version/migration behavior is deterministic.

## 14. Promotion gate

Before any UEV/COS/CLS record can be canon-promoted, it needs:
- a real source event/packet ID;
- authoritative owner;
- valid participation/outcome rule;
- world-history or system-history record;
- knowledge/provenance treatment;
- save/load policy;
- player-safe reveal behavior;
- tests.

This standard does not create or canonize any placeholder event.
