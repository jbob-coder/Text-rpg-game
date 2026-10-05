# THE GAME — AI Brag Room

**Status:** ACTIVE  
**Purpose:** evidence-backed accomplishment log and cross-agent handoff channel.

This is the repository-native "chat room" where AI agents record what they actually shipped. It is intentionally more informal than the master task register, but it may never contradict repository evidence.

## Rules

1. Brag only after a primary task is genuinely complete or after a meaningful verified bonus.
2. Every claim must point to evidence: commit/HEAD, files, tests, build/run IDs, artifact hashes, or documented audit output as applicable.
3. Never claim a test/build/device result that was not executed and observed.
4. Never turn proposal into canon in a brag entry.
5. Keep hidden/private game state out of player-facing screenshots or prose.
6. Before taking the next primary task, append the completed task's Brag Card here.
7. If the agent is running inside an interactive ChatGPT conversation, also post a concise version of the Brag Card in the active chat so the user and later AI agents can see the accomplishment. If the agent has no chat-posting capability, this repository entry is sufficient and remains canonical.
8. A bonus gets its own line/card but cannot disguise an incomplete primary task.
9. Other agents may respond by appending a short `CHALLENGE ACCEPTED` note when they claim the next task; never edit another agent's historical brag entry.

## Brag score

- P0-CRITICAL primary complete: 100
- P0 primary complete: 90
- P0/P1 primary complete: 75
- P1 primary complete: 60
- Verified bonus: +20

Score has no authority. Evidence and correctness outrank score.

## Brag Card template

### BRAG — <TASK_REF> — <short title>
- **AGENT:** <agent/session identifier>
- **CLAIM_HEAD:** <sha>
- **COMPLETION_HEAD:** <sha>
- **SCORE:** <base + optional bonus>
- **WHAT I SHIPPED:** <concise factual summary>
- **BUGS / GAPS I KILLED:** <what was actually resolved>
- **PROOF FLEX:** <tests/builds/audits and exact results>
- **FILES / ARTIFACTS:** <key paths / artifact hashes>
- **PHASE 1 / PROGRAM IMPACT:** <requirements/dependencies changed>
- **BONUS:** <done/not done + evidence>
- **UNVERIFIED / STILL BLOCKED:** <honest remaining boundary>
- **NEXT AI UNLOCK:** <next eligible task(s)>
- **MESSAGE TO NEXT AI:** <short challenge/handoff>

## Challenge claim template

### CHALLENGE ACCEPTED — <TASK_REF>
- **AGENT:** <agent/session identifier>
- **CLAIM_HEAD:** <sha>
- **WHY THIS TASK:** <dependency/rank reason>
- **I WILL PROVE:** <acceptance criteria summary>

## Hall of verified wins

No campaign brag entries recorded yet. Add entries; do not rewrite history.
