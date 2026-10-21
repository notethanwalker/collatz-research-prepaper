# Literature, intellectual lineage, and provisional originality assessment

## 1. What is being credited

This pre-paper concerns an AI-assisted research programme directed by Ethan Walker. Its organizing questions, technical deductions, borrowed theorems, computational artifacts, and later literature comparisons are not interchangeable kinds of contribution. We preserve those distinctions rather than attach a single name to every statement in a branch.

A result may be correct without being new; useful without proving Collatz; independently reconstructed within this review without having received independent human peer review; or inspired by an informal question whose proposed mathematical answer later proves false. Generous attribution means retaining all these relationships accurately.

The accompanying `audits/attribution_ledger.json` separates:

1. **Direct user evidence:** exact conversation messages preserved in the research record.
2. **Documentary origin evidence:** a contemporaneous report explicitly identifying an idea or priority as the user's, sometimes preserving a quotation. These are distinguished from a fresh reading of the original conversation.
3. **Direct mathematical dependency:** an external theorem actually used, with its hypotheses and scope.
4. **Documented adaptation or inspiration:** a report explicitly says it followed a source or modified its mechanism.
5. **Related work:** a relevant comparison found in this review, without evidence that it historically inspired the project.
6. **Unknown provenance:** the origin was not located. This is not evidence of independent invention.

The reference labels below identify entries in `sources/primary_bibliography.json`. Each entry records author, title, date or date uncertainty, URL, associated claims, what it supports, and exactly how much was inspected. Original research, author surveys, books, software repositories, community proof records, and project notes have different evidentiary roles. The filename “primary bibliography” does not mean that every included lead was read in full or that every item is an original research article.

## 2. Documented contributions to the research direction

### 2.1 Ethan Walker's questions and priorities

There is direct conversation evidence for four important machine-research decisions. Walker requested a machine for the **full conjecture**, drawing on the Library rather than merely simulating a supplied starting number. He then requested both state reduction and detection of every counterexample, expressly prioritizing the latter if the goals conflicted. He proposed integrating the symbolic checker with the Collatz machine, describing this as merging the programme's ideas. On 21 October 2026, at 15:32:39 UTC, he requested continuation of the reduction iteration until a reasonable stopping point.

These support credit for the originating brief, priority ordering, synthesis, and continuation criteria. They do not establish that a completeness theorem has been proved, that state minimality is known, or that the user originated the general theory of nontermination certificates. Earlier message timestamps are not supplied by the retained evidence and are not reconstructed from file dates. The exact message identifiers and wording are preserved in attribution records A01–A04.

Older reports provide additional documentary, rather than freshly recovered conversational, evidence:

- **Sorting and division surplus.** Notation Transform 06, dated 7 October, explicitly calls the user's sorting intuition its origin. It records discussions at 10:32, 10:42, and 11:03 CDT. The intuition that maximal division should dominate multiplication motivates a research question, not a universal inequality already proved.
- **Alternation and fairness.** FP02, dated 8 October, attributes to the user the proposed bias-erasing effect of multiplication, addition, and maximal division. Subsequent finite-ensemble and chronological analyses test and qualify that proposal. An erroneous universal version should not be credited as a theorem or erased from the intellectual history.
- **Survivors versus an integer.** The 12 October UTC survivor-intersection checkpoint explicitly identifies the user's insistence on distinguishing vanishing fractional survivor populations from the continued survival of one actual integer. This priority remains central to the pre-paper's quantifier discipline.
- **Complete GDR accounting.** The 14 October foundation records the user's request to understand growth, division and residual contributions together, rather than assume fairness or demand compensation from a selected local event.
- **Summability and integration.** The 20 October arithmetic-budget report explicitly develops the user's summability/integration direction. The inspiration and problem formulation are credited separately from Tonelli's theorem, finite flow duality, and existing orbit-sparsity inputs.
- **Arithmetic generator and observer.** The 20 October machine-direction report attributes to the user the shift from superficial state-count comparisons toward the arithmetic driver, the resource coordinate and the halting observer. This motivates the controlled Antihydra comparisons; it is not a theorem that five-state and six-state machines obey different universal laws.

The precise Library identifiers, report paths and passage anchors appear in A05–A10. These credits should remain in any shortened publication. Conversely, absent documentation, the report does not assign Walker every intermediate conjecture or proof trick in a model-generated note.

### 2.2 Internal research lineage

Later reports often complete or correct earlier ones. Research15's golden-rotation handoff explicitly identifies Research11 as an earlier proposal of the target; Research15 should not receive sole credit for originating that target. Shortcut15 acknowledges an external clean-window mechanism and changes its growth constant. The October15 GDR notes already derive reciprocal summability from classical spatial sparsity, so a later synthesis must not present that deduction as newly discovered on October21.

Signed model names and audit labels are retained as provenance of the research artifacts, not represented as external referees or human coauthors. A publication must separately determine responsible human authorship and disclose AI assistance appropriately. Repeated summaries of a theorem do not constitute multiple independent validations.

## 3. The core mathematical lineage

