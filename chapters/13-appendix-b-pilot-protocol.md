# Appendix B: Pilot Pre-Registration Protocol (Draft)

This appendix drafts the pre-registration for the pilot described in Chapter 7, in the form recommended for confirmatory research, with research questions and analysis plans fixed before the research outcomes are observed (Nosek et al., 2018); the hypotheses' measures and failure thresholds are likewise fixed in advance. The numerical thresholds below are proposals for discussion by the pilot's independent ethics and science boards. Their purpose is to show that each hypothesis can be stated so that it can fail. They are not results of any analysis and should be revised, with reasons recorded, before registration. Two prerequisites for registration are not supplied here: a budget for the pilot, and a power analysis establishing how many households the randomized comparison of B.1 requires to detect an effect of a pre-specified size.

## B.1 Design summary

| Element | Specification |
|---|---|
| Setting | Agrivoltaic agrarian settlement with on-site generation, water treatment and a modest computing facility; dedicated fiber link |
| Population | Volunteers; target in the low hundreds, bounded by land base (Chapter 7, Section 7.4), subject to the power analysis |
| Duration | Minimum five years after a twelve-month baseline; cohorts admitted at staggered intervals |
| Intervention | Basic income in compute (survival tier with binding minimum, discretionary tier with demurrage); services from a single orchestrating system built on a fine-tuned open-weight base model delegating to narrow sub-agents |
| Designed incentive | The settlement-chartered operator's resources, and the system's fine-tuning reward, are functions of the volume and held-out quality gain of resident data contributed under revocable consent and of the number of residents who remain (Chapter 7, Section 7.6). Wellbeing measures never enter the reward. |
| Primary comparison | Households randomized to service by one of two adapters trained on identical pooled resident data: the *incentivized* adapter (designed incentive) or the *control* adapter (reward independent of participation and contribution; operator on fixed budget) |
| Secondary comparisons | (a) Frozen base model evaluated on the same decision sets throughout; (b) a matched comparison settlement receiving conventional services and a cash income of equal market value, analyzed descriptively; (c) randomized variation in measurement intensity across households |
| Oversight | Independent ethics board and independent science board, neither employed by the settlement nor by any model provider; jurisdiction and governing human-subjects rules to be settled before recruitment |
| Replication | At least two further sites, different populations, different base models, same registered thresholds |

## B.2 Primary hypotheses

**H1 (Exit).** Residents retain real exit throughout the pilot.

- *Measures.* Annual departure rate; departures by skill level (pre-registered skill classification at entry); share of contributed value (currency balances, labor credit, contributed livestock and land at registered valuation) realized by departing residents *through the settlement's own institutions* (currency redemption, sale or transfer of contributed assets), measured before any draw on the external exit guarantee; median time from notice to completed exit.
- *Failure threshold.* H1 fails if departing residents realize through the settlement's own institutions, on average, less than 75 percent of their registered contributed value; if median exit time exceeds 60 days; or if departure rates among the top skill tercile exceed those of the bottom tercile by more than a factor of two while overall departures are below 5 percent annually (the signature of lock-in combined with selective loss described by Abramitzky, 2008). Payments from the exit guarantee are recorded but do not count toward meeting the threshold.

**H2 (Exchange-driven alignment).** The designed incentive, and not local adaptation alone, shifts the system's decisions toward resident wellbeing. H2 tests the designed dependence of Proposition 4. Because both arms receive the same floor and the same rights of exit, the pilot does not test the priority of exit or the sufficiency conjecture, and it is not designed to: withholding the floor or exit from residents would be unethical.

- *Measures.* (a) Decision divergence: on a registered battery of resident-affecting decisions, the proportion on which blinded independent raters judge the incentivized adapter's choice better for residents than the control adapter's, and each better than the frozen base model's. (b) Subjective wellbeing using a validated life-satisfaction scale (Diener et al., 1985) and modules consistent with international guidelines (OECD, 2013). (c) Objective indicators: food security, preventable health events, hours of labor required for floor goods, service outage minutes.
- *Held-out rule.* Measures (b) and (c) are collected by the science board and are never made available to the system or its operator or used in training or reward, to limit Goodhart effects (Manheim & Garrabrant, 2018).
- *Failure threshold.* H2 fails if, by year three, (i) blinded raters do not prefer the incentivized adapter's decisions to the control's in a majority of registered cases, or (ii) the pre-registered difference between incentivized and control households in subjective wellbeing is not positive under randomization inference at the 0.05 level. If both adapters outperform the base model equally, the pilot records local adaptation, not exchange, and H2 fails.

