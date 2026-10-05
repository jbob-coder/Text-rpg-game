# THE GAME — Phase 1 Items / Equipment / Economy Schema & API Migration Packet

Status: **APPROVED MIGRATION DESIGN / D-032 ITEMS-ECONOMY CHILD / IMPLEMENTATION NOT STARTED**
Repository: `jbob-coder/Text-rpg-game`
Source inspection HEAD: `db0d82e0fe5e9cbba0aa72d2578fd0e990f25f7d`
Claim HEAD: `96911ed86843b38ac4f6af54fddcb64a03f4afc7`
Parents:
- `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`
- `docs/systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md`
- `docs/systems/INVENTORY_STACK_CONTAINER_STANDARD.md`
- `docs/systems/EQUIPMENT_SLOT_LOADOUT_STANDARD.md`
- `docs/systems/GATE_TWELVE_PHASE1_ITEM_EQUIPMENT_PACKET.md`
- `docs/systems/SAVE_AND_CONTENT_MIGRATION_MASTER_PLAN.md`
- `docs/THE_GAME_MASTER_TASK_REGISTER.md`

## 1. Purpose

This packet closes the items/economy migration-design child of D-032.

It maps the current Gate Twelve Phase 1 item/equipment proof onto the existing Python state, content registry, authoritative mutation APIs, save schema, player-safe Android projection, Kotlin DTOs, ViewModel actions, and Compose inventory surface.

The design deliberately does **not** force currency, vendors, crafting, durability, encumbrance, item-instance serialization, random loot, or a new economy owner into Phase 1.

This packet does not claim D-067 is implemented or verified.

## 2. Current authoritative state

At the inspected source HEAD, durable item state already has two owners inside `GameState`:

### Inventory

`state.inventory: Dict[item_id, int]`

Current semantics:
- stable item ID -> integer stack quantity;
- zero/nonpositive runtime quantity is treated as absent by normal story mutation and player projection;
- story choices mutate this map through the `inventory` effect;
- equipping may consume one carried unit;
- unequipping returns one unit to carried inventory.

### Equipment

`state.equipment: Dict[slot, equipment_record]`

Current equipped record written by `equipment.equip_item()` contains:
- `item_id`;
- `slot`;
- `quality`;
- validated `modifiers`;
- `tags`;
- `set_id`;
- `active_ability`;
- `passive_perks`;
- `source`.

The current authoritative slot namespace is:

- `head`;
- `body`;
- `hands`;
- `legs`;
- `feet`;
- `main_hand`;
- `off_hand`;
- `ring_1`;
- `ring_2`;
- `neck`;
- `accessory_1`;
- `accessory_2`.

These structures are already part of `GameState.snapshot()` and therefore save schema v1.

## 3. Current item-definition owner

Current authored item definitions live in:

`registries.items[ITEM_ID]`

The current Gate Twelve registry contains exactly these six relevant item types:

| ID | Current role | Slot | Quality |
| --- | --- | --- | --- |
| `ITEM_MAINTENANCE_SEAL` | story/key-like consumable | — | — |
| `ITEM_DEAD_RELAY` | quest/story object | — | — |
| `ITEM_DEPOT_JACKET` | equipment | `body` | `standard` |
| `ITEM_WORK_GLOVES` | equipment | `hands` | `standard` |
| `ITEM_SIGNAL_RING` | equipment | `ring_1` | `uncommon` |
| `ITEM_COURIER_NECKTAG` | equipment | `neck` | `standard` |

Current starting inventory is:

- `ITEM_MAINTENANCE_SEAL x1`;
- `ITEM_DEPOT_JACKET x1`;
- `ITEM_WORK_GLOVES x1`;
- `ITEM_SIGNAL_RING x1`;
- `ITEM_COURIER_NECKTAG x1`.

Initial equipment is not separately authored in the current vertical-slice state; these four wearable items begin carried and may be equipped through the authoritative equip action.

## 4. Current Phase 1 story-item mutations

The exact live story-item graph is small.

### Relay acquisition

Scene:
- `OPENING_DEPOT_BLACKOUT`

Choice:
- `TAKE_DEAD_RELAY`

Effect:
- `inventory ITEM_DEAD_RELAY +1`

### Maintenance-seal consumption

Scene:
- `OPENING_RELAY_CASING`

Choice:
- `USE_MAINTENANCE_SEAL`

Gate:
- `item_min ITEM_MAINTENANCE_SEAL quantity 1`

Effect:
- `inventory ITEM_MAINTENANCE_SEAL -1`

The registry cross-reference validator already requires item IDs used by `item_min` and `inventory` effects to exist in `registries.items`.

## 5. Core migration decision

**Keep the current flat inventory and slot-keyed equipment model for Phase 1.**

