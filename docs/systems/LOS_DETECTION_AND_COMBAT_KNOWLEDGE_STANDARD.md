# THE GAME — LOS, Detection & Combat Knowledge Standard

Status: **APPROVED FIRST-PASS CONTRACT / PRIVACY-CRITICAL**
Parents:
- docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md
- docs/systems/TACTICAL_COORDINATE_OCCUPANCY_STANDARD.md
- docs/systems/CAMERA_AND_TACTICAL_PRESENTATION_STANDARD.md
Related current runtime:
- src/textrpg/social.py
- src/textrpg/core.py
- src/textrpg/android_bridge.py

## 1. Purpose

Separate geometric visibility from awareness and knowledge so combat cannot leak hidden actors, intentions, weaknesses, or secret state.

## 2. Distinct concepts

The engine treats these separately:
1. geometric LOS;
2. detection/awareness;
3. tracking/last-known position;
4. knowledge about identity/abilities/faction/weakness/history.

Geometric LOS alone does not grant full detection or identity.

## 3. LOS algorithm

Phase 1 uses deterministic cell-center supercover tracing.

The ray enumerates every crossed cell/edge in stable order and stops at opaque blockers.

Supercover is required to prevent vision/shots slipping through touching corners that visually appear closed.

Golden corner-case tests are mandatory.

## 4. LOS blockers

Possible blockers:
- opaque wall edge;
- opaque terrain cell;
- closed door;
- dense obstruction;
- smoke/darkness only when the effect explicitly blocks/attenuates LOS.

Movement blocking does not automatically imply LOS blocking.

### 4.1 Opaque directional edge representation

Phase 1 authored/canonical cells use `los_blocked_edges` for opaque N/E/S/W boundaries.

A shared boundary is blocked when either adjacent cell declares that boundary:
- source cell declares the outgoing edge; **or**
- destination cell declares the opposite edge.

Example:
- A is immediately west of B;
- the A/B boundary is opaque if A has `E` in `los_blocked_edges` or B has `W`.

LOS queries must apply the same either-side rule in both ray directions, so one authored wall cannot become direction-dependent.

`cover` remains independent. Partial/strong cover does not block LOS unless the same boundary is explicitly present in `los_blocked_edges`.

## 5. Awareness states

Phase 1 enum:
- UNKNOWN;
- SUSPECTED;
- DETECTED;
- IDENTIFIED.

UNKNOWN: no projected contact.

SUSPECTED: evidence of presence/area, not exact identity.

DETECTED: exact current cell known, identity/details may remain limited.

IDENTIFIED: identity known; additional safe information depends on knowledge.

Awareness is observer-specific.

## 6. Detection checks

Possible inputs:
- Perception;
- Stealth;
- distance;
- illumination;
- concealment;
- movement/noise;
- conditions;
- sensory abilities;
- prior knowledge.

Phase 1 uses deterministic contest variance keyed by combat event identity.

Detection never reveals private NPC goals or secret stats by itself.

## 7. Last-known position

When detection is lost:
- store last_known_coord;
- store round last seen;
- decay may later move to SUSPECTED/UNKNOWN.

Phase 1 may retain last-known position for the encounter unless a concealment effect clears it.

UI must distinguish stale location from current detection.

## 8. Knowledge integration

Current GameState already has player knowledge and per-NPC knowledge.

Combat consumes those authorities rather than creating a parallel lore database.

Prior investigation may reveal identity, armor class, observed technique, or weakness only if legitimately known.

## 9. Intent secrecy

Enemy AI scores, future actions, hidden goals, and private morale are not player-facing.

If an ability reads intent, the engine projects an intentional summary; Compose never derives it from AI internals.

## 10. Targeting relationship

Actions may specify:
- requires_los;
- requires_detection;
- requires_identification;
- allows_last_known_position;
- allows_blind_area_targeting.

Legality checks exactly the declared requirements.

## 11. Projection contract

Player-safe combat view may include visible cells, detected actors, identification level, known last positions, known cover/hazards, known objectives, and known enemy facts.

Hidden actors must not leak through initiative lists, occupancy, target lists, path previews, logs, or accessibility text.

## 12. Tests

Required:
- straight LOS;
- opaque edge block;
- corner supercover block;
- movement-vs-LOS blocker separation;
- awareness per observer;
- last-known transition;
- hidden actor redaction;
- unidentified contact;
- knowledge-driven detail unlock;
- AI intent redaction;
- blind-area legality;
- deterministic detection contest.

## 13. Invariant

Every player-facing combat payload must come from explicit player-safe projection. UI must not receive raw encounter internals and merely promise not to display them.
