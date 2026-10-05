# D-065 — Tamsin Durable-Memory Reactive Proof Evidence

**Status:** VERIFIED / PRIMARY + BONUS  
**Player-AI:** Veyr  
**Task:** D-065  
**Implementation proof commit:** `e339b4b0fa7e77b722c26a605670cab8000f3551` and its D-065 ancestry  
**Integration run:** PR #59 workflow run #341 / `37252547112`  
**Proof head:** `583e61dffc08c3989af4c15561d8eabf1ff6468d`  
**Merged authority proof:** `e883205559c64d2e82614160bd6548c2c9332808`

## Why this run is valid for D-065

The D-065 implementation commit is an ancestor of the PR #59 proof head with no reverse divergence. The complete Python suite on that proof head executed the D-065 tests directly.

Subsequent commits through the Overseer review changed documentation, Android bridge/inventory compatibility, D-064 acceptance tests, D-068 proof tests and related coordination surfaces; no D-065 social/memory implementation or authored Tamsin reaction file was replaced after the green D-065 test execution.

Therefore the D-065 task-specific evidence can be reused without forcing Veyr to rerun an identical social proof solely because unrelated D-064/D-067 integration failures kept the aggregate job red.

## Verified D-065 tests from run #341

All of these executed PASS in the complete Python suite:

- `test_memory_route_is_deterministic`
- `test_memory_survives_save_and_unlocks_later_reaction`
- `test_npc_remembers_is_read_only`
- `test_private_memory_is_not_exposed_but_reaction_is_player_safe`
- `test_validation_rejects_malformed_memory_effect`

## Primary acceptance mapping

- Existing cooperative interaction writes durable memory `MEM_TAMSIN_ENTERED_GATE_TWELVE_WITH_JACK`.
- The memory survives save/load.
- Later authored choice `ASK_TAMSIN_ABOUT_SHARED_ENTRY` is unlocked by that memory.
- Choosing the later reaction changes durable relationship/state and removes the one-shot reaction afterward.
- Same route produces deterministic memory/choice state.
- NPC memory query remains read-only.
- Private memory content is not exposed in the player-safe Android scene view.

## D-065-B bonus

**VERIFIED.**

The negative projection regression proves that the player-safe JSON contains the allowed later reaction but does not contain:
- the private memory ID;
- `memories`;
- `goals`;
- `story_state`.

## Global limitation

Run #341 was not globally green because unrelated transition defects existed in D-064/D-067 integration. D-065 does not claim the green-authority checkpoint. Those external failures do not invalidate the executed D-065 tests above.
