# DOC_0000003 — Documentation-First Execution Rule

Status: **REVIEWABLE**
Domain/program owner: D-07 Documentation / Coordination
Authority/evidence class: OWNER_DECISION + CONFIRMED_DOCUMENTED
Stable ID: DOC_0000003

Upstream: DOC_0000001; EXISTING::docs/program/00_OWNER_DIRECTIVE_2026-10-02.md; EXISTING::docs/program/01_DOCUMENTATION_PROGRAM_MASTER.md
Downstream: implementation planning, world/content production, asset production, APK reconstruction, QA and migration.

## Rule
Large implementation, destructive rework, and final APK reconstruction must not outrun the documentation required to define target behavior, dependencies, migration, and acceptance evidence.
Required sequence: authority -> documentation -> decisions -> dependencies -> planning -> implementation -> tests -> review -> migration/rebuild -> verification.

## What documentation-first does not prohibit
Small reversible experiments, read-only audits, proofs of concept, tooling used to validate assumptions, and limited implementation needed to obtain evidence remain allowed.

## Current
The repository contains implementation branches and historical work. They remain evidence; they are not automatic final architecture.

## Target
Before major implementation, the relevant specification identifies current behavior, target behavior, delta, dependencies, state owner, migration impact, rollback/recovery boundary, and acceptance evidence.

## Breaking-change gate
Before deliberate breakage: identify scope, insufficiency of current behavior, replacement source of truth, dependencies, save/data impact, migration/recovery, and verification plan.

## Exception
An emergency repair may precede full design documentation only to restore a broken baseline; it must be documented immediately afterward as provisional or confirmed evidence.

## Acceptance
Another developer can identify the target and verification path without reconstructing hidden intent.

## Revision trigger
Explicit owner change to the documentation-first mandate or creation of a separately governed prototype lane.

## Next action
Use this rule to gate world expansion, major system rewrites, and application/APK teardown.