# Publication assessment and principal findings

## Executive assessment

The archive supports a substantial research synthesis, but not a proof of Collatz, a proof of the named divergent C5 trajectories, or a proof of the unresolved Antihydra trajectory. Nor does it presently establish that the constructed blank-tape machine halts exactly when the full Collatz conjecture is false. Its proved halting specification is existence of a certificate in explicitly defined languages. Closing the gap between those statements would itself require a major new theorem.

The most defensible contribution is a collection of sharply delimited results about **arithmetic memory, admissible certificate languages, and the distinction between a deterministic driver and the condition that observes it**. A second contribution is the systematic identification of what several attractive proof architectures fail to control. These results explain why more precise accounting, longer experiments, smaller machines, or more expressive finite certificates do not by themselves complete the conjecture.

There are candidate units for specialist review. “Candidate” here means that the statement is sufficiently precise and its argument sufficiently developed to warrant assessment, not that publication novelty or importance has been established. No claim below should be advertised as a significant advance toward solving Collatz solely because it is new within this project's archive.

The user's preference has been to publish only if the contribution is substantial. Accordingly, this document is a pre-publication research record and triage tool, not a recommendation to submit a collection of modest observations. The best next publication decision is to obtain focused mathematical and priority review of the strongest coherent units before selecting any manuscript.

## Candidate A: sharp arithmetic-memory thresholds

**Primary claims:** NAV-076–082, with NAV-062–066 as related but distinct grammar/counting results, and the Navigation14 extensions NAV-089, NAV-092 and NAV-095.

The latest navigation work moves beyond an unrestricted affine endpoint formula by retaining the exact debt strip, source divisibility, and predecessor guards. Within this specified system it proves sharp inverse-memory thresholds: the C3 narrow-strip regime separates at widths eight and nine, while the corresponding C5 regime separates at sixteen and seventeen. Explicit neutral-loop witnesses demonstrate sharpness. These are not the same thresholds as the C3 band-fourteen/fifteen counting transition; the latter concerns a different question about history capacity.

The significant point is not that trajectories possess memory, which is elementary, but that a precisely defined resource restriction yields a quantified change in **recoverability of arithmetic history**. The equal-clock separation theorem then shows that a merger cannot be treated as free: the extra division prefix it requires changes the comparison. The accompanying no-pointwise-domination result blocks a tempting universal “replace the source by a smaller one” argument.

The final Navigation14 addition strengthens this comparison: all same-clock C5 ancestor sources compatible with a fixed width-seventeen strip have multiplicity at most twenty-two, and at most nineteen when entering relative debt is two. This yields a duration-independent obstruction to preserving at least two prior rounds through the specified same-clock suffix merger. In contrast, C3 has unbounded possible equal-clock multiplicity in band fifteen. The rational edge certificate and bounded exact inverse checks have been independently reconstructed in this audit. These are claims about the precisely guarded comparison geometry, not generic bounds on all ancestors of a number.

This is one of the clearest potential standalone mathematical units because it has explicit hypotheses, exact thresholds, sharpness witnesses, and a direct falsifiable interface. Publication assessment should concentrate on whether this formulation or an equivalent arithmetic-strip theorem already exists, whether the invariant has useful applications beyond the selected parser, and whether the full boundary-case proof survives external checking.

**What it does not show:** that the trajectory of a specified source remains in a narrow strip, that all C3 sources descend, or that C5 grows at its ensemble-average rate. The strip theorem is local structural information, not a global confinement theorem.

## Candidate B: certificate-language separation and relative incompleteness

**Primary claims:** MC-A1–14, MC-S1–5, MC-H01–08, especially MC-H07.

The automatic checker provides an exact finite test for a specified base-encoded invariant set. The symbolic checker provides a different finite representation and a sound method for verifying closure. The comparison map with exceptional set \(\{2^{2^j}:j\geq0\}\) separates these representations: the symbolic chart covers an infinite forward-invariant set avoiding one that no infinite automatic subset in any integer base can cover in the required way. The argument is representation-specific, not an assertion that finite descriptions in general fail.

The stronger diagonal comparison construction has a density-one divergent set and very mild forward growth while defeating both the enumerated automatic and eligible symbolic certificate families. This is valuable as a control experiment in theorem form: exceptionally broad coverage in numerical terms does not imply coverage by a chosen finite invariant language. Its construction is effective, and its proof specifies which languages are being diagonalized against.

