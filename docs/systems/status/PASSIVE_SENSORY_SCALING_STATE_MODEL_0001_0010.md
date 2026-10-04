# THE GAME — Sensory Passive Scaling & State Model 0001–0010

Status: **PHASE-C CALIBRATION / TARGET DESIGN / NOT IMPLEMENTED**

Parents:
- `PASSIVE_REGISTRY_SCHEMA.md`
- `PASSIVE_REQUIREMENT_LANGUAGE.md`
- `calibration/PASSIVE_DETAIL_SENSORY_0001_0010.md`

Purpose: define bounded sensory scaling, error handling, authoritative state categories, and test expectations for Sensory 0001–0010.

## Global sensory state model

Future implementation should separate:
- `qualification_state` — hidden drill/field evidence;
- `ownership_state` — acquired/revealed passive;
- `signal_state` — what sensory information physically exists and is available;
- `interpretation_state` — confidence/discrimination/tracking result;
- `truth_state` — objective world truth, never replaced by passive confidence;
- `sensory_context` — lighting, noise, occlusion, contact, contamination, range, injury/equipment;
- `projection_state` — player-safe result.

Rules:
1. a passive cannot create a signal where none exists unless explicitly defined;
2. interpretation bonuses never rewrite objective truth;
3. false positives/uncertainty remain possible;
4. duplicate ownership does not stack;
5. ability-assisted input requires source compatibility;
6. exact numeric coefficients remain `TBD`.

## SEN_0001 — Low-Light Acuity
Effect input: visual discrimination threshold in low but nonzero visible light.
Cap: total darkness remains unreadable without another source.
Tests: low light improves; total darkness does not; glare/injury still matter.

## SEN_0002 — Motion Focus
Effect input: tracking continuity for one already visible moving target.
Cap: no hidden-target revelation and limited target count.
Tests: clutter benefit; occlusion still breaks/weakens track; multiple-target overload persists.

## SEN_0003 — Peripheral Discipline
Effect input: peripheral movement notice/attention-shift resolver.
Cap: actual visual field and occlusion remain.
Tests: peripheral cue improvement; behind-character/no-vision cue not granted; false motion possible.

## SEN_0004 — Sound Separation
Effect input: source-separation confidence among audible overlapping sounds.
Cap: no raw hearing-range increase.
Tests: mixed audible sources improve; inaudible source remains absent; barriers/acoustics still matter.

## SEN_0005 — Scent Memory
Effect input: match confidence between current odor and learned odor reference.
Cap: unknown/contaminated odors remain uncertain.
Tests: learned odor recognized better; novel odor not named automatically; contamination reduces confidence.

## SEN_0006 — Thermal Discrimination
Effect input: interpretation precision of an available thermal cue.
Cap: no thermal signal generation.
Tests: ordinary/ability-assisted compatible source improves; no source means no reading; heat resistance unchanged.

## SEN_0007 — Vibration Sense
Effect input: contact-vibration detection/interpretation.
Cap: physical contact and propagation required.
Tests: contacted surface works; no contact gives none; damping reduces signal; source identity remains uncertain.

## SEN_0008 — Range Estimation
Effect input: distance-estimate error band.
Cap: not exact instrumentation.
Tests: trained visual range improves; poor visibility worsens estimate; instrument remains more precise where designed.

## SEN_0009 — Threat Localization
Effect input: time/confidence to localize direction after a cue is already detected.
Cap: does not create cue or prove hostility.
Tests: detected cue localizes faster; no cue gives nothing; decoy cue can mislead.

## SEN_0010 — Detail Retention
Effect input: short-term retention decay of already perceived physical details.
Cap: no permanent perfect memory and no correction of misperception.
Tests: observed detail retained longer; unseen detail absent; incorrect observation can remain incorrect.

# Cross-passive composition

High-risk overlaps:
- Motion Focus + Peripheral Discipline;
- Sound Separation + Threat Localization;
- Low-Light Acuity + equipment-based enhancement;
- Thermal Discrimination + Thermal Sight;
- Range Estimation + ranged equipment;
- Detail Retention + future cognitive memory passives.

Default rule:
Signal generation, interpretation, confidence, and memory are separate stages. Passives should modify only their documented stage.

# Hidden qualification lifecycle

Before qualification:
- drill/confirmation counters may exist internally;
- normal Status projection exposes no name, slot, exact threshold, or progress percentage.

On qualification:
1. validate meaningful evidence;
2. require false-positive/error review where specified;
3. create ownership once;
4. reveal player-safe effect;
5. keep institutional/public knowledge separate.

# Implementation gate

Before runtime work:
- define sensory pipeline stages;
- define objective truth versus perceived result;
- define confidence/error representation;
- map each passive to an authoritative resolver;
- add save/migration behavior;
- add hidden-progress filtering;
- add false-positive and spoofing tests;
- add equipment/ability-assisted integration tests.

No runtime file/module is claimed here.
