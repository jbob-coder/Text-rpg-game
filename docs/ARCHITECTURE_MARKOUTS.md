# Architecture Markouts

Purpose: provide fixed reference points for reconstructing the project when multiple chats or long-running changes make the state difficult to follow.

A markout is not a claim that work is complete. It is a named architectural boundary that tells a contributor where truth should live and what must be checked before changing it.

## M-001 — Authoritative Playthrough State

Authority: `GameState` and versioned save data.

Owns durable playthrough facts such as current scene, time, player state, flags, relationships, knowledge, inventory, quests, and important history.

Rule: if future content must react to a fact, that fact needs stable state rather than prose-only continuity.

## M-002 — Deterministic Resolution

Authority: rules/check-resolution code plus seed/turn state.

Owns reproducible action outcomes, degree-of-success bands, gates, and effects.

Rule: the same authoritative state, seed, and action should resolve identically unless the rules version intentionally changes.

## M-003 — Character Progression

Authority: player attributes, skills, resources, abilities/mastery, conditions, perks, equipment, and training systems.

Rule: permanent attributes move slowly; temporary and equipment effects must not mutate base attributes just to represent a modifier.

## M-004 — Effective Modifier Pipeline

Authority: effective-stat/check calculation helpers.

Owns the composition order for base values plus conditions, equipment, set bonuses, perks, and contextual effects.

Rule: each modifier source must be applied exactly once. Helper functions that expose a modifier must not also mutate the base value behind the caller's back.

## M-005 — NPC Information Boundary

Authority: NPC private knowledge, player knowledge, memories, relationship axes, authored social network, and information-propagation events.

Rule: knowledge is owned by a specific actor. A fact does not become globally known merely because it exists in content.

## M-006 — Quest and Story Graph

Authority: stable scene/quest IDs, quest stages, branch effects, failure states, and content validation.

Rule: branching prose can recombine, but durable consequences must remain inspectable in state.

## M-007 — Presentation Boundary

Authority: visual bible, character identity specs, client/UI runtime.

Rule: presentation consumes rules state; it does not become the authority for game rules or save continuity.

## M-008 — External Reference Boundary

Authority: `docs/REFERENCE_NOTES.md` for abstract lessons only.

Rule: source novels, games, and other references may inform abstract mechanics, but names, protected prose, characters, setting, dialogue, and unique story elements are not project canon.

## M-009 — Cross-Chat Context

Authority: repository files first; per-chat records under `docs/chat_context/` second.

Rule: each chat owns its own context file. No chat overwrites another chat's record. Canonical docs are updated only after verification.

## M-010 — Verification Boundary

Authority: executed tests, validation output, commit state, and reproducible commands.

Rule: historical test results remain evidence of that historical state only. Never claim the current branch passes until the current code has actually been verified.

## Markout use

Before a non-trivial change, identify the markouts touched. After the change, record which invariants were preserved, which files changed, what was tested, and any unresolved conflict.
