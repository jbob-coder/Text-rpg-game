# Game Context — Text RPG Foundation Chat

Contributor scope: information accessible to this chat as of 2026-09-26.

This file intentionally records game-related context across projects while keeping each project distinct. It is a continuity artifact, not a claim that every older project is still active.

## 1. Current Text RPG Game

### Identity

- `USER_CURRENT`: Repository: `jbob-coder/Text-rpg-game`.
- `VERIFIED_REPO`: Development branch: `foundation/text-rpg-systems`.
- `VERIFIED_REPO`: This shared context branch was created from that foundation branch: `context/shared-game-context`.
- `VERIFIED_REPO`: `main` was not modified by the foundation work described here.
- Product direction: authored, deterministic, stateful choice RPG / text RPG with persistent consequences and a pen-and-paper campaign feel.
- Runtime generative AI is not required and should not be the game engine.

### Core design requested by the user

The player should be able to:
- read authored scenes and make decisions;
- act alone or with a party/group;
- train over real in-game time;
- fight, investigate, talk, equip gear, learn, and develop powers;
- have old choices, old conversations, stats, knowledge, relationships, equipment, and party composition change later options;
- encounter important characters with their own personalities, memories, private knowledge, goals, and story progress;
- experience hidden/private conversations where information can remain private or later leak through authored rules;
- earn progress gradually rather than gaining major abilities/statistics from one trivial button press;
- use many meaningful stats/perks/powers/equipment systems without turning the interface into an unreadable spreadsheet;
- eventually use consistent pixel-art portraits/scene art/sprites/animations.

### Reference direction

The uploaded `My Vampire System` material is reference material only.

Allowed abstraction:
- visible status/progression;
- levels/experience/quests as a legible progression pattern;
- powers with costs, drawbacks, prerequisites, cooldowns, and evolution;
- ability rank separate from raw combat effectiveness;
- active/passive equipment;
- crafting quality depending on material and crafter/process quality;
- multiple resource/energy layers when each has a distinct gameplay function;
- faction/social/information systems;
- major unlocks and passive rules that materially change play.

Not allowed as project canon:
- copied novel prose;
- copied character identities;
- copied proprietary terminology;
- copied locations/factions/story arcs;
- one-to-one recreation of source UI.

### Implemented rules foundation

`VERIFIED_REPO` from `docs/IMPLEMENTATION_STATUS.md` and current source:

- authoritative serializable `GameState`;
- deterministic authored scene engine;
- persistent history;
- visible vs hidden vs locked choices;
- four check outcomes: critical success, success, failure, critical failure;
- conditions based on player stats, relationships, player knowledge, NPC knowledge, party membership, ability rank, perks, inventory;
- effects for flags, player values, relationships, player/NPC knowledge, inventory, quests, party, perks, personality;
- equipment/perk modifiers can affect checks without rewriting base player values;
- ability mastery XP/rank;
- technique prerequisites based on rank/mastery/knowledge/perks;
- versioned JSON persistence;
- content validation and stable-ID rules;
- seven core attributes;
- grouped skill catalog;
- derived values/resources;
- training and recovery;
- timed conditions/injuries;
- equipment slots, set IDs, set bonus helpers;
- NPC memory/private knowledge/social leak-candidate rules;
- pixel visual bible;
- abstract source-reference notes.

### Canonical current attribute model

Core attributes, intended 0–100 and slow moving:
- Might
- Agility
- Endurance
- Intellect
- Will
- Perception
- Presence

Skills are narrower and advance faster.

Skill families:
- Combat: unarmed, blades, ranged, defense, tactics
- Physical: athletics, stealth, traversal, survival
- Technical: engineering, technical_systems, medicine, crafting
- Social: persuasion, deception, intimidation, empathy, leadership
- Knowledge: investigation, history, factions, powers, creatures

Universal resources:
- Health
- Stamina
- Focus
- Resolve

Power-specific resources may exist separately.

### Derived-stat formulas currently documented

Provisional values:
- Max Health = 50 + Endurance × 2.0 + Will × 0.5
- Max Stamina = 40 + Endurance × 1.5 + Athletics × 0.5
- Max Focus = 30 + Intellect × 0.8 + Will × 0.7
- Max Resolve = 25 + Will × 1.1 + Presence × 0.35 + Leadership × 0.15
- Initiative = Agility × 0.7 + Perception × 0.3
- Accuracy = Perception × 0.55 + Agility × 0.20 + Ranged × 0.25
- Evasion = Agility × 0.65 + Perception × 0.20 + Athletics × 0.15
- Guard = Endurance × 0.45 + Might × 0.25 + Defense × 0.30
- Carry Capacity = 10 + Might × 0.8 + Endurance × 0.2

These are balancing placeholders, not final canon numbers.

### NPC/social model

Important NPCs should have stable IDs and independent state for:
- personality;
- memories;
- private knowledge;
- goals;
- story state;
- multidimensional relationships.

Relationship axes:
- trust
- respect
- affection
- fear
- suspicion
- debt
- loyalty

Personality axes:
- empathy
- aggression
- caution
- ambition
- honesty
- loyalty
- curiosity
- discipline

Knowledge must be character-owned. Player knowledge is not automatically NPC knowledge.

Secret propagation should be deterministic and inspectable. The system may calculate eligible leak targets from authored networks/personality/secrecy, but content decides whether the leak event actually fires.

### Power progression

A power should not be just an unlock button. Desired fields include:
- stable ability ID;
- family/category;
- rank;
- mastery XP;
- discovered/active techniques;
- passives;
- resource costs;
- cooldown/recovery;
- physical/mental prerequisites;
- incompatibilities;
- drawbacks;
- evolution requirements;
- hidden properties discovered through play.

Desired technique progression concept:
Unknown → Discovered → Unstable → Learned → Practiced → Mastered → Specialized/Evolved.

Current implementation has mastery stages and rank thresholds, but the broader runtime slice still needs costs/cooldowns/drawbacks/evolution integration.

### Visual direction

- pixel art readable on mobile;
- strong silhouettes;
- limited local palette;
- no photorealistic assets mixed into pixel UI;
- no fake “smooth painting + pixel filter” standard;
- every recurring character needs a canonical identity sheet;
- generated image is not canon until it matches that sheet and is approved;
- recommended assets: dialogue portraits/emotions, full-body references, sprite/paper-doll layers, equipment variants, injury/status overlays;
- animation should communicate state rather than exist only as decoration.

### Current verified engineering next actions

1. Integrate condition modifiers and equipment set bonuses into effective-stat/check calculations without double counting.
2. Add power costs/cooldowns/technique stages/drawbacks/evolution prerequisites.
3. Add explicit NPC goal/story-state transitions and relationship utilities.
4. Add quest graphs, branching objectives, failure states, and validation.
5. Execute deterministic authored information-propagation events.
6. Define the first original playable vertical slice/canon opening.
7. Add character visual identity records.
8. Connect to a pixel-art runtime only after client technology is deliberately selected.

### Known repository inconsistency

`VERIFIED_REPO`:
- `docs/IMPLEMENTATION_STATUS.md` says the branch-equivalent verification passed 29 tests.
- `README.md` still says the latest verification is 16 tests.
This is a documentation drift issue. The implementation-status document is newer/more detailed, but the test suite should be rerun against the live branch before a new “current” test claim is made.

---

## 2. Pixel RPG / Goblin Underwater work

### Most recent explicit direction recovered from recent chat

`USER_PRIOR` dated 2026-09-26:
- user named repository `rpg pixel goblin underwater`, corresponding to `jbob-coder/pixel-rpg-goblin-underwater` in discovered repositories;
- requested a branch called **Godot tools and shortcuts**;
- that branch should record Godot code/tools/features, official references, and how the code is applied so another bot can understand what Godot offers;
- user also asked the other chat to work on the avatar full-body pixel style, starting from a foot blueprint with all six sides;
- later asked for animation reverse-engineering/reference for walking, running, crouching, with proper foot/joint behavior researched first;
- user wants the assistant itself to create/generate the requested development assets rather than hand the task off to an unrelated service.

