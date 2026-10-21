# Collatz research pre-paper

Research snapshot prepared for Ethan Walker on 21 October 2026. Source cutoff: 16:35 UTC. This repository preserves the delivered research package; it is not a claim to prove the Collatz conjecture.

## Quick links

- [Read the 162-page PDF](Collatz_PrePaper_Audit_2026-10-21.pdf)
- [Read or edit the full Markdown manuscript](Collatz_PrePaper_Audit_2026-10-21.md)
- [Browse the 258-claim ledger](Collatz_Claim_Ledger_2026-10-21.csv)
- [Source coverage and audit limits](Collatz_Source_Coverage_2026-10-21.md)
- [Sources and documented inspirations](chapters/literature_attribution.md)
- [Reproduce the included bounded checks](REPRODUCIBILITY.md)
- [Download the original research package](downloads/Collatz_PrePaper_Research_Package_2026-10-21.zip)

The original package remains unchanged in `downloads/`. The expanded files are available for browsing and revision. The repository is public at the owner’s request. No reuse license has been added.

---

# Collatz research pre-paper bundle

Prepared 2026-10-21, with a source-discovery cutoff of 16:35 UTC. Later uploads are outside this edition. This is an AI-assisted research synthesis and argument audit, not a claim to solve the Collatz conjecture and not an externally peer-reviewed paper.

## Start here

1. Read `Collatz_PrePaper_Audit_2026-10-21.md` (or the matching final PDF) for the mathematical narrative, precise map/clock conventions, arguments, counterexamples and publication-candidate assessment.
2. Use `Collatz_Claim_Ledger_2026-10-21.csv` to filter the 258 claim entries by chapter, status, assumptions, sources or limitations.
3. Use `Collatz_Claim_Ledger_2026-10-21.json` for machine-assisted follow-up. Its `claims` array preserves every original claim field and nested source record; `claim_origins` maps IDs to chapter ledgers. The CSV is a readable projection, not a lossless substitute.
4. Consult `Collatz_Source_Coverage_2026-10-21.md` and `.json` before interpreting a source as fully read, a proof as audited, or a test as rerun.
5. Consult `Collatz_Primary_Bibliography_2026-10-21.json` for primary references and historical source credit, and `Collatz_Attribution_Ledger_2026-10-21.json` for documented origins, inspiration and provenance distinctions.
6. `Collatz_Supporting_Validation_2026-10-21.json` records schema, ID, dependency, count and file-hash checks for the supporting deliverables. It is structural validation, not mathematical proof verification.

## Claim statuses

- `checked_proof` (195): Argument reconstructed or checked within this AI-assisted audit, under its stated assumptions. Not external peer review, proof-assistant certification, or a claim of historical novelty.
- `conditional` (16): Implication established only under an explicitly unproved or uninstantiated hypothesis.
- `conjecture` (13): Proposed statement or unresolved target, not an established theorem.
- `computational` (11): Finite experiment, exact computation, artifact check, or recorded computational observation; no unrestricted infinite conclusion follows from testing alone.
- `refuted` (15): Proposed statement or inference fails at the scope identified; consult the counterexample and limitations.
- `known_external` (8): External/classical result or inherited mathematical foundation, not a project novelty claim.

The status belongs to the exact statement and assumptions in that row. In particular, a checked restricted theorem can coexist with an open universal conjecture. A refuted heuristic does not refute the Collatz conjecture. A conditional theorem does not establish its premise. These categories are review labels, not independent mathematical refereeing.

## Source coverage and attribution

The Library discovery inventory had 2,473 entries, including unrelated material. That is not a count of Collatz documents read. The curated coverage register contains 172 project-source review rows and 21 archive-manifest rows, with overlaps and archive members explicitly identified. The 56 core bibliography rows overlap with the historical 193-record atlas; do not add them as unique papers or current inspections.

Library file IDs, document titles, archive-member names, source sections and recorded hashes are the retrieval trail. They do not grant public access. Relative source paths in evidence are documentary locators inside the original research collection, not a promise that those source files are in this delivery. Public source URLs in the bibliography lead to the relevant external works. Obtain original project files from the owner's Library and third-party publications from their original authorized sources.

Credit records distinguish the user's documented research directions from mathematical proof authorship; direct dependencies from analogies; contemporaneous quotations from report paraphrases; and related literature from documented inspiration. No exhaustive priority claim is made. AI-assisted source provenance is retained. Publication authorship and responsibility need human determination.

## Verification and reproducibility

- No external human peer review was performed.
- No external Lean or Coq project was built or kernel-replayed by this audit.
- Mathematical proof review, independently implemented finite checks, reexecuted supplied checkers, byte/hash matching and inherited output records are distinct evidence levels.
- Some large trajectory records and the final machine's 10,000-boundary / 8,114,452-step native replay were read as inherited evidence, not rerun here. The exact final quotient checker was separately rerun at its stated scope.
- Every finite checker proves only the finite identities or cases it actually evaluates. Infinite or all-source conclusions require the mathematical arguments and their hypotheses.
- The supporting-file assembly verifies exact aggregation, unique IDs, required fields, allowed statuses, dependency references and readable CSV round-trip IDs. It does not rerun the mathematical experiments merely by exporting their records.

To reproduce a particular claim, locate its exact Library source/version and archive member; compare the recorded SHA-256 when one is available; read the cited section and the audited limitations; obtain the named checker and inputs from that source archive; and rerun only the explicit documented test. Keep inherited output separate from newly generated results. A matching hash establishes file identity, not correctness. If a log records a local-versus-archive revision difference, preserve that distinction rather than treating the files as interchangeable.

The research-package ZIP also includes the editable chapter files, chapter claim ledgers, sanitized source read logs, selected bounded-check result records and standalone Python verification scripts. Its `REPRODUCIBILITY.md` identifies the included runnable subset and required inputs; `SHA256SUMS.txt` identifies the packaged files. The original large machine reproduction archives and full third-party papers are not included. Original machine archives can be retrieved by their Library IDs.

The present bundle is a research synthesis and navigation package, not a self-contained copy of the entire research corpus or every executable source dependency. Check the source-coverage register for clipped reads, selected sections, access failures, historical inspections, and known cross-log clarifications. Only a test actually rerun from the included or retrieved source should be described as reproduced.

## Delivery hygiene

The intended delivery consists of the named final manuscript and curated companions, not render previews or smoke tests. Raw Library inventories, raw tool responses, private download/signed URLs, unrelated Library metadata, internal operational notes, and downloaded third-party papers/OCR are intentionally excluded. Source documents are cited rather than redistributed.

## Before publication

Select a narrow coherent result; state all map, clock, positivity, integrality, fixed-source, uniformity and quantifier hypotheses; have a qualified mathematician independently check the proof and external theorem interfaces; perform a targeted priority search; and agree on authorship and credit. Treat this bundle as a detailed starting point for that work, not as publication-ready certification.
