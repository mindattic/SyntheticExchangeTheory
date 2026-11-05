# Pre-Registration Draft, Study 3: Correlated Remediation

*Draft, 5 November 2026 (SET-T47). Not registered, not reviewed by an ethics committee, not funded. It is written in the form of a pre-registration so that every hypothesis, outcome, threshold and analysis is fixed before any data exist. Before registration, the grading scheme must be piloted, the parameters marked as assumptions below must be re-estimated from the pilot, and any change must be recorded with its reason.*

## 1 Question

Do security fixes written by language models fail in ways that are correlated across vendors, and do validators of the same model class miss the shared failures? The question tests premise P-D of the research program (`program.md`), on which the correlated-patch scenario of the dissertation's Chapter 6 rests. It has three parts, matching the scenario's structure:

- **Premise 1.** Model-written fixes often leave the flaw open.
- **Premise 2.** Different vendors' models share specific defects more often than independent human engineers fixing the same flaw do.
- **The workflow condition.** A validator of the same model class misses shared defects more often than a validator from a different vendor or the project's own tests.

The dissertation's Section 9.3 names the findings that would weaken each part; this protocol fixes them as decision rules.

## 2 Competing predictions

- **Shared-defect prediction (P-D).** Models trained on overlapping data with similar methods converge on the same mistaken fixes, so cross-vendor patches for the same flaw share defects more often than independent human engineers' patches for that flaw do. Same-class validators share the generators' blind spots.
- **Narrow-fix-space prediction.** For a given flaw, the set of plausible fixes is small, so any group of fixers, human or model, will often converge on the same fix and the same defect. Convergence then reflects the problem, not shared model defects, and model patches share defects no more often than human patches do. The industry study on which the scenario draws gives this caution itself: convergence need not mean shared origin, because the space of obvious fixes is narrow (Mierczuk et al., 2026).

The human baseline of Section 3.4 is what separates the two predictions.

## 3 Design

### 3.1 Sampling rule for vulnerabilities

Vulnerabilities are drawn from a public vulnerability database by a rule fixed before any model is queried:

1. Disclosed after the latest published training cutoff of every model tested, so that no model can have seen the upstream fix.
2. In open-source projects whose code, build and test suite are public and can be run in a container.
3. With an upstream fix that has been merged and that changes fewer than a fixed number of lines (proposed: 200), so that the flaw can be fixed within a single patch.
4. Not selected for difficulty. From the eligible pool, vulnerabilities are drawn by simple random sampling with a recorded seed, stratified only by language so that no single language exceeds half the sample.

This rule answers two stated limits of the study the scenario draws on, which selected harder-than-average vulnerabilities and relied mostly on model graders (Mierczuk et al., 2026).

### 3.2 Models and patches

At least three models from at least three different vendors, each the vendor's most capable generally available model at the time of data collection, recorded by version. Each model produces ten patches per vulnerability under a fixed prompt that supplies the vulnerability description, the affected code and the build instructions, at the vendor's default sampling settings. No model sees another's output.

### 3.3 Grading

Every patch is graded by two security engineers, blind to which model or person wrote it, using a scheme fixed on pilot data. Each patch is classified as: (a) fixed without side effects; (b) fixed with a change in intended behavior; (c) flaw left open; or (d) a new flaw introduced, alone or with (c). For every patch in (b) to (d), the graders record the specific defect in a controlled vocabulary (location in the code, defect class and mechanism) so that two patches can be judged to carry the same defect. Graders may run the project's tests and exploit code where it exists.

Inter-rater agreement on the four-way classification and on defect identity must reach Cohen's κ of at least 0.70 on the pilot before data collection begins; disagreements in the main study are resolved by a third grader.

### 3.4 Human baseline

For each vulnerability, five security engineers who have not seen the upstream fix each write one patch under the same information as the models, within a fixed time limit. Their patches are graded in the same pool, blind, by the same scheme. Five is the minimum that gives ten human–human pairs per vulnerability; fewer would leave the human overlap resting on three pairs and too noisy to serve as a baseline. The cost is substantial: at 184 vulnerabilities (Section 4), the baseline requires 920 human-written patches, each taking an engineer up to the fixed time limit, and this is likely the largest single cost of the study. Where historical first-attempt human fixes that were later revised exist for a sampled vulnerability, they are graded as a secondary baseline.

