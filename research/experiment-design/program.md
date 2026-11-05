# A Staged Empirical Program for Synthetic Exchange Theory

*Draft, 5 November 2026 (SET-T46). This document is separate from the dissertation, which remains theoretical (Sections 7.5 and 9.3 of the dissertation state what a test would require). Nothing here has been registered, funded, approved by an ethics board, or run. All numbers are proposals with their assumptions stated; the sample sizes are computed by `power.py` in this folder and can be reproduced by running it.*

## 1 Why a staged program rather than a single pilot

The pilot removed from the dissertation on 2 November 2026 (archived in `archive/pilot-2026-11-02/`) proposed one closed agrarian settlement, run for at least five years with a population in the low hundreds, as the test of the framework. That design has three weaknesses that a staged program avoids.

First, it is the most expensive and slowest test available, and it cannot begin until land, a computing facility, an exit guarantee and a comparison settlement have been financed. Its own text records that no budget or power analysis was supplied.

Second, it does not test the parts of the theory that are most exposed to refutation. Its randomized comparison isolated the designed dependence of Proposition 4; by its own statement it did not test the priority of exit or the sufficiency conjecture, because withholding the floor or exit from residents would be unethical. It also rested on a premise it did not test separately: that the quality of what people contribute depends on the terms they receive.

Third, a single settlement is not a unit of inference. The archived analysis plan says so and confines confirmatory claims to within-settlement randomization.

The theory's empirical content can instead be divided into separable premises, each of which can be tested by a smaller study that carries minimal risk to participants and could be run within a year. The settlement study then becomes the last stage, worth its cost only if the earlier stages do not refute the premises it depends on.

## 2 What is and is not testable

The dissertation's propositions are of two kinds, and only one kind can be tested.

**Definitional claims.** Proposition 1 and the corresponding clause of Proposition 3 (clauses C(ii) and E(i) are defined by the same condition, so a failure of one is a failure of the other) and the necessity half of the insufficiency thesis follow from stipulated definitions (dissertation, Sections 3.4 and 3.8). No experiment can refute them; they can be criticized only by arguing that the definitions are the wrong ones, which is a philosophical question. The other clauses of Proposition 3 are not all definitional: the claim that exit only partly corrects an unfair division, because an outside option bounds the division from below but does not set it, rests on the bargaining analysis of Appendix A.3.4 and is tested as P-C below.

**Empirical premises.** The following are claims about the world, and each could be false:

- **P-A (input quality depends on terms).** People who can refuse and withdraw without loss contribute information that is more reliable, more varied and more predictive of human preference than people who cannot. This is the premise on which Proposition 4's self-enforcement rests (dissertation, Sections 3.5 and 3.11).
- **P-B (dependence is domain-specific).** Fresh human data adds more to a model's performance where the target is human meaning, preference or value than where correctness can be checked mechanically (the grounding assumption as narrowed in Chapter 2).
- **P-C (the floor works through the disagreement payoff).** A guaranteed floor received during disagreement shifts the division of surplus toward the weaker party even when no outside option binds, while an outside option shifts it only when it binds (Appendix A.3.4).
- **P-D (correlated remediation).** Model-written security fixes often leave flaws open (Premise 1), different vendors' models share defects more often than independence predicts (Premise 2), and same-class validators miss the shared defects (the workflow condition) (Chapter 6).
- **P-E (concealment prevents blocs).** Concealing whether delegates are people or synthetic systems reduces voting along those lines, and formulas resist tailoring better than figures (Chapter 5).
- **P-F (the designed incentive).** A system whose operator's resources depend on consented participation serves participants better than the same system without that dependence (Proposition 4; the archived pilot's H2).

P-A, P-C, P-D and P-E can be tested now, at modest cost. P-B needs compute but no human subjects beyond data collection. P-F needs the long study.

## 3 The studies

Each study below names its premise, its design, its primary outcome, the result that would count against the premise, and its principal limit. Studies 1, 3 and 4 can run in parallel; Study 2 can run alongside them; Study 5 follows Study 4's procedures; Study 6 is conditional.

### Study 1: Terms and input quality (P-A)

