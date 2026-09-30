# SCENARIO_QUERY_MODEL_V1_DRAFT

Status: DRAFT_REFERENCE_STANDARD
Authority: ROUNDS_097_099
Purpose: prevent arbitrary world content insertion

## Query keys

Required where applicable:
- YEAR
- ERA
- WORLD
- REGION
- BIOME
- SETTLEMENT_TYPE
- CREATURE_THREAT_RANGE
- SPECIES_ALLOWED
- FACTIONS_PRESENT
- TECHNOLOGY_LEVEL
- LEGAL_CONTEXT
- KNOWLEDGE_LAYER
- ACADEMY_RELEVANCE
- RARITY_LIMIT
- PORTAL_ACCESS
- ECOLOGICAL_STATE
- CURRENT_WORLD_PRESSURES

## Eligibility sequence

1. Historical availability.
2. Geographic availability.
3. Biome survival.
4. Ecological reason for presence.
5. Legal/political plausibility.
6. Technology compatibility.
7. Faction capability.
8. Knowledge compatibility.
9. Threat suitability.
10. Consequence plausibility.

## Example query

YEAR: 2670
REGION: human-controlled temperate frontier
BIOME: mixed forest
PLAYER_CONTEXT: Academy field exercise
THREAT: T1–T2
PORTAL_ACCESS: indirect
PUBLIC_KNOWLEDGE: normal
RARITY: common-to-uncommon

The query must return only entities whose records support all required constraints.

## Rejection reasons

Reject a candidate if:
- it did not exist yet;
- no route puts it in the region;
- biome is incompatible;
- rarity is too high for casual use;
- the faction lacks access;
- required technology does not exist;
- local law would radically alter the scene and that consequence is omitted;
- the threat exceeds available response without an explicit escalation reason;
- using it would expose TRUE/CLASSIFIED knowledge that characters do not possess.

## Causality check

For every inserted event/entity answer:
- Why here?
- Why now?
- How did it arrive?
- What sustains it?
- Who knows?
- Who benefits?
- What responds?
- What changes afterward?

If those cannot be answered, the insertion is not ready.