The Collatz-side restrictions are complementary. Commuting digit actions, pairs of involutions or idempotents, semilinear traps, and context-pumping proposals each have precise limitations. Several proposed expressive shortcuts collapse to detecting a nontrivial cycle rather than adding divergent-orbit coverage.

The general tools here, including automata closure, pumping, semilinearity and diagonalization, are established mathematics. The possible project contribution is their exact combination and application to the defined verification problem. A publication claim should therefore be framed as a **relative expressivity and verification result**, with a serious prior-art search in automatic structures, program verification and invariant synthesis. It should not be framed as a new undecidability theorem for the ordinary Collatz conjecture.

**What it does not show:** that Collatz itself has an uncertifiable divergent orbit, that every hypothetical divergent Collatz orbit has a symbolic chart, or that generic undecidability prevents a complete checker for this particular map.

## Candidate C: matched drivers with different observers

**Primary claims:** AH-01, AH-03–13, AH-16–18.

The Antihydra analysis identifies a precise all-prefix resource inequality, rather than substituting average endpoint growth for safety. The machine comparisons show why that distinction matters. In particular, the ID7546 comparison realizes the same actual arithmetic driver from the same seed eight, but has a simpler observer whose nonhalting behavior can be proved. This is stronger evidence than a comparison between vaguely similar transition tables or between unrelated initial sources.

The native clock, handoff guards and resource coordinates are retained. The source-family funding theorem supplies increasingly long funded runs with an effective bound, while clearly allowing the source to vary with the requested run length. The restricted invariant obstructions explain why specified polynomial, congruence or bounded-window approaches do not certify the remaining named-source question.

The potentially useful general principle is a disciplined **driver–observer decomposition**: two machines can share their arithmetic driver yet differ in the logical burden imposed by their observers. A successful proof for one observer does not transfer to the other without a theorem relating their safety predicates. This principle has precedents in dynamical systems and program verification; the exact same-driver construction and the arithmetic funding analysis are the project-specific objects to assess.

**What it does not show:** Antihydra seed-eight safety for all future prefixes. The growing-source funding result is not a fixed-source infinite theorem. The finite machine catalogue is a finite classification with explicit unclassified cases, not a universal classification of small machines.

## Candidate D: finite descriptions, entropy and restricted Diophantine exclusion

**Primary claims:** LEG-05–15, LEG-18–20, LEG-31–37, CL01–08.

This branch contains several different types of information and should not be compressed into one purported universal complexity theorem. Examples include subpolynomial multiplicity of normalized shape components, finite-word precision packing, the entropy-derived chronological maximum-height exponent approximately \(1.05268\), bounded-description restrictions, and exclusion of specified rotation-coded or rank-two patterns.

The finite arithmetic arguments give useful constraints on what a fixed positive survivor would have to do. They identify costs of repeated templates, bounded dictionaries and specified low-complexity substitutions. The more advanced arguments invoke S-unit or Subspace-type methods and require careful separation of fixed algebraic data from parameters that change with the trajectory.

This review found substantive omissions in the original Research43–44 presentation. Research43 needed a common-frequency hypothesis and the corresponding residual-height control. Research44 needed uniform control of the degree growth in an infinite error tail. A separately stated amendment supplies these conditions and estimates. Its restricted rank-two argument has been checked independently within this audit, including the pointwise nature of the jet rescue. That does not turn the originally incomplete statement into a proof as originally written, and it does not establish the existence of the required towers for arbitrary Collatz orbits.

These deeper results are research-proof drafts requiring specialist review. The claim ledger explicitly flags that requirement. The publication question is not merely whether the final inequality looks plausible, but whether all uniformity constants, quantifiers, nonvanishing conditions and dependence on the fixed source are correct.

Priority review is particularly important here. The reciprocal-summability lineage runs through Heppner's stopping estimate and García–Tal's collision/window argument, with Sharpe providing a documented immediate formalized source used by the project. Rozier supplies a relevant harmonic/entropy antecedent. A chronological prefix maximum bound must not be conflated with a uniform spatial occupation estimate, but neither should a distinction in formulation be treated as evidence of novelty. The bibliography records additional priority leads that have not been verified strongly enough to import as theorems.

## Candidate E: closure, representation and original-source proof ownership

**Primary claims:** CL12–18, CL20–23, CL27–38, GDR-06–16.

