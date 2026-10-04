# Conversation Context — Evolved Game Documentation Framing

Recorded: 2026-10-03 AST
Repository: `jbob-coder/Text-rpg-game`
Program branch: `docs/master-game-development-program`

## Owner correction

The current game is the reference point for creating the evolved game.

The documentation program is not migration-first. Its immediate purpose is to understand what exists, preserve the identity of the game, deliberately design the larger/upgraded version, enumerate what must be created, and only then let implementation follow that design.

Required sequence for each domain:

1. CURRENT REALITY
2. PRESERVE IDENTITY
3. EVOLVED GAME DESIGN
4. CREATION REQUIREMENTS
5. IMPLEMENT LATER

Migration/API/save work remains necessary only when later implementation changes durable contracts. It is downstream of the game-design objective.

## First selected domain

Progression / Classes / Ranks.

Primary evolved design:
- `docs/systems/PROGRESSION_CLASSES_RANKS_EVOLVED_GAME_DESIGN.md`

Next children:
- full 23-skill registry;
- combat class catalog;
- profession/rank/status namespace;
- training/mentor/facility standard;
- Gate Twelve progression proof packet;
- progression UX contract.
