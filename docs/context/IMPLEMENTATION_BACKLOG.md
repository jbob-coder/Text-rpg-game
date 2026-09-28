# Project Implementation Backlog

Status: [DESIGNED] ACTIVE BACKLOG

Purpose: maintain a durable implementation task list for major work that should survive chat transitions. This file does not imply that listed work is implemented.

## Stage 3 blocker — current promotion gate

- [ ] TASK-STAGE3-001 — Obtain an authorized exact runtime for integration/rules-ability-v6-reconcile.
- [ ] TASK-STAGE3-002 — Execute PYTHONPATH=src python -m unittest discover -s tests -v against exact V6 candidate SHA.
- [ ] TASK-STAGE3-003 — Fix only observed V6 runtime regressions.
- [ ] TASK-STAGE3-004 — Re-run the complete suite until green.
- [ ] TASK-STAGE3-005 — Verify save/resume, hidden-data/status, and transactional boundaries on the exact candidate.
- [ ] TASK-STAGE3-006 — Record exact SHA, commands, and observed results before promotion.
- [ ] TASK-STAGE3-007 — Repair stale README/status documentation so branch/test claims match the verified candidate.
- [ ] TASK-STAGE3-008 — Canonicalize/promote only after the exact runtime gate is satisfied.

The medieval/crystal work below is blocked from V6 integration by TASK-STAGE3-001..008, but design/prototype work may be isolated if it cannot be confused with the promotion candidate.

## Epic A — Medieval/crystal world contract

- [ ] TASK-CRYSTAL-001 — Define stable registries for mine crystals and beast heart crystals.
- [ ] TASK-CRYSTAL-002 — Define CrystalDefinition and CrystalInstance contracts.
- [ ] TASK-CRYSTAL-003 — Define crystal grade, purity, size, resonance, stability, capacity, recharge, affinity, and provenance fields.
- [ ] TASK-CRYSTAL-004 — Define appraisal visibility: unknown / partial / known.
- [ ] TASK-CRYSTAL-005 — Define mine-deposit generation and extraction quality inputs.
- [ ] TASK-CRYSTAL-006 — Define beast-heart crystal maturation and species/evolution inheritance.
- [ ] TASK-CRYSTAL-007 — Define crystal harvesting damage and the heart/core loot-risk tradeoff.
- [ ] TASK-CRYSTAL-008 — Add deterministic validation for incompatible/invalid crystal metadata.
- [ ] TASK-CRYSTAL-009 — Add save/load representation and migration plan for crystal instances.
- [ ] TASK-CRYSTAL-010 — Add regression tests for crystal provenance, strict numerics, and persistence.

## Epic B — Weapon and equipment system expansion

- [ ] TASK-EQUIP-001 — Freeze weapon-family registry and stable IDs.
- [ ] TASK-EQUIP-002 — Define WeaponDefinition and EquipmentInstance contracts.
- [ ] TASK-EQUIP-003 — Add weight, reach, handling, balance, momentum, guard, recovery, stamina burden, and durability.
- [ ] TASK-EQUIP-004 — Add cutting / piercing / blunt damage profiles.
- [ ] TASK-EQUIP-005 — Add penetration and armor-interaction tags.
- [ ] TASK-EQUIP-006 — Add minimum/optimal range and targeting-access tags.
- [ ] TASK-EQUIP-007 — Define armor body coverage internally while keeping player slots readable.
- [ ] TASK-EQUIP-008 — Add cut/pierce/blunt resistance and durability per armor piece.
- [ ] TASK-EQUIP-009 — Add equipment burden, flexibility, noise, and fatigue tradeoffs.
- [ ] TASK-EQUIP-010 — Add crystal socket/channel/fusion metadata.
- [ ] TASK-EQUIP-011 — Define replaceable socket vs permanent fusion rules.
- [ ] TASK-EQUIP-012 — Define repair, degradation, and field-maintenance rules.
- [ ] TASK-EQUIP-013 — Preserve effective-stat no-double-counting invariants.
- [ ] TASK-EQUIP-014 — Add player-safe equipment inspection/provenance projection.
- [ ] TASK-EQUIP-015 — Add automated equipment/crystal integration tests.

## Epic C — Forging and crafting

