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
