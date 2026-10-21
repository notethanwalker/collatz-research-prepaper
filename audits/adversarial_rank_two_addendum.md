# Independent targeted review: canonical Research43–44

**Date:** 21 October 2026.  
**Reviewed amendment:** `legacy_rank_two_amendment.md`, including its pointwise jet-rescue section C2.  
**Source texts read:** canonical Research35, Research40, Research42, Research43 and Research44; Research39/41 are used only through the explicitly stated local inputs checked by the primary route reviewer.

## Verdict

The proposed amendment repairs the two identified proof omissions **within its strengthened common-frequency, bounded-distortion, aligned-height, prefix-code and aperiodic-limit framework**. I found no further gap in the amended dimension/height/tail/Newton argument after including the pointwise jet-rescue clarification below.

This is a new audit reconstruction. It does not retroactively make the broader Research43 standalone statement proved, does not certify the unamended Research44 tail argument, and does not establish that arbitrary hypothetical Collatz histories possess the required tower. General finite rank, transfer from linearly recurrent systems, global exhaustive coverage and positive-cycle exclusion remain separate obligations.

## 1. Irrational slope: the omitted hypothesis is genuinely used

Put m=L0 and assume m≤L1≤Bm, both K_a/L_a→δ∈[0,1], and L1/L0→ρ>1 irrational. Fix q and p=floor(qρ), with d0=qρ−p∈(0,1). Then

ΔL=d0m+o(m),  ΔK=δd0m+o(m).

For Y=2^ΔL 3^(-ΔK), this gives h(Y)≤(log2 3)m+o(m). When δ>0 the two exponents eventually have the same sign, so height is the maximum of their two contributions, not their sum. When δ=0, a possibly negative ΔK contributes only o(m). This verifies the claimed leading constant independent of the chosen fixed q.

Without common frequency, ΔK can be Θ(qm), and multiplying its height by e≈Kd/q need not make the residual cost small. Thus the original standalone theorem's missing hypothesis cannot be treated as a cosmetic omission. The broader assertion is not established by this argument; no counterexample to the broader theorem itself is claimed.

The Padé count is sufficient: with N≈(2−η)d, the dominant difference U−C_N is at least

[ηK−(2−η)²/2]d²+lower-order terms.

Choose η∈(0,2−log2 3), then K larger than (2−η)²/(2η), then q sufficiently large, then d sufficiently large relative to q and the rational-scalar height constant. This makes the height coefficient strictly less than N. All choices are fixed before j tends to infinity. The use of m=L0 is essential; bounded distortion alone would not permit replacing the main valuation by the maximum block length.

## 2. Rational slope: the linear degree bound controls the entire infinite tail

For a normal polynomial monomial x^i t^s Y^f, i≥0, 0≤s<q, f≤e, multiply a path term x^r t^(B_r), 0≤B_r≤r. Let k=floor((s+B_r)/q). After reduction,

l=i+r+(p−q)k≥r,  and  f+k≤e+floor(l/q)+1.

This proves the amendment's degree bound for every term, uniformly in the infinite path index. One fixed denominator clears all coefficients of the polynomial pair; path coefficients are integers. Compatible Euler operators only multiply coefficients by integers, so their iterates retain a uniform lower bound on coefficient valuations.

With ε=|v2Y|=o(m), and with v2t≥0 after the chosen ordering of lengths, each term of x-degree l has valuation at least

l(m−ε/q)−(e+1)ε−C.

For large j the coefficient of l is positive. Consequently the infinite series and all fixed Euler derivatives converge, and the part of x-order at least N has valuation at least

Nm−(e+N/q+1)ε−C=Nm−o(m).

The original fixed-polynomial-degree remark is insufficient by itself. The amended **linear growth of tail degree** is the missing reason the infinite series is controlled.

## 3. Jet rescue must be pointwise

The new section C2 is necessary and correct. In general

J(P0)+J(P1)G

does not formally have x-order N, even when P0+P1G does. At each specialization choose a nonzero pair jet of minimum total order. All lower pair jets vanish at that point, so Leibniz cross terms disappear there and only there. Its evaluated error equals J(P0+P1G), which retains the original filtration and the just-proved tail bound.

The additional term J(P1)(r_j−G) has superlinear valuation because coarse-prefix matching grows without bound, while evaluation of a fixed polynomial can lower valuation by at most O(m). A finite degree-dependent jet family permits selection of one fixed J on an infinite subsequence. No rationality of derivatives of G is assumed or needed.

This supplies the valid high-precision rational value used in the height contradiction. The later fixed-error Newton argument may use the rescued pair even though its formal order is not N.

## 4. Leading dominance is uniform, not merely coefficientwise

For rational ρ=p/q in lowest terms, distinct normal pairs (l,s), 0≤s<q, have distinct weights λ=l+s(p−q)/q separated by at least 1/q. The leading polynomial A*(Y) is fixed. If nonzero at Y_j, its valuation is o(m) because h(Y_j)=o(m).

To conclude dominance, split the remaining series into finitely many x-degrees below a fixed cutoff and the infinite tail. The finite competitors have valuation gap at least m/q−o(m). Choose the cutoff greater than 2λ*+2; the uniform linear tail bound then places all higher degrees strictly above the leading term for sufficiently large j. This validates the conclusion v2(error)=O(m).

If A*(Y_j)=0 infinitely often, finite rational-root cardinality gives constant Y on a subsequence. Unique prime factorization turns its two fixed valuation relations into a fixed rational monomial multiplier shape. The previously established fixed-shape theorem applies, with the same aperiodic coarse limit retained on every subsequence.

The irrational Newton lemma is similarly valid after making its implicit uniformity explicit: positive limiting weights are coercive, so only finitely many support points can compete below any fixed threshold. The unique lowest weight therefore persists uniformly after a finite cutoff, not merely one competing monomial at a time.

## Final classification

- **Original R43 standalone theorem:** insufficiently stated for its supplied proof; do not quote without adding common frequency or an equivalent proved residual-height hypothesis.
- **Original R44 proof:** missing a uniform infinite-tail estimate; do not replace that omission with finite checks.
- **Amended restricted rank-two exclusion:** the mathematical proof chain now passes this independent targeted argument-level review.
- **Universal Collatz or unrestricted recurrence exclusion:** not established.

Finite normal-form and Padé checks supplied by the route reviewer remain regression evidence. The conclusion above rests on the explicit estimates and quantifier order, not those finite counts.
