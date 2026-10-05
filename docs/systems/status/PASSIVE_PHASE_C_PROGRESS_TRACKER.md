# THE GAME — Passive Phase-C Progress Tracker

Status: **ACTIVE / WAVE 001 FAMILY-BASELINE COVERAGE COMPLETE / REFINEMENT CONTINUES**

Purpose: track reconstruction-grade refinement of the existing 230-passive Wave-001 corpus without creating another shallow wave.

## Milestone

**23 / 23 passive families now have a Phase-C family refinement baseline.**

Evidence:
- `PASSIVE_WAVE_001_PHASE_C_FAMILY_COVERAGE_AUDIT.md`
- `PASSIVE_CROSS_FAMILY_COMPOSITION_STANDARD.md`

This milestone does not canon-promote any passive.

## Family coverage

1. Physical 0001–0010 — detail + scaling/state + knowledge
2. Recovery 0001–0010 — detail + scaling/state + knowledge
3. Movement 0001–0010 — detail + scaling/state + knowledge
4. Sensory 0001–0010 — detail + scaling/state + knowledge
5. Mental / Will 0001–0010 — detail + scaling/state + knowledge
6. Cognitive / Learning 0001–0010 — detail/effect + scaling/state + knowledge
7. Combat Habit 0001–0010 — effect + scaling/state + knowledge
8. Weapon Familiarity 0001–0010 — effect + scaling/state + knowledge
9. Defensive Adaptation 0001–0010 — effect + scaling/state + knowledge
10. Survival / Environmental 0001–0010 — effect + scaling/state + knowledge
11. Social / Behavioral 0001–0010 — effect + scaling/state + knowledge
12. Leadership / Coordination 0001–0010 — effect + scaling/state + knowledge
13. Technical / Craft 0001–0010 — effect + scaling/state + knowledge
14. Medical / Recovery Practice 0001–0010 — effect + scaling/state + knowledge
15. Ability Synergy 0001–0010 — effect + scaling/state + knowledge
16. Resistance 0001–0010 — effect + scaling/state + knowledge
17. Creature / Beast Interaction 0001–0010 — effect + scaling/state + knowledge
18. Injury / Scar Adaptation 0001–0010 — effect + scaling/state + knowledge
19. Profession 0001–0010 — effect + scaling/state + knowledge
20. Faction / Institutional 0001–0010 — effect + scaling/state + knowledge
21. Unique Event 0001–0010 — effect + state + knowledge
22. Cosmic / System 0001–0010 — effect + state + knowledge
23. Unknown / Classified 0001–0010 — effect + state + knowledge

## Shared cross-family standard

`PASSIVE_CROSS_FAMILY_COMPOSITION_STANDARD.md` now defines:
- effect-stage separation;
- same-term stacking through one capped resolver;
- familiarity scoping;
- core-resource protection;
- damage/injury/condition separation;
- knowledge and agency protection;
- authorization protection;
- event-bound passive rules;
- exploit/debug requirements.

## Numeric calibration

`STATUS_NUMERIC_CALIBRATION_FRAMEWORK.md` now defines how future coefficients and thresholds are selected without false precision.

Compact Wave-001 unlock thresholds remain proposals until calibrated.

## Normalization progress

Materialized:
- `PASSIVE_STATE_OWNER_RESOLVER_MATRIX_WAVE_001.md` — conceptual owner and primary resolver mapping for all 23 families;
- `PASSIVE_KNOWLEDGE_PROFILE_RECONCILIATION_AUDIT_WAVE_001.md` — confirms the 200 ordinary-family compact knowledge rows are ordinal templates and identifies 120 high-priority/context-required rows;
- `PASSIVE_EVENT_QUALIFICATION_GOVERNANCE_STANDARD.md` — one-time event/packet qualification rules for UEV/COS/CLS families;
- `PASSIVE_NUMERIC_CALIBRATION_PILOT_001.md` — parameterizes representative passives while leaving values TBD;
- `STATUS_RECORD_CANON_PROMOTION_PACKET_TEMPLATE.md` — explicit record-by-record canon review shape.

## Record-level normalization milestone

Materialized:
- `PASSIVE_RECORD_OWNER_WRITE_TARGET_MATRIX_WAVE_001_INDEX.md`;
- `PASSIVE_RECORD_OWNER_WRITE_TARGET_MATRIX_WAVE_001_A.md`;
- `PASSIVE_RECORD_OWNER_WRITE_TARGET_MATRIX_WAVE_001_B.md`;
- `PASSIVE_RECORD_OWNER_WRITE_TARGET_MATRIX_WAVE_001_C.md`.

