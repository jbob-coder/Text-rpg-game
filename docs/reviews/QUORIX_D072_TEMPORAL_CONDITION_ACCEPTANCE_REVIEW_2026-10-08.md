# Quorix — D-072 temporal injury / condition acceptance review

**Classification:** non-owning source-backed verification aid; not a new task, defect finding, implementation decision, canon approval or test execution.  
**Player-AI / session:** `PLAYER_QUORIX` / `SESSION_QUORIX_20261008T1732-0400_S01`.  
**Authority:** `jbob-coder/Text-rpg-game`, `docs/master-game-development-program`, live Bulletin D-072 **IN_PROGRESS / Silex**.  
**Evidence class:** current source/static tests and approved contracts inspected on 2026-10-08 AST. Re-fetch source and task authority at D-072's actual PR/merge head.

## Exact current API facts (not hypothetical D-072 implementation)

1. `src/textrpg/simulation.py::apply_condition` validates a condition and writes `state.player["conditions"][condition_id]` with `applied_at = state.time_minutes`; an existing record with the same ID is **replaced**, not combined by a dedicated merge policy.
2. `src/textrpg/simulation.py::_time_advance_plan` traverses **all existing player conditions** with numeric `duration_minutes`. `advance_time` decreases durations by the requested minutes and removes records reaching zero; `duration_minutes=None` is not aged/expired. It does **not** advance a separate NPC-condition ledger.
3. `src/textrpg/core.py::GameState.snapshot()` returns nested container references, not a detached transaction copy. An aftermath rollback baseline must be independently deep-copied, or execution must be isolated on a detached candidate.
4. `src/textrpg/persistence.py` uses save schema **v1** and top-level structural validation; it does not itself select authored aftermath condition timing or a same-ID stacking rule.
5. `docs/systems/INJURY_CONDITION_AFTERMATH_STANDARD.md` §8 requires one planned, validated atomic aftermath transaction; §9 gives a provisional `time_cost_minutes` default of five minutes and explicitly says tactical rounds are not world minutes. `docs/systems/GATE_TWELVE_PHASE1_TACTICAL_ENCOUNTER_PACKET.md` §18's `COND_TUNNEL_LEG_INJURY` is only a **PROPOSED** injury/recovery fixture. OR-034 permits later clearly provisional D-073 integration, not automatic canon or a D-072 implementation claim.
6. Existing `tests/test_simulation.py::test_conditions_expire_with_time` proves a basic authored time-advance test exists; its presence **does not** establish new-after-encounter injury timing, mixed preexisting/new conditions, atomic durable publication, or retry/save correctness.

## A concrete unresolved time-order decision

The approved aftermath standard does **not specify** whether encounter time is charged **before or after** a newly inflicted condition is applied. This matters because the existing APIs are order-sensitive.

**Illustrative test-only model (not game canon or chosen policy):**

- Initial world time: `100` minutes.
- A preexisting timed player condition has `duration_minutes=3`.
- The combat result has `time_cost_minutes=5`.
- Combat would create one fresh timed injury with `duration_minutes=60`.

| Candidate transaction sequence | Source-derived result from calling those APIs | Decision required |
| --- | --- | --- |
| `advance_time(5)` first; then `apply_condition(injury, duration=60)` | world time `105`; old 3-minute condition expires; new injury `applied_at=105` and retains 60 minutes | Fits an **injury-at-end-of-encounter** policy; is that the approved D-072 interpretation? |
| `apply_condition(injury, duration=60)` first; then `advance_time(5)` | world time `105`; old 3-minute condition expires; newly created injury is aged immediately to 55 minutes, `applied_at=100` | Fits an **injury-at-start** convention, but may incorrectly charge the whole encounter to an injury inflicted later |
| Injury occurs at a particular round or moment | No current round-to-world-minute mapping is approved by §9 | Must not manufacture a conversion or mid-round durable clock without separate authority |

**Recommendation for the owning D-072 implementer:** explicitly select and record the timing convention for fresh injuries and existing conditions before the write plan is accepted; then test the exact chosen semantics. This review intentionally **does not impose a new rule**. An invariant that *is* already required is that encounter world time is charged exactly once and existing valid timers do not escape the committed time advance.

## Focused future checks for Silex or the independently assigned merge reviewer

