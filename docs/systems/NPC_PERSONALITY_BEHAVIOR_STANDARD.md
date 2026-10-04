# THE GAME — NPC Personality & Behavior Standard

Status: **APPROVED FIRST-PASS V05 CONTRACT / CURRENT PRIMITIVES EXIST**
Parent:
- docs/systems/NPC_SOCIAL_AND_RIVAL_MASTER_PLAN.md
Current source:
- src/textrpg/social.py

## 1. Purpose

Define personality as durable behavioral tendency that influences decisions without becoming a deterministic script, random flavor label, or replacement for goals/knowledge.

## 2. Current authoritative axes

Current source defines:
- empathy;
- aggression;
- caution;
- ambition;
- honesty;
- loyalty;
- curiosity;
- discipline.

Do not add or rename axes casually because current content already uses these values.

## 3. Numeric range

Target normalized range:
- 0..100 inclusive.

Interpretation:
- 0 does not mean incapable;
- 50 is ordinary/neutral tendency;
- 100 does not force every action.

Values are tendencies consumed by authored rules.

## 4. Axis semantics

Empathy:
- sensitivity to harm/needs of others.

Aggression:
- preference for forceful/confrontational responses;
- not identical to hostility.

Caution:
- risk aversion and preference for information/safety.

Ambition:
- drive toward advancement/status/goals.

Honesty:
- tendency toward truthful/direct information sharing;
- constrained by secrecy, loyalty, fear, and orders.

Loyalty:
- tendency to preserve bonds/group commitments;
- distinct from relationship-axis loyalty toward a specific target.

Curiosity:
- tendency to investigate novelty/unknowns.

Discipline:
- tendency to follow plans/orders, resist impulsive deviation, and protect secrets.

## 5. Personality vs relationship

Personality is an actor trait.

Relationship is actor-to-target state.

Tamsin can have high personality loyalty while still having low relationship loyalty toward Jack early in the story.

Never collapse them into one field.

## 6. Personality vs goals

Goals specify what the NPC is trying to achieve.

Personality affects goal weighting, method choice, risk tolerance, and response to failure.

Personality does not create a goal without an authored goal-generation rule.

## 7. Personality vs knowledge

NPC choices must use what the NPC knows/believes.

High aggression cannot make an NPC attack a hidden target whose existence is unknown.

High curiosity cannot reveal secret knowledge.

## 8. Behavior scoring pattern

Recommended deterministic decision pattern:
decision_score =
- goal utility;
- relationship modifiers;
- personality modifiers;
- doctrine/role constraints;
- known risk;
- current condition;
- world/quest constraints.

Personality contribution should be bounded so one axis does not overwhelm all authored objectives unless design explicitly intends it.

## 9. Bounded modifiers

Design guidance, not current runtime formula:
- strong alignment may contribute roughly +0..20 utility;
- strong conflict may contribute -0..20;
- hard legal/order constraints can make an action illegal;
- goals/objectives generally outweigh mild personality preference.

## 10. Change over time

Personality changes more slowly than relationships.

Allowed mutation sources:
- major authored life event;
- long-term progression;
- persistent trauma/recovery if designed;
- deliberate character arc.

Routine dialogue choices should usually change relationships, memory, goals, or story state.

Any personality mutation should record source, before/after, clamp 0..100, append history, and be rare.

## 11. Current Tamsin baseline

Current authored values:
- empathy 55;
- aggression 20;
- caution 65;
- ambition 40;
- honesty 70;
- loyalty 60;
- curiosity 75;
- discipline 70.

These values make Tamsin a useful Phase 1 proof for curiosity toward Gate Twelve, cautious exploration, disciplined handling of dangerous knowledge, and non-aggressive companion behavior.

This is descriptive interpretation, not a new runtime formula.

## 12. Combat integration

Companion/enemy AI may consume personality through deterministic utility modifiers.

Examples:
- caution raises cover/withdraw utility;
- discipline raises adherence to orders;
- aggression raises offensive utility;
- empathy may reduce lethal preference where alternatives exist.

No axis overrides legal action constraints.

## 13. Information propagation

Current leak eligibility already consumes discipline, honesty, and secrecy.

Future rumor rules should use the same personality authority rather than duplicate gossip-chance fields.

## 14. Player visibility

Exact personality numbers are not player-facing by default.

UI may expose observed trait labels or known tendencies only when justified by player knowledge.

Developer diagnostics may show exact values.

## 15. Validation/tests

Required:
- every axis finite 0..100;
- unknown axes rejected in strict authored records;
- relationship loyalty stays independent;
- personality mutation atomic/clamped;
- same state produces same behavior modifiers;
- hidden information does not become available through personality;
- companion order behavior deterministic.

## 16. Migration

Preserve current PERSONALITY_AXES and NPC_TAMSIN values.

Add richer behavior around them; do not replace them with a generic personality-type label.
