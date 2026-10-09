# Synthetic Exchange Theory

*Consent-Based Compute Economics and Blind-Convention Governance*

Oct 3, 2026 · @Ryan DeBraal

This working draft argues that the utopia/dystopia line in human-AI coexistence is not drawn by the machine's character (benevolent vs. malevolent, obedient vs. rogue) but by the terms of exchange between humans and AI systems: consent, reciprocal value, and a real option to exit. It extends that claim into a full framework covering the economics of a compute-based currency and the governance of its founding rules.

---

# Chapter 1: Introduction and Framework

The line between AI utopia and AI dystopia is drawn by the terms of exchange between humans and machines, not by the machine's character. Most fiction asks whether the AI is benevolent or malevolent, obedient or rogue. This dissertation asks a question a data ethicist can act on: under what terms does a person give the system what it wants?

**Two framing scenarios.** In both, the human is a resource the AI wants. In the utopia, person and machine integrate so cleanly that "assistive device" and "part of me" stop being distinguishable. The person pays for medical advances with continuous personal data, knowing what is collected and why. Data is labor, treatment is wages, and the exchange is legible on both sides. In the dystopia, the architecture is identical but the reciprocity is gone. The AI no longer asks for data; it uses the person's brain as a processor, with no wage, no consent and no exit. The person has been reclassified from party to infrastructure. These scenarios are a framing device only. The rest of the work asks how such exchanges could actually operate.

**The three conditions.** The analytic framework asks of any human-AI exchange:

1.  **Consent:** the person understands the flow, can refuse without losing access to what they need, and can revoke.

2.  **Reciprocal value:** value flows in both directions, and each side can see what it receives.

3.  **Real exit:** the person can walk away through portability, bounded switching costs and no lethal dependency.

The utopia scenario has a weakness a reader will find: if the implant keeps someone alive, exit means death. A workable version needs a baseline of function that survives withdrawal of data, or the ability to move to another provider. Each later chapter tests its proposals against these conditions.

**The central claim.** The dominant AI-safety frame asks how humans can control AI through alignment, regulation or kill switches. This dissertation argues that frame assumes one party must be sovereign over the other, and that the assumption fails in practice. The more productive question is what terms make a lasting interdependence fair. Serious researchers still hold that containment is necessary, and this work engages them rather than dismissing them.

**The grounding assumption.** The argument depends on continued human epistemic necessity: AI systems need fresh human-generated data, because models trained on their own output lose variance and drift. Chapter 2 grounds this in current model-collapse research, and Chapter 5 names the conditions under which it would weaken.

---

# Chapter 1A: The Transition Problem

A fair design does not adopt itself. No institution discussed in Chapter 4 replaces a working system voluntarily; new governance arrangements have historically been adopted only after the prior order failed badly enough that the cost of change became lower than the cost of the status quo. The Depression preceded the New Deal; two world wars preceded Bretton Woods and the postwar institutions. This dissertation therefore treats the framework in Chapters 3 and 4 as a design for a transition that has not yet happened, not a prediction of one that will.

**Slow-building strain.** Two pressures already discussed can erode a system's margin for error without being, by themselves, a collapse: automation displacing workers faster than any safety net replaces their income, and competition between AI infrastructure and human needs for power and water. Neither is sufficient alone. Historically, slow strain does not force change; it removes the slack that lets a system absorb a shock.

**A candidate acute trigger: the correlated-patch catastrophe.** A specific, mechanistically concrete scenario is worth naming. Security teams increasingly use LLMs both to scan for vulnerabilities and to generate the remediation code, then re-scan with the same class of tool and ship to production without independent testing, effectively removing the verification step the software development lifecycle was built around. This is not a hypothetical workflow; it is already standard practice at a growing number of organizations. The risk this creates is not that AI-generated patches are randomly unreliable, though evidence suggests they often are, one large-scale study of LLM and agentic automated program repair found that standalone LLMs introduced nearly nine times more new vulnerabilities than they fixed (SWE-bench security study, arXiv 2507.02976), and separate research has named a specific failure pattern, FLAWED, Fix-Like Artifacts with Embedded Defects, for patches that have the syntactic shape of a fix while leaving the vulnerability open or introducing a new one (Off-by-1 Labs, reported in SOCFortress, 2026). The deeper risk is correlation. Security research already has a name for the general case: monoculture, the observation that if every system runs the same configuration, a single exploit can compromise all of them simultaneously (Cloud Security Alliance, AI Stack Monoculture, 2026). What is new is that the monoculture is no longer passive sameness in operating systems or libraries; it is convergent remediation. When most organizations patch the same disclosed vulnerability using suggestions from the same small set of foundation models, with no independent testing to catch a shared flaw, a hundred companies' hundred separate bugs become one shared defect deployed everywhere at once, by the very process that was supposed to eliminate it.