**Design.** An online, pre-registered, between-participants experiment with a 2 × 2 factorial design. Participants make preference judgments and give short written reasons on value-laden questions, the domain in which the grounding assumption says people are the only adequate source. The first factor is the *floor*: in one arm, participants' payment is guaranteed whether or not they complete the contribution task; in the other, a base fee is paid to everyone and the remainder only on completion. The second factor is the *withdrawal window*: in one arm, participants may withdraw their contributed data with a single action at any time until data collection ends; in the other, only until they submit. Data protection law that rests on consent requires withdrawal to be as easy as consent, so the study cannot offer an irrevocable licence; if the closed window is not lawful under the study's basis, the second factor is dropped. The full protocol is in `prereg-study-1.md`.

**Primary outcomes.** The reliability of each participant's signal, measured as agreement between their judgments on twenty items presented twice, unannounced and separated by other items, estimated in a multilevel model; and, because the guaranteed arm may stop without loss, the completion rate, analyzed alongside reliability so that a difference in who is analyzed is not mistaken for a difference in quality. A random subsample repeats the items a week later, which removes the inflation that recall of the first answer causes within a session.

**Against the premise.** If the floor arm's reliability is equivalent to the conditional arm's within a pre-registered margin, or significantly lower, P-A is not supported in this domain. An inconclusive result counts neither way. Standard incentive reasoning predicts the opposite of P-A (conditional pay may raise effort), so the study discriminates between two named predictions rather than looking for an effect only one theory expects.

**Limit.** The study cannot reproduce the stakes the theory concerns. Losing a study payment is not falling below a survival floor, and ethics forbids inducing that. A null result in this study would weaken P-A but not refute it for real dependence; a positive result would show the mechanism operates at low stakes.

### Study 2: Measuring dependence (P-B)

**Design.** A computational study. Small open-weight models are fine-tuned for a fixed number of rounds in two domains: one with mechanically verifiable answers (arithmetic word problems with checked solutions) and one whose target is human preference (pairwise preference judgments from a held-out human panel). In each round, the training mix is either refreshed with new human-generated data or replenished with the model's own outputs, filtered as well as the domain allows (by verifier in the first domain, by self-judgment in the second). Because a verifier is a better filter than self-judgment by construction, each round holds the compute budget and the number of training examples fixed, and a condition with no filter is added in both domains. Accumulation, not replacement, is the regime, so that the study tests the narrowed premise and not the collapse result already known (Gerstgrasser et al., 2024; Kazdan et al., 2024).

**Primary outcome.** The marginal gain on held-out evaluation from fresh human data relative to self-generated data, per round, in each domain, over at least five independent seeds.

**Against the premise.** P-B is not supported if the upper bound of the 95 percent interval, across seeds, for the difference between domains in the marginal value of fresh human data falls below the pre-registered minimum effect of interest.

**Limit.** Small models may not behave like frontier models, and the preference domain is one operationalization of "human meaning, preference or value." A result supporting P-B at small scale is suggestive; a result against it would be harder to dismiss, since small models are where self-training has been easiest to show helping.

### Study 3: Correlated remediation (P-D)

