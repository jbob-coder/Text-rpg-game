# THE GAME — NPC Knowledge, Belief & Privacy Standard

Status: **APPROVED FIRST-PASS V05 CONTRACT / PRIVACY-CRITICAL**
Parent:
- docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md
Current source:
- src/textrpg/social.py
- src/textrpg/core.py

## 1. Purpose

Define what an NPC knows, believes, suspects, or remains uncertain about and prevent omniscient behavior or player-facing leaks.

## 2. Current foundation

Current npc_learn stores:
- source;
- confidence 0..1;
- truth string;
- secrecy 0..5;
- turn_learned.

Current player state has a separate knowledge container.

This separation is correct and must be preserved.

## 3. World truth vs belief

A proposition may have:
- authoritative world truth;
- Jack/player knowledge;
- each NPC's independent belief;
- rumor variants.

NPC decisions use their belief/knowledge, not hidden world truth.

## 4. Target record

Fields:
- knowledge_id or proposition_id;
- subject/entity references;
- believed value/claim;
- source;
- confidence 0..1;
- truth_relation;
- secrecy 0..5;
- learned_at;
- last_confirmed_at;
- provenance;
- share policy;
- tags.

Current simple records remain a valid migration subset.

## 5. Confidence

Confidence describes certainty, not truth.

An NPC may be highly confident and wrong.

Exact confidence is not player-facing by default.

## 6. Truth relation

Suggested:
- confirmed_true;
- confirmed_false;
- mixed;
- unknown.

A later contradiction should create/update belief history rather than erase why the NPC acted previously.

## 7. Secrecy

Keep current 0..5:
- 0 ordinary/shareable;
- 1 mildly sensitive;
- 2 private;
- 3 restricted;
- 4 highly restricted;
- 5 critical secret.

Secrecy influences sharing/leaks but is not itself a complete access-control system.

## 8. Transfer

Knowledge transfer requires:
- speaker possesses belief;
- recipient can receive;
- authored/social rule allows transfer;
- recipient gets new source/learned time;
- recipient memory may record the communication.

Current share_knowledge provides the foundation.

## 9. Rumor

Rumor is uncertain belief/provenance, not a disconnected second knowledge system.

Propagation may alter confidence/source or create a claim variant only through explicit rules.

## 10. Discovery and inference

NPCs may learn through:
- witnessing;
- investigation;
- dialogue;
- records;
- combat observation;
- faction reports;
- inference.

Inference must use only inputs available to that NPC and be deterministic.

## 11. Forgetting/revision

Phase 1 does not require forgetting.

Future revision must preserve audit history and must not destroy quest/rival causality.

## 12. Player-safe boundary

Android may receive:
- facts Jack knows;
- NPC claims explicitly communicated;
- whether an NPC knows something only when the game deliberately reveals it.

Never project:
- full NPC knowledge map;
- secrecy values;
- hidden source;
- private beliefs;
- hidden faction intel.

## 13. Combat integration

Tactical awareness is short-horizon encounter state.

Durable knowledge is written only for meaningful facts such as recognizing Jack, observing a technique, learning an escape route, or witnessing a major injury.

Tactical sight never copies all player stats/inventory into NPC knowledge.

## 14. Current Tamsin evidence

Current content already demonstrates:
- player can privately learn KNOW_RELAY_DESTINATION_SERVICE_GATE_12;
- Tamsin can separately learn it through recovery or disclosure;
- later choices differ using npc_knows/npc_not_knows;
- Tamsin knowledge changes party/story outcomes.

This is the Phase 1 model to preserve and deepen.

## 15. Tests

Required:
- confidence/secrecy bounds;
- speaker must know before sharing;
- player/NPC knowledge independent;
- false belief allowed;
- deterministic eligible leak list;
- private belief never projected;
- combat does not leak hidden player info;
- save/load;
- query does not mutate.

## 16. Migration

Keep current knowledge IDs and npc_learn/share_knowledge contracts.

Add richer metadata backward-compatibly or through explicit schema migration; do not rename existing knowledge IDs merely for style.
