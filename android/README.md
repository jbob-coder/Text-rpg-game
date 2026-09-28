# THE GAME — Android P0 bootstrap

This directory is the repository-owned replacement path for the lost/ephemeral Android
wrapper which previously produced a user-reported black screen.

It is a diagnostic vertical slice, not the final pixel-art client.

## Architecture

```text
Android Activity
  -> android_bridge.py
  -> existing textrpg content/rules engine
  -> build_scene_view() + build_status_view()
  -> Android presentation
```

The Android layer sends intent. It does not calculate stats, ability results, quest
state, requirements, or authored outcomes.

The build consumes the existing repository directly:

- Python engine source: `../src/textrpg`
- Authored content assets: `../content`
- Android-only bridge: `app/src/main/python/android_bridge.py`

No copied second engine or copied second content pack is maintained.

## Pinned build contract

- Android Gradle Plugin: 9.2.1
- Gradle: 9.4.1
- JDK: 17
- Chaquopy: 17.0.0
- Embedded Python: 3.11
- minSdk: 24
- compileSdk / targetSdk: 36
- ABIs: `armeabi-v7a`, `arm64-v8a`, `x86_64`

Python 3.11 is intentional: Chaquopy 17 supports both 32-bit and 64-bit ABIs through
Python 3.11. Keeping `armeabi-v7a` protects the bootstrap from failing on Android
devices with a 32-bit userspace.

The project does not use pip requirements or static proxies, and Chaquopy bytecode
compilation is disabled for source, pip, and stdlib in this diagnostic build. This
avoids making a matching host Python installation part of the bootstrap contract,
keeps the build close to the repository's standard-library-only engine, and preserves
readable Python tracebacks. The tradeoff is a larger/slower debug package.

## Build

Prerequisites:

1. JDK 17.
2. Android SDK Platform 36 and normal Android SDK build tools.
3. Network access for the first Gradle/plugin/Python-runtime dependency resolution.

From this directory:

```bash
./gradlew :app:assembleDebug
```

Windows:

```bat
gradlew.bat :app:assembleDebug
```

Expected debug artifact:

```text
app/build/outputs/apk/debug/app-debug.apk
```

A successful Gradle build is necessary evidence, but it is not proof that the black
screen is fixed.

## Device verification

Install and launch on the representative device/runtime:

```bash
adb install -r app/build/outputs/apk/debug/app-debug.apk
adb shell am force-stop com.jbobcoder.textrpg
adb shell am start -n com.jbobcoder.textrpg/.MainActivity
```

Capture startup evidence:

```bash
adb logcat -c
adb shell am force-stop com.jbobcoder.textrpg
adb shell am start -n com.jbobcoder.textrpg/.MainActivity
adb logcat -d -s TextRpgStartup python.stdout python.stderr native.stdout native.stderr AndroidRuntime
```

Acceptance checks for this P0 slice:

1. A visible "Starting local rules engine…" surface appears immediately.
2. The first authored scene renders; there is no silent blank/black screen.
3. Enabled choices can be selected and disabled choices cannot.
4. A choice changes the scene/state through the Python rules engine.
5. `save_v1.json` is committed to app-private storage after a successful choice.
6. Force-stop/relaunch resumes from that save.
7. A startup/runtime failure replaces the game view with a visible diagnostic and also
   appears under Logcat tag `TextRpgStartup`; native/Python stdout and stderr are also redirected to Logcat.
8. APK inspection confirms the expected native ABI libraries and authored content asset.

Do not mark TASK A-001/A-002/A-003 complete until the relevant build/device evidence
has actually been observed.

## Visual scope

The repository Visual Bible locks the shipped product to pixel style. This bootstrap
uses a deliberately simple crisp diagnostic shell so startup and engine integration can
be proven with low blast radius. It is not visual acceptance for U-001/P-001/M-002.
After the startup gate is green, the presentation layer can move to the full pixel
avatar/map/navigation design without changing the engine boundary.
