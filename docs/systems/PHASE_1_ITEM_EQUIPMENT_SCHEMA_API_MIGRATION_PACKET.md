# THE GAME — Phase 1 Item / Equipment Schema & API Migration Packet

Status: **APPROVED MIGRATION DESIGN / D-032 ITEMS-ECONOMY CHILD / IMPLEMENTATION NOT STARTED**  
Repository: `jbob-coder/Text-rpg-game`  
Authority branch: `docs/master-game-development-program`  
Task: D-063  
Source inspection HEAD: `cc94a62a5ddac38f3c747d0791ae9b0173c5ef60`

Parents:
- `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`
- `docs/systems/ITEM_ECONOMY_LOOT_MASTER_PLAN.md`
- `docs/systems/ITEM_RECORD_CATALOG_STANDARD.md`
- `docs/systems/INVENTORY_STACK_CONTAINER_STANDARD.md`
- `docs/systems/EQUIPMENT_SLOT_LOADOUT_STANDARD.md`
- `docs/systems/GATE_TWELVE_PHASE1_ITEM_EQUIPMENT_PACKET.md`
- `docs/systems/SAVE_AND_CONTENT_MIGRATION_MASTER_PLAN.md`
- `docs/PHASE_1_SOLO_PLAYABLE_PARALLEL_TRACK.md`

## 1. Purpose

Map the current Gate Twelve inventory/equipment proof onto the Python state, content registry, save contract, player-safe bridge, Kotlin DTOs and Android actions without forcing unfinished economy systems into Phase 1.

This closes the items/economy migration-design child of D-032. It does not implement currency, vendors, crafting, durability, encumbrance, random loot, or item instances.

## 2. Current authoritative state

Phase 1 already has sufficient durable owners:

- `GameState.inventory`: `item_id -> integer quantity`;
- `GameState.equipment`: `slot -> equipped item record`;
- static item definitions: `content.registries["items"]`;
- equipment legality/modifiers: Python `equipment.py` plus modifier validation;
- authored acquisition/consumption: scene effects through `RulesEngine.choose()`;
- persistence: existing schema-v1 `inventory` and `equipment` fields;
- player-safe inventory/equipment: `AndroidGameSession._inventory_view_for()`;
- equipment actions: `AndroidGameSession.equip()` / `unequip()`;
- Kotlin presentation: typed `GameInventoryItem`, `GameEquipmentSlot`, `GameInventory`.

Do not add a competing top-level item/economy state owner for the Phase 1 proof.

## 3. Stable Phase 1 item set

Current proof IDs:

- `ITEM_MAINTENANCE_SEAL`;
- `ITEM_DEAD_RELAY`;
- `ITEM_DEPOT_JACKET`;
- `ITEM_WORK_GLOVES`;
- `ITEM_SIGNAL_RING`;
- `ITEM_COURIER_NECKTAG`.

Current starting inventory contains one each of every ID above except `ITEM_DEAD_RELAY`.

`TAKE_DEAD_RELAY` acquires the Dead Relay.

`USE_MAINTENANCE_SEAL` requires one Maintenance Seal and consumes one through the authored route.

These stable IDs must not be casually renamed or reused.

## 4. Current equipment authority

Current `DEFAULT_SLOTS` remain authoritative for Phase 1:

- head;
- body;
- hands;
- legs;
- feet;
- main_hand;
- off_hand;
- ring_1;
- ring_2;
- neck;
- accessory_1;
- accessory_2.

`equip_item()` currently validates, before commit:

- item mapping and item ID;
- supported slot;
- possession when `consume_inventory=True`;
- modifier paths;
- base/permanent attribute requirements;
- base/permanent skill requirements;
- set ID;
- tags;
- passive-perk IDs.

The base/permanent requirement rule is retained. Equipped bonuses must not qualify other equipment and create circular/order-dependent legality.

The equipped record currently owns item ID, slot, quality, modifiers, tags, set ID, optional active ability, passive perks and source.

## 5. Mutation/API boundaries

### Authored story items

Use:

`Android request -> AndroidGameSession.choose() -> RulesEngine.choose() -> authored inventory effect -> GameState`

Examples:
- `TAKE_DEAD_RELAY`;
- `USE_MAINTENANCE_SEAL`.

`RulesEngine.choose()` snapshots the complete state and restores it if any effect or later choice step fails. Keep story-item mutation inside that transaction.

### Equipment

Use:

`Android request -> AndroidGameSession.equip/unequip -> equipment.py -> GameState`

Current bridge behavior is already transactionally bounded:

- deep snapshot before mutation;
- equip consumes one carried unit;
- occupied slot replacement returns the previous item to inventory;
- unequip returns one item;
- history records the change;
- any rule/type/value failure restores the prior state.

