# Decision Gap Register

Status: ACTIVE
Purpose: prevent proposals from silently turning into canon.

## Priority gaps

| ID | Area | Gap | Current status |
|---|---|---|---|
| GAP-001 | Gate Twelve | Step 5 geometry contract is persisted in the Master Plan | CLOSED — documented 2026-10-02 |
| GAP-002 | Repository governance | old README/status pointers still describe earlier canonical branches/objectives | OPEN |
| GAP-003 | World | hierarchy/coordinate-space contract documented; final WORLD_GEO representation and actual geography remain undecided | PARTIALLY SPECIFIED |
| GAP-004 | World | Depot Plaza external world destination unknown | OPEN |
| GAP-005 | World | Quiet Stair external destination unknown | OPEN |
| GAP-006 | World | Service Tunnel deeper destination unknown | OPEN |
| GAP-007 | Map | Plaza <-> Platform Nine connector not implemented in authored graph | OPEN |
| GAP-008 | Art | contextual character/room panel contract | SPECIFIED — implementation pending |
| GAP-009 | Art | reusable overlay/occlusion rules | REVIEWABLE — global reuse/occlusion matrix documented; implementation-specific bindings remain |
| GAP-010 | Characters | scene-presence projection ownership/shape | SPECIFIED — exact implementation pending |
| GAP-011 | Society | citizen classes/hierarchy not designed | OPEN |
| GAP-012 | Society | fictional prejudice/discrimination rules not designed | OPEN |
| GAP-013 | Progression | class/specialization architecture documented; class catalog, exact entry rules, respec and counts remain | REVIEWABLE ARCHITECTURE |
| GAP-014 | Progression | rank namespaces documented; exact scales/caps remain undecided | REVIEWABLE ARCHITECTURE |
| GAP-015 | Combat | tactical combat architecture documented; position, turn order, formulas, AI and exact action economy remain | REVIEWABLE ARCHITECTURE |
| GAP-016 | Combat | persistent adversary architecture documented; eligibility, adaptation catalog, recurrence and removal rules remain | REVIEWABLE ARCHITECTURE |
| GAP-017 | Balance | world-anchored balance philosophy documented; numeric bands, caps, curves and difficulty parameters remain | REVIEWABLE ARCHITECTURE |
| GAP-018 | Economy | final currency/economy model not decided | OPEN |
| GAP-019 | Economy | crafting/repair adoption not decided | OPEN |
| GAP-020 | Ecology | beast/entity standard plus beast-zone/ecosystem schema documented; actual species/zones and simulation depth remain | REVIEWABLE SCHEMA — content pending |
| GAP-021 | Android | full current-component keep/replace/retire audit not complete | OPEN |
| GAP-022 | Android | final APK rebuild matrix not created | OPEN |
| GAP-023 | Documentation | full cross-document machine-readable index not created | OPEN |
| GAP-024 | Governance | priority repository decision not yet propagated to every stale report/pointer | OPEN |

## Closure rule

A gap closes only when:
- a decision is written;
- conflicts are reconciled/superseded;
- downstream documents are updated;
- implementation-required gaps include acceptance/verification criteria.

A chat statement alone does not close a repository gap.


## Gate Twelve master-plan status — 2026-10-02

Steps 1–14 are now documented in `docs/assets/GATE_TWELVE_REGION_MASTER_PLAN.md`.

The first implementation task is `GT-IMP-001`: player-safe scene-presence projection.

This does not close broader world/system gaps. Gate Twelve is the documentation pilot, not the completed world.
