# World Director Memory Layer

Status: ACTIVE_CAMPAIGN_CONTINUITY
Created: 2026-09-29
Campaign: ChatGPT-narrated Text RPG / Jack Wilson continuity
Purpose: persistent operational memory for the living world, distinct from deep history and engine implementation.

## Why this exists

The repository already stores:
- deterministic RPG engine rules;
- historical worldbuilding;
- campaign authority corrections.

This layer stores what a future narrator needs in order to resume the *living world*: current anchors, unresolved facts, active pressures, off-screen events, and causal consequences.

It must never rely on chat memory alone.

## Authority order

1. Current explicit user instructions.
2. `context/CURRENT_NARRATIVE_AUTHORITY.md`.
3. `context/chats/text-rpg-foundation-chat/NARRATIVE_CANON_CORRECTION_2026-09-29.md`.
4. `context/world_director/LIVE_WORLD_STATE.md`.
5. `context/world_director/WORLD_EVENT_LEDGER.md`.
6. Campaign-specific files explicitly referenced by the live state.
7. `docs/world_history/WORLD_HISTORY_MASTER_INDEX.md` and its active campaign files.
8. Older summaries only when compatible.

## Boot sequence for a future narrator

Read in this order before continuing live play:

1. `context/CURRENT_NARRATIVE_AUTHORITY.md`
2. `context/world_director/README.md`
3. `context/world_director/WORLD_DIRECTOR_PROTOCOL.md`
4. `context/world_director/LIVE_WORLD_STATE.md`
5. `context/world_director/ACADEMY_CONTINUITY_ANCHOR.md`
6. `context/world_director/WORLD_EVENT_LEDGER.md`
7. Any files referenced by LIVE_WORLD_STATE as current scene/character/location state.
8. `docs/world_history/WORLD_HISTORY_MASTER_INDEX.md` only as needed for broader causal history.

If a required live-state fact is absent, mark it UNKNOWN. Do not import a similarly named fact from another Jack Wilson project.

## Separation of concerns

- `docs/world_history/` = what happened historically.
- `context/world_director/` = what is true or active now and how the narrator simulates it.
- `src/textrpg/` = deterministic implementation machinery.
- `content/` = authored playable content.
- chat memory = convenience only, never sole authority.

## Core rule

The narrator may control the world, institutions, NPCs, hidden events, timing pressures, discoveries, failures, wars, rumors, markets, weather, ecology, and causal consequences.

The narrator does **not** choose Jack Wilson's unspoken decisions, beliefs, dialogue, or voluntary actions. Player agency remains with the user.
