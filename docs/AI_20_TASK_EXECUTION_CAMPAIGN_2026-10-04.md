# THE GAME — 20-Task AI Execution Campaign

**Status:** ACTIVE QUEUE DESIGN  
**Repository:** `jbob-coder/Text-rpg-game`  
**Authority branch:** `docs/master-game-development-program`  
**Queue owner:** `docs/AI_TASK_BULLETIN_BOARD.md`  
**Semantic task authority:** `docs/THE_GAME_MASTER_TASK_REGISTER.md`  
**Created from observed program HEAD:** `10967480dd1defeadcda1f8b4f7ea6fdc3b4e90f`  
**Important:** the observed HEAD is historical context only. Every claimant must fetch live HEAD.

## 1. Campaign objective

Turn the completed first-pass documentation floor into an evidence-backed path toward a genuinely integrated Gate Twelve Phase 1 while continuing reconstruction-grade program control.

The campaign contains exactly **20 ranked primary tasks**: existing D-060 plus D-061 through D-079.

Ranking is based on:
1. evidence/control correctness;
2. Phase 1 dependency impact;
3. migration readiness;
4. engine authority and save safety;
5. Android/player-safe projection dependency;
6. deterministic verification;
7. low-end performance;
8. final integration value.

The ranking is a default execution order, not permission to ignore dependencies. An agent takes the highest-ranked task that is both `READY` and dependency-safe.

## 2. Priority and points

- **P0-CRITICAL** — program correctness or major integration blocker. Base brag score: 100.
- **P0** — direct Phase 1 or migration blocker. Base brag score: 90.
- **P0/P1** — high-value integration/verification work that may proceed after direct blockers. Base brag score: 75.
- **P1** — important depth/quality work that should not preempt an eligible P0. Base brag score: 60.
- **BONUS** — optional evidence/quality extension. +20 brag score. A bonus never makes an incomplete primary task complete.

Scores are for visibility only. Never optimize points over correctness, safety, evidence, or architecture.

## 3. Ranked campaign

| Rank | Task | Priority | Importance | Primary result |
|---:|---|---|---:|---|
| 1 | D-060 Exact-revision corpus inventory and quota recalibration | P0-CRITICAL | 100/100 | Reproducible immutable inventory and ranked second-pass backlog |
| 2 | D-061 Progression schema/API migration child | P0 | 99/100 | Close progression portion of D-032 |
| 3 | D-062 Social schema/API migration child | P0 | 98/100 | Close broader social portion of D-032 |
| 4 | D-063 Items/economy schema/API migration child | P0 | 97/100 | Close items/economy portion of D-032 |
| 5 | D-064 Player-safe room/actor projection runtime slice | P0 | 96/100 | Implement D-030 without leaking hidden state |
| 6 | D-065 Tamsin durable-memory reactive proof | P0 | 95/100 | Advance Phase 1 recurring-NPC relationship |
| 7 | D-066 Phase 1 progression proof | P0 | 94/100 | Persistent meaningful progression path |
| 8 | D-067 Phase 1 inventory/equipment exact-head proof | P0 | 93/100 | Verified obtain/use/equip/save/UI loop |
| 9 | D-068 Phase 1 activity exact-head proof | P0 | 92/100 | Verified time/resource/persistent activity loop |
| 10 | D-069 Tactical schemas, validators and pure grid core | P0 | 91/100 | First bounded combat implementation layer |
| 11 | D-070 Tactical transient state, turn and action engine | P0 | 90/100 | Deterministic encounter execution core |
| 12 | D-071 Tactical awareness, LOS, cover, objectives, retreat and bounded AI | P0 | 89/100 | Complete core encounter decision layer |
| 13 | D-072 Tactical aftermath, injury and world consequence transaction | P0 | 88/100 | Durable post-combat consequences without tactical save schema |
| 14 | D-073 Gate Twelve tactical content + Python bridge projection/actions | P0 | 87/100 | One playable engine-side Gate Twelve encounter |
| 15 | D-074 Android tactical DTO/mapper/ViewModel/Compose surface | P0 | 86/100 | Player-safe tactical Android surface |
| 16 | D-075 Phase 1 quest branch and world-consequence proof | P0/P1 | 84/100 | Verify persistent branching and later divergence |
| 17 | D-076 Phase 1 integrated save/load + deterministic regression gate | P0 | 83/100 | Exact-head continuity/determinism evidence |
| 18 | D-077 Android Phase 1 consumer/test-gap closure | P0/P1 | 80/100 | Close current projection/render/interaction evidence gaps |
| 19 | D-078 Low-end performance profiling and bounded budgets | P0/P1 | 78/100 | Evidence-backed Galaxy A02-class performance path |
| 20 | D-079 Phase 1 integrated acceptance candidate + APK provenance | P0-CRITICAL FINAL GATE | 100/100 final-gate | Decide whether Phase 1 actually passes its exit gate |

