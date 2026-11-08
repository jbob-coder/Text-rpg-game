# THE GAME — What Kind of Game Is It, and How Do You Play?

**Document type:** Player-facing game identity and play guide  
**Written:** 2026-11-08  
**Status:** Current product direction + verified source-backed Phase 1 explanation; **not a release announcement, new canon, gameplay expansion or claim that the final Android UI exists**  
**Repository:** jbob-coder/Text-rpg-game  
**Authority:** [Game Foundation](GAME_FOUNDATION.md), [Phase 1 Solo Playable](PHASE_1_SOLO_PLAYABLE_PARALLEL_TRACK.md), [Progression Master Plan](systems/PROGRESSION_MASTER_PLAN.md), [Android UX Master](android/APPLICATION_UX_MASTER_PLAN.md), [Product Presentation Decision](PRODUCT_PRESENTATION_DECISION_2026-11-08.md)

## The game in one paragraph

**THE GAME is a single-player, story-driven, choice-based text role-playing game (RPG) with persistent consequences, character development and a functional world map.** Instead of steering a 3D character around an action scene, you mainly **read or listen to descriptions, choose what to say or do, inspect your character and surroundings, travel between reachable locations, use equipment and abilities, and live with the results**. The underlying game tracks what you did, what you know, whom you trust, your condition and resources, and how the world reacts. Its longer-term ambition includes richer social systems, an expanding world and tactical encounters, but **the complete envisioned game is not yet implemented**.

## 1. Genre and player experience

| Question | Answer |
| --- | --- |
| What genre? | **Narrative / choice-driven RPG**, with exploration, progression, quests, dialogue, simulation systems and planned tactical combat |
| Single-player or multiplayer? | **Single-player first.** NPCs and companions are simulated game characters; online multiplayer is not part of Phase 1 |
| Real-time 3D action? | **No.** Primary interaction is authored text and selectable actions; travel uses a functional schematic location map |
| Linear visual novel? | **Not just a visual novel.** Choices can be checked against skills, knowledge, inventory and relationships and can update persistent state |
| Random AI story generation? | **No runtime generative AI required.** Authored content and deterministic rules control valid events and outcomes |
| What matters most? | **Consequences.** Information, preparation, resource management, NPC history and decisions can change later possibilities |
| Where can you play? | The repository contains a **Python CLI development client** and an **Android Kotlin/Compose client with a Python engine bridge**. Current Android build/physical-device release readiness requires separate exact-head verification |

**Working name:** THE GAME / Text RPG Game. A final commercial title is not established by this document.

## 2. The core play loop

1. **Arrive somewhere.** The game presents the current place, the situation and player-visible people or objects.
2. **Observe and read.** Take in the description, available information, your condition and the actions offered. Some facts may remain hidden until discovered.
3. **Choose an action.** Investigate, speak, answer, train, use something, make a decision, travel or engage with a challenge when that action is actually offered.
4. **Resolve the choice.** The Python rules layer checks the authored requirements (for example, existing knowledge, attributes/skills, items, relationships, time or resources) and determines the result.
5. **See the consequence.** Dialogue, quest state, discoveries, inventory, resources, relationships, world flags or future choices may change. A choice can succeed, partially succeed or have a cost depending on its rule.
6. **Prepare and progress.** Inspect Stats/Character, change equipment when allowed, develop skills or abilities through the supported mechanics, and plan the next move.
7. **Explore the world.** Use the schematic map to move among discovered/reachable places where the authoritative game allows travel.
8. **Save, stop and return.** Important changes should persist after a save/load cycle; Phase 1 requires this behavior to be proven as an integrated loop.

**Flow:** Read location → inspect situation → select choice → rule evaluation → persistent consequence → manage/travel → continue.

There is no requirement to type arbitrary commands or have a conversation with a live AI. In the current slice, the **available authored choices** are the main interaction contract.

## 3. What you do on the Android screens

The **currently checked-in Compose code** exposes the following *separate top-level* sections in [GameScreen.kt](../android/app/src/main/java/com/thegame/rpg/ui/GameScreen.kt):

| Existing section | Player purpose |
| --- | --- |
| **Story** | Read the present scene, view available choices and act |
| **Character** | Check player summary and manage supported equipment slots |
| **Stats** | Inspect attributes, skills, modifiers, derived numbers and projected abilities/conditions |
| **Inventory** | Review carried items and use existing equip/unequip actions where allowed |
| **Quests** | Inspect the current quest projection |
| **Map** | Examine a schematic location graph and travel through eligible routes |
| **More** | Access supporting controls/settings |

**Important:** The black-and-gold UI screenshots shared as references show alternative designs, including six sub-tabs inside Character. That **is not the current implemented navigation**. Future grouping may simplify the experience, but only after validating the real data and actions.

Narration/audio controls are part of the existing Android design and code paths; they are **not proof** that audio features have been exercised successfully on the intended physical device at the latest HEAD.

## 4. Character growth and decisions

The current engine's **seven actual core attributes** are: **Might, Agility, Endurance, Intellect, Will, Perception and Presence**. Skills are separate. Current resource models include **Health, Stamina, Focus and Resolve**, plus power-specific resources where supported. Equipment, conditions and other effects can alter effective numbers.

The engine also contains **ability/technique mastery**, requirements and costs. The design direction is that progress should be earned through meaningful play—practice, use, discovery, learning, quests and relevant time/resource investment—not granted merely because a decorative button exists.

The images showing **Lv. 3 Adventurer, STR/DEX/CON, MP, a universal XP bar, Skill Points, Combat/Magic/Life/Utility ability sets, a free “Choose Class” or “Unlock Class” button, and Power Strike** are **UI examples, not verified mechanics in this repository**. Class identity, generic character level, point allocation/reset, exact ability taxonomy and balance need their own approved contracts. Do not teach the player to use features that are not actually implemented.

