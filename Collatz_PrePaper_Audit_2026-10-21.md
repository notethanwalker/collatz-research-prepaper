---
title: "Collatz Research: A Pre-Paper Audit"
subtitle: "Claims, arguments, limitations, and intellectual provenance"
author: "Prepared by dot for Ethan Walker"
date: "21 October 2026 — Research draft, not peer reviewed"
lang: en-US
---

# Orientation, scope, and how to read this pre-paper

## Purpose and publication posture

This is an argument-centered audit of Ethan Walker's Collatz research programme, prepared by dot on 21 October 2026. It is meant to let a mathematician or another model understand what the programme has actually established, how the arguments work, which external results they use, and what remains unresolved. It is not a proof of the Collatz conjecture, a claim that the whole programme is novel, or a submission-ready journal article.

The strongest material is not one completed universal proof. It is a substantial collection of exact reductions, restricted impossibility theorems, source-family certificates, comparison-system constructions, quantitative conditional criteria, and executable verification artifacts. Some ingredients are classical. Some are explicitly imported from recent formalizations. Others are project-specific combinations or refinements whose publication priority still needs a targeted literature review.

The source cutoff for this edition is 21 October 2026 at 16:35 UTC, including Navigation14 uploaded during the audit. The review prioritizes the newest research but follows dependencies backward. It does not equate “latest file” with “strongest result.” Two contemporaneous files called Navigation 13 are different branches, not successive versions; several earlier branches have later corrections absent from their first summaries. Duplicate files, altered claim ledgers, and reused numerical prefixes are distinguished wherever they affect interpretation.

The mathematical unit of review is a claim with its hypotheses and proof, not an enthusiastic description of a research pass. A valid theorem about a restricted certificate language is not promoted into a theorem about all Collatz trajectories. A finite experiment is not promoted into an infinite-orbit statement. A formalization claimed by an external author is distinguished from a proof-assistant build actually executed during this review.

## The central unresolved problem

For positive integers, define the ordinary Collatz map
\[
 T(n)=\begin{cases}n/2,&n\equiv0\pmod2,\\3n+1,&n\equiv1\pmod2.\end{cases}
\]
The conjecture says every positive source eventually reaches one. A bounded orbit repeats and enters a cycle; an unbounded orbit is injective and eventually leaves every finite set. Thus a counterexample would be a nontrivial cycle or an escaping orbit.

The research repeatedly reaches a distinction between **locally realizable finite behavior** and **the infinite behavior of one fixed positive integer**. Every finite valuation word can be realized by a suitable congruence class. Statistical laws hold for suitable finite source ensembles. Many proposed proof mechanisms cover whole arithmetic families. None of these facts alone forces a particular fixed source to acquire enough contraction, close its proof dependencies, stay within a safe resource budget, or possess a certificate in a chosen finite language.

The pre-paper therefore retains several distinct missing theorems rather than calling all of them “the same last step”:

- For direct descent bounds: every source must eventually receive a sound finite certificate below its original height.
- For source-visible potentials: the complete unresolved occupation or replenishment cost must be bounded, not merely a selected local burst.
- For proof graphs and boundary packets: every residual obligation must obtain an actual finite receiver or a smaller-source connection with all premises accounted for.
- For Antihydra and comparison resource systems: the named source must satisfy the required all-prefix safety bound, not just a finite history or a family of sources growing with the requested horizon.
- For the blank-tape certificate refuter: if Collatz is false, at least one accepted certificate must exist. A certificate for every divergent orbit would be sufficient but is stronger than this existential goal.

These are genuine mathematical obligations. Rephrasing them in a different notation is not counted as a new proof.

## Status labels

The claim ledger separates validity, evidence, originality, and usefulness. They are different questions.

**Reviewed proof.** The stated argument has been reconstructed and checked within its explicit hypotheses. This does not imply publication novelty or formal proof-assistant verification.

**Conditional theorem.** The implication is justified, but an arithmetic premise needed for the desired Collatz or named-source conclusion is open. A conditional theorem may itself be a correct and useful theorem.

**Finite certificate or computational result.** A specified finite computation has exact checks, or a sampled observation has a recorded protocol. Exhaustive finite certificates and sampled numerical patterns are distinguished. Neither is an infinite theorem without an additional argument.

**Known external input.** A result belongs to prior literature or an external formalization. The report credits the author and identifies the precise use. A project rederivation or application does not transfer ownership of the theorem.

**Conjecture or proposed architecture.** A plausible target or mechanism is recorded without asserting its missing premise.

**Refuted proposal or method-specific obstruction.** An earlier proposed conclusion is false, or a rigorously specified method cannot deliver it. The obstruction's scope is retained: failure of a formula is not failure of Collatz.

**Inherited or incompletely reviewed.** The current account depends on a source argument not fully reconstructed in this audit. Such a dependency is not silently upgraded by repeated citation.

Several S-unit, Subspace and amended rank-two arguments are explicitly marked as research-proof drafts requiring external specialist review. Their ledger label records the present argument-level check, not a claim of completed specialist validation.

“Independent” in the audit record refers to separate mathematical reconstruction or separately written/executed checkers in this AI-assisted review. It does not mean external peer review by an unaffiliated mathematician. Formal Lean artifacts that were not compiled are explicitly marked as uncompiled. This distinction is especially important for the early R-bound counterexample and the much later native Turing-machine certificates.

## A map of the substantive contributions

The chapters organize the programme by mathematical mechanism rather than by the order in which files were generated.

1. **Source-dependent enclosures and complete residuals.** Exact affine accounting, counterexamples to overly loose upper bounds, complete failure predicates for specified methods, the six-schema core, quantitative complement normalization, and source-visible summable budgets.
2. **Binary, entropy, and finite-description restrictions.** Corrected block identities, bounded-dictionary and bounded-complexity consequences, height/occupation restrictions, rotation-coded exclusions, and the limits of density or shrinking cylinders as a fixed-source argument.
3. **Closure and representation.** Boundary certificates, component quotients, faithful first jets, restricted replay obstructions, source-owned receivers, and the difference between an abstract closure theorem and its unproved arithmetic coverage hypothesis.
4. **Antihydra and matched machine comparisons.** Exact reductions to arithmetic drivers and observer/resource coordinates; same-driver controls with different safety outcomes; funding laws, residue guards, and conditional growing-run estimates.
5. **Recent region navigation and arithmetic memory.** The latest N05–N14 statements, corrected parser interfaces, bounded-debt grammars, predecessor/merger thresholds, conditional drawdown criteria, and explicit finite experiments.
6. **Certificate languages and native machines.** Automatic invariant checking, structural restrictions on digit memory, symbolic chart soundness, comparison-system separation theorems, and the exact compiled certificate-search machine.
7. **Intellectual provenance and publication assessment.** Direct theorem dependencies, adaptations, documented inspirations, related prior work, the user's research-direction contributions, and the remaining originality checks.

Several connections are worth keeping in view while reading. A source residue is not a resettable random input. A proof-reduction edge is not necessarily a forward trajectory step. A finite symbolic chart may represent an infinite invariant set, but an arbitrary finite program generating an orbit is not automatically such a chart. A shrinking set of compatible sources may retain a given integer forever. A locally contracting ensemble may leave an unmatched atom. A bounded resource grammar can permit nonperiodic choices without proving that a named source stays inside it.

## Clocks and conventions

The same letter is used for different purposes in older notes. This synthesis makes the principal clocks explicit:

| Object | Convention | What one unit counts |
|---|---|---|
| Ordinary Collatz \(T\) | odd \(3n+1\), even \(n/2\) | One elementary operation |
| Shortcut Collatz \(C\) | odd \((3n+1)/2\), even \(n/2\) | One shortcut transition |
| Odd acceleration \(S_c\) | \((cn+1)/2^{v_2(cn+1)}\) | One odd-to-odd round |
| Parser region | A specified finite word of accelerated depths | One completed region, not one odd operation |
| Common-future proof graph | A guarded, certified relation between sources | One proof-reduction edge |
| Native Turing machine | A literal transition table | One write and one unit head move |

Some Antihydra coordinates use another affine driver with its own clock, specified in that chapter. Some anchor constructions make one absorbing, while ordinary shortcut Collatz has the \(1\leftrightarrow2\) cycle. Statements using an absorbing anchor are not silently transferred to the unstopped map.

For an ordinary prefix with \(M\) odd operations and \(H\) halvings, time is \(M+H\). For a shortcut prefix of length \(K\), every transition includes one division by two, including the odd transitions. For an odd-depth word, cumulative depth is \(\sum a_i\). A rate such as \(c/4\) on the odd-round clock is not the same quantity on the ordinary clock.

## Attribution principles

The report separates five relationships:

1. **Direct dependency:** an external theorem is used with its actual hypotheses.
2. **Adaptation:** an existing technique is modified for the project's object or certificate language.
3. **Documented inspiration:** a source or user prompt is explicitly recorded as motivating an idea.
4. **Related prior art identified during review:** mathematically relevant work, without evidence it originally inspired the project.
5. **Uncertain provenance:** an origin or priority remains unverified.

For example, Hercher's half-source merger is an external theorem, not a project discovery. Finite flow arguments use established supply-demand machinery. Reciprocal summability has a classical collision/window antecedent and a documented recent formalized proof source; both deserve credit. A theorem about a slope-tied mechanical itinerary must not be assumed to cover every arbitrary-width rotation coding simply because the language sounds similar.

Ethan Walker's documented contributions include directing the comparative programme, insisting on preserved original-source constraints and parallel viewpoints, requesting the merger of symbolic checking with native certificate search, and prioritizing sound counterexample coverage over a smaller state count. These are credited as research-direction and problem-formulation contributions. They are not, without more evidence, assertions of sole authorship or worldwide priority for every mathematical statement produced in the programme. AI-assisted derivations and audits are disclosed rather than presented as independent external validation.

## What a mathematician should evaluate first

A useful reading order is the publication-assessment chapter, followed by the strongest restricted theorems and their exact countercontrols. Check, in each case:

- Is the object precisely defined, including its map, clock, source domain and certificate language?
- Is the theorem unconditional, or does its desired application depend on an unproved all-source premise?
- Does the proof genuinely reduce a problem, or merely restate it in an equivalent representation?
- Is the contribution a new theorem, a useful specialization, a sharper constant, a negative result about a specified method, or an engineering artifact?
- Are source families allowed to vary with horizon? Are targets and proof ownership kept fixed?
- Is novelty established, merely plausible, or not claimed?

This review intentionally preserves useful failed approaches and exact counterexamples. They explain why a promising-looking argument did not close, prevent rediscovery of the same error, and often clarify what a stronger method would have to retain.


\clearpage

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


\clearpage

# Source-dependent bounds, complete residuals, and summable budgets

This chapter reconstructs the GDR/Great Minds and subsequent budget routes. Its main distinction is between a sound certificate, a complete description of where one particular certificate fails, and a theorem that every source must eventually obtain a certificate. The first two are achieved in several concrete forms; the third remains open.

## Maps, clocks, and the exact affine ledger (GDR-01)

Write \(T(n)=3n+1\) for odd \(n\), and \(T(n)=n/2\) for even \(n\). This is the ordinary-operation clock. Write \(C(n)=(3n+1)/2\) for odd \(n\), and \(C(n)=n/2\) for even \(n\), for the shortcut clock. Finally, \(S(n)=(3n+1)/2^{v_2(3n+1)}\) acts on positive odd integers. None of these clocks may be substituted for another in an exponent or a stopping-time claim.

If an ordinary prefix has \(M\) odd operations and \(H\) halvings, then its length is \(t=M+H\) and
\[
 n_t=\frac{3^M X+B}{2^H},\qquad
 B=\sum_{j=1}^{M}3^{M-j}2^{h_j},
\]
where \(h_j\) counts the halvings **before** odd operation \(j\). The updates are \(B\mapsto3B+2^H\) at an odd operation and \(H\mapsto H+1\) at a halving. Thus, with
\[
 E=\log_2\left(1+\frac{B}{3^M X}\right),
 \qquad R(X,t)=\left(\frac{n_t}{X}\right)^{1/t},
\]
one has
\[
 t\log_2 R=M\log_2 6+E-t.
\]
These are exact accounting identities, not estimates and not a new convergence theorem. They belong to standard affine/parity-word Collatz mathematics; the project's contribution is careful integration with explicit enclosures and clocks. A formula omitting the additive translation, or replacing \(h_j\) by the number of later halvings, is generally wrong.

For any odd coefficient \(c\), a prescribed odd-depth word \(a_1,\ldots,a_m\), with \(H_j=\sum_{i\le j}a_i\), has offset
\[
 B_0=0,\quad B_j=cB_{j-1}+2^{H_{j-1}},\quad
 S_c^m(X)=\frac{c^mX+B_m}{2^{H_m}}.
\]
Its exact positive odd sources occupy the single class
\[
 X\equiv (2^{H_m}-B_m)c^{-m}\pmod{2^{H_m+1}}.
\]
The extra bit enforces an odd endpoint. Reduction of the final congruence at each earlier accumulated depth similarly enforces odd intermediate endpoints, hence exact valuations at every round. This is the classical finite-word coding mechanism, not a new independence assumption. Infinitely many positive representatives realize every finite word; that fact does not supply one positive representative for an arbitrary infinite word.

Sources: *GDR Route 01 Foundation* (14 October); *R Formula 1.5* §§2–6; *Resistant C3 Histories Replayed in C5 and C7* §2. Classical context: Terras/Everett parity coding and the Syracuse formulation used by Tao and Kontorovich–Lagarias.

## One finite upper-bound dip is sufficient, but not automatically available (GDR-02)

Suppose a source-defined admissible set contains the actual count and its correction enclosure is sound. Define
\[
 U_X(t)=\max_{m\in\mathcal A(X,t)}
 2^{[m\log_2 6+e_+(X,t,m)-t]/t}.
\]
Then a finite \(U_X(t)<1\) certifies descent, subject to the stated preterminal domain or an explicit conditional no-prior-descent argument. The running minimum
\[
 D_X(N)=\min_{1\le t\le N}U_X(t)
\]
preserves a certificate once obtained. It is not a claim that the trajectory or the individual upper bound decreases monotonically. If every \(X>1\) has a finite such certificate, strong induction proves convergence. An infimum equal to one is insufficient; strict inequality is essential.

Under the temporary assumption that all relevant odd inputs are at least \(X\),
\[
 E\le M\log_2(1+1/(3X)),\qquad
 R^t\le \frac{(3+1/X)^M}{2^{t-M}}.
\]
If this conditional bound becomes subunit, either descent already occurred or the hypothesis forces it now. After an earlier descent it need not remain an unconditional bound on the observed endpoint. This distinction prevents an illegitimate extension of a preterminal theorem through the \(1,4,2\) cycle.

The project-directed shift from permanent contraction to one source-dependent certificate is useful problem formulation. The induction argument itself is elementary and standard. Computing an exact admissible set by reconstructing the whole itinerary does not eliminate itinerary complexity merely because its input is only \(X,t\).

Source: *R Formula 1.5—Eventual Upper-Bound Dip* §§1–9, Library `libfile_726ad16d3f4c81919cac28b547e963f1`.

## Two proved failures of bounding constructions (GDR-03 and GDR-04)

### The generic preterminal correction bound fails at 27

The frozen generic enclosure combines
\[
 E_+=\min\left\{
 \log_2\left[1+\frac{2^{t-2M+1}(1-(2/3)^M)}{X}\right],
 M\log_2(10/9)\right\}.
\]
For \(X=27\), first arrival at one occurs after 111 ordinary operations, with \(M=41,H=70\). For **every** preterminal horizon \(1\le t\le111\), exact integer checks give, with \(q=H-M+1\),
\[
 3^M27+2^q(3^M-2^M)>2^H27,
 \qquad 10^M>3^M2^H.
\]
These are the two rational versions of \(U^{t}>1\). The generic enclosure therefore never certifies this source, even when supplied the exact count. At fixed \(X,t\), both candidate expressions increase with \(M\), so a looser count ceiling cannot repair the failure. The actual orbit first falls below 27 at operation 96, reaching 23.

This refutes completeness of the **specified generic formula**, not Collatz and not the conditional or fully joint construction. The saved Lean draft was explicitly uncompiled; the exact Python/integer certificate, not the mere presence of Lean syntax, supports the finite claim.

Source: *R15 Proposition Test Setup and Counterexample* §§1–5, Library `libfile_609e82d012c481918d98164330429d1a`.

### A fixed-precision projected filter can fail at every horizon

For the particular fixed-\(k\) modular filter used by R1.5, take \(X=2^k-1\). Its maximally alternating ordinary candidate has \(M=\lceil t/2\rceil\) and offset \(B=3^M-2^M\). Its numerator is
\[
 3^M(X+1)-2^M.
\]
Because \(2^k\mid X+1\), the projected endpoint/parity tests never exclude this candidate, even when later genuine itinerary bits would. Its homogeneous rate is at least \(\sqrt{3/2}>1\). Thus this projected bound never dips.

This is an all-horizon obstruction to that implementation's relaxation. It is not a theorem that every method using congruences or finite automata is incomplete. Additional source-size information, higher precision, or different certified relations may change the result.

Source: *R Formula 1.5*, §8.

## Exact loss of coverage through an offset interval (GDR-05)

In shortcut time \(K\), an actual endpoint is \((3^M X+B)/2^K\). GM02 admitted any integral endpoint whose offset lay in
\[
 3^M-2^M\le B\le 2^{K-M}(3^M-2^M).
\]
For every positive \(X\) and every \(K\ge4\), this relaxation admits an endpoint above \(X\). Choose \(M=K-1\) and put \(a=3^{K-1}-2^{K-1}\). Since \(a\ge2^K-1\), the integer interval \([a,2a]\) represents every residue modulo \(2^K\). It therefore contains an offset making the endpoint integral, regardless of \(X\). Meanwhile \(3^{K-1}/2^K\ge27/16>1\).

The inequality for \(a\) begins at \(K=4\) and persists from \(a_{K+1}=3a_K+2^{K-1}\). For \(K\le3\), possible descents are already in the elementary covered classes. Thus this standalone relaxation adds no coverage to the preceding construction, for any horizon menu.

There are only \(K\) genuine one-zero parity words, with offsets
\[
 B_j=3^{K-1}+2^j3^{K-j-1}-2^K,
 \quad 0\le j<K.
\]
Replacing them by a long interval destroys their correlation. Endpoint integrality does not reconstruct it. This is a clean, publishable-in-principle **method-specific obstruction or worked counterexample**, though no independent novelty claim has been established.

Source: *Great Minds 03—Combined Bounds*, §2, Library `libfile_be640de10bc88191b46129852815d2d4`.

## Complete historical residual and an exact normalization map (GDR-06)

For odd \(n>1\), write
\[
 h=v_2(n+1),\quad u=(n+1)/2^h,\quad
 b=v_2(3^h u-1),\quad U(n)=(3^h u-1)/2^b.
\]
The maximal shallow profile has depth word \(1^{h-1},b+1\), with \(h\) odd operations and \(h+b\) halvings. A frozen GDR envelope's complete failure predicate is
\[
 \mathcal F=\{n>2\text{ odd}:v_2(3n-1)\in\{2,4\},\ U(n)\ge n\}.
\]
Adding a root inverse when \(3\mid n+1\), and the merger when \(b\ge2\), leaves
\[
 \mathcal K=\{n\in\mathcal F:b=1,\ 3\nmid n+1\}.
\]
Its exact six schemata, with \(j\ge0\), are
\[
\begin{array}{c|cc}
 h=2&96j+27&96j+91\\
 h\ge3\text{ odd}&2^h(12j+1)-1&2^h(12j+5)-1\\
 h\ge4\text{ even}&2^h(12j+7)-1&2^h(12j+11)-1.
\end{array}
\]
For \(b=1,h\ge2\), \(U(n)>n\), so the endpoint condition is automatic. The table follows by reducing \(3^h u\equiv3\pmod4\), excluding \(3\mid u\), and retaining the extra \(h=2\) guard. Four schemata have two unbounded parameters. Six formulas do not make a six-state convergence proof.

For every \(n>1\) outside \(\mathcal K\), define \(D(n)\) by priority:

1. Halve even \(n\).
2. If odd and \(3\mid n+1\), use \((2n-1)/3\).
3. Otherwise, if \(b\ge2\), use \((n-1)/2\).
4. Otherwise use the first contracting parser-region endpoint.

All edges have an actual finite common future. The merger is the retained Hercher identity
\[
 C^{h+2}(n)=C^{h+1}((n-1)/2)=(3^h u-1)/4.
\]
It can also be derived directly: the partner reaches \(3^{h-1}u-1\), which is \(2\pmod4\) under the guard; one halving and one odd shortcut step give the displayed meeting point. This is a credited imported merger, not a new project theorem merely because its proof is reproduced.

To specify branch 4, put \(q=v_2(3n-1)\), \(w=(3n-1)/2^q\). Its endpoint is \((3n+1)/2^{v_2(3n+1)}\) for \(q=1\); \(2\cdot3^{j-1}w+1\) for \(q=2j\); and \((3^jw+1)/2^g\), \(g=v_2(3^jw+1)\), for \(q=2j+1\ge3\). Outside the core the remaining even case has \(j\ge3\). These are exact guarded formulas, not fractional divisions declared to be steps.

Sources: *Whole Previous Failure Set Route*; *Great Minds Pass 08 Execution* §§1–3, Library `libfile_83d51c573b2881918a0c05a9b1d461f0`; Christian Hercher, [There are no Collatz-m-Cycles with m≤91](https://arxiv.org/abs/2201.00406). Cycle-specific results elsewhere in Hercher's paper must not be imported as arbitrary-prefix results.

## Uniform shifted contraction and its exact limitation (GDR-07)

For the above \(D\),
\[
 D(n)+5\le\frac67(n+5),\qquad n>1,\ n\notin\mathcal K.
\]
The even, inverse, and merger branches are immediate linear inequalities. For the even parser branch \(q=2j,j\ge3\), the ratio is
\[
 \frac{2\cdot3^j w+18}{4^j w+16}.
\]
The desired inequality is \((6\cdot4^j-14\cdot3^j)w\ge30\). At \(j=3\), the coefficient is six and admissible \(w\ge5\); it subsequently increases. The odd parser branch satisfies the stronger factor \(3/4\), apart from small entries handled exactly. The \(q=1\) branch uses the endpoint bound \((3n+1)/4\), with its small exceptions checked directly.

Repeated complement reduction therefore reaches one or the core in \(O(\log n)\) **proof-reduction edges**, not ordinary Collatz steps. For a core edge,
\[
 U(n)+5\le g_h(n+5),\qquad g_h=3^h/2^{h+1}\ge9/8.
\]
Consequently any connected guarded path with \(k\) core edges, total core length \(H\), and \(r\) complement edges obeys
\[
 \frac{w+5}{X+5}\le
 \frac{3^H}{2^{H+k}}\left(\frac67\right)^r.
\]
Multiplication telescopes the intermediate shifted heights. A right side below one gives a smaller common-future source, hence a valid induction certificate. No theorem forces that inequality on every source.

There is a narrow optimality result: in the class of constant translations \(n+c\) absorbing every core edge at its pure factor \(g_h\), the \(h=2\) edge forces \(c\ge5\). The complement edge \(2\to1\) then forces a uniform contraction factor at least \((c+1)/(c+2)\ge6/7\). This does not establish optimality among nonlinear potentials or richer proof graphs.

Source: *Great Minds Pass 08 Execution*, §§4–5. The shift \(n+5\) already occurred in earlier project normalization; the new assertion is its quantified use on this full complement and mixed proof system.

## A one-sided divisibility certificate and an exact redundancy (GDR-08)

On the core, put \(A=3^{h+1}u-5\). If \(2^{2j}\mid A\), then the ordinary trajectory has a checkpoint at time \(2h+3j\) with
\[
 Z=1+\frac{3^{j-1}A}{2^{2j}}.
\]
After the core exit, an odd step and a halving give \(1+A/4\); each further odd-operation/two-halving block multiplies the shifted value by \(3/4\). The divisibility guard supplies each legitimate block. The final checkpoint may be even.

Let \(j_h\) be the least \(j\ge1\) with \((3/2)^h(3/4)^j\le3/4\). Then \(j_h\le2h\). The sufficient condition
\[
 v_2(3^{h+1}u-5)\ge2j_h
\]
forces \(Z<X\) within at most \(8h\) ordinary operations. For every \(h\ge2\), it describes two complete cofactor classes after the modulo-three exclusion.

However, this success set is contained in the first-core-excursion rule: the first exit has a large contracting-region valuation, and its complete complement reduction is no larger than \(Z\). It is therefore proof compression, not an independent increase in accumulated coverage. The distinction is worth preserving in any publication claim.

Source: *Great Minds Pass 08 Execution*, §7.

## Finite continuation saturation is not an infinite counterexample (GDR-09)

Fix one core schema and its permitted \(h\). After a short, explicitly specified release, its sources become \(r+2cj\), where \(c\) is odd. For any prescribed finite depth word with compatible odd residue \(t\pmod{2^{H+1}}\), solve
\[
 j\equiv((t-r)/2)c^{-1}\pmod{2^H}.
\]
Thus every finite continuation occurs in infinitely many roots of that fixed schema. No universally successful forward-lookahead bound depending only on the schema and \(h\), but not on cofactor or source magnitude, can cover it.

Similarly, \(X_k=36\cdot8^k-5\) produces \(k\) successive core edges with shifted growth \((9/8)^k\). These witnesses grow with \(k\). Neither construction proves a fixed positive source with infinite adverse continuation. They also do not exclude source-dependent or inverse/merger certificates.

Source: *Great Minds Pass 08 Execution*, §8; the finite-word mechanism is standard parity coding.

## Historical normalization can return the original obligation (GDR-10)

The creative-reference construction gives a finite boundary identity
\[
 E_N-E_1=\partial Q_N+P_N,
\]
with initial packet vertices at most \((3N+1)/2\). Under strong induction at the **fixed** target \(N\), complement normalization replaces every packet vertex by one or a core vertex in \([N,(3N+1)/2]\), without increasing the number of packet vertices. Append each actual common-future chain to \(Q_N\); combine its endpoint coefficient into the new packet. This proves the boundary identity and the support statement. It does not bound all intermediate trajectory heights or later repair support.

For \(N=27\), the packet is \(E_{41}-E_{40}\). The priority reduction sends 41 to 27, and 40 to one. The normalized packet is again \(E_{27}-E_1\). Hence normalization alone returns the same unproved obligation, not a proof of closure.

A larger packet port is not automatically discharged because it has a link to a number smaller than itself: that number must be below the original induction target or otherwise independently anchored. This source-ownership condition is a recurring useful correction across the project.

Source: *GDR and Great Minds Failure Set Assessment* §§4–7, Library `libfile_545198ced0348191bdc49991f40fda46`.

## Countable transport menus and nonuniform gate slack (GDR-11)

Here is a valid abstract theorem, not a proved Collatz arithmetic inequality. Let \(S\) be countable, \(*\) terminal, and \(N(x)\subseteq S\cup\{*\}\) a nonempty countable neighbor set. Let \(w(x)>0\), \(\sum w<\infty\), and nonnegative receiving capacities \(\kappa(y)\) have finite sum. If every finite terminal-free source cut satisfies
\[
 w(A)\le\kappa(N(A)),
\]
then there is nonnegative supported flow with row sums \(w(x)\) and column sums at most \(\kappa(y)\). The terminal may have capacity \(W=\sum w\).

For finitely many source rows, group target columns by their subsets of neighboring source rows. There are finitely many such patterns. Finite weighted Hall/max-flow gives a flow to these pattern nodes; proportional disaggregation by actual target capacities restores literal columns. For infinitely many rows, use the compact product of coordinate intervals \([0,\min(w(x),\kappa(y))]\), including terminal capacity \(W\). Column partial-sum constraints are closed. Crucially,
\[
 \sum_{y\notin F} f_{xy}\le\sum_{y\notin F}\kappa(y)\longrightarrow0
\]
uniformly over admissible arrays, so complete row sums are continuous. The finite-intersection property now preserves every row demand. Without this summable-capacity tightness, coordinatewise limits could lose row mass.

If \(\kappa(y)=w(y)-\delta(y)\) with \(0\le\delta(y)\le w(y)\), a nonempty terminal-free closed component \(E\) would satisfy
\[
 w(E)\le\kappa(E)=w(E)-\delta(E).
\]
It must therefore avoid every positive-slack point. A gate meeting every bad component suffices; uniform positive relative slack is unnecessary. A forward sufficient residue gate can be imported only with its exact theorem and clock. On a residual domain, the raw gate's intersection need not suffice; one must retain it or prove the normalizer-image gate hits each bad component.

This is a careful application/extension of standard finite flow and compactness techniques. Gale's supply-demand theorem is a direct method dependency. The project does **not** prove the needed literal Collatz cut inequality, and a formal inverse word does not itself define a legal edge. No novelty claim for general flow/compactness is justified here without further literature work.

Sources: *GDR2 Countable Menus* (`libfile_15eed1fb89d0819191574ca8e52e1add`); *GDR2 Nonuniform Gate Slack* (`libfile_5349dcd5a1d48191ac8a05a957dac151`); independent handoff review. Gate source: Keenan Monks, Kenneth G. Monks, Kenneth M. Monks, Maria Monks, [Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph](https://arxiv.org/abs/1204.3904), Corollary 5.8.

## Exact finite packet contraction (GDR-12)

Let \(d\) be positive odd, \(n\) positive odd, and \(n\ge1024d+1\). For \(P=\{n,n+2d,n+4d,n+6d\}\), set \(V(x)=\sqrt{x-1}\). Then
\[
 \sum_{x\in P}V(S(x))\le0.99\sum_{x\in P}V(x).
\]
The four inputs occupy all odd classes modulo eight: two have depth one, one depth two, and one depth at least three. Thus
\[
 \sum V(S(x))\le4q_0\sqrt{n+6d},\qquad
 \sum V(x)\ge4\sqrt{n-1},
\]
where \(q_0=(5\sqrt6+2\sqrt3)/16\). The ratio is at most \(q_0\sqrt{1031/1024}<0.99\); the last inequality follows rationally from \(\sqrt2<99/70\). This is a finite deterministic inequality, not an average over an orbit assumed random.

For \(d=1\), the stronger global statement with factor \(0.9999\) follows by this theorem for \(n\ge1025\), plus complete rational radical enclosures for the 512 smaller odd starts. For coefficient five the corresponding homogeneous factor exceeds one, providing a useful comparison.

However, after one odd C3 round outputs avoid multiples of three. The transported population cannot simply be regrouped into equal-weight consecutive odd packets at every step. Using stride three repairs the support issue, not the unequal-weight issue.

Source: *Summable Budgets From Arithmetic*, §5, Library `libfile_ce760bd4954881918b982366854624be`. The finite depth-class mechanism is standard; the explicit packet formulation/constants and subsequent matching residual are project constructions whose independent novelty is unestablished.

## An exact residual inequality with an open arithmetic input (GDR-13)

Give odd source \(X>3072\) permanent mass \(X^{-2}\) and kill it on entering the certified finite base. Let \(\mu_t(y)\) be transported surviving mass and
\[
 V_t=\sum_y\mu_t(y)\sqrt{y-1}.
\]
Partition the two admissible odd residue classes modulo three into four-term stride-three packets. Match the minimum mass in each packet and call the remaining nonnegative weighted potential \(U_t\). Matched packets contract by the previous theorem; every unmatched entry satisfies \(V(S(y))\le\sqrt2 V(y)\). Hence
\[
 V_{t+1}\le\rho V_t+(\sqrt2-\rho)U_t,\qquad\rho=0.99.
\]
If \(\sum U_t/(t+1)<\infty\), multiplying by \(1/(t+2)\) and summing proves
\[
 (1-\rho)\sum_t\frac{V_t}{t+1}
 \le V_0+(\sqrt2-\rho)\sum_t\frac{U_t}{t+1}<\infty.
\]
A permanent survivor contributes a fixed positive mass and positive potential at every time, contradicting harmonic summability. The implication is proved. The bound on the **actual unmatched transported mass** is not. An absorbed source cannot be reintroduced as free contracting companion mass.

More generally, fixed positive source weights and any divergent time charge exclude permanent survivors if their weighted total occupation is finite. This is Tonelli/elementary summability, not a discovery that ensemble density automatically controls atoms.

Source: *Summable Budgets From Arithmetic*, §§3–6,10. Documented inspiration includes the user's integration/summability question and the earlier project *Fairness Series and Core Coverage Assessment*, explicitly acknowledged by the source report.

## Infinite unresolved histories incur infinite logarithmic occupation (GDR-14)

Before first descent below a fixed odd \(X>1\), put \(n_m=S^m(X)\) and
\[
 J_X=\sum_{m<\tau_X}\frac1{\log(n_m+5)}.
\]
Since \(S(n)+5\le(3/2)(n+5)\), an infinite survivor satisfies
\[
 J_X\ge\sum_{m\ge0}\frac1{\log(X+5)+m\log(3/2)}=\infty.
\]
Thus a source-derived finite occupation budget would suffice for first-descent induction. Defining it as the unknown future occupation is circular.

Nevertheless, any uninterrupted run of \(k\) depth-one rounds has \(2^{k+1}\mid X+1\) and costs less than \(1/\log2\). A run of \(k\) repeated depth pairs \((1,2)\) has \(2^{3k+1}\mid X+5\), and its \(2k\) rounds cost less than \(2/(3\log2)\). These bounds follow because all entries within a run exceed its entry and the run length is bounded by the entry's divisibility.

For \(X_k=2^{3k+1}-5\), after \((1,2)^k\) and the next depth-three round, the odd state is
\[
 Y_k=(3\cdot9^k-7)/4.
\]
The lifting-the-exponent identity \(v_2(9^k-1)=3+v_2(k)\) shows that exactly \(v_2(k)\) depth-one rounds immediately follow. Their initial budget is \(O(\log k/k)\). This is one renewal, not a bound on all later renewals. An indefinitely changing sequence of individually cheap bursts may still incur infinite total cost.

Source: *Summable Budgets From Arithmetic*, §§7–8; elementary valuations and the earlier project occupation-charge idea are explicitly reused.

## Higher lattice representatives are already summable (GDR-15)

For an exact depth word \(w\) of length \(m\), let \(Q_w=2^{H_w+1}\) and \(r_w\) its least positive odd source. With source weights \(X^{-s}\), \(s>1\), all nonminimal representatives satisfy
\[
 \sum_{k\ge1}(r_w+Q_wk)^{-s}\le\zeta(s)Q_w^{-s}.
\]
Summing over all positive depth words, even ignoring survival, gives
\[
 L_m\le\zeta(s)2^{-s}(2^s-1)^{-m}.
\]
For \(s=2\), \(\sum_{m\ge1}L_m\le\pi^2/48\). This follows by factoring the independent *sum over all finite words*, not by assuming independence along a fixed orbit.

Every fixed source eventually becomes its own least representative as the growing word modulus exceeds it. The difficult atomic contribution therefore migrates into the remaining least-representative sector. The estimate works for other odd coefficients too and cannot alone distinguish Collatz from coefficient-five cycles.

Source: *Summable Budgets From Arithmetic*, §9, refining *Compatibility Pressure and Positive Lift*.

## A no-go result for overly simple global weights (GDR-16)

Suppose \(A n^{-s}\le h(n)\le B n^{-s}\) for all large odd \(n\), with \(A,B,s>0\), and the unweighted deterministic push-forward on the surviving odd states, \((Ph)(y)=\sum_{x:S(x)=y}h(x)\), satisfies \(Ph\le h\). The sum is over sources outside the killed base. Each surviving actual edge gives \(h(S(x))\ge h(x)\). But \(x_k=2^{k+1}-1\) has \(k\) depth-one rounds ending at \(y_k=2\cdot3^k-1\), with \(y_k/x_k\to\infty\). Monotonicity would require \(A x_k^{-s}\le B y_k^{-s}\), an impossibility.

Thus bounded residue corrections to a pure power-law weight cannot supply that global pointwise supermeasure. This does not rule out irregular source-history weights, packet inequalities, unbounded-amplitude corrections, or variable-time descent. Long ascending Mersenne prefixes are classical; the project applies that obstruction to a precisely specified transport proposal.

Source: *Summable Budgets From Arithmetic*, §11.

## Matched-word comparisons separate arithmetic from sampling (GDR-17)

For the same legal ordinary word, with \(M\) odd operations and \(H\) halvings, across odd coefficients \(c\),
\[
 \frac{R_c}{R_3}
 =(c/3)^{M/(M+H)}2^{(E_c-E_3)/(M+H)}.
\]
A large-source word near the C3-neutral balance \(H/M\approx\log_2 3\) therefore has per-odd-round factor approximately \(c/3\). A fair-depth reference with mean two instead has factor \(c/4\); on the ordinary clock it is \((c/4)^{1/3}\). This is conditional matched-word algebra, not an orbit-wide optimal growth law.

The saved experiments distinguish transplanting an exact word from reusing a starting number, and distinguish a genuinely copied 2,442-step record word from a synthetic word sharing only an odd/halving count pair. After a prescribed prefix ends, segment-only rates are measured separately from the geometric rate of the whole prefix. The observed C5/C7 returns toward reference growth are finite observations, not individual-orbit fairness or divergence proofs.

Source: *Resistant C3 Histories Replayed in C5 and C7*, §§1–7, Library `libfile_dfadf9746a808191ac495cb0c5bfca35`. The comparison design follows the user's explicit emphasis on matched systems and source-information resources; stochastic reference background is credited to the Syracuse/\(3x+1\),\(5x+1\) literature.

## Assessment for a pre-paper

The strongest material here is a collection of precisely scoped proof-method results: the complete failure of a relaxed bound, explicit residual normalization and shifted contraction, continuation-saturation obstructions, finite packet contraction, source-visible budget implications, and exact negative controls. They make the missing arithmetic input visible instead of renaming it.

The standard identities, inverse predecessors, imported merger, finite flow machinery, and summability principles should not be presented as new discoveries. The specialized synthesis, constants, exact residual descriptions, and counterexamples may warrant exposition or a methods contribution after a focused originality review. None currently establishes a full universal R ceiling, cumulative compensation law, or convergence proof.


\clearpage

# Foundational routes: exact arithmetic, recurrence, entropy, and the fixed-source obstruction

## Scope and audit standard

This chapter reviews the latest substantive checkpoints in the early Binary, Shortcut, golden-rotation, FP/fairness, notation-transform, Region Family Analysis, and causality-map routes. “Early” describes their place in the project, not a cutoff at their first reports. In particular, Binary25 is read through its October 7 corrective audit; Shortcut15 supersedes several earlier logarithmic constants; FP60 is read with the actual FP57–59 arguments; Region's October 12 fixed-source checkpoint controls its population conclusions; the canonical Research series is followed through Research44 and its Research35/39–43 dependency chain; and the latest completed causality analysis located is Pass05, October 13. A later Pass06 plan is not a completed result.

The source register at the end identifies actual Library objects. Repeated handoff summaries are not independent evidence. Two large cumulative handoffs were only partly read, and are not used as proof substitutes. Mathematical statuses below mean: a self-contained argument checked here, a deduction conditional on a stated theorem or research draft, an exact finite computation, a conjecture, or a corrected/refuted inference. “Checked” is not formal verification, external refereeing, or an assertion of historical novelty.

The most useful prospective contributions are:

1. A finite entropy–height inequality and the consequent maximum-height exponent 1.0526808586 for an injective positive orbit.
2. Fixed-event and fixed-dictionary prefix bounds, using fixed-dimensional Diophantine approximation, followed by quantitative repair occupation per turnover. These are substantial research proof drafts and deserve specialist review before publication.
3. A complete elementary exclusion of eventual codings of the golden rotation by an arbitrary single interval, with a separate exact geometry verifier.
4. Corrected arithmetic recurrence/packing bounds for binary-run shapes, including a sharper one-use threshold, but not a capacity contradiction.
5. Exact history-conditioned Region laws, together with an unusually clear explanation of why exponentially vanishing survivor density does not eliminate a fixed positive seed.
6. Concrete countercontrols: endpoint-telescoping cocycles, finite-memory mixing without individual fairness, carryless growth with the same finite valuation laws, and failed alternate-history architectures.

No result in this chapter proves Collatz, proves the project's full FP target, or excludes every nonterminal positive cycle.

## 1. Common maps, clocks, and elementary foundations

Use distinct symbols to avoid a recurrent source of confusion:

\[
 C(x)=\begin{cases}x/2&x\equiv0\pmod2,\\(3x+1)/2&x\equiv1\pmod2,\end{cases}
 \qquad U(n)=\frac{3n+1}{2^{a(n)}},\quad a(n)=v_2(3n+1)
\]

for the shortcut map on positive integers and accelerated map on positive odd integers. One accelerated round of depth \(a\) expands into the shortcut parity block \(10^{a-1}\). Write \(\alpha=\log_2 3\), \(c=\alpha-1\), \(A_N=\sum_{i<N}a_i\), and \(H_N\) for a stated maximum height, never silently for the last iterate.

For an accelerated word,

\[
 2^{A_N}n_N=3^N n_0+C_N,\qquad
 C_N=\sum_{i<N}3^{N-1-i}2^{A_i}.                                      \tag{1.1}
\]

For a binary shortcut word of length \(L\) with \(h\) ones,
\(C^L(x)=(3^h x+B)/2^L\). Equal length-\(L\) parity words therefore force the starting integers to be congruent modulo \(2^L\). This finite residue injection is the source of many valid packing statements below; it is not a source of independent random bits. Its classical background is the 2-adic parity conjugacy developed by Bernstein and Lagarias [E1].

A positive orbit that is unbounded cannot repeat a state: repetition would make its future periodic and bounded. Its states are consequently pairwise distinct and tend to infinity in the sense of eventually leaving every finite set. This fact does not say that they increase monotonically.

The exact accelerated logarithmic identity is

\[
 A_N=N\alpha+\log_2(n_0/n_N)+
 \sum_{i<N}\log_2(1+1/(3n_i)).                                      \tag{1.2}
\]

Distinctness alone bounds the correction by \(O(\log N)\); the stronger reciprocal-summability theorem discussed in §4 bounds its entire infinite sum. Both estimates must be used with their proper domain.

## 2. Binary routes: a useful arithmetic calculus, not a finite information budget

### 2.1 Centered runs and exact switch law [LEG-01]

Set \(D_a=2^a-3\) and \(S_a(n)=D_a n-1\). On a depth-\(a\) step,

\[
 S_a(U(n))=(3/2^a)S_a(n).
\]

Thus a maximal constant-depth run preserves the signed integer obtained by removing all factors of 2 and 3 from \(S_a\). Call this its shape \(s\). The word “6-free” in the notes means coprime to 6, not squarefree. If a run has length \(r\) and changes from \(a\) to \(b\), its entrance satisfies
\(v_2(S_a(n_{\rm in}))=ar+\min(a,b)\). This gives an exact finite precision ledger.

At the switch state \(x\), put \(m=\min(a,b)\) and write

\[
 D_a x-1=2^m3^t s,\qquad
 D_b x-1=2^{m+\rho}3^k s',\quad \rho\ge1.
\]

Eliminating \(x\) gives

\[
 D_b3^t s+\varepsilon=D_a2^\rho3^k s',\qquad
 \varepsilon=(2^b-2^a)/2^m.                                        \tag{2.1}
\]

The switch is reconstructed from \((a,b,s,t)\) by \(x=(1+2^m3^t s)/D_a\). This is a genuine relation between binary precision consumption and ternary/shape regeneration. It does not imply that regeneration is impossible. Sources: Binary03 and the corrective audit [LEG-S24, LEG-S03].

A useful elementary refinement is \(|s|<n_{\rm in}/2\) for a nonterminal run. It improves subsequent range bounds; treating shape size as an independent quadratic resource is unnecessarily weak.

### 2.2 Finite-height capacity and its correct scale [LEG-02]

Binary08 imposes a finite parameter cap \(a,b\le H\), \(|s|,|s'|<2^H\). A two-2-adic-logarithm estimate of Chim, with multiplicative dependence treated separately, bounds the switch exponents by \(t,\rho=O(H\log H)\). Counting reconstructing tuples and then run lengths yields

\[
 \#\{\text{distinct switches under the cap}\}=O(H^3\log H\,2^H),
 \qquad N\le C_{\rm start}+O(H^4(\log H)^2 2^H).                  \tag{2.2}
\]

Hence an indefinitely distinct history cannot keep all these parameters capped, and necessarily
\(H\ge\log_2N-O(\log\log N)\). The phrase “near-linear bit height” must not be mistaken for \(H\asymp N\). The result is logarithmic parameter growth versus time. Chim's published logarithmic estimate is an external ingredient, not a project theorem [E2]. The October 7 audit checked the numerical substitutions and separates \(A=\pm3^q\), where an independence hypothesis would fail. This remains a research application requiring specialist verification of the imported bound, not a certified new Diophantine theorem [LEG-S23, LEG-S03 §§2–3].

### 2.3 Gcd-normalized components: strong recurrence restrictions and a prime-content correction [LEG-03–05]

From (2.1),

\[
 g=\gcd(|s|,|s'|)\mid 2^{|a-b|}-1.
\]

At a unit-depth exit \(a=1,b\ge2\), define \(u=|s|/g\), \(v=|s'|/g\). Then

\[
 x+1=2\,3^tgu,\quad D_bx-1=2^{\rho+1}3^kgv,\quad
 g\mid2^{b-1}-1,\quad\gcd(u,v)=1.                               \tag{2.3}
\]

**Correction.** These quotients are coprime to one another, not necessarily supported on primes absent from the opposite original shape. The actual orbit fragment \(195\to293\to55\), with depths 1 and 4, has
\(s=-49,s'=119,g=7,u=7,v=17\). The “source-only” quotient 7 still divides 119. Statements about new primes, or independent prime information, do not follow from (2.3).

Suppose all states under consideration are distinct and at most \(M\). Then \(b,t,k,\rho=O(\log M)\), and the possible shared gcds are counted by

\[
 Q(M)=\sum_{b\le\lfloor\log_2(3M+1)\rfloor}\tau(2^{b-1}-1)=M^{o(1)}.
\]

The elementary divisor bound \(\tau(n)=n^{o(1)}\), together with (2.3), implies that any fixed value of \(u\), or of \(v\), occurs at only \(M^{o(1)}\) distinct unit exits. This covers all allowable depths, not only a shallow cutoff [LEG-S05, LEG-S03 §§4–6].

For a hypothetical accelerated orbit with maximum \(M_N\le N^{D+o(1)}\), (1.2) gives \(A_N=N\alpha+O(\log N)\). At least \((2-\alpha)N-O(\log N)\) steps have depth 1. Each unit run lasts \(O(\log M_N)\), so there are \(E_N=\Omega(N/\log N)\) complete unit runs. The multiplicity bound implies that for every fixed \(\eta>0\), all but \(o(E_N)\) exits satisfy \(u,v\ge N^{1-\eta}\).

For fixed \((b,u,v)\), (2.3) gives one CRT class modulo \(uv\): \(x\equiv-1\pmod u\) and \(D_bx\equiv1\pmod v\). Thus its occurrence count is at most \(1+\lfloor M/(uv)\rfloor\). For \(D<2\), almost all these exit signatures are one-use. This supersedes an earlier \(D<4/3\) threshold. It is not a contradiction: \(N\) states may carry \(N\) distinct signatures. “Almost all large,” “many distinct,” “never reused,” and “fresh primes at every time” are different statements.

### 2.4 Persistent primes and a uniform renewal bound [LEG-06]

If a prime \(p\ge5\) divides consecutive shapes, then consecutive branch labels are congruent modulo \(r=\operatorname{ord}_p(2)\ge3\). A persistence episode therefore uses shortcut blocks \(10^{a-1}\) with \(a\) restricted to one residue class modulo \(r\). A renewal count bounds its binary language by a constant times \(\lambda^L\), uniformly in the class and \(r\), where

\[
 \lambda^3-\lambda^2-1=0,\quad \lambda=1.465571\ldots,
 \qquad h_* =\log_2\lambda=0.551463\ldots.
\]

Distinct states below \(M\) have distinct parity blocks once \(L=\lceil\log_2(M+1)\rceil\). The episode length is therefore \(O(M^{h_*}+\log M)\). This is a persistence bound for one shared prime under a finite range cap, not a universal orbit growth theorem [LEG-S03 §7].

### 2.5 Endpoint collapse, word precision, and the recycling boundary [LEG-07–08]

For full switch letters \(\lambda_j=(a_j,b_j,t_j,\rho_j,k_j)\), define

\[
 z_j=\frac{D_{a_j}2^{\rho_j}3^{k_j}}{D_{b_j}3^{t_j}},\qquad
 \delta_j=\frac{\varepsilon_j}{D_{b_j}3^{t_j}},\qquad
 z_js_{j+1}=s_j+\delta_j.
\]

With \(Z_m=\prod_{j<m}z_j\), the entire accumulated correction is exactly

\[
 \sum_{j<m}Z_j\delta_j=Z_ms_m-s_0,\qquad
 Z_m=\frac{D_{a_0}}{D_{a_m}}2^{\sum\rho_j}3^{\sum(k_j-t_j)}.          \tag{2.4}
\]

The ternary exponent also telescopes against the run ledger. One cannot count every intermediate correction as a separately discarded, irrecoverable information cost. Route23 is a useful negative result precisely because it invalidates that proposed accumulation [LEG-S07].

A fixed full affine word \(W\), however, imposes an exact congruence: its distinct realizing initial shapes are congruent modulo \(2^{R(W)+1}\), where \(R(W)=\sum\rho\). For \(|s|\le S\),

\[
 \operatorname{Occ}(W)\le1+\lfloor S/2^{R(W)}\rfloor,
\quad
 J-\ell+1\le |\mathcal F_\ell|+S\sum_{W\in\mathcal F_\ell}2^{-R(W)}. \tag{2.5}
\]

Here \(\mathcal F_\ell\) is the set of realized length-\(\ell\) full words and \(J\) the number of letters. Since every recharge is at least one and \(S<M/2\), in a polynomial range \(M\le N^{D+o(1)}\), words longer than \((D+o(1))\log_2N\) are one-use. The earlier coefficient \(2D\) was unnecessary [LEG-S06, LEG-S03 §8].

Eventual repetition of one *full* affine program forces an actual periodic orbit by increasing 2-adic precision. This is periodic-itinerary rigidity, not a proof that the only positive cycle is the terminal one. An autonomous deterministic finite-state generator is eventually periodic; a finite alphabet, a branching finite graph, or a finite algorithm with unbounded memory need not be. Route25's broad “recycling closed” language is narrowed by the audit: aperiodic indefinite reuse remains open [LEG-S04, LEG-S03 §9].

## 3. Shortcut recurrence and the entropy–height frontier

### 3.1 A quantitative Hamming recurrence barrier [LEG-09]

For a shortcut orbit \(x_t=C^t(x_0)\), put
\(D_q(L)=\#\{0\le t<L:b_t\ne b_{t+q}\}\), where \(b_t=x_t\bmod2\). If the orbit is unbounded, every sufficiently long clean comparison interval would make two distinct states congruent modulo a modulus exceeding both, hence equal, a contradiction.

The elementary envelope is \(x_t+1\le(3/2)^t(x_0+1)\). Set \(K=\lceil\log_2(x_0+1)\rceil\), \(B=K+cq+1\), and choose disjoint windows recursively by
\(s_{j+1}=s_j+K+\lceil c(s_j+q)\rceil\le\alpha s_j+B\).
Each window must contain a disagreement. Consequently

\[
 D_q(L)\ge \log_\alpha\!\left(1+\frac{(\alpha-1)L}{B}\right)-O(1). \tag{3.1}
\]

For fixed \(q\), the coefficient of \(\log_2L\) is
\(1/\log_2\alpha=1.505007\ldots\). If a periodic template of period \(q\) differs from the actual word at \(e\) positions, every shift disagreement is incident to an edit, so \(D_q(L)\le2e(L+q)\). Thus at least \(0.752503\ldots\log_2L-O(1)\) edits are required. A growing lag \(q\le L^\vartheta\), \(\vartheta<1\), reduces the leading coefficient by \(1-\vartheta\).

For \(q=1\), each completed accelerated event \(a_i\ge2\) creates a 10 and a 01 transition in the expanded word. The exact endpoint convention in Shortcut14 makes this \(D_1(A_N)=2\#\{i<N:a_i\ge2\}\). This yields its logarithmic exceptional-event floor [LEG-S01, LEG-S18].

**Credit and scope.** The clean-window/residue-height mechanism is explicitly credited by the project to M. Sharpe's `DefectHeight.lean` and `ParityDefects.lean` [E3]. The project improves a rational growth envelope to the exact \(\log_2(3/2)\) coefficient. It does not discover parity injection, prove positive defect density, or bound complexity above.

### 3.2 The finite entropy inequality and current universal exponent [LEG-10]

Let the first \(M\) shortcut states be distinct, \(H=\max_{t<M}x_t\), \(r=\lceil\log_2(H+1)\rceil\), and \(p=M^{-1}\sum_{t<M}b_t\). If
\(q=p-(r-1)/(2M)\ge1/2\), then

\[
 \boxed{\log_2M\le r\,h_2(q)},                                   \tag{3.2}
\]

where \(h_2\) is binary entropy. This is finite and deterministic; the only random choice is a uniformly sampled index in the actual finite prefix.

**Proof.** The \(M\) length-\(r\) future parity words are distinct by residue injection, so their entropy is \(\log_2M\). At offset \(j\), the proportion of ones differs from \(p\) by at most \(j/M\). Entropy subadditivity and concavity give an upper bound \(r h_2(\bar p)\), with \(\bar p\ge q\). Since entropy decreases above one half, this is at most \(r h_2(q)\).

The shortcut growth identity and the reciprocal harmonic bound on distinct odd states give

\[
 p\ge\tau-O_{x_0}(\log M/M),\qquad \tau=\log_3 2.
\]

If an infinite injective orbit had a subsequence with \(H\le M^{\kappa+o(1)}\) and \(\kappa<1/h_2(\tau)\), then \(r=O(\log M)\) on that subsequence. Substitution in (3.2) gives \(1\le\kappa h_2(\tau)+o(1)\), a contradiction. Hence

\[
 \boxed{\liminf_{M\to\infty}\frac{\log H_M}{\log M}
 \ge\frac1{h_2(\log_3 2)}=1.0526808586079714\ldots.}              \tag{3.3}
\]

This is the latest universal maximum-height threshold located in these routes, not the older 1.044667 regime parameter, not the weaker 1.03449 consequence of another spatial exponent, and not the proposed research goal 1.1. It does not bound the individual last term from below and supplies no upper bound to contradict escape [LEG-S30, LEG-S29].

The interval-occupation extension retains an essential boundary cost. For \(M\) selected distinct states in \([L,U)\), whose visit times form \(B\) intervals, and \(2^r\ge U-L\), replace \(q\) by \(p_J-B(r-1)/(2M)\). The same argument works, while endpoint telescoping bounds

\[
 p_J\ge\tau-\frac{B\log_2(2U/L)+M/(3L\ln2)}{M\log_2 3}.
\]

In a dyadic band with \(B\log L/M\to0\), one obtains \(M\le L^{h_2(\tau)+o(1)}\). Frequent reentry can defeat the hypothesis. Discarding this boundary term would reintroduce the very error the extension repairs. García–Tal's 1999 uniform spatial sparsity is relevant prior art, with a different locality statement [E4]. Rozier's earlier distinct-odd harmonic correction and entropy/parity framework are also direct antecedents [E11]. The finite chronological inequality and explicit boundary costs are candidate quantitative reformulations pending priority review, not established novel discoveries.

### 3.3 Chronological conditional entropy and growing descriptions [LEG-11–12]

FP59 retains empirical chronology rather than assuming a Markov chain. For a distinct accelerated prefix let \(S=\sum a_i\), \(E=S-N\), \(D=\#\{a_i\ge2\}\), and expand it to a length-\(S\) binary word. Cyclic pair counts are exactly

\[
 \#11=N-D,\quad\#10=\#01=D,\quad\#00=E-D.
\]

With \(H=\max(n_i+1)\), \(k=\lceil\log_2(3H/2)\rceil\), and \(g=S-k+1>0\), the actual, nonwrapping length-\(k\) windows are distinct. Entropy chain rules, with explicit wrap cost, yield

\[
 \frac gS\log_2g\le h_2(N/S)+(k-1)
 \left[\frac NS h_2(D/N)+\frac ES h_2(D/E)\right].                \tag{3.4}
\]

For \(H\le N^{d+o(1)}\), any limiting \(\delta=D/N\) obeys

\[
 h_2(\delta)+(\alpha-1)h_2\!\left(\frac\delta{\alpha-1}\right)
 \ge\frac\alpha d.                                             \tag{3.5}
\]

Thus there is a positive exceptional-event density in each fixed polynomial-height regime. At \(d=2\), it is eventually greater than \(1/16\). Optimizing the left side over \(\delta\) recovers (3.3), not an improved universal exponent. Calling (3.4) a Markov *assumption* would be incorrect: conditional entropy is an upper bound valid for the empirical word [LEG-S22 Components01–02].

For an \(M\)-state binary reference machine, repair fraction \(\rho\) gives
\(H(W_k)\le\log_2M+k[h_2(\rho)+\rho\log_2(2M)]\).
This makes dictionary complexity explicit. A fixed machine requires positive repair density under polynomial height. If its size grows as \(M_N\le(\log N)^{a+o(1)}\), accelerated repairs satisfy

\[
 \liminf\frac{R_N\log_2\log_2N}{N}\ge\frac\alpha{2ad}.
\]

The factor 2 comes from expanding depth repairs into at most two binary repairs. A universal block dictionary of at most \(\ell2^\ell\) states can describe any binary word of total length \(m\) with at most \(2m/\ell+1\) repairs. Hence the \(N/\log\log N\) order in the growing-polylogarithmic-size regime cannot be improved merely by this generic coding argument. These statements concern a stated finite-state representation, not Kolmogorov complexity or the impossibility of a simple deterministic algorithm generating an intricate orbit.

## 4. Bi-convergence, golden bridges, and a restricted exclusion theorem

### 4.1 The correction series has different real and 2-adic limits [LEG-13]

Divide (1.1) by \(3^N\):

\[
 S_N=C_N/3^N=\sum_{i<N}\frac{2^{A_i}}{3^{i+1}},\quad
 n_N=\frac{3^N}{2^{A_N}}(n_0+S_N),\quad v_2(n_0+S_N)=A_N.
\]

Thus \(S_N\to-n_0\) in \(\mathbb Q_2\). On the other hand,

\[
 n_0+S_N=n_0\prod_{i<N}(1+1/(3n_i)).                              \tag{4.1}
\]

The reciprocal-summability theorem for an escaping orbit makes the product converge to a positive finite real number. Consequently \(S_N\) has a positive finite real limit while its 2-adic limit is the negative integer \(-n_0\). There is no contradiction: two completions have different topologies. If \(\Delta_i=i\alpha-A_i\), the same conclusion gives \(\sum_i2^{-\Delta_i}<\infty\) and \(\Delta_i\to\infty\). It gives neither a positive linear drift nor an algebraic real limit [LEG-S20].

**External credit.** Sharpe's September 5, 2026 `orbit_summability.tex` and Lean `OrbitPacking.lean` give an elementary finite packing proof, and explicitly credit García–Tal (1999) for stronger interval sparsity implying summability [E3–E4]. For example, the source's bound
\(8^m|S|\le2\cdot216^m+243^m\) for a suitable injective finite image below \(32^m\) yields summable dyadic-type shell contributions. This is imported prior work, not a project discovery. The root audit inspected the pinned Lean source; this chapter did not run its Lean build.

The project's two-prefix determinants and product-formula attempts did not turn the two limits into independent constraints: their carries are coupled, and the claimed margin cancels. They are valuable recorded failed arguments.

### 4.2 The exact golden bridge cocycle and the repaired logical gaps [LEG-14]

For a binary word \(W\) of length \(r\), with \(h\) ones, let
\(c(W)=\sum_{i:w_i=1}2^i3^{\#\{j>i:w_j=1\}}\). Research13 defines

\[
 K(W)=3^{-h}[4c(W)+2^{r+1}-3^h],
\]

and obtains the exact composition law

\[
 K(AB)=K(A)+2^{|A|}3^{-|A|_1}(K(B)-1).                           \tag{4.2}
\]

It yields nested congruences and the transported defect residue
\(R\equiv\varepsilon2^a3^{-(p+1)}K(M)\pmod{2^Q}\). These are arithmetic constraints, but nesting does not force least positive representatives to grow. The nested palindromes \(W=1^r\) give \(c(W)=3^r-2^r\), \(K(W)=3-2^{r+1}/3^r\), whose least positive residue modulo \(2^{r+1}\) is always 3.

The October 5 repair also corrects a substitution-theoretic overreach: the Akiyama–Shirasaka result invoked requires the phase to lie in the quadratic field. Arbitrary phases share the same finite factor language, by density of rotation and finite right-continuous partitions, but need not themselves be primitive-substitutive words. A proposed exponential lower bound for the transported least residue was not proved. Finite computations at selected Fibonacci scales are evidence about those scales, not the missing infinite theorem [LEG-S21, LEG-S28; E5].

### 4.3 Golden rotation with arbitrary interval width: a self-contained route [LEG-15]

Research15 replaces that residue-growth endgame with a geometric argument. Let \(\theta=(\sqrt5-1)/2\). For every \(0<\beta<1\) and every phase \(x\), no positive shortcut Collatz orbit has an eventual parity tail

\[
 b_t=\mathbf1_{[0,\beta)}(\{x+t\theta\}).                         \tag{4.3}
\]

Here the interval width \(\beta\) is independent of the rotation angle. This is wider than the usual mechanical-word subclass.

**Proof architecture.** Discard an initial tail so (4.3) starts at time 0, with positive source \(N\). The coding is not eventually periodic: a nonzero irrational shift cannot preserve a nontrivial interval on a dense orbit. Hence the Collatz states cannot repeat. If the parity words at times \(s\) and \(s+q\) agree for \(\ell\) steps, residue injection and \(n_t+1\le(3/2)^t(N+1)\) give

\[
 \ell\le c(s+q)+\log_2(N+1).                                    \tag{4.4}
\]

Let \(q=F_k,Q=F_{k+1},\delta_k=\theta^k\), with the usual Fibonacci indexing. The displacement \(F_k\theta-F_{k-1}=(-1)^{k-1}\delta_k\) makes the lag-\(q\) disagreement set the union of two short boundary intervals, one at 0 and one at \(\beta\). A Fibonacci tower of height \(Q\) visits each at most once. Thus among its first \(Q\) comparisons there are at most two defects.

Zero defects contradict \(Q\le cq+O_N(1)\). If there is one defect, apply (4.4) before and after it to get
\(Q\le(c^2+2c)q+O_N(1)\). Both fail for large \(k\), because
\(Q/q\to\varphi\) and \(\varphi>c^2+2c=(\log_2 3)^2-1\). Therefore there are exactly two defects for all large \(k\).

The remaining point is not a probabilistic assertion. Define the oriented short interval \(J_k=[-\delta_k,0)\) for odd \(k\), \([0,\delta_k)\) for even \(k\), and
\(H_k=\bigcup_{t=0}^{F_{k+1}-1}(J_k-t\theta)\).
The explicit tower partition uses
\(I_k=[-\delta_{k+2},\delta_{k+1})\) for odd \(k\), with the two endpoints interchanged in magnitude for even \(k\). Its induction gives

\[
 \bigcap_{k=K}^{m}H_k
 =\bigcup_{r=1}^{F_{K+1}}(r\theta+I_m),\quad
 \bigcap_{k\ge K}H_k=\{r\theta:1\le r\le F_{K+1}\}.             \tag{4.5}
\]

Two defects force both \(x\) and \(x-\beta\) into every \(H_k\), so they are two of these fixed orbit centers. Their defects then occur at \(Q-r\) and \(Q-s\). The initial clean interval has length \(Q-\max(r,s)\), which again violates (4.4) since \(\varphi>c\). This proves the stated restriction [LEG-S02].

A separately retrieved verifier performs the interval arithmetic in \(\mathbb Q(\sqrt5)\), including half-open endpoint conventions. A fresh run checked 17 tower levels, 108 finite intersections, 378 late-defect cases and 12 selected empty intersections. These regressions support the implementation, not the infinite induction.

**Prior-art boundary.** Sharpe's dated September 5, 2026 mechanical classification proves that a globally mechanical positive itinerary has slope \(1/2\) and seed 1 or 2, and that any mechanical tail reaches 1 [E3]. Mechanical words there are exactly \(\lfloor(t+1)\gamma+\rho\rfloor-\lfloor t\gamma+\rho\rfloor\). This subsumes mechanical golden/silver special cases, but not automatically (4.3) with independent arbitrary \(\beta\). The latter theorem merits comparison with the broader rotation-coding literature before a novelty claim. It does not cover all irrational rotations, all quadratic rotations, or arbitrary Collatz itineraries.

## 4A. Latest canonical Research branch: rank-two structure after Research44

The canonical `Collatz_Research` series continues beyond the golden theorem to Research44, October 6. Its latest claim is a rank-two recurrence exclusion under substantial tower hypotheses, not an extension of the golden theorem to all orbits. The relevant correction chain is Research35's decorated Padé count, Research39's counterexample and return-word repair, Research40's local height/jet repairs, Research41's equal-multiplier case, Research42's exact elimination and fixed-shape case, and Research43–44's moving-slope argument. These seven notes were read in full for this addendum [LEG-S35–41].

### 4A.1 The obstruction Research39 actually refutes [LEG-31]

Finite dictionary rank, a prefix tree, bounded polynomial degree, and a surviving Padé denominator do not by themselves prohibit deep cancellation. Research39 constructs a concrete rank-two countercontrol using the Thue–Morse series \(f(x)=\sum v_nx^n\). Two exact Padé errors have orders 23 and 22, and their nonzero determinant is \(26x^{22}+12x^{23}\). The series-valued unit \(R(x)=E_a(x)/(xE_b(x))\), with \(R(0)=1\), is installed in the corrections of a two-leaf tree \(\{01,10\}\). The resulting specialized Padé value is exactly zero, while its denominator remains nonzero and the projected binary coding is aperiodic.

This is an exact generalized-series counterexample to unrestricted descent, not a positive Collatz orbit. Its information-bearing unit is not shown to be an actual finite-block rational correction of height \(O(M)\). The later route must use that arithmetic restriction, not simply rename the same finite-rank argument.

A separate correction concerns return words. Durand's start-to-start returns form a code, but need not be prefix-free: Fibonacci returns to marker 1 include 10 and 100, whose Collatz corrections both equal \(1/3\). For a marker \(u\), switch from start-to-start \(W\) to end-to-end first-right-return \(V\), so \(Wu=uV\). Then

\[
 z(V)=z(W),\qquad
 c(V)=\frac{c(W)+(z(W)-1)c(u)}{z(u)}.                              \tag{4A.1}
\]

The end-to-end dictionary is prefix-free, and rationality/linear height is preserved if marker length is \(O(M)\). Interlevel conjugating words still have to be tracked; a local boundary change is not a proof of a whole aligned tower transfer. Durand's original definition and code theorem are direct primary antecedents [E12].

### 4A.2 Fixed-series height rigidity and compatible jets [LEG-32]

Research40 proves an elementary, useful arithmetic lemma. Let \(F\in\mathbb Q[[x]]\cap\mathbb Z_2[[x]]\) be fixed. Suppose rational \(x_j,r_j\) satisfy

\[
 m_j=v_2(x_j)\to\infty,\quad h(x_j)\le\gamma m_j+o(m_j),\quad
 h(r_j)\le A m_j+o(m_j),\quad
 v_2(r_j-F(x_j))/m_j\to\infty,
\]

where \(\gamma<2\), \(A<\infty\), and \(h(a/b)=\log_2\max(|a|,b)\). Then \(F\) is rational.

**Proof.** If not, choose \(d\) with \(2d+1>A+\gamma d\), and a nonzero pair of degree-\(d\) polynomials with \(QF-P=O(x^{2d+1})\). Its nonzero error has a fixed leading order \(K\ge2d+1\). Integrality makes this leading term dominate at \(x_j\) for large \(j\). The superlinear approximation implies \(r_jQ(x_j)-P(x_j)\ne0\), with valuation \(Km_j+O(1)\). But common-degree homogenization gives its rational height at most \(h(r_j)+d h(x_j)+O(1)\), contradicting \(v_2(r)\le h(r)\). The factor is \(d\), not an unnecessarily doubled \(2d\).

This excludes Research39's specific hidden nonrational series as a bounded-height rational edge in its fixed one-scale realization. It says nothing about arbitrary moving series.

For regrading \(t^q=Yx^{p-q}\), ordinary differentiation holding \(t,Y\) fixed is invalid in the quotient. Research40 instead uses commuting Euler derivations

\[
 D_0=qx\partial_x+(p-q)t\partial_t,\qquad
 D_1=t\partial_t+qY\partial_Y.
\]

They preserve the relation, normal-form degrees, coefficient integrality and the \(x^N\) filtration. A minimum-order nonzero pair jet at a nonzero torus point rescues a vanishing polynomial pair from a fixed finite jet family. **The rescued error need not be formally of order \(N\).** The high-order identity holds at the evaluation point because all lower pair jets vanish there and Leibniz cross terms disappear there. Genuine cancellation with a nonzero denominator is not removed by jets alone [LEG-S39].

### 4A.3 Exact rank-two correction elimination and fixed shapes [LEG-33–34]

For a binary coarse word \(v\), put \(P_n=\prod_{s<n}z_{v_s}\), \(G=\sum P_n\), \(H=\sum v_nP_n\), and \(\Psi=c_0G+(c_1-c_0)H\). Summing the path recursion gives

\[
 G-1=z_0G+(z_1-z_0)H,
\quad
 (z_1-z_0)\Psi=D G-(c_1-c_0),
\quad D=c_1(1-z_0)-c_0(1-z_1).                                  \tag{4A.2}
\]

For distinct actual prefix-code blocks, \(D\ne0\): otherwise their periodic inverse-parity values \(c/(1-z)\) agree. Parity coding is injective, so their infinite periodic words agree, making the finite blocks prefix-comparable, a contradiction. Therefore unequal multipliers permit exact correction elimination, and \(\Psi\in\mathbb Q\) of height \(O(M)\) forces \(G\in\mathbb Q\) of height \(O(M)\). No probabilistic independence is used.

For equal multipliers \(z_j=2^{L_j}/3^{K_j}\),
\(\Psi_j=c_{j,0}/(1-z_j)+(c_{j,1}-c_{j,0})f_j(z_j)\), where \(f_j\) has binary coefficients. An aperiodic coarse limit \(v^{(j)}\to v\) gives superlinear approximation to the fixed series \(f\), while \(h(z_j)/v_2(z_j)\le\log_2 3<2\). The height lemma forces \(f\) rational and hence its finite-alphabet coefficients eventually periodic, a contradiction [LEG-S38].

More generally, fixed monomial shapes \(z_{j,a}=\alpha_a t_j^{p_a}\), with positive fixed integers \(p_a\) and fixed nonzero rational \(\alpha_a\), reduce to
\(G_v(t)=\sum A_nt^{S_n}\), where support gaps are \(p_{v_n}\) and consecutive nonzero coefficient ratios are \(\alpha_{v_n}\). If the two shape pairs differ, a rational coefficient recurrence has finitely many normalized support-point states; repetition determines the same future gap/ratio word, forcing eventual periodicity of \(v\). Genuine Collatz multipliers give \(h(t_j)/v_2(t_j)\le\log_2 3+o(1)\), so the fixed-series lemma applies. Identical shapes reduce to the equal-multiplier case [LEG-S37].

These are restricted exclusion theorems: aligned rational scalar height, growing block scale, and an aperiodic compactness limit are hypotheses. A moving family of aperiodic words can converge to a periodic word. A fixed compact subshift with no eventually periodic points would ensure the desired limit, but arbitrary tower coverage is not proved.

### 4A.4 Irrational Newton weights and rational residual rigidity [LEG-35–36]

Research43's local Newton lemma is sound independently of its broader application. For a fixed nonzero Laurent error \(E=P_0+P_1G_v(X,Y)\), its coefficients range over a finite rational set. After a fixed monomial shift its support is nonnegative. If \(L_{j,1}/L_{j,0}\to\rho>0\) irrational, the weights \(a+b\rho\) on integer exponent pairs have a unique minimum and a positive gap above that minimum. Coefficient valuations are bounded. Thus, at \(X_j=2^{L_{j,0}}/3^{K_{j,0}}\), \(Y_j=2^{L_{j,1}}/3^{K_{j,1}}\), the error is nonzero eventually and has valuation \(O(L_{j,0})\). Large support points are uniformly separated by positivity; only finitely many candidates lie near the minimum.

For a rational limiting ratio \(p/q\), Research44 introduces

\[
 x=z_0,\quad t=z_1/z_0,\quad Y=z_1^q/z_0^p,
 \qquad t^q=Yx^{p-q}.
\]

Under common fine-letter frequencies \(K_{j,a}/L_{j,a}\to\delta\), both \(\Delta L=qL_1-pL_0\) and \(\Delta K=qK_1-pK_0\) are sublinear in \(m=L_0\). Consequently \(h(Y)=h(2^{\Delta L}3^{-\Delta K})=o(m)\). Normal monomials \(x^nt^s\), \(0\le s<q\), have distinct leading weights \(n+s(p-q)/q\), separated by at least \(1/q\). A leading coefficient polynomial \(A(Y)\), if nonzero at the specialization, has valuation \(o(m)\). If it vanishes infinitely often, \(Y\) freezes to one of finitely many rational roots and gives a fixed monomial shape, already covered by Research42.

### 4A.5 The two audit amendments and the conditional combined conclusion [LEG-37]

The originals' rank-two conclusion should not be quoted without the following distinctions.

**First omission, Research43.** Its standalone final theorem omits common fine-letter frequency, but its borrowed residual-height ledger uses that assumption. The amended statement retains it explicitly, or requires a separately proved equivalent residual-height bound. For irrational \(\rho\), choose fixed large \(q\), \(p=\lfloor q\rho\rfloor\). Then
\(\Delta L=(q\rho-p)m+o(m)\), \(\Delta K=\delta\Delta L+o(m)\), and \(h(Y)\le\alpha m+o(m)\), with leading constant independent of fixed \(q\).

**Second omission, Research44.** If \(Y\) is not 2-adically integral, bounding only the polynomial's fixed \(Y\)-degree does not bound the infinite error tail. The audit supplies a uniform estimate. A term \(x^it^sY^f\cdot x^nt^{B_n}\), with \(B_n\le n\), reduces with \(k=\lfloor(s+B_n)/q\rfloor\) to \(x\)-degree \(\ell=i+n+(p-q)k\ge n\), and \(Y\)-degree at most \(e+\lfloor\ell/q\rfloor+1\). Clearing one fixed denominator bounds coefficient valuations below uniformly; Euler jets multiply by integers and preserve this property. With \(\varepsilon_j=|v_2Y_j|=o(m_j)\), the entire order-\(N\) tail therefore has

\[
 v_2(\text{tail})\ge Nm_j-(e+N/q+1)\varepsilon_j-O(1)
                  =Nm_j-o(m_j).                               \tag{4A.3}
\]

Convergence and leading-term uniqueness now follow uniformly: first split off finitely many \(\ell\) below a fixed cutoff, then bound the rest by (4A.3). Merely saying that every fixed coefficient has sublinear valuation would not justify an infinite-tail conclusion.

The multiplier-only Padé count uses \(U=2(d+1)q(e+1)\) unknowns and at most \(\sum_{\ell<N}q(e+\lfloor\ell/q\rfloor+2)\) conditions. Choose \(e\asymp d/q\), \(N=(2-\eta)d+O(1)\), with \(0<\eta<2-\alpha\). In the irrational case choose \(q\) large, then \(d\) large; in the rational case \(q\) is fixed and \(d\) is chosen large. The main ordinary height is \(\alpha d m\), with controlled smaller overheads, whereas precision is \(Nm-o(m)\). Crucially use base scale \(m=L_0\), not a maximum scale without its distortion factor.

Pointwise minimum-jet rescue and coarse-prefix agreement make the rational Padé value either contradict its height or vanish. In the latter case the fixed error has superlinear valuation, contradicting irrational Newton rigidity or the repaired rational leading-form argument. No degree grows with the tower level.

**Amended conditional theorem.** No positive Collatz itinerary can supply infinitely many aligned binary rank-two levels having: distinct prefix-code blocks; lengths tending to infinity with bounded distortion; common limiting fine-letter frequency; rational grouped scalar of linear height; and a subsequential coarse limit that is not eventually periodic, provided the reconstructed Padé/jet ledger above is accepted. The standalone amendment is preserved separately as `legacy_rank_two_amendment.md`; its new estimates must not be attributed to the October6 originals. A targeted second audit checked the degree/tail repair and the pointwise jet issue; this is still internal analytical review, not external certification.

The coverage gaps remain: actual return-tower alignment/marker costs, preservation of an aperiodic limit, arbitrary finite rank greater than two, linearly recurrent transfer, high-complexity compression, exhaustive orbit coverage, and nonterminal cycles. Research44 itself leaves these open. The valid rank-two local algebra is worth presenting even if the global recurrence program does not close.

## 5. FP and fairness: what is proved, what would prove too much

### 5.1 Population mixing does not establish a fixed-orbit law [LEG-16]

On odd 2-adic integers with normalized Haar measure \(\mu\), the accelerated odd-multiplier map \(U_c(n)=(cn+1)/2^{v_2(cn+1)}\), for odd \(c\ge3\), has transfer operator

\[
 Pf(q)=\sum_{a\ge1}2^{-a}f((2^aq-1)/c).
\]

If an input density depends only on the residue modulo \(2^r\), one application lowers its resolution by one, and \(P^{r-1}f=1\). For every absolutely continuous probability density,
\(\tfrac12\|P^tf-1\|_1\le\tfrac12\|f-\mathbb E_{t+1}f\|_1\to0\).
This is a genuine ensemble theorem, with direct arithmetic proof [LEG-S31].

A point mass is singular, not covered. So is a limiting sparse population if its limiting law has not been shown absolutely continuous. The family \(2^k-1\) illustrates noncommuting limits: after any fixed number \(t\) of rounds, sufficiently large \(k\) gives \(3^t2^{k-t}-1\equiv3\pmod4\), despite the broad Haar mixing result. This is not a divergent fixed seed. Even a coarse residue bias can increase for one step: equal mass on classes 1 and 3 modulo 8 is balanced modulo 4, but its next mass on 1 modulo 4 is 3/4. Statistical-fairness mechanisms therefore need a separate transfer to one chronological positive orbit, not merely a convincing mixing picture [LEG-S32].

### 5.2 The FP target and its domain [LEG-17]

The retained observer is

\[
 Q_N(r)=N^{-1}\#\{i<N:a_i\ge r\},\quad
 W_N=\sum_{r\ge1}|Q_N(r)-2^{1-r}|,\quad FP_N=(1+W_N)^{-1}.
\]

It measures the geometric marginal depth law with first-moment control. It is not the stronger assertion of an iid chronological word. On a hypothetical distinct positive orbit, (1.2) gives \(\limsup A_N/N\le\alpha<2\). Since \(\sum_rQ_N(r)=A_N/N\),

\[
 \liminf W_N\ge2-\alpha,\qquad \limsup FP_N\le1/(3-\alpha).      \tag{5.1}
\]

Thus proving \(FP_N\to1\) on that hypothetical survivor domain would exclude escape. It is not presently proved. On the indefinitely continued terminal state 1, every depth is 2 and \(FP_N\to1/2\), so an unqualified all-orbit claim is false. Cycles are a separate obligation [LEG-S09 §3].

### 5.3 Fixed-event prefix theorem, with the hard proof step exposed [LEG-18]

FP57 states: for every fixed integer \(R\ge0\) and every \(\varepsilon>0\), there is a finite, generally ineffective constant \(C_{R,\varepsilon}\) such that every actual positive odd prefix starting at \(x\), of length \(h\), with at most \(R\) events \(a_i\ge2\), satisfies

\[
 \boxed{h\le(1+\varepsilon)\log_2(x+1)+C_{R,\varepsilon}.}        \tag{5.2}
\]

The exceptional depth magnitudes are unrestricted. The number \(R\) is fixed before any dimension, form, or Diophantine theorem is chosen.

Here is enough of the proof to locate its nontrivial obligations. Put \(m_t=n_t+1\), \(Z_t=2^{A_t}m_t/3^t\). Then

\[
 Z_{t+1}-Z_t=(2^{a_t}-2)2^{A_t}3^{-(t+1)}\ge0,
 \quad x+1\le Z_t\le2^R(x+1).
\]

An induction on \(R\) disposes of bounded starting states and bounded post-event states. In a violating family with \(x\to\infty\), all post-event states may therefore be taken to infinity and \(Z_t/(x+1)\to1\) uniformly. On a subsequence, adjacent event spacings are either fixed or tend to infinity. Group the former into clusters with start \(\ell_i\), end \(k_i\), fixed widths, and diverging intercluster gaps. Set \(k=k_s\), \(A_i'=Z_{k_i}\), \(A_0'=x+1\), and \(X_i=3^kA_i'\), giving a fixed-dimensional integer vector.

At the real place choose the forms \(X_1-X_0,\ldots,X_s-X_{s-1},X_s\); at 2 and 3 choose coordinate forms. Direct valuation estimates give the decisive cancellation

\[
 \Pi(X)=\prod_{v\in\{\infty,2,3\}}\prod_i|L_{i,v}(X)|_v
 \le C_R(x+1)2^{-h}3^{\sum_i(k_i-\ell_i)}.                       \tag{5.3}
\]

All exceptional-depth magnitudes cancel, rather than being hidden in coefficients. The vector height is at most \(2^R3^h(x+1)\). A violation of (5.2) therefore makes \(\Pi(X)\le H(X)^{-\delta}\) for a fixed \(\delta>0\). Dividing by the gcd does not spoil this: it multiplies \(\Pi\) by \(g_{\rm outside\{2,3\}}^{-s-1}\le1\).

The fixed-dimensional p-adic Subspace Theorem supplies a fixed proper rational relation among the \(A_i'\). Normalization by \(x+1\) makes its coefficients sum to zero, so it becomes a nontrivial relation among cluster increments. Expand these into at most \(2R\) rational \(\{2,3\}\)-unit terms with fixed coefficients. Partition into minimally vanishing subsums. The fixed-term S-unit theorem gives finitely many projective ratios within each subsum; their ternary valuations force bounded temporal separation. No subsum can cross diverging cluster gaps. But a relation confined to a participating cluster would make its strictly positive increment vanish. This contradiction proves (5.2).

The external theorems are Schlickewei's p-adic Subspace Theorem in Evertse's formulation, and Evertse–Schlickewei–Schmidt's nondegenerate multiplicative-group equation theorem [E6–E7]. They are not new project results. The precise inputs are fixed dimension d≥2; fixed rational linear forms, linearly independent at each of the places infinity,2,3; a fixed positive exponent delta; and primitive integer vectors with the displayed form product at most H^(−delta), which lie in finitely many proper rational subspaces. For the unit equation, the number of nonzero terms, rational coefficients and finite-rank multiplicative group are fixed; after dividing a minimally vanishing subsum by one term, no proper subsum vanishes. The theorem then gives finitely many projective ratios. It supplies neither a bound on their heights nor uniformity as the number of terms grows. The saved complete proof was reread here, including primitivity and degenerate subsums; it appears coherent as a research proof. Specialist independent review remains particularly important because the conclusion is stronger than the elementary logarithmic floor.

One consequence is \(D_N/\log(N+2)\to\infty\), where \(D_N=\#\{i<N:a_i\ge2\}\), on every indefinitely continued positive orbit. Indeed, for every fixed \(\lambda>\alpha\), (5.2) and the exponential height envelope force the number of events in \([t,\lambda t]\) to tend to infinity. Summing multiplicative windows gives the result. It is still not positive density or FP convergence [LEG-S25].

### 5.4 Fixed rational dictionaries, high-source floor, and repair occupation [LEG-19–20]

FP58 generalizes the reference center \(-1\) to a fixed finite union \(\mathcal C\) of rational periodic accelerated cycles. A chosen reference path \(c_t\in\mathcal C\) incurs a repair whenever either \(a_t\ne b(c_t)\), or \(c_{t+1}\ne U(c_t)\). Pattern/phase changes are charged, not free. Let \(\beta\ge1\) be the least mean reference depth.

For at most \(R\) repairs, the asserted prefix bounds are

\[
 B_h=\sum_{t<h}b(c_t)\le(1+\varepsilon)\log_2(x+1)+K,
 \quad h\le\frac{1+\varepsilon}{\beta}\log_2(x+1)+K'.             \tag{5.4}
\]

They hold for all positive prefixes if every reference center is negative. For mixed positive/negative dictionaries every actual state must exceed a fixed floor, for example \(\lceil2\max|c|\rceil+2\). The floor is necessary: the actual fixed point 1 agrees forever with the positive reference \(\{1\}\).

The signed ledger is \(Z_t=2^{A_t}(n_t-c_t)/3^t\), with two fixed-coefficient unit terms per repair. The additional issue is zero total correction within a cluster. If this occurs, the actual affine word maps its initial rational reference exactly to the terminal one. Forward denominators divide \(D2^a\), backward denominators divide \(D3^b\); hence every intermediate denominator divides \(D\), which is coprime to 6. Backward parity makes every intermediate reference odd 2-adically, so uniqueness forces the genuine rational Collatz path. Reassigning that path removes the cluster's repairs. Remaining clusters have nonzero increments, and the fixed-form/S-unit argument applies as in (5.3), with \(2^{-B_h}\). This step, and the high-floor modification, were examined in the full FP58 proof [LEG-S26 Appendices A–B]. Constants remain nonuniform in \(R\), dictionary size, periods, and center heights.

Define canonical turnovers from source \(x_j\): \(L_j=\lceil\log_2(x_j+1)\rceil\); \(K_j\) is the first accelerated time whose accumulated depth reaches \(L_j\); \(e_j=A_{K_j}-L_j\); \(x_{j+1}=U^{K_j}(x_j)\). A sharp inherited endpoint bound is
\(\tfrac12 3^{K_j}2^{-e_j}<x_{j+1}<3^{K_j}2^{-e_j}\), so
\(L_{j+1}\le\alpha K_j-e_j+1\le\alpha L_j+1\).

Let \(r_j\) be the minimum repairs in turnover \(j\). Two adjacent turnovers with \(r_j,r_{j+1}\le R\) concatenate with at most \(2R+1\) repairs. By (5.4),
\(L_{j+1}+L_{j+2}\le\chi L_j+O_R(1)\), where \(\chi=\alpha(1+\varepsilon)/\beta<2\). Write \(\rho^2+\rho=\chi\), \(0<\rho<1\), and
\(V_j=(1+\rho)L_j+L_{j+1}\). Such a low-low pair gives \(V_{j+1}\le\rho V_j+O_R(1)\); all pairs have asymptotic expansion at most \(\alpha\). Telescoping \(\log V_j\) on a hypothetical distinct orbit bounds the density of low-low pairs. As at most two pairs are destroyed by each high-repair turnover, FP60 obtains, for each fixed \(R\),

\[
 \liminf_{J\to\infty}J^{-1}\#\{j<J:r_j>R\}
 \ge c_\beta:=\frac{-\log\rho_\beta}
 {2(\log\alpha-\log\rho_\beta)}>1/10,
 \quad \rho_\beta=\frac{\sqrt{1+4\alpha/\beta}-1}{2}.             \tag{5.5}
\]

There is no height-growth assumption. It follows that mean repairs per turnover tend to infinity. The quantifier order is fixed dictionary, fixed \(R\), long orbit, then \(R\to\infty\); no growing-\(R\) estimate is hidden here. A fixed dictionary and a fixed bound on average repairs per turnover can therefore describe only finitely many positive cycles. This is ineffective and does not identify them [LEG-S09 §4 and complete component].

The counterfamily \(x_r=2^{3r+2}-5\), with depth prefix \((1,2)^r,1,1\), has a canonical turnover with \(K=2r+2,q=L-K=r,e=0\), and \(r\) ordinary exceptions, but only one repair relative to the rational cycle \(-5,-7\). Thus the dictionary theorem is genuinely broader than bounded ordinary exceptions or bounded deficit. This finite family cannot be concatenated without compatibility.

### 5.5 Exact alternate histories and proved architecture limits [LEG-21–23]

FP60 contains constructive arithmetic, not only necessary complexity bounds. For \(M\ge0\), put \(q=M+4\). Choose a positive integer \(X\) satisfying

\[
 3^q\mid2^{2M+1}X+1,\qquad3^MX\equiv3\pmod4.
\]

Let \(V=(2^{2M+1}X+1)/3^q\), \(x=3^MX\), \(z=2^{q+1}V-1\). CRT gives infinitely many such sources. The actual alternate depth word \((1^q,2^M,3)\) from \(z\) reaches \(U(x)\), with every claimed valuation checked symbolically, and

\[
 z=\frac{64}{81}(8/9)^M x+2(2/3)^q-1<x.                         \tag{5.6}
\]

A second family \((1^q,2^m,3,3)\), under a different explicit ternary congruence, reaches additional source progressions. These are infinite families, not a cover of all sources with a particular valuation. The complete three-block architecture \((1^q,2^r,3^s)\) misses every \(x\equiv19\pmod{108}\), even with any prescribed finite initial unit run. That is an architecture obstruction, not a counterexample to Collatz.

For any alternate positive source \(z<x\) meeting the end of an initial \(k\)-unit run from \(x\), its alternate accelerated clock \(h\) must exceed \(k\). If \(v_3(x)=M\ge1\), then \(h\ge k+M+2\). This obstruction allows arbitrary alternate depths; it explains why changed-clock constructions are needed [LEG-S09 inverse component].

FP59 closes another infinite surgery family. In a word of fixed length \(h\), move \(\Delta\) divisions from position \(j\) to earlier \(i\), keeping all other depths, total budget, and endpoint fixed. The affine-carry change is

\[
 C'-C=(2^\Delta-1)\sum_{t=i+1}^{j}3^{h-1-t}2^{A_t}.
\]

The last summand uniquely has the smallest ternary valuation, \(h-1-j\). Therefore the alternate source is an integer exactly when \(2\cdot3^j\mid\Delta\). But \(a_j>\Delta\) then forces direct descent below the original source using the elementary upper bound \(U(n)\le2n\). Such surgery cannot supply a *new* smaller-source certificate for a prefix that has not already descended. It does not rule out three or more edits, changed clocks, changed endpoints, or other architectures [LEG-S22 Component04].

Finally, FP60 supplies a real-valued affine control with positivity, distinctness, polynomial growth, and the critical biased Bernoulli finite-block law. It is not integer-compatible. This shows why an argument retaining only those real/statistical features cannot finish the integer problem. The proposed universal coalescence statement and its quantitative prefix criterion remain conditional proof routes, not established consequences of (5.6).

## 6. Region Family Analysis: exact laws and the survivor intersection

### 6.1 Family parser and deterministic contracting episodes [LEG-24]

For positive odd \(n\), classify by \(q=v_2(3n-1)\):

- S: \(q=1\), \(n\equiv1\pmod4\), one accelerated round.
- A: \(q=2\), \(n\equiv7\pmod8\), one round.
- B: \(q=4\), \(n\equiv27\pmod{32}\), two rounds.
- C: \(q=3\), \(n\equiv3\pmod{16}\), two rounds.
- D: \(q\ge5\), \(n\equiv11\pmod{32}\), at least three rounds.

These are exhaustive disjoint source classes. In \(u=(n+1)/4\), an A block is \(u\mapsto3u/2\) and B is \(u\mapsto(9u+1)/8\). The expanding A/B subsystem is not the whole dynamics.

The remaining H-family blocks \(\{S,C,D\}\) satisfy strict nonterminal contraction. The sharp bounds recorded and algebraically checked in the current state are S: \(7/9\), C: \(11/19\), even-q D: \(91/107\), odd-q D: \(5/11\), with equality examples \(9\to7,19\to11,107\to91,11\to5\). For instance C has word \((1,2+h)\), \(n=(8u+1)/3\), \(u\) odd, \(u\equiv1\pmod3\), \(h=v_2(3u+1)\), and endpoint \((9n+5)/2^{h+3}\).

An H-only episode of \(r\) nonterminal blocks therefore satisfies \(n_r\le(91/107)^r n_0\). It must reach 1 or exit to A/B in at most \(\lfloor\log n_0/\log(107/91)\rfloor\) such blocks. This is an actual fixed-source result, not a population argument [LEG-S13, opening consolidated results].

It does not imply compensation for an earlier expanding episode. The explicit family \(x_M=3\cdot8^{M+1}-5\) follows \(M\) B blocks then C, ending at \(y_M=(3\cdot9^{M+1}-5)/2>x_M\) for \(M\ge5\). At \(M=5\): \(786427\to797159\). A locally contracting block need not descend below the original comparison source.

### 6.2 History-conditioned A/B laws are exact but population-based [LEG-25]

Use natural density among eligible A or B entries, equivalently normalized odd-multiplier residue cylinders, not pooled visits from trajectories. A maximal A run has length \(L=v_2(u)\) and odd endpoint \(3^L v\). Its next family probabilities are B: \(1/4\), C: \(1/2\), D: \(1/4\). For B write \(u+1=2^{3M+s}v\), \(s\in\{0,1,2\}\); the endpoint is \(9^M2^sv-1\). Conditional on a B entry, its next family probabilities are A: \(4/7\), C: \(2/7\), D: \(1/7\).

Multiplication by odd \(3^L\) or \(9^M\) is a bijection on the retained finite residue classes. Thus the same next-law holds after any fixed finite history, even when its run lengths are specified. This is an arithmetic conditional-uniformity proof, not an independent-fresh-bit assumption. The surviving alternating A/B chain has substochastic matrix

\[
 Q=\begin{pmatrix}0&1/4\\4/7&0\end{pmatrix},\qquad Q^2=I/7.
\]

Consequently surviving \(k\) complete A/B pairs has exact density \(7^{-k}\), in either orientation. Natural-density passage for a fixed number of runs truncates run lengths at \(R\), with omitted mass at most a constant times \(2^{-R}\). This does not justify interchanging an unbounded history length with the source-range limit [LEG-S15].

### 6.3 Why density zero is not fixed-seed extinction [LEG-26]

Let \(S_k\) be the nested sets of positive entries surviving \(k\) pairs. Their Haar measures and fixed-depth natural densities tend to zero. This implies a null infinite survivor set, not an empty one. For example \(E_k=\{n:7^k\mid n\}\) and \(F_k=E_k\cup\{1\}\) have identical densities, but one intersection is empty in positive integers and the other contains 1.

For nested nonempty subsets of positive integers, \(m_k=\min S_k\) is nondecreasing and
\(\bigcap_kS_k=\varnothing\) iff \(m_k\to\infty\). This is an exact fixed-source reformulation, not an estimate supplied by \(7^{-k}\). Similarly, summable positive atomic weights detect every fixed integer, but the Haar survival estimate does not transfer to that different measure.

For the repeated schedule \((A^1B^1)^k\), the map is \(F(u)=(27u+2)/16\), so \(11F(u)+2=(27/16)(11u+2)\). A fixed positive source has only finitely many copies; the infinite 2-adic source is \(-2/11\), not positive. But arbitrary schedule changes regenerate valuation, and this periodic argument does not cover them. In general a finite history has
\(2^Q u_k=3^P u_0+C\), determining a nested source residue modulo \(2^{Q+1}\). An infinite positive source exists precisely when its least positive representatives stabilize at that integer. The unproved step is their nonstabilization for every infinite compatible schedule [LEG-S14].

**Inspiration.** This checkpoint explicitly elevates the user's fixed-fraction-versus-fixed-source concern into the central proof obligation. It should receive credit as problem formulation, independently of whether a universal extinction theorem is eventually obtained.

## 7. Notation transforms and causal countermodels

### 7.1 Rational base 3/2: renewal is real, an extra resource is not [LEG-27]

For canonical base-3/2 length, let \(q_1=1\), \(q_{\ell+1}=\lceil3q_\ell/2\rceil\); then \(L(n)=\ell\) iff \(q_\ell\le n<q_{\ell+1}\). An odd shortcut step adds one digit; an even step removes \(1+g\) digits, where the gate \(g\in\{0,1\}\) has an exact prefix criterion. For \(L\ge3\), \(g(n)=1\) iff \(n<3q_{L-2}\).

For even \(n\ge8\), \(g(n)=0\) implies \(g(n/2)=1\). Odd steps do not erase a gate already set. Thus among \(E\) even events, extra deletions \(D\ge\lfloor(E-1)/2\rfloor\), apart from the stated small terminal boundary. This is a valid renewal lemma, but it does not bound the number of odd events.

Let \(r=3/2\), \(\beta=\log_r2-1\), and \(H(n)=L(n)-\log_rn\), a bounded function. Exact length and size accounting gives

\[
 D=\beta E-\sum_{\rm odd\ steps}\log_r(1+1/(3n))
       +H(n_0)-H(n_N).                                         \tag{7.1}
\]

The gate gain is therefore the ordinary growth ledger plus a bounded endpoint term, not an independent dissipative resource. Moreover the growing block 1110 has map \((27n+19)/16\), centered by \(11n+19\); \(K\) copies occur iff \(16^K\mid11n+19\). There are arbitrarily long genuine finite growing blocks as the source grows, though no fixed positive source repeats this block forever. Finite leading-base digits, finite trailing digits, and a finite future parity prescription remain jointly realizable in arbitrarily large integers via growing extension intervals and CRT [LEG-S27].

The rational-base representation is prior art, not a newly invented numeral system: Akiyama–Frougny–Sakarovitch and Eliahou–Verger-Gaugry are explicit antecedents, with rewriting comparisons to Yolcu–Aaronson–Heule and Sterin–Woods [LEG-S11; E8–E9]. The user's sorting/division-surplus intuition is recorded in NT06. Its useful formulation is a search for cumulative division surplus; the naive claim that mean geometric valuation 2 for a population forces that same mean on one positive orbit is not proved [LEG-S12].

### 7.2 Causality maps: identify missing arithmetic, not just convincing motifs [LEG-28–29]

The latest completed Pass05 distinguishes the original 3n+1 and 5n+1 maps, targeted interventions, and carryless arithmetic. A residue-matched pair of later 5n+1 episodes sharing a finite local history has different next depths because its earlier carry ancestry leaves an exact higher-modulus condition. This is evidence against attributing the outcome to the local motif alone. Such matched positive entries are not two alternative histories from one original source.

One exact intervention has a 5n+1-derived six-cycle \(7\to9\to23\to29\to73\to179\to7\). In its entry family \(7+2^{15}h\), the six-step return has a fixed-source valuation budget: positive \(h\) repeats the pattern exactly \(\lfloor v_2(h)/14\rfloor+1\) times before exit, while \(h=0\) is the cycle. This proves local exit from that template, not later compensation or descent below an earlier source.

The sharper control is the carryless map

\[
 K(n)=\operatorname{oddpart}(n\mathbin{\mathrm{XOR}}(n\ll2)\mathbin{\mathrm{XOR}}1).
\]

For \(n_m=(10\cdot8^m-3)/7\), write \(m=Lu\), \(L=2^{v_2(m)}\), \(u\) odd. If \(3u+1=4^j\), the exact polynomial identity over \(\mathbb F_2\) makes a finite block send \(n_m\) to \(n_{2m}\). It iterates to an actual unbounded positive carryless orbit from one fixed seed. With \(k=3u+1=4^j\), the full chronological mean valuation has

\[
 \liminf A_N/N=2k/(2k-1),\qquad \limsup A_N/N=(k+1)/k,
\]

so it need not even converge, and both bounds approach 1 across this family. Its bit-length ledger is \(2N-A_N\), not \(N\log_2 5-A_N\). The Frobenius identity is the operative mechanism; restoring ordinary carries with the same XOR constant produces 5n−1, not 5n+1. None of this is a Collatz counterexample [LEG-S17 §§5–7].

Other finite-bit interventions retain all the specified finite Haar depth-word masses yet create positive all-depth-one traps. The original C3/C5 finite residue matrices can forget their starting row after five steps while actual C5 cycles remain biased. These exact controls show that finite ensemble transition laws, local mixing, and motif repetition alone cannot prove an individual positive-integer fairness theorem. Their publication value is diagnostic and methodological, not evidence that original Collatz diverges [LEG-S16–17].

## 8. The López–Stoll objection and rules for imported claims [LEG-30]

The October 6 private, unsent draft questions a passage in López–Stoll's arXiv:2101.12747v1 that transfers an irrationality conclusion between a real limit and a 2-adic limit of common rational approximants. The general transfer principle is false. For example, set

\[
 b_n=\lfloor(3/2)^n\sqrt2\rfloor,\qquad a_n=2^n b_n/3^n.
\]

Then \(a_n\to\sqrt2\) in the reals, since the error is below \((2/3)^n\), while \(v_2(a_n)\ge n\), so \(a_n\to0\) in \(\mathbb Q_2\). The denominators are odd. Shared approximants, nested binary compatibility, and an irrational real limit do not imply an irrational 2-adic limit.

This example is not a counterexample to the paper's specific Collatz series or to its theorem. A special additional argument might repair the passage. The defensible project status is “dependency quarantined pending a valid specific justification,” not “paper disproved.” The saved document is a draft objection, not correspondence actually sent or an author response [LEG-S10; E10].

The same rule applies internally: algebraicity of a real normalizer, eventual substitutivity at an arbitrary phase, fresh independent bits, and a bounded-description hypothesis must each be proved or retained as assumptions. Cross-completion intuition is not a substitute for such a proof.

## 9. Publication triage and unresolved joins

**Strong candidates for a carefully scoped technical note.** The finite entropy inequality (3.2), its chronological extension (3.4), and explicit boundary terms are short enough to be independently checked. The general Hamming recurrence barrier has a clear credited predecessor and a transparent constant improvement. The arbitrary-width golden theorem has a complete finite-geometric induction and a reproducible exact verifier. Binary's corrected component recurrence and affine-word packing form a coherent arithmetic toolbox. Region's exact history-conditioned laws plus the survivor-intersection warning make a useful rigorous exposition.

**High-value proofs needing specialist review.** The amended Research43–44 combined rank-two argument should retain its explicit strengthened hypotheses, uniform-tail estimate and pointwise jet warning, separate from the original claims. FP57–58 should be isolated as theorem-and-proof manuscripts, with the two imported Diophantine theorems stated exactly, signed-cluster removal fully proved, constants explicitly ineffective, and no growing-parameter extrapolation. FP60 repair occupation and cycle-family finiteness should be presented as consequences of those fixed-dictionary theorems. The finite inverse constructions and architecture obstructions are elementary and can be reviewed separately from the deep dependency.

**Worth publishing as corrections or controls, not breakthroughs.** The binary gcd-prime counterexample; endpoint collapse of the cocycle; rational-base gate accounting; failure of a universal iid inference; zero-density versus emptiness; and carryless/intervention models all prevent attractive but invalid proof routes. Preserve the historical claim, the precise counterexample, and the surviving restricted lemma.

**Still missing.** No route here supplies a universal upper bound on compatible aperiodic histories, a uniform growing-repair Diophantine bound, a proof that every original orbit has bounded reference complexity, a fixed-positive-source escape theorem for the A/B subsystem, an all-source alternate-history descent construction, or a proof of full FP. More necessary novelty does not become a contradiction until paired with a valid upper bound on realizable novelty. Strong population decay does not become fixed-source extinction without arithmetic nonstabilization. Local compensation does not become original-source descent without the full accumulated multiplier and offset.

## 10. Reproducibility and read coverage

The October 21 audit reran the Binary corrective report's exact-arithmetic regression over 5,000 odd starts, recording 102,652 completed runs, 97,652 switch occurrences, and 1,985 distinct unit-exit states. It verified switch equations, gcd divisibility, reconstruction, telescoping, shape size, repeated-word packing, and the explicit prime-content counterexample. Pooled trajectories overlap; these are not independent orbit trials.

The golden geometry verifier was also rerun successfully, as described in §4.3. Neither computation proves an asymptotic statement or establishes Collatz. JSON outputs accompany the source ledger.

Forty mathematical notes, plus the exact golden verifier, were retrieved. The Research35/39–44 addendum also includes a new independent exact regression of126,719 prefix-incomparable block pairs,266,910 normal-form degree cases and21 Padé dimension cases, plus a separately labeled analytical amendment. These do not constitute formal verification. The cumulative FP handoff was read only through line 1,000 of 12,438; Region's current state only through line 1,000 of 4,585, with its opening current theorems used and its two latest standalone probability/intersection notes read in full. FP58's first 1,000 lines and final 103 lines were read separately, completing the file. Some older reports were used only for specific sections; this is a selective latest-first audit, not a claim that every historical branch file has been line-by-line certified.


## Source register: project documents

- **[LEG-S01]** Collatz_Proof_Shortcut_Research_15_General_Hamming_Recurrence_Barrier_2026-10-06.md. Library ID `libfile_d9f52b1db2fc819183e2b2a1ebbe7cd7`; path `/Collatz_Proof_Shortcut_Research_15_General_Hamming_Recurrence_Barrier_2026-10-06.md`; version not supplied (immutable uploaded file). Read: §§1–6: clean-window construction, general shift barrier, edit corollaries, credits.
- **[LEG-S02]** Collatz_Research_15_Golden_Rotation_Proof_HANDOFF_2026-10-06.md. Library ID `libfile_c583ff1b4d10819189ecca97bcb7c053`; path `/Collatz_Research_15_Golden_Rotation_Proof_HANDOFF_2026-10-06.md`; version not supplied (immutable uploaded file). Read: Complete restricted theorem and §§1–5: interval partition, two-defect argument, endpoint intersection, verifier.
- **[LEG-S03]** Collatz_Binary_Route_Audit_and_Proof_Integration_2026-10-07.md. Library ID `libfile_1974ea494ff881918ff5a9d83647d4ec`; path `/Collatz_Binary_Route_Audit_and_Proof_Integration_2026-10-07.md`; version not supplied (immutable uploaded file). Read: §§1–10: full mathematical correction audit; §11 exact regression script rerun.
- **[LEG-S04]** Collatz_Binary_Route_25_Periodic_Recycling_Closure_and_Three_Question_Resolution_2026-10-07.md. Library ID `libfile_f2a45ffa7cac8191ba84fe1ec6a62b73`; path `/Collatz_Binary_Route_25_Periodic_Recycling_Closure_and_Three_Question_Resolution_2026-10-07.md`; version not supplied (immutable uploaded file). Read: Full periodic full-affine-program argument and its stated aperiodic boundary; subordinate to later audit.
- **[LEG-S05]** Collatz_Binary_Route_22_Subpolynomial_Component_Recurrence_2026-10-07.md. Library ID `libfile_594ac686141c81918ff0aea50dd4498b`; path `/Collatz_Binary_Route_22_Subpolynomial_Component_Recurrence_2026-10-07.md`; version not supplied (immutable uploaded file). Read: Full subpolynomial component recurrence proof.
- **[LEG-S06]** Collatz_Binary_Route_24_Affine_Word_Precision_Packing_2026-10-07.md. Library ID `libfile_4e92a94150648191887bc7ea6b606873`; path `/Collatz_Binary_Route_24_Affine_Word_Precision_Packing_2026-10-07.md`; version not supplied (immutable uploaded file). Read: Full affine-word precision and packing proof; constants corrected by later audit.
- **[LEG-S07]** Collatz_Binary_Route_23_Endpoint_Collapse_of_Correction_Stream_2026-10-07.md. Library ID `libfile_b74d2a5eed888191a5a73f38c1856886`; path `/Collatz_Binary_Route_23_Endpoint_Collapse_of_Correction_Stream_2026-10-07.md`; version not supplied (immutable uploaded file). Read: Full endpoint-collapse identities.
- **[LEG-S08]** Collatz_FP_Current_Handoff.md. Library ID `libfile_10e8dae86bc08191bfd8c0a963bb80f3`; path `/Collatz Notation Transform/Collatz_FP_Current_Handoff.md`; version 37. Read: Opening current FP60 summary and inherited material through line1000 only; not a proof substitute.
- **[LEG-S09]** Collatz_FP_60_Proof_Routes_and_Checked_Progress_2026-10-11.md. Library ID `libfile_45d19c53ee748191b7ee395bbfd24d59`; path `/Collatz Notation Transform/Collatz_FP_60_Proof_Routes_and_Checked_Progress_2026-10-11.md`; version not supplied (immutable uploaded file). Read: Complete executive report and embedded three research components: repair occupation, cycle consequence, inverse constructions and controls.
- **[LEG-S10]** Lopez_Stoll_Proof_Objection_Draft_2026-10-06.md. Library ID `libfile_4725015f52688191b921b7a14f5bbd7a`; path `/Lopez_Stoll_Proof_Objection_Draft_2026-10-06.md`; version not supplied (immutable uploaded file). Read: Entire private unsent objection draft, including general cross-completion counterexample.
- **[LEG-S11]** Collatz_Notation_Transform_04_Breakthrough_Assessment_and_Prior_Art_2026-10-07.md. Library ID `libfile_d11b29c093208191880ae17334f9d1f8`; path `/Collatz Notation Transform/Collatz_Notation_Transform_04_Breakthrough_Assessment_and_Prior_Art_2026-10-07.md`; version not supplied (immutable uploaded file). Read: Entire prior-art assessment and listed rational-base/rewriting antecedents.
- **[LEG-S12]** Collatz_Notation_Transform_06_Sorting_and_Division_Surplus_Hypothesis_2026-10-07.md. Library ID `libfile_e6bcc042dc6481918b3e375ae1c523a7`; path `/Collatz Notation Transform/Collatz_Notation_Transform_06_Sorting_and_Division_Surplus_Hypothesis_2026-10-07.md`; version not supplied (immutable uploaded file). Read: Entire note; §1 user-origin quotes, exact sorting targets, audited drift heuristic.
- **[LEG-S13]** Region_Family_Analysis_Current_State_2026-10-12.md. Library ID `libfile_3c60af12c4708191813403e13b8918ec`; path `/Collatz Notation Transform/Region Family Analysis/Region_Family_Analysis_Current_State_2026-10-12.md`; version 9. Read: Current opening consolidation through line1000 only, especially family parser, contraction, transition matrix, compensation counterfamily; historical remainder not certified.
- **[LEG-S14]** Collatz_Infinite_Survivor_Intersection_Checkpoint_2026-10-12.md. Library ID `libfile_7046e905ce2c81919ba4b29ed85037db`; path `/Collatz Notation Transform/Region Family Analysis/Collatz_Infinite_Survivor_Intersection_Checkpoint_2026-10-12.md`; version not supplied (immutable uploaded file). Read: Entire fixed-source survivor-intersection checkpoint.
- **[LEG-S15]** Collatz_AB_History_Conditioned_Transition_Probabilities_2026-10-12.md. Library ID `libfile_b28c8f86f62481918af0ce6a99ead535`; path `/Collatz Notation Transform/Region Family Analysis/Collatz_AB_History_Conditioned_Transition_Probabilities_2026-10-12.md`; version not supplied (immutable uploaded file). Read: Entire maximal-run history-conditioned laws, finite-history density proof and scope limits.
- **[LEG-S16]** Archaeology_Pass05_Causality_Map_2026-10-13.md. Library ID `libfile_7322ca927ce88191988839ca80383f9c`; path `/Collatz Notation Transform/Causality Map Route/Archaeology_Pass05_Causality_Map_2026-10-13.md`; version not supplied (immutable uploaded file). Read: Entire Pass05 map and distinctions between original maps, interventions and carryless control.
- **[LEG-S17]** Archaeology_Pass05_Analysis_2026-10-13.md. Library ID `libfile_8d6e32a9b7b88191a01da00811f96ca0`; path `/Collatz Notation Transform/Causality Map Route/Archaeology_Pass05_Analysis_2026-10-13.md`; version not supplied (immutable uploaded file). Read: Entire Pass05 analysis; exact algebra checked at exposition level; underlying large-trajectory bundles not rerun.
- **[LEG-S18]** Collatz_Proof_Shortcut_Research_14_Height_Optimized_Defect_Floor_2026-10-06.md. Library ID `libfile_d5fdee1838a0819191b71815fc7315ec`; path `/Collatz_Proof_Shortcut_Research_14_Height_Optimized_Defect_Floor_2026-10-06.md`; version not supplied (immutable uploaded file). Read: Height-optimized transition/exception floor and clock conversion.
- **[LEG-S19]** Collatz_Proof_Shortcut_Research_11_Binary_Parity_Complexity_and_Growth_Language_Spectrum_2026-10-06.md. Library ID `libfile_757d818e9cfc819194f75dddaf4e04b9`; path `/Collatz_Proof_Shortcut_Research_11_Binary_Parity_Complexity_and_Growth_Language_Spectrum_2026-10-06.md`; version not supplied (immutable uploaded file). Read: Binary factor-language framework and scope corrections; not every inherited historical comparison recertified.
- **[LEG-S20]** Collatz_Proof_Shortcut_Research_06_Bi_Convergent_Correction_Series_and_Revised_Endgame_2026-10-06.md. Library ID `libfile_eacff95010648191a84bb714dd93e23c`; path `/Collatz_Proof_Shortcut_Research_06_Bi_Convergent_Correction_Series_and_Revised_Endgame_2026-10-06.md`; version not supplied (immutable uploaded file). Read: Bi-convergent correction identities, inherited summability, failed product-formula route and E-sequence comparison.
- **[LEG-S21]** Collatz_Research_13_Golden_Renormalization_Bridge_Cocycle_2026-10-05.md. Library ID `libfile_d8b59830fd00819182703cc08a925cee`; path `/Collatz_Research_13_Golden_Renormalization_Bridge_Cocycle_2026-10-05.md`; version not supplied (immutable uploaded file). Read: Bridge-unit definition/composition law, phase/substitution and transported-residue claims read against later repair.
- **[LEG-S22]** Collatz_FP_59_Chronological_Entropy_Growing_Description_Costs_and_Relocation_Barriers_2026-10-11.md. Library ID `libfile_8cb680b391448191908ac448d3371490`; path `/Collatz_FP_59_Chronological_Entropy_Growing_Description_Costs_and_Relocation_Barriers_2026-10-11.md`; version not supplied (immutable uploaded file). Read: Complete empirical conditional-entropy, growing-machine, relocation proofs and embedded audits.
- **[LEG-S23]** Collatz_Binary_Route_08_Finite_Height_Capacity_and_Near_Linear_Bit_Height_2026-10-07.md. Library ID `libfile_23a916bd51d08191980214e92baa7a67`; path `/Collatz_Binary_Route_08_Finite_Height_Capacity_and_Near_Linear_Bit_Height_2026-10-07.md`; version not supplied (immutable uploaded file). Read: Finite cap and logarithmic-form application read with later audit; primary Chim paper opened, application not externally certified.
- **[LEG-S24]** Collatz_Binary_Route_03_All_Exponent_Centers_and_Run_Ledger_2026-10-06.md. Library ID `libfile_74a76f04d2a88191874e8e645994469e`; path `/Collatz_Binary_Route_03_All_Exponent_Centers_and_Run_Ledger_2026-10-06.md`; version not supplied (immutable uploaded file). Read: All-exponent centered-run definition and exact ledger; later audit controls final statements.
- **[LEG-S25]** Collatz_FP_57_Fixed_Event_Prefix_Bound_and_Bounded_Deficit_Closure_2026-10-10.md. Library ID `libfile_f02753504dcc819181cda6f3947c66f2`; path `/Collatz Notation Transform/Collatz_FP_57_Fixed_Event_Prefix_Bound_and_Bounded_Deficit_Closure_2026-10-10.md`; version not supplied (immutable uploaded file). Read: Complete fixed-event prefix proof, Subspace/S-unit dependencies, primitive rescaling, exceptional-subspace resolution and rate consequences.
- **[LEG-S26]** Collatz_FP_58_Complete_Report_and_Symbolic_Scope_Check_2026-10-10.md. Library ID `libfile_644b115ffb2081918e82715730d1d6d0`; path `/Collatz Notation Transform/Collatz_FP_58_Complete_Report_and_Symbolic_Scope_Check_2026-10-10.md`; version not supplied (immutable uploaded file). Read: Complete report in two reads; finite negative/mixed reference prefix proof, zero-cluster removal, high-floor restriction, symbolic family and external-reference notes.
- **[LEG-S27]** Collatz_Notation_Transform_03_Gate_Renewal_Theorem_and_Size_Accounting_Audit_2026-10-07.md. Library ID `libfile_196b889001488191814f6769360ab155`; path `/Collatz Notation Transform/Collatz_Notation_Transform_03_Gate_Renewal_Theorem_and_Size_Accounting_Audit_2026-10-07.md`; version not supplied (immutable uploaded file). Read: Entire gate-renewal theorem, rational-base length accounting, finite growing block and CRT scope control.
- **[LEG-S28]** Collatz_Audit_Repair_HANDOFF_2026-10-05_2148_CDT.md. Library ID `libfile_013245ae4b5c8191afbdfe4b9f4929c3`; path `/Collatz_Audit_Repair_HANDOFF_2026-10-05_2148_CDT.md`; version 1. Read: Entire October5 repair: phase hypothesis, residue-nesting counterexample, corrected numerical scope.
- **[LEG-S29]** Collatz_Strategy_01_Full_Project_Review_and_One_Goal_2026-10-08.md. Library ID `libfile_203830d6183881919bb35b8331121fcf`; path `/Collatz Notation Transform/Collatz_Strategy_01_Full_Project_Review_and_One_Goal_2026-10-08.md`; version not supplied (immutable uploaded file). Read: Current strategy synthesis and corrected entropy threshold; inherited full-project coverage not reproduced.
- **[LEG-S30]** Entropy_Height_Finite_Lemma_2026-10-08.md. Library ID `libfile_7821d95a48f481919818d1c01fbd47ce`; path `/Collatz Notation Transform/Entropy_Height_Finite_Lemma_2026-10-08.md`; version not supplied (immutable uploaded file). Read: Complete finite entropy proof, exact height identity, all-time consequence and boundary-controlled occupation addendum.
- **[LEG-S31]** Collatz_FP_02_Alternation_Mixing_and_Its_Domain_2026-10-08.md. Library ID `libfile_70ca1e98257c8191850d7093abff74af`; path `/Collatz Notation Transform/Collatz_FP_02_Alternation_Mixing_and_Its_Domain_2026-10-08.md`; version not supplied (immutable uploaded file). Read: Entire finite-resolution/absolutely-continuous mixing proof and singular-population controls.
- **[LEG-S32]** Collatz_FP_14_Statistical_Fairness_Mechanisms_2026-10-08.md. Library ID `libfile_1716c045b5648191921ef654996ac281`; path `/Collatz Notation Transform/Collatz_FP_14_Statistical_Fairness_Mechanisms_2026-10-08.md`; version not supplied (immutable uploaded file). Read: Fairness mechanism survey and domain restrictions; used as background rather than independent proof of a trajectory law.
- **[LEG-S33]** Collatz_Proof_Shortcut_Research_01_Critical_Survival_Entropy_and_Fixed_Source_Stabilization_2026-10-06.md. Library ID `libfile_9c2fdfcab858819198879234fa150c05`; path `/Collatz_Proof_Shortcut_Research_01_Critical_Survival_Entropy_and_Fixed_Source_Stabilization_2026-10-06.md`; version not supplied (immutable uploaded file). Read: Critical-survival and stabilization framing; latest standalone checkpoints prioritized.
- **[LEG-S34]** collatz_golden_geometry_verify.py. Library ID `libfile_41829de61b7c8191bfb26efc0e4c7fd3`; path `/collatz_golden_geometry_verify.py`; version not supplied (immutable uploaded file). Read: Exact Q(sqrt5) arithmetic; half-open circle partitions; finite intersection and late-defect regressions.

- **[LEG-S35]** Collatz_Research_44_Rational_Slope_Residual_Rigidity_and_Rank_Two_Closure_2026-10-06.md. Library ID `libfile_0ee99dbc95308191bb9ad5df5ea1ba2e`; path `/Collatz_Research_44_Rational_Slope_Residual_Rigidity_and_Rank_Two_Closure_2026-10-06.md`; version not supplied (uploaded file). Read: Entire Research44. Rational residual height, regraded Padé count, normal-weight separation, fixed residual root reduction, final claimed rank-two theorem. Missing infinite-tail estimate repaired separately in2026-10-21audit..
- **[LEG-S36]** Collatz_Research_43_Irrational_Length_Slope_Exclusion_and_Newton_Face_Rigidity_2026-10-06.md. Library ID `libfile_bc120f43f71481918463d79c0b5e51ea`; path `/Collatz_Research_43_Irrational_Length_Slope_Exclusion_and_Newton_Face_Rigidity_2026-10-06.md`; version not supplied (uploaded file). Read: Entire Research43. Formal path-series nonrationality, multiplier-only Padé count, irrational Newton lemma, tower application. Standalone theorem omits common-frequency/residual-height input required by its proof..
- **[LEG-S37]** Collatz_Research_42_Rank_Two_Correction_Elimination_and_Fixed_Shape_Descent_2026-10-06.md. Library ID `libfile_7b132917bcc4819186f94654d85344b3`; path `/Collatz_Research_42_Rank_Two_Correction_Elimination_and_Fixed_Shape_Descent_2026-10-06.md`; version not supplied (uploaded file). Read: Entire Research42. Exact correction elimination, prefix-code nondegeneracy, weighted-path rationality, fixed monomial shape height and compactness theorem..
- **[LEG-S38]** Collatz_Research_41_Equal_Multiplier_Rank_Two_Compactness_Descent_2026-10-06(2).md. Library ID `libfile_c1c9e98217988191a23a803257d76741`; path `/Collatz_Research_41_Equal_Multiplier_Rank_Two_Compactness_Descent_2026-10-06(2).md`; version not supplied (uploaded file). Read: Entire Research41 latest numberedcopy(2). Equal-(length,odd-count) collapse, compactness precision, height-rigidity application, explicit aperiodic-limit/alignment assumptions..
- **[LEG-S39]** Collatz_Research_40_Height_Rigidity_and_Compatible_Jet_Repair_2026-10-06.md. Library ID `libfile_9d1af27c208c8191a4776b0468e72a19`; path `/Collatz_Research_40_Height_Rigidity_and_Compatible_Jet_Repair_2026-10-06.md`; version not supplied (uploaded file). Read: Entire Research40. Fixed-series height rigidity proof and compatible Euler jets, including minimum-jet evaluation identity and restrictions..
- **[LEG-S40]** Collatz_Research_39_Two_Leaf_Descent_Audit_and_Return_Word_Repair_2026-10-06.md. Library ID `libfile_b6d38042fbc88191b6f58c453adcc69d`; path `/Collatz_Research_39_Two_Leaf_Descent_Audit_and_Return_Word_Repair_2026-10-06.md`; version not supplied (uploaded file). Read: Entire Research39. Generalized-edge two-leaf counterexample, return-word convention correction, local conjugacy and jet warnings. Source reproduction archive not rerun..
- **[LEG-S41]** Collatz_Research_35_Decorated_Scalar_Pade_Higher_Rank_Count_2026-10-06(2).md. Library ID `libfile_c58c9990ac5c81919f539ce629b0a479`; path `/Collatz_Research_35_Decorated_Scalar_Pade_Higher_Rank_Count_2026-10-06(2).md`; version not supplied (uploaded file). Read: Entire Research35 latest numberedcopy(2). Decorated scalar construction, common-frequency residual height, fixed-rank dimension count and unresolved specialization boundary..

## Primary external references and inspection scope

- **[E1]** D. J. Bernstein and J. C. Lagarias, *The 3x+1 conjugacy map*, [author-hosted primary PDF](https://websites.umich.edu/~lagarias/doc/bernstein.pdf). Opened for the classical 2-adic parity-conjugacy background. The finite congruence argument used here is reproduced in §1.
- **[E2]** K. C. Chim, *Lower bounds for linear forms in two p-adic logarithms*, Journal of Number Theory266 (2025), 295–349, Theorem2.1, DOI [10.1016/j.jnt.2024.07.012](https://doi.org/10.1016/j.jnt.2024.07.012), [author/institution-hosted full text](https://tugraz.elsevierpure.com/ws/portalfiles/portal/92346766/1-s2.0-S0022314X24001793-main.pdf). Primary PDF opened; the project audit's detailed substitution is retained as the application to be specialist-checked.
- **[E3]** M. Sharpe / Collatz proof project, [repository](https://github.com/msharpe248/collatz), [mechanical-classification TeX](https://raw.githubusercontent.com/msharpe248/collatz/main/paper/mechanical_classification.tex), [orbit-summability TeX](https://raw.githubusercontent.com/msharpe248/collatz/main/paper/orbit_summability.tex), and [DefectHeight Lean source](https://github.com/msharpe248/collatz/blob/main/lean/Collatz/DefectHeight.lean). Actual TeX theorem/proof text and source were inspected, not just README descriptions. Both papers are dated September 5, 2026 in the inspected text. Root inspection pinned OrbitPacking.lean at commit ec8174b567d5cab4960024782210b5f5db02bd3a; this chapter did not execute a Lean build. These are primary author/project artifacts, not an external peer-review guarantee.
- **[E4]** M. V. P. García and F. A. Tal, *A note on the generalized 3n+1 problem*, Acta Arithmetica 90 (1999), 245–250, [DOI](https://doi.org/10.4064/aa-90-3-245-250), [journal PDF](https://matwbn.icm.edu.pl/ksiazki/aa/aa90/aa9033.pdf). Classical interval-packing antecedent. Direct PDF access in this worker returned403; its role was recovered from the project and Sharpe's explicit proof/credit, with primary verification assigned to the bibliography audit. Do not describe the worker as having read the full original.
- **[E5]** S. Akiyama and M. Shirasaka, quadratic-rotation symbolic-dynamics work, [primary journal page](https://www.jstage.jst.go.jp/article/jmath/59/4/59_4_1199/_article/-char/en). The phase restriction is sourced to the project's explicit October5 repair; the theorem was not independently recertified here. The final golden proof does not depend on it.
- **[E6]** J.-H. Evertse, *The p-adic Subspace Theorem* (2011), [author notes](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf), Theorem1.1, attributing the p-adic theorem to H. P. Schlickewei (1977). Primary statement retrieved; only the fixed-dimensional rational-form specialization at infinity,2,3 is used. The project separately records page-image inspection.
- **[E7]** J.-H. Evertse, H. P. Schlickewei, W. M. Schmidt, *Linear equations in variables which lie in a multiplicative group*, Annals of Mathematics155 (2002), 807–836, [journal](https://annals.math.princeton.edu/2002/155-3/p04), [author preprint](https://arxiv.org/abs/math/0409604). Primary statement retrieved. Only finite projective ratios of fixed-length nondegenerate unit equations are used, not bounds on solution heights or growing-dimensional uniformity.
- **[E8]** S. Akiyama, C. Frougny, J. Sakarovitch, rational-base numeration (2008), [author-hosted description](https://perso.telecom-paristech.fr/jsaka/PUB/Files/RBNS-abs.html). Attribution recovered from NT04 and confirmed as an antecedent in E9; not independently reviewed theorem by theorem.
- **[E9]** S. Eliahou and J.-L. Verger-Gaugry, rational-base/Collatz work (2025), [primary journal PDF](https://comptes-rendus.academie-sciences.fr/mathematique/item/10.5802/crmath.662.pdf). Primary text opened; credits rational base3/2 to Akiyama–Frougny–Sakarovitch. Rewriting comparisons cited by NT04 are [Yolcu–Aaronson–Heule](https://arxiv.org/html/2105.14697v3) and [Sterin–Woods](https://arxiv.org/html/2007.06979v4); these comparisons were not independently audited in this worker.
- **[E10]** López–Stoll, [arXiv:2101.12747v1](https://arxiv.org/abs/2101.12747v1), [primary PDF](https://arxiv.org/pdf/2101.12747v1). Primary PDF opened; the saved objection targets printed p.7 after equation15, p.8 after equation16, and the theorem transfer on p.29. This chapter proves only the general countercontrol in §8, not a paper-specific theorem refutation.

- **[E11]** Olivier Rozier, *The3x+1 Problem: A Lower Bound Hypothesis*, [author-hosted primary PDF](https://www.ipgp.fr/~rozier/pub/LBHv4.pdf), especially Lemma2.5/Theorem2.6. Primary text opened; the bibliography reviewer inspected the distinct-odd harmonic correction in detail. Its lower-bound hypothesis is conjectural and is not imported as a theorem.
- **[E12]** Fabien Durand, *A characterization of substitutive sequences using return words*, [primary preprint](https://arxiv.org/pdf/0807.3322), §2.3 and Proposition6. Actual definition and code conclusion inspected directly. The first-right-return comparison source, Berthé etal., *Maximal bifix decoding*, was named in Research39, but its author-hosted PDF timed out in this audit; no uninspected theorem is attributed to it.


\clearpage

# Constraint maturation, exact certificate closure, and source-faithful representations

## Scope, status, and the right interpretation of “closure”

This chapter audits the Constraint Maturation Route, its comparison/faithful-jet continuation, the October 18 concrete and signed-word closure reports, and Creative Closure 08–09 of October 20. The strongest conclusions in these sources are exact structural theorems, restricted impossibility theorems, explicitly guarded infinite certificate families, and conditional endgames. They do **not** prove universal Collatz convergence. In particular, “a terminating compiler,” “a finite local normalizer,” “an exact presentation,” and “a complete proof of a conditional closure theorem” must not be conflated with termination of the outer arithmetic dynamics.

There are several publishable-sized mathematical objects here, subject to specialist review and a fuller priority search: the integral signed-word presentation and its birth-basis normalization; primitive-section kernel transfer and a bounded-replay obstruction; a faithful first-jet encoding at the golden ratio; quantitative restrictions on the 12/112 subsystem; and collision-aware certificate transport. The most recent receiver families are useful construction results, but their novelty relative to earlier merger formulae is not established. The packing argument immediately used in Creative Closure 09 is explicitly credited to Michael Sharpe; the earlier García–Tal collision-free-window antecedent and its October 15 internal transport are also essential provenance, not a new project result.

Throughout, “proved” means a written argument whose stated hypotheses have been checked in this audit. It does not mean proof-assistant verification or independent journal refereeing. Reported verifier counts are implementation checks, not independent mathematical evidence. Internal source keys are listed at the end; the machine-readable read log records exact Library identities and the distinction between full text retrieval and section-level audit.

## 1. Notation and the source-ownership contract

Use the shortcut map
\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd},\end{cases}
\]
and the accelerated odd map
\[
S(n)=\frac{3n+1}{2^{a(n)}},\qquad a(n)=v_2(3n+1).
\]
In certificates, 1 may be made absorbing. Where complete parity coding is used, retain the ordinary shortcut convention \(T(1)=2,T(2)=1\). A hypothetical escaping orbit never reaches these states, so the conventions agree on it. Counts of shortcut operations, odd rounds, renewal blocks, and binary decoder steps are different clocks.

For a finite positive depth word \(w=(a_1,\ldots,a_m)\), let \(H_j=\sum_{i\le j}a_i\), \(H_0=0\), and
\[
B_w=\sum_{j=0}^{m-1}3^{m-1-j}2^{H_j}.
\]
Its formal action is
\[
S_w(x)=\frac{3^m x+B_w}{2^{H_m}}.
\]
It becomes an actual orbit segment only on its exact guard. One convenient full odd-input/odd-output guard is
\[
x\equiv(2^{H_m}-B_w)(3^m)^{-1}\pmod{2^{H_m+1}}.
\]
Backward integrality authenticates the preceding depths: if a positive odd endpoint \(z\) gives an integer inverse source \((2^{H_m}z-B_w)/3^m\), successive predecessors are positive odd and have exactly the prescribed depths. This is finite arithmetic, not a universal path-existence assertion.

A smaller-source certificate at original target \(N\) is a genuine finite merger between \(N\) and a positive source \(Y<N\). Under strong induction, the supplied proof of \(Y\) proves \(N\). Larger checkpoints may be used if they are owned by such an already supplied source. Replacing the original bound \(N\) with a later, much larger checkpoint would invalidate that induction. Creative Closure 08–09 repeatedly preserves this distinction.

## 2. The 12/112 subsystem: strong restrictions without all-word exclusion

### 2.1 Exact guarded model and finite-versus-infinite quantifiers

The depth macros \(A=(1,2)\), \(B=(1,1,2)\) have actions \((9n+5)/8\) and \((27n+19)/16\). On an indefinitely continuing macro itinerary, after its first macro write \(n=36u-5\). The normalized system is
\[
A(u)=9u/8\quad(u\equiv0\bmod8),\qquad
B(u)=(27u-1)/16\quad(u\equiv3\bmod16).
\]
Both strictly increase positive legal integers. A word with \(a\) A's and \(b\) B's fixes one source residue modulo \(2^{H}\), \(H=3a+4b\), with formal composition
\[
F_w(u)=(P_wu-C_w)/2^H,\qquad P_w=3^{2a+3b}.
\]
Every finite word has arbitrarily large positive realizers. This establishes \(\forall k\,\exists u_k\), not \(\exists u\,\forall k\). The missing assertion is that no **one fixed positive integer** realizes an infinite word. [CC05, CC09]

The inverse contractions are
\[
I_A(y)=8y/9,\qquad I_B(y)=(16y+1)/27.
\]
They have an ordinary-real invariant interval \([0,1/11]\), while their 2-adic images are disjoint cylinders \(8\mathbb Z_2\) and \(3+16\mathbb Z_2\). Each infinite address has one 2-adic source. The real and 2-adic limits of its rational approximants need not be equal as numbers in a common ordered field. A generic sign-transfer argument is false: the alternative inverse maps \(2y/3,(2y+1)/3\) have real attractor \([0,1]\) but cover all of \(\mathbb Z_2\); their forward system admits the increasing positive orbit \(2,3,4,6,9,13,\ldots\). This is a countermodel to a method, not a Collatz counterexample.

### 2.2 A source-specific factor-complexity theorem

Let \(p_s(k)\) count distinct length-\(k\) factors in a hypothetical infinite positive A/B itinerary. Set \(\lambda=27/16\), \(g=\log_2\lambda\). Then [CC05, Theorem 1]
\[
p_s(k)\ge\max\left(1,1+\left\lfloor\frac{3k-\log_2u_0}{g}\right\rfloor\right),
\quad
\liminf_{k\to\infty}\frac{p_s(k)}k\ge\frac3{\log_2(27/16)}\approx3.97410.
\]
**Proof.** Equal length-\(k\) windows at positions \(i<j\) impose the same residue modulo \(2^{H(w)}\ge2^{3k}\). Since the positive states strictly increase, \(u_j-u_i\ge2^{3k}\). But \(u_j<u_0\lambda^j\), so \(j>(3k-\log_2u_0)/g\). All windows beginning before that threshold are distinct. Counting proves the claim.

This excludes eventually periodic, Sturmian/Fibonacci, and the cited Thue–Morse macro codes by their known low factor complexities. It does not exclude a high-complexity aperiodic itinerary. Credit the classical combinatorics of words separately from this arithmetic application; the internal report’s complexity citations are pointers, not a completed priority review.

### 2.3 Switching and finite rational-center pressure

A run of \(r\) A's starting at \(u\) requires \(2^{3r}\mid u\). A run of \(r\) B's requires \(2^{4r}\mid11u-1\), because
\[
11B(u)-1=(27/16)(11u-1).
\]
Writing \(a=\log_2(11u_0)/3\), \(b=\log_2(27/16)/3\), a prefix of \(m\) macros with \(s(m)\) switches obeys
\[
m\le\frac ab\big((1+b)^{s(m)+1}-1\big).
\]
Indeed a run beginning at time \(t\) has length at most \(a+bt\); iterate this inequality over constant-symbol runs. Thus an infinite itinerary would require logarithmically many switches. That still permits infinitely many renewals. [CC05, Theorem 2]

A better two-place object is the **finite rational periodic center**
\[
c_w=\frac{C_w}{P_w-2^H}=\frac{p_w}{d_w}\in[0,1/11],
\]
in lowest terms, with \(d_w\) odd. Every positive legal source satisfies
\[
d_wu-p_w\in2^H\mathbb Z_{>0},\qquad u\ge c_w+2^H/d_w.
\]
This follows by subtracting the center equation from the source congruence, using invertibility of \(P_w-2^H\) modulo \(2^H\), and ordinary positivity. Consequently an infinite fixed source requires \(d_w\ge2^H/u_0\) at every prefix. Divergence of
\[
\max_{t\le T}(H_t-\log_2d_{w_t})_+
\]
would exclude that address. CC09 proves such compression for a balanced two-block substitution family, but not for arbitrary addresses. Growing denominators of order \(P_w\) remain compatible with the inequality. This is a genuine finite-rational bridge, not an identification of infinite real and 2-adic limits.

## 3. Arithmetic description restrictions: what S-unit arguments actually buy

For \(S_c(x)=\operatorname{oddpart}(cx+1)\), fixed odd \(c\ge3\), group a maximal depth-one run with its next depth-at-least-two exit. At its entry define
\[
(c-2)x_i+1=2^{h_i}K_i,\quad K_i\text{ odd},
\]
and write the deep depth \(d_i=e_i+1\ge2\). The exact renewal equation is
\[
c^{h_i}K_i+2^{e_i}-2^{e_i+h_{i+1}}K_{i+1}=1.
\]
The three signed terms have no vanishing proper subsum: the first two are positive and at least 3 and 2, while the negative term’s magnitude is their sum minus 1 and exceeds either one.

**Restricted finiteness theorem.** For a fixed finite prime set \(\mathcal S\), only finitely many positive renewal transitions have both endpoint cores \(\mathcal S\)-supported. Apply the Evertse–Schlickewei–Schmidt theorem to the displayed nondegenerate equation in the multiplicative group generated by \(\mathcal S\cup\{2\}\cup\operatorname{primes}(c)\). Each solution triple determines the next state, and leaves only finitely many initial \(h_i\). Hence eventual confinement of all cores to one finite prime set implies eventual periodicity, not necessarily arrival at 1. [CC11, §6; ESS is an external deep input.]

CC12 extends this to a **fixed number \(q\ge1\)** of renewals with unrestricted intermediate cores. The expanded chronological equation has \(2q+2\) terms; exact binary valuation order forces any zero subsum to acquire every term. Fixed-\(q\) S-unit finiteness therefore bounds returns whose two endpoint cores lie in a fixed finite-prime family. On a nonperiodic orbit, bounded-gap returns occur only finitely often, and such cores have density zero in renewal time. The dimension and bound depend on \(q\); taking \(q\to\infty\) while keeping those constants fixed would be invalid.

CC13 makes the parameter dependence explicit. For a dictionary \(D=\bigcup_{\ell=1}^{L}\eta_\ell\Gamma\), where \(\Gamma\le\mathbb Q_{>0}^{\times}\) has rank \(r\), set
\[
n_q=2q+1,\quad D_q=(6n_q)^{3n_q},\quad B_q(r)=\exp(D_q(n_q+2r+1)).
\]
On any segment with distinct first-successor states,
\[
\#\{i:K_i,K_{i+q}\in D\}\le L^2B_q(r).
\]
For a length-\(N\) core window,
\[
J_D\le1+\left\lfloor\frac{N-1}{Q+1}\right\rfloor+L^2\sum_{q=1}^QB_q(r).
\]
Thus even a dictionary chosen after observing the window cannot capture a positive fraction when \(r(N)=o(\log N)\) and \(\log L(N)=o(\log N)\). Fix \(Q\) first, let \(N\to\infty\), then let \(Q\to\infty\). For the relative rank of the full core window,
\[
\operatorname{rank}\langle K_i/K_0:1\le i<N\rangle
\ge\max\left(0,\frac{\log(N-1)}{2\cdot18^9}-2\right).
\]
These extremely weak numerical constants still give a precise description-capacity restriction. They do not charge each new prime as physical descent.

That last leap is explicitly refuted: \(X=64t+7\mapsto X'=108t+13>X\) has a fixed shallow/shallow/depth-two renewal, with cores \(K=8t+1,K'=54t+7\) and \(4K'=27K+1\). CRT can put arbitrarily many new prescribed primes into \(K'\), absent from \(K\), without increasing the exit depth. A descending counterpart also exists. Prime novelty alone is not a division-surplus budget. [CC12, §6D]

A complementary CC13 theorem says only finitely many one-renewal transitions have both cores of binary Hamming weight at most two, \(\{1\}\cup\{1+2^t:t\ge1\}\). Its proof expands into at most six terms and verifies nondegeneracy before invoking ESS. The corresponding three-digit claim is false: homogeneous transported pieces can produce infinite descending families. This is another reason to classify degenerate cancellations dynamically rather than discard them by assumption.


### 3.1 Unrestricted depth labels at a fixed switch count: connected cancellation

CC14 concerns a different clock from the shallow/deep renewals above. Fix odd \(c\ge3\), positive odd \(d\), and a number \(q\ge1\) of **genuine changes of exact odd-step depth** in \(S_{c,d}(x)=\operatorname{oddpart}(cx+d)\). There are \(q\) completed maximal constant-depth runs, with active labels \(a_0,\ldots,a_q\), adjacent labels unequal, and completed-run lengths \(r_i\ge1\). Neither depth labels nor run lengths are bounded. At each run entry set
\[
D_a=2^a-c,\quad \alpha_a=d/D_a,\quad Z_a(x)=D_ax-d,\quad
\sigma_a(x)=Z_a(x)/2^{v_2(Z_a(x))}.
\]
Exclude the zero centered deviation. If the two endpoint signed odd parts \(\sigma_{a_0}(x_0),\sigma_{a_q}(x_q)\) are supported on one fixed finite prime set, then **only finitely many such positive blocks exist**. This removes a bounded-depth-menu assumption, but not the fixed-switch-count or endpoint-prime hypotheses. [CC14, main report §§2–6]

Here is the substantive mechanism. Write \(z_i=x_i-\alpha_{a_i}\), \(\Delta_i=\alpha_{a_{i+1}}-\alpha_{a_i}\), and
\[
t_j=2^{\sum_{i<j}a_i r_i}/c^{\sum_{i<j}r_i}.
\]
The centered run equations telescope to
\[
z_0-\sum_{i=0}^{q-1}t_{i+1}\Delta_i-t_qz_q=0.
\]
Maximality gives the exact valuation \(v_2 Z_{a_i}(x_i)=a_i r_i+\min(a_i,a_{i+1})\). The jump terms have strictly ordered binary valuations after an initial equal pair. Any zero subsum must include that first pair, then each successive jump, and finally the endpoint: the **grouped equation** has no proper vanishing subsum.

Clearing the center denominators and expanding their factors creates \((q+2)2^q\) labelled raw terms. Their coefficients are fixed for fixed \(c,d,q\), and their multiplicative variables belong to one fixed finite-rank rational group. Unlike the grouped terms, these raw terms can cancel properly. This is real, not a hypothetical loophole: the growing family \(32t+27\to48t+41\to36t+31\), with depths \(1,2,1\), produces a raw \(24-24\) cancellation.

The portable lemma in CC14 resolves precisely this issue. Suppose
\[
B_i=\sum_{\ell=1}^{m_i}\gamma_{i\ell}U_i2^{n_{i\ell}},\qquad \sum_i B_i=0,
\]
with fixed finitely generated rational group, fixed nonzero coefficients, fixed term counts, no proper grouped zero sum, and one anchor \(U_a=1\). Then the tuple of signed odd rational parts \(O(U_i)=U_i/2^{v_2(U_i)}\) ranges over a finite set.

**Proof.** Partition the labelled raw terms into minimal zero sums. The Evertse–Schlickewei–Schmidt theorem gives finitely many projective ratio vectors in each part. Connect two original groups whenever a minimal zero sum meets both. If this graph were disconnected, summing all minimal parts inside one component would give a forbidden proper grouped zero sum. It is therefore connected. Along any edge,
\[
\frac{O(U_j)}{O(U_i)}=
 O\!\left(\frac{T_{j h}}{T_{i\ell}}\frac{\gamma_{i\ell}}{\gamma_{jh}}\right).
\]
The right side belongs to a finite set; powers of two have disappeared. A spanning tree propagates these finite choices from the anchor. There are finitely many partitions of the bounded label set, proving the result.

In the dynamical application the finite anchored odd part is \(W=c^{r_0}\sigma_{a_0}(x_0)\). The first successor \(y\) obeys
\[
(2^{a_0}-c)y-d=2^{\min(a_0,a_1)}W.
\]
Consequently \(y\le2c|W|+d\), with the sharper C3 bound \(4|W|+1\). There are finitely many \(y\); each determines \(a_1=v_2(cy+d)\), finitely many \(a_0\), and \(r_0\le\log_c|W|\). Reconstruct \(x_0\); its later actual runs are deterministic. This completes the finiteness proof. On a nonperiodic orbit, finite-prime-supported active centered shapes therefore have zero upper Banach density in **depth-change time**, not automatically in ordinary time.

The controls are essential. Without the anchor, \(U,U,-2U\) permits \(U=3^n\). Without grouped nondegeneracy, \(3^n,-3^n,1,-1\) has a disconnected free scale. With unbounded raw count, \(3^n-\sum_{\epsilon\in\{0,1\}^n}2^{\sum\epsilon}=0\) defeats uniform finiteness. A bounded-witness variant permits an unbounded total graph only if an anchor-to-target chain has bounded relation size, bounded length, and finitely many accumulated odd coefficient corrections. The reports do not prove that all Collatz histories supply such a chain.

**Significance and credit.** The connectivity argument is elementary; S-unit finiteness is external. The interesting application is the combination of exact maximal-run valuations, grouped nondegeneracy, and quotient propagation that allows unbounded depth labels. This is a more specific candidate than a claim to have invented graph connectivity or S-unit methods.

### 3.2 Source carries identify the integer but do not trap its endpoint

For a finite exact depth prefix in \(S_{c,d}\), let \(\rho_m\) be its least positive source modulo \(2^{H_m+1}\) and \(z_m\) its actual endpoint. Appending depth \(a\) gives a unique \(t_m\in\{0,\ldots,2^a-1\}\) satisfying
\[
\rho_{m+1}=\rho_m+2^{H_m+1}t_m,\qquad
2^a z_{m+1}=cz_m+d+2c^{m+1}t_m.
\]
Divide the next exact-depth congruence by two and invert the odd coefficient \(c^{m+1}\) to prove uniqueness. Also \(t_m=0\) exactly when \(a=v_2(cz_m+d)\). The nondecreasing positive \(\rho_m\) stabilize if and only if a **single ordinary positive integer** realizes the infinite word. For an actual source \(X\), once the modulus exceeds \(X\), its canonical representative equals \(X\). This inherited source-lift identity does not prove eventual carries must persist on a bad word. [CC15, §2; explicitly credits Shortcut Research 05]

The comparator \(c=1\), odd positive \(d\), has an additional property absent from the argument for C3. Put \(L_m=2^{H_m}-\sum_{j<m}2^{H_j}\) and \(q_m=\lfloor dL_m/2^{H_m+1}\rfloor\). Direct substitution yields
\[
\rho_m=dL_m-2^{H_m+1}q_m,\qquad z_m=d-2q_m\in\{1,3,\ldots,d\}.
\]
Thus source identification gives finite trapping after a bit-length-controlled number of rounds. C3 only has an exponentially growing endpoint envelope. **Reading enough bits to identify the source is not the same as trapping the endpoint.** Even a finite trap need not select the cycle of one: the \(c=1\) control's cycles are inverse-doubling orbits modulo \(d\).

CC15 also isolates legality from formal simplification. A Farkas comparator may erase a factor of three via \((n-1)/3\) at odd \(n\equiv1\pmod6\); an actual reverse Collatz edge cannot. The paper's legal \(G/M\) reduction is attributed to Yolcu–Aaronson–Heule, not inferred from that comparator.

A matched-center calculation explains a genuine C3 repair. Let \(E(y)=2y+t\) with \(d=(c-2)t\), and \(\ell=1+v_2(c-1)\). The residual addend after the next shallow lift is \(d^*=t\operatorname{oddpart}(c-1)\). It equals the original \(d\) precisely when \(c=3\). This gives \(S_{3,d}^2(2y+d)=S_{3,d}^2(y)\) when \(v_2(3y+d)=2\). Transporting that identity yields the familiar smaller-half-source merger after a suitable shallow run. CC15 explicitly recognizes it as the already catalogued Hercher primitive, not new global coverage; the matched C5 control \(c=5,d=3,t=1\) has \(1\) fixed while \(3\leftrightarrow9\) persists.

## 4. Exact signed-word elimination is an integral Collatz presentation

This is one of the most coherent prospective paper sections. [SW1, §§1–9; independently reconstructed in CF]

Let \(F_{\mathbb Z}=\bigoplus_{r\ge0}\mathbb Ze_r\). Define \(Q(t)=e_{(t-3)/4}\) for positive odd \(t\equiv3\pmod4\), and \(Q(t)=0\) otherwise. The supplied word transducer is precisely binary multiplication by three: each transition satisfies \(3d+c=d'+2c'\). Its compiler becomes
\[
H(1)=0,\quad H(2n)=H(n),
\]
\[
H(2^hv-1)=H((3v-1)/2)+\sum_{j=0}^{h-2}Q(3^jv),
\]
for odd input \(>1\), \(v\) positive odd. The recursive argument strictly decreases, so every \(H(n)\) is a finite nonnegative integer vector. Put
\[
U_r=6r+4,\quad V_r=18r+13,\quad L_r=e_r-H(V_r)+H(U_r).
\]

**Theorem 4.1 (integral structure).**
\[
F_{\mathbb Z}/\langle L_r\rangle_{\mathbb Z}
\cong\bigoplus_{C\ne C(1)}\mathbb Zb_C,
\]
where \(C\) runs over the undirected components of the actual shortcut graph, and \(e_r\) maps to \(b_{C(V_r)}-b_{C(U_r)}\), with the base-component symbol zero.

**Substantial proof.** Let \(\mathcal B=\langle x_n:n\ge1\mid x_1=0,x_n=x_{T(n)}\rangle_{\mathbb Z}\). The map \(e_r\mapsto x_{V_r}-x_{U_r}\) sends \(H(n)\) to \(x_n\), by induction on the decreasing compiler argument. In an odd block, telescope the intermediate labels \((3^{j+1}v-1)/2\); successive differences are either zero by actual graph edges or exactly the emitted \(e_r\)-image.

Conversely, put \(D(m)=H(2m+1)-H(3m+2)\). Direct compiler subtraction gives \(D(m)=0\) for even \(m\); if \(m+1=2^h(4r+3)\), it gives \(D(m)=L_r\); if \(m+1=2^h(4r+1)\), it gives \(D(m)=D(3r)\), with \(3r<m\). Thus every actual edge difference \(H(n)-H(T(n))\) is zero or one supplied row, and \(x_n\mapsto[H(n)]\) is well-defined. The two maps are inverse on generators.

Finally, quotienting a graph’s free vertex group by edge differences leaves the free group on its connected components: collect the finitely many coefficients in each component, and use finite paths to transport them to one representative. Killing \(x_1\) removes precisely its component. This also proves there is no torsion; rational coefficients do not hide an integral obstruction. The graph-component abelianization, component-indicator separation, and incidence-flow path argument are standard graph algebra. The project-specific work is the finite decreasing compiler H, its actual-edge identities, and the explicit integral equivalence between that constrained signed-word presentation and the graph presentation. Those ingredients, rather than the generic quotient fact, carry the candidate contribution.

In a functional graph, undirected connectedness equals finite forward-orbit merger. The merger relation is transitive by advancing two meeting times to a common later time, and every edge lies in it. Hence
\[
e_r\in\operatorname{span}_{\mathbb Q}^{\rm finite}\{L_s\}
\iff T^a(V_r)=T^b(U_r)\text{ for some finite }a,b.
\]
When a merger is supplied, an integer certificate is explicitly
\[
e_r=L_r+\sum_{i<a}E(T^iV_r)-\sum_{j<b}E(T^jU_r),\quad E(n)=H(n)-H(T(n)),
\]
and each \(E(n)\) reduces by the decreasing recursion to zero or one row.

### 4.2 Exact norm gap and the dual obstruction

For a component indicator \(f\), anchored by \(f(1)=0\), define \(z_r=f(V_r)-f(U_r)\in\{-1,0,1\}\). Conversely \(f(n)=\langle H(n),z\rangle\). These are mutually inverse correspondences between constrained row-annihilating assignments and binary component labels.

For each \(r\),
\[
\inf_{\lambda\in\mathbb Q^{(\mathbb N)}}\left\|e_r-\sum_s\lambda_sL_s\right\|_1\in\{0,1\},
\]
with the minimum attained. It is zero when the endpoint orbits merge. If they do not, choose the indicator of one nonbase endpoint component. Then \(|z_s|\le1\), \(|z_r|=1\), and every row annihilates \(z\), so every finite residual has literal unweighted norm at least 1; the zero row combination attains 1.

Therefore “every target admits residual norm \(<1\)” is **equivalent to**, not weaker than, universal exact elimination, which is itself equivalent to Collatz. The exact finite normalizer is a useful theorem; existence of its required input at every target remains open. Retain every external column of a finite packet. Solving only an internal matrix block does not certify the full row identity.

## 5. The birth basis removes signed feedback but does not remove dynamics

Write \(4r+3=3^{d_r}v_r\), \(3\nmid v_r\), and set
\[
a(r)=2^{d_r+2}v_r-1,\qquad b_r=H(a(r)).
\]
SW2 proves \(a(r)\) is the first input at which coordinate \(e_r\) occurs, and
\[
b_r=e_r+\sum_{a(s)<a(r)}m_{rs}e_s,\quad m_{rs}\ge0.
\]
Indeed an emission at level \(j\le d_r\) needs source at least \(2^{j+2}(4r+3)/3^j-1\), minimized at \(j=d_r\). Every earlier emission and the recursive continuation has smaller birth. Thus this is an integral unitriangular basis with a finite inverse at each coordinate.

A component-preserving, terminating normalization \(R(n)\le n\) reduces an input to 1 or a birth integer: strip even factors; at an odd block with emissions choose the last emission’s birth; otherwise recurse on \((3v-1)/2\). Define
\[
F(r)=a^{-1}(R(V_r)),
\]
with a base symbol \(*\) when \(R(V_r)=1\). The full relation module becomes
\[
\langle L_r\rangle_{\mathbb Z}=\langle b_r-b_{F(r)}\rangle_{\mathbb Z},\quad b_*=0.
\]
This is equality of full finite-support submodules, not a statement that each old row individually is one incidence edge. \(R\) induces a bijection of actual Collatz components with the weak components of \(F\).

The simplification is exact but its limitation is sharp. A finite incidence expression for \(b_r\) must contain the full forward \(F\)-path to \(*\). Sum coefficients over the finite support graph component of \(r\); it must contain \(*\). A finite functional component containing a sink is a tree oriented toward it, so leaf elimination forces unit coefficient on that unique path. Other components contribute only cycle circulations. Signed cancellation cannot bypass the missing forward path in this basis.

There are arbitrarily long increasing direct runs:
\[
r_0=6\cdot8^k-1,\qquad r_j=6\cdot9^j8^{k-j}-1,\quad 0\le j\le k,
\]
with \(d_{r_j}=0\) and \(F(r_j)=(9r_j+1)/8\). Even the first subsequent change of \(d\) leaves a net-expanded birth. More generally every prescribed finite \(d\)-word occurs along direct growing edges, via one compatible dyadic cylinder and a sufficiently large source. Yet an infinite eventually periodic direct-growth word is impossible: one period acts as \((Av+B)/2^M\), \(A>2^M\), \(B>0\), and the positive integer \(W=(A-2^M)v+B\) loses exactly \(M\) factors of two per period. The exit bound is \(\lfloor v_2(W)/M\rfloor\). This is another exact fixed-source/varying-source separation, not all-aperiodic termination.

## 6. What compactness and abstract closure do, and do not, prove

### 6.1 Pinned compactness

Fix one target \(t\). In the compact product \(\{-1,0,1\}^{\mathbb N}\), impose all row equations, all binary reconstruction constraints, and the pin \(z_t\ne0\). Each condition involves finitely many coordinates and is closed. If no global witness exists, a finite collection is inconsistent. Moreover CA constructs a finite genuine graph from the compiler chains used in that collection. If its critical endpoints were disconnected, a finite component indicator would satisfy all those constraints, contradiction. A finite connecting path therefore yields an integer row certificate.

This is a correct conversion from a **proved nonexistence theorem** to a finite certificate. It is not a proof that nonzero witnesses do not exist. The condition “nonzero somewhere” is not closed: unit vectors can converge coordinatewise to zero. No uniform finite certificate for all targets follows merely by dropping the pin. The increasing finite-constraint search remains a semidecision procedure until witness exclusion is established. [CA, compactness section]

### 6.2 Hereditary frontier closure

LG states a general graph theorem. Maintain
\[
e_x-e_o-\partial J=\sum_{(a,q)\in\mathcal F}a(e_{u(q)}-e_{v(q)}),
\]
where \(J\) is a finite genuine-edge chain and the full frontier contains every obligation. Every applicable, finitely executing rule must provide a genuine finite chain \(P\), finitely many children, and the exact identity
\[
B(q)=\partial P+\sum_i c_iB(q_i),
\]
with a supplied well-founded rank satisfying \(\rho(q_i)<\rho(q)\) for every nonzero child. Guards must cover all admitted obligations; rank-zero obligations need actual base certificates.

**Proof of closure.** For natural ranks bounded by the finite initial maximum \(N\), count obligations at ranks \(N,N-1,\ldots,0\). Each expansion decreases that finite tuple lexicographically, regardless of how many lower-rank children it creates. Hence every continuing execution empties the frontier, and the invariant gives \(\partial J=e_x-e_o\). This is an application of the established Dershowitz–Manna finite-multiset termination principle, not a new general well-foundedness theorem. The application problem is to supply those ranks and complete guarded identities for the actual Collatz obligation system.

A local compiler that finishes and then emits a fresh obligation of equal or larger rank does not meet this hypothesis. Nor does a rank derived from unknown eventual stopping time count as an independently supplied construction.

### 6.3 Genuine tightness versus loss of mass at infinity

LG also proves a separate transport criterion. Given finite nonnegative stochastic splitting on genuine edges, an absorbing target, a proper nonnegative potential \(V\), and explicit positive defects \(d(u)\) off target satisfying
\[
\sum_vP(u,v)V(v)\le V(u)-d(u),
\]
finite exact propagation gives \(M_k\le V(x)\), \(\sum_k\sum_u\mu_k(u)d(u)\le V(x)\), hence coordinate decay off target. Properness supplies the uniform tail bound \(\sum_{V(u)>B}\mu_k(u)\le V(x)/B\). Finite sublevels plus coordinate decay imply all mass reaches the target in the limit; the unweighted edge residual eventually falls below the discrete threshold 2, and a finite path is extractable.

Neither the required proper potential nor the drift inequality is supplied universally for Collatz. The isolated outward chain rejects any generic “coordinate decay suffices” claim. Similarly, for signed residuals supported below \(H_j\), Creative Closure 08 proves
\[
\|r_j\|_1\le(1+H_j)^s\sum_i|r_j(i)|(1+i)^{-s}.
\]
Exponential weighted decay \(e^{-\lambda j}\) gives exact finite success only with support growth \(H_j=O(e^{\kappa j})\) and \(\lambda>s\kappa\). The countercontrol \(r_j=e_{2^j}\) has weighted norm tending to zero and unweighted norm exactly 1. No actual Collatz residual estimate meeting this rate comparison is established. [CR08, §9]

## 7. Golden height: useful exact identities, a false quotient cycle, and a faithful repair

Let \(P_n(q)\) be the finite binary polynomial and \(\phi=(1+\sqrt5)/2\). Define \(V(n)=P_n(\phi)-1\). The inherited carry law is
\[
\phi^{a(n)}V(S(n))=\phi^2V(n)-L(n),\quad L(n)\ge0.
\]
CC proves zero loss is isolated away from termination: a zero-loss \(n>1\) has positive loss at its next nonterminal successor. Consequently positive losses have lower frequency at least one half on any hypothetical nonterminal orbit.

That frequency is not an independent contraction theorem. With \(\alpha=\log_2\phi\), \(V(n)\asymp n^\alpha\), so \(h(n)=\log_\phi V(n)-\log_2n\) is bounded for odd \(n\ge3\). Define
\[
\ell(n)=-\log_\phi\left(1-\frac{L(n)}{\phi^2V(n)}\right),\quad
\epsilon(n)=\log_2(1+1/(3n)).
\]
For a nonterminal step,
\[
\ell(n)=2-\log_2 3-\epsilon(n)+h(n)-h(S(n)).
\]
Thus the average normalized loss on a hypothetical escape tends to \(2-\log_2 3\), a bounded-change-of-coordinate identity compatible with escape. Calling that average an additional independent “tax” would count the same arithmetic twice. [CC, §§2–3]

There is a more refined exact polynomial factorization. For \(F\in\mathbb N[q]\), binary carrying gives \(F-P_{F(2)}=(2-q)N_F\), \(N_F\in\mathbb N[q]\). For an actual word, its accumulated carry \(K_m\) splits as
\[
K_m=J_mP_{n_0}+J_B+M_{3^m,n_0}+A_{3^mn_0,B},
\]
where \(J_m=((q+1)^m-P_{3^m})/(2-q)\), \(J_B=(B_m(q)-P_B)/(2-q)\), \(M_{a,b}=(P_aP_b-P_{ab})/(2-q)\), and \(A_{a,b}=(P_a+P_b-P_{a+b})/(2-q)\). The first two terms normalize the coefficient and ordered offset; the latter two retain interaction with the marked source. They are four parts of one exact defect, not four independent charges. [CC, §4]

### 7.1 A decisive counterexample to an autonomous height quotient

Actual arrows \(15\to23\) and \(25\to19\) satisfy
\[
V(15)=V(19)=2+4\phi,\quad V(23)=V(25)=3+5\phi.
\]
The quotient therefore admits a false 2-cycle by switching representative 23 to 25. This is not a Collatz cycle. Even adding any fixed suffix precision fails to determine future height: for \(k\ge3\), \(x=4\cdot2^k+1\) and \(y=3\cdot2^k+1\) have equal revaluation and equal residue modulo \(2^k\), but \(V(Sx)-V(Sy)=\phi^{k-1}>0\). A proposed Goodstein-like master must preserve sources or prove that representative changes are lawful. [CC, §5]

### 7.2 Faithful first jets

**Theorem 7.1.** The map
\[
J(n)=(P_n(\phi),P_n'(\phi)),\qquad n\ge0,
\]
is injective. [FJ, Theorem 2.1]

**Proof.** Put \(r=1/\phi\). For \(f(x)=1+\sum_{i\ge1}c_ix^i\), \(|c_i|\le1\),
\[
rf'(r)-3f(r)\le-3+2r+r^2+\frac{r^4}{(1-r)^2}=-r^2<0.
\]
So \(r\) cannot be a double zero. If two binary polynomials had the same jet at \(\phi\), their difference \(F\in\{-1,0,1\}[q]\) would be divisible by \((q^2-q-1)^2\), hence have a double zero at \(\psi=-r\). Remove its lowest nonzero monomial, normalize its sign, and substitute \(q=-x\) to contradict the inequality.

The four-coordinate representation
\[
P_n(q)=A+Bq+(q^2-q-1)(C+Dq)\pmod{(q^2-q-1)^2}
\]
has nonnegative integer counters and digit-append update
\[
(A,B,C,D)\mapsto(B+\varepsilon,A+B,B+D,C+D).
\]
At the conjugate embedding let \(u=P_n(\psi),v=P_n'(\psi)\). The lowest bit is exactly
\[
\varepsilon_0=1\iff3u-\psi v>1,
\]
because the bit-zero interval is \([2\phi-5,3\phi-4]\), the bit-one interval \([2\phi-2,3\phi-1]\), with positive gap \(2-\phi\). Strip the bit by
\[
u'=(u-\varepsilon_0)/\psi,\quad v'=(v-u')/\psi.
\]
This gives exact finite-source decoding, not a fixed-precision numerical representation.

**What is encoded, and why the result is not tautological.** The input is the finite binary digit polynomial \(P_n(q)=\sum_i\epsilon_iq^i\), with \(\epsilon_i\in\{0,1\}\), ignoring irrelevant leading zeros. Neither the numeral \(n\), its word, nor an external source label is appended to the output. The four displayed integers are the coefficients of the remainder in the fixed quotient ring \(\mathbb Z[q]/(q^2-q-1)^2\); equivalently,
\[
P_n(\phi)=A+B\phi,\qquad
P_n'(\phi)=B+(2\phi-1)(C+D\phi).
\]
The scalar quotient by \(q^2-q-1\) genuinely loses information: the distinct binary polynomials \(q^2\) and \(q+1\), encoding 4 and 3, already agree there. Squaring the modulus does **not** make the quotient faithful on arbitrary integer polynomials, since every multiple of the squared modulus is invisible. The theorem is the special fact that this kernel contains no nonzero difference of two binary digit polynomials. The bounded alphabet and no-double-zero estimate do the work.

There is no information-theoretic compression or universal finite-state model: these four exact integers are unbounded and together determine the entire original input. Its possible utility is a fixed-dimensional algebraic representation with affine digit updates and an exact bit separator, repairing an invalid scalar state quotient. As a bare injective code it has no logical force beyond retaining the source itself; it supplies neither a well-founded height nor finite orbit/predicate complexity. A publication should emphasize the restricted representation theorem and exact calculus, not the impressive-sounding coordinate count.

FJ additionally classifies lattice points of the compact infinite-word jet set: their eventual decoder tails are 0, 1, or 01, corresponding to 2-adic sources in \((1/3)\mathbb Z\). Bounded conjugate coordinates and contracting original-embedding updates force a finite lattice orbit; the source supplies a forty-candidate exact cycle enumeration. This audit independently reproduced every transition and all three cycles using exact quadratic-ring arithmetic; the check is retained in `closure_focused_checks.py`. Nonnegative counters alone are not finite-source authentication: the eventually alternating expansion of \(5/3\in\mathbb Z_2\) has counters \((1,0,1,0)\). An injective four-integer code is not four states, and its decoder’s termination on finite inputs is not outer Collatz termination.

**Credit.** The report explicitly cites Shmerkin–Solomyak’s work on double zeros of \(\{-1,0,1\}\)-series as mathematical context/inspiration; the displayed golden-ratio inequality is supplied directly. Goodstein base-change maximality is a comparison methodology, not an imported Collatz theorem.

## 8. Primitive sections, one-progression rigidity, and a bounded-proof obstruction

Let \(b:\mathbb N\to\{0,1\}\) satisfy \(b(0)=b(1)=0\), \(b(2n)=b(n)\), \(b(2n+1)=b(3n+2)\). Let \(g(n)=b(3n+1)\) and
\[
\mathcal U_3(b)=\{n\mapsto b(3^kn+r):k\ge1,0<r<3^k,3\nmid r\}.
\]
For \(E_if(n)=f(2n+i)\), an exact descriptor update is
\[
E_if_{k,r}=f_{k,s/2}\ (s\text{ even}),\quad
E_if_{k,r}=f_{k+1,3(s-1)/2+2}\ (s\text{ odd}),\quad s=3^ki+r.
\]
**Theorem 8.1.**
\[
\mathcal K_2(g)=\mathcal U_3(b),\qquad
\mathcal K_2(b)=\{b\}\cup\mathcal U_3(b).
\]
Same-level updates multiply the primitive residue by \(2^{-1}\bmod3^k\); since 2 generates every unit group modulo \(3^k\), they reach all primitive descriptors at that level. The other bit reaches the next level. Closure gives the reverse inclusion. This is equality of actual sequences, not a claim that different descriptors are linearly independent. [CC, §6]

If \(g\) has finite kernel in **either** base 2 or base 3, it has finite kernels in both: the primitive family is closed in both bases, and \(b(3n+2)=g(2n+1)\). Cobham’s theorem gives eventual periodicity. An elementary affine-residue argument, or the published arithmetic-progression component-sufficiency theorem, then forces \(b\equiv0\). Christol’s theorem consequently makes a nontrivial algebraic equation for \(\sum g(n)z^n\) over \(\mathbb F_2(z)\) or \(\mathbb F_3(z)\) another sufficient endgame. Neither automaticity nor algebraicity is proved here.

Let \(W_N=\operatorname{span}_{\mathbb Q}\{E_wg:|w|\le N\}\). Any nonzero invariant must have
\[
\dim W_N\ge N+1.
\]
If the dimension ever failed to increase, that finite-dimensional space would be stable under both sections. Finite-valued sequences in a finite-dimensional space form a finite set: finitely many evaluation coordinates separate the space, so their 0/1 vectors have finitely many possibilities. Kernel finiteness would contradict nonzero \(b\). Hence an actual whole-sequence certificate \(\dim W_N\le N\) at one depth would suffice. A finite matrix evaluated only on already terminating inputs proves no such bound. [CC, §§7–8]

FJ proves a focused obstruction to one proposed compiler for these relations. For distinct sections \(x_i(n)=3^{k_i}n+r_i\), choose a nonzero term of maximal \(k_i=K\), and fix an odd-operation budget \(M\). On the infinite progression
\[
3^Kn+r_*\equiv-1\pmod{2^{M+1}},\quad n>2\cdot6^M(1+\max r_i),
\]
its first \(M\) odd rounds are shallow and cannot meet any other section’s trajectory within \(M\) odd shortcut operations, even with arbitrarily many even divisions. A meeting height bounds total companion length by \(2M+1\). Equal affine slopes would force equal powers of 2 and 3, hence the same maximal exponent and all-odd path, but distinct offsets prevent equality. Unequal slopes have a nonzero integer numerator after a common denominator is cleared, and the displayed source bound exceeds all possible intercept coincidences.

Thus bounded replay plus endpoint cancellation cannot produce a universal nontrivial section relation. This does **not** show actual infinite rank: if Collatz holds, all bad-component functions vanish. It rules out this proof compiler, not unbounded recursive proofs, other identities, or the conditional finite-rank criterion. [FJ, §7]

## 9. Collision-aware transport and representation-dependent certificate difficulty

CC16 gives a complete column-bound calculation for four specified smaller-source rule families. The naïve weight \(x^{-2}\) fails: demands from 9 and 11 overload receiver 7, since
\[
1/9^2+1/11^2-1/7^2=97/480249>0.
\]
With \(w(x)=x^{-3}\), the full incoming fibers instead satisfy
\[
\sum_{x\to y}w(x)\le\lambda w(y),\quad
\lambda=\frac{3136}{6561}+\frac8{27}+\frac18+\frac1{64}=\frac{384169}{419904}<\frac{11}{12}.
\]
For example the deep-descent predecessor fiber is geometric in \(4^j\), and the other three fibers are injective with ratios exceeding \(3/2,2,4\), respectively. This gives all-path receiving bounds \(\sum_{\text{length }k\text{ paths}\to y}w(\text{start})\le\lambda^kw(y)\), and total ancestry weight \(<12w(y)\). A deterministic decreasing normalizer has disjoint fibers whose induced weight remains comparable to \(r^{-3}\). No source atoms are dropped.

This proves collision control **on the enabled-rule domain**. It does not prove that every nonterminal source enables a rule. The all-finite-cut Hall condition on the remaining actual graph is still missing. Counting different proofs of the same integer target as separate target capacity would be double spending. The Atlas Crosscheck’s H1 route must retain literal recipients, normalized sufficient gates, and all collisions. [CC16; AX]

CC18 supplies a sharp and constructive comparison. Define the lawful sibling \(E_k(X)=4^kX+(4^k-1)/3\) for \(k\ge1\), with \(S(E_kX)=S(X)\). If \(3^L\mid X\) and a positive odd \(Y\) reaches **any** \(E_k(X)\) in \(1\le m\le L\) odd rounds, then \(Y>3X\). The separate length-zero case is also larger, since \(Y=E_k(X)>3X\) for \(k\ge1\). To prove this, write \(3^mY=2^H(AX+\beta)-B\), \(A=4^k,\beta=(A-1)/3\). Because \(3^m\mid X\), the intercept \(Y_0=(2^H\beta-B)/3^m\) is an integer inverse source of the positive odd \(\beta\), so \(Y_0\ge1\). Its positivity and \(B>0\) imply \(2^H/3^m>Y_0/\beta\), hence \(Y>(A/\beta)X+1>3X\).

Yet the progression
\[
X=296959+1048576t,\quad Y=(X-1)/2
\]
has a synchronous thirteen-odd-round merger at \(903035+3188646t\), with every displayed positive-time target state above \(X\). CRT intersects this progression with \(3^L\mid X\) for every \(L\). Thus one restricted root-sibling inverse representation needs arbitrarily many rounds while another representation supplies a fixed thirteen-round certificate. This is a method-specific lower bound, not a Collatz stopping-time lower bound. Enlarging the half-companion rule’s guard adds no receiving multiplicity: the literal incoming source remains uniquely \(X=2Y+1\). [CC18, Theorems 2.1 and 5.1]

## 10. Creative closure: source transport, receiver calculus, and the limits of proof grammars

### 10.1 Conditional architectures and a sharp language distinction

Creative04's title “full-proof architectures” means **sufficient proof architectures**, not a completed proof. One version retains a fixed finite set of external ports and all Boolean target-separating masks. An authenticated boundary relation can remove masks, but never revive them. A lexicographic rank consisting of the number of surviving masks followed by the multiset of unresolved source-record ranks would terminate an assembler, provided every nonterminal macro either removes a mask or strictly lowers source ancestry, its guards cover every reachable state, and every terminal carrier is actually received. New internal vertices are harmless; a new unreceived **external** port invalidates the old fixed-mask count. No universal Collatz progress table meeting these conditions is supplied. [CR04, Part IV §§4–6]

A concrete warning is \(L(4^k)=3\cdot4^k+2\xrightarrow{(HO)^k}3^{k+1}+2\): every bit of the supplied all-halving source record can be consumed while an unbounded carrier remains at source 1. This is not a terminal base theorem.

Another architecture seeks an infinite **completely certified set of integers** recognizable in both bases two and three. Cobham forces ultimate periodicity, hence a complete infinite arithmetic progression; Monks' progression-sufficiency theorem then gives universal convergence. This is a valid conditional synthesis of known external theorems. No such doubly recognizable certified set is constructed here. [CR04, Part III §6]

The report proves a useful obstruction to replacing this with a much weaker finite-state certificate engine. Suppose a finite automaton with \(J\) states accepts only legal inverse shortcut itineraries from absorbing 1. Then every accepted word contains fewer than \(J\) inverse odd steps. Indeed, a repeated automaton state between odd-step positions supplies a pumpable inverse word
\[
W(x)=(2^A x-B)/3^d,\qquad d>0.
\]
Soundness of every pumped word makes \(W^j(x)\) integral for all \(j\). Since \(2^A-3^d\) is coprime to three,
\[
3^{dj}\mid(2^A-3^d)x-B\quad\hbox{for all }j,
\]
so \(W(x)=x\). Reversing the word gives a genuine directed cycle at a state already having a forward path to 1, impossible in a deterministic graph with the absorbing odd step excluded. This is a complete pumping argument, not a claim about the regularity of all convergent **numerals**. With at most \(d\) odd steps, counting path words gives only \(O_d((\log X)^{d+1})\) certified inputs up to \(X\), too sparse for a progression. The numeral, itinerary, and constructor-instruction languages are three different objects.

### 10.2 Original smaller sources survive arbitrarily long expanding prefixes

Use \(O(n)=(3n+1)/2\) at odd \(n>1\), \(H(n)=n/2\) at even \(n\), and absorb at 1. For positive odd \(q\), \(\ell\ge1\), set
\[
N=4q8^\ell-5,\quad a=3q8^\ell-5<N,\quad Y=q9^\ell.
\]
Both sources execute \((OOH)^\ell\), ending at \(T=4Y-5\) and \(3Y-5\). For \(u=Y-2\), the source endpoint halves to \((3u+1)/2=O(u)\). Thus the high quarter-source \(u\) at \(T=4u+3\) is owned by the **original** \(a<N\). Any completed receiver connecting \(T\) and \(u\) proves \(N\) from that original source. The elementary guarded block \(8d-5\to12d-7\to18d-10\to9d-5\) proves all prefix guards. [CR07, Parts IV–V]

This is not limited to the center \(-5\). Let a fixed expanding shortcut word have \(W(x)=(Ax+B)/2^L\), \(A=3^o\), \(D=A-2^L>0\). Choose \(2^k>D\) and positive \(q\) with \(2^{L\ell+k}q\equiv B\pmod D\), and put
\[
N=(2^{L\ell+k}q-B)/D,\qquad
 a=((2^k-D)2^{L\ell}q-B)/D.
\]
If \(a\ge2^{L+1}\), both execute \(W^\ell\), and \(a<N\). At the target endpoint \(T\), the original source owns \(F(T)\), where \(F(x)=((2^k-D)x-B)/2^k\). Both initial values lie in the unique integrality/parity cylinder of the repeated word, because \(Dn+B\) is divisible by \(2^{L\ell}\); the size guard keeps all prefix states at least two. Iteration about the rational fixed point \(-B/D\) proves the endpoint identity. The cylinder and positivity requirements are essential, and the receiver at \((T,F(T))\) is not automatically complete.

For the benchmark \(N=4\cdot8^\ell-5\), three disjoint exponent classes have complete receivers from \(a=3\cdot8^\ell-5\): \(\ell\equiv109\pmod{512}\), \(201\pmod{256}\), and \(157\pmod{2048}\). Common futures are respectively
\[
(6561\cdot9^\ell-4489)/4096,\quad
(2187\cdot9^\ell-1187)/2048,\quad
(19683\cdot9^\ell-11035)/16384.
\]
The reports provide the literal guarded words. These are genuine infinite smaller-source certificate families, not proofs that every benchmark exponent is covered or that the full older residual is empty. Their source is below the frozen \(N\), even though the merger can occur before the target ever descends below \(N\).

### 10.3 A long receiver burst has a decreasing local rank and only two boundary caps

Let \(J(x)=9x+1\), \(K(x)=9x-1\), \(B(x)=9x+2\), \(D(x)=3x-1\), \(L(x)=3x+2\), and \(g_F(x)=E_{F(x)}-E_x\). These are **two-ended receiver obligations**, not convergence assertions about one endpoint. Creative07 gives complete smaller-index dispatch for odd \(J\), all \(D\), odd \(K\), and all \(L\), while retaining growing even \(K\) and \(B\) interfaces. In particular, for odd \(n>1\), \(a=(n+1)/2\), actual odd steps give
\[
g_L(n)\equiv g_K(a)-g_D(a)
\]
modulo actual finite path boundaries. Signs and both children matter. [CR07, Part III §§3–5]

For \(v\equiv7\pmod8\), put \(q=(v-1)/2\), \(t=(9v+1)/8\). The paths \(v\to L(q)\), \(q\xrightarrow{OO}t\), and \(B(v)\xrightarrow{OHO}B(t)\) prove
\[
g_B(v)\equiv g_B(t)-g_L(q).
\]
Although \(t>v\), the exact integer rank \(\mathcal P(n)=3^{v_2(n+1)}\operatorname{oddpart}(n+1)\) satisfies \(\mathcal P(t)=\mathcal P(q)=\mathcal P(v)/3\). This is a true local branching termination measure. It is not global: the legal cross-type return \(B(254)\to J(127)\to L(63)\) raises it from 255 to 729.

Write \(v_0+1=2^h3^sQ\), with \(h\ge3,s\ge1,\gcd(Q,6)=1\), and \(k=\lfloor h/3\rfloor\). Put \(v_i=2^{h-3i}3^{s+2i}Q-1\), \(A_i=2^{h+s-i-2}Q\). Iterating fusion, normalizing its \(L\) companions, and applying the odd-\(L\)/even-\(D\) identities telescopes to
\[
g_B(v_0)\equiv g_B(v_k)-g_K(A_0)+g_K(A_k).
\]
Both \(A_0,A_k<v_0\). Thus an arbitrarily long burst exposes only a terminal \(B\) receiver and two smaller \(K\) caps. The number of exposed boundaries is independent of burst length. But the source endpoints already connect by \(A_0\xrightarrow{H^k}A_k\); without an **independently received cap**, substituting the endpoint contacts simply recovers the known target path \(B(v_0)\to B(v_k)\). Compression does not close itself. This is an exact explanation of why a useful cancellation formula can still fail to provide new coverage.

### 10.4 A complete proof grammar is still sparse, and its instructions are not context-free

The proof constructors \(E(t)=4t+1\), \(R(t)=(16t-1)/9\) for \(t\equiv13\pmod{18}\), and the retained interior source \(S(t)=(8t+1)/3\), together with dyadic extension, generate actual complete proofs from a finite seed pool. Keeping \(S\) matters because the literal path from \(R(t)\) passes through it. Nevertheless the whole forward-closed constructed set \(\mathscr C\) has
\[
\#(\mathscr C\cap[1,X])=O(X^{19/20}).
\]
For the height \(H(n)=n-1/7\), a primitive parent's admissible padding exponents form one class modulo nine. The total child \(H^{-d}\)-mass is bounded by the parent's mass times
\[
\kappa(d)=\frac{(9/16)^d+(3/8)^d}{1-4^{-9d}}.
\]
At \(d=19/20\), exact power inequalities give \(\kappa<39/40\). Sum the geometric generation bound and the convergent padding/doubling tails to prove the count. Hence this particular grammar cannot contain a full arithmetic progression, however many complete proofs it generates. [CR07, Part VI §4]

There is a separate exact memory obstruction. The legal instruction language from seed one satisfies
\[
E^jR^k\text{ legal}\iff9^k\mid7E_j(1)-1
\iff j\equiv a_k\pmod{9^k}
\]
for a unique coherent residue \(a_k\). These exponent pairs are not semilinear: a fixed nonzero horizontal generator and a positive vertical generator in one linear component would force its fixed horizontal increment to be divisible by arbitrarily high \(9^k\); without such a horizontal generator a component has only finitely many points at each height. A finite union cannot supply every infinite horizontal fiber. Parikh's theorem therefore makes the legal \(E/R\) instruction language non-context-free. This is a constructor-language obstruction, **not** a claim that the numeral language of convergent integers is non-context-free. Credit Parikh for the external formal-language theorem; the exact growing-modulus guard is the project-specific input.

### 10.5 Creative Closure 08–09: clock grade, owned repunits, and fixed-preview failure


For an already convergent odd source define its completed grade \(\kappa=H-2M\). For arbitrary finite paths only the relative grade is defined. Equal-clock mergers preserve completed grade; the older constructors in CR08 preserve a lower grade floor of a supplied finite proof forest. Therefore that grammar cannot manufacture the proof of 27 from the one-proof alone, since its completed grade is \(-12\). This is a grammar obstruction, not an assumption that a hypothetical counterexample possesses a completed grade.

A smaller-source merger with excess target clocks \((\Delta M,\Delta H)\) both lowers grade and has leading source slope below one when
\[
\Delta M\log_2 3<\Delta H<2\Delta M.
\]
The first positive integer pair is \((3,5)\). There is no such interval for coefficient 5 with positive excess multiplications, a specific constructive distinction rather than a heuristic average-depth argument.

**Complete guarded family.** For \(k\ge1,d\ge3\), if \(N\) legally realizes target word \((1,1,2),1^{[k]},d\), then
\[
Y=(27N+3)/32<N
\]
is a positive odd source with word \(1^{[k-1]},2,d-2\) and the same endpoint. The first target bits force \(N\equiv39\pmod{64}\); affine offset identity \(B_a-32B_b=3^{k+2}\) establishes endpoint equality, and inverse integrality verifies the source guards. The relative grade difference is \(-1\). Example: \(2919\to14033\leftarrow2463\), with no displayed target descent. This repackages a retained half-source merger; credit Christian Hercher’s merger input where reused, rather than presenting the underlying primitive as newly discovered. [CR08, §§4–5]

The long-reset residual has \(R_r=(9^r-1)/8\) and \(N_r=(2^{3r+2}-11)/3\), odd \(r\ge3\), with target checkpoint \(9R_r-1=R_{r+1}-2\). CR09 enlarges the supplied reservoir: all \(R_j\) for \(1\le j\le(3r-1)/2\) have owners \(4^j-1<N_r\), via \(2j\) odd shortcut operations and three halvings. It supplies explicit guarded receiver modules, cofactor families, and variable-length adjacent receivers. The universal repunit-minus-two receiver remains open.

A particularly clean limitation is all-parameter, not experimental. For every fixed shortcut preview \(D\), choose arbitrarily large odd \(r\) with \(R_r\equiv-1\pmod{2^{D+8}}\). The target shadow \(9(-1)-1=-10\) lies in the negative cycle \(-10,-5,-7\). Shadows of \(R_r,R_{r+1},R_{r+2}\), namely \(-1,-8,-71\), reach \(-1\) through disjoint values of magnitude at most 118. At most one bit of congruence is lost per shortcut step, so all actual prefixes remain separated modulo 256 through the preview. No fixed forward-preview table using only those three records is exhaustive. Complete source histories, the larger reservoir, inverse paths, or recursive receivers remain possible. [CR09, §6]

## 11. Uniform repeated-word cost and individual escape constraints

### 11.1 A word-independent repetition budget

For any positive depth word of \(m\) odd rounds and total depth \(H\), put \(A=3^m,Q=2^H\), and assume \(A>Q\). Its offset obeys
\[
B\le2^{H-m}(3^m-2^m)<Q^{\alpha},\quad\alpha=\log_2 3.
\]
If \(k\) copies are legal from \(X>0\), the positive integer
\[
V(X)=(A-Q)X+B
\]
is divisible by \(Q^k\), because \(V(F_wX)=(A/Q)V(X)\) and \(\gcd(A,Q)=1\). Hence
\[
X+1>Q^{k-\alpha}.
\]
For \(k\ge2\), if no checkpoint in the burst falls below \(X\),
\[
\sum_{i<km}\frac1{\log(n_i+5)}<\frac2{\log(4/3)}.
\]
For \(k\ge3\), cyclically rotate to the first-copy minimum; at least \(k-1\) copies remain, giving the unconditional bound \(3/\log(4/3)\). The constants are uniform over all expanding words and their lengths. [CR09, §7]

Nevertheless any infinite C3 orbit must have infinite total reciprocal-log charge, since \(S(n)+5\le(3/2)(n+5)\). Infinitely many different bounded-cost bursts can therefore still renew an infinite total. The theorem is a strong one-burst budget, not a budget for all center changes. Its positivity hypothesis is essential: for \(3n-1\), word \((1,2)\) acts as \((9n-5)/8\), and at the positive cycle source 5 the analogous \(V\) is zero, so the divisibility lower bound is unavailable.

### 11.2 Pointwise leading-phase equidistribution

Any hypothetical infinite nonperiodic positive orbit of \(S_c\), fixed odd \(c>1\), has distinct integer states, so \(n_i\to\infty\). Its phase obeys
\[
\theta_{i+1}=\theta_i+\log_2c+\epsilon_i\pmod1,
\quad\epsilon_i=\log_2(1+1/(cn_i))\to0.
\]
For fixed nonzero Fourier frequency \(\ell\), let \(u_i=e^{2\pi i\ell\theta_i}\), \(\lambda=e^{2\pi i\ell\log_2c}\ne1\). Telescoping bounds
\[
\left|\frac1m\sum_{i<m}u_i\right|
\le\frac{2+2\pi|\ell|\sum_{i<m}\epsilon_i}{m|\lambda-1|}\to0.
\]
Weyl’s criterion gives uniform distribution of leading binary phase along that **one orbit**, conditional on its escape. This is not a population-to-pointwise inference. It gives neither trailing-bit fairness nor mean halving depth two. Any fixed positive-width phase gate is visited with positive frequency and inherits divergent reciprocal-log charge, so a genuinely finite budget on one such gate would exclude escape. A cycle arm would still be needed. [CR09, §8]

### 11.3 Externally credited injective-set packing and reciprocal summability

The report credits Michael Sharpe’s repository proof as the source of this argument; its elementary rederivation is sound on the displayed hypotheses. Let \(A_0\subset[0,32^m)\) and suppose \(T^{5m}\) is injective on \(A_0\). Then
\[
|A_0|\le2\cdot27^m+(3125/108)^m.
\]
For a \(k\)-step word with \(o\) odd operations, the offset estimate gives \(T^k(n)<2\cdot3^o\) when \(n<2^k\). Inputs with \(o<3m\) therefore have fewer than \(2\cdot27^m\) distinct endpoints. The rest occupy at most \(\sum_{j=3m}^{5m}\binom{5m}{j}\) parity classes, bounded by
\[
(1+3/2)^{5m}/(3/2)^{3m}=(3125/108)^m.
\]
Both bases are smaller than 32.

Every escaping orbit’s value set satisfies equal-time injectivity: a collision after the same number of iterates would create a repeated later orbit value, hence periodicity. Apply the finite packing estimate to its values below \(32^m\) and sum geometric shell bounds to obtain
\[
\sum_{t\ge0}\frac1{T^t(N)}<\infty.
\]
Thus the accelerated orbit’s additive correction \(E_m=\sum_{i<m}\log_2(1+1/(3n_i))\) converges. The exact logarithmic identity yields the necessary escape condition
\[
m\log_2 3-H_m\to+\infty,\qquad 3^m/2^{H_m}\to\infty.
\]
Its leading phase asymptotically follows one fixed irrational rotation. This is not a positive lower bound on average growth exponent: the accumulated margin might grow sublinearly. Summable reciprocals and divergent reciprocal-log charges are compatible. The argument’s threshold requires \(1/2<\beta<1/\log_2c\), explaining its coefficient-three range and failure to transfer to coefficient five. [CR09, §9]

**Attribution caution.** The earlier *Individual Orbit Infinite Series Bound* (GDR 2.0, cycle 05, 15 October) had already derived reciprocal summability and its clock consequences from the García–Tal (1999) collision-free orbit-window theorem. The literature chapter records the classical primary source and that internal antecedent. Thus Sharpe is the immediate repository/formalization influence for CR09’s displayed estimate, not the first origin of the underlying escape constraint. CR09 names `OrbitPacking.lean` and `OrbitSummability.lean` at repository commit `ec8174b567d5cab4960024782210b5f5db02bd3a`. Its own text says no Lean build was run. The mathematical proof above can be audited independently of that build, but historical credit and formal-verification claims must remain distinct.

## 12. Publication triage and claims that must not be promoted

A defensible publication plan is modular rather than “one near-complete proof.”

1. **Exact compiler presentations and finite certificate extraction.** State the integral isomorphism, explicit edge-row compiler, norm dichotomy, pinned compactness extraction, and birth-basis incidence normal form. Include worked signed certificates and an independent exact checker. Explain up front that universal elimination is equivalent to Collatz.
2. **Source-faithful algebraic encodings.** Present the first-jet injection, uniform bit separator, lattice decoder classification, carry formulas, and the false scalar-height quotient cycle. Connect to the documented double-zero literature; search prior work on redundant Pisot/jet representations before asserting novelty.
3. **Kernel rigidity and proof-method limitations.** Pair primitive-section equality and the one-progression regularity criterion with the bounded-replay obstruction. This makes the difference between a finite criterion and a compiler capable of proving it mathematically explicit. Credit Cobham, Christol–Kamae–Mendès France–Rauzy, and Adamczewski–Bell accurately.
4. **Restricted renewal rigidity.** Give the A/B factor-complexity and switch bounds, finite-center compression, endpoint S-unit returns, moving-dictionary restrictions, and countercontrols. State fixed parameters and distinctness hypotheses prominently; do not count applications of ESS as a new general number-theoretic technique.
5. **Guarded certificate transport and obstruction families.** Combine the collision-aware receiver bounds, thirteen-round versus unbounded root-sibling comparison, grade-changing mergers, and fixed-preview failure families. Separate new organization from reused Hercher primitives, and compare actual residual coverage against the full historical certificate union.
6. **Escape constraints as a survey/application section.** Include pointwise phase law, uniform repeated-word cost, and Sharpe’s credited packing argument. These sharpen the shape of a hypothetical escape; they do not eliminate it.

The following inferences are explicitly invalid or unsupported, often with counterexamples supplied by the research itself:

- finite positive witnesses for every prefix imply one positive infinite witness;
- real inverse-limit sign constrains an unrelated 2-adic limit;
- finite local arithmetic, four integer coordinates, or a finite alphabet imply finite predicate rank;
- terminating local compiler implies terminating repeated obligation creation;
- fixed-\(q\) S-unit finiteness remains uniform with unbounded word dimension;
- fresh primes carry an automatic division cost;
- weighted residual decay or coordinatewise convergence gives literal unweighted closure without tightness;
- a scalar golden height plus a fixed suffix gives autonomous dynamics;
- average loss, leading-phase equidistribution, or population density gives future trailing-depth fairness;
- a finite table of receivers is exhaustive merely because its known rows are exact;
- all unknown duals are continuous, Baire-1, or Hardy-\(H^2\) without proof. SW2 shows component density and explicit discontinuous compiler truncations, and the dyadic replicas of a nonzero binary invariant already violate \(H^2\).

No global Collatz conclusion follows from the audited package. The positive outcome is a set of exact interfaces with genuine proofs, a record of which proposed bridges fail, and several focused objects a mathematician can independently investigate.

## Source key and credit ledger

Internal sources, with their original dates and exact identities, are recorded in `closure_read_log.json`. Short keys used above:

- CC05: CMR Pass05, *Direct attempt to exclude every infinite 12/112 continuation*, 16 October; `libfile_998d99cf20708191a555fc1f0c40481a`.
- CC09: CMR Pass09, *Finite rational-center bridge between real and 2-adic inverse composition*, 16 October; `libfile_46b186c4bb748191ace4e2613fdbbbc5`.
- CC11/12/13: CMR reports on comparative rules, renewal-return rigidity, and arithmetic descriptions, 16–17 October; `libfile_1f2e21c675b88191882800e4a6197d8a`, `libfile_e252a84e49488191866e570b6c62dff4`, `libfile_8a1287785fdc81918ca0bdbff0a26709`.
- CC14/15: *Connected cancellation* and *Matched centers, exact carries, and legal repair*, 17 October; archive identities `libfile_9de3288a34888191940f763c4b347d7a` and `libfile_6247a16dff4c8191adf802fdebfe680d`. Read the main reports and CC14 portable lemma within the extracted archives. Same-number earlier pass branches are not interchangeable.
- CC16/17/18: CMR receiving-capacity, sibling compiler, and delayed-repair reports, 17 October; `libfile_629777c3b32c8191bc1584f4fa3bbf32`, `libfile_9919e3c0c30c8191bad1c81b7ca3488f`, `libfile_bce485c7c5548191b639ca2672d1b32e`.
- CC: *Comparative closure investigation: primitive sections, carry decomposition, and faithful domination*, 17 October; `libfile_de9a2563abfc81919269e171e4e83c14`.
- FJ: *Faithful Fibonacci lifts and an unbounded-closure test*, 17 October; `libfile_cef0e72a251481919ad273e04fb1a8e6`.
- AX: *Atlas crosscheck and proof integration*, 17 October; `libfile_ace77384863481919928da859800a604`.
- SW1/SW2: *Signed word elimination: exact structure theorem* and *Further proofs and the unresolved universal step*, 18 October; `libfile_a51cf773e2988191bd64af2f01bbf854`, `libfile_fc8da13f5e908191b6b829989cca6ae6`.
- CF/CA: *Concrete Closure Follow Up Answer and Proof* and *Additional Structure Results*, 18 October; `libfile_51e5757d787c81918e6b2d482876a5cc`, `libfile_76235aa7ab348191bbff865cd4d1fef8`.
- LG: *A proved local-to-global closure mechanism for exact edge certificates*, 18 October; `libfile_5363ea00b6008191a648d465fe333b0a`.
- CR04/CR07: *Full-Proof Architectures* and *Transported Sources and Collective Receivers*, 19 October; `libfile_b792c584582c8191b6e9f348ad40d89d`, `libfile_69e6c604e4c88191bf33d5ed919e20b1`.
- CR08/CR09: *Clock grade, coordinated history rewrites, and source-owned renewal* and *Supplied repunit receivers, uniform repetition budgets, and individual clock constraints*, 20 October; `libfile_66c043f1ecb48191a4b72046f1b1f83f`, `libfile_ed5cbaa1bbdc81919608521cb93c4ff0`.

External mathematical inputs and documented inspirations:

- Evertse, Schlickewei, Schmidt, *Linear equations in variables which lie in a multiplicative group*, Annals of Mathematics 155 (2002), 807–836. The exact external finiteness/counting input, not a project theorem. https://annals.math.princeton.edu/2002/155-3/p04
- Cobham, *On the base-dependence of sets of numbers recognizable by finite automata* (1969), and Christol, Kamae, Mendès France, Rauzy, *Suites algébriques, automates et substitutions*, BSMF 108 (1980), 401–419. Automaticity and finite-field algebraicity inputs. https://numdam.org/articles/10.24033/bsmf.1926/
- Adamczewski–Bell, *A problem around Mahler functions*, arXiv:1303.2019. Corrected title: several internal reports say “about,” but the primary record says “around.” Separate-base Mahler rigidity is a conditional comparator, not a supplied equation for the unknown Collatz witness. https://arxiv.org/abs/1303.2019
- Shmerkin–Solomyak, *Zeros of {-1,0,1}-power series and connectedness loci for self-affine sets*, Experimental Mathematics 15 (2006), 499–511. Explicitly documented context for the first-jet no-double-zero method; not evidence of novelty of the specific encoding. https://arxiv.org/abs/math/0504545
- Fernández-Duque–Weiermann, *A Walk with Goodstein*, Bulletin of Symbolic Logic 30 (2024), 1–19. Documented inspiration for canonical domination and base-change maximality, with no proved Collatz simulation imported. https://arxiv.org/abs/2004.09110
- Dershowitz–Manna, *Proving Termination with Multiset Orderings* (1979). Direct established foundation for hereditary frontier closure. https://www.cs.tau.ac.il/~nachumd/papers/LNCS/Multisets.pdf
- Yolcu–Aaronson–Heule, *An Automated Approach to the Collatz Conjecture*, Journal of Automated Reasoning 67 (2023). Relative termination and rule-removal methodology; termination of a restricted subsystem must remain distinguished from full termination. https://arxiv.org/abs/2105.14697
- Monks, Monks, Monks, Monks, *Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph*, arXiv:1204.3904. Component-sufficiency and orbit-gate background; no source-height bound is supplied merely by sufficiency. https://arxiv.org/abs/1204.3904
- Hercher, *There are no Collatz m-Cycles with m ≤ 91*, arXiv:2201.00406v3, Lemma 9. Explicitly credited merger primitive reused by creative receiver constructions. https://arxiv.org/html/2201.00406v3
- Parikh, *On Context-Free Languages*, JACM 13(4) (1966), 570–581, DOI 10.1145/321356.321364. The semilinearity theorem is independently confirmed by Esparza, Ganty, Kiefer and Luttenberger, *Parikh’s Theorem: A simple and direct automaton construction*, IPL 111(12) (2011), 614–619. https://arxiv.org/abs/1006.3825
- García and Tal, *A note on the generalized 3n+1 problem*, Acta Arithmetica 90 (1999), 245–250, DOI 10.4064/aa-90-3-245-250. Classical collision-free-window antecedent of the individual reciprocal-series control; see the independent literature chapter and the October 15 GDR2 transport. https://doi.org/10.4064/aa-90-3-245-250
- Michael Sharpe, `msharpe248/collatz`, pinned `OrbitPacking.lean` and `OrbitSummability.lean`, as credited in CR09. https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/OrbitPacking.lean and https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/OrbitSummability.lean

Primary records for the first-jet inspiration, Goodstein comparison, Mahler title, Christol paper, and multiset theorem were reopened in this audit. Other citations above preserve explicit source attribution and should be integrated with the report’s independent literature-audit chapter. No undocumented inspiration is inferred solely from mathematical resemblance.


\clearpage

# Antihydra, arithmetic observers, and controlled machine comparisons

## Scope, principal conclusions, and evidential status

This chapter reconstructs the Machine Research sequence through its last saved Antihydra checkpoint, **Effective Growing Run Funding / Continuation 05, 20 October 2026, 23:15 UTC**. It prioritizes those results but follows the dependencies back through the champion experiments, observer tools, certificate lab, and Pass 01. The separate Full Collatz Halting Equivalence folder and newer Comparative Navigation chapters are not audited here. Sixteen prose reports and twelve companion archives were retrieved; the precise coverage is in the accompanying read log.

The strongest results are not a solution of Antihydra. They are:

1. An explicit six-state champion insertion, with an all-parameter tape proof, that realizes **Antihydra's exact arithmetic driver from its exact seed 8** but has an elementary nonhalting proof. It isolates the stopping observer, rather than arithmetic expansion alone, as the relevant difference in this comparison.
2. Exact prefix-budget, phase, maximal-run, and successor-guard identities. These make missing proof obligations precise, including the distinction between funding the current run and renewing the condition needed for the next one.
3. Several genuinely quantified obstructions to restricted proof languages, not merely unsuccessful searches. Fixed congruence neighborhoods, certain polynomial/cofactor descriptions, and unordered bounded digit-window statistics cannot supply the proposed global invariants.
4. Honest source families with retained arithmetic quotients and earned budgets, culminating in an **effective, unbounded growing-run funding theorem**. This is an asymptotic theorem over a family of starting sources, not an infinite-time theorem about source 8.
5. A reproducible comparison methodology: preserve the source, distinguish true native halting from formal continuation, control every internal prefix, and test renewal as well as immediate affordability.

These are worthwhile pre-paper propositions and methodological results. Historical novelty is not established by this audit. Antihydra's blank-tape outcome remains unresolved in the latest saved research and on the official reference inspected for this review. No proof-assistant verification of these new Antihydra arguments was performed. [AH-S01, AH-S02; official status: https://bbchallenge.org/antihydra]

Labels AH-01 onward identify claims in the machine-readable ledger. “Checked proof” below means that an explicit mathematical argument was reconstructed and examined, not that a formal kernel accepted it. Reported exhaustive inventories are distinguished from the independent bounded tests performed for this review.

## 1. Models, clocks, and the logical question

### 1.1 Antihydra is not the ordinary Collatz map (AH-01)

Write

\[
f(x)=\lfloor3x/2\rfloor,\qquad w(x)=2-3(x\bmod2).
\]

The arithmetic observer system starts at \((x_0,b_0)=(8,0)\) and updates

\[
x_{t+1}=f(x_t),\qquad b_{t+1}=b_t+w(x_t).
\]

Here **t counts arithmetic returns**, not primitive Turing steps. Even inputs earn 2; odd inputs spend 1. If \(E_t,O_t\) count the respective inputs among updates 0 through t−1, then

\[
b_t=2E_t-O_t=2t-3O_t.
\]

The actual machine halts precisely on the first attempted odd update with budget zero, represented arithmetically by the first \(b_t=-1\). Thus its nonhalting assertion is the **all-prefix** statement

\[
\forall t\ge0,\quad b_t\ge0
\quad\Longleftrightarrow\quad
\forall t\ge0,\quad O_t\le2t/3.
\tag{1}
\]

The formal arithmetic recurrence can be continued after this event, but that continuation is not the native machine's execution. A later positive formal budget cannot undo an earlier halt.

The native table is

`1RB1RA_0LC1LE_1LD1LC_1LA0LB_1LF1RE_---0RA`.

With \(A(x,b)=0^\infty1^b0\,1^{x-4}(E0)0^\infty\), x≥6 and b≥0, blank tape reaches A(8,0) after **11 primitive steps**. If x−4=2n, its next return takes \(2b+3n^2+12n+11\) primitive steps. If x−4=2n+1 and b>0, it takes \(3n^2+12n+5\). If x−4=2n+1 and b=0, arrival at the undefined F0 entry takes \(3n^2+9n-1\). Completing that undefined entry by `1RH` adds one primitive step and one printed bit. Halting conventions therefore matter to exact step counts. [AH-S10 §§1–3, AH-S15 §2 and companion native rules]

By contrast, ordinary shortcut Collatz is

\[
T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.\end{cases}
\]

A t-letter parity word for T has slope \(3^{O_t}/2^t\). Both branches of f expand approximately by 3/2; its word slope is \(3^t/2^t\). A proof about one map cannot be transferred by reusing the letter O.

The arithmetic f is strictly increasing on integers x≥2 and injective on nonnegative integers: its image has residues 0 or 1 modulo 3, with inverse 2x/3 on residue 0 and (2x+1)/3 on residue 1. Since 8≡2 mod3, it has no predecessor. Consequently no distinct smaller source can merge forward into the orbit of 8. This blocks a literal transfer of the Collatz smaller-owner method; it does not block every conceivable descent or comparison argument. [AH-S15 §6]

### 1.2 A pointwise simulator is not a full-conjecture machine (AH-02)

Pass 01's two-state, eight-symbol simulator is derived from Michel's three-state, four-symbol construction. Its table is total; reaching arithmetic value 1 is detected by an **external observer**, not by an undefined transition. For an encoded input n, a simulation theorem relates that input's trace to its Collatz orbit. This does not establish that a particular blank-tape machine halts if and only if every positive integer converges. Universal quantification, enumeration, certificate search, and the chosen halting polarity require additional constructions, treated elsewhere in this writeup.

The simulator also retains physical allocation information. If a shortcut word has length t, o odd letters, and

\[
s=\sum_{j=0}^{t-1}\#\{\text{odd letters before position }j\},
\]

then, for incoming allocated length L,

\[
L_{\rm out}=L+o,\qquad \tau=2t(L+1)+2s.
\tag{2}
\]

The summaries compose as

\[
(t_1,o_1,s_1)\star(t_2,o_2,s_2)
=(t_1+t_2,o_1+o_2,s_1+s_2+t_2o_1).
\]

This is an exact clock cocycle, not a claim that arithmetic value alone determines tape state. Leading zero cells remain allocated. An absorbing-at-1 interpretation must truncate a word at its first hit of 1. No optimality or state-count lower bound follows. [AH-S16 §3 and companion `collatz_machine_build`; Michel's account: https://arxiv.org/abs/1409.7322]

## 2. Prefix resources and sufficient safety certificates

### 2.1 The minimal block data (AH-03)

For a finite word of rewards +2 and −1, let Δ be its total reward and m the minimum partial sum, including the empty prefix. A block is safe from budget b exactly when b+m≥0. Concatenation satisfies

\[
(\Delta_1,m_1)\star(\Delta_2,m_2)
=(\Delta_1+\Delta_2,\min(m_1,\Delta_1+m_2)).
\tag{3}
\]

This follows by splitting prefixes at the concatenation boundary. It is associative because both sides summarize the same ordered word. OEE and EEO both earn 3, but their minima are −1 and 0: net gain alone cannot certify safety.

For a macro graph with states z, suppose every admitted state has a covered, finite, nonempty next macro, and every edge e:z→z′ is sound on its full arithmetic guard. A reserve F supplies a sufficient certificate if

\[
F(z)\ge0,\quad F(z)+m_e\ge0,\quad
F(z)+\Delta_e\ge F(z'),
\tag{4}
\]

and the initial budget is at least F(z₀). Induction gives safety of every internal prefix and sufficient reserve at the next boundary. Coverage, closure, and nonempty finite progress are indispensable: sound rules with no rule covering a reachable state do not prove nonhalting. Defining F to be the maximum future deficit merely repackages the unsolved safety property unless an independent description and proof are supplied. [AH-S09 §2]

### 2.2 Capped observers require drawdown information (AH-04)

For a fixed cap C, let \(c_{t+1}=\min(C,c_t+w_t)\), initially c₀=b₀=0, and let \(M_t=\max_{s\le t}b_s\). Direct induction yields

\[
c_t=b_t-\max(0,M_t-C).
\tag{5}
\]

For a general block, let M be the maximum partial sum and D the maximum drawdown from an earlier peak to a later partial sum. Its cap adapter is

\[
c_{\rm out}=\min(c+\Delta,C+\Delta-M),\qquad
\min_{\rm block}c=\min(c+m,C-D).
\tag{6}
\]

For consecutive blocks u,v,

\[
D_{uv}=\max(D_u,D_v,M_u-\Delta_u-m_v).
\]

Thus capped and uncapped observers cannot be compared using only net reward, or even only net reward and minimum. At cap 11 on the actual source-8 driver, the first capped failure is update **1153**, while the true uncapped budget is **572**, its peak is **584**, and the drawdown is **12**. This is a finite same-source observer control, not a theorem that every finite cap eventually fails. The present review independently reproduced it. [AH-S03 §6]

## 3. Exact Antihydra coordinates and the successor problem

### 3.1 Odd-first run pairs and a complete unsafe-cofactor family (AH-05)

At an odd x>1 write

\[
x=1+2^ku,\quad k=v_2(x-1)\ge1,\quad u>0\text{ odd}.
\]

There are exactly k consecutive odd inputs. They lead to the even value 1+3^ku. Put \(\ell=v_2(1+3^ku)\). The following ℓ even updates end at the next odd entry

\[
x'=3^\ell(1+3^ku)/2^\ell.
\]

The combined word \(O^kE^\ell\) has total reward 2ℓ−k and minimum −k. It is affordable exactly when b≥k. Put h=b−k. At the next odd entry,

\[
h'=h+2\ell-k',\qquad k'=v_2(x'-1).
\tag{7}
\]

This exposes the renewal obligation: paying k does not bound k′.

More precisely, set

\[
Z=3^{k+\ell}u+3^\ell-2^\ell,\qquad d=v_2(Z).
\]

Then k′=d−ℓ and h′=h+3ℓ−d. Hence, for fixed k,ℓ≥1 and h≥0, the next odd run is unaffordable if and only if

\[
\boxed{u\equiv(2^\ell-3^\ell)3^{-(k+\ell)}
\pmod {2^{h+3\ell+1}}.}
\tag{8}
\]

Conversely, this congruence forces u odd and the stipulated exact ℓ, so it is not just a necessary residue test. The coefficient 3 is invertible modulo powers of 2; positive lifts are infinite. Additional fixed ternary ancestry conditions can be imposed by the Chinese remainder theorem. The result describes possible local failures, not source-8 reachability. [AH-S08 §3]

A particularly informative pair is (27,6) versus (13755,6). Both have k=1, ℓ=3, h=5. The first is an actual source-8 state and returns to (135,11) with k′=1; the second returns to (69633,11) with k′=12 and cannot afford the next odd run. Its source is not 8. A checker must classify wrong source, wrong earned budget, post-halt formal continuation, and genuine seed state separately. Even (135,0) is not an authentic counterexample, because the earned budget at 135 is 11.

An explicit regeneration family also rules out “small current runs imply bounded next demand.” For K=18m+5, let u=(2^(K+1)−1)/9 and x=(2^(K+2)+7)/9. Then k=ℓ=1 but x′=2^K+1, so k′=K. Even divisibility of x by 3 does not remove the phenomenon. [AH-S15 §§4–5]

### 3.2 Even-first phases make internal safety exact (AH-06)

At an even driver state set y=x−1, which is positive odd. Define

\[
k=v_2(3y+1),\qquad
G_k(y)=3^{k-1}(3y+1)/2^k.
\tag{9}
\]

The phase word is \(EO^{k-1}\): it first earns 2, then spends k−1. Its reward is 3−k and its minimum is min(0,3−k). Thus, for entering b≥0, endpoint affordability is equivalent to safety of every internal prefix. From (y,b)=(7,0), the original problem is exactly

\[
\sum_{j<m}k_j\le3m\qquad\text{for every }m.
\tag{10}
\]

Equation (10) is an equivalence, not a newly established upper bound.

Write y=3^r u with u odd and 3∤u. Then

\[
k=v_2(3^{r+1}u+1),\quad r'=k-1,\quad
u'=(3^{r+1}u+1)/2^k,\quad b'=b+3-k.
\tag{11}
\]

The identity \((b+r)'=b+2\) is useful accounting, but it does not bound the future r′. In fact pure powers y=3^r can have successive phase costs 1 and any prescribed K≥2. Resetting a visible valuation can transfer its information into the cofactor rather than erase it.

The phase is injective. For output z=3^r u, the only possible predecessor is

\[
y=(2^{r+1}u-1)/3,
\]

provided \(2^{r+1}u\equiv1\pmod3\); its cost is r+1. This gives exact ancestry tests, not a new global invariant. [AH-S06 §§2–3; AH-S05 §3]

### 3.3 Maximal equal-cost runs and exact handoffs (AH-07)

For k≥1 define

\[
D_k=3^k-2^k,\qquad W_k(y)=D_ky+3^{k-1}.
\]

If μ=v₂(W_k(y)), then the actual next cost is k exactly when μ≥k+1. Indeed

\[
3^{k-1}(3y+1)=W_k(y)+2^ky.
\]

Under the cost-k branch,

\[
W_k(G_k(y))=(3/2)^kW_k(y).
\tag{12}
\]

Each phase therefore decreases μ by k, and the maximal constant-cost run contains

\[
L=\lfloor(\mu-1)/k\rfloor
\tag{13}
\]

phases. Its total reward is L(3−k), its prefix minimum min(0,L(3−k)), and its affine endpoint is obtained by solving (12). Positivity of W makes the run finite.

Write W=2^μu with u positive odd, e=μ−kL∈{1,…,k}, and V=3^(kL)u. The next phase cost is

\[
k_{\rm next}=\begin{cases}
e,&e<k,\\
k+v_2(3V-1),&e=k.
\end{cases}
\tag{14}
\]

At exit budget B=b+L(3−k), an upward handoff is affordable precisely when

\[
v_2(3^{kL+1}u-1)\le B+3-k.
\tag{15}
\]

A downward cost need not be safe if the remaining reserve is too small. Full local admissibility includes

\[
u\text{ odd positive},\quad\mu\ge k+1,\quad
2^\mu u>3^{k-1},\quad
2^\mu u\equiv3^{k-1}\pmod {D_k}.
\]

These guards matter when constructing counterexamples.

The continuation report proves a stronger obstruction than unconstrained examples: choose μ=k(L+1), enforce the displayed admissibility modulo odd D_k, and impose

\[
3^{kL+1}u\equiv1+2^N\pmod {2^{N+1}}.
\]

The Chinese remainder theorem supplies positive u with arbitrarily prescribed promotion N. One may fund the entire present run and still make the next cost exceed its exit reserve. This rules out an unrestricted “long funded run automatically renews safety” inference. It does not show these states descend from 8. [AH-S05 §4; AH-S03 §§3–4]

## 4. What restricted invariants cannot do

### 4.1 Exact parity cylinders and arithmetic-progression failures (AH-08)

For p_j∈{0,1}, j=0,…,t−1, put

\[
A(p)=\sum_{j=0}^{t-1}3^{t-1-j}2^jp_j.
\]

Iteration gives

\[
2^tf^t(x)=3^tx-A(p).
\]

The word p is realized exactly by

\[
x\equiv3^{-t}A(p)\pmod {2^t}.
\tag{16}
\]

Proof of sufficiency follows recursively from the parity of the first update, then division by 2 and induction. Two sources separated by 2^tq in the same cylinder end separated by 3^tq. This is a transported arithmetic relationship, not independence of random parity events.

For any arithmetic progression a+qℕ and fixed finite budget B, there are arbitrarily large members that fail. Its modulus fixes only v₂(q) initial parity bits. Extend that compatible prefix by sufficiently many odd inputs to exhaust B; (16) and the Chinese remainder theorem realize the extended word while respecting the odd part of q. Therefore no fixed dyadic neighborhood of 8 is uniformly safe at budget zero. Nor does a fixed finite backward parity history with its earliest ancestor freely varying suffice: ternary ancestry constraints and future dyadic words can coexist. [AH-S15 §7; AH-S06 §§4,6]

### 4.2 A theorem about a specified certificate language (AH-09)

There is no inductive safety set containing (8,0), contained in b≥0, and defined by a finite Boolean combination of polynomial sign/equality tests in (x,b) and fixed congruences.

The proof is worth stating because the quantifiers are stronger than “we failed to find an invariant.” If such a set existed, its closed orbit would be safe. Along that orbit,

\[
x_t-1\ge7(3/2)^t,\qquad0\le b_t\le2t.
\]

For each of finitely many polynomials, regard x as the main variable. Beyond a polynomial threshold C(1+b)^D, its sign is determined by its highest nonzero x-coefficient at that b; identically zero specializations are harmless. At a sufficiently late orbit point, freeze its integer budget. The polynomial tests then remain unchanged along all sufficiently large x, and the congruences remain unchanged on a common arithmetic progression. Thus the alleged safety set contains a whole tail of a fixed-budget progression. Section 4.1 supplies a failing source in that tail, contradicting inductive closure into b≥0.

Later reports extend this argument to precise lifted cofactor languages and certain finite windows of complete phase states. The lifted argument uses infinitely many boundaries with r≤2 on any safe orbit, so the unbounded exponential cofactor again eventually outruns polynomial tests. Budget-dependent precision by itself does not repair the problem if the modulus is independent of the cofactor. Fixed histories are handled by infinitely many bounded-cost blocks and their exact affine relation to the present cofactor. These extensions must retain their stated language restrictions; arbitrary valuation, exponentiation, ordered-digit, or nonpolynomial validity relations are not covered. [AH-S06 §5; AH-S05 §11; AH-S04 §4]

This is not an undecidability result, a proof of unprovability, or an exclusion of all finite certificates.

### 4.3 Unordered bounded windows cannot provide the proposed global potential (AH-10)

A distinct obstruction concerns a one-step credit function depending only on unordered counts of binary windows of fixed width w. For N≥w+3, the odd number x=2^N+3 and its successor f(x)=3·2^(N−1)+4 have identical padded width-w window histograms. Any potential of those counts has zero change, while this odd update costs one unit. It cannot satisfy the required global one-step reserve inequality. This does not exclude ordered binary information, source-restricted predicates, or multiphase certificates. Eight exact rational linear-programming refutations in Search 01 additionally reject the finite feature families actually tested; those finite LP certificates are not needed for the quantified window argument. [AH-S06 §7]

A monotone height can likewise miss the boundary it is meant to protect. The project constructs a monotone quantity involving b+log_(3/2)(x−1), but the trajectory from (15,1) reaches formal (109,−1) after five updates. Monotonicity is not separation from the unsafe set. [AH-S09 §5]

## 5. Honest source families, retained quotients, and shadowing

### 5.1 Two families with genuinely earned budgets (AH-11)

For j≥1 and positive odd t define

\[
R_j(t)=\frac{3^{2^jt}-1}{2^{j+2}}.
\tag{17}
\]

The quotient is an odd positive integer. LTE gives

\[
v_2(R_j(t)-R_j(u))=v_2(t-u),
\tag{18}
\]

so it preserves 2-adic precision exactly. An expression retaining R_j(t) must not silently replace it by an arbitrary odd cofactor.

Starting at the power of two 2^a with a=2^jt−1, the honest prefix \(E^aOE^j\) leads to

\[
X_j(t)=2\cdot3^jR_j(t),\qquad
B_j(t)=2^{j+1}t+2j-3.
\tag{19}
\]

The original source is j=2,t=1: source 8 reaches (90,9) after six updates EEEOEE.

For the comparison family a=2^jt, the honest prefix \(E^aO^{j+2}\) leads to

\[
\widetilde X_j(t)=3^{j+2}R_j(t)+1,\qquad
\widetilde B_j(t)=2^{j+1}t-j-2.
\tag{20}
\]

This is not merely an adversarial arbitrary-budget family. At j=2,t=1 it starts from 16 and genuinely fails at update **22**, with endpoint x=118342 and budget −1. Its phase costs are 1,1,1,5,6,2,6. The failure was independently reproduced in this review. [AH-S05 §§5–6]

For a compatible finite continuation word w of length L (L≥2 in the odd-exponent case, L≥1 in the even-exponent case), exact parameter congruences follow from (16) and (18). The odd-exponent family starts EO, with a unique odd parameter residue modulo 2^(L−1); the even-exponent family starts E, with a unique odd residue modulo 2^L. If D(w) is its required initial reserve, the unsafe parameter cutoffs are respectively

\[
t\le\left\lfloor\frac{D(w)-2j+2}{2^{j+1}}\right\rfloor,
\quad
t\le\left\lfloor\frac{D(w)+j+1}{2^{j+1}}\right\rfloor.
\tag{21}
\]

Since D(w)≤L and the congruence periods grow exponentially, at most the least positive compatible parameter can be unsafe; larger lifts are funded. This powerful word-by-word statement does **not** exclude t=1 from every possible future word. [AH-S05 §7]

### 5.2 A finite Hydra-related shadow, not a renewed source (AH-12)

At j=2, write R=R₂(t), so the two endpoints are 18R and 81R+1, with budgets 8t+1 and 8t−4. Their next phase costs involve 1+v₂(27R−1) and v₂(243R+1). Their difference relation limits how both costs can simultaneously be large; it does not transfer credit between two different executions.

Put K=v₂(243R+1). The odd-family endpoint 18R shadows the rational point −2/27 for exactly K+1 parity inputs. The rational prefix is E,O,E,O; after four steps it reaches −2. Here the rational extension is F(z)=(3z−ε(z))/2 on rationals with odd denominator, where ε(z) is their residue modulo 2; it is **not** the real-floor function on rationals. The identity F(1−z)=1−F(z) relates its continuation to the complementary integer orbit from 3, the driver used by Hydra. This is an exact finite shadow, not a reduction of one open problem to the other.

The source equation supplies K≤8t−2. Combined with the first five reference rewards, it proves that the shadow is funded through departure with at least **11 units of reserve**; that reserve also funds the departure update plus ten subsequent worst-case odd updates. The bound is sharp for t=1. In that case K=6, the shadow lasts seven inputs, and the departure state is (1531,11), followed by (2296,10). [AH-S05 §§8–10; AH-S04 §2]

The departure retains a new descriptor, not another member of the old source family. With V=(243R+1)/2^K and H=f^(K−3)(3), its endpoint satisfies

\[
x_h=3^{K-2}V+1-H.
\tag{22}
\]

Literal renewal into a different honest odd-source member is impossible: their distinct power-of-two roots are all predecessor-free modulo 3, f is injective, and its forward orbit increases. Thus one cannot repeatedly replace t=1 by a larger t and reuse an asymptotic source theorem. [AH-S04 §3]

Continuation 04/05 develops exact coupled clocks and every-prefix adapters, but the simple offset invariant fails: on the actual source, b−c becomes negative at global update 42 although both budgets are still positive. In the source-16 control an internal negative budget is hidden by a nonnegative formal endpoint. A synchronized negative shadow block can preserve the margin b−a while decreasing both b and an odd-run length a; preservation is not production of new margin. Dropping the exact exponential cofactor equation admits counterexamples absent from the authenticated source. These are diagnostics of failed closure, not proofs of source-8 failure. [AH-S03 §7; AH-S02 §3B and companion audit]

## 6. The latest positive theorem: effective funding of growing run depth

### 6.1 Exact statement (AH-13)

Let

\[
y_0(t)=\frac{a3^{dt}-b}{q},\qquad q=2^h,
\]

with positive odd a,b, b>q, integers h,d≥1, and admissible positive t for which y₀ is positive odd. Assume a genuinely earned entering budget B(t)=γt+β≥0. The letter b in this parametrization is a **fixed source coefficient**, not the evolving observer budget. Let K_R(t) be total driver length of the first R maximal constant-cost phase runs, computed by formal continuation without assuming safety. Define

\[
A(t)=2\cdot10^{13}\log\max(a,b,3)\,\log\max(dt,3),
\qquad Q(t)=(1+A(t))^2.
\]

Then for every R≥0 and every admissible t,

\[
\boxed{K_R(t)+1\le Q(t)^R.}
\tag{23}
\]

In particular all of the first

\[
\boxed{R_{\rm fund}(t)=
\left\lfloor\frac{\log(B(t)+1)}{\log Q(t)}\right\rfloor}
\tag{24}
\]

complete maximal runs are affordable. For fixed source-family parameters and γ>0,

\[
R_{\rm fund}(t)\sim\frac{\log t}{2\log\log t},
\qquad K_R(t)=O((\log(t+2))^{2R})\quad(R\text{ fixed}).
\]

No unknown finite exceptional parameter set is omitted. [AH-S01 §§1–6]

### 6.2 Proof reconstruction

**External Diophantine input.** The rational specialization of Yu's p-adic logarithmic-form bound, as stated by Faye, Luca, and Ziegler, implies for positive odd U,V, integer N≥1, and U3^N≠V,

\[
v_2(U3^N-V)\le10^{13}\log\max(U,V,2)\log\max(N,3).
\tag{25}
\]

For U≠V use bases 3,U/V and exponents N,1. Multiplicative independence is not required in that stated theorem. Rational reduction can only reduce height, and V is a 2-adic unit. The numerical constant bounds the published expression at two bases and p=2; U=V is handled directly by LTE. Nonzero-form hypotheses are checked by positivity below. This audit verified the cited rational theorem and its constant specialization, but did not reread Yu's entire original paper. [External references E7–E8]

**Retain one large source power.** After m phases with total length S and phase start lengths 0=s₀<⋯<s_(m−1)<S, direct composition of (9) gives

\[
y=\frac{a3^S3^{dt}-E_S}{q2^S},\qquad
E_S=b3^S-q\sum_i3^{S-s_i-1}2^{s_i}.
\tag{26}
\]

The start lengths are a subset of {0,…,S−1}; summing all possible terms gives 3^S−2^S. Hence E_S is positive odd and

\[
(b-q)3^S+q2^S\le E_S\le b3^S.
\tag{27}
\]

Its logarithmic height is O(S), not O(t+S).

**Bound the next phase.** Multiply 3y+1 by q2^S:

\[
q2^S(3y+1)=a3^{S+1}3^{dt}-(3E_S-q2^S).
\]

Both coefficients are positive odd and at most max(a,b)3^(S+1); the left side is positive. Apply (25) with exponent **dt**, absorbing 3^(S+1) into the coefficient height. It yields

\[
k\le A(t)(S+1).
\tag{28}
\]

**Bound a whole constant-cost run.** With the W_k clock from (12),

\[
q2^SW_k(y)=a3^SD_k3^{dt}
-\{E_SD_k-q2^S3^{k-1}\}.
\]

Again both coefficients are positive odd. For the second, (27), b>q, and D_k−3^(k−1)=2·3^(k−1)−2^k≥0 give strict positivity. Their heights are bounded by max(a,b)3^(S+k). Equation (25) gives

\[
\mu\le\tfrac12A(t)(S+k+1).
\]

The run length u=kL is at most μ. Combining with (28),

\[
S+u+1\le[1+A/2+A^2/2](S+1)\le(1+A)^2(S+1).
\]

Induction over runs proves (23). If Q^R≤B+1, then K_R≤B. Every driver update costs at most one unit, so this crude worst-case bound funds every prefix of those runs. Taking logarithms proves (24) and its asymptotic. All argument steps use formal arithmetic, so none assumes the desired safety conclusion.

### 6.3 What improved, and what did not

The earlier Continuation 03 proved K_R(t)=o(t) (AH-26) for each fixed R using S-unit estimates. Its run compression retained at most (R+2)2^R labelled terms. Two odd terms forced any zero subsum involving them into a finite nondegenerate S-unit solution set; harmless all-even cancellations could be removed before the lower bound was applied. That proof handled variable costs and arbitrary run repetitions but left ineffective constants/exceptions. The later p-adic estimate is the stronger headline result because it is effective, explicit, and permits R to grow with t. The earlier proof remains informative about the arithmetic mechanism and should be credited as a developmental step, not counted as an independent solution. [AH-S04 §1A]

For the honest odd family the parameters are

\[
(a,b,q,d)=(3^j,3^j+2^{j+1},2^{j+1},2^j),
\]

and for the even family they are

\[
(a,b,q,d)=(3^{j+2},3^{j+2},2^{j+2},2^j).
\]

At the actual source-8 phase entry, (a,b,q,d,t)=(9,17,8,4,1), B=9. Formula (24) certifies **zero runs** with the deliberately coarse constant. More fundamentally, even a much improved bound of the form Q(1)^R does not imply

\[
K_R(1)-3M_R(1)\le9,
\]

where M_R is the number of phases. This is the cumulative expenditure inequality that would be needed. Source parameter t is not elapsed time, and §5.2 forbids the proposed literal recentering.

Finally, the coefficient envelope (27) is not a replacement for the exact ordered source word. The packet gives S=30, m=10, budget 9, y=17134933 and E=2906681588696785, lying within the allowed interval [1881583926664833,2950784590682033], yet 3y+1=2^13·6275, an unaffordable next cost 13. This is an off-source counterexample to that relaxation, independently checked here, not a counterexample to the honest orbit. [AH-S01 §7]

## 7. Champion experiments as controlled tests, not complexity folklore

### 7.1 Late attachments are completely classified (AH-14)

The Marxen–Buntrock five-state champion has table

`1RB1LC_1RC1RB_1RD0LE_1LA1LD_1RH0LA`.

Its blank run halts after 47,176,870 primitive steps with 4098 ones, a known result, not a project discovery. For a late attachment, redirect E0 to `1RF` and choose F0,F1 independently among 28 write/move/target instructions. There are 28²=784 syntactic extensions, not quotient classes under symmetries.

At the original stopping time T, every extension shares

\[
0^\infty1(F0)1(001)^{4095}1\,0^\infty.
\]

The report gives an exhaustive case proof: **112 halt at T+1, 16 halt at T+2, 656 never halt**. Among the 192 tables with exactly one halting F entry, 112 halt and 80 do not. For the 80 nonhalting cases with F1 as the sole halt entry, every visit to F reads zero; the F0→E subcases require an adjacent-one invariant to establish this. An explicit extension F0=`1RE`, F1=`1RH` satisfies the five-step moving-boundary rule

\[
1(F0)1W\longrightarrow1(F0)10W
\]

up to the specified head translation, creating an ever-growing blank gap. The extra state alone does not create an Antihydra-like cumulative observer. [AH-S13 §§2–4]

### 7.2 Internal insertion inventory and its correct scope (AH-15)

Redirect one of nine nonhalting champion transitions to F while retaining its write/move action and the old E0 halt; then choose F0,F1. This produces **7056 tables**, of which 5184 have no new halt instruction. The first inventory reported 3399 halting, 3272 nonhalting, and 385 unresolved. The later Quantity report supersedes this with **3428 halting, 3365 nonhalting, 263 unresolved**; in the sole-halt subfamily the counts are 1880,3061,243. The previously unresolved B0 slice is now completely classified: 314 halting and 470 nonhalting.

These are reported computational inventories with archived certificates. This review did not independently rerun all 7056 cases. “Unresolved” means unresolved by those tools and time limits, not a newly established open problem in the literature. Classification mechanisms include literal halting traces, translated whole-configuration recurrence, blank-ray escape, sound local overapproximations, moving-front certificates, and genuine quotients onto at most five states. A timeout proves nonhalting via BB(5) only after the relevant quotient is established and the exact bound is exceeded; it cannot be applied to arbitrary six-state tables. [AH-S12 §§Results,What actually certifies; AH-S10 §6]

Simple controls help interpret the catalogue. ID 406 has C(n)→C(n+3) in seven steps for n≥1; ID 110 has C(n)→C(n+2) in 2n+4 steps. Linear or growing sweep length does not by itself imply difficult statistical behavior.

### 7.3 Same generator and same seed, different stopping condition (AH-16)

The standout insertion is **ID 7546**, E1 redirected to `0LF`, with F0=`1LD`, F1=`1LA`:

`1RB1LC_1RC1RB_1RD0LE_1LA1LD_1RH0LF_1LD1LA`.

Let \(C(n)=0^\infty(A0)1^n0^\infty\). For every k≥0,

| Input | Output | Primitive steps |
|---|---|---:|
| C(4k) | C(6k+8) | 6k²+26k+21 |
| C(4k+1) | C(6k+7) | 6k²+24k+19 |
| C(4k+2) | C(6k+10) | 6k²+30k+31 |
| C(4k+3) | halt | 8k+14 |

These are all-parameter tape rules, not polynomial fits. Define

\[
Q(a,b)=0^\infty(A0)1^a(0011)^b0^\infty.
\]

A direct finite transition trace yields Q(a,b+1)→Q(a+6,b) in 2a+8 steps. Another trace converts each encountered group of four ones to 1001 while returning A four cells left. The initial sweep gives Q(2,k+1), Q(1,k+1), Q(4,k+1) from the first three residue cases in 8k+9,8k+9,8k+15 steps respectively; the fourth exits to halt. Consuming b pending blocks costs b(2a+8)+6b(b−1), proving the three return formulas.

Even n remains even, so the halt residue 3 mod4 is unreachable from blank C(0). This proves nonhalting. On that sector, x=n/2+8 gives exactly

\[
x_0=8,\quad x_{t+1}=f(x_t).
\]

For the full canonical family put p=n mod2 and x=(n−p)/2+8−2p. The observer is “halt iff p=1 and x is odd”; otherwise update x by f and preserve p. Thus **the very same table** initialized at C(5) has the same arithmetic seed 8 but halts at its first odd driver value:

\[
C(5)\xrightarrow{49}C(13)\xrightarrow{145}C(25)
\xrightarrow{379}C(43)\xrightarrow{94}H,
\]

for **667 primitive steps**.

Antihydra instead retains a changing unbounded b whose values can differ at the same x. Its generator does not depend on b before stopping. This is the strongest controlled explanatory example in the chapter: one can hold generator and seed fixed while changing a provably safe sector observer into a first-hit observer or an unresolved cumulative observer. It proves neither a general hardness hierarchy for observers nor a six-state minimality theorem. All six working states are reached; that is not minimality. [AH-S10 §§1–5]

## 8. Solved comparisons: preserve the original proof mechanism

### 8.1 Skelet #34 renews a scalar reserve (AH-17)

Let q(m) be the next **strictly larger** power of two minus m, and c(m)=q(m)−1 its all-ones countdown. The strictness and the −1 are essential. In the report's reset coordinates, write n=A(2r+1), A=2^k, s=A−1 and H=q(m)−n>0. With a∈{0,1},

\[
m'=A^2[4(m+s)+1+2a],\quad n'=r,
\]

and exact headroom renewal is

\[
H'=4A^2H+(8A^3-1)r+(3-2a)A^2\ge4H+1.
\tag{29}
\]

Internal countdowns stay positive, the finite rank decreases within a stage, and the outer reset supplies new positive headroom. That is a closed resource argument, unlike a current-run budget check without successor closure. It reconstructs a known nonhalting proof, not a new result about the machine. [AH-S11; AH-S08 §2.1]

### 8.2 Skelet #33 also renews a binary interface (AH-18)

The transition E1 differs from #34. Here the proof retains a leading-11 shape in the rank n (or n=1), and writes

\[
c(m)=3\cdot2^j+R,\quad L=R-2n\ge0,\quad U=2^j-R-1\ge0.
\]

With A=2^k, n=A(2r+1), and s=2(A−1),

\[
m'=A^2[4(m+s)+1]+1,\quad n'=r,
\]

\[
L'=4A^2L+(16A^3-2)r+11A^2-2,
\quad U'=4A^2U+A^2(8A-7)+1.
\tag{30}
\]

Both margins and the binary shape are renewed. Stripping trailing zeroes and the final bit preserves the required leading shape; it is not enough merely to keep a scalar positive.

Indeed, c(m)−2n can be arbitrarily large while the next reset leaves the admissible interface: n=1 and m=3·2^h−1 give c(m)=2^h, whose next rank reduces to zero. This is a failure of the projected invariant, not a counterexample to the actual #33 theorem. The comparison's lesson is to prove renewal of the **semantic shape used by the next macro**, not just solvency. The leading-11 predicate itself fails on the actual Antihydra orbit. [AH-S03 §2; AH-S08 §2.2]

The primary #33 forum summary has a coefficient-2 typo in one displayed transition. The linked Coq expression and odd case use coefficient 4; the concrete reset E₃₃(3,33)→E₃₃(1,134), not 68, resolves the discrepancy. This review verified the relevant source expression, but did not locally build the formalization. Credit belongs to Jason Yuen (`int-y1`) **and Maja Kądziołka** for the #33 formal proof. Kądziołka also identified and repaired a fixed-width counter issue in the #34 proof. Do not present this as a newly found formal-proof bug. [External references E4–E6]

### 8.3 Other comparisons retain distinct roles

Skelet #1 supplies guarded accelerators and a closed translated recurrence; the work of Shawn Ligocki, Pavel Kropitz, `uni-cycle`, and Maja Kądziołka should not be collapsed into a generic “budget” analogy. Chris Xu's Skelet #17 proof uses a regular corridor and an exceptional endgame. Newcomb Greenleaf's 1992 argument for the distinct four-state chaotic machine uses a creator-context fact: a dangerous singleton is created with a neighboring group that later amalgamates, excluding the terminal pattern. None is the Marxen–Buntrock five-state step champion.

The useful common methodology is narrower: identify exactly what makes the dangerous configuration impossible on the authenticated execution, and prove that the information survives the transformation. These are documented comparison inspirations; similarity of vocabulary is not a mathematical reduction. [AH-S16 §5; AH-S03 §1; external E12–E14]

## 9. Original-source Collatz comparison from Pass 01

### 9.1 A guarded merger theorem, not a universal descent theorem (AH-19)

For odd r≥3 put

\[
N_r=(2^{3r+2}-11)/3,\quad R_j=(9^j-1)/8,
\quad M_r=9R_r-1=R_{r+1}-2.
\]

Using O(n)=(3n+1)/2 on odd inputs and H(n)=n/2 on even inputs, the exact target word is

\[
N_r\xrightarrow{\,O(OOH)^rOHHO\,}M_r.
\]

Two smaller owners are P_r=9·2^(2r−3)−1, reaching R_r by O^(2r−3)HOH, and W_r=4^(r+1)−1, reaching R_(r+1) by O^(2r+2)H³.

When v₂(r+1)=2, set q=R_(r+1)/4>3 and factor q+1=2^(k+1)u, k≥1. If R=3^ku≡3 mod4, then

\[
M_r=4q-2\xrightarrow{\,HOHH\,O^{k-1}HO\,}(3R-1)/4
\xleftarrow{\,O^{k+1}HH\,}q.
\tag{31}
\]

The owner W_r reaches q by O^(2r+2)H⁵. Every indicated letter must satisfy its parity guard. Algebraic iteration verifies the endpoints; the valuation and residue assumptions verify those guards. Therefore a signed chain can cancel the common endpoint and leave the boundary E_(N_r)−E_(W_r). Since W_r<N_r, strong induction would certify N_r once smaller-source convergence is available. Explicit admissible classes include r≡59 mod64, 75 mod128, and 171 mod256, corresponding to k=1,2,3. [AH-S16 §§1–2]

The theorem adds a guarded original-source merger family, not a proof for all r or all n. The primitive half-source merger was already present in the Library and should not be claimed again as a new result.

### 9.2 Exact limits of the displayed approach (AH-20)

The identity v₂(R_r−R_s)=v₂(r−s) implies that every finite parity word beginning H occurs at infinitely many genuine seams of this family. Moreover M_r/N_r>(27/32)(9/8)^r. A fixed number of shortcut steps cannot force a return below the original source for arbitrarily large r: even maximal halving at that fixed horizon cannot overcome this ratio. This rules out a uniform fixed-horizon direct-descent strategy for this family, not eventual descent and not a merger to a high checkpoint of a smaller owner.

The currently displayed target and owner prefixes have disjoint support in the relevant chain representation, so their signed residual has ℓ¹ norm at least 2. Adding owner suffixes, as in (31), can escape that restricted obstruction. The proof limitation must not be inflated into an impossibility of all certificates. [AH-S16 §4]

## 10. The most recent failed continuation routes, precisely classified (AH-21–AH-23)

Continuation 05 records useful negative information rather than an answer to the open orbit.

* **Ordered history / ternary tree.** A first-failure word with m even letters has length 3m+1. If its even positions are i_j≤3j, the exact guard can be expressed through
  \(P_I(s)=(s-1)3^n+\sum_{i\in I}2^i3^{n-1-i}\), with 2^n dividing P_I(s). For s=8 the leading coefficient is 7. The optimized valuations over the admissible trees recover the actual next even position before failure, or the already existing failure cutoff. Thus this optimization is an exact re-encoding unless an independent bound is proved. A crude positivity estimate is too weak.
* **Binary-run reserve.** At an even x, if R(x) counts binary runs of ones, then the next phase cost obeys k≤2R(x)+2. Thus b≥2R(x)−1 funds the current phase. But (6,1)→(28,0) loses that guard, and a source-20 control fails. A 100,000-step successful observation on source 8 is not closure. A popcount-based candidate already loses on the actual source at update 45; an interval candidate from Continuation 04 loses at update 40. Both losses were independently reproduced here.
* **Coupled clocks.** Exact synchronized-clock formulas and a reserve adapter were obtained, but no source-derived regeneration inequality was proved. The internal-prefix failure examples rule out endpoint-only substitutes.
* **Rational-base digits.** For shifted y=x−1, the recurrence is y′=ceil(3y/2). Its base-3/2 representation appends the parity digit. Along the branch beginning at y=7, whose representation is 2122, the exact identity is
  \(b_N=3(s(y_N)-7)-N\), where s is digit sum. Safety becomes s(y_N)≥7+ceil(N/3). This is an equivalent branch-specific target. Population digit-distribution theorems average over all integers, not this one sparse branch. For the proposed branch operator \(B\phi(z)=[\phi(2z/3)-\phi((2z-1)/3)]/2\), the natural sign-weighted composition operator S is an isometric right inverse: BS=I. Hence \(\|B^k\|=1\), so a population strict contraction cannot simply be imported. Existing all-source branch normality is itself conjectural, and even a limiting 1/2 frequency would need an effective prefix bound to exclude early failure.
* **Coefficient envelopes.** Section 6.3's exact off-source witness shows why height, phase count, and source scaling without the common ordered word are insufficient.

These are separate statements: finite refutations, exact identities, restricted-language barriers, and open renewal obligations. Keeping those categories separate is itself an important part of the research methodology. [AH-S02 §3 and four companion audits; external E15–E16]

## 11. Reproducibility, attribution, and a publication plan

### 11.1 Independent checks performed for this review (AH-25)

A new, self-contained checker was written without importing or executing the archived research scripts. It passed:

* 10,000 positive odd inputs for phase, maximal-run, and handoff identities;
* 1,022 parity words of lengths 1–9, each checked at two positive source lifts;
* 175 unsafe-cofactor families with k,ℓ=1,…,5 and h=0,…,6;
* 64 honest source prefixes, both families at j=1,…,4 and odd t≤15;
* 20 rational-shadow/departure checks using the correct odd-denominator, 2-adic-parity extension;
* all 128 ID 7546 canonical inputs n=0,…,127 against literal tape simulation, and the exact 667-step C(5) control;
* 531 Antihydra native endpoint/clock cases, and the 11-step blank initialization;
* the actual-source candidate-loss and cap-11 controls, source-16 failure, and the coefficient-envelope witness.

These checks catch algebraic, indexing, clock, and implementation errors over finite domains. They do not convert an inductive proof sketch into a formal proof, validate every archived certificate, or prove infinite Antihydra safety. Exact script and results accompany the audit.

### 11.2 Credit and provenance

The Library reports identify their immediate authors as ChatGPT or Codex (OpenAI), and the arithmetic-observer direction explicitly attributes the change of emphasis to the user's proposed comparison. A paper should name the human research author(s) according to their actual contributions and disclose computational/AI assistance appropriately; this audit does not infer the user's legal name or claim that machine-generated text establishes priority.

External ideas should be credited at their actual level:

* **Machines and exact native semantics:** Heiner Marxen and Jürgen Buntrock for the five-state champion; Michael Buro and Pascal Michel for early champion analysis as documented by Michel. For Antihydra, `mxdys` is credited with the June 2024 discovery and Racheline (`rae`) with the exact macro rules in Ligocki's account. Daniel Yuan is credited with Hydra's discovery, not merely the author who explained it.
* **Known solved comparison proofs:** the people and proof projects named in §8, including Kądziołka and Yuen. The BB(5)=47,176,870 theorem is an external collective formal result, not a consequence first established by the insertion experiment.
* **Number-theoretic inputs:** Yu's p-adic logarithmic forms, using the verified rational statement in Faye–Luca–Ziegler; the earlier S-unit route uses the Evertse/Subspace-Theorem tradition through the precise statements in Bell–Diller–Jonsson–Krieger. These are imported theorems. The source-family application and its quantifier analysis are the project's work.
* **Methodological relatives:** energy-game progress measures and counterexample-guided abstraction refinement are appropriate related work for reserve certificates and spurious-source counterexample refinement. Unless a report explicitly records their use, describe them as related methods, not a retroactively asserted inspiration.
* **Rational-base comparison:** the 2026 works cited below supply current population-distribution and normality context. Their results must not be credited with the unproved sparse-branch bound needed here.

### 11.3 What could be developed into a paper

A focused paper could center on the **matched-generator experiment plus a formal observer semantics**: the all-parameter ID 7546 proof, exact uncapped/capped adapters, and source-authenticated counterexample discipline. A second mathematical note could present the **effective source-family funding theorem**, including all positivity and logarithmic-height checks, alongside the fixed-source limitation. A third contribution could organize the **restricted-language impossibility results** with precise logical syntax, avoiding an exaggerated “no invariant” title.

Before submission: independently reproduce the full inventory from certificates; formally check or obtain adversarial human review of the quantified obstruction proofs; build the exact native macro proofs; verify bibliographic priority beyond the presently checked sources; and state unmistakably that (1) remains open. More simulation, a promising population statistic, or another algebraically equivalent formulation of (1) is not the missing theorem.

## Source register

The AH-S labels below refer to the exact Library records, not to similarly named earlier drafts. All report versions were retrieved in full on 21 October 2026. Exact modification times, version IDs, archive associations, and inspected sections are recorded in `antihydra_read_log.json`.

- **AH-S01. Effective_Growing_Run_Funding_2026-10-20.md**. Library `libfile_acb5147370f88191982c771e14d40770`. Path: `/Collatz Notation Transform/Machine Research/Champion Internal Insertions - 2026-10-20/Effective_Growing_Run_Funding_2026-10-20.md`. Saved 2026-10-20T23:15:16.711831+00:00.

- **AH-S02. Antihydra_Continuation_05_Effective_Funding_And_Source_Closure_2026-10-20.md**. Library `libfile_10e46867315481918e19f1ede974795c`. Path: `/Collatz Notation Transform/Machine Research/Champion Internal Insertions - 2026-10-20/Antihydra_Continuation_05_Effective_Funding_And_Source_Closure_2026-10-20.md`. Saved 2026-10-20T23:15:15.685129+00:00.

- **AH-S03. Antihydra_Continuation_04_Comparison_Guided_Successor_Guards_2026-10-20.md**. Library `libfile_860fe48e70e481918b26f5d1e414b4dc`. Path: `/Collatz Notation Transform/Machine Research/Champion Internal Insertions - 2026-10-20/Antihydra_Continuation_04_Comparison_Guided_Successor_Guards_2026-10-20.md`. Saved 2026-10-20T22:54:06.310950+00:00.

- **AH-S04. Antihydra_Continuation_03_Bounded_Run_Funding_2026-10-20.md**. Library `libfile_82fc59bf3b80819198bda0a921826cf5`. Path: `/Collatz Notation Transform/Machine Research/Champion Internal Insertions - 2026-10-20/Antihydra_Continuation_03_Bounded_Run_Funding_2026-10-20.md`. Saved 2026-10-20T22:05:43.273326+00:00.

- **AH-S05. Antihydra_Solution_Search_02_Source_Credit_and_Shadowing_2026-10-20.md**. Library `libfile_3c4a820ca22881918e1cd9df3862641c`. Path: `/Collatz Notation Transform/Machine Research/Champion Internal Insertions - 2026-10-20/Antihydra_Solution_Search_02_Source_Credit_and_Shadowing_2026-10-20.md`. Saved 2026-10-20T21:37:06.705225+00:00.

- **AH-S06. Antihydra_Solution_Search_01_2026-10-20.md**. Library `libfile_61139c7fe7fc819197ed06a7c7060455`. Path: `/Collatz Notation Transform/Machine Research/Champion Internal Insertions - 2026-10-20/Antihydra_Solution_Search_01_2026-10-20.md`. Saved 2026-10-20T21:12:33.660292+00:00.

- **AH-S07. Antihydra_Research_Direction_2026-10-20.md**. Library `libfile_d17a2f026d248191befbb42da4d5aca6`. Path: `/Collatz Notation Transform/Machine Research/Champion Internal Insertions - 2026-10-20/Antihydra_Research_Direction_2026-10-20.md`. Saved 2026-10-20T21:17:13.181009+00:00.

- **AH-S08. Antihydra_Certificate_Lab_2026-10-20.md**. Library `libfile_d570bd5b92548191b5fce59969cb9a0f`. Path: `/Collatz Notation Transform/Machine Research/Champion Internal Insertions - 2026-10-20/Antihydra_Certificate_Lab_2026-10-20.md`. Saved 2026-10-20T20:46:56.464323+00:00.

- **AH-S09. Antihydra_Observer_Safety_Tools_2026-10-20.md**. Library `libfile_44326e908ca88191af78e367283f179b`. Path: `/Collatz Notation Transform/Machine Research/Champion Internal Insertions - 2026-10-20/Antihydra_Observer_Safety_Tools_2026-10-20.md`. Saved 2026-10-20T20:27:15.734752+00:00.

- **AH-S10. Champion_Antihydra_Quantity_2026-10-20.md**. Library `libfile_05a850524d388191bde6a42ae55d023e`. Path: `/Collatz Notation Transform/Machine Research/Champion Internal Insertions - 2026-10-20/Champion_Antihydra_Quantity_2026-10-20.md`. Saved 2026-10-20T20:14:38.093903+00:00.

- **AH-S11. Five_State_Budget_Comparison_Skelet34_and_33_2026-10-20.md**. Library `libfile_4e0e8dbca5088191bb2d59b8984062ae`. Path: `/Collatz Notation Transform/Machine Research/Champion Internal Insertions - 2026-10-20/Five_State_Budget_Comparison_Skelet34_and_33_2026-10-20.md`. Saved 2026-10-20T20:33:30.245694+00:00.

- **AH-S12. Champion_Internal_Insertions_2026-10-20.md**. Library `libfile_0f3d9f0a324081918362f84bd18a6d5d`. Path: `/Collatz Notation Transform/Machine Research/Champion Internal Insertions - 2026-10-20/Champion_Internal_Insertions_2026-10-20.md`. Saved 2026-10-20T20:00:37.619105+00:00.

- **AH-S13. Champion_One_State_Attachments_2026-10-20.md**. Library `libfile_73d90335e18881918b6f23f654a24ce3`. Path: `/Collatz Notation Transform/Machine Research/Champion Attachments - 2026-10-20/Champion_One_State_Attachments_2026-10-20.md`. Saved 2026-10-20T19:44:41.323904+00:00.

- **AH-S14. Collatz_Machines_Arithmetic_Observer_Research_Direction_2026-10-20.md**. Library `libfile_a6b2d1f3a7248191af9581d459bb43d7`. Path: `/Collatz Notation Transform/Machine Research/Antihydra Transfer - 2026-10-20/Collatz_Machines_Arithmetic_Observer_Research_Direction_2026-10-20.md`. Saved 2026-10-20T19:03:43.840694+00:00.

- **AH-S15. Antihydra_Proof_Transfer_Assessment_2026-10-20.md**. Library `libfile_09a9854ec2348191ae34b8049dd7b943`. Path: `/Collatz Notation Transform/Machine Research/Antihydra Transfer - 2026-10-20/Antihydra_Proof_Transfer_Assessment_2026-10-20.md`. Saved 2026-10-20T18:46:36.071751+00:00.

- **AH-S16. Collatz_Machine_Research_Pass01_2026-10-20.md**. Library `libfile_f96dca2b64e8819190d187fb84b64c5d`. Path: `/Collatz Notation Transform/Machine Research/Pass 01 - 2026-10-20/Collatz_Machine_Research_Pass01_2026-10-20.md`. Saved 2026-10-20T18:33:24.218384+00:00.

### Verified external references

- **E1**. [BBChallenge Antihydra](https://bbchallenge.org/antihydra). Official status, table and arithmetic description inspected.
- **E2**. [Shawn Ligocki, BB(6) is Hard (2024-07-06)](https://www.sligocki.com/2024/07/06/bb-6-2-is-hard.html). Exact macro rules and discovery attribution inspected; mxdys and Racheline/rae credited.
- **E3**. [Pascal Michel, Behavior of Busy Beavers](https://bbchallenge.org/~pascal.michel/beh). Champion section, return rules, blank runtime, ones count, historical analysis credits inspected.
- **E4**. [Skelet #34/#35 formal proof discussion; Maja Kądziołka](https://discuss.bbchallenge.org/t/skelet-34-and-35-coq-proof/165). Fixed-width counter correction and formalization authorship verified; no local build.
- **E5**. [Skelet #33 formal proof discussion; Jason Yuen and Maja Kądziołka](https://discuss.bbchallenge.org/t/skelet-33-doesnt-halt-coq-proof/180). Joint credit and overview coefficient typo inspected.
- **E6**. [busycoq, verify/Skelet33.v](https://github.com/meithecatte/busycoq/blob/master/verify/Skelet33.v). reset_invariant, step_reset, do_reset and E_next inspected through repository webpage; coefficient4 verified; no local Coq build.
- **E7**. [Faye, Luca and Ziegler, On a variant of Pillai’s problem with factorials and S-units (2024; online2023)](https://link.springer.com/article/10.1007/s11139-023-00787-1). Theorem4 equation5 rational Yu estimate inspected in full; explicit coefficient specialization checked.
- **E8**. [Kunrui Yu, p-adic logarithmic forms and group varieties II, Acta Arithmetica89(1999)337–378](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/89/4/110761/p-adic-logarithmic-forms-and-group-varieties-ii). Publisher metadata and DOI verified. Original PDF fetch blocked403. Mathematical reliance uses verified E7 statement, not a claimed fresh reading of original proof.
- **E9**. [Bell, Diller, Jonsson and Krieger, Birational maps with transcendental dynamical degree, PLMS128(2024)e12573](https://api.repository.cam.ac.uk/server/api/core/bitstreams/c62d2578-8916-4829-97b1-20459f149466/content). Author-institutional full PDF inspected, Theorem4.1 p19 and Theorem4.4 p21; S-unit/Subspace-Theorem statements and attribution verified.
- **E10**. [BBChallenge, BB(5)=47,176,870 announcement (2024-07-02)](https://discuss.bbchallenge.org/t/july-2nd-2024-we-have-proved-bb-5-47-176-870/237). Official result and collective formal proof attribution inspected; not rebuilt.
- **E11**. [Shawn Ligocki, BB(2,5) is Hard (2024-05-10)](https://www.sligocki.com/2024/05/10/bb-2-5-is-hard.html). Hydra arithmetic and Daniel Yuan discovery credit inspected.
- **E12**. [Shawn Ligocki, Skelet #1 is infinite (2023)](https://www.sligocki.com/2023/03/13/skelet-1-infinite.html). Accelerator/recurrence proof and contributor/update credits inspected.
- **E13**. [Chris Xu, Skelet #17 proof, arXiv:2407.02426](https://arxiv.org/html/2407.02426v1). Macro corridor and exceptional endgame sections inspected; no claim of local formal build.
- **E14**. [Newcomb Greenleaf, 1992 chaotic four-state machine proof, hosted by Heiner Marxen](https://turbotm.de/~heiner/BB/TM4-proof.txt). Complete proof text read; creator-context/amalgamation argument checked.
- **E15**. [Cassaigne, Espinoza, Rigo and Stipulanti, arXiv:2602.21895 (2026)](https://arxiv.org/abs/2602.21895). Abstract and metadata inspected; population versus sparse-branch scope verified. Full external proof not audited in this pass.
- **E16**. [Andrieu, Eliahou and Vivion, arXiv:2510.11723v2 (2026 revision)](https://arxiv.org/html/2510.11723v2). HTML and abstract inspected; normality remains conjectural. Not a complete theorem-by-theorem audit.
- **E17**. [Brim, Chaloupka, Doyen, Gentilini and Raskin, Faster Algorithms for Mean-Payoff Games (2011)](https://lsv.ens-paris-saclay.fr/~doyen/papers/Faster_Algorithms_for_Mean-Payoff_Games.pdf). Introduction and energy-game/progress-measure context inspected; related work, not new Antihydra proof.
- **E18**. [Clarke, Grumberg, Jha, Lu and Veith, Counterexample-guided Abstraction Refinement](https://web.stanford.edu/class/cs357/cegar.pdf). Primary CEGAR methodological description inspected; related work unless explicitly documented inspiration.
- **E19**. [Pascal Michel, Simulation of the Collatz 3x+1 function by Turing machines, arXiv:1409.7322](https://arxiv.org/abs/1409.7322). Abstract and machine-size distinctions inspected; no universal-minimality claim.
- **E20**. [Shawn Ligocki, Skelet #34 (2023-02-02)](https://www.sligocki.com/2023/02/02/skelet-34.html). Reset/countdown proof inspected and compared against formalization discussion.


\clearpage

# Comparative navigation: exact arithmetic, bounded-debt languages, and the fixed-source gap

## Scope, provenance, and reading guide

This chapter audits Comparative Navigation 05–13, giving priority to the two distinct Navigation 13 reports of 21 October 2026, Navigation 12, and Navigation 11. There are also two distinct Navigation 08 reports. They must not be collapsed into a single version history. The duplicate copies of Navigation 05, 06, 07, and 09 have identical extracted-text SHA-256 hashes; they supply no independent evidence. All these reports identify their preparer as GPT-6 Astra Pro, for Ethan Walker. This attribution records provenance, not independent human or formal verification.

The strongest material is a collection of exact, source-guarded arithmetic representations; all-shape resource bounds; explicit counterexamples to tempting proof mechanisms; and precise conditional implications. No source-specific infinite C5 escape theorem, native Antihydra nonhalting theorem, or universal Collatz theorem is established. Several results are mathematically useful without being historically new. The novelty assessment below is deliberately provisional.

Short source keys used here are N05, N06, N07; N08-S (*Sampling Interfaces*); N08-C (*Arithmetic Counters*); N09, N10, N11, N12; N13-C (*Conditioned Regions*, 15:29 UTC); and N13-T (*Tilted Observers*, 15:45 UTC). Exact Library IDs, titles, timestamps and local source copies appear at the end and in the accompanying machine-readable read log. The claim inventory uses stable NAV identifiers, exact assumptions, and a distinction between checked proofs, conditional implications, finite computations, conjectures, and refuted proposals.

### Common arithmetic and clocks

For positive odd integers define

\[
F_{c,\rho}(n)=\rho^{a-1}\frac{cn+1}{2^a},\qquad a=v_2(cn+1).
\]

The three main cases are C3 = \((3,1)\), C5 = \((5,1)\), and Antihydra phase arithmetic = \((3,3)\). C3 and C5 observations stop upon reaching one; a statement about infinite continuation explicitly uses the formal recurrence instead. In Antihydra, \(n=x-1\) at an even checkpoint of the driver \(x\mapsto\lfloor3x/2\rfloor\). A phase has one even-input update followed by \(a-1\) odd-input updates, and native budget increment \(3-a\). It first earns two units and then spends one per remaining update. Its minimum budget is therefore at entrance or exit. Formal phase arithmetic after a negative budget is not native execution.

For a depth word \(w=(a_0,\ldots,a_{m-1})\), set

\[
H_m=\sum_{i<m}a_i,\quad \Delta_m=H_m-2m,
\quad W_m=9m-4H_m,\quad V_m=4H_m-7m,
\quad b_m=3m-H_m.
\]

Only Antihydra has native \(b\). In the ordinary maps it is a comparison score. In particular, neither \(W\) nor a forest frontier is the arithmetic value of the orbit.

The inherited word compiler is fundamental:

\[
F_w(n)=\frac{P_wn+B_w}{2^{H_w}},\qquad
P_w=c^m\rho^{H_w-m},\qquad
n\equiv(2^{H_w}-B_w)P_w^{-1}\pmod{2^{H_w+1}}.
\tag{A}
\]

On concatenating words 1 then 2, the triples compose as
\((P_2P_1,P_2B_1+2^{H_1}B_2,H_1+H_2)\).
A final odd integral output authenticates all the intermediate exact divisions: an unremoved power of two in an intermediate denominator cannot be cancelled by subsequent odd multipliers and integer additions. Every prescribed finite positive-depth word has positive source lifts; sufficiently high lifts avoid absorption. This does **not** identify one positive integer realizing an arbitrary infinite word.

Among odd source residues the cylinder in (A) has density \(2^{-H}\). Thus the normalized two-adic source ensemble has independent depths with law \(\Pr(a=k)=2^{-k}\). The corresponding assertion on one named ordinary source is absent. The distinction is not cosmetic: the positive integers form a countable null subset of that reference probability space.

The exact growth identity is

\[
\log_2\frac{n_m}{n_0}
=m\log_2(c\rho/4)+\Delta_m\log_2(\rho/2)
+\sum_{i<m}\log_2\left(1+\frac1{cn_i}\right).
\tag{B}
\]

The last term is positive. Its average tends to zero if \(n_i\to\infty\), but not automatically on a cycle. Every growth claim below retains that qualification.

## 1. Newest result: a sharp arithmetic-memory threshold

### 1.1 Full arithmetic/debt states are reversible in narrow strips

**Checked theorem, N13-T §5.** For the ordinary map \((cn+1)/2^a\), with odd \(c\ge3\), let \(d=\operatorname{ord}_c(2)\). Within any positive debt strip consisting of at most \(4d\) consecutive integer levels, an output state \((y,D')\) has at most one predecessor \((n,D)\) whose transition remains in that strip. Here debt is the unreflected open-recovery coordinate

\[
D'=D+4a-9>0.
\]

Indeed every predecessor has

\[
n=(2^ay-1)/c,\qquad D=D'+9-4a.
\tag{1.1}
\]

If two exponents \(a,b\) are allowed, then \(2^ay\equiv2^by\equiv1\pmod c\). Hence \(y\) is a unit modulo \(c\), and \(a-b\) is a multiple of \(d\). Different incoming debts are separated by at least \(4d\), impossible in a strip whose diameter is at most \(4d-1\). More generally a width-\(B\) strip admits at most

\[
1+\left\lfloor\frac{B-1}{4d}\right\rfloor
\]

predecessors of a given full output state.

For C3 the unique-predecessor width is eight; for C5 it is sixteen. This is stronger than a finite enumeration: it applies at every history length. Repeated inverse decoding requires a known length or a marked starting boundary; the endpoint alone does not identify an unspecified historical cut. Recovery and overflow transitions are outside the guard. Forward arithmetic remains deterministic at every width.

The first possible ambiguities occur at widths nine and seventeen:

- C3: \((13,1)\), depth three, and \((3,9)\), depth one, both lead to \((5,4)\).
- C5: \((83,1)\), depth five, and \((5,17)\), depth one, both lead to \((13,12)\).

Antihydra is different. Its output has \(v_3(y)=a-1\), so its phase depth and predecessor are uniquely recovered without any strip restriction. It remains injective at every width. The ordinary-map theorem is therefore a restricted-history result, not a claim that all the systems lose history at some common complexity threshold.

### 1.2 Sharpness even for same-clock neutral loops

**Checked arithmetic examples, N13-T §6.** Sharpness is attained by two eight-update paths with common entrance debt two, common total depth eighteen, and identical final debt. For C3 use

\[
w=(2,4,2,2,1,3,2,2),\qquad
v=(3,2,2,2,4,1,2,2).
\]

Their maps are

\[
F_w(n)=\frac{6561n+202159}{262144},\qquad
F_v(n)=\frac{6561n+228403}{262144}.
\]

Thus \(F_w(n)=F_v(n-4)\) on the exact class \(n\equiv389809\pmod{524288}\). The first two inputs 389809 and 389805 meet at 9757. Their debt paths are

\[
(2,1,8,7,6,1,4,3,2),\qquad
(2,5,4,3,2,9,4,3,2).
\]

For C5 use

\[
w=(2,3,2,2,2,5,1,1),\qquad
v=(3,4,2,2,4,1,1,1).
\]

The offsets are 894577 and 2457077 with coefficient 390625 and denominator 262144. Their difference is \(4\cdot390625\), and the common class is \(n\equiv417135\pmod{524288}\). Inputs 417135 and 417131 meet at 621583, with debt paths

\[
(2,1,4,3,2,1,12,7,2),\qquad
(2,5,12,11,10,17,12,7,2).
\]

These are not complete critical trees. Every proper discrepancy prefix is nonnegative and total discrepancy is two. Each path adds two pending slots and closes no root, regardless of the incoming frontier. They preserve outside forest action, length, total division, terminal debt and endpoint, but not internal resource requirements.

The audit independently reproduced the complete census of all \(\binom{17}{7}=19448\) eight-depth words of total depth eighteen. At width nine, 288 loops have 284 C3 codes and 288 C5 codes; at width seventeen, 2264 loops have 1312 C3 codes and 2263 C5 codes. The no-collision thresholds follow from the inverse proof, not extrapolation from this census.

The research report authenticates two occurrences of the C5 word \(w\) on source seven, at rounds 63997 and 420159, by replaying that source through round 420167. The current values have 20508 and 135455 bits, respectively. The companions are current-value-minus-four, **not** sources below the original seven. These two large-source contacts are report-backed finite observations; the present audit rechecked the template and census, not that 420167-round replay.

### 1.3 Every equal-clock merger must separate internally

Suppose two distinct ordinary-map histories have the same length and total depth and finish at the same value. At their first synchronized arithmetic meeting, the immediately preceding depths differ by a nonzero multiple of \(d\). Their cumulative depths at the meeting agree, because their subsequent histories coincide. Consequently some proper prefix has

\[
|H_i^{(1)}-H_i^{(2)}|\ge d.
\]

The corresponding debt paths separate by at least \(4d\); a common strip must contain at least \(4d+1\) levels. This explains the sharp loops structurally.

There is also a quantitative obstruction to a pointwise free improvement. For equal-clock ordinary words,

\[
\frac{B_v-B_w}{c^M}
=\frac1c\sum_{i=0}^{M-1}\frac{2^{H_i^v}-2^{H_i^w}}{c^i}.
\tag{1.2}
\]

If \(v\) starts from a strictly smaller source and meets \(w\), the left side is positive. It is impossible that \(H_i^v\le H_i^w\) at every prefix. Some extra cumulative division must be paid. This does **not** prove that every smaller-source replacement has a larger maximum deficit. The displayed C5 example happens to do so: required original-style credit rises from zero to one, and required \(W\)-credit from ten to fifteen. A correct replacement certificate must carry its own prefix-resource signature. [N13-T §§5–7.]

### 1.4 An exact lifted normal form inside an open recovery

Write \(D=4j+r\) with \(r\in\{1,2,3,4\}\), \(j\ge0\). The residue follows the cycle \(1\to4\to3\to2\to1\). Put \(d_r=3\) for \(r=1\), and \(d_r=2\) otherwise. The debt equation gives

\[
a=d_r+j'-j.
\]

For \(X=(2/\rho)^j n\), substitution into the actual arithmetic gives

\[
X'=\frac{\rho^{d_r-1}}{2^{d_r}}
\left(cX+(2/\rho)^j\right).
\tag{1.3}
\]

Thus division variability is a periodic baseline plus a height change. In ordinary maps \(X\) is an integer with \(v_2(X)=j\), so the coordinate has not erased the source or its height. In Antihydra it is a rational with odd denominator and the same recoverable two-adic height. This is an exact normalization, not a freely chosen control input or a bound on \(j\). [N13-T §4.]

**Publication assessment.** The strip inverse law, sharp loop witnesses, prefix-separation theorem and resource tradeoff form a coherent short technical unit. Their claim is restricted arithmetic memory, not Collatz resolution. A literature search is still required before claiming priority for the restricted-injectivity observation or its exact thresholds.

## 2. Tilted observers and conditional outcome theorems

### 2.1 One reflection family contains the existing observers

Define

\[
U_\theta(m)=\max_{0\le s\le m}\{H_m-H_s-\theta(m-s)\},
\]
\[
L_\theta(m)=\max_{0\le s\le m}\{\theta(m-s)-(H_m-H_s)\}.
\]

Both include the empty interval. The first obeys Lindley reflection
\(U_\theta(m+1)=\max(0,U_\theta(m)+a_m-\theta)\).
For the forest counters defined in §5,

\[
U_2=Q-1,\quad K=-\min_{s\le m}\Delta_s,
\quad D_W=4U_{9/4},\quad D_b=U_3,\quad D_V=4L_{7/4}.
\tag{2.1}
\]

The proof is direct substitution, using that negative discrepancy jumps are only minus one. A critical root closes at a **new strict** minimum of \(\Delta\). A weak recovery also accepts ties. Returning to \(Q=1\) through a depth-two update need not close a root.

For fixed \(m\), \(U_\theta(m)\) is the maximum of finitely many affine functions of \(\theta\), hence convex, nonincreasing, and piecewise linear. A unique maximizing interval of length \(m-s\) gives derivative \(-(m-s)\). Zero-workload record sets are nested as slope increases. At \(Q_m=1\) and \(m>0\), every score with slope \(\theta>2\) is at a strict new maximum. Different slopes identify different costly episodes, not interchangeable notions of difficulty. [N13-T §§2–3.]

### 2.2 Drawdown, rather than positive score drift, can be enough

Let \(D_W(m)=\max_{s\le m}W_s-W_m\). Since the running maximum includes zero, \(W_m\ge-D_W(m)\). If a **formal infinite named trajectory** satisfies

\[
D_W(m)\le16\lceil\log_2(m+1)\rceil\quad(m\ge1),
\tag{2.2}
\]

then

\[
H_m\le\frac94m+4\lceil\log_2(m+1)\rceil.
\]

For C5 this yields

\[
n_m>\frac{n_0(5/2^{9/4})^m}{[2(m+1)]^4}\longrightarrow\infty.
\tag{2.3}
\]

For Antihydra,
\(b_m\ge[3m-16\lceil\log_2(m+1)\rceil]/4\), which is nonnegative for every integer \(m\ge32\). The first 32 actual phases must be checked independently; phase minima then cover the driver. This is a complete conditional implication, but (2.2) remains unproved. It does not require every recovery to finish. [N12 §4.]

This corrects an over-strong methodological claim in N10 §8.2 that a gain condition was additionally needed for a complete proof. Small drawdown alone does not imply positive linear \(W\)-drift, so that observation was correct. However, the desired C5 escape and native Antihydra safety have slack relative to the \(9/4\) line and need not establish positive linear \(W\)-drift. N12 explicitly extracts this weaker sufficient obligation.

More generally \(D_W(m)\le\gamma m+C\) gives C5 escape when
\(\gamma<4\log_2 5-9\), and eventual Antihydra safety when \(\gamma<3\), with an explicit finite bootstrap. The source-specific late bound \(D_W(m)\le m/4\) for \(m\ge2048\) would give \(H_m\le37m/16\); \(5^{16}>2^{37}\) certifies exponential escape. It is a conjecture, not a proved invariant.

For C3 the direction is reversed. Before absorption every odd input is at least three, so
\(n_m/n_0\le(10/3)^m2^{-H_m}\). A source-dependent lower-depth estimate \(V_m=4H_m-7m\ge-o(m)\) on a hypothetical nonabsorbing continuation would force contradiction, since \((10/3)/2^{7/4}<1\). This is a conditional target, not a shortcut to a universal lower bound.

### 2.3 Multiscale control is stronger than the outcome requires

N13-T proposes H13-S, separately for each named growing candidate:

\[
U_{2+\epsilon}(m),\ L_{2-\epsilon}(m)
\le\frac2\epsilon\lceil\log_2(m+1)\rceil,
\quad \epsilon=2^{-k},\ k\ge0.
\tag{2.4}
\]

It was formulated with the retained data available and tested only at seven slopes on each side, \(k=0,\ldots,6\), through the finite retained horizons. Those 42,000,714 observer-prefix comparisons are not an infinite theorem or out-of-sample confirmation.

Taking \(s=0\) gives
\(|H_m-2m|\le\epsilon m+2\ell_m/\epsilon\), where \(\ell_m=\lceil\log_2(m+1)\rceil\). For \(m\ge8\), select a dyadic \(\epsilon\) within a factor two of \(\sqrt{2\ell_m/m}\). Then

\[
|H_m-2m|\le3\sqrt{2m\ell_m}.
\tag{2.5}
\]

The full all-scale hypothesis would imply mean depth two. C5 then has an exponential lower bound, its positive addition correction has zero average, and its geometric factor tends to \(5/4\). Antihydra's phase factor tends to \(9/4\), and budget per phase tends to one. Native safety still needs its finite bootstrap; the single upper slope \(\epsilon=1/2\) gives \(b_m\ge m/2-4\ell_m\ge0\) for \(m\ge64\), and the actual first 64 phases were reported checked.

The full two-sided family is unnecessary for these weaker outcomes. One suitable upper slope below \(\log_2 5\) suffices for C5; slope \(5/2\) with logarithmic allowance suffices for Antihydra after bootstrap. Conversely, finite testing at seven slopes cannot justify the increasingly fine scale selected in (2.5).

Under the geometric **reference** alone, exponential moments provide an eventual logarithmic workload bound at each fixed \(\epsilon\). With \(z=1+\epsilon/2\), both
\(z^{-1-\epsilon}/(2-z)<1\) and \(z^{2-\epsilon}/(2z-1)<1\). Stopped exponential bounds, a union over interval starts and dyadic summation yield the stated scale because \(z^{2/\epsilon}\ge9/4>2\). The onset may depend on \(\epsilon\); countable intersection does not give a common onset, an all-prefix constant, or a theorem for ordinary source seven.

## 3. Recovery packets: exact cost, finite masks, and slow safe behavior

### 3.1 The cut is useful precisely because completion is not assumed

At a running maximum of \(W\), a weak recovery packet ends at the first nonnegative relative score after at least one update. Its proper prefixes are strictly negative. A strict-record packet ends at the first positive score and allows proper zero scores. If the event never occurs, the packet remains unfinished. Absorption is a separate stopping alternative. The exact queue is

\[
D_{m+1}=\max(0,D_m+4a_m-9).
\tag{3.1}
\]

For a completed packet of length \(L\) and gain \(g\),
\(H=(9L-g)/4\) and \(g\equiv L\pmod4\). Strict gains are 1 through 5; weak gains are 0 through 5, with gain 5 possible only for the one-step depth-one packet. The last depth is one or two. A strict packet is a succession of zero-gain weak packets followed by a positive-gain one. These are exact parser facts. [N11 §2.]

### 3.2 Sharp all-shape credit and affine envelopes

For increments \(p-qa\), \(p\ge q>0\), every prefix of length \(t\ge1\) satisfies
\(H_t\le H-(L-t)\). Hence the worst entering-credit requirement is at most

\[
\max(0,q(H-L)-(p-q)).
\]

The frontloaded word \((H-L+1,1,\ldots,1)\) attains it and is a legitimate first recovery for every admissible \((L,g)\). Thus

\[
R_W\le\max(0,5(L-1)-g),\qquad
R_b\le\max\left(0,\frac{5L-g-8}{4}\right).
\tag{3.2}
\]

If a packet begins at chronological time \(t\) with score \(w\), its native Antihydra reserve is \((3t+w)/4\). The sufficient deadline

\[
5L\le3t+w+g+8
\tag{3.3}
\]

therefore funds every possible internal shape with those clocks. It does not prove that the actual packet meets the deadline.

There are also sharp shape bounds for the offset. For proper prefixes, strict packets satisfy \(H_i\ge\lceil9i/4\rceil\); weak packets satisfy \(H_i\ge\lfloor9i/4\rfloor+1\). These minima define a balanced word, while \(H_i\le H-L+i\) is attained by the frontloaded word. Substitution into the weighted offset formula in §5 shows that balanced/frontloaded words minimize/maximize \(B\) for C3/C5, with the inequality reversed for Antihydra. The balanced words use only depths at most three and need at most three or four \(W\)-units; the frontloaded word may need linearly many. Duration-only bounds are deliberately conservative. [N11 §§3–4.]

### 3.3 What completion proves, system by system

For C3 an unfinished recovery has \(H_j\ge9j/4\), so before absorption
\(n_j/n\le[(10/3)/2^{9/4}]^j\). Every attempt finishes or reaches one, with

\[
L\le1+\frac{\log(n/3)}{\log(2^{9/4}/(10/3))}.
\]

Every completed packet except the one-step depth-one packet contracts: the other one-step packet has depth two, and for \(L\ge2\), admissible gains give \(H\ge2L\). This does not control the chronology of the expanding one-step packets.

For C5 every completed recovery grows by more than \((5/2^{9/4})^L\). Infinitely many completed recoveries would imply escape: their endpoints are unbounded, while infinitely many visits to a bounded set would force an eventually periodic deterministic integer orbit. Infinite completion is not established for sources seven or twenty-one. The actual cycle through 83, with depths \((5,1,1)\), never recovers from that cut and rejects a source-universal completion claim.

Every completed Antihydra recovery earns \((3L+g)/4>0\) native units, including zero-\(W\)-gain packets. Internal costs nevertheless require payment. [N11 §5.]

### 3.4 A time-bound hypothesis and an exact local observable

H11-R64 asserts that every weak packet starting at a running maximum \(t\ge2048\) on each named source completes within \(64\lceil\log_2(t+2)\rceil\). Combined with (3.2), \(3t\ge320\lceil\log_2(t+2)\rceil-8\) funds future Antihydra packets. The report gives an authenticated initial checkpoint at phase 2053, \(W=2277,b=2109\). For C5 the same hypothesis gives

\[
n_m>n_0(5/2^{9/4})^m/[2(m+2)]^{80}
\]

at late times. Neither implication proves the waiting hypothesis. An \(O(\log t)\) chronological bound is much stronger than the previously proved \(O(\log n)\) source-height clocks when arithmetic height itself is exponential in \(t\).

The capped weak recovery time \(\min(\tau,R)\), \(R\ge2\), is determined by
\(n\bmod2^{\lfloor(9R-5)/4\rfloor}\); for the strict convention use exponent \(\lfloor(9R-6)/4\rfloor\). Union the exact cylinders for completions of lengths below \(R\). A maximal-depth short completion and a source shift by \(2^H\) prove sharpness: the shift preserves earlier depths but forces the last output even, increasing its actual depth enough to prevent completion at that time.

At cap five, weak counts among 512 odd classes modulo 1024 are \((384,32,16,24,56)\); strict counts among 256 classes modulo 512 are \((192,16,8,5,35)\). The means are \(109/64\) and \(443/256\). This is not the earlier critical-tree cap-five observable, which needs only eight bits. The audit independently recomputed all these masks.

In the geometric reference, \(\Pr(\tau>N)\le\mu^N\), with
\(\mu=(5/4)/(10/9)^{9/4}\), \(\mu^4=387420489/409600000<1\), and \(\mu^{64}<1/2\). Summability motivates the time hypothesis only in that ensemble. The reference recovery mean is finite, in contrast with the critical-tree mean; a stopped-sum argument gives \(\mathbb E\tau=\mathbb E g\). The source reports rigorous rational enclosures near 3.232347322 for weak recovery and 3.412384247 for strict recovery, obtained by exact dynamic programming through length 1024. Those full-horizon DP enclosures were not rerun in this audit. [N11 §§6–8.]

### 3.5 Long duration is not intrinsically dangerous

For every \(r\ge0\),

\[
Z_r=(3,2,2)(3,2,2,2)^r(2)
\]

is a weak recovery of length \(4r+4\), total depth \(9r+9\), and gain zero. It needs three \(W\)-units for \(r=0\), four otherwise, and never spends native Antihydra credit. Every finite word has actual positive-source cylinders. All maximal equal-depth runs are at most four, and all changes reset the appropriate local prime record. Therefore short local runs and repeated resets do not imply quick recovery. This does not refute H11-R64 for a fixed named source, because varying \(r\) changes the constructed source. [N11 §9.]

More generally, an open or completed recovery of maximum relative debt \(B\) requires at most
\(\max(0,\lfloor(B-3)/4\rfloor)\) native entering units, independently of duration. At an open prefix of length \(t\), native gain is \((3t-D_t)/4\); a completed nonnegative endpoint only improves it. A sufficiently large first depth followed by ones attains the bound. A proof may therefore allow controlled slow behavior instead of forcing all packets into a fast-return theorem. [N12 §4.]

## 4. Canonical regions, hidden peaks, and conditioned references

### 4.1 Exact region parsing and queue actions

The canonical types are

- \(E_j=(1,2^{j-1})\), with the next unconsumed depth known to be one;
- \(G_{j,h}=(1,2^{j-1},2+h)\), \(j,h\ge1\);
- \(S(a)=(a)\), \(a\ge2\), included in the broad G group.

The notation \(2^{j-1}\) in a word denotes repetition, not exponentiation of a depth. A trailing shallow/neutral fragment without the required lookahead remains unclassified. A = \(E_1\), B = \(E_2\); C is the \(j=1\) longer-G family.

Their \((W,V,b)\) gains are respectively

\[
E_j:(j+4,j-4,j+1),\quad
G_{j,h}:(j+5-4h,j-3+4h,j+2-h),
\]
\[
S(a):(9-4a,4a-7,3-a).
\]

Every E earns \(W\); every G earns \(V\); only \(E_1,E_2,E_3\) spend \(V\). A longer G first earns \(j+4\) units of \(W\) and then spends \(4h-1\). Therefore its exact debt action is

\[
D'_W=\max(D_W-j-5+4h,4h-1),
\tag{4.1}
\]

not merely reflection of its net gain. E and S use ordinary reflected net gains. For \(V\), maxima occur at block boundaries, so reflected net gain is exact there. A C3 example, \(19\to29\to11\), has depths \((1,3)\), net \(W\)-gain two, but terminal drawdown three. Net gain and drawdown from a newly earned peak are different.

If \(\bar D\) uses only complete-region net gains and

\[
A_k=\max_{i\le k,\,i\text{ longer G}}\min(j_i+4,4h_i-1),
\]

then at the same endpoint

\[
0\le D_W-\bar D\le A_k.
\tag{4.2}
\]

Each omitted internal maximum exceeds its larger neighboring boundary by exactly the displayed local amount. The maximum of those omissions bounds the error; they do not accumulate additively. The family \(j=4h-4\) has net gain one but arbitrarily large hidden peak, so no source-universal constant correction exists. [N12 §2.]

For slopes \(2\le\theta\le3\), an E gains \((\theta-2)j+1\) in \(\theta m-H\). A longer G gains \(g=(\theta-2)(j+1)+1-h\), first earning \(p=(\theta-2)j+1\) and then spending \(q=h-(\theta-2)\ge0\). Its exact action is \(U'=\max(U-g,q)\). Below slope two the neutral portion no longer rises, so that particular interior-maximum formula must not be reused without reanalysis. [N13-T §2.]

An actual Antihydra packet at phase 88 has depths \((7,1,1,1,4,1,1,3,1)\) and relative \(W\)-scores \((-19,-14,-9,-4,-11,-6,-1,-4,1)\). It repays, spends again, and recovers inside a later G prefix. This source-authenticated counterexample rejects the proposed one-pass “E starts final drainage” mechanism, not the exact queue rules. [N12 §3.]

### 4.2 The exact two-state reference kernel

Under the geometric source reference retain F, meaning the next depth is already known to be one, and U, meaning unrestricted. After E the parser is in F; after longer G or S it is in U. Given F,

\[
\Pr(E_j\mid F)=\tfrac12 4^{-(j-1)},\quad
\Pr(G_{j,h}\mid F)=4^{-(j-1)}2^{-(h+2)}.
\]

The group transition matrix is \(\bigl(\begin{smallmatrix}2/3&1/3\\1/3&2/3\end{smallmatrix}\bigr)\), but blocks are not iid. Weight duration by \(s\) and negative \(W\)-gain by \(z\). For

\[
u=(s/2)z^{-5},\quad v=(s/4)z^{-1},\quad
w=\frac{sz^3}{8(1-z^4/2)},\quad z^4<2,\ v<1,
\]

the kernel is

\[
K=\begin{pmatrix}
u/(1-v)&2uw/(1-v)\\
u/[2(1-v)]&v+w+uw/(1-v)
\end{pmatrix},\qquad \det(I-K)=1-u-v-w.
\tag{4.3}
\]

The determinant reproduces the raw one-update moment. Regrouping does not create a second independent rarity factor. Conditional expected \(W\)-gains are 3 in F and 0 in U; expected durations are \(5/3\) and \(4/3\). Their stationary half-and-half mixture gives drift one per update. An actual deterministic path requires control of its source-selected routing error, not just a reference transition matrix. [N12 §5.]

### 4.3 Conditioning a long recovery changes the appropriate reference

For \(\theta>1\) define the analytic reference family
\(\pi_\theta(a)=\theta^{-1}(1-\theta^{-1})^{a-1}\). A word with clocks \((m,H)\) has probability

\[
\Pr_\theta(w)=(\theta-1)^{H-m}/\theta^H.
\]

At fixed clocks all permitted words therefore have equal relative weights under every \(\theta\), even after imposing first recovery, band, tree, or region constraints. This is an exact change-of-measure statement, not independence of the conditioned interior depths. Only \(\theta=2\) is the original uniform-source law.

For \(\theta=9/4\), \(\pi_*(a)=(4/9)(5/9)^{a-1}\), and a recovery of gain \(g\) satisfies

\[
\Pr_2(w)/\Pr_*(w)=\mu^m(10/9)^{g/4},
\]

with the same \(\mu\) as in §3.4. Near-zero-gain long recoveries have clocks near mean depth \(9/4\), not two.

Writing \(p=1/\theta,r=1-p\), the biased E/G kernel is

\[
\begin{pmatrix}p/(1-pr)&r^2/(1-pr)\\p^2/(1-pr)&1-p^2/(1-pr)\end{pmatrix}.
\]

Its stationary E share is \(p^2/(p^2+r^2)\), and mean region duration is \((1-pr)/(p^2+r^2)\). At \(9/4\), these are \(16/41\) and \(61/41\), with matrix \(\bigl(\begin{smallmatrix}36/61&25/61\\16/61&45/61\end{smallmatrix}\bigr)\). The corresponding offspring mean is \(5/4\), and unconditioned reference extinction probability is \(4/5\); no infinite tilted tree is thereby asserted inside a completed packet.

N13-C computes finite conditional statistics by completion counts \(B_r(d)\): count positive-debt interior paths with \(r\) remaining steps and terminal debt \(-g\). Each edge is weighted by its number of possible completions, and depth/region occurrences are counted by forward/backward products with the parser memory retained. The report checks the DP exhaustively through length eight and evaluates it through length 256. At length 256 its conditional depth-one share is about 0.444218 and local-parser E share about 0.389297, close to \(4/9\) and \(16/41\). The retained long packets have similar descriptive shares. The duration bins, dependent samples and parser boundary choices prevent an automatic goodness-of-fit claim.

The slow family \(Z_r\) has no depth-one updates and only S/G regions while having the same near-critical clocks. It refutes any source-universal assertion that every long packet must exhibit the tilted local proportions. [N13-C §§6–9.]

### 4.4 A local/global split of the remaining hypothesis

For a longer-G hidden peak at least \(b\), one needs both
\(j\ge J=\max(1,b-4)\) and \(h\ge h_0=\lceil(b+1)/4\rceil\). Under the original reference,

\[
\Pr(A_{\rm block}\ge b\mid F)
=\frac23\,4^{-(J-1)}2^{-h_0},
\]

and the U probability is half as large. A large terminal depth alone is insufficient: the preceding earning prefix must also be long.

N13-C proposes, separately for named sources,

\[
A(t)\le4+\lceil\tfrac12\log_2(t+2)\rceil\quad(t\ge64),
\qquad \bar D(t)\le t/4\quad(t\ge2048)
\tag{4.4}
\]

at canonical boundaries, retaining all earlier peaks in \(A\). Both are unproved. The no-bootstrap hidden-peak variant is actually false: Antihydra phases 4–8 have depths \((1,2,2,4)\), producing hidden peak seven when that early right side is six. The revised threshold is a post-counterexample hypothesis.

Assuming (4.4) and an authenticated finite bootstrap through the first boundary beyond 2048, (4.2) gives \(D_W(m)\le m/4+A(m)\) at all late update times. Negative \(W\)-increments occur only at S or terminal-G updates, so no hidden interior negative step is lost. Consequently

\[
n_m>\frac{n_0[5/2^{37/16}]^m}{2^{5/4}(m+2)^{1/8}}
\]

for C5, and \(b_m\ge11m/16-A(m)/4\) for Antihydra. This separates a local joint valuation exclusion from the global succession of region debts; it does not solve either one. [N13-C §8.]

## 5. Forest semantics and all-shape results inherited by the newest work

### 5.1 A forward tree, not an inverse Collatz tree

A depth-\(a\) update is a preorder node with \(a-1\) ordered children. Begin with one pending slot; processing a node changes pending count by \(a-2\). When it reaches zero, count one completed root and restart at one. A complete \(m\)-node tree has nonnegative proper discrepancy prefixes and final discrepancy minus one, hence \(H=2m-1\). The exact identities are

\[
Q_m=1+\Delta_m+K_m,\qquad K_m=-\min_{s\le m}\Delta_s.
\tag{5.1}
\]

Thus homogeneous growth is \((c\rho/4)^m(\rho/2)^{Q-K-1}\). Internal shape drops out of that factor but remains in offset, source guard, and prefix safety. Also \(\Delta_m/m\to0\) iff both \(Q_m/m\to0\) and \(K_m/m\to0\). For the nontrivial direction, the running negative minimum is \(o(m)\) whenever the discrepancy itself is \(o(m)\). These are identities and equivalent targets, not proofs that the target holds. [N06 §§3–4.]

For a packet with discrepancy total \(\delta\), minimum \(\mu\), maximum \(\nu\), and maximum ordered upward excursion \(R\), the exact action on any initial frontier \(q\ge1\) is

\[
k=\max(0,1-q-\mu),\quad q'=q+\delta+k,
\quad q_{\max}=\max(q+\nu,1+R).
\tag{5.2}
\]

These fields compose by prefix-minimum/maximal-excursion algebra. Different initial frontiers \(q_1<q_2\) synchronize exactly when the running minimum is at most \(1-q_2\), and their difference never exceeds \(q_2-q_1\). Equal frontier counts do not retrospectively equate ancestry. [N07 §2; N08-S §2.]

### 5.2 C3 can finish an arbitrary finite pending workload

Starting with \(q\) pending slots and no new-root reset until those slots are filled, every proper unfinished prefix has \(H_j\ge2j+1-q\). Before absorption,

\[
n_j/n\le2^{q-1}(5/6)^j.
\]

Therefore the operation finishes or reaches one within

\[
1+\frac{\log(n/3)+(q-1)\log2}{\log(6/5)}
\]

odd rounds. This controls arbitrary tree shapes, not a finite catalogue. It does not bound how often a new workload is later started. [N06 §6; N08-S §2.]

A complete C3 tree grows iff it has one or two nodes. The one- and two-node words are \((1)\) and \((2,1)\). The only three-node words have maps \((27n+37)/32\) and \((27n+49)/32\), with legal source classes 33 and 61 modulo 64; both descend. For \(m\ge4\), \(2(5/6)^m<1\) proves descent for every shape. C5 complete trees always grow, with homogeneous multiplier \(2(5/4)^m\). Infinitely many such completions suffice for C5 escape but are not established on a named source. Antihydra complete trees earn \(m+1\) native units but can need as many as \(\max(0,m-3)\) units at entrance, attained by the star \((m,1,\ldots,1)\). [N06 §§6–7.]

### 5.3 Sharp offset and scheduling information

For every word,

\[
\frac BP=\frac1c\sum_{i=0}^{m-1}
\left(\frac4{c\rho}\right)^i
\left(\frac2\rho\right)^{\Delta_i}.
\tag{5.3}
\]

For a complete tree, \(0\le\Delta_i\le m-1-i\) at proper prefixes. The unary tree attains every lower bound, and the star every upper bound after the empty prefix. Their offsets are

\[
B_U=\frac{(c\rho)^m-4^m}{c\rho-4},\qquad
B_S=(c\rho)^{m-1}+2^m\frac{c^{m-1}-2^{m-1}}{c-2}.
\]

Thus \(B_U\le B\le B_S\) in ordinary maps; the inequalities reverse for \(\rho\ge3\). An adjacent depth swap changes offset by
\(2^a\rho^{b-1}-2^b\rho^{a-1}\), multiplied by the appropriate prefix denominator and suffix coefficient in context. Source guards change too. [N07 §4.]

For positive-gain complete child packets, arranging children in increasing required entering credit minimizes total credit: the two-packet cost is \(\max(R_A,R_B-g_A)\), and an adjacent-exchange comparison proves the rule. Affine endpoint optimization uses a different order, based on \(\beta/(\alpha-1)\) for child maps \(\alpha n+\beta\), \(\alpha>1\). A ten-node Antihydra example has lower offset in the order requiring three entering units, while the other order needs zero. The actual source fixes the order; optimization across alternative words is not an operation available on that source. [N07 §5.]

For scores \(p-qa\), \(p\ge2q\), and a tree of \(m\) nodes with depths at most \(d\), the sharp maximal requirement is

\[
\max\left(0,\max_{1\le t<m}
\min\{(qd-p)t,\ q(m-1)-(p-q)t\}\right),
\tag{5.4}
\]

with zero for the one-node exceptional case. It follows from the simultaneous bounds \(\Delta_t\le(d-2)t\) and \(\Delta_t\le m-1-t\); a queued-sibling path attains the maximizing prefix. Combs with depth \(d\) repeated \(k\) times followed by \((d-2)k+1\) leaves show unbounded required credit even with bounded individual depth. Moderate-depth clusters, not only record depths, matter. [N10 §7.]

### 5.4 Classical reference law and the exact conditional C3 bridge

The geometric source law gives a critical geometric offspring distribution. With \(C_r\) the Catalan numbers,

\[
\Pr(T=m)=C_{m-1}/2^{2m-1},\quad
\Pr(T>m)=\binom{2m}{m}/4^m,
\quad f(z)=1-\sqrt{1-z}.
\]

The reference tree is finite almost surely but has infinite mean. These are classical branching/ordered-tree facts, not new Collatz theorems. The tail is not the no-descent survival tail from another stopping rule. Starting with \(q\) roots gives
\(\Pr(T_q=m)=\frac qm\binom{2m-q-1}{m-1}2^{-(2m-q)}\).

For actual C3 prefixes avoiding one, \(4K_m\le m\) suffices for descent, by \(H_m\ge7m/4\) and \((10/3)^4<2^7\). At completed roots it is enough that
\(\sum_{i\le J}\min(T_i,16)\ge4J\). The reference capped mean is \(300540195/67108864\approx4.4784\), but no source-selected theorem supplies that mean. For escape exclusion alone, root cap five would suffice if its liminf mean exceeds \(1/(2-\log_2 3)\); the reference mean \(315/128\) exceeds that threshold. This remains conditional and does not exclude cycles by itself. [N06 §8.]

The capped first-tree size at R depends only on \(n\bmod2^{2R-2}\). At cap five its counts among 128 odd residues modulo 256 are \((64,16,8,5,35)\). The audit recomputed them, as well as the largest odd-affine interval discrepancy constants \(1097/128\) for C3/C5 and \(1001/128\) for Antihydra. These are exact finite masks; the problem is their values at the actual selected roots, not access to an uncomputable observable. [N08-S §§3–4.]

The reference root-count moments and unfinished-tree age also follow from \(f\). If \(u_N=\binom{2N}{N}/4^N\) and \(S_N=(2N+1)u_N\), then
\(\mathbb E K_N=S_N-1\) and \(\operatorname{Var}K_N=2N+2-S_N-S_N^2\). The last renewal time has law \(\Pr(G_N=g)=u_gu_{N-g}\), giving mean age \(N/2\), variance \(N(N+1)/8\), and the classical scaled arcsine limit. Very old unfinished trees are compatible with the reference, but these formulas give no probability assignment to a named source. [N07 §9; N08-C §6.]

## 6. Bounded-debt languages: safe internal complexity is not a safe exit theorem

### 6.1 Complete small-band graphs

Inside \(1\le D\le B\), every edge is \(D\xrightarrow{a}D+4a-9\). Recovery and overflow are explicit exits.

- At B = 3 there is no interior cycle; only \(3\xrightarrow2 2\xrightarrow2 1\).
- At B = 4 the entire cyclic graph is \(1\xrightarrow3 4\xrightarrow2 3\xrightarrow2 2\xrightarrow2 1\).
- At B = 5 there are two four-step returns from debt two: \(P=(2,3,2,2)\) and \(Q=(3,2,2,2)\).

For the width-four cycle, write its affine map as \((Pn+B_0)/512\). The centered reserve \(C(n)=(P-512)n+B_0\) gives the exact number of complete repeats
\(\lfloor(v_2(C(n))-1)/9\rfloor\). Legality of one repeat is exactly reserve valuation at least ten; each repeat subtracts nine from that valuation. None of the relevant positive odd states has zero reserve. After the repeats, at most four actual tests identify recovery, absorption, or an unhandled overflow, which must not be executed as if certified safe. [N12 §6.]

The P/Q maps have coefficients/offsets

| Map | Coefficient | P offset | Q offset | Denominator |
|---|---:|---:|---:|---:|
| C3 | 81 | 287 | 323 | 512 |
| C5 | 625 | 513 | 613 | 512 |
| Antihydra | 19683 | 10725 | 9753 | 512 |

Every finite binary choice sequence has source realizations. The packet \((3,2)\{P,Q\}^*(1)\) is a weak recovery with bounded debt, arbitrary finite length and binary complexity, and no native Antihydra spending. Its pending forest boundary grows linearly. It shows why sublinear frontier is sufficient for an exact reference rate but unnecessary for the weaker safety/growth outcome.

Within this language C3 contracts uniformly and cannot continue forever; an actual infinite C5 continuation would grow; every Antihydra step is funded. None of the named sources has been proved to stay in this language indefinitely.

### 6.2 All width-five binary history is exactly recoverable

**Checked theorem, N13-C §3.** Let the common coefficient be \(A=p^r\). For C3, C5, Antihydra, respectively, \((r,h)=(4,2),(4,2),(9,5)\), where \(h=v_p(b_1-b_0)<r\). For a k-routine binary history,

\[
B_\epsilon=\sum_{i=0}^{k-1}A^{k-1-i}512^i b_{\epsilon_i}.
\]

If \(j\) is the latest differing choice between two histories, its term has uniquely lowest p-adic order. Hence

\[
v_p(B_\epsilon-B_\eta)=h+r(k-1-j)<rk.
\]

All \(2^k\) offsets are distinct modulo \(A^k\), so distinct histories cannot have an equal-clock integer-source merger. The endpoint tags identifying the final branch are P/Q = 10/1 modulo 27 for C3, 74/124 modulo 125 for C5, and 48/291 modulo 729 for Antihydra. After selecting a tag, reverse \(x=(512y-b)/A\) and check the guard. This decodes a specified finite history without asserting that its next exit is safe. The later general strip theorem strengthens the ordinary-map uniqueness range beyond this particular binary grammar.

### 6.3 Counting thresholds are not first-collision thresholds

For the closed-path adjacency matrix of the debt band, every m-step loop has \(4H=9m\), hence \(m=4k,H=9k\). N13-C supplies positive integer vectors for B = 14 and 15 with
\(3v_{14}-A_{14}v_{14}=3\mathbf1\) and
\(3v_{15}-A_{15}v_{15}=-174\mathbf1\).
The first certificate implies every closed-path count is below \(3^m\) at every length. At B = 15 an exact power gives

\[
(A_{15}^{24})_{8,8}=292366481680>3^{24}=282429536481.
\]

The pigeonhole principle therefore forces a C3 endpoint-code collision. Both vector identities and this matrix power were independently recomputed in the audit. Width fifteen is the first width at which this **counting method** can force a collision, not the first actual collision width, which is nine. For C5, source-cylinder disjointness gives \(N\le2^H<5^m\) on these loops, so this count cannot force a collision at any width. Actual C5 collisions nevertheless exist. [N13-C §4; N13-T §§5–6.]

N13-C also gives an earlier twelve-step C3 width-nine pair and a C5 width-31 embedding of the N08 subtree pair. N13-T's eight-step C5 width-17 pair improves the resource-width witness; it does not invalidate the earlier embedding. A common short tail can neutralize the \(W\)-gain of any same-size complete-tree merger after refining its endpoint cylinder. That construction preserves source shift but does not remove original-source ownership requirements.

### 6.4 Reversible and funded history does not guarantee a funded next phase

After \((3,2)\) and k P/Q routines, the formal Antihydra history has earned \(1+3k\) native units, stayed inside the narrow band, and retained a uniquely decodable past. Prescribe next depth \(3k+5\). The finite-cylinder theorem realizes the whole word at infinitely many positive sources; the next phase first earns two and then spends \(3k+4\), reaching minus one at its final driver step. Thus long duration, narrow debt, recoverability and earned credit do not force a safe exit at arbitrary sources. This is a changed-source family, not a counterexample to source eight. [N13-C §5.]

In any fixed positive strip \(\ell\le D_i\le u\),
\(H_m=(9m+D_m-D_0)/4\). Consequently C3 exits or absorbs; an actual infinite C5 continuation confined there escapes at factor \(5/2^{9/4}\), not \(5/4\); and Antihydra is funded if entrance credit is at least \(\max(0,\lfloor(u-D_0-3)/4\rfloor)\). These are outcome guarantees **conditional on staying in the guard**. [N13-T §4.]

Finally, if both \(D_W'\) and \(D_V'\) are positive, their reflected recurrences give
\(D_W'+D_V'=D_W+D_V-2\). A positive-positive episode with entering total S has at most \(\lfloor S/2\rfloor\) states. Clipping can create another episode later, so this is not a globally decreasing potential. [N13-C §2.]

**Small textual correction.** N13-T §8 correctly gives interior feasibility thresholds \(B\ge j+5\) for E, \(B\ge\max(j+5,4h)\) for longer G, and \(B\ge4a-8\) for a deep S step. Its final prose suggests those thresholds depend on absolute strip location. For wholly interior transitions this is unnecessary and incorrect: translating every debt by a constant preserves every edge and every range width. The thresholds extend to any translated positive strip of the same width. Native funding at entrance is a separate, location-dependent resource issue.

## 7. Arithmetic memory, source mergers, and ownership

### 7.1 Baseline strides and event inverses

N05 uses \(d=c\rho-4\), \(Z=dn+\rho\), \(\lambda=c\rho/4\), \(\eta=\rho/2\). Direct substitution gives

\[
Z(F(n))=\lambda\eta^{a-2}Z(n)+\rho(1-\eta^{a-2}).
\]

At depth two, \(Z'=\lambda Z\) exactly. The identity \(cZ=d(cn+1)+4\) shows that \(v_2(Z)=1,2,\ge3\) correspond to next depth one, at least three, and two, respectively. A nonzero neutral reserve therefore has exact stride length \(\lfloor(v_2(Z)-1)/2\rfloor\). C3 at one is the separated zero case.

A deviation event is one depth \(a\ne2\) followed by its maximal neutral stride L. It always finishes, has \(M=L+1,H=a+2L\), and discrepancy \(a-2\). Its duration and signed deviation are distinct. Its reference event law is \(\Pr(a,L)=2^{-a}4^{-L}\) at the event section; shallow share is \(2/3\), not the canonical E share \(1/2\). These are different sampling cuts. [N05 §§2–5.]

In Antihydra an event endpoint y has
\(v_3(5y+3)=2L+\mathbf1_{a\ge3}\). It recovers L and the shallow/deep tag; reversing neutral multiplication and then using \(a=1+v_3(\text{phase output})\) recovers the whole event. For ordinary C3/C5, endpoint prime valuation is ambiguous: a deep resonance can create the record. Given ordinary endpoint y and \(t=v_p((p-4)y+1)\), all incoming neutral durations lie in \(0,\ldots,t\). For each L, reverse the neutral action to an intermediate value \(m_L\), then solve \(x=(2^a m_L-1)/p\) with \(a\ne2\) and \(2^am_L\equiv1\pmod p\). For \(L<t\), only the resonance class \(a\equiv2\pmod{\operatorname{ord}_p(2)}\) is allowed. This is a complete incoming atlas, not a source-fairness theorem. [N05 §§6–8.]

### 7.2 Same-clock endpoint codes create genuine smaller-source relations

For equal clocks and common P,
\(F_w(x)=F_v(z)\) iff \(z=x-(B_v-B_w)/P\). An integral shift exists exactly when \(B_v\equiv B_w\pmod P\). It is even. N08-C strengthens the sufficient-high-lift statement: if \(B_v>B_w\) and x is an actual positive source of w, the companion is automatically positive in formal arithmetic. A negative odd source cannot evolve through positive-coefficient branches to the positive common endpoint. Absorption and native budget guards remain separate.

For complete same-size trees, replacement preserves all outside forest action. The smallest C3 tree collision in the exhaustive small-size census has six nodes; one pair has sources 3025 and 3021, common endpoint 1079, and shift four. The first C5 tree collision has eight nodes, sources 35823 and 35819, endpoint 427083, and shift four. N08-S reports ten authentic current-source contacts in the retained C5 traces, including source-seven rounds 115213 and 184909. These are finite contacts inside unfinished global trees, not new roots and not contacts below original seven. [N08-S §§6–7; N08-C §3.]

Every complete m-node tree ends with depth one, fixing \(B\bmod c\); there are at most \((c\rho)^{m-1}\) endpoint codes but \(C_{m-1}\) shapes. At most one shape per code lacks a larger-offset, smaller-source representative. For C3 the uncovered fraction is at most \(3^{m-1}/C_{m-1}\to0\); the count first forces a collision at size eighteen, much later than the actual size-six witness. C5 counting alone forces none; Antihydra injectivity forbids them. These are equal-size source-family statements. Large C3 trees already descend by §5, so this is not new coverage of the difficult non-descent regime.

For forests with total-depth ratio \(\alpha\in(1,2)\), the exponential shape rate is
\(\exp[\alpha\log\alpha-(\alpha-1)\log(\alpha-1)]\). Its C3 code-capacity threshold is about 1.641794, above the homogeneous growth-critical \(\log_2 3\approx1.584963\). Pure shape counting does not force a collision in the resistant regime. This limitation does not prohibit specific congruence-driven mergers there. [N08-C §4.]

### 7.3 Preserving the original past has an exact price

If a local shift d follows an unchanged prefix U, pulling it back requires original-source shift

\[
d_{\rm original}=2^{H_U}d/P_U,
\quad\text{integral iff }P_U\mid d.
\tag{7.1}
\]

Thus a C5 current-value-minus-four relation cannot preserve even one earlier round unchanged. This is inherited from earlier project merger work, not first discovered in N08. Changing the earlier prefix by a new construction is not ruled out.

For an r-round ordinary prefix and an m-node tree suffix, the strengthened endpoint code is modulo \(c^{r+m}\). In C3 pure counting now needs asymptotically \(m/r>\log3/\log(4/3)\approx3.81884\). But the actual next-tree size after r rounds of a fixed source is at most a constant plus \(2.22390r\), by the source-height bound and first-tree completion bound. More elementarily,

\[
\frac{C_{m-1}}{3^{r+m-1}}\le(4/3)^C(64/81)^r\to0
\]

for a source-dependent C at all permitted next-tree sizes. Therefore waiting for the next tree to become large enough for this particular past-preserving pigeonhole guarantee cannot finish the proof at arbitrarily late times. Specific congruences or changed earlier histories remain possible. [N09 §6.]

### 7.4 Local prime records are not the whole history

For ordinary p = 3 or 5 and constant depth a, use \(D_a(n)=(p-2^a)n+1\). At a switch to b,

\[
(p-2^a)D_b(y)=(p-2^b)D_a(y)+(2^b-2^a).
\]

If \(\nu=v_p(D_a(y))\ge1\), elementary valuation comparison and lifting the exponent give

\[
v_p(D_b(y))\ge\nu
\iff b-a\equiv0\pmod{(p-1)p^{\nu-1}}.
\tag{7.2}
\]

A full a-run of length L followed by the first such b-update contracts by at most \(25/36\) in C3 and \(4/9\) in C5. The old record has \(\nu\ge L\), forcing \(aL+b\ge L+1+(p-1)p^{L-1}\); compare every preabsorption multiplier with \((p+1/3)/2^a\). Overlapping packets cannot have their factors multiplied without a disjoint parse.

A corridor allowing constant depths and record-retaining switches always ends in absorption or a recognized reset. All retaining changes occur by
\(B_p(n)=\max\{m\ge1:(p-1)p^{m-1}\le\operatorname{bitlength}(p(n+1))+2m\}\), with zero if empty. The number of changes is on an \(O(\log\log n)\) scale; total corridor length is at most \(\operatorname{bitlength}(n+1)+3B_p(n)+3\). The final constant-depth run is bounded by its centered reserve. Constructed geometric-depth families \((1,p,p^2,\ldots)\) show unbounded finite retaining complexity across growing sources. Other explicit corridors grow by unbounded factors overall, so finite no-reset completion does not mean net contraction. [N10 §§2–4.]

For Antihydra, \(D_a(n)=(3^a-2^a)n+3^{a-1}\). Given endpoint y, set \(a=1+v_3(y)\). Its maximal backward constant-cost suffix has exactly
\(L_-=\lfloor v_3(D_a(y))/a\rfloor\) phases; reverse reserve multiplication to obtain the entry. At every genuine change a to b,
\(v_3(D_b(y))=\min(a,b)-1\). A selected local record resets while the full arithmetic past remains uniquely recoverable. No erasure premise is needed to explain possible reference-like statistics. [N10 §5.]

## 8. Deterministic statistical mechanisms and decisive negative controls

### 8.1 Genuine traversal would be enough; a reference matrix is not traversal

The ruler sequence \(a_t=1+v_2(t)\) has
\(H_N=2N-s_2(N)\), full geometric marginal frequencies, and exact discrepancy \(-s_2(N)\). Its completed tree sizes are \(1,2,4,8,\ldots\); its canonical E/G groups alternate. It has no adjacent depth-one updates. Thus full random-reference tree and Markov laws are stronger than necessary for mean depth two. The observed raw streams contain many adjacent ones and do not equal this counter. Finite realizations do not authenticate one infinite arithmetic source. [N07 §6.]

For a Markov reference P, stationary \(\pi\), and solution \(h-Ph=f-\pi f\), any deterministic state path satisfies

\[
\sum_{t<N}(f(s_t)-\pi f)
=h(s_0)-h(s_N)+\sum_{i,j}(N_{ij}-N_iP_{ij})h(j).
\tag{8.1}
\]

The identity requires no randomness. A deterministic routing bound would control its last term. Holroyd–Propp rotor routing and Xu's actual counter traversal are documented methodological inspirations; merely writing down P does not supply their hypotheses. For E/G the identity separates weighted routing imbalance, G-reward imbalance, and a bounded endpoint correction. Cancellation may suffice without every individual row having small error. [N07 §7.]

The normalized odd coordinate \(z=(n-1)/2\) gives an actual packet digit rewrite
\(z=r_w+2^{H_w}t\mapsto z'=P_wt+b_w\). Consecutive packets satisfy
\(P_wt+b_w=r_v+2^{H_v}s\). Across all 128 consecutive high quotients t the cap-five output mask is exactly balanced, because P is odd. The actual quotient is fixed, not freshly redrawn. Constant-depth-one runs provide a strong negative control: their odd cores traverse a complete multiplicative residue subgroup while every observed depth remains one. A well-traversed unrelated coordinate is not a fair branch-test schedule. [N08-S §§4–5.]

### 8.2 Two-adic isometric counters, with explicit tail cost

Suppose nonzero integer outputs satisfy
\(v_2(z_t-z_s)=v_2(t-s)\). Each residue modulo \(2^r\) is then visited once per interval of length \(2^r\). For \(a_t=1+v_2(z_t)\), each tail count differs from its geometric reference by less than one. If the largest valuation in an interval of length L is R, the full tail discrepancy \(\mathcal W\) satisfies

\[
L\mathcal W<R+2,\qquad
\left|\sum(a_t-2)\right|<R+2.
\]

The nonlinear counter \(2t^2+t+1\) is an elementary example, since its difference is \((t-s)(2(t+s)+1)\). Fixed exponential families \((uA^t+v)/2^s\), with \(A\equiv1\pmod4\), \(s=v_2(A-1)\), odd fixed u,v, and \(2^s\mid u+v\), also have this isometry. Zero terms are excluded. Rare deep valuations still need a bound. [N08-C §2.]

The fixed-base estimate \(v_2(uA^t+v)=O_{A,u,v}(\log(t+2))\) imports a theorem, rather than following from finite residue balance alone. Chim's Theorem 2.1 supplies logarithmic exponent dependence for multiplicatively independent algebraic p-adic units; dependent fixed rational bases reduce to elementary valuation formulas. The audit checked the theorem's unit and independence hypotheses and printed pp. 297–299. No uniform constant for changing cofactors follows. [Kwok Chi Chim, *Lower bounds for linear forms in two p-adic logarithms*, JNT 266 (2025), 295–349, DOI 10.1016/j.jnt.2024.07.012.]

Fixed-cofactor region-parameter families can genuinely satisfy such constant-or-counter laws. They sample different sources as the region length changes, not consecutive visits of a fixed source. N09 proves why the literal temporal interpretation fails: for positive E-entry cofactors,
\(2^hu'=3^ju+1\) in C3, \(2^hu'=5^ju-1\) in C5, and \(2^hu'=3^{2j-1}u+1\) in Antihydra. Thus \(\gcd(u,u')=1\), and legal E-entry congruences give \(u>1\), so \(u'\ne u\). Coprimality does not imply fairness: arbitrarily long all-A source cylinders retain it while having discrepancy minus their length. [N08-C §2.8; N09 §5.]

### 8.3 Bounded observations do not control sampling or the deep tail

For cutoff R,

\[
\Delta_N/N=\left[N^{-1}\sum\min(a_i,R)-(2-2^{1-R})\right]
+N^{-1}\sum(a_i-R)_+-2^{1-R}.
\tag{8.2}
\]

Even convergence of every fixed finite-depth frequency needs a separate uniform-integrability condition on the excess-depth term to imply mean depth two. Adding a spike of size \(2^j\) at index \(2^j\) in the ruler sequence changes only \(O(\log N)\) entries, preserving every fixed finite-word frequency of the ruler, while producing mean-depth liminf three and limsup four. It is a formal countercontrol, not an authenticated infinite Collatz word. [N08-C §5.]

Root sampling is a different issue. At every node of a complete preorder tree the restarted tree parser sees that node's fringe subtree. Hence all-time cap-R sum is \(\sum_v\min(|T_v|,R)\), between
\(m-1+\min(m,R)\) and \(\sum_{s=1}^m\min(s,R)\), attained by star and unary tree. N09's word
\((1^L,2^{L-1},1)\), L at least ten, has root cap-five mean \((L+5)/(L+1)\to1\) but time cap-five mean \(3-5/L\ge5/2\). Every C3 checkpoint of the finite word exceeds the original source by its homogeneous multiplier alone. Arbitrarily many finite repetitions have source cylinders. A favorable same-horizon time average therefore cannot replace the root-selected descent criterion. [N09 §4.]

### 8.4 Two explicit failed safety mechanisms

First, the actual Antihydra subtree beginning at phase 19, shifted value 7634069 with native credit 23, has 62 nodes and needs six native units; optimal sibling reordering would need only three. Its first two depths are \((6,6)\). The actual source is safe but not greedily resource-optimal. The stronger \(W\)-requirements are thirty versus fifteen. This is an authentic fixed-source counterexample to that optimal-order conjecture. [N09 §3.]

Second, N10 rules out a global linear potential in the seven features
\(1,\operatorname{bitlength}(x),\operatorname{popcount}(x),\text{number of 1-runs},v_2(x),v_2(x-1),v_2(x+1)\).
The required inequalities are \(\Phi(x)\ge0\), \(\Phi(8)\le0\), and
\(\Phi(\lfloor3x/2\rfloor)-\Phi(x)\le2-3(x\bmod2)\).
The exact certificate uses the following nonnegative weights, with \(f(x)=\lfloor3x/2\rfloor\):

| Necessary inequality | x | Weight |
|---|---:|---:|
| \(-\Phi(x)\le0\) | 256 | 13/420 |
| \(\Phi(f(x))-\Phi(x)\le-1\) | 279 | 2/7 |
| Same odd-step inequality | 281 | 5/21 |
| Same odd-step inequality | 285 | 43/84 |
| Same odd-step inequality | 301 | 5/21 |
| \(\Phi(f(x))-\Phi(x)\le2\) | 342 | 1/7 |
| \(\Phi(f(x))-\Phi(x)\le-1\) | 439 | 1/84 |
| \(\Phi(8)\le0\) | 8 | 13/420 |

The weighted sum cancels every feature coefficient and gives \(0\le-1\). The audit independently verified all seven zero sums and the minus-one right side. This is an exact infeasibility certificate for that global linear class, not an impossibility theorem for guarded, nonlinear, relational or macro-level potentials. [N10 §6.]

## 9. What is worth carrying into a paper

### Strong candidates for a self-contained technical contribution

1. **Guarded arithmetic memory:** the strip inverse law, sharp neutral-loop examples, compulsory prefix separation and no-pointwise-free-reduction theorem. The hypotheses are clean and the proofs short enough to audit without the whole research history.
2. **Recovery/region interface:** exact hidden-peak correction, all-shape credit envelopes, bounded-debt grammars, and distinct conditioned references. These turn qualitative safety claims into testable arithmetic obligations.
3. **A rigorously scoped comparative framework:** source cylinders, forward forests, all-shape growth/credit results, endpoint codes, and the price of preserving original source history. Much of the machinery is classical or inherited; the value is their precise integration and the distinctions it enforces.
4. **Negative-results catalogue:** actual nonoptimal scheduling, time/root sampling failure, sparse-tail failure, seven-feature potential infeasibility, unsafe exits after reversible funded histories, and the counting obstruction for preserved ancestry. These exclude explicit avenues rather than merely reporting unsuccessful searches.

None should be advertised as a resolution of Collatz or Antihydra. The potentially publishable mathematical content is narrower, and priority has not been established. A final manuscript should compare these specializations to existing parity coding, accelerated Collatz trees, queue/ladder processes, and constrained lattice-path work before asserting novelty.

### Exact remaining gaps

The decisive unproved step is source-generated closure: a real entrance must constrain its next exceptional valuation, fund all internal prefixes, and re-establish an admissible successor state. The depth-cylinder theorem intentionally permits arbitrary finite choices across changing sources and therefore cannot provide that restriction by itself. A successful route might establish one suitable slope bound, a paid-language exit theorem, a derived counter traversal with controlled resets, a weighted routing bound, or an original-source-owned merger. No theorem presently proves that the actual source always takes one of these controlled alternatives.

Do not conflate the goals:

- C5 escape needs a one-sided upper-depth envelope below \(\log_2 5\), not exact mean two.
- Native Antihydra safety needs every-prefix funding, not merely arithmetic growth or positive net gains.
- Exact reference rate requires mean-depth and addition-correction control.
- C3 convergence needs actual source selection/chronology beyond the proved all-shape inner operations.

### Verification and empirical scope

The research reports generated 200,000-update records in N05, reanalysed them in N06–N08, and generated million-update records in N09. N11 added only 13, 33, and 5 odd rounds/phases, leaving final horizons 1,000,013; 1,000,033; and 1,000,005. N12 and both N13 reports mostly reanalyse those same records. Their numerous comparison counts are overlapping implementation coverage, not independent scientific replications. All source hypotheses were formulated with finite data available; later constants should not be portrayed as preregistered predictions.

This audit obtained and read every report identified above and both N13 ledgers. It did not rerun their archived reproduction packages or regenerate the million-step trajectories. It supplied a separate standard-library verifier that passed normal-form/cofactor checks, small-tree and packet checks, cap-five masks, all odd-affine mask constants, the N10 rational certificate, N13 band matrix certificates, all 19,448 equal-clock eight-step words, sharp loop witnesses and width-five code separation. The proof arguments, not finite tests, support universal scoped statements. The separate files record exact coverage.

## 10. Attribution and source map

### Documented inspiration, direct dependency, and related background

- **Lindley workload reflection:** N11 explicitly credits D. V. Lindley, *The theory of queues with a single server* (1952), DOI 10.1017/S0305004100027638. The arithmetic specialization is deterministic; no stochastic stability theorem is imported to a named source.
- **Ordered trees, critical branching, cyclic forest counting:** N06 onward explicitly credit classical Galton–Watson/Catalan theory and Svante Janson's 2012 survey, *Simply generated trees, conditioned Galton–Watson trees, random allocations and condensation*, arXiv:1112.0510. The tree-count and reference-age formulas here are classical applications or direct elementary derivations, not priority claims.
- **Parity/two-adic coding:** Bernstein and Lagarias, *The 3x+1 Conjugacy Map* (1996), DOI 10.4153/CJM-1996-060-x, is cited as relevant background in N06. The project had already developed its finite affine cylinders. A citation to background does not establish that every generalized-map formula here appears verbatim there.
- **A direct non-elementary input:** Chim's 2025 theorem supplies the fixed-base logarithmic valuation estimate in N08-C. Its role is stronger than analogy and must be named beside that claim. The verified primary PDF is https://tugraz.elsevierpure.com/ws/portalfiles/portal/92346766/1-s2.0-S0022314X24001793-main.pdf .
- **Deterministic counter and endgame methodology:** Chris Xu's *Skelet #17 and the fifth Busy Beaver number*, arXiv:2407.02426v2, is repeatedly identified as inspiration for deriving an actual parameter traversal, counting operations on that traversal, and proving exceptional exits separately. No Collatz conclusion transfers from it.
- **Faithful partial acceleration:** the Skelet #1 work of Shawn Ligocki and Maja Kądziołka is cited for accelerators that certify only covered transitions and retain unknown exits, followed by a separate closed translated-cycle theorem. The reports point to https://www.sligocki.com/2023/03/13/skelet-1-infinite.html and https://discuss.bbchallenge.org/t/skelet-1-is-a-translated-cycler-coq-agrees/166 .
- **Reset renewal:** Ligocki's *Skelet #34 is Infinite*, https://www.sligocki.com/2023/02/02/skelet-34.html , is documented inspiration for proving completion before available credit expires and preserving a successor condition.
- **Deterministic routing:** Holroyd and Propp, *Rotor Walks and Markov Chains*, arXiv:0904.4507, is explicitly credited for local routing mechanisms that yield deterministic statistical control. This is methodological inspiration; the actual arithmetic routing hypothesis remains absent.
- **Context preservation:** Newcomb Greenleaf's *The Chaos Machine Never Halts: a Proof* (1992), https://turbotm.de/~heiner/BB/TM4-proof.txt , is cited for retaining entry direction and neighboring producer information. It is an analogy about adequate state, not a proof dependency of the arithmetic lemmas.
- **Constrained paths and conditioning:** N13-C identifies Banderier and Flajolet's *Basic analytic combinatorics of directed lattice paths* (2002), DOI 10.1016/S0304-3975(02)00007-5, and Banderier et al.'s arXiv:1609.06473 as related frameworks. The report explicitly does not import a general asymptotic conditioning theorem.
- **Antihydra semantics:** Shawn Ligocki's *BB(6) is Hard (Antihydra)*, https://www.sligocki.com/2024/07/06/bb-6-2-is-hard.html , supplies the external driver/counter comparison. The reduction's native-machine correctness should be cited to its proper source, not inferred from phase arithmetic alone.
- **Earlier internal work:** centered affine clocks, the finite word compiler, general same-clock merger principle, original-prefix lift obstruction, finite-potential limitations, and the 7/4 C3 threshold were inherited from the Binary Route, Region Navigation, Creative Closure 08, and earlier audits. N05–N13 should receive credit for their stated specializations and combinations, not for rediscovering those inputs. The read log identifies which predecessors were directly inspected here; further original-history priority belongs in the broader pre-paper provenance audit.

External comparison sources above are documented by the research reports. Only Chim's precise theorem statement was independently reopened in this chapter's audit; a separate bibliography/attribution review may verify the others. None of these citations certifies the missing fixed-source result.

### Exact Library source keys

| Key | Library ID | Report title, abbreviated only here |
|---|---|---|
| N05 | libfile_7388d1bfc1388191baec7625b569b152 | Neutral Strides, Deviation Events, and Recoverable Memory |
| N06 | libfile_6f94cba960148191832f11dd86ad963e | Critical Forests and the Deterministic Bridge |
| N07 | libfile_3b278a4d14cc8191a2813c11e50e8961 | Parser Interfaces, Shape Envelopes, and Deterministic Controls |
| N08-S | libfile_a5082de052808191a213b21eb1dd2ee0 | Sampling Interfaces, Subtree Mergers, and Arithmetic Counters |
| N08-C | libfile_943968303adc8191ae727849c43947e7 | Arithmetic Counters, History Mergers, and Tail Control |
| N09 | libfile_e66b38adf1f4819185a63ad431c088c8 | Hypothesis Tests, Cofactor Turnover, and Source Ownership |
| N10 | libfile_fa0590416ffc81919ee873ebd4f50b2c | Prime Record Resets and Safety Hypotheses |
| N11 | libfile_d6dc469f6a108191bd899788ddd4bc32 | Recovery Packets, Source Deadlines, and Deterministic Queue Control |
| N12 | libfile_250eca26a5ac8191a75a1b209b7a9e47 | Region-Resolved Recovery and Bounded-Debt Grammars |
| N13-C | libfile_cf69ef40231481919ac353ebe1ef1d4a | Conditioned Regions, Reversible Bands, and Exit Hypotheses |
| N13-T | libfile_1491aa6386048191b505732a66a85a43 | Tilted Observers, Arithmetic Memory, and Debt-Funded Mergers |

N13-T ledger: libfile_44d921a74c208191ad16299e4aa15465. N13-C ledger: libfile_8043367d08008191b97ba9c57e12beb8. Full titles and exact creation times are preserved in sources/recent_navigation_read_log.json. No numerical claim is promoted merely because an internal ledger called it a theorem.

## Latest-source addendum: Navigation 14, received 21 October 2026 at 16:33 UTC

**Cutoff and relation to the earlier chapter.** This addendum includes the report *Comparative Navigation 14: Exact band envelopes, bounded ancestry, and all-scale hypothesis audits*, uploaded at 16:33:06.215878 UTC, and its claim ledger and hypotheses file, within the final 16:35 UTC source cutoff. Its report ID is **libfile_04928dec5c4c819194f330055948b6d3**; ledger **libfile_7204afbba5388191b1de47ca559947ce**; hypotheses **libfile_cbd18f3533108191a03b26bdc64d582b**. The declared preparer remains GPT-6 Astra Pro, for Ethan Walker. No later sources are incorporated.

N14 extends the two N13 branches rather than replacing them. It explicitly adopts translation invariance of the debt band, consistent with the small textual correction above. It inherits the width thresholds, the eight-step merger words, the two source-seven contact indices, the width-fifteen C3 path count, and H13-S. Its strongest additional result is a duration-independent bound on **all** possible C5 ancestor sources in a fixed band and fixed endpoint/clock context. The all-scale audit is stronger only in scale coverage, not in chronological horizon. NAV-086–097 distinguish these developments.

### A. Two extremal paths bound every band bridge (NAV-086–087)

Fix a band \([1,B]\), \(B\ge4\), entering debt \(d\), ending debt \(e\), and length \(M\ge1\). Every legal debt edge has increment \(4a-9\), hence lies in \(\{-5,-1,3,7,\ldots\}\). A bridge exists exactly when

\[
e\equiv d-M\pmod4,\qquad e\ge d-5M.
\tag{14.1}
\]

For each proper interior index \(i\), let \(r_i\in\{1,2,3,4\}\) represent \(d-i\) modulo four. Define \(L_i\) to be the smallest integer in this residue class at least \(\max(1,d-5i)\), and \(U_i\) the largest at most \(\min(B,e+5(M-i))\). Attach the prescribed endpoints to both paths. Then

\[
L_i\le D_i\le U_i
\]

for every legal bridge, and both entire bounding paths are themselves legal. The lower bound comes from the maximum possible decrease in the elapsed time; the upper bound comes from the decrease still available before the prescribed endpoint. Rounding to the required residue preserves adjacent differences at least minus five and congruent to minus one modulo four. The end conditions (14.1) close the two paths; \(B\ge4\) ensures each phase has a representative. Their depths \((9+D_{i+1}-D_i)/4\) are positive integers. This proves feasibility and simultaneous, rather than separately attained, extremality. [N14 §2.]

Since

\[
H_i=(9i+D_i-d)/4,\qquad
C/P=\frac1c\sum_{i=0}^{M-1}(\rho/c)^i(2/\rho)^{H_i},
\tag{14.2}
\]

the lower path minimizes the affine offset for C3/C5 and maximizes it for Antihydra; the upper path does the reverse. For any score \(pi-qH_i\), \(q>0\), the upper path has the worst pointwise resource history, and therefore the greatest required initial credit. These are sharp bounds across different guarded sources, not permission to rearrange one source's word. Formula \(\Delta_i=(i+D_i-d)/4\), followed by the general frontier action, bounds completed roots and pending slots too. It does **not** imply identical forest actions for arbitrary alternative paths. The independently written verifier checked 6,614 small legal bridges and 40,919 prefix comparisons; the parameter-wide argument is the proof, not that finite check.

### B. Forward expansion bounds backward source separation (NAV-088)

For two ordinary-map bridges with common clocks and common entering debt \(D_0\), meeting at one arithmetic endpoint, their source difference is

\[
x-x'=\frac1c\sum_{i=0}^{M-1}\frac{2^{H_i'}-2^{H_i}}{c^i}.
\]

If both lie in \([\ell,u]\) and \(t=2^{9/4}/c<1\), geometric summation gives the duration-independent bound

\[
|x-x'|<\frac{2^{(u-D_0)/4}-2^{(\ell-D_0)/4}}
{c-2^{9/4}}.
\tag{14.3}
\]

Thus every fixed C5 band and fixed endpoint/clock context has finitely many possible odd source integers, uniformly in duration. The argument does not work for C3 at this slope. More generally, the ratio for the normalized offset in a fixed-slope band is \(2^\theta/[c\rho^{\theta-1}]\), the reciprocal homogeneous forward growth factor. When it is less than one, bounded prefix-height variation gives a convergent offset bound. This is a deterministic estimate over all permitted paths; it neither presumes nor proves that a named source stays in the band. [N14 §3.]

### C. An exact rational certificate sharpens C5 to at most 22 ancestors (NAV-089–090)

Write \(D=4j+r\), \(1\le r\le4\), and \(X=2^j n\). For C5,

\[
X'=(5X+2^j)/2^s,\qquad s=3\ (r=1),\quad s=2\ (r\ne1).
\]

Backward multiplication over four phases is \(512/625<1\). Let rational functions \(l,u\) on the band satisfy, on **every** permitted edge \(D\to E\),

\[
l(D)\le2^j/5+(2^s/5)l(E),\qquad
u(D)\ge2^j/5+(2^s/5)u(E).
\tag{14.4}
\]

N14 constructed them by rational policy iteration. This audit independently constructs them from lower- and upper-successor policies, sums each eventual cycle geometrically, and then checks every edge inequality directly. Their validity therefore does not depend on trusting either optimization procedure.

| D | l(D) | u(D) |
|---:|---:|---:|
|1|613/113|5565/113|
|2|513/113|23729/565|
|3|433/113|19729/565|
|4|369/113|16529/565|
|5|3178/565|27938/565|
|6|2678/565|23842/565|
|7|2278/565|19842/565|
|8|1958/565|16642/565|
|9|3404/565|28164/565|
|10|14972/2825|24068/565|
|11|12972/2825|20068/565|
|12|11372/2825|16868/565|
|13|20184/2825|28616/565|
|14|18136/2825|4904/113|
|15|82488/14125|4104/113|
|16|74488/14125|3464/113|
|17|136176/14125|5904/113|

For an \(M\)-step bridge \((n,d)\to(y,e)\), write \(d=4j_0+r_0\), \(e=4j_1+r_1\), and

\[
\beta=2^{(9M+r_1-r_0)/4}/5^M,\qquad Y=2^{j_1}y.
\]

Telescoping (14.4) in the backward affine recurrence gives the complete source interval

\[
\frac{\beta(Y+u(e))-u(d)}{2^{j_0}}
\le n\le
\frac{\beta(Y+l(e))-l(d)}{2^{j_0}}.
\tag{14.5}
\]

Its diameter is at most \([u(d)-l(d)]/2^{j_0}\). For width seventeen the maximum over \(d\) is exactly \(4952/113<44\); at relative debt two it is \(21164/565<38\). Odd integers are two units apart, so a query has at most **22** source candidates, or **19** at debt two. The bounds apply to translated positive strips as well. Entering debt, ending debt, endpoint, and clock remain specified; dropping any of that context asks a different inverse question. Arithmetic injectivity below widths nine/seventeen is stronger than these real interval estimates at small widths. [N14 §4.]

A complete inverse algorithm now enumerates the positive odd integers in (14.5), replays each actual recurrence, and rejects any source that absorbs early, exits the band, or misses the final arithmetic/debt state at the specified time. Completeness follows from the proved interval. At width seventeen the number of candidates is bounded independently of time, but each replay still costs \(O(M)\) arithmetic updates with potentially large integers. N14's constructed 256-update example, with a 578-bit input, reports one accepted source among nineteen candidates despite more than \(10^{132}\) possible formal band words. That particular generated example was not independently regenerated here; it is not a named-source orbit claim.

### D. The inherited merger family now has a complete inverse classification (NAV-091)

At endpoint 621583, duration eight, and entering/ending relative debt two, (14.5) becomes

\[
814694289887/1953125\le n\le162943670671/390625.
\]

It contains exactly six odd integers, 417125 through 417135. Exact replay accepts only **417131 and 417135**, the already known N13 pair. For every integer \(t\ge0\), the endpoint progression

\[
Y_t=621583+781250t
\]

has exactly the two corresponding predecessors

\[
417131+524288t,\qquad417135+524288t
\tag{14.6}
\]

in this context. Indeed, the entire inverse interval shifts by \(524288t\), and membership in the finite union of eight-step, total-depth-eighteen word cylinders depends only on the source modulo \(2^{19}=524288\). The base replay decides every shifted candidate; accepted paths stay positive under their cylinder lifts. This is a whole-progression proof, not extrapolation from several tested lifts. [N14 §5.]

N14 reports regenerating the original source-seven trajectory through round 420167 and applying this complete classification at the inherited contact indices 63997 and 420159. The two actual translated bands are respectively 7 through 23 and 4 through 20. The result upgrades “a companion exists” to “these are the only two ancestors in this specified eight-step band context.” It supplies no new contact location or longer trajectory horizon, and still does not pull the companion below original source seven. This audit independently checked the six candidates and progression identity, not the reported 420167-round replay.

### E. A three-way distinction in ancestry capacity (NAV-092–094)

The inherited C3 width-fifteen count is \(N=292366481680>3^{24}\) for 24-step loops from debt eight. Concatenating \(k\) such loops creates \(N^k\) distinct words with clocks \(M=24k,H=54k\), but at most \(3^{24k}\) endpoint-code classes. Some class has at least

\[
\left\lceil(N/3^{24})^k\right\rceil
\]

words. Distinct words cannot have the same full offset: they would have the same exact source cylinder but different deterministic depth sequences. Within one residue class, choose a sufficiently large common odd endpoint in its compatible congruence class; all reconstructed sources are positive and satisfy their exact word cylinders. Taking the endpoint above one excludes absorption. Consequently **possible equal-clock ancestor multiplicity is unbounded in one fixed C3 band**, while the endpoint may depend on \(k\). At \(k=100\) the lower bound is 32. This is an all-\(k\) pigeonhole proof, not an infinite ancestry claim for a particular endpoint. [N14 §6.]

N14 also gives endpoint-sensitive finite examples, all independently reproduced in this audit: endpoint \((91,2)\) has 33 eighty-step ancestors at entering debt two in width fifteen, and 1563 in width seventeen; the entire restricted inverse tree of \((9757,2)\) becomes empty at depth sixteen in width nine and depth seventeen in width seventeen. Exhaustion is only within the stated band. A nonempty eighty-step inverse tree is not an infinite one.

C5, by contrast, has uniformly bounded source multiplicity in every fixed band and fixed clock context, despite admitting mergers. Antihydra remains injective. An additional elementary explanation in the equal-driver-clock case is

\[
P=3^H,\qquad C/P=\frac13\sum_{i<M}(2/3)^{H_i},\qquad0<C/P<1,
\]

because \(H_i\ge i\). Two meeting equal-clock histories would have an integral source difference strictly between minus one and one, hence zero; determinism then identifies the histories. This is an alternative proof of an inherited property, not a new native-safety result. The three systems share the same finite-cylinder reference depth law, so merging or erasure alone cannot explain that law or its realization on a fixed source.

### F. A pointwise original-history obstruction, independent of suffix duration (NAV-095)

Suppose distinct C5 sources share an unchanged prefix of \(r\) rounds and total depth \(H_0\). Their initial difference is a nonzero multiple of \(2^{H_0+1}\), by the exact cylinder. Their suffix-entry difference is therefore

\[
2\cdot5^r k,\qquad k\in\mathbb Z\setminus\{0\}.
\]

If suffix histories have equal clocks, a common final arithmetic/debt state, and lie in a common width-seventeen positive strip with the same entering debt, (14.5) bounds that difference by \(4952/113<50\). But \(r\ge2\) forces its magnitude to be at least fifty. Thus **no such merger can preserve two or more earlier rounds unchanged, regardless of suffix duration**. [N14 §7.]

This is stronger than the earlier obstruction to a particular counting argument: it excludes every suffix in the entire guarded language. It does not rule out changing the earlier word, unequal clocks, wider bands, different source relations, or collective arguments. The width-eighteen real bound exceeding fifty merely removes this particular numerical obstruction; it does not construct a preserving merger.

### G. Every dyadic scale is now covered, but only on the same finite records (NAV-096–097)

For a record ending at \(N\), define

\[
R_N=\max_{i\le N}\Delta_i-\min_{i\le N}\Delta_i.
\]

For every \(m\le N\) and \(\epsilon>0\), both \(U_{2+\epsilon}(m)\) and \(L_{2-\epsilon}(m)\) are at most \(R_N\): each is a discrepancy difference minus a nonnegative elapsed-time allowance. Therefore all dyadic \(\epsilon=1/q\) with \(q\ge R_N/2\) automatically satisfy H13-S on that finite record, since \(R_N\le2q\le2q\lceil\log_2(m+1)\rceil\) for \(m\ge1\). Only finitely many coarser slopes need explicit tests. [N14 §8.]

N14 reports ranges 2006, 2107, and 2918 for C5 seven, C5 twenty-one, and Antihydra respectively. It checks dyadic \(q\) through 512, 1024, and 1024 explicitly; all remaining dyadic values follow from the lemma. The reported 64,001,096 exact two-sided observer/prefix comparisons all pass. Horizons remain **1,000,013; 1,000,033; and 1,000,005**. The earlier chapter's statement that only seven scales were tested describes N13 accurately; this addendum supersedes that finite scale-coverage limit, not its all-time caveat. The record-range lemma does not give a future uniform bound, and all-time H13-S and its conditional consequences remain open. The extended finite-record calculations were not rerun in this audit.

### Assessment, credits, and independent verification

The strongest new publication unit is the combination of pointwise band extremizers, duration-independent C5 source localization, a fully displayed rational certificate, a complete inverse algorithm, and the pointwise ownership obstruction. The C3 repetition consequence gives a useful contrast. These are coherent finite/parameter-wide results with no unproved statistical premise. They still do not supply the source-generated exit and renewal theorem needed for any named infinite outcome.

N14 explicitly credits classical dynamic programming, citing Dimitri Bertsekas, *Affine Monotonic and Risk-Sensitive Models in Dynamic Programming*, arXiv:1608.01393, only as an abstract-level methodological comparison. No theorem from that paper is a dependency of the displayed inequalities. Xu's Skelet #17 and Kądziołka's Skelet #1 remain documented inspiration for separating faithful partial acceleration from a verified exceptional exit/endgame. The affine cylinder, lift, width thresholds, merger witnesses, C3 band count, and H13-S are inherited and should retain their earlier source credit. Historical priority for the new combination remains unestablished.

The self-contained standard-library script `audits/verify_navigation14_audit.py` requires no input data files. Its output, `audits/navigation14_audit_verification.json`, records independently verified rational certificates at eight widths (492 edge inequalities, including all sixty width-seventeen edges), the base and translated eight-step inverse checks, the bridge comparisons, complete C3 finite inverse counts/exhaustions, and a fresh computation of the inherited width-fifteen matrix count. The source archive **libfile_92cc2262f0108191ac187319de09cff9** was identified but not materialized or executed. The long constructed example, source-contact replay, and all-scale million-record comparisons remain report-backed computations. No claim is upgraded merely because the accompanying ledger labels it proved.


\clearpage

# Effective counterexample certificates, automata obstructions, and the native refuter

## 1. Scope, conventions, and headline result

This chapter audits the 21 October 2026 machine/certificate branch, prioritizing the final Pass08 artifact while tracing its mathematical contract back through Pass01–Pass06. It separates theorem, conditional reduction, comparison-system counterexample, finite regression, and implementation claim. All proofs below have been read and checked at the argument level; this is not formal verification in a proof assistant. Selected executable regressions and the final full transition-quotient audit were rerun for this review.

Write

\[
T(n)=\begin{cases}n/2&2\mid n,\\(3n+1)/2&2\nmid n,\end{cases}\qquad
\mathcal C:\quad\forall n\ge1\ \exists t\ge0\ T^t(n)=1.
\]

The shortcut map has the same reaches-1 property as ordinary Collatz. Here a **bad trap** is a nonempty set \(S\subseteq\mathbb N_{>0}\) satisfying \(1\notin S\) and \(T(S)\subseteq S\). A **divergent** orbit means one that is not eventually periodic, hence tends to infinity. Merely being nonperiodic from its initial term is not enough.

The most recent implementation is an explicit deterministic blank-tape Turing machine with **499,710 working states, two tape symbols, and one separate halt state**, making one-cell left or right moves. Its exact proved predicate is

\[
\begin{aligned}
M\downarrow\quad\Longleftrightarrow\quad&
(\exists\text{ all-base automatic bad-trap certificate})\\
&{}\lor\ (\exists\text{ frozen-v1 symbolic recurrent-chart certificate}).
\end{aligned}\tag{1}
\]

Consequently \(M\downarrow\Rightarrow\neg\mathcal C\), and every nontrivial finite positive cycle would cause it to halt. The missing reverse implication is

\[
\neg\mathcal C\ \Longrightarrow\ \text{at least one certificate in (1) exists}. \tag{2}
\]

No source inspected proves (2). The machine is neither a proved full-Collatz-equivalence machine nor a minimal-state machine. Conversely, its specification is not merely “simulate finitely many seeds”: accepted certificates prove an infinite invariant exactly.

**Source anchors.** Final report: Library `libfile_d5a4157b8d9c8191a5baf492cfa97b3e`, “Result,” “Verification and its limits,” and “The mathematical boundary is unchanged.” Final reproduction ZIP: `libfile_a18b1049cbf081919c9ccfbbe6584eef`. The full proof/checker lineage is in source key §12 and the accompanying read log. Historical documents saying that a native symbolic checker is “not yet built” describe earlier milestones, not the current Pass08 state. Conversely, newer compilation does not establish a stronger mathematics theorem than its source contract.

## 2. Exact automatic certification

### Theorem A1. Finite, exact all-base closure checking

For any integer base \(b\ge2\) and finite complete \(q\)-state DFA \(A\), one can decide whether its canonical positive-integer language is a bad trap. Represent positive integers least-significant digit first; canonical words are nonempty and end in a nonzero digit. Noncanonical accepted words have no membership significance.

**Proof.** Nonemptiness is graph reachability followed by a nonzero final digit. If nonempty, a witness has at most \(q\) digits: choose a shortest path to the state immediately before that last digit, removing repeated states. Thus one may also test all \(1\le n<b^q\). Exclusion of 1 is one membership test.

A closure failure is a pair \((n,m)\) with accepted input, rejected output, and either

\[
2m=n\quad\text{or}\quad 2m=3n+1.
\]

The first equation itself forces even input, and the second forces odd input. For the more general branch \(2m=an+e\), with \((a,e)=(1,0)\) or \((c,1)\) and \(c\) a fixed positive odd integer, read digit pairs \((x_i,y_i)\) and update

\[
r_0=e,\qquad r_{i+1}=\frac{r_i+a x_i-2y_i}{b},
\]

allowing a transition only when the numerator is divisible by \(b\). The interval \([-2,a]\) is invariant: its extreme numerators are at least \(-2b\) and at most \(ab\). After \(L\) digits,

\[
b^Lr_L=e+an-2m.
\]

Therefore final carry zero is exactly the arithmetic relation, not a congruence approximation.

Each side stores its DFA state, a positivity flag, and the acceptance bit at the most recent nonzero digit. This last bit, rather than the current DFA acceptance, handles arbitrary high zero padding on the shorter number. Both numbers must be positive. The resulting product has at most

\[
16q^2(a+3)
\]

states. Reachability of a state with carry zero, accepted input and rejected output decides failure. Every actual failing pair has a finite padded expansion and hence a path in this graph; every reported path reconstructs a real failing pair. Exhausting the finite graph proves universal closure. ∎

For C3 the odd product has at most \(96q^2\) states, and the even product at most \(64q^2\). A shortest path to a failure has fewer states than the full graph, so a failure has an input below \(b^{96q^2}\). The native implementation may use the enormously conservative exhaustive integer cutoff instead of graph reachability without changing the predicate. This cutoff is a theorem about finite transducer states, not a guessed trajectory horizon. Blocks \([b^k,b^{k+1}-1]\) contain \((b-1)b^k\), not \(b^k\), integers; the source correctly uses the former.

### Theorem A2. Exact search predicate and cycle coverage

Enumerate \(b+q=3,4,\ldots\), then all eligible pairs, all \(q^{bq}\) transition tables and all \(2^q\) accepting masks, with start state renamed 0. Each level and each check is finite. Hence the no-input search halts exactly when an automatic bad trap exists in some integer base.

Any accepted set contains an orbit avoiding 1. Every nontrivial finite cycle is a finite language in every base and is therefore eventually found. Fairly enumerating all bases is essential: trying all automata in base 2 before moving to base 3 would starve the latter forever.

**What is standard, and what was delivered.** Finite-state carry relations, regular-language Boolean operations, reachability, and recurrence-set soundness are established methods. The deliverable is an explicit canonical/padding-correct checker, quantified bounds, fair closed search, and independently testable native lowering. Existing regular-sanctuary research is acknowledged in the source; the project does not establish priority for the general automaton strategy. The precise distinction is **checker completeness for a proposed DFA** versus **certificate-language completeness for every actual Collatz failure**.

Sources: Pass03 `completeness_routes_audit.md` §§1–2, 9 and `all_base_machine/ALL_BASE_MACHINE_PROOF.md`; Library `libfile_734f7d825644819183a60339ea9db540` and bundle `libfile_6d02905c800c8191b4f11025410fe3b0`.

## 3. Collatz-specific restrictions on automatic traps

### Theorem A3. Dyadic normalization costs at most one state

If \(I\) is a binary-automatic bad trap recognized by a \(q\)-state LSB DFA, then

\[
S=\bigcup_{k\ge0}2^kI
=\{n:\operatorname{oddpart}(n)\in I\}
\]

is a bad trap, invariant under doubling and even halving, recognized by at most \(q+1\) states.

**Proof.** Closure of \(I\) under even halving proves the equality. An odd member of \(S\) already belongs to \(I\), so its odd successor belongs to \(I\subseteq S\); even successors remain in \(S\). If 1 belonged to \(S\), it would belong to \(I\). Add a fresh start state looping on 0 and taking its 1-transition to the original start's 1-successor; thereafter use the original transitions. This skips precisely the initial zeros encoding a power of 2. Simply overwriting the old start's zero edge would be unjustified because that old state might be visited internally. ∎

### Theorem A4. Divergence forces every binary leading prefix

Every divergent C3 orbit has infinitely many members beginning with each specified canonical leading binary prefix.

**Proof.** In a deterministic map on positive integers, a bounded subsequence repeats a state and forces eventual periodicity. A divergent orbit therefore tends to infinity. It has infinitely many odd entries \(u_j\), and

\[
u_{j+1}=(3u_j+1)/2^{a_j},\quad a_j\ge1.
\]

On \(\mathbb R/\mathbb Z\),

\[
\theta_{j+1}=\theta_j+\log_2 3+\epsilon_j,
\quad \theta_j=\log_2u_j\pmod1,
\quad\epsilon_j=\log_2(1+(3u_j)^{-1})\to0.
\]

The omega-limit set \(K\) is nonempty and compact. If \(\theta_{j_l}\to x\), then \(\theta_{j_l+1}\to x+\log_2 3\); hence \(K\) contains the forward irrational rotation orbit of each of its points. That orbit is dense, so \(K\) is the whole circle. Every prefix corresponds to a nonempty open mantissa interval, visited infinitely often by sufficiently long orbit members. This proves topological density, not equidistribution or an effective rate. ∎

### Theorem A5. Automatic enclosure of divergence has quantitative density

If a \(q\)-state binary LSB DFA recognizes a set \(I\) containing a divergent orbit, then

\[
\underline d(I)\ge2^{-q-1}>0.
\]

If additionally \(I\) is doubling-invariant, every aligned block

\[
[aB,(a+1)B),\qquad a\ge1,\quad B=2^{q-1},
\]

meets \(I\). Thus \(\underline d(I)\ge1/B\), and successive members have gaps at most \(2B-1\), with the initial finite boundary treated in the usual way.

**Proof.** Reverse the DFA to a \(q\)-state NFA reading MSB first. By A4, every canonical prefix has some accepted extension. From an appropriate reached NFA state a shortest path to a final state has at most \(q-1\) edges. For each length-\(k\) prefix choose such a completion. The \(2^{k-1}\) resulting integers are distinct and below \(2^{k+q-1}\). For \(m=\lfloor\log_2X\rfloor\), choose \(k=m-q+1\). There are at least \(2^{m-q}\) members below \(X\), giving the stated conservative lower-density bound uniformly between powers of 2. If doubling preserves membership, pad each short accepted completion with MSB-trailing zeros until its extension has length exactly \(q-1\); the resulting number lies in the indicated aligned block. ∎

No exponential determinization cost belongs in this completion-length estimate. A subset construction is needed if one wants to *decide* prefix extendibility of an LSB presentation, which is a different operation.

**Exact search refinement.** Cycle search together with search over normalized, prefix-extendible automatic traps has exactly the original binary automatic search predicate. A trap containing a divergent member satisfies the prefix condition after normalization. A trap without such a member already contains a nontrivial cycle. Discarding all non-prefix-extendible traps without retaining the cycle arm would be an incorrect refinement.

### Theorem A6. Explicit terminating seeds meet every binary leading prefix

For \(j\ge1\), choose a positive odd multiple \(a\) of \(3^{j-1}\), and define

\[
u=(2^a+1)/3^j,\qquad n=2^ju-1.
\]

Then \(u\) is a positive odd integer and

\[
T^i(n)=3^i2^{j-i}u-1\quad(0\le i\le j),\qquad T^j(n)=2^a.
\]

Thus every member of this family terminates. To obtain any chosen binary prefix of length \(\ell\) and value \(v\), let \(h=\operatorname{bitlength}(3^j)\) and choose \(j\) with

\[
v3^j<2^{h+\ell-1}<(v+1)3^j. \tag{3}
\]

Such \(j\) exists by irrational rotation of \(j\log_2 3\). Choose the permitted \(a\) sufficiently large that \(a\ge2h+\ell-j-1\), and put \(L=a+j-h\). Then

\[
n=2^L\frac{2^h}{3^j}-\frac{3^j-2^j}{3^j}.
\]

The correction lies strictly between 0 and 1. The integer gap in (3), magnified by \(2^{L-\ell+1}\ge2^h>3^j\), dominates that correction, proving

\[
v2^{L-\ell+1}<n<(v+1)2^{L-\ell+1}.
\]

This gives the desired prefix. Divisibility of \(2^a+1\) follows, for example, from the elementary lifting identity \(v_3(2^a+1)=1+v_3(a)\) for odd \(a\). The construction may produce huge integers; it is an existence theorem with exact finite certificates, not an efficient uniform bound.

Doubling this terminating seed proves that, for every fixed positive \(v\), the intervals \([v2^k,(v+1)2^k)\) contain terminating numbers at every sufficiently large scale. This does **not** give arbitrarily long consecutive intervals of terminating integers.

### Theorem A7. Every base has terminating prefix coverage

Every canonical prefix in every integer base \(b\ge2\) extends to a terminating seed.

If \(b\) is not a power of 2, \(\log_b2\) is irrational, so the mantissas of the terminating powers \(2^k\) are dense. If \(b=2^r\), use A6 for the binary representation of the prefix value \(v\), yielding \(v2^s\le n<(v+1)2^s\), and multiply by \(2^j\), \(0\le j<r\), to make \(s+j\) divisible by \(r\).

### Corollary A8. A regular trap has a quantitatively substantial complement

If a bad trap has a \(q\)-state base-\(b\) LSB presentation, then

\[
\underline d(\mathbb N_{>0}\setminus S)\ge(b-1)b^{-q-1}.
\]

The complement contains every terminating number. Reverse its complemented DFA, use A7 and the same \(q-1\) completion argument, and count \((b-1)b^{k-1}\) length-\(k\) prefixes. This gives the formula exactly as in A5.

For a dyadically normalized binary trap, the complement is doubling-invariant too. The stronger aligned-block argument applies to it. If the trap also contains divergence, both colors meet every aligned block of length \(2^{q-1}\), and

\[
2^{-(q-1)}\le\underline d(S)\le\overline d(S)\le1-2^{-(q-1)}.
\]

The general-base conclusion must **not** be upgraded to bounded gaps: multiplying by an arbitrary base is not known to preserve trap membership. Nor is binary automaticity automatically preserved as recognizability in an unrelated base.

### Corollary A9. Uniform accepting tails are forbidden

No fixed binary word \(w\), ending in 1, can send every reachable DFA state into the accepting set of a C3 bad trap. Otherwise every LSB word \(uw\), with \(|u|=k\), is accepted. If \(v\) is the value represented by \(w\), this includes the entire interval \([v2^k,(v+1)2^k)\), which eventually contains a terminating seed by A6. In particular a synchronizing word with a productive canonical accepting continuation is impossible. This is more precise than saying that all synchronizing behavior is forbidden.

**Significance and limits.** A3–A9 are a coherent arithmetic/automata package: hypothetical automatic enclosures of divergence must be normalized, prefix-rich and syndetic; actual C3 arithmetic simultaneously makes their complements prefix-rich. It remains entirely possible for two complementary regular languages to have bounded gaps. None of these necessary conditions produces a trap or excludes all traps.

Sources: Pass02 `automatic_bridge.md` §§2–7 and `automatic_density_audit.md` in bundle `libfile_829449ba14f08191805f41cce25e72e8`; Pass03 `collatz_regular_closure.md` §§1–4, Library `libfile_9fb80679d2a08191a5f24551f7204105`; Pass04 `all_base_density_restriction.md`, Library `libfile_932f9b3858848191b5db4942aaeaeef6`.

## 4. Explicitly excluded finite-state memory classes

Put \(z_j=(4^j-1)/3\), \(j\ge1\). Its LSB binary word is \(1(01)^{j-1}\), and

\[
T(z_j)=2^{2j-1}.
\]

Both \(z_j\) and \(2z_j\) terminate. This elementary identity drives several exact exclusions.

### Theorem A10. Popcount-only and normalized commuting memory cannot support a trap

Every positive popcount \(j\) occurs among the terminating \(z_j\). Any nonempty set whose membership depends only on binary popcount therefore contains a terminating member and cannot be a bad trap. No regularity assumption is needed.

Suppose digit actions \(a=\delta_0\), \(b=\delta_1\) commute and the start state \(s\) satisfies \(a(s)=s\). For every reachable \(p=\delta_w(s)\), commuting \(a\) through \(w\) gives \(a(p)=p\). Thus all acceptance depends only on the number of 1s. This excludes normalized commuting actions without requiring permutation transitions.

### Theorem A11. Two involutive digit actions cannot support a trap, even without normalization

Suppose \(a^2=b^2=\mathrm{id}\). Put \(r=b\circ a\), using right-to-left composition. The generated group elements have the forms \(r^k\) and \(r^kb\). Every reachable state is therefore \(r^k(s)\) or \(r^kb(s)\).

Reading \(z_j\)'s word reaches \(r^{j-1}b(s)\), while reading \(2z_j\)'s word \((01)^j\) reaches \(r^j(s)\). Positive powers cover every point in each finite \(r\)-orbit. The first \(q\) terms of each terminating family therefore cover all reachable states of a \(q\)-state automaton. Any nonempty accepted positive language contains a terminating seed, a contradiction to being a trap. ∎

This includes genuinely noncommuting dihedral actions. For example, \(a(x)=-x\), \(b(x)=1-x\) on \(\mathbb Z/m\mathbb Z\), \(m\ge3\), satisfy the hypotheses but do not commute.

### Theorem A12. Two idempotent digit actions cannot support a trap

Suppose \(a^2=a\), \(b^2=b\), without permutation or normalization assumptions. Collapse repeated adjacent equal letters in any canonical positive LSB word. Its state is unchanged. The resulting alternating word ending in 1 is either \(1(01)^k\) or \(01(01)^k\), representing \(z_{k+1}\) or \(2z_{k+1}\). Hence every canonically reachable state has a terminating representative. This is exactly what trap exclusion requires; states reached only by the empty word or noncanonical words need not be covered. ∎

**Unresolved class and countercontrols.** Arbitrary noncommuting permutation actions are not excluded. With start 0 and image-list actions \(a=(0,2,1)\), \(b=(1,2,0)\), the orbit of \(b\circ a\) misses state 2 although that state is reached by input 3. The proposed set accepting only state 2 is not a trap because \(T(3)=5\) is rejected. The counterexample refutes only the claim that the single repunit family covers every permutation automaton.

Similarly, the exact state-to-state Collatz relation need not be strongly connected. On \(\mathbb Z/3\mathbb Z\), digit maps \(a(x)=2x\), \(b(x)=2x+1\) give a normalized permutation presentation in which state 0 records divisibility by 3. A nonmultiple of 3 never maps under C3 to a multiple, so no relation edge enters that state from its complement. The weaker possible route “every state can reach the state of 1” is not refuted, but is unproved in general.

A strongly connected transition graph with self-loops need not be synchronizing: identity on digit 0 and a cyclic permutation on digit 1 is a counterexample. Graph aperiodicity, transition-monoid aperiodicity, synchronization, and commutativity must not be conflated.

**Publication assessment.** A11–A12 are short, clean, independently checked deductions with explicit infinite structural scope, stronger than finite enumeration. They are candidates for a focused lemma package, with novelty still requiring literature review. The inspiration is the elementary one-step-to-power-of-two repunit identity and the normal forms for groups/semigroups generated by two involutions/idempotents, not a newly invented general group theory.

Sources: `collatz_regular_closure.md` §§5–6; Pass04 `noncommuting_memory/noncommuting_group_memory.md`, standalone Library `libfile_0cd944bd1a7081918d27d7efcc2f9c37`.

## 5. Boundaries of density and semilinear reasoning

### Theorem A13. Semilinear traps add no pure-divergence detection

Every infinite arithmetic progression meets the terminating basin: apply Kenneth M. Monks's sufficiency theorem to the merger class of 1. Every infinite one-dimensional semilinear set contains an infinite arithmetic progression. Therefore no infinite semilinear bad trap exists. A nonempty finite invariant set contains a cycle, and every nontrivial cycle is finite. Consequently an exact search over semilinear bad traps has precisely cycle-existence coverage, not general divergence coverage.

Credit: this is an immediate local corollary of [Monks, The Sufficiency of Arithmetic Progressions for the 3x+1 Conjecture, Theorem 1.1](https://monks.scranton.edu/files/pubs/SufficiencyRev4.pdf), not a replacement for or strengthening of Monks's theorem. It must not be applied to arbitrary automatic sets: an infinite automatic set need not contain an arithmetic-progression tail.

Population-level almost-boundedness is likewise not enough. A positive-density forward trap with minimum \(m>1\) is compatible with minima less than every \(f(n)\to\infty\), since every such \(f\) eventually exceeds \(m\). Taking \(f\equiv m-1\) is outside that hypothesis. Density-one finite descent is compatible with descent from almost all trap members into other, smaller trap members; the minimum may lie in the exceptional set. The corpus gives a computable, non-Collatz comparison map with exact even halving and a density-one automatic divergent trap while almost all inputs attain a value at most 3. This is a logical countercontrol, not an application to the exact odd branch of C3.

Source: Pass03 `density_obstruction.md`, Library `libfile_c317b183c20c8191b685bf23a682f0d1`. For the underlying external population theorem, consult [Tao, Almost all orbits of the Collatz map attain almost bounded values, Theorem 1.3 and Remark 1.4](https://arxiv.org/abs/1909.03562). No new uniform stopping theorem is claimed here.

## 6. Rewrite pumping: an exact negative result for a natural enlargement

The mixed binary/ternary string system used here is the published system of Yolcu, Aaronson and Heule. It has boundary symbols / and ., binary symbols f,t, ternary symbols 0,1,2, and rules

\[
\begin{array}{ll}
D:&f.\to .\ ;\ t.\to2.,\\
A:&f0\to0f,\ f1\to0t,\ f2\to1f,\ t0\to1t,\ t1\to2f,\ t2\to2t,\\
B:&/0\to/t,\ /1\to/ff,\ /2\to/ft.
\end{array}
\]

On canonical words /w., the left boundary starts with value 1; f,t apply \(2x,2x+1\), and ternary d applies \(3x+d\). Auxiliary rules preserve value and D implements a shortcut Collatz update. The published termination equivalence is credited to [Yolcu, Aaronson and Heule, An Automated Approach to the Collatz Conjecture, §3.2](https://www.cs.cmu.edu/~mheule/publications/collatz.pdf). The following pumping classification is the corpus's separate deduction.

### Theorem A14. Ordinary context pumping exists iff a nontrivial C3 cycle exists

A finite witness \(s\to^+usv\) is sound for nontermination by context closure, but in this particular system it exists if and only if a positive C3 cycle avoiding 1 exists.

**Proof.** Every rule preserves boundary symbols in number and order, so neither \(u\) nor \(v\) contains a boundary. Blocks not bounded by / on the left cannot use B; blocks not bounded by . on the right cannot use D. Without B, the lexicographic measure (number of binary digits, number of binary-before-ternary pairs) decreases. Without D, use (number of ternary digits, number of binary-before-ternary pairs). Thus every noncanonical block terminates.

Every internal canonical block has the identical digit string at the endpoints \(s\) and \(usv\), because the new contexts have no boundaries. If any such block changes during the derivation, it makes a nonempty exact return. That return must contain a D rule, since A∪B terminates by the second measure, and hence gives a positive number returning after an actual positive number of Collatz steps. The unique canonical value-1 word /. is a normal form, so this is nontrivial. If no canonical block changes, iterating the pump would force infinitely many steps in finitely many noncanonical blocks, contradicting their termination.

Conversely, traverse a nontrivial cycle starting from an all-binary representation. After each dynamic update, normalize with A and B. Their termination and the absence of ternary digits in a canonical irreducible word ensure the unique all-binary representation is recovered. At the end of the cycle the original word returns. This is a pump with empty contexts. ∎

Scattered subsequence comparison is not enough. The verified terminating trace

\[
/t.\to/2.\to/ft.\to/f2.\to/1f.\to/fff.\to/ff.\to/f.\to/.
\]

has interpreted values \(3,5,5,8,8,8,4,2,1\), and /t. is a subsequence of /ft. but not a contiguous context occurrence. Higman-style comparability alone cannot repeat a rewrite inside arbitrary inserted letters. The missing property is transition compatibility with the proposed ordering.

**Significance.** This closes a concrete proposed completeness bridge: implementing this pumping arm adds no existential detection beyond the cycles already covered. It does not rule out stronger recurrence certificates or every use of well-quasi-orders. The assertion concerns the displayed system even on malformed initial words, not just canonical encodings.

Source: Pass04 `complete_refutation_reduction.md`, standalone Library `libfile_2ce24ca25d2c8191910288284b2fd56a`, including the explicit proof and `rewrite_pumping_controls.py`.

## 7. A finite exponential-chart certificate language

The v1 language has signed integer constants, one natural parameter \(k\), addition, subtraction, multiplication, and \(b^E\) for fixed integers \(b\ge2\). Exponents have the syntactically natural grammar: nonnegative constants, \(k\), sums, products and nested fixed-base powers. In particular a subtraction is not admitted inside an exponent merely because one could prove its value nonnegative.

### Theorem S1. Exact normalization is sound, but not complete for semantic equality

Normal forms are integer polynomials in recursively defined atoms: \(k\) and \(b^M\), where \(M\) is a nonempty monomial in lower-depth atoms. If a natural exponent normalizes to

\[
E=c_0+\sum_j c_jM_j\qquad(c_j\ge0),
\]

then normalize its power by

\[
b^E=b^{c_0}\prod_j(b^{M_j})^{c_j}.
\]

Ring operations use exact polynomial arithmetic. Structural induction on expression depth proves preservation of values, using \(b^{x+y}=b^xb^y\) and \(b^{cx}=(b^x)^c\) only for natural exponents. Therefore identical normal forms imply equality at every natural parameter. The converse is not asserted: v1 deliberately misses identities involving base changes or more general exponential arithmetic.

Every atom and monomial is nonnegative and nondecreasing. A chart \(P\) passes the lower-bound check when all nonconstant coefficients are nonnegative and \(P(0)\ge2\); negative constant coefficients are permitted. It then satisfies \(P(k)\ge2\) for all \(k\ge0\). This is a sufficient syntactic positivity criterion, not a general positivity oracle.

### Theorem S2. Exhaustive residue rows certify a genuine infinite trap

A certificate has finitely many nonempty charts \(P_i\). Chart \(i\) supplies a positive modulus \(m_i\), with exactly one row for every residue \(r<m_i\). A row targets chart \(j\) at a nonnegative affine parameter \(at+b\) and proves one identity:

\[
2P_j(at+b)=P_i(m_it+r)
\quad\text{or}\quad
2P_j(at+b)=3P_i(m_it+r)+1.
\]

Their integrality forces the correct even or odd branch. Put \(S=\bigcup_iP_i(\mathbb N)\). Each chart lies above 1, and each natural parameter has its unique Euclidean residue row, so every member's successor lies in \(S\). Thus \(S\) is a nonempty bad trap. Multiple representations cause no ambiguity because each row proves the same trusted deterministic successor.

All validation and polynomial operations terminate on finite mathematical inputs, however expensive. Memory exhaustion, recursion exceptions and user interruption are not successful certificate acceptance. An enumerator can use a fair mathematical search or increasing resource budgets without turning a failure-to-compute into a false theorem.

Every nontrivial cycle is covered by one constant chart per node, modulus 1 and the actual successor identities. The C5 cycle \(13\to33\to83\to208\to104\to52\to26\to13\) is a positive control under its trusted coefficient 5 and is rejected under unchanged C3. The ordinary C3 cycle involving 1 is excluded by the positivity requirement.

### Theorem S3. Finite equational proofs have exactly v1 equality coverage

The native-friendly calculus replaces a trusted sparse normalizer with a finite proof checker. Its equality rules comprise reflexivity, symmetry, transitivity, congruence; ring associativity, commutativity, distribution, units, zero and additive inverse; checked ground signed addition/multiplication; and

\[
b^0=1,\qquad b^1=b,\qquad b^{u+v}=b^ub^v,
\]

with syntactically natural exponents. Separate structural-substitution judgments prove that a term was obtained by replacing \(k\) with a natural term. **A substitution judgment is not an equality axiom.** All premises point backward in a finite proof DAG.

Every equality rule preserves the v1 normal form; induction on proof lines gives the reverse inclusion. For the forward inclusion, structurally normalize a term using finite ring expansion and collection. For a power, normalize its natural exponent to a natural reification, expand natural coefficients into finite repeated sums, split exponents, and evaluate ground powers through repeated multiplication. All operations are finite; intermediate proofs can be enormous. Therefore

\[
\operatorname{nf}_{v1}(E)=\operatorname{nf}_{v1}(F)
\quad\Longleftrightarrow\quad
E=F\text{ has a finite proof in this calculus}.
\]

Canonical term interning makes exact term-ID comparison sufficient for a proof producer. Duplicate term IDs do not create unsoundness; they can only obstruct a noncanonical proposed proof.

### Theorem S4. The native lower witness is exactly v1's lower-bound test

For chart \(P\), the native checker requires a natural term \(U\), a nonnegative integer \(d\), a structural proof of \(U(0)\), and an equality proof

\[
P(k)=(2+d)+(U(k)-U(0)). \tag{4}
\]

Monotonicity of natural syntax immediately proves \(P(k)\ge2\). Conversely, write a v1-accepted polynomial as constant \(c\) plus nonconstant part \(Q\), whose coefficients are positive, and reify \(Q\) as a natural term \(U\). Set \(d=c+U(0)-2\ge0\). Equation (4) has identical v1 normal forms and therefore a finite equational proof by S3. In the other direction (4) preserves nonnegative nonconstant coefficients and gives \(P(0)=2+d\). Thus this native interface neither shrinks nor secretly enlarges frozen-v1 coverage.

The compiled checker uses 22 equality-record kinds and six structural-substitution kinds. It validates the term DAG and recomputes naturalness flags before checking every proof line, all chart lower witnesses and every residue row. Signed literal arithmetic is encoded using positive and negative natural-register parts; no signed arithmetic oracle is needed.

**Attribution and significance.** Recurrent-set nontermination proofs are an established verification method, as in [Chen, Cook, Fuhs, Nimkar and O'Hearn, Proving nontermination via safety](https://discovery.ucl.ac.uk/1455006/1/TACAS14-nontermination.pdf). The project's contribution is the specific restricted exponential language, exact coverage-preserving equational kernel, proof-carrying native serialization, and controlled separation from automata on comparison dynamics. General recurrence-set existence is not effective expressibility in a chosen syntax; relative completeness in other verification frameworks is not a Collatz completeness theorem.

Sources: Pass04 `symbolic_certificates/SOUNDNESS_AND_COMPLETENESS.md` §§2–7, standalone Library `libfile_5ace602808e08191a1b398923eafc682`; Pass06 `native_joint/trace_calculus/EQUATIONAL_NATIVE_CONTRACT.md`, `PROOF_KINDS.md`, `FORMAT.md`, `native_terms.py`, `native_proof.py`, `native_charts.py`, contained in final bundle `libfile_a18b1049cbf081919c9ccfbbe6584eef` and earlier source bundle `libfile_452715f241cc8191a5d83bffb68d1128`.

## 8. Comparison-system strictness and chart limitations

To avoid several reused letters in the wider corpus, call the relevant comparison map

\[
H_{\mathrm{sq}}(n)=
\begin{cases}
n^2,&n=2^{2^j}\text{ for some }j\ge0,\\
1,&\text{otherwise}.
\end{cases}
\]

It is not C3, C5, the signed-word vector-valued H construction, or another clock/receiver map bearing that letter.

### Theorem S5. A one-chart symbolic certificate defeats every automatic base on this control

The chart \(P(k)=2^{2^k}\), parameter update \(k\mapsto k+1\), has \(P(k+1)=P(k)^2\), and the natural witness \(k\) proves the trusted squaring guard. It covers **every** nonterminating seed of \(H_{\mathrm{sq}}\): outside its image the map goes straight to 1.

Every nonempty invariant set avoiding 1 must be a tail of \(\{2^{2^k}:k\ge0\}\). In base \(b\), the representation lengths are

\[
L_k=\lfloor2^k\log_b2\rfloor+1,
\]

whose successive gaps tend to infinity. Any infinite regular canonical language has a nonempty pump on a sufficiently long accepting path, and therefore contains an infinite arithmetic progression of accepted lengths. No such progression fits in \(\{L_k\}\) once its successive gaps exceed the pumping increment. Thus no automatic bad trap exists in **any** integer base.

This proves strict enlargement of the available certificate paradigms **across the stated comparison systems**, not strict extra coverage for C3. Moreover the C3 all-base arithmetic checker itself is not an implementation of this different map. The comparison is between invariant representation/checking methodologies, with system-specific trusted transition checks.

The corpus's later fixed-height and diagonal controls show that the symbolic language is still not universally complete for elementary computable dynamics. The companion chapter `h_obstruction_audit.md` supplies their exact definitions and proofs, including variable-height tower growth, a density-one linear-growth diagonal countercontrol, v1 versus v2 monotonicity distinctions, and the specialized 20-state H verifier. The native 499,710-state artifact remains **v1**, not v2. These limitations must accompany any claim that symbolic certificates “see what automata miss.”

Sources: Pass04 `SOUNDNESS_AND_COMPLETENESS.md` §5 and Library `libfile_cbc079dd451c819193e09eea162e3d7b`; Pass05 `chart_completeness_explanation.md`, Library `libfile_6a714c71b2b8819192a5ba029eb71c8e`, and reproduction bundle `libfile_54fc40d352c0819190d1aca7c3dd4b24`.

## 9. Computability: which quantifiers the construction does and does not remove

### Theorem L1. First descent characterizes full convergence

Let \(D(n,t)\) mean that some \(1\le j\le t\) has \(T^j(n)<n\). Then

\[
\mathcal C\iff\forall n>1\ \exists t\ D(n,t).
\]

Convergence supplies a visit to 1; the converse is strong induction on the source. Hence if C3 fails, its least bad seed never drops below itself. A finite no-descent prefix verifies only finitely many instances of this universal-time obligation.

For \(S_t=\{n>1:\forall1\le j\le t,\ T^j(n)\ge n\}\), let \(m_t=\min S_t\). The set is nonempty: \(2^{t+1}-1\) supplies a sufficiently long initial odd run. Each \(m_t\) is computable by finite search; it is nondecreasing. Then

\[
\neg\mathcal C\iff(m_t)\text{ is bounded}
\iff(m_t)\text{ eventually stabilizes};
\qquad\mathcal C\iff m_t\to\infty.
\]

Indeed an eternal no-dip seed bounds the sequence. If it stabilizes at \(a\), nesting puts \(a\) in every \(S_t\), making \(a\) the least bad seed. No finite stabilization detector follows.

### Theorem L2. Global refutation and seedwise classification are different targets

A blank-tape machine halting iff \(\exists n\) whose orbit never reaches 1 needs only **one** certificate somewhere whenever the bad set is nonempty. It need not classify every bad seed. In contrast, a machine \(D(n)\) halting exactly on bad seeds, dovetailed with ordinary convergence simulation, would decide the entire C3 basin. Conversely a basin decider gives such a seedwise detector. Neither generic undecidability nor the written \(\Pi_2\) formula settles the decidability of this particular fixed basin.

Likewise, the conventional universal-existential formulation of \(\mathcal C\) does not prove that this one fixed sentence cannot have a useful explicitly specified ordinary halting equivalent. The hierarchy excludes a uniform effective reduction of every sentence of the relevant class, not a special arithmetic theorem about this particular sentence. Nonconstructive existence of a program with the right truth value does not identify it. [Calude's 2019 note, Question 1](https://www.cs.auckland.ac.nz/~cristian/collatzproblem.pdf), explicitly asks for the program after recalling such an existence argument; this is background motivation rather than a completed constructive solution.

### Theorem L3. Conditional total first-descent budgets are equivalent to a complete global refuter

Suppose an explicit ordinary \(M\) is proved to halt iff \(\neg\mathcal C\). For input \(n>1\), dovetail \(M\) and the orbit until either \(M\) halts or \(n\) descends, returning the number of orbit steps used. This defines an explicitly total computable \(b(n)\): under \(\mathcal C\), descent occurs; under its negation, \(M\) halts. Under \(\mathcal C\), every \(n\) descends within \(b(n)\).

Conversely, suppose an explicitly total computable \(b\) has the proved conditional adequacy property

\[
\mathcal C\Longrightarrow\forall n>1\ D(n,b(n)).
\]

Test sources in increasing order, halting at the first finite budget failure. Under \(\mathcal C\) none fails; otherwise the least bad seed never descends and must fail. Thus this machine halts iff \(\neg\mathcal C\). The requirement is **unconditional totality plus proved conditional adequacy**, not an arbitrary large empirical budget. A Busy Beaver function is not an available computable subroutine.

### Theorem L4. A finite counterexample-hitting bound gives a truth-side machine

If an explicit \(B\) is proved to satisfy “whenever C3 is false, some bad seed is at most \(B\),” dovetail the trajectories of \(1,\ldots,B\) and halt once all reach 1. It halts iff \(\mathcal C\). No uniform running-time bound is needed, but the hitting theorem is essential and has not been supplied. A source-faithful reduction of every source above \(B\) to a smaller one would suffice by the least-counterexample argument.

### Theorem L5. Proof search is a precise upper envelope, relative to its theory

Fix an effective theory \(F\) capable of proving concrete finite machine runs. Its proof enumerator for \(\neg\mathcal C\) halts exactly when \(F\vdash\neg\mathcal C\). Relevant arithmetic soundness gives halting implies truth; mere consistency is not the same assumption. Truth implies provability remains an additional unproved bridge.

If \(F\vdash(\operatorname{Halt}(N)\Rightarrow\neg\mathcal C)\), then every actual halt of \(N\) yields a finite execution proof in \(F\), and hence an \(F\)-proof of \(\neg\mathcal C\). Thus the proof enumerator covers every actually halting refuter whose soundness is \(F\)-provable. This elementary metatheorem does not prove that C3 is independent of \(F\), nor that a special complete refuter cannot exist. It explains why replacing a specialized checker with generic proof search changes efficiency and language without magically supplying truth-to-provability.

Two useful controls accompany these results. Arbitrarily long all-odd positive prefixes converge 2-adically to \(-1\), not to a positive source; prefixwise positive realizability is not full ordinary realization. Every ultimately periodic parity itinerary of a positive source is eventually cyclic: for a block \((3^sx+B)/2^L\), integrality of all repetitions forces \(2^{Lr}\mid(2^L-3^s)x-B\) for every \(r\), hence the numerator vanishes. Therefore a fixed repeated expanding branch word does not certify positive divergence.

Sources: Pass01 `logical_machine_routes.md` §§1–11 and construction report Library `libfile_528d128a64b88191a0a6503a2e04f7a5`; Pass03 `completeness_routes_audit.md` §§4–6, Library `libfile_734f7d825644819183a60339ea9db540`.

## 10. Native construction and reduction: what the artifact certifies

### Theorem M1. Fair native enumeration realizes exactly (1)

The automatic arm retains the proved all-base search. After every completed automatic rejection, the scheduler checks one symbolic candidate and then resumes the old automatic enumeration. Symbolic candidates enumerate all \((B,C)\), \(B\ge64\), \(C\ge0\), diagonally. Base-\(B\) digits of \(C\) encode term, proof, chart and row records, with enough capacity at sufficiently large \(B\) for any finite certificate. Inactive high digits may be ignored, introducing duplicates but losing no witnesses.

Every candidate check terminates: all record arrays and loops have finite natural bounds; term/proof references point backward; divisors are positive; all arithmetic macros terminate. Therefore no candidate permanently starves the other arm. The two only acceptance exits are automatic certification and actual symbolic certification; syntax-only acceptance or a comparison-system H success cannot trigger a production C3 halt. S3–S4 prove full frozen-v1 coverage of the equational interface.

The untrusted serializer has useful constructive paths and an executable fair exhaustive proof-search fallback. The fallback is complete mathematically but may be astronomical. No practical full-v1 sparse-polynomial proof producer is claimed. This distinction does not affect runtime verifier soundness or existential coverage.

### Theorem M2. The compiler chain preserves blank-tape halting

The source has finitely many nonnegative registers and only INC, DEC-with-zero-test, JUMP and HALT. It is closed and starts with zero registers. Unary blocks separated by delimiters represent the registers on a finite nonblank portion of a four-symbol tape. A marker records the active position. INC shifts a finite suffix to insert one unary cell; DEC tests an empty block or shifts to delete one. Navigation and return scans terminate on the canonical representation. The blank initializer constructs that representation. Each source instruction therefore has a finite, nonzero simulation, and only a source acceptance HALT becomes a native halt.

A fixed two-bit encoding of each logical symbol converts this into a binary tape with blank 00. The optimized compiler permits controlled left/right bit orientations; its finite templates preserve each logical transition. The final chosen symbol map is \([0,2,1,3]\), one of six blank-preserving permutations tested.

Register allocation and return-ABI rewrites preserve source halting with finite stuttering. Crucially, the final nine-bit INC-only calling convention is justified by a global invariant: all return-tag bits start zero; only certified setup/dispatch code accesses them; calls are nonnested; every return consumes all bits; no control edge enters halfway through setup. Therefore 389 calls need only set their one-bits and may omit 3,501 redundant clears. This is not valid for arbitrary dirty-tag states.

Safe transition completion changes only rows formerly targeting TRAP and unreachable under the canonical initialized-register invariant. These rows can still be reachable in the unconstrained control graph or on malformed tapes. The resulting preservation claim is for valid initialized computations, not arbitrary inputs to the modified logical machine.

Finally an exact finite-control quotient supplies a map \(f\) with \(f(H)=H\) satisfying, for every source state and read bit,

\[
\delta'(f(q),a)=(w,d,f(t))\quad\text{whenever}\quad\delta(q,a)=(w,d,t).
\]

The initial state maps correctly and every quotient state has a preimage. Induction on native steps gives identical tapes and head positions, mapped control states, and simultaneous halting. **Only this final quotient is step-for-step**; source rewrites and layout/encoding changes alter timing.

### Frozen counts and evidence

The historical complete-symbolic counts are 1,616,592 → 1,498,101 → 1,007,210 → 517,823 → **499,710** working states. The net reduction from the first complete merged table is 1,116,882 states, approximately 69.09%. The final table is a quotient of 653,205 raw binary states. The selected source has 19,916 primitive instructions and 69 physical registers. These counts include the actual closed search, initializer and necessary control machinery, and exclude the separate halt state.

The earlier 17,259-state automatic-only machine has a weaker certificate language; it is not an equal-coverage competitor. The 20-state specialized H verifier has a different target entirely.

For this review the final quotient auditor was rerun, verifying all **1,306,410 transition equations**, all **999,420 text transitions**, the initial/H bindings, surjectivity and exact text/JSON/packed agreement. The reported source-ABI, register-allocation, canonical-safe completion and compiler tests were read, not all independently reimplemented. The self-contained release records a 10,000-source-boundary full-tape/head replay over 8,114,452 native steps. That finite replay supports implementation correctness; the general simulation invariants, not replay length, establish all-future preservation. Earlier billions-step counts belong to older artifacts and must not be attributed to the final timing-changed table.

Selected literal table SHA-256:
`985131028cee1ca8bf8fd629de20854647e34108c5e8c54504e1695b5a8d9a8a`.

Selected JSON SHA-256:
`f87b708ea0e5fd64546f385cf699a63cd2bf94c20589940dfe080af01c123a66`.

Compact release ZIP SHA-256:
`5c86565afcf6a3f18d9507ab6ecfd26790ed1fb1498c61a0b3492b187d5b421b`.

**Publication assessment.** This is a reproducible proof-checker/compiler artifact and case study in semantics-preserving reduction, not evidence for a conjecture about smallest universal or Collatz-equivalent Turing machines. The meaningful mathematical endpoint is a completely explicit ordinary machine implementing a carefully bounded certificate language. No formal proof-assistant verification of the entire source/compiler is claimed.

## 11. Proposed paper organization and claim triage

The strongest coherent presentation is not “we built a small Collatz machine,” but **finite counterexample languages for Collatz: exact verification, arithmetic restrictions, and controlled expressive separation**.

1. **Main theorem package:** exact all-base automatic checking and fairness (A1–A2), Collatz-specific prefix/density restrictions (A3–A9), structural automaton exclusions (A10–A12). These have fully written arguments and exact scope. Literature novelty is unestablished; the proof package itself is suitable for review.
2. **Negative-methods theorem:** rewrite context pumping adds only cycle coverage (A14), accompanied by the tiny terminating subsequence false positive. This is a concrete diagnostic contribution, not generic skepticism about finite methods.
3. **Certificate-language theorem:** frozen-v1 soundness and equality/lower-bound equivalence with the finite native calculus (S1–S4), plus the exact H comparison separation and chart obstructions (S5 and companion chapter). Distinguish syntactic completeness, comparison-system coverage, and C3 completeness in every theorem statement.
4. **Reproducible artifact:** native 499,710-state implementation with explicit table hashes, complete quotient correspondence and source/compiler proof contracts. Place the state progression and finite regression inventories in an appendix rather than suggesting that state reduction resolves (2).
5. **Conceptual appendix:** logical formulations and conditional reductions L1–L5. These are mainly elementary but useful because they rule out quantifier mistakes and identify what genuinely remains to be proved.

Claims not ready to make: automatic separation for C3; symbolic completeness for arbitrary divergent C3 orbits; strict extra C3 detection beyond automata; a complete or minimal Collatz-halting-equivalent machine; general exclusion of group automata; extending binary bounded gaps to every base; deriving a fixed universal bound from density-one descent or Tao; or identifying a finite last-change detector for \(m_t\).

A useful next mathematical question is the **weak global certificate bridge** (2), not the unnecessarily stronger demand that every bad orbit admit a chart. Any proposed proof must exhibit what special feature of the exact C3 arithmetic defeats the comparison-system obstructions. A useful next verification project is a proof-assistant formalization of the checker and lowering contracts. Either would be qualitatively different from another state-layout sweep.

## 12. Source and credit key

All local Library items below live in “Collatz Notation Transform / Machine Research / Full Collatz Halting Equivalence - 2026-10-21.” Full archive-inner paths, read scopes, local hashes and rerun evidence are recorded in `sources/certificates_machines_read_log.json`; structured claims are in `audits/certificates_machines_claims.json`.

- **Pass01:** `libfile_528d128a64b88191a0a6503a2e04f7a5` construction report; `libfile_d8786c596bd08191b55317b6bd5b1622` source/check bundle. Logical interfaces, first-descent formulations, automatic baseline, semilinear consequences and explicit missing bridge.
- **Pass02:** `libfile_829449ba14f08191805f41cce25e72e8` native/checker bundle; `libfile_e15548538ff08191b6451d13de96358d` report. Dyadic normalization, automatic density/syndeticity proofs, compiler simulation and exact control quotient.
- **Pass03:** `libfile_6d02905c800c8191b4f11025410fe3b0` bundle; `libfile_9fb80679d2a08191a5f24551f7204105` regular-closure proofs; `libfile_734f7d825644819183a60339ea9db540` completeness routes; `libfile_29ebb09fc2a8819193d6414d6602570d` primary comparison audit; `libfile_c317b183c20c8191b685bf23a682f0d1` density obstruction.
- **Pass04:** `libfile_9aa79ba5821c8191a3a17024cb4bfbb8` bundle; `libfile_932f9b3858848191b5db4942aaeaeef6` all-base density; `libfile_0cd944bd1a7081918d27d7efcc2f9c37` noncommuting memory; `libfile_2ce24ca25d2c8191910288284b2fd56a` rewrite pumping; `libfile_5ace602808e08191a1b398923eafc682` symbolic proofs; `libfile_30d4da048c848191af966eb424808e29` joint-search proof.
- **Pass05:** `libfile_54fc40d352c0819190d1aca7c3dd4b24` bundle; `libfile_6a714c71b2b8819192a5ba029eb71c8e` chart-completeness explanation; `libfile_3fa636d9bdcc8191a975929a1d2d182a` specialized H native proof. See companion audit for the precise comparison results and v2.
- **Pass06:** `libfile_452715f241cc8191a5d83bffb68d1128` source/proof bundle; `libfile_c0b2be00e95c8191ab6c0ddb01a26e2b` full-native report. Exact frozen-v1 finite calculus and native integration; earlier implementation status is superseded, not silently promoted into full Collatz coverage.
- **Pass07:** `libfile_a3543a3032cc8191aefbc3801c2c3292` report; `libfile_3eb436c087e48191a887403a01846381` historical checkpoint. Layout, blank-preserving encoding, canonical-safe completion, exact quotient.
- **Pass08:** `libfile_d5a4157b8d9c8191a5baf492cfa97b3e` final report; `libfile_a18b1049cbf081919c9ccfbbe6584eef` compact reproduction. Final ABI invariant, selected table, source/audit chain and portability/replay results.

External credit is differentiated from local proof responsibility: Monks supplies arithmetic-progression sufficiency; Yolcu–Aaronson–Heule supply the mixed-base rewriting presentation; Chen–Cook–Fuhs–Nimkar–O'Hearn supply relevant recurrence-set verification context; Calude supplies an explicitly documented motivating program-construction question. Irrational rotations, finite automata pumping, carry transducers, ring normalization, proof carrying, register simulation and bisimulation quotient are established methods. The corpus also explicitly acknowledges [existing regular-sanctuary research](https://github.com/GettysburgResearch/collatz/blob/main/research/RESULTS_CATALOG.md); that acknowledgment is historical source evidence, not a claim that the current moving catalog has been exhaustively audited here. No mathematical novelty or priority is established by an absence of a citation in these local notes.


\clearpage

# Symbolic recurrence certificates: the squaring control, representation obstructions, and the specialized native verifier

## Audit verdict and attribution

The substantive proofs inspected in the Pass04 symbolic kernel and the Pass05 obstruction and H-machine files are valid within their stated versions and domains. They establish a useful sequence of exact distinctions:

1. A finite recurrent-set certificate can prove genuine unbounded divergence without representing its set by a finite automaton.
2. The fixed-height tower comparison has a single accepted symbolic chart covering every bad seed, but no automatic bad trap in any integer base.
3. The restricted chart language is nevertheless not universally complete, even for total computable dynamics with only linearly growing divergent orbits.
4. The 20-working-state binary H machine exactly checks one solved infinite affine-tower schema. It neither compiles the whole symbolic kernel nor recognizes Collatz counterexamples.

The mathematical content comes from the user's *Full Collatz Halting Equivalence – 2026-10-21* corpus, especially [H1–H9] below. The proofs in this chapter have been independently reconstructed from the full substantive source texts and relevant construction code. Two previously supplied independent audit suites were rerun in separate output directories; an additional focused script supplied 12,778 new regression checks. Those computations support implementation fidelity, not the universal theorems.

The strongest candidate for a self-contained mathematical contribution is the explicit relative-incompleteness theorem with a decidable density-one bad set and increments at most two. The all-base squaring separation and the audited finite checker provide a particularly clear motivating example. No historical-priority or literature-novelty claim is established here. None of these results resolves Collatz.

## 1. Definitions and notation hygiene

Throughout, parameters range over \(\mathbb N=\{0,1,2,\ldots\}\), states of the dynamical systems range over \(\mathbb N_{>0}\), and success means eventually visiting 1. A **bad trap** for a deterministic map \(F\) is a nonempty set \(S\subseteq\{2,3,\ldots\}\) satisfying \(F(S)\subseteq S\). Such a set certifies that every represented starting value avoids 1 forever. It need not coincide with a single orbit.

We distinguish the following maps, even though the corpus sometimes reuses short letters for different objects:

- \(C_c(n)=n/2\) for even \(n\), and \((cn+1)/2\) for odd \(n\), with \(c=3\) or \(5\). Thus \(C_3\) is the shortcut Collatz map. Its reaches-1 property agrees with the ordinary unaccelerated Collatz map.
- Put \(x_j=2^{2^j}\). The squaring comparison is
  \[
  H_{\rm sq}(n)=\begin{cases}n^2,&n=x_j\text{ for some }j\ge0,\\1,&\text{otherwise}.\end{cases}
  \]
  This is the map called **H** in the Pass03–Pass05 automatic/symbolic comparison files and in the native H machine. Its special sequence begins \(2,4,16,256,65536,\ldots\).
- Put \(t_0=2\), \(t_{j+1}=2^{t_j}\), and \(T=\{t_j:j\ge0\}\). The variable-height comparison is
  \[
  G_{\rm tow}(n)=\begin{cases}2^n,&n\in T,\\1,&n\notin T.\end{cases}
  \]
  Its special sequence begins \(2,4,16,65536,\ldots\). In particular \(G_{\rm tow}\ne H_{\rm sq}\): the next value after 16 distinguishes them.
- The diagonal map \(F_{\mathcal L}\) constructed in Section 6 depends on a specified effective list of representation languages. It is neither of the preceding maps.

There are further unrelated uses of H in the larger corpus: the signed-word compiler's vector-valued \(H(n)\), and the guarded even-halving operation \(H(n)=n/2\) in *Creative Closure 09*, Section 1. Neither is \(H_{\rm sq}\). The powers-of-three and dyadically saturated controls in Pass03 also use F and G for other maps. These objects must not be identified merely by letter.

Both comparison maps above are total computable. Membership in \(\{x_j\}\) is decided by checking that \(n\) is a power of two whose positive exponent is a power of two. Membership in T is decided by generating its increasing sequence until reaching or exceeding n, or repeatedly taking exact base-two logarithms and accepting when 2 is reached. Computation can be impractically large without being noncomputable. [H1 §1; H2 §1; H3 §3; H7 “Trusted system and certificate meaning”]

## 2. What the symbolic checker actually certifies

### 2.1 Grammar and finite certificate data

The chart expression grammar consists of integer constants, one natural variable k, addition, subtraction, multiplication, and powers \(b^E\) with fixed integer base \(b\ge2\). Exponents use the smaller **natural-expression grammar**: nonnegative integer constants, k, addition, multiplication, and recursively such fixed-base powers. Subtraction and negative constants are not allowed within exponent syntax. Each expression has finite fixed nesting depth; there is no iteration primitive, variable base, conditional parameter restriction, division, or unverified recursive orbit definition.

A certificate is a nonempty finite list of charts \(P_i(k)\). Chart i has a positive modulus \(m_i\), precisely one row for each residue \(r=0,\ldots,m_i-1\), a target chart j, and target parameter \(at+b\) with \(a,b\ge0\). The row is read with source parameter \(k=m_it+r\). All chart images include **every** natural parameter, not a hidden selected subsequence.

The dynamics selector is an external trusted argument. A certificate cannot choose H semantics while purporting to refute \(C_3\). The source code checks exact field sets, exact integer types, residue uniqueness and exhaustiveness, valid target indices, and natural affine updates. In particular Python booleans and floating-point values are not accepted as integer fields. [H1 §§1–4; H4; H5 “Scope and preservation”; H6 §§1–4]

### 2.2 Exact normalization and soundness

A normal form is a finite integer polynomial in recursive atoms: k and powers \(b^M\), where M is a lower-level nonempty monomial. If a natural exponent normalizes to
\[
E=c_0+\sum_M c_M M,\qquad c_0,c_M\ge0,
\]
then v1 rewrites
\[
b^E=b^{c_0}\prod_M(b^M)^{c_M}.
\]
Ring operations are exact sparse-polynomial operations. A structural induction proves preservation of evaluation: the induction hypothesis handles lower-depth expressions, distributivity handles ring operations, and the displayed exponent law handles powers. Hence identical normal forms imply equality at every natural parameter. This proof is semantic, not an inference from sampled values.

The v1 positivity check requires all nonconstant normal-form coefficients to be nonnegative, then evaluates the normal form at zero and requires the result to be at least two. Every atom and monomial is nonnegative and nondecreasing on \(\mathbb N\). Thus that value at zero is a genuine uniform lower bound, even if the constant coefficient is negative. The empty list of charts is prohibited, so parameter zero supplies an explicit represented element. [H1 §§2–3; H4 “Finite soundness argument”]

For \(C_c\), a row verifies one of
\[
2P_j(at+b)=P_i(m_it+r),\qquad
2P_j(at+b)=cP_i(m_it+r)+1.
\]
Because the target is integer-valued and c is odd, the first identity proves evenness of the source and the second proves oddness. Parity is therefore not an unchecked annotation. For \(H_{\rm sq}\), a natural witness W(t) must satisfy
\[
P_i(m_it+r)=2^{2^{W(t)}},\qquad
P_j(at+b)=P_i(m_it+r)^2.
\]
The first identity proves the guard as well as giving an index; the second proves the trusted successor.

**Theorem 2.1 (recurrent-set soundness).** Every accepted certificate for a trusted supported map F supplies a nonempty bad trap.

**Proof.** Let \(S=\bigcup_iP_i(\mathbb N)\). Positivity gives \(S\subseteq\{2,3,\ldots\}\), and nonemptiness follows from \(P_0(0)\in S\). Given \(n=P_i(k)\), Euclidean division supplies the unique available row \(k=m_it+r\). Its verified identity identifies the actual successor as \(P_j(at+b)\in S\). Thus \(F(S)\subseteq S\); induction on time proves avoidance of 1. Multiple representations of n do not create ambiguity, because every row establishes the same deterministic successor. ∎

One constant chart per node proves every nontrivial finite \(C_3\) or \(C_5\) cycle. This overlaps automatic finite-set coverage, not a newly proved divergent Collatz case. The known \(C_5\) cycle \(13,33,83,208,104,52,26\) is a positive control; its use under \(C_3\) fails actual arithmetic identities. [H1 Theorems 1 and 4]

## 3. A complete symbolic control with no all-base automatic invariant

**Theorem 3.1 (exact H coverage and all-base separation).** The set \(X=\{2^{2^j}:j\ge0\}\) is exactly the set of bad seeds for \(H_{\rm sq}\). It has an accepted one-chart v1 certificate. No nonempty bad trap for \(H_{\rm sq}\) is automatic in any fixed integer base \(b\ge2\). In fact no infinite subset of X is b-automatic.

**Proof of exact coverage.** The identities \(x_{j+1}=x_j^2\) and \(x_j\ge2\) show that every element of X follows a strictly increasing orbit inside X. Every positive integer outside X maps to 1 in one step. If S is a nonempty bad trap, S must lie in X. The set of indices occurring in S has a least element K; closure forces all later indices, so
\[
S=\{x_j:j\ge K\}.
\]
The chart \(P(k)=2^{2^k}\), modulus one, witness k, and update \(k\mapsto k+1\) passes the kernel. Its recurrence follows from
\[
2^{2^{k+1}}=2^{2\cdot2^k}=(2^{2^k})^2.
\]
The normalizer proves this identity rather than trusting an H-specific unproved recurrence axiom.

**Proof of the automatic obstruction.** Canonical base-b representations of \(x_j\) have lengths
\[
\ell_j=\lfloor 2^j\log_b2\rfloor+1.
\]
Writing \(\alpha=\log_b2>0\), we have \(\ell_{j+1}-\ell_j\ge\alpha2^j-1\to\infty\). Finitely many repeated early lengths, possible in large bases, are irrelevant. Suppose an infinite subset of X had a regular canonical representation language. It contains an accepted word long enough to pump a nonempty loop of length d. Pumping this loop gives accepted word lengths \(A+jd\), an infinite arithmetic progression. Once successive allowable lengths differ by more than d, two consecutive sufficiently large terms of that progression cannot both occur among the \(\ell_j\). Contradiction. ∎

This is a separate one-base argument for each b. Cobham's two-base theorem is unnecessary. Leading-zero padding does not help: intersect a padded language with the regular language of canonical representations; least-significant-digit-first conventions can also be reversed or canonically restricted without losing regularity.

The result is a strict separation between **representation classes across comparison dynamics**. It is not a claim that the existing C3 arithmetic automaton has been run with H substituted into its transition checks. The joint-search documentation explicitly states that H does not use the C3/C5 automatic checker. Nor is it a theorem of strictly increased semantic coverage for actual \(C_3\). [H1 Theorems 2–3; H2 §§2–6; H10 “Comparison systems and honest test interpretation”; earlier origin H11 §6]

The H chart cannot transfer to Collatz: every represented value is a power of two. Under \(C_3\) its successor is half the value, not its square, and repeated halvings reach 1. This is a full arithmetic argument, stronger than merely rejecting a foreign label.

## 4. What v2 improves, and what remains incomplete

### 4.1 Prime-base normalization

Version 2 factors every fixed base exactly by trial division. If \(b=\prod_p p^{v_p}\), it uses
\[
b^{c_0+\sum_Mc_MM}=b^{c_0}\prod_{M,p}(p^M)^{v_pc_M}.
\]
Trial division terminates mathematically, produces exact integer factors, and does not use probable primality or floating-point logarithms. Structural induction again proves normal-form soundness.

The old normal form has a fixed recursive interpretation into the new prime-base representation, extended through polynomial operations. Equal old forms therefore have equal new images. An old nonconstant monomial maps to a nonconstant product with nonnegative coefficients; the former sufficient positivity check is preserved, including evaluation at zero. Since all outer certificate checks are unchanged, every certificate accepted by the mathematical v1 checker remains accepted by mathematical v2. This is not a bound on the extra factoring cost on finite hardware. [H5 “Prime-base normalization”; H6 §§1–2]

For example, v2 accepts \(P(k)=4^{2^k}\), witness \(k+1\), update \(k+1\). It recognizes \(P(k)=2^{2^{k+1}}\) exactly; v1 rejects that literal base-four guard. However v1 accepts the rewritten base-two chart describing the identical tail. Thus this example proves an increase in accepted encodings, not an increase in semantic existence coverage.

### 4.2 Quadratic lower bounds

When the old coefficientwise test fails, v2 isolates
\[
P(k)=Ak^2+Bk+C+R(k),
\]
where all coefficients in the remaining nonconstant monomials R must be nonnegative. Its quadratic routine rejects \(A<0\) and \(A=0,B<0\). For \(A=0,B\ge0\), or \(A>0,B\ge0\), the natural minimum is C. If \(A>0,B<0\), the exact natural minimum occurs at \(\lfloor-B/(2A)\rfloor\) or the next integer. Exact integer arithmetic computes the smaller value m; monotonicity of R gives the sound bound \(P(k)\ge m+R(0)\). The minima need not coincide, so this bound is not generally the exact minimum of P. [H5 “Quadratic positivity rule”; H6 §3]

For instance, \(k^2-6k+11\) is certified with minimum 2 but decreases between k=1 and k=2. Consequently the v1 assertion “every nonconstant eligible chart is strictly increasing from k=1” is **false for v2**. The corrected statement is eventual strict increase and unboundedness. If \(A>0\), the quadratic eventually strictly increases; if \(A=0,B>0\), it already does; if \(A=B=0\), a nonconstant eligible normal form has a positive nonempty remainder monomial. Each such monomial is strictly increasing for integer \(k\ge1\), by induction through its positive products and powers. These alternatives prove the corrected statement. The source's update and obstruction audit explicitly make this repair. [H3 “Pass05 version update”; H8 §1]

The positivity checker remains incomplete even on plain polynomials. The fresh control
\[
k^4-2k^3+k^2+2=k^2(k-1)^2+2\ge2
\]
is rejected by v2 because its negative cubic coefficient lies in the remainder. This proves incompleteness of that sufficient positivity rule. It does not prove that the represented range has no alternate certifiable presentation, still less that a Collatz invariant is missed.

The sources do not establish a completeness theorem for equality recognition in v2. The correct supported statement is “equal normal forms imply true equality”; an unrecognized identity is not grounds for unsound acceptance. Overall certificate incompleteness across computable systems follows from the next two sections, independently of whether a stronger equality procedure could recognize additional identities.

## 5. Fixed-height charts cannot capture the variable-height comparison

### 5.1 An explicit fixed-height bound

Set \(E_0(x)=x\), \(E_{h+1}(x)=2^{E_h(x)}\).

**Lemma 5.1.** For every finite expression P in the chart grammar, there are fixed positive integers c and h with
\[
|P(k)|\le E_h(c(k+2))\quad(k\ge0).
\]

**Proof.** Constants and k have linear bounds. To combine child bounds, increase their constants and heights until both are bounded by \(U=E_H(C(k+2))\ge2\). Absolute values of sums or differences are at most \(2U\le2^U\), and products are at most \(U^2\le2^{2U}\le2^{2^U}\). Thus the required family of bounds is closed under the ring operations after at most two extra fixed levels. For a power \(b^Q\), choose an integer \(B\ge\log_2 b\). Increasing C if necessary makes \(BU\le2^U\), uniformly in k. Since Q is natural and \(Q\le U\),
\[
b^Q\le2^{BU}\le2^{2^U}.
\]
This adds only two fixed levels. The finite structural induction completes the proof. ∎

The variable-height sequence eventually exceeds every such bound, even with any fixed index shift d. For \(k-d\ge h\),
\[
t_{k-d}=E_h(t_{k-d-h}).
\]
The inner term eventually exceeds \(c(k+2)\), since the sequence grows at least exponentially in its index. Strict increase of \(E_h\) then proves the assertion.

### 5.2 Image obstruction for both versions

**Theorem 5.2.** No finite union of eligible chart images for v1 or v2 is a bad trap for \(G_{\rm tow}\), even if a separately sound G-transition verifier is supplied.

**Proof.** A bad trap must be contained in T, because all other states map directly to 1; as with H it must be an infinite tail. For v1, a nonconstant eligible P is strictly increasing on \(k\ge1\). If its image lay in T, its kth ordered values would force \(P(k)\ge t_{k-1}\). For v2, eventual strict increase instead gives \(P(k)\ge t_{k-k_0}\) for some fixed \(k_0\) and all \(k\ge k_0\). Both contradict Lemma 5.1 and variable-height domination. Hence every eligible chart image contained in T is constant. A finite union of those is finite and cannot be a bad trap under strictly increasing G. ∎

The argument is not vacuous rejection of an unsupported system tag: it rules out representation before any transition-identity checker is chosen. It also treats invariant **enclosures**, not just exact formulas for an individual orbit. G has no all-base automatic bad trap either, by the same pumping-length obstruction; its representation lengths have gaps tending to infinity. [H3 §3; H8 §§1–2]

### 5.3 A second obstruction independent of the positivity rule

For any finite family with the present residue/affine updates, choose a fixed integer \(L\ge2\) bounding all \(a+b+1\). Because \(k=mt+r\) implies \(t\le k\),
\[
k_{s+1}+1=at+b+1\le L(k_s+1),
\]
so \(k_s+1\le L^s(k_0+1)\). Combining the finitely many expression bounds with this exponential parameter bound yields fixed H,C such that the tracked values are bounded by \(E_H(C(s+1))\). Explicitly, the inner quantity \(c(k_s+2)\) is at most \(2^{C(s+1)}\) after increasing C, which adds only one tower level. A \(G_{\rm tow}\) orbit \(t_{j+s}\) exceeds every such bound. Thus changing the positivity rule alone cannot repair G while retaining these finite-depth expressions and affine updates.

Actual Collatz obeys \(C_3(n)\le2n\) for positive n and hence \(C_3^s(n)\le2^s n\). It therefore lies well below the forbidden growth regime. The G proof is not a growth obstruction to a hypothetical divergent Collatz orbit. [H3 “Independent transition-growth obstruction”; H8 §2]

## 6. The stronger diagonal obstruction: density one and only linear growth

The preceding countercontrol can be dismissed as much faster-growing than Collatz. The corpus's stronger diagonal construction removes that issue. The following abstract formulation makes its exact effective hypothesis explicit.

**Theorem 6.1 (sparse-hole countercontrol).** Let \(L_0,L_1,\ldots\) be a uniformly effectively enumerated list of infinite subsets of \(\{2,3,\ldots\}\), with an algorithm which, given e and a bound B, finds an element of \(L_e\) above B. There is a decidable set \(S\subseteq\{2,3,\ldots\}\) of natural density one, containing 2, and a total computable map F such that:

1. every n in S has \(n+1\le F(n)\le n+2\), and every positive n outside S has \(F(n)=1\);
2. S is exactly the set of bad seeds, and \(n+s\le F^s(n)\le n+2s\) for n in S;
3. no \(L_e\) is contained in S, and no finite nonempty set is a bad trap.

**Proof.** Put \(r_{-1}=1\). Inductively use the supplied search to choose
\[
r_e\in L_e,\qquad r_e>\max\{r_{e-1}+2,2^e,3\}.
\]
Each search terminates. The computable sequence \(r_e\) is strictly increasing, unbounded, and has gaps at least three. Put \(R=\{r_e:e\ge0\}\) and \(S=\{n\ge2:n\notin R\}\). To decide whether n lies in R, generate the sequence until its first term at least n and compare. This halts, proving decidability of R and S. Because \(r_e>2^e\), at most \(1+\lfloor\log_2N\rfloor\) holes lie at or below N, a sufficient bound for density zero of R and density one of S. All holes are at least four, so 2 belongs to S.

For n in S define F(n) to be its least larger S member. No two holes are adjacent, so this member is n+1 or n+2. For all other positive n put F(n)=1. Decidability of S makes F total computable. Induction gives the stated linear bounds, and all outside states reach 1 immediately. Every \(L_e\) contains the excluded value \(r_e\). Finally, a finite nonempty subset of S has a maximum whose strictly larger successor leaves it; a bad trap cannot contain an outside state. ∎

### 6.1 Effective application to the exact chart and automaton families

For a fixed v1 or v2 kernel, enumerate finite expression trees and retain precisely those with a certified lower bound at least two and a nonconstant normal form. Grammar validation and exact normalization/lower-bound evaluation terminate mathematically. The monotonicity proofs above show every retained expression is unbounded. Hence sequential evaluation finds a value above any supplied threshold. The list is infinite, for example because all \(k+c\), \(c\ge2\), qualify. Duplicates do not matter. Nonconstant accepted normal forms cannot secretly denote constant functions, because the proven unboundedness excludes that possibility.

For automata, enumerate every integer base \(b\ge2\) and every finite DFA; intersect with canonical representations of integers at least two. Infinitude is decidable by the finite-state criterion of a reachable directed cycle with an accepting continuation. Canonical encodings guarantee that infinitely many accepted words represent infinitely many distinct numbers. Enumerating accepted canonical words therefore finds a member above any bound.

Interleave these two effective lists, or the union of both v1 and v2 chart lists together with all-base automata. Theorem 6.1 applies.

**Corollary 6.2 (joint representation incompleteness).** For the resulting map \(F_{\mathcal L}\), every surviving orbit diverges with increments at most two and the bad set has density one, but there is no all-base automatic bad trap and no bad trap expressible as a finite union of the specified eligible chart images.

**Proof.** Every bad trap lies in S and is infinite. Any infinite automatic candidate is one of the \(L_e\) and meets R. Any nonconstant eligible chart image is likewise listed and meets R. A finite union of eligible chart images lying in S could therefore use only constants, giving a finite set, which cannot be invariant. Finite automatic candidates fail by the same maximum argument. ∎

The argument also excludes finite unions mixing automatic components and eligible chart components: every component contained in S must be finite/constant, so the entire union is finite. This last formulation is an immediate corollary of the source proof, not a separately discovered Collatz result.

The effective hypothesis matters. This does not enumerate all semantic infinite decidable sets: infinitude and totality are not supplied by a generic finite-program enumeration. The diagonal construction consequently does not contradict the decidability of its own S. It defeats the explicitly enumerable structured families, not all conceivable finite descriptions or proof systems.

The original chart-only diagonal map in [H3 §3A] has a weaker construction than the joint map in [H8 §3]. The stronger conclusion about automatic sets belongs to the **revised interleaved construction**, not automatically to the old F. Likewise a map diagonalized only against v1 must not silently be asserted to defeat arbitrary future kernel extensions. The enumeration must be rerun or include the specified union from the outset. [H8 §§3–4]

## 7. Exact audit of the 20-state H machine

### 7.1 Its entire infinite certificate schema

The native machine fixes \(H_{\rm sq}\) permanently. Its natural fields a,g,c,d,b,h specify
\[
P(k)=2^{2^{ak+b}},\qquad W(k)=gk+h,\qquad\text{next parameter }ck+d.
\]
Every chart value is already at least two. Injectivity of exponentiation over natural numbers makes guard correctness equivalent to \(a=g,b=h\). Squaring correctness is equivalent to
\[
ack+ad+b=ak+b+1\quad\text{for every }k\in\mathbb N,
\]
which holds exactly when \(ac=a,ad=1\). Since all fields are natural, \(ad=1\) forces \(a=d=1\); then \(c=1\), and guard equality forces \(g=1,b=h\). Therefore the universal obligations reduce **necessarily and sufficiently** to
\[
a=g=c=d=1,\qquad b=h.
\]
The accepted charts are exactly the tails \(\{x_j:j\ge b\}\). Constants \(a=0\) cannot pass. The b=0 instance represents the entire bad set of H. This is a complete solution of this particular schema, not just a sound heuristic. [H7 “Exact reduction of the universal obligations”; H9 “Universal certificate proof”]

### 7.2 Encoding and acceptance language

The serialized tape begins
\[
\text{claim}\;\Vert\;1^a0\;\Vert\;1^g0\;\Vert\;1^c0\;\Vert\;1^d0\;\Vert\;\operatorname{pair}(b,h)\;\Vert\;00.
\]
Column i of the paired unary offsets is \((\mathbf1_{i<b},\mathbf1_{i<h})\), for \(0\le i<\max(b,h)\). Equal offsets give only 11 columns; unequal offsets give an asymmetric column. The coefficients are arbitrary unary naturals, not fixed-width flags. The trusted-H claim bit is 0; 1 is rejected, not reinterpreted as a request to select C3.

Thus the exact accepted framed prefix is
\[
010101010(11)^*00.
\]
Nine states check the header; three states distinguish the offset-pair cases; a thirteenth state is a total nonhalting rejection sink. All verifier transitions preserve the read symbol and move right by one. Accepted offset b takes \(11+2b\) verifier transitions. A finite product exploration with an independently specified automaton reached 14 product states and verified the prefix-language equivalence, not merely a sample of offsets. [H7 “Concrete certificate encoding”; H9 “Exact serialization and unbounded equality”]

### 7.3 Blank-tape execution and framing qualification

The preferred full binary table has 20 working states, excluding the separate halting state. Seven initializer states write the span 1010101 moving left from coordinate zero, leaving ones at \(0,-2,-4,-6\), then enter the verifier at \(-7\). The initially blank tape supplies the leading and terminal zeros. The fixed certificate 01010101000 occupies \(-7\) through 3. Eleven verification steps follow, so the machine halts after exactly 18 transitions, head at coordinate 4. The retained 25-state full-cell writer takes 23 transitions. Both counts include initialization and all reject/scanning states; there are no macro moves or externally preloaded nonblank cells.

The verifier is a framed tape-prefix parser, not a strict finite-file validator. Blank extension supplies unwritten zeros; the first 00 pair terminates the certificate; later debris is ignored. For example, written strings 010101010 and 01010101000 produce the same relevant blank-extended prefix, while 010101010001 accepts before the final remote 1. These are not arithmetic false acceptances under the declared framing. A claim of validating all file boundaries or rejecting every truncated encoding would be false. The current source audit correctly states this qualification. [H9 “Framing caveat and adversarial input”]

The fixed blank-tape machine initializes an already known valid certificate and always halts on that one stipulated configuration. Its substantive infinite checking behavior resides in the reusable verifier on other framed inputs. It is not an exhaustive search for unknown invariants, not a compilation of arbitrary expression normalization, and not a 20-state reduction of the 17,259-state historical C3 automatic search. Its claim-bit rejection checks system binding; the separate halving-versus-squaring proof establishes actual C3 non-transfer. No minimality theorem is claimed.

## 8. Quantifiers, limitations, and paper-ready claims

The certified global refutation predicate is of the form
\[
(\exists A\;\operatorname{Auto}_3(A))\;\lor\;(\exists C\;\operatorname{Chart}_3(C)).
\]
Soundness implies that acceptance refutes Collatz. Full global equivalence needs the converse implication: **if any positive Collatz counterexample exists, some accepted C3 certificate exists**. It does not require every divergent orbit or every bad seed to have a chart. A seedwise recognizer instead needs, for each bad seed n, a certificate containing n or finite checked entry evidence leading from n to a certified trap. These are different quantifier strengths. [H3 §6; H10 “Exact predicate” and “Soundness for Collatz”]

No inspected proof establishes either C3 completeness statement, no nontrivial accepted C3 chart is exhibited, and no theorem here shows that C3 charts necessarily reduce to finite cycles. The comparators neither prove nor disprove possible completeness for the exact Collatz arithmetic. They refute a generic inference from “finite orbit-generating algorithm,” “unbounded divergence,” or even “slow growth” to representability in these certificate languages.

The mathematical checker terminates on finite valid syntax with unbounded exact resources. The Python implementation may fail from recursion limits, large-integer formatting, expansion, factoring cost, time, or memory. None is acceptance. A proof of a native or fair-search implementation must separately preserve the mathematical acceptance event and enumeration coverage. A successful 18-step H run does not discharge those tasks.

Recommended paper claims, ranked by strength of current support:

1. **Theorem-level:** exact soundness of the specified v1/v2 recurrent-chart kernels, complete nontrivial-cycle coverage, and preservation of old acceptance under v2.
2. **Theorem-level:** a one-chart symbolic certificate covering every H bad seed, with no automatic bad trap in any base; present it as a matched expressiveness separation, not a Collatz advance by itself.
3. **Theorem-level:** variable-height obstruction and the stronger effective sparse-hole theorem, including density-one bad set and linear growth. The latter deserves a clear standalone statement and proof, with its language-relative hypothesis prominent.
4. **Artifact-level:** the 20-state, two-symbol specialized H verifier and complete blank-tape trace. Its solved schema and advantageous paired-unary encoding should appear in the abstract or theorem statement, not be relegated to fine print.
5. **Not established:** full Collatz halting equivalence, semantic v2 improvement for C3, minimal state counts, universal mathematical-proof incompleteness, or historical novelty of these constructions.

The core recurrent-set idea is established program-verification methodology. Chen, Cook, Fuhs, Nimkar, and O'Hearn explicitly develop closed recurrence sets and nontermination via safety; their paper should be credited for that conceptual lineage, not cited as a Collatz completeness result. Chatterjee, Goharshady, Novotný, and Žikelić provide a different program-reversal approach with relative completeness under its framework. Neither transfers completeness to this restricted expression grammar. [External references below]

## 9. Reproduction record and sources

### Re-executed and fresh checks

The original corpus files were not modified. Archive byte comparisons matched the substantive Pass05 proofs, kernel, and native construction. Two test/audit scripts differ from their Library-bundle copies only by inspected portability path rewrites; their algorithms are unchanged.

- The supplied independent H audit was copied to a separate audit output directory and rerun. It passed: 20-state/18-step and 25-state/23-step blank runs; 14-state product-language proof; 61,250 natural-field tests; 131,071 arbitrary finite written tapes; and five large-offset tests, including equal offset 10,000 in 20,011 verifier steps.
- The supplied independent v2 audit was copied and rerun against the original frozen kernels. It passed: 1,999 factorizations; 10,712 exact quadratic minima; 3,040 lower-bound expressions; 1,500 normal-form evaluations; 4,000 substitutions; 120 accepted old-certificate variants; and the documented adversarial controls.
- A fresh focused audit used a new literal-table parser and simulator, verified the live native tables against the audited snapshots, reproduced H dynamics on 1 through 1,000, checked base-four acceptance versus base-two semantic rewriting, checked the v2 monotonicity correction and remaining positive-quartic rejection, and checked 11,664 affine-field combinations. Total: 12,778 checks.

The principal source hashes are:

- v1 checker: `8b7201acef5be4a8b10e531c6ca22896036c949b2160ecb404dccfa957fdb15f`.
- v2 checker: `679a828a73228f6f17198157113a515c6b49efb6f01c77416e2d31707df36966`.
- 20-state H literal table: `2e8cceb3e370c04b7ffb835844f89cb50a24d7aabfc8e1b4161f6ae003e55ed6`.

### Local source key

These are user-supplied corpus artifacts, not external peer-reviewed publications. The companion source manifest records exact Library file IDs, bundle membership where checked, SHA-256 hashes, and read scope.

- **[H1]** Pass04, `symbolic_certificates/SOUNDNESS_AND_COMPLETENESS.md`, all eight sections. Also exported as `Native_Machine_04_Symbolic_Certificates_2026-10-21.md`.
- **[H2]** Pass04, `Why_Symbolic_Certificates_See_What_Automata_Miss_2026-10-21.md`, all sections.
- **[H3]** Pass05, `chart_completeness_explanation.md`, Sections 1–7 and the Pass05 update.
- **[H4]** Pass04, `symbolic_audit/INDEPENDENT_AUDIT.md`, together with the full v1 `symbolic_chart_checker.py` inspected through the complete v2 source and exact v1/v2 diff.
- **[H5]** Pass05, `symbolic_v2/SOUNDNESS_V2.md`, entire text and full v2 checker source.
- **[H6]** Pass05, `symbolic_v2_audit/INDEPENDENT_AUDIT.md` and `audit.py`, entire files.
- **[H7]** Pass05, `H_machine/PROOF_AND_SCOPE.md`, `build_and_test.py`, `machine.tm`, and certificate encoding files; full proof and construction source.
- **[H8]** Pass05, `obstruction_audit/INDEPENDENT_AUDIT.md`, all five sections.
- **[H9]** Pass05, `H_audit/INDEPENDENT_AUDIT.md`, `audit.py`, snapshots, and audit results; full proof and independent source.
- **[H10]** Pass05, `joint_search_v2/PROOF.md`, full proof, especially the trusted-system, comparison, and exact-predicate clauses. Historical state-boundary statements are time-stamped Pass05 claims, not assertions about later Pass06–Pass08 progress.
- **[H11]** Pass03, `completeness_primary_audit.md`, full text, especially Section 6 as the earlier source of the all-base H obstruction.

### External conceptual references, checked 21 October 2026

- Hong-Yi Chen, Byron Cook, Carsten Fuhs, Kaustubh Nimkar, and Peter O'Hearn, *Proving nontermination via safety*, TACAS 2014; especially the recurrence-set definitions in Section 2. [Author-hosted primary paper](https://discovery.ucl.ac.uk/1455006/1/TACAS14-nontermination.pdf).
- Krishnendu Chatterjee, Ehsan Kafshdar Goharshady, Petr Novotný, and Đorđe Žikelić, *Proving Non-termination by Program Reversal*, arXiv:2104.01189 (2021). The abstract's relative-completeness claim is framework-specific. [Primary arXiv record](https://arxiv.org/abs/2104.01189).


\clearpage

# Literature, intellectual lineage, and provisional originality assessment

## 1. What is being credited

This pre-paper concerns an AI-assisted research programme directed by Ethan Walker. Its organizing questions, technical deductions, borrowed theorems, computational artifacts, and later literature comparisons are not interchangeable kinds of contribution. We preserve those distinctions rather than attach a single name to every statement in a branch.

A result may be correct without being new; useful without proving Collatz; independently reconstructed within this review without having received independent human peer review; or inspired by an informal question whose proposed mathematical answer later proves false. Generous attribution means retaining all these relationships accurately.

The accompanying `audits/attribution_ledger.json` separates:

1. **Direct user evidence:** exact conversation messages preserved in the research record.
2. **Documentary origin evidence:** a contemporaneous report explicitly identifying an idea or priority as the user's, sometimes preserving a quotation. These are distinguished from a fresh reading of the original conversation.
3. **Direct mathematical dependency:** an external theorem actually used, with its hypotheses and scope.
4. **Documented adaptation or inspiration:** a report explicitly says it followed a source or modified its mechanism.
5. **Related work:** a relevant comparison found in this review, without evidence that it historically inspired the project.
6. **Unknown provenance:** the origin was not located. This is not evidence of independent invention.

The reference labels below identify entries in `sources/primary_bibliography.json`. Each entry records author, title, date or date uncertainty, URL, associated claims, what it supports, and exactly how much was inspected. Original research, author surveys, books, software repositories, community proof records, and project notes have different evidentiary roles. The filename “primary bibliography” does not mean that every included lead was read in full or that every item is an original research article.

## 2. Documented contributions to the research direction

### 2.1 Ethan Walker's questions and priorities

There is direct conversation evidence for four important machine-research decisions. Walker requested a machine for the **full conjecture**, drawing on the Library rather than merely simulating a supplied starting number. He then requested both state reduction and detection of every counterexample, expressly prioritizing the latter if the goals conflicted. He proposed integrating the symbolic checker with the Collatz machine, describing this as merging the programme's ideas. On 21 October 2026, at 15:32:39 UTC, he requested continuation of the reduction iteration until a reasonable stopping point.

These support credit for the originating brief, priority ordering, synthesis, and continuation criteria. They do not establish that a completeness theorem has been proved, that state minimality is known, or that the user originated the general theory of nontermination certificates. Earlier message timestamps are not supplied by the retained evidence and are not reconstructed from file dates. The exact message identifiers and wording are preserved in attribution records A01–A04.

Older reports provide additional documentary, rather than freshly recovered conversational, evidence:

- **Sorting and division surplus.** Notation Transform 06, dated 7 October, explicitly calls the user's sorting intuition its origin. It records discussions at 10:32, 10:42, and 11:03 CDT. The intuition that maximal division should dominate multiplication motivates a research question, not a universal inequality already proved.
- **Alternation and fairness.** FP02, dated 8 October, attributes to the user the proposed bias-erasing effect of multiplication, addition, and maximal division. Subsequent finite-ensemble and chronological analyses test and qualify that proposal. An erroneous universal version should not be credited as a theorem or erased from the intellectual history.
- **Survivors versus an integer.** The 12 October UTC survivor-intersection checkpoint explicitly identifies the user's insistence on distinguishing vanishing fractional survivor populations from the continued survival of one actual integer. This priority remains central to the pre-paper's quantifier discipline.
- **Complete GDR accounting.** The 14 October foundation records the user's request to understand growth, division and residual contributions together, rather than assume fairness or demand compensation from a selected local event.
- **Summability and integration.** The 20 October arithmetic-budget report explicitly develops the user's summability/integration direction. The inspiration and problem formulation are credited separately from Tonelli's theorem, finite flow duality, and existing orbit-sparsity inputs.
- **Arithmetic generator and observer.** The 20 October machine-direction report attributes to the user the shift from superficial state-count comparisons toward the arithmetic driver, the resource coordinate and the halting observer. This motivates the controlled Antihydra comparisons; it is not a theorem that five-state and six-state machines obey different universal laws.

The precise Library identifiers, report paths and passage anchors appear in A05–A10. These credits should remain in any shortened publication. Conversely, absent documentation, the report does not assign Walker every intermediate conjecture or proof trick in a model-generated note.

### 2.2 Internal research lineage

Later reports often complete or correct earlier ones. Research15's golden-rotation handoff explicitly identifies Research11 as an earlier proposal of the target; Research15 should not receive sole credit for originating that target. Shortcut15 acknowledges an external clean-window mechanism and changes its growth constant. The October15 GDR notes already derive reciprocal summability from classical spatial sparsity, so a later synthesis must not present that deduction as newly discovered on October21.

Signed model names and audit labels are retained as provenance of the research artifacts, not represented as external referees or human coauthors. A publication must separately determine responsible human authorship and disclose AI assistance appropriately. Repeated summaries of a theorem do not constitute multiple independent validations.

## 3. The core mathematical lineage

### 3.1 Finite arithmetic and the population/trajectory distinction

Terras's 1976 Theorem1.2 and Corollary1.3 establish the finite parity-vector/residue correspondence; Everett receives the classical independent co-credit. Terras's 1979 clarification addresses the density argument. Bernstein and Lagarias place this arithmetic in a 2-adic conjugacy framework [L01–L04]. These are foundations for the project's exact cylinders, parity-word injectivity, affine compositions, and residue realizers, not new project theorems.

One must distinguish existence of a finite word realizer, a compatible 2-adic infinite sequence, and realization by one positive integer. The reverse rationality/periodicity assertion is not a consequence of writing down a conjugacy. Kontorovich–Lagarias explicitly distinguish stochastic models from the deterministic problem [L05]. Tao's almost-bounded-values theorem applies to almost all sources in **logarithmic density**, with any prescribed bound tending to infinity; it is not a theorem that every source reaches a common fixed bound [L06]. These limitations govern the Region, FP, GDR and recent-navigation interpretations throughout this pre-paper.

### 3.2 Orbit sparsity: García–Tal, Heppner, and Sharpe

García and Tal's 1999 paper is a decisive antecedent [L07]. Its Lemmas1–3 transfer a collision argument into arbitrary translated intervals. Their equation(6), using a stopping estimate credited to Heppner [L08], bounds equal-time collision-free sets by a logarithmic factor times a power strictly below one. Corollary1 includes infinite orbit value sets. This is stronger information than the qualitative statement “Banach density zero.”

For the project, the immediate consequence is elementary: a bound of the form
\[
\#(O\cap[a,a+X))\le K\log(2X)X^{1-\eta},\qquad \eta>0,
\]
with uniform constants yields reciprocal summability by dividing the positive axis into dyadic shells. **Banach density zero by itself would not justify that inference.** For an injective orbit, summing over distinct values equals summing over time. For a cycle, summing distinct cycle values is finite while summing repeatedly visited values over all time diverges. This distinction must be preserved.

Michael Sharpe's repository supplies a newer elementary finite-packing proof and Lean formalization, explicitly acknowledging García–Tal and a public MathOverflow derivation [L09,L12]. The project's use of his packing, defect-height and mechanical machinery must credit him by name. The original source's packing estimate uses the bases8,216 and243; later changes in a tail estimate or logarithmic envelope are refinements of that mechanism, not ownership of it. The pinned `OrbitPacking.lean` source was inspected at commit `ec8174b567d5cab4960024782210b5f5db02bd3a`; the external Lean project was not rebuilt here.

### 3.3 Exactly what the quantitative refinements add

Three mathematically different statements must not be conflated.

**Uniform spatial windows.** The October15 GDR calculation obtains
\[
\#(S\cap[a,a+X))\le18(\lfloor\log_2X\rfloor+1)X^{39/40}
\]
for a synchronous-collision-free set. Its proof explicitly substitutes an elementary parity-binomial-tail estimate for unspecified stopping constants, then uses García–Tal's translated-window argument. It is a transparent quantitative instantiation of an established mechanism. It is not a newly discovered type of orbit sparsity.

**Chronological maximum height.** The legacy entropy argument samples an index from an actual prefix of \(M\) distinct states, injects its future parity words into words of length \(r=\lceil\log_2(H+1)\rceil\), and retains the overlap boundary cost. With empirical odd proportion \(p\), it obtains
\[
\log_2 M\le r\,h_2\!\left(p-\frac{r-1}{2M}\right)
\]
when the argument of \(h_2\) is at least one half. The distinct-odd harmonic correction gives \(p\ge\log_3 2-o(1)\). Consequently
\[
\liminf_{M\to\infty}\frac{\log H_M}{\log M}
\ge \frac1{h_2(\log_3 2)}=1.0526808586079714\ldots.
\]
This is a **prefix maximum**, not a lower bound for every last iterate. Its occupation extension has an explicit reentry-boundary cost, so it cannot simply be asserted as a uniform translated-window exponent.

**Prior-art assessment.** Parity injection, entropy subadditivity/binomial tails and collision-free counting are classical ingredients. Rozier's Lemma2.5 and Theorem2.6 explicitly supply the distinct-odd harmonic-correction antecedent [L49]. García–Tal's stated constants do not immediately identify the exact chronological exponent above, but that does not establish its novelty. A short finite reformulation or an optimized constant may be worth publishing if its exact increment over prior work is made clear. The proper current label is **candidate quantitative reformulation, priority unresolved**, not “new entropy barrier.”

A further lead must remain visible: Michael John Curry's 2026 work is attributed by a related author's repository with an explicit uniform exponent approximately0.9653844 [L50–L51]. Its original DOI and record were inaccessible in this audit. We neither import its theorem as verified nor suppress it when discussing originality of our weaker39/40 bound. The source must be obtained before claiming a best-known quantitative window estimate. The related repository's own occupation and moving-anchor assumptions are expressly open, not external solutions to the project's arithmetic frontier.

### 3.4 Mechanical words, arbitrary-width rotations, and return words

Sharpe's mechanical classification uses words
\[
 b_t=\lfloor(t+1)\gamma+\rho\rfloor-\lfloor t\gamma+\rho\rfloor.
\]
Its interval width is tied to the rotation slope. The manuscript classifies globally mechanical positive itineraries and proves that an eventually mechanical itinerary reaches one [L10]. This covers the corresponding slope-tied golden and silver special cases. It does **not by definition** cover every coding
\[
 b_t=\mathbf1_I(\{t\theta+\rho\}),\qquad |I|=\beta,
\]
where \(\theta\) is the golden rotation and \(\beta\) is arbitrary and independent of \(\theta\).

The project's repaired arbitrary-width golden theorem therefore has a genuine scope distinction, but its historical originality remains unresolved. Akiyama–Shirasaka is relevant rotation/substitution literature [L52]; the final project proof must not be advertised as a consequence of an earlier overbroad substitution claim. An exact geometry verifier checks finite identities and endpoint conventions, not universal publication priority.

Likewise, the Research39 correction respects Durand's return-word convention: start-to-start return words form a code, not necessarily a prefix code [L53]. The project explicitly tests the failure and derives a changed-alignment formula. Its later rank-two closure statement remains conditional on common frequency, distortion and alignment-height assumptions. Finite rank or linear recurrence alone is not asserted to verify these assumptions.

### 3.5 Existing merger and gate theorems

Hercher's Lemma9 gives the precise lower-source common-future identity used by the programme; Remark10 already applies it to a least unbounded source [L13]. Hercher's separate cycle bound must not be confused with this lemma's general applicability. The project's graph composition, path accounting or receiver construction may add a useful organization, but the primitive merger and its least-source use are not new.

Kenneth M. Monks's sufficient-progression work and the four-Monks sufficient-set paper supply the appropriate residue-gate background [L14–L15]. In particular, Corollary5.8 and the later strong-sufficiency statements have different target sets and scopes. These are exact structural results, not permission to assume a hypothetical orbit samples all residue classes with their population frequencies.

### 3.6 Diophantine and analytic inputs

Chim's two-p-adic-logarithm bound and Yu's logarithmic-form work are external tools, not project discoveries [L17–L18]. The present audit retrieved Chim's primary metadata and abstract but not the full theorem; the historical application checks therefore remain separately labeled. The Antihydra audit inspected the rational Yu formulation in Faye–Luca–Ziegler, including the actual hypotheses, before specializing constants [L19]. A citation to Yu's title alone would not suffice.

Fixed-event and fixed-dictionary arguments use fixed-dimensional Subspace/S-unit machinery. Evertse–Schlickewei–Schmidt give a bound on nondegenerate solutions in fixed multiplicative rank and dimension; this is not a general bound on solution heights or an estimate uniform in a growing number of terms [L20]. Bell–Diller–Jonsson–Krieger provide useful exact formulations inspected in the comparison work [L21]. The project-specific contribution, if correct, is the particular affine ledger, handling of zero clusters and quantifier discipline, not a new Subspace Theorem.

Closure comparisons also acknowledge Christol–Kamae–Mendès France–Rauzy, Adamczewski–Bell, and Shmerkin–Solomyak [L30–L32]. Their automatic/algebraic, Mahler, and small-coefficient-series constraints apply to specified classes. None supplies an unrestricted Collatz bridge merely by analogy. Fernández-Duque–Weiermann and Dershowitz–Manna provide canonical-domination and well-founded-order context [L33–L34]; a proposed Collatz rank still needs actual decrease on every relevant transition.

### 3.7 Flow, recurrence certificates, and machines

Gale's theorem is explicitly a finite-network theorem [L16]. It supplies the feasibility/cut interface, not the arithmetic inequalities demanded by the project's source rows. Passing to countably many rows requires the stated compactness/tail conditions. The project cannot credit itself with max-flow duality or credit Gale with proving its open Collatz budget.

Cobham and the automatic-sequence literature supply rigidity for representations in independent bases [L22–L23]. Recurrence-set and program-reversal approaches supply established ways to certify nontermination [L24–L25]. Relative completeness in a rich semantic setting is not completeness of this project's finite automaton, automatic-set or symbolic-chart syntax. The explicit separation examples are potentially useful precisely because they state which syntax fails. Creative07’s instruction-language obstruction uses the classical semilinearity theorem of Parikh, with a modern automaton formulation by Esparza–Ganty–Kiefer–Luttenberger [L54–L55]; its particular growing-modulus argument is the project contribution, not a new language theorem.

Yolcu–Aaronson–Heule's mixed-base rewriting, Calude's explicit-program question and Michel's small Collatz simulators are important machine antecedents [L26–L28]. A pointwise simulator given an integer input and a blank-tape program detecting falsity of the full conjecture are different objects. The compiled table, verifier language and reductions are project-specific artifacts. An external statement that some equivalent program exists nonconstructively does not provide a constructive certificate-completeness proof.

## 4. Credit for comparison systems and their proofs

The Antihydra chapter borrows named machines and solved controls; it does not originate them. For Antihydra, credit **mxdys** for the discovery reported on28June2024, **Racheline/rae** for the exact macro rules, and **Shawn Ligocki** for the arithmetic exposition [L35–L36]. For Hydra, credit **Daniel Yuan** for the20April2024 discovery and Ligocki for the analysis [L37]. The project driver-observer comparison is distinct from those discoveries and does not solve Antihydra.

The five-state champion requires separate credit for Marxen–Buntrock's discovery and Buro/Michel's analysis [L38]. A discovery year is not asserted here because the consulted accounts need reconciliation. The BB(5) determination is a collective BBChallenge achievement, not the work of one explanatory article [L39]. Skelet33's proof credit includes **Jason Yuen/int-y1 and Maja Kądziołka**; the inspected Coq source resolves a coefficient typo in the forum presentation. Skelet34's fixed-width correction is part of Kądziołka's existing analysis, not a new project discovery [L40–L41]. The Skelet1, Chris Xu Skelet17 and Newcomb Greenleaf controls retain their own distinct authors and machine identities [L42–L44]. No local Coq rebuild is implied by reading the formal source.

The recent rational-base papers by Cassaigne–Espinoza–Rigo–Stipulanti and Andrieu–Eliahou–Vivion are related context [L45–L46]. A population-frequency result does not prove a fixed branch's behavior, and a normality conjecture is not a proved resource-safety theorem. Energy-game and abstraction-refinement work [L47–L48] offers methodological comparisons. Unless a project note explicitly records historical influence, these works should be called **related work**, not retroactively named as inspirations.

## 5. What may be publishable, and what can presently be claimed

| Material | Existing foundation | Defensible description now | Additional requirement before a novelty claim |
|---|---|---|---|
| Parity cylinders, affine formulas, basic stopping-density facts | Terras–Everett; Bernstein–Lagarias | Known foundation, carefully applied | No novelty claim intended |
| Reciprocal summability and correction-product consequences | García–Tal/Heppner; Sharpe; earlier project rederivation | Known consequence and useful exposition | Do not market as a new theorem |
| Explicit39/40 window bound | Classical collision-free transfer and parity tails | Audited conservative quantitative instance | Check Curry and other optimized bounds |
| Entropy-height1.0526808586 and chronological boundary costs | Classical word injection/entropy; Rozier harmonic correction | Candidate finite quantitative reformulation | Exact same-statement priority search; compare differing clocks and quantifiers |
| Hamming recurrence with exact logarithmic coefficient | Sharpe defect-height mechanism | Transparent adaptation and constant refinement | Determine whether exact coefficient is already implicit/published |
| Arbitrary-width golden exclusion | Mechanical classification is narrower; rotation-coding literature | Restricted proof candidate, with exact geometry | Broader rotation/substitution and Collatz coding priority review |
| Fixed-dictionary Diophantine restrictions | Subspace/S-unit theorems | Potentially substantial application with nonuniform constants | Specialist proof review; application-specific prior-art search |
| Source-visible budgets, receiver closure and conditional navigation criteria | Flow/compactness, sufficient sets, merger primitives | Exact interfaces and method-specific reductions | Prove missing arithmetic input; identify genuinely new application statement |
| Certificate-language obstructions and matched comparison systems | Automata/recurrence-set methods and known machines | Potential technical note with explicit scope | Compare same language, map, domains and certificate obligations |
| Native machine/checker and compression artifacts | Existing simulation/rewrite traditions | Reproducible construction and engineering contribution | Do not claim minimum state count or full equivalence without required completeness |
| Refuted bounds, alignment errors, population-to-orbit countercontrols | Exact project calculations and standard logic | Valuable negative results and methodological case studies | Separate internal correction from new literature obstruction |

Publication usefulness does not require pretending that all the ingredients are novel. A short paper presenting an unusually clear finite inequality, a reproducible exact construction, or a sharp separation between certificate classes can be worthwhile. But the pre-paper should say what the earlier literature already proves and state its increment precisely. “No exact match located in the sources checked” is the strongest available novelty statement for several branches, not “first proof.”

## 6. Breadth of the historical literature review

The GDR2 atlas dated16October contains193 source records, of which191 are external and two internal. Its normalization reports about171 external work clusters, not193 distinct papers. It records153 theorem/section inspections, five full-text inspections,14 abstract-only records,16 metadata-only records and five inaccessible records. The six substantive domain expansions cover arithmetic, dynamics, combinatorics, analysis, global structures and formal/analytic representations, with a root crosswalk over36 routes and22 retained mechanism families.

Those figures describe the **historical audit's own records**. They are not a claim that171 external works were reread during this pre-paper review, nor that all claimed applications were independently reproved. The full source index is retained inside the machine-readable bibliography so authors outside this chapter's core list are not lost. The original route-to-literature crosswalk and inspection levels remain attached to their claims. Historical records are preserved rather than silently rewritten as current verification.

The current pass concentrated primary reading on priority-critical dependencies: Terras's finite coding, Bernstein–Lagarias, Tao's exact density qualification, García–Tal's actual quantitative inequality, Sharpe's proof and credit paragraphs, Hercher's merger, Monks's gates, Gale's finite scope, Rozier's harmonic/entropy argument, and the specific number-theoretic and machine sources logged by the companion audits. Failed retrievals remain disclosed. In particular, inaccessible Chim, Yu, Everett or Curry originals are not presented as freshly read in full.

## 7. Suggested acknowledgment and citation practice

A suitable starting acknowledgment is:

> This research programme was directed by Ethan Walker, whose questions shaped its source-visible accounting, survivor-versus-integer distinction, arithmetic-driver/observer comparisons, and integration of symbolic certificates with a full-conjecture machine goal. The work was developed with AI assistance. Its mathematical foundations and immediate inspirations are credited at the points of use, including Terras and Everett, Bernstein and Lagarias, García and Tal and their Heppner input, Michael Sharpe, Tao, Hercher, the Monks authors, Gale, and the Diophantine, automata and Busy Beaver contributors identified in the bibliography. These acknowledgments do not imply endorsement or external peer review.

For a final paper, replace broad acknowledgments with precise theorem-level citations wherever a proof imports a result. Preserve discovery, analysis, formalization and exposition credits separately. Pin mutable code when possible. State whether a formal proof was actually built. Do not infer publication dates from upload dates, equate a public repository with a refereed article, or convert “inspired by” into “proved by.” Where the record does not establish an origin, say so.

## 8. Core reference register

The entries below give concise navigation. The machine-readable bibliography contains the full claim associations, inspection limitations, local hashes where available and the historical atlas. A listed reference is not automatically an imported theorem.

- **[L01]** Riho Terras. *A stopping time problem on the positive integers* (1976). [Source](https://matwbn.icm.edu.pl/ksiazki/aa/aa30/aa3034.pdf). Inspection: Primary scan downloaded; OCR generated; visually inspected printed pp.242–243, Theorems1.1–1.2 and Cor1.3–1.4. Introduction and density discussion read; not whole paper independently reproved.

- **[L02]** Riho Terras. *On the existence of a density* (1979). [Source](https://matwbn.icm.edu.pl/ksiazki/aa/aa35/aa3518.pdf). Inspection: Both pages OCR-read, printed p101 visually inspected; statement and short proof checked.

- **[L03]** C. J. Everett. *Iteration of the number-theoretic function f(2n)=n, f(2n+1)=3n+2* (1977). [Source](https://doi.org/10.1016/0001-8708(77)90087-1). Inspection: Original publisher retrieval403; no original-proof inspection this pass.

- **[L04]** Daniel J. Bernstein, Jeffrey C. Lagarias. *The 3x+1 conjugacy map* (1996). [Source](https://websites.umich.edu/~lagarias/doc/bernstein.pdf). Inspection: Primary PDF introduction pp1–3 and displayed conjugacy/series/Periodicity Conjecture inspected.

- **[L05]** Alex V. Kontorovich, Jeffrey C. Lagarias. *Stochastic Models for the 3x+1 and 5x+1 Problems* (2010). [Source](https://arxiv.org/abs/0910.1944). Inspection: Primary2009 manuscript §§1–2, Theorems2.1–2.2 read now; further §§3.1–3.2 inspection recorded in historical atlas.

- **[L06]** Terence Tao. *Almost all orbits of the Collatz map attain almost bounded values* (2022). [Source](https://arxiv.org/abs/1909.03562). Inspection: Primary v6 HTML Theorem1.3, Remark1.4, Syracuse §1.2, affine identity1.7 and parity-cylinder discussion inspected; journal2022 and v7 historical inspections distinguished.

- **[L07]** Manuel V. P. Garcia, Fabio A. Tal. *A note on the generalized 3n+1 problem* (1999). [Source](https://doi.org/10.4064/aa-90-3-245-250). Inspection: Entire six-page primary PDF text read; Lemmas1–3, Prop1–2, Theorem1/eq6, Cor1 checked; cited Heppner original not reread.

- **[L08]** E. Heppner. *Eine Bemerkung zum Hasse–Syracuse Algorithmus* (1978). [Source](https://doi.org/10.4064/aa-90-3-245-250). Inspection: Bibliography and attributed Proposition1 in García–Tal inspected; original article not retrieved.

- **[L09]** Michael Sharpe, Collatz proof project (manuscript byline). *Reciprocal Summability of Every Unbounded Natural Collatz Orbit: A Lean Proof* (2026). [Source](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/paper/orbit_summability.tex). Inspection: Full TeX source read at pinned commit. Root inspected OrbitPacking.lean; no local Lean build or kernel replay here.

- **[L10]** Michael Sharpe, Collatz proof project (manuscript byline). *Classification of Positive Natural Collatz Seeds with Mechanical Parity Itineraries* (2026). [Source](https://github.com/msharpe248/collatz/blob/main/paper/mechanical_classification.tex). Inspection: Full TeX theorem/definition/proof read from main; pinned-path fetch failed; current-source snapshot not same verified pin as L09. No Lean build.

- **[L11]** Michael Sharpe. *DefectHeight.lean* (2026). [Source](https://github.com/msharpe248/collatz/blob/main/lean/Collatz/DefectHeight.lean). Inspection: Source inspected by legacy chapter auditor; no Lean build.

- **[L12]** Pulowski (MathOverflow display name). *Is it known that a divergent Collatz trajectory must have summable reciprocals?* (2026). [Source](https://mathoverflow.net/questions/513539). Inspection: Full question text read; page says Jul24, repository dates observation July2026. Identity beyond displayed name not inferred.

- **[L13]** Christian Hercher. *There are no Collatz m-Cycles with m≤91* (2023). [Source](https://arxiv.org/abs/2201.00406). Inspection: Primary v3 PDF Lemma8, Lemma9 full proof pp4–5, Remark10 and cycle theorem scope inspected.

- **[L14]** Kenneth M. Monks. *The sufficiency of arithmetic progressions for the 3x+1 conjecture* (2006). [Source](https://monks.scranton.edu/files/pubs/SufficiencyRev4.pdf). Inspection: Historical atlas AN05/GS01 records Theorem1.1, inverse formulas and proof inspection; not newly reopened by attribution auditor.

- **[L15]** Keenan Monks, Kenneth G. Monks, Kenneth M. Monks, Maria Monks. *Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph* (2013). [Source](https://arxiv.org/abs/1204.3904). Inspection: Primary PDF Cor5.8 and §6 definitions/Prop6.3/Thm6.4 inspected. Served PDF title date2024 differs from publication2013; publication year retained.

- **[L16]** David Gale. *A theorem on flows in networks* (1957). [Source](https://msp.org/pjm/1957/7-2/pjm-v7-n2-p04-p.pdf). Inspection: Primary §1–2 definitions, Feasibility Theorem and minimum-cut interface read.

- **[L17]** Kwok Chi Chim. *Lower bounds for linear forms in two p-adic logarithms* (2025). [Source](https://doi.org/10.1016/j.jnt.2024.07.012). Inspection: Author/institution abstract and publication metadata inspected; linked PDF403. Older project carries specific application audit; no new full theorem inspection here.

- **[L18]** Kunrui Yu. *p-adic logarithmic forms and group varieties. II* (1999). [Source](https://doi.org/10.4064/aa-89-4-337-378). Inspection: Original publisher metadata verified by Antihydra auditor; original PDF403, not reread.

- **[L19]** Bernadette Faye, Florian Luca, Volker Ziegler. *On a variant of Pillai’s problem with factorials and S-units* (2024). [Source](https://link.springer.com/article/10.1007/s11139-023-00787-1). Inspection: Theorem4/eq5 inspected and constant specialization checked by Antihydra auditor; author metadata reopened directly.

- **[L20]** Jan-Hendrik Evertse, Hans Peter Schlickewei, Wolfgang M. Schmidt. *Linear equations in variables which lie in a multiplicative group* (2002). [Source](https://arxiv.org/abs/math/0409604). Inspection: Primary introduction/Theorem1.1 and nondegeneracy/dimension discussion inspected now; not full proof.

- **[L21]** Jason P. Bell, Jeffrey Diller, Mattias Jonsson, Holly Krieger. *Birational maps with transcendental dynamical degree* (2024). [Source](https://api.repository.cam.ac.uk/server/api/core/bitstreams/c62d2578-8916-4829-97b1-20459f149466/content). Inspection: Primary institutional PDF Theorem4.1 p19 and Theorem4.4 p21 inspected by Antihydra auditor.

- **[L22]** Alan Cobham. *On the base-dependence of sets of numbers recognizable by finite automata* (1969). [Source](https://research.ibm.com/publications/on-the-base-dependence-of-sets-of-numbers-recognizable-by-finite-automata). Inspection: Primary IBM publication abstract/metadata inspected; original full proof not reread.

- **[L23]** Jean-Paul Allouche, Jeffrey Shallit. *Automatic Sequences: Theory, Applications, Generalizations* (2003). [Source](https://www.cambridge.org/core/books/abs/automatic-sequences/cobhams-theorem/C070C48818D5A1C8602FE789386D264D). Inspection: Chapter11 pointer recorded by Pass03 source audit; no claim full book inspected.

- **[L24]** Hong-Yi Chen, Byron Cook, Carsten Fuhs, Kaustubh Nimkar, Peter O’Hearn. *Proving nontermination via safety* (2014). [Source](https://discovery.ucl.ac.uk/1455006/1/TACAS14-nontermination.pdf). Inspection: Section2 recurrence-set definitions checked by machine auditor.

- **[L25]** Krishnendu Chatterjee, Ehsan Kafshdar Goharshady, Petr Novotný, Đorđe Žikelić. *Proving Non-termination by Program Reversal* (2021). [Source](https://arxiv.org/abs/2104.01189). Inspection: Primary abstract and author list inspected; detailed completeness hypotheses not independently audited in this pass.

- **[L26]** Emre Yolcu, Scott Aaronson, Marijn J. H. Heule. *An Automated Approach to the Collatz Conjecture* (2023). [Source](https://arxiv.org/abs/2105.14697). Inspection: Primary abstract/metadata reopened; chapter auditors inspect exact rewrite system and semantics; source-level credit recorded.

- **[L27]** Cristian S. Calude. *The Collatz Problem, the Halting Problem and Randomness* (2019). [Source](https://www.cs.auckland.ac.nz/~cristian/collatzproblem.pdf). Inspection: Complete two-page primary note read; Question1 and its preceding nonconstructive-existence claim directly inspected.

- **[L28]** Pascal Michel. *Simulation of the Collatz 3x+1 function by Turing machines* (2014). [Source](https://arxiv.org/abs/1409.7322). Inspection: Primary arXiv metadata/abstract read; pointwise simulator distinction verified; not full machine proofs reread.

- **[L29]** GettysburgResearch (repository account). *Collatz research RESULTS_CATALOG* (date not independently fixed). [Source](https://github.com/GettysburgResearch/collatz/blob/main/research/RESULTS_CATALOG.md). Inspection: Historical citation only; moving catalog not exhaustively audited.

- **[L30]** Gilles Christol, Teturo Kamae, Michel Mendès France, Gérard Rauzy. *Suites algébriques, automates et substitutions* (1980). [Source](https://numdam.org/articles/10.24033/bsmf.1926/). Inspection: Primary record reopened by closure auditor; exact theorem interfaces recorded historically.

- **[L31]** Boris Adamczewski, Jason P. Bell. *A problem around Mahler functions* (2017). [Source](https://arxiv.org/abs/1303.2019). Inspection: Primary title corrected by closure auditor; historical theorem-level inspection in atlasFA09.

- **[L32]** Pablo Shmerkin, Boris Solomyak. *Zeros of {-1,0,1}-power series and connectedness loci for self-affine sets* (2006). [Source](https://arxiv.org/abs/math/0504545). Inspection: Primary record reopened by closure auditor; documentary use in faithful-jet source verified.

- **[L33]** David Fernández-Duque, Andreas Weiermann. *A Walk with Goodstein* (2024). [Source](https://arxiv.org/abs/2004.09110). Inspection: Primary record reopened by closure auditor; project source explicitly records comparison.

- **[L34]** Nachum Dershowitz, Zohar Manna. *Proving Termination with Multiset Orderings* (1979). [Source](https://www.cs.tau.ac.il/~nachumd/papers/LNCS/Multisets.pdf). Inspection: Primary theorem source reopened by closure auditor.

- **[L35]** Shawn Ligocki. *BB(6) is Hard (Antihydra)* (2024). [Source](https://www.sligocki.com/2024/07/06/bb-6-2-is-hard.html). Inspection: Primary author account exact macros/credit checked by Antihydra auditor.

- **[L36]** BBChallenge contributors. *Antihydra* (date not independently fixed). [Source](https://bbchallenge.org/antihydra). Inspection: Table/arithmetic/status checked21Oct2026 by Antihydra auditor.

- **[L37]** Shawn Ligocki. *BB(2,5) is Hard (Hydra)* (2024). [Source](https://www.sligocki.com/2024/05/10/bb-2-5-is-hard.html). Inspection: Primary author account read by Antihydra auditor.

- **[L38]** Pascal Michel. *Behavior of Busy Beavers* (date not independently fixed). [Source](https://bbchallenge.org/~pascal.michel/beh). Inspection: Champion table/macros/counts and analysis credits inspected by Antihydra auditor; precise discovery year withheld pending date discrepancy.

- **[L39]** BBChallenge collaboration, mxdys (announcement). *We have proved BB(5)=47,176,870* (2024). [Source](https://discuss.bbchallenge.org/t/july-2nd-2024-we-have-proved-bb-5-47-176-870/237). Inspection: Official announcement and contributor scope checked by Antihydra auditor; no full formal project rebuild here.

- **[L40]** Jason Yuen (int-y1), Maja Kądziołka. *Skelet #33 does not halt: Coq proof* (date not independently fixed). [Source](https://discuss.bbchallenge.org/t/skelet-33-doesnt-halt-coq-proof/180). Inspection: Forum account plus Skelet33.v reset_invariant, step_reset, do_reset, E_next inspected by Antihydra auditor; no Coq build.

- **[L41]** Shawn Ligocki, Maja Kądziołka (formal proof/correction). *Skelet #34; Skelet #34 and #35 Coq proof* (2023). [Source](https://www.sligocki.com/2023/02/02/skelet-34.html). Inspection: Author account and https://discuss.bbchallenge.org/t/skelet-34-and-35-coq-proof/165 inspected by Antihydra auditor.

- **[L42]** Shawn Ligocki, Pavel Kropitz, uni-cycle, Maja Kądziołka. *Skelet #1 is infinite* (2023). [Source](https://www.sligocki.com/2023/03/13/skelet-1-infinite.html). Inspection: Primary account checked by Antihydra auditor; page includes later updates.

- **[L43]** Chris Xu. *Skelet #17 and the fifth Busy Beaver number* (2024). [Source](https://arxiv.org/html/2407.02426v1). Inspection: Primary arXiv metadata/abstract verified directly; relevant macro/endgame sections read by Antihydra auditor.

- **[L44]** Newcomb Greenleaf. *Proof for the chaotic four-state machine* (1992). [Source](https://turbotm.de/~heiner/BB/TM4-proof.txt). Inspection: Full primary proof text read by Antihydra auditor.

- **[L45]** Julien Cassaigne, Bastiàn Espinoza, Michel Rigo, Manon Stipulanti. *Symbols frequencies in the Thue–Morse word in base3/2 and related conjectures* (2026). [Source](https://arxiv.org/abs/2602.21895). Inspection: Primary arXiv abstract/metadata read directly; population sequence frequency1/2 distinguished from fixed Antihydra branch.

- **[L46]** Mélodie Andrieu, Shalom Eliahou, Léo Vivion. *A Normality Conjecture on Rational Base Number Systems* (2025). [Source](https://arxiv.org/html/2510.11723v2). Inspection: Primary metadata/abstract read directly; companion auditor opened v2HTML and normality conjecture. Not full theorem-by-theorem audit.

- **[L47]** Lubor Brim, Jakub Chaloupka, Laurent Doyen, Raffaella Gentilini, Jean-François Raskin. *Faster Algorithms for Mean-Payoff Games* (2011). [Source](https://lsv.ens-paris-saclay.fr/~doyen/papers/Faster_Algorithms_for_Mean-Payoff_Games.pdf). Inspection: Introduction and progress-measure context inspected by Antihydra auditor; related method, not documented original inspiration.

- **[L48]** Edmund M. Clarke, Orna Grumberg, Somesh Jha, Yuan Lu, Helmut Veith. *Counterexample-Guided Abstraction Refinement* (2000). [Source](https://web.stanford.edu/class/cs357/cegar.pdf). Inspection: Primary methodological description inspected by Antihydra auditor; similarity does not prove historical influence.

- **[L49]** Olivier Rozier. *The 3x+1 problem: a lower bound hypothesis* (2017). [Source](https://www.ipgp.fr/~rozier/pub/LBHv4.pdf). Inspection: Primary author PDF §§2.1–2.2, Lemma2.5 and full Theorem2.6 proof pp5–7 inspected; introduction explicitly credits Lagarias and Terras/Everett.

- **[L50]** Michael John Curry. *An Explicit Windowed Sparsity Bound for Divergent 3x+1 Orbits, with Logarithmic-Floor Exclusion beyond the Harmonic Barrier* (2026). [Source](https://doi.org/10.5281/zenodo.22087163). Inspection: DOI and Zenodo record failed to open currently, as in October15 audit. Title/attribution via De Jesús repository; original not read.

- **[L51]** Elias De Jesús. *A Global Occupation Conjecture for the Accelerated 3x+1 Map: Divergent-Orbit Sparsity, Exact Realizers, and the Moving-Anchor Problem; companion EOC Lean Verification repository* (2026). [Source](https://github.com/innerlightr-wq/eoc-lean-verification). Inspection: Current README sections on open frontier, manuscript highlights, literature and citations inspected. No Lean build; manuscript itself not inspected.

- **[L52]** Shigeki Akiyama, Masayuki Shirasaka. *Recursively renewable words and coding of irrational rotations* (2007). [Source](https://www.jstage.jst.go.jp/article/jmath/59/4/59_4_1199/_article/-char/en). Inspection: Primary journal metadata and abstract read; full theorem hypotheses not independently recertified.

- **[L53]** Fabien Durand. *A characterization of substitutive sequences using return words* (1998). [Source](https://arxiv.org/pdf/0807.3322). Inspection: Legacy auditor inspected §2.3 and Proposition6 in author arXiv posting. Not independently reread by bibliography auditor.

- **[L54]** Rohit J. Parikh. *On Context-Free Languages* (1966). [Source](https://doi.org/10.1145/321356.321364). Inspection: Original attribution identified; current original full text not inspected. Standard semilinearity theorem corroborated by Esparza et al primary abstract.

- **[L55]** Javier Esparza, Pierre Ganty, Stefan Kiefer, Michael Luttenberger. *Parikh’s Theorem: A simple and direct automaton construction* (2011). [Source](https://arxiv.org/abs/1006.3825). Inspection: Closure auditor inspected primary arXiv abstract and metadata; semilinearity of context-free Parikh images explicitly stated.


### Final-cutoff addition from Navigation 14

**[L56]** Dimitri Bertsekas, *Affine Monotonic and Risk-Sensitive Models in Dynamic Programming* (2016; revised 2017), [primary arXiv record](https://arxiv.org/abs/1608.01393). Navigation 14 cites this as a methodological comparison for affine Bellman inequalities and policy iteration. The abstract and metadata were read in this audit; the full paper was not. The band-envelope theorem rests on its displayed rational edge inequalities, checked directly, not on an uninspected theorem from this paper. This addition brings the core reference register to 56; the historical atlas remains separately classified. Attribution record A33 preserves this distinction.