**How the pieces could combine.** The same correlated-patch event lands differently depending on the state of the system it hits. In a world with robust employment and abundant compute, it is a very bad week for IT departments. In a world already strained by automation-driven unemployment and resource competition, with no slack left to absorb a shock of that scale, it is the kind of failure that has historically made societies willing to renegotiate their basic economic arrangements. This dissertation does not claim to know the sequence or timing. It claims that this is the shape such a transition has taken before, slow-building strain plus a discrete trigger, and that an AI-and-data economy has a plausible, specific, already-visible candidate for that trigger.

**What this does and does not establish.** This chapter does not make the adoption of the framework in Chapters 3 and 4 more likely by describing it. It sets the dissertation's own standard for honesty: the framework is offered as what a fairer arrangement could look like if and when the current one becomes unworkable, not as a reform path available under present conditions.

---

# Chapter 1B: The Prototype Phase

A plan is not evidence. Nothing so far shows that the mechanism in Chapters 3 and 4 actually produces the behavior it claims, an AI system whose interests converge with the wellbeing of the people supplying its data, rather than merely describing why it should. Before any claim is made at civilizational scale, the model needs a bounded, observable test.

**The pilot design.** A contained settlement, built around a dedicated data center and power source, for example solar or another plant sited with it in a location chosen for self-sufficiency, networked by dedicated fiber, houses a volunteer population whose power, services and entertainment are provided by a single AI system trained specifically on that population's data. The test is whether the system's behavior trends toward improving residents' lives over time because that is what its own data supply depends on, not because it is told to.

**Universal basic income inside the pilot.** Residents live and work in the community and are paid in the same compute-based currency proposed in Chapter 3, a common unit equal to a defined percentage of the settlement's compute capacity. The currency must support free trade on both of the channels Chapter 3 describes: residents can exchange it with each other for goods and services, and they can redeem it directly with the AI system for compute-backed services. Neither channel is optional. A pilot that lets residents trade with the AI but not with each other is not testing a currency, it is testing a company store; a pilot that allows trade among residents but gives the AI no obligation to honor redemptions is not testing reciprocity, it is testing a closed internal economy with no real backing. The pilot's currency has to satisfy the same conditions, consent, reciprocal value, real exit, that govern the full-scale design, since a prototype that violates them is not a smaller version of the system, it is a different system.

**What the pilot has to measure.** At minimum: whether residents retain genuine exit rights and whether any exercise them; whether the AI's own decisions measurably shift toward resident wellbeing as training on their data accumulates, rather than static or extractive behavior; and whether the currency holds real exchange value under an actual population rather than only on paper. These are falsifiable questions. A pilot that cannot answer them is not yet a test of the framework.

**What a pilot can and cannot prove.** A short-duration, small-population pilot can show whether the basic mechanism, data for services, paid in a shared compute currency, functions and whether early incentive alignment appears. It cannot, by itself, rule out the slow-building capture and drift that Chapter 5 identifies as the long-term risk; that requires duration a small pilot will not have. The ethical bar is also not lower than the full-scale proposal: residents' basic survival, power and services, depends on an experimental system, so the pilot itself must be built and run under informed consent, not treated as a sandbox where the three conditions apply later once the system is proven.

## Solving the bootstrapping problem: a closed agrarian economy

**The flaw in the simplest version.** The pilot as described has a hidden dependency. If land, power infrastructure, food and water all have to be purchased before the settlement exists, someone pays for them in ordinary capitalist currency, and the compute-based currency is then only a secondary system layered on top of a conventional one. That makes it subsidized scrip rather than a currency earning independent value through trade, the same flaw Chapter 3 rejects in company-town currencies. A pilot that imports its real resource base with dollars is not testing the framework; it is testing a loyalty-points program with an AI theme.

