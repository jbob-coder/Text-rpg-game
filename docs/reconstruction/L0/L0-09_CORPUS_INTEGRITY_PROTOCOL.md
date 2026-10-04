# L0-09 — Corpus Integrity Protocol

Layer: **L0 Foundation**
Depends on: L0-00 (protocol), L0-07 (prohibitions)
Governs: every write to this corpus

---

## 1. Why this document exists

During construction of this corpus, seven defects were produced and caught. They
are listed here because the *pattern* matters more than the individual errors:
every one of them was either silent or plausible, and none would have been
visible to a reader without an explicit check.

Crashes are safe. A crash stops the work. **Plausible output that is wrong,
stated confidently, is the dangerous failure** — because a rebuild cannot tell
which parts of an authority document to trust.

This document therefore defines a verification step that runs after every
generation, before content is considered delivered.

## 2. Observed failure modes

| # | Failure | What happened | How it was caught |
| ---: | --- | --- | --- |
| 1 | **Truncation** | A write was cut off mid-document; the deliverable was believed complete but was absent | New `no truncated documents` check |
| 2 | **Index off-by-one (1st)** | Block slicing produced a palette with 6-character hex values carrying a stray prefix | Cross-check against an independent source |
| 3 | **Index off-by-one (2nd)** | Same class of error while re-running the palette comparison | Fixed after the first was fixed; see §3 |
| 4 | **Regex over-capture** | A node-name list adjacent to pixel rows was parsed as malformed rows; a **non-existent defect** was nearly reported as canon | Row-width assertion against the declared grid |
| 5 | **Format mismatch** | Batch catalogs contain literal `\n` sequences; a parser returned 100 of 500 rows, which looked like 400 missing units | Count assertion; parse retried with unescaping |
| 6 | **Stale assertion** | "64 branches" written into a document from a pre-fetch listing; the measured count was 60 | Post-fetch recount; corrected in place with a note |
| 7 | **Ignored existing tooling** | A custom PNG decoder was written before discovering the repository's own verifier | Repository tooling survey |

Defects 2, 3, 4 and 6 are the serious ones: each produced output that looked
correct. Defect 4 would have added a fictional bug to an authority document.

## 3. The verification step
Verification is mechanical where it can be and judgement-based where it must
be. The harness below covers the mechanical part; §4 covers the rest.

### 3.1 The harness

`tools/verify_reconstruction_corpus.py`, in the repository, standard library
only. Run it after every generation step:

```bash
python tools/verify_reconstruction_corpus.py
python tools/verify_reconstruction_corpus.py --json evidence.json   # machine-readable
```

Exit code `0` on pass, `1` on failure. Every check maps to an observed failure.

| Check | Guards against |
| --- | --- |
| `no truncated documents` | an interrupted write leaving a partial deliverable |
| `code fences balanced` | an unterminated fence swallowing content |
| no literal newline escapes in corpus prose | unescaped writes and format mismatches |
| `no empty h2 sections` | headings whose entire body is empty to a reader |
| `no duplicate headings` | ambiguous numbering and cross-references |
| `relative links resolve` | cross-references to documents that do not exist |
| `registry markdown/json agree` | two generated companions drifting apart |
| no unresolved placeholder markers | unfinished work presented as specification |
| `layer cross-references resolve` | a layer citing a document that was never written |

The harness is a **floor, not a ceiling**. It cannot detect a wrong palette or
an invented fact. Those still require the reasoning checks in §4.

### 3.2 The generation rule

> Generate → verify → write → verify again → only then commit.

A generated artifact is not a deliverable until the harness passes. If a
deliverable is too large to write in one pass, it is written in sections and the
harness is run between them — which is how failure 1 is prevented.

## 4. Reasoning checks the harness cannot perform

These are judgement obligations, not automatable, and they are where the real
risk lives.

### 4.1 Verify before asserting

Before writing a factual claim into this corpus, confirm it from a primary
source. Specifically:

- **Counts** must be measured, not estimated. "60 branches", not "~64".
- **Palettes** must be decoded from bytes, not read from a palette declaration.
- **Row structures** must be asserted against their declared grid.
- **Identities** must come from the source document, not from memory.

### 4.2 Prefer the repository's own tooling

Before writing a script to inspect repository state, check whether the
repository already has one. `tools/verify_pixel_raster_equivalence.py` already
answered the raster-equivalence question; writing a second decoder produced
weaker evidence and wasted effort.

### 4.3 Distinguish "no defect found" from "defect found"

A failed check is a claim about the world. Before recording it, confirm the
check itself is correct. Failure 4 was a defect in the *check*, reported as a
defect in the *art*.

### 4.4 Record corrections in place

When a correction is needed, fix the document **and** state what was wrong, in
the document or in the build log. A silent correction leaves the reader unable
to judge which statements are trustworthy.

### 4.5 Prefer machine-checkable claims

Where a statement can be made assertable, make it assertable:

- registry counts → both Markdown and JSON, verified equal;
- raster evidence → a JSON file with per-pixel measurements;
- integrity → the harness.

A corpus whose claims can be re-verified is trustworthy in a way a prose-only
corpus is not.

## 5. What this does not protect against

Stated plainly, so the corpus's reliability is not overclaimed:

| Risk | Not caught by | Mitigation |
| --- | --- | --- |
| An invented fact that reads plausibly | the harness | review against the source authority; `NOT SPECIFIED IN DOCS` is always available |
| A wrong but well-formed interpretation | the harness | reasoning review (§4) |
| Canon drift from an upstream authority changing | the harness | conflict rule in `README.md` §3 |
| A reference image that becomes unreachable | the harness | L1-00 records identity + hash so retrieval can be validated |
| Silent omission — a topic simply not written | the harness | the layer index states what each layer must deliver |
| Model unavailability mid-task | the harness | commit per layer; §6 |

## 6. Persistence rule

**Commit per layer, and per substantial section within a layer.**

A commit is the only durable boundary against interruption. In this session an
interrupted response lost an entire deliverable; had the preceding work not
been committed, it would have been lost too.

Rule: never leave completed work uncommitted. Push when a layer is complete.

## 7. Applying this to subagents and future passes

Any agent — including a delegated subagent — that writes into this corpus must:

1. run `tools/verify_reconstruction_corpus.py` before reporting completion;
2. report the harness result, not an assurance that everything is fine;
3. not report a defect it has not confirmed is in the subject rather than in
   the check;
4. not fill a documented gap with invented content — write
   `NOT SPECIFIED IN DOCS` and move on.

A subagent's summary is a **self-report**. Where a subagent's output becomes a
document, verify it the same way as any other generated content.

## 8. Current status

```
$ python tools/verify_reconstruction_corpus.py
12 documents, 198,005 characters
STATUS: PASS (9/9 checks passed)
```

Re-run after every write to this corpus. A corpus that fails its own harness is
not shippable, regardless of how complete it looks.