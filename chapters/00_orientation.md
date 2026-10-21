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
