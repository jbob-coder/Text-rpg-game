# THE GAME — Android Build & Configuration Reconstruction Standard

Status: **APPROVED FIRST-PASS V12 CONTRACT / CURRENT CONFIGURATION RECORDED**
Parents:
- docs/android/APK_REBUILD_AND_EVOLUTION_MASTER_PLAN.md
Current source:
- android/app/build.gradle.kts
- android/build.gradle.kts
- android/settings.gradle.kts
- android/gradle.properties
- android/app/src/main/AndroidManifest.xml

## 1. Purpose

Record the current Android build contract and define what must be preserved, intentionally migrated, or reverified during final APK reconstruction.

## 2. Current configuration snapshot

At the documentation branch state inspected on 2026-10-04:

Application:
- namespace: com.thegame.rpg
- applicationId: com.thegame.rpg
- minSdk: 24
- targetSdk: 37
- compileSdk: Android 37 release API
- versionCode: 1
- versionName: 0.1.0-pixel-client-v1

Runtime/toolchain declarations:
- Java source/target: 17
- Chaquopy Python: 3.10
- Android Gradle Plugin: 9.2.0
- Kotlin Compose plugin: 2.2.10
- Chaquopy Gradle plugin: 17.0.0

Native ABI filters:
- armeabi-v7a
- arm64-v8a
- x86_64

Current Compose dependencies include:
- Compose BOM 2026.09.00
- Activity Compose/KT extensions 1.13.0
- lifecycle-viewmodel-ktx 2.11.0
- Material3
- UI tooling/test dependencies.

These are current source facts, not permanent final-version mandates.

## 3. Current packaging

Android main source packages:
- content from ../../content into app assets;
- Python source from ../../src through Chaquopy.

A build must verify that required authored content is actually embedded.

## 4. Current project configuration

settings.gradle.kts:
- google();
- mavenCentral();
- gradlePluginPortal() for plugin management;
- FAIL_ON_PROJECT_REPOS;
- module :app.

gradle.properties currently includes:
- 2 GiB Gradle JVM max heap;
- UTF-8;
- AndroidX;
- non-transitive R;
- built-in Kotlin.

## 5. Manifest snapshot

Current manifest:
- queries Android TTS service intent;
- application label THE GAME;
- allowBackup=true;
- supportsRtl=true;
- DeviceDefault.NoActionBar theme;
- MainActivity exported launcher.

Final reconstruction must explicitly review backup/data behavior and theme/presentation rather than inheriting them accidentally.

## 6. Signing status

No explicit release signingConfig is present in the inspected app build file.

Therefore:
- current repository source does not establish final production signing;
- debug/repository CI build evidence is not an update-signing guarantee;
- signing keys/secrets must never be committed into documentation or repository source.

Final release signing strategy requires a separate secure configuration decision.

## 7. Versioning

Before distributable releases:
- versionCode must monotonically increase for Android update compatibility;
- versionName should map to the release scheme;
- artifact provenance must record both.

Do not change applicationId if in-place update continuity is desired unless migration/reinstallation consequences are explicitly accepted.

## 8. Toolchain migration rule

When updating AGP/Kotlin/Compose/Chaquopy/Gradle:
1. record old versions;
2. record reason;
3. consult compatibility requirements;
4. change smallest coherent set;
5. run Python + Android unit + instrumentation/build;
6. inspect APK content/ABIs;
7. record exact HEAD/workflow/artifact.

Do not combine a major toolchain upgrade with unrelated UI reconstruction without need.

## 9. ABI policy

Current debug/build workflow expects:
- arm64-v8a;
- armeabi-v7a;
- x86_64.

Galaxy A02-class physical devices are expected to use ARM, but actual target-device ABI must be verified from device evidence before release claims.

Dropping an ABI is a compatibility decision requiring evidence.

## 10. Minimum Android version

minSdk 24 is the current source configuration.

Do not raise it merely for convenience without:
- target-device check;
- feature dependency;
- owner-visible compatibility consequence.

## 11. Secrets

Never store:
- keystore passwords;
- signing keys;
- service credentials;
- API secrets
in tracked build files or documentation.

Use secure CI/local secret mechanisms.

## 12. Reproducibility

A release candidate record must include:
- Git SHA;
- build workflow/tool versions;
- variant;
- applicationId/version;
- included ABIs;
- APK SHA-256;
- content identity/version;
- test evidence.

## 13. Acceptance

This standard documents current configuration and migration rules.

It does not claim:
- release signing configured;
- Play Store readiness;
- current-head build success;
- Galaxy A02 physical verification.