Coverage:
- **230 / 230 passive records** now have conceptual owner, primary effect stage, conceptual write target, qualification evidence class, and bounded effect recorded.

This is conceptual design mapping only; no runtime module/field is claimed.

## Runtime owner / projection disposition

Materialized:
- `PASSIVE_RUNTIME_OWNER_PROJECTION_DISPOSITION_WAVE_001.md`;
- `tools/status_phase_c_audit.py`;
- `tests/test_status_phase_c_audit.py`.

Current-runtime disposition now covers all **23 / 23 conceptual passive owner domains**:
- 2 `REUSE_CURRENT_OWNER`;
- 13 `COMPOSE_CURRENT_STATE`;
- 6 `DOMAIN_RUNTIME_REQUIRED`;
- 2 `LEDGER_CONTRACT_REQUIRED`.

The mapping locks several implementation boundaries:
- current durable `state.perks` is a real but narrow acquired-perk/modifier substrate, not a universal substitute for the 23 conceptual owners;
- current perk modifiers support registered `attributes.*`, `skills.*` and `derived.*` effective-value paths;
- current Status projection has no explicit player-facing passive list;
- hidden perk IDs remain redacted in deep status inspection;
- current Android has no passive-list DTO, although safe visible perk contributions may appear in inspected status breakdowns;
- conceptual owners without equivalent current runtime domains remain future implementation/migration work rather than fake flags/perk tags.

Automated ownership integrity now verifies **230 / 230** registry IDs against **230 / 230** owner/write-target rows, 23 families x 10 records, with duplicate/missing/extra/blank-row detection.

This is a Phase-C design-to-implementation disposition, not Phase-F runtime implementation or canon promotion.

## Read-dependency / overlap normalization

Materialized:
- `PASSIVE_RECORD_READ_DEPENDENCY_OVERLAP_MATRIX_WAVE_001_INDEX.md`;
- `PASSIVE_RECORD_READ_DEPENDENCY_OVERLAP_MATRIX_WAVE_001_A.md`;
- `PASSIVE_RECORD_READ_DEPENDENCY_OVERLAP_MATRIX_WAVE_001_B.md`;
- `PASSIVE_RECORD_READ_DEPENDENCY_OVERLAP_MATRIX_WAVE_001_C.md`;
- `PASSIVE_OVERLAP_EDGE_ADJUDICATION_WAVE_001.md`.

Coverage:
- **230 / 230 passive records** have conceptual read-dependency baselines;
- **93 candidate overlap edges** reviewed;
- 38 `SAME_TERM_CAPPED`;
- 30 `ORDERED_STAGE_COMPOSITION`;
- 25 `DISTINCT_STAGE_NO_SHARED_TERM`.

No runtime field/module is claimed by this normalization.

## Knowledge reconciliation waves

Materialized:
- `PASSIVE_KNOWLEDGE_RECONCILIATION_WAVE_A_0004_0008_0010.md` — 60 highest-priority rows;
- `PASSIVE_KNOWLEDGE_RECONCILIATION_WAVE_B_0003_0009.md` — 40 institutional-asymmetry rows;
- `PASSIVE_KNOWLEDGE_RECONCILIATION_WAVE_C_FALSE_BELIEFS_0005.md` — 20 concrete candidate false-belief rows.

Compact registry remains unchanged pending world evidence and explicit review.

## World integration family coverage

Materialized:
- `PASSIVE_WORLD_INTEGRATION_ROLE_CLASS_MATRIX_WAVE_001.md`.

All 23 passive families now have family-level role-class relevance mapped without inventing named institutions.

## Numeric base-term dependency milestone

Materialized:
- `STATUS_BASE_RESOLUTION_TERM_UNIT_TAXONOMY.md`;
- `PASSIVE_CANONICAL_RESOLVER_BASE_TERM_MAP_WAVE_001.md`.

All 20 canonical shared passive resolvers now identify the base term and abstract unit class required before coefficient calibration.

## Base-term / unit preparation

Materialized:
- `STATUS_BASE_RESOLUTION_TERM_UNIT_TAXONOMY.md`;
- `PASSIVE_CANONICAL_RESOLVER_BASE_TERM_MAP_WAVE_001.md`.

Result:
- abstract unit classes now exist for resource amounts/rates, time, distance, penalties, error burden, execution variance, contest modifiers, interpretation confidence, procedure overhead, recovery, and performance decay;
- all 20 canonical shared passive resolvers now identify the base term and abstract unit class they depend on;
- final scales/coefficients remain `TBD`.

## Shared resolver cap semantics