### Older Pixel RPG authority recovered from prior chat

`USER_PRIOR` dated 2026-09-21:
- prior active repo was `jbob-coder/Chatgptjuegolpcal`;
- active branch `pixel-rpg`;
- Monster Choice RPG, WorldLife RPG, Shooter RPG were said to be abandoned/non-authoritative **for that Pixel RPG project**;
- live repo/source/build evidence outranks chat memory;
- Godot version must be checked from the live project before making claims (previously 4.7.2);
- free development only;
- do not use paid/billing-risk tools;
- Higgsfield specifically was marked do-not-use in that workflow;
- workflow: read state → establish authority → bounded task → implement → test → document;
- never claim unrun tests/builds.

### Pixel RPG presentation/gameplay direction

- third-person pixel-styled 3D;
- Android landscape;
- visible player;
- left joystick movement;
- right side independent camera;
- physical exploration;
- monster hunting;
- body-part targeting/breaking/severing;
- enterable buildings;
- compact settlement;
- hard visual edges;
- controlled palette;
- nearest-neighbor/pixel treatment;
- clear silhouettes;
- avoid realistic PBR look;
- avoid voxel-like look unless explicitly changed later.

### Status warning

`UNKNOWN`: The relationship between the 2026-09-21 `Chatgptjuegolpcal` authority and the 2026-09-26 `pixel-rpg-goblin-underwater` repository must be checked live before implementation. Do not silently treat them as the same repository.

---

## 3. WorldLife RPG

### Android concept

`USER_PRIOR`:
- original life-simulation RPG inspired by the concept of BitLife but not copying UI/writing/branding/assets;
- name used: **WorldLife RPG**;
- Android target using Kotlin + Jetpack Compose;
- game logic separated from UI;
- `GameState` authoritative and persistent;
- deterministic/seedable randomness;
- local saves survive updates;
- stable IDs for characters/events/locations/entities;
- expandable architecture;
- no external paid services.

Initial requested vertical slice included:
- new game creation: gender/name/background;
- start around age 0–1;
- age-up and daily/weekly tick;
- choices with outcomes and stats;
- education/skills/economy;
- relationships/reputation;
- jobs;
- events/options;
- death conditions;
- end summary.

Later pivot:
- open-world 2D/3D third-person presentation;
- Monster-Hunter-like camera reference without copying IP;
- horizontal/landscape;
- left movement joystick;
- right side camera control;
- later crouch/jump;
- shooter-style mobile control scheme;
- streets/buildings/interiors/world layout;
- image assets reusable/editable;
- user asked about APK testing and local installation.

Constraints:
- free tools;
- avoid billing;
- Google Drive was preferred in some workflows;
- APK install outside app store;
- Android device for testing.

### iOS WorldLife branch

`USER_PRIOR` dated 2026-08-31:
- separate iOS project;
- SwiftUI frontend;
- authoritative deterministic `GameState`/`GameEngine`;
- JSON save/load;
- deterministic RNG;
- XCTest;
- iOS 17;
- XcodeGen;
- persistent city/districts;
- player stats/events/NPC relationships/economy/safety/opportunity;
- source was generated but not Xcode-compiled or Simulator-tested at that point.

### Status

`STALE_OR_SUPERSEDED` for Pixel RPG only: one later Pixel RPG handoff explicitly called WorldLife abandoned/non-authoritative for that project. Keep the WorldLife history, but do not assume it is the active game unless the user reactivates it.

---

## 4. Godot Crystal Life RPG / Original open-world project

This project went through multiple names/continuity states. Preserve details but verify which repository is authoritative before edits.

### Core direction

`USER_PRIOR`:
- Godot-only;
- Godot 4.7 family, later instructions referenced 4.7.1 stable and another sandbox reported `4.7.stable.official.5b4e0cb0f`;
- first-person;
- large detailed 3D open-world RPG/life sim;
- realistic diegetic watch/time UI;
- time speeds: fast/normal/slow/slower/slowest;
- 50+ stats separated from temporary effects;
- world theme around **2010 AC (After Crystal)**;
- gateways opened in ancient history; beasts/mutations/crystals changed civilization;
- crystals power technology;
- normal phones/cars, not default cyberpunk;
- credits used as currency in one iteration;
- original large-beast hunting;
- body-part damage and area/quality-dependent loot;
- no Monster Hunter IP copying.

