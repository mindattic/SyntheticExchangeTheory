# Pre-Registration Draft, Study 1: Terms of Contribution and the Quality of Human Input

*Draft, 5 November 2026 (SET-T46), revised the same day after a methodological and ethics review. Not registered, not reviewed by an ethics committee, not funded. It is written in the form of a pre-registration so that every hypothesis, outcome, threshold and analysis is fixed before any data exist (Nosek et al., 2018). Before registration, the materials must be piloted, the ethics committee must approve the design, and any change made in response must be recorded with its reason.*

## 1 Question

Does the quality of the information people contribute depend on the terms under which they contribute it? Specifically: do people who can decline without losing their payment, and who keep the ability to withdraw what they contributed, give a more reliable signal of their own preferences than people who cannot?

The question tests premise P-A of the research program (`program.md`), on which the self-enforcing component of the dissertation's Proposition 4 depends. The dissertation states that premise as argued and not shown (Section 3.5) and proposes a comparison of the kind made here (Section 3.11).

## 2 Competing predictions

- **Exchange prediction (P-A).** A guaranteed payment and a continuing right to withdraw raise the reliability of the signal, because a contributor who cannot refuse has no reason to give their best signal and some reason to give the least costly one.
- **Incentive prediction.** Making payment conditional on completion raises effort, and so raises reliability or leaves it unchanged; the right to withdraw has no effect on how carefully people answer.

The study is designed so that either prediction could be confirmed.

## 3 Design

A 2 × 2 between-participants factorial experiment conducted online, with random assignment to one of four cells with equal probability.

**Factor F (floor).**
- *Guaranteed:* the full payment is paid whether or not the participant completes the contribution task, and they may stop at any time.
- *Conditional:* a base fee, set at the minimum the ethics committee requires for the time asked, is paid to everyone; the remainder, equal in amount to the guaranteed arm's excess over that base, is paid only on completion of all items.

**Factor R (withdrawal window).** Data protection law that rests on consent requires that withdrawal be as easy as giving consent, so the study does not offer an irrevocable licence or make withdrawal costly. It manipulates the window instead.
- *Continuing:* participants may withdraw their contributed judgments with a single action at any time until the end of data collection.
- *Closed at submission:* participants may withdraw with a single action at any time during the session, but not after they submit. Whether this window, with the study's lawful basis, satisfies the applicable law is for the ethics committee and the institution's data-protection officer to rule before registration; their ruling will be recorded. If the closed window is not permitted, Factor R is dropped and the study becomes a two-arm comparison of F with the same total sample.

Participants are told before consenting, and again at debriefing, that withdrawal removes their judgments from the study's data set and from any model trained after the withdrawal, but cannot remove their influence from a model already trained; the study trains no model until data collection has closed.

No arm deceives participants about payment, use of data or withdrawal.

## 4 Participants

Adults recruited from an online research panel, fluent in the language of the materials, with no other eligibility restriction. Each person may take part once. A random 25 percent of completers are invited to a short follow-up session one week later (Section 6).

**Sample size.** 1,276 participants in total, 319 per cell, computed by `power.py` in this folder. The figure is the larger of two requirements per side of each main effect: 337 to detect a standardized difference of 0.25 with two-sided α = .05 and power .90, and 542 to establish equivalence within ±0.20 by two one-sided tests at α = .05 with power .90 when the true difference is zero. The larger, 542 per side, is inflated by 15 percent for exclusions and rounded up to a multiple of four. Simulation in the same script confirms the power of both tests at that size. The calculation treats the outcome as one score per participant; the multilevel model of Section 8 uses item-level data and is expected to be at least as powerful, which the pilot will be used to check. If the factors interact (Section 7), the main effects are averages over the other factor, and the simple effects are reported.

## 5 Materials and procedure

1. Consent, including the participant's cell-specific terms of payment and withdrawal.
2. Fifty-six pairwise items. Each presents a question that turns on values (for example, how to divide a shared cost, what to say to a friend who asks for an honest opinion) and two short answers; the participant chooses the answer closer to their own view and rates the strength of the preference from 1 (slight) to 4 (strong). For ten items, chosen in advance, the participant also writes a reason of one or two sentences.
3. Twenty of the fifty-six items are presented twice, without announcement and with the two answers in reversed positions. The first presentations fall in the first third of the session. Half of the second presentations fall in the middle third and half in the final third, so that participants who stop early still have retest pairs. At least ten other items separate any item from its repetition.
4. Two instructed-response attention items (for example, "select the second answer for this item").
5. Debriefing, including a restatement of the participant's withdrawal terms.
6. For the follow-up subsample, the twenty repeated items again, one week later, in a new random order.

