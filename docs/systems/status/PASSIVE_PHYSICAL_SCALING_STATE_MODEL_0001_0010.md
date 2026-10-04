# THE GAME — Physical Passive Scaling & State Model 0001–0010

Status: **PHASE-C CALIBRATION / TARGET DESIGN / NOT IMPLEMENTED**

Parents:
- `PASSIVE_REGISTRY_SCHEMA.md`
- `PASSIVE_REQUIREMENT_LANGUAGE.md`
- `calibration/PASSIVE_DETAIL_PHYSICAL_0001_0010.md`
- `PASSIVE_PHYSICAL_KNOWLEDGE_REFINEMENT_0001_0010.md`

Purpose: define bounded scaling behavior, hard caps, and future authoritative state ownership for the first ten Physical Adaptation passives without inventing runtime code or numeric balance.

## Global scaling rules

1. These passives do not scale directly from Level by default.
2. Scaling comes from relevant training history, adaptation state, familiarity, recovery, and future calibrated attributes/skills.
3. Duplicate ownership never stacks duplicate copies.
4. Passive effects modify a bounded resolution term; they do not replace injury, stamina, attribute, skill, or primary-ability systems.
5. No physical passive may produce immunity.
6. Exact numeric coefficients remain `TBD` until a balance model exists.
7. Hidden progress is authoritative gameplay state and must not be reconstructed by Android/UI.

## State ownership vocabulary

Future implementation should separate:
- `qualification_state` — hidden counters/evidence proving unlock;
- `ownership_state` — passive acquired/revealed/active state;
- `adaptation_state` — any post-unlock scaling/proficiency;
- `effect_input` — authoritative runtime state the passive modifies;
- `projection_state` — player-safe public/self-known representation.

The exact engine module/file is intentionally not named until repository architecture mapping is performed.

---

## PASSIVE_PHY_0001 — Iron Tendons

Scaling axis:
- relevant high-load movement history;
- completed recovery;
- safe adaptation continuity.

Effect input:
- tendon-strain accumulation from tagged repeated-load actions.

Proposed scaling behavior:
- base passive provides a modest reduction to qualifying tendon-strain accumulation;
- later adaptation may improve efficiency within a capped band;
- scaling does not apply to catastrophic overload events above a future safety threshold.

Hard caps:
- tendon injury remains possible;
- no reduction to unrelated bone, joint, muscle, or organ injury;
- no raw Might increase.

Future authoritative ownership:
- qualification: training/adaptation evidence ledger;
- effect: injury/strain resolver;
- projection: revealed passive summary only.

Tests:
- repeated valid load gains benefit;
- one extreme overload still injures;
- duplicate passive does not double effect;
- non-tendon injuries unchanged.

---

## PASSIVE_PHY_0002 — Dense Bone

Scaling axis:
- long-term safe skeletal loading;
- recovery history;
- future medical/adaptation state.

Effect input:
- fracture/skeletal-stress resolution.

Proposed scaling:
- bounded improvement to fracture-resistance threshold or severity calculation;
- strongest within trained load/impact envelope;
- diminishing gains at advanced adaptation.

Hard caps:
- bones remain breakable;
- joints, organs, soft tissue unaffected unless another system applies;
- no armor rating against every damage type.

Future authoritative ownership:
- qualification: adaptation evidence;
- effect: skeletal injury resolver;
- projection: known passive + qualitative effect.

Tests:
- fracture risk changes only where applicable;
- extreme force can still fracture;
- no benefit to poison/heat/soft-tissue injury;
- self-fracture farming rejected.

---

## PASSIVE_PHY_0003 — Efficient Recruitment

Scaling axis:
- movement-pattern familiarity;
- quality of practice;
- neuromuscular adaptation history.

Effect input:
- efficiency/consistency of already available muscular output in a familiar movement.

Proposed scaling:
- reduces wasted effort and variance;
- may slightly improve stamina efficiency and force-expression consistency;
- benefit falls sharply for unfamiliar movements.

Hard caps:
- cannot exceed available muscle capacity;
- cannot grant Bioelectric Overdrive behavior;
- cannot directly raise base Might.

Future authoritative ownership:
- qualification: tagged training history;
- adaptation: per-pattern familiarity;
- effect: movement/task resolver.

Tests:
- familiar movement receives benefit;
- unfamiliar movement does not;
- raw stat remains unchanged;
- overdrive ability remains categorically stronger for burst output.

---

## PASSIVE_PHY_0004 — Load Bearer

Scaling axis:
- trained carried-load bands;
- posture control;
- sustained-load conditioning.

Effect input:
- encumbrance stamina/posture penalties.

Proposed scaling:
- reduces fatigue/posture penalty inside trained load bands;
- reduced or no benefit above trained load band;
- future progression can expand the trained band through legitimate conditioning.

Hard caps:
- actual mass unchanged;
- encumbrance never becomes zero at extreme load;
- joint/crush/fall injury remains possible.

Future authoritative ownership:
- qualification: load-session evidence;
- adaptation: trained-load band;
- effect: encumbrance/fatigue resolver.

Tests:
- trained load benefits;
- excessive load retains major penalties;
- no mass reduction;
- unsafe overload cannot farm qualification.

---

## PASSIVE_PHY_0005 — Shock Acclimation

Scaling axis:
- supervised/legitimate blunt-stress history;
- recovery;
- controlled exposure variety.

Effect input:
- stagger/disruption duration or severity after non-catastrophic blunt impact.

Proposed scaling:
- reduces performance disruption after qualifying impact;
- does not reduce authoritative damage by itself;
- strongest against familiar non-catastrophic shock patterns.

Hard caps:
- no damage immunity;
- concussion/internal injury remain authoritative;
- catastrophic impacts can exceed acclimation.

Future authoritative ownership:
- qualification: event provenance + recovery;
- effect: stagger/disruption resolver;
- injury remains separate state owner.

Tests:
- stagger reduced while damage unchanged;
- self-harm events do not qualify;
- catastrophic impact bypasses cap;
- overlap with Impact Cushion remains distinct.

---

## PASSIVE_PHY_0006 — Grip Endurance

Scaling axis:
- sustained grip history;
- climbing/tool/weapon retention practice;
- forearm recovery.

Effect input:
- grip-specific fatigue accumulation.

Proposed scaling:
- slows local grip-fatigue accumulation;
- advanced adaptation may improve recovery between grip actions;
- does not increase maximum instantaneous grip force.

Hard caps:
- tendon/nerve injury remains possible;
- no unlimited hanging/weapon retention;
- Grip Field synergy is capped.

Future authoritative ownership:
- qualification: tagged grip activity;
- effect: local fatigue resolver;
- projection: qualitative endurance benefit.

Tests:
- fatigue reduction only in grip-tagged tasks;
- maximum force unchanged;
- extreme duration still causes failure;
- ability synergy does not erase tissue limits.

---

## PASSIVE_PHY_0007 — Joint Stability

Scaling axis:
- trained movement range;
- rehabilitation/control work;
- repeated stable execution.

Effect input:
- minor instability/position-loss checks within trained range.

Proposed scaling:
- reduces probability/severity of minor instability;
- benefit is range-of-motion specific;
- rehabilitation may restore lost applicability after injury if later systems support it.

Hard caps:
- no ligament-tear immunity;
- extreme leverage bypasses protection;
- damaged joints can still fail.

Future authoritative ownership:
- qualification: movement/rehabilitation history;
- adaptation: trained-range tags;
- effect: joint stability/injury resolver.

Tests:
- benefit within trained range;
- reduced/absent benefit outside range;
- injury can disable/reduce effect;
- intentional destabilization farming rejected.

---

## PASSIVE_PHY_0008 — Sprint Economy

Scaling axis:
- repeated legitimate sprint conditioning;
- locomotion familiarity;
- recovery quality.

Effect input:
- stamina cost of sprint-tagged locomotion.

Proposed scaling:
- bounded reduction to stamina cost per qualifying sprint action;
- terrain/familiarity may modify benefit;
- top speed remains governed elsewhere.

Hard caps:
- no top-speed increase by passive alone;
- heat/oxygen/muscle limits remain;
- stamina cost never reaches zero.

Future authoritative ownership:
- qualification: sprint-session evidence;
- adaptation: locomotion/terrain familiarity if later approved;
- effect: movement stamina-cost resolver.

Tests:
- sprint cost reduced;
- walk/non-sprint actions unaffected unless explicitly tagged;
- top speed unchanged;
- heat/recovery systems still constrain use.

---

## PASSIVE_PHY_0009 — Core Bracing

Scaling axis:
- trained brace timing;
- load/impact context;
- posture familiarity.

Effect input:
- trunk-stability and force-transfer checks when a valid brace opportunity exists.

Proposed scaling:
- improves stability/force handling if the character successfully braces;
- no effect when surprised or unable to brace;
- advanced adaptation may widen the timing window modestly.

Hard caps:
- no blanket damage reduction;
- overwhelming force can break posture;
- internal injury remains possible.

Future authoritative ownership:
- qualification: brace/load training history;
- effect: posture/guard resolver;
- projection: known stability benefit.

Tests:
- benefit only during valid brace state;
- surprise hit receives no automatic benefit;
- overwhelming force still breaks posture;
- no duplicate application with unrelated guard modifiers.

---

## PASSIVE_PHY_0010 — Repetition Tolerance

Scaling axis:
- familiarity with one repeated task family;
- sustained legitimate work history;
- recovery.

Effect input:
- fatigue/performance-decay curve for familiar repeated physical work.

Proposed scaling:
- slows performance decay for tagged familiar tasks;
- benefit can differ by task family;
- adaptation may broaden only through actual experience.

Hard caps:
- no generic unlimited stamina;
- sleep, nutrition, recovery, and overuse injury remain;
- peak output does not rise.

Future authoritative ownership:
- qualification: task-tagged history;
- adaptation: per-task familiarity;
- effect: fatigue/work-capacity resolver.

Tests:
- familiar task benefits;
- unrelated task receives no benefit;
- overuse injury still accumulates;
- exhaustion farming cannot bypass recovery requirement.

---

# Cross-passive stacking rules

Potential additive stacking requires review when two records affect:
- the same fatigue channel;
- the same injury threshold;
- the same stamina-cost term;
- the same posture/stability calculation.

Default policy:
- independent mechanisms may coexist;
- identical modifier terms should combine through a capped resolver rather than unchecked multiplication;
- exact stacking math remains `TBD`.

Important overlap reviews:
- Iron Tendons + Joint Stability;
- Load Bearer + Core Bracing;
- Grip Endurance + Repetition Tolerance;
- Sprint Economy + Repetition Tolerance;
- Shock Acclimation + defensive/stagger passives;
- physical passives + primary defensive abilities.

# Hidden-progress state model

Before unlock:
- counters/evidence exist only in authoritative state;
- player projection exposes nothing unless external world knowledge independently reveals a method.

On qualification:
1. authority validates requirement packet;
2. passive ownership is created exactly once;
3. reveal transition is recorded;
4. player-safe projection gains the passive;
5. hidden exact threshold remains hidden unless knowledge rules say otherwise.

After unlock:
- adaptation scaling may continue if the passive design supports it;
- post-unlock scaling must not reuse hidden qualification counters blindly.

# Implementation mapping requirements

When implementation begins, each passive needs:
- exact state owner;
- event IDs and deduplication;
- save fields;
- migration;
- projection schema;
- stacking resolver;
- test fixtures;
- exploit tests;
- developer/debug visibility separate from player projection.

No runtime file/module is claimed by this design document.

# Phase-C result

Physical 0001–0010 now have:
- effect identity;
- unlock proposals;
- knowledge refinement;
- scaling direction;
- hard caps;
- future state ownership;
- test focus.

Still blocked:
- numeric coefficients;
- runtime architecture mapping;
- named institutions/history;
- final canon promotion.
