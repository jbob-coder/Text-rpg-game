# THE GAME — Character Identity & Profile Standard

Status: **APPROVED FIRST-PASS CONTRACT / V05**
Parents:
- docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md
- docs/world/WORLD_NPC_POPULATION_STANDARD.md
- docs/android/PLAYER_SAFE_ROOM_ACTOR_PROJECTION_CONTRACT.md

## 1. Purpose

Define what makes a persistent character the same character across world state, social simulation, tactical encounters, UI, saves, and visual assets.

Identity is not a UI label. It is durable gameplay data with a stable ID.

## 2. Current reality

Current runtime uses stable NPC IDs in GameState.npcs, relationships, party state, effects, and content. The current vertical slice contains NPC_TAMSIN as the only authored named character record and uses encounter/story state separately from her visual identity data.

Current NPC dynamic state includes:
- personality;
- knowledge;
- memories;
- goals;
- story_state.

Current character visual/content data is separate.

This separation should be preserved and made explicit.

## 3. Identity layers

A persistent character record has four layers:

1. Stable identity
   - character_id;
   - canonical/provisional status;
   - player-facing name when known;
   - character type;
   - creation/source authority.

2. Static authored profile
   - age band/date data when canon;
   - physical identity;
   - background/origin;
   - role/profession;
   - faction/institution memberships;
   - home/work anchors;
   - visual identity references.

3. Durable mutable state
   - current condition;
   - relationships;
   - knowledge;
   - memories;
   - goals;
   - schedule/presence;
   - story tracks;
   - inventory/equipment when modeled;
   - faction/rank state.

4. Player-safe identity projection
   - only the identity details the player can legitimately know.

## 4. Stable ID rules

Persistent character IDs:
- are semantic;
- never encode current location/rank;
- survive display-name changes;
- survive portrait/sprite replacement;
- survive faction change;
- survive temporary absence;
- are never reused for a different person.

Recommended namespaces:
- CHAR_* for central/player-grade persistent characters;
- NPC_* for persistent non-player characters;
- encounter-local ACTOR_* only for nonpersistent tactical entities.

Promotion from encounter-local actor to persistent NPC requires an explicit migration and a new stable persistent ID.

## 5. Player identity

Jack is the directly controlled player character in the target design.

The player adapter must reference the authoritative player record rather than copy Jack into NPC state merely so shared actor systems can consume him.

Shared actor interfaces may expose common fields without collapsing player/NPC ownership.

## 6. Name visibility

The player-facing name can differ by knowledge state:
- unknown person;
- role/title;
- partial identity;
- full known name.

The stable internal ID is never hidden from engine/tooling but must not be exposed to the player merely because it exists.

## 7. Identity versus state

The following do not create a new identity:
- injury;
- disguise;
- equipment change;
- promotion;
- faction defection;
- relationship change;
- memory loss;
- portrait expression;
- combat state.

Those are state/projection changes attached to the same stable character.

## 8. Visual identity

A recurring named character may reference:
- gameplay sprite family;
- portrait family;
- equipment overlays;
- expression set;
- injury variants;
- room anchors.

Visual assets never become the source of truth for character presence or state.

## 9. Canon status

Recommended record status:
- proposal;
- provisional_canon;
- canon;
- retired/historical.

Promotion requires explicit content/world authority, not merely runtime presence.

## 10. Required validation

A persistent character record must validate:
- unique ID;
- valid referenced locations/factions/assets;
- no duplicate identity under another stable ID;
- static/dynamic state separation;
- player-safe projection rules;
- save migration when durable schema changes.

## 11. Phase 1

NPC_TAMSIN remains the first recurring-character proof.

The first implementation should not create a broad population system before one recurring character can preserve identity, knowledge, memory, relationship, goal, presence, projection, and save/load coherently.

## 12. Tests

Required:
- stable ID survives rename/presentation changes;
- unknown-name projection;
- no hidden identity leak;
- save/load identity preservation;
- encounter-local actor cannot silently become a persistent NPC;
- visual replacement does not alter gameplay identity.