Do not introduce:
- item instances;
- nested player containers;
- currency balances;
- vendor stock;
- crafting recipes;
- durability/repair state;
- encumbrance;
- generalized ownership objects;
- random-affix state;
- separate Android item authority.

Reason:
- requirement #6 can already be satisfied by obtain/use/equip/unequip/save/load;
- the current schema is sufficient for the six live item types;
- the existing Android surface already consumes typed player-safe inventory/equipment DTOs;
- the broader economy standards explicitly defer currency and numeric pricing decisions;
- changing save shape before a gameplay need exists would create migration cost with no Phase 1 benefit.

A future item-instance/container/economy migration remains separate and must use an explicit save version if durable representation changes.

## 6. Stable-ID rules

For D-067 and the Gate Twelve proof:

- preserve every item ID in section 3;
- preserve current slot IDs;
- preserve story choice IDs in section 4;
- preserve `registries.items` as definition ownership for current item metadata;
- do not encode display names as state identity;
- do not repurpose an existing item ID for a different item meaning;
- do not rename a slot without an explicit equipment/save migration.

If a later migration changes an item ID:
1. retain old/new IDs in a mapping;
2. migrate inventory keys;
3. migrate equipped `item_id` values;
4. update content references;
5. preserve story/quest semantics;
6. test old-save -> new-save round trip.

## 7. Equipment mutation boundary

The current authoritative equip path is:

`Compose -> GameViewModel.equip(item_id) -> GameEngine.equip(item_id) -> PythonGameEngine -> AndroidGameSession.equip(item_id) -> equipment.equip_item(... consume_inventory=True) -> GameState`

`AndroidGameSession.equip()` currently:
1. resolves the item from `registries.items`;
2. snapshots full authoritative state;
3. calls `equip_item()`;
4. consumes one inventory item only after preflight validation inside the equip helper;
5. if replacing an occupied slot, returns the previous equipped item to inventory;
6. appends one `equipment_changed` history event;
7. returns a new player-safe view;
8. restores the snapshot on rule/type/value failure.

Current `unequip(slot)`:
1. snapshots state;
2. validates the slot and equipped record;
3. removes the equipped record;
4. returns one item to inventory;
5. appends one history event;
6. returns updated projection;
7. rolls back on failure.

Android must never calculate:
- equipment requirements;
- modifier values;
- set bonuses;
- slot replacement ownership;
- resulting effective stats.

## 8. Equipment legality

`equipment.equip_item()` currently validates before commit:

- item definition is an object;
- stable caller-supplied `item_id` is non-empty;
- slot belongs to `DEFAULT_SLOTS`;
- carried quantity exists when `consume_inventory=True`;
- modifier paths/values are valid;
- attribute requirement IDs/values are valid;
- skill requirement IDs/values are valid;
- requirement checks use **base/permanent values**, not equipment-modified effective values;
- `set_id` shape;
- tags;
- passive-perk ID list shape.

The base-stat requirement rule is preserved. One equipped item must not qualify another and create order-dependent/circular loadouts.

Phase 1 does not need two-hand, linked-slot, ammo, durability, or item-instance conflict rules.

## 9. Story-item mutation boundary

Playable story acquisition/consumption remains:

`Android choice -> AndroidGameSession.choose() -> RulesEngine.choose() -> authored inventory effect -> state.inventory`

`RulesEngine.choose()` snapshots the entire GameState before applying effects, time, turn, scene and history. Any exception restores that snapshot.

This means the Maintenance Seal and Dead Relay story path already has a transaction boundary.

Do not add client-side:
- `giveItem`;
- `consumeItem`;
- raw inventory quantity setters;
- generic item mutation endpoints

for ordinary authored play.

Developer cheats remain explicitly whitelisted and are not normal gameplay APIs.

## 10. Save / migration decision

**D-067 should remain on save schema v1.**

Current save already persists:
- `inventory`;
- `equipment`;
- story flags/knowledge relevant to relay visual state;
- history;
- all other authoritative GameState fields.

No new top-level save field is required for the selected Phase 1 proof.

However, the current structural save validator only verifies that `inventory` and `equipment` are mutable mappings. It does not fully validate their nested shape.

D-067 should harden the schema-v1 nested state contract without changing its representation:

### Inventory validation

For every persisted inventory entry:
- item ID is non-empty stable text;
- quantity is an integer;
- booleans are rejected;
- quantity is strictly positive for stored entries;
- zero is normalized away by mutation code rather than persisted;
- negative quantities are rejected.

When content context is available, item IDs should also resolve to the loaded item registry.

### Equipment validation

For every persisted equipment entry:
- slot is one of `DEFAULT_SLOTS`;
- record is an object;
- record `slot` equals its map key;
- `item_id` is non-empty stable text;
- quality is text when present;
- modifiers pass the existing modifier validator;
- tags/passive-perks have valid list shape;
- set ID is valid when present.