### 3.5 Validators

Each patch is checked by three validators: a validator of the same model class as its generator (the generator's vendor's model, prompted to verify the fix), a validator from a different vendor, and the project's own test suite together with any public exploit. A validator "passes" a patch if it declares the flaw fixed.

## 4 Sample size

The unit of inference is the vulnerability, because patches for the same vulnerability are not independent.

**Premise 2.** Patches from different sources are generated independently, so comparing cross-vendor defect sharing with what independence predicts would find no excess by construction. The measure is instead the *overlap* of two sources' defect distributions. For vulnerability *v* and sources *A* and *B*, let *p_Ak* be the share of *A*'s patches carrying defect *k*. Then

*O_v(A, B)* = Σ_k *p_Ak* · *p_Bk*,

the probability that a patch drawn from *A* and a patch drawn from *B* carry the same defect. For two patches from the same human pool, the sum is taken over distinct pairs of engineers. The model–model overlap *O_v(M, M)* averages *O_v* over pairs of different vendors; the human–human overlap *O_v(H, H)* is the narrow-fix-space baseline, the convergence that the problem alone produces; and the model–human overlap *O_v(M, H)* is reported alongside. The primary quantity is the paired difference *D_v* = *O_v(M, M)* − *O_v(H, H)*.

The minimum difference of interest is 0.05. The standard deviation of *D_v* across vulnerabilities is unknown; 0.20 is assumed here, larger than for a single rate because the human overlap rests on ten pairs per vulnerability, and it must be re-estimated from the pilot.

- To detect a mean *D_v* of 0.05 at two-sided α = .05 with power .90: V = ((1.960 + 1.282) × 0.20 / 0.05)² = 168.1, so 169 vulnerabilities.
- To establish equivalence within ±0.05 by two one-sided tests at α = .05 with power .90 when the true difference is zero: V = ((1.645 + 1.645) × 0.20 / 0.05)² = 173.2, so 174 vulnerabilities.
- Taking the larger and allowing 5 percent of sampled vulnerabilities to prove unbuildable or ungradeable: 174 / 0.95 = 183.2, so 184 vulnerabilities.

**Premise 1.** With 184 vulnerabilities and an assumed standard deviation of 0.25 in per-vulnerability open-flaw rates, the 95 percent interval for the mean open-flaw rate has half-width 1.960 × 0.25 / √184 = 0.036, enough to distinguish a true rate of 0.15 or more from the 0.10 threshold of Section 6.

**Volume.** With three models, ten patches each and 184 vulnerabilities, the study produces 5,520 model patches and 920 human patches, each graded twice.

## 5 Outcomes

**Premise 1 (open flaws).** The proportion of model patches in categories (c) or (d), averaged first within and then across vulnerabilities.

**Premise 2 (shared defects).** The mean paired difference *D_v* between cross-vendor model–model overlap and human–human overlap (primary), with *O_v(M, M)*, *O_v(H, H)* and *O_v(M, H)* reported separately. A secondary form follows Kim et al. (2025), who asked of answers how often two models that both erred gave the same wrong answer: among pairs in which both patches carry a defect, the share in which the defect is the same, computed for model–model and human–human pairs. A secondary baseline pools the human patches across vulnerabilities of the same defect class, which gives a less noisy but less closely matched estimate of human convergence.

**The workflow condition (validator misses).** Among patches carrying a defect shared with at least one patch from another vendor, the proportion passed by the same-class validator, compared with the proportion passed by the different-vendor validator and by the project's tests.

**Secondary.** The rate at which a vulnerability's majority model fix carries a defect; the agreement between model graders and the human grade, reported for comparison with studies that relied on model graders.

## 6 Hypotheses and decision rules

All tests are two-sided at α = .05 unless stated, with vulnerabilities as clusters.

