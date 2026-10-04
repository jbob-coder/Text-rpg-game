# THE GAME — Medical / Recovery Practice Passive Scaling & State Model 0001–0010

Status: **PHASE-C CALIBRATION / NOT CANON / NOT IMPLEMENTED**

Purpose: define bounded scaling and authoritative state categories for `PASSIVE_MED_0001`–`PASSIVE_MED_0010`.

## Shared state

Future implementation should distinguish:
- `qualification_state`;
- `ownership_state`;
- `supervision_state`;
- `medical_case_state`;
- `protocol_state`;
- `patient_observation_state`;
- `contamination_state`;
- `rehabilitation_plan_state`;
- `quality_review_state`;
- `projection_state`.

## Per-record model

| ID | Effect input | Scaling direction | Hard cap |
|---|---|---|---|
| MED_0001 | triage ordering overhead/error | supervised reviewed case history | no hidden diagnosis revelation |
| MED_0002 | execution variance in learned control procedure | validated supervised practice | underlying injury severity remains |
| MED_0003 | routine contamination error risk | verified sterile-procedure history | no immunity to contaminated inputs |
| MED_0004 | recovery-change recognition burden | monitored case history with confirmed observations | no automatic cause/diagnosis |
| MED_0005 | structured pain-assessment inconsistency | supervised assessment history | patient report and uncertainty remain authoritative |
| MED_0006 | fine motor steadiness in practiced stabilization | validated procedure history | no substitute for missing tools/knowledge |
| MED_0007 | handling/protocol error | reviewed known-protocol practice | no authority beyond known protocol |
| MED_0008 | adjustment error within an authorized rehab plan | supervised rehabilitation cases | no unrestricted treatment design |
| MED_0009 | recall burden for known injury presentations | verified prior case exposure | novel presentations remain uncertain |
| MED_0010 | communication breakdown under patient distress | supervised patient-contact history | cannot force calm or compliance |

## Qualification rules

The compact records currently require:
- supervised cases;
- protocol adherence;
- qualifying windows without negligence-caused patient harm.

Future qualification must:
1. bind evidence to stable case IDs;
2. verify supervision where required;
3. count each qualifying case once;
4. require protocol adherence for the counted event;
5. distinguish unavoidable adverse outcome from negligent procedure failure;
6. keep exact hidden progress out of ordinary Status projection.

## Cross-family overlap watchlist

- Triage Reflex ↔ Crisis Clarity;
- Bleeding Control Habit ↔ Medicine skill;
- Sterile Routine ↔ Technical/Craft Clean Assembly;
- Recovery Monitoring ↔ Sensory/Investigation;
- Pain Assessment ↔ Empathy / Pain Compartmentalization;
- Stabilization Hands ↔ Fine Motor Calibration;
- Medication Discipline ↔ Technical procedure passives;
- Rehabilitation Insight ↔ Recovery/Physical families;
- Injury Pattern Memory ↔ Cognitive memory passives;
- Patient Calm ↔ Social/Behavioral Calm Presence.

Same-resolver effects use one capped composition path.

## Required tests

- passives do not expose hidden diagnoses;
- patient state remains authoritative;
- missing supplies/tools cannot be fabricated;
- duplicate case IDs do not double-count qualification;
- protocol failure cannot qualify merely because the case completed;
- save/load preserves case evidence and ownership exactly once;
- player-safe projection omits hidden medical/internal fields unless legitimately known.

No runtime module is claimed here.
