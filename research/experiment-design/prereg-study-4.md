# Pre-Registration Draft, Study 4: A Guaranteed Floor Versus an Outside Option

*Draft, 5 November 2026 (SET-T47). Not registered, not reviewed by an ethics committee, not funded. It is written in the form of a pre-registration so that every hypothesis, outcome, threshold and analysis is fixed before any data exist (Nosek et al., 2018). Before registration, the protocol must be piloted, the sample size recomputed from the pilot's variance (Section 4), the ethics committee must approve the design, and any change made in response must be recorded with its reason.*

## 1 Question

Does a floor received during disagreement protect a weaker bargainer in a different way from an outside option? Specifically: does removing the weaker party's cost of delay raise its share of the bargain when no outside option binds, and does an outside option raise its share only when the option is worth more than what the party would otherwise obtain?

The question tests premise P-C of the research program (`program.md`), which rests on Appendix A.3.2 and A.3.4 of the dissertation. A.3.2 models the survival constraint as impatience: a party below its floor discounts the future steeply and, in the limit, receives its disagreement payoff and none of the surplus; raising its disagreement payoff to the floor restores a finite discount rate and a positive share. A.3.4 states the outside-option principle: an outside option changes the bargained payoff only if it binds, so that the payoff is the larger of the unprotected payoff and the option's value.

## 2 Competing predictions

- **Strategic prediction (Appendix A.3).** Removing the weaker party's cost of delay raises its share even though nothing binds; an outside option below the unprotected share has no effect; an outside option above it raises the weaker party's payoff to about the option's value.
- **Naive prediction.** An outside option acts as a disagreement payoff: any option, binding or not, raises the weaker party's share by an amount that increases with the option's value. Binmore et al. (1989), in the abstract read for this project, describe treating outside options as disagreement payoffs as naive and report that their experiment supported the strategic prediction.

The study is designed so that either prediction could be confirmed.

## 3 Design

A four-arm between-pairs experiment with real payments. Each participant plays one bargaining game, once, with one anonymous partner; there is no rematching. Within each pair the roles of weaker party (W) and stronger party (S) are assigned at random, and pairs are assigned to arms at random with equal probability.

**The game.** The pair divides a sum V = £20 by alternating offers. S always makes the first offer; W accepts or rejects; if W rejects, W makes the next offer; and so on. After every rejected offer, a random draw ends the game with probability 0.1, in which case both receive nothing from it; with probability 0.9 play continues to the next offer. There is no fixed last round, so the game is stationary and its predictions do not depend on a horizon. (An earlier version of this draft capped play at ten rounds; a review showed that the cap moves the predicted shares substantially, for example to 0.170 for W in arm 1, so the cap was replaced by random termination.) Agreement in round t pays each party its agreed share of V multiplied by its own shrinkage factor raised to the power t − 1, so delay shrinks what each party can take home, and shrinks W's faster.

**The cost of delay.** In arms 1 to 3, W's shrinkage factor is δ_W = 0.6 and S's is δ_S = 0.9: each round of disagreement removes 40 percent of what W can take home and 10 percent of what S can. Combined with the continuation probability of 0.9, the effective discount factors are δ_W′ = 0.6 × 0.9 = 0.54 and δ_S′ = 0.9 × 0.9 = 0.81. This is the laboratory analogue of the survival constraint of A.3.2, expressed as the steeper discounting A.3.2 uses rather than as a fixed amount. The program description (`program.md`, Study 4) speaks of a fixed per-round cost; a fixed cost makes the predicted division a corner (the party with the lower cost takes almost everything), whereas proportional discounting maps directly onto the asymmetric Nash solution the appendix uses (Binmore et al., 1986) and gives interior predictions.

**The four arms.**
1. *No protection.* As above.
2. *Non-binding outside option.* At any point at which W is responding to an offer, W may instead take an outside option, which ends the game; S then receives nothing from it. The option pays o = 0.08 of the sum's current value to W, that is, £1.60 shrunk by W's factor in the same way as an agreement in that round (£1.60 × 0.6^(t−1) in round t), so that taking the option is not a way to escape the cost of delay.
3. *Binding outside option.* As arm 2, with o = 0.35 (£7 × 0.6^(t−1) in round t).
4. *Floor.* W's extra shrinkage is removed: δ_W = δ_S = 0.9, so that both effective discount factors are 0.81. This is how the study implements the floor of A.3.2, whose effect in the model is to remove the steep impatience of a party below its floor; no separate payment is made, so the floor is not counted twice. No outside option is offered.

