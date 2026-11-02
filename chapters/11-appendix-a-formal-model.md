# Appendix A: Formal Model

This appendix gives the minimal mathematics behind the propositions of Chapter 3 and the economic design of Chapter 4. It is intentionally elementary. Every result here is a textbook consequence of the cited theory, a direct calculation, or, where the text says so, a stated assumption, and the point of setting them out is to show precisely which assumptions each design choice depends on.

## A.1 Notation

| Symbol | Meaning |
|---|---|
| $N(t)$ | Number of enrolled persons at time $t$ |
| $C(t)$ | Total measured compute operating under the framework in period $t$, in standard compute units (global compute where the whole of it does) |
| $\theta$ | Share of global compute allocated to the basic income (set by the convention, Chapter 5) |
| $\sigma(t)$, $\sigma_0$ | Survival-tier share of each allocation, $0 < \sigma(t) \le 1$, time-varying under the binding minimum of A.2, and its ordinary value |
| $a(t)$, $\bar a$ | Per-person allocation, $a(t) = \theta C(t) / N(t)$, and a fixed nominal holding (A.2) |
| $f$ | Physical floor: the quantity of the standard floor bundle a party requires per period |
| $p_f(t)$ | Price per unit of the floor bundle in compute units |
| $\bar f$ | Value of the floor bundle, $\bar f = p_f f$, in compute units |
| $d_i$ | Disagreement payoff of party $i$, a flow per period; $V$ and $u_i$ below are measured in the same way, and the comparison with $\bar f$ in A.3.2 is per period |
| $c_s$ | Cost to the synthetic party of supplying floor goods within an exchange (A.3.1) |
| $r_h, r_s$ | Discount rates of the two parties in the alternating-offers model (A.3) |
| $D_{BA}$, $P_{AB}$, $g$ | Dependence of party $B$ on party $A$, the power of $A$ over $B$, and the function relating dependence to its arguments (Emerson, A.5) |
| $\kappa_j$ | Dependence of synthetic party $j$, through its principal, on a population's human-generated input |
| $V$, $u_i$ | Joint value of agreement and party $i$'s bargained payoff (A.3); $u_i^*$ is the payoff before the survival tier and $u_i^{*\prime}$ after it |
| $\alpha$ | Bargaining weight of the human party in the asymmetric Nash solution (A.3) |
| $\Delta$ | Value per period of the survival tier (A.3.1) |
| $o_h$ | Value of the human party's outside option (A.3.4) |
| $L$ | Lump sum received against a pledged tier (A.3.3) |
| $p(t)$ | Price of a representative bundle of goods and services in compute units (A.2) |
| $W_i(t)$ | Discretionary balance held by party $i$ |
| $\rho$ | Rate at which a held balance grows or shrinks by being held (A.4) |
| $\delta$ | Demurrage rate on idle discretionary balances and loan claims (per period) |
| $r$ | Return on held balances in a conventional interest-bearing regime, or the interest rate on a loan claim (A.4.3) |
| $y_i(t)$ | Discretionary inflow to $i$ (allocation plus earnings) |
| $c_i(t)$ | Discretionary outflow from $i$ (spending, transfers) |
| $k_i$ | Constant net inflow $y_i - c_i$ (A.4) |
| $K_i$, $\pi$ | Productive capital held by $i$ and its rate of return (A.4.3) |
| $v_B$, $\lambda_B$ | Party $B$'s motivational investment in goals mediated by $A$, and the availability of those goals outside the relation (A.5) |
| $M$, $b$, $\gamma$ | Number of synthetic parties drawing on one population; private benefit and total cost of a degrading action (A.5) |
| $\Sigma_i$, $\Sigma_P$ | Informational shadow of a flow from source $i$, and the collective shadow of population $P$ (A.6) |

## A.2 Indexing, the real value of the allocation, and the binding floor

The allocation is defined as a share of total compute, so the per-person quantity is

$$a(t) = \frac{\theta\, C(t)}{N(t)}.$$

Let $p(t)$ be the price of a representative bundle of goods and services measured in compute units. A fixed nominal holding $\bar a$ has real value $\bar a / p(t)$, which falls whenever $p(t)$ rises, that is, whenever compute becomes more abundant relative to the real output it is exchanged against. The indexed allocation instead has real value

