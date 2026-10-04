# THE GAME — Biological Repair, Reserve & Transformation Standard

Status: **PROVISIONAL CROSS-TIER DESIGN STANDARD / NOT CANON UNTIL OWNER REVIEW / NOT IMPLEMENTED**

Parents:
- `PRIMARY_ABILITY_WAVE_001_REFINEMENT_COMPLETENESS_AUDIT.md`
- `ABILITY_ENERGY_RESERVE_ACCOUNTING_STANDARD.md`
- relevant Uncommon, Rare, Super Rare, and Epic ability detail packets.

Purpose: define a shared biological-state vocabulary for Knit Flesh, Bioelectric Overdrive, Adaptive Regeneration, and Adaptive Arsenal without merging their distinct laws.

## 1. Biological state layers

Future authoritative character state should distinguish:
- stable identity;
- current body structure;
- tissue/condition state;
- biological reserve;
- recovery strain;
- learned biological templates;
- regeneration adaptation history;
- temporary transformation state.

No UI layer owns these states.

## 2. Identity boundary

Biological abilities operate on physical biological state.

Default rule:
- identity, memory, learned skills, Status progression, and primary ability identity are not biological material and are not recreated by repair or transformation.

This keeps repair/transformation separate from identity restoration.

## 3. Biological reserve

`biological_reserve` is an ability-specific accounting abstraction representing available material/energy support for advanced biological effects.

It is not automatically equivalent to:
- Health;
- Stamina;
- Focus;
- body mass;
- food inventory;
- any other ability reserve.

A later implementation must define how ordinary recovery, nutrition, rest, and ability use affect this reserve.

## 4. Conservation principle

Biological abilities do not create unlimited material.

A future resolver must account for:
- starting body/material state;
- available biological reserve;
- ability-specific efficiency;
- temporary versus permanent material changes;
- recovery/replenishment.

Any net material increase requires an explicitly authored source.

## 5. Knit Flesh

Knit Flesh accelerates natural repair toward a biologically valid recovery state.

Shared-standard interpretation:
- it is repair, not redesign;
- external use requires the parent ability's contact rule;
- it follows the target's existing anatomy rather than a new template;
- material/recovery limits remain authoritative;
- it does not gain Adaptive Arsenal-style form creation.

Required future state:
- repair target;
- repair stage;
- available biological support;
- medical/stabilization context;
- ability owner and target;
- completion/termination reason.

## 6. Bioelectric Overdrive

Bioelectric Overdrive changes temporary neuromuscular signaling/performance.

It is not a repair or transformation reserve.

Required separation:
- activation state;
- performance multiplier/profile;
- Stamina/Focus cost;
- recovery-strain accumulation;
- cooldown/recovery state.

It does not automatically increase structural durability.

## 7. Adaptive Regeneration

Adaptive Regeneration is deeper self-repair with history-dependent efficiency.

Required state:
- current repair demand;
- biological reserve;
- previously qualified regeneration-pattern history;
- current efficiency modifier;
- recovery strain;
- unresolved condition constraints.

Adaptation history must be keyed to meaningful biological pattern categories rather than one generic “regeneration level.”

## 8. Regeneration adaptation

A regeneration adaptation entry should eventually identify:
- pattern ID/category;
- qualifying prior survival/recovery evidence;
- familiarity/efficiency state;
- last relevant update;
- cap;
- invalidation or diminishing-return rule if used.

The ability must not become universally efficient against every future condition merely because the character regenerated before.

## 9. Adaptive Arsenal

Adaptive Arsenal deliberately changes body structure using learned biological templates.

It is transformation, not repair.

Required state:
- template ID;
- template version;
- body region(s);
- activation/progress state;
- temporary material allocation;
- biological reserve cost;
- compatibility/viability state;
- reversion state.

## 10. Template acquisition

A template cannot be created merely because the user sees an external biological form.

A future template rule must specify:
- how the form is learned;
- required knowledge/practice;
- compatibility requirements;
- minimum data/history;
- whether templates are discovered, trained, researched, or ability-generated;
- permanence/versioning.

