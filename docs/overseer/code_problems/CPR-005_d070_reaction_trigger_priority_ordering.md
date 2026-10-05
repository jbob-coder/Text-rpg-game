# CPR-005 — D-070 reaction trigger-priority ordering is underspecified

- **STATUS:** REVIEW REQUESTED / LINK CANDIDATE D-070
- **REPORTER:** Veyra
- **CURRENT_TASK:** D-070 — Tactical transient state, turn and action engine
- **OBSERVED_HEAD:** `947ba0a8958da92b0ccf285a0220a1ecf80afc62`
- **DATE:** 2026-10-05
- **BULLETIN_TASK:** D-070 already owns deterministic reaction scheduling; do not create a duplicate task unless AXIOM finds a broader causal owner.
- **TEMPORARY_PATCH_PRESENT:** no
- **SUSPECTED_CAUSAL_LAYER:** approved turn/reaction contract lacks an ordering direction / authored priority representation.

## Failure

The approved Phase-1 turn standard requires deterministic reaction ordering:

1. trigger priority;
2. higher round initiative;
3. actor_id ascending;
4. reaction_id ascending.

However, the repository does not define:
- the data type or authored owner of reaction trigger priority;
- whether a larger numeric priority fires earlier or later;
- whether priority is an ordinal rank where a smaller value fires first;
- a canonical default value when two reaction candidates omit priority.

A repository search of the tactical/turn combat authorities found the phrase `trigger priority` only in `docs/systems/TURN_INITIATIVE_ACTION_BUDGET_STANDARD.md`; no second authority resolves the direction.

D-070 can implement reserve/consume/expire accounting independently, but it cannot finish its required deterministic reaction queue without inventing one of these semantics.

## Expected behavior

The authoritative contract should define one deterministic comparison rule that the D-070 scheduler and tests can encode without UI/AI ownership leakage.

The decision should remain bounded to scheduling. D-071 continues to own awareness/AI logic that decides when/why a reaction candidate is generated.

## Reproduction

1. Read `docs/systems/TURN_INITIATIVE_ACTION_BUDGET_STANDARD.md`, section 8.
2. Observe the required ordering list beginning with `trigger priority`.
3. Search tactical/turn/combat authorities for `trigger priority`.
4. Observe no defined numeric/string representation or ascending/descending rule.
5. Attempt to specify the required D-070 regression:
   - candidate A priority 1;
   - candidate B priority 2;
   - equal initiative;
   - distinct stable IDs.
6. The authority does not determine which candidate should resolve first.

## Executed evidence

Executed repository/source review only:
- exact authority read of `docs/systems/TURN_INITIATIVE_ACTION_BUDGET_STANDARD.md`;
- exact read of the D-070 preflight and Master Task Register requirement that deterministic reaction ordering be completed before D-070 DONE;
- tactical/turn authority search found no second `trigger priority` definition.

No failing runtime/unit test is claimed because any test choosing ascending or descending priority would itself invent the missing rule.

## Affected files / APIs

- `docs/systems/TURN_INITIATIVE_ACTION_BUDGET_STANDARD.md`
- `docs/evidence/D070_TRANSIENT_COMBAT_PREFLIGHT_2026-10-05.md`
- future D-070 reaction scheduler API/tests
- future authored reaction/trigger definitions if a priority field becomes necessary

## Affected domains

- D-070 transient combat scheduler
- reaction reserve/consume/expire lifecycle
- deterministic replay/transcript ordering
- D-070-B transcript hash
- downstream D-071 reaction trigger selection

## What it blocks

Blocks only the final deterministic multi-reaction ordering portion of D-070.

It does **not** block:
- CombatSession/TacticalActorState state;
- round initiative;
- activation/action budget;
- movement preview/commit;
- event indexing/rollback;
- reaction reserve accounting;
- next-round reinforcement admission.

## Temporary patch

None. Veyra will continue independent D-070 work and will not choose an ordering direction until AXIOM resolves the contract.

## Causal hypothesis

**Hypothesis:** the turn standard established the tie-break dimensions conceptually but omitted the representation/direction for the first dimension because no authored reaction-trigger schema existed yet.

This is a contract omission, not evidence of a current runtime regression.

## Why the current task cannot safely absorb the problem

D-070 owns the scheduler implementation, but silently choosing “higher priority first” or “lower rank first” would turn an implementation preference into canon/contract behavior.

The missing rule can be repaired inside D-070 after AXIOM clarifies the existing authority; a duplicate implementation task is not requested.

## Unverified facts

- no Problem Pressure Score is self-assigned;
- no AXIOM rating/verdict is claimed;
- no runtime bug exists yet because D-070 reaction scheduling has not been implemented;
- no canonical priority field/type/default is assumed;
- no root-cause reward is claimed.

## Requested AXIOM decision

Please choose and document:
1. priority representation for Phase 1 (recommended minimal option: integer rank);
2. comparison direction (smaller rank first or larger value first);
3. default priority if an authored candidate does not specify one;
4. whether D-070 owns only the runtime candidate priority value while D-071 later owns trigger-generation policy.

After that decision, Veyra can add the exact deterministic queue regression without inventing semantics.
