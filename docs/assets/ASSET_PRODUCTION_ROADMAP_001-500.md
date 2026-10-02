# THE GAME — Pixel Asset Production Roadmap v1 (001–500)

## Global program pointer

This 001–500 roadmap is a child plan of `docs/MASTER_DOCUMENTATION_PROGRAM.md`. Asset production must follow `docs/PIXEL_ART_INTEGRATION_AND_REUSE_STANDARD.md` and the repository priority rules in `docs/PROJECT_PRIORITY_AND_CONTEXT_ROUTING.md`.


## Scope

This roadmap defines the complete **v1 production baseline** before bulk visual generation begins.

It does **not** claim that every future named NPC, quest, region, enemy, item or story beat is known today. Instead, it plans every reusable visual family required by the current architecture and supplies non-canon expansion templates so future authored content can plug into the same system without redesigning the pipeline.

## Five exact 100-unit batches

| Batch | IDs | Purpose | Canon boundary |
| --- | --- | --- | --- |
| 001 | 001–100 | Current playable slice: player, Tamsin, current items, nine current locations, map/UI, Trace FX | Grounded in current provisional canon + technical UI |
| 002 | 101–200 | Character/NPC production framework, customization, animation, portrait/emotion/social staging | Mostly technical/non-canon templates except current player/Tamsin dependencies |
| 003 | 201–300 | Equipment, weapons/tools, inventory objects, consumables/materials, loot/crafting presentation | Technical/non-canon templates until a stable item ID is authored |
| 004 | 301–400 | World/building/interior modules, props, environment states, travel/map infrastructure | Technical/non-canon templates; named current locations inherit Batch 001 |
| 005 | 401–500 | UI/HUD, combat/interaction feedback, ability/status FX, transitions, accessibility/debug presentation | Technical system assets; ability-specific art requires authored ability IDs |

Total planned units: **500**.

## Production meaning of “planned 100%”

Planning is complete when all 500 units have:

- a stable production ID;
- native source size/family;
- intended system/screen use;
- dependency/ownership notes;
- canon or technical/non-canon classification;
- reference-to-blueprint expectations;
- integration target;
- QA/visibility rules.

Planning does **not** mean all 500 must be produced before the first usable asset enters the game. Production is dependency-driven after the plan is complete.

## Generation rule

Generated imagery remains reference-only.

No asset can skip:

`BRIEF_LOCKED -> REFERENCE_GENERATED -> REFERENCE_SELECTED -> BLUEPRINTED -> PIXEL_MASTER_BUILT -> INTEGRATED -> VERIFIED`

## Canon protection

Future-framework entries use generic archetype/system IDs such as `NPC_ARCHETYPE_MEDIC_BASE` or `PROP_GENERIC_SERVICE_DOOR_A`.

Those IDs are not story canon. When authored content later defines a stable character/item/location, the production asset should either:

1. inherit the template; or
2. receive a new stable content-bound asset ID.

Do not silently promote a template into a named story entity.

## Dependency order after planning

1. Character rig + first paper-doll equipment pair.
2. Tamsin canonical identity.
3. Current-location replacement scenes.
4. Current inventory/item visuals.
5. UI icon replacement.
6. Ability FX.
7. Reusable NPC archetype system.
8. World modules.
9. Generic equipment/item library.
10. Extended animation/combat/interaction library.
11. Accessibility/debug polish.
12. Future authored content inheritance.

## Mobile budget strategy

The game targets modest Android hardware. Pixel art helps only if packaging/runtime choices remain disciplined.

Guidelines:

- keep native masters small;
- use atlases where runtime loading benefits;
- avoid shipping 1024px concept/reference boards inside the APK;
- references live outside production assets;
- reuse modular location layers;
- reuse character rig/equipment layers;
- load scene/state overlays only as needed;
- prefer lossless PNG for small alpha sprites and indexed-color opportunities where tooling supports them;
- do not duplicate identical assets under multiple story-scene names.

## Completion condition for documentation phase

The documentation phase is complete only after Batch 001, 002, 003, 004 and 005 each validate to exactly 100 unique catalog units and the master roadmap links all five.

Bulk reference generation may begin only after that verification.
