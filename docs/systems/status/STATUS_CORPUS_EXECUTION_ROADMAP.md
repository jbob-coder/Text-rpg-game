# THE GAME — Status / Ability / Passive Corpus Execution Roadmap

Status: **ACTIVE EXECUTION PLAN / WAVE 001 STRUCTURALLY COMPLETE**

## Phase A — governing rules

Materialized:
- master plan;
- Status core contract;
- rarity standard;
- primary ability registry schema;
- passive registry schema;
- passive requirement language;
- knowledge visibility;
- Level/XP;
- awakening event;
- Level-100 exception;
- ability authoring guide;
- passive authoring guide;
- Status UX contract;
- balance/test matrix;
- ability/passive cross-reference.

Result: **COMPLETE for current design authority layer.**

## Phase B — controlled calibration wave

Wave 001 realized:
- 47 primary ability records;
- 230 passive records;
- 188 technique records;
- 230 passive unlock-path records;
- 230 passive knowledge records;
- 47 awakening profiles;
- 47 counter profiles.

Total structured records: **1,019**.

Structural audit:
- 1,019 unique IDs;
- 0 duplicate IDs;
- 0 dangling ability-parent references;
- 0 dangling passive-parent references.

See:
- `DOCUMENTATION_UNIT_LEDGER.md`
- `STATUS_CORPUS_WAVE_001_AUDIT.md`

Result: **STRUCTURALLY COMPLETE.**

These records remain `CALIBRATION_PROPOSAL` unless separately promoted.

## Phase C — reconstruction-grade refinement and consistency audit

Status: **IN PROGRESS.**

### Common ability slice 001–010

Materialized:
- `calibration/PRIMARY_ABILITY_DETAIL_COMMON_001_010.md`
- `calibration/ABILITY_TECHNIQUE_DETAIL_COMMON_001_010.md`
- `COMMON_ABILITY_RARITY_OVERLAP_AUDIT_001_010.md`

Linked compact records now also have:
- 40 individualized technique rows;
- 10 individualized awakening profiles;
- 10 individualized counter profiles.

Rarity/overlap audit result:
- 5 PASS;
- 5 PARTIAL;
- 0 FAIL;
- 0 recommended deletions.

Flagged adjacency checks:
- Kinetic Palm versus Vector Nudge;
- Skin Reinforcement versus Stonehide;
- Static Reservoir versus Lightning Conduit;
- Water Draw versus Vapor Sculpt;
- Impact Cushion versus Momentum Bank.

These must be resolved while deep-authoring the adjacent higher-tier records.

### Physical passive slice 0001–0010

Materialized:
- `calibration/PASSIVE_DETAIL_PHYSICAL_0001_0010.md`
- `PASSIVE_PHYSICAL_KNOWLEDGE_REFINEMENT_0001_0010.md`

Knowledge refinement now covers:
- military/security knowledge;
- research knowledge;
- false-rumor patterns;
- over-classification review.

Knowledge-posture review flags:
- PASSIVE_PHY_0004 likely over-classified;
- PASSIVE_PHY_0008 likely too unknown;
- PASSIVE_PHY_0010 likely over-classified.

No compact knowledge row was silently promoted or rewritten by that audit.

### Remaining Phase-C work

- physical passive scaling/cap detail;
- authoritative hidden-progress ownership mapping;
- implementation/test mapping;
- named institutions and historical cases;
- higher-tier ability deep authoring;
- remaining passive families;
- duplicate mechanics;
- rarity drift;
- impossible requirements;
- hidden-information leaks;
- world-integration gaps;
- excessive art/content burden.

### Phase C next order

1. **Deep-author Uncommon abilities 001–010.**
2. Resolve Common↔Uncommon adjacency flags during that slice.
3. Finish Physical passive scaling/caps and state-owner mapping.
4. Deep-author Recovery passives 0001–0010.
5. Continue Rare abilities and remaining passive families.
6. Do **not** create another thousand shallow records until the refinement pattern passes review.

## Phase D — world integration

Map selected records into:
- schools;
- government;
- military/security;
- research;
- factions;
- professions;
- beast ecology;
- laws;
- illicit markets;
- classified programs;
- historical events.

No record becomes socially real merely because it exists in the calibration catalog.

## Phase E — canon promotion

Owner-approved or design-authority-approved records can move from calibration proposal to target canon.

Promotion must be explicit. No bulk auto-promotion.

Promotion review must check:
- parent design compatibility;
- rarity fit;
- overlap;
- counterplay;
- hidden-information policy;
- world consequences;
- visual/content burden;
- implementation feasibility.

## Phase F — implementation mapping

Only after design coherence:
- engine schema;
- save schema;
- evaluator;
- projection;
- Android models;
- loaders;
- validators;
- tests.

No runtime implementation is implied by the documentation corpus.
