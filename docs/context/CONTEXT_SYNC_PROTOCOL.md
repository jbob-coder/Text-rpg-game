# Context Sync Protocol

Purpose: keep multiple ChatGPT chats and human workstreams aligned on the same game without relying on conversational memory.

## Mandatory workflow

Before doing meaningful design or implementation work on this project:
1. Read `docs/context/README.md`.
2. Read `docs/context/GAME_DIRECTION_AND_UI.md`.
3. Read `docs/context/CHECKPOINTS.md`.
4. Read `docs/context/DECISIONS.md`.
5. Read `docs/IMPLEMENTATION_STATUS.md`, `docs/GAME_FOUNDATION.md`, and `docs/SYSTEMS_CATALOG.md`.
6. Read the relevant record under `docs/context/chats/`.
7. For implementation claims, inspect actual source/tests on the branch being discussed.

After meaningful work, append or add a chat/workstream record. Do not overwrite another chat's history to make records agree.

When a user clarifies how the game should feel, progress, present information, or react to choices, update the durable direction records rather than leaving that instruction only in chat.

## Markup vocabulary

Use these markers consistently:

- `[DIRECTION]` — product/design principle. Not an implementation claim.
- `[DESIGNED]` — accepted or actively developed design; code not implied.
- `[IMPLEMENTED]` — corresponding source/data exists.
- `[VERIFIED]` — behavior inspected and/or tests were actually executed with recorded evidence.
- `[PROVISIONAL]` — deliberately temporary, especially balancing values.
- `[UNKNOWN]` — evidence is insufficient.
- `[CONFLICTING]` — sources or workstreams disagree.
- `[SUPERSEDED]` — replaced by a newer accepted decision.
- `[RISK]` — known failure mode, architecture hazard, balancing problem, or continuity risk.
- `[BLOCKER]` — progress cannot safely continue without resolution.
- `[QUESTION]` — open design/technical question.
- `[EVIDENCE]` — file, commit, test, source, or user direction supporting a claim.
- `[SUPERSEDES:<ID>]` — this record replaces a prior decision/checkpoint.
- `[CONFLICTS_WITH:<ID>]` — explicit conflict link.
- `[RELATES_TO:<ID>]` — non-conflicting relation link.

## Checkpoint format

Every checkpoint should contain:

- `CHECKPOINT_ID`
- date/time when known
- branch/repository
- `CURRENT_OBJECTIVE`
- `DIRECTION`
- `VERIFIED_STATE`
- `DESIGNED_NOT_IMPLEMENTED`
- `CONFLICTS`
- `COMPLETED`
- `IN_PROGRESS`
- `NEXT_ACTION`
- `BLOCKERS`
- `RISKS`
- `FILES_CHANGED`
- `TESTS_RUN`
- `TEST_RESULTS`
- `EVIDENCE`

A reported historical test result must be labeled as historical unless this workstream actually ran it.

## Per-chat record rules

Each meaningful chat/workstream gets its own file under `docs/context/chats/`.

A chat record should preserve:
- user instructions that affect product direction
- system designs proposed or accepted
- player-facing UI/status-screen requirements when discussed
- rejected ideas and why
- unresolved alternatives
- conflicts with existing repository documents
- implementation work actually performed
- tests actually run
- decisions that another chat must know before continuing

Do not paste full copyrighted source material or full chat transcripts when a precise technical summary is enough.

## Conflict handling

When two chats disagree:
1. Do not silently merge the claims.
2. Record both positions.
3. Mark the item `[CONFLICTING]`.
4. Identify the evidence for each side.
5. Resolve only from stronger repository evidence or explicit user direction.
6. Record the resolution in `DECISIONS.md` with a new decision ID.

Implementation evidence and product direction answer different questions. Source/tests establish what exists; explicit current user direction establishes what the product is supposed to become. Do not use stale implementation merely to overrule a newer deliberate design decision.

## Compression / difficult-context recovery

When context becomes large, preserve at minimum:
- current objective
- product/game direction
- status-screen/player-information architecture when relevant
- player/stat/system design decisions
- persistent world-state architecture
- NPC memory/knowledge model
- quests and unresolved states
- active design conflicts
- branch/commit/file evidence
- next action

Repository files outrank remembered summaries when they conflict about implementation state. Explicit current user direction supersedes older design assumptions when the user deliberately changes direction, but the change must be recorded rather than silently rewriting history.
