# THE GAME — Canon Review Dry Run: PASSIVE_TEC_0006 Repair Economy

Status: **DRY REVIEW ONLY / NO CANON PROMOTION**

Review template:
- `STATUS_RECORD_CANON_PROMOTION_PACKET_TEMPLATE.md`

## 1. Record identity

- record ID: `PASSIVE_TEC_0006`
- display name: Repair Economy
- type: passive
- family: Technical / Craft
- current design status: calibration proposal
- implementation: not implemented

## 2. Dry-run decision

**PROPOSED REVIEW OUTCOME: APPROVE_WITH_OPEN_NUMERIC_FIELDS — OWNER DECISION REQUIRED**

No canon promotion occurs.

Reason:
the passive has a narrow, non-supernatural identity, clear conceptual ownership, deterministic qualification shape, and an existing local world context where repair work is confirmed. Final coefficients, unlock thresholds, and knowledge provenance remain open.

## 3. Governing effect

Current bounded effect:
reduces wasted consumables during familiar repair procedures.

Hard boundaries:
- does not create missing parts/materials;
- does not repair an item by itself;
- does not substitute for Technical/Craft skill;
- does not make unfamiliar procedures familiar;
- cannot convert poor source materials into valid components;
- quality requirements remain authoritative.

## 4. State ownership

Conceptual owner:
`TECHNICAL_TASK_STATE`.

Conceptual write target:
`TECHNICAL_TASK_STATE.modifier.repair_economy`.

Required conceptual reads:
- technical task state;
- tool/material state;
- procedure state;
- quality evidence state.

Current direct-overlap matrix:
`NONE_IDENTIFIED`.

This reduces current stacking risk, but future resource-accounting overlap still requires review if other passives begin modifying the same consumable-waste term.

## 5. Qualification

Current compact calibration proposal:
- technical tasks >= 45;
- verified repairs/outputs >= 15;
- quality review = passed.

Guardrails:
- meaningful legitimate events only;
- duplicate/trivial/self-destructive farming excluded;
- hidden progress remains absent from ordinary Status projection.

The exact numeric thresholds remain proposals and are not required to define the passive's conceptual identity.

## 6. Numeric readiness

Required future parameter:
a bounded reduction to **avoidable consumable/material waste** for an eligible familiar repair procedure.

Still `TBD`:
- material-accounting unit;
- base expected avoidable waste;
- passive coefficient;
- cap/floor;
- familiarity threshold;
- procedure-quality interaction.

The passive must never reduce required material consumption below the physically/procedurally required amount.

## 7. Knowledge and visibility

Current compact posture:
- public known;
- school known;
- government known;
- faction known;
- exact qualification threshold hidden.

This broad knowledge posture is plausible for an ordinary technical practice concept, but final world provenance still needs actual education/trade/institution records.

Do not interpret “known” as proof that every region, profession, or organization teaches the same method.

## 8. World integration

Confirmed local Gate Twelve evidence:
- Workshop Row contains repair shops / municipal contractors;
- Relay Workbench is a technical/maintenance context.

Safe conclusion:
Repair Economy has a plausible local professional use context.

Not established:
- a named trade school;
- a licensing system;
- an actual local passive-training program;
- exact repair economy standards;
- universal government knowledge.

Role classes likely relevant:
- INDUSTRIAL_BODY;
- PROFESSIONAL_ASSOCIATION;
- SCHOOL_AUTHORITY;
- MILITARY_SECURITY where maintenance doctrine exists.

## 9. Exploit review

Must prevent:
- counting the same repair/output twice;
- intentionally wasting materials to farm qualification;
- save/load duplicate credit;
- treating failed/low-quality output as verified repair;
- converting the passive into free material generation.

## 10. Test obligations

Required future tests:
- valid repair event counts once;
- duplicate event ID does not count twice;
- failed quality review does not qualify;
- unfamiliar procedure receives no full benefit;
- required materials remain required;
- material inventory cannot increase through Repair Economy;
- save/load preserves qualification state exactly once;
- hidden thresholds remain hidden.

## 11. Open blockers

- exact consumable/material accounting model;
- numeric coefficient/cap;
- final unlock thresholds;
- actual education/trade provenance;
- owner/canon approval;
- runtime mapping.

## 12. Dry-run conclusion

Repair Economy appears conceptually mature enough for eventual canon approval while numeric and world-provenance fields remain open.

This dry run does **not** promote the passive.