$$\frac{a(t)}{p(t)} = \frac{\theta}{N(t)} \cdot \frac{C(t)}{p(t)},$$

which, holding $\theta$ fixed, is the per-capita share $\theta / N$ of the real purchasing power of all compute, $C/p$. Indexing therefore converts the question "does the basic income keep its value?" into the question "does the real value of the world's compute grow faster than population?" That is the correct question for a framework whose premise is that compute is the productive base of the economy. A fixed-quantity design would instead tie the real value of the basic income to the falling relative price of compute, so that the income would shrink as the economy it is supposed to share in grows.

A percentage does not by itself secure the physical floor. The survival tier delivers the floor only if

$$\sigma\, a(t) \ \ge\ \bar f(t) \quad\Leftrightarrow\quad \sigma\,\frac{\theta\, C(t)}{N(t)} \ \ge\ p_f(t)\, f,$$

and nothing in the arithmetic guarantees this. Chapter 4 therefore makes the tier a percentage with a binding minimum:

$$\sigma(t) = \min\left\{1,\ \max\left\{\sigma_0,\ \frac{\bar f(t)}{a(t)}\right\}\right\},$$

where $\sigma_0$ is the ordinary survival share. Chapter 4 allows $p_f$, and therefore $\bar f$ and $\sigma$, to differ by place; the appendix writes the single-place case, and the formulas hold place by place. When $\bar f(t) > a(t)$, the constraint binds at $\sigma = 1$, the allocation as a whole falls short of the floor, and the floor can be met only by raising $\theta$; that is a decision the convention must take, and it is why the floor standard $f$ becomes a contested parameter (Chapters 5 and 7). The design therefore guarantees the floor only up to what the agreed share of capacity can buy.

## A.3 The survival tier as a disagreement payoff

Consider a single exchange between a human party $h$ and a synthetic party $s$ in which agreement makes total value $V$ available for division, with $V > d_h + d_s$, where $d_h$ and $d_s$ are the disagreement payoffs, all measured per period or as present values over the life of the exchange. With transferable utility and complete information, the Nash bargaining solution (Nash, 1950) maximizes $(u_h - d_h)(u_s - d_s)$ subject to $u_h + u_s = V$. Each party receives its disagreement payoff plus half the surplus $V - d_h - d_s$:

$$u_h^* = d_h + \frac{V - d_h - d_s}{2} = \frac{V + d_h - d_s}{2}, \qquad u_s^* = \frac{V - d_h + d_s}{2}.$$

The symmetric split is the limit of the alternating-offers model when the two parties discount the future at the same rate. When they do not, with discount rates $r_h$ and $r_s$, the limit is the asymmetric Nash solution (Binmore et al., 1986),

$$u_h = d_h + \alpha\,(V - d_h - d_s), \qquad u_s = d_s + (1 - \alpha)\,(V - d_h - d_s), \qquad \alpha = \frac{r_s}{r_h + r_s},$$

so that the more patient party takes the larger share of the surplus. The results of A.3.1 generalize to any fixed $\alpha$: in the substitution case $u_h^{*\prime} = u_h^* + (1 - \alpha)\Delta + \alpha c_s$ and $u_s^{*\prime} = u_s^* - (1 - \alpha)(\Delta - c_s)$, so that the human party's gain lies between $(1-\alpha)\Delta$ and $\Delta$ and the provider's loss between $0$ and $(1-\alpha)\Delta$. A.3.2 uses the dependence of $\alpha$ on impatience directly.

**A.3.1 What an unconditional floor does to the division of surplus.** Suppose the survival tier gives $h$ goods worth $\Delta$ per period, received whether or not agreement is reached. Two cases must be distinguished.

*The purely additive case.* If the tier is simply added to whatever $h$ has, it raises $h$'s payoff on disagreement and $h$'s payoff on agreement by the same amount: $d_h$ becomes $d_h + \Delta$ and $V$ becomes $V + \Delta$. The surplus $V - d_h - d_s$ is unchanged, and

$$u_h^{*\prime} = \frac{(V + \Delta) + (d_h + \Delta) - d_s}{2} = u_h^* + \Delta.$$

The human party is better off by exactly the value of the tier and no more. The division of the surplus is unchanged.

