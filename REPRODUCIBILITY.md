# Reproducibility and audit scope

The main PDF and Markdown contain the mathematical arguments; the JSON ledger carries their assumptions and evidence. Read the limitations and specialist-review flags before interpreting a checked-proof label.

## Included standalone finite checks

Use Python 3 from this package directory. No network, credentials or third-party Python packages are required for these seven scripts:

- `python audits/verify_gdr_claims.py`
- `python audits/verify_navigation_audit.py`
- `python audits/verify_navigation14_audit.py`
- `python audits/closure_focused_checks.py`
- `python audits/antihydra_independent_checks.py`
- `python audits/adversarial_checks.py`
- `python audits/adversarial_jet_cycles.py`

They write their bounded-check results into `audits/`. Results supplement the proofs; they do not establish universal orbit claims. The navigation script covers its documented N05-N13 suite; the separate Navigation14 verifier covers its documented edge certificates and exact inverse checks.

Other recorded audit results, including native-machine exhaustive reruns and symbolic-language tests, require the original project archives identified in the source logs. Those archives are not silently represented as included here. Original full machine tables remain in their separately delivered Library reproduction archive. No Lean build or external peer review is claimed.

## Rebuild the document

The editable chapters are in `chapters/`. With Python, Pandoc, XeLaTeX and the named fonts already installed, create `output/`, run `python build/assemble.py`, then `bash build/render_pdf.sh`. The renderer isolates TeX caches within the package. Platform-specific TeX paths may need adjustment outside the environment used for this edition.

This package intentionally excludes downloaded full third-party papers, raw Library metadata inventories, private tool responses and signed download URLs. Primary-source links and hashes preserve the provenance without redistributing those papers.