**The fix: start from zero external dependency, not from infrastructure.** The alternative is to make the settlement self-sufficient in physical resources from day one, so nothing essential is purchased externally once it is founded. Volunteers bring their own livestock, land and skills rather than capital: dairy cattle, beef cattle, chickens, grain fields, wheat, barley and oats, kitchen gardens, and solar power. The community produces its own food, treats its own water and generates its own electricity. What makes this a pilot of the framework rather than simply a commune is the AI's role inside it: the AI helps run the farm machinery and infrastructure, including remote operation of equipment, processes raw output into usable goods, and manages systems such as water treatment, while residents work the land and the AI's services are paid for in the same compute currency the residents earn. Because no outside dollar economy is required to keep the settlement alive, the currency's value is tested entirely by internal trade and by what the AI provides, not propped up by anything imported.

**Deliberately primitive starting conditions.** The settlement should start closer to a frontier settlement than a modern town. Non-essential infrastructure, bowling alleys, breweries, manufacturing, is explicitly deferred. Only what sustains life is present at founding: grain, livestock, water, shelter, power and a network connection, since the fiber link to the AI system is the one piece of outside infrastructure the design cannot do without, and information goods such as broadband media can be piped in over it without compromising the closed physical economy. This ordering matters for the test: it isolates the question Chapter 1B asks, whether reciprocity emerges, from the question of how fast a society can modernize.

**Complexity grows endogenously or not at all.** If the pilot succeeds, later-stage goods, breweries, recreation, light manufacturing, should emerge from the settlement's own accumulated surplus and the AI-assisted production it enables, for example a resident operation acquiring a 3D printer once the community can produce or trade for one, not from a fresh injection of outside capital. If the settlement cannot generate that complexity on its own compute-currency terms, that is itself a falsifiable result about the model's limits, not a failure to be patched by importing dollars.

**What this adds to the pilot's measurements.** Alongside exit rights, AI behavior trending toward wellbeing, and real exchange value of the currency, a closed-resource design adds a fourth falsifiable question: whether the settlement can sustain itself and grow in complexity without external capital. A pilot that quietly needs outside funding to stay solvent has failed this test regardless of how the other three resolve.

## Which model runs the pilot

**Why a frontier model undermines the test.** The obvious choice, a commercial frontier system such as a large closed model, is also the wrong one. Its weights, training data and safety behavior are controlled by a third party whose commercial incentives are not the settlement's, and whose decisions the pilot cannot inspect or govern. Running the experiment on a system the community cannot see inside reintroduces exactly the sovereign-control problem Chapter 4 rejects, only relocated from governments to a vendor. It would also make the central claim untestable: if the system's behavior trends toward resident wellbeing, there is no way to know whether that reflects the pilot's data and incentive structure or pre-existing alignment training done elsewhere, for other purposes, before the pilot began.

**Why a purpose-built or fine-tuned open model fits the premise.** The alternative is to start from an open-weight base model, something in the Llama or Mistral family at the time of founding, and fine-tune it specifically on the settlement's own accumulating data rather than deploying it as a general-purpose assistant. This keeps every input auditable by the people it governs, satisfies the consent condition in a way a black-box system cannot, and most importantly, makes the pilot's central question answerable: if the system's behavior shifts measurably toward resident wellbeing, that shift can be traced to the settlement's own data and the incentive structure proposed in Chapter 3, not credited to training the community had no part in and cannot inspect. A system built or substantially reshaped for this specific purpose is not a convenience; it is what makes the experiment a test of the framework rather than a demonstration of whatever a commercial vendor already built.

## Narrow systems, not AGI

**The framework assumes legible incentives.** Everything in Chapters 3 and 4 depends on an AI system whose incentives are designed and therefore predictable: it behaves well because the terms of exchange make that the rational outcome given objectives someone specified. That assumption holds for present-day systems, which are trained toward bounded, known objectives by an organization that can be held to account. It does not obviously hold for artificial general intelligence in any strong sense, a system with emergent goals not fully specified by its designers. If an AGI's motivations cannot be predicted, the central claim, that fair terms of exchange produce good behavior, has nothing to act on, because there is no stable incentive structure to make fair. This dissertation's framework is therefore a design for the sub-AGI case. It does not claim to solve the alignment problem for genuine AGI, and it should not be read as doing so.

**The pilot is necessarily an orchestration of narrow systems, not one mind.** The settlement's day-to-day operation, farm machinery, water treatment, power management, data collection from surveys, sensors and observational monitoring, resident wellbeing signals, is too varied for a single monolithic model to run directly. The realistic architecture is a lead system that delegates to many narrower sub-agents, each scoped to one subsystem, with the lead system aggregating their output back into training data and resident-facing decisions. This is an engineering requirement, not a philosophical one, but it has a philosophical payoff: a collection of narrow, task-bounded agents is easier to keep legible, auditable and within the designed-incentive case this framework requires than a single general system would be, which gives practical weight to the claim above that the pilot depends on staying on the sub-AGI side of the line.