No template grants unrelated knowledge.

## 11. Template boundaries

Every Adaptive Arsenal template needs:
- stable template ID;
- intended function;
- allowed body region;
- material requirements;
- activation time;
- sustain cost;
- movement/control requirements;
- reversion requirements;
- incompatibilities;
- content/visual requirements.

A template cannot silently change the ability into unrestricted shapeshifting.

## 12. Reversion

Temporary biological transformation requires a deterministic reversion path.

Future state must answer:
- whether reversion is automatic or commanded;
- minimum resources needed;
- what happens if resources are low;
- whether partial reversion can persist;
- how save/load resumes an active transformation;
- how equipment interacts with transformed regions.

## 13. Repair versus transformation

If transformed tissue requires repair:
- Adaptive Arsenal remains responsible for the active form/template;
- a repair system may restore compatible transformed tissue only if the interaction is explicitly allowed;
- repair does not automatically unlock or alter templates;
- reversion must reconcile repaired transformed state back to the valid base state.

The exact stacking rule remains open.

## 14. State-transition classes

Use distinct transition categories:
- `REPAIR`;
- `SIGNALING_OVERDRIVE`;
- `REGENERATION`;
- `TRANSFORMATION`;
- `REVERSION`.

A single event should identify which category owns the change.

This prevents a repair effect from being interpreted as transformation or an overdrive effect as regeneration.

## 15. Resource interactions

Provisional resource directions:
- Knit Flesh: Focus + Stamina + target biological support;
- Bioelectric Overdrive: Stamina + Focus + recovery strain;
- Adaptive Regeneration: Stamina + Focus + biological reserve;
- Adaptive Arsenal: Stamina + biological reserve, with Focus only if later approved for precision.

No resource conversion is implied solely by coexistence.

## 16. Save/load requirements

Persist:
- biological reserve;
- recovery strain;
- active repair/regeneration state;
- adaptation-history entries;
- learned template IDs/versions;
- active transformation/reversion state;
- any ability transaction markers needed for deduplication.

Loading cannot duplicate reserve, template acquisition, repair completion, or transformation material.

## 17. Projection rules

Player-safe Status may display only known information.

Possible visible data:
- active known transformation;
- known template name;
- perceivable reserve/recovery status if the ability provides that awareness;
- revealed adaptation information.

Hidden biological requirements and undiscovered templates remain authoritative-only.

## 18. Cross-tier matrix

| Ability | State-change class | Target | Distinguishing law |
|---|---|---|---|
| Knit Flesh | REPAIR | self/touched target | accelerates natural repair |
| Bioelectric Overdrive | SIGNALING_OVERDRIVE | self | temporary performance signaling |
| Adaptive Regeneration | REGENERATION | primarily self | deeper repair plus history-dependent efficiency |
| Adaptive Arsenal | TRANSFORMATION / REVERSION | self | learned deliberate biological forms |

## 19. Required tests

Future minimum tests:
- Knit Flesh does not create an Adaptive Arsenal template;
- Bioelectric Overdrive does not automatically repair state;
- Adaptive Regeneration consumes/uses its bounded reserve model;
- regeneration adaptation applies only to qualified pattern categories;
- Adaptive Arsenal cannot activate an unknown template;
- transformation and reversion survive save/load deterministically;
- duplicate save/load cannot multiply biological reserve or templates;
- identity/progression state is not rewritten by biological repair;
- cross-ability stacking uses explicit rules.

## 20. Remaining design gates

Still open:
- biological reserve replenishment;
- exact mass/material accounting;
- Knit Flesh repair scope;
- Adaptive Regeneration pattern taxonomy;
- template acquisition method;
- transformation/reversion timing;
- transformed-state equipment rules;
- repair/transformation stacking;
- numeric costs/caps;
- institutional/world doctrine.

This standard resolves the shared biological state vocabulary without canon-promoting any ability.