### Movement/world systems discussed

- first-person movement;
- crouch toggles (C/Ctrl/B in a prototype);
- camera-height change;
- crouch speed;
- jump blocked while crouched;
- low-beam crouch test;
- hinge doors;
- build city/settlement piece by piece;
- enterable buildings/interiors;
- world streaming;
- occlusion/visibility distance;
- LOD/HLOD;
- MultiMesh;
- physics activation ranges;
- background loading;
- origin shifting if needed;
- “only render what player can see” / Minecraft-distance-style performance thinking.

### NPC direction

- NPCs should not use runtime generative AI;
- detailed authored interaction rules;
- schedules, needs, relationships, memory, knowledge;
- Sims-like life-sim interaction depth but upgraded;
- deterministic simulation.

### World/ecology direction

- continent/biomes;
- cities/districts;
- wildlife;
- economy;
- quests;
- combat;
- crafting;
- equipment;
- weather;
- day/night;
- audio;
- animation;
- customization;
- large creature hunting/ecology;
- persistent obstacles/boulders/gates/locks/power/alarms/damage.

### ASCII 3D prototype

Prior project context included:
- GPU-based ASCII shader on a single node;
- brightness mapping;
- A/D grid density;
- E/F prompts;
- rotating cube/crystal;
- pedestal;
- experimental XYZ/index-grid and image-to-character mapping;
- performance experimentation with an approximate 10 GB RAM upper test budget.

### Repositories/paths seen in prior work

Do not assume all are current:
- `jbob-coder/mvs-world-reconstruction_box`
- `jbob-coder/mvs-world-reconstruction`
- local path previously reported: `C:\Users\jeanw\Desktop\MVS_Military_School`
- `godot-only-development-archive/test_projects/ascii_3d_render_sandbox`

### Governance requirements

- research official stable Godot docs before important engine work;
- Godot Forum secondary source;
- keep research-to-code traceability;
- distinguish documented vs implemented vs parsed/imported vs executed vs visually validated vs performance/export validated;
- no shortcuts;
- modular/testable architecture;
- preserve old work when archiving/reorganizing.

### Major IP change

`USER_PRIOR` dated 2026-07-30:
- vampire content deleted/prohibited;
- remove source-story names and identity-bearing terminology;
- create original title/world/cast/factions/locations/abilities/creatures/institutions/lore/visuals/dialogue/terminology.

This must be treated as a hard IP constraint in later iterations of that project.

---

## 5. MVS reconstruction / source-analysis projects

The user has used `My Vampire System` material to study mechanics and reconstruct system/world logic for private design/research.

Important distinctions:
- private research/extraction is not automatically runtime game canon;
- source manuscript text must not be committed;
- canon/non-canon separation must be explicit;
- later original-IP game work removed vampire-specific names/elements.

Prior repository/branch governance included:
- `main`
- `world-assumptions`
- `novel-reconstruction`
in one locked reconstruction phase;
- legacy branches should be individually extracted before retirement/deletion.

One prior assistant record said these branches were synchronized at a specific commit, but that is historical and must not be treated as current without live verification.

---

## 6. Veilbound Choice RPG

`USER_PRIOR`:
- repository `jbob-coder/jbob-coder-veilbound-choice-rpg`;
- private;
- Python >=3.11;
- original-IP text/choice RPG/life-sim;
- branching chapters;
- command exploration;
- player/family/school systems;
- NPC memory/schedules;
- relationships;
- abilities;
- world simulation;
- resource recovery;
- save/load.

Quality rule:
- read relevant files;
- distinguish facts/assumptions/unknowns;
- small tested changes;
- verify with `python -m veilbound_choice_rpg.verify`;
- preserve original IP;
- runtime must not import external canon/extraction material;
- safety/blocked-action rules cannot be bypassed.