The signed-word quotient identifies actual connected-component information and makes the universal elimination requirement explicit. Its algebraic mechanism is standard presentation/abelianization machinery; its utility is to reveal exactly which arithmetic coverage statement is still missing. The faithful first-jet encoding is a more specialized constructive result: retaining a derivative coordinate repairs loss of information in a scalar algebraic evaluation. Faithful encoding alone, however, does not supply an autonomous descending rank.

The receiver and packet calculus retains ownership of the original source. It distinguishes a number smaller than the current expanded state from a number smaller than the induction anchor. Explicit mergers and delayed receiver constructions cross barriers that defeat short fixed grammars. Conversely, finite replay and sparse grammar obstructions show why selected closure procedures remain incomplete.

The transport side makes the same issue quantitative. Contracting matched packets do not settle an unmatched residual atom. Countable flow statements need the stated tightness and capacity conditions. A summable budget for all transported unresolved mass would give the desired conclusion, but a budget only for selected bursts does not. The countable-menu and packet-contraction results are useful infrastructure, not evidence that the necessary global budget has been proved.

A coherent contribution might be an exact formal account of **source-owned proof certificates and their coverage limits**, supported by benchmark certificates and counterexamples. Whether it merits publication depends on its relation to existing termination, rewriting, proof-complexity and Collatz merger methods. The standard parts should be credited as such, rather than presented as a new general closure principle.

## The native machine: a reproducible artifact, not the missing theorem

The final selected construction has **499,710 working states, two tape symbols, and a separate halt state**, with literal unit left/right head moves. Its specification is the disjunction of the all-base automatic checker and the frozen-v1 symbolic checker. The reduction history and exact table hashes are recorded in the machine chapter. The final exhaustive quotient tests concern a finite compiled artifact and its specified semantics.

This is substantial implementation work, especially because coverage preservation was prioritized over state reduction. It does not establish a minimum state count. A much smaller comparison-map verifier or a smaller automatic-only search has different semantics and is not a directly interchangeable improvement. Nor is the final machine currently a proved halting equivalent for full Collatz falsehood: the missing certificate-completeness implication remains open.

The artifact is best treated as reproducible infrastructure for a theoretical certificate-language paper. State count alone is not a claim of field-level importance or a Busy Beaver record. A future general certificate theorem could change its mathematical significance, but that theorem must be proved separately.

## Corrections that must survive any later compression

A short paper or handoff must retain the following safeguards, even if it omits the development history:

1. The affine translation counts divisions before the corresponding odd step; clocks cannot be interchanged silently.
2. Real and 2-adic convergence cannot be identified merely because both are attached to the same finite words.
3. A finite source family with arbitrary precision does not produce one positive source realizing an infinite word.
4. Shrinking residue density, Haar mixing, or ensemble-average growth does not exclude every fixed positive integer.
5. The local modulo restriction and harmonic correction cannot be extended globally without their original hypotheses.
6. A smaller-source merger must be smaller than the original induction anchor and must carry its actual guards and division costs.
7. The two Navigation13 branches answer different questions. Width8/9 arithmetic memory, width14/15 counting capacity, and named-source drawdown hypotheses are not interchangeable.
8. The corrected region-interior feasibility statement is invariant under translation of the strip; resource at entry can still depend on its position.
9. A comparison-system separation is not a theorem that the analogous Collatz certificate language is complete or incomplete.
10. A sound proof-search machine halts on accepted evidence, not automatically on every true counterexample.

## Recommended threshold before external publication

A publication decision should follow five concrete checks:

- Select one coherent theorem package, rather than asking a reader to validate the entire research programme at once.
- Reconstruct every dependency from its precise primary theorem, including exceptional cases, map conventions and effective versus ineffective constants.
- Obtain specialist review for the Diophantine arguments and an unaffiliated mathematical review for the strongest elementary claims. The present independent checks are within one AI-assisted research process, not external peer review.
- Complete a targeted priority search around the selected theorem. Preserve documented inspiration separately from related work discovered afterward.
- Release a minimal reproducibility package with exact definitions, proofs, countercontrols and test scope. Do not imply that finite tests validate an infinite conclusion.

The strongest current assessment is therefore: **there is enough precise mathematics and reproducible construction here to justify serious specialist evaluation of several restricted results, but not enough evidence yet to assert a major Collatz breakthrough or a submission-ready significant contribution.** This pre-paper is designed to make that evaluation possible without hiding the open bridges or losing the credit owed to prior work.
