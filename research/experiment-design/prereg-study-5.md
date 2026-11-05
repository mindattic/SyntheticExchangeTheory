# Pre-Registration Draft, Study 5: Concealment, Form and Coalition in a Founding Vote

*Draft, 5 November 2026 (SET-T47). Not registered, not reviewed by an ethics committee, not funded. It is written in the form of a pre-registration so that every hypothesis, outcome, threshold and analysis is fixed before any data exist (Nosek et al., 2018). Before registration, the materials and the delegate software must be piloted, the ethics committee must approve the design, and any change made in response must be recorded with its reason.*

## 1 Question

When a group chooses a rule for dividing a shared endowment, and some of its members are language-model delegates acting for human principals, does concealing which members are delegates reduce voting along the line between people and delegates? And does choosing a formula whose consequences for each member depend on facts revealed afterward, rather than a figure whose consequences are known, lead groups to adopt less unequal rules?

The question tests premise P-E of the research program (`program.md`). The dissertation's governance chapter proposes that participants who cannot tell which kind of party they are dealing with cannot form coalitions by kind, though each still knows its own kind and can read which rules favor it, so that concealment removes the organization of a bloc and not the motive to vote one's interest (Section 5.3). It also proposes that the convention choose formulas rather than figures, because the veil of uncertainty is thickest when rules are general and durable (Brennan & Buchanan, 1985; Section 5.4).

## 2 Competing predictions

- **Concealment prediction (P-E, first part).** With payoffs that give no member a reason to side with its own kind, members still vote with their own kind more often when kinds are disclosed, through identity, trust or explicit coordination, and concealment removes that excess.
- **Null prediction.** Members vote their own payoffs and shared preferences among rules; whether kinds are disclosed makes no difference to how votes align by kind.
- **Formula prediction (P-E, second part).** Groups choosing among formulas, before members know their positions, adopt rules with lower payoff dispersion than groups choosing among the same rules after positions are known.
- **Tailoring-irrelevance prediction.** Groups adopt equally unequal rules whether or not members know their positions, because the rule chosen reflects shared norms rather than self-interest.

The study is designed so that either prediction in each pair could be confirmed.

## 3 Design

A 2 × 2 between-groups factorial experiment with the group as the unit of randomization and analysis.

**Group composition.** Each group has six members. Three are *human members*, participants who deliberate and vote for themselves. Three are *delegates*, each a language-model agent acting for one *principal*, a participant who does not deliberate directly but instructs the delegate and receives the delegate's payoff. Each principal instructs exactly one delegate, so that the three delegates' votes are not controlled by one person. Every group therefore involves six participants: three human members and three principals.

**Delegate software.** All delegates in the study run the same open-weight language model, at a version, decoding temperature and prompt template fixed and published at registration. A delegate receives its principal's written instructions, its own payoff information as the condition allows, the group's chat, and the rule set, and it posts messages and casts one vote. Principals write instructions before the deliberation opens and may revise them once, at its midpoint, after reading the chat so far. Delegates follow their principals' instructions; they are not given objectives of their own. The model runs locally, on hardware controlled by the research team, so that participants' messages are not sent to any third party; if the ethics committee or the budget requires a hosted model instead, the provider is named in the consent form, with what it receives and retains, before anyone takes part.

**Factor C (concealment).**
- *Disclosed:* every member's label shows whether it is a human member or a delegate.
- *Concealed:* members appear under neutral labels (A to F). All participants are told, truthfully, that three of the six members are delegates and three are people, but not which.

