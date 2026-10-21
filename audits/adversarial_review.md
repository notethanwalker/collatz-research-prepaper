# Adversarial mathematical review of the pre-paper chapters

**Review date:** 21 October 2026.  
**Purpose:** Attempt to break the strongest claims, rather than restate the claim inventory. This review is independent of the chapter writers' checks, but is not journal refereeing or proof-assistant verification.

## Executive verdict

No fatal error was found in the principal elementary theorem packages reviewed: the automatic-language restrictions; the finite chart soundness and effective sparse-hole obstruction; the first-jet injection and decoder cycle classification; the guarded residual contraction; the summable-capacity countable-flow theorem; the deterministic packet inequality and its conditional occupation consequence; and the stated Navigation budget thresholds.

The strongest conclusions remain **proof-method theorems, restricted arithmetic theorems, conditional reductions, and auditable implementations**, not a Collatz solution or proof that a solution is imminent. The drafts mostly preserve this boundary unusually well. In particular, the open inputs in the countable-flow, unmatched-mass, source-budget, and certificate-completeness approaches have not been supplied by any of the reviewed lemmas.

There is one literal hypothesis omission that should be repaired before publication: the root-sibling theorem in `closure_constraints.md` §9 must restrict the sibling index to **k≥1**, as its source does. Without that restriction, k=0 and m=0 give Y=X, contradicting Y>3X. The original theorem is correct; the abbreviated chapter statement is under-specified.

There are also several clarifications worth making: define the inverse transport operator in GDR-16; make the terminal-free-cut convention explicit in GDR-11; label the chart kernel/version at each implementation claim; and retain the research-draft status of the deep Subspace/S-unit applications. These are detailed below.

## 1. Scope and evidence

The following chapter arguments were read, with source-level reconstruction where needed:

- `certificates_machines.md`: A1–A14, S1–S5, L1–L5 and the stated M1–M2 proof contracts. This audit did not independently reimplement the complete 499,710-state compiler.
- `h_obstruction_audit.md`: all mathematical sections, especially the v1/v2 distinction, image obstruction, affine-update obstruction, and diagonal construction.
- `closure_constraints.md`: the signed presentation, norm gap, birth-basis limitation, compactness hypotheses, first jets, section-replay obstruction, root-sibling barrier, repeated-word budgets and escape constraints. Source texts `faithful_jets.md`, `faithful_audit.md`, `pass18.md`, and `creative09.md` were consulted in detail.
- `gdr_bounds_transport.md`: the full elementary argument chain, with direct reads of `Great_Minds_Pass_08_Execution_2026-10-15.md`, `GDR2_COUNTABLE_MENUS.md`, `GDR2_NONUNIFORM_GATE_SLACK.md`, and `Collatz_Summable_Budgets_From_Arithmetic_2026-10-20.md`.
- `recent_navigation.md`: the sharp strip threshold and collision examples, equal-clock prefix separation, drawdown and multiscale implications, recovery funding, and distinctions between completed packets and source-specific completion hypotheses.
- `legacy_routes.md`: focused checks of the finite entropy–height argument, fixed-source versus family quantifiers, golden proof architecture, source-population limits, FP theorem statements and deep-input status. The entire deep Subspace-Theorem proof chain was not re-refereed here.

