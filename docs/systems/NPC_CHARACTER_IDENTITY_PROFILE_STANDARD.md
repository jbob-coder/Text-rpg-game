# THE GAME — NPC Character Identity & Profile Standard

Status: **APPROVED FIRST-PASS V05 CONTRACT / RUNTIME PARTIAL**
Parents:
- docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md
- docs/world/WORLD_NPC_POPULATION_STANDARD.md
Visual authority:
- docs/assets/CHARACTER_PIXEL_BLUEPRINTS.md
- docs/assets/ROOM_ACTOR_PANEL_OVERLAY_REUSE_STANDARD.md

## 1. Purpose

Define the stable identity record for persistent characters so story, social simulation, world placement, combat, UI, saves, and visual assets all refer to the same person.

Identity data answers who the character is. It must not silently become mutable current state such as location, injury, relationship, or schedule.

## 2. Current reality

Current GameState stores NPC runtime state under state.npcs keyed by stable NPC ID. The current social shell contains personality, knowledge, memories, goals, and story_state.

Current authored content also contains a character identity record for NPC_TAMSIN with visual/body/outfit anchors.

The runtime therefore has identity and state concepts, but they are not yet normalized into one reconstruction-grade character schema.

## 3. Stable character ID

Persistent named character IDs use semantic stable IDs:
- prefix NPC_;
- uppercase snake case;
- identity ID survives display-name changes;
- never recycle an ID for a different person.

NPC_TAMSIN is the current proof.

Supporting encounter actors may use encounter-local IDs until promoted to persistent NPC status.

## 4. Identity record fields

Required for a recurring named NPC:
- npc_id;
- display_name;
- identity_status;
- person_type/species only when canonically relevant;
- age/date data only when needed;
- pronouns/presentation only if authored;
- origin/home reference;
- occupation/role;
- faction/institution membership references;
- legal/social status references;
- short identity summary;
- visual_identity_id;
- portrait/sprite family;
- canon_status;
- provenance;
- aliases known to the world;
- player-facing name rules.

Optional:
- birthday;
- family relations;
- education;
- languages;
- citizenship;
- cultural background;
- permanent marks;
- medical history;
- known public reputation.

## 5. Identity status

Recommended:
- PLACEHOLDER;
- PROPOSED;
- PROVISIONAL_CANON;
- CANON;
- RETIRED_IDENTITY.

PLACEHOLDER cannot receive final identity art.
PROPOSED is design content.
PROVISIONAL_CANON may be used in a vertical slice but remains reviewable.
CANON is accepted current game identity.
RETIRED_IDENTITY remains referentially stable for save/history compatibility.

## 6. Identity vs runtime state

Identity record must not own:
- current location;
- current health;
- temporary injuries;
- current party membership;
- relationship values;
- current goals;
- current knowledge;
- current schedule override;
- current equipment;
- current combat position.

Those belong to runtime/domain state.

Identity may own default/starting references but runtime state must be initialized explicitly.

## 7. Name visibility

A character may exist before Jack knows their name.

Player-safe projection should separate:
- internal entity ID;
- known display label;
- true identity;
- alias/role label;
- identification confidence if needed.

An unknown actor may project as a role label while internal state still uses a stable NPC ID.

UI must never leak the true name merely because asset filenames or registry keys contain it.

## 8. Physical identity and visuals

Recurring named NPCs require a visual identity contract before final art:
- body/silhouette anchors;
- skin/hair/eyes where authored;
- default clothing identity;
- permanent marks;
- equipment attachment points;
- forbidden deviations;
- portrait/sprite compatibility;
- optional emotion/pose families.

Visual variants do not create new identities.

Injuries, equipment, uniforms, expressions, and temporary disguises are state/variant layers.

## 9. World identity

Identity may reference:
- home entity ID;
- workplace;
- institution;
- faction;
- rank/status record.

Those references must remain stable IDs, not free-form prose used as authority.

If parent-world canon is undecided, leave the reference UNKNOWN/PROPOSED rather than inventing a settlement.

## 10. Promotion from supporting actor

When a temporary/support actor becomes persistent:
1. assign/confirm stable NPC ID;
2. preserve observed encounter history if the actor already existed in runtime;
3. create identity profile;
4. reconcile visual provenance;
5. migrate any relationship/knowledge references;
6. avoid creating a duplicate new person.

## 11. Retirement/death

Death does not delete identity.

Identity remains addressable for history, quests, memories, relationships, succession, and save migration. Runtime lifecycle state marks death/absence.

## 12. Player-safe projection

Minimum public character projection may include:
- player-known display name/label;
- portrait/sprite reference;
- visible role/faction if known;
- visible condition/equipment;
- contextual relationship summary if product design allows it.

Private identity fields remain domain-only.

## 13. Validation

Reject:
- duplicate npc_id;
- missing display identity for a named canon NPC;
- unknown canon_status;
- visual identity pointing to another named NPC without explicit shared-body permission;
- current-state fields embedded into immutable identity;
- aliases that conflict with another stable identity without disambiguation.

## 14. Migration impact

Do not destructively rewrite current content/state in one pass.

Target:
- introduce normalized identity registry;
- adapt current NPC_TAMSIN first;
- preserve current state.npcs runtime shape until migration tests prove equivalence;
- keep existing stable IDs.

## 15. Phase 1 requirement

NPC_TAMSIN is the Phase 1 identity proof because a stable ID, character identity details, social state, and branching content already exist.

The Tamsin Phase 1 Social Proof Packet owns the exact proof path.
