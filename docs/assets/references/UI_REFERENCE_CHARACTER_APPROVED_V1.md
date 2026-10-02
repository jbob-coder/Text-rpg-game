# Reference Audit — UI_REFERENCE_CHARACTER_APPROVED_V1

Status: `REFERENCE_SELECTED / CHARACTER_TAB_APPROVED`  
Scope: Jack Wilson Character-tab visual reference for the Text-rpg-game pixel-art stack  
Production use: reference only; do not package this full-size source image in the APK

## Persisted reference

- Google Drive file: `UI_REFERENCE_CHARACTER_APPROVED_V1.jpeg`
- Drive file ID: `1OrLsw_mvbZ5HipFObfX8wdvA7vAPa-Ve`
- Drive folder: `Text-rpg-game Asset References`
- Source: user-provided approved character reference supplied in the project conversation on 2026-10-01
- Source resolution: 1536 x 1024 RGB JPEG
- SHA-256: `af453993693ff0447da3a1bf07e0276013f0c87f6a69442f86c5f3192487d867`

## Approved observations

This reference is authoritative for the intended visual presentation of Jack Wilson on the Character surface and for future character-art alignment:

- recognizable Jack Wilson identity rather than a permanently generic player silhouette;
- human-readable, non-chibi proportions;
- detailed dark pixel-art treatment with layered clothing and equipment;
- clear hair/face silhouette;
- jacket/chest layer, gloves, trousers and boots reading as separate material/equipment regions;
- equipment presented as authored visual assets rather than generic geometric placeholders;
- consistent character identity when reused at smaller UI scales.

## Boundaries

The reference does **not** independently define:

- authoritative gameplay stats or numeric values visible in the mockup;
- inventory ownership, equipment legality or equip/unequip rules;
- hidden story state;
- collision/hitbox geometry;
- the exact 32x48 technical rig anchors;
- six-view turnaround geometry that is not visible in this single reference;
- animation timing or frame counts.

Those remain controlled by repository data, manifests, blueprints and player-safe projected state.

## Relationship to existing player pipeline

The existing 32x48 paper-doll architecture remains valid. This reference changes the visual target: future player/Character artwork should be aligned to Jack's approved identity rather than refined from memory or treated as an unbounded generic style exercise.

The reference is not itself a runtime sprite. Native pixel masters and paper-doll layers must still be reconstructed, integrated and verified through the existing asset pipeline.

## Related records

- `docs/assets/REFERENCE_REGISTRY.md`
- `docs/assets/CHARACTER_PIXEL_BLUEPRINTS.md`
- `docs/assets/production_packets/BATCH_001_WAVE_A_BLUEPRINTS.md`
- `docs/assets/manifests/BATCH_001_WAVE_A.json`
- PR #22: `feature/player-avatar-art-pass`


## Branch reconciliation note

This reference record originated on `feature/player-avatar-art-pass` / PR #22 and is copied into the master documentation branch so later documentation cannot regress to the older generic-player assumption merely because of stacked-branch ancestry. This documentation reconciliation does not merge PR #22 runtime code or declare its player raster final.