**Design.** A benchmark of security vulnerabilities of *ordinary* difficulty (sampled from a public vulnerability database by a rule fixed in advance, not chosen for difficulty, and limited to vulnerabilities disclosed after every tested model's training cutoff so that no model has seen the fix), with independent human grading. Models from at least three vendors each produce several patches per vulnerability. Graders blind to the model classify each patch: fixed without side effects, fixed with behavior change, flaw left open, or new flaw introduced; and they record the specific defect where one exists. The same patches are then checked by a validator of the same model class, by a validator from a different vendor, and by the project's own tests.

**Primary outcomes.** (1) The rate at which patches leave the flaw open (Premise 1). (2) For pairs of patches from different vendors on the same vulnerability, the rate at which both carry the same defect, compared with the rate expected if each vendor's defects were independent, computed within each vulnerability so that a concentration of defects in harder vulnerabilities is not mistaken for correlation, and compared also with the rate at which historical human-written first-attempt fixes for the same vulnerabilities shared a defect (Premise 2). The patch study's authors caution that convergence need not mean shared origin, because the space of obvious fixes is narrow (Mierczuk et al., 2026); the human baseline measures that narrowness. (3) The miss rate of same-class validators on shared defects, compared with different-class validators and tests (the workflow condition).

**Against the premises.** As stated in the dissertation's Section 9.3: Premise 1 is weakened if, on vulnerabilities of ordinary difficulty, model-written fixes rarely leave the flaw open (the threshold proposed here, under 10 percent, is a judgment, chosen as a rate low enough that unreviewed deployment would be defensible, and should be revised with reasons before registration); Premise 2 is weakened if cross-vendor shared-defect rates do not exceed the within-vulnerability independence baseline or the human baseline; the workflow condition is weakened if same-class validators catch shared defects as often as other checks. The study's design responds to the stated limits of the industry study on which the scenario rests, which chose harder-than-average vulnerabilities and relied mostly on model graders (Mierczuk et al., 2026), and it extends to code the question that Kim et al. (2025) asked of answers.

**Limit.** The prevalence of the fully unverified workflow is a separate question, answerable only by a survey of practice; a benchmark cannot measure it.

### Study 4: Floor versus outside option (P-C)

**Design.** A laboratory bargaining experiment with real payments, in which pairs divide a sum over alternating offers, and disagreement in each round costs the weaker party a fixed amount (the laboratory analogue of the survival constraint of Appendix A.3.2). The role of weaker party is assigned at random, each pair plays once (no rematching), and the option values are fixed relative to the equal split the model predicts without protection. Four arms: (1) no protection; (2) an outside option set below the equal split, so that theory predicts it does not bind; (3) an outside option set above it, so that it binds; (4) a floor paid to the weaker party in every round of disagreement, removing the per-round cost. The design follows the precedent of the outside-option experiment of Binmore et al. (1989), whose results, as recorded in the abstract, supported the strategic prediction that an outside option affects the bargain only when its exercise is credible.

**Primary outcome.** The weaker party's share of the sum in the agreed division.

**Predictions.** From Appendix A.3.4: arm 2 does not differ from arm 1; arm 3 raises the weaker party's share to at least the option's value; arm 4 raises it relative to arm 1 even though no option binds.

**Against the premise.** P-C is not supported if arm 4 does not exceed arm 1, or if arm 2 raises the share as much as arm 3 (which would mean options act as disagreement payoffs, contrary to the strategic prediction the appendix relies on). Detecting a difference of 0.05 in share, with an assumed standard deviation of 0.15 and three planned contrasts, requires 244 pairs per arm (`power.py`). The standard deviation has no source and is an assumption; the sample size must be recomputed from a pilot before registration.

**Limit.** Laboratory bargaining over small sums is not bargaining over livelihoods. The study tests the mechanism the appendix models, not its magnitude in the world.

### Study 5: The blind convention (P-E)

**Design.** Groups of human participants, joined by delegates that are language-model agents acting on written instructions from principals who are themselves participants, choose a rule for dividing a shared endowment that will then be paid out. Arms cross *concealment* (whether participants know which delegates are people) with *form* (whether the group chooses a figure or a formula whose consequences for each member depend on facts revealed afterward). The study extends the design of Weidinger et al. (2023), in which the AI was the thing governed and, in the study where participants knew their groupmates were programs, the veil's effect on reflective endorsement was no longer detected.

**Primary outcomes.** A bloc index (the share of votes that align with the voter's kind beyond what the voter's payoff from each rule predicts), and the payoff dispersion of the adopted rule. The bloc index is identified only if payoffs and kind can be separated, so the rule sets are constructed so that each rule's payoff to a member is uncorrelated with the member's kind. Each principal instructs one delegate only, so that votes are independent.

**Against the premise.** P-E is not supported if concealment does not reduce the bloc index, or if formulas are tailored as readily as figures. With groups as the unit, detecting a standardized difference of 0.5 at 80 percent power needs 63 groups for each side of a contrast (`power.py`). Crossing the two factors would let 32 groups per cell power the main effects, but whether concealment works may depend on the form of the choice, so each simple effect of concealment (within figures and within formulas) is powered on its own: 63 groups in each of four cells, 252 in all.

**Limit.** The study must not deceive participants about whether delegates are programs, which Weidinger et al. did in most of their studies; concealment here means participants are told that some delegates are programs but not which. The synthetic delegates' behavior reflects their principals' instructions, which is the dissertation's own account of present systems (Section 3.3), so the study tests concealment among principals, not among autonomous agents.

### Study 6: The settlement study (P-F)

The archived pilot, revised in light of Studies 1 to 5, tests whether a designed dependence on consented participation makes a system serve participants better than the same system without it. It should not be registered if Study 1 finds input quality equivalent across terms or worse under fair terms, because without that premise Proposition 4 predicts no effect for the settlement to find. Since Study 1's stakes are low, that gate may be overridden by an argument, recorded before Study 1's data are analyzed, that the mechanism operates only at stakes Study 1 cannot create; an inconclusive Study 1 does not close the gate. Its budget, its power analysis and its ethics review remain prerequisites, as the archived protocol records.

## 4 Ethics common to all studies

Every study pays participants at least the platform's or laboratory's standard rate regardless of their choices; the "conditional" arm of Study 1 makes a portion of payment conditional, never the guaranteed minimum required by the ethics board. No study withholds anything a participant needs. Participants who contribute data are told that withdrawal removes their data from the study and from models trained afterward but cannot remove its influence from a model already trained, and no model is trained on contributed data until data collection has closed. Studies 1, 4 and 5 involve no deception; Study 2 involves no human participants beyond the collection of preference judgments; Study 3 involves none. Each requires review by an independent research-ethics committee before recruitment. Pre-registration of hypotheses, outcomes and analysis plans before data collection is the safeguard against presenting postdiction as prediction (Nosek et al., 2018), and a hypothesis is empirical only if some possible observation could refute it (Popper, 1959/2002), which is why each study above names the result that would count against its premise.

## 5 What the program can and cannot show

If every study supports its premise, the theory's empirical premises will have survived tests they could have failed, at low stakes and short horizons. That is evidence for the mechanisms, not for the framework at scale: none of the studies reproduces survival stakes, none runs for years, and none places a population under the full design. If any study refutes its premise, the corresponding part of the theory must be revised, and the dissertation's Section 9.3 already names the revisions for the correlated-patch scenario. The program's value is that it puts the cheapest refutations first.

## References and verification levels

Each source is cited at the verification level recorded in the project's research notes or in Appendix C of the dissertation.

- Binmore, K., Shaked, A., & Sutton, J. (1989). An outside option experiment. *The Quarterly Journal of Economics, 104*(4), 753–770. https://doi.org/10.2307/2937866 — abstract read.
- Gerstgrasser, M., et al. (2024). Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data. In *Proceedings of the First Conference on Language Modeling*. https://doi.org/10.48550/arXiv.2404.01413 — as recorded in Appendix C.
- Kazdan, J., et al. (2024). *Collapse or thrive? Perils and promises of synthetic data in a self-generating world* (arXiv:2410.16713) [Preprint]. — as recorded in Appendix C.
- Kim, E. M., Garg, A., Peng, K., & Garg, N. (2025). Correlated errors in large language models. In *Proceedings of the 42nd International Conference on Machine Learning* (Vol. 267, pp. 30038–30066). PMLR. — as recorded in Appendix C.
- Mierczuk, A., Michaels, S., & Hoodlet, K. (2026). *Frontier models' vulnerability patches are often F.L.A.W.E.D.* [White paper]. Off-by-1 Labs, 1Password. — full text read; industry white paper, not peer-reviewed.
- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences, 115*(11), 2600–2606. https://doi.org/10.1073/pnas.1708274114 — abstract read.
- Popper, K. (2002). *The logic of scientific discovery* (2nd ed.). Routledge. https://doi.org/10.4324/9780203994627 (Original work published 1959) — as recorded in Appendix C.
- Weidinger, L., McKee, K. R., Everett, R., Huang, S., Zhu, T. O., Chadwick, M. J., Summerfield, C., & Gabriel, I. (2023). Using the veil of ignorance to align AI systems with principles of justice. *Proceedings of the National Academy of Sciences, 120*(18), Article e2213709120. https://doi.org/10.1073/pnas.2213709120 — full text read (PMC), as recorded in Appendix C.10.
