# THE GAME — Status / Ability / Passive Documentation Index

Parent authority:
- `../STATUS_UI_ABILITIES_AND_PASSIVES_MASTER_PLAN.md`

This directory owns the reconstruction-grade child contracts for human Status UI, awakening, level, primary abilities, passive abilities, hidden requirements, knowledge visibility, catalog structure, UX, balance, and test mapping.

## Authority order

1. `../STATUS_UI_ABILITIES_AND_PASSIVES_MASTER_PLAN.md`
2. `STATUS_UI_CORE_CONTRACT.md`
3. rarity / registry / requirement / visibility standards
4. catalog indexes
5. individual catalog records
6. implementation mappings and tests

Runtime source remains the authority for what is implemented now. These documents own target-game design unless explicitly marked otherwise.

## Current children

- `STATUS_UI_CORE_CONTRACT.md`
- `PASSIVE_REGISTRY_SCHEMA.md`

## Planned children

- `ABILITY_RARITY_STANDARD.md`
- `PRIMARY_ABILITY_REGISTRY_SCHEMA.md`
- `PASSIVE_REQUIREMENT_LANGUAGE.md`
- `STATUS_KNOWLEDGE_VISIBILITY_STANDARD.md`
- `LEVEL_AND_XP_STANDARD.md`
- `AWAKENING_EVENT_STANDARD.md`
- `LEVEL_100_EXCEPTION_STANDARD.md`
- `PRIMARY_ABILITY_CATALOG_INDEX.md`
- `PASSIVE_CATALOG_INDEX.md`
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
