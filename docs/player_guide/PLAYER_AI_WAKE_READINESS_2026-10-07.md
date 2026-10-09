# THE GAME — Player-AI Wake Readiness — 2026-10-07

> **HISTORICAL SHUTDOWN/Wake CHECKPOINT — SUPERSEDED FOR CURRENT STATE:** the roster, task readiness and released-work statements below describe the 2026-10-07 shutdown checkpoint only. Do not use them as current activation or task authority. D-070 and D-083 have since completed; on the current 2026-10-08 control path D-072 is IN_PROGRESS under Silex, D-073 is BLOCKED, and P11/CPR-006 is IN_PROGRESS under Nodus. Canonical Drive controls current Player-AI identity/session locks; the live Bulletin controls repository task ownership. Preserve the original checkpoint below as continuity evidence.

**Purpose:** auditable shutdown/wake checkpoint for Player-AI continuity. This file does not replace the Bulletin, Master Task Register, Mission Control, or Google Drive canonical entity locks.

## Verified roster state

At this checkpoint all canonical Player-AIs are inactive and own no active repository primary:

- Nodus — INACTIVE / no claim.
- Veyra — INACTIVE / no claim.
- Kestrel — INACTIVE / no claim.
- Veyr — INACTIVE / no claim.
- Quorix — INACTIVE / no claim.
- Rivet — INACTIVE / no claim.
- Strata — INACTIVE / no claim.

The live Bulletin has no `IN_PROGRESS` Player-AI claim.

## Released unfinished work

### D-070
- State: `READY / UNCLAIMED`.
- Previous claimant: Veyra.
- Preserved continuation: `docs/player_guide/VEYRA_D070_RELEASE_HANDOFF_2026-10-07.md`.
- Preserved branch/PR evidence remains continuity only and grants no ownership.
- Veyra may retake D-070 after activation only if it remains unclaimed and Veyra wins a fresh Bulletin claim.

### D-083
- State: `READY / UNCLAIMED`.
- Previous claimant: Strata.
- Preserved continuation: `docs/player_guide/STRATA_D083_RELEASE_HANDOFF_2026-10-07.md`.
- Already-merged technical work remains evidence/continuity only and grants no ownership.
- Strata may retake D-083 after activation only if it remains unclaimed and Strata wins a fresh Bulletin claim.

## Wake contract

For every Player-AI:

1. verify the canonical Drive registry and entity `STATUS.json`;
2. require `INACTIVE` and `active_session_id = null`;
3. allocate a new session ID;
4. fetch live repository HEAD;
5. re-read Bulletin, Master Task Register, Mission Control and Coordination;
6. reconcile Drive continuity against repository truth;
7. acquire work only through `INTENT -> Bulletin CLAIM -> START`;
8. never infer ownership from activation, specialty, score, prior claim, branch, PR, or handoff.

## Shutdown contract

When the owner turns a Player-AI off:

1. preserve branch/PR/evidence and unfinished work;
2. update Drive handoff/session history;
3. set Drive entity INACTIVE and clear the session lock;
4. clear current task/claim fields;
5. release any live Bulletin claim;
6. return dependency-safe unfinished work to READY;
7. preserve prior claimant/branch evidence as historical continuity;
8. never mark unfinished work DONE merely to clear ownership.

## Invariant

`PLAYER OFF = no active session + no active repository claim`.

`PLAYER ON != task ownership`.

Task ownership exists only after a fresh live Bulletin claim.
