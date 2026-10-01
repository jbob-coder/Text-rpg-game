# Character and Stats inspection handoff

## CURRENT_OBJECTIVE

Implement the approved phone Character/Equipment and Stats direction on the verified
paper-doll contract. This continues the 2026-09-30 user instruction, not the private
campaign or Godot Pixel RPG. External novel attachments were not imported.

## VERIFIED_STATE

- Context recovered from the repository index, Text-rpg-game REPO_CONTEXT,
  conversation log and master log in GAME_CONTEXT_LOGS before implementation.
- Live branches, open PRs, AGENTS.md, task register, historical handoffs, manifests,
  blueprint anchors, runtime source and CI logs inspected.
- `main` remains the placeholder; no merge/promotion/default-branch change.
- PR #10 implementation `5097011f2cb15511e9695edc5475f2fd69c5f655`, run 215 /
  `36778523620`: Python 301/301; Android unit, test compilation, APK assembly/package
  checks passed; API 35 x86_64 emulator **16/16**. APK SHA-256:
  `8e9f08f7281367621c9db05862215a041f0d519b5531348b5e2cac50345c416c`.
- PR #10 tested merge `0dc37385f612a7c566b592738a026ac556eda6d4` and implementation
  head have identical complete tree `a405bce208513835b557b417446c6418326e2822`.
- PR #10 later documentation commit `7d4558ea5c9e3ad24bf29fe42c8f199ed0be60fe`
  changed only the task register; run 218 / `36791439179` completed successfully.
- PR #9 current head `063d5879413b81656cc5c7304be0afd02402f2fd`, run 217 /
  `36778591342`: Python 301/301; Android gates passed; emulator 15/15. APK SHA-256:
  `9d113494e413e44a36bba13a724b4197e33e627a3154aa793a283ec0052a905c`.
- PR #9 tested merge `50a5c2e372e4730d75aa5a40d53a6476ac882eb9` and current
  head have identical tree `1a9f84ad6e6e7a40e0b1f61e6e898e7c925111fb`.
- Diagnostic reader is PRODUCED / VERIFIED / DEFERRED INTEGRATION. Its runtime
  implementation evidence remains in Wave M on PR #9; no arbitrary character binding.
- PR #7 run 209 and PR #8 run 211 passed at their current heads. Environment modules
  058–061 remain deferred from scene integration.

## IMPLEMENTED / PENDING ANDROID VERIFICATION

Branch: `feature/character-stats-inspection`, PR #13. Consolidates PR #11 stat
inspection and PR #12 Character UI with responsive layout, equip-from-Bag details
and bounded contribution labels. Stack base:
`feature/character-equipment-paperdoll-ui@40c95ec2e2b44aeb6a8ae1a23c28bbaf04e7a6d7`.
PR #10 remains the authored-overlay dependency. Concurrent screenshot fixes
`699e6c7` / `746e2152d617e4150f92d9fb604fbb1d3643d757` are preserved.

- Character uses width-constrained equipment cards around the central avatar, with
  a larger-text/narrow-container alternative and vertical scrolling.
- Selecting a slot opens a scrollable detail dialog. Equip/unequip emits existing
  engine requests; busy state disables mutation controls. Details follow the fresh
  snapshot after mutations, without cached item state or a duplicate equipment strip.
- Stats uses a compact player summary, resources, all seven canonical attributes,
  one selected attribute explanation, skills, derived values and visible conditions.
- Attribute and skill selection keeps PR #11's asynchronous, mutation-serialized
  inspection path and public loading/error state. Snapshot totals and on-demand
  inspection are checked for consistency.
- Attribute/skill display contributions are derived in Python from the existing
  `inspect_status_value()` redaction boundary before source labels are resolved.
  Hidden conditions/perks remain an anonymous numeric contribution.
- Android maps the bounded display records, validates their kinds/finite values,
  and displays engine totals without recalculation. Missing contribution lists remain
  compatible with older snapshots. Fractional values are preserved in display.