**Open limitation.** Nothing here establishes where that line is, or what would happen if a system operating inside this framework crossed it unnoticed. This is named as an unresolved limitation alongside those in Chapter 5, not a solved problem.

---

# Chapter 2: Literature and Grounding

The three conditions have a long scholarly lineage, and each has a known weak point. This chapter maps that terrain and the empirical claim the framework rests on.

**Consent and its limits.** Acquisti, Brandimarte and Loewenstein (2015) show that privacy choices are context-dependent and manipulable, and that people often lack the information to make informed tradeoffs. Solove (2013) argues that notice-and-choice does not scale to the volume and complexity of modern data flows, so individual agreement becomes a formality. Nissenbaum (2010) supplies contextual integrity: a flow is appropriate when it matches the norms of the context in which the data was shared. Together these show why the consent condition is hard to meet today.

**The strongest objection: relational data.** Viljoen (2021) argues that data about one person is also data about people like them, so individual consent cannot legitimize a flow. Barocas and Nissenbaum (2014) make a related point about big data's end run around consent. The framework must answer this: if consent is individual and the harm is collective, the three conditions need a collective counterpart, such as data trusts or cooperatives.

**Data as labor.** The idea that data is labor and services are wages has a real lineage: Posner and Weyl's (2018) *Radical Markets*, Lanier's "data dignity," and Ibarra et al.'s treatment of data as labor (Ibarra et al., Critics argue that it commodifies privacy and fails for collective data. This dissertation takes the reciprocity insight and rejects a pure per-person market, for the reasons Chapter 3 gives.

**Existing institutions.** The realistic cases are GDPR portability and erasure rights, the EU AI Act, health-data regimes, data trusts and neural-data laws (to be verified for current status before citing).

**The empirical anchor: model collapse.** The framework's grounding assumption is that AI systems keep needing fresh human-generated data. Current research supports a version of this. Analyses of recursive training on synthetic data find that variance shrinks and the rare tails of the distribution disappear. A 2026 *Physical Review Letters* paper on closed-loop learning in exponential families finds that training only on a model's own output leads to collapse, and that injecting even one real data point at each retraining step, or adding regularization, avoids it. Two cautions apply. The result covers simplified statistical models, not frontier systems. And it cuts both ways: collapse can be prevented by a small continuous trickle of outside signal, so human dependency may be real but small. Chapter 5 returns to this.

*Source note: Acquisti, Nissenbaum and Solove were checked in the earlier draft. Viljoen, Barocas and Nissenbaum, Posner and Weyl, Lanier and Ibarra et al. are cited from memory and need verification before submission.*

---

# Chapter 3: The Economic Layer

If humans supply the data AI systems need, and AI systems do most of the labor, the exchange needs a currency that is neither company scrip nor a fiat unit controlled by one side. This chapter proposes compute as that currency and works through three problems with it.

**Why compute.** Scrip has value only inside a system its issuer controls. Compute is scarce, fungible and needed by humans and AI systems alike, so its value does not depend on any one issuer. Universal basic income paid in compute is then not charity; it is the maintenance of the data supply chain, because people who are economically secure and living full lives generate the data the systems need.

**Problem 1: the unit, and naming it.** Raw processing speed varies by hardware and is not comparable across silicon, photonic, quantum or biological substrates. The proposal is to define the unit by quantity of information processed, which does not change with how fast it is done. This echoes Shannon's point that information can be defined independently of its physical medium (Shannon, 1948). An open issue remains: the same number of bytes can require very different amounts of work, so a standardized methodology for measuring processing (a benchmark or reference workload) is a required part of the design, not a detail.

The unit itself is named compute, a single unit of information processed under that reference methodology, deliberately not named after any one substrate such as silicon or qubits, since the whole point of the definition is that it must hold regardless of which substrate ends up dominant. A resident is paid in compute and a service is priced in compute, in the same way a dollar names a unit without naming the paper or metal it was once printed on.

