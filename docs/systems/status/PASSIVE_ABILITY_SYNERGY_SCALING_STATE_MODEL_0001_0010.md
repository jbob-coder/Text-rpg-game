# THE GAME — Ability Synergy Passive Scaling & State Model 0001–0010

Status: **PHASE-C CALIBRATION / NOT CANON / NOT IMPLEMENTED**

Purpose: define bounded scaling and authoritative state categories for `PASSIVE_SYN_0001`–`PASSIVE_SYN_0010`.

## Shared state

Future implementation should distinguish:
- `qualification_state`;
- `ownership_state`;
- `primary_ability_identity`;
- `mastery_state`;
- `technique_state`;
- `ability_resource_state`;
- `ability_strain_state`;
- `recovery_state`;
- `counter_history`;
- `evolution_signal_state`;
- `projection_state`.

## Per-record model

| ID | Effect input | Scaling direction | Hard cap |
|---|---|---|---|
| SYN_0001 | recovery-transition inefficiency after ability use | validated ability-use/recovery history | no free resource generation |
| SYN_0002 | unnecessary technique execution overhead | high mastery of one known technique | cannot remove required steps/cost |
| SYN_0003 | instability variance during repeated known technique use | validated repeated technique history | no immunity to failure/overload |
| SYN_0004 | missed personal overuse warning cues | reviewed overuse/strain history | cannot expose unknown hidden system data |
| SYN_0005 | post-ability recovery inefficiency | valid recovery history | recovery rules/caps remain authoritative |
| SYN_0006 | control error at deliberately reduced output | precision practice with same ability law | cannot create new output modes |
| SYN_0007 | dual-task performance loss | simple-effect + familiar-task practice | no unlimited multitasking |
| SYN_0008 | learning friction after documented counter | reviewed counter encounters | does not reveal every future counter |
| SYN_0009 | Focus overhead for low-complexity familiar use | extensive safe use history | no zero-cost ability use |
| SYN_0010 | recognition error for legitimate evolution signals | validated mastery/discovery history | no automatic future-technique reveal |

## Qualification rules

The compact records currently require:
- primary ability uses;
- mastery stage at least learned;
- controlled overuse review.

Future qualification must:
1. bind evidence to stable ability/technique IDs;
2. count each valid use/review once;
3. reject trivial zero-cost use loops;
4. reject intentionally reckless overuse as an efficient qualification path;
5. preserve hidden progress outside ordinary Status projection.

## Cross-family overlap watchlist

- Resource Cycling / Recovery Channel ↔ Recovery family;
- Technique Compression ↔ Procedural Chunking;
- Cast Stability ↔ Mental/Will Focus Under Fire;
- Overuse Warning ↔ sensory/interoceptive systems;
- Precision Scaling ↔ ability mastery;
- Dual-Task Control ↔ Cognitive/Mental-Will multitask handling;
- Counter-Feedback ↔ Error Memory / Analytical Habit;
- Ability Familiarity ↔ core ability mastery/cost system;
- Evolution Sensitivity ↔ awakening/evolution discovery standards.

Same-resolver effects use one capped composition path.

## Required tests

- primary-ability identity remains singular;
- passive cannot create a new technique or evolution unless parent rules permit;
- resource effects cannot create free Focus/Stamina/Resolve or ability reserves;
- overuse-warning state does not expose hidden developer values by default;
- duplicate ability-use events do not double-count;
- save/load preserves qualification exactly once;
- player-safe projection reveals only legitimately discovered evolution information.

No runtime module is claimed here.
