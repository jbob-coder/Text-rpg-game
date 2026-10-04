# THE GAME — Android Device, Performance & Compatibility Acceptance Standard

Status: **APPROVED FIRST-PASS V12 CONTRACT / GALAXY A02-CLASS PRODUCT TARGET / CURRENT PHYSICAL ACCEPTANCE UNVERIFIED**
Parents:
- docs/android/APK_REBUILD_AND_EVOLUTION_MASTER_PLAN.md
- docs/systems/CAMERA_AND_TACTICAL_PRESENTATION_STANDARD.md
Related:
- docs/android/ANDROID_CI_AUTOMATED_ACCEPTANCE_STANDARD.md

## 1. Purpose

Define how THE GAME proves compatibility and responsiveness on low-end Android hardware without confusing emulator success with physical-device acceptance.

## 2. Product target

Current design direction requires the game to be capable of shipping on Galaxy A02-class low-end Android hardware.

This is a design/acceptance target.

It is not a claim that the current app has been tested successfully on a Galaxy A02.

Historical Galaxy A03 references and Pixel 7 Pro emulator validation are separate evidence.

## 3. Compatibility dimensions

Device acceptance must record:
- exact device/model;
- Android version;
- CPU/ABI;
- RAM class;
- display resolution/density;
- available storage;
- build SHA/version;
- APK hash;
- install/update method.

## 4. Functional acceptance

On target/representative low-end physical hardware verify:
- install;
- first launch;
- restart;
- save/load;
- Story;
- Map/travel;
- Character/status;
- inventory/equipment;
- quests;
- activities used by Phase 1;
- tactical combat when implemented;
- settings/accessibility;
- interruption/resume policy.

## 5. Performance budgets

Exact numeric thresholds require measured prototypes.

Until then the design budget is:
- event-driven Python rules;
- bounded active actors;
- compact pixel assets;
- no mandatory continuous 3D physics;
- no whole-world art residency;
- bounded animation/effects;
- no per-frame AI/world simulation;
- limited recomposition scope.

Do not invent final FPS/memory targets without measurement.

## 6. Measurements to capture

For representative scenarios:
- cold-start time;
- warm-start time;
- input-to-visible-response latency;
- tactical action resolution latency;
- navigation transition latency;
- peak/steady memory;
- jank/frame timing where meaningful;
- battery/thermal behavior for sustained play;
- crash/ANR occurrence.

Record tool/method and scenario.

## 7. Memory pressure

Low-end fallback should prefer:
- unload noncurrent large scene assets;
- cache only bounded reusable assets;
- avoid duplicate decoded bitmaps;
- constrain simultaneous effects;
- preserve recoverable state before high-risk transitions.

## 8. Display/readability

Verify:
- portrait/landscape mode chosen by final UX;
- smallest supported width;
- touch targets;
- text scale;
- contrast;
- pixel-art scaling;
- no clipped critical actions.

Do not infer phone readability from desktop screenshots.

## 9. Compatibility versus quality tiers

A low-effects/reduced-motion path may reduce nonessential presentation.

It must not:
- change authoritative rules;
- hide necessary state;
- create competitive/gameplay differences;
- disable accessibility essentials.

## 10. Physical evidence

A physical-device acceptance packet should include:
- device facts;
- source HEAD;
- APK hash;
- steps;
- result;
- screenshots/photos when useful;
- measured numbers;
- failures/known limitations.

Manual observation must be labeled manual.

## 11. Update compatibility

If testing an update over an installed prior version:
- signing identity must match;
- applicationId must match;
- versionCode must advance;
- save migration must be tested.

If any condition fails, the result is reinstall behavior, not in-place update proof.

## 12. Acceptance levels

A. Emulator functional evidence.
B. Representative modern physical device.
C. Low-end representative physical device.
D. Named target-class device acceptance.

Do not collapse these into one “Android tested” label.

## 13. Current status

Confirmed historical:
- representative emulator runtime exists for a prior exact SHA.

Unverified in this documentation session:
- current-head APK build;
- Galaxy A02 physical install/runtime;
- Galaxy A03 physical acceptance;
- final low-end performance.

Those remain future evidence gates.