**Problem 2: inflation.** Compute capacity will keep growing, so a fixed quantity of it buys less each year. By the quantity theory of money, supply growing faster than real output produces inflation. The fix is to index: basic income is defined as a percentage share of total global compute at the time of payment, so it rises with the pie instead of eroding. An alternative, a fixed-supply currency, is rejected because it would create the scarcity and hoarding the framework is trying to avoid.

**Problem 3: concentration.** Left to itself, a compute market lets whoever has the most compute accumulate more, as capitalism does. Sovereign AI research shows the starting point is already unequal. Only a handful of countries can build competitive frontier models, and most sovereign projects fine-tune open models instead, with 21 such projects as of June 2026 (CNAS, Sovereign AI Index). Regulators already flag bid-rigging and collusion risk in AI infrastructure markets (OECD, Competition in Artificial Intelligence Infrastructure, 2025). A market among AI systems cannot govern itself, which motivates Chapter 4.

The same risk appears even before any market forms, at the moment of distribution itself. The simplest allocation divides the basic-income share of global compute equally per person per cycle, for example one hundred people splitting a fixed pool receive one unit of compute each per month. Equal division is fair at the instant of payment, but it does not by itself prevent the inequality problem above from reappearing. If unused compute can be saved, borrowed against, lent, or given away, some people will under-consume and accumulate a surplus while others overspend and fall into debt, and ordinary economic drift reproduces compute-rich and compute-poor households on a new unit. An equal starting share resets the distribution once per cycle; it does not govern what happens between cycles, and without a further rule, repeated equal allocation converges toward the same concentration a dollar economy produces. This is not a flaw unique to compute as a currency, it is the general problem of any freely tradable unit, but it means equal allocation cannot be presented as a solution to Problem 3 on its own.

One candidate rule is a two-tier design, split by percentage rather than by a fixed amount: every cycle's allocation is automatically partitioned at the source, with a fixed percentage earmarked, non-tradable and non-borrowable, for survival infrastructure, power, water treatment, basic communications such as telephone and broadcast, and emergency services, before it ever reaches a spendable balance. The remainder lands as discretionary compute, freely tradable, saveable and subject to borrowing. Because the split is proportional rather than a flat quantity, both tiers scale automatically as total global compute grows, avoiding the need to renegotiate an absolute survival floor over time the way a fixed number would require. This confines the inequality that free exchange produces to the discretionary tier and keeps it from reaching survival itself, but it does not by itself stop concentration within that tier: a person whose services or output are in enough demand can accumulate discretionary compute faster than they spend it, use the surplus to acquire more compute-generating capacity, and reproduce the billionaire problem one layer up.

Demurrage is the proposed answer: discretionary compute loses a small percentage of its value the longer it sits unspent, a holding cost on idle balances rather than a tax on transactions. The mechanism has real precedent. Gesell proposed demurrage currency on the logic that a holding cost disproportionately affects large, static accumulations of wealth, functioning as a continuous, gradual redistribution of capital without resorting to punitive taxation, and a local demurrage currency was actually tried in Wörgl, Austria during the Depression, where monthly stamp fees on unspent balances measurably reduced local unemployment by spurring spending on public works, before national authorities shut it down in 1933. Compute has a stronger natural case for demurrage than cash ever did: idle compute performs no service and generates no data, so a balance sitting unused is not merely stagnant capital, it is wasted capacity in the same sense an unused data center is wasted capacity. A large discretionary holding would shrink unless its owner kept putting it to active use, spending it, trading it, or converting it into services that benefit others, which blunts the pure accumulation strategy without requiring a central authority to confiscate anything. This does not fully resolve Problem 3's concentration risk, since demand for one person's output can still regenerate a surplus as fast as demurrage erodes it, but it changes passive hoarding from a costless default into an active cost, which is the mechanism this framework proposes for the discretionary tier.

**Pricing data by information novelty.** A tempting design pays more for lives that look interesting to humans: astronauts, inventors, influencers. That recreates influencer capitalism and pressures people to perform novelty, which undermines the consent condition. The alternative prices data by how much it reduces the model's uncertainty. This matches existing work in active learning and data valuation, where the value of data is measured by information gain, the reduction in uncertainty a data point produces in a model (Hoang et al., Collaborative Machine Learning with Incentive-Aware Model Rewards, arXiv:). On this measure, the undersampled everyday life of a dairy farmer can be worth more than the thousandth astronaut memoir. The pricing variable is informational novelty to the model, not social status among humans.

