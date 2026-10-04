# THE GAME — Status / Ability / Passive Balance & Test Matrix

Status: **ACTIVE TARGET-GAME VERIFICATION CONTRACT / IMPLEMENTATION DEFERRED**

Parents:
- `../STATUS_UI_ABILITIES_AND_PASSIVES_MASTER_PLAN.md`
- `STATUS_UI_CORE_CONTRACT.md`
- `PRIMARY_ABILITY_REGISTRY_SCHEMA.md`
- `PASSIVE_REGISTRY_SCHEMA.md`
- `PASSIVE_REQUIREMENT_LANGUAGE.md`
- `STATUS_KNOWLEDGE_VISIBILITY_STANDARD.md`
- `LEVEL_AND_XP_STANDARD.md`
- `LEVEL_100_EXCEPTION_STANDARD.md`
- `STATUS_UI_UX_CONTRACT.md`

Purpose: define how design balance, structured data, hidden information, progression, save/load, Android projection, and exploit resistance will be verified.

## 1. Verification layers

The Status program uses separate verification layers:

1. **document structure** — IDs, references, required fields;
2. **design consistency** — laws, rarity, overlap, counters;
3. **world consistency** — knowledge, institutions, legality, history;
4. **engine behavior** — authoritative state transitions;
5. **save/migration** — persistence and compatibility;
6. **projection/privacy** — player-safe data only;
7. **Android UX** — correct rendering of projected truth;
8. **content QA** — authored scenes/training/events satisfy system rules;
9. **exploit QA** — no trivial/farm/self-harm bypasses;
10. **performance/accessibility** — mobile-safe presentation.

Passing one layer does not imply the others pass.

## 2. Current Wave 001 structural matrix

| Check | Current result | Evidence |
|---|---|---|
| primary ability count | PASS — 47 | `STATUS_CORPUS_WAVE_001_AUDIT.md` |
| passive count | PASS — 230 | audit |
| technique count | PASS — 188 | audit |
| passive unlock-path count | PASS — 230 | audit |
| passive knowledge-profile count | PASS — 230 | audit |
| awakening-profile count | PASS — 47 | audit |
| counter-profile count | PASS — 47 | audit |
| global ID uniqueness | PASS — 1,019 unique | audit |
| dangling ability references | PASS — 0 | audit |
| dangling passive references | PASS — 0 | audit |
| full schema completeness | PARTIAL | deep-authoring phase |
| canon promotion | NOT RUN | proposals remain non-canon |
| runtime implementation | NOT RUN | implementation deferred |

## 3. Primary ability design tests

Every ability promoted from calibration must pass:

### Law integrity
- core law can be stated in one coherent rule;
- every technique stays inside that rule;
- forbidden domains remain forbidden;
- no scene-specific convenience power appears without evolution/canon change.

### Rarity fit
- rationale exists;
- adjacent-tier comparison exists;
- same-tier peer comparison exists;
- higher rarity is not justified solely by raw damage;
- rarity does not guarantee victory.

### Resource balance
- meaningful effects identify cost;
- repeated use creates bounded burden;
- resource recovery is defined;
- no unlimited output through omitted cost fields.

### Counterplay
- at least one meaningful natural/tactical/environmental/knowledge route exists;
- counters are not all “be stronger”;
- counterplay does not require hidden omniscient information.

### Failure
- overuse has a consequence;
- misfire/loss-of-control behavior is bounded;
- catastrophic behavior is explicit rather than improvised.

## 4. Technique tests

For every implemented technique:
- parent ability exists;
- prerequisites are satisfiable;
- prerequisites cannot be bypassed by client/UI state;
- cost is applied exactly once;
- target/range validation occurs in authority layer;
- invalid targets do not consume or mutate unintended state unless design says so;
- failure state is deterministic where required;
- mastery updates once per qualifying event;
- hidden techniques do not appear in player-safe projection;
- FX failure does not alter authoritative outcome.

## 5. Passive unlock tests

For every implemented passive:
- unmet requirement remains `UNSEEN`;
- exact threshold boundary is deterministic;
- valid event increments progress once;
- invalid/trivial event does not increment;
- duplicate event ID does not increment twice;
- save/reload cannot duplicate progress;
- self-harm exploit path is rejected where forbidden;
- recovery requirements are enforced;
- sequence/time-window rules resolve correctly;
- mutually exclusive conditions are validated;
- reveal occurs only after qualification;
- activation state matches design.

## 6. Hidden-information tests

Player-safe projection must prove:
- no hidden passive name;
- no hidden passive icon;
- no hidden slot count;
- no hidden progress percentage;
- no exact unlock threshold unless learned;
- no true rarity if only public rarity is known;
- no undiscovered technique;
- no classified institutional notes;
- no hidden Level-100 mechanism.

