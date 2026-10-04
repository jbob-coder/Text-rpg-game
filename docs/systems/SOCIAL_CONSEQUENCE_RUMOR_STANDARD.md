# THE GAME — Social Consequence & Rumor Propagation Standard

Status: **APPROVED FIRST-PASS CONTRACT / V05**
Parents:
- docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md
- docs/systems/NPC_MEMORY_EVENT_STANDARD.md
- docs/systems/NPC_KNOWLEDGE_BELIEF_PRIVACY_STANDARD.md
Current runtime:
- src/textrpg/social.py

## 1. Purpose

Define how a meaningful event can propagate through memories, beliefs, relationships, goals and rumor networks without giving NPCs omniscient knowledge.

## 2. Current foundation

social.py already supports:
- knowledge transfer;
- deterministic leak eligibility;
- deterministic leak execution;
- relationship changes;
- memories;
- goals.

This standard connects those primitives into a bounded consequence chain.

## 3. Consequence pipeline

Preferred flow:

world/event truth
-> observers/perception
-> observer memory
-> observer belief/knowledge
-> relationship/goal response
-> optional sharing/rumor
-> recipient belief/memory
-> later behavior/world consequence.

Every arrow requires an explicit rule.

## 4. Rumor is not truth

A rumor record is a belief transmitted through a source chain.

It must preserve:
- origin/source when known;
- confidence;
- secrecy;
- transformations/corrections when modeled;
- recipient.

A rumor can be false.

The world truth layer is not overwritten by rumor.

## 5. Network authority

Information can propagate only through an authored or derived social/contact network.

A network edge may come from:
- relationship;
- faction;
- workplace;
- household;
- location co-presence;
- explicit communication channel.

Merely existing in the same save file does not create a propagation edge.

## 6. Determinism

Current leak selection uses sorted eligible targets when recipients are not explicitly authored.

Keep deterministic selection for authoritative simulation.

If later weighted propagation is added, it must use seeded deterministic variation and preserve reproducibility.

## 7. Secrecy and personality

Secrecy, discipline, honesty, and other explicit social values may affect leak eligibility.

They do not guarantee or forbid disclosure unless the rule says so.

## 8. Relationship consequences

A transmitted rumor may change relationships only when:
- recipient believes it sufficiently;
- the content is relevant;
- an authored consequence exists.

Do not add relationship points simply because information moved.

## 9. Reputation

Regional/faction reputation is a separate aggregate system.

Individual rumor propagation may feed reputation through explicit adapters but must not replace persistent person-to-person relationships.

## 10. Privacy

Player UI must not show:
- eligible leak targets;
- secret network edges;
- hidden rumor holders;
- exact confidence/secrecy unless intentionally revealed.

The player learns consequences through the world.

## 11. Performance

Propagation runs on discrete events, not every frame.

Use bounded recipient counts and avoid uncontrolled graph cascades in one tick.

## 12. Tests

Required:
- no network edge => no transfer;
- deterministic recipient selection;
- secrecy/personality eligibility;
- false rumor remains distinct from truth;
- transfer memory creation;
- relationship only through authored consequence;
- bounded cascade;
- player-safe redaction;
- save/load.
