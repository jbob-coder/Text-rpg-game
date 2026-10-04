# THE GAME — Canon Review Dry Run: PASSIVE_REC_0001 Second Wind

Status: **DRY REVIEW ONLY / NO CANON PROMOTION**

Review template:
- `STATUS_RECORD_CANON_PROMOTION_PACKET_TEMPLATE.md`

## 1. Record identity

- record ID: `PASSIVE_REC_0001`
- display name: Second Wind
- type: passive
- current design status: calibration proposal
- implementation: not implemented
- parent family: Recovery

## 2. Dry-run decision

**PROPOSED REVIEW OUTCOME: APPROVE_WITH_OPEN_NUMERIC_FIELDS — OWNER DECISION REQUIRED**

This is not an actual canon promotion.

## 3. Governing law

Current defined law:
once per demanding activity window, after a verified meaningful Stamina drop and valid recovery opportunity, improve recovery from ordinary exertion.

Hard boundaries:
- not an instant refill;
- cannot repeatedly trigger without reset;
- does not bypass active penalties;
- affects Stamina recovery, not unrelated Focus/Resolve state.

## 4. Identity and overlap

Distinct from:
- general Stamina regeneration;
- Recovery family passives that improve sleep, pain recovery, or environmental recovery;
- Ability Synergy recovery effects, which follow primary-ability exertion.

Primary overlap risk:
two or more recovery passives modifying the same Stamina-recovery term.

Required rule:
use the cross-family capped composition resolver.

## 5. State ownership

Conceptual owner:
`CORE_RESOURCE_STATE`.

Read dependencies:
- demanding activity-window state;
- meaningful Stamina-drop evidence;
- valid recovery opportunity;
- reset state.

Write target:
bounded modifier to authoritative Stamina recovery.

Qualification evidence:
recovery-cycle history.

## 6. Numeric readiness

Defined parameter:
`PAS_CAL_REC_0001_RECOVERY_WINDOW_EFF`.

Still TBD:
- recovery bonus amount/rate;
- demanding-activity threshold;
- meaningful Stamina-drop threshold;
- reset definition;
- cap interaction with other recovery modifiers.

The mechanic identity does not require those final coefficients to remain conceptually coherent.

## 7. Knowledge and visibility

Current review result:
broad public/school/government knowledge is plausible.

Exact hidden qualification threshold remains internal.

Known misconception to preserve as world-facing correction:
Second Wind is not an instant Stamina refill.

## 8. World integration

Role classes:
- school;
- military/security;
- health/recovery;
- professional training;
- public fitness culture.

Named institutions/history: `TBD`.

## 9. Exploit review

Must prevent:
- trivial exertion loops;
- save/load re-trigger;
- multiple triggers in one activity window;
- hidden threshold leakage through UI;
- stacking into unlimited Stamina recovery.

## 10. Test obligations

Required:
- one valid trigger per activity window;
- no second trigger before reset;
- trivial exertion fails;
- Stamina cap respected;
- Focus/Resolve unchanged;
- save/load preserves trigger/reset state;
- same-term stacking cap works;
- player projection does not reveal hidden qualification counter.

## 11. Open blockers

- exact numeric calibration;
- exact activity-window/reset semantics;
- named world integration;
- owner/canon approval;
- runtime mapping.

## 12. Dry-run conclusion

Second Wind appears **conceptually mature enough for eventual canon approval with numeric fields still open**, but no promotion occurs until the owner explicitly reviews/approves the record.