Debug/developer projection must be separate and explicitly enabled.

## 7. Knowledge-state tests

For each knowledge-sensitive datum:
- system truth can differ from public belief;
- public/school/government/military/research/faction scopes can differ;
- false belief is stored as a belief, not overwritten into system truth;
- discovery events durably update player/character knowledge;
- save/load preserves discovered knowledge;
- UI never marks a belief “false” before the character has evidence.

## 8. One-primary-ability tests

Engine rules must prevent:
- ordinary acquisition of a second primary ability;
- passive records being interpreted as primary abilities;
- techniques being serialized as independent primary abilities;
- equipment temporarily mutating primary identity without explicit rule.

The only replacement path is the future Level-100 exception mechanism.

## 9. Unique-ability tests

When Unique implementation exists:
- no two active owners can possess the same Unique identity unless canon explicitly permits succession;
- save migration preserves uniqueness;
- clone/duplication exploits cannot duplicate ownership;
- Level-100 replacement interaction follows final Unique rules;
- public classification may differ from true Unique state only through authored visibility rules.

## 10. Level / XP tests

Blocked until numeric Level design is completed.

Future tests must cover:
- valid XP source;
- invalid source;
- kill contribution;
- assist policy;
- party split;
- trivial-target farming;
- duplicate kill credit;
- controlled/summoned source;
- PK legal/moral separation from XP truth;
- Level boundary;
- Level 100 historical rarity assumptions.

No test should encode an unapproved XP formula.

## 11. Save and migration tests

Future save schema must verify:
- primary ability stable ID persists;
- known techniques persist;
- mastery persists;
- passive hidden progress persists without leaking;
- revealed/active passive state persists;
- knowledge scopes relevant to player persist;
- deprecated IDs migrate explicitly;
- no ID reuse;
- irreversible Level-100 changes are recoverable only through designed migration/backup path;
- corrupted unknown IDs fail safely.

## 12. Android projection tests

Android receives only projected data.

Tests should verify:
- hidden fields absent from serialized model;
- missing hidden records do not imply UI slots;
- loading/error state does not fabricate values;
- rendering order does not expose debug text;
- orientation/size changes do not duplicate actions;
- process recreation does not create a second gameplay truth;
- accessibility labels do not leak hidden content.

## 13. Awakening-event tests

Future age-18 event implementation should cover:
- identity verification;
- awakening success;
- unstable manifestation;
- medical emergency;
- unreadable result;
- public/private field split;
- rare+ security handling;
- Unique information suppression path;
- official record creation;
- post-event Status state;
- recruiter/world reaction;
- save/load during safe checkpoints.

## 14. Ability/passive interaction tests

For each approved cross-reference:
- synergy activates only when both required records/states exist;
- multiplier/cost effects respect caps;
- duplicate modifier application is prevented;
- overlap does not create immunity/unlimited resources;
- hidden synergy does not reveal hidden passive data;
- removal/migration of one side resolves safely.

## 15. Adversarial exploit scenarios

Required adversarial suite should include:
- repeated trivial training input;
- intentional injury farming;
- helpless-target kill farming;
- save/reload duplicate event;
- rapid UI tap duplication;
- offline/reconnect replay if applicable;
- event ID reuse;
- stale Android projection;
- corrupted catalog entry;
- invalid parent reference;
- hidden catalog enumeration;
- resource underflow/overflow;
- stack overflow through duplicate effects;
- interrupted Level-100 transition.

## 16. Balance review bands

Balance review should compare characters across:
- same Level / different rarity;
- different Level / same rarity;
- lower rarity with higher mastery;
- higher rarity with poor resources/control;
- passive-heavy specialist;
- equipment-supported specialist;
- favorable/unfavorable environment;
- team versus solo;
- injured versus healthy;
- informed versus uninformed opponent.

The objective is not equal outcomes. The objective is coherent, explainable outcomes.

## 17. Content acceptance

A promoted ability/passive is incomplete if the game world has no way to:
- train it;
- discover it;
- counter it;
- react to it;
- use it outside a stat sheet where plausible.

At least one authored content path should demonstrate each major system behavior before final implementation certification.

## 18. Performance and accessibility

Status presentation must be tested on the application target class, including Galaxy A03-class low-end hardware.

Verify:
- no excessive animation cost;
- reduced-motion path;
- non-color-only rarity/status information;
- scalable text;
- large touch targets;
- safe flash behavior;
- nearest-neighbor pixel-art handling;
- missing-asset fallback.

## 19. Promotion gate

No record is `VERIFIED` until:
- document checks pass;
- design audit passes;
- world integration is sufficient;
- implementation exists;
- automated/manual tests relevant to the record run successfully;
- failures are recorded and resolved or explicitly accepted.

Documentation alone may be complete while implementation remains absent. Those states must remain separate.
