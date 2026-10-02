# THE GAME — Asset Reference Registry

This registry tracks generated/collected reference images separately from production pixel assets.

A reference appearing here does **not** imply canon approval or production readiness.

| Reference ID | Status | Scope | Persisted location | SHA-256 | Allowed use | Rejected use |
| --- | --- | --- | --- | --- | --- | --- |
| `UI_REFERENCE_CHARACTER_APPROVED_V1` | `REFERENCE_SELECTED / CHARACTER_TAB_APPROVED` | Jack Wilson Character-tab visual identity/presentation | Google Drive file ID `1OrLsw_mvbZ5HipFObfX8wdvA7vAPa-Ve` | `af453993693ff0447da3a1bf07e0276013f0c87f6a69442f86c5f3192487d867` | Jack visual identity, human proportions, silhouette, layered clothing/equipment presentation, character-art alignment across UI scales | Gameplay stat authority, hidden state, collision/hitbox geometry, exact 32x48 anchors, unseen turnaround views, animation timing |
| `REF_BATCH001_CONCEPT_BOARD_A` | `REFERENCE_GENERATED / STYLE_DIRECTION_ACCEPTED / CANON_GEOMETRY_REJECTED` | Broad Batch 001 style probe | Google Drive file ID `1JDvlmF_Mfy93rs_Llq5rB444EOUF5Gzr` | `2d52f5364cecd1338e3c4cd0eafdbba7d5575e980f4c3d7856db3c6119e83ec8` | Pixel-density direction, modular sheet layout, dark industrial value language, restrained cyan/gold accents, icon/scene/FX family coherence | Canon player face, canon Tamsin geometry, item existence, courier identity, district architecture, relay state contract |

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

