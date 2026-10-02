# Owner Directive — 2026-10-02

Status: **ACTIVE / AUTHORITATIVE OWNER DIRECTION**  
Repository: `jbob-coder/Text-rpg-game`  
Priority: **PRIMARY GAME REPOSITORY FOR THIS PROGRAM**

## 1. Purpose

This file records explicit owner decisions that govern the current documentation-first development program.

It is not a design brainstorm. When older documentation conflicts with a newer explicit owner decision recorded here, the newer decision controls unless it is later superseded explicitly.

## 2. Priority repository

`jbob-coder/Text-rpg-game` is the priority repository for the current Text Pixel RPG / THE GAME documentation and development program.

Other repositories, prototypes, historical reports, external references, and previous project plans may provide evidence or ideas, but they must not silently override this repository's current authoritative documentation.

Where practical, stale pointers in related documentation should be updated so they route future work toward this repository.

## 3. Documentation-first mandate

Documentation is the primary goal before large-scale implementation or APK reconstruction.

The intended sequence is:

`authority -> documentation -> decisions -> dependencies -> planning -> implementation -> tests -> review -> migration/rebuild -> verification`

The project must be documented deeply enough that another session or agent can resume without reconstructing intent from chat history.

## 4. Two-million-file target

The owner explicitly set a target of **2,000,000 separate documentation files**.

This means separate files, not words, pages, or a symbolic size target.

Production must be incremental so the workflow remains recoverable:

- 1 sub-batch = 100 files
- 10 sub-batches = 1 batch of 1,000 files
- 2,000 batches = 2,000,000 separate files

The target does **not** authorize filler. Each produced file must have a concrete purpose, relationship, dependency, decision, specification, guide, test contract, content definition, or other justified project role.

## 5. Existing documentation is editable

Existing documentation is not frozen.

When previous documents are inconsistent with the current direction, incomplete, stale, contradictory, or attached to an obsolete source of truth, they may be classified and changed as:

- KEEP
- UPDATE
- REWRITE
- SUPERSEDE
- MERGE
- DELETE

Historical decisions that remain useful for auditability should be preserved and marked as historical or superseded rather than silently erased.

## 6. Application / APK authority

The current application is **not** a protected design constraint.

The owner has explicitly authorized substantial changes when they produce a materially better game aligned with the final documentation.

Existing application components may be classified as:

- KEEP
- UPGRADE
- REWORK
- REPLACE
- DELETE
- REBUILD

This permission includes breaking or replacing existing presentation, navigation, UI structure, rendering, and other implementation areas when necessary.

However, destructive or breaking work must be controlled. Before a significant replacement, documentation should state:

- what is being changed or removed;
- why it is insufficient;
- what replaces it;
- affected dependencies;
- save/data compatibility impact;
- migration path;
- verification requirements;
- rollback/recovery boundary where practical.

Gameplay-authoritative state must not be moved into presentation code merely to simplify a rebuild.

## 7. External-reference rule

External game/reference material is non-authoritative.

Use it to extract useful principles such as:

- modular construction;
- spatial hierarchy;
- circulation;
- layered pixel-art composition;
- reusable overlays;
- contextual character/room panels;
- asset families;
- sectioned production;
- UX and readability patterns.

Do not automatically inherit:

- contradictory numbers;
- exact colors;
- exact dimensions;
- proprietary names;
- character identities;
- lore;
- one-to-one layouts;
- distinctive protected expression.

The rule is:

> Extract useful structure; rebuild it as original project design.

## 8. Map/world production rule

Maps are to be planned and constructed piece by piece as real game content, not generated as one flattened image.

World documentation is expected to expand beyond Gate Twelve to cover, as applicable:

- coordinate systems;
- places and routes;
- zones and regions;
- cities and villages;
- kingdoms and political geography;
- resources and ecosystems;
- loot, items, equipment, and accessories;
- NPCs and society;
- citizen classes and hierarchy;
- fictional discrimination/conflict systems;
- beast zones and ecology;
- world level/balance;
- stats, abilities, passives;
- activities;
- classes, ranks, and skill trees;
- tactical combat;
- persistent adversaries;
- application/APK integration.

## 9. Combat inspiration boundary

General design concepts may be inspired by tactical games and persistent-adversary systems.

The project may use general ideas such as:

- tactical positioning;
- cover;
- turns/action economy;
- terrain;
- persistent enemy memory;
- rivalries;
- promotion;
- adaptation;
- recurring adversaries.

The implementation must use original terminology, data structures, rules, presentation, characters, and content rather than copying protected expression from other games.

## 10. Current pilot

Gate Twelve remains the first detailed pilot region for validating the documentation method.

Its existing master plan is not discarded. New global documentation must connect to it rather than creating an unrelated parallel system.

## 11. Development permission boundary

The owner grants broad permission to improve, restructure, replace, break, remove, and rebuild game-development components when justified by the final design.

This permission does **not** override explicit owner prohibitions or project safety/compatibility constraints.

The governing principle is:

> Do not preserve a weak implementation merely because it already exists; do not destroy a working dependency without documenting and validating its replacement.

## 12. Continuity rule

Every substantial documentation batch should end with a recoverable handoff containing:

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

Repository documentation outranks remembered chat summaries when they conflict.
