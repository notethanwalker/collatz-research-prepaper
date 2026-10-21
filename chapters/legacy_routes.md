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
