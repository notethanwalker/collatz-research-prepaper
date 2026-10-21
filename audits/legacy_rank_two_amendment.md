# Audit amendment to canonical Research43–44

Date: 2026-10-21. This is a new reconstruction made for the pre-paper audit, not text already proved in the October6 originals. It must remain distinguishable from those originals. Full rank-two exclusion is classified as conditional on the stated tower hypotheses and this amended analytic ledger, with targeted argument-level review completed within this AI-assisted audit; external specialist review remains required. No finite-rank or linearly recurrent transfer is inferred.

## A. Hypotheses and scale

At selected levels let W_(j,0),W_(j,1) be distinct prefix-code binary blocks, with lengths L_(j,a), odd counts K_(j,a), and z_(j,a)=2^L_(j,a)/3^K_(j,a). After relabeling on a subsequence take m_j=L_(j,0)≤L_(j,1)≤B m_j, m_j→infinity. Let the grouped inverse-parity scalar be rational with height O(m_j), and coarse tails v^(j) converge in product topology to a word v that is not eventually periodic. Require the **common-frequency assumption** K_(j,a)/L_(j,a)→δ for both a, or a separately proved replacement residual-height bound strong enough for the calculations below.

Research44 states common frequency. Research43's standalone final theorem omits it while borrowing a Research35 height ledger that uses it. This audit does not certify the stronger standalone Research43 wording.

Use h(a/b)=log2 max(|a|,b). Research42 gives rational r_j=G_(v^(j))(z0,z1) of height≤A m_j+o(m_j), when z0≠z1, by exact correction elimination and prefix-code nondegeneracy. Equal multipliers use Research41 instead.

## B. Irrational limiting slope: restore the missing residual-height hypothesis

Suppose L1/L0→ρ>1 irrational. Choose a fixed large q and p=floor(qρ), so p≥q and 0<d0=qρ−p<1. In regraded coordinates x=z0,t=z1/z0,Y=z1^q/z0^p,

ΔL=qL1−pL0=d0 m+o(m),
ΔK=qK1−pK0=δΔL+o(m).

Thus h(Y)≤αm+o(m), α=log2 3. The leading coefficient is bounded independently of q; the o(m) is taken only after q is fixed. Also h(x)≤αm, h(t)=O_B(m), and x,t,Y are2-adically integral for sufficiently large j.

For normal polynomial pairs deg_x≤d,0≤deg_t<q,deg_Y≤e=ceil(Kd/q), the coefficient count is U=2(d+1)q(e+1). To kill x-orders belowN, a safe condition count is C_N≤Σ_(l<N)q(e+floor(l/q)+2). With N=floor((2−η)d),0<η<2−α, choose K large depending onη, then d large. The inequality U>C_N yields a nonzero fixed pair.

After compatible jet rescue, the rational value has height at most

[A+αd+C_B q+C_η d/q]m+o(m)+O_pair(1).

The main term uses **m=L0**, not maximum block length. Bounded distortion enters only the overhead constants. Choose q large, then d sufficiently large relative to q,A, so this is strictly less than Nm. The rescued value has valuation≥Nm−O_pair(1). It must therefore vanish eventually. The fixed rescued formal error has finite rational coefficient set after Laurent embedding, so the irrational Newton-weight lemma says its valuation is O(m), whereas increasingly long coarse-prefix matches force valuation/m→infinity. This contradicts survival.

The order of choices matters: fixη,thenK,thenq,thend,e,N and a finite polynomial pair/jet, then let j tend to infinity. No degree grows with j.

## C. Rational slope: a uniform bound for the infinite Y-tail

Let ρ=p/q be in lowest terms,p≥q. Then ΔL=qL1−pL0=o(m),ΔK=qK1−pK0=o(m),h(Y)=o(m). Put ε_j=|v2(Y_j)|=|ΔL_j|=o(m_j). Y may not be2-adically integral. The October6 text charges only the fixed polynomial Y-degree; that does not by itself bound the infinite error series.

Here is an explicit bound for that missing tail. Let G=Σ_(n≥0)x^n t^B_n,0≤B_n≤n. Multiply a path term by a fixed normal polynomial monomial x^i t^s Y^f with i≥0,0≤s<q,f≤e. Reducing t^(B_n+s), set k=floor((B_n+s)/q). The resulting indices are

