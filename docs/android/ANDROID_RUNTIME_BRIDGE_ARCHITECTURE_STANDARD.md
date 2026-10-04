# THE GAME — Android Runtime & Python Bridge Architecture Standard

Status: **APPROVED FIRST-PASS V12 CONTRACT / CURRENT FOUNDATION EXISTS / FINAL REBUILD NOT STARTED**
Parents:
- docs/android/APK_REBUILD_AND_EVOLUTION_MASTER_PLAN.md
- docs/android/APK_FINAL_RECONSTRUCTION_MATRIX.md
Related:
- docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md
- docs/systems/SAVE_AND_CONTENT_MIGRATION_MASTER_PLAN.md
Current implementation:
- Android Kotlin/Jetpack Compose client
- Chaquopy Python bridge
- authoritative Python gameplay engine

## 1. Purpose

Define the final reconstruction boundary between Android application/runtime concerns and the authoritative Python game domain.

This standard preserves the strongest current architecture while allowing later screen/navigation/rebuild work.

## 2. Current architecture

Current client is repository-owned Android code.

Current app stack includes:
- Kotlin;
- Jetpack Compose;
- Chaquopy;
- bundled Python engine from ../../src;
- bundled authored content from ../../content;
- Android ViewModel/application state;
- player-safe Python projection;
- Android mapper/DTO/Compose consumers.

Historical exact-SHA validation proves this architecture has launched and played on a representative emulator at a prior branch/SHA. That evidence does not prove current-head or Galaxy A02 compatibility.

## 3. Authority boundary

Required direction:

GameState / Python domain systems
-> player-safe projection
-> bridge serialization/mapping
-> ViewModel application state
-> Compose presentation.

Android must not become authoritative for:
- stats;
- inventory;
- equipment rules;
- quests;
- travel legality;
- combat legality;
- NPC hidden state;
- progression formulas;
- world state.

## 4. Runtime ownership

Python owns:
- durable gameplay state;
- deterministic rules;
- save/load;
- authored content validation;
- hidden-state redaction source;
- gameplay action validation.

Android owns:
- application lifecycle;
- boot/error presentation;
- navigation/presentation state;
- touch/gesture handling;
- local visual selection state;
- TTS/audio platform integration;
- accessibility;
- platform file/request mediation when required.

## 5. Bridge contract

Bridge APIs should:
- expose explicit typed actions;
- return detached player-safe projections;
- use stable public error codes;
- validate arguments before authoritative mutation;
- avoid generic raw-state setters;
- remain deterministic for same gameplay state/action.

Do not expose GameState.snapshot directly to Compose.

## 6. Content packaging

Current app source set packages:
- ../../content as Android assets;
- ../../src as Chaquopy Python source.

Final reconstruction must keep content/source packaging traceable to exact Git HEAD and build artifact.

If content becomes larger, packaging/loading may be reworked, but the authoritative content version must remain explicit.

## 7. Lifecycle

Android lifecycle events must not create gameplay mutations by themselves.

Required behavior:
- Activity recreation restores/presents current session safely;
- app interruption during an unsupported transient mode follows that subsystem's restart/checkpoint policy;
- save ownership stays in Python/persistence;
- presentation selection may be recreated independently when nonauthoritative.

## 8. Error model

Public runtime states:
- starting;
- ready;
- recoverable error;
- fatal/content incompatibility error where necessary.

Developer detail may include:
- exception class;
- technical message;
- source/version metadata.

Player-facing errors must not expose private state/secrets.

## 9. Dependency isolation

Compose should depend on stable mapped models/interfaces rather than:
- Python object internals;
- content JSON structure;
- filesystem paths;
- raw asset filenames when stable asset IDs exist.

This allows domain migration without rewriting every screen.

## 10. Future tactical mode

Phase 1 combat may add transient authoritative CombatSession state in Python while leaving durable GameState schema v1 unchanged.

Android consumes optional combat projection and explicit combat actions. It does not calculate pathing/LOS/damage.

## 11. Performance

Bridge calls should be:
- bounded;
- event-driven;
- off the critical render loop where expensive;
- free of continuous polling when state has not changed.

Avoid serializing the entire world for each UI recomposition.

## 12. Security/privacy

No raw:
- NPC private goals;
- hidden knowledge;
- secret world state;
- AI utility;
- unredacted authored conditions;
should cross the player-facing bridge.

## 13. Tests

Required reconstruction evidence:
- Python bridge boot;
- mapping valid projection;
- malformed projection rejection;
- action error mapping;
- save/load;
- activity recreation;
- hidden-state redaction;
- combat optional field when implemented;
- representative Android instrumentation.

## 14. Rebuild rule

KEEP the authoritative Python/player-safe projection architecture unless exact evidence proves it blocks final requirements.

Screen rewrites do not justify moving gameplay authority into Kotlin.
