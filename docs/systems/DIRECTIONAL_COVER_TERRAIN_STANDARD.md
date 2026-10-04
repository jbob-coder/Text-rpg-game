# THE GAME — Directional Cover & Tactical Terrain Standard

Status: **APPROVED FIRST-PASS CONTRACT / PHASE 1 NUMERIC DEFAULTS**
Parents:
- docs/systems/TACTICAL_COMBAT_MASTER_PLAN.md
- docs/systems/TACTICAL_COORDINATE_OCCUPANCY_STANDARD.md
- docs/systems/LOS_DETECTION_AND_COMBAT_KNOWLEDGE_STANDARD.md

## 1. Purpose

Define cover as directional edge data and define terrain properties shared by movement, LOS, attacks, AI, and UI.

## 2. Cover representation

Each cell can define cover on N/E/S/W incoming edges.

Phase 1 rating:
- 0 = none;
- 1 = partial;
- 2 = strong.

Cover is separate from LOS blocking.

## 3. Which edge protects

Trace the attack ray into the target cell. The boundary edge through which the ray first enters the target cell determines directional cover.

This works for diagonal attack angles even though movement is cardinal.

Corner ambiguity follows the deterministic supercover tie rule.

## 4. Phase 1 cover modifiers

Initial tuning:
- no cover: +0 defense;
- partial cover: +10 defense;
- strong cover: +20 defense.

These are attack-contest defense modifiers, not armor.

## 5. Flanking

No separate hidden flanking bonus in Phase 1.

If the incoming edge has no cover, the target gets no cover modifier even if other edges are protected. That lost protection is the flanking benefit.

## 6. Terrain record

Cell fields may include:
- terrain_id;
- movement_cost;
- blocks_movement;
- blocks_los;
- concealment;
- cover edges;
- hazard_ids;
- elevation;
- tags.

Tags do nothing until a rule consumes them.

## 7. Concealment versus cover

Cover is physical protection/target difficulty.

Concealment affects detection/clarity.

Smoke may conceal without physically protecting.

## 8. Elevation

Phase 1 supports z layers structurally but has no universal high-ground bonus.

Elevation effects must be explicit. Until then, elevation mainly changes topology and LOS.

## 9. Hazards

Hazard definitions own trigger, effect, visibility, duration, immunity tags, and forced-movement behavior.

Terrain references hazard IDs rather than duplicating logic.

## 10. Destructibility

Not required for Phase 1.

If later added, destruction changes authoritative movement/LOS/cover state before visuals.

## 11. AI use

AI scores cover only if it knows the relevant terrain/threat and can legally reach the destination.

No hidden-player-position cheating.

## 12. Android projection

UI may render cover class, movement cost, known hazards, and blocked LOS.

Prefer semantic values none/partial/strong unless final UX chooses exact numbers.

## 13. Tests

Required:
- incoming-edge selection;
- +0/+10/+20 modifiers;
- no double flank bonus;
- cover vs LOS blocker;
- diagonal corner determinism;
- concealment without cover;
- hazard ownership;
- AI hidden-threat redaction.
