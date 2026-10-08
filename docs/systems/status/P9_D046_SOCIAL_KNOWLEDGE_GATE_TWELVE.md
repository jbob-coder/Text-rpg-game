# D-046 P9 — Gate Twelve Social Passive Knowledge Integration

Status: Phase-C adjudication, NOT CANON, NOT IMPLEMENTED.
Owner: Veyr / PLAYER_VEYR.

## Source-backed resolution

The D-075 Tamsin/Dead Relay cooperative versus solo quest-branch proof (`docs/evidence/D075_PHASE1_QUEST_BRANCH_WORLD_CONSEQUENCE_2026-10-04.md`; `tests/test_phase1_quest_branch_world_consequence.py`) establishes durable actor-specific social/quest consequences and the later player-visible `ASK_TAMSIN_ABOUT_SHARED_ENTRY` choice. It does not establish public reputation, passive acquisition, an institution or access to NPC private memories.

`src/textrpg/core.py` stores durable `relationships`, `knowledge`, `npcs`, `quests` and `history`; `src/textrpg/social.py` provides relationship/memory/knowledge operations. The Status Phase-C owner disposition labels conceptual `SOCIAL_CONTEXT_STATE` COMPOSE_CURRENT_STATE, not an implemented target passive owner.

| Passive | Supported world/knowledge context | Still missing |
|---|---|---|
| `PASSIVE_SOC_0007` Rapport Habit | Existing Tamsin relationship and cooperative interaction are an actor-specific rapport-maintenance context. | Repeated verified social event/anti-duplicate qualification and approved social effect API. One cooperative quest does not unlock a habit. |
| `PASSIVE_SOC_0010` Reputation Awareness | An explicitly visible choice can be a known actor-specific precedent. | Authored public reputation/witness-publication truth, recipient knowledge provenance, qualification and visibility rules. Hidden NPC thoughts are not public reputation. |

SOC_0010's compact public-rumor/classification posture is flagged likely over-classified in `PASSIVE_SOCIAL_BEHAVIORAL_KNOWLEDGE_REFINEMENT_0001_0010.md`. No current Gate Twelve evidence proves the proposed public/institutional knowledge holders. Preserve the registry row; review real provenance before canon promotion.

## Privacy and implementation boundary

Keep world truth, NPC-private memories/relationships and player-known facts separate. The player-safe Android projection must not expose NPC-private records or hidden passive requirements. Unqualified passives have no name, icon, progress or unlock clue. `social.ensure_npc` can create new NPC shells, so future integration requires validation against authorized durable NPC identities. Proposed passive effects require an atomic, replay-safe qualification contract, not inferred UI state.

## Validation and next action

Later tests should verify the D-075 cooperative/secret branch visibility difference, reject unknown NPC IDs without mutation, preserve rollback, and redact private NPC/passive metadata. Start from `tests/test_social.py` and `tests/test_phase1_quest_branch_world_consequence.py`.

Current-source mapping for SOC_0007/SOC_0010 is clarified. Public reputation publication, typed qualification/anti-repeat evidence, effect parameters, explicit passive-list projection and canon review remain blocked. No runtime tests or Android tests were executed for this documentation pass. No existing stable ID, content row or code is changed by this packet.
