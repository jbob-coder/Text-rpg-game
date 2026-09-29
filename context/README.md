# Shared Game Context Registry

Branch: `context/shared-game-context`

Created: 2026-09-26

## Read first for the narrated Jack Wilson campaign

For the ChatGPT-narrated campaign, read `context/CURRENT_NARRATIVE_AUTHORITY.md` before older cross-project summaries. The current campaign authority is Jack Wilson with the ability `Steal`, with ChatGPT acting as narrator / Game Master. Android/APK, open-world Android, pixel-client work, unrelated Jack Wilson continuities, and any ability assignment replacing `Steal` are outside this campaign unless the user explicitly reintroduces them.

The dated correction record is `context/chats/text-rpg-foundation-chat/NARRATIVE_CANON_CORRECTION_2026-09-29.md`.

## Purpose

This branch is a shared continuity registry for multiple ChatGPT conversations working with the user on game projects. Each chat contributes **its own accessible context separately**. The files are not a claim that one chat can directly read another chat's private runtime context; the repository is the exchange layer.

## Contribution protocol

1. Each chat writes only inside its own folder under `context/chats/`.
2. Do not overwrite another chat's context file.
3. Do not silently merge contradictory memories. Record the conflict and the date/source instead.
4. Separate:
   - `VERIFIED_REPO`: observed directly in the live repository/files.
   - `USER_CURRENT`: current explicit user instruction.
   - `USER_PRIOR`: prior user instruction recovered from earlier conversations.
   - `DERIVED`: design interpretation or abstraction.
   - `STALE_OR_SUPERSEDED`: older project state retained only for continuity.
   - `UNKNOWN`: not verified.
5. Live project files and current explicit user instructions outrank old chat memory.
6. Never claim IMPLEMENTED / TESTED / VERIFIED unless the evidence was actually observed.
7. Keep projects separate. Similar mechanics across projects do not make them the same project.
8. Preserve original IP. Reference novels/games may inform abstract mechanics, but copyrighted story text, characters, names, and proprietary setting material are not game canon.
9. Runtime generative AI is not assumed unless a specific project explicitly requires it. Current Text RPG foundation explicitly does **not** require runtime generative AI.
10. Cost constraint: prefer free/local tooling; do not introduce paid or billing-risk services without explicit authorization.

## Current contributor folders

- `context/chats/text-rpg-foundation-chat/` — context contributed from the chat that is currently developing `jbob-coder/Text-rpg-game`.
- Other chats should create a new sibling folder with a distinct name and place their own context there.

## Project-specific continuity note

The uploaded private-RPG continuity rules state that important state should live in files, not chat memory; long history may be summarized, but current state, location, quests, NPC memory, and unresolved threads must survive. Those rules also say not to move that game into a repository unless explicitly requested. The user explicitly requested this shared repository branch, so repository use is authorized for this context registry.

## Do not use this branch as automatic canon

This branch preserves knowledge and provenance. Individual game repositories and their verified files remain the authority for implementation details.
