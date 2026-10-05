# Code Problem Evidence Packets

This directory stores detailed `CPR-###` evidence packets reviewed by AXIOM.

## Naming

`CPR-###_<short_snake_case_name>.md`

Example:
`CPR-004_save_migration_unknown_field_loss.md`

## Required packet

```md
# CPR-### — <short title>

- STATUS: REPORTED
- REPORTER:
- CURRENT_TASK:
- OBSERVED_HEAD:
- DATE:

## Failure

<what actually failed>

## Expected behavior

<contract-supported expected result>

## Reproduction

<minimum deterministic reproduction, if available>

## Executed evidence

<exact command/test/workflow/run/job/log and observed result>

## Affected authority

- files:
- APIs/contracts:
- state/save/projection owners:
- domains/tasks:

## Blocking impact

<what cannot safely continue>

## Temporary patch

- PRESENT: yes/no
- DESCRIPTION:
- ROOT_CAUSE_FOLLOWUP:

## Causal hypothesis

<hypothesis only; do not present as fact until proven>

## Unverified

<facts not yet established>

## AXIOM review

- PROBLEM_PRESSURE_SCORE:
- RATING:
- VERDICT:
- TASK LINK/CREATION:
- REQUIRED REVIEWERS:
- ROOT-CAUSE ACCEPTANCE:
```

Screenshots may supplement a runtime/UI failure, but executable evidence is preferred for code defects.
