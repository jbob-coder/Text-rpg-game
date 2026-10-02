# Documentation Coverage and Expectation Matrix

Status: **ACTIVE / QA INDEX**
Last audit: 2026-10-02

## Purpose

Track whether the documentation program is meeting its intended depth and identify where documentation exists only as architecture versus implementation-ready specification.

This matrix does not measure progress by file count alone.

## Quality legend

- `DRAFT` — incomplete structure.
- `STRUCTURED` — required areas identified; major decisions remain.
- `REVIEWABLE` — authority/current/target/gaps/dependencies are clear.
- `IMPLEMENTATION_READY` — scoped implementation can proceed without material guessing.
- `VERIFIED_IMPLEMENTATION` — matching observed implementation evidence exists.

## Current coverage

| Domain | Primary documents | Current quality | Main remaining expectation |
|---|---|---|---|
| Program governance | 00–12 program docs, task register, AGENTS, README | REVIEWABLE | machine-readable global cross-doc index |
| Gate Twelve | Gate Twelve Region Master Plan + map/asset blueprints | IMPLEMENTATION_READY for documented pilot slices | implementation evidence for GT-IMP tasks |
| Contextual visual composition | document 11 | REVIEWABLE | include beasts, then implement scene-presence projection |
| Pixel art/assets/UI | program 03 + Visual Bible + asset master plan | REVIEWABLE | global reuse/occlusion matrix and remaining asset family specs |
| World hierarchy/maps | world spatial/ID/template/sequence docs | REVIEWABLE | actual world geography, WORLD_GEO decision, polities/regions |
| Characters/NPC/social | program 04 + foundation/social docs | STRUCTURED | NPC v2 schema, autonomy, hierarchy, social systems |
| Beasts/ecosystem | program 06 + beast standard | STRUCTURED | final taxonomy, ecosystem schema, beast-zone schema, actual species/zones |
| Progression/classes/ranks | program 05 + foundation | STRUCTURED | final class/rank/skill-tree architecture |
| Tactical combat | program 05 | STRUCTURED | original action economy, terrain, AI, encounter and UI rules |
| Persistent rivalry | program 05 | STRUCTURED | original persistent adversary schema/flow |
| Economy/items | program 06 + existing equipment foundation | STRUCTURED | currency/value, loot, resource, crafting/service decisions |
| World level/balance | program 05 | STRUCTURED | scaling philosophy, region threat, formulas/limits |
| Android/APK | program 07 + historical Android validation | REVIEWABLE architecture | current component keep/migrate/replace audit |
| Final teardown/rebuild | program 07 | STRUCTURED | final rebuild matrix waits on upstream design stability |
| Guides/process | program 08 + world templates | STRUCTURED | domain execution guides for each recurring content type |

## Gate Twelve audit result

Gate Twelve now satisfies the documentation expectation for:
- authority;
- spatial hierarchy;
- circulation;
- zone function;
- geometry;
- visual language;
- asset decomposition;
- UX ownership;
- state layers;
- performance strategy;
- implementation order;
- verification;
- migration;
- execution handoff.

Its implementation remains a separate phase.

## Known stale statement found during audit

`docs/program/01_DOCUMENTATION_PROGRAM_MASTER.md` previously stated that Gate Twelve only had Steps 1–4 and that Step 5 was not persisted.

That statement became stale after the later documentation batch and must be replaced with the current Steps 1–14 status.

## Beast expectation

All future scene-presence, ecosystem, combat, asset, map and resource documentation must account for **bestias** where relevant.

Do not treat beasts as merely NPCs and do not use generic “monster” terminology as the normative category.

## Next documentation depth priorities

1. synchronize stale program status statements;
2. expand scene presence to characters + beasts;
3. lock beast/ecosystem/beast-zone schemas;
4. create global asset reuse/occlusion matrix;
5. document actual world geography only when grounded by owner decisions;
6. deepen classes/ranks/skill-tree architecture;
7. define tactical combat;
8. define persistent adversary system;
9. define world scaling/balance;
10. audit current Android components against final-document expectations.
