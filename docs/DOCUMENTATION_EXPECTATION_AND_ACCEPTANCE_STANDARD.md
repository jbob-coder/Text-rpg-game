# THE GAME — Documentation Expectation and Acceptance Standard

Status: **ACTIVE / P0 RECONSTRUCTION STANDARD**  
Repository: `jbob-coder/Text-rpg-game`  
Parent authorities:
- `docs/MASTER_GAME_DEVELOPMENT_PROGRAM.md`
- `docs/DOCUMENTATION_CORPUS_ARCHITECTURE.md`

Moving-base source provenance:
- `docs/program/12_DOCUMENT_EXPECTATION_AND_ACCEPTANCE_STANDARD.md`
- source branch: `docs/settlement-region-build-plan@65d2db8538c1b8302c314f2fbe9eb7a1b585b51d`
- source blob: `0f952e7faf2f92f9a0315d8f5a81341abcf5c6c2`
- selectively extracted under D-044; the `docs/program/*` hierarchy is not activated.

## 1. Purpose

The documentation program is a reconstruction system, not a file-count exercise.

A substantive document is useful only when a future developer, AI agent, designer, artist, tester, or project owner can use it to:

- identify what is true now;
- identify what is intended;
- identify what is unknown or blocked;
- locate the source of authority;
- understand dependencies and consumers;
- reconstruct the subject without undocumented assumptions;
- determine what evidence is required before claiming implementation or completion.

File count, word count, record count, and other corpus metrics do not override reconstruction value.

The large numerical documentation targets remain **UNRESOLVED UNITS** until the owner explicitly resolves them.

## 2. Authority and evidence vocabulary

Use the current project vocabulary where the distinction applies.

### VERIFIED CURRENT IMPLEMENTATION

Directly supported by inspected repository source, data, asset, branch or observed execution evidence.

A historical test result is verified evidence only for its exact recorded head.

### ESTABLISHED DESIGN/CANON

A current accepted design/canon rule owned by an active authority document or explicit owner decision.

Do not infer canon merely because a proposal is detailed.

### PROPOSED DESIGN

A target, option or working architecture that has not been accepted as canon/current implementation.

### INFERENCE

A conclusion derived from evidence but not directly stated or implemented.

Record the evidence and what would invalidate the inference.

### UNKNOWN

Repository evidence does not establish the answer.

Unknown is preferable to fabricated precision.

### BLOCKED

The work cannot safely advance until a named prerequisite is satisfied.

### DEPRECATED

The subject remains historical evidence but is no longer the active path.

Use `SUPERSEDED` inside a document when describing a specific earlier decision/version if that term is clearer, but active project status should remain unambiguous.

### MIGRATION REQUIRED

Current and target states differ in a way that needs an explicit transition, compatibility, data, consumer or replacement plan.

### OWNER DECISION REQUIRED

The repository can frame the decision and consequences, but the project owner must accept/reject/select the option.

## 3. Mandatory document identity

Every substantive new or materially revised document should identify, where relevant:

- title;
- status;
- repository;
- parent authority;
- authority/evidence class;
- scope;
- explicit non-scope;
- related stable IDs;
- source branches/heads when implementation evidence is involved;
- upstream dependencies;
- downstream consumers;
- related migrations;
- related tests/evidence;
- unresolved decisions;
- last meaningful audit/update date when chronology matters.

Small indexes may omit fields that add no useful information.

A historical evidence file must not masquerade as live authority merely because it remains linked.

## 4. Mandatory reconstruction questions

A reconstruction-grade specification should answer, where applicable:

1. What does this document own?
2. What does it explicitly not own?
3. What existing repository facts constrain it?
4. What established owner/design decisions constrain it?
5. What is VERIFIED CURRENT IMPLEMENTATION?
6. What is ESTABLISHED DESIGN/CANON?
7. What is PROPOSED DESIGN?
8. What is inferred?
9. What is UNKNOWN?
10. What is BLOCKED?
11. What is DEPRECATED or superseded?
12. What requires migration?
13. What requires an owner decision?
14. What stable IDs/schema fields/records are involved?
15. What systems, files, assets, content and consumers depend on it?
16. What mutates authoritative state?
17. What is presentation-only?
18. What persists through save/load or application preferences?
19. What failure/edge cases matter?
20. What would force this document to be revised?
21. What implementation/assets/content would be created, changed, migrated, retired or removed?
22. How will implementation be verified?
23. What evidence is insufficient by itself?
24. What is the next unresolved action?
25. If implementation disappeared, what instructions would a future developer need to rebuild it correctly?

A document may state **not applicable** rather than manufacture content.

## 5. Current -> target -> delta -> migration -> acceptance

Every implementation-facing specification must distinguish these layers.

