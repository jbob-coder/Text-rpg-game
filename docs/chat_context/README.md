# Shared Game Context Branch

Branch: `shared/game-context`
Base: `foundation/text-rpg-systems`

Purpose: preserve game-development context from separate ChatGPT conversations without requiring the chats to communicate directly.

## Rule

Each chat writes to its own context file under `docs/chat_context/`. Do not overwrite another chat's file. Shared facts should only be promoted into canonical project documentation after they are verified against the repository and, where applicable, approved by Jack.

## Status labels

- `CONFIRMED`: verified in repository files/tests or explicitly fixed by Jack as a project decision.
- `DIRECTION`: intended design direction stated by Jack; not necessarily implemented.
- `DESIGNED`: documented design or architecture not yet proven as integrated behavior.
- `UNVERIFIED`: prior-chat claim or proposed work that has not been checked in the current repository state.
- `SUPERSEDED`: older direction replaced by a later decision.

## Authority

Repository state outranks chat recollection for implementation facts. For this shared context branch, keep implementation facts separate from design intent. Do not treat reference material as game canon.

## Files

- `CHATGPT_TEXT_RPG_CONTEXT_2026-09-26.md` — context from the current Text RPG conversation.
- Other chats should create their own clearly named file in this directory rather than editing the current-chat record.

## Reference-material rule

`My Vampire System` material is research/reference only. Extract abstract mechanics and design lessons; do not copy protected prose, characters, names, setting, dialogue, or unique story content into the game. The game must remain an original IP.