### 3.1 Finite arithmetic and the population/trajectory distinction

Terras's 1976 Theorem1.2 and Corollary1.3 establish the finite parity-vector/residue correspondence; Everett receives the classical independent co-credit. Terras's 1979 clarification addresses the density argument. Bernstein and Lagarias place this arithmetic in a 2-adic conjugacy framework [L01–L04]. These are foundations for the project's exact cylinders, parity-word injectivity, affine compositions, and residue realizers, not new project theorems.

One must distinguish existence of a finite word realizer, a compatible 2-adic infinite sequence, and realization by one positive integer. The reverse rationality/periodicity assertion is not a consequence of writing down a conjugacy. Kontorovich–Lagarias explicitly distinguish stochastic models from the deterministic problem [L05]. Tao's almost-bounded-values theorem applies to almost all sources in **logarithmic density**, with any prescribed bound tending to infinity; it is not a theorem that every source reaches a common fixed bound [L06]. These limitations govern the Region, FP, GDR and recent-navigation interpretations throughout this pre-paper.

### 3.2 Orbit sparsity: García–Tal, Heppner, and Sharpe

García and Tal's 1999 paper is a decisive antecedent [L07]. Its Lemmas1–3 transfer a collision argument into arbitrary translated intervals. Their equation(6), using a stopping estimate credited to Heppner [L08], bounds equal-time collision-free sets by a logarithmic factor times a power strictly below one. Corollary1 includes infinite orbit value sets. This is stronger information than the qualitative statement “Banach density zero.”

For the project, the immediate consequence is elementary: a bound of the form
\[
\#(O\cap[a,a+X))\le K\log(2X)X^{1-\eta},\qquad \eta>0,
\]
with uniform constants yields reciprocal summability by dividing the positive axis into dyadic shells. **Banach density zero by itself would not justify that inference.** For an injective orbit, summing over distinct values equals summing over time. For a cycle, summing distinct cycle values is finite while summing repeatedly visited values over all time diverges. This distinction must be preserved.

Michael Sharpe's repository supplies a newer elementary finite-packing proof and Lean formalization, explicitly acknowledging García–Tal and a public MathOverflow derivation [L09,L12]. The project's use of his packing, defect-height and mechanical machinery must credit him by name. The original source's packing estimate uses the bases8,216 and243; later changes in a tail estimate or logarithmic envelope are refinements of that mechanism, not ownership of it. The pinned `OrbitPacking.lean` source was inspected at commit `ec8174b567d5cab4960024782210b5f5db02bd3a`; the external Lean project was not rebuilt here.

### 3.3 Exactly what the quantitative refinements add

Three mathematically different statements must not be conflated.

**Uniform spatial windows.** The October15 GDR calculation obtains
\[
\#(S\cap[a,a+X))\le18(\lfloor\log_2X\rfloor+1)X^{39/40}
\]
for a synchronous-collision-free set. Its proof explicitly substitutes an elementary parity-binomial-tail estimate for unspecified stopping constants, then uses García–Tal's translated-window argument. It is a transparent quantitative instantiation of an established mechanism. It is not a newly discovered type of orbit sparsity.

**Chronological maximum height.** The legacy entropy argument samples an index from an actual prefix of \(M\) distinct states, injects its future parity words into words of length \(r=\lceil\log_2(H+1)\rceil\), and retains the overlap boundary cost. With empirical odd proportion \(p\), it obtains
\[
\log_2 M\le r\,h_2\!\left(p-\frac{r-1}{2M}\right)
\]
when the argument of \(h_2\) is at least one half. The distinct-odd harmonic correction gives \(p\ge\log_3 2-o(1)\). Consequently
\[
\liminf_{M\to\infty}\frac{\log H_M}{\log M}
\ge \frac1{h_2(\log_3 2)}=1.0526808586079714\ldots.
\]
This is a **prefix maximum**, not a lower bound for every last iterate. Its occupation extension has an explicit reentry-boundary cost, so it cannot simply be asserted as a uniform translated-window exponent.

**Prior-art assessment.** Parity injection, entropy subadditivity/binomial tails and collision-free counting are classical ingredients. Rozier's Lemma2.5 and Theorem2.6 explicitly supply the distinct-odd harmonic-correction antecedent [L49]. García–Tal's stated constants do not immediately identify the exact chronological exponent above, but that does not establish its novelty. A short finite reformulation or an optimized constant may be worth publishing if its exact increment over prior work is made clear. The proper current label is **candidate quantitative reformulation, priority unresolved**, not “new entropy barrier.”

A further lead must remain visible: Michael John Curry's 2026 work is attributed by a related author's repository with an explicit uniform exponent approximately0.9653844 [L50–L51]. Its original DOI and record were inaccessible in this audit. We neither import its theorem as verified nor suppress it when discussing originality of our weaker39/40 bound. The source must be obtained before claiming a best-known quantitative window estimate. The related repository's own occupation and moving-anchor assumptions are expressly open, not external solutions to the project's arithmetic frontier.

### 3.4 Mechanical words, arbitrary-width rotations, and return words

