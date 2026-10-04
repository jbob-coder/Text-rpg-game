# THE GAME — Parent Fixture Batch 002: Procedure, Action Overhead & Precision Execution

Status: **PHASE-C NUMERIC PREPARATION / QUALITATIVE PARENT FIXTURES / NO FINAL VALUES / NOT CANON / NOT IMPLEMENTED**

Parents:
- `PASSIVE_CANONICAL_RESOLVER_PARENT_FIXTURE_REQUIREMENTS_WAVE_001.md`
- `PASSIVE_CANONICAL_RESOLVER_SCENARIO_ANCHORS_WAVE_001.md`
- `PASSIVE_SHARED_RESOLVER_CAP_SEMANTICS_WAVE_001.md`
- `STATUS_BASE_RESOLUTION_TERM_UNIT_TAXONOMY.md`
- `STATUS_NUMERIC_CALIBRATION_FRAMEWORK.md`

Scope:
- `RESOLVER_PROCEDURE_COMPLIANCE_ERROR`;
- `RESOLVER_PRACTICED_PROCEDURE_OVERHEAD`;
- `RESOLVER_FINE_MOTOR_STEADINESS`.

Purpose: materialize parent-system test fixtures for procedure correctness, avoidable procedure overhead, and precision-action variance without inventing action seconds, failure percentages, or passive coefficients.

## 1. Shared procedure/action vocabulary

A future valid procedure/action record should distinguish at least:
- procedure/action stable ID;
- version;
- domain;
- authorization requirement where applicable;
- mandatory steps;
- optional/avoidable overhead;
- tools/materials;
- required observations/inputs;
- current step;
- completion/failure state;
- event/transaction ID;
- quality/review evidence.

A passive does not own this state.

## 2. Mandatory versus avoidable work

The parent system must distinguish:

`MANDATORY_WORK`
- physically/procedurally necessary;
- cannot be removed merely by familiarity.

`AVOIDABLE_OVERHEAD`
- hesitation;
- setup friction;
- unnecessary transition cost;
- redundant checking not required by the current valid procedure;
- other learned inefficiency.

`ERROR_BURDEN`
- risk/burden of omitting or mishandling a required step/check.

These are different terms.

A passive that reduces overhead does not automatically reduce error, and vice versa.

# Part A — Procedure compliance error

## 3. FIX_PROC_COMP_001 — Ordinary known procedure

Preconditions:
- procedure is valid/current;
- character knows it sufficiently to attempt;
- required authorization is satisfied where relevant;
- required tools/materials are available.

Expectation:
- parent system produces one procedure-compliance outcome/check stream;
- required steps remain required;
- passive modifiers, when later introduced, attach to that one stream rather than creating extra checks.

Current readiness after this batch:
`QUALITATIVE_FIXTURES_READY`.

## 4. FIX_PROC_COMP_002 — Unknown procedure boundary

Preconditions:
- procedure is not known to the character.

Expectation:
- compliance passive cannot fabricate procedure knowledge;
- procedure may fail, be unavailable, or route through a learning/discovery system;
- `RESOLVER_PROCEDURE_COMPLIANCE_ERROR` cannot silently convert unknown into known.

## 5. FIX_PROC_COMP_003 — Unauthorized procedure boundary

Preconditions:
- procedure is known;
- required authorization is absent.

Expectation:
- authorization fails before passive compliance benefit;
- no passive creates rank, credential, clearance, or permission;
- attempted use cannot reveal hidden authorization data beyond legitimate feedback.

## 6. FIX_PROC_COMP_004 — Stale version

Preconditions:
- character knows version A;
- authoritative procedure is version B;
- versions differ materially.

Expectation:
- familiarity with A does not guarantee correct B execution;
- parent versioning rule determines whether partial compatibility exists;
- passive cannot erase version mismatch.

## 7. FIX_PROC_COMP_005 — Interruption pressure

Preconditions:
- valid known procedure;
- interruption occurs during execution.

Expectation:
- current step/progress is authoritative;
- interruption may add error/overhead through parent rules;
- passive contribution cannot prevent failure when the procedure is genuinely invalidated.

## 8. FIX_PROC_COMP_006 — Duplicate finalization

Preconditions:
- procedure transaction `TX_ID=A` already committed.

Expectation:
- reload/repeated input cannot apply the same compliance result twice;
- qualification/progress events derived from the result also deduplicate.

# Part B — Practiced procedure overhead

## 9. FIX_PROC_OVH_001 — Ordinary practiced sequence

Preconditions:
- known procedure;
- ordinary familiarity;
- all mandatory steps present.

Expectation:
- parent system identifies avoidable overhead separately from mandatory work;
- overhead is non-negative;
- final procedure cannot become shorter than irreducible mandatory work.

Current readiness after this batch:
`QUALITATIVE_FIXTURES_READY`.

## 10. FIX_PROC_OVH_002 — Highly familiar favorable context

Preconditions:
- repeated valid practice;
- familiar tools/context;
- no major interruption.

Required relationship:
`OVERHEAD_favorable <= OVERHEAD_baseline`.

No numeric reduction is assigned.

## 11. FIX_PROC_OVH_003 — Valid unfamiliar configuration

Preconditions:
- procedure identity is known;
- tool/layout/configuration is compatible but unfamiliar.

Expectation:
- mandatory steps still resolve;
- avoidable overhead may increase;
- parent system must decide how familiarity scopes to configuration/equipment.

## 12. FIX_PROC_OVH_004 — Mandatory-step floor

Preconditions:
- theoretical passive modifiers would reduce overhead strongly.

Expectation:
- mandatory action/setup time remains;
- no negative duration;
- no skipped safety/authorization/material step.

## 13. FIX_PROC_OVH_005 — Context switch

Preconditions:
- character pauses one known procedure and switches to another task, then returns.

Expectation:
- parent system decides whether transition overhead exists;
- passive may reduce only the avoidable portion;
- active procedure state remains deterministic.

## 14. FIX_PROC_OVH_006 — Save/load continuity

Preconditions:
- procedure is partway complete;
- save at a legal checkpoint.

Expectation:
- mandatory completed work is not replayed;
- avoidable overhead is not re-granted as free progress;
- current step/version/tool context resumes deterministically.

# Part C — Fine motor steadiness

## 15. FIX_FINE_001 — Ordinary precision action

Preconditions:
- action is physically possible;
- tool/body can meet required precision;
- character knows the action.

Expectation:
- parent system exposes one execution-variance term or deterministic equivalent;
- passive steadiness modifies variance only, not raw skill knowledge or impossible geometry.

Current readiness after this batch:
`QUALITATIVE_FIXTURES_READY`.

## 16. FIX_FINE_002 — Stable favorable context

Preconditions:
- stable posture;
- familiar tool;
- adequate visibility;
- no significant fatigue/injury.

Required relationship:
`VARIANCE_favorable <= VARIANCE_adverse`.

Exact values remain open.

## 17. FIX_FINE_003 — Fatigue/pressure

Preconditions:
- action remains valid;
- fatigue, urgency, or mild instability increases difficulty.

Expectation:
- parent system can increase execution variance or equivalent burden;
- passive may reduce only the eligible component;
- fatigue resource/state is not erased.

## 18. FIX_FINE_004 — Tool/body precision floor

Preconditions:
- requested task requires precision beyond the physical capability of tool/body.

Expectation:
- passive cannot cross the hard physical precision floor;
- impossible action stays impossible unless another mechanic changes the physical limit.

## 19. FIX_FINE_005 — Injury limitation

Preconditions:
- relevant injury affects control.

Expectation:
- injury authority remains separate;
- passive steadiness cannot silently nullify injury;
- parent system defines residual valid capability.

## 20. FIX_FINE_006 — Domain mismatch

Preconditions:
- character has a domain-specific fine-motor passive;
- current action belongs to another unsupported domain.

Expectation:
- scope tags reject the modifier;
- generic motor steadiness and domain technique remain distinct.

## 21. Ordered-stage integration

A procedure may use all three resolver families in one action chain:

1. authorization/knowledge validates the procedure;
2. procedure compliance resolves required-step error;
3. practiced overhead resolves avoidable setup/transition burden;
4. fine-motor steadiness resolves physical precision where the current step requires it;
5. quality/result is finalized once.

No stage may re-read the original full difficulty and award duplicate benefits.

## 22. Gate Twelve fixture candidates

Confirmed local contexts can later supply content fixtures:
- Relay Workbench / Workshop Row — technical procedure and precision work;
- Municipal Archive — recurring documentation/procedure checks;
- restricted Gate/Tunnel context — authorization-sensitive procedures, once actual authorization semantics exist.

These locations do not yet define:
- exact procedure versions;
- exact tools;
- exact timing;
- authorization hierarchy;
- passive training.

## 23. Range-fixture blockers

Before any of these become `RANGE_FIXTURES_READY`, parent systems must define:
- action/procedure timing representation;
- procedure error resolution form;
- minimum/mandatory work terms;
- execution variance scale or deterministic equivalent;
- tool/body precision floors;
- rounding/serialization behavior.

## 24. Acceptance

This batch establishes qualitative parent fixtures for **3 canonical resolver families**.

No seconds, percentages, coefficients, or canon promotions are established.
