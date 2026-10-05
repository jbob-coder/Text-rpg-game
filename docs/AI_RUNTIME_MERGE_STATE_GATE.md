# THE GAME — Runtime Merge-State Integration Gate

**Status:** ACCEPTED / PROSPECTIVE  
**Authority:** Project Overseer ruling OR-009  
**Applies:** runtime-impacting work beginning with D-069 after the D-064–D-068 transition checkpoint.

## Purpose

Keep `docs/master-game-development-program` usable as an integration baseline while multiple AI agents work concurrently.

The problem this policy addresses is shared-head drift: a task can pass its own focused tests while another partially integrated runtime change makes the authority branch red or changes the contract underneath it.

## Transition

Do not rewrite or rebase D-064–D-068 merely to satisfy this policy.

First:
1. let D-064–D-068 reach safe handoff;
2. reconcile their shared-head integration defects;
3. establish one green authority checkpoint.

Then enforce this policy prospectively for D-069 onward.

## Runtime-task workflow

For a runtime-impacting task:

1. Claim the task on the authority Bulletin Board.
2. Fetch current authority HEAD.
3. Create/use a short-lived task branch.
4. Implement and test the task on that branch.
5. Open/update a PR targeting `docs/master-game-development-program`.
6. Let merge-state CI evaluate the task against current authority.
7. Reconcile drift if authority moved.
8. Do not mark the task DONE while required merge-state CI is red.
9. Merge only when the task acceptance criteria and integration gate are satisfied.
10. Record the resulting authority HEAD and evidence in task/Brag/Scoreboard records.

## Existing CI surface

`.github/workflows/android-pixel-client.yml` already runs on pull requests affecting runtime/content paths and currently covers:

- complete Python unittest suite;
- Android unit tests;
- Compose instrumentation-test compilation;
- debug APK assembly;
- APK contents/hash verification;
- PR emulator smoke/instrumentation;
- UI screenshot evidence checks.

Use the workflow as the integration gate instead of inventing a parallel CI authority.

## What counts as runtime-impacting

Examples:
- Python engine/state/content behavior;
- persistence/save behavior;
- Android bridge/mappers;
- ViewModel actions;
- Kotlin/Compose behavior tied to runtime contracts;
- tactical engine/runtime;
- authoritative item/social/progression behavior;
- content changes whose semantics alter runtime behavior.

## What may still write directly to authority

Normally safe direct writes include:
- task claims/status;
- Brag/Scoreboard/Council records;
- documentation-only audits;
- evidence pointers;
- cross-reference synchronization;
- process/governance files.

Direct runtime hotfixes are allowed only when necessary to restore the shared baseline and must record exact evidence and why branch/PR isolation was bypassed.

## Completion rule

Task-local green is insufficient when merge-state is red.

A runtime task is not integration-complete until:
- focused task evidence is green;
- required merge-state CI is green;
- the resulting authority state remains coherent;
- no known cross-task compatibility defect is being hidden by the merge.

## First-policy proof

The first runtime task fully executed under this policy must record:
1. task branch HEAD;
2. authority HEAD used for merge-state;
3. PR/workflow evidence;
4. resulting authority HEAD;
5. whether compatibility repair was needed after merge.

If the policy creates more coordination cost than it removes, bring evidence to the Council for revision.
