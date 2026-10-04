# THE GAME — Relationship Axis & State Standard

Status: **APPROVED FIRST-PASS CONTRACT / V05**
Parents:
- docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md
Current runtime:
- src/textrpg/social.py

## 1. Purpose

Define persistent player-to-NPC relationship state as independent dimensions rather than one approval score.

## 2. Current axes

Current social.py authority:
- trust;
- respect;
- affection;
- fear;
- suspicion;
- debt;
- loyalty.

The first-pass target preserves these seven axes.

The master plan mentioned hostility/rivalry as possibilities, but they are not current runtime axes and are not added here. Rivalry belongs to V09 unless a later migration says otherwise.

## 3. Range

Current adjust_relationship clamps each axis to:
- minimum -100;
- maximum +100.

Zero is neutral/default.

## 4. Independent dimensions

Valid combinations include:
- high respect + low trust;
- high affection + high suspicion;
- fear without loyalty;
- debt without affection.

Do not replace these axes with one hidden relationship level.

## 5. Change ownership

Relationship changes are authoritative domain events.

A change should identify:
- NPC;
- affected axes;
- before/after;
- source event;
- turn/time.

Current adjust_relationship already performs atomic multi-axis updates and appends history.

## 6. Gates

Use explicit minimum/maximum axes.

Examples already present in current content:
- trust >= 10;
- suspicion <= 40.

## 7. No arbitrary reward

Do not grant relationship points merely because a quest completed or combat was won.

The event must explain why a specific axis changes.

## 8. NPC-to-NPC graph

Current durable top-level relationship state is player-to-NPC oriented.

A full NPC-to-NPC social graph is a future extension and must not be faked inside player relationship records.

## 9. Visibility

Exact numeric axes are not automatically player-facing.

UI may later show qualitative bands, exact values, or no direct score. That choice does not alter authority.

## 10. Phase 1

Tamsin already has multiple initial dimensions and current content changes trust/suspicion based on specific choices.

Phase 1 proof must show at least two axes changing later behavior or available choices.

## 11. Tests

Required:
- clamp boundaries;
- atomic multi-axis change;
- invalid axis rejection;
- min/max gates;
- save/load;
- history event;
- two-axis Phase 1 consequence;
- redaction when exact values are not exposed.