### CURRENT

What exists at the inspected source/evidence head.

Include:
- files;
- schemas;
- assets;
- consumers;
- runtime flow;
- persistence;
- tests;
- defects/debt.

### TARGET

What the system is intended to become.

Target does not imply implemented.

### DELTA

What differs between current and target.

### MIGRATION

How the project transitions without silently losing:

- authoritative state;
- stable identity;
- save compatibility;
- behavior;
- player-safe visibility;
- asset provenance;
- test coverage;
- recovery capability.

### ACCEPTANCE

What observed evidence proves the scoped target is implemented.

Do not collapse these five layers into one narrative.

## 6. Decision completeness

A decision is durable only when the current authority records, where relevant:

- decision statement;
- status;
- reason;
- evidence;
- affected systems/assets/content;
- incompatible alternatives;
- dependencies;
- migration impact;
- unresolved consequences;
- rollback/recovery considerations;
- acceptance/verification expectation;
- supersession relationship if it replaces an earlier decision.

Repeated proposals do not become established design through repetition.

## 7. Stable-ID and schema expectation

Documents governing durable records should identify:

- stable ID;
- namespace/type;
- parent/child relationship;
- references/consumers;
- lifecycle;
- rename/merge/split rules if applicable;
- save/persistence impact;
- migration behavior;
- validation rules;
- unknown fields/relationships.

Do not rename established IDs for cosmetic consistency without a migration reason.

## 8. Asset-document expectation

Important production asset documentation should identify, where applicable:

- stable asset ID or planned ID family;
- purpose;
- source/code master;
- native grid/resolution;
- perspective;
- anchor/pivot;
- z-order/occlusion;
- palette/material family;
- lighting assumption;
- state ownership;
- variants/derivatives;
- raster/export;
- exact branch/head/blob/hash provenance;
- runtime consumer;
- raster/source precedence;
- reuse permissions;
- forbidden reuse;
- current production stage;
- QA/test evidence;
- missing work;
- migration/occlusion risk;
- canon/owner approval state.

A source master, raster, integrated consumer, verified runtime, and canon approval are different stages.

A reference image is not a production asset.

## 9. World-document expectation

World documentation should identify, as relevant:

- stable entity ID;
- entity class;
- hierarchy parent/children;
- coordinate space;
- boundaries;
- routes/entrances/exits;
- terrain/climate;
- population/society;
- political control;
- economy/resources;
- ecosystem;
- beasts/beast zones;
- institutions/services;
- gameplay role;
- player discovery/access;
- visual/material identity;
- state variants;
- persistence;
- neighboring/expansion relationships;
- unresolved geography/system decisions.

Gate Twelve must not silently become the whole world.

Unestablished parent geography remains unknown/proposed.

## 10. Character/NPC/beast presence expectation

Any scene-composition or room-presence specification must account for the classes of visible entity that can materially affect the scene.

At minimum consider:

- player;
- NPC/character;
- party member;
- support actor;
- beast;
- environmental entity/prop;
- hidden/non-visible entity;
- transient effect.

Presence truth comes from authoritative/player-safe projection.

A sprite or catalog entry does not authorize presence.

Hidden NPC goals, memories, knowledge, relationships, secret flags, future state, private AI intent and undiscovered equipment remain private unless a dedicated player-safe projection explicitly exposes derived information.

## 11. System-document expectation

A reconstruction-grade gameplay/system specification should identify:

- purpose;
- player-facing behavior;
- authoritative owner;
- state/data schema;
- stable IDs;
- inputs;
- outputs;
- mutation rules;
- deterministic/random behavior;
- formulas or unresolved variables;
- invariants;
- dependencies;
- execution sequence;
- visibility/projection;
- persistence/save implications;
- failure behavior;
- edge cases;
- Android/UI consumers;
- migration;
- extension points;
- tests;
- acceptance criteria.

Combat/progression/economy formulas may remain unknown, but unknown values must be explicit.

## 12. Android/application-document expectation

Application specifications should identify:

- source authoritative data;
- player-safe projection;
- application-local/presentation state;
- Compose/ViewModel/bridge consumers;
- mutation route;
- loading/error/fallback behavior;
- responsive layout;
- accessibility;
- reduced motion where animation exists;
- save/app-preference boundary;
- hidden-state prohibitions;
- emulator evidence;
- physical-device evidence;
- APK/release implications.

Presentation convenience is not permission to move gameplay authority into Android.

## 13. Test/evidence expectation

A test/evidence section must distinguish:

- test source exists;
- test executed;
- exact head executed;
- result observed;
- emulator/runtime evidence;
- physical-device evidence;
- historical evidence.

Never write “passes” based solely on test source or an older workflow run.

For consequential claims record, where available:

- branch;
- commit SHA;
- command/workflow;
- run/job ID;
- result;
- artifact;
- screenshot;
- APK/hash;
- known gap.

## 14. Cross-document reference expectation

Every major document should link to actual upstream/downstream repository owners.

Prefer:

`parent authority -> child specification -> implementation file -> test/evidence`

and:

`decision -> migration -> verification -> supersession`

Avoid orphan documentation.

If two active files overlap:

1. determine the master;
2. classify the other as child/complementary/historical/superseded;
3. update indexes;
4. remove silent contradictory authority.

Do not copy a requirement into many files when a durable reference is enough.

## 15. Documentation quality states

These states describe documentation maturity, not implementation state.

### DRAFT

Structure exists but major required sections/evidence are missing.

### STRUCTURED

Required subject areas are identified; important decisions/evidence remain incomplete.

### REVIEWABLE

Current/target/gaps/dependencies/unknowns are clear enough for domain review.

### IMPLEMENTATION_READY

A developer can implement the scoped feature without materially guessing its rules, authority or acceptance contract.

This does not mean the implementation exists.

### VERIFIED_IMPLEMENTATION

The documentation points to observed implementation evidence matching the scoped contract.

This status must name the exact evidence/head.

A document may be complete as documentation while implementation remains pending.

## 16. Acceptance checklist

A substantive document is acceptable for its claimed maturity only when applicable checks pass:

- [ ] scope is explicit;
- [ ] non-scope is explicit;
- [ ] parent authority is explicit;
- [ ] evidence/design status is explicit;
- [ ] current and target are separated;
- [ ] verified, established, proposed, inferred and unknown material are distinguishable;
- [ ] blockers are explicit;
- [ ] owner decisions are explicit;
- [ ] dependencies/consumers are linked;
- [ ] stable IDs/terms are consistent;
- [ ] data/state ownership is explicit;
- [ ] hidden-state boundary is explicit where relevant;
- [ ] persistence/save/app-preference boundary is explicit where relevant;
- [ ] assets/systems/files affected are identified;
- [ ] migration is addressed when current behavior changes;
- [ ] failure/edge cases are addressed;
- [ ] tests/acceptance are defined;
- [ ] observed evidence is not overstated;
- [ ] reconstruction instructions exist for major systems;
- [ ] next action is explicit;
- [ ] external/reference material is not represented as canon without a decision;
- [ ] stale statements do not silently contradict newer authority;
- [ ] numerical documentation targets have not been converted into filler or assumed units.

## 17. Anti-filler rule

Do not:

- clone boilerplate solely to increase file count;
- create one-line files with no unique ownership;
- split one coherent specification into many shallow files for a metric;
- repeat the same decision across many files instead of cross-referencing;
- invent details merely to fill a section;
- mark a template as completed content;
- create fake examples that look like implemented repository state;
- mark a proposal as canon because it is detailed;
- mark test source as a test result.

A short document with unique reconstruction value is preferable to a long duplicate.

A long document is justified when the subject requires detailed reconstruction information.

## 18. Revision triggers

Re-audit a document when:

- its parent authority changes;
- implementation source changes materially;
- a stable schema/ID changes;
- a referenced branch is rebased/superseded;
- an owner decision resolves an unknown;
- evidence contradicts the document;
- a downstream implementation exposes an omitted edge case;
- migration changes the authoritative owner;
- a raster/source/consumer relationship changes;
- a test or release gate changes.

Historical evidence files may remain unchanged if their exact scope/date is clear.

## 19. Batch audit cadence

After a meaningful documentation batch:

1. verify expected files exist;
2. resolve exact branch/head when implementation evidence is cited;
3. identify stale statements;
4. update the task/decision register;
5. update cross-reference/index owners;
6. inspect for duplicate authority;
7. inspect for orphan links;
8. verify structured evidence syntax where applicable;
9. record what remains unknown/blocked;
10. record whether the batch is a complete set or a partial slice.

This audit is part of the work.

## 20. Reconstruction acceptance question

Before declaring a major specification reconstruction-grade, ask:

> If the implementation and chat history disappeared, could a competent developer rebuild the intended system from this documentation, identify what was current versus proposed, preserve hidden-state/authority boundaries, migrate durable state safely, and know how to verify the result?

If the answer is no, the document is not yet reconstruction-grade.

## 21. Relationship to moving-base source

This standard selectively preserves the moving-base document's useful QA structure.

It deliberately does **not** import:

- the moving `docs/program/*` hierarchy as current authority;
- its older evidence labels where they conflict with the owner's current vocabulary;
- stale coverage/status claims;
- any assumption that documentation scale means a fixed number of files.

Current parent authorities and the live task/cross-reference system govern this standard.
