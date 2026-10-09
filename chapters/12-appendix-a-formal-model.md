# Appendix A: Formal Model

This appendix gives the minimal mathematics behind the propositions of Chapter 3 and the economic design of Chapter 4. It is intentionally elementary. Every result here is either a textbook consequence of the cited theory or a direct calculation, and the point of setting them out is to show precisely which assumptions each design choice depends on.

## A.1 Notation

| Symbol | Meaning |
|---|---|
| $N(t)$ | Number of enrolled parties at time $t$ |
| $C(t)$ | Total measured global compute in period $t$, in standard compute units |
| $\theta$ | Share of global compute allocated to the basic income (set by the convention, Chapter 5) |
| $\sigma$ | Survival-tier share of each allocation, $0 < \sigma < 1$ |
| $a(t)$ | Per-person allocation, $a(t) = \theta C(t) / N(t)$ |
| $f$ | Physical floor: the bundle of floor goods a party requires per period |
| $p_f(t)$ | Price of the floor bundle in compute units |
| $\bar f$ | Value of the floor bundle, $\bar f = p_f f$, in compute units |
| $d_i$ | Disagreement payoff of party $i$ |
| $D_{BA}$ | Dependence of party $B$ on party $A$ (Emerson) |
| $\kappa_j$ | Dependence of synthetic party $j$, through its principal, on a population's human-generated input |
| $W_i(t)$ | Discretionary balance held by party $i$ |
| $\delta$ | Demurrage rate on idle discretionary balances and loan claims (per period) |
| $r$ | Return on held balances in a conventional interest-bearing regime |
| $y_i(t)$ | Discretionary inflow to $i$ (allocation plus earnings) |
| $c_i(t)$ | Discretionary outflow from $i$ (spending, transfers) |

## A.2 Indexing, the real value of the allocation, and the binding floor

The allocation is defined as a share of total compute, so the per-person quantity is

$$a(t) = \frac{\theta\, C(t)}{N(t)}.$$

Let $p(t)$ be the price of a representative bundle of goods and services measured in compute units. A fixed nominal holding $\bar a$ has real value $\bar a / p(t)$, which falls whenever $p(t)$ rises, that is, whenever compute becomes more abundant relative to the real output it is exchanged against. The indexed allocation instead has real value

$$\frac{a(t)}{p(t)} = \frac{\theta}{N(t)} \cdot \frac{C(t)}{p(t)},$$

which, holding $\theta$ fixed, is the per-capita share $\theta / N$ of the real purchasing power of all compute, $C/p$. Indexing therefore converts the question "does the basic income keep its value?" into the question "does the real value of the world's compute grow faster than population?" That is the correct question for a framework whose premise is that compute is the productive base of the economy. A fixed-quantity design would instead tie the real value of the basic income to the falling relative price of compute, so that the income would shrink as the economy it is supposed to share in grows.

A percentage does not by itself secure the physical floor. The survival tier delivers the floor only if

$$\sigma\, a(t) \ \ge\ \bar f(t) \quad\Longleftrightarrow\quad \sigma\,\frac{\theta\, C(t)}{N(t)} \ \ge\ p_f(t)\, f,$$

and nothing in the arithmetic guarantees this. Chapter 4 therefore makes the tier a percentage with a binding minimum:

$$\sigma(t) = \max\left\{\sigma_0,\ \frac{\bar f(t)}{a(t)}\right\},$$

where $\sigma_0$ is the ordinary survival share. When $\bar f(t) > a(t)$, the allocation as a whole falls short of the floor, and the constraint can be met only by raising $\theta$; that is a decision the convention must take, and it is why the floor standard $f$ becomes a contested parameter (Chapters 5 and 8).

## A.3 The survival tier as a disagreement payoff

Consider a single exchange between a human party $h$ and a synthetic party $s$ in which agreement makes total value $V$ available for division, with $V > d_h + d_s$, where $d_h$ and $d_s$ are the disagreement payoffs. With transferable utility, the Nash bargaining solution (Nash, 1950) maximizes $(u_h - d_h)(u_s - d_s)$ subject to $u_h + u_s = V$. Each party receives its disagreement payoff plus half the surplus $V - d_h - d_s$:

$$u_h^* = d_h + \frac{V - d_h - d_s}{2} = \frac{V + d_h - d_s}{2}, \qquad u_s^* = \frac{V - d_h + d_s}{2}.$$