## 4. Task specifications

### Rank 1 — D-060 Exact-revision corpus inventory and quota recalibration
**Priority:** P0-CRITICAL  
**Dependencies:** D-058 DONE; D-059 DONE.  
**Why:** current inventory tooling can be contaminated by working-tree state and cannot serve as exact-revision evidence until fixed.

**Do:**
- make inventory operate on an immutable Git revision;
- prove untracked files and uncommitted edits cannot affect revision-bound counts;
- prove different revisions produce different correct results;
- record measured revision in output;
- run/persist fresh corpus evidence;
- reconcile D-019 and D-058 claims where evidence requires;
- publish ranked second-pass/depth backlog and Phase 1 impact.

**Acceptance:** deterministic exact-revision inventory + regression tests + persisted evidence + synchronized controls.

**BONUS D-060-B:** produce a machine-readable delta between the new exact-revision inventory and the prior structural snapshot, explaining every material category change without rewriting historical evidence.

---

### Rank 2 — D-061 Progression schema/API migration child
**Priority:** P0  
**Dependencies:** D-060 DONE; D-032 parent active.

**Do:**
- inspect current progression/skills/powers/state/save/content/Android APIs;
- map the Phase 1 progression proof onto existing authoritative state;
- define stable IDs, mutation boundaries, migration/save impact, player-safe projection, Android mapping, rollback and tests;
- create the missing D-032 progression migration packet;
- do not invent a new top-level state owner unless migration evidence requires it.

**Acceptance:** implementation-ready progression migration packet consumed by Phase 1 and synchronized under D-032.

**BONUS D-061-B:** add machine-readable progression migration fixtures/checklist that future implementation tests can consume.

---

### Rank 3 — D-062 Broader social schema/API migration child
**Priority:** P0  
**Dependencies:** D-060 DONE; D-032 parent active.

**Do:**
- map NPC identity, relationship axes, memory, knowledge, goals/story state and privacy onto current `social.py`, GameState, saves and Android projection;
- define atomic write boundaries and redaction rules;
- preserve separation between player knowledge and NPC private knowledge;
- specify Tamsin-compatible Phase 1 path;
- create the missing D-032 social migration packet.

**Acceptance:** implementation-ready social migration packet with save/privacy/Android/test boundaries.

**BONUS D-062-B:** create explicit positive/negative privacy fixtures proving what Tamsin memory/knowledge may and may not appear in player-safe projections.

---

### Rank 4 — D-063 Items/economy schema/API migration child
**Priority:** P0  
**Dependencies:** D-060 DONE; D-032 parent active.

**Do:**
- map current flat inventory, equipment slots, item definitions, requirements, story-item consumption and acquisition;
- define compatibility for Phase 1 without forcing currency/vendors/crafting;
- map save and Android DTO/consumer impact;
- define rollback, validation and exact-head tests;
- create the missing D-032 items/economy migration packet.

**Acceptance:** implementation-ready items/economy migration packet; D-032 can be reassessed for closure.

**BONUS D-063-B:** create a compatibility matrix for every current Phase 1 item/equipment action showing state owner, mutation API, save field, projection and test.

---

### Rank 5 — D-064 Implement player-safe room/actor projection
**Priority:** P0  
**Dependencies:** D-060 DONE; D-030 contract/migration map DONE.

**Do:**
- implement the bounded D-030 migration path;
- add versioned player-safe room/actor projection;
- use semantic placement keys, not bridge pixel coordinates;
- add strict Python/Kotlin validation;
- preserve opening-story equivalence before retiring old heuristics;
- add mapper/ViewModel/Compose tests;
- keep save schema unchanged unless evidence requires a designed migration.

