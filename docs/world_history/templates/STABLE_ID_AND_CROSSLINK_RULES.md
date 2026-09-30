# STABLE_ID_AND_CROSSLINK_RULES

Status: ACTIVE_ARCHITECTURE_STANDARD
Authority: PHASE_01

## 1. Stable-ID rule

Once a stable ID is promoted, its meaning is immutable.

It may be:
- ACTIVE;
- DEPRECATED;
- SUPERSEDED;
- RETIRED;

but never reassigned to a different concept.

## 2. Canonical entity prefixes

Approved families:
- ERA_*
- EVENT_*
- WAR_*
- SPECIES_*
- ECOSYSTEM_*
- HUMAN_LINEAGE_*
- ABILITY_*
- CREATURE_*
- CRYSTAL_*
- PORTAL_*
- ORG_*
- FACTION_*
- LAW_*
- TECH_*
- CITY_*
- REGION_*
- WORLD_*
- PERSON_*
- SECRET_*
- DISCOVERY_*
- TIMELINE_*
- STATUS_*
- INSTITUTION_*
- DISEASE_*
- PROFESSION_*
- RESOURCE_*

New prefixes require an index update.

## 3. Era normalization

Canonical era records use the numbered/date-bounded form when available, for example:
- ERA_030_EARLY_CRYSTAL_2473_2505
- ERA_040_CRYSTAL_INDUSTRIALIZATION_2506_2558
- ERA_050_PORTAL_EXPANSION_2559_2605

Short forms such as:
- ERA_EARLY_CRYSTAL_2473
- ERA_CRYSTAL_INDUSTRIALIZATION
- ERA_PORTAL_EXPANSION

are aliases only unless a separate parent-era record is explicitly created.

Aliases must be written as:
`Alias: Portal Expansion`
or
`Legacy alias: ERA_PORTAL_EXPANSION`

Do not silently create two canonical records for one era.

## 4. Authority labels

Authority text must not masquerade as a stable entity ID.

Bad:
`SPECIES_HOMUNCULUS_001_PLUS_USER_AUTHORIZED_CONNECTIVE_DESIGN`

Good:
`Authority: SPECIES_HOMUNCULUS_001 + USER_AUTHORIZED_CONNECTIVE_DESIGN`

## 5. Supersession

When canon changes:
- retain old file/ID for provenance when useful;
- mark `Status: SUPERSEDED`;
- name the replacing file/ID;
- explain exactly which claims no longer apply;
- do not reuse the old ID.

## 6. Cross-link format

Use both stable ID and repository path when a relationship is important.

Example:
`EVENT_VEINFALL_2473 — docs/world_history/events/EVENT_VEINFALL_2473.md`

For lightweight mentions, stable ID alone is acceptable if the owning index resolves it.

## 7. Reference ownership

One technical concept should have one owning record.

Other files may summarize it but should not independently redefine it.

Examples:
- creature biology owned by creature record;
- war date/campaign registry owned by war record;
- law definition owned by law record;
- narrative experience owned by history chapter.

## 8. Knowledge-layer metadata

Reference entries should state one or more:
- PUBLIC
- RESTRICTED
- CLASSIFIED
- TRUE
- PROTAGONIST_MYSTERY
- UNKNOWN

TRUE is author-world truth, not automatic character knowledge.

## 9. Homunculus freeze rule

Until PHASE 07:
- `SPECIES_HOMUNCULUS_001` retains provenance but is not extended;
- future hostile secret-society design must use a new `FACTION_HOMUNCULUS_*` ID;
- old Homunculus rebellion/custodial IDs must not be silently redefined.

## 10. Validation checklist

Before creating a new ID:
1. search indexes and owning volume;
2. confirm concept does not already exist;
3. confirm prefix;
4. confirm date/region if needed;
5. assign owning file;
6. record aliases separately;
7. add cross-links;
8. never infer protagonist secrets to complete an entry.
