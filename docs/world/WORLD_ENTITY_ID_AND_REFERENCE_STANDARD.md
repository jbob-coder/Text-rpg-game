# World Entity ID and Reference Standard

Status: **ACTIVE FOUNDATION / CHILD OF WORLD MASTER**  
Parent: `docs/world/WORLD_DEVELOPMENT_MASTER_INDEX.md`

## 1. Purpose

Prevent places, routes, NPCs, factions, beasts, ecosystems, resources, items and other durable world entities from being silently renamed, reused or merged as the corpus expands.

## 2. Stable-ID principle

A stable ID represents one semantic identity for its lifetime.

Never reuse an old ID for a different entity.

Player-facing display names may change without changing the stable ID when semantic identity is unchanged.

Existing valid IDs such as `PLATFORM_NINE` remain valid; this standard does not force mass renaming.

## 3. Recommended prefixes for new IDs

When a domain has no established stronger convention, use explicit namespaces such as:
`WORLD_`, `POLITY_`, `REGION_`, `SETTLEMENT_`, `DISTRICT_`, `LOCATION_`, `ROUTE_`, `FACTION_`, `NPC_`, `BEAST_`, `ECOSYSTEM_`, `RESOURCE_`, `ITEM_`, `ABILITY_`, `CLASS_`, `RANK_`, `QUEST_`, `EVENT_`.

These are conventions, not migration commands.

## 4. Reference record

A major entity record should state:
stable ID; display name; entity type; authority state; parent; children; connected routes; relevant systems; source documents; implementation files when present; unresolved gaps; superseded IDs/names if any.

## 5. Cross-reference rule

Cross-document relations should use stable IDs, not prose names alone.

Examples:
- Region -> contains -> Settlement
- Route -> connects -> Location
- NPC -> belongs_to -> Faction
- Resource zone -> yields -> Resource
- Test -> verifies -> Behavior

## 6. Rename

Rename display text freely when identity stays the same.

Rename a stable ID only when identity was incorrectly modeled and all of the following are documented:
consumer inventory; old->new mapping; save/content migration; cross-reference update; verification; rollback/history.

## 7. Merge/split

Never silently repurpose an ID during merge/split.

If identities change:
- create new IDs;
- mark prior records superseded;
- preserve old->new history;
- migrate consumers explicitly.

## 8. Acceptance

A world/entity catalog is not reconstruction-grade if stable IDs can be silently reused or if references depend only on mutable display names.