The exact primary statements in [Monks, *The Sufficiency of Arithmetic Progressions for the 3x+1 Conjecture*](https://monks.scranton.edu/files/pubs/SufficiencyRev4.pdf), Theorem 1.1, and [Monks–Monks–Monks–Monks, *Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph*](https://arxiv.org/pdf/1204.3904), were checked. The former really concerns merger classes; the latter really establishes forward occurrence of 2 modulo 9. The two imports are not being conflated.

## 2. Automatic certification and arithmetic restrictions

### 2.1 The finite checker has the right logical scope

The carry interval [-2,a] is invariant under the displayed paired-digit transition, and the terminal zero carry gives an integer equality, not merely a congruence. Remembering acceptance at the latest nonzero digit correctly removes high-zero padding. Positivity flags exclude zero. Thus a finite product graph can check an infinite set exactly.

The bound of 16q²(a+3) product states is consistent with two q-state DFA components, two Boolean flags per side, and a+3 carries. The graph argument establishes checker completeness **for a proposed automaton**. It says nothing about whether every divergent Collatz orbit is enclosed by any automaton.

The all-base search is fair because bases and state counts are diagonally enumerated, not searched one base to exhaustion. A finite cycle is a regular language in each base, so cycle coverage is genuine. The chapter appropriately does not infer full counterexample coverage.

### 2.2 Prefix density is valid, with two necessary distinctions

For a non-eventually-periodic positive orbit, distinctness forces escape from every finite set. The vanishing-error irrational-rotation argument then makes the omega-limit of the leading logarithmic phase the whole circle. This supports infinitely frequent visits to each fixed leading prefix. It does not, by itself, supply a rate.

Reversing a q-state LSB DFA gives a q-state NFA, not a determinized machine. From a coaccessible state, an accepting continuation can be shortened to at most q−1 edges. The resulting per-prefix counting proves the displayed lower-density estimate. No exponential determinization cost is warranted in that existence argument.

The stronger bounded-gap conclusion requires closure under multiplication by two. It must not be exported to arbitrary bases. For a dyadically normalized trap, both directions of dyadic membership hold, so its complement has the same doubling property. Both colors meeting every sufficiently placed aligned block is logically possible and does not exclude all automatic traps.

The terminating-prefix construction uses exact divisibility and irrational rotation. Its negative correction is less than one and the integer separation in the strict prefix inequality is amplified enough to dominate it. In a non-power-of-two base, powers of two alone give prefix coverage. This justifies the complement-density argument.

### 2.3 The noncommuting exclusions survive adversarial checks

For involutions a,b, the two terminating families reach r^j(s) and r^{j−1}b(s), r=b∘a. Finite group-orbit periodicity makes positive j sufficient to cover both normal forms. No commutation assumption is hidden.

For idempotents, repeated adjacent digits can be removed without changing the state. Every reduced canonical word is alternating and ends in 1, hence is represented by a terminating repunit or twice a repunit. Only canonically reachable states need to be covered.

Neither argument covers arbitrary noncommuting permutation actions. The draft's countercontrols preserve that limitation. Synchronizing, strongly connected, aperiodic, commuting, and permutation automata are not interchangeable classes.

### 2.4 Semilinear and rewriting conclusions are genuinely narrower

Monks's sufficient-set theorem implies that every positive arithmetic progression meets the merger class of 1. An infinite semilinear set contains such a progression. Therefore a semilinear bad trap must be finite, and its existence is equivalent to existence of a nontrivial cycle. This is a direct corollary of imported work, not a new Collatz sufficiency theorem.

The ordinary context-pumping argument also appears sound on the displayed rewriting system: boundary order is preserved; blocks missing a relevant boundary have a terminating measure; a changed canonical internal block gives a genuine finite Collatz return. Scattered-subsequence comparability does not supply a legal pumping context. The result excludes this particular pumping enlargement, not every well-quasi-order method.

## 3. Chart certificates and the linear-growth diagonal obstruction

### 3.1 Versioned soundness, not an oracle for identities

The normal forms are sound by structural induction. Positive nonconstant coefficients and evaluation at zero give v1's lower bound. Exhaustive residue rows plus natural affine parameter updates give actual forward closure. Integer target expressions force parity, so a branch label cannot bypass the arithmetic guard.

The native equality/lower-witness equivalences have the correct direction: finite proofs reproduce exactly frozen-v1 normal-form equality and positivity, rather than adding an unrestricted semantic equality oracle. This conclusion is mathematical; it does not certify that an arbitrary finite implementation never exhausts resources or that a practical proof producer finds witnesses quickly.

v2's prime-base normalization preserves old acceptance, but the exhibited base-four/base-two pair proves only improved acceptance of literal encodings. It does not prove new semantic existence coverage. The quadratic positivity fallback permits initial decreases, so only **eventual** strict increase may be used in v2's image obstruction.

### 3.2 The two tower obstructions use different hypotheses

The variable-height image obstruction needs eligible nonconstant charts to be eventually strictly increasing. That is proved for the stated v1/v2 sufficient positivity rules. Every fixed grammar expression is bounded by a tower of fixed height; a strictly increasing chart whose values all lie in the variable-height tower sequence would eventually exceed that bound.

The independent transition-growth obstruction does not need the positivity rule. Finitely many affine parameter updates bound parameter growth exponentially in transition time, while fixed-depth expressions still give only fixed-height tower growth. It is important not to confuse these two proofs or claim that changing positivity alone fixes the latter.

Actual C3 has an exponential upper bound in ordinary transition time. Consequently the fast-growth comparison alone does not obstruct a hypothetical Collatz certificate.

### 3.3 The sparse-hole theorem removes that irrelevant growth objection

The diagonal construction is valid under its explicitly supplied effective hypothesis. Each enumerated infinite language has an algorithm to find a member above any bound. Choosing holes r_e with r_e>r_(e−1)+2 and r_e>2^e produces a decidable density-zero hole set: to decide membership of n, generate holes until the first at least n. The complement's next member is at most two larger.

Every represented infinite component hits a deliberately excluded hole; finite components cannot form an invariant under the strictly increasing map. Thus the constructed map has a decidable density-one bad set and linear-growth divergent orbits but no automatic or specified finite-chart-union bad trap.

There is no contradiction with the decidability of its own bad set. The enumeration does not cover all infinite decidable sets, whose infinitude/totality cannot be uniformly certified this way. Likewise it does not defeat unspecified future chart extensions or all finite proof systems. The language family must be named before diagonalization.

This is a clean relative-incompleteness theorem. Calling it an incompleteness theorem **for Collatz** would be incorrect.

## 4. First jets, signed closure, and source preservation

### 4.1 First-jet injectivity is an all-length proof

The no-double-zero inequality at r=1/φ is correct: the infinite tail r⁴/(1−r)² equals one, leaving −r²<0. Equal value and derivative at φ would force divisibility by (q²−q−1)² and hence a prohibited double zero at the conjugate. This proves injection of all finite binary polynomials, not merely of a tested range.

The four-counter digit recurrence is correct. The bit separator has a strictly positive gap, but using it repeatedly requires exact algebraic arithmetic or increasing precision. Four unbounded integer counters are not four finite states.

A new independent exact cycle enumeration reproduced the lattice classification. On periodic decoder states, the original embedding gives p∈[−φ,0], d∈[0,φ²], and the conjugate gives u∈[−1,φ], v∈[−2φ,φ+2]. These inequalities force the four p values and ten derivative values reported in the source. To justify the bounded integer enumeration, writing p=a+bφ gives b=(p−u)/√5∈[−2φ/√5,1/√5]; similarly derivative b lies between −(φ+2)/√5 and (φ²+2φ)/√5. Thus all coefficient pairs lie well inside the independently used search box. Exact integer sign tests leave exactly the cycles with bits 0, 1, and 01.

This classifies a decoder after boundedness and eventual periodicity have been proved. It does not bound the outer Collatz iteration. Nonnegative four-tuples alone do not authenticate finite sources; the 5/3 example is essential, not cosmetic.

### 4.2 Signed presentations are exact reformulations, not compressed convergence proofs

The presented integral module is the component group of the actual functional graph. The two maps described in the chapter explain why no rational/integral torsion gap is hidden. An undirected finite path is equivalent to finite forward merger in a deterministic functional graph.

The norm gap is also exact: a separated component indicator yields a bounded dual functional taking value ±1 on the unresolved target. No finite rational row combination can have unweighted residual norm below one. Thus obtaining that threshold is already equivalent to the missing merger, not a weaker approximate result.

The birth-basis incidence presentation removes signed feedback but retains the forward obligation. A finite expression killing a basis vertex must connect it to the terminal vertex in the finite support graph. Circulations in unrelated components do not supply this connection.

Pinned compactness is valid because all conditions are closed and the target coordinate remains nonzero. Unpinned “nonzero somewhere” is not closed. Hereditary frontier closure is valid when an actual well-founded rank decreases on every nonzero child and all guards are exhaustive. A rank defined from unknown stopping time would only restate the desired theorem.

### 4.3 The bounded-replay obstruction has the stated restricted reach

The selected maximal-slope section has M all-shallow rounds on an infinite dyadic progression. Any companion meeting at such a high checkpoint has total shortcut length bounded in terms of M, even when even steps were initially unrestricted. Equal affine slopes force the same maximal exponent and an all-odd path; different offsets then prevent equality. Unequal slopes have a nonzero integer numerator after clearing a uniform denominator, and the displayed source bound exceeds every possible intercept coincidence.

This defeats uniformly bounded replay followed by endpoint cancellation. It does not prove infinite rank of the unknown component functions: if Collatz holds, those functions are zero. Finite expressions with unbounded recursive lemmas are outside the obstruction.

### 4.4 Required root-sibling correction

**Chapter:** `closure_constraints.md` §9.  
**Source:** `sources/closure/pass18.md`, equation (1.2) and Theorem 2.1.

Replace the opening with:

> For k≥1 define E_k(X)=4^kX+(4^k−1)/3. Let L≥1 and 3^L divide the positive odd X. If a positive odd Y reaches E_k(X) in 1≤m≤L odd rounds, then Y>3X. The m=0 case also has Y=E_k(X)>3X.

The restriction k≥1 makes β=(4^k−1)/3 positive, as required by the inverse-integrality argument and division by β. If one instead admits k=0 and m=0, Y=X is an immediate counterexample. No change to the original source theorem is needed.

## 5. Residual contraction, countable transport, and packet budgets

### 5.1 The residual map is genuinely total on its stated complement

The six core schemata agree with the valuation definition. Outside the core, the priority branches are exhaustive. The inverse branch and merger branch are common-future reductions, not necessarily forward trajectory steps. Their numerical decreases therefore give proof-reduction complexity, not Collatz stopping-time complexity.

The shifted factor 6/7 is valid, including small boundary states. Core factors are at least 9/8. Their product only telescopes along **one connected guarded path**; one cannot combine independent extrema from different sources. The constant-shift optimality result is confined to the specified pure-core-factor class.

Continuation saturation chooses new source representatives as the horizon grows. It refutes fixed schema-only forward-lookahead bounds, not source-dependent certificates. The normalized 27 packet returning E_27−E_1 is a concrete circularity control.

### 5.2 The countable-flow theorem is correct because capacity is summable

For a finite set of source rows, grouping target columns by their finite neighborhood patterns is legitimate. Proportional disaggregation preserves literal-column capacities and does not count multiple proof words as multiple recipients.

For infinitely many rows, product compactness alone would not preserve row mass. The key extra fact is the uniform bound

Σ_(y outside F) f_xy ≤ Σ_(y outside F) κ(y) → 0.

This makes the full row-sum function continuous on the closed capacity-constrained array space. Finite intersection then supplies all row equalities.

The phrase “terminal-free source cut” should be defined immediately as **a finite A with terminal not in N(A)**. Every source is already nonterminal, so otherwise the phrase can be misread. Cuts with a terminal neighbor are automatically feasible because that one column has capacity W.

If κ=w−δ and a closed terminal-free component meets a positive-slack vertex, summing its rows contradicts finite total mass. No uniform relative slack is needed. The conclusion is component exclusion, not a uniform rate or algorithm to construct a useful arithmetic flow. The literal Collatz cut inequality is still completely open.

### 5.3 Packet contraction does not refresh the transported population

For four inputs at odd stride, the depth classes 1,1,2,≥3 are exact modulo eight. The square-root estimate and the stated 0.99 threshold are valid. A new rational-enclosure test also reproduced the global stride-one 0.9999 claim in its finite small-source range.

After a round, the transported measure is neither uniform nor equal-weight on fresh packets. Matching the minimum mass per stride-three packet correctly isolates a nonnegative unmatched potential U_t. The resulting recurrence

V_(t+1) ≤ ρV_t+(√2−ρ)U_t

is a deterministic inequality about the actual source-labelled measure.

The harmonic implication is valid. Multiplying by 1/(t+2), summing finite horizons and weakening denominators gives the displayed bound on ΣV_t/(t+1). Initial potential is finite because ΣX^(−2)√X converges. A permanent survivor has fixed positive source mass and stays above the killed finite base, so contributes a uniform positive potential and contradicts harmonic summability.

The missing input is **ΣU_t/(t+1)<∞ for the actual transported measure**. Finite packet contraction, Haar estimates, or already absorbed companion sources do not establish it.

### 5.4 Define the operator in the power-law no-go theorem

**Chapter:** GDR-16.

“An inverse transport operator” is too broad. The proof needs the deterministic unweighted push-forward on surviving states:

(Ph)(y)=Σ_(x: S(x)=y, x and y surviving) h(x).

Then every surviving edge contributes its full h(x), and Ph≤h implies h(S(x))≥h(x). The long all-shallow family gives the contradiction with h comparable to n^(−s). A normalized or killed-at-every-step operator need not have this property. The source context uses the required operator; it should be made explicit in the standalone theorem.

### 5.5 The smaller budgets are properly limited

Nonminimal depth-cylinder representatives have an absolutely summable total source weight. Every fixed source eventually becomes the minimal representative of its own longer word, so the hard atomic sector has not disappeared.

The repeated-word divisibility budget is valid because its centered integer is strictly positive. This positivity fails at the comparison 3n−1 cycle and is precisely why that countercontrol is useful. A uniform finite charge for one burst does not bound the total charge over infinitely many changing bursts.

Leading-phase equidistribution follows from vanishing rotation errors; reciprocal-summability strengthens this to asymptotic shadowing of one fixed irrational rotation. Neither gives mean trailing depth two or positive average exponential growth. These are different observables.

## 6. Conditional Navigation thresholds and legacy claims

### 6.1 Thresholds checked

The strip inverse proof depends on differences of legal incoming exponents being multiples of ord_c(2). A strip with at most 4 ord_c(2) levels has too small a diameter to contain two predecessor debts. The stated next-width counterexamples show sharpness. Endpoints require a known length or marked start to recover a history; endpoint injectivity is not arbitrary-cut reconstruction.

The drawdown implications are correct:

- D_W≤16 ceil(log2(m+1)) gives H_m≤9m/4+4 ceil(log2(m+1)).
- C5 then grows at least exponentially divided by the stated quartic polynomial.
- Antihydra has nonnegative phase-end budget from m≥32, **provided the earlier native phases are independently authenticated**.
- The multiscale hypothesis gives the stated O(sqrt(m log m)) depth deviation, but the optimizing dyadic slope moves to finer scales. Seven tested slopes cannot supply it.
- The single upper slope 5/2 yields the stated m≥64 native bootstrap. A future formal arithmetic path cannot be treated as native execution if an earlier budget already went negative.
- A small drawdown theorem can suffice without positive W drift. The newer weaker sufficient criterion genuinely corrects the earlier over-strong methodological demand.

The hypotheses remain source-specific conjectures. Reference martingales and finite retained tests do not establish them for source seven or twenty-one.

### 6.2 Legacy entropy–height claim

The finite entropy bound uses uniformly sampled indices in one actual prefix, not random dynamics. Parity injection distinguishes the future blocks because the starting values are distinct and lie below 2^r. Each marginal changes by at most j/M; concavity and the monotonicity of binary entropy above one half yield the displayed inequality.

Combining it with the exact growth ledger gives the maximum-height exponent 1/h_2(log_3 2). This is a lower bound on a prefix maximum. It is not a lower bound on each last iterate, an upper height bound, or an escape contradiction. The interval version must retain its reentry-boundary cost.

### 6.3 Deep Diophantine arguments need a separate status

The fixed-event and fixed-dictionary prefix theorems invoke nontrivial fixed-dimensional Subspace and S-unit results. The chapter exposes the correct sensitive points: fixed R before choosing forms, removal of gcd content, nondegenerate subsums, zero-correction clusters, and a high-source floor for positive centers. These protections are necessary and should remain prominent.

This adversarial review did not independently referee every Diophantine estimate in the source proof. The defensible status is **substantial, coherent research proof draft with identified external dependencies**, pending specialist review. It must not be silently upgraded to the same verification status as the elementary first-jet inequality or an exact integer identity merely because a chapter writer has read it.

The golden arbitrary-width rotation exclusion depends on its complete half-open Fibonacci tower intersection lemma. Finite interval tests support implementation but cannot replace that induction. The theorem concerns one fixed golden rotation with arbitrary single interval width, not arbitrary irrational rotations.

## 7. New reproduction record

Two new scripts were written for this review; they do not import the earlier audit functions.

- `adversarial_checks.py` / `adversarial_checks.json`:
  - 199,999 sources for core-schema equivalence and complement/core shifted inequalities, with exact inverse and merger clock checks;
  - 35,519 packet inequalities proved numerically by **rational lower/upper radical enclosures**, not floating-point comparison;
  - 65,536 distinct first-jet codes;
  - 1,912 eligible involution/idempotent transition pairs on up to four states, checking canonical-state coverage by terminating representatives;
  - 2,728 exact depth-word/source pairs;
  - bootstrap integer inequalities through 100,000, plus the exact comparison 5^16>2^37.
- `adversarial_jet_cycles.py` / `adversarial_jet_cycles.json`: the analytically complete 40-candidate periodic decoder box, with exact algebraic sign tests, yields exactly bit cycles 0, 1, 01.

All checks passed. The broad finite ranges are regression evidence, not substitutes for the corresponding universal proofs. The 40-state classification is different: once the analytic candidate-box proof is supplied, its finite exact enumeration is the final complete step of that theorem.

## 8. Recommended editorial decisions

1. Make the k≥1 sibling correction and define the raw push-forward P before publication.
2. Keep four levels visibly separate: elementary checked theorem; deep-input research proof draft; conditional implication with an open hypothesis; finite experiment/implementation audit.
3. Introduce every theorem with its map, clock, source domain, and fixed versus variable parameters. The corpus reuses A/B/H/T, and the new compilation should not inherit those collisions.
4. Retain original-source ownership whenever invoking induction or a companion proof. Smaller than a later checkpoint is not smaller than the original target.
5. Do not market a source-wise certificate criterion as a theorem that certificates exist. Do not market countably many individually finite checks as a terminating search for an unknown successful witness.
6. Preserve the explicit negative controls and failed approaches. They are mathematically valuable and explain exactly why the remaining input is not a bookkeeping detail.
7. For the native machine, distinguish a complete final transition quotient check from the general compiler invariants and finite replay tests. The native artifact is frozen v1; the small H verifier has a different target and solved schema.
8. Treat novelty as unestablished except where a specialist literature comparison supports it. Recurrent sets, carry automata, Hall/max-flow, compactness, S-unit machinery, irrational rotations, and component group presentations are established tools. The potentially original content is the particular exact synthesis, restricted result, constant, or countercontrol, not those general methods.

**Bottom line:** The principal claims examined are mathematically defensible with their restrictions intact. Their significance lies in exact finite verification, source-faithful reformulation, rigorous limitations of tempting methods, and sharply stated missing arithmetic obligations. None of the reviewed results closes those missing universal obligations.
