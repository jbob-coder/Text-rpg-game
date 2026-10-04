# THE GAME — Movement Passive Scaling & State Model 0001–0010

Status: **PHASE-C CALIBRATION / TARGET DESIGN / NOT IMPLEMENTED**

Parents:
- `PASSIVE_REGISTRY_SCHEMA.md`
- `PASSIVE_REQUIREMENT_LANGUAGE.md`
- `calibration/PASSIVE_DETAIL_MOVEMENT_0001_0010.md`

Purpose: define bounded scaling, caps, authoritative state categories, overlap handling, and implementation tests for Movement 0001–0010.

## Global movement state model

Future implementation should separate:
- `qualification_state` — hidden evidence proving unlock;
- `ownership_state` — acquired/revealed state;
- `movement_familiarity_state` — terrain/motion/route families known through history;
- `movement_context` — current surface, load, velocity, obstacle, posture, injury, and equipment;
- `effect_input` — exact movement resolver term modified;
- `projection_state` — player-safe representation.

Rules:
1. Level does not directly scale these passives by default.
2. Duplicate ownership does not stack.
3. A movement passive only modifies its named resolver/context.
4. No movement passive bypasses authoritative injury or environment failure.
5. Same-resolver effects enter one capped composition rule.
6. Hidden qualification counters never appear in ordinary player projection.
7. Exact coefficients remain `TBD`.

## PASSIVE_MOV_0001 — Sure Foot

Scaling axis:
terrain-family familiarity and successful legitimate traversal history.

Effect input:
minor slip/footing-error probability or correction burden on qualifying familiar terrain.

Cap:
cannot remove severe hazard/fall outcomes.

State owner:
surface/terrain traversal authority.

Tests:
- familiar qualifying terrain receives benefit;
- unfamiliar terrain receives reduced/none;
- overwhelming hazard still resolves normally;
- duplicate ownership does not stack.

## PASSIVE_MOV_0002 — Quiet Landing

Scaling axis:
controlled landing history within trained envelope.

Effect input:
avoidable landing noise and movement disruption.

Cap:
does not reduce authoritative fall severity beyond what separate systems allow.

State owner:
landing/noise movement authority.

Tests:
- valid controlled landing gains benefit;
- outside-envelope landing does not inherit full benefit;
- Stealth remains separate;
- Fall Roll overlap is capped.

## PASSIVE_MOV_0003 — Lateral Burst

Scaling axis:
practiced lateral initiation history.

Effect input:
first-step hesitation/efficiency for qualifying lateral starts.

Cap:
no direct top-speed increase.

State owner:
movement initiation authority.

Tests:
- practiced lateral start gains benefit;
- forward/unrelated start does not;
- poor traction still limits output;
- Direction Change does not double first-step benefit.

## PASSIVE_MOV_0004 — Balance Recovery

Scaling axis:
legitimate recovery history from non-injury balance loss.

Effect input:
time/cost to return from minor balance-loss state to stable locomotion.

Cap:
does not cancel knockdown/injury states.

State owner:
balance/posture recovery authority.

Tests:
- minor stumble recovery improves;
- injury/knockdown remains authoritative;
- engineered repeated falls do not qualify;
- save/reload cannot duplicate evidence.

## PASSIVE_MOV_0005 — Vault Habit

Scaling axis:
obstacle-family familiarity and valid vault completions.

Effect input:
setup hesitation and stamina cost of qualifying vault actions.

Cap:
physical obstacle capability remains unchanged.

State owner:
obstacle traversal authority.

Tests:
- familiar valid vault gains benefit;
- impossible obstacle remains impossible;
- carried-load penalties remain;
- trivial obstacle loop rejected for qualification.

## PASSIVE_MOV_0006 — Climb Economy

Scaling axis:
surface/route-family familiarity and sustained climbing history.

Effect input:
climb-specific stamina/fatigue cost.

Cap:
grip strength, equipment, route difficulty, and fall risk remain separate.

State owner:
climbing traversal authority.

Tests:
- familiar climb receives bounded economy;
- unfamiliar/technical route retains normal challenge;
- Grip Endurance overlap uses capped composition;
- no wall-cling behavior emerges.

## PASSIVE_MOV_0007 — Terrain Reader

Scaling axis:
terrain observation linked to subsequent traversal outcomes.

Effect input:
route-choice quality modifier or avoidable route-selection penalty.

Cap:
cannot reveal unobserved hidden information or guarantee optimal route.

State owner:
terrain observation/route-evaluation authority.

Tests:
- observed hazards can inform route benefit;
- hidden hazard remains hidden;
- no free map knowledge;
- Investigation/Perception remain separate.

## PASSIVE_MOV_0008 — Long Stride

Scaling axis:
sustained travel history and gait familiarity.

Effect input:
long-duration locomotion stamina/efficiency term.

Cap:
does not raise top speed or eliminate environmental/recovery cost.

State owner:
travel locomotion authority.

Tests:
- sustained travel receives benefit;
- sprint-only action does not receive same modifier;
- heat/load terrain costs remain;
- Sprint Economy overlap is bounded.

## PASSIVE_MOV_0009 — Fall Roll

Scaling axis:
legitimate controlled landing/roll practice inside survivable envelope.

Effect input:
avoidable disruption and force-distribution term during qualifying fall landing.

Cap:
fall severity/injury authority cannot be bypassed.

State owner:
fall/landing authority plus injury resolver interface.

Tests:
- valid survivable fall with roll opportunity can gain bounded benefit;
- no roll opportunity means no activation;
- severe fall remains severe;
- unsafe self-endangerment does not advance qualification;
- Impact Cushion overlap remains bounded.

## PASSIVE_MOV_0010 — Direction Change

Scaling axis:
practiced directional-transition history across qualifying traction conditions.

Effect input:
avoidable momentum loss/transition cost during a practiced turn.

Cap:
does not cancel inertia, traction limits, or turn-radius constraints.

State owner:
locomotion direction/velocity authority.

Tests:
- practiced turn preserves bounded efficiency;
- insufficient traction still limits turn;
- no kinetic energy storage;
- Lateral Burst overlap is separated by initiation versus transition.

# Cross-passive composition

High-risk overlaps:
- Quiet Landing + Fall Roll;
- Lateral Burst + Direction Change;
- Climb Economy + Grip Endurance;
- Long Stride + Sprint Economy;
- Sure Foot + Joint Stability;
- Balance Recovery + future defensive recovery passives.

Default rule:
If two effects modify the same authoritative term, use one capped resolver. Do not multiply percentage reductions independently.

# Hidden qualification lifecycle

Before qualification:
- counters/evidence may exist internally;
- normal Status projection shows no name, slot, exact threshold, or progress percentage.

On qualification:
1. validate meaningful evidence;
2. create ownership once;
3. record reveal transition;
4. expose only allowed player-safe fields;
5. preserve knowledge asymmetry.

After qualification:
Post-unlock familiarity/adaptation state, if used, remains separate from original unlock counters.

# Implementation gate

Before runtime work each movement passive needs:
- concrete engine state owner;
- event/evidence IDs;
- save fields;
- migration behavior;
- stacking resolver;
- projection fields;
- exploit tests;
- movement integration tests;
- debug-only hidden-state inspection.

No runtime module is claimed here.