*The substitution case.* If the tier replaces something $h$ would otherwise have obtained from $s$ within the exchange, for example floor goods previously bought from the provider it is bargaining with, then $h$'s disagreement payoff rises by $\Delta$ while the joint value of agreement changes by the cost $c_s$ that $s$ no longer bears in supplying those goods: $d_h$ becomes $d_h + \Delta$ and $V$ becomes $V + c_s$. Assume $c_s \in [0, \Delta]$, that is, that the provider's cost of supplying the goods did not exceed their value to the person, and assume that the surplus remains positive, $V + c_s > d_h + \Delta + d_s$; otherwise the exchange is no longer worth entering and ends, which is itself the removal of a dependence. The surplus then falls by $\Delta - c_s$, and

$$u_h^{*\prime} = u_h^* + \frac{\Delta + c_s}{2}, \qquad u_s^{*\prime} = u_s^* - \frac{\Delta - c_s}{2}.$$

The human party's net gain from a tier worth $\Delta$ therefore lies between $\Delta/2$, when the provider supplied the floor goods at no cost to itself and the tier only duplicates them under agreement, and $\Delta$, when the provider's cost equaled their value, which is the additive case again. Under the assumption, the provider's payoff falls by at most $\Delta/2$ and the human party's rises by at least $\Delta/2$. If instead $c_s > \Delta$, because the provider's cost of supplying floor goods exceeded their value to the person, as it may where a provider supplies them in order to create dependence, then the surplus grows by $c_s - \Delta$, the human party gains more than $\Delta$, and the provider's payoff rises as well: relieving such a provider of a loss-making obligation benefits it, and the dependence it bought is what it loses. The substitution case is not a benefit beyond the tier. It is the case in which part of the tier's value is absorbed by the shrinkage of a joint surplus the exchange no longer needs to create, and the fall in $s$'s payoff is the bargaining counterpart of the fall in $h$'s dependence on $s$ that occurs when an alternative source of a valued good appears (A.5).

The working draft of this dissertation claimed that an unconditional floor raises the human party's payoff by an additional $\Delta/2$ in every exchange it enters. That claim was wrong in three ways: it ignored the additive case, in which there is no such effect; it counted one floor as a separate gain in every bilateral bargain; and it treated the substitution-case shift as a gain beyond the tier, which A.3.1 shows it is not. The floor's most important bargaining effect is the one in A.3.2.

**A.3.2 The impatience constraint.** Model the survival constraint of Chapter 3 as a stated assumption: when $d_h < \bar f$, the human party cannot sustain disagreement for longer than its stocks allow, which in the alternating-offers model is a discount rate $r_h$ that rises without bound as the stocks run out. In the asymmetric solution above, $r_h \to \infty$ gives $\alpha \to 0$ and $u_h \to d_h$: the party below its floor receives its disagreement payoff and none of the surplus. Raising $d_h$ to at least $\bar f$ restores a finite $r_h$, and with it a positive share. Unlike the effect in A.3.1, this does not depend on whether the floor substitutes for anything the counterparty supplies, and the comparison between $d_h$ and $\bar f$ is per period. This constraint is the bargaining-theoretic reason for clause E(i) of Chapter 3, and so for the first design consequence of Section 3.6; Proposition 1 records the definitional link between that clause and consent.

**A.3.3 Why inalienability matters.** Suppose the survival tier could be pledged against a loan. In a period of need, a party pledges it and receives a lump sum $L$. For the duration of the pledge its disagreement payoff falls by the value of the pledged tier, and if that pushes $d_h$ below $\bar f$, the impatience of A.3.2 returns in every exchange the party enters until the pledge is redeemed. The pledge thus has a hidden cost beyond the loan's interest. Because the parties most likely to pledge are those in the most acute need, alienability concentrates this hidden cost on the weakest. Making the tier non-tradable and non-borrowable is equivalent to prohibiting this transaction (Calabresi & Melamed, 1972).

**A.3.4 Outside options versus disagreement payoffs.** If instead of a floor the human party is given an outside option $o_h$, a second provider it may switch to, the outside-option principle, derived in the strategic bargaining literature and tested experimentally by Binmore et al. (1989), implies that the bargained payoff is $\max\{u_h^*, o_h\}$ evaluated with $d_h$ unchanged: the option matters only if it binds. When it binds, the weaker party receives exactly the option's value, which is then more than it would otherwise have obtained; the option protects only up to its own value, and the counterparty can lower that value by raising switching costs until the option no longer binds and protects nothing. A disagreement payoff at or above the floor protects in a different way, because it removes the impatience of A.3.2 whether or not anyone leaves. This is the formal reason the framework prefers a guaranteed floor to a guarantee of competition, while still requiring both.