**A.3.1 What an unconditional floor does to the division of surplus.** Suppose the survival tier gives $h$ goods worth $\Delta$ per period, received whether or not agreement is reached. Two cases must be distinguished.

*The purely additive case.* If the tier is simply added to whatever $h$ has, it raises $h$'s payoff on disagreement and $h$'s payoff on agreement by the same amount: $d_h$ becomes $d_h + \Delta$ and $V$ becomes $V + \Delta$. The surplus $V - d_h - d_s$ is unchanged, and

$$u_h^{*\prime} = \frac{(V + \Delta) + (d_h + \Delta) - d_s}{2} = u_h^* + \Delta.$$

The human party is better off by exactly the value of the tier and no more. The division of the surplus is unchanged.

*The substitution case.* If the tier replaces something $h$ would otherwise have obtained from $s$ within the exchange, for example floor goods previously bought from the provider it is bargaining with, then the value of agreement is unchanged while $h$'s disagreement payoff rises: $d_h$ becomes $d_h + \Delta$ with $V$ fixed. Then

$$u_h^{*\prime} = u_h^* + \frac{\Delta}{2}, \qquad u_s^{*\prime} = u_s^* - \frac{\Delta}{2}.$$

The human party's share of the surplus rises at the synthetic party's expense. This is not a benefit additional to the tier; it is a transfer of surplus from $s$ to $h$, and it is the bargaining counterpart of the fall in $h$'s dependence on $s$ that occurs when an alternative source of a valued good appears (A.5).

The working draft of this dissertation claimed that an unconditional floor raises the human party's payoff by an additional $\Delta/2$ in every exchange it enters. That claim was wrong in two ways: it ignored the additive case, in which there is no such effect, and it counted one floor as a separate gain in every bilateral bargain. The floor's most important bargaining effect is the one in A.3.2.

**A.3.2 The impatience constraint.** If $d_h < \bar f$, the human party cannot sustain disagreement for longer than its stocks allow. In strategic models of alternating offers, the parties' time preferences are among the incentives that drive agreement, and the outcome converges to the Nash solution as the frictions of delay vanish (Binmore et al., 1986). A party below the floor faces a very high cost of delay and so bargains as an extremely impatient party, which weakens its position in every exchange. Raising $d_h$ to at least $\bar f$ removes this source of weakness. Unlike the effect in A.3.1, this does not depend on whether the floor substitutes for anything the counterparty supplies. Proposition 1 of Chapter 3 is the qualitative statement of this constraint.

**A.3.3 Why inalienability matters.** Suppose the survival tier could be pledged against a loan. In a period of need, a party pledges it and receives a lump sum $L$. For the duration of the pledge its disagreement payoff falls by the value of the pledged tier, and if that pushes $d_h$ below $\bar f$, the impatience of A.3.2 returns in every exchange the party enters until the pledge is redeemed. The pledge thus has a hidden cost beyond the loan's interest. Because the parties most likely to pledge are those in the most acute need, alienability concentrates this hidden cost on the weakest. Making the tier non-tradable and non-borrowable is equivalent to prohibiting this transaction (Calabresi & Melamed, 1972).

**A.3.4 Outside options versus disagreement payoffs.** If instead of a floor the human party is given an outside option $o_h$, a second provider it may switch to, the outside-option principle (Binmore et al., 1989) implies that the bargained payoff is $\max\{u_h^*, o_h\}$ evaluated with $d_h$ unchanged: the option matters only if it binds. When it binds, the stronger party can confine the weaker to the option's value, and can lower that value by raising switching costs. A disagreement payoff at or above the floor protects in a different way, because it removes the impatience of A.3.2 whether or not anyone leaves. This is the formal reason the framework prefers a guaranteed floor to a guarantee of competition, while still requiring both.

## A.4 Demurrage and the dynamics of accumulation

Let party $i$'s discretionary balance evolve in continuous time as

$$\frac{dW_i}{dt} = y_i - c_i + \rho\, W_i,$$

where $\rho$ is the rate at which the balance grows or shrinks merely by being held. The analysis below concerns positive balances. Under the rules of Chapter 4, demurrage applies to positive balances and to outstanding loan claims held by lenders; negative balances, debts owed, do not decay, so demurrage forgives no debt.

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

