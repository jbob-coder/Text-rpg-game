# THE GAME — Gate Twelve Progression Proof Packet

Status: **ACTIVE TARGET-GAME DESIGN / D-045 MATERIALIZED CHILD / DOCUMENTATION-ONLY PROOF PACKET**  
Task: **Parallel P16 / D-045**  
Owner: **Veyra / PLAYER_VEYRA**  
Authority boundary: this packet reconstructs one bounded Gate Twelve progression route across existing and target progression contracts. It does **not** implement class, profession, rank, mentor, facility, training-path, save-schema, or Android changes.

Read with:

- `docs/systems/PROGRESSION_CLASSES_RANKS_EVOLVED_GAME_DESIGN.md`
- `docs/systems/EVOLVED_SKILL_REGISTRY.md`
- `docs/systems/COMBAT_CLASS_CATALOG.md`
- `docs/systems/PROFESSION_RANK_STATUS_NAMESPACE_STANDARD.md`
- `docs/systems/TRAINING_MENTOR_FACILITY_PROGRESSION_STANDARD.md`
- `docs/systems/PHASE_1_PROGRESSION_SCHEMA_API_MIGRATION_PACKET.md`
- `docs/evidence/D066_PHASE1_PROGRESSION_PROOF_2026-10-04.md`
- `docs/evidence/D068_PHASE1_ACTIVITY_PROOF_2026-10-04.md`

---

# 1. Purpose

This packet proves that the evolved progression contracts can be applied to one already-authored Gate Twelve route without inventing a second progression engine or pretending that target class/profession/rank systems already exist.

The bounded route is built around CURRENT Trace Echo progression and Trace Chamber training evidence:

`ABILITY_TRACE_ECHO`
-> `TECHNIQUE_SIGNAL_PULSE`
-> authored practice
-> durable ability/technique mastery
-> world-time/resource cost
-> save/load and deterministic replay
-> player-safe Android projection.

A second CURRENT seam, `TRAIN_POWER_FUNDAMENTALS_TWO_HOURS`, proves that the same Gate Twelve/Trace Chamber context can train the registered `powers` skill through the current activity/simulation owner.

The evolved-game question is therefore not whether Gate Twelve has progression evidence. It does. The question is how that evidence should connect to future class, profession, rank, mentor, facility and UX systems without silently converting design proposals into runtime truth.

---

# 2. Authority labels

Every statement below is one of three kinds.

## 2.1 CURRENT

CURRENT means source/evidence already proves the behavior or identity in the existing game.

CURRENT in this packet includes:

- the registered `powers` skill;
- `ABILITY_TRACE_ECHO`;
- `TECHNIQUE_SIGNAL_PULSE`;
- the D-066 one-hour Signal Pulse practice route;
- existing ability/technique mastery and resources;
- `TRACE_CHAMBER` as a current specialized Trace Echo practice/training/recovery environment;
- `TRAIN_POWER_FUNDAMENTALS_TWO_HOURS` in `TRACE_STABILIZATION_HUB`;
- current world-time and resource costs;
- current save schema v1;
- the current player-safe ability/technique projection proven by D-066.

## 2.2 TARGET

TARGET means the evolved design intends the concept, but no claim is made that the complete runtime owner exists.

TARGET in this packet includes:

- class acquisition through evidence;
- Ability Specialist progression;
- profession qualification and profession grade;
- training-path orchestration;
- mentor/evaluator capability;
- facility capability;
- advanced plateau/evidence gates;
- player-safe training/class/profession UX.

## 2.3 PROPOSAL

PROPOSAL means a namespace, record, content binding, threshold, or world fact is not yet canon/runtime authority.

Examples here include:

- `CLASS_ABILITY_SPECIALIST` as the proposed Ability Specialist ID;
- `TRAINING_PATH_*`;
- `MENTOR_CAP_*`;
- `EVAL_CAP_*`;
- `FACILITY_CAP_*`;
- `PROF_*` and `PROF_GRADE_*`;
- any future named mentor, evaluator, institution, certification, profession, or facility binding not already present as current authored authority.

No PROPOSAL in this packet is promoted to CURRENT merely because it participates in the proof model.

---

# 3. Current Gate Twelve progression evidence

## 3.1 D-066 — Trace Echo mastery proof

D-066 verified the following bounded route:

