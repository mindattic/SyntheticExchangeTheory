# Chapter 2: Literature and Grounding

The three conditions have a long scholarly lineage, and each has a known weak point. This chapter maps that terrain and the empirical claim the framework rests on.

**Consent and its limits.** Acquisti, Brandimarte and Loewenstein (2015) show that privacy choices are context-dependent and manipulable, and that people often lack the information to make informed tradeoffs. Solove (2013) argues that notice-and-choice does not scale to the volume and complexity of modern data flows, so individual agreement becomes a formality. Nissenbaum (2010) supplies contextual integrity: a flow is appropriate when it matches the norms of the context in which the data was shared. Together these show why the consent condition is hard to meet today.

**The strongest objection: relational data.** Viljoen (2021) argues that data about one person is also data about people like them, so individual consent cannot legitimize a flow. Barocas and Nissenbaum (2014) make a related point about big data's end run around consent. The framework must answer this: if consent is individual and the harm is collective, the three conditions need a collective counterpart, such as data trusts or cooperatives.

**Data as labor.** The idea that data is labor and services are wages has a real lineage: Posner and Weyl's (2018) *Radical Markets*, Lanier's "data dignity," and Ibarra et al.'s treatment of data as labor (Ibarra et al., Critics argue that it commodifies privacy and fails for collective data. This dissertation takes the reciprocity insight and rejects a pure per-person market, for the reasons Chapter 3 gives.

**Existing institutions.** The realistic cases are GDPR portability and erasure rights, the EU AI Act, health-data regimes, data trusts and neural-data laws (to be verified for current status before citing).

**The empirical anchor: model collapse.** The framework's grounding assumption is that AI systems keep needing fresh human-generated data. Current research supports a version of this. Analyses of recursive training on synthetic data find that variance shrinks and the rare tails of the distribution disappear. A 2026 *Physical Review Letters* paper on closed-loop learning in exponential families finds that training only on a model's own output leads to collapse, and that injecting even one real data point at each retraining step, or adding regularization, avoids it. Two cautions apply. The result covers simplified statistical models, not frontier systems. And it cuts both ways: collapse can be prevented by a small continuous trickle of outside signal, so human dependency may be real but small. Chapter 5 returns to this.

*Source note: Acquisti, Nissenbaum and Solove were checked in the earlier draft. Viljoen, Barocas and Nissenbaum, Posner and Weyl, Lanier and Ibarra et al. are cited from memory and need verification before submission.*
