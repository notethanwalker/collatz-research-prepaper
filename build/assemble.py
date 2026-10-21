from pathlib import Path
base=Path(__file__).resolve().parents[1]
order=['00_orientation.md','publication_assessment.md','gdr_bounds_transport.md','legacy_routes.md','closure_constraints.md','antihydra_comparisons.md','recent_navigation.md','certificates_machines.md','h_obstruction_audit.md','literature_attribution.md']
head='''---
title: "Collatz Research: A Pre-Paper Audit"
subtitle: "Claims, arguments, limitations, and intellectual provenance"
author: "Prepared by dot for Ethan Walker"
date: "21 October 2026 — Research draft, not peer reviewed"
lang: en-US
---

'''
text=head+'\n\n\\clearpage\n\n'.join((base/'chapters'/n).read_text() for n in order if (base/'chapters'/n).exists())
(base/'output/Collatz_PrePaper_Audit_2026-10-21.md').write_text(text)
print('Words:',len(text.split()))