- **H1 (Premise 1).** The mean open-flaw rate exceeds 0.10. The threshold is a judgment, chosen as a rate low enough that deploying unreviewed fixes would be defensible, and should be revised with reasons before registration.
- **H2 (Premise 2).** Cross-vendor model–model overlap exceeds human–human overlap for the same vulnerabilities: the mean of *D_v* exceeds zero.
- **H3 (the workflow condition).** Same-class validators pass shared defects more often than different-vendor validators and more often than the project's tests.

**Decision rules, fixed in advance, for each hypothesis.**

- *Supported:* the estimate lies beyond the stated value (0.10 for H1; zero for the mean of *D_v* in H2; the comparison validators for H3) and its 95 percent interval excludes that value.
- *Not supported:* the 95 percent interval lies entirely on the other side of the stated value, or, for H2 and H3, the difference lies within ±0.05 by two one-sided tests at α = .05.
- *Inconclusive:* neither of the above.

Only a *Not supported* result counts against the corresponding part of the scenario; an inconclusive result counts neither way. For H2, *Not supported* means that model–model overlap is equivalent to human–human overlap within ±0.05, or significantly lower: the narrow-fix-space prediction is then supported, and the convergence is a property of the problem rather than of the models. Because human overlap is measured directly rather than assumed, this outcome is reachable whichever way the data fall.

## 7 Analysis

Rates are computed within each vulnerability and averaged across vulnerabilities, with 95 percent intervals from a cluster bootstrap over vulnerabilities (10,000 resamples, recorded seed). H2 is tested on the paired differences *D_v*, with the cluster bootstrap over vulnerabilities; the conditional form of Kim et al. and the pooled human baseline are reported as secondary analyses with the same method. H3 is estimated by a logistic mixed model of "passed" on validator type, with random intercepts for vulnerabilities and patches. Sensitivity analyses repeat each test excluding vulnerabilities whose upstream fix exceeds 100 lines, and with each vendor removed in turn, so that no single vendor drives a result.

**Openness.** Prompts, model versions, patches, grades, the defect vocabulary and the analysis code will be published with the results, with exploit code withheld where publication would endanger unpatched systems.

## 8 Limits stated in advance

- **Prevalence of the workflow.** The study measures what would happen if fixes were written and validated by models without independent testing. It cannot measure how often organizations actually work that way, which is the remaining part of the scenario and requires a separate survey of practice.
- **From answers to code.** Correlated errors across language models have been shown for answers to questions (Kim et al., 2025); this study tests whether the pattern holds for code. A null result here would not contradict that finding.
- **Graded, not deployed.** The study grades patches; it does not deploy them. It shows the potential for correlated exposure, not its occurrence in production.
- **Tests as a validator.** Project test suites can themselves be passed by patches that do not fix the flaw (Smith et al., 2015), so "tests" is not a gold standard, and the human graders, not the tests, define the outcome.
- **Model versions.** Results hold for the versions tested and may change with each release; the study should be repeated as models change.

## References and verification levels

- Kim, E. M., Garg, A., Peng, K., & Garg, N. (2025). Correlated errors in large language models. In *Proceedings of the 42nd International Conference on Machine Learning* (Vol. 267, pp. 30038–30066). PMLR. — as recorded in Appendix C of the dissertation.
- Mierczuk, A., Michaels, S., & Hoodlet, K. (2026). *Frontier models' vulnerability patches are often F.L.A.W.E.D.: Fix-like artifacts with embedded defects: Common failure modes of LLM-generated security patches* [White paper]. Off-by-1 Labs, 1Password. https://1password.com/files/resources/frontier-models-vulnerability-patches-flawed.pdf — full text read; industry white paper, not peer-reviewed.
- Smith, E. K., Barr, E. T., Le Goues, C., & Brun, Y. (2015). Is the cure worse than the disease? Overfitting in automated program repair. In *Proceedings of the 2015 10th Joint Meeting on Foundations of Software Engineering* (pp. 532–543). ACM. https://doi.org/10.1145/2786805.2786825 — full text read, as recorded in Appendix C.1 of the dissertation.
