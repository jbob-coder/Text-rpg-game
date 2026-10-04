# THE GAME — Android CI & Automated Acceptance Standard

Status: **APPROVED FIRST-PASS V12 CONTRACT / CURRENT WORKFLOWS EXIST**
Parents:
- docs/android/APK_REBUILD_AND_EVOLUTION_MASTER_PLAN.md
- docs/android/ANDROID_BUILD_CONFIGURATION_RECONSTRUCTION_STANDARD.md
Current workflows:
- .github/workflows/android-pixel-client.yml
- .github/workflows/android-apk-artifact.yml

## 1. Purpose

Define the automated evidence required before an Android implementation or APK candidate can be called verified.

A successful compile alone is not sufficient.

## 2. Current workflow evidence

android-pixel-client.yml currently contains jobs for:
- complete Python unittest discovery;
- Android debug unit tests;
- instrumentation-test compilation;
- debug APK assembly;
- APK payload/hash checks;
- representative emulator instrumentation under qualifying triggers;
- screenshot-set verification.

Its emulator configuration uses:
- API 35;
- x86_64;
- Pixel 7 Pro profile;
- software-rendered/headless settings.

android-apk-artifact.yml is a historical/integration packaging workflow tied to an exact verified parent and integration branch.

Do not generalize either workflow's old result to current HEAD.

## 3. Required current-head CI layers

For final reconstruction, automated acceptance should separate:

A. Python domain
- full test suite;
- content/schema validation;
- save migration tests.

B. Android JVM
- mapper/DTO tests;
- ViewModel/action delegation;
- navigation/presentation state where practical.

C. Android build
- debug/release-candidate variant as applicable;
- packaged Python/content presence;
- expected ABIs;
- artifact hash.

D. Instrumentation/emulator
- real MainActivity boot;
- bridge initialization;
- core screen flow;
- save/load;
- relevant gameplay mode;
- screenshots/semantics where useful.

E. Static/repository checks
- no missing assets/content;
- no forbidden secret files;
- exact version/provenance output.

## 4. Trigger policy

CI should run enough validation on pull requests to prevent integration regressions.

Expensive emulator/device-style jobs may use controlled triggers when cost/runtime is significant, but a release candidate requires them explicitly.

No release claim should depend on a job that did not run.

## 5. Artifact verification

For each APK artifact:
- file exists;
- SHA-256 recorded;
- expected ABI libraries present;
- required content present;
- source HEAD recorded;
- build variant recorded.

Artifact name should include enough source identity to prevent confusion.

## 6. Exact-head rule

Tests from parent/previous SHA are historical evidence.

A candidate is verified only for the exact source that produced it, unless a separate reproducibility proof demonstrates runtime sources are byte-for-byte unchanged and records that relationship.

## 7. Failure policy

Any failed required gate blocks the corresponding claim.

Do not:
- ignore a failing test because app launches;
- call instrumentation passing if only assembly ran;
- call device compatibility verified from an emulator;
- call APK delivered if only a hash exists.

## 8. Screenshot evidence

Screenshot tests/evidence should verify:
- real nonempty PNG;
- expected test surface;
- no black screen;
- essential layout states;
- source/run linkage.

Screenshots supplement assertions; they do not replace state/rule tests.

## 9. Determinism

Gameplay tests should use deterministic seeds/state where relevant.

Flaky nondeterministic tests are defects, not acceptable release noise.

## 10. Retention and evidence

Short-lived CI artifact retention is acceptable for routine runs if:
- durable repository evidence records hash/run/source for important checkpoints;
- release artifacts use an intentional delivery/archive process.

## 11. Release-candidate gate

Before calling an APK release candidate:
- required Python tests green;
- Android unit tests green;
- build green;
- instrumentation green;
- content/ABI/hash checks green;
- migration tests green when schema changed;
- performance/device gates handled separately;
- known limitations recorded.

## 12. Current limitations

This documentation does not execute current workflows.

Historical validation remains bounded to its recorded branch/SHA/run.