## 5. World and setting

The owner's **main fictional setting direction** centers on a civilization shaped by crystals, gateways, beasts and crystal-based energy/technology. Exact chronology, world origin, political geography and accepted events require canon review under **D-084**; in particular **AC means “Antes del Crystal” (before the Crystal event)**, not “After Crystal”. No post-Crystal dating abbreviation is established here.

The playable engineering proof region is **Gate Twelve**. Its existing *The Dead Relay* content is a **provisional vertical slice** that demonstrates branching story and systems. Gate Twelve is not automatically the final universe's entire map or definitive origin story.

Names and descriptions appearing only in UI reference screenshots—such as “Rivercross,” the market square and named class/skill examples—are **not imported into the canon or game content**.

## 6. A hypothetical moment of play

*Illustration only; not a transcript or promise of exact in-game choices:*

You enter a guarded location. The text describes a damaged device, a wary local NPC and a route that may be inaccessible. You can investigate first, speak to the NPC, attempt a technical approach if eligible, or leave. If you discover a fact or earn trust, a later choice may become available. A failed attempt may cost time or resources. On returning, the game should remember changes that were stored in its authoritative state.

This is the intended difference between reading a story with buttons and playing an RPG with a persistent world.

## 7. How to try the current development slice

**Prerequisite:** a local checkout of this repository's real game branch, **docs/master-game-development-program** (or an intentionally selected derived working branch), Python 3.10+ and the repository's source/content files. Do **not** use the minimal placeholder `main` branch as the game.

From the repository root on macOS/Linux:

```bash
PYTHONPATH=src python -m textrpg.cli content/vertical_slice_01.json --save local_save.json
```

On Windows PowerShell:

```powershell
$env:PYTHONPATH = "src"
python -m textrpg.cli content/vertical_slice_01.json --save local_save.json
```

The CLI is a **development play interface**, not the final Android presentation. Its authored vertical-slice content comes from [vertical_slice_01.json](../content/vertical_slice_01.json). The `--save` option provides a local save path; actual recovery and save/load behavior must still be confirmed for the exact revision being tested.

To verify the Python suite locally (this document did **not** run it):

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

The Android code uses Kotlin/Compose and a Python bridge. Building, installing and manually exercising an APK needs a separate Android SDK/device/emulator workflow and cannot be inferred from this document or from another PR's green CI. Consult [APK Rebuild & Evolution Master Plan](android/APK_REBUILD_AND_EVOLUTION_MASTER_PLAN.md) and the repository workflows for verified build instructions/evidence.

## 8. Present features versus future ambition

| Domain | Current evidence | Remaining / not implied |
| --- | --- | --- |
| Authored scene choices | Python core + content pack + CLI and Android Story consumer | Full final story, all chapters and all locations |
| Stats, resources, conditions | Engine rules/status projections and Android Stats | Screenshot-specific naming, point-allocation and generic level/XP |
| Skills/powers | Engine skill/ability/technique state and projections | Complete class/ability-set UI and new power definitions |
| Inventory/equipment | Python equipment logic and Android Character/Inventory surfaces | Final market/economy and all gear art |
| NPCs/quests/knowledge | Stateful systems, a bounded playable content slice and existing tests | Complete autonomous society/final world narrative |
| Travel | Schematic graph/navigation and eligibility rules | Seamless 3D open world or invented destinations |
| Tactical combat | Bounded tactical Python foundations exist; the Phase 1 integration chain remains incomplete | Finished Android tactical encounter interface / production balance |
| Save/load | Versioned persistence and current client paths exist | Assumption of release-ready data recovery without exact-head and physical-device checks |
| Visual presentation | Existing Android UI and historically accumulated pixel assets | Later owner-directed text-first/no unwanted pixel-art policy is **not yet fully integrated**; compare PR #97/#94 |

## 9. What the player should expect from a first playable version

**A compact, meaningful slice:** one small region, real choices with consequences, a few persistent characters and quests, one legitimate progression path, a limited equipment loop, functional map travel, and reliable save/reload. A **full-class roster, giant kingdom map, randomized NPC civilization, polished tactical interface and final black-and-gold menu suite are not prerequisites for that first proof** unless their direct acceptance gate specifically requires them.

The release gate is stricter than “the APK opens”: the core loop, persistence, hidden-information safety, exact-HEAD automated tests, device startup and performance must be verified. See [Phase 1 exit gate](PHASE_1_SOLO_PLAYABLE_PARALLEL_TRACK.md#8-phase-1-exit-gate).

## 10. Source of truth and change control

- **Player-facing identity / how to play:** this document, subordinate to owner canon and verified implementation.
- **Product presentation and screenshot boundaries:** [2026-11-08 decision](PRODUCT_PRESENTATION_DECISION_2026-11-08.md), engineering direction pending review/merge.
- **Rules and content:** Python source, approved content packs, schema/migration tests, relevant system masters.
- **Android presentation:** current Kotlin code and [UX master](android/APPLICATION_UX_MASTER_PLAN.md) after an approved presentation update.
- **World facts:** D-084 canon provenance work; Gate Twelve is provisional.
- **Work priorities/claims:** [Live Bulletin](AI_TASK_BULLETIN_BOARD.md) and [Master Task Register](THE_GAME_MASTER_TASK_REGISTER.md), not this guide.

**Plain-English summary:** This is a **story-first role-playing game where your choices, knowledge and character state shape what can happen next**. You play by reading, choosing, investigating, progressing, traveling and saving—not by controlling a full 3D avatar. The Android UI and final world are still being developed.