# Global Asset Reuse and Occlusion Matrix

Status: **REVIEWABLE / GLOBAL VISUAL CONTRACT**
Domain: Pixel Art / Assets / UI

## Purpose

Define when an existing pixel asset may be reused, overlaid, recolored, repositioned, or rejected so that reused assets do not look misplaced or contradict world state.

## Reuse dimensions

Every candidate reuse must be evaluated against:

1. native grid;
2. perspective/camera;
3. world scale;
4. anchor/pivot;
5. z-order;
6. occlusion;
7. light direction;
8. palette/value family;
9. material/body-surface family;
10. semantic identity;
11. state ownership;
12. animation timing if animated;
13. target screen/readability;
14. accessibility meaning if used as UI feedback.

## Decision classes

### R0 — Direct reuse
All relevant dimensions match.

Examples:
- same municipal lamp in two compatible civic scenes;
- same generic panel chrome in multiple UI screens.

### R1 — Reuse with placement metadata
Art is unchanged; anchor/z-order/location differs.

Examples:
- pipe support placed at different corridor positions.

### R2 — Reuse with approved visual variant
Identity remains the same but lighting/palette/state requires a dedicated variant.

Examples:
- same door under normal versus emergency lighting.

### R3 — Reuse as overlay
Asset represents temporary state and can layer over compatible base art.

Examples:
- injury overlay;
- blackout shadow;
- Trace FX;
- quest marker.

### R4 — Derivative family asset
Shares design language but requires a newly authored asset.

Examples:
- second workshop window size;
- another beast species using the same icon language but unique anatomy.

### R5 — Forbidden reuse
Reusing the asset would misrepresent identity, perspective, state, or meaning.

Examples:
- one named NPC's identity-bearing accessory used generically;
- one beast species' anatomy used for another species;
- top-down map sprite used as a dialogue portrait;
- locked-door art shown when gameplay says open.

## Occlusion order — environment scene

Default order:

1. distant/background environment
2. terrain/floor
3. permanent architecture
4. rear permanent props
5. rear state overlays
6. rear actors/entities
7. main actors/entities
8. foreground props/architecture
9. status/injury overlays
10. ability/environment FX
11. interaction markers
12. contextual UI

Exact order can change per scene when perspective requires it, but semantic state may not be hidden incorrectly.

## Character paper-doll

Use the existing project rig/z-order contract.

Equipment logic remains authoritative in gameplay state.

An unmapped equipped item:
- remains equipped logically;
- does not receive invented visual geometry;
- may show icon/text feedback;
- is recorded as missing visual production work.

## Beast visual layering

Potential layers:
- ground shadow;
- base body;
- rear appendages;
- armor/scales/fur variants where authored;
- equipment/tagging if the setting supports it;
- injury;
- status;
- ability/FX;
- foreground occlusion.

Species-specific anatomy must not be flattened into a universal paper-doll assumption unless the future beast rig architecture explicitly supports it.

## Lighting compatibility

Direct reuse requires compatible dominant lighting.

If lighting conflicts:
- create approved variant;
- use controlled palette transformation only if the asset contract permits;
- otherwise author a new family asset.

Do not rely on arbitrary runtime tinting to repair identity/material conflicts.

## Perspective compatibility

Perspective is a hard boundary.

Do not directly reuse across:
- map vs scene;
- portrait vs gameplay sprite;
- top-down vs side/front;
- UI icon vs world object

unless the asset was explicitly designed as a multi-context master.

## State compatibility

Permanent base assets must not encode temporary state by default.

Temporary state examples:
- blackout;
- alarm;
- injury;
- quest indicator;
- active Trace;
- current/reachable map status;
- temporary damage.

Use overlays/variants when the underlying identity remains the same.

## Text-art compatibility

Text-art or ASCII-like decorative assets may be reused only if:
- font/grid assumptions match;
- aspect ratio remains stable;
- screen scale remains readable;
- they do not become hidden gameplay information;
- they do not conflict with pixel-art silhouette/perspective.

Text-art is presentation, never gameplay authority.

## Map assets

Map base:
- neutral geography/architecture.

Map overlays:
- player position;
- current node;
- reachable;
- unavailable;
- quest/event;
- danger;
- route preview;
- temporary world-state changes.

Map art must never make an unavailable route look traversable solely because a line exists.

## Asset reuse record

For reusable production assets, record:
- asset ID;
- family;
- source/native size;
- perspective;
- anchors;
- allowed contexts;
- allowed transforms;
- required variants;
- forbidden contexts;
- state owner;
- known consumers;
- lifecycle status.

## Acceptance checklist

Reuse is approved when:
- [ ] identity remains correct;
- [ ] perspective matches;
- [ ] scale matches;
- [ ] anchor/occlusion is defined;
- [ ] light/material compatibility is acceptable;
- [ ] state meaning is correct;
- [ ] mobile readability is preserved;
- [ ] no hidden gameplay state is invented;
- [ ] a missing unique asset is not being disguised through incorrect reuse.