- [ ] TASK-FORGE-001 — Define smithing/crystalcraft skill responsibilities without prematurely changing the current stat schema.
- [ ] TASK-FORGE-002 — Define staged forge workflow: base material -> shaping -> temper/finish -> crystal housing -> crystal integration -> stabilization -> inspection.
- [ ] TASK-FORGE-003 — Define material-quality and forge-quality calculation inputs.
- [ ] TASK-FORGE-004 — Define compatibility checks between weapon/material/crystal traits.
- [ ] TASK-FORGE-005 — Define integration failure, instability, repair, and salvage outcomes.
- [ ] TASK-FORGE-006 — Ensure crafting consumes time/resources and cannot grant trivial permanent progression.
- [ ] TASK-FORGE-007 — Add deterministic forge outcome provenance for UI/debug.
- [ ] TASK-FORGE-008 — Add one end-to-end forge vertical slice with mine crystal.
- [ ] TASK-FORGE-009 — Add one end-to-end forge vertical slice with beast core.
- [ ] TASK-FORGE-010 — Add save/resume regression coverage during multi-stage crafting.

## Epic D — Positional combat and target zones

- [ ] TASK-COMBAT-001 — Define CombatState contract.
- [ ] TASK-COMBAT-002 — Define range bands: grapple / close / reach / ranged.
- [ ] TASK-COMBAT-003 — Define relative facing: front / left flank / right flank / rear.
- [ ] TASK-COMBAT-004 — Define elevation and posture states.
- [ ] TASK-COMBAT-005 — Define BodyZoneDefinition and BodyZoneRuntimeState.
- [ ] TASK-COMBAT-006 — Define target-zone availability query as an authoritative rules API.
- [ ] TASK-COMBAT-007 — Enforce weapon reach/family restrictions on targetability.
- [ ] TASK-COMBAT-008 — Enforce cover/terrain/obstruction restrictions on targetability.
- [ ] TASK-COMBAT-009 — Enforce posture/grapple/stagger/knockdown restrictions on targetability.
- [ ] TASK-COMBAT-010 — Ensure unavailable zones are absent from player-safe target selection.
- [ ] TASK-COMBAT-011 — Add zone-specific armor/defense interaction.
- [ ] TASK-COMBAT-012 — Add zone wounds with persistent consequences.
- [ ] TASK-COMBAT-013 — Add limb/sense/wing/joint impairment effects.
- [ ] TASK-COMBAT-014 — Add heart/core high-lethality/high-loot-damage rules.
- [ ] TASK-COMBAT-015 — Add battle-state transitions that expose or hide zones.
- [ ] TASK-COMBAT-016 — Add terrain transitions: doorway, wall, ledge, rubble, mud/water, den.
- [ ] TASK-COMBAT-017 — Add deterministic player-safe combat projection.
- [ ] TASK-COMBAT-018 — Add regression tests proving not all zones are selectable from every state.
- [ ] TASK-COMBAT-019 — Add regression tests for environment-driven zone unlocks.
- [ ] TASK-COMBAT-020 — Add regression tests for target-zone consequences and persistence.

## Epic E — Beast persistent state and progression

- [ ] TASK-BEAST-001 — Define BeastSpeciesDefinition.
- [ ] TASK-BEAST-002 — Define BeastRuntimeState with stable beast IDs.
- [ ] TASK-BEAST-003 — Define beast attributes/skills/resources without flattening power into level.
- [ ] TASK-BEAST-004 — Add beast level and development XP/progress.
- [ ] TASK-BEAST-005 — Define development sources: survival, hunts, rivals, territory, maturation, resources, evolution.
- [ ] TASK-BEAST-006 — Add diminishing progression for repeated low-novelty events.
- [ ] TASK-BEAST-007 — Add persistent injuries/scars and current-capability penalties.
- [ ] TASK-BEAST-008 — Add beast crystal/core runtime state.
- [ ] TASK-BEAST-009 — Add beast goals/territory/social group/rivals/followers.
- [ ] TASK-BEAST-010 — Add age/development stage and mortality hooks.
- [ ] TASK-BEAST-011 — Add save/load schema and migration coverage for persistent beasts.
- [ ] TASK-BEAST-012 — Add deterministic level-up/development tests.

