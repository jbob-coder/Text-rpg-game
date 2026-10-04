# THE GAME — Android Navigation & Ephemeral UI-State Audit — 2026-10-04

Status: **ACTIVE D-026/D-021 EVIDENCE / CURRENT NAVIGATION AND TEMPORARY STATE RESOLVED**  
Repository: `jbob-coder/Text-rpg-game`  
Branch: `docs/master-game-development-program`  
Audited source HEAD: `5a734b567d99b81f1aafa07ff88539ea0ceb54c7`

Parents:
- `docs/android/ANDROID_CONSUMER_AND_PROJECTION_MAP.md`
- `docs/android/ANDROID_CONSUMER_FIELD_AUDIT_2026-10-04.md`
- `docs/android/APPLICATION_UX_MASTER_PLAN.md`

## 1. Purpose

This audit closes the current-source navigation and temporary/hardcoded presentation-state slice left open by D-026/D-021.

It separates:

- authoritative game state;
- player-safe projected state;
- ViewModel application state;
- local Compose navigation/selection state;
- activity presentation preferences;
- developer-only transient input.

No state in this document is promoted to persistence merely because the UI remembers it.

## 2. Current primary navigation

The production shell defines seven `GameSection` values:

1. `STORY`
2. `CHARACTER`
3. `STATS`
4. `INVENTORY`
5. `QUESTS`
6. `MAP`
7. `MORE`

`BottomPixelNav` iterates `GameSection.entries`, so all seven are current bottom-navigation destinations.

The `MORE` panel also provides:
- a Character/Equipment route;
- a Settings route.

This means Character is currently reachable both directly from the bottom navigation and through More. That is current presentation behavior, not a gameplay rule.

## 3. Settings is an overlay, not a gameplay section

`PixelGameShell` owns:

`settingsOpen: Boolean`

When true, `SettingsPanel` replaces the normal section content within the shell.

The top status bar toggles Settings.

The More panel can also open Settings.

Selecting a bottom-navigation section closes Settings.

Disposition:

**APPLICATION/COMPOSE PRESENTATION STATE.**

Do not put `settingsOpen` into `GameState` or the save schema.

## 4. Scene-change navigation reset

`PixelGameShell` remembers:

- current `section`;
- `settingsOpen`;
- `lastSceneId`.

When projected `snapshot.sceneId` changes:

- navigation returns to `STORY`;
- Settings closes;
- `lastSceneId` updates.

This is a presentation policy built on an authoritative projected scene change.

Disposition:

**KEEP AS PRESENTATION POLICY unless final UX deliberately changes it.**

The UI is not deciding which scene exists; it only changes which panel is displayed after the engine reports a new scene.

## 5. ViewModel application state

Current `GameUiState` fields:

- `bootState`;
- `snapshot`;
- `busy`;
- `travelTransition`;
- `statInspectionPath`;
- `statInspection`;
- `statInspectionBusy`;
- `statInspectionError`.

Classification:

| Field | State class | Durable save? |
| --- | --- | --- |
| `bootState` | application/startup | no |
| `snapshot` | player-safe view of authoritative game state | no separate Android persistence; authoritative state persists through engine save |
| `busy` | application concurrency guard | no |
| `travelTransition` | transient presentation animation | no |
| `statInspectionPath` | transient UI selection/request | no |
| `statInspection` | transient player-safe inspection result | no |
| `statInspectionBusy` | application request state | no |
| `statInspectionError` | temporary presentation/error state | no |

None of these fields authorizes direct mutation of domain state.

## 6. Travel transition ownership

`TravelTransitionUiState` contains:

- token;
- fromLocation;
- toLocation.

It is created only after `engine.travel(locationId)` succeeds and returns a snapshot with a changed projected location.

`finishTravelTransition(token)` removes only the matching transient transition.

Disposition:

**KEEP EPHEMERAL.**

It must not become route authority, save data, or evidence that travel succeeded before the engine confirms it.

## 7. Stats inspection state

The ViewModel tracks the selected inspection path, safe result, busy state and public error.

After successful gameplay mutations such as choose/equip/unequip, the inspection state is cleared.

Disposition:

**KEEP EPHEMERAL PLAYER-SAFE UI STATE.**

Do not persist an inspection result as gameplay truth.

## 8. Local Compose selection state

Current local selections include:

### Inventory

