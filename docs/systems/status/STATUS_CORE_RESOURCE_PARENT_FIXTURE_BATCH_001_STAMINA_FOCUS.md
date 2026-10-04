# THE GAME — Core Resource Parent Fixture Batch 001: Stamina Recovery & Focus Drain

Status: **PHASE-C NUMERIC PREPARATION / QUALITATIVE PARENT FIXTURES / NO FINAL VALUES / NOT CANON / NOT IMPLEMENTED**

Parents:
- `PASSIVE_CANONICAL_RESOLVER_PARENT_FIXTURE_REQUIREMENTS_WAVE_001.md`
- `PASSIVE_CANONICAL_RESOLVER_SCENARIO_ANCHORS_WAVE_001.md`
- `PASSIVE_CANONICAL_RESOLVER_BASE_TERM_MAP_WAVE_001.md`
- `STATUS_BASE_RESOLUTION_TERM_UNIT_TAXONOMY.md`
- `PROGRESSION_CLASSES_RANKS_EVOLVED_GAME_DESIGN.md`

Scope:
- `RESOLVER_STAMINA_RECOVERY_OPPORTUNITY`;
- `RESOLVER_PROLONGED_FOCUS_DRAIN`.

Purpose: materialize the first parent-system fixture batch using relationships that are already supported by the current resource design, while deliberately refusing to invent a universal Stamina/Focus scale or passive coefficient.

## 1. Current-reality evidence

Current/target documentation supports:
- Health, Stamina, Focus, and Resolve as distinct core resources;
- resource maxima derived from authoritative character state;
- bounded resource recovery;
- training/action systems that can consume Stamina/Focus;
- authoritative engine ownership rather than UI ownership.

The current provisional vertical slice starts with:
- Stamina 70;
- Focus 60.

Those are **content-instance values**, not proof of a universal final maximum or balance range.

This fixture batch must therefore test relationships and transaction invariants without treating 70/60 as global scale definitions.

## 2. Readiness result

Before this batch:
- both resolvers had base-term definitions and qualitative scenario anchors;
- final range fixtures were absent.

After this batch:
- `RESOLVER_STAMINA_RECOVERY_OPPORTUNITY` -> `QUALITATIVE_FIXTURES_READY`;
- `RESOLVER_PROLONGED_FOCUS_DRAIN` -> `QUALITATIVE_FIXTURES_READY`.

Neither becomes `RANGE_FIXTURES_READY`.

Still required:
- authoritative resource scales/max logic;
- ordinary spend/recovery ranges;
- authoritative time/task-window units;
- executable or formally simulated parent resolver.

## 3. Shared fixture notation

Use symbolic terms:

- `S_cur` — current Stamina;
- `S_max` — authoritative effective maximum Stamina;
- `F_cur` — current Focus;
- `F_max` — authoritative effective maximum Focus;
- `R_base` — no-passive Stamina recovery result for one valid transaction;
- `D_base` — no-passive Focus drain for one eligible sustained-task interval;
- `C_active` — active condition/context modifiers;
- `TX_ID` — stable authoritative transaction/event identity.

Required invariants:
- `0 <= S_cur <= S_max`;
- `0 <= F_cur <= F_max`;
- recovery cannot produce `S_cur > S_max`;
- drain cannot produce `F_cur < 0`;
- one committed `TX_ID` is applied once.

No exact numeric resource scale is implied.

# Part A — Stamina recovery fixtures

## 4. FIX_STAM_REC_001 — Ordinary valid recovery

Preconditions:
- character is below `S_max`;
- a legitimate recovery opportunity exists;
- no blocking condition invalidates recovery;
- transaction ID is new.

No-passive expectation:
- recovery result is non-negative;
- final Stamina does not exceed `S_max`;
- transaction commits once.

Ordering requirement:
`ordinary_valid_recovery >= no_valid_recovery`.

No exact recovery amount is assigned.

## 5. FIX_STAM_REC_002 — Full-resource cap

Preconditions:
- `S_cur = S_max`;
- a nominal recovery opportunity exists.

Expectation:
- effective Stamina gain is zero;
- no overflow resource is created;
- unused recovery does not convert to Focus/Resolve/Health.

This fixture establishes the hard resource cap before passive modifiers.

## 6. FIX_STAM_REC_003 — Near-cap clamp

Preconditions:
- `S_cur < S_max`;
- missing Stamina is smaller than the unconstrained recovery result would otherwise be.

Expectation:
- final result clamps to `S_max`;
- excess recovery does not become a second resource;
- audit can distinguish requested recovery from accepted recovery if future implementation needs it.

## 7. FIX_STAM_REC_004 — Invalid opportunity

Preconditions:
- no valid recovery opportunity exists.

Expectation:
- `R_base = 0` for this recovery transaction;
- Second Wind/Recovery Channel/etc. cannot manufacture an opportunity;
- UI state cannot trigger recovery authority.

## 8. FIX_STAM_REC_005 — Blocking condition

Preconditions:
- a nominal recovery opportunity exists;
- an authoritative condition explicitly blocks or reduces ordinary recovery.

Expectation:
- blocking/reduction resolves before passive bonus finalization according to the eventual parent order;
- a passive cannot silently bypass the blocking condition.

The exact condition catalog remains outside this fixture batch.

## 9. FIX_STAM_REC_006 — Duplicate transaction

Preconditions:
- one valid recovery transaction with `TX_ID=A` has already committed;
- save/load or repeated input presents `TX_ID=A` again.

Expectation:
- second application is rejected/deduplicated;
- Stamina does not increase again.

