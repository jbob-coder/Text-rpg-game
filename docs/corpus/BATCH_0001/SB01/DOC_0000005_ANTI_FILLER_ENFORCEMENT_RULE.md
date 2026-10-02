# DOC_0000005 — Anti-Filler Enforcement Rule

Status: **REVIEWABLE**
Domain/program owner: D-07 Documentation / Coordination
Authority/evidence class: OWNER_DECISION + CONFIRMED_DOCUMENTED
Stable ID: DOC_0000005

Upstream: DOC_0000004; EXISTING::docs/production/PRODUCTION_CONTROL_ARCHITECTURE.md; EXISTING::docs/program/12_DOCUMENT_EXPECTATION_AND_ACCEPTANCE_STANDARD.md
Downstream: every manifest, document QA, scale-up decisions.

## Rule
A numbered file is allowed only when it owns a distinct project responsibility that would otherwise be ambiguous, duplicated, or lost.

Valid ownership includes authority, requirement, decision, schema, entity/content record, system specification, asset record, world record, implementation handoff, migration, test/verification contract, risk, evidence, or a distinct operational guide.

## Reject when
- created only to increase count;
- repeats another document without narrowing or operationalizing it;
- contains only a title or one-line restatement;
- invents details to fill sections;
- splits one indivisible rule into fragments with no independent consumers;
- copies mapped existing documentation without a new ownership role.

## Merge test
If two proposed files have the same upstreams, consumers, decision, and revision trigger, they probably belong together.

## Split test
Separate files are justified when ownership, consumers, revision triggers, evidence, implementation consequences, or lifecycle materially differ.

## Acceptance
A file passes anti-filler review when deleting it would remove a distinct piece of project control, specification, evidence, or content ownership.

## Revision trigger
Systematic over-fragmentation or a formal change in corpus granularity.

## Next action
Apply this rule before reserving future manifest entries and during every sub-batch QA pass.