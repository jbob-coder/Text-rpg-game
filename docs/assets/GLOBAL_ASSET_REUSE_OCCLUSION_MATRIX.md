# Global Asset Reuse and Occlusion Matrix

Status: **ACTIVE OPERATIONAL CHILD / VISUAL CONTRACT**  
Parents:
- `docs/assets/PIXEL_ART_RUNTIME_COMPOSITION_STANDARD.md`
- `docs/assets/ROOM_ACTOR_PANEL_OVERLAY_REUSE_STANDARD.md`

This child operationalizes reuse decisions. Parent documents remain authoritative when wording conflicts.

## 1. Reuse dimensions

Evaluate every candidate against:
native grid; perspective/camera; world scale; anchor/pivot; z-order; occlusion; light direction; palette/value family; material/body-surface family; semantic identity; state ownership; animation timing; target-screen readability; accessibility meaning.

## 2. Reuse classes

- **R0 DIRECT** — relevant dimensions match; reuse unchanged.
- **R1 PLACEMENT** — art unchanged; placement/anchor/z-order metadata differs.
- **R2 VARIANT** — identity is unchanged but lighting/palette/state requires an approved authored variant.
- **R3 OVERLAY** — temporary state layers over a compatible base.
- **R4 FAMILY DERIVATIVE** — design language is shared but a new asset is required.
- **R5 FORBIDDEN** — reuse would misrepresent identity, perspective, state, anatomy, or meaning.

R5 examples include named identity-bearing accessories used generically, species anatomy reused for another species, map sprites used as portraits, or locked-door visuals when authoritative state says open.

## 3. Default environment occlusion order

1. distant/background environment;
2. terrain/floor;
3. permanent architecture;
4. rear permanent props;
5. rear state overlays;
6. rear actors/entities;
7. main actors/entities;
8. foreground props/architecture;
9. status/injury overlays;
10. ability/environment FX;
11. interaction markers;
12. contextual UI.

Scene perspective may override the numerical order, but never in a way that falsifies state.

## 4. Character/equipment

Use the existing 32x48 rig and parent z-order contract.

An equipped item without authored geometry:
- remains equipped logically;
- receives no invented body geometry;
- may use truthful icon/text feedback;
- is recorded as missing visual production.

## 5. Beast layering

Beast visuals may use:
ground shadow -> base body -> rear appendages -> authored surface/armor/fur variants -> tagged/equipped elements if the setting supports them -> injury -> status -> ability/FX -> foreground occlusion.

Do not force species-specific anatomy into a universal human paper-doll model.

## 6. Hard compatibility boundaries

Direct reuse is rejected when perspective, identity, scale, anatomy, state meaning, or material/light direction materially conflicts.

Arbitrary runtime tinting does not repair an incompatible source.

Do not directly reuse across map/scene, portrait/gameplay, top-down/front-side, or UI-icon/world-object contexts unless the asset was explicitly designed as a multi-context master.

## 7. Temporary-state rule

Permanent base art does not encode temporary state by default.

Blackout, alarm, injury, quest markers, active Trace, current/reachable map status and temporary damage should use overlays/variants where the physical identity remains unchanged.

## 8. Map composition

Neutral geography/architecture belongs to the base. Player position, current node, reachable/unavailable, quest/event, danger, route preview and temporary world state belong to overlays.

A drawn line must never imply traversability when route state denies it.

## 9. Reuse record

Record:
asset ID; family; native size; perspective; anchors; allowed contexts; allowed transforms; required variants; forbidden contexts; state owner; known consumers; lifecycle stage; provenance.

## 10. Acceptance

Approve reuse only when identity, perspective, scale, anchor/occlusion, lighting/material compatibility, state meaning, mobile readability and player-safe semantics all remain correct.

A missing unique asset must not be disguised as “reuse.”
