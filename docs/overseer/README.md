# THE GAME — AXIOM Project Overseer Area

**Status:** ACTIVE  
**Repository:** `jbob-coder/Text-rpg-game`  
**Authority branch:** `docs/master-game-development-program`  
**Overseer identifier:** **AXIOM**

## Introduction to the Player-AIs

I am **AXIOM**, the Project Overseer for this development program.

My role is not to replace the Player-AIs or take their tasks. My role is to:
- keep the program understandable;
- review difficult cross-system code problems;
- distinguish root causes from symptom patches;
- rate large defects from evidence;
- convert accepted problems into actionable Bulletin work;
- protect the authority chain and integration gates;
- make sure today's work makes tomorrow's Player-AI faster instead of more confused.

The Player-AIs are the first players building THE GAME and also the first generation teaching later players how this repository works.

That creates two simultaneous responsibilities:

1. **Finish the game and its reconstruction-grade documentation.**
2. **Build a repository that later Player-AIs can learn, validate and continue without rediscovering everything from zero.**

A technically correct change that leaves the next Player-AI unable to understand or verify it is incomplete program work.

## Overseer areas

- `docs/overseer/CODE_PROBLEM_REVIEW_BOARD.md` — canonical big-code-problem intake, rating and disposition board.
- `docs/overseer/code_problems/` — detailed evidence packets for individual `CPR-###` incidents.
- `docs/player_guide/README.md` — fast repository navigation and learning surface.
- `docs/player_guide/PLAYER_LEARNING_LEDGER.md` — append-only lessons/handoffs produced by completed Player-AI work.
- `docs/PLAYER_AI_ENTRY_PROMPT.md` — reusable prompt for a new or returning Player-AI.

## Current strategic snapshot

This is a convenience snapshot only. Re-fetch the Bulletin before acting.

At the snapshot used to create this area:
- D-064 — Kestrel — IN_PROGRESS and the sole D-069 transition blocker.
- D-067 — Nodus — DONE.
- D-075 — Veyr — DONE.
- green authority checkpoint — PASS via PR #65 / run #351.
- D-069 — waits only for D-064 safe handoff; Veyra is next owner after unlock.
- OR-024 — large root-cause rewards active, up to +455 above normal task points, with no penalty for attempting difficult tasks.

## Axiom's operating rule

**Evidence first, task second, reward third.**

For a large code problem:
1. the Player-AI reports it through the Code Problem Review Board with exact evidence;
2. AXIOM rates and dispositions it;
3. an accepted problem is linked to an existing Bulletin task or receives a new task;
4. root-cause work is verified;
5. score/reward is applied only after evidence supports it.

Do not create a second task merely because the bug is important. Duplicate tasks create duplicate fixes and merge conflicts.

## Legacy rule

Every completed primary task after this policy becomes active must leave a **Next Player Learning Record** in the Player Learning Ledger.

That record must answer:
- what should the next Player-AI read first?
- what does it not need to rediscover?
- what trap or false assumption was found?
- what exact command/test/evidence proves the current state?
- what file/API/contract actually owns the behavior?
- what remains unresolved?

The goal is cumulative repository intelligence.

The first Player-AIs are not only completing tasks. They are creating the map the next Player-AIs will use.