## A.4 Demurrage and the dynamics of accumulation

Let party $i$'s discretionary balance evolve in continuous time as

$$\frac{dW_i}{dt} = y_i - c_i + \rho\, W_i,$$

where $\rho$ is the rate at which the balance grows or shrinks merely by being held. The analysis below concerns positive balances. Under the rules of Chapter 4, demurrage applies to positive balances and to outstanding loan claims held by lenders. For a loan claim, the holding cost is a periodic charge of $\delta$ on the claim's face value, paid by the lender out of the interest it receives or its own balance; the borrower's obligation is unchanged, so that debts are not reduced by demurrage, which is why the lender's net return in A.4.3 is $r - \delta$.

**A.4.1 Interest-bearing regime ($\rho = r > 0$).** If $y_i - c_i = k_i > 0$ is constant, then

$$W_i(t) = \left(W_i(0) + \frac{k_i}{r}\right) e^{rt} - \frac{k_i}{r},$$

which grows without bound. Two parties with the same net inflow but different initial stocks diverge exponentially, and their difference grows at rate $r$. The dynamic is analogous to the one Piketty (2014) identified in the tendency of inherited wealth to dominate earned income when the return on capital exceeds the growth rate of the economy; the model here contains no growth rate, so the analogy is qualitative.

**A.4.2 Demurrage regime ($\rho = -\delta < 0$).** With the same constant net inflow,

$$W_i(t) = \frac{k_i}{\delta} + \left(W_i(0) - \frac{k_i}{\delta}\right) e^{-\delta t},$$

which converges to the steady state

$$W_i^* = \frac{k_i}{\delta}.$$

Three properties of this result carry the argument of Chapter 4.

1. **Accumulation is bounded.** No party's balance grows without limit. The stock that a given net inflow can sustain is capped at that inflow divided by the demurrage rate.
2. **Initial endowments are forgotten.** The term in $W_i(0)$ decays at rate $\delta$. Inherited or windfall stocks do not compound; they dissipate. The half-life of an idle endowment is $\ln 2 / \delta$. At a demurrage rate of 1 percent per month, this half-life is about 69 months, roughly five years and nine months; at 0.5 percent per month it is about 11.5 years.
3. **Inequality in stocks reduces to inequality in flows.** For two parties with positive net inflows, the ratio of their steady-state balances equals the ratio of their net inflows: $W_i^* / W_j^* = k_i / k_j$ for $k_i, k_j > 0$. Demurrage does not eliminate inequality. It eliminates the compounding of inequality, so that the distribution of holdings mirrors the distribution of current net inflow, income less spending, rather than the history of accumulation.

The third property is the exact form of the limitation acknowledged in Chapter 4: a person whose output is in persistent high demand sustains a large balance, because $k_i$ is large. What demurrage removes is the pathway by which a large balance, once acquired, generates further balances independently of current inflow.

**A.4.3 Converting balances to productive capital or to credit.** The analysis above treats $W_i$ as an idle balance. A party can escape demurrage by converting balances into productive assets, for instance by purchasing compute-generating capacity, whose returns then enter $y_i$. Let $K_i$ denote such capital with return $\pi$. Then $y_i$ includes $\pi K_i$, and if $K_i$ is not itself subject to a holding cost and its returns are reinvested in capacity, $dK_i/dt = \pi K_i$, so that $K_i$ grows exponentially at rate $\pi$: the regime of A.4.1 with $r$ replaced by $\pi$. The compounding channel reopens through capital rather than money. Lending is a second route: a loan that pays interest $r$ and is exempt from demurrage simply reproduces the regime of A.4.1. Chapter 4 therefore applies the holding cost to loan claims as well as to balances, so that the lender's net return is $r - \delta$. That does not close the credit channel: whenever $r > \delta$ the lender is in the positive-return regime of A.4.1 and accumulation through lending is again unbounded, and at $r = \delta$ the claim neither decays nor compounds, so that a constant net flow of new lending raises it without limit, linearly rather than exponentially. Accumulation through credit is bounded only if $r < \delta$, and demurrage on claims otherwise lowers the rate of compounding through credit without removing it. This is the formal statement of the capital channel of concentration (Section 4.8). Demurrage on money alone cannot close it. Closing it requires a holding cost on compute capacity itself, a cap on individually held capacity, or collective ownership of capacity above some scale. Chapter 4 discusses the trade-offs; the formal model shows only that one of them is needed.