Sharpe's mechanical classification uses words
\[
 b_t=\lfloor(t+1)\gamma+\rho\rfloor-\lfloor t\gamma+\rho\rfloor.
\]
Its interval width is tied to the rotation slope. The manuscript classifies globally mechanical positive itineraries and proves that an eventually mechanical itinerary reaches one [L10]. This covers the corresponding slope-tied golden and silver special cases. It does **not by definition** cover every coding
\[
 b_t=\mathbf1_I(\{t\theta+\rho\}),\qquad |I|=\beta,
\]
where \(\theta\) is the golden rotation and \(\beta\) is arbitrary and independent of \(\theta\).

The project's repaired arbitrary-width golden theorem therefore has a genuine scope distinction, but its historical originality remains unresolved. Akiyama–Shirasaka is relevant rotation/substitution literature [L52]; the final project proof must not be advertised as a consequence of an earlier overbroad substitution claim. An exact geometry verifier checks finite identities and endpoint conventions, not universal publication priority.

Likewise, the Research39 correction respects Durand's return-word convention: start-to-start return words form a code, not necessarily a prefix code [L53]. The project explicitly tests the failure and derives a changed-alignment formula. Its later rank-two closure statement remains conditional on common frequency, distortion and alignment-height assumptions. Finite rank or linear recurrence alone is not asserted to verify these assumptions.

### 3.5 Existing merger and gate theorems

Hercher's Lemma9 gives the precise lower-source common-future identity used by the programme; Remark10 already applies it to a least unbounded source [L13]. Hercher's separate cycle bound must not be confused with this lemma's general applicability. The project's graph composition, path accounting or receiver construction may add a useful organization, but the primitive merger and its least-source use are not new.

Kenneth M. Monks's sufficient-progression work and the four-Monks sufficient-set paper supply the appropriate residue-gate background [L14–L15]. In particular, Corollary5.8 and the later strong-sufficiency statements have different target sets and scopes. These are exact structural results, not permission to assume a hypothetical orbit samples all residue classes with their population frequencies.

### 3.6 Diophantine and analytic inputs

Chim's two-p-adic-logarithm bound and Yu's logarithmic-form work are external tools, not project discoveries [L17–L18]. The present audit retrieved Chim's primary metadata and abstract but not the full theorem; the historical application checks therefore remain separately labeled. The Antihydra audit inspected the rational Yu formulation in Faye–Luca–Ziegler, including the actual hypotheses, before specializing constants [L19]. A citation to Yu's title alone would not suffice.

Fixed-event and fixed-dictionary arguments use fixed-dimensional Subspace/S-unit machinery. Evertse–Schlickewei–Schmidt give a bound on nondegenerate solutions in fixed multiplicative rank and dimension; this is not a general bound on solution heights or an estimate uniform in a growing number of terms [L20]. Bell–Diller–Jonsson–Krieger provide useful exact formulations inspected in the comparison work [L21]. The project-specific contribution, if correct, is the particular affine ledger, handling of zero clusters and quantifier discipline, not a new Subspace Theorem.

Closure comparisons also acknowledge Christol–Kamae–Mendès France–Rauzy, Adamczewski–Bell, and Shmerkin–Solomyak [L30–L32]. Their automatic/algebraic, Mahler, and small-coefficient-series constraints apply to specified classes. None supplies an unrestricted Collatz bridge merely by analogy. Fernández-Duque–Weiermann and Dershowitz–Manna provide canonical-domination and well-founded-order context [L33–L34]; a proposed Collatz rank still needs actual decrease on every relevant transition.

### 3.7 Flow, recurrence certificates, and machines

Gale's theorem is explicitly a finite-network theorem [L16]. It supplies the feasibility/cut interface, not the arithmetic inequalities demanded by the project's source rows. Passing to countably many rows requires the stated compactness/tail conditions. The project cannot credit itself with max-flow duality or credit Gale with proving its open Collatz budget.

Cobham and the automatic-sequence literature supply rigidity for representations in independent bases [L22–L23]. Recurrence-set and program-reversal approaches supply established ways to certify nontermination [L24–L25]. Relative completeness in a rich semantic setting is not completeness of this project's finite automaton, automatic-set or symbolic-chart syntax. The explicit separation examples are potentially useful precisely because they state which syntax fails. Creative07’s instruction-language obstruction uses the classical semilinearity theorem of Parikh, with a modern automaton formulation by Esparza–Ganty–Kiefer–Luttenberger [L54–L55]; its particular growing-modulus argument is the project contribution, not a new language theorem.

Yolcu–Aaronson–Heule's mixed-base rewriting, Calude's explicit-program question and Michel's small Collatz simulators are important machine antecedents [L26–L28]. A pointwise simulator given an integer input and a blank-tape program detecting falsity of the full conjecture are different objects. The compiled table, verifier language and reductions are project-specific artifacts. An external statement that some equivalent program exists nonconstructively does not provide a constructive certificate-completeness proof.

## 4. Credit for comparison systems and their proofs

