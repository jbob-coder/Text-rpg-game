# THE GAME — Passive Knowledge Profile Reconciliation Audit — Wave 001

Status: **PHASE-C AUDIT / COMPACT ROWS UNCHANGED / NOT CANON**

Parents:
- `STATUS_KNOWLEDGE_VISIBILITY_STANDARD.md`
- `KNOWLEDGE_EVIDENCE_CONFIDENCE_STANDARD.md`
- `calibration/PASSIVE_KNOWLEDGE_WAVE_001.md`
- family knowledge-refinement files.

Purpose: identify where Wave-001 knowledge profiles are still calibration scaffolding rather than believable world-specific knowledge.

## Structural finding

The compact knowledge registry has **230 rows**.

Of those:
- **200 rows** belong to 20 ordinary passive families;
- **30 rows** belong to the special Unique Event, Cosmic/System, and Unknown/Classified families.

For the 20 ordinary families, the knowledge profile is an exact ordinal template:
- every `0001` row uses the same knowledge posture;
- every `0002` row uses the same posture;
- ...
- every `0010` row uses the same posture.

This means the ordinary-family compact knowledge layer is structurally complete but not yet individualized enough to represent a believable world.

## Exact ordinary-family template

| Ordinal | Count | Current compact posture | Reconciliation status |
|---|---:|---|---|
| 0001 | 20 | public/school/government known; faction mixed | plausible default, still needs family-specific provenance |
| 0002 | 20 | public rumored; institutions broadly know | plausible default |
| 0003 | 20 | public unknown; school rumored; government known; faction secret | justification required |
| 0004 | 20 | public/school unknown; government/faction classified | high-priority individualization |
| 0005 | 20 | public false belief; school partial; government known | false belief must be individually authored |
| 0006 | 20 | broadly known | plausible default |
| 0007 | 20 | public rumored; institutional knowledge mixed | plausible only with family-specific reasons |
| 0008 | 20 | unknown in all ordinary scopes | high-priority individualization |
| 0009 | 20 | public/school known; classified government detail | classification rationale required |
| 0010 | 20 | public false belief; school rumored; government/faction restricted | high-priority individualization |

## Audit conclusion

The repeated pattern was useful for testing the knowledge schema, but it must not be mistaken for final world canon.

A passive's ordinal position inside a calibration family is not a valid reason for:
- secrecy;
- classification;
- public rumor;
- false belief;
- institutional ignorance.

## Priority tiers

### Tier A — strongest mismatch risk
Review every ordinary-family:
- `0004`;
- `0008`;
- `0010`.

That is **60 compact rows** requiring individual world justification or revision.

### Tier B — strong context requirement
Review every ordinary-family:
- `0003`;
- `0009`.

That is **40 additional rows** where institutional/public asymmetry needs a concrete reason.

### Tier C — authored-content requirement
Every `0005` false-belief row requires an actual false recipe/rumor and provenance.

That is **20 rows**.

### Tier D — plausible baseline but not finished
`0001`, `0002`, `0006`, and `0007` can remain provisional more easily, but still require world-specific provenance before canon promotion.

## Reconciliation rule

For each compact row eventually record:
- existence knowledge by scope;
- unlock-method knowledge by scope;
- confidence/truth state;
- provenance/source;
- institution/faction owner where applicable;
- classification reason;
- false rumor text where applicable;
- historical cases;
- region/time variation;
- discovery/declassification event.

Do not collapse these into one generic “known/unknown” field.

## Classification rule

A `GOV_CLASSIFIED` or `FACTION_CLASSIFIED` claim is incomplete unless the world defines:
- which government/faction;
- which office/unit or role class;
- why the information is restricted;
- what exactly is classified: existence, effect, trigger, user identity, history, or method;
- who can access it;
- what changes that access.

“Government knows” is not a sufficient final world record.

## All-unknown rule

A `PUBLIC_UNKNOWN / SCHOOL_UNKNOWN / GOV_UNKNOWN / FACTION_UNKNOWN` profile is especially difficult to justify for repeatable passives.

Before retaining it, document:
- why repeated users have not created reliable records;
- whether the effect is subtle/misattributed;
- whether Status suppresses disclosure;
- whether the passive is genuinely extremely rare;
- whether evidence is systematically destroyed or isolated.

Otherwise revise the posture during explicit canon review.

## False-belief rule

A false belief must include:
- the actual claim;
- origin;
- population that believes it;
- why it persists;
- risk/consequence;
- evidence that could correct it.

Do not keep `PUBLIC_FALSE_BELIEF` as an empty label.

## Special-family result

### Unique Event
Current case-dependent knowledge model is structurally appropriate.

Final knowledge must come from the authored event and its witnesses/records.

### Cosmic / System
The disputed/rumored model is plausible provisionally, but `GOV_CLASSIFIED_OR_UNCONFIRMED` must not be read as proof that a government knows the truth.

### Unknown / Classified
Compartmented knowledge is appropriate for this calibration family, but every row eventually needs an actual requirement-packet owner and classification authority.

## Registry policy

This audit does **not** rewrite `PASSIVE_KNOWLEDGE_WAVE_001.md`.

Compact rows stay as calibration proposals until:
1. world integration supplies real institutions/events/provenance;
2. family audits recommend an individualized posture;
3. explicit owner/canon review approves the change.

## Acceptance target

The compact knowledge registry becomes reconstruction-grade only when a future developer can answer for every passive:
- who knows it;
- what they know;
- why they know it;
- how certain they are;
- whether the knowledge is true/partial/false;
- where/when that knowledge applies;
- what event can change visibility.

No passive is canon-promoted by this audit.