## 10. FIX_STAM_REC_007 — Adverse versus favorable ordering

Create two otherwise comparable valid recovery contexts:

`FAVORABLE_RECOVERY_CONTEXT`
- safe/appropriate rest context;
- ordinary recovery allowed.

`ADVERSE_RECOVERY_CONTEXT`
- constrained but still valid recovery context.

Required relationship:
- parent system must document which context produces equal or lower no-passive recovery;
- passive coefficients cannot invert a hard parent-system restriction without explicit design.

No magnitude is assigned.

## 11. Passive composition fixtures for Stamina

Once candidate passive coefficients exist, test:
- no passive;
- Second Wind only;
- Recovery Channel only where ability-use context qualifies;
- both eligible in one transaction;
- duplicate passive ID;
- one passive context-ineligible;
- shared cap reached.

Expected structural result:
one `RESOLVER_STAMINA_RECOVERY_OPPORTUNITY` finalization per transaction.

# Part B — prolonged Focus-drain fixtures

## 12. FIX_FOCUS_DRAIN_001 — Ordinary sustained task

Preconditions:
- character performs an eligible sustained task;
- task interval is valid;
- character has Focus available;
- no passive contribution.

Expectation:
- parent resolver returns a non-negative drain amount/rate;
- Focus cannot increase because of the drain resolver;
- final Focus remains at or above zero.

No amount/time unit is locked here.

## 13. FIX_FOCUS_DRAIN_002 — Short/non-eligible task

Preconditions:
- task does not meet the parent resolver's sustained-task eligibility rule.

Expectation:
- prolonged-Focus-drain resolver contributes no sustained-task drain;
- other action costs may still exist in their own resolver.

This prevents every Focus expenditure from being misclassified as prolonged drain.

## 14. FIX_FOCUS_DRAIN_003 — Favorable sustained context

Preconditions:
- eligible sustained task;
- familiar/supported context;
- ordinary healthy resource state.

Expectation:
- no-passive drain is no worse than an otherwise comparable adverse context once the parent model defines those inputs.

Required ordering:
`D_favorable <= D_adverse`.

Exact difference remains `TBD`.

## 15. FIX_FOCUS_DRAIN_004 — Adverse sustained context

Preconditions:
- eligible sustained task;
- higher legitimate distraction/precision/pressure burden.

Expectation:
- parent drain is equal to or greater than the matched favorable case;
- adverse context cannot be erased solely by UI state.

## 16. FIX_FOCUS_DRAIN_005 — Zero-Focus boundary

Preconditions:
- `F_cur = 0`.

Expectation:
- Focus cannot underflow;
- task behavior at zero Focus must be determined by the parent task/action system;
- the passive resolver cannot create Focus merely by reducing drain.

## 17. FIX_FOCUS_DRAIN_006 — Task termination

Preconditions:
- sustained task ends or ceases to qualify.

Expectation:
- prolonged drain stops according to authoritative task/time semantics;
- passive modifier does not continue after parent eligibility ends.

## 18. FIX_FOCUS_DRAIN_007 — Save/load interval integrity

Preconditions:
- a sustained task interval partially advances;
- save/load occurs at a legal checkpoint.

Expectation:
- elapsed/committed drain is not charged twice;
- unprocessed interval is not skipped;
- rounding cannot create Focus over repeated reloads.

Exact timing implementation remains open.

## 19. Passive composition fixtures for Focus drain

Future candidate coefficients must test combinations drawn from the canonical shared Focus-drain family, including context-eligible cases such as:
- Cognitive Endurance;
- Calibration Patience;
- Professional Focus;
- Negotiation Stamina;
- White Room where its classified packet/context is legitimately valid.

Expected structural result:
- one canonical Focus-drain transaction;
- scope tags select eligibility;
- one shared cap/floor;
- final drain never becomes negative.

## 20. Cross-resource isolation

Required fixture:
a Stamina recovery event and a Focus-drain event occur in the same broader activity.

Expectation:
- each resource resolves independently unless an explicit parent rule couples them;
- Stamina recovery does not restore Focus;
- Focus-drain reduction does not restore Stamina;
- passive composition cannot invent cross-resource conversion.

## 21. Current-values compatibility fixture

The provisional Dead Relay initial content values:
- Stamina 70;
- Focus 60

may be used later as one **content-instance regression fixture**.

They must not be used to conclude:
- universal max Stamina = 70;
- universal max Focus = 60;
- passive percentage values;
- universal spend/recovery rates.

The regression purpose is only:
- current content remains valid under future resource-schema migration;
- starting resources clamp correctly to whatever effective maxima the character has.

## 22. Required parent decisions before range fixtures

To move these resolvers to `RANGE_FIXTURES_READY`, define:

### Stamina
- effective maximum logic;
- ordinary action spend examples/ranges;
- ordinary recovery transaction ranges;
- recovery-window/reset semantics;
- world/simulation timing basis;
- blocking-condition order.

### Focus
- effective maximum logic;
- ordinary action spend examples/ranges;
- sustained-task drain representation;
- authoritative task/time interval;
- zero-Focus behavior;
- recovery interaction.

## 23. Acceptance

This batch is complete when a future developer can create deterministic parent tests without guessing:
- which transactions qualify;
- what must remain bounded;
- what ordering relationships must hold;
- what must be deduplicated;
- what values are still intentionally `TBD`.

Current result:
- qualitative fixture schemas: **READY**;
- final resource ranges: **NOT READY**;
- passive coefficients: **BLOCKED**;
- runtime implementation: **DEFERRED**.

No numeric value or passive is canon-promoted by this fixture batch.