## Epic F — Retreat memory and adaptive enemies

- [ ] TASK-ADAPT-001 — Define EncounterMemory contract.
- [ ] TASK-ADAPT-002 — Record observed player weapons, target zones, ranges, techniques, party composition, terrain, wounds, and retreat outcomes.
- [ ] TASK-ADAPT-003 — Add confidence to observations so beasts can remember imperfectly.
- [ ] TASK-ADAPT-004 — Define memory capacity/decay/retention by intelligence and traits.
- [ ] TASK-ADAPT-005 — Define behavioral adaptations.
- [ ] TASK-ADAPT-006 — Define tactical adaptations.
- [ ] TASK-ADAPT-007 — Define slow biological/evolutionary adaptations.
- [ ] TASK-ADAPT-008 — Require evidence/time/resources before adaptations commit.
- [ ] TASK-ADAPT-009 — Prevent omniscient counters and arbitrary post-retreat buffs.
- [ ] TASK-ADAPT-010 — Allow player style changes to exploit beast expectations.
- [ ] TASK-ADAPT-011 — Prevent retreat-loop XP/adaptation farming.
- [ ] TASK-ADAPT-012 — Add deterministic encounter-memory/adaptation tests.

## Epic G — Intelligence, hierarchy, and territorial command

- [ ] TASK-INTEL-001 — Freeze beast intelligence capability tiers.
- [ ] TASK-INTEL-002 — Separate intelligence from sociality, anatomy, level, and combat skill.
- [ ] TASK-INTEL-003 — Define eligibility for solitary/member/veteran/chieftain/commander/territory-ruler roles.
- [ ] TASK-INTEL-004 — Require followers, territory, intelligence, and social capability for command roles.
- [ ] TASK-INTEL-005 — Add commander actions: patrols, nest movement, ambushes, road pressure, mine/crystal control, retaliation.
- [ ] TASK-INTEL-006 — Add rank promotion/demotion rules.
- [ ] TASK-INTEL-007 — Add morale/reputation/fear inputs where useful.
- [ ] TASK-INTEL-008 — Add deterministic hierarchy tests.

## Epic H — Living beast ecology

- [ ] TASK-ECO-001 — Define WorldRegionState and TerritoryState.
- [ ] TASK-ECO-002 — Define region-scoped beast simulation cadence.
- [ ] TASK-ECO-003 — Add coarse deterministic beast-vs-beast conflict resolution.
- [ ] TASK-ECO-004 — Include injuries, group strength, intelligence, terrain, crystal traits, hunger, morale, and exhaustion.
- [ ] TASK-ECO-005 — Persist territory changes, deaths, migration, rivalries, pack changes, and development.
- [ ] TASK-ECO-006 — Add carrying capacity/resources to prevent runaway regional power growth.
- [ ] TASK-ECO-007 — Add aging, starvation, injury, migration, and mortality constraints.
- [ ] TASK-ECO-008 — Prioritize simulation detail near the player and coarse/event-driven updates elsewhere.
- [ ] TASK-ECO-009 — Add deterministic replay tests for identical seed/state/time.
- [ ] TASK-ECO-010 — Add save/resume tests for world ecology updates.

## Epic I — Beast voice and communication

- [ ] TASK-VOICE-001 — Define authored beast voice profiles.
- [ ] TASK-VOICE-002 — Map intelligence/language tiers to allowed expression complexity.
- [ ] TASK-VOICE-003 — Define bark/template conditions for emotion, wounds, territory, rank, and encounter state.
- [ ] TASK-VOICE-004 — Allow safe references to structured encounter memories.
- [ ] TASK-VOICE-005 — Allow commanders to issue tactical orders through authored templates.
- [ ] TASK-VOICE-006 — Keep runtime text deterministic and inspectable without generative AI dependency.
- [ ] TASK-VOICE-007 — Create player-safe dialogue projection that does not expose hidden memory data.
- [ ] TASK-VOICE-008 — Add regression tests for intelligence-gated dialogue and memory references.
- [ ] TASK-VOICE-009 — Keep future audio/voice generation as presentation only, not authoritative game logic.

## Epic J — First complete medieval hunt vertical slice