The Antihydra chapter borrows named machines and solved controls; it does not originate them. For Antihydra, credit **mxdys** for the discovery reported on28June2024, **Racheline/rae** for the exact macro rules, and **Shawn Ligocki** for the arithmetic exposition [L35–L36]. For Hydra, credit **Daniel Yuan** for the20April2024 discovery and Ligocki for the analysis [L37]. The project driver-observer comparison is distinct from those discoveries and does not solve Antihydra.

The five-state champion requires separate credit for Marxen–Buntrock's discovery and Buro/Michel's analysis [L38]. A discovery year is not asserted here because the consulted accounts need reconciliation. The BB(5) determination is a collective BBChallenge achievement, not the work of one explanatory article [L39]. Skelet33's proof credit includes **Jason Yuen/int-y1 and Maja Kądziołka**; the inspected Coq source resolves a coefficient typo in the forum presentation. Skelet34's fixed-width correction is part of Kądziołka's existing analysis, not a new project discovery [L40–L41]. The Skelet1, Chris Xu Skelet17 and Newcomb Greenleaf controls retain their own distinct authors and machine identities [L42–L44]. No local Coq rebuild is implied by reading the formal source.

The recent rational-base papers by Cassaigne–Espinoza–Rigo–Stipulanti and Andrieu–Eliahou–Vivion are related context [L45–L46]. A population-frequency result does not prove a fixed branch's behavior, and a normality conjecture is not a proved resource-safety theorem. Energy-game and abstraction-refinement work [L47–L48] offers methodological comparisons. Unless a project note explicitly records historical influence, these works should be called **related work**, not retroactively named as inspirations.

## 5. What may be publishable, and what can presently be claimed

| Material | Existing foundation | Defensible description now | Additional requirement before a novelty claim |
|---|---|---|---|
| Parity cylinders, affine formulas, basic stopping-density facts | Terras–Everett; Bernstein–Lagarias | Known foundation, carefully applied | No novelty claim intended |
| Reciprocal summability and correction-product consequences | García–Tal/Heppner; Sharpe; earlier project rederivation | Known consequence and useful exposition | Do not market as a new theorem |
| Explicit39/40 window bound | Classical collision-free transfer and parity tails | Audited conservative quantitative instance | Check Curry and other optimized bounds |
| Entropy-height1.0526808586 and chronological boundary costs | Classical word injection/entropy; Rozier harmonic correction | Candidate finite quantitative reformulation | Exact same-statement priority search; compare differing clocks and quantifiers |
| Hamming recurrence with exact logarithmic coefficient | Sharpe defect-height mechanism | Transparent adaptation and constant refinement | Determine whether exact coefficient is already implicit/published |
| Arbitrary-width golden exclusion | Mechanical classification is narrower; rotation-coding literature | Restricted proof candidate, with exact geometry | Broader rotation/substitution and Collatz coding priority review |
| Fixed-dictionary Diophantine restrictions | Subspace/S-unit theorems | Potentially substantial application with nonuniform constants | Specialist proof review; application-specific prior-art search |
| Source-visible budgets, receiver closure and conditional navigation criteria | Flow/compactness, sufficient sets, merger primitives | Exact interfaces and method-specific reductions | Prove missing arithmetic input; identify genuinely new application statement |
| Certificate-language obstructions and matched comparison systems | Automata/recurrence-set methods and known machines | Potential technical note with explicit scope | Compare same language, map, domains and certificate obligations |
| Native machine/checker and compression artifacts | Existing simulation/rewrite traditions | Reproducible construction and engineering contribution | Do not claim minimum state count or full equivalence without required completeness |
| Refuted bounds, alignment errors, population-to-orbit countercontrols | Exact project calculations and standard logic | Valuable negative results and methodological case studies | Separate internal correction from new literature obstruction |

Publication usefulness does not require pretending that all the ingredients are novel. A short paper presenting an unusually clear finite inequality, a reproducible exact construction, or a sharp separation between certificate classes can be worthwhile. But the pre-paper should say what the earlier literature already proves and state its increment precisely. “No exact match located in the sources checked” is the strongest available novelty statement for several branches, not “first proof.”

## 6. Breadth of the historical literature review

The GDR2 atlas dated16October contains193 source records, of which191 are external and two internal. Its normalization reports about171 external work clusters, not193 distinct papers. It records153 theorem/section inspections, five full-text inspections,14 abstract-only records,16 metadata-only records and five inaccessible records. The six substantive domain expansions cover arithmetic, dynamics, combinatorics, analysis, global structures and formal/analytic representations, with a root crosswalk over36 routes and22 retained mechanism families.

Those figures describe the **historical audit's own records**. They are not a claim that171 external works were reread during this pre-paper review, nor that all claimed applications were independently reproved. The full source index is retained inside the machine-readable bibliography so authors outside this chapter's core list are not lost. The original route-to-literature crosswalk and inspection levels remain attached to their claims. Historical records are preserved rather than silently rewritten as current verification.

