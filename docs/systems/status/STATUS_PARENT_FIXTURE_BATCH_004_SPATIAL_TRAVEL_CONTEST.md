# THE GAME — Parent Fixture Batch 004: Spatial Judgment, Equipment Retention & Travel Efficiency

Status: **PHASE-C NUMERIC PREPARATION / QUALITATIVE PARENT FIXTURES / NO FINAL VALUES / NOT CANON / NOT IMPLEMENTED**

Parents:
- `PASSIVE_CANONICAL_RESOLVER_PARENT_FIXTURE_REQUIREMENTS_WAVE_001.md`
- `PASSIVE_CANONICAL_RESOLVER_SCENARIO_ANCHORS_WAVE_001.md`
- `SPATIAL_REFERENCE_FRAME_AND_TRANSIT_STANDARD.md`
- `STATUS_BASE_RESOLUTION_TERM_UNIT_TAXONOMY.md`
- `STATUS_NUMERIC_CALIBRATION_FRAMEWORK.md`

Scope:
- `RESOLVER_ENGAGEMENT_DISTANCE_JUDGMENT`;
- `RESOLVER_EQUIPMENT_RETENTION`;
- `RESOLVER_TRAVEL_EFFICIENCY`.

Purpose: define qualitative parent fixtures for spatial judgment, physical retention contests, and route/travel efficiency without inventing a world-meter scale, contest score, or travel formula.

# Part A — Engagement distance judgment

## 1. FIX_RANGE_001 — Clear stationary target

Preconditions:
- target is legitimately observed;
- target and user positions are valid;
- equipment/body reach profile is known enough to use.

Expectation:
- parent system can produce a spacing/range judgment;
- passive may reduce judgment error;
- actual geometry remains authoritative.

Current readiness after this batch:
`QUALITATIVE_FIXTURES_READY`.

## 2. FIX_RANGE_002 — Moving target

Expectation:
- judgment can become harder as target position changes;
- action commit revalidates current geometry;
- passive cannot freeze or predict target movement.

## 3. FIX_RANGE_003 — Unfamiliar reach profile

Preconditions:
- target/equipment is visible;
- reach behavior is not well learned.

Expectation:
- judgment may carry larger error/uncertainty;
- equipment-familiarity knowledge can matter separately;
- passive cannot invent exact hidden reach.

## 4. FIX_RANGE_004 — Elevation/terrain complication

Expectation:
- slope, elevation, obstruction, and path geometry may alter practical spacing;
- simple screen/map distance cannot silently replace physical geometry.

## 5. FIX_RANGE_005 — Out-of-reach boundary

Preconditions:
- actual current physical geometry places target beyond valid reach.

Expectation:
- better judgment can correctly identify the problem;
- passive cannot extend physical reach.

## 6. FIX_RANGE_006 — Unobserved target boundary

Expectation:
- no range judgment is produced from hidden truth alone;
- target must be legitimately observed through an authorized information source.

# Part B — Equipment retention

## 7. FIX_RET_001 — Ordinary contested hold

Preconditions:
- user legitimately holds/controls equipment;
- another force/action contests retention.

Expectation:
- one retention contest or deterministic equivalent resolves;
- passive contributes at most through the canonical retention modifier;
- success is not guaranteed.

Current readiness after this batch:
`QUALITATIVE_FIXTURES_READY`.

## 8. FIX_RET_002 — Stable favorable hold

Preconditions:
- familiar equipment;
- good stance/grip;
- ordinary body condition.

Required relationship:
retention outcome/modifier should be no worse than a matched adverse leverage case before random/contest resolution.

No numeric bonus is assigned.

## 9. FIX_RET_003 — Awkward leverage / poor footing

Expectation:
- parent system can represent reduced retention circumstances;
- passive does not erase footing, leverage, or body-state consequences.

## 10. FIX_RET_004 — Fatigue/injury interaction

Expectation:
- fatigue/injury remains independently authoritative;
- passive cannot make damaged/disabled grip fully normal by itself.

## 11. FIX_RET_005 — Equipment failure boundary

Preconditions:
- equipment/strap/handle physically fails.

Expectation:
- retention modifier cannot restore destroyed hardware;
- equipment condition is resolved separately.

## 12. FIX_RET_006 — Overwhelming contest

Expectation:
- sufficiently unfavorable physical contest can still defeat retention;
- no absolute disarm immunity.

## 13. FIX_RET_007 — One contest, one finalization

If Shield Habit and Weapon Retention both qualify for the same held-item contest:
- both eligibility checks occur;
- modifiers compose through one canonical resolver;
- the contest is finalized once.

# Part C — Travel efficiency

## 14. FIX_TRAVEL_001 — Ordinary traversable route

Preconditions:
- route exists;
- route is legally/physically traversable;
- origin/destination are valid.

Expectation:
- parent system produces travel time/cost/pace according to route state;
- passive can reduce only avoidable inefficiency.

Current readiness after this batch:
`QUALITATIVE_FIXTURES_READY`.

## 15. FIX_TRAVEL_002 — Familiar route

Expectation:
- route familiarity may reduce avoidable navigation/pace inefficiency;
- actual route length and mandatory traversal remain.

## 16. FIX_TRAVEL_003 — Rough terrain

Expectation:
- terrain can increase parent travel burden;
- passive may reduce eligible inefficiency but not make impassable terrain passable.

## 17. FIX_TRAVEL_004 — Load/fatigue

Expectation:
- carried load and fatigue can affect travel through parent systems;
- travel-efficiency passive does not erase carry/fatigue authority.

## 18. FIX_TRAVEL_005 — Blocked route boundary

Expectation:
- blocked/locked/unreachable route cannot be traversed solely through efficiency;
- discovery/access authority resolves first.

## 19. FIX_TRAVEL_006 — Gate Twelve authored-route regression

Current Gate Twelve evidence includes authored route edges and some minute costs.

Required rule:
- those route minutes are valid content-specific travel evidence where authored;
- Gate Twelve node coordinates remain presentation/map values;
- neither is silently converted into universal meters or a global pace formula.

A future range fixture may use existing authored route minutes as regression cases only after the parent travel model defines what they mean.

## 20. FIX_TRAVEL_007 — Save/load route transaction

Expectation:
- committed travel cost/time is not applied twice;
- route arrival is not duplicated;
- interrupted travel behavior follows parent travel rules.

## 21. Cross-system order

A travel/action situation may involve:
1. route/access validity;
2. observed geometry/range;
3. movement/travel cost;
4. equipment/body state;
5. action/contest resolution.

Passives modify authorized terms only.

## 22. Range blockers

Before these resolvers become `RANGE_FIXTURES_READY`, define:
- authoritative world distance unit or deterministic geometry equivalent;
- equipment/body reach taxonomy;
- contest scale/equivalent;
- travel time/cost representation;
- terrain/load/fatigue contributions;
- route access/interrupt semantics.

## 23. Acceptance

This batch establishes qualitative parent fixtures for **3 canonical resolver families**.

No meters, contest points, travel percentages, or canon promotions are established.
