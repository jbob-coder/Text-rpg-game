# Shared Context Architecture

This directory is the coordination and continuity layer for `jbob-coder/Text-rpg-game`.

It exists so multiple ChatGPT conversations, human contributors, and future tools can reconstruct the same project state without relying on chat memory.

## Branch roles

- `shared/game-context` — shared documentation, conversation-derived direction, checkpoints, decisions, conflicts, handoffs, and architecture references.
- `foundation/text-rpg-systems` — implementation branch identified by the current repository status documentation.
- `main` — must not be treated as containing unmerged foundation work unless verified directly.

The context branch does not prove that a design exists in executable code. Implementation claims require repository evidence.

## Canonical reading order

A new chat working on this game should read, in order:

1. `docs/context/README.md`
2. `docs/context/CONTEXT_SYNC_PROTOCOL.md`
3. `docs/context/CHECKPOINTS.md`
4. `docs/context/DECISIONS.md`
5. `docs/IMPLEMENTATION_STATUS.md`
6. `docs/GAME_FOUNDATION.md`
7. `docs/SYSTEMS_CATALOG.md`
8. relevant entries under `docs/context/chats/`
9. the actual source/tests for any implementation-specific claim

## Authority order

When sources conflict, use this order:

1. Current executable source, authored content, schemas, and tests on the branch being discussed.
2. Current repository implementation/status documents when they are supported by repository evidence.
3. Accepted decisions and checkpoints in this directory.
4. Per-chat context records.
5. Chat memory or conversational recollection.

If a lower source disagrees with a higher source, do not silently merge them. Record a conflict.

## Required state labels

Every non-trivial project claim should be classifiable as one of:

- `DIRECTION` — product/design principle guiding the project; not itself an implementation claim.
- `DESIGNED` — agreed conceptual design, not proven implemented.
- `IMPLEMENTED` — code/data exists that appears to implement it.
- `VERIFIED` — implementation was checked by inspection and/or an executed test with recorded evidence.
- `PROVISIONAL` — intentionally temporary or subject to balancing/revision.
- `UNKNOWN` — evidence is insufficient.
- `CONFLICTING` — two authoritative-looking sources disagree and require resolution.
- `SUPERSEDED` — replaced by a newer accepted decision.

`IMPLEMENTED` and `VERIFIED` are deliberately different. A file existing is not the same as runtime behavior having been tested.

## Files in this context layer

- `CONTEXT_SYNC_PROTOCOL.md` — mandatory procedure, markup vocabulary, evidence rules, handoffs, conflict handling, and checkpoint rules.
- `CHECKPOINTS.md` — append-only project checkpoints.
- `DECISIONS.md` — compact architectural/design decision log.
- `chats/` — one independent context record per meaningful chat/workstream.

## Anti-drift rules

- Never simplify, reset, or replace established project direction silently.
- Never promote a conversation idea directly to `IMPLEMENTED`.
- Never overwrite another chat's record to make histories agree.
- Prefer adding a newer record with `SUPERSEDES`/`CONFLICTS_WITH` links.
- Preserve unresolved questions and risks during context compression.
- Important continuity must live in files and stable IDs, not only prose memory.
- Repository files outrank remembered summaries when they conflict.

## What belongs in a chat record

Record only information relevant to continuing the project:

- user direction and constraints
- accepted designs
- rejected/superseded designs
- implementation claims and their evidence
- files changed
- tests actually run and observed results
- architecture decisions
- unresolved questions
- known risks
- next action

Do not copy an entire transcript when a precise durable summary captures the same project state.
