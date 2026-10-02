# DOC_0000018 — Supersession Trace Rule

Status: **REVIEWABLE**
Domain/program owner: D-07 Documentation / Coordination
Authority/evidence class: CONFIRMED_DOCUMENTED
Stable ID: DOC_0000018

Upstream: DOC_0000001; DOC_0000006; DOC_0000012; DOC_0000016; DOC_0000017
Downstream: historical preservation, decision logs, migration, stale-pointer cleanup.

## Rule
New authority must not silently erase older authority. Supersession is explicit and traceable.

## Required trace
When document B replaces document A:
- mark A as SUPERSEDED where practical;
- identify B as the superseding authority;
- identify the reason for replacement;
- preserve historical provenance;
- review downstream consumers of A;
- update active indexes/pointers.

## ID rule
If ownership changes materially, the new authority receives a new immutable DOC ID. The old ID remains permanently reserved.

## Partial supersession
If only part of a document is replaced, record the exact section/decision affected rather than marking unrelated content obsolete.

## Acceptance
A future session can determine what was authoritative before, what replaced it, and why.

## Revision trigger
Change if historical retention or graph semantics change.

## Next action
Use this rule during stale-pointer remediation and future architectural replacements.