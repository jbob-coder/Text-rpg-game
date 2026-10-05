# AXIOM D-064 support branch status

**DO NOT MERGE THIS BRANCH.**

This branch was created only as an isolated support experiment for Kestrel's D-064 surgical rebuild.

Two preliminary wiring commits landed:
- `GameScreen.kt` passes `snapshot.room.actors`;
- `SceneIllustration.kt` accepts `roomActors` and forwards them to the actor catalog.

The catalog/test portion was **not completed** through the available write path, so this branch is intentionally incomplete and is not a merge candidate.

Authoritative execution guidance remains:
`docs/evidence/D064_LIVE_AUTHORITY_SURGICAL_REBASE_MANIFEST_2026-10-04.md`

Kestrel retains D-064 ownership and should create the final fresh GREEN branch from live authority.
