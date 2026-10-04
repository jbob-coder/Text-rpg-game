# THE GAME — Status Knowledge & Visibility Standard

Status: **ACTIVE TARGET-GAME DESIGN**

Purpose: separate what exists in the rules from what a character, institution, or player is allowed to know.

## 1. Core rule

Existence is not visibility.

The authoritative system may know:
- hidden passive definitions;
- true rarity;
- undiscovered techniques;
- secret evolution paths;
- classified historical users;
- exact unlock requirements;
- concealed drawbacks.

The player-facing Status must reveal only information legitimately known/revealed.

## 2. Knowledge scopes

Every sensitive Status datum should support one or more scopes:

- SYSTEM_ONLY
- SELF_VISIBLE
- PUBLIC
- SCHOOL
- GOVERNMENT
- MILITARY_SECURITY
- RESEARCH
- FACTION_SPECIFIC
- CLASSIFIED
- PLAYER_DISCOVERED
- FALSE_PUBLIC_BELIEF

These scopes describe knowledge, not ownership.

## 3. Primary ability visibility

Potentially separate:
- true ability identity;
- public ability name;
- true rarity;
- public rarity;
- known techniques;
- hidden techniques;
- known drawback;
- hidden drawback;
- evolution path;
- cosmic/system classification.

A user may know more about their own ability than the public, but self-knowledge is not automatically complete.

## 4. Passive visibility

Before qualification:
- no name;
- no icon;
- no slot;
- no progress percentage;
- no exact requirement.

After qualification/reveal:
- passive becomes visible to the owner;
- public/institutional visibility still depends on separate rules;
- hidden future stages remain hidden.

## 5. Awakening event visibility

The public awakening/classification event does not automatically authorize full Status disclosure.

Future event design must define:
- publicly announced fields;
- school-only fields;
- government record fields;
- protected/classified fields;
- emergency suppression rules;
- consent/privacy rules;
- deliberate concealment/fraud handling.

## 6. Misclassification

The setting may support:
- incomplete classification;
- public alias;
- suppressed rarity;
- false public record;
- mistaken interpretation;
- ability evolution invalidating old assumptions.

Misclassification must be authored; UI should not randomly lie without a source.

## 7. Hidden requirements

Requirement data is internal until discovered.

The world may contain:
- exact method;
- partial method;
- theory;
- rumor;
- false method;
- dangerous counterfeit method.

Player knowledge should cite provenance when possible.

## 8. Classified knowledge

High-value abilities/passives may be classified because of:
- military value;
- assassination risk;
- destabilizing unlock method;
- forbidden experiments;
- cosmic significance;
- enemy intelligence risk.

Classification level is world-state metadata and may differ by government/faction.

## 9. Player-safe projection rule

When implemented:
- engine keeps full authoritative record;
- projection removes fields outside current visibility;
- Android renders only projection;
- hidden registries are never inferred client-side;
- debugging tools must remain separate from player UI.

## 10. Discovery events

A discovery event may reveal:
- passive existence;
- unlock method;
- technique requirement;
- true rarity;
- historical user;
- drawback;
- counter.

Discovery should create durable knowledge state.

## 11. Reconstruction acceptance

Another developer must be able to answer:
- who knows a Status fact;
- why they know it;
- whether the player can see it;
- whether it is true, false, partial, or classified;
- what event changes visibility.
