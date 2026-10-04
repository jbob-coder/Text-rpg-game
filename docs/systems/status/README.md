# THE GAME — Status / Ability / Passive Documentation Index

Parent authority:
- `../STATUS_UI_ABILITIES_AND_PASSIVES_MASTER_PLAN.md`

This directory owns the reconstruction-grade child contracts for human Status UI, awakening, Level, primary abilities, passives, hidden requirements, knowledge visibility, catalog structure, UX, balance, and test mapping.

## Authority order

1. `../STATUS_UI_ABILITIES_AND_PASSIVES_MASTER_PLAN.md`
2. `STATUS_UI_CORE_CONTRACT.md`
3. rarity / registry / requirement / visibility standards
4. authoring guides and catalog indexes
5. individual catalog records and deep-authoring packets
6. cross-reference, UX, balance/test, implementation mappings
7. runtime tests/evidence

Runtime source remains the authority for what is implemented now. These documents own target-game design only where their status says so.

## Governing standards

- `STATUS_UI_CORE_CONTRACT.md`
- `ABILITY_RARITY_STANDARD.md`
- `PRIMARY_ABILITY_REGISTRY_SCHEMA.md`
- `PASSIVE_REGISTRY_SCHEMA.md`
- `PASSIVE_REQUIREMENT_LANGUAGE.md`
- `STATUS_KNOWLEDGE_VISIBILITY_STANDARD.md`
- `LEVEL_AND_XP_STANDARD.md`
- `AWAKENING_EVENT_STANDARD.md`
- `LEVEL_100_EXCEPTION_STANDARD.md`

## Authoring guides

- `ABILITY_CONTENT_AUTHORING_GUIDE.md`
- `PASSIVE_CONTENT_AUTHORING_GUIDE.md`

## Catalog execution

- `PRIMARY_ABILITY_CATALOG_INDEX.md`
- `PASSIVE_CATALOG_INDEX.md`
- `STATUS_CORPUS_EXECUTION_ROADMAP.md`
- `STATUS_CORPUS_REFINEMENT_QUEUE.md`
- `DOCUMENTATION_UNIT_LEDGER.md`
- `STATUS_CORPUS_WAVE_001_AUDIT.md`

Wave 001 currently contains **1,019 structurally verified stable-ID documentation units**.

This number is a structural milestone, not a claim that 1,019 records are final canon or complete implementation specifications.

## Current deep-authoring slices

- `calibration/PRIMARY_ABILITY_DETAIL_COMMON_001_010.md`
- `calibration/ABILITY_TECHNIQUE_DETAIL_COMMON_001_010.md`
- `calibration/PASSIVE_DETAIL_PHYSICAL_0001_0010.md`

The linked Common awakening/counter/technique table records have also begun individualized refinement.

## Integration / UX / QA contracts

- `ABILITY_PASSIVE_CROSS_REFERENCE.md`
- `STATUS_UI_UX_CONTRACT.md`
- `STATUS_BALANCE_AND_TEST_MATRIX.md`

## Scale rule

Do not put thousands of ability/passive records into one unstructured file.

Catalogs must remain:
- ID-stable;
- family-indexed;
- cross-referenced;
- machine-checkable where practical;
- explicit about current/public/classified/player-known state;
- explicit about source/canon status;
- explicit about whether a record is design-only or implemented.

## Quality rule

Do not use record count as a proxy for completion.

After a structural wave reaches scale, priority shifts to:
- schema completion;
- individualized mechanics;
- contradiction/overlap review;
- world integration;
- UX/privacy validation;
- implementation/test mapping;
- explicit canon promotion.