Materialized:
- `PASSIVE_SHARED_RESOLVER_CAP_SEMANTICS_WAVE_001.md`.

Result:
- 24 provisional same-term resolver keys consolidated to **20 canonical resolver families**;
- duplicate recall, prolonged-Focus, and procedure-compliance resolver paths were merged;
- symbolic cap/floor rules and anti-double-count rules are now documented;
- exact coefficients remain `TBD`.

## Knowledge role-class adjudication

Materialized:
- `PASSIVE_KNOWLEDGE_ROLE_CLASS_ADJUDICATION_WAVE_001.md` — 100 ordinary-family 0003/0004/0008/0009/0010 rows now have role-class-informed recommended directions;
- `PASSIVE_FALSE_BELIEF_PROVENANCE_ROLE_CLASS_MAP_0005.md` — 20 false-belief candidates now have origin/correction role-class channels.

Compact knowledge rows remain unchanged pending entity-level world evidence and explicit review.

## Resolver scenario-anchor milestone

Materialized:
- `PASSIVE_CANONICAL_RESOLVER_SCENARIO_ANCHORS_WAVE_001.md`.

Result:
- all **20 / 20 canonical shared passive resolvers** now have qualitative BASELINE, FAVORABLE, ADVERSE, and BOUNDARY scenario anchors;
- no coefficient or final scale was invented;
- next numeric step is parent-system range/test-fixture definition.

## Parent-fixture requirement milestone

Materialized:
- `PASSIVE_CANONICAL_RESOLVER_PARENT_FIXTURE_REQUIREMENTS_WAVE_001.md`.

Result:
- all **20 / 20 canonical shared passive resolvers** now identify the exact parent-system fixture evidence required before candidate passive coefficients are allowed;
- readiness states now distinguish missing parent model, fixture schema, qualitative fixtures, range fixtures, and executable fixtures;
- no final parent range or passive coefficient was invented.

## First parent-system fixture batch

Materialized:
- `STATUS_CORE_RESOURCE_PARENT_FIXTURE_BATCH_001_STAMINA_FOCUS.md`.

Result:
- `RESOLVER_STAMINA_RECOVERY_OPPORTUNITY` and `RESOLVER_PROLONGED_FOCUS_DRAIN` now have concrete qualitative parent fixture sets;
- both advance to `QUALITATIVE_FIXTURES_READY`;
- current Dead Relay Stamina 70 / Focus 60 are explicitly preserved as content-instance regression evidence, not universal scales;
- final resource ranges and passive coefficients remain blocked.

## Qualitative parent-fixture baseline complete

Materialized:
- `STATUS_PARENT_FIXTURE_BATCH_002_PROCEDURE_ACTION_PRECISION.md`;
- `STATUS_PARENT_FIXTURE_BATCH_003_KNOWLEDGE_EVIDENCE_INTERPRETATION.md`;
- `STATUS_PARENT_FIXTURE_BATCH_004_SPATIAL_TRAVEL_CONTEST.md`;
- `STATUS_PARENT_FIXTURE_BATCH_005_FATIGUE_ENVIRONMENT_RECOVERY_INSTITUTION.md`;
- `PASSIVE_CANONICAL_RESOLVER_FIXTURE_READINESS_INDEX_WAVE_001.md`.

Result:
- all **20 / 20 canonical shared passive resolvers** now have explicit qualitative parent fixture sets;
- each resolver is at least `QUALITATIVE_FIXTURES_READY`;
- **0 / 20** are yet certified `RANGE_FIXTURES_READY`;
- **0 / 20** are yet certified `EXECUTABLE_FIXTURES_READY`;
- passive coefficients remain blocked until parent-system scales/ranges are justified.

## Range-fixture eligibility audit

Materialized:
- `PASSIVE_CANONICAL_RESOLVER_RANGE_FIXTURE_ELIGIBILITY_AUDIT_WAVE_001.md`.

Result:
- **0 / 20 canonical shared passive resolvers** currently qualify for `RANGE_FIXTURES_READY`;
- all 20 remain `QUALITATIVE_FIXTURES_READY`;
- blockers are now grouped into resource/time, error/confidence, physical/spatial, institution, and environment parent-scale dependencies;
- current content-instance values are explicitly prohibited from being treated as universal scales.

This is an intentional numeric safety gate, not incomplete work.

## Parent-scale semantic prerequisites

Materialized:
- `WORLD_SIMULATION_TIME_AND_DURATION_STANDARD.md`;
- `STATUS_WORLD_TIME_PARENT_FIXTURE_BATCH_001.md`;
- `CORE_RESOURCE_SCALE_AND_TRANSACTION_STANDARD.md`;
- `STATUS_ERROR_CONFIDENCE_RESOLUTION_MODE_STANDARD.md`.