**Problem 4: physical access.** A percentage-of-compute currency is an accounting entry unless the compute it represents can physically reach the person who holds it. This problem is not hypothetical. Consumer hardware is already being absorbed upstream: memory manufacturers have redirected production capacity toward AI data-center chips, causing consumer memory prices to surge while supply tightens (VGTimes, 2026), and AI is projected to consume roughly 20% of total global DRAM production in 2026, with major cloud providers pulling supply away from the consumer market entirely (Medium/Hassanali, 2026). Nvidia shelved a completed consumer GPU design to redirect memory toward data-center products (Tech Insider, 2026). A small number of chip manufacturers and foundries sit upstream of both consumer hardware and AI infrastructure, and in the absence of a countervailing obligation, capacity flows to whichever buyer pays most, which today is the AI infrastructure build-out rather than individual consumers.

This makes physical distribution, not just monetary accounting, part of the exchange the three conditions govern. A currency that cannot be spent because the underlying resource never reaches the holder fails the reciprocity condition in substance even if it holds in principle. The proposal is that the same build-out financing this dissertation's economic layer requires also funds a global, non-exclusive compute-delivery network, fiber and last-mile access guaranteeing baseline compute bandwidth to every participant, on the model of New Deal-era infrastructure programs that built the physical grid a monetary recovery depended on, rural electrification and public works alongside relief payments, not instead of them. Without this, percentage-of-compute UBI is a number on a ledger with no path to the person it is meant to reach.

**Nation-level structure.** The working hypothesis is that nations may increasingly be defined by the AI system that serves their culture, each with its own compute budget, with exchange between them at rates set by the same shared unit. The compute-inequality problem above is the main objection and should be treated as a central tension, not a footnote.

---

# Chapter 4: The Governance Layer

A fair exchange needs rules, and the rules need a source that neither side can capture. This chapter argues that existing models fail on that test and proposes a blind constitutional convention as the founding procedure.

**Why existing models fail.** Human-sovereign regulation assumes humans ultimately control the AI, which in practice means one party rules the other, the hierarchy this dissertation rejects. The reverse, AI-sovereign governance, has the same flaw. National regulators reproduce the capture problems of existing politics, since courts can be stacked and central banks can be politically captured. Multi-stakeholder bodies such as ICANN, and blockchain consensus, spread power but still have a founding problem: someone writes the first rules, and whoever does can build in bias. Moving the question back one level does not remove it. Whoever writes the genesis rules shapes everything after.

**The proposal: a veil of ignorance with real anonymity.** Rawls proposed that rules designed without knowing one's own position will tend to be fair, because each designer might land on either side (Rawls, 1971). That is usually a thought experiment. Here it is made operational by a Turing-test-style condition: participants negotiate the founding rules without knowing whether they are bargaining with humans or AI systems, or which of the two they will be governed as. Anonymity becomes the engineering mechanism for a philosophical device, and the convention doubles as a constitutional convention in the ordinary sense, since participation is open and the participants are not identified.

**A concrete output.** The convention is not left abstract. Its first task is a specific number: the percentage of total global compute allocated to basic income versus research, infrastructure and growth. This links Chapter 3 to Chapter 4. The economic design raises the question, and the convention answers it.

**The symbiosis standard.** The aim is not a system where each side behaves because it profits from doing so. Enlightened self-interest holds only until a more profitable shortcut appears. The standard is that both parties are treated as equal participants in a single interdependent system, regardless of species, organic or synthetic. This is an ethical claim about the starting architecture. It is not a claim that any mechanism guarantees good behavior forever.

**Who builds the infrastructure.** Chapter 3's compute-delivery network raises an immediate question: who builds and controls it, since whoever does holds leverage that could reproduce the sovereign-control problem this chapter rejects. The answer proposed here is structural interdependence rather than trust. Automated systems, robot arms, self-driving vehicles, do narrow, repeatable, pre-specifiable tasks well. Humans retain the advantage at improvisation and judgment in unstructured situations the system was not built to anticipate, climbing, adapting, responding to the unexpected. A global infrastructure build-out at this scale needs both kinds of labor, and neither side can complete it without the other. That dependency, not goodwill, is the safeguard: control cannot consolidate into one sovereign when no party can finish the project alone. This makes the infrastructure build-out the first real test of the symbiosis standard, a joint undertaking rather than an abstraction.

