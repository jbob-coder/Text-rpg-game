# THE GAME — Asset Reference Registry

This registry tracks generated/collected reference images separately from production pixel assets.

A reference appearing here does **not** imply canon approval or production readiness.

| Reference ID | Status | Scope | Persisted location | SHA-256 | Allowed use | Rejected use |
| --- | --- | --- | --- | --- | --- | --- |
| `REF_BATCH001_CONCEPT_BOARD_A` | `REFERENCE_GENERATED / STYLE_DIRECTION_ACCEPTED / CANON_GEOMETRY_REJECTED` | Broad Batch 001 style probe | Google Drive file ID `1JDvlmF_Mfy93rs_Llq5rB444EOUF5Gzr` | `2d52f5364cecd1338e3c4cd0eafdbba7d5575e980f4c3d7856db3c6119e83ec8` | Pixel-density direction, modular sheet layout, dark industrial value language, restrained cyan/gold accents, icon/scene/FX family coherence | Canon player face, canon Tamsin geometry, item existence, courier identity, district architecture, relay state contract |
| `REF_BATCH001_CONCEPT_BOARD_B` | `REFERENCE_GENERATED / STYLE_DIRECTION_ACCEPTED / PRODUCTION_STRUCTURE_ACCEPTED / CANON_GEOMETRY_REJECTED` | Broad Batch 001 production-direction probe | Google Drive file ID `1QFjPo-Rd6wCNwsZU7MVSKMsX67x1o3Ko` | `f8f97ebcb9d99dfe8e419bd87536003b6c1f84f710834fc7c8dcb33f01edf83a` | Resolution hierarchy, paper-doll separation, portrait/gameplay distinction, icon silhouettes, location/map composition, dark industrial palette structure | Canon player identity, exact Tamsin geometry when conflicting with identity contract, courier identity, generic NPC canon, unsupported items, relay state expansion, district topology |
| `REF_BATCH001_WAVE_A_BOARD_C` | `REFERENCE_GENERATED / STYLE_DIRECTION_ACCEPTED / PLAYER_SELECTION_REJECTED / TAMSIN_SELECTION_REJECTED` | Dedicated Wave A candidate sheet | Google Drive file ID `1Id6tO2-2Mte6L2W9nVE7qRKoL9qVnoCW` | `31de936c8e091decfbeb91f0a3321ffcc85885dc2f57f65eeca3fe51efd3e909` | Player proportion study; Tamsin build/palette/collar/badge/satchel/detail-density study | Player identity; Tamsin fringe side; Tamsin sleeve asymmetry; direct canonical reconstruction |

## Selection policy

A reference may be advanced to `REFERENCE_SELECTED` only for a clearly bounded asset brief.

Examples:

- a dedicated Tamsin six-view turnaround may be selected for `NPC_TAMSIN_TURNAROUND`;
- a dedicated neutral anatomy board may be selected for `PLAYER_BODYFRAME_A_TURNAROUND`;
- a generic mixed concept sheet cannot be selected as the canonical source for all assets it depicts.

## Persistence policy

Persist selected and materially useful references outside the APK in a durable source store.

Recommended Google Drive structure:

```
Text-rpg-game Asset References/
  Batch 001/
    Character/
    Equipment/
    Locations/
    UI/
    FX/
  Batch 002/
  ...
```

Production PNGs and manifests belong in the repository only after reconstruction and QA. Large concept/reference boards should remain outside the repository unless there is a specific reason to version them there.

## Required registry fields for future references

- stable reference ID;
- generation/source date when known;
- generator/source;
- exact asset brief(s) it targets;
- persisted file ID/path;
- SHA-256 when materialized;
- selected/rejected status;
- accepted observations;
- rejected deviations;
- related blueprint/manifests.

