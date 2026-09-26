# Project Checkpoints

Append-only checkpoints for reconstructing project state across chats.

---

## CHECKPOINT_ID: CP-2026-09-27-STATS-SCHEMA-01

Repository: `jbob-coder/Text-rpg-game`
Context branch: `shared/game-context`
Implementation branch referenced by existing status docs: `foundation/text-rpg-systems`

### CURRENT_OBJECTIVE

[DIRECTION] Design the game's stat schema and broader system catalog in enough detail that multiple chats can contribute without drifting. The immediate shared task is **design architecture**, not runtime implementation.

### DIRECTION

[DIRECTION] The game is a life-and-decisions text RPG with slow progression, meaningful consequences, persistent world/character state, earned capability, and a world that feels alive because earlier actions alter later states.

[DIRECTION] Progress should not come from trivial or instantaneous gains. Attributes move slowly; narrower skills/mastery can advance faster.

[DIRECTION] Important continuity must live in structured game state and stable IDs, not only prose or chat memory.

### VERIFIED_STATE

[VERIFIED] The shared context branch contains the existing game foundation, implementation-status, systems catalog, reference notes, visual bible, and the new context architecture index.

[IMPLEMENTED] Existing repository files currently define a seven-attribute catalog: `might`, `agility`, `endurance`, `intellect`, `will`, `perception`, `presence`.

[IMPLEMENTED] Existing repository design/code also includes skills, derived values, resources, training, conditions/injuries, recovery, equipment, equipment sets, NPC memory/knowledge, and deterministic secret-propagation support.

### DESIGNED_NOT_IMPLEMENTED

[DESIGNED] This chat proposed an expanded eight-attribute model that separates Agility and Dexterity and uses Constitution as a dedicated robustness attribute:
`STR / CON / AGI / DEX / PER / INT / WIL / PRE`.

[DESIGNED] The intended layer model is:
`core attributes -> resources -> derived statistics -> abilities -> mastery -> techniques -> evolution`.

[DESIGNED] Character level, ability level, mastery, technique progression, and evolution progression should remain separable concepts.

### CONFLICTS

[CONFLICTING] `STAT-ATTR-001`: current repository has seven core attributes; this chat has proposed eight. The key unresolved issue is whether `agility` should continue covering coordination/precision or whether `dexterity` becomes a separate core attribute. Do not change executable code until the design is intentionally resolved.

### COMPLETED

[VERIFIED] Added `docs/context/README.md` defining authority order, state labels, branch roles, anti-drift rules, and canonical reading order.

[VERIFIED] Added `docs/context/CONTEXT_SYNC_PROTOCOL.md` defining markup, checkpoint, handoff, conflict, and compression rules.

### IN_PROGRESS

[DESIGNED] Build a complete, non-redundant stats/system architecture and compare it against the current seven-attribute foundation before selecting the canonical schema.

### NEXT_ACTION

1. Define the responsibility boundary for every candidate core attribute.
2. Test the schema against physical combat, stealth, social play, investigation, technical tasks, injury/recovery, training, powers, and life-simulation decisions.
3. Remove redundant attributes or split overloaded ones.
4. Define which values are core attributes vs skills vs resources vs derived values.
5. Record the resolved schema in `DECISIONS.md` before implementation changes.

### BLOCKERS

[BLOCKER] No implementation blocker. Canonical stat-schema selection is intentionally unresolved.

### RISKS

[RISK] Too many core stats can make the UI and balancing unreadable.
[RISK] Too few core stats can make attributes overloaded and reduce build identity.
[RISK] Renaming or splitting already implemented attributes will require save/schema migration if done after content expands.

### FILES_CHANGED

- `docs/context/README.md`
- `docs/context/CONTEXT_SYNC_PROTOCOL.md`
- `docs/context/CHECKPOINTS.md`

### TESTS_RUN

None by this chat for this design checkpoint.

### TEST_RESULTS

[UNKNOWN] Existing `IMPLEMENTATION_STATUS.md` reports 29 passing tests from earlier branch-equivalent verification. This chat has not rerun them and does not claim fresh verification.

### EVIDENCE

- `docs/GAME_FOUNDATION.md`
- `docs/SYSTEMS_CATALOG.md`
- `docs/IMPLEMENTATION_STATUS.md`
- current conversation direction