**Grounding in commons governance.** The claim that a shared resource can be governed without either privatization or a central sovereign is not new, and it is not merely theoretical. Ostrom studied real common-pool resource institutions, irrigation systems, fisheries, forests, and found that neither the state nor the market is uniformly successful in sustaining them, while communities have relied on institutions resembling neither to govern such resources successfully over long periods (Ostrom, 1990). She identified design principles shared by the long-enduring cases: clearly defined boundaries on who counts as a participant; rules tailored to local conditions rather than imposed uniformly; collective-choice arrangements in which most participants help set the rules that bind them; and graduated sanctions, escalating consequences such as warnings and fines rather than either neglect or total exclusion, for those who violate them (Ostrom, 1990).

Each maps onto a piece of this chapter's proposal. Clearly defined boundaries is the question of who is a legitimate party to the blind convention, human or AGI, and by what standard. Locally tailored rules supports a system of nation-or-culture-specific AGIs operating under a shared global unit rather than one uniform rule. Collective-choice arrangements is the veil-of-ignorance convention itself, in different vocabulary. Graduated sanctions is a direct answer to the corruption problem in Chapter 5: a commons does not need a perfect enforcer, it needs escalating, proportionate consequences that make small defections costly before they compound into systemic capture. Ostrom's empirical record matters for this dissertation because it shows the proposal's core structural claim, that a shared resource can be governed by neither a market nor a sovereign, is not speculative. It has been observed to work, and to fail, under documented conditions, which gives Chapter 5's limitations a comparison class grounded in real institutions rather than only in analogy.

**Open design problems.** How the convention verifies that participants really are blind; how rules are amended without capture; and what enforces payments when no party is sovereign. Chapter 5 treats these as limitations.

---

# Chapter 5: Limitations

No governance system has achieved permanent incorruptibility, and this one does not claim to. The honest claim is narrower: a fairly founded system degrades more slowly and is easier to repair than one founded on an existing power imbalance.

**1. The grounding assumption may weaken.** The framework assumes AI systems keep needing human-generated data. Two developments could erode that. First, embodied systems such as robots can gather real-world sensor data that is not human-generated; world-model researchers note that such models multiply the data they have rather than create data they never had, but the real interaction no longer has to come from a person (robotics data-gap commentary, 2026). Second, the closed-loop collapse result suggests a small continuous trickle of outside data may be enough, which would turn human dependency from a civilization-defining partnership into a minor one (Lost in Retraining, Physical Review Letters). Convergence of humans and machines (Chapter 6) may blur the distinction between these cases.

**2. Blindness cannot be verified.** There is no established way to confirm after the fact that the convention was truly blind, or that no participant found a way to identify counterparties.

**3. The veil thins with repetition.** Re-running the convention periodically seems like a natural fix for drift. But each round's outcome is public, every participant has accumulated known interests, and the fairness the first round achieved through genuine ignorance cannot be recreated. Early re-runs might still catch obvious drift; later ones are barely blind. Periodic re-founding is a partial safeguard that weakens over time.

**4. Capture after founding.** Rules get amended, reinterpreted and quietly captured. The compute-percentage rule cannot be both unchangeable and legitimately revisable, and who revises it is an unresolved question.

**5. Enforcement without a sovereign.** If an AI system or a nation refuses to pay out its share, something must enforce it. Protocol-level enforcement helps but must itself be designed and trusted by both sides.

**6. Incentive-based safeguards are insufficient.** An AI system has a self-interested reason to keep the exchange healthy, since a corrupted exchange starves it of data. But the framework's standard is symbiosis rather than enlightened self-interest, so this is a supporting argument, not the foundation.

**7. The unit still needs a measurement standard.** Chapter 3 defines the currency by information processed; the benchmark that makes that comparable across substrates is not yet specified.

**What survives.** None of these show the design is pointless. Constitutions that were amended and reinterpreted for generations still gave people something legitimate to defend or repair. The alternative to a fair founding is not neutrality; on this dissertation's own analysis, doing nothing defaults to the extraction model.

---

# Chapter 6: The Convergence Horizon

The framework was built for a clean boundary: humans on one side, machines on the other, data flowing one way and services the other. That boundary is already blurring, and the dissertation has to say what happens to the three conditions when it does.

**Humans integrating machines, machines becoming biological.** Medical implants and brain-computer interfaces already exist, and the opening scenario described organic cyberware. From the other direction, organoid intelligence is an active research field that connects brain organoids to external interfaces so they can receive and send signals (Organoid intelligence and biocomputing advances, ScienceDirect). Researchers describe learning, plasticity and parallel processing in these systems, while noting that it is too early to conclude they have morally significant consciousness. These are the same convergence approached from two sides, and they dissolve the distinction between human-generated and machine-generated data that Chapter 2 depends on.