Every participant receives a show-up fee, set by the ethics committee, regardless of the game's outcome. Sessions have a fixed time limit; if a session runs out of time, pairs still bargaining are recorded as ending without agreement, and their outcome is zero under the rule of Section 6, as for a random termination. Participants see the rules of their own arm in full, including both discount factors and any option, before play. No arm involves deception.

## 4 Predictions and their derivation

**The unprotected split.** The game is the alternating-offers game with effective discount factors δ_W′ = 0.54 and δ_S′ = 0.81, with S proposing first. Its subgame-perfect outcome is immediate agreement, with S's share (1 − δ_W′)/(1 − δ_W′ δ_S′) = 0.46/0.5626 = 0.818, so W's predicted share is 0.182 (£3.65). The asymmetric Nash benchmark of Appendix A.3, with r = −ln δ′, gives α = r_S/(r_W + r_S) = 0.211/0.827 = 0.255 for W; the two benchmarks differ because the first gives S the advantage of moving first. Both place W's unprotected share between 0.18 and 0.26; the option values are set below that range (0.08) and above it (0.35).

**Arm predictions** (W's share of V at agreement, subgame-perfect benchmark):

| Arm | Predicted W share | Reason |
|---|---|---|
| 1 No protection | 0.182 | as derived above |
| 2 Option 0.08 | 0.182 | the option is worth less than W obtains without it, so it does not bind (A.3.4) |
| 3 Option 0.35 | 0.350 | the option binds; S offers W the option's value, max{0.182, 0.35} (A.3.4) |
| 4 Floor | 0.447 | equal effective factors of 0.81: W's share as responder is 1 − (1 − 0.81)/(1 − 0.81²) = 0.447 (A.3.2) |

These values were computed in closed form and checked by backward induction over a horizon of 400 rounds, with the option discounted like agreement, by the following script (run with `python -I`):

```python
def solve(dW, dS, p, o=None, T=400):
    vW = vS = 0.0
    for t in range(T, 0, -1):
        reach = p ** (t - 1)
        fW, fS = dW ** (t - 1) * reach, dS ** (t - 1) * reach
        if t % 2 == 1:  # S proposes, W responds (or takes the option)
            resW = vW if o is None else max(vW, o * fW)
            x = resW / fW
            vW, vS = resW, (1 - x) * fS
        else:           # W proposes, S responds
            x = vS / fS
            vW, vS = (1 - x) * fW, vS
    return vW

print(solve(0.6, 0.9, 0.9), solve(0.6, 0.9, 0.9, o=0.08),
      solve(0.6, 0.9, 0.9, o=0.35), solve(0.9, 0.9, 0.9))
```

Output: arm 1 0.1824, arm 2 0.1824, arm 3 0.3500, arm 4 0.4475.

Laboratory bargainers are not expected to reproduce these point values. The confirmatory predictions are the directions of three contrasts, stated in Section 7, and only the directions are tested.

## 5 Participants

Adults recruited to a laboratory or to an online platform with real-time matching, fluent in the language of the materials, each taking part once. **Sample size:** 244 pairs per arm, 976 pairs (1,952 participants) in all, from `power.py`: detecting a difference of 0.05 in W's share with an assumed standard deviation of 0.15 (d = 0.333) at the Bonferroni-corrected α = 0.0167 with power .90. The standard deviation has no source; it is an assumption, and the sample size will be recomputed from the pilot's observed standard deviation before registration. Equivalence by two one-sided tests within ±0.05 at α = 0.0167 has power of about 0.88 at this size by the normal approximation (`power.py`). Pairs in which either participant fails the comprehension check (Section 6) are replaced, and the replacement count is reported.

## 6 Procedure and outcomes

1. Consent and instructions for the participant's arm, followed by a comprehension check of four questions on the payoffs of agreement at different rounds and, where relevant, of the outside option or the floor. A participant who fails twice is paid the show-up fee and does not play.
2. The game, with a fixed time limit per offer; an offer not made in time is recorded as an offer of zero to the responder.
3. A short questionnaire (age, prior participation in bargaining studies) and payment.

**Primary outcome.** W's realized payoff from the game as a share of V: the accepted share multiplied by δ_W^(t−1) in arms 1 to 3 and by 0.9^(t−1) in arm 4, the option's realized value divided by V if W took the option, and zero if the game ended without agreement, by random termination or because the session ran out of time. Disagreement and option exits are thus included in the outcome rather than excluded from it.

**Secondary outcomes.** S1, the share of V offered to W in S's first offer; S2, the round of agreement; S3, the proportion of games ending without agreement; S4, in arms 2 and 3, the proportion of W taking the option.

## 7 Hypotheses and decision rules

Three planned contrasts, each tested two-sided at the Bonferroni-corrected α = 0.0167, with effects in units of W's share of V.

- **C1 (floor).** Arm 4 exceeds arm 1.
- **C2 (non-binding option).** Arm 2 does not differ from arm 1.
- **C3 (binding versus non-binding option).** Arm 3 exceeds arm 2.

**Decision rules, fixed in advance.** For C1 and C3:
- *Supported:* the effect is positive and its 98.33 percent interval excludes zero.
- *Not supported:* the 96.67 percent interval lies entirely within ±0.05 (equivalence by two one-sided tests at α = 0.0167), or the effect is negative with its 98.33 percent interval excluding zero.
- *Inconclusive:* neither of the above.

For C2, the prediction is a null: it is *supported* if the 96.67 percent interval lies within ±0.05, *not supported* if the effect is positive with its 98.33 percent interval excluding zero, and inconclusive otherwise.

For the research program, P-C counts as **not supported** only if C1 is *Not supported*, or if C3 is *Not supported* (arm 2 raises W's share as much as arm 3, as the naive prediction implies). A *Not supported* C2 alone, with C3 supported, is reported as evidence that non-binding options have some effect, contrary to A.3.4's limiting statement, but does not by itself count against P-C. Inconclusive results count neither way.

## 8 Analysis

Each contrast is estimated as a difference in mean primary outcome between two arms, by ordinary least squares on arm indicators with heteroskedasticity-robust standard errors, using all pairs that played. Because each pair plays once with no rematching, pairs are independent; if the study is run in laboratory sessions, standard errors are additionally clustered by session and both are reported. As a robustness check, the analysis is repeated with the accepted share (without discounting) for pairs that agreed. Secondary outcomes are analyzed with the same model (logistic for S3 and S4), with a Holm correction across the four.

**Openness.** The anonymized data, the instructions, the software and the analysis code will be published with the results.

## 9 Limits stated in advance

- **Stakes.** Bargaining over £20 is not bargaining over a livelihood. The study tests the mechanism Appendix A.3 models, not its magnitude in the world.
- **The floor as a discount factor.** Arm 4 implements only the impatience channel of A.3.2. The additive and substitution effects of A.3.1 are accounting results about the size of the surplus and are not tested here.
- **Induced impatience.** Real survival pressure is a property of the person; here it is a rule of the game. Participants may not behave as people who are actually short of necessities would.
- **Point predictions.** The subgame-perfect values in Section 4 are benchmarks; the confirmatory claims are the directions of the contrasts.
- **Population.** A laboratory or online panel is not the population whose terms the theory concerns. Replication on other populations is required before the result bears weight.

## References and verification levels

- Binmore, K., Rubinstein, A., & Wolinsky, A. (1986). The Nash bargaining solution in economic modelling. *The RAND Journal of Economics, 17*(2), 176–188. https://doi.org/10.2307/2555382 — abstract read.
- Binmore, K., Shaked, A., & Sutton, J. (1989). An outside option experiment. *The Quarterly Journal of Economics, 104*(4), 753–770. https://doi.org/10.2307/2937866 — abstract read.
- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences, 115*(11), 2600–2606. https://doi.org/10.1073/pnas.1708274114 — abstract read.