Do not add generic client APIs such as `setInventory`, `setQuantity`, `setEquipment` or raw state mutation.

## 6. Save-schema decision

Keep save schema v1 for Phase 1.

Reason:
- `inventory` and `equipment` already exist as durable top-level fields;
- the selected proof needs item-type quantities plus current slot records only;
- item instances, durability, containers, currency ledgers and vendor state are not Phase 1 requirements.

Any future incompatible item-instance/container/economy representation requires an explicit migration instead of silently repurposing the current fields.

## 7. Current content-validation strengths

Current validators already:

- restrict registry categories;
- validate stable registry IDs;
- require registry metadata to be objects;
- cross-reference `item_min.item_id` against the item registry;
- cross-reference authored `inventory` effect item IDs;
- cross-reference power item requirements;
- reject initial inventory IDs absent from the item registry.

Therefore the migration should extend the existing registry/validator rather than create another item catalog.

## 8. Current content-validation gaps

Direct source inspection identifies four bounded gaps:

1. `item_min.quantity` is not statically validated as a positive non-boolean integer.
2. authored `inventory` effect `quantity` is not statically validated as a non-zero integer.
3. item registry records are not comprehensively preflighted for current item semantics such as slot, quality, modifiers, requirements and tag shape.
4. initial inventory IDs are cross-referenced, but each initial quantity is not validated there as a positive non-boolean integer.

D-067 should add the smallest shared validators required by the current six-item proof. Do not use these gaps as justification for implementing the entire future economy schema.

## 9. Raw inventory-effect hardening

The current `inventory` effect directly computes:

`state.inventory[item_id] = current + delta`

and removes the key when the result is nonpositive.

Inside the current authored choices, the outer choice snapshot provides rollback and `USE_MAINTENANCE_SEAL` has an `item_min` possession gate. However the low-level effect does not independently enforce current quantity/delta shape or sufficient quantity.

D-067 should introduce or reuse one authoritative bounded inventory mutation helper that:

- requires non-empty stable item ID;
- requires integer/non-boolean delta;
- rejects zero delta in authored content;
- validates current quantity;
- prevents invalid underflow unless an explicitly designed operation allows it;
- removes zero quantity cleanly;
- is used by authored inventory effects.

Kotlin must not duplicate this logic.

## 10. Nested save-state validation gap

`loads_state()` validates schema version, top-level fields and container shape, but it does not fully validate every nested inventory quantity or equipped record before returning the state.

The current Android projection defensively skips invalid/nonpositive inventory quantities and treats malformed equipment records as empty slots. That is useful presentation hardening but may hide corrupt durable state.

D-067 should add bounded nested validation:

### Inventory

- item ID is non-empty text;
- quantity is integer, not boolean;
- quantity > 0;
- item ID resolves against content registry before a loaded state becomes live.

### Equipment

- slot is supported;
- record is an object;
- record slot matches its owner key where applicable;
- item ID is non-empty;
- referenced item exists when content context is available;
- item definition slot is compatible;
- persisted modifier/requirement fields are valid where retained.

Keep structural save validation engine-side. Registry-aware validation may occur when the loaded candidate is checked against the current content before session replacement.

## 11. Atomicity requirements

D-067 must prove:

- failed equip leaves inventory/equipment unchanged;
- failed replacement neither loses the old item nor consumes the new item;
- failed unequip leaves both slot and inventory unchanged;
- malformed story-item mutation cannot partially commit the rest of a choice;
- invalid loaded item/equipment state never replaces the current Android session;
- save failure cannot mutate authoritative item state.

The existing full-state snapshot rollback is the preferred outer bridge/choice boundary.

## 12. Player-safe projection

Current Python inventory projection is already appropriately bounded.

Inventory entries expose:
- ID;
- display name;
- quantity;
- equippable;
- legal slot;
- quality when present.

Equipment entries expose:
- slot;
- equipped state;
- item ID/name/quality when equipped.

Raw modifier maps are not exposed in inventory/equipment DTOs.

Player-safe equipment contributions are obtained through the status explanation pipeline, which preserves engine ownership of calculations.

Keep this separation.

## 13. Android/Kotlin status

Current Kotlin already has typed item/equipment consumption:

- `GameInventoryItem`;
- `GameEquipmentSlot`;
- `GameInventory`;
- `BridgeSnapshotMapper` mapping for inventory/equipment;
- Character/Inventory presentation using projected state;
- equip/unequip requests delegated to the engine.

Unlike D-061's ability mapping gap, D-063 does not require a new Android item DTO architecture.

D-067 should verify the current mapper/action/render path on exact HEAD rather than reimplement it.