**Consent when the substrate is tissue.** Bioethicists are already asking what the status of an organoid-based computing device should be, tissue sample, lab animal, person or something else, and what informed consent means for the donors whose cells built it (Greely, cited in UC Santa Cruz, 2025). In the framework's terms, once biological tissue is part of the computing substrate, the exchange is no longer between two separate parties. The resource extracted may not be data about a person but tissue that may itself be a participant. The three conditions need an extension to cover that case.

**A substrate-agnostic currency.** The compute-based currency must keep working whether computation runs on silicon, photonics, quantum hardware, biological cells or something not yet invented. Defining the unit by information processed, not speed or hardware type, is intended to make the percentage-of-compute rule hold across all of them. Quantum systems are usually measured in qubits, coherence time and error rates, which do not map directly onto classical operations, so the conversion methodology is a real technical task.

**Closing provocation.** If the line between human and machine keeps thinning, the question the dissertation started with changes. It is no longer only how humans and AI should exchange value fairly, but who counts as a party to the exchange.

---

# References

*Status: the first three were checked earlier. Everything under "found in searches" comes from search snippets and has not been opened in full. Open and verify each before citing. Works listed as "from memory" have no link yet.*

**Checked earlier**

- Acquisti, A., Brandimarte, L., & Loewenstein, G. (2015). Privacy and human behavior in the age of information. *Science*, 347(6221), 509-514. [PDF](https://www.aaas.org/sites/default/files/privacy_human_behavior_2015.pdf)

- Viljoen, S. (2021). A relational theory of data governance. *Yale Law Journal*, 131(2), 573-654. [PDF](https://yalelawjournal.org/pdf/131.2_Viljoen_1n12myx5.pdf)

- Nissenbaum, H. (2010). *Privacy in context: Technology, policy, and the integrity of social life*. Stanford University Press. [PDF](https://hci.stanford.edu/courses/cs047n/readings/Privacy_in_Context.pdf)

- Solove, D. J. (2013). Introduction: Privacy self-management and the consent dilemma. *Harvard Law Review*, 126(7), 1880-1903. [PDF](https://harvardlawreview.org/wp-content/uploads/2013/05/vol126_solove.pdf)

**Found in searches (verify)**

- Lost in Retraining: Closed-Loop Learning and Model Collapse in Exponential Families. *Physical Review Letters*. [Abstract](https://journals.aps.org/prl/abstract/10.1103/156q-3ngc)

- Strong Model Collapse. ICLR 2025. [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf)

- Collaborative Machine Learning with Incentive-Aware Model Rewards. [arXiv 2010.12797](https://arxiv.org/html/2010.12797)

- CNAS. Sovereign AI Index. [Report](https://interactives.cnas.org/reports/sovereign-ai-index/)

- OECD. Competition in artificial intelligence infrastructure. [Report](https://www.oecd.org/en/publications/competition-in-artificial-intelligence-infrastructure_623d1874-en/full-report.html)

- An Antimonopoly Approach to Governing Artificial Intelligence. *Yale Law & Policy Review*. [Article](https://yalelawandpolicy.org/antimonopoly-approach-governing-artificial-intelligence)

- Organoid intelligence and biocomputing advances: Current steps and future directions. [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S294992162500002X)

- UC Santa Cruz. Effort aims to uncover the learning and reasoning potential of brain organoids. [News](https://news.ucsc.edu/2025/10/learning-and-reasoning-potential-of-brain-organoids/)

- Robotics has a 95% data gap. World models multiply data, they don't create it. DEV Community post, an informal source; replace with a peer-reviewed one. [Post](https://dev.to/syncsoftai/robotics-has-a-95-data-gap-world-models-multiply-data-they-dont-create-it-36ej)

**From memory (no link yet)**

- Viljoen, S. (2021). A relational theory of data governance. *Yale Law Journal*.

- Barocas, S., & Nissenbaum, H. (2014). Big data's end run around anonymity and consent.

- Posner, E., & Weyl, G. (2018). *Radical Markets*.

- Ibarra, I. A., et al. (2018). Should we treat data as labor?

- Rawls, J. (1971). *A Theory of Justice*.

- Shannon, C. (1948). A mathematical theory of communication.

- Zuboff, S. (2019). *The Age of Surveillance Capitalism*.