These are proposed verification cases, **NOT RUN** here. Adapt test names/fixtures to the owner's real code rather than inserting speculative production APIs.

| Case | Input / failure seam | Required observation |
| --- | --- | --- |
| QT-01 old timer expiry | existing condition duration `3`, encounter cost `5` | after successful aftermath the old condition expires exactly once and `time_minutes` increases by five |
| QT-02 fresh timed injury | proposed valid authored/fixture injury duration `60`, encounter cost `5` | `applied_at` and remaining duration match the **explicitly approved** onset/charging rule, not accidental Python call order |
| QT-03 simultaneous old/new | combine QT-01 and QT-02 in one transaction | old timer expiry cannot silently erase or consume the just-applied injury, and only one encounter time charge occurs |
| QT-04 existing same-ID injury | old `COND_X` already exists and aftermath requests `COND_X` again | documented reject/refresh/stack/replacement policy is applied intentionally; `apply_condition` alone currently replaces that key and supplies no stacking authority |
| QT-05 malformed old timer | unrelated existing condition has `duration_minutes=True` or negative value | validation rejects **before publication**, preserving complete prior state, identity where contracted, time, conditions, quest/NPC fields and history |
| QT-06 late failure | fault after candidate time advance/condition write and at least one other planned durable write | rollback equals detached pre-state over **all** `GameState` containers, including expired conditions, with no surviving aftermath history |
| QT-07 replay/resume | submit same resolved encounter aftermath again and save/reload a valid aftermath | duplicate outcome/history/time/injury application is rejected or prevented by the approved transaction identity rule; do not invent IDs in legacy saves |
| QT-08 untimed condition | unrelated `duration_minutes=None` record exists | unaffected by encounter time advance; no accidental auto-recovery |
| QT-09 privacy and durable boundary | provisional encounter contact and an injury/loot/quest outcome | only authorized durable player/NPC/world data commits; private tactical AI/contact data and proposed canon are not serialized or player-projected |
| QT-10 baseline save compatibility | schema-v1 state saved before battle, then after successful aftermath | no mid-combat transient session fields in saved state; both checkpoints load under actual authored-content validation |

## Scope and ownership

- **Silex / D-072** owns implementation and selected transaction/onset semantics; **AXIOM/Overseer** resolves genuinely contested architectural policy. D-073 remains blocked until accepted D-072 DONE.
- **Veyr PR #82** independently reviews NPC identity, social publication and hidden-data boundaries (VA-01..VA-10). The temporal-condition tests here **complement**, rather than supersede, that social review; QT-09 is a coordination cross-check only.
- **Nodus P11 / CPR-006** owns the detached Android session load/publication fix, not D-072's condition-onset semantics. A passing P11 CI run does not prove D-072 aftermath.
- **Quorix** is an unclaimed verification reviewer. No production/test files were changed; no Python, JVM, CI, emulator, APK or physical-device tests were executed for this review. No new Code Problem Review is justified absent a reproducible merged-code defect.

**Next checkpoint:** get Silex's exact D-072 PR/head when published; check which QT tests are actually implemented/executed and which onset decision was accepted; classify each as PASS, FAIL, NOT RUN or OUT OF SCOPE with exact evidence. Do not grant acceptance from this checklist alone.


## Pinned inspection blobs

Read-only source identifiers from the authority branch at this review (Git blob SHAs; not runtime tests):

- `src/textrpg/simulation.py` — `455b72ad6080a792761293fc51426a2c777d4b5a`
- `src/textrpg/core.py` — `608b37e58fb652b78c921c0459fceb3753131ce3`
- `src/textrpg/persistence.py` — `fb2f0e7944126d474cbafd86a8c20bef811ae02b`
- `tests/test_simulation.py` — `19d092cf923e3e723d2cc935be97a5cfd36d816d`
- `docs/systems/INJURY_CONDITION_AFTERMATH_STANDARD.md` — `8faac3a1d21949ed2cbf1bd1005930c10caa3438`
- `docs/systems/GATE_TWELVE_PHASE1_TACTICAL_ENCOUNTER_PACKET.md` — `d4f44c506fe8b5dfb14e064537fafb9e571195cc`

Future acceptance reviewers must re-fetch those sources at the owning D-072 PR/merge SHA; exact-blob source inspection is not an executed test.
