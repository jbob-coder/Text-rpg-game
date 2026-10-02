# Conversation Context — Gate Twelve Map / Pixel Art / Animation

Recorded: 2026-10-01 AST
Repository: `jbob-coder/Text-rpg-game`
Working branch: `docs/gate-twelve-map-pixel-asset-blueprint`

## Current objective

Prepare the Gate Twelve district for systematic authored pixel-art and animation production without repeatedly redesigning its existing map geometry.

Runtime animation implementation remains paused until this continuity reconciliation is recorded.

## Repository authority order

1. Current repository files and exact branch/HEAD.
2. Fresh build/test/runtime evidence.
3. `docs/THE_GAME_MASTER_TASK_REGISTER.md`.
4. Current implementation/handoff documentation.
5. This conversation-context record.
6. Historical chat memory.

Do not use `main` as canonical implementation merely because it is the default branch.

## User decisions preserved

### Geometry
- Existing Gate Twelve district geometry is the scaffold.
- Do not re-plan or redraw the layout every time a new asset is produced.
- Geometry changes must be explicit map-design changes, never incidental art-fit changes.

### Pixel-art application
- Authored pixel art should dominate the visible environment.
- Compose/procedural rendering may handle navigation, hit-testing, overlays and state presentation, but must not replace authored visual identity.
- Reuse existing stable asset IDs where they already represent the required object.
- Preserve nearest-neighbor/integer-safe pixel presentation.
- Do not invent geometry, hidden state, unsupported bindings or gameplay meaning.

### Asset planning
Each region brief should identify:
- confirmed bounds;
- identity/material direction;
- required sprites/tiles/props;
- existing code-present assets;
- planned-only assets;
- missing assets;
- how each item attaches to the existing map.

### Animation model
Animation is separated into:
1. STATIC — permanent geometry/material.
2. AMBIENT LOOP — presentation-only environmental motion that does not imply gameplay state.
3. STATE-DRIVEN — motion allowed only when player-safe authoritative state supports it.

The fixed map scaffold remains underneath all animation.

### Initial bounded implementation targets
1. Service Tunnel ambient infrastructure loop.
2. Gate Twelve Echo-active state overlay.
3. Depot Plaza blackout state loop.

These are implementation candidates, not claims that runtime animation already exists.

## Documents already produced
- `docs/assets/GATE_TWELVE_MAP_PIXEL_ASSET_BLUEPRINT.md`
- `docs/assets/GATE_TWELVE_MAP_ANIMATION_BLUEPRINT.md`
- `docs/assets/README.md` links both.

PR #29 currently carries this documentation line.

## Project-separation rule

The separately uploaded private-RPG context-preservation rules describe a different source-of-truth hierarchy based on private state/session files. This repository does not contain that hierarchy.

Therefore:
- do not import the private-RPG state/session model into this repository;
- do preserve the general anti-downgrade rule: never silently simplify or reset established state;
- keep private-RPG continuity and this repository's engineering continuity separate unless the user explicitly connects them.

## Standing safety permission recorded

The user explicitly allowed the assistant to make necessary decisions so the work remains safe.

Within this repository task that means the assistant may choose conservative, reversible engineering actions without repeated confirmation when they:
- preserve data and history;
- avoid `main` and protected/shared-history changes;
- use a working branch;
- keep project boundaries separated;
- add tests, documentation and diagnostics;
- prefer the smallest reversible change;
- stop rather than guess when evidence is missing.

This permission does not cover destructive, irreversible, external-account, credential, billing, release, repository-visibility, force-push, or durable-data-loss actions.

## Before runtime animation begins

Required:
- inspect exact parent branch/HEAD;
- select the smallest first animation slice;
- inspect current scene/overlay renderer before introducing a new mechanism;
- avoid duplicating an existing overlay/asset under another ID;
- add tests/contracts for new bindings;
- run exact-HEAD CI/build/emulator checks;
- inspect phone-scale visual evidence;
- update repository-native continuity with actual results.

## Next action

After this log is committed, begin with the smallest reversible animation candidate, currently Service Tunnel ambient infrastructure, unless fresh repository evidence shows a safer prerequisite.
