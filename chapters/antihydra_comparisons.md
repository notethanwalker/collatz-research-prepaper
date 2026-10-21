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
