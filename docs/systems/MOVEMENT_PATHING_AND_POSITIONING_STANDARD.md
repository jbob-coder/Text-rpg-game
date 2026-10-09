# THE GAME — Tactical Movement, Pathing & Positioning Standard

Status: **APPROVED FIRST-PASS CONTRACT / PHASE 1 DEFAULTS LOCKED / D-069 GRID + D-070 MOVEMENT SLICE VERIFIED**
Parents:
- docs/systems/TACTICAL_COORDINATE_OCCUPANCY_STANDARD.md
- docs/systems/TURN_INITIATIVE_ACTION_BUDGET_STANDARD.md

## 1. Purpose

Define movement points, terrain cost, path preview/commit, movement interruption, forced movement, and positioning rules.

### Current bounded runtime checkpoint

Verified implementation now covers the Phase 1 movement substrate without claiming every future movement rule:
- D-069: cardinal occupancy/traversability, deterministic pathfinding, explicit z transitions and transition-aware optimal pathing;
- D-070: committed movement/sprint transactions, action-budget enforcement, rollback, reinforcement/round interaction and deterministic event/transcript behavior;
- D-071: movement commits that integrate observer-specific detection/objective updates under the same rollback boundary.

Evidence: `docs/evidence/D069_TACTICAL_SCHEMA_GRID_CORE_FINAL_2026-10-05.md`, `docs/evidence/D070_TRANSIENT_ENGINE_2026-10-08.md`, and `docs/evidence/D071_TACTICAL_DECISIONS_2026-10-08.md`.

This checkpoint does not claim the D-073 authored encounter/bridge, D-074 Android tactical surface, final terrain balance, or future special movement abilities.

## 2. Phase 1 movement allowance

Default Move:
- action-budget cost: 1;
- movement points: 6.

Default Sprint:
- action-budget cost: 2;
- movement points: 10;
- cannot reserve a new reaction later in the same activation unless an ability explicitly overrides this.

These are tuning constants.

## 3. Terrain costs

Phase 1:
- normal traversable cell: 1;
- difficult terrain: 2;
- severe terrain: 3 when authored;
- blocked: impassable;
- climb/vertical transition: authored cost, minimum 1.

Cost is paid when entering the destination cell/edge.

## 4. Path legality

Every step must be a valid edge, traversable for the actor, within remaining movement points, legal for occupancy, and inside encounter restrictions.

No client-side route may bypass engine legality.

## 5. Occupancy

Phase 1:
- enemy cell: cannot enter/pass;
- ally cell: may pass if policy allows, cannot end;
- incapacitated body: default non-blocking unless encounter says otherwise;
- props: authored blocking metadata.

Destination is revalidated immediately before commit.

## 6. Movement interruption

Movement may be interrupted by reactions, hazards, objective triggers, incapacitation, topology changes, or encounter resolution.

If interrupted after movement begins:
- traversed steps remain;
- remaining movement points from that action are lost unless a rule says otherwise;
- actor remains at last committed cell;
- action-budget cost remains spent.

If validation fails before the first step, no cost is spent.

## 7. Stepwise events

Recommended:
- MOVE_STARTED;
- MOVE_STEP;
- reaction/trigger events;
- MOVE_INTERRUPTED or MOVE_COMPLETED.

One Move action may contain many step events.

## 8. Zones of control

No universal zone-of-control system is required for Phase 1. Threatened movement should initially come from explicit reaction definitions.

## 9. Forced movement

Push/pull/knockback/drag:
- source defines direction/distance;
- each step revalidates;
- target spends no action budget;
- hazards may trigger;
- reaction behavior is action-defined;
- movement stops at first blocked step;
- collision damage is not automatic unless defined.

## 10. Swaps and teleports

No generic swap in Phase 1.

Teleport/reposition requires explicit action, legal destination, and occupancy validation. It may ignore intermediate path edges if its definition says so.

## 11. Facing

Move may update facing to final movement direction.

Facing is rules state, not animation state. No separate rotate cost in Phase 1.

## 12. Player-safe preview

UI may show reachable cells, path, cost, known hazards/cover, and visible occupancy.

Hidden units must not be leaked through impossible-looking holes in a preview. Safe policy can stop movement on attempted contact rather than expose the unseen blocker.

## 13. AI

AI uses the same path query and cannot use hidden-information routes.

## 14. Tests

Required:
- 6-point Move;
- 10-point Sprint;
- terrain costs;
- no diagonal;
- ally/enemy occupancy;
- interruption;
- forced-movement stop;
- equal-cost deterministic route;
- hidden blocker safety;
- vertical edge;
- no out-of-bounds displacement.

## 15. Target interfaces

Pure/query functions should include neighbors, path_cost, find_path, reachable_cells, and validate_move_action. Query functions do not mutate encounter state.