1. discover `ABILITY_TRACE_ECHO` through the authored Gate Twelve path;
2. discover `TECHNIQUE_SIGNAL_PULSE`;
3. execute `PRACTICE_SIGNAL_PULSE_ONE_HOUR`;
4. increase technique mastery;
5. increase ability mastery;
6. pay the authoritative stamina/focus/world-time costs;
7. save and load;
8. preserve the selected mastery/resource/time values;
9. reproduce the selected result across a save boundary;
10. project only discovered/player-safe progression into Android.

The proof passed its final isolated verification at PR #42 / workflow run #319 (`37250623837`): Python 319/319, Android JVM/build/package PASS, API-35 emulator 35/35 PASS.

This is CURRENT evidence of ability and technique progression. It is not evidence that a combat class or profession has been acquired.

## 3.2 D-068 — Powers skill training proof

D-068 verified the authored choice `TRAIN_POWER_FUNDAMENTALS_TWO_HOURS` in `TRACE_STABILIZATION_HUB` at `TRACE_CHAMBER`.

CURRENT contract:

- subject: `powers`;
- duration: 120 minutes;
- intensity: 1;
- authored requirements: stamina >= 16, focus >= 10;
- exact authoritative result from the zero/absent starting skill state: Powers -> 2.0;
- exact resource result: -16 stamina, -10 focus;
- exact time result: +120 minutes;
- save/load preservation;
- Android delegates the exact choice and consumes returned authoritative state.

This is CURRENT skill-training evidence. It is not profession qualification, class acquisition, certification, institutional rank, or a universal training-path implementation.

---

# 4. Current stable IDs and owners

P16 introduces no new persisted gameplay ID.

| Current identity / state | Status | Current owner | P16 interpretation |
| --- | --- | --- | --- |
| `powers` | CURRENT | registered skill / player skill state | knowledge skill used by evolved Ability Specialist design |
| `ABILITY_TRACE_ECHO` | CURRENT | ability authority under `state.abilities` | discovered exceptional ability |
| `TECHNIQUE_SIGNAL_PULSE` | CURRENT | technique state nested under ability owner | current technique-practice evidence |
| `TECHNIQUE_DIRECTIONAL_TRACE` | CURRENT | authored ability/technique authority | stronger later extension, not required for this proof |
| `PRACTICE_SIGNAL_PULSE_ONE_HOUR` | CURRENT authored content ID | authored choice/effect -> Python progression authority | current ability/technique PRACTICE evidence |
| `TRAIN_POWER_FUNDAMENTALS_TWO_HOURS` | CURRENT authored content ID | authored choice -> `simulation.train` | current `powers` PRACTICE evidence |
| `TRACE_CHAMBER` | CURRENT location identity | world/content owner | current specialized environment anchor |
| `TRACE_STABILIZATION_HUB` | CURRENT scene identity | authored content owner | current scene hosting the two-hour Powers activity |
| `CLASS_ABILITY_SPECIALIST` | TARGET/PROPOSAL | Combat Class Catalog design authority | not a runtime class state |
| `PROF_*` / `PROF_GRADE_*` | PROPOSAL namespaces | future profession owner | no Gate Twelve profession record selected here |
| `TRAINING_PATH_*` | PROPOSAL namespace | future progression/training definition owner | no canonical concrete path created here |
| `MENTOR_CAP_*` / `EVAL_CAP_*` | PROPOSAL namespaces | future capability registries | no current mentor/evaluator binding inferred |
| `FACILITY_CAP_*` | PROPOSAL namespace | future facility-capability registry | no concrete capability ID assigned by P16 |

The current Phase 1 durable owners remain those in D-061: player attributes/skills/resources, abilities, perks, knowledge, inventory/flags where independently owned, world time and history. P16 does not add a generic `progression` object.

---

# 5. Evidence classification

The P12 evidence model can classify the existing Gate Twelve route without rewriting it.

| Current evidence | Target evidence class | What it legitimately proves | What it does not prove |
| --- | --- | --- | --- |
| Signal Pulse one-hour practice | PRACTICE | legal authored ability/technique practice occurred | class acquisition, profession, rank |
| two-hour Powers training | PRACTICE | legal registered-skill training occurred | certification, profession identity |
| Trace Echo/Signal Pulse mastery state | PRACTICE / ability-owner evidence | meaningful ability/technique progress | evaluator approval |
| safe resource payment and cooldown/drawback handling | ability-owner evidence | current control/resource discipline behavior | Ability Specialist class ownership |
| save/load + deterministic replay | implementation evidence | current state survives and reproduces correctly | target schema exists |
| Trace Chamber use | world/location evidence | a current specialized Trace Echo environment exists | a generic `FACILITY_CAP_*` record or institution |
| future authored dangerous/meaningful application | CLASS_FIELD_PROOF only if accepted later | may contribute to class acquisition | automatically granting the class |
| future supervised professional work | SUPERVISED_WORK only if accepted later | may contribute to profession qualification | class acquisition or rank |

