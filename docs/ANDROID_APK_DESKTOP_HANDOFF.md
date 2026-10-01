# THE GAME — Android APK and desktop continuation

Repository: `jbob-coder/Text-rpg-game`  
Working branch: `fix/player-hub-runtime-recovery` / PR #15  
Implementation candidate: `f88453c38b8efd91a4af74b3cd4f59b6903a9a03`  
Verification status: verified on Android API 35 x86_64; APK delivered. Physical Galaxy A03 acceptance remains open.

This handoff finishes the outstanding Character/Stats build and APK request. The complete game still has work remaining in content, progression, authored character references, device validation and production polish. `main` is a placeholder and remains unchanged.

## What this candidate implements

- Character fits a phone-width layout, with equipment slots surrounding the avatar and a larger-text alternative. A selected slot opens one scrollable, height-limited dialog for current bonuses and engine-owned equip/unequip actions.
- Stats uses a compact summary, all seven canonical attributes, resources, skills, derived values and one selected explanation. Equipment contributions come from the Python engine's redacted inspection boundary.
- More → Skills opens the dedicated skill list and requests the same authoritative inspection API. Fractional values retain their display precision.
- Missing or malformed saves show their public error inside the playable game. A failed load preserves the current snapshot and corrupt save bytes. Startup failures still use the startup error screen.
- Avatar equipment retains exact item + slot mappings, explicit z-order and the shared transparent 32×48 canvas. Unknown visual mappings do not generate invented clothing or equipment art.

Canonical attributes remain Might, Agility, Endurance, Intellect, Will, Perception and Presence. The jacket still grants +2 Endurance, gloves +1 Technical Systems, ring +1 Perception and neck tag +1 Presence. Save schema 1 and stable IDs are unchanged.

## Branch relationships

| Branch / PR | Role | Continuation rule |
| --- | --- | --- |
| `integration/android-open-world-v1-reconcile` / #5 | Android/world integration parent | Keep its existing engine/world contracts. |
| `feature/pixel-asset-wave-a` / #7 | Current pixel catalog and named scene art | Do not replace named scenes simply to increase asset completion. |
| `fix/avatar-overlay-rig-contract` / #10 | Exact authored paper-doll registry | Retained in this candidate's ancestry. |
| `feature/player-safe-stat-inspection` / #11 | Redacted on-demand stat inspection | Retained; UI does not own calculations. |
| `feature/character-equipment-paperdoll-ui` / #12 | Initial Character UI | Parent of the responsive consolidation. |
| `feature/character-stats-inspection` / #13 | Responsive Character/Stats and display contributions | Run 229 passed at `0fe6a9f…`; visual review motivated this follow-up. |
| `feature/player-safe-skills-ui` / #14 | Dedicated Skills surface | Consolidated into #15 with its source ancestry preserved. Do not apply it again blindly. |
| `fix/player-hub-runtime-recovery` / #15 | Consolidated candidate and requested APK gate | Start desktop work from the verified implementation below. |
| `feature/pixel-asset-wave-l-environment-modules` / #8 | Environment assets 058–061 | Produced/verified; scene integration remains deferred. |
| `feature/pixel-asset-wave-m-diagnostic-reader` / #9 | Diagnostic reader 034 | Produced/verified; held-character integration remains deferred. |

No PR was remotely merged, no history was force-pushed, and no release/store build was published. The source merge into #15 consolidates feature ancestry on that working branch; it does not promote the default branch.

## Open the tested source on a computer

Use a fresh directory so existing local changes are preserved:

```bash
git clone --branch fix/player-hub-runtime-recovery https://github.com/jbob-coder/Text-rpg-game.git
cd Text-rpg-game
git checkout --detach f88453c38b8efd91a4af74b3cd4f59b6903a9a03
git status --short
```

For new work, create your own branch from that commit with `git switch -c feature/device-qa-continuation`. Before editing, read `AGENTS.md`, `docs/THE_GAME_MASTER_TASK_REGISTER.md`, `docs/IMPLEMENTATION_STATUS.md`, `docs/V6_STABILIZATION_HANDOFF.md` and the handoffs relevant to your change. Recheck live branch heads and CI; dated context logs are secondary to repository evidence.

