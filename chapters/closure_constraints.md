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