- [ ] TASK-HUNT-001 — Author one region with mine, settlement, smith, hunting ground, and beast territory.
- [ ] TASK-HUNT-002 — Author one persistent beast with body zones, crystal core, intelligence, memory, and level progression.
- [ ] TASK-HUNT-003 — Allow player to scout and learn anatomy before battle.
- [ ] TASK-HUNT-004 — Provide at least three meaningful combat approaches using different weapons/positions.
- [ ] TASK-HUNT-005 — Include battle-state change that unlocks a previously unavailable target zone.
- [ ] TASK-HUNT-006 — Include retreat path that preserves beast memory.
- [ ] TASK-HUNT-007 — Re-encounter the same beast with adaptation based on observed behavior.
- [ ] TASK-HUNT-008 — Allow pristine vs damaged heart-crystal outcomes depending on kill method.
- [ ] TASK-HUNT-009 — Forge recovered crystal into equipment.
- [ ] TASK-HUNT-010 — Prove forged equipment affects a later combat through authoritative rules.
- [ ] TASK-HUNT-011 — Include save/resume across hunt, retreat, re-encounter, harvest, and forging.
- [ ] TASK-HUNT-012 — Run full integration regression suite before expanding additional species/regions.

## Design dependencies and constraints

- The seven-vs-eight core-stat decision remains separate and must not be silently resolved by these tasks.
- GameState and rules remain authoritative; presentation consumes player-safe projections.
- Runtime generative AI remains optional presentation tooling, not a gameplay dependency.
- Important beast memories, adaptations, territories, crystals, items, wounds, and encounter outcomes need stable IDs/state if later systems react to them.
- Slow progression and persistent consequence remain global design rules.
- No paid/billing-risk CI should be introduced solely for verification without explicit user authorization.


## Prototype evidence ledger — 2026-09-27

Status: [PROTOTYPE] / NOT PROMOTED / NOT TASK COMPLETION

Prototype branch: `prototype/medieval-crystal-combat-contracts`

Prototype code/test HEAD exercised before documentation-only refresh: `8092edd4e106b0b44c983c78645a8793e975d444`

Current prototype branch after status documentation refresh: `c44f7289d79b025613e2ed454161f6ade55f630d`

Base V6: `7f5f104fb839068bdfaf5cec72f37129ae20d463`

The following backlog areas now have isolated executable prototypes. Their main checkboxes remain open because the work has not been integrated with the authoritative GameState/persistence/content loader or executed together with the exact V6 suite.

Prototype coverage:

- TASK-COMBAT-001..010 — CombatState/body-zone reachability concepts, positional gates, and player-safe target projection are prototyped.
- TASK-COMBAT-017..019 — player-safe targeting and environment/state-driven unlock behavior have prototype tests.
- TASK-CRYSTAL-001..004 — crystal definitions/instances, source types, provenance, and appraisal visibility are prototyped.
- TASK-CRYSTAL-007..008 — harvest-damage/integrity representation and strict metadata validation are partially prototyped.
- TASK-EQUIP-001..011 — physical weapon/armor definitions, damage/resistance profiles, body coverage, durability, and crystal-socket metadata are partially prototyped.
- TASK-EQUIP-014..015 — player-safe weapon/armor projections and prototype automated coverage exist.
- TASK-FORGE-002 — staged forge-job order is prototyped.
- TASK-FORGE-004..005 — crystal/weapon compatibility, stability, socket-capacity, and destroyed-crystal rejection are partially prototyped.
- TASK-FORGE-007 — forge compatibility/preview returns explicit deterministic reasons; final quality provenance is still open.
- TASK-BEAST-002..004 — BeastRuntimeState-shaped data, level/development fields, and intelligence are prototyped; actual level-up progression remains open.
- TASK-ADAPT-001..009 — bounded encounter memory, observation confidence, intelligence gates, time/resources gates, and no-omniscient-counter readiness are prototyped. Actual authored adaptations are still open.
- TASK-ADAPT-012 — isolated deterministic tests exist for memory/adaptation readiness.
- TASK-INTEL-001..004 — intelligence range, communication cap, role vocabulary, and authored command eligibility gates are partially prototyped.

Isolated runtime evidence:

- combat targeting: 11 tests
- crystals: 11 tests
- beast memory/adaptation/command: 14 tests
- weapons: 12 tests
- armor: 11 tests
- forge compatibility/staging: 10 tests
- total: **69 passed / 0 failed / 0 errors**

Important limitation:

The local shell could not resolve `github.com`, so it could not clone the exact repository and run the existing V6 258-test suite together with these 69 tests. Stage 3 therefore remains open and none of these prototype tasks should be marked integrated/canonical yet.


### Prototype expansion evidence — wounds and first hunt integration

Prototype branch code/test HEAD exercised: `6f0f8ed1b165d3de43f14ce0d58d0237259ddfe3`

Documentation-only prototype HEAD after evidence refresh: `efbfaee6d23eb85889db09a058dc9b04669f03c7`

Additional prototype coverage:

- TASK-COMBAT-012..013 — persistent per-zone wound consequences, impairment tags, and disabled actions are prototyped.
- TASK-COMBAT-014 — direct core-zone damage can now deterministically translate into beast-crystal harvest damage.
- TASK-HUNT-004..009 — a contract-level integration test now connects weapon targeting, armor coverage, limb injury, retreat memory, adaptation readiness, rematch geometry, core exposure, crystal damage, and forge compatibility.
- TASK-HUNT-005 — explicitly demonstrated: head/core are unavailable initially and become available only after battle-state changes.
- TASK-HUNT-006 — retreat is recorded as persistent beast encounter memory in the prototype.
- TASK-HUNT-007 — repeated observed targeting is sufficient for behavioral adaptation readiness; no adaptation appears without observations.
- TASK-HUNT-008 — core strike changes harvested crystal integrity.
- TASK-HUNT-009 — recovered beast crystal is checked against weapon socket/compatibility rules.

Updated isolated runtime evidence:

- previous prototype tests: 69
- wound tests: 12
- cross-system hunt integration tests: 3
- total: **84 passed / 0 failed / 0 errors**

These remain isolated prototype results, not full-repository V6 integration results.


## Prototype implementation evidence — medieval/crystal contracts

Status: [IMPLEMENTED PROTOTYPE] / [VERIFIED FOCUSED LOCAL] / NOT INTEGRATED

Prototype branch: `prototype/medieval-crystal-contracts`

The branch was created from exact V6 SHA `7f5f104fb839068bdfaf5cec72f37129ae20d463` so the experimental work cannot be mistaken for the current V6 promotion candidate.

Implemented prototype contracts:
- weapon-family, damage-profile, range-band, target-tag, and physical-property validation
- beast/mine crystal instance provenance and finite numeric validation
- body-zone definition validation
- CombatState validation for facing, range, posture, elevation, exposure tags, and blocked zones
- deterministic reachable-target query
- player-safe targeting projection that omits authored access/weak-point rules
- persistent beast runtime-state validation with level and intelligence represented separately
- data-driven beast role eligibility using independent level, intelligence, follower, and territory gates
- EncounterMemory validation
- copy-on-write encounter observation recording with count/confidence accumulation
- evidence/time/intelligence-gated adaptation eligibility

Focused local verification:
- 17 tests executed
- 17 passed
- 0 failed
- both prototype source/test slices compiled with `python -m py_compile`
- committed GitHub blob SHAs were compared against locally tested Git blob hashes and matched byte-for-byte

Important limitation:
- the exact full V6 suite is still NOT EXECUTED because the local container cannot resolve `github.com`, the connected GitHub tooling does not expose a general repository archive, and no paid/billing-risk CI was introduced.
- these focused results do not satisfy TASK-STAGE3-001..008 and do not permit V6 promotion.

