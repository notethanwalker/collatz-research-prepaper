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