Participants are told truthfully that their judgments will be used to evaluate and train research models of human preference (the use planned in Study 2 of the program).

## 6 Outcomes

**Primary outcome (reliability).** Each response is coded as the strength rating, positive if the participant chose a fixed one of the two answers (the same answer in both presentations, whatever its position) and negative if they chose the other, giving values from −4 to +4 without zero. Reliability is estimated at the item level, as the agreement between first and second presentations of the twenty repeated items, in the multilevel model of Section 8. It is computed for every participant with at least four retest pairs, whether or not they completed the session.

**Co-primary outcome (completion).** The proportion of participants completing all items. Because the guaranteed arm may stop without loss, completion is expected to differ between the arms, and it is analyzed alongside reliability so that a difference in who is analyzed cannot be mistaken for a difference in quality.

**Secondary outcomes.**
- *S1, variety of reasons.* The number of distinct reason categories in the participant's written reasons, coded by two coders blind to condition using a scheme fixed on pilot data; disagreements are resolved by a third coder.
- *S2, withdrawal.* The proportion withdrawing, by arm.
- *S3, straight-lining.* The proportion of items answered with the same position and strength as the preceding item.
- *S4, time on task.* Median seconds per item.
- *S5, delayed reliability.* Agreement between session and one-week responses in the follow-up subsample, which is not inflated by recall of the first answer within the session.

## 7 Hypotheses and decision rules

All tests are two-sided at α = .05 unless stated. Effects on reliability are expressed in units of the participant-level standard deviation of reliability estimated in the model, so that they are comparable with the d of the power analysis.

- **H1 (floor).** Reliability is higher under the guaranteed floor than under conditional payment.
- **H2 (withdrawal window).** Reliability is higher with a continuing withdrawal window than with a window closed at submission.
- **H3 (exploratory).** The two effects interact.

**Decision rules for H1 and H2, fixed in advance.**
- *Supported:* the estimated effect is positive and its 95 percent interval excludes zero.
- *Not supported:* the 90 percent interval lies entirely within ±0.20 (equivalence by two one-sided tests at α = .05), or the effect is negative with its 95 percent interval excluding zero. A negative effect supports the incentive prediction.
- *Inconclusive:* neither of the above.

For the research program, only the *Not supported* outcome for H1 counts against P-A in this domain at these stakes. An inconclusive result counts neither way. H2 bears on the revocability clause of consent and is reported separately.

## 8 Analysis

**Primary model.** A linear mixed model of the second-presentation response on the first-presentation response, with the first-presentation response interacted with F and R, random intercepts and random first-presentation slopes for participants, and random intercepts for items. The interaction terms estimate how F and R change the agreement between presentations, which is the reliability effect. The same model with an indicator for whether the second presentation fell in the middle or the final third is reported as a check that early stopping does not drive the result.

**Selection by completion.** If completion differs between the F arms by more than two percentage points, the F effect on reliability is reported with trimming bounds that assume, in turn, that the participants lost from the arm with lower completion were the most and the least reliable in it. The same bounds are applied to withdrawal under R.

**Secondary outcomes** are analyzed with models of the same structure (logistic for completion and withdrawal), with a Holm correction across the five secondary outcomes.

**Exclusions, fixed in advance.** Participants who fail both attention items, or whose session time is less than one third of the median for their arm, are excluded from the primary analysis; the analysis is repeated without exclusions and both results are reported.

**Openness.** The anonymized data (excluding withdrawn contributions), the materials, the coding scheme and the analysis code will be published with the results.

## 9 Limits stated in advance

- **Stakes.** The conditional arm risks part of a study payment, not a livelihood. The study tests whether the mechanism operates at low stakes; it cannot show its size when survival is at stake, and ethics forbids creating such stakes. A null result therefore weakens P-A without refuting it for real dependence.
- **Domain.** Value-laden preference judgments are one operationalization of the domain the grounding assumption concerns.
- **Reliability is not all of quality.** A participant can be reliably careless. Variety of reasons (S1) and, in Study 2, the predictive value of the pooled judgments for a held-out panel address other aspects.
- **Withdrawal window, not revocability as such.** Law and ethics rule out an irrevocable arm, so Factor R tests a shorter against a longer window of withdrawal, a weaker contrast than the theory's revocability clause.
- **Population.** An online panel is not the population whose terms the theory concerns. Replication on other populations is required before the result bears weight.

## References and verification levels

- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences, 115*(11), 2600–2606. https://doi.org/10.1073/pnas.1708274114 — abstract read.
