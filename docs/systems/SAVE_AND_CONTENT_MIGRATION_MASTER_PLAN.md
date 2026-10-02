# THE GAME — Save, Content & State Migration Master Plan

Status: **HIGH-RISK GOVERNANCE / REQUIRED BEFORE BREAKING CONTRACTS**
Parents:
- `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`
- `docs/EXISTING_STATE_REWORK_DECISION_MATRIX.md`
- `docs/android/APK_REBUILD_AND_EVOLUTION_MASTER_PLAN.md`

## 1. Purpose

Prevent final reconstruction from losing authoritative game state.

Any change to stable IDs, save schema, core stats, item/equipment semantics, NPC state, quest state, map routes, or ability systems must have an explicit migration.

## 2. Migration categories

- additive compatible;
- rename;
- field split;
- field merge;
- type change;
- ID remap;
- schema version;
- content graph migration;
- asset ID migration;
- removal/deprecation;
- irreversible reset — last resort, owner-visible.

## 3. Stable-ID rule

Never silently reuse an old ID for a different meaning.

For renames:
- old ID;
- new ID;
- migration mapping;
- compatibility period if needed;
- tests.

## 4. Save versions

Each breaking save structure gets:
- schema version;
- loader;
- migrator;
- validation;
- rejection of unsupported versions;
- fixtures.

## 5. Player state migration

Audit:
- attributes;
- derived values;
- resources;
- skills;
- abilities;
- techniques;
- perks/passives;
- conditions;
- inventory;
- equipment;
- party;
- relationships;
- knowledge;
- quests;
- flags;
- time;
- location.

## 6. World state migration

Audit:
- discovered locations;
- routes;
- world events;
- faction state;
- NPC locations/schedules;
- rival state;
- resource depletion;
- beast zones if persistent;
- economy if persistent.

## 7. Quest migration

Need mapping for:
- quest ID;
- stage;
- objectives;
- mutually exclusive paths;
- failed/completed state;
- hidden state;
- rewards already claimed.

Do not restart quests silently.

## 8. NPC migration

Need:
- NPC ID;
- memory;
- knowledge;
- relationships;
- goals;
- schedule/location;
- injuries;
- faction;
- rival state.

## 9. Item migration

Need:
- item IDs;
- stacks;
- equipped slots;
- modifiers;
- condition/quality if introduced later;
- ownership;
- quest relevance.

## 10. Map migration

If routes/coordinates change:
- preserve current location;
- remap invalid node;
- preserve discovered state;
- update route graph;
- avoid trapping save in inaccessible location.

## 11. Visual asset migration

Asset IDs may change without gameplay state only if:
- stable gameplay ID remains;
- manifest maps old visual key to new;
- fallback exists during transition;
- screenshots verify.

## 12. Migration implementation pattern

1. document old schema;
2. document new schema;
3. write pure migration function where possible;
4. retain old fixture;
5. run old->new;
6. validate new;
7. load/save round trip;
8. verify gameplay;
9. record evidence.

## 13. Rollback

Before destructive migration:
- branch;
- backup fixture;
- previous release/source provenance;
- ability to detect failed migration;
- no overwrite of only copy before success.

## 14. Unsupported legacy policy

If a schema cannot be migrated:
- detect explicitly;
- explain to user;
- preserve export/backup if practical;
- never reinterpret corrupt/unknown state as fresh game silently.

## 15. Final APK dependency

The final APK rebuild cannot delete legacy adapters until:
- supported saves migrate;
- tests pass;
- player state survives;
- old adapter consumers are gone.

## 16. Open migration risks

- future stat/class redesign;
- global world-map expansion;
- tactical combat persistent state;
- rival network state;
- item quality/durability if introduced;
- NPC schedule state;
- economy/resource persistence.
