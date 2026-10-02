# Android Pixel Client Validation

> Current priority: `jbob-coder/Text-rpg-game`, [master documentation program](MASTER_GAME_DEVELOPMENT_PROGRAM.md) and [decision/rebuild execution register](DECISION_AND_REBUILD_EXECUTION_REGISTER.md). This report preserves its bounded historical/provisional scope; it is not the final world, current canonical branch, or final APK plan.

Validated: 2026-09-27 17:34 AST  
Repository: `jbob-coder/Text-rpg-game`  
Branch: `feature/android-pixel-client-v1`  
Exact source SHA: `510851cc165702fbe19ef005083a03cbcd00a9f3`  
Workflow: Android Pixel Client, run 65, run ID `36351957867`

## Result

The repository-owned Kotlin/Jetpack Compose + Chaquopy Android client passed the complete currently configured base-client validation gate.

This evidence applies only to the exact SHA above. Later commits require fresh evidence.

## Python engine

Command executed by workflow:

`PYTHONPATH=src python -m unittest discover -s tests -v`

Result:

- 290 tests run
- 290 passed
- 0 failures/errors reported
- workflow job: success

## Android build gates

The Android job succeeded at the exact source SHA:

- Android unit tests: success
- Compose instrumentation tests: compile success
- debug APK assembly: success
- APK structure verification: success
- bundled Python content check: success
- expected native ABI entries present:
  - `arm64-v8a`
  - `armeabi-v7a`
  - `x86_64`

Exact debug APK SHA-256:

`94e325d55c5dd1404dbab8d0209dbfe1f8c0c29c5abecfdd582736851da4cd74`

The push workflow intentionally did not upload the APK artifact, so this hash is build evidence, not a claim that the artifact has already been delivered to the user.

## Representative Android runtime

Environment configured by workflow:

- Android emulator API 35
- x86_64
- Pixel 7 Pro profile

Connected instrumentation result:

- 3 tests started
- 3 tests finished
- 0 failures reported
- Gradle connected Android test build: SUCCESS

Verified runtime behaviors include:

1. real `MainActivity` starts;
2. Python engine initializes through Chaquopy;
3. visible pixel gameplay renders instead of a black screen;
4. player avatar and scene illustration render;
5. `TAKE_DEAD_RELAY` advances to the authored next scene;
6. narrative scroll resets correctly on scene change;
7. Save succeeds;
8. gameplay can advance after the save;
9. Load/Continue restores the saved scene and returns the player to gameplay.

## Black-screen incident disposition

The old NativeActivity/WebView test wrapper was ephemeral and its exact internal failure cannot be forensically recovered from authoritative repository source.

The product failure class is nevertheless resolved for the repository-owned replacement client at this exact SHA: representative Android runtime evidence shows visible startup and gameplay with no black-screen failure.

This does not claim that the exact historical wrapper crash mechanism was identified.

## Remaining release gates

Not proven by this evidence:

- physical handset installation on the user's phone;
- distributable APK delivery from this exact or later release candidate;
- in-place update continuity/signing strategy for future release APKs;
- later open-world candidate behavior;
- production polish/accessibility completeness.

The next runtime gate should cover the open-world integration candidate, including a real map travel transition into an authored narrative scene.
