# THE GAME — Passive Numeric Calibration Pilot 001

Status: **PHASE-C PARAMETERIZATION PILOT / VALUES TBD / NOT CANON / NOT IMPLEMENTED**

Parents:
- `STATUS_NUMERIC_CALIBRATION_FRAMEWORK.md`
- `PASSIVE_CROSS_FAMILY_COMPOSITION_STANDARD.md`
- `PASSIVE_STATE_OWNER_RESOLVER_MATRIX_WAVE_001.md`

Purpose: prove that passive effects can be reduced to explicit measurable resolver parameters before any final coefficient is selected.

No final numeric values are assigned in this pilot.

## Pilot rules

For each selected passive define:
- parameter ID;
- authoritative owner;
- effect stage;
- measurement domain;
- direction;
- floor/cap requirement;
- scenario anchors;
- known overlap set.

A later calibration pass may assign candidate values only after base-system ranges are documented.

## Representative parameters

| Passive | Parameter ID | Owner | Stage | Measurement | Direction | Hard boundary |
|---|---|---|---|---|---|---|
| PASSIVE_REC_0001 Second Wind | PAS_CAL_REC_0001_RECOVERY_WINDOW_EFF | CORE_RESOURCE_STATE | RESOURCE_RECOVERY | valid recovery gained per qualifying recovery opportunity | increase | cannot exceed resource cap or create an opportunity that does not exist |
| PASSIVE_COG_0005 Deep Recall | PAS_CAL_COG_0005_RECALL_FAILURE | KNOWLEDGE_LEARNING_STATE | KNOWLEDGE_RECALL | failure/error rate retrieving already learned information | decrease | cannot retrieve unknown information |
| PASSIVE_CBT_0001 Guard Recovery | PAS_CAL_CBT_0001_GUARD_TRANSITION | COMBAT_ACTION_STATE | EXECUTION | post-action transition overhead into valid guard state | decrease | cannot reduce mandatory action recovery to zero unless another system explicitly permits it |
| PASSIVE_WPN_0002 Recoil Familiarity | PAS_CAL_WPN_0002_RECOIL_DISRUPTION | EQUIPMENT_HANDLING_STATE | EXECUTION | handling/aim disruption from a familiar recoil profile | decrease | underlying recoil force is unchanged |
| PASSIVE_DEF_0006 Evasion Recovery | PAS_CAL_DEF_0006_EVASION_RECOVERY | DEFENSIVE_REACTION_STATE | EXECUTION | recovery overhead after a valid evasive action | decrease | cannot create an extra action or movement budget |
| PASSIVE_SUR_0001 Heat Tolerance | PAS_CAL_SUR_0001_HEAT_PERF_PENALTY | ENVIRONMENT_EXPOSURE_STATE | STATE_RECOVERY / FAMILIARITY | non-critical heat performance penalty inside acclimated band | decrease | environmental injury thresholds remain authoritative |
| PASSIVE_SOC_0004 Negotiation Stamina | PAS_CAL_SOC_0004_NEGOTIATION_DRAIN | SOCIAL_CONTEXT_STATE | RESOURCE_COST | Focus/Resolve drain attributable to prolonged structured negotiation | decrease | cannot generate Focus/Resolve or guarantee persuasion |
| PASSIVE_LDR_0004 Morale Anchor | PAS_CAL_LDR_0004_TEAM_RESOLVE_LOSS | TEAM_COORDINATION_STATE | STATE_RECOVERY / RESOURCE_COST | avoidable Resolve loss in valid trusted-team context | decrease | cannot force loyalty, courage, or obedience |
| PASSIVE_TEC_0006 Repair Economy | PAS_CAL_TEC_0006_CONSUMABLE_WASTE | TECHNICAL_TASK_STATE | EXECUTION | avoidable consumable/material waste during familiar repair procedure | decrease | cannot create missing materials or parts |
| PASSIVE_MED_0003 Sterile Routine | PAS_CAL_MED_0003_CONTAMINATION_ERROR | MEDICAL_CASE_STATE | EXECUTION | contamination-error contribution from routine procedure execution | decrease | contaminated environment/input remains hazardous |
| PASSIVE_SYN_0009 Ability Familiarity | PAS_CAL_SYN_0009_FOCUS_OVERHEAD | ABILITY_EXECUTION_STATE | RESOURCE_COST | avoidable Focus overhead for eligible familiar low-complexity ability use | decrease | ability can never become zero-cost by this passive alone |
| PASSIVE_RES_0005 Toxin Resistance | PAS_CAL_RES_0005_TOXIN_EFFECT | HAZARD_RESISTANCE_STATE | RESISTANCE | eligible effect magnitude/duration for one documented toxin family | decrease | family-specific; no universal toxin immunity |
| PASSIVE_BST_0009 Track Interpretation | PAS_CAL_BST_0009_TRACK_ERROR | CREATURE_FIELD_KNOWLEDGE_STATE | INTERPRETATION | interpretation error/confidence burden on valid known-family tracks | decrease | poor/absent evidence remains poor/absent |
| PASSIVE_INJ_0001 Scar Flexibility | PAS_CAL_INJ_0001_SCAR_MOBILITY_PENALTY | INJURY_REHABILITATION_STATE | STATE_RECOVERY / EXECUTION | mobility penalty attributable to fully healed scar tissue | decrease | active injury is not erased |
| PASSIVE_PRO_0008 Documentation Discipline | PAS_CAL_PRO_0008_DOCUMENT_OMISSION | PROFESSION_WORK_STATE | EXECUTION | omission/error rate in recurring known documentation workflow | decrease | incorrect source data remains incorrect |
| PASSIVE_FAC_0002 Credential Navigation | PAS_CAL_FAC_0002_WORKFLOW_ERROR | INSTITUTIONAL_SERVICE_STATE | AUTHORIZATION_WORKFLOW | avoidable error/overhead in a known valid credential process | decrease | no authorization or clearance bypass |

## Required baseline data before assigning values

### Resource terms
Need:
- ordinary Focus/Resolve/Stamina cost ranges;
- normal recovery rates;
- maximum resources;
- action-time scale.

### Action terms
Need:
- base guard/evasion transition windows;
- action queue/initiative rules;
- equipment handling penalties;
- movement budget rules.

### Environmental terms
Need:
- temperature/exposure state model;
- performance-penalty bands;
- injury threshold model;
- acclimation-band representation.

### Error/confidence terms
Need:
- diagnostic/interpretation confidence scale;
- false-positive/false-negative handling;
- evidence quality representation.

### Work/procedure terms
Need:
- task duration scale;
- quality grades;
- material/consumable accounting;
- protocol-error representation.

## Candidate test anchors

Every parameter should eventually be tested at:
1. no passive;
2. passive newly qualified;
3. mature legitimate history;
4. favorable context;
5. adverse context;
6. same-term overlap with one other eligible passive;
7. cap boundary;
8. save/load round trip.

## Calibration rule

A coefficient should not be selected until:
- the base term exists;
- the unit is known;
- the passive's owner is known;
- the overlap resolver is known;
- scenario anchors are executable or at least numerically modelable.

## Result

This pilot validates the parameterization method while intentionally leaving all final values `TBD`.

No passive is canon-promoted and no runtime value is established by this file.