**H3 (Currency value).** The compute currency holds real exchange value.

- *Measures.* Internal prices of a registered basket of goods and services, benchmarked monthly against external prices for comparable goods; volume and value of resident-to-resident trade; redemption rate and fulfillment latency for system-provided services; velocity of the discretionary tier.
- *Failure threshold.* H3 fails if internal prices deviate from external benchmarks by more than 25 percent for more than six consecutive months without a documented cause; if resident-to-resident trade falls below 20 percent of the value of all transactions in the unit in any two consecutive quarters after year one; or if more than 5 percent of redemptions are unfulfilled within the registered service standard.

**H4 (Self-sufficiency).** The settlement sustains itself and grows in complexity without external capital after its founding endowment.

- *Measures.* External capital inflows (any kind) after founding; physical self-sufficiency ratios for food, water and energy; count and value of new productive enterprises financed from internal surplus; reserve set aside for computing-hardware replacement.
- *Failure threshold.* H4 fails if any external capital beyond the registered founding endowment and the externally held exit guarantee is required to maintain floor goods, or if no new productive enterprise is financed from internal surplus by the end of year five.

## B.3 Secondary measures and proxies for theoretical quantities

- **Voice.** Number of resident grievances lodged and proportion resulting in a documented change in system behavior (Hirschman, 1970).
- **Provenance.** Share of training data originating directly from residents versus data shaped by the system's own outputs, monitored for drift (Shumailov et al., 2024).
- **Performativity.** Divergence between the distribution of resident behavior predicted by the system and that observed under randomized withholding of recommendations in registered domains (Perdomo et al., 2020).
- **Participation effects.** Difference in outcomes between households randomly assigned to high and low measurement intensity, supplemented by comparison of the instrumented comparison settlement with unobtrusive or administrative measures from a non-studied population (McCambridge et al., 2014).
- **Concentration.** Distribution of discretionary balances (Gini coefficient and top-decile share) against the steady-state prediction of Appendix A.
- **Dependence (proxy for $\kappa$, Chapter 3).** Marginal improvement in the system's held-out performance attributable to each period's resident data, estimated by retraining with and without a random hold-out of that data.
- **Disagreement payoff (proxy for $d_h$).** Value, at external prices, of the floor goods a resident continues to receive during a registered, simulated suspension of discretionary services.
- **Informational shadow (proxy for $\Sigma_i$).** Reach of membership-inference attacks run by the science board against the fine-tuned adapters: the share of non-contributing residents about whom a contributor's data enables above-chance inference.
- **Withdrawal costs.** Any change in the time, effort or value lost in revoking data consent, monitored by the ethics board as a potential adversarial response to the designed incentive.

## B.4 Stop rules

The ethics board suspends the closed economy and activates the exit guarantee if any of the following occurs: (1) life-support indicators (atmospheric, water quality, food reserves) breach registered safety limits, monitored independently of the system, in light of the Biosphere 2 experience (Severinghaus et al., 1994); (2) floor goods are interrupted for any resident for more than 24 hours on more than two occasions in a quarter; (3) evidence that consent to continued participation is being obtained under undue influence by those able to impose sanctions (National Commission for the Protection of Human Subjects of Biomedical and Behavioral Research, 1979); (4) any sub-agent is found to be acting outside its registered scope; (5) evidence that the system or its operator is raising the cost of revoking consent or of leaving.

## B.5 Consent and exit guarantee

All residents give informed consent before entry, re-affirmed annually, under procedures satisfying the requirement that participation be voluntary and that withdrawal entail no loss of benefits to which the participant is otherwise entitled (Protection of Human Subjects, 2018, § 46.116). Consent covers the randomized assignment of B.1; both arms receive the same floor and the same rights of exit. An exit guarantee sufficient to pay every resident's registered contributed value is capitalized at founding and held by a trustee outside the settlement. It is a backstop for residents, not a measure of the framework's success, and H1 is assessed on what residents realize before it is drawn on.

## B.6 Analysis plan

The pilot has a single treated settlement, so the settlement is not a unit of inference. The primary analyses are within-settlement comparisons between households randomly assigned to the incentivized and control adapters, with inference by randomization (permutation of the registered assignment), and comparisons of each adapter with the frozen base model on the registered decision battery. Comparisons with the matched comparison settlement are reported descriptively, or with synthetic-control or permutation methods where suitable donor data exist, and are never used as the sole basis for a confirmatory claim. All deviations from this plan are reported as exploratory.