`InventorySection` remembers:
- selected equipment slot ID, keyed by current slot list;
- selected inventory item ID, keyed by current item list.

These selections control detail/focus only.

They do not equip or unequip until the explicit action callback is invoked.

### Map

`MapSection` remembers:
- selected node ID, keyed by current location and projected node list.

The selected node is presentation focus.

Reachability and travel legality still come from projected/domain state.

### Narrative text reveal

`NarrativePanel` remembers:
- number of currently visible characters.

The value is keyed by scene ID/body/text-delay setting and controls only visual text reveal.

### Settings developer input

`SettingsPanel` remembers:
- current cheat-code text entry.

The text field is local input only. Applying a cheat still routes through the engine action.

Disposition for all:

**LOCAL PRESENTATION STATE / DO NOT SAVE AS GAME STATE.**

## 9. Presentation preferences in MainActivity

`MainActivity` currently uses `rememberSaveable` for:

- `autoReadNarration` — default `false`;
- `narrationRate` — default `0.92f`;
- `textDelayMs` — default `0`.

These are application/presentation preferences, not RPG simulation state.

Current limitation:

They are not represented in the engine save schema and should remain outside `GameState`.

Future UX may move durable user preferences to an application settings store, but that is a separate persistence concern from game saves.

## 10. Current boot routing

`TheGameRoot` shows the game shell only when:

- `bootState == BootState.Ready`; and
- a non-null `GameSnapshot` exists.

Otherwise it shows `PixelBootScreen`.

Disposition:

**KEEP APPLICATION BOOT BOUNDARY.**

Gameplay content must not be rendered from a half-started engine session.

## 11. Stable test/preview `GameScreen` surface

A second public composable named `GameScreen` is explicitly documented in source as a stable UI contract used by instrumentation tests and preview clients.

It is not the same as the production `PixelGameShell` navigation state machine.

Its navigation callback uses string labels for:
- Stats;
- Inventory;
- Quests;
- Map;
- More.

It always renders the Story surface as its body.

Disposition:

**KEEP AS TEST/PREVIEW CONTRACT unless deliberately migrated.**

Do not infer final production navigation solely from this compatibility surface.

## 12. Current hardcoded presentation values that are acceptable today

The following are presentation constants, not domain truth:

- `GameSection` labels;
- default navigation destination `STORY`;
- auto-return to Story on scene change;
- narration default `0.92f`;
- text reveal default `0` ms;
- Story wide-layout threshold `720.dp`;
- current panel proportions/heights;
- UI labels such as SETTINGS / MORE;
- slot display-name formatting.

These may be redesigned by final UX work without save migration so long as their underlying domain semantics are preserved.

## 13. Hardcoded state that must not expand into gameplay authority

Future work must not place these decisions in Compose/local UI state:

- route legality;
- quest completion;
- actor presence;
- hidden NPC disposition;
- tactical action legality;
- activity completion;
- class/rank unlocks;
- ability/passive discovery;
- item ownership;
- canonical world discovery.

Those belong to domain state and player-safe projection.

## 14. Current navigation graph

Current production presentation graph:

`BOOT -> STORY`

From the bottom bar:

`STORY <-> CHARACTER <-> STATS <-> INVENTORY <-> QUESTS <-> MAP <-> MORE`

Additional presentation edges:

- any section -> Settings through top status bar;
- More -> Character;
- More -> Settings;
- any authoritative scene change -> Story;
- Settings -> previous section by closing Settings;
- successful travel may show transient travel overlay above the shell without replacing the selected section state itself.

This is a UI graph, not a world-travel graph.

## 15. D-026 / D-021 effect

This closes the **current navigation and temporary/hardcoded UI-state audit**.

Combined with `ANDROID_CONSUMER_FIELD_AUDIT_2026-10-04.md`, current Android documentation now covers:

- GameSnapshot fields;
- action paths;
- screen consumers;
- direct major catalog dependencies;
- test-source surfaces;
- production navigation;
- ViewModel ephemeral state;
- local Compose selections;
- application presentation preferences.

Still open:
- future target projection schemas that do not yet exist;
- per-entry code-only asset consumer/zero-consumer proof beyond the completed 24-raster audit;
- implementation/equivalence evidence after future migrations;
- final UX/navigation redesign decisions.

## 16. Verification boundary

No Kotlin/Python/content/save/runtime file changed.

No tests or builds were executed.

This is exact-source documentation at the recorded audited HEAD.
