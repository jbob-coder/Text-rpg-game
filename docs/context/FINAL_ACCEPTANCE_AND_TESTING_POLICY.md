# Final Acceptance and Testing Policy

Status: [DIRECTION] ACCEPTED

This policy records the user's explicit project instruction that the user will **not perform intermediate game testing**. The user intends to check the game only when the project is complete within the agreed scope and a final acceptance/release candidate is ready.

## User role

The user is the final acceptance tester, not an ongoing QA dependency.

During normal development, contributors and AI workstreams must not rely on requests such as:

- "run this build and tell me what happens";
- "check this screen";
- "reproduce this bug on your device";
- "try this branch before I continue";
- manual regression checklists that require the user to unblock implementation.

A final acceptance check may be requested only after the project reaches the completion gate defined below.

## Internal verification responsibility

Intermediate verification must be performed without depending on the user, using the strongest available zero-cost/local mechanisms appropriate to the change:

- static source and data inspection;
- authored unit and integration tests;
- deterministic simulations;
- content/schema/reference validation;
- save/load and migration verification;
- automated gameplay/state-transition checks;
- repository diff and exact-SHA evidence;
- local or otherwise free runtime execution when available.

The presence of authored tests is not equivalent to executed passing tests.

If a required runtime path cannot be executed, it must remain explicitly marked [UNKNOWN] or unverified. Work may continue only where doing so does not bypass a required stage gate.

## Cost constraint

Do not introduce or run paid/billing-risk CI solely to obtain verification. In particular, do not create a GitHub Actions workflow solely to run the suite unless the user explicitly changes this constraint.

Prefer free/local execution.

## Stage-gate effect

The current project remains in Stage 3 — Integration, Hardening, and Stabilization until its exact runtime verification gate is satisfied.

Static hardening may continue while runtime execution is unavailable, but Stage 4 canonicalization/migrations must not be used to bypass the unresolved Stage 3 runtime gate.

Likewise, a later stage must not be declared complete merely because the user has chosen not to perform intermediate manual testing.

## Final acceptance readiness

"Ready for the user to check" means all of the following are true for the agreed project scope:

1. Intended scope for the release candidate is implemented.
2. Integration/reconciliation work is complete.
3. The full required automated suite has executed successfully on the exact final candidate SHA.
4. Required content/static validators are clean.
5. Save/load, progression, state-transition, and migration paths that apply to the release candidate are verified.
6. No known critical or release-blocking defects remain.
7. Project documentation and implementation-status records match the final candidate.
8. A playable/release build or final runnable package is prepared for the user.
9. Any remaining known non-blocking limitations are disclosed before acceptance.

This is an operational completion standard, not a claim that software can be mathematically proven to contain zero defects.

## Current application

At the time this policy was recorded:

- active stage: late Stage 3;
- active implementation branch: `integration/rules-ability-v6-reconcile`;
- exact referenced V6 SHA before this documentation-only context update: `7718cd422d69eb4515dfa5beb7dd4ab117c1c6fe`;
- authored test inventory: 251 methods across 17 test files;
- exact full runtime suite on that V6 SHA: not yet executed;
- Foundation and V5 remain protected from this policy documentation change.

The runtime suite remains the principal promotion gate.
