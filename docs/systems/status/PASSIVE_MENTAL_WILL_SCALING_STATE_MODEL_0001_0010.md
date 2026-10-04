# THE GAME — Mental / Will Passive Scaling & State Model 0001–0010

Status: **PHASE-C CALIBRATION / TARGET DESIGN / NOT IMPLEMENTED**

Parents:
- `PASSIVE_REGISTRY_SCHEMA.md`
- `PASSIVE_REQUIREMENT_LANGUAGE.md`
- `calibration/PASSIVE_DETAIL_MENTAL_WILL_0001_0010.md`

Purpose: define bounded scaling, state ownership, reset semantics, overlap handling, and test expectations for Mental / Will 0001–0010.

## Global mental/will state model

Future implementation should separate:
- `qualification_state` — hidden legitimate stress/recovery evidence;
- `ownership_state` — passive acquired/revealed;
- `stress_state` — current acute/sustained pressure context;
- `fear_state` — fear response and post-fear recovery state;
- `pain_state` — pain/distraction state separate from injury authority;
- `focus_state` — Focus resource and concentration degradation;
- `resolve_state` — Resolve resource and drain;
- `task_state` — current task, familiarity, progress, interruption severity;
- `recovery_state` — completed post-event recovery and return toward baseline;
- `projection_state` — player-safe representation.

Rules:
1. Level does not directly scale these passives by default.
2. Emotional state is not deleted merely because task degradation is reduced.
3. Injury state remains separate from pain distraction.
4. Same-resolver effects enter one capped composition path.
5. Hidden progress is never exposed before legitimate qualification.
6. Qualification cannot reward deliberate self-harm or engineered trauma.
7. Exact numeric coefficients remain `TBD`.

## WIL_0001 — Stress Lock

Scaling axis:
legitimate familiar-task performance under acute stress plus completed recovery.

Effect input:
acute-stress task-quality degradation.

Cap:
cannot remove all stress penalties or emotional consequences.

State owner:
stress + task-performance authority.

Tests:
- familiar task under acute stress gains bounded benefit;
- unfamiliar task does not inherit full benefit;
- post-event recovery still required;
- emotional state remains present.

## WIL_0002 — Fear Processing

Scaling axis:
recognized fear-event recovery history.

Effect input:
post-fear decision-quality recovery penalty/duration.

Cap:
does not prevent initial fear response.

State owner:
fear/recovery authority.

Tests:
- resolved fear event recovers decision quality faster;
- active fear remains active;
- no fear immunity;
- unsafe repeated fear farming rejected.

## WIL_0003 — Pain Compartmentalization

Scaling axis:
history of functioning after properly stabilized painful conditions.

Effect input:
pain-related attention/distraction penalty.

Cap:
injury severity, unsafe-use warnings, and physical penalties remain.

State owner:
pain-distraction authority interfacing with injury state.

Tests:
- stabilized pain distraction reduced;
- injury penalties unchanged;
- unstabilized critical condition does not gain inappropriate benefit;
- no self-injury qualification exploit.

## WIL_0004 — Focus Under Fire

Scaling axis:
trained-task continuity during legitimate external threat.

Effect input:
threat-induced concentration degradation.

Cap:
direct hit/stagger/incapacitation remain interruptions.

State owner:
threat context + concentration authority.

Tests:
- valid threat pressure receives benefit;
- no-threat task does not receive special modifier;
- direct disruption still interrupts;
- collusive fake-threat farming rejected.

## WIL_0005 — Interruption Resistance

Scaling axis:
successful resumption of familiar tasks after minor interruptions.

Effect input:
task-progress loss and reorientation cost.

Cap:
major interruptions can still fully break progress where the task model says so.

State owner:
task-progress/interruption authority.

Tests:
- minor interruption preserves more context;
- major interruption remains major;
- unrelated task does not inherit context;
- save/reload cannot duplicate progress.

## WIL_0006 — Patience Engine

Scaling axis:
verified long-duration deliberate tasks.

Effect input:
impatience/low-action performance-decay term.

Cap:
fatigue, sleep need, and Focus cost remain.

State owner:
long-task/vigilance authority.

Tests:
- long deliberate task stays stable longer;
- idle waiting alone does not qualify;
- sleep deprivation still degrades performance;
- Cognitive Endurance overlap capped.

## WIL_0007 — Crisis Clarity

Scaling axis:
reviewed emergency prioritization history.

Effect input:
time-pressure prioritization error/decision-order burden.

Cap:
cannot create missing expertise or hidden information.

State owner:
crisis-decision authority.

Tests:
- known emergency options prioritized more consistently;
- unknown correct answer not revealed;
- no free Tactics/Medicine/Leadership skill;
- non-crisis decision does not gain same modifier.

## WIL_0008 — Resolve Reserve

Scaling axis:
sustained-pressure history and recovery.

Effect input:
Resolve drain during one defined stress window.

Cap:
one bounded reduction per qualifying window; no repeated micro-window reset exploit.

State owner:
Resolve + stress-window authority.

Tests:
- one qualifying window gains benefit;
- repeated micro-events do not retrigger;
- window reset requires valid recovery/state transition;
- no Resolve creation beyond allowed conservation.

## WIL_0009 — Emotional Recovery

Scaling axis:
history of resolved intense events and successful return toward baseline.

Effect input:
lingering post-event performance disruption.

Cap:
does not force emotional state to zero or erase memory.

State owner:
post-event recovery authority.

Tests:
- resolved event recovery improves;
- unresolved event remains unresolved;
- personality/relationship state not overwritten;
- no instant reset after every emotion change.

## WIL_0010 — Cognitive Endurance

Scaling axis:
long-duration reasoning/vigilance history.

Effect input:
Focus degradation over qualifying cognitive work.

Cap:
sleep/fatigue and maximum Focus remain authoritative.

State owner:
Focus + cognitive-task authority.

Tests:
- prolonged reasoning loses Focus more slowly;
- short burst reasoning gets little/no special advantage;
- no Intellect increase;
- no Time Partition behavior.

# Cross-passive composition

Highest-risk overlaps:
- Stress Lock + Focus Under Fire;
- Fear Processing + Emotional Recovery;
- Pain Compartmentalization + Pain Recovery;
- Focus Under Fire + Interruption Resistance;
- Patience Engine + Cognitive Endurance;
- Resolve Reserve + future recovery/resource passives.

Default rule:
Different mechanisms may coexist, but effects touching the same authoritative degradation/drain term must use one capped resolver rather than multiply independently.

# Hidden qualification lifecycle

Before qualification:
- meaningful-event and recovery counters may exist internally;
- normal Status projection exposes no name, slot, exact threshold, or progress percentage.

On qualification:
1. validate event legitimacy;
2. validate completed recovery;
3. verify demonstrated functional decision quality where required;
4. create ownership once;
5. reveal only player-safe effect information.

After qualification:
Post-unlock adaptation history, if used, remains separate from original unlock counters.

# Anti-exploit rule

Invalid qualification evidence includes:
- deliberate self-harm;
- staged fake emergencies with no meaningful pressure;
- collusive threat loops;
- save/reload duplication;
- trivial repeated interruptions;
- deliberate sleep deprivation solely to farm stress evidence;
- repeated intentional fear induction where the activity has no legitimate purpose.

# Implementation gate

Before runtime work:
- define stress/fear/pain/focus/resolve state ownership;
- define stress-window lifecycle;
- define task familiarity;
- define interruption severity;
- define recovery completion;
- define projection filtering;
- define save/migration behavior;
- add anti-farm and state-reset tests.

No runtime module is claimed here.