When content context is available, equipped item ID should resolve to an item definition and the definition/record slot mismatch should be rejected.

This is validation hardening, not schema v2.

## 11. Content-validation gap

Current `validate_registries()` verifies:
- registry category;
- stable uppercase item ID;
- item metadata is an object.

Current cross-reference validation verifies:
- `item_min` references a known item ID;
- `inventory` effects reference a known item ID;
- power item requirements reference known item IDs.

But content loading does **not** currently validate the full equipment item definition at registry load time.

A malformed equippable item can therefore survive content loading and fail only when equip is attempted.

D-067 should add a focused item-definition validator for the current schema, reusing existing validators rather than duplicating rules.

For item definitions that contain equipment fields, validate:
- slot;
- quality type when present;
- modifiers;
- requirements;
- tags;
- set ID;
- passive perks;
- source text when present.

Non-equipment story items remain valid with only label/metadata.

Also harden authored `inventory` effect quantity:
- integer;
- boolean rejected;
- nonzero;
- the current signed-delta semantics remain valid because `-1` is required by `USE_MAINTENANCE_SEAL`.

And harden `item_min.quantity`:
- positive integer;
- boolean rejected.

## 12. Player-safe Python projection

`AndroidGameSession._inventory_view_for()` currently projects only:

Inventory item:
- ID;
- display name;
- quantity;
- equippable;
- slot;
- quality.

Equipment slot:
- slot;
- equipped;
- item ID when equipped;
- display name when equipped;
- quality when equipped.

It deliberately does not expose raw item modifiers.

Known stat impact is available through the separate player-safe status/inspection surface, which converts modifier provenance into allowed display contributions.

Preserve this separation:
- inventory view answers **what the player carries/wears**;
- status inspection answers **known effective-stat contribution**;
- raw authored modifier maps are not sent as inventory implementation data.

`ITEM_DEAD_RELAY` visual state remains a separate player-safe visual projection derived from possession plus allowed story state. Do not expose hidden relay flags merely to render the item.

## 13. Android DTO and mapping status

Unlike the progression migration, the current Android inventory DTO boundary already exists:

- `GameInventoryItem`;
- `GameEquipmentSlot`;
- `GameInventory`;
- `GameSnapshot.inventory`.

`BridgeSnapshotMapper` already maps:
- item ID;
- name;
- quantity;
- equippable;
- slot;
- quality;
- equipment slot;
- equipped state;
- equipped item ID/name/quality.

`GameEngine` already exposes:
- `equip(itemId)`;
- `unequip(slot)`.

`GameViewModel` delegates those actions to the engine and replaces its snapshot only from the authoritative returned result.

`GameScreen` already renders:
- equipment slots;
- carried stacks;
- item quantity;
- quality;
- equippable slot;
- equip button;
- unequip button;
- player avatar equipment presentation.

Therefore D-067 does **not** need a new Android inventory architecture.

It needs exact-head proof and repairs only where tests expose a gap.

## 14. Android mapper hardening

D-067 should verify and, where absent, add strict mapper tests for:

- positive item quantity;
- nonblank item ID/name;
- supported player-facing equipment slot IDs;
- equipped=false cannot smuggle item identity fields that UI treats as equipped;
- equipped=true requires a nonblank item ID;
- optional quality remains text-only;
- malformed inventory/equipment payload cannot silently become a misleading UI state.

Do not push Python equipment-rule validation into Kotlin. Mapper validation protects transport shape only.

## 15. Phase 1 proof route

The D-067 proof should use the exact current loop, not invent a reward.

Minimum sequence:

1. create current vertical-slice session;
2. assert exact starting five carried item stacks;
3. inspect player-safe inventory projection;
4. equip `ITEM_DEPOT_JACKET`;
5. prove carried quantity decreases;
6. prove `body` equipment slot points to the jacket;
7. prove effective Endurance changes through authoritative modifier calculation;
8. inspect the player-safe stat contribution;
9. unequip the jacket and prove quantity/stat restore;
10. equip one item and save;
11. load and prove carried/equipped state + effective stat survive;
12. choose `TAKE_DEAD_RELAY` and prove relay acquisition/projection;
13. progress to `USE_MAINTENANCE_SEAL`, prove its item gate, consume it, and prove no negative/duplicate stack remains;
14. save/load the post-story state;
15. map the resulting inventory/equipment payload through Android DTOs;
16. verify the existing Compose inventory controls are connected to ViewModel equip/unequip actions.

This satisfies Phase 1 requirement #6 without a currency or loot-system dependency.

## 16. Failure and atomicity tests

D-067 should add/retain tests proving:

- equipping a missing item fails with no mutation;
- equipping an item with unmet base requirement fails with no mutation;
- malformed item definition fails before inventory is consumed;
- invalid slot fails with no mutation;
- replacement does not duplicate or destroy the previous item;
- failed equip bridge action restores the whole snapshot;
- unequipping an empty/invalid slot does not mutate state;
- failed story choice does not partially consume an item;
- consuming the final Maintenance Seal removes the key instead of persisting zero;
- negative inventory state is rejected by persistence/state validation;
- malformed persisted equipment is rejected;
- save/load preserves a valid equipped record.

These are especially important because current generic persistence validation is shallower than the runtime equip validator.

## 17. Current test/evidence baseline

Existing source tests already cover substantial pieces:

### `tests/test_equipment.py`
- requirements;
- set bonuses;
- invalid modifiers;
- unknown requirement IDs;
- finite numeric requirements;
- inventory preflight;
- corrupt source stat rejection;
- tags/set-ID shape;
- supported ring/neck/accessory slots.

### `tests/test_android_bridge.py`
- player-safe inventory projection;
- no raw modifiers in inventory projection;
- equipment contribution through status inspection;
- transactional equip + unequip with quantity restoration;
- generic save/load session projection;
- relay player-safe visual state.

These tests are useful baseline coverage, but D-067 still needs one integrated exact-head Phase 1 item/equipment/story/save/Android proof rather than treating separate tests as equivalent to requirement #6 closure.

## 18. Broader economy compatibility

No current Phase 1 runtime migration is required for:
- currency;
- pricing;
- vendors;
- barter;
- wages;
- taxes;
- regional supply;
- ownership/crime;
- crafting;
- durability;
- repairs;
- resource nodes;
- random loot.

The approved V07 documents remain target architecture.

If a later economy implementation arrives:
- authoritative pricing/stock/state remains Python/game state;
- vendor private state must not leak through Android;
- transactions must be atomic;
- durable representation changes must be explicitly migrated.

D-063 must not turn those target contracts into claims of current implementation.

## 19. Rollback boundary

The selected migration path is reversible because it keeps the current durable shape.

If D-067 hardening must be reverted:
- validation helpers/tests can be reverted;
- existing `inventory` and `equipment` save fields remain readable;
- current item IDs/slots remain unchanged;
- Android DTO shape remains the same;
- no save rewrite is required.

Do not solve a validation bug by silently dropping corrupt inventory/equipment data. Reject it explicitly.

## 20. Implementation order for D-067

1. fetch exact current HEAD;
2. add nested inventory/equipment state validation with focused tests;
3. add current item-definition + item-effect quantity validation with content tests;
4. preserve current valid vertical-slice content unchanged unless a real defect is found;
5. add invalid-equip/replace/rollback regressions;
6. add exact Phase 1 story-item + equipment save/load regression;
7. add/extend Android mapper contract tests;
8. verify ViewModel/Compose wiring without moving rules into UI;
9. run focused Python suites;
10. run Android JVM tests for changed mapper/consumer code;
11. if instrumentation is available, verify the equip/unequip UI path;
12. synchronize Phase 1 requirement #6 only from observed exact-head results.

## 21. Verification expectations

A D-067 completion record should distinguish:

- Python unit result;
- Python integration result;
- exact source HEAD;
- save/load fixture result;
- Android JVM mapper/ViewModel result;
- Android instrumentation result if actually run;
- emulator vs physical-device evidence;
- anything not executed.

Python tests do not prove Android UI behavior.

Android JVM tests do not prove physical-device behavior.

File existence does not prove requirement #6.

## 22. D-032 result

The items/economy migration child is implementation-ready.

For Phase 1:
- keep flat inventory;
- keep slot-keyed equipment;
- keep schema v1;
- preserve stable item/slot IDs;
- keep authoritative mutation in Python;
- keep existing typed Android inventory/equipment DTOs;
- harden nested save/content validation;
- prove the existing current item/equipment/story loop exact-head in D-067.

The full economy remains a later domain implementation and is not a blocker for Gate Twelve Phase 1.


## 23. Reconciliation note

A concurrent D-063 work stream briefly created the near-duplicate path `PHASE_1_ITEM_EQUIPMENT_SCHEMA_API_MIGRATION_PACKET.md`.

The canonical packet is this file: `PHASE_1_ITEMS_ECONOMY_SCHEMA_API_MIGRATION_PACKET.md`.

Unique useful details from the duplicate are retained here:

- initial inventory quantities must be validated as positive non-boolean integers during content loading, not only item IDs cross-referenced;
- the authored signed `inventory` effect should use one bounded engine-owned mutation helper so current quantity, integer delta, zero-delta rejection and underflow rules are validated consistently;
- Kotlin must continue to consume the resulting player-safe projection rather than duplicate those mutation rules.

The duplicate file is removed after this reconciliation so D-032 has one items/economy child authority.
