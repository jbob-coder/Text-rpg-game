# THE GAME — Android Release Provenance, Signing & Rollback Standard

Status: **APPROVED FIRST-PASS V12 CONTRACT / RELEASE EXECUTION NOT STARTED**
Parents:
- docs/android/APK_REBUILD_AND_EVOLUTION_MASTER_PLAN.md
- docs/android/APK_FINAL_RECONSTRUCTION_MATRIX.md
- docs/android/ANDROID_BUILD_CONFIGURATION_RECONSTRUCTION_STANDARD.md
- docs/android/ANDROID_CI_AUTOMATED_ACCEPTANCE_STANDARD.md

## 1. Purpose

Define how an Android APK/release candidate is tied back to exact source, build configuration, test evidence, signing identity, content, and recovery/rollback information.

A downloadable APK without provenance is not sufficient release evidence.

## 2. Release identity

Each candidate should record:
- release/candidate ID;
- Git repository;
- branch/ref;
- exact commit SHA;
- versionCode;
- versionName;
- applicationId;
- build variant;
- build workflow/run;
- artifact ID/name;
- APK SHA-256;
- included ABIs;
- content ID/version;
- save schema version;
- signing identity fingerprint where safe to disclose;
- test/acceptance packet references;
- known limitations.

## 3. Signing boundary

Current inspected Gradle source does not define a production release signingConfig.

Therefore final signing remains unresolved.

Rules:
- never commit private signing keys;
- never commit keystore passwords;
- never place credentials in docs;
- signing identity continuity is required for in-place Android updates;
- record only safe public fingerprints/metadata necessary to prove continuity.

## 4. Debug versus release

A debug APK can prove:
- build;
- packaging;
- runtime/test behavior for that variant.

It does not by itself prove:
- production signing;
- store readiness;
- update continuity from a future release key;
- final optimization/permission behavior.

Every evidence packet must state the variant.

## 5. In-place update continuity

For update-over-existing-install behavior:
- applicationId must remain compatible;
- signing identity must match;
- versionCode must increase;
- save migration must support the installed state;
- package install/update must be tested.

Changing any of these may convert an update into reinstall/migration work.

## 6. Artifact integrity

At minimum:
- compute SHA-256 after build;
- record exact file size;
- inspect archive for required native ABI entries and content;
- do not rename/repackage the APK after hashing without creating a new hash record.

If an artifact is copied to another storage provider, verify its hash after transfer when practical.

## 7. Source provenance

Preferred provenance chain:

repository HEAD
-> CI/local build configuration
-> test results
-> APK artifact
-> SHA-256
-> installation/device evidence.

If an artifact is built from a commit whose runtime source is proven identical to a previously verified commit, record that relationship explicitly. Do not assume it.

## 8. Content provenance

APK evidence should record:
- bundled content pack ID;
- canon/provisional status when relevant;
- schema version;
- required asset/manifest version or commit.

A UI build with stale content must not be mislabeled as the current game.

## 9. Save compatibility

Before release:
- identify oldest supported save schema/version;
- run migration fixtures;
- test unsupported-version handling;
- preserve a rollback/recovery strategy.

If a release irreversibly migrates saves, backup/recovery consequences must be explicit before rollout.

## 10. Rollback model

Rollback can mean:
- source rollback;
- feature rollback;
- APK version rollback;
- save/content rollback.

They are not equivalent.

Android may reject installing an older versionCode as an ordinary update. A code rollback may therefore require a newly versioned APK containing reverted code rather than installing the old APK.

## 11. Feature migration rollback

For major subsystem replacements:
1. keep old path until replacement passes;
2. migrate consumers;
3. prove zero-consumer state;
4. remove/archive old path;
5. retain Git history and migration record.

This aligns with the final APK teardown rules.

## 12. Failed release recovery

A release packet should define:
- known safe prior source;
- whether save schema changed;
- whether data migration is reversible;
- whether a hotfix can preserve signing/applicationId;
- how to identify affected build by version/hash.

Do not promise rollback when save/data migration makes it impossible.

## 13. Distribution/storage

The repository may use CI artifacts or other owner-approved storage for delivery.

Whatever distribution path is used:
- artifact hash remains the identity check;
- source/build metadata remains attached;
- expiration of a CI artifact does not erase the release evidence record.

## 14. Permissions/privacy review

Before final release, record:
- manifest permissions/queries;
- backup policy;
- external data/storage behavior;
- narration/TTS platform integration;
- any network access if later introduced.

The current manifest queries TTS services and uses allowBackup=true; final policy requires explicit review rather than accidental inheritance.

## 15. Release checklist

Minimum:
- exact source HEAD captured;
- version fields correct;
- signing identity established;
- required tests green;
- APK built;
- APK hash/content verified;
- migration tests green if needed;
- device/performance gate completed at required acceptance level;
- accessibility/critical UX checked;
- known limitations written;
- rollback/recovery path written;
- artifact provenance persisted.

## 16. Current status

This document establishes the reconstruction/release evidence contract only.

Not claimed:
- production release signing exists;
- current-head APK built;
- final release candidate exists;
- Galaxy A02 acceptance exists;
- in-place update path has been proven.
