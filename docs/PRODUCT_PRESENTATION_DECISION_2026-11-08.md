# THE GAME — Product Presentation & Screenshot Blueprint Decision

**Date:** 2026-11-08  
**Status:** Selected engineering/documentation direction; proposed for review. **Not merged, not implemented, not a new owner gameplay/canon decision.**  
**Repository/authority:** jbob-coder/Text-rpg-game / docs/master-game-development-program (baseline 8fb27ce31b530ee301068310caecf8118d23f371)  
**Scope:** Game type, Android presentation priorities, handling of user-supplied mobile UI screenshots and blueprints, related documentation synchronization.

## 1. Evidence and authority

- **Existing owner directive (higher priority):** THE GAME is a **text RPG with a functional world map**. Unwanted pixel-art presentation must be removed; story, choices, interactions, equipment, stats, quests and inventory stay text-first. See [PR #97](https://github.com/jbob-coder/Text-rpg-game/pull/97) for proposed/unmerged implementation and its competing draft PR #94. Do **not** infer either PR was merged.
- **Product foundation:** [GAME_FOUNDATION.md](GAME_FOUNDATION.md) describes authored choices, durable consequences, deterministic rules, NPC memories, information-gated choices and earned progression.
- **Phase 1 contract:** [PHASE_1_SOLO_PLAYABLE_PARALLEL_TRACK.md](PHASE_1_SOLO_PLAYABLE_PARALLEL_TRACK.md) uses provisional Gate Twelve to prove the smallest persistent playable loop, rather than committing to a complete world or final UI.
- **Current Android code:** [GameScreen.kt](../android/app/src/main/java/com/thegame/rpg/ui/GameScreen.kt) exposes Story / Character / Stats / Inventory / Quests / Map / More. [CharacterSection.kt](../android/app/src/main/java/com/thegame/rpg/ui/CharacterSection.kt) and [StatsSection.kt](../android/app/src/main/java/com/thegame/rpg/ui/StatsSection.kt) are separate real Compose screens. Their current behavior is not the same as the supplied fantasy UI concepts.
- **Owner's 2026-10-08 canon correction:** the main fictional world is crystal-centered; **AC means Antes del Crystal (before the Crystal event)**. The post-Crystal dating notation and specific dates remain unverified. The Gate Twelve slice is provisional; imported story names/locations from a screenshot are not canon. See the live [Bulletin](AI_TASK_BULLETIN_BOARD.md) and D-084.
- **Reference images:** the user supplied images of Story, Character/Overview, Stats, Skills and Abilities mobile screens and generated blueprints. They demonstrate information hierarchy and styling ideas, **not** a complete gameplay contract, working app, measured display density or authorization to copy any art.

## 2. Chosen direction

**Keep the authored, single-player, choice-driven, text-first RPG as the product.** Use the **functional schematic world map** for exploration/travel. Improve Android presentation incrementally with readable type, clear hierarchy, touch-usable navigation, conditional choices, compact status summaries and restrained visual framing. Optional dark/gold/high-contrast styling can be considered as a **candidate skin**, not an adopted asset standard or mandatory full screenshot recreation.

The UI is a **projection and control surface**, not the source of game truth. Python state, authored content and player-safe DTOs own whether classes, ability sets, resources, NPCs, quests, destinations or actions exist. Android may organize these data but must not invent them.

The screen images are **layout/interaction study material**. Reusable patterns worth exploring: persistent navigation; character summary; tabbed/grouped read-only views if useful; resource displays backed by the real model; selection/locked/empty states; skill details with requirements; readable choice lists. Nothing in this decision authorizes pixel characters, imported icons, new skills, reset mechanics, XP bars or classes.

## 3. Screenshot-to-runtime compatibility matrix

| Shown in images | Current verified system | Decision / gate |
| --- | --- | --- |
| Decorative black/gold card-and-tab design | Current Compose client uses separate sections and historic pixel presentation | **Candidate visual reference only**; implement accessible original UI after source/DTO audit |
| Story/location paragraph + choice buttons | Authored scene and choice engine; Android Story surface | **Preserve** text-first narrative and real selectable choices |
| World navigation | Existing player-safe map and travel actions | **Preserve** functioning map graph and discovery/reachability |
| Overview / Stats / Skills / Abilities / Class / Background character tabs | Current top-level Character and Stats screens; abilities may appear in Stats | **Do not claim implemented**; future grouping only if it reduces navigation cost without duplicate state |
| STR/DEX/CON/INT/WIS/CHA/LUK/PER, HP/MP/STA | Current seven authored attributes: might, agility, endurance, intellect, will, perception, presence; current resources include health, stamina, focus, resolve | **No field replacement by screenshot**; requires approved mechanics/schema migration |
| Lv. 3 / generic XP 240/500 / SP 2 / point allocation | Engine has authored stats, skills and ability/technique mastery; class, level and generic point economy remain separate roadmap decisions | **Illustrative only**; no currency, level, allocation or reset rule inferred |
| Class-required locks and “Unlock Class” action | Class design in Progression Master Plan, not a verified integrated class acquisition UX | **Future candidate**; show a locked state only from explicit authoritative eligibility flags |
| Combat/Magic/Life/Utility set counts and “Power Strike” | Screenshot labels and example numbers; no corresponding approved data contract established from these images | **No canon or runtime introduction** |
| “Rivercross” market and blacksmith | Example scene text in image; provisional existing playable region is Gate Twelve | **No canon promotion or story content change** |
| Exact smartphone dimensions, dp values and colors in generated blueprint | Image depicts screen pixels, not device-specific density, layout constraints or measured accessibility | **Unverified estimates**; measure using actual Compose preview/emulator/device |

## 4. Rejected approaches and rationale

1. **Clone every screenshot as a working screen now:** would introduce unsupported XP/class/ability rules and unverified dimensions.
2. **Continue legacy pixel-art mandate as current shipping policy:** contradicts later owner-directed text-first / map-only requirement.
3. **Replace the Python engine or rebuild the APK for styling:** unnecessary blast radius and conflicts with staged Phase 1 verification.
4. **Keep contradictory documentation without an explicit precedence note:** agents would implement incompatible UX and generate avoidable regressions.

## 5. Implementation sequence and dependencies (not a task claim)

1. **Documentation decision first (this branch):** establish current-vs-target boundaries; add a plain-English game/how-to-play guide; cross-link the highest-impact entrypoints.
2. **Integration/reliability before UI redesign:** review pending defect PRs and run exact-HEAD Python, Android unit/assemble and emulator gates. A green PR branch alone does not certify the authoritative HEAD. No release signoff claimed.
3. **Text-first presentation integration:** reconcile PR #97 versus #94, use approved owner direction and current code review, preserve map navigation and player-safe visibility. Do not merge merely because this decision exists.
4. **Small UI specification:** map each chosen screenshot pattern to existing Python projection, Kotlin DTO, action, loading/empty/locked state, accessibility focus, viewport test and save/load effect. If no authoritative source exists, mark it deferred.
5. **Incremental implementation:** change one screen at a time with tests and screenshot/physical-device review on the chosen low-end Android target; retain existing game data/save compatibility.
6. **Owner-canon and expansion:** D-084 remains the owner-priority world-history/narrative Bible work; this UX clarification does not assign/close/reprioritize tasks or grant canon approval.

## 6. Acceptance and non-goals

- UI changes preserve text choices, no unwanted pixel-art, the functional world map, hidden-state redaction, authoritative save/load and low-end readability.
- New controls exist **only** with verified state/actions and have accessible labels, visible disabled reasons and regression checks.
- No screenshot-only numbers, creatures, locations, character level, class, currency, ability-point economy, skill tree, resistances or resource names enter canon or save schema without separate approval and migration.
- This document adds **zero gameplay rules, images, source files, APKs or tests**. It does not certify any running build or resolve open PRs.

## 7. Related authority and handoff

- [Game type and how to play](GAME_TYPE_AND_HOW_TO_PLAY.md) — player-facing definition, actual/target boundaries and starter flow.
- [Game foundation](GAME_FOUNDATION.md) — design pillars; current precedence pointer.
- [Android UX master](android/APPLICATION_UX_MASTER_PLAN.md) — provisional UI hierarchy and consumer gate.
- [Legacy visual Bible](VISUAL_BIBLE.md) — historical pixel-art detail, **superseded for current presentation**.
- [Master program](MASTER_GAME_DEVELOPMENT_PROGRAM.md), [live Bulletin](AI_TASK_BULLETIN_BOARD.md), [Master Task Register](THE_GAME_MASTER_TASK_REGISTER.md) — execution and task authority.
- [Phase 1](PHASE_1_SOLO_PLAYABLE_PARALLEL_TRACK.md) — minimum functional slice and release evidence requirements.

**Change discipline:** this is an engineering recommendation synthesized from established owner directions and verified code; it is **not** an invented owner decision or proof of UI implementation.