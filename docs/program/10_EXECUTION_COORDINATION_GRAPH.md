# Execution Coordination Graph

Status: ACTIVE / PROGRAM DEPENDENCY MAP

## Graph model

The documentation program is treated as a dependency graph.

`G = (V, E)`

Node types:
- requirement;
- decision;
- document;
- world entity;
- system;
- repository file;
- implementation task;
- asset;
- test;
- risk;
- evidence.

Example edges:
- Decision -> constrains -> Document
- Document -> specifies -> System
- System -> implemented_by -> File
- Test -> verifies -> Behavior
- Asset -> renders -> State
- Location -> belongs_to -> Region
- Route -> connects -> Location
- Gap -> blocks -> Task
- Decision -> supersedes -> Decision

## Core execution path

`Owner Directive`
-> `Program Master`
-> `Decision Gaps`
-> `Domain Architecture`
-> `Pilot Deep Documentation`
-> `Subsystem Specifications`
-> `Content/Asset Production`
-> `Implementation Tasks`
-> `Tests/Runtime Evidence`
-> `Migration/Retirement`
-> `Final APK Rebuild`

## Current pilot path

`Gate Twelve Steps 1-4`
-> `Step 5 Geometry Contract`
-> `Material/Visual Language`
-> `Asset Decomposition`
-> `Application UX`
-> `State Layers`
-> `Performance/Section Strategy`
-> `Implementation Order`
-> `Verification`
-> `Migration`
-> `Execution Handoff`

## Approval boundaries

Routine reversible documentation and working-branch engineering: authorized.

Explicit review/extra caution required before:
- destructive repository/history operations;
- irreversible data deletion;
- canonical/default branch promotion;
- release publication;
- paid/external account changes;
- save-breaking migration without an authored migration/recovery plan.

## Failure/recovery contract

For major changes record:
- failure mode;
- detection;
- state/data preserved;
- rollback or compensating action;
- exact evidence needed before declaring success.

## Agent/session handoff

Every substantial work session should leave:
- CURRENT_OBJECTIVE
- VERIFIED_STATE
- COMPLETED
- IN_PROGRESS
- NEXT_ACTION
- BLOCKERS
- ASSUMPTIONS
- UNKNOWNS
- DECISIONS
- RISKS
- FILES_CHANGED
- TESTS_RUN
- RESULTS

No future session should need hidden reasoning to resume the project.
