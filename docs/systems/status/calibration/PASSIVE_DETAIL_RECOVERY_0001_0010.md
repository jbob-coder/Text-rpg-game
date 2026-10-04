# THE GAME — Recovery Passive Detail 0001–0010

Status: **RECONSTRUCTION-GRADE CALIBRATION DRAFT / NOT CANON UNTIL PROMOTED / NOT IMPLEMENTED**

Parents:
- `../PASSIVE_REGISTRY_SCHEMA.md`
- `../PASSIVE_REQUIREMENT_LANGUAGE.md`
- `../STATUS_KNOWLEDGE_VISIBILITY_STANDARD.md`
- `PASSIVES_WAVE_001.md`
- `PASSIVE_UNLOCK_PATHS_WAVE_001.md`
- `PASSIVE_KNOWLEDGE_WAVE_001.md`

Purpose: deepen the first ten Recovery passive records while preserving hidden qualification, legitimate recovery history, and bounded effects.

Global rules:
- recovery passives improve recovery efficiency or discipline rather than creating instant restoration;
- exact numeric thresholds remain calibration proposals;
- trivial repetition and artificial farming do not count;
- rest quality and relevant character state continue to matter;
- hidden progress remains authoritative and player-invisible until qualification or discovery permits disclosure.

## PASSIVE_REC_0001 — Second Wind

Effect:
Once per demanding activity window, improves recovery from ordinary exertion after a verified meaningful stamina drop and a valid recovery opportunity.

Boundaries:
- not an instant stamina refill;
- cannot trigger repeatedly without reset conditions;
- does not bypass other active penalties.

Acquisition:
Linked proposal `UNLOCK_REC_0001`: six qualifying recovery cycles in the current calibration table.

Scaling:
Recovery history and pacing quality; not Level alone.

Cap:
One bounded recovery event per activity window until reset conditions are satisfied.

Knowledge:
`KNOW_REC_0001`; broad method known, exact threshold hidden.

Implementation needs:
activity-window state, recovery-event validation, reset state, stamina-recovery resolver.

## PASSIVE_REC_0002 — Rapid Lactate Clearance

Effect:
Speeds recovery from high-intensity exertion fatigue between efforts.

Boundaries:
- applies to short-duration exertion recovery;
- does not erase total fatigue;
- does not affect unrelated Focus or Resolve recovery by default.

Acquisition:
`UNLOCK_REC_0002`: seven qualifying recovery cycles.

Scaling:
Relevant conditioning and recovery history.

Cap:
Between-effort recovery can improve but never becomes zero-time.

Knowledge:
`KNOW_REC_0002`; public rumor is incomplete.

Implementation needs:
high-intensity fatigue tag, between-effort state, qualifying-history validator.

## PASSIVE_REC_0003 — Deep Recovery

Effect:
Improves rest-based Stamina and Focus recovery when adequate sleep conditions are met.

Boundaries:
- adequate sleep remains required;
- interruption or poor conditions can reduce the benefit;
- does not turn short sleep into full recovery.

Acquisition:
`UNLOCK_REC_0003`: eight qualifying recovery cycles.

Scaling:
Long-term quality-rest history.

Cap:
Cannot exceed future maximum-restoration rules for a valid rest cycle.

Knowledge:
`KNOW_REC_0003`; institutions know more than the public.

Implementation needs:
sleep quality, duration, interruption, environment, Stamina/Focus recovery integration.

## PASSIVE_REC_0004 — Heat Recovery

Effect:
Improves post-exertion recovery after safe heat exposure.

Boundaries:
- not general heat resistance;
- applies during recovery rather than active exposure;
- environment and character condition still matter.

Acquisition:
`UNLOCK_REC_0004`: nine qualifying recovery cycles.

Scaling:
Safe acclimation and recovery history.

Cap:
Does not remove the need for a valid recovery state.

Knowledge:
`KNOW_REC_0004`; current compact profile is heavily restricted and requires world justification.

Implementation needs:
heat-exposure history, recovery-state resolution, anti-farm rules.

## PASSIVE_REC_0005 — Cold Recovery

Effect:
Improves post-exposure recovery after safe cold stress.

Boundaries:
- not general cold resistance;
- applies after exposure;
- does not replace ordinary recovery requirements.

Acquisition:
`UNLOCK_REC_0005`: ten qualifying recovery cycles.

Scaling:
Safe acclimation and recovery history.

Cap:
No immunity or zero-time recovery.

Knowledge:
`KNOW_REC_0005`; public profile includes incomplete/incorrect beliefs that require explicit later authoring.

