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
