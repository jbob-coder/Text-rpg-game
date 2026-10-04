# THE GAME — Recovery Passive Scaling & State Model 0001–0010

Status: **PHASE-C CALIBRATION / TARGET DESIGN / NOT IMPLEMENTED**

Parents:
- `PASSIVE_REGISTRY_SCHEMA.md`
- `PASSIVE_REQUIREMENT_LANGUAGE.md`
- `calibration/PASSIVE_DETAIL_RECOVERY_0001_0010.md`

Purpose: define bounded scaling, caps, state ownership, stacking expectations, and implementation-test requirements for Recovery 0001–0010.

## Global recovery-state model

Future implementation should separate:
- `qualification_state` — hidden evidence that can unlock the passive;
- `ownership_state` — whether the passive exists for the character;
- `adaptation_state` — post-unlock history that may affect bounded scaling;
- `recovery_context` — current authoritative context such as rest, exertion, sleep, environment, or clearance;
- `effect_input` — the exact recovery term the passive modifies;
- `projection_state` — player-safe representation.

Rules:
1. Level does not directly scale these passives unless later approved.
2. Duplicate ownership does not stack.
3. Recovery effects never bypass their required context.
4. Two passives modifying the same resolver must use a capped stacking rule.
5. Hidden qualification counters never appear in normal player projection.

## PASSIVE_REC_0001 — Second Wind

Scaling axis:
qualifying exertion/recovery history and pacing discipline.

Effect input:
short-term Stamina rebound after a meaningful drop.

Cap:
one bounded benefit per activity window until a valid reset.

State owner:
activity-window and stamina-recovery authority.

Required tests:
- valid exertion permits one benefit;
- second attempt before reset does not repeat;
- trivial exertion does not qualify;
- unrelated Focus/Resolve state is unchanged.

## PASSIVE_REC_0002 — Rapid Lactate Clearance

Scaling axis:
high-intensity conditioning and between-effort recovery history.

Effect input:
between-effort fatigue-recovery time or penalty.

Cap:
never reaches zero recovery time.

State owner:
high-intensity fatigue/recovery authority.

Required tests:
- tagged high-intensity effort receives benefit;
- ordinary low-intensity activity does not gain the same modifier;
- cumulative fatigue still exists;
- duplicate ownership does not multiply.

## PASSIVE_REC_0003 — Deep Recovery

Scaling axis:
quality-rest history.

Effect input:
valid sleep/rest Stamina and Focus restoration.

Cap:
cannot exceed the future maximum recovery allowed for a normal rest cycle.

State owner:
sleep/rest authority.

Required tests:
- adequate sleep receives benefit;
- invalid or interrupted rest gives reduced/none according to future rules;
- no direct Health restoration is implied;
- no micro-rest exploit.

## PASSIVE_REC_0004 — Heat Recovery

Scaling axis:
safe heat-exposure recovery history.

Effect input:
post-exposure recovery penalty/duration.

Cap:
no active heat-resistance effect.

State owner:
environmental exposure + recovery authority.

Required tests:
- post-exposure state receives benefit;
- active exposure is not reduced by this passive alone;
- invalid farming does not advance qualification;
- stacking with future heat resistance remains bounded.

## PASSIVE_REC_0005 — Cold Recovery

Scaling axis:
safe cold-exposure recovery history.

Effect input:
post-exposure recovery penalty/duration.

Cap:
no active cold-resistance effect.

State owner:
environmental exposure + recovery authority.

Required tests:
- post-exposure state receives benefit;
- active exposure is not reduced by this passive alone;
- invalid farming does not advance qualification;
- future cold-resistance stacking remains bounded.

## PASSIVE_REC_0006 — Sleep Efficiency

Scaling axis:
consistent valid sleep history.

Effect input:
restorative efficiency of one adequate sleep cycle.

Cap:
requires a valid sleep cycle and cannot convert short rests into full sleep.

State owner:
sleep-quality/recovery authority.

Required tests:
- valid sleep gains bounded improvement;
- invalid sleep does not receive full benefit;
- repeated short sleeps cannot duplicate one full-cycle reward;
- Deep Recovery stacking uses one capped resolver.

## PASSIVE_REC_0007 — Breath Reserve

Scaling axis:
breathing practice and exertion history.

Effect input:
short oxygen-demand spike tolerance/recovery.

Cap:
finite duration; no oxygen creation.

State owner:
oxygen-demand/breathing authority.

Required tests:
- short demand spike gains benefit;
- prolonged zero-input state still reaches failure according to normal rules;
- no underwater-breathing behavior;
- unrelated stamina recovery does not silently inherit the modifier.

## PASSIVE_REC_0008 — Pain Recovery

Scaling axis:
history of successful recovery after stabilized pain states.

Effect input:
lingering performance penalty after stabilization.

Cap:
does not erase active authoritative pain state or unrelated condition state.

State owner:
pain/recovery authority.

Required tests:
- stabilized state receives benefit;
- active unresolved state does not receive the same modifier;
- underlying condition remains separate;
- no hidden-state leak in player projection.

## PASSIVE_REC_0009 — Microtear Repair

Scaling axis:
training/recovery consistency.

Effect input:
ordinary recovery of training-scale muscle microdamage.

Cap:
does not enter major-regeneration logic.

State owner:
training-recovery / muscle-recovery authority.

Required tests:
- training-scale recovery receives bounded improvement;
- major recovery state does not route through this passive;
- overlap with Knit Flesh/Adaptive Regeneration is not additive without a resolver;
- recovery context remains required.

## PASSIVE_REC_0010 — Recovery Discipline

Scaling axis:
consistent adherence to valid recovery windows.

Effect input:
avoidable return-to-activity penalties once a valid clearance threshold is reached.

Cap:
cannot make an invalid return state valid.

State owner:
recovery-plan / clearance authority.

Required tests:
- valid cleared return can reduce avoidable penalty;
- blocked return remains blocked;
- repeated cycling cannot farm progress;
- behavior state remains distinct from raw resource recovery.

# Cross-passive stacking

Highest-risk overlaps:
- Second Wind + Rapid Lactate Clearance;
- Deep Recovery + Sleep Efficiency;
- Heat Recovery + future heat resistance;
- Cold Recovery + future cold resistance;
- Pain Recovery + future pain-tolerance passives;
- Microtear Repair + healing abilities;
- Recovery Discipline + profession/mental habit passives.

Default rule:
Different mechanisms may coexist, but any two effects touching the same authoritative term must enter one capped resolver rather than multiply independently.

# Hidden qualification lifecycle

Before qualification:
- authoritative counters/evidence may exist;
- Status reveals no passive name, slot, progress percentage, or exact threshold unless separate world knowledge allows a method to be known.

On qualification:
1. validate evidence;
2. create ownership once;
3. record reveal transition;
4. update player-safe projection;
5. preserve exact hidden threshold according to knowledge rules.

After qualification:
- post-unlock adaptation history, if used, must be separated from the original unlock counters.

# Implementation gate

Before runtime work, each recovery passive needs:
- concrete engine state owner;
- event/evidence identifiers;
- save fields;
- migration behavior;
- player-safe projection fields;
- stacking resolver;
- unit/integration tests;
- exploit tests;
- debug-only visibility.

No runtime file/module is claimed here.
