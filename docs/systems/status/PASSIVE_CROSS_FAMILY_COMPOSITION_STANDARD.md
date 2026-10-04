# THE GAME — Passive Cross-Family Composition & Ownership Standard

Status: **PROVISIONAL CROSS-FAMILY DESIGN STANDARD / NOT CANON / NOT IMPLEMENTED**

Purpose: prevent the 23 Wave-001 passive families from stacking into uncontrolled duplicate modifiers or leaking responsibility between state owners.

## 1. Core rule

Each passive effect must modify one explicitly named authoritative resolution term or one clearly defined state transition.

A passive does not directly rewrite a final outcome merely because its description sounds relevant.

## 2. Effect stages

Use these provisional effect stages:

- `SIGNAL_INPUT` — what information physically reaches the character;
- `INTERPRETATION` — how available information is interpreted;
- `DECISION` — selection/prioritization among known options;
- `EXECUTION` — physical/technical/social execution quality;
- `RESOURCE_COST` — cost paid by an action/process;
- `RESOURCE_RECOVERY` — valid recovery amount/rate;
- `STATE_RECOVERY` — return from a condition or disruption state;
- `FAMILIARITY` — reduced friction for a known domain/task/context;
- `RESISTANCE` — bounded reduction to an incoming effect;
- `KNOWLEDGE_RECALL` — retrieval of already acquired information;
- `AUTHORIZATION_WORKFLOW` — operating more reliably inside already valid institutional permissions.

A passive should normally own one primary stage.

## 3. Same-term stacking

If two or more passives modify the same authoritative term:
1. gather eligible modifiers;
2. reject duplicate ownership of the same passive ID;
3. apply any family-specific eligibility gates;
4. combine through one capped resolver;
5. enforce a hard minimum/maximum result;
6. record contributing passive IDs for audit/debug;
7. expose only player-safe information.

Do not multiply independent percentage discounts by default.

## 4. Different-stage composition

Passives on different stages may coexist.

Example:
- a sensory passive improves interpretation;
- a combat habit improves decision timing;
- a weapon-familiarity passive improves execution.

They can all contribute because they act on distinct stages.

This is safer than letting all three modify one global “success chance.”

## 5. Familiarity scoping

Any passive using familiarity must identify its scope:
- task;
- tool/equipment;
- terrain;
- environment;
- species;
- profession;
- institution;
- technique;
- team;
- injury/rehabilitation context.

Familiarity does not automatically transfer across scopes.

Cross-domain transfer requires an explicit relationship rule.

## 6. Core-resource protection

Health, Stamina, Focus, and Resolve remain authoritative core resources.

A passive that:
- reduces drain;
- improves recovery;
- reduces ramp-up cost;
- improves pacing

must identify which exact resource transition it affects.

No passive creates resources from nothing unless a separate approved law explicitly does so.

## 7. Damage / injury / condition separation

Passives that improve:
- bracing;
- balance;
- flinch control;
- pain distraction;
- recovery;
- environmental tolerance

must not silently reduce underlying damage/injury unless their record explicitly targets that resolver.

## 8. Knowledge protection

Passives may improve:
- recall;
- interpretation;
- pattern recognition;
- confidence calibration.

They may not fabricate:
- hidden facts;
- secret intentions;
- unknown contacts;
- unobserved species traits;
- unpublished Status information;
- unauthorized classified data.

## 9. Agency protection

Social and leadership passives may improve the user's behavior, communication, coordination, or interpretation.

They do not directly overwrite another person's:
- decision;
- emotion;
- loyalty;
- consent;
- relationship;
- belief.

Any future mechanic that actually alters another mind requires its own explicit governing law.

## 10. Authorization protection

Profession, faction/institution, classified, and system-related passives may improve operation inside valid permissions.

They do not:
- grant rank;
- create credentials;
- bypass clearance;
- create authorization;
- convert familiarity into system administration.

## 11. Event-bound passives

Unique Event, Cosmic/System, and Unknown/Classified passives require stable event or requirement-packet IDs.

They must be non-farmable by repetition unless the parent record explicitly says otherwise.

Save/load must not duplicate one-time qualification.

## 12. Exploit-resistance requirements

Future tests must cover:
- duplicate passive IDs;
- multiple passives touching one term;
- save/load replay;
- stale projection;
- trivial event repetition;
- invalid familiarity transfer;
- resource underflow/overflow;
- hidden-information leakage;
- authorization bypass;
- condition/damage bypass through unrelated modifiers.

## 13. Debug/audit requirement

The authoritative resolver should eventually be able to explain:
- base term;
- eligible passive IDs;
- rejected passive IDs and why;
- cap applied;
- final authoritative term;
- projection-safe result.

This does not require exposing internal math to the player.

## 14. Promotion gate

No passive should move from calibration to implementation mapping until:
- its primary effect stage is identified;
- its authoritative state owner is identified;
- same-term overlaps are listed;
- cap behavior is defined;
- hidden-information impact is reviewed;
- save/load and exploit tests are specified.

No Wave-001 passive is canon-promoted by this standard.