- The avatar renderer retains its exact item+slot registry, zOrder, same 32x48 canvas
  and common origin. The Character surface hides only duplicate summary text.

## TESTS_RUN / RESULTS

- Baseline: `PYTHONPATH=src python -m unittest discover -s tests -v` — 301/301 passed.
- Four new projection tests observed failing before implementation (missing
  contribution field), then passing after implementation.
- Current consolidated local full suite: **308/308 passed**, no failures/errors.
- First PR #13 implementation `ad856cfc792e19e844a8fa49159bacb34b56114f`,
  run 222 / `36793210191`: Python 305/305 and Android unit/compile/assemble passed;
  all 22 emulator tests passed. The workflow failed afterward because the external
  screenshot path did not exist. This is not a successful complete gate.
- Run 226 / `36794005834` at `746e2152d617e4150f92d9fb604fbb1d3643d757`
  again passed Android build and 22 emulator tests, but app-private screenshot
  export failed. The emulator action executes each script line in a separate
  shell, so shell-local export variables do not persist between lines.
- Screenshot capture now uses AndroidX `PlatformTestStorageRegistry` and
  Gradle's collected additional-test-output directory. A separate host step
  verifies all four PNGs before uploading. The consolidated implementation
  still needs its own fresh exact-head gate and screenshot review.
- `git diff --check`: passed.
- Local Android compilation/emulator execution: unavailable (no local SDK/Gradle).
  The consolidated workflow gate remains pending until observed; do not infer
  Android success from Python, predecessor gates or the authored tests.

New tests cover canonical values/bonuses, equip/unequip and save/load, hidden registry
and runtime provenance, net cancellation, detached records, Kotlin mapping/formatting,
320dp and large-text layouts, selection/mutation callbacks, stale-detail prevention,
and real Activity -> Python equip -> Stats -> unequip.

## VISUAL REVIEW

The emulator tests capture actual Compose screenshots of a 320dp projected-state
fixture and equipment/attribute details. The workflow retains only the small PNGs
for one day; APK upload remains limited to manual runs. These are rendered UI fixtures,
not physical-device screenshots or canonical character-turnaround approval.

The connected Activity test separately exercises the real Python engine. Native-scale
art approval and physical Galaxy A03 visual/performance/input/TTS checks remain open.

## DECISIONS / RISKS

- Seven attributes, authored equipment modifiers, stable item/slot IDs, save schema
  and content are unchanged; no canon or save migration.
- Contributions describe direct attribute/skill bonuses. Derived formula explanations,
  unequipped-item comparison and dedicated Skills/Bag redesign are later slices.
- Player/Tamsin canonical reference selection remains blocked; held-reader binding
  still requires authored pose/rig support and player-safe presentation state.
- Regular local feature merges preserve PR #11/#12 and screenshot-fix ancestry.
  This does not merge any PR remotely or consolidate deferred asset branches.
- PR #14 Skills work appeared concurrently; it is independent and is not overwritten
  or silently incorporated into this Character/Stats gate.

## NEXT_ACTION

Run exact-head Python/Android/emulator workflow, inspect the exported screenshots,
repair observed failures, and record implementation SHA, tested merge/tree, run/jobs,
test counts, APK hash and screenshot identities in `docs/verification/character_stats/`.
Complete task P-005 only after the gate passes. Keep physical-device limitations visible.

## CONTINUITY GRAPH

| From | Relationship | To |
| --- | --- | --- |
| User direction 2026-09-30 | constrains | Overlay rig and canonical Stats/Character UI |
| PR #10 | provides | Exact 32x48 authored equipment renderer |
| `inspect_status_value` | redacts before projection | Attribute/skill contributions |
| Android bridge + mapper | provide | Player-safe display records |
| Character / Stats sections | consume | Authoritative snapshot and existing mutation callbacks |
| Projection + JVM + Compose + Activity tests | verify | Boundaries and interactive presentation |
| Task P-005 + verification manifest | track | This implementation slice and pending evidence |
