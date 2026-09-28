# Dedicated Reference Brief — PLAYER_BODYFRAME_A_TURNAROUND

Asset: `001 PLAYER_BODYFRAME_A_TURNAROUND`  
Target state after acceptable generation: `REFERENCE_SELECTED`

## Purpose

Generate a neutral six-view anatomy/construction reference that exists only to reconstruct the reusable 32x48 player paper-doll base.

This is **not** a player character design.

## Required board

- minimum board size: 1536x1024;
- six equal-height figures;
- flat dark-neutral or medium-neutral background;
- orthographic turnaround presentation;
- views in this exact order:
  1. front;
  2. front three-quarter;
  3. left profile;
  4. right profile;
  5. rear three-quarter;
  6. back;
- equal ground line;
- equal apparent height;
- neutral standing pose;
- arms relaxed enough to expose torso/hip construction;
- hands visible;
- feet fully visible;
- no cropping.

## Subject

A neutral adult human construction model intended for a 32x48 pixel-art RPG sprite.

The subject must be intentionally non-specific:

- no canonical face;
- no distinctive hairstyle;
- no facial hair;
- no scars;
- no tattoos;
- no jewelry;
- no role insignia;
- no faction symbols;
- no weapon;
- no bag;
- no armor;
- no jacket;
- no shoes with distinctive design;
- no story identity.

Use a close-fitting, plain, non-branded underlayer only to clarify anatomy.

The head should be bald or featureless enough that no hairstyle identity is introduced. Facial features should be minimal construction marks only; no distinctive eyes, brows, nose, mouth, facial hair, or expression design.

## Proportion locks

The generated reference must be compatible with the following 32x48 reconstruction envelope:

- occupied height target: 44 px;
- top margin target: 2 px;
- ground pivot: `(16,47)`;
- head center: `(16,8)`;
- head target height: roughly 10–11 px;
- adult readable ratio near 1 head : 4 total body height at gameplay scale;
- shoulder span target: x=8..24 around y=15;
- pelvis center: `(16,28)`;
- left knee: `(12,37)`;
- right knee: `(20,37)`;
- left foot anchor: `(11,46)`;
- right foot anchor: `(21,46)`;
- main-hand attachment: `(27,31)`;
- off-hand attachment: `(5,31)`.

The reference may suggest subtle anatomy but cannot move the anchor architecture.

## Desired pixel-art language

- modern detailed retro pixel art;
- deliberate pixel clusters;
- crisp hard edges;
- no painterly smoothing;
- no anti-aliased silhouette dependence;
- no soft photographic gradients;
- body planes readable through 4–7 value/color groups;
- enough detail to understand knees, elbows, hands and feet, but not so much that the design depends on subpixel detail.

## Lighting

- neutral frontal/upper-front light;
- low drama;
- same light on all six views;
- no colored rim light;
- no Trace/ability glow;
- no environment reflection.

## What generation may solve

- shoulder-to-neck transition;
- elbow volume;
- forearm taper;
- hip/upper-leg transition;
- knee volume;
- calf taper;
- simple hand silhouette;
- simple foot silhouette;
- chest/back depth in profile.

## What generation may not solve

- permanent player identity;
- hair;
- skin-tone canon;
- outfit;
- equipment;
- class/job;
- role;
- background;
- personality;
- story affiliation.

## Rejection conditions

Reject the reference if:

- one view is taller/shorter than the others;
- the body changes build between views;
- perspective foreshortening is visible;
- hands/feet change size materially;
- the front/back do not share shoulder/hip width;
- the subject becomes chibi;
- the subject becomes highly muscular/stylized;
- the face becomes a distinctive canonical-looking identity;
- clothing hides the body structure;
- any view is cropped;
- generated text or labels overlap the subject;
- the design relies on anti-aliasing or smooth painting that cannot survive 32x48 reconstruction.

## Selection output

When a candidate is accepted, record:

- reference ID;
- Drive file ID;
- SHA-256;
- six-view consistency notes;
- any deviations that must be corrected during reconstruction;
- whether each anchor/proportion requirement can be satisfied.

Only then advance asset 001 to `REFERENCE_SELECTED`.

## Prompt-ready generation specification

Create a six-view orthographic character turnaround reference for a 32x48 pixel-art RPG paper-doll base. Show one neutral adult human construction model in front, front three-quarter, left profile, right profile, rear three-quarter, and back views, all equal height on one ground line. Use modern detailed retro pixel art with crisp deliberate pixel clusters, no anti-aliasing, no painterly rendering, neutral lighting, flat unobtrusive background, plain close-fitting non-branded underlayer, relaxed neutral stance, visible hands and feet. Maintain identical anatomy/proportions across all six views. The figure should read as an adult human at roughly one head to four total body heights when reduced to gameplay scale. No hair identity, no distinctive face, no scars, tattoos, jewelry, bags, armor, weapons, faction symbols, role markers, ability effects, environment, or story details. This image is a technical reconstruction reference only, not final game art.