## 14. Selected D-067 proof route

Use the existing runtime/content loop:

1. verify exact starting inventory;
2. inspect player-safe inventory;
3. equip `ITEM_DEPOT_JACKET` or another current equippable item;
4. prove carried quantity decrements;
5. prove correct slot changes;
6. prove the authoritative status contribution changes;
7. unequip or replace and prove exact return behavior;
8. execute `TAKE_DEAD_RELAY`;
9. execute the legal `USE_MAINTENANCE_SEAL` route and prove consumption;
10. save;
11. load;
12. prove inventory/equipment/story-item state and relevant projection survive.

No new reward item is needed to satisfy Phase 1.

## 15. D-067 test map

Use/extend:

- `tests/test_equipment.py`;
- `tests/test_validation.py`;
- `tests/test_content.py`;
- `tests/test_persistence.py`;
- `tests/test_android_bridge.py`;
- `tests/test_save_resume_routes.py`.

Required focused coverage:

1. current six item definitions pass strengthened validation;
2. invalid slot/modifier/requirement fails content validation;
3. invalid `item_min` quantity fails;
4. invalid inventory-effect delta fails;
5. invalid initial inventory quantity fails content load;
6. malformed nested saved inventory/equipment is rejected before live replacement;
7. equip consumes exactly one item;
8. occupied-slot replacement returns the prior item exactly once;
9. invalid equip has zero partial mutation;
10. unequip returns exactly one item and clears exactly one slot;
11. equipment modifier appears through player-safe status projection;
12. Dead Relay acquisition and Maintenance Seal consumption follow authored choices;
13. save/load preserves the selected proof state;
14. failed Android load keeps the previous live state.

Android/JVM/UI evidence should additionally confirm that typed quantity/slot/quality mapping and equip/unequip delegation work without moving legality or stat arithmetic into Compose.

## 16. Economy boundary

D-063 does **not** authorize or require Phase 1 implementation of:

- currency;
- prices;
- vendors/vendor funds;
- barter/taxes;
- regional pricing;
- crafting;
- durability/repair;
- encumbrance;
- random modifiers;
- item-instance serialization;
- resource-node markets;
- theft/ownership economy.

Those remain separate V07/world/economy work when their state/contracts are ready.

## 17. Stable-ID migration rule

For any future item rename:

old ID -> new ID -> explicit migration of inventory keys, equipped records, content/quest refs and visual mappings -> legacy fixture -> validation -> save round trip.

For any slot migration, explicitly map old slot to new slot and define collision behavior. Never silently drop equipped gear.

## 18. Rollback boundary

The intended D-067 migration is additive hardening.

If it must be reverted:
- existing schema-v1 inventory/equipment remains;
- current stable item IDs remain;
- no save rewrite occurs;
- current Android item/equipment DTOs remain valid.

No destructive migration is authorized by this packet.

## 19. D-032 synchronization result

This packet completes the **items/economy migration child** of D-032.

At the source inspection HEAD, the master register already records progression, social, combat and persistent-adversary children as complete. Therefore adding this packet satisfies the final documented migration child.

D-032 may be marked **DONE** when the master register is synchronized to include this packet and no newer conflicting migration authority has appeared.

D-032 completion means the migration-design packet set is complete. It does not mean the corresponding runtime implementation tasks are complete.

## 20. Phase 1 impact

Requirement 6 moves to:

**CURRENT RUNTIME FOUNDATION EXISTS / MIGRATION-READY / EXACT-HEAD INTEGRATED PROOF PENDING.**

D-067 becomes dependency-eligible after board synchronization.

D-063 itself does not prove requirement 6.

## 21. Verification boundary

This D-063 packet is source-grounded documentation work.

Inspected:
- current V07 masters/standards/proof packet;
- current vertical-slice item registry/choices;
- `core.py`;
- `equipment.py`;
- `validation.py`;
- `content.py`;
- `persistence.py`;
- `android_bridge.py`;
- current Kotlin inventory DTO/mapper/consumer surface;
- current item/equipment/content/persistence/bridge tests.

No runtime source was changed by D-063.

No claim is made that:
- full Python tests were executed;
- Android JVM/build tests were executed;
- physical device/APK was tested;
- economy runtime exists;
- D-067 is complete.

## 22. Next action

After synchronization:

1. mark D-032 DONE if the live register still confirms all other children complete;
2. mark D-063 DONE;
3. promote D-067 from BLOCKED to READY;
4. append the Nodus D-063 Brag Card;
5. refresh newly eligible work;
6. take the highest-ranked different READY task not already claimed;
7. skip D-063-B while higher-priority P0 primary work is READY.
