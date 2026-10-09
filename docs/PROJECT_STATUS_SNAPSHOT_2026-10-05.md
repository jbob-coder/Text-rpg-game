# THE GAME — Project Status Snapshot — D-081 Baseline

> **HISTORICAL EXACT-REVISION SNAPSHOT:** every count, percentage, task state and “active critical dependency” statement below applies only to source HEAD `37cc88b6d068cdc160ecb5c69fdb9a1b0c1aeb7d` on 2026-10-05. It is immutable evidence, not today's queue. For current ownership/readiness use the live Bulletin; for current semantic/completion reporting regenerate the tracker at the desired revision under `docs/PROJECT_STATUS_TRACKING_STANDARD.md`.

**Source HEAD:** `37cc88b6d068cdc160ecb5c69fdb9a1b0c1aeb7d`  
**Tree SHA:** `b06d1096dffcca1b29ad48b2c7a69447cb425499`  
**Tree completeness:** recursive Git tree `truncated=false`  
**Evidence:** `docs/evidence/D081_PROJECT_STATUS_BASELINE_2026-10-05.json`  
**Tracker:** `tools/project_status_tracker.py`  
**Metric standard:** `docs/PROJECT_STATUS_TRACKING_STANDARD.md`

## Executive status

At the exact source HEAD above:

- **Master Task Register completion:** **67.07%** — 55 of 82 registered tasks are DONE.
- **Phase 1 D-060..D-079 completion:** **45.00%** — 9 of 20 tasks are DONE.
- **Tracked files:** **620**.
- **Tracked blob bytes:** **6,546,962**.
- **Repository Markdown documents:** **425**.
- **Markdown documents under `docs/`:** **423**.
- **Structured documentation paths under `docs/`:** **25**.
- **Document-like paths:** **450**.

The 67.07% number is a conservative task-register metric only. It does **not** mean that 67.07% of all game content, worldbuilding, art, runtime implementation, Android release work, or final APK work is complete.

## Task-state map

- DONE: **55**
- IN_PROGRESS: **10**
- BLOCKED: **3**
- PENDING: **9**
- OTHER/non-canonical active state: **4**
- UNKNOWN/missing recognized status: **1**

The non-canonical/unknown states count as incomplete.

## Phase 1 D-060..D-079

- DONE: **9**
- IN_PROGRESS: **1** — D-064.
- BLOCKED: **1** — D-069.
- PENDING: **9** — D-070, D-071, D-072, D-073, D-074, D-076, D-077, D-078, D-079.

The active critical dependency remains D-064 -> D-069.

## Top-level repository map

| Area | Files | Tracked bytes |
|---|---:|---:|
| `docs/` | 455 | 4,866,103 |
| `android/` | 101 | 883,400 |
| `tests/` | 31 | 316,205 |
| `src/` | 20 | 318,399 |
| repository root | 4 | 27,002 |
| `tools/` | 4 | 59,108 |
| `content/` | 3 | 68,788 |
| `.github/` | 2 | 7,957 |

## Documentation-area map

| Area | Files | Tracked bytes |
|---|---:|---:|
| `docs/systems/` | 268 | 2,182,978 |
| `docs/` root | 56 | 1,140,731 |
| `docs/assets/` | 49 | 733,977 |
| `docs/evidence/` | 18 | 254,674 |
| `docs/world/` | 18 | 102,092 |
| `docs/android/` | 14 | 157,692 |
| `docs/GAME_CONTEXT_LOGS/` | 13 | 49,176 |
| `docs/verification/` | 10 | 169,386 |
| `docs/overseer/` | 5 | 32,555 |
| `docs/player_guide/` | 3 | 32,307 |
| `docs/superpowers/` | 1 | 10,535 |

## Document-count definitions

The project now reports more than one document count so the word “documents” is not ambiguous.

- **Repository Markdown documents:** every tracked `.md` path.
- **Docs Markdown documents:** tracked `docs/**/*.md`.
- **Structured docs under docs:** tracked `.json`, `.yaml`, `.yml`, and `.csv` under `docs/`.
- **Document-like paths:** `AGENTS.md` + `README.md` + docs Markdown + structured docs.

Logs, PNGs, source files and build/config files are not counted in the document-like total.

## Major non-DONE areas at the baseline

Current in-progress or blocking work includes:

- D-006 — existing-state repository audit;
- D-019 — reproducible documentation/world/asset inventory;
- D-021 / D-026 — Android consumer/projection mapping;
- D-029 — asset provenance/stage exactization;
- D-042 — deep source audit;
- D-045 — reconstruction-grade domain documentation;
- D-046 — Status UI / ability / passive reconstruction corpus;
- D-064 — player-safe room/actor projection;
- D-069 — tactical schema/grid core, blocked on D-064;
- D-012 / D-033 — late-stage APK work blocked;
- D-070..D-079 remaining Phase 1 implementation/verification tasks;
- D-081 — status tracker itself was IN_PROGRESS at this source revision.

The exact complete non-DONE list and raw statuses are preserved in the JSON evidence file.

## How future Nodus reports status

From a complete checkout:

```bash
python tools/project_status_tracker.py \
  --revision HEAD \
  --json-output /tmp/the-game-project-status.json \
  --markdown-output /tmp/the-game-project-status.md
```

For historical status, use an exact commit SHA instead of `HEAD`.

The tracker resolves the requested revision to an immutable commit, inventories committed paths, reads the Master Task Register from that same commit, and ignores dirty/untracked working-tree state.

## Validation

D-081 validation completed:

- complete GitHub recursive tree reconciliation: **PASS**;
- tree returned `truncated=false`;
- exact task-register parser reconciliation: **PASS**;
- synthetic local Git repository validation of status parsing: **PASS**;
- dirty/untracked isolation test: **PASS**;
- document-count test: **PASS**;
- task-completion and Phase 1 percentage test: **PASS**.

No full runtime/Android build pass is claimed by this documentation/tooling task.

## Authority boundary

This snapshot is a reporting view, not a replacement authority.

- exact repository state remains structural truth;
- `docs/THE_GAME_MASTER_TASK_REGISTER.md` remains task-state authority;
- D-019 remains the detailed corpus/inventory authority;
- `docs/MASTER_DOCUMENTATION_RECORD.md` remains documentation interpretation authority;
- fresh runtime/build/test evidence remains necessary for implementation claims.