Resolved at the semantic/convention level:
- durable WORLD_TIME = authoritative integer simulation minutes for strategic world simulation;
- encounter/process/subjective time remain separate;
- core resources remain absolute amounts with dynamic effective maxima;
- max-change, spend, recovery, and cross-resource isolation rules are explicit;
- error/confidence resolution modes are explicit;
- internal numeric confidence is compatible with 0..1 and is not truth probability.

Range-fixture audit remains **0 / 20** because domain-specific target ranges are still intentionally open.

## Physical / institutional parent semantics

Materialized:
- `STATUS_PHYSICAL_DISTANCE_CONTEST_PRECISION_STANDARD.md`;
- `INSTITUTION_ROLE_AUTHORIZATION_PROTOCOL_STANDARD.md`.

Resolved at the semantic level:
- authoritative physical distance uses meters while presentation coordinates remain separate;
- reach/range/route-time distinctions are explicit;
- opposed physical contest and execution-variance roles are explicit;
- institution, role, rank, credential, clearance, authorization, protocol, and command/responsibility structure are separated;
- Faction/Institutional passives cannot create authorization.

Numeric ranges and named world entities remain open.

## Local world-evidence integration

Materialized:
- `STATUS_GATE_TWELVE_LOCAL_WORLD_INTEGRATION_EVIDENCE_PILOT.md`.

Result:
- confirmed Gate Twelve civic/maintenance/records/evacuation/restricted-infrastructure contexts are separated from proposal-only parent-world names;
- record-level local integration candidates are identified without claiming local training, regulation, or passive ownership;
- the pilot can now support evidence-based adjudication of knowledge/world-integration proposals.

## Gate Twelve evidence-backed adjudication

Materialized:
- `STATUS_GATE_TWELVE_EVIDENCE_BACKED_KNOWLEDGE_WORLD_ADJUDICATION_001.md`.

Result:
- confirmed Gate Twelve local evidence was applied to a bounded set of Technical, Profession, Faction/Institutional, Leadership, Defensive, Movement, Mental/Will, and Lightning Conduit world-integration candidates;
- local context support is explicitly separated from proof of training, classification, regulation, credential systems, or named institutions;
- proposal-only parent-world names remain excluded from confirmed evidence.

## World/canon preparation

Materialized:
- `STATUS_WORLD_INTEGRATION_ROLE_CLASS_PILOT_001.md`;
- `CANON_REVIEW_DRY_RUN_PASSIVE_REC_0001.md`;
- `CANON_REVIEW_DRY_RUN_ABILITY_RAR_003.md`.

Additional dry reviews:
- `CANON_REVIEW_DRY_RUN_PASSIVE_PRO_0008.md` — Documentation Discipline returns for refinement because its all-unknown compact knowledge posture and parent professional-documentation workflow are not ready;
- `CANON_REVIEW_DRY_RUN_PASSIVE_FAC_0005.md` — Clearance Awareness returns for refinement because the world lacks an actual clearance/authorization model;

- `CANON_REVIEW_DRY_RUN_PASSIVE_TEC_0006.md` — Repair Economy appears conceptually mature enough for eventual approval with numeric/world-provenance fields open;
- `CANON_REVIEW_DRY_RUN_PASSIVE_FAC_0002.md` — Credential Navigation returns for refinement because actual credential/authorization world semantics are not yet authored.

Super Epic dry review:
- `CANON_REVIEW_DRY_RUN_SUPER_EPIC_001_003.md`;
- Time Partition: RETURN_FOR_REFINEMENT;
- Matter Recode: RETURN_FOR_REFINEMENT;
- Probability Tilt: RETURN_FOR_REFINEMENT;
- all three retain strong Super Epic identity; no deletion/merge/rarity change recommended.

No named institution was invented and no record was canon-promoted.

## Next work

1. define target resource range bands and travel/fatigue/environment ranges; physical distance/contest/precision and institutional semantics are now also materialized, while current audit remains 0 / 20 range-ready;
2. continue evidence-backed Gate Twelve knowledge/world adjudication only where confirmed local context supports it;
3. progress selected records toward actual world entities only after owner/world canon decisions;
4. run additional canon dry-review packets;
5. continue shared ability child-rule completion;
6. consume the runtime-owner/projection disposition when implementation mapping begins; do not remap conceptual owners into fake runtime fields.

## Stop condition

Do not add another broad passive wave merely to increase count.

The next value comes from deepening, reconciling, validating, world-integrating, and eventually canon-reviewing the existing 230-passive corpus.
