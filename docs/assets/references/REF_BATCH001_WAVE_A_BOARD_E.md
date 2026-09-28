# Reference Audit — REF_BATCH001_WAVE_A_BOARD_E

Status: `REFERENCE_GENERATED`  
Selection result: **REJECTED for asset 001 and asset 018**  
Use: detail-language / presentation study only

## Persisted reference

- Google Drive file: `REF_BATCH001_WAVE_A_BOARD_E.png`
- Drive file ID: `10bXF6javjkOuuYXULhsFwSrsUvky3yLQ`
- Resolution: 1536 x 1024 PNG
- SHA-256: `93edd7ea8a62b4621b603c43ceebfdc2633b7da7028939e24880e4ba133671b0`
- File size: 2,421,682 bytes

## Asset 001 — PLAYER_BODYFRAME_A_TURNAROUND

Decision: **REJECT**

The player panel still depicts a specific protagonist-like identity rather than the locked neutral construction body:

- distinctive dark hairstyle;
- recognizable face/eyes;
- fixed shirt/shorts presentation;
- repeated animations tied to that invented identity.

Useful only for proportion/detail-density study. Asset 001 remains `BRIEF_LOCKED`.

## Asset 018 — NPC_TAMSIN_TURNAROUND

Decision: **REJECT**

Several details are directionally useful: slim athletic build, high collar, charcoal utility clothing, compact satchel, badge scale, dark work trousers, and overall 32x48 density.

However, the actual front-facing pixels still violate the locked anatomical-side contract:

- heavy fringe remains primarily on **viewer-left**;
- front-facing Tamsin's anatomical **left** is **viewer-right**;
- therefore the fringe is still on the wrong anatomical side.

The sleeve treatment also does not provide a clean enough one-sleeve contrast to prove that only Tamsin's anatomical right sleeve is rolled.

The anatomical-side labels printed on the sheet do not override contradictory rendered pixels.

Asset 018 remains `BRIEF_LOCKED`.

## Pipeline decision

Board E confirms that mixed atlas generation continues to override individual character constraints even when the sheet contains correct written labels.

Therefore:

- do not use Board E for canonical pixel reconstruction;
- do not advance either turnaround to `REFERENCE_SELECTED`;
- continue implementation using already blueprint-locked assets;
- canonical player/Tamsin selection remains a separate one-asset-per-image task.

## Classification

`REFERENCE_GENERATED -> DETAIL_LANGUAGE_ACCEPTED -> PLAYER_SELECTION_REJECTED -> TAMSIN_SELECTION_REJECTED`