The current pass concentrated primary reading on priority-critical dependencies: Terras's finite coding, Bernstein–Lagarias, Tao's exact density qualification, García–Tal's actual quantitative inequality, Sharpe's proof and credit paragraphs, Hercher's merger, Monks's gates, Gale's finite scope, Rozier's harmonic/entropy argument, and the specific number-theoretic and machine sources logged by the companion audits. Failed retrievals remain disclosed. In particular, inaccessible Chim, Yu, Everett or Curry originals are not presented as freshly read in full.

## 7. Suggested acknowledgment and citation practice

A suitable starting acknowledgment is:

> This research programme was directed by Ethan Walker, whose questions shaped its source-visible accounting, survivor-versus-integer distinction, arithmetic-driver/observer comparisons, and integration of symbolic certificates with a full-conjecture machine goal. The work was developed with AI assistance. Its mathematical foundations and immediate inspirations are credited at the points of use, including Terras and Everett, Bernstein and Lagarias, García and Tal and their Heppner input, Michael Sharpe, Tao, Hercher, the Monks authors, Gale, and the Diophantine, automata and Busy Beaver contributors identified in the bibliography. These acknowledgments do not imply endorsement or external peer review.

For a final paper, replace broad acknowledgments with precise theorem-level citations wherever a proof imports a result. Preserve discovery, analysis, formalization and exposition credits separately. Pin mutable code when possible. State whether a formal proof was actually built. Do not infer publication dates from upload dates, equate a public repository with a refereed article, or convert “inspired by” into “proved by.” Where the record does not establish an origin, say so.

## 8. Core reference register

The entries below give concise navigation. The machine-readable bibliography contains the full claim associations, inspection limitations, local hashes where available and the historical atlas. A listed reference is not automatically an imported theorem.