The repository-owned build uses JDK 17, Gradle 9.4.1, Python 3.10, Android SDK 37 and the pinned project dependencies. There is no claimed local Android build from this ChatGPT workspace; Android execution uses the documented CI environment.

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
gradle -p android testDebugUnitTest
gradle -p android :app:assembleDebugAndroidTest
gradle -p android :app:assembleDebug
gradle -p android connectedDebugAndroidTest
```

The commands above use Bash environment syntax. On Windows PowerShell, set `$env:PYTHONPATH = "src"` before running `python -m unittest discover -s tests -v`; the Gradle commands are unchanged.

The connected test command requires a running compatible emulator or device. The APK output is `android/app/build/outputs/apk/debug/app-debug.apk`. The candidate includes ARMv7, ARM64 and x86_64 libraries; its declared minimum is Android 7.0 / API 24. It is a debug build for testing.

## Device acceptance still required

1. Install the delivered APK on the Galaxy A03 and confirm visible startup, Story, Character, Stats, More → Skills, Bag and Map.
2. Equip/unequip the jacket and confirm Endurance changes between 35 and 37 while the authored overlay appears/disappears. Confirm unmapped items do not generate avatar art.
3. Check equipment dialog height, both slot rails, large text, scrolling and readable cyan/gold contrast. The included screenshots show actual rendered Compose fixtures; they are not physical-handset photos or approval of a canonical character turnaround.
4. Save, advance, load and confirm restoration. Check missing/malformed-load recovery without deleting the only save.
5. Check touch response, memory/performance, narration and available offline TTS voices on the device. Emulator evidence does not establish those physical-device results.

The package is `com.thegame.rpg`. If installing over an older debug build fails because its signing certificate differs, preserve its saves before considering any uninstall. Do not reset or clear app data as a routine troubleshooting step. A durable signing/update policy remains future work.

## Next engineering work

Finish physical-device acceptance before calling this APK device-approved. Then choose a small implementation slice from the live task register. Preserve `GameState → World/Quest/Narrative → Rules/Stats/Abilities/Equipment → player-safe projection → Android UI`. Keep raw story flags and hidden provenance out of Compose.

Additional player/Tamsin art and the held diagnostic reader require approved rig/pose and projected presentation-state support. Existing reusable environment modules remain available for legitimate future consumers. Novel attachments and the private campaign were not imported into this Android repository.

## Exact verification and delivered artifact

Completed: 2026-09-30 21:21 AST.

| Evidence | Result |
| --- | --- |
| Implementation | `f88453c38b8efd91a4af74b3cd4f59b6903a9a03` |
| Tested temporary merge | `a59b12d9ad3f272086666cf50bf998da8ae4c3b4` |
| Both complete Git trees | `f238a2e20665695ea2ed9a959251fbbf3c2962a9` |
| Android Pixel Client | Run 233 / `36799678887`, all three jobs passed |
| Python | 308/308 passed, both locally and in CI |
| Android | Unit tests, instrumentation compilation, assembly, ABI/content checks and APK signing verification passed |
| Representative runtime | API 35 x86_64, 30/30 connected tests, 0 failures/skips |
| Screenshots | Four downloaded/hash-verified PNGs, all visually reviewed |
| APK | `THE-GAME-character-stats-f88453c.apk`, 48,331,290 bytes (46.09 MiB) |
| APK SHA-256 | `8decee3cb660015e8b048a495509a8856673023bdc2c9f99d4200148ef243fe3` |
| Signing | Verified APK Signature Scheme v2; Android Debug certificate |
| Certificate SHA-256 | `144f73b0eee46e3079e0e4f7d658fa591320336da30e606736e704ed07df4407` |

Workflow: https://github.com/jbob-coder/Text-rpg-game/actions/runs/36799678887

The evidence archive contains this handoff, `verification.json`, build-source/signature records and all four screenshots. `equipment-jacket-detail.png` is now 1120×899 rather than the earlier 1120×2387 full-height panel; the other captures are 1120×2240. Accessory labels and the dark application background were reviewed. These confirm the approved layout/style direction in rendered fixtures; exact comparison with unavailable original mockup images and physical-device approval are not claimed.

The five failures reproduced in run 230 were fixed. Runs 231/232 stopped at merge-related compile defects, which were corrected before the green run. They remain historical failed-job evidence, not acceptance gates.

Repository evidence and any later documentation commit identify this immutable runtime separately. Documentation-only changes do not make a new delivered APK or change this hash.
