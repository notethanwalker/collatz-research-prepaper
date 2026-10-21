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
