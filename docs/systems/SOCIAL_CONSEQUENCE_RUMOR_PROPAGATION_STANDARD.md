# THE GAME — Social Consequence & Rumor Propagation Standard

Status: **APPROVED FIRST-PASS V05 CONTRACT / CURRENT LEAK PRIMITIVE EXISTS**
Parent:
- docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md
Current source:
- src/textrpg/social.py

## 1. Purpose

Define how an event can propagate through memories, relationships, knowledge, rumors, and institutions without giving every NPC omniscient awareness.

## 2. Current foundation

Current social.py already has:
- share_knowledge;
- eligible_leak_targets;
- execute_leak_event;
- deterministic sorted recipient selection;
- personality/secrecy inputs;
- history event recording;
- atomic rollback.

This is the correct foundation for bounded rumor propagation.

## 3. Consequence packet

A social event may produce a consequence packet containing:
- source event ID;
- witnesses;
- direct participants;
- memory writes;
- knowledge/belief writes;
- relationship deltas;
- goal changes;
- story-state transitions;
- faction/institution notification;
- rumor seeds;
- public-state changes.

Each write must have an owning subsystem.

## 4. Direct knowledge first

An NPC may only propagate a fact/belief they possess.

No event should send a rumor from a holder whose knowledge state lacks it.

Current eligible_leak_targets already enforces holder knowledge.

## 5. Social network

Rumor spread requires an authored/reconstructed network:
- direct relationship;
- workplace;
- family;
- faction;
- neighborhood;
- party;
- event co-presence;
- communication channel.

Network edges are not automatically bidirectional.

Phase 1 may use a tiny explicit network rather than simulating an entire settlement.

## 6. Propagation event

A rumor/leak event should specify:
- event_id;
- holder;
- knowledge/claim ID;
- eligible network;
- max recipients;
- voluntary/involuntary mode;
- selection policy;
- confidence transformation;
- secrecy impact;
- memory consequence.

If recipient selection is not authored, use deterministic stable order or deterministic seeded selection.

## 7. Distortion

Phase 1 does not require rumor mutation/distortion.

Future distortion must create a new belief/claim variant with traceable provenance rather than silently changing world truth.

## 8. Public information

Some events become public through:
- official announcement;
- posted notice;
- widely witnessed event;
- institutional bulletin.

Public status may make a fact available to a population tier, but named NPC knowledge should still update through a bounded broadcast/event process when their decisions depend on it.

## 9. Relationship consequences

Hearing a rumor does not automatically change relationship.

A separate authored rule may alter trust/suspicion/fear if:
- NPC believes the claim;
- target is relevant;
- event has social significance.

This keeps cause traceable.

## 10. Secrecy and discipline

Current leak eligibility uses:
- holder discipline;
- honesty;
- knowledge secrecy.

Future rules can add loyalty, fear, institutional policy, or relationship, but must remain deterministic and testable.

## 11. False beliefs

Rumors may be false.

NPC behavior uses the believed record.

Later correction creates a contradiction/update event and may affect relationship/memory.

## 12. Player actions

Jack may:
- share;
- conceal;
- lie if dialogue system supports it;
- publish;
- warn;
- reveal evidence.

Each should operate on knowledge/belief records and social consequences rather than setting arbitrary “NPC knows everything” flags.

## 13. World event integration

Important consequences may alter:
- NPC schedule;
- faction goal;
- service availability;
- quest path;
- law/enforcement response;
- adversary recurrence;
only after the relevant domain validates the change.

## 14. Privacy and UI

Player sees only rumors/facts Jack has learned.

UI does not receive the global rumor graph or all recipient lists.

Developer diagnostics may expose propagation for testing.

## 15. Performance

Propagation is event-driven, not continuous gossip simulation.

Bound:
- recipients per event;
- propagation depth per simulation step;
- number of active rumor chains;
- off-screen update frequency.

## 16. Tests

Required:
- holder must know claim;
- deterministic recipient order;
- max recipient cap;
- no state creation during eligibility query;
- atomic rollback;
- false belief allowed;
- relationship not auto-mutated;
- hidden recipient list not player-projected;
- save/load preserves propagated knowledge.

## 17. Phase 1

Tamsin's Gate Twelve knowledge chain proves direct knowledge gating.

A later Phase 1 extension may add one bounded leak or communication consequence, but the core playable requirement does not require settlement-wide rumor simulation.
