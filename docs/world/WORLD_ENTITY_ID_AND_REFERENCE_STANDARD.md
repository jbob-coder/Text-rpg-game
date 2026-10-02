# World Entity ID and Reference Standard

Status: DOCUMENTED / GLOBAL FOUNDATION

## Purpose

Prevent cities, regions, NPCs, routes, resources, beasts and other world entities from being renamed/reused inconsistently as the documentation corpus expands.

## Stable-ID principle

A stable ID represents one semantic identity for its lifetime.

Never reuse an old ID for a different entity.

Names displayed to players may change without changing the stable ID when identity is unchanged.

## Recommended prefixes

These are documentation conventions; existing IDs are not renamed merely to match them.

- `WORLD_`
- `POLITY_`
- `REGION_`
- `SETTLEMENT_`
- `DISTRICT_`
- `LOCATION_` when a more specific existing ID does not already exist
- `ROUTE_`
- `FACTION_`
- `NPC_`
- `BEAST_`
- `ECOSYSTEM_`
- `RESOURCE_`
- `ITEM_`
- `ABILITY_`
- `CLASS_`
- `RANK_`
- `QUEST_`
- `EVENT_`

Existing stable IDs such as `PLATFORM_NINE` remain valid.

## Reference record

Every major world entity document should state:
- stable ID;
- display name;
- entity type;
- authority status;
- parent entity;
- child entities;
- connected routes;
- relevant systems;
- source documents;
- implemented files if any;
- unresolved gaps;
- superseded IDs/names if any.

## Cross-reference rule

Documents refer to stable IDs, not only prose names.

Example:
`DISTRICT_GATE_TWELVE -> contains -> PLATFORM_NINE`

A future graph index can derive relationships such as:
- Region -> contains -> Settlement
- Route -> connects -> Location
- NPC -> belongs_to -> Faction
- ResourceZone -> yields -> Resource
- Test -> verifies -> Behavior

## Rename rule

Rename display text freely when needed.

Rename stable IDs only if:
- identity was incorrectly modeled;
- migration is documented;
- all consumers are updated;
- saves/content references are handled.

## Merge/split rule

When two entities merge or one splits:
- never silently repurpose IDs;
- create new IDs where identity changes;
- mark old records SUPERSEDED;
- retain historical mapping.

## Locked decisions

1. Stable IDs are semantic identities, not filenames.
2. Existing valid IDs survive future documentation restructuring.
3. Cross-doc references should use IDs.
4. Merge/split history is preserved.