**Acceptance:** actor presence comes from authoritative player-safe projection with equivalence and redaction tests passing.

**BONUS D-064-B:** add an opening-scene equivalence evidence packet that enumerates every actor placement before/after migration and proves no hidden/private NPC field crosses the bridge.

---

### Rank 6 — D-065 Tamsin durable-memory reactive proof
**Priority:** P0  
**Dependencies:** D-062 DONE. D-064 recommended before Android presentation changes.

**Do:**
- implement one explicit durable Tamsin memory/consequence from an existing Gate Twelve interaction;
- make a later authored action/scene react to that durable state;
- preserve current relationship axes and privacy;
- prove save/load persistence;
- add deterministic regression coverage;
- update Phase 1 requirements 3 and 4 based on evidence.

**Acceptance:** one meaningful recurring-NPC path visibly reacts to a prior durable interaction after save/load.

**BONUS D-065-B:** add a negative regression proving the private memory itself is not exposed in Android/player-safe projection while its allowed consequence is.

---

### Rank 7 — D-066 Phase 1 progression proof
**Priority:** P0  
**Dependencies:** D-061 DONE.

**Do:**
- select the smallest current Gate Twelve-compatible progression route from existing contracts/content;
- implement or complete one meaningful progress gain and unlock/mastery/skill change;
- ensure authoritative Python mutation;
- prove save/load persistence and deterministic behavior;
- project only player-safe progression data.

**Acceptance:** Phase 1 requirement 5 has an exact-head implemented and tested proof, not UI-only progression.

**BONUS D-066-B:** add a deterministic replay fixture proving the same seed/state/actions produce the same progression result before and after save/load.

---

### Rank 8 — D-067 Phase 1 inventory/equipment exact-head proof
**Priority:** P0  
**Dependencies:** D-063 DONE.

**Do:**
- verify the documented Gate Twelve item/equipment proof using current inventory/equipment authority;
- cover acquisition or possession, inspection/use/equip legality, mutation, projection and save/load;
- include Maintenance Seal / Dead Relay / current loadout where the live packet still authorizes them;
- repair only evidenced defects.

**Acceptance:** requirement 6 is proven on one exact implementation HEAD across Python state, persistence and Android presentation.

**BONUS D-067-B:** add invalid-equip/rollback boundary tests proving failed equipment actions cannot partially mutate authoritative state.

---

### Rank 9 — D-068 Phase 1 activity exact-head proof
**Priority:** P0  
**Dependencies:** D-060 DONE; existing V10 contracts.

**Do:**
- verify `TRAIN_POWER_FUNDAMENTALS_TWO_HOURS` or the live selected proof action;
- prove location/action legality, time/resource cost and persistent result;
- prove save/load;
- verify Android request/presentation path where available;
- repair bounded defects only.

**Acceptance:** requirement 8 has exact-head runtime + persistence evidence.

**BONUS D-068-B:** add interruption/atomicity regression coverage showing an invalid/interrupted activity cannot spend only part of its required state unless explicitly designed.

---

### Rank 10 — D-069 Tactical schemas, validators and pure grid core
**Priority:** P0  
**Dependencies:** D-060 DONE; D-032 combat migration packet active.

**Do:**
- implement tactical authored schemas/validators;
- retain backward compatibility for content packs without tactical sections;
- implement coordinate, occupancy, bounds, pathing, LOS primitives and cover-edge resolution at the smallest safe layer;
- add strong unit tests before session/runtime integration.

**Acceptance:** malformed tactical content is rejected; old content still loads; deterministic pure grid/path/LOS/cover tests pass.

**BONUS D-069-B:** add invariant/property-style regression cases for symmetric visibility where appropriate, blocked-cell path rejection, occupancy uniqueness and edge-cover consistency.

---

### Rank 11 — D-070 Tactical transient state, turn and action engine
**Priority:** P0  
**Dependencies:** D-069 DONE.

**Do:**
- implement transient authoritative `CombatSession`/encounter state;
- implement initiative/activation/action budget;
- implement movement/action legality and deterministic committed-event resolution;
- ensure previews do not consume deterministic event indices;
- do not add tactical state to GameState schema v1.