A prior memory reports hundreds of tests/checks passing, but that number is historical unless rerun.

---

## 7. Private Jack Wilson RPG campaign

This is a player/campaign continuity context and should not be conflated with the Text RPG engine unless explicitly imported.

Known player-character continuity:
- character name: Jack Wilson;
- start level: 1;
- level cap used in one continuity: 20;
- start location ID: `ROOM_JACK_START_01`;
- year used: 2670 CE;
- relative start: T-14 days to T0;
- ability stable ID: `ABILITY_STEAL`.

Steal ability concepts from earlier play:
- external/exceptional ability relative to setting;
- permanently steals stats and up to 3 abilities in one earlier description;
- requires physical contact;
- contact maintained around 5 seconds in one iteration;
- activation stamina cost roughly 4–5 in one earlier iteration;
- stolen stat multiplier ×4 in one earlier version;
- target may collapse;
- an older continuity included a severe death-curse risk.

Sample older starting stats:
- HP 10
- Stamina 10
- Attack 8
- Speed 5
- Evade 6
- Luck 1

These values are **historical campaign notes**, not automatically current canon. Check the current state files/handoff before play.

### Private RPG context-preservation rules

Uploaded rules state:
1. `data/state.json` is the highest file authority;
2. then `data/map.json`;
3. `data/npcs.json`;
4. `data/quests.json`;
5. `sessions/*.md`;
6. `markdown/*.md`.

If chat memory conflicts with those files, files win.

Also:
- do not simplify/reset/overwrite unless asked;
- do not discard existing state;
- do not invent a different setting;
- long history may be compressed, but current state/location/active quests/NPC memory/unresolved plot threads must remain.

---

## 8. Hollow Reach CRPG

Older project pointer:
- Pygame;
- 640×480;
- state-based screens;
- CRPG rather than tactics game.

No current implementation authority is available in this chat. Treat as historical until live files are supplied.

---

## 9. Jack-Wilson-World / memory-heavy game repository

Prior project structure included directories such as:
- RAW_LOGS
- MEMORY_CHUNKS
- SESSIONS
- TIMELINES
- CHARACTERS
- NPCS
- RELATIONSHIPS
- KINGDOMS
- FACTIONS
- WORLD
- ECONOMY
- SECRETS
- IMPORTERS
- STAGING
- ANALYTICS
- RECONSTRUCTION
- SAVEGAME
- BRAIN
- GAME_ENGINE
- ENGINE_SOURCES
- PROMPTS

This context reflects the user's preference that game/world continuity be file-backed, inspectable, and durable rather than existing only in chat memory.

---

## 10. Cross-project user constraints that materially affect game work

These are recurring instructions and should be checked against the current project before action:

- quality over speed;
- current files/live repository outrank stale chat memory;
- do not claim tools/actions/tests that were not actually executed;
- make small, reversible changes;
- preserve source of truth and stable IDs;
- distinguish current facts from assumptions/unknowns;
- provide test/verification evidence;
- avoid paid/billing-risk tooling unless explicitly authorized;
- original IP, no direct copying of referenced games/novels;
- game systems should be expandable and maintainable;
- deterministic rules are strongly preferred for simulation/save/replay reliability;
- persistent state should live in files/data, not only prose;
- when multiple projects exist, do not blend their mechanics/repositories/authority accidentally.

## 11. Open conflicts / verification requirements

Before doing cross-project work, resolve these live:
- Which Pixel RPG repository is currently authoritative: `Chatgptjuegolpcal` or `pixel-rpg-goblin-underwater`?
- Which MVS/open-world Godot reconstruction repository is current: `mvs-world-reconstruction_box`, `mvs-world-reconstruction`, or another renamed project?
- Which Godot exact version is current for each repo?
- Which historical project is active vs archived?
- Whether WorldLife is being revived or remains inactive.
- Whether Jack Wilson campaign state files supersede the historical values above.

Do not guess these answers from this context file. Inspect the live project or ask only when the information cannot be established from files.