The central prohibition is:

> Evidence may satisfy an owner-defined requirement. Evidence does not become the owner.

---

# 6. Ability Specialist handoff

## 6.1 Target class identity

The Combat Class Catalog defines Ability Specialist as TARGET and proposes `CLASS_ABILITY_SPECIALIST`.

It is not implemented at runtime.

Ability Specialist deepens control, safe mastery, technique integration and advanced use of an existing exceptional ability. It does not create the ability.

## 6.2 Current evidence already present

The current Gate Twelve route supplies several pieces that a future Ability Specialist acquisition rule could legally inspect:

- discovered `ABILITY_TRACE_ECHO`;
- discovered `TECHNIQUE_SIGNAL_PULSE`;
- meaningful technique/ability mastery progression;
- actual resource expenditure and recovery constraints;
- current Powers knowledge/skill interaction;
- legal practice in a specialized Trace Echo environment;
- persistent progression through save/load;
- player-safe ability identity and mastery projection.

These are evidence inputs only.

## 6.3 Missing authority before class acquisition

The current route does **not** prove:

- a durable class-state owner;
- an implemented class-acquisition transaction;
- a final class-entry threshold;
- an accepted class field-proof record;
- an evaluator requirement or evaluator identity;
- a mentor requirement or mentor identity;
- a class feature grant;
- a class rank;
- a specialization;
- a save migration for durable class state.

Therefore the correct result of P16 is:

**Gate Twelve has a valid evidence foundation for future Ability Specialist acquisition, but Jack does not become `CLASS_ABILITY_SPECIALIST` by documentation inference.**

---

# 7. Powers skill handoff

`powers` is CURRENT and belongs to the Knowledge family.

The Evolved Skill Registry TARGET design gives it:

- study;
- supervised observation;
- controlled experimentation;
- mentor instruction;
- direct ability experience;
- support for technique discovery;
- strong affinity with Ability Specialist;
- useful affinity with Investigator and Operator;
- possible Research or specialist medical/technical profession relationships where canon supports them.

The D-068 activity is therefore a valid CURRENT example of deliberate `powers` training.

It does not establish:

- a final skill plateau;
- a class threshold;
- a profession threshold;
- a certification;
- a mentor identity;
- a final training-path record;
- a universal formula for future evolved progression.

---

# 8. Training, mentor and facility handoff

## 8.1 Activity identity remains current-authority content

P12 preserves `ACTIVITY_*` as the future activity-record identity family and forbids a competing training-activity owner.

The current Gate Twelve proof predates a normalized target activity registry and uses authored content choice IDs such as:

- `PRACTICE_SIGNAL_PULSE_ONE_HOUR`;
- `TRAIN_POWER_FUNDAMENTALS_TWO_HOURS`.

P16 does not rename or retroactively reclassify those stable content IDs.

## 8.2 Training path

A future `TRAINING_PATH_*` may orchestrate a Trace Echo route, but P16 does not mint a canonical training-path ID.

A future definition would have to reference:

- the actual subject owner;
- accepted authored activity IDs/categories;
- evidence classes;
- world access;
- facility capability;
- mentor/evaluator capability only where required;
- condition/safety gates;
- plateau/evidence gates;
- player-safe visibility;
- authoritative mutation owner.

Until that registry exists, the current authored actions remain the playable authority.

## 8.3 Facility

`TRACE_CHAMBER` is CURRENT evidence of a specialized Trace Echo training/practice/recovery environment.

The TARGET capability direction is an ability-control/specialist environment.

P16 deliberately does not create a concrete `FACILITY_CAP_*` record because no accepted runtime/content registry currently requires one.

Trace Chamber existence does not prove:

- a canon institution that owns it;
- a network of equivalent facilities;
- universal access;
- a specific qualification;
- a mentor;
- an evaluator;
- a profession.

## 8.4 Mentor and evaluator

No current mentor/evaluator is required by the D-066 or D-068 proof.

P16 therefore creates no NPC binding.

A future mentor/evaluator dependency must identify:

1. an authorized durable NPC;
2. accepted `MENTOR_CAP_*` and/or `EVAL_CAP_*` capability;
3. current presence/schedule;
4. social/world access;
5. the exact training/class/profession rule consuming that capability.

Friendship, profession, organization rank, or mere presence cannot substitute for capability.

---

# 9. Profession, grade and rank handoff

The P7 namespace standard keeps profession, class, rank, civic status, reputation and Level separate.

## 9.1 Profession

The TARGET Research profession family is the strongest existing profession-direction example for this proof because its target skill anchors include Powers and its natural class relationships include Ability Specialist.

That is design direction, not a canon profession record.

P16 does not create a `PROF_*` identity for Jack.

Future profession qualification would need an accepted profession definition plus profession-owned evidence such as study, supervised work, assessment, work history or other authored qualification.

## 9.2 Profession grade

No `PROF_GRADE_*` exists for this proof.

Powers skill, ability mastery, class evidence, or Trace Chamber access cannot automatically create a profession grade.

## 9.3 Institution/faction rank

No institutional or faction rank is created or advanced by this route.

Training completion is not rank appointment, and rank is not training completion.

## 9.4 Civic/social status and reputation

No civic/legal status or reputation band is inferred from ability practice.

If future world law restricts ability training, the world/status owner must define the legal consequence separately.

---

# 10. Bounded evolved proof scenario

P16 defines the following **documentation proof scenario**, not a new saved record.

## Stage A — current discovery

Jack reaches the existing Gate Twelve Trace Echo path and discovers `ABILITY_TRACE_ECHO` and `TECHNIQUE_SIGNAL_PULSE`.

Classification: CURRENT.

Owners: authored content -> Python ability/technique authority -> existing `GameState` owners.

## Stage B — current practice

Jack executes `PRACTICE_SIGNAL_PULSE_ONE_HOUR`.

Classification: CURRENT PRACTICE evidence.

Result: authoritative mastery/resource/time mutation under existing rules.

## Stage C — current skill training

In the existing Trace Chamber stabilization context, Jack may execute `TRAIN_POWER_FUNDAMENTALS_TWO_HOURS`.

Classification: CURRENT PRACTICE evidence for `powers`.

Result: current skill/time/resource mutation under `simulation.train`.

This is a separate current proof seam; it is not silently merged into the D-066 mastery calculation.

## Stage D — target evidence interpretation

The evolved design may recognize the resulting state as evidence relevant to Ability Specialist because the class catalog explicitly values:

- discovered ability;
- ability/technique mastery;
- safe resource management;
- Powers knowledge;
- controlled specialist practice.

Classification: TARGET interpretation over CURRENT evidence.

No class mutation occurs.

## Stage E — future acquisition gate

A future class-acquisition owner could require additional `CLASS_FIELD_PROOF`, evaluator evidence, mentor access, a plateau gate or other accepted criteria.

Classification: TARGET/PROPOSAL until implemented.

If requirements are not satisfied, the player remains exactly as the current runtime represents them: a character with the existing skills/ability/technique state, not an implicitly assigned class.

## Stage F — profession/rank independence

Even if later Ability Specialist acquisition succeeds, no profession, profession grade, institution rank, faction rank, civic status or reputation is granted unless its independent owner accepts its own evidence.

---

# 11. Player-safe visibility contract

## 11.1 Current safe evidence

D-066 already proves a bounded player-safe ability projection carrying:

- stable ability ID;
- display name;
- rank;
- mastery stage/XP;
- form/state;
- safe ability resource values;
- discovered techniques and their safe mastery/use/cooldown state;
- completed evolution IDs where the current safe view permits them.

Raw authored requirements, discovery requirements and effects do not cross the typed Android boundary.

## 11.2 Target training/class/profession projection

Future UX may show only player-known information such as:

- known training option;
- known subject;
- known duration/cost;
- current availability;
- known location;
- known mentor/evaluator identity where revealed;
- known facility capability;
- known evidence already achieved;
- known next requirement;
- known class/profession status.

It must not reveal:

- hidden thresholds;
- secret class/profession requirements;
- undiscovered locations;
- secret mentors;
- private NPC memory/goals;
- hidden faction clearance;
- private evaluator logic;
- exact hidden formulas;
- future story state.

The Progression UX Contract must define how unknown requirements are represented without turning UI into progression authority.

---

# 12. Persistence and migration contract

CURRENT Phase 1 remains save schema v1.

P16 does not add:

- `state.classes`;
- `state.professions`;
- `state.ranks`;
- `player.class`;
- a generic evidence ledger;
- a persisted available-training list;
- a new top-level progression object.

Existing D-066/D-068 progress continues to persist through current owners.

Before any future durable class/profession/rank/training evidence is added, the implementing task must define:

1. authoritative durable owner;
2. stable record schema;
3. default/legacy behavior;
4. validation;
5. old-save migration;
6. round-trip preservation;
7. deterministic mutation path;
8. rollback;
9. replay/duplicate-evidence behavior where relevant;
10. player-safe projection and Android versioning.

A convenient UI requirement is not sufficient reason to create durable state.

---

# 13. Future validation and test matrix

These are future gates. **P16 executes none of them.**

| Future gate | Required proof |
| --- | --- |
| current route preservation | D-066 Trace Echo/Signal Pulse practice remains deterministic and save-safe |
| current Powers training preservation | D-068 legal route retains exact time/resource/skill ownership |
| class identity resolution | every implemented `CLASS_*` reference resolves |
| no implicit class award | D-066/D-068 evidence alone cannot mutate class state |
| evidence qualification | only accepted evidence classes satisfy a class/profession requirement |
| mentor identity | concrete mentor reference resolves to durable NPC and capability |
| evaluator identity | certification requires accepted evaluator capability when rule demands it |
| facility identity | concrete world location and facility capability both resolve |
| access | undiscovered/unauthorized facility does not become available |
| profession separation | class/skill/mastery cannot auto-create `PROF_*` or `PROF_GRADE_*` |
| rank separation | training/profession/class cannot auto-create institution/faction rank |
| privacy | hidden gates, NPC-private state and undiscovered world truth remain absent from safe projection |
| transactionality | time/resources/progression/evidence commit or rollback together under the accepted owner |
| persistence | existing schema-v1 state round-trips until explicit migration |
| migration | any new durable owner has old-save fixture and new-save round-trip |
| Android | UI delegates actions and consumes typed safe projection; no local unlock arithmetic |

---

# 14. Reconstruction acceptance matrix

| P16 acceptance requirement | Result |
| --- | --- |
| CURRENT/TARGET/PROPOSAL separated | satisfied explicitly in sections 2–12 |
| current stable IDs identified | satisfied in section 4 |
| authoritative owners identified | satisfied in sections 3–4 and 12 |
| bounded Gate Twelve evidence chain | satisfied by D-066 + D-068 mapping |
| skill handoff | `powers` CURRENT; evolved relationships remain TARGET |
| class handoff | Ability Specialist TARGET; no inferred class acquisition |
| profession handoff | Research-family direction TARGET; no canon profession/grade |
| rank/status handoff | independent owners; no inferred appointment/status |
| training/mentor/facility handoff | current authored activities/Trace Chamber preserved; target capability registries not invented |
| player-safe visibility | explicit allow/deny boundary |
| migration seam | schema-v1 preserved; future durable-owner gate explicit |
| future test seam | section 13 |
| next D-045 child | Progression UX Contract |

---

# 15. What P16 does not claim

P16 does not claim:

- that Jack currently has an Ability Specialist class;
- that `CLASS_ABILITY_SPECIALIST` exists in runtime state;
- that Jack has a profession or profession grade;
- that Trace Chamber belongs to a canon institution;
- that a mentor/evaluator exists for this route;
- that a `TRAINING_PATH_*` or `FACILITY_CAP_*` runtime registry exists;
- that any hidden threshold has been chosen;
- that any final numeric class/profession/rank balance is approved;
- that save schema v2 exists;
- that Android has a normalized training/class/profession UX;
- that D-072/D-073 tactical work is changed;
- that Python, Android, Gradle, CI, emulator, device or APK tests were executed for P16.

---

# 16. Direct next D-045 child

After this packet, the direct D-045 child is:

**Progression UX Contract**

That contract should define how current and future progression information is presented across Python player-safe projection, typed Kotlin mapping, ViewModel delegation and Compose without exposing hidden requirements or moving mutation/arithmetic into UI.

It should consume this packet rather than rediscover:

- CURRENT Trace Echo/Signal Pulse ownership;
- CURRENT Powers/Trace Chamber training evidence;
- Ability Specialist TARGET status;
- profession/rank namespace separation;
- mentor/evaluator/facility capability separation;
- schema-v1 current persistence boundary;
- the rule that evidence never becomes the owner that interprets it.