**Acceptance:** a headless deterministic encounter can execute turns/actions with stable results and no durable mutation before aftermath.

**BONUS D-070-B:** produce a deterministic combat transcript/replay hash test demonstrating identical committed event sequence from identical seed/state/actions.

---

### Rank 12 — D-071 Awareness, LOS, cover, objective, retreat and bounded AI
**Priority:** P0  
**Dependencies:** D-070 DONE.

**Do:**
- integrate detected vs hidden contacts;
- directional cover and legal target knowledge;
- objective completion and retreat;
- bounded AI candidate generation/utility selection;
- optional companion-order legality as scoped by current contract;
- guarantee hidden AI/private state is not player-facing.

**Acceptance:** encounter can resolve objective/retreat paths with knowledge-correct behavior and deterministic bounded AI.

**BONUS D-071-B:** add developer-only AI decision diagnostics that are excluded by tests from player-safe bridge projection.

---

### Rank 13 — D-072 Tactical aftermath, injury and world consequence
**Priority:** P0  
**Dependencies:** D-071 DONE.

**Do:**
- implement validated aftermath plan and atomic GameState commit;
- use existing authoritative fields/APIs for player conditions, inventory, quests, relationships, knowledge, flags, NPC consequences and time;
- implement/approve the Phase 1 injury only through current content/canon authority;
- preserve pre-combat rollback until commit;
- do not dump full tactical event logs into durable history.

**Acceptance:** encounter consequences persist atomically; failure before commit leaves world state recoverable; injury has a defined recovery path.

**BONUS D-072-B:** add fault-injection tests proving aftermath validation/commit cannot leave half-applied persistent state.

---

### Rank 14 — D-073 Gate Twelve tactical content + Python bridge
**Priority:** P0  
**Dependencies:** D-072 DONE.

**Do:**
- materialize the approved/proposed Gate Twelve tactical records without inventing unresolved canon;
- implement `start_combat`, movement/action/end/retreat/order APIs as authorized;
- project only visible cells, detected contacts, legal actions/moves, objective, action budget, safe log and allowed conditions;
- implement active-combat save interruption policy exactly as contracted.

**Acceptance:** one Gate Twelve tactical encounter can be started, played and resolved/retreated through the authoritative Python bridge.

**BONUS D-073-B:** generate a combat projection redaction audit proving hidden positions, goals, utility scores, unrevealed abilities and secret branches never cross the bridge.

---

### Rank 15 — D-074 Android tactical DTO/mapper/ViewModel/Compose surface
**Priority:** P0  
**Dependencies:** D-073 DONE.

**Do:**
- add typed nullable combat DTOs and strict mapping;
- add explicit ViewModel combat actions;
- add minimal tactical surface with selection/pan/zoom/action bar/objective/end/retreat;
- keep legality/path/LOS/hit/damage calculations in Python;
- add JVM and instrumentation coverage.

**Acceptance:** Android can operate the bounded tactical encounter using player-safe engine projection with no duplicated gameplay authority.

**BONUS D-074-B:** add tactical accessibility checks for large text, reduced motion/presentation behavior and touch interaction without moving authoritative rules into Compose.

---

### Rank 16 — D-075 Quest branch + world-consequence proof
**Priority:** P0/P1  
**Dependencies:** D-060 DONE; current quest/world contracts.

**Do:**
- select one existing Gate Twelve branching quest path;
- prove two meaningful resolutions or consequence branches;
- prove later scene/actor/world state differs based on earlier choice;
- prove navigation and save/load preserve the divergence;
- avoid inventing new canon when current content already suffices.

**Acceptance:** requirements 7 and 11 have exact-head evidence for persistent branching and visible later consequence.

**BONUS D-075-B:** create a branch-difference evidence fixture that shows only intended state/projection differences between the two proof paths.

---

### Rank 17 — D-076 Integrated save/load + deterministic regression gate
**Priority:** P0  
**Dependencies:** D-065 through D-075 relevant proof tasks DONE.

