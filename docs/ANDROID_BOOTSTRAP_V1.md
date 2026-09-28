# Android Runtime Bootstrap V1 — P0 handoff

Updated: 2026-09-27 21:40 AST

## Objective

Replace the unrecoverable ephemeral Android wrapper with a repository-owned,
reproducible client path that can diagnose the user-reported black screen and preserve
the stabilized Python rules engine as the authority.

Working branch: `feature/android-runtime-bootstrap-v1`  
Base: `fix/v6-runtime-boundaries@7be1adef22a1bf9d4826691e665b7417235f53a5`

## Decisions

1. **Embed the existing engine; do not port rules into Java/Kotlin.**
   Chaquopy is used as the Android/Python boundary. The app packages the current
   `src/textrpg` tree directly.
2. **Keep the first Android client deliberately small.**
   The first gate is startup, first-scene rendering, deterministic choices, save/resume,
   and diagnostics. Full navigation, avatar layers, map, audio, and final pixel assets
   remain separate tasks.
3. **Show UI before Python startup.**
   `MainActivity` installs a visible boot surface first, then starts Python from a
   single background executor. Catchable Python/Java/native-linker initialization
   failures are shown on-screen plus Logcat; native stdout/stderr are redirected for
   startup diagnosis. A process-killing native crash still requires Logcat evidence.
4. **Use only player-safe projections for rendering.**
   Scene rendering consumes `RulesEngine.build_scene_view()`; status rendering consumes
   `build_status_view()`. Authored requirements/outcomes, raw modifier provenance, and
   resolution history are not sent to the visible Android UI.
5. **Persist authoritative state, not duplicated UI state.**
   Choice execution occurs through `RulesEngine.choose()`. Schema-1 JSON from
   `dumps_state()` is written with Android `AtomicFile`; resume uses `loads_state()`.
6. **Retain 32-bit ARM coverage.**
   Python 3.11 plus `armeabi-v7a` avoids assuming every low-end Android installation
   exposes a 64-bit userspace. `arm64-v8a` and `x86_64` are also packaged.
7. **Pin the build chain.**
   AGP 9.2.1 / Gradle 9.4.1 / JDK 17 / Chaquopy 17.0.0 are explicit repository inputs.

## State ownership graph

```text
content/*.json
    -> textrpg.content
        -> GameState + RulesEngine
            -> choice/simulation/quest/power/equipment/social systems
                -> player-safe scene/status projections
                    -> android_bridge.py
                        -> MainActivity presentation

MainActivity choice tap
    -> android_bridge.AndroidGameSession.choose_json()
        -> RulesEngine.choose()
            -> GameState mutation
                -> player-safe projection
                -> dumps_state()
                    -> Android AtomicFile save
```

The Java activity never computes rule outcomes.

## Failure containment

- Missing/malformed content: visible startup diagnostic.
- Unsupported/corrupt save: visible startup diagnostic; existing save is retained.
- Catchable Python/native startup failure: visible diagnostic + `TextRpgStartup` Logcat.
- Native/Python stdout and stderr: redirected to `native.stdout`, `native.stderr`,
  `python.stdout`, and `python.stderr` Logcat tags.
- Choice/rules failure: bridge restores the pre-choice deep-copied state before
  propagating the error; Java does not commit a new save.
- Save write failure: `AtomicFile.failWrite()` preserves the previous committed save.
- Activity recreation: the app reconstructs the session from the last committed save.

## Verification status

CONFIRMED from repository design/source:
- Existing engine exposes player-safe scene/status projections.
- Existing persistence contract is schema 1.
- Android bootstrap source and pinned wrapper are repository-owned on this working branch.
- Android imports the existing engine/content paths instead of maintaining copies.

NOT YET VERIFIED:
- Gradle configuration resolves successfully on a JDK 17 + Android SDK host.
- Debug APK assembles.
- Expected ABIs/assets are present in the APK.
- APK installs and launches on a representative device.
- Python 3.11 executes this exact engine on Android.
- First scene/choice/autosave/resume behave correctly on Android.
- Historical user-reported black screen is absent.

Therefore A-001 remains `IN_PROGRESS`, and A-002/A-003 remain incomplete.

## Next execution gate

From `android/`:

```bash
./gradlew :app:assembleDebug
```

Then inspect/install the APK and capture:

```bash
adb logcat -d -s TextRpgStartup python.stdout python.stderr native.stdout native.stderr AndroidRuntime
```

Any build/runtime defect should be repaired on this branch with the smallest focused
change, followed by another build/install/log capture. Do not promote the branch based
only on source inspection.