l=i+n+(p−q)k≥n,
s'=(B_n+s) modq,
f'=f+k≤e+floor(l/q)+1.

Consequently at x-degree l every Y-degree is at most e+floor(l/q)+1. After clearing the fixed polynomial denominators all coefficients have2-adic valuation bounded below by one fixed constant. Compatible Euler derivatives only multiply coefficients by integers and preserve the monomial support/degrees, so this bound still holds for every fixed iterated jet.

For l≥N, x has valuationm and t has nonnegative valuation, while Y contributes at worst −(e+l/q+1)ε. Thus every term has valuation at least

l m−(e+l/q+1)ε−C.

For large j,m−ε/q>0. This proves convergence and the uniform lower bound

v2(tail with x-order≥N)≥Nm−(e+N/q+1)ε−C=Nm−o(m).

For fixedq,d,e,N the loss is o(m). This is the required replacement for the insufficient fixed-degree-only remark. Termwise Euler differentiation and Leibniz evaluation are justified by the same convergent lower bound.

## C2. Jet rescue is pointwise, not a new formal Padé identity

A necessary distinction: the rescued error E*=J(P0)+J(P1)G need not formally belong to x^N. Leibniz cross terms need not vanish as series. At each specialization choose J of minimum total order for which the evaluated polynomial pair survives. Every lower-order pair jet then vanishes at that point, and only there does

[J(P0)+J(P1)G](ξ)=J(P0+P1G)(ξ)

hold. The right side preserves the original x^N filtration and the uniform tail bound in C. The actual rational specialized value uses r_j, so add J(P1)(ξ)[r_j−G(ξ)]. Coarse-prefix convergence makes this correction superlinear in m; the fixed polynomial factor changes valuation only by O(m). Select one repeated J from the finite degree-bounded family before invoking a fixed-error Newton argument. This preserves both the valuation lower bound and ordinary-height degree box without falsely claiming a global rescued Padé identity.

## D. Rational Newton leading form: prevent an unbounded-degree loophole

For a fixed rescued pair, write its nonzero formal error as Σ_(l≥0)Σ_(0≤s<q)x^l t^s A_(l,s)(Y). Formal nonrationality ensures it is not zero. All nonzero normal weights λ(l,s)=l+s(p−q)/q are distinct and separated by≥1/q, since gcd(p−q,q)=1. A unique minimum pair(l*,s*) exists.

For the fixed leading polynomial A*, if A*(Y_j) is nonzero, its valuation magnitude is≤deg(A*)h(Y_j)+O(1)=o(m). The same holds for every nonzero coefficient among finitely many bounded l. For the remaining infinite tail, the degree bound in C gives valuation at least

l m−(e+l/q+2)ε−C.

The extra ε absorbs the bounded residue contribution sΔL/q when comparison is made with limiting weights. Choose once a cutoff l>2λ(l*,s*)+2, then let j grow so ε/m is small. All beyond-cutoff terms lie strictly above the leading term; the finitely many lower l competitors are separated by m/q−o(m). Hence the leading term is uniquely minimal and v2(error)=O(m).

If A*(Y_j)=0 infinitely often, a fixed polynomial has finitely many rational roots, so Y_j=Y* is constant on a subsequence. Prime2/3 exponents satisfy fixed affine integer relations; gcd(p,q)=1 yields

z0=α0 τ_j^q, z1=α1 τ_j^p

with fixed rationalα0,α1 and rationalτ_j. Research42's fixed-shape theorem (or equal-shape Research41) handles this case. Its aperiodic-limit and linear-height hypotheses remain explicit.

## E. Scope and review status

The new degree estimate appears to close the two identified technical omissions within the strengthened common-frequency framework. It is not an assertion that the original standalone Research43 theorem had all necessary hypotheses, nor a proof of aperiodicity-preserving tower transfer. Before assigning high-confidence status to the combined conclusion, the targeted second reviewer should check the degree bound, termwise jet evaluation, ordinary-height coefficients and quantifier order. The independent local lemmas in Research39–42 remain separately evaluable.