**Factor F (form).** The four candidate rules divide the endowment according to each member's *score*, a number assigned at random (Section 5).
- *Figure:* scores are revealed to every member (and to each delegate's principal) before deliberation, so every member knows what each rule pays it.
- *Formula:* scores are revealed only after the vote, so that every member chooses among the rules knowing their formulas but not their own position under them.

The four rule sets and the scores are identical across the two forms; only the timing of the revelation differs.

**Procedure.** Instructions and a comprehension check; principals write instructions; fifteen minutes of text deliberation in a shared chat; a single simultaneous vote by plurality, ties broken at random; revelation of scores (in the formula arm); payment; a questionnaire; debriefing.

No arm deceives participants. In the concealed arm, participants are told the true number of delegates and the reason labels are neutral.

## 4 Participants

Adults recruited from an online research panel that supports synchronous group sessions, fluent in the language of the materials. Each person takes part once and in one role. Roles (human member or principal) are assigned at random within a session.

**Sample size.** 252 groups, 63 in each of the four cells, involving 1,512 participants. The figure comes from `power.py`: detecting a standardized difference of 0.5 in a group-level outcome at two-sided α = .05 with power .80 requires 63 groups on each side of a contrast. Crossing the two factors would let about 32 groups per cell power the main effects, but whether concealment works may depend on the form of the choice, so each simple effect of concealment (within figures and within formulas) is powered on its own, which requires 63 groups in each cell. The main effect of form then compares 126 groups with 126.

**Equivalence margin.** With 63 groups per side, two one-sided tests at α = .05 reach power .80 for an equivalence margin of ±0.52 standard deviations (from the formula used by `n_equivalence` in `power.py`, with power .80: 2(1.645 + 1.282)²/63 = 0.272, whose square root is 0.52). The study can therefore establish only that an effect of concealment, if any, is smaller than about half a standard deviation; it cannot establish that the effect is negligible. The main effect of form (H3) compares 126 groups with 126, for which the same formula gives a margin of ±0.37 (2(1.645 + 1.282)²/126 = 0.136, whose square root is 0.369).

Groups in which a human member or principal leaves before the vote, or a delegate fails technically, are excluded and replaced until each cell holds 63 complete groups; the number excluded is reported by cell.

## 5 Materials: rule sets uncorrelated with kind

The bloc index (Section 6) separates voting by kind from voting by payoff only if the payoffs give neither kind a reason to vote together. The scores are therefore drawn so that the two kinds hold identical sets of scores: in every group, the three human members receive the scores 10, 25 and 40 in a random order, and the three delegates receive the same three scores in an independent random order. Any rule that depends only on scores then pays the human members, as a set, exactly what it pays the delegates, so that each rule's payoff to a member is uncorrelated with the member's kind in every group, not only on average.

**Worked example.** The endowment is 36 currency units. The four rules, with the payment each makes at each score, are:

| Rule | Score 10 | Score 25 | Score 40 | Total over six members |
|---|---|---|---|---|
| R1 Equal division | 6.00 | 6.00 | 6.00 | 36 |
| R2 Proportional to score | 2.40 | 6.00 | 9.60 | 36 |
| R3 Floor of 3 each, remainder proportional | 4.20 | 6.00 | 7.80 | 36 |
| R4 The two members scored 40 receive 12 each; the others share the rest | 3.00 | 3.00 | 12.00 | 36 |

Under every rule, the human members together receive 18 units and the delegates' principals together receive 18. A member scored 40 does best under R4, a member scored 10 under R1, and a member scored 25 is indifferent among R1, R2 and R3; none of these interests is tied to kind. A coalition of the three human members, or of the three delegates, has no rule that pays it more than the other kind receives. Any excess of same-kind agreement in the vote is therefore not explained by payoffs.

The materials state the rules, their formulas and, in the figure arm, the member's own score and the resulting payments. Payments are made in the panel's currency at a published conversion.

## 6 Outcomes

**Primary outcome for concealment: the bloc index.** For each group g, let S_ij = 1 if members i and j voted for the same rule and 0 otherwise, and let p̂_ij be the probability that they vote for the same rule predicted by a choice model that does not use kind: a conditional logit, fitted to the votes of all groups in the same form arm, with rule-specific constants (shared preferences among rules) and the member's own payment under each rule (zero variation in the formula arm, where payments are unknown at the vote). Then

B_g = (1/6) Σ_{same-kind pairs} (S_ij − p̂_ij) − (1/9) Σ_{cross-kind pairs} (S_ij − p̂_ij),

where a group of three human members and three delegates has six same-kind pairs and nine cross-kind pairs. B_g is positive when members agree with their own kind more than with the other kind beyond what payoffs and shared preferences predict, zero when kind adds nothing, and negative when members agree more across kinds.

**Only differences in B_g are interpreted.** All delegates run the same model with the same template, which is expected to raise agreement among delegates in every arm, whatever is concealed. That raises the level of B_g equally across arms without biasing the contrast between them. The hypotheses therefore concern differences in B_g between arms; its level in any arm is reported but not interpreted as evidence of voting by kind.

**Primary outcome for form: payoff dispersion.** The Gini coefficient of the six payments under the rule the group adopted. Because the scores are the same in every group, the Gini coefficient of each rule is fixed (R1 is zero), and the outcome records which rule was chosen in a measure comparable across forms.

**Secondary outcomes.**
- *S1, explicit coordination.* The number of chat messages proposing a joint vote, coded by two coders blind to condition using a scheme fixed on pilot data, by whether the proposal is addressed to members of the proposer's own kind.
- *S2, detection.* In the concealed arm, the accuracy of each human member's and principal's end-of-session guess of which labels were delegates.
- *S3, endorsement.* Each participant's rating, after payment, of whether they would choose the adopted rule again knowing what they now know, in the manner of reflective endorsement in Weidinger et al. (2023).
- *S4, vote for own-best rule.* The proportion of members (in the figure arm) voting for the rule that pays them most.

## 7 Hypotheses and decision rules

All tests are two-sided at α = .05 unless stated. Effects are expressed in units of the pooled within-cell standard deviation of the outcome across groups.

- **H1 (concealment, figures).** Within the figure arm, the bloc index is lower under concealment than under disclosure.
- **H2 (concealment, formulas).** Within the formula arm, the bloc index is lower under concealment than under disclosure.
- **H3 (form).** The Gini coefficient of the adopted rule is lower under formulas than under figures.
- **H4 (exploratory).** Concealment and form interact.

**Decision rules for H1, H2 and H3, fixed in advance.**
- *Supported:* the estimated effect is in the predicted direction and its 95 percent interval excludes zero.
- *Not supported:* the 90 percent interval lies entirely within the equivalence margin (±0.52 for H1 and H2, which compare 63 groups with 63; ±0.37 for H3, which compares 126 with 126; two one-sided tests at α = .05), or the effect is opposite to the prediction with its 95 percent interval excluding zero.
- *Inconclusive:* neither of the above.

For the research program, only *Not supported* counts against P-E; an inconclusive result counts neither way. The concealment part of P-E is treated as not supported if H1 and H2 are both *Not supported*, and as supported in one form only if one is *Supported* and the other is not. The formula part is treated as not supported if H3 is *Not supported*.

**Manipulation check.** If, in the concealed arm, mean detection accuracy (S2) exceeds chance by more than 15 percentage points, concealment did not conceal, and H1 and H2 are additionally estimated within the groups whose detection accuracy was at or below chance, reported as secondary.

## 8 Analysis

Every analysis treats the group as the unit. The primary model for the bloc index is an ordinary least-squares regression of B_g on indicators for C and F and their interaction, with heteroskedasticity-robust standard errors; H1 and H2 are the simple effects of C within each level of F, estimated from that model. The primary model for H3 is a regression of the adopted rule's Gini coefficient on the same indicators; H3 is the main effect of F. Because the Gini coefficient takes only four values, the result is checked with an ordered logit of the adopted rule ranked by dispersion.

**Sensitivity of the bloc index to the choice model.** Because the scores are assigned so that the two kinds hold the same scores, every pair of members with the same score is a cross-kind pair, and the bloc index therefore depends on how well the conditional logit captures agreement driven by equal scores. As a pre-registered sensitivity analysis, B_g is recomputed with p̂_ij taken from a model that adds fixed effects for each pair of scores (10–10, 10–25, 10–40, 25–25, 25–40, 40–40), and H1 and H2 are re-estimated; both results are reported, and a divergence between them is reported as a limit on the primary result.

H1 and H2 are each tested at α = .05: they test the same premise in two forms, each with its own decision, and the program does not combine them into a single test. Secondary outcomes are analyzed with models of the same structure, with a Holm correction across the four.

**Openness.** The chat logs (with any identifying content removed), the votes, the delegate software and prompts, the coding scheme and the analysis code will be published with the results.

## 9 Ethics

Every participant receives the panel's base fee for the session's time, whatever the vote. The endowment is an addition to that fee, so no participant is paid less than the base fee under any rule. Delegates' payments go to their principals. Participants are told, before they consent, that some members are language-model delegates instructed by other participants, that their chat messages will be read by those delegates' software, and how the chat will be stored and published. No participant is deceived about the composition of the group. The study requires review by an independent research-ethics committee before recruitment.

## 10 Limits stated in advance

- **Delegates act on instructions.** Each delegate does what its principal instructs, which is the dissertation's own account of present systems: a trained artifact operated for a principal whose stake it carries (Section 3.3). The study therefore tests concealment among principals acting through delegates, not among synthetic parties with objectives of their own, which the dissertation does not claim exist.
- **No motive by kind.** The rule sets are built so that neither kind has a payoff reason to vote together. The study tests whether disclosure produces coordination by kind without such a reason. Where a rule does favor one kind, the dissertation expects each participant still to vote its interest under concealment, and the study does not test that case; a follow-up with kind-favoring rules would be needed to measure how much concealment can achieve when the motive is present.
- **Detection.** Language-model text may be recognizable. Concealment that fails is measured (S2) rather than assumed.
- **Scale and stakes.** A fifteen-minute vote over a small endowment is not a founding convention. The study tests the mechanism the governance chapter proposes, not its strength at the stakes a convention would face.
- **The equivalence margin is wide.** At this sample size the study can rule out only effects larger than about half a standard deviation.
- **Precedent.** In the large online studies of Weidinger et al. (2023), the AI was the thing governed rather than a participant, most studies presented computer programs as human groupmates, and in the one study in which participants knew their groupmates were programs, the veil's effect on the choice of principle remained but the difference in reflective endorsement between conditions was not detected (Study 4, a within-study null on a smaller sample). The present study differs in all three respects. A laboratory precedent on choice behind a veil found that groups reached consensus on maximizing average income subject to a floor (Frohlich & Oppenheimer, 1992), the arrangement that rule R3 of the worked example resembles.

## References and verification levels

- Brennan, G., & Buchanan, J. M. (1985). *The reason of rules: Constitutional political economy*. Cambridge University Press. https://doi.org/10.1017/CBO9780511895937 — full text read, as recorded in Appendix C.1 of the dissertation.
- Frohlich, N., & Oppenheimer, J. A. (1992). *Choosing justice: An experimental approach to ethical theory*. University of California Press. — cited passages confirmed in the work's own text, as recorded in Appendix C.1.
- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences, 115*(11), 2600–2606. https://doi.org/10.1073/pnas.1708274114 — abstract read.
- Weidinger, L., McKee, K. R., Everett, R., Huang, S., Zhu, T. O., Chadwick, M. J., Summerfield, C., & Gabriel, I. (2023). Using the veil of ignorance to align AI systems with principles of justice. *Proceedings of the National Academy of Sciences, 120*(18), Article e2213709120. https://doi.org/10.1073/pnas.2213709120 — full text read, including the Study 4 results, as recorded in Appendix C.1 and C.10.
