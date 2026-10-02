# Documentation Expectation and Acceptance Standard

Status: **ACTIVE / NORMATIVE**
Repository: `jbob-coder/Text-rpg-game`
Applies to: all new and materially revised design/planning documentation

## 1. Purpose

The documentation program is not measured only by how many files exist.

A document is useful only when another developer, agent, designer, artist, or future session can use it to make the correct next decision without reconstructing hidden intent from chat history.

This standard defines the minimum expectation for a documentation unit.

## 2. Mandatory document header

Every substantive document should identify, where relevant:

- title;
- status;
- domain/program owner;
- authority/evidence class;
- scope;
- related stable IDs;
- upstream dependencies;
- downstream consumers.

Small index files may omit fields that would add no value.

## 3. Mandatory questions

A substantive design/specification document must answer:

1. What does this document own?
2. What does it explicitly not own?
3. What existing repository facts constrain it?
4. What owner decisions constrain it?
5. What is already implemented?
6. What is documented but not implemented?
7. What is proposed?
8. What remains unknown?
9. What conflicts or historical decisions exist?
10. What other documents depend on this one?
11. What implementation/assets/content would be created, changed, migrated, retired, or deleted?
12. What would force this document to be revised?
13. How will implementation be verified?
14. What is the next unresolved action?

A document may state “not applicable” rather than fabricate an answer.

## 4. Evidence classes

Use these labels consistently:

- `CONFIRMED_IMPLEMENTED`
- `CONFIRMED_DOCUMENTED`
- `OWNER_DECISION`
- `PROPOSED`
- `EXTERNAL_REFERENCE_IDEA`
- `UNKNOWN`
- `CONFLICTING`
- `SUPERSEDED`
- `DEFERRED`
- `RETIRED`

A repeated proposal does not become confirmed through repetition.

## 5. Decision completeness

A decision is considered documented only when the document records:

- decision statement;
- reason;
- affected systems/assets/content;
- incompatible alternatives if relevant;
- migration impact;
- unresolved consequences;
- verification expectation.

## 6. Implementation relationship

Every implementation-facing document must distinguish:

### Current
What actually exists now.

### Target
What the final documented architecture should become.

### Delta
What must change to move from current to target.

### Migration
How the transition happens without silently losing required behavior/state.

### Acceptance
What evidence proves the target was implemented.

## 7. Asset/document expectation

Asset documentation must identify:

- stable asset ID or planned ID family;
- native grid/resolution;
- perspective;
- anchor/pivot;
- z-order/occlusion;
- palette/material family;
- lighting assumption;
- state ownership;
- reuse permissions;
- forbidden reuse;
- current lifecycle state;
- consumers;
- QA expectation.

A reference image is not a production asset.

## 8. World-document expectation

World documents must identify, as relevant:

- stable entity ID;
- hierarchy parent/children;
- coordinate space;
- routes;
- boundaries;
- population/society;
- economy/resources;
- ecosystem;
- beasts/beast zones;
- gameplay role;
- visual language;
- world-state variants;
- unresolved geography/system decisions.

## 9. Character/NPC/beast presence expectation

Any scene-composition document must account for every class of entity that can visibly occupy or materially affect the scene.

At minimum distinguish:

- player;
- NPC/character;
- party member;
- beast;
- environmental entity/prop;
- hidden/non-visible entity;
- transient effect.

Do not classify the game's beasts as generic “monsters” in normative documentation unless a future explicit taxonomy introduces that term.

## 10. System-document expectation

System specifications must identify:

- state owner;
- inputs;
- outputs;
- deterministic/random behavior;
- persistence;
- failure behavior;
- UI projection;
- balance variables;
- extension points;
- testing.

For combat/progression/economy systems, formulas may remain unresolved, but unresolved values must be explicit.

## 11. Cross-document reference expectation

A document should link to the actual upstream/downstream repository documents it relies on.

Avoid orphan documents.

When a document supersedes another decision:
- preserve the historical record;
- mark the old decision superseded;
- update active indexes/pointers.

## 12. Quality statuses

Use the following documentation quality states:

### DRAFT
Structure exists but major sections are missing.

### STRUCTURED
All required areas exist but decisions/evidence may still be incomplete.

### REVIEWABLE
Current/target/gaps/dependencies are clear enough for domain review.

### IMPLEMENTATION_READY
A developer can implement the scoped feature without guessing material rules.

### VERIFIED_IMPLEMENTATION
The documented implementation has matching observed evidence.

A document may be complete as documentation while its implementation remains pending.

## 13. Acceptance checklist

A substantive document passes documentation QA when:

- [ ] scope is explicit;
- [ ] authority/status is explicit;
- [ ] current versus target is separated;
- [ ] confirmed versus proposed is separated;
- [ ] unknowns are visible;
- [ ] dependencies are linked;
- [ ] stable IDs/terms are used consistently;
- [ ] assets/systems affected are identified;
- [ ] migration is addressed if current behavior changes;
- [ ] verification/acceptance exists;
- [ ] next action is explicit;
- [ ] no external reference is presented as canon without a decision;
- [ ] no stale statement contradicts a newer active document without being marked superseded.

## 14. Anti-filler rule

Documentation-count targets do not override quality.

Do not:
- clone boilerplate solely to increase file count;
- create one-line files with no unique ownership;
- repeat the same decision across dozens of files without cross-linking;
- invent details merely to fill sections;
- mark a template as completed content.

## 15. Audit cadence

After each meaningful documentation batch:

1. verify files exist at the expected paths;
2. identify stale statements;
3. update the decision-gap register;
4. update coverage/status index;
5. check new documents for orphan references;
6. record what remains undecided.

This audit is part of the work, not an optional cleanup phase.