**Do:**
- build one integrated Gate Twelve regression sequence spanning relationship/knowledge, progression, item/equipment, activity, quest consequence and tactical aftermath;
- save, reload and continue;
- prove schema/version behavior;
- prove deterministic authoritative outcomes;
- add corruption/unsupported-field rejection where current persistence contract requires it.

**Acceptance:** requirements 12 and 15 are proven across the integrated Phase 1 state rather than isolated subsystem tests.

**BONUS D-076-B:** add a controlled corrupted/unsupported-save fixture proving failure is explicit and cannot silently accept unknown authoritative state.

---

### Rank 18 — D-077 Android Phase 1 consumer/test-gap closure
**Priority:** P0/P1  
**Dependencies:** D-064, D-067, D-068, D-074, D-075, D-076 DONE where relevant.

**Do:**
- close D-021/D-026 current confirmed gaps;
- add dedicated QuestSection projection/render coverage;
- direct `contentId` and `canonStatus` assertions;
- dedicated derived-stat Compose assertion;
- validate actor/activity/tactical/current map/player-safe consumers;
- run exact-head Android unit/build/instrumentation gates available.

**Acceptance:** current Phase 1 Android consumers have explicit field/action/render evidence and no known hidden-authority duplication.

**BONUS D-077-B:** produce a machine-readable screen -> projection field -> engine owner -> tests/evidence matrix for all Phase 1 surfaces.

---

### Rank 19 — D-078 Low-end performance profiling and bounded budgets
**Priority:** P0/P1  
**Dependencies:** D-077 DONE; tactical/Android slice integrated enough to measure.

**Do:**
- define measurable budgets from the approved Galaxy A02-class product target;
- profile representative bounded Gate Twelve/Android/tactical workload in the best available environment;
- record device/emulator distinction explicitly;
- bound actor counts, effects, allocations/assets and expensive recomposition/simulation paths;
- repair evidence-backed hotspots that fit a bounded slice;
- do not claim physical A02/A03 compatibility without physical evidence.

**Acceptance:** requirement 16 has documented budgets, measured evidence, limitations and repeatable profiling method.

**BONUS D-078-B:** build a worst-case bounded Phase 1 performance scenario and a regression ledger that future agents can compare without changing gameplay authority.

---

### Rank 20 — D-079 Phase 1 integrated acceptance candidate + APK provenance
**Priority:** P0-CRITICAL FINAL GATE  
**Dependencies:** all required Phase 1 proof tasks above DONE; unresolved owner-only decisions explicitly separated.

**Do:**
- run the complete Phase 1 exit checklist against one exact HEAD;
- execute Python tests and relevant Android build/JVM/instrumentation gates;
- build a debug/test APK when supported;
- record APK SHA-256 and exact source HEAD;
- verify clean-start core loop, persistence, no known hidden-state leak, deterministic behavior and measured performance path;
- synchronize Phase 1, master record, implementation status, task register and bulletin;
- do not publish/release/merge main.

**Acceptance:** either Phase 1 is evidence-backed PASS on the stated target scope, or the task records an exact failing gate and creates the next repair task. No ambiguous "mostly complete."

**BONUS D-079-B:** create a final reconstruction handoff bundle/index linking exact-head tests, APK provenance, Phase 1 proof evidence, known limitations and next expansion dependency.

## 5. Bonus execution rule

Each primary task has one bonus task. Bonus work:
- unlocks only after its parent primary task is DONE;
- is optional;
- cannot delay a higher-ranked READY P0/P0-CRITICAL primary task;
- must still be evidence-backed and repository-relevant;
- must be recorded in the AI Brag Room if completed.

## 6. Sequence rule

Default sequence is rank 1 -> 20.

If the next rank is blocked but a lower-ranked task is dependency-safe and READY, the agent may take that lower task. The bulletin board must record why.

After every primary completion, the completing agent must:
1. synchronize authoritative records;
2. append a Brag Card to `docs/AI_BRAG_ROOM.md`;
3. if operating in an interactive ChatGPT room, post the same concise Brag Card in chat;
4. ensure at least one next evidence-backed task is READY or explicitly BLOCKED;
5. claim the next different eligible task;
6. repeat.

The repository Brag Room is canonical continuity. Chat posting is an additional human-visible celebration channel when the agent has access to one.