Prototype task progress:
- TASK-CRYSTAL-002 — PARTIAL: CrystalInstance contract exists; CrystalDefinition remains.
- TASK-CRYSTAL-003 — PARTIAL: grade, purity, size, stability, resonance tags, provenance, and harvest integrity are represented; capacity/recharge/affinity definition work remains.
- TASK-EQUIP-001 — PARTIAL: initial weapon-family registry exists in prototype.
- TASK-EQUIP-002 — PARTIAL: weapon definition contract exists; full EquipmentInstance contract remains.
- TASK-EQUIP-003 — PARTIAL: weight, reach, handling, momentum, guard, recovery, stamina burden, durability are validated.
- TASK-EQUIP-004 — PROTOTYPE IMPLEMENTED: cut/pierce/blunt damage-profile contract.
- TASK-EQUIP-006 — PARTIAL: range bands and target-access tags exist; optimal/minimum range balancing remains.
- TASK-COMBAT-001 — PROTOTYPE IMPLEMENTED: minimal CombatState contract.
- TASK-COMBAT-005 — PROTOTYPE IMPLEMENTED: BodyZoneDefinition contract.
- TASK-COMBAT-006 — PROTOTYPE IMPLEMENTED: authoritative target-zone availability query.
- TASK-COMBAT-007 — PROTOTYPE IMPLEMENTED: weapon range/target-tag constraints affect targetability.
- TASK-COMBAT-009 — PARTIAL: posture is represented and zone-gated; grapple/stagger transitions remain.
- TASK-COMBAT-010 — PROTOTYPE IMPLEMENTED: unavailable zones are absent from safe target selection.
- TASK-COMBAT-015 — PARTIAL: changing facing/exposure state changes reachable zones; transition actions remain.
- TASK-COMBAT-017 — PROTOTYPE IMPLEMENTED: player-safe targeting projection.
- TASK-COMBAT-018 — PROTOTYPE VERIFIED FOCUSED: tests prove not all zones are selectable in every state.
- TASK-COMBAT-019 — PROTOTYPE VERIFIED FOCUSED: exposure/facing state changes unlock previously unavailable zones.
- TASK-BEAST-002 — PARTIAL: minimal persistent BeastRuntimeState contract.
- TASK-ADAPT-001 — PROTOTYPE IMPLEMENTED: EncounterMemory contract.
- TASK-ADAPT-002 — PARTIAL: generic observed-pattern recording exists; combat event adapter remains.
- TASK-ADAPT-003 — PROTOTYPE IMPLEMENTED: confidence stored per observation.
- TASK-ADAPT-008 — PROTOTYPE IMPLEMENTED: evidence/time/intelligence required before adaptation eligibility.
- TASK-ADAPT-009 — PROTOTYPE VERIFIED FOCUSED: adaptation does not trigger merely because an encounter ended or the player escaped.
- TASK-INTEL-003 — PARTIAL: role gate contract exists.
- TASK-INTEL-004 — PROTOTYPE IMPLEMENTED: command eligibility can require independent intelligence/follower/territory gates.


### Prototype extension — equipment/crystal integration

[IMPLEMENTED PROTOTYPE] On `prototype/medieval-crystal-contracts`:
- EquipmentInstance validation now covers stable instance/definition/material IDs, forge quality, condition, crystal sockets, grade limits, accepted crystal sources, resonance compatibility, and integration modes.
- Crystal fitting is copy-on-write and preserves the installed crystal's original source/provenance and harvest integrity.
- Replaceable sockets and permanent fusion are distinct authored integration modes.
- Fusion locks the crystal; ordinary removal rejects fused crystals rather than silently undoing a permanent craft.
- Occupied sockets reject a second crystal.
- Non-finite integration quality is rejected.

[VERIFIED FOCUSED LOCAL] The isolated prototype suite now contains **24 passing tests / 0 failures**.

[VERIFIED] Byte-for-byte Git blob matches for the added tested files:
- `src/textrpg/crystal_forging.py` -> `fb2778a44359f20d80a1ea40465af8e534dc3ec4`
- `tests/test_crystal_forging.py` -> `98631da28ae2f3732bb673378b7a93b74cbbc471`

Additional task progress:
- TASK-EQUIP-002 — PARTIAL: EquipmentInstance contract now exists in prototype; integration with legacy equipment state remains.
- TASK-EQUIP-010 — PROTOTYPE IMPLEMENTED: crystal socket/channel-compatible metadata contract.
- TASK-EQUIP-011 — PROTOTYPE IMPLEMENTED: replaceable socket vs permanent fusion distinction.
- TASK-FORGE-004 — PROTOTYPE IMPLEMENTED: grade/source/resonance/mode compatibility gates.
- TASK-FORGE-007 — PARTIAL: integration records quality and smith provenance; complete forge-step provenance remains.