**A.4.3 Converting balances to productive capital or to credit.** The analysis above treats $W_i$ as an idle balance. A party can escape demurrage by converting balances into productive assets, for instance by purchasing compute-generating capacity, whose returns then enter $y_i$. Let $K_i$ denote such capital with return $\pi$. Then $y_i$ includes $\pi K_i$, and if $K_i$ is not itself subject to a holding cost, the compounding channel reopens through capital rather than money. Lending is a second route: a loan that pays interest $r$ and is exempt from demurrage simply reproduces the regime of A.4.1. Chapter 4 therefore applies the holding cost to loan claims as well as to balances, so that the lender's net return is $r - \delta$. This is the formal statement of the "billionaire problem one layer up." Demurrage on money alone cannot close the capital channel. Closing it requires a holding cost on compute capacity itself, a cap on individually held capacity, or collective ownership of capacity above some scale. Chapter 4 discusses the trade-offs; the formal model shows only that one of them is needed.

## A.5 The power-dependence relation and divided dependence

Following Emerson (1962), write the dependence of party $B$ on party $A$ as an increasing function of $B$'s motivational investment $v_B$ in goals mediated by $A$ and a decreasing function of the availability $\alpha_B$ of those goals outside the relation:

$$D_{BA} = g(v_B, \alpha_B), \qquad \frac{\partial g}{\partial v_B} > 0, \quad \frac{\partial g}{\partial \alpha_B} < 0.$$

Power is $P_{AB} = D_{BA}$. The relation's imbalance is $P_{AB} - P_{BA} = D_{BA} - D_{AB}$.

In the human–synthetic exchange, let $A = s$ and $B = h$. The human party's dependence on synthetic services rises with the importance of those services ($v_h$) and falls with the availability of alternatives ($\alpha_h$), which the framework raises through the floor, portability and competition. The synthetic party's dependence on human data, $D_{sh}$, which Chapter 3 writes $\kappa_j$ for synthetic party $j$, rises with the marginal value of fresh human data to its principal's objective ($v_s$) and falls with the availability of substitutes ($\alpha_s$), including synthetic data, data from environments, and data from populations outside the exchange.

Proposition 4 of Chapter 3 states that the framework's self-enforcing component rises with $\kappa_j$; no particular functional form is claimed. The research on recursive training reviewed in Chapter 2 is, in these terms, evidence about $\alpha_s$: if synthetic data substitutes poorly for human data, $\alpha_s$ is low and $\kappa_j$ is high; if a small continuing supply of real data suffices, $\alpha_s$ is high for all but a small residual, and $\kappa_j$ is low.

The second half of Proposition 4 can be illustrated with the simplest model of a commons. Suppose $M$ synthetic parties draw equally on the same population, and that one of them can take an action, such as extracting data in a way that degrades the population's willingness or ability to contribute, which yields it a private benefit $b$ and reduces the value of the population's future input to all $M$ parties by a total of $c$. The acting party bears only its share, $c/M$, of that cost. The action is privately worthwhile whenever $b > c/M$, even when it is collectively destructive, $c > b$. As $M$ grows, the range of destructive actions that are individually rational widens, however large the aggregate dependence of the synthetic parties on the population may be. This is Hardin's (1968) logic applied to the synthetic side of the exchange, and it is the formal reason that material dependence is not sufficient for self-enforcement and that the governance layer is needed even when the grounding assumption holds.

## A.6 Collective exit and the informational shadow

Let a flow from source $i$ license inferences about the set $\Sigma_i$ of parties, with $i \in \Sigma_i$. Call $\Sigma_i$ the informational shadow of the flow. Individual consent by $i$ is adequate for the flow if and only if $\Sigma_i = \{i\}$. For a population $P$, define its collective shadow as $\Sigma_P = \bigcup_{i \in P} \Sigma_i$. Proposition 5 of Chapter 3 requires that the three conditions be satisfied for the collective whose membership is $\Sigma_P$.

Under information-gain pricing (Chapter 4), the value of a flow to a model is its expected reduction in the model's uncertainty about the model's parameters. Suppose, as is typical for the models that matter here, that those parameters describe regularities of populations rather than facts about individuals. Then a flow reduces uncertainty mainly to the extent that it is informative about many parties, which is to say to the extent that its shadow is large. Under that assumption the price of a flow and the inadequacy of individual consent for it can be expected to rise together. The expectation is a conjecture, not a theorem: where a model's parameters encode individuals, a flow highly informative about one rare person can command a high price while casting a small shadow. To the extent that the conjecture holds, it is the formal reason the economic and governance layers must be designed together.