## A.5 The power-dependence relation and divided dependence

Following Emerson (1962), write the dependence of party $B$ on party $A$ as an increasing function of $B$'s motivational investment $v_B$ in goals mediated by $A$ and a decreasing function of the availability $\lambda_B$ of those goals outside the relation:

$$D_{BA} = g(v_B, \lambda_B), \qquad \frac{\partial g}{\partial v_B} > 0, \quad \frac{\partial g}{\partial \lambda_B} < 0.$$

Power is $P_{AB} = D_{BA}$. The relation's imbalance is $P_{AB} - P_{BA} = D_{BA} - D_{AB}$.

In the human–synthetic exchange, let $A = s$ and $B = h$. The human party's dependence on synthetic services rises with the importance of those services ($v_h$) and falls with the availability of alternatives ($\lambda_h$), which the framework raises through the floor, portability and competition. The synthetic party's dependence on human data, $D_{sh}$, which Chapter 3 writes $\kappa_j$ for synthetic party $j$, rises with the marginal value of fresh human data to its principal's objective ($v_s$) and falls with the availability of substitutes ($\lambda_s$), including synthetic data, data from environments, and data from populations outside the exchange.

Proposition 4 of Chapter 3 states that the framework's self-enforcing component rises with $\kappa_j$, subject to the premise, stated there, that the quality of the input depends on the terms its source receives; no particular functional form is claimed. The research on recursive training reviewed in Chapter 2 is, in these terms, evidence about $\lambda_s$: if synthetic data substitutes poorly for human data, $\lambda_s$ is low and $\kappa_j$ is high; if a small continuing supply of real data suffices, $\lambda_s$ is high for all but a small residual, and $\kappa_j$ is low.

The second half of Proposition 4 can be illustrated with the simplest model of a commons. Suppose $M$ synthetic parties draw equally on the same population, and that one of them can take an action, such as extracting data in a way that degrades the population's willingness or ability to contribute, which yields it a private benefit $b$ and reduces the value of the population's future input to all $M$ parties by a total of $\gamma$. The acting party bears only its share, $\gamma/M$, of that cost. The action is privately worthwhile whenever $b > \gamma/M$, even when it is collectively destructive, $\gamma > b$. As $M$ grows, the range of destructive actions that are individually rational widens, however large the aggregate dependence of the synthetic parties on the population may be. This is Hardin's (1968) logic applied to the synthetic side of the exchange, and it is the formal reason that material dependence is not sufficient for self-enforcement and that the governance layer is needed even when the grounding assumption holds.

## A.6 Collective exit and the informational shadow

Let a flow from source $i$ materially change what the recipient can infer about the set $\Sigma_i$ of parties, with $i \in \Sigma_i$, materiality being the threshold Section 3.7 assigns to the governance layer. Call $\Sigma_i$ the informational shadow of the flow. Individual consent by $i$ is consent at the right level for the flow only if $\Sigma_i = \{i\}$; whether it is adequate then depends on the remaining clauses of the three conditions. For a population $P$, define its collective shadow as $\Sigma_P = \bigcup_{i \in P} \Sigma_i$. Proposition 5 of Chapter 3 requires that the three conditions be satisfied for the collective whose membership is $\Sigma_P$.

Under information-gain pricing (Chapter 4), the value of a flow to a model is its expected reduction in the model's uncertainty about the model's parameters. Suppose, as is typical for the models that matter here, that those parameters describe regularities of populations rather than facts about individuals. Then a flow reduces uncertainty mainly to the extent that it is informative about many parties, which is to say to the extent that its shadow is large. Under that assumption the price of a flow and the inadequacy of individual consent for it can be expected to rise together. The expectation is a conjecture, not a theorem: where a model's parameters encode individuals, a flow highly informative about one rare person can command a high price while casting a small shadow. To the extent that the conjecture holds, it is the formal reason the economic and governance layers must be designed together.
