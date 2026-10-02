# Documentation Program Master

Status: ACTIVE / PROGRAM CONTROL
Repository: `jbob-coder/Text-rpg-game`

## Outcome

Create a repository-native body of documentation sufficient for another capable developer/agent to understand the game, decide what is authoritative, identify unresolved design decisions, build systems/assets/maps in the intended order, verify them, and eventually rebuild the Android client from a documented final architecture.

## Program domains

| ID | Domain | Primary output |
|---|---|---|
| D-01 | World/map/regions | spatial hierarchy, coordinates, geography, settlements, travel and expansion |
| D-02 | Pixel art/assets/UI | visual grammar, reusable assets, overlays, panels, scene composition |
| D-03 | Characters/NPC/social | identity, presence, panels, hierarchy, relationships, memory, factions |
| D-04 | Progression/combat/systems | stats, skills, classes, ranks, abilities, passives, tactical combat, rival evolution |
| D-05 | Economy/items/ecosystem | resources, loot, items, accessories, production, beasts, ecology, scarcity |
| D-06 | Android/APK | application architecture, UX surfaces, migration, teardown/rebuild and release evidence |
| D-07 | Documentation/coordination | indexes, guides, decision records, dependency graph, QA and handoffs |

## Evidence classes

Every meaningful statement should be classifiable as one of:
- CONFIRMED IMPLEMENTED
- CONFIRMED DOCUMENTED
- OWNER DECISION
- PROPOSED
- EXTERNAL REFERENCE IDEA
- UNKNOWN
- CONFLICTING
- SUPERSEDED
- DEFERRED

Do not convert PROPOSED into CONFIRMED merely by repeating it in multiple documents.

## Change authority

Broad project-development permission is active for reversible engineering and documentation work.

Breaking/rebuild work is allowed when it is deliberately documented and materially improves the product. Before destructive replacement:
1. identify current behavior/files;
2. identify why replacement is required;
3. define the new source of truth;
4. define save/data/API compatibility impact;
5. define rollback or compensating recovery;
6. define tests and user-visible acceptance evidence;
7. execute only when the relevant implementation phase begins.

## Cross-document contract

Every specialized document must answer:
- What does this document own?
- What does it explicitly not own?
- Which upstream documents constrain it?
- Which downstream files/systems consume it?
- What is confirmed?
- What is proposed?
- What remains unknown?
- What would force revision?
- What tests or evidence prove implementation?

## Traceability contract

Important requirements receive stable IDs.

Example:
- P-WORLD-001: world spatial hierarchy must remain expandable.
- P-ART-001: temporary state is an overlay, not baked into reusable base art.
- P-NPC-001: scene presence must be engine-owned.
- P-COMBAT-001: tactical combat must be original and state-driven.
- P-APK-001: UI must not own authoritative gameplay state.

Implementation work later maps:
`Requirement -> document/component -> task -> acceptance test -> observed evidence`.

## Program phases

### Phase A — Inventory and authority
Audit what exists, classify it, mark stale pointers, preserve owner directives.

### Phase B — Domain architecture
Create the seven domain programs and decision-gap register.

### Phase C — Pilot depth
Finish Gate Twelve to implementation-grade detail across map, art, state, UX and migration.

### Phase D — World expansion
Expand hierarchy to regions, cities, villages, kingdoms, ecosystems, resources, factions, beast zones and routes.

### Phase E — System depth
Lock progression, economy, combat, rivalry, NPC autonomy, classes/ranks, world scaling and balance.

### Phase F — Asset/content production
Generate/reconstruct only assets and content backed by documented contracts and stable IDs.

### Phase G — Android reconstruction
Audit current client, decide keep/replace/retire per component, rebuild in bounded slices, preserve engine authority, migrate saves/contracts where necessary.

### Phase H — Final execution handoff
Produce one final implementation authority map stating exactly what survives, changes, migrates, gets deleted, or remains deferred.

## Current status

Existing repository documentation is substantial but fragmented across different historical branches/objectives. This program does not invalidate useful prior work; it re-indexes it under the current priority and marks stale operational pointers for later update.

Gate Twelve Steps 1–4 are confirmed present. Step 5 was previously claimed as complete in chat but is not currently persisted in the Master Plan; therefore it remains unfinished until actually written and verified in the repository.