- **[L01]** Riho Terras. *A stopping time problem on the positive integers* (1976). [Source](https://matwbn.icm.edu.pl/ksiazki/aa/aa30/aa3034.pdf). Inspection: Primary scan downloaded; OCR generated; visually inspected printed pp.242–243, Theorems1.1–1.2 and Cor1.3–1.4. Introduction and density discussion read; not whole paper independently reproved.

- **[L02]** Riho Terras. *On the existence of a density* (1979). [Source](https://matwbn.icm.edu.pl/ksiazki/aa/aa35/aa3518.pdf). Inspection: Both pages OCR-read, printed p101 visually inspected; statement and short proof checked.

- **[L03]** C. J. Everett. *Iteration of the number-theoretic function f(2n)=n, f(2n+1)=3n+2* (1977). [Source](https://doi.org/10.1016/0001-8708(77)90087-1). Inspection: Original publisher retrieval403; no original-proof inspection this pass.

- **[L04]** Daniel J. Bernstein, Jeffrey C. Lagarias. *The 3x+1 conjugacy map* (1996). [Source](https://websites.umich.edu/~lagarias/doc/bernstein.pdf). Inspection: Primary PDF introduction pp1–3 and displayed conjugacy/series/Periodicity Conjecture inspected.

- **[L05]** Alex V. Kontorovich, Jeffrey C. Lagarias. *Stochastic Models for the 3x+1 and 5x+1 Problems* (2010). [Source](https://arxiv.org/abs/0910.1944). Inspection: Primary2009 manuscript §§1–2, Theorems2.1–2.2 read now; further §§3.1–3.2 inspection recorded in historical atlas.

- **[L06]** Terence Tao. *Almost all orbits of the Collatz map attain almost bounded values* (2022). [Source](https://arxiv.org/abs/1909.03562). Inspection: Primary v6 HTML Theorem1.3, Remark1.4, Syracuse §1.2, affine identity1.7 and parity-cylinder discussion inspected; journal2022 and v7 historical inspections distinguished.

- **[L07]** Manuel V. P. Garcia, Fabio A. Tal. *A note on the generalized 3n+1 problem* (1999). [Source](https://doi.org/10.4064/aa-90-3-245-250). Inspection: Entire six-page primary PDF text read; Lemmas1–3, Prop1–2, Theorem1/eq6, Cor1 checked; cited Heppner original not reread.

- **[L08]** E. Heppner. *Eine Bemerkung zum Hasse–Syracuse Algorithmus* (1978). [Source](https://doi.org/10.4064/aa-90-3-245-250). Inspection: Bibliography and attributed Proposition1 in García–Tal inspected; original article not retrieved.

- **[L09]** Michael Sharpe, Collatz proof project (manuscript byline). *Reciprocal Summability of Every Unbounded Natural Collatz Orbit: A Lean Proof* (2026). [Source](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/paper/orbit_summability.tex). Inspection: Full TeX source read at pinned commit. Root inspected OrbitPacking.lean; no local Lean build or kernel replay here.

- **[L10]** Michael Sharpe, Collatz proof project (manuscript byline). *Classification of Positive Natural Collatz Seeds with Mechanical Parity Itineraries* (2026). [Source](https://github.com/msharpe248/collatz/blob/main/paper/mechanical_classification.tex). Inspection: Full TeX theorem/definition/proof read from main; pinned-path fetch failed; current-source snapshot not same verified pin as L09. No Lean build.

- **[L11]** Michael Sharpe. *DefectHeight.lean* (2026). [Source](https://github.com/msharpe248/collatz/blob/main/lean/Collatz/DefectHeight.lean). Inspection: Source inspected by legacy chapter auditor; no Lean build.

- **[L12]** Pulowski (MathOverflow display name). *Is it known that a divergent Collatz trajectory must have summable reciprocals?* (2026). [Source](https://mathoverflow.net/questions/513539). Inspection: Full question text read; page says Jul24, repository dates observation July2026. Identity beyond displayed name not inferred.

- **[L13]** Christian Hercher. *There are no Collatz m-Cycles with m≤91* (2023). [Source](https://arxiv.org/abs/2201.00406). Inspection: Primary v3 PDF Lemma8, Lemma9 full proof pp4–5, Remark10 and cycle theorem scope inspected.

- **[L14]** Kenneth M. Monks. *The sufficiency of arithmetic progressions for the 3x+1 conjecture* (2006). [Source](https://monks.scranton.edu/files/pubs/SufficiencyRev4.pdf). Inspection: Historical atlas AN05/GS01 records Theorem1.1, inverse formulas and proof inspection; not newly reopened by attribution auditor.

- **[L15]** Keenan Monks, Kenneth G. Monks, Kenneth M. Monks, Maria Monks. *Strongly sufficient sets and the distribution of arithmetic sequences in the 3x+1 graph* (2013). [Source](https://arxiv.org/abs/1204.3904). Inspection: Primary PDF Cor5.8 and §6 definitions/Prop6.3/Thm6.4 inspected. Served PDF title date2024 differs from publication2013; publication year retained.

- **[L16]** David Gale. *A theorem on flows in networks* (1957). [Source](https://msp.org/pjm/1957/7-2/pjm-v7-n2-p04-p.pdf). Inspection: Primary §1–2 definitions, Feasibility Theorem and minimum-cut interface read.

- **[L17]** Kwok Chi Chim. *Lower bounds for linear forms in two p-adic logarithms* (2025). [Source](https://doi.org/10.1016/j.jnt.2024.07.012). Inspection: Author/institution abstract and publication metadata inspected; linked PDF403. Older project carries specific application audit; no new full theorem inspection here.

- **[L18]** Kunrui Yu. *p-adic logarithmic forms and group varieties. II* (1999). [Source](https://doi.org/10.4064/aa-89-4-337-378). Inspection: Original publisher metadata verified by Antihydra auditor; original PDF403, not reread.

- **[L19]** Bernadette Faye, Florian Luca, Volker Ziegler. *On a variant of Pillai’s problem with factorials and S-units* (2024). [Source](https://link.springer.com/article/10.1007/s11139-023-00787-1). Inspection: Theorem4/eq5 inspected and constant specialization checked by Antihydra auditor; author metadata reopened directly.

- **[L20]** Jan-Hendrik Evertse, Hans Peter Schlickewei, Wolfgang M. Schmidt. *Linear equations in variables which lie in a multiplicative group* (2002). [Source](https://arxiv.org/abs/math/0409604). Inspection: Primary introduction/Theorem1.1 and nondegeneracy/dimension discussion inspected now; not full proof.

- **[L21]** Jason P. Bell, Jeffrey Diller, Mattias Jonsson, Holly Krieger. *Birational maps with transcendental dynamical degree* (2024). [Source](https://api.repository.cam.ac.uk/server/api/core/bitstreams/c62d2578-8916-4829-97b1-20459f149466/content). Inspection: Primary institutional PDF Theorem4.1 p19 and Theorem4.4 p21 inspected by Antihydra auditor.

- **[L22]** Alan Cobham. *On the base-dependence of sets of numbers recognizable by finite automata* (1969). [Source](https://research.ibm.com/publications/on-the-base-dependence-of-sets-of-numbers-recognizable-by-finite-automata). Inspection: Primary IBM publication abstract/metadata inspected; original full proof not reread.

- **[L23]** Jean-Paul Allouche, Jeffrey Shallit. *Automatic Sequences: Theory, Applications, Generalizations* (2003). [Source](https://www.cambridge.org/core/books/abs/automatic-sequences/cobhams-theorem/C070C48818D5A1C8602FE789386D264D). Inspection: Chapter11 pointer recorded by Pass03 source audit; no claim full book inspected.

- **[L24]** Hong-Yi Chen, Byron Cook, Carsten Fuhs, Kaustubh Nimkar, Peter O’Hearn. *Proving nontermination via safety* (2014). [Source](https://discovery.ucl.ac.uk/1455006/1/TACAS14-nontermination.pdf). Inspection: Section2 recurrence-set definitions checked by machine auditor.

- **[L25]** Krishnendu Chatterjee, Ehsan Kafshdar Goharshady, Petr Novotný, Đorđe Žikelić. *Proving Non-termination by Program Reversal* (2021). [Source](https://arxiv.org/abs/2104.01189). Inspection: Primary abstract and author list inspected; detailed completeness hypotheses not independently audited in this pass.

- **[L26]** Emre Yolcu, Scott Aaronson, Marijn J. H. Heule. *An Automated Approach to the Collatz Conjecture* (2023). [Source](https://arxiv.org/abs/2105.14697). Inspection: Primary abstract/metadata reopened; chapter auditors inspect exact rewrite system and semantics; source-level credit recorded.

- **[L27]** Cristian S. Calude. *The Collatz Problem, the Halting Problem and Randomness* (2019). [Source](https://www.cs.auckland.ac.nz/~cristian/collatzproblem.pdf). Inspection: Complete two-page primary note read; Question1 and its preceding nonconstructive-existence claim directly inspected.

- **[L28]** Pascal Michel. *Simulation of the Collatz 3x+1 function by Turing machines* (2014). [Source](https://arxiv.org/abs/1409.7322). Inspection: Primary arXiv metadata/abstract read; pointwise simulator distinction verified; not full machine proofs reread.

- **[L29]** GettysburgResearch (repository account). *Collatz research RESULTS_CATALOG* (date not independently fixed). [Source](https://github.com/GettysburgResearch/collatz/blob/main/research/RESULTS_CATALOG.md). Inspection: Historical citation only; moving catalog not exhaustively audited.

- **[L30]** Gilles Christol, Teturo Kamae, Michel Mendès France, Gérard Rauzy. *Suites algébriques, automates et substitutions* (1980). [Source](https://numdam.org/articles/10.24033/bsmf.1926/). Inspection: Primary record reopened by closure auditor; exact theorem interfaces recorded historically.

- **[L31]** Boris Adamczewski, Jason P. Bell. *A problem around Mahler functions* (2017). [Source](https://arxiv.org/abs/1303.2019). Inspection: Primary title corrected by closure auditor; historical theorem-level inspection in atlasFA09.

- **[L32]** Pablo Shmerkin, Boris Solomyak. *Zeros of {-1,0,1}-power series and connectedness loci for self-affine sets* (2006). [Source](https://arxiv.org/abs/math/0504545). Inspection: Primary record reopened by closure auditor; documentary use in faithful-jet source verified.

- **[L33]** David Fernández-Duque, Andreas Weiermann. *A Walk with Goodstein* (2024). [Source](https://arxiv.org/abs/2004.09110). Inspection: Primary record reopened by closure auditor; project source explicitly records comparison.

- **[L34]** Nachum Dershowitz, Zohar Manna. *Proving Termination with Multiset Orderings* (1979). [Source](https://www.cs.tau.ac.il/~nachumd/papers/LNCS/Multisets.pdf). Inspection: Primary theorem source reopened by closure auditor.

- **[L35]** Shawn Ligocki. *BB(6) is Hard (Antihydra)* (2024). [Source](https://www.sligocki.com/2024/07/06/bb-6-2-is-hard.html). Inspection: Primary author account exact macros/credit checked by Antihydra auditor.

- **[L36]** BBChallenge contributors. *Antihydra* (date not independently fixed). [Source](https://bbchallenge.org/antihydra). Inspection: Table/arithmetic/status checked21Oct2026 by Antihydra auditor.

- **[L37]** Shawn Ligocki. *BB(2,5) is Hard (Hydra)* (2024). [Source](https://www.sligocki.com/2024/05/10/bb-2-5-is-hard.html). Inspection: Primary author account read by Antihydra auditor.

- **[L38]** Pascal Michel. *Behavior of Busy Beavers* (date not independently fixed). [Source](https://bbchallenge.org/~pascal.michel/beh). Inspection: Champion table/macros/counts and analysis credits inspected by Antihydra auditor; precise discovery year withheld pending date discrepancy.

- **[L39]** BBChallenge collaboration, mxdys (announcement). *We have proved BB(5)=47,176,870* (2024). [Source](https://discuss.bbchallenge.org/t/july-2nd-2024-we-have-proved-bb-5-47-176-870/237). Inspection: Official announcement and contributor scope checked by Antihydra auditor; no full formal project rebuild here.

- **[L40]** Jason Yuen (int-y1), Maja Kądziołka. *Skelet #33 does not halt: Coq proof* (date not independently fixed). [Source](https://discuss.bbchallenge.org/t/skelet-33-doesnt-halt-coq-proof/180). Inspection: Forum account plus Skelet33.v reset_invariant, step_reset, do_reset, E_next inspected by Antihydra auditor; no Coq build.

- **[L41]** Shawn Ligocki, Maja Kądziołka (formal proof/correction). *Skelet #34; Skelet #34 and #35 Coq proof* (2023). [Source](https://www.sligocki.com/2023/02/02/skelet-34.html). Inspection: Author account and https://discuss.bbchallenge.org/t/skelet-34-and-35-coq-proof/165 inspected by Antihydra auditor.

- **[L42]** Shawn Ligocki, Pavel Kropitz, uni-cycle, Maja Kądziołka. *Skelet #1 is infinite* (2023). [Source](https://www.sligocki.com/2023/03/13/skelet-1-infinite.html). Inspection: Primary account checked by Antihydra auditor; page includes later updates.

- **[L43]** Chris Xu. *Skelet #17 and the fifth Busy Beaver number* (2024). [Source](https://arxiv.org/html/2407.02426v1). Inspection: Primary arXiv metadata/abstract verified directly; relevant macro/endgame sections read by Antihydra auditor.

- **[L44]** Newcomb Greenleaf. *Proof for the chaotic four-state machine* (1992). [Source](https://turbotm.de/~heiner/BB/TM4-proof.txt). Inspection: Full primary proof text read by Antihydra auditor.

- **[L45]** Julien Cassaigne, Bastiàn Espinoza, Michel Rigo, Manon Stipulanti. *Symbols frequencies in the Thue–Morse word in base3/2 and related conjectures* (2026). [Source](https://arxiv.org/abs/2602.21895). Inspection: Primary arXiv abstract/metadata read directly; population sequence frequency1/2 distinguished from fixed Antihydra branch.

- **[L46]** Mélodie Andrieu, Shalom Eliahou, Léo Vivion. *A Normality Conjecture on Rational Base Number Systems* (2025). [Source](https://arxiv.org/html/2510.11723v2). Inspection: Primary metadata/abstract read directly; companion auditor opened v2HTML and normality conjecture. Not full theorem-by-theorem audit.

- **[L47]** Lubor Brim, Jakub Chaloupka, Laurent Doyen, Raffaella Gentilini, Jean-François Raskin. *Faster Algorithms for Mean-Payoff Games* (2011). [Source](https://lsv.ens-paris-saclay.fr/~doyen/papers/Faster_Algorithms_for_Mean-Payoff_Games.pdf). Inspection: Introduction and progress-measure context inspected by Antihydra auditor; related method, not documented original inspiration.

- **[L48]** Edmund M. Clarke, Orna Grumberg, Somesh Jha, Yuan Lu, Helmut Veith. *Counterexample-Guided Abstraction Refinement* (2000). [Source](https://web.stanford.edu/class/cs357/cegar.pdf). Inspection: Primary methodological description inspected by Antihydra auditor; similarity does not prove historical influence.

- **[L49]** Olivier Rozier. *The 3x+1 problem: a lower bound hypothesis* (2017). [Source](https://www.ipgp.fr/~rozier/pub/LBHv4.pdf). Inspection: Primary author PDF §§2.1–2.2, Lemma2.5 and full Theorem2.6 proof pp5–7 inspected; introduction explicitly credits Lagarias and Terras/Everett.

- **[L50]** Michael John Curry. *An Explicit Windowed Sparsity Bound for Divergent 3x+1 Orbits, with Logarithmic-Floor Exclusion beyond the Harmonic Barrier* (2026). [Source](https://doi.org/10.5281/zenodo.22087163). Inspection: DOI and Zenodo record failed to open currently, as in October15 audit. Title/attribution via De Jesús repository; original not read.

- **[L51]** Elias De Jesús. *A Global Occupation Conjecture for the Accelerated 3x+1 Map: Divergent-Orbit Sparsity, Exact Realizers, and the Moving-Anchor Problem; companion EOC Lean Verification repository* (2026). [Source](https://github.com/innerlightr-wq/eoc-lean-verification). Inspection: Current README sections on open frontier, manuscript highlights, literature and citations inspected. No Lean build; manuscript itself not inspected.

- **[L52]** Shigeki Akiyama, Masayuki Shirasaka. *Recursively renewable words and coding of irrational rotations* (2007). [Source](https://www.jstage.jst.go.jp/article/jmath/59/4/59_4_1199/_article/-char/en). Inspection: Primary journal metadata and abstract read; full theorem hypotheses not independently recertified.

- **[L53]** Fabien Durand. *A characterization of substitutive sequences using return words* (1998). [Source](https://arxiv.org/pdf/0807.3322). Inspection: Legacy auditor inspected §2.3 and Proposition6 in author arXiv posting. Not independently reread by bibliography auditor.

- **[L54]** Rohit J. Parikh. *On Context-Free Languages* (1966). [Source](https://doi.org/10.1145/321356.321364). Inspection: Original attribution identified; current original full text not inspected. Standard semilinearity theorem corroborated by Esparza et al primary abstract.

- **[L55]** Javier Esparza, Pierre Ganty, Stefan Kiefer, Michael Luttenberger. *Parikh’s Theorem: A simple and direct automaton construction* (2011). [Source](https://arxiv.org/abs/1006.3825). Inspection: Closure auditor inspected primary arXiv abstract and metadata; semilinearity of context-free Parikh images explicitly stated.


### Final-cutoff addition from Navigation 14

**[L56]** Dimitri Bertsekas, *Affine Monotonic and Risk-Sensitive Models in Dynamic Programming* (2016; revised 2017), [primary arXiv record](https://arxiv.org/abs/1608.01393). Navigation 14 cites this as a methodological comparison for affine Bellman inequalities and policy iteration. The abstract and metadata were read in this audit; the full paper was not. The band-envelope theorem rests on its displayed rational edge inequalities, checked directly, not on an uninspected theorem from this paper. This addition brings the core reference register to 56; the historical atlas remains separately classified. Attribution record A33 preserves this distinction.
