# D-075 — Phase 1 Persistent Quest Branch / World Consequence Proof

**Status:** VERIFIED / PRIMARY + D-075-B  
**Player-AI:** Veyr  
**Task:** D-075  
**PR:** #66  
**Proof head:** `4b6eee6a19bd69c452b46443e7d15a3b967295a7`  
**Authority merge:** `ad5767d312d9e6fef4b34c0f3cfa339c378826a4`  
**Workflow run:** #352 / `37254171985`  
**Authority observed at evidence write:** `68c59959c0ba842caf8ec4846faea2691965961c`

## Scope

This proof uses the existing `QUEST_DEAD_RELAY` cooperative-vs-solo resolution. It adds no new quest engine, no new canon branch, and no runtime architecture.

Two equivalent initial baselines are resolved through:
- cooperative route with Tamsin;
- solo route keeping Gate Twelve secret.

Both routes:
- reach terminal quest completion;
- save and reload into fresh sessions;
- navigate onward to the same later `DISTRICT_HUB` checkpoint;
- preserve their intended durable branch fingerprint.

## Visible consequence

The cooperative route exposes the later player-safe action:
`ASK_TAMSIN_ABOUT_SHARED_ENTRY`.

The solo route does not.

The cooperative player-safe view does not leak the private memory identifier or raw `memories` container.

This satisfies the required visible later divergence without exposing private NPC state.

## Persistent semantic differences

The normalized fixture records intended branch differences in:
- route;
- party membership;
- Tamsin's Gate Twelve knowledge;
- durable Tamsin memory IDs;
- Tamsin story state;
- trust;
- suspicion;
- goal progress;
- player-safe choice IDs.

Both routes retain the same terminal quest status/stage, so the test distinguishes branch consequence from accidental quest incompleteness.

## Verification

Run #352:
- **python-engine: PASS**
  - 349 tests;
  - `OK`.
- **android-unit-and-assemble: PASS**
  - JVM/unit tests PASS;
  - instrumentation-test compile PASS;
  - debug APK assembly PASS;
  - package/hash verification PASS.
- **android-emulator-smoke: PASS**
  - emulator boot/smoke PASS;
  - screenshot verification PASS.

APK SHA-256:
`4bb7c133dcecfbc9958651f6b3e10e3f3d6aec594c42c2896a87118b735fb28b`

## D-075-B

**VERIFIED.**

`tests/fixtures/d075_dead_relay_branch_diff.json` is the machine-readable normalized branch-difference fixture. The regression test asserts the actual semantic diff keys equal the intended set exactly.

## Files

- `tests/fixtures/d075_dead_relay_branch_diff.json`
- `tests/test_phase1_quest_branch_world_consequence.py`

## Phase 1 impact

D-075 proves:
- requirement #7 — one quest chain with persistent branching;
- a concrete requirement #11 world/actor-state consequence candidate through later visible branch divergence.

The broader integrated acceptance still depends on the tactical chain and later integrated persistence gate.
