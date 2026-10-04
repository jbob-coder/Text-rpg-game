# 2026-10-04 — Parent Scale Semantics & Super Epic Dry-Review Checkpoint

Repository: `jbob-coder/Text-rpg-game`
Branch: `docs/master-game-development-program`
PR: #33

## 1. Authoritative world-time semantics

Materialized:
- `docs/systems/status/WORLD_SIMULATION_TIME_AND_DURATION_STANDARD.md`
- `docs/systems/status/STATUS_WORLD_TIME_PARENT_FIXTURE_BATCH_001.md`

Key decisions:
- current `GameState.time_minutes` remains the durable coarse world-time compatibility authority until explicit migration;
- strategic WORLD_TIME uses integer simulation minutes;
- turn count is not elapsed time;
- encounter/process/subjective time are separate domains;
- sub-minute actions must reconcile through a documented encounter/process commit;
- device wall-clock time is not gameplay authority by default;
- temporal abilities do not rewind durable campaign WORLD_TIME under current laws.

Current implementation edge case documented:
- zero-duration timed conditions can persist until a time-advance operation processes them; target design must reject or immediately resolve that ambiguity.

World-time parent fixtures:
- 18 explicit fixtures.

## 2. Core-resource scale and transaction semantics

Materialized:
- `docs/systems/status/CORE_RESOURCE_SCALE_AND_TRANSACTION_STANDARD.md`

Current reference formulas documented:
- max_health = 50 + 2.0*Endurance + 0.5*Will;
- max_stamina = 40 + 1.5*Endurance + 0.5*Athletics;
- max_focus = 30 + 0.8*Intellect + 0.7*Will;
- max_resolve = 25 + 1.1*Will + 0.35*Presence + 0.15*Leadership.

Unmodified authored-input reference envelopes:
- Health: 50–300;
- Stamina: 40–240;
- Focus: 30–180;
- Resolve: 25–185.

These are current implementation reference envelopes only, not final target balance.

Target semantics now define:
- absolute resource amounts rather than universal 0–100 percentages;
- current/base/effective maximum separation;
- max increase does not auto-refill;
- max decrease clamps current when required;
- spend/recovery transaction requirements;
- no default cross-resource conversion;
- ability-specific reserves remain separate.

Final representative target maxima, ordinary spend/recovery bands, zero-resource consequences, and precision remain open.

## 3. Error / confidence / resolution-mode semantics

Materialized:
- `docs/systems/status/STATUS_ERROR_CONFIDENCE_RESOLUTION_MODE_STANDARD.md`

Current implementation mapped:
- current authored scene checks use a deterministic seeded margin model;
- current NPC knowledge confidence validates 0..1.

Target resolution modes:
- DETERMINISTIC_RULE;
- MARGIN_CHECK;
- SEEDED_VARIANCE_MARGIN;
- OPPOSED_CONTEST;
- WEIGHTED_OUTCOME.

Key rules:
- hard invalidity resolves before uncertainty;
- ERROR_BURDEN is not automatically a probability;
- numeric confidence remains compatible with 0..1;
- confidence is not objective truth probability;
- SYSTEM_CONFIRMED is an authority/provenance state, not simply confidence=1;
- committed seeded outcomes cannot be rerolled through save/load.

## 4. Physical distance / contest / precision semantics

Materialized:
- `docs/systems/status/STATUS_PHYSICAL_DISTANCE_CONTEST_PRECISION_STANDARD.md`

Target decision:
- authoritative physical world distance uses meters;
- map/presentation coordinates are not meters unless an explicit transform defines that relationship.

Also defined:
- route distance versus route time;
- reach/range distinctions;
- opposed physical contest structure;
- equipment-retention contest boundary;
- accuracy versus precision;
- physical/tool precision floors;
- deterministic seeded contest behavior where uncertainty is used.

Final reach bands, contest ranges, precision ranges, and tactical cell-to-meter mapping remain open.

## 5. Institution / authorization parent model

Materialized:
- `docs/systems/status/INSTITUTION_ROLE_AUTHORIZATION_PROTOCOL_STANDARD.md`

Separated:
- institution membership;
- role;
- rank;
- credential;
- clearance;
- authorization;
- protocol;
- command/responsibility graph;
- reputation;
- profession.

Key rule:
Faction/Institutional familiarity passives cannot create credentials, clearance, rank, authority, or hidden knowledge.

Gate Twelve restricted infrastructure remains evidence that an access model is relevant, not proof that a credential/clearance hierarchy already exists.

## 6. Range-fixture audit status

Updated:
- `PASSIVE_CANONICAL_RESOLVER_RANGE_FIXTURE_ELIGIBILITY_AUDIT_WAVE_001.md`
- `PASSIVE_CANONICAL_RESOLVER_FIXTURE_READINESS_INDEX_WAVE_001.md`
- `STATUS_BASE_RESOLUTION_TERM_UNIT_TAXONOMY.md`

Semantic prerequisites now substantially mapped:
- world time;
- core resources;
- error/confidence resolution modes;
- physical distance/contest/precision;
- institutional authorization/protocol.

Range readiness remains deliberately:
- **0 / 20 RANGE_FIXTURES_READY**.

Reason:
domain-specific target ranges are still open.

Next numeric dependencies:
1. target core-resource calibration bands and ordinary spend/recovery ranges;
2. travel/fatigue/environment ranges;
3. domain-specific error/difficulty/variance and physical contest ranges;
4. at least one real institutional workflow after parent-world approval.

## 7. Super Epic canon dry review

Materialized:
- `docs/systems/status/CANON_REVIEW_DRY_RUN_SUPER_EPIC_001_003.md`

Results:
- ABILITY_SEP_001 Time Partition — RETURN_FOR_REFINEMENT;
- ABILITY_SEP_002 Matter Recode — RETURN_FOR_REFINEMENT;
- ABILITY_SEP_003 Probability Tilt — RETURN_FOR_REFINEMENT.

All three:
- retain strong distinct Super Epic identities;
- have dedicated non-numeric child standards;
- have no current deletion/merge/demotion/promotion recommendation;
- remain blocked by numeric envelopes, world integration, state-owner/runtime mapping, and explicit owner approval.

No canon promotion occurs.

## 8. Structural verification

Wave-001 corpus remains:
- 47 primary abilities;
- 230 passives;
- 188 techniques;
- 230 passive unlock paths;
- 230 passive knowledge profiles;
- 47 awakenings;
- 47 counters;
- **1,019 total**;
- **1,019 unique IDs**;
- 0 duplicate IDs;
- 0 dangling ability references;
- 0 dangling passive references.

Documentation verification:
- world-time standard: 35 numbered sections;
- world-time fixture batch: 18 explicit fixtures;
- core-resource standard: 27 numbered sections;
- error/confidence standard: 27 numbered sections;
- physical distance/contest standard: 27 numbered sections;
- institution/authorization standard: 29 numbered sections.

## 9. Next work

Recommended sequence:
1. build non-canon target calibration bands for core Stamina/Focus maxima, spends, and recovery using current formulas only as reference evidence;
2. define travel/fatigue/environment parent scales;
3. define domain-specific error/difficulty/variance and contest ranges;
4. rerun range-fixture eligibility;
5. continue Legendary/Prime Legendary/Unique child-rule closure and canon dry reviews;
6. continue evidence-backed world integration without inventing parent-world entities;
7. keep runtime implementation deferred until design coherence.

No runtime/gameplay code changed in this checkpoint.