Implementation needs:
cold-exposure state, qualifying recovery evidence, anti-farm rules.

## PASSIVE_REC_0006 — Sleep Efficiency

Effect:
Improves the restorative value of an otherwise adequate sleep period.

Boundaries:
- adequate sleep remains required;
- no direct daytime resource generation;
- short repeated rests cannot replace one valid sleep cycle by default.

Acquisition:
`UNLOCK_REC_0006`: six qualifying recovery cycles.

Scaling:
Consistent sleep quality and routine history.

Cap:
Benefit applies only inside a valid sleep-recovery calculation.

Knowledge:
`KNOW_REC_0006`; existence broadly known, exact qualification hidden.

Implementation needs:
sleep-cycle state, quality evaluator, recovery cap, micro-rest exploit protection.

## PASSIVE_REC_0007 — Breath Reserve

Effect:
Improves tolerance to short oxygen-demand spikes through trained breathing efficiency.

Boundaries:
- does not create oxygen;
- applies to short demand spikes rather than indefinite deprivation;
- no underwater-breathing effect.

Acquisition:
`UNLOCK_REC_0007`: seven qualifying recovery cycles.

Scaling:
Breathing practice, exertion recovery, and conditioning history.

Cap:
No indefinite breath-holding behavior.

Knowledge:
`KNOW_REC_0007`; competing theories remain part of the calibration profile.

Implementation needs:
oxygen-demand state, breathing-efficiency term, short-spike duration, recovery interaction.

## PASSIVE_REC_0008 — Pain Recovery

Effect:
Reduces lingering performance penalties after a painful condition has been stabilized.

Boundaries:
- applies after stabilization;
- does not hide active authoritative state;
- pain and underlying condition remain separate concepts.

Acquisition:
`UNLOCK_REC_0008`: eight qualifying recovery cycles.

Scaling:
Relevant recovery history.

Cap:
Cannot erase every lingering penalty.

Knowledge:
`KNOW_REC_0008`; current all-unknown profile should be reviewed later rather than silently promoted.

Implementation needs:
pain-state separation, stabilization flag, lingering-penalty resolver.

## PASSIVE_REC_0009 — Microtear Repair

Effect:
Slightly improves ordinary recovery from training-scale muscle microdamage when normal recovery requirements are met.

Boundaries:
- training-scale recovery only;
- not major regeneration;
- does not duplicate Adaptive Regeneration;
- requires a valid recovery context.

Acquisition:
`UNLOCK_REC_0009`: nine qualifying recovery cycles.

Scaling:
Recovery consistency and relevant training history.

Cap:
Major recovery states remain outside this passive.

Knowledge:
`KNOW_REC_0009`; effect known, exact trigger details restricted in the current profile.

Implementation needs:
training-recovery state, muscle-recovery channel, overlap tests with healing abilities.

## PASSIVE_REC_0010 — Recovery Discipline

Effect:
Improves adherence to recovery windows and reduces avoidable penalties when resuming activity at legitimately cleared thresholds.

Boundaries:
- behavior/consistency oriented;
- does not shorten every required recovery period;
- cannot override a blocked return state.

Acquisition:
`UNLOCK_REC_0010`: ten qualifying recovery cycles.

Scaling:
Consistency of appropriate recovery behavior over time.

Cap:
Cannot convert an invalid return state into a valid one.

Knowledge:
`KNOW_REC_0010`; current misinformation/restriction profile requires later world justification.

Implementation needs:
clearance state, recovery-plan adherence, return-state logic, hidden qualification history.

# Family-level consistency rules

1. Recovery passives improve recovery, not instantaneous restoration.
2. Qualification comes from legitimate recovery history.
3. Effects touching the same recovery term require capped stacking.
4. Recovery passives do not silently become resistance passives.
5. Recovery passives do not silently become primary healing abilities.
6. Exact thresholds and knowledge profiles remain calibration proposals.

# Major overlap checks

- Second Wind ↔ stamina recovery.
- Deep Recovery ↔ Sleep Efficiency.
- Heat Recovery ↔ future environmental resistance.
- Cold Recovery ↔ future environmental resistance.
- Pain Recovery ↔ future pain-tolerance effects.
- Microtear Repair ↔ Knit Flesh / Adaptive Regeneration.
- Recovery Discipline ↔ profession/medical/mental habit passives.

# Promotion blockers

Before canon promotion:
- exact recovery-state model;
- numeric scaling/caps;
- knowledge classification review;
- false-rumor authoring;
- overlap tests;
- named institutions/history;
- runtime state-owner mapping.
