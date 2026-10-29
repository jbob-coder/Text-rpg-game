# THE GAME — 2026-10-27 owner correction: text gameplay plus navigation map

**Repository:** jbob-coder/Text-rpg-game  
**Authority branch:** docs/master-game-development-program  
**Owner decision (2026-10-27 AST):** Keep a navigable map and make the remaining gameplay interaction text-based. Do not keep unwanted pixel-art scene illustrations, animated sprites, paper-doll renders, decorative pixel graphics, or orphan production assets in the active Android runtime.

## Why this record exists

During the owner's engine/bug audit, the assistant discovered that the existing Android client and repository standards still enforce pixel art, contradicting the owner-confirmed direction. The owner explicitly directed that unwanted visual material be located and removed, beginning with the visual area, and finally directed agents to continue the **habitual development workflow** rather than push changes directly to main.

This newest, explicit owner instruction **supersedes** the older pixel-art product constraint, production plans and asset-generation directives *for active implementation*. Preserve old notes solely as provenance of a superseded direction. Do not resurface old pixel plans as new work or introduce graphics without a fresh explicit owner direction.

## Current product contract

- **Retain:** Python RulesEngine, deterministic decisions, textual scene titles/bodies/choices, player and NPC text, status, quests, inventory, equipment mechanics, save/load, narration, Android bridge and safe snapshot mapping.
- **Retain the map:** discovered locations, route edges, selection, reachability and lawful travel. A simple non-pixel positional map canvas is permitted as a navigational surface, not an illustration/animation engine.
- **Retire:** pixel scene images, player/NPC sprites, rasterized decorative item/paper-doll graphics, pixel overlays, icon/animation asset catalogs, and tests/tooling whose only purpose is to require those images.
- **Never silently remove:** stable gameplay IDs, routes, scene/quest save state, actor semantic information or player-facing choices. Keep the underlying Python visual metadata/validation until a separately verified schema/content migration proves it is safe to remove.
- **No expansion:** do not create new chapters, locations, content, world logic, animation substitutes, or visual effects as part of this clean-up.

## Execution and verification constraints

Work on a short-lived task branch from docs/master-game-development-program and submit a draft PR with exact file scope. `main` is the placeholder default branch and must not be overwritten. For every visual component, remove its active consumer before deleting its source. Keep text and map regression tests, do not weaken Python gameplay tests to hide errors. Verify Kotlin/Android compile, Python unittest, and emulator/device when available before declaring the cleanup complete. Historical documents are source evidence, **not active marching orders**.
