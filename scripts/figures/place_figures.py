"""Place every figure in its chapter with an APA 7 caption, and write the List of Figures.

Run after build_figures.py:  python -I scripts/figures/place_figures.py
Idempotent: a chapter that already contains a figure's file name is left alone for that figure.

Caption form (APA 7): a bold "Figure N" line, an italic title in title case, the image, then a "Note." paragraph.
Each figure is cited by number in the paragraph that precedes it ("mention"), as APA requires.
"""
from __future__ import annotations

import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build_figures import NUMBERS, filename  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CH = os.path.join(ROOT, "chapters")

# (slug, chapter file, anchor, mode, mention sentence, title, alt text, note)
# mode "after": insert after the paragraph containing the anchor; "before": insert before the heading line equal to anchor.
PLACEMENTS = [
    ("one-architecture-two-terms", "01-introduction.md", "They do not differ in the character of the system:", "after",
     "Figure 1 shows the two scenarios as one architecture under two sets of terms.",
     "One Architecture, Two Sets of Terms",
     "Two panels of the same exchange between a person and a synthetic system; in the first the three conditions hold, in the second all three fail and the failures are linked.",
     "The flows are the same in both scenarios: data and attention from the person, services and care from the system. In the first scenario real exit, consent and reciprocal value hold; in the second all three fail, and the failures are not independent: the loss of exit entails the loss of consent, which removes the pressure that sustained reciprocity (Section 3.4)."),
    ("framework-architecture", "01-introduction.md", "not during it.", "after",
     "Figure 2 summarizes the architecture of the framework that the chapters build.",
     "The Architecture of the Framework: Conditions, Layers and Premises",
     "A layered diagram: the three conditions at the top, the economic and governance layers beneath them, and the two premises at the base.",
     "The three conditions of Chapter 3 are what the design secures; the economic layer (Chapter 4) builds the floor and prices the flows; the governance layer (Chapter 5) sets every parameter that allocates power. Both layers rest on the grounding assumption of Chapter 2 and on the enforcement presupposition stated at the head of Chapter 4. Chapters 6 to 8 concern how the arrangement could come into being, where it fails, and whom it covers."),
    ("disagreement-payoff-vs-exit-option", "03-formal-statement.md", "The non-tradable survival tier of Chapter 4 is designed to be such a payoff.", "after",
     "Figure 3 shows the difference in the bargaining set.",
     "A Disagreement Payoff Moves the Bargained Share; an Exit Option Only Bounds It",
     "Two bargaining-set diagrams with the human party's payoff on the horizontal axis and the synthetic party's on the vertical axis; raising the disagreement payoff moves the Nash solution, while an outside option changes it only when it binds.",
     "Both panels plot the feasible frontier on which the parties' payoffs sum to the joint value of agreement. Left: raising the human party's disagreement payoff from d to d′ moves the Nash solution along the frontier toward the human party (Nash, 1950). Right: an outside option changes the outcome only when it exceeds the bargained payoff, and then the human party receives exactly the option's value (Binmore et al., 1989); the counterparty can lower that value by raising switching costs, which it cannot do to a payoff received during impasse. The points are illustrative."),
    ("conditions-and-dependencies", "03-formal-statement.md", "and governance is needed for what neither can reach.", "after",
     "Figure 4 shows the nine clauses and the dependencies among them.",
     "The Three Conditions, Their Nine Clauses, and the Dependencies Among Them",
     "Three columns list the clauses of real exit, consent and reciprocal value; arrows mark the four entailments between clauses.",
     "An arrow runs from a clause whose failure entails the failure of the clause at its head. Solid arrows are unconditional (Proposition 1); dashed arrows hold under the stated condition. Exit is prior because its failures cannot be corrected from inside the exchange (Proposition 3); consent and reciprocity are not ordered with respect to each other."),
    ("dependence-and-divided-commons", "03-formal-statement.md", "the degree to which they can rely on the self-interest of synthetic parties to sustain them.", "after",
     "Figure 5 shows both halves of the proposition.",
     "Dependence Rises With Value and Falls With Availability; Divided Among Many Parties, It Loses Its Restraining Force",
     "Left, contours of dependence in the plane of motivational investment and availability of alternatives; right, the private share of a collective cost falling below the private benefit as the number of synthetic parties grows.",
     "Left: contours of D = v/λ, one admissible form of Emerson's (1962) dependence function; dependence is high where investment is high and alternatives are few. Right: the share γ/M of a collective cost γ borne by one of M synthetic parties, drawn with γ = 8 and b = 2; once M exceeds γ/b, degrading the population pays privately although it costs all of them together (Appendix A.5; Hardin, 1968). The parameters are illustrative."),
    ("floor-additive-and-substitution", "03-formal-statement.md", "when an alternative source of a valued good appears.", "after",
     "Figure 6 shows the two cases.",
     "What an Unconditional Floor Does to the Division of Surplus: The Additive and Substitution Cases",
     "Two bargaining-set diagrams: in the additive case the frontier and the disagreement point both shift by the value of the floor; in the substitution case the frontier shifts only by the provider's saved cost.",
     "Drawn with V = 10, d = (2, 2), Δ = 3 and c_s = 1 under a symmetric Nash split (Appendix A.3.1). Left: the floor raises the human party's disagreement payoff and the joint value by the same Δ, so the division is unchanged and the human party is better off by exactly Δ. Right: the floor replaces goods the provider supplied at cost c_s, the surplus shrinks by Δ − c_s, the human party gains between Δ/2 and Δ, and the provider's payoff falls by at most Δ/2. The working draft's claim of a Δ/2 gain in every bargain was the substitution case misread as general."),
    ("impatience-and-bargaining-weight", "03-formal-statement.md", "though it does depend on the survival constraint just stated.", "after",
     "Figure 7 plots the bargaining weight against the human party's discount rate.",
     "Impatience Below the Floor Drives the Human Party's Share of the Surplus Toward Zero",
     "A curve of the human party's bargaining weight, r_s over r_h plus r_s, falling toward zero as the human party's discount rate grows without bound.",
     "The weight α = r_s/(r_h + r_s) is the limit of the alternating-offers model with unequal discount rates (Binmore et al., 1986), drawn for a fixed r_s. The survival constraint that sends r_h to infinity for a party below its floor is a stated assumption (Appendix A.3.2); under it the party receives its disagreement payoff and none of the surplus. A floor keeps r_h finite and α positive."),
    ("informational-shadow", "03-formal-statement.md", "could ever satisfy the conditions in full.", "after",
     "Figure 8 shows the shadow of a single flow and the collective shadow of a population.",
     "The Informational Shadow of a Flow and the Level at Which Consent Must Be Given",
     "Left, a flow from one source casts a shadow over other parties; right, a population's collective shadow is the union of its members' shadows.",
     "Left: a flow from source i licenses inferences about a set of parties, its shadow Σ_i, which includes i and others who consented to nothing (Viljoen, 2021). Right: the collective shadow of a population is the union of its members' shadows, and Proposition 5 requires the three conditions at that level, above the materiality threshold the governance layer sets (Appendix A.6)."),
    ("scope-of-claims", "03-formal-statement.md", "a superintelligence could in principle have designed and stable ones.", "after",
     "Figure 9 shows the scope of each of the three theses.",
     "The Scope of the Theory's Claims: Where the Necessary Condition Holds and Where the Sufficiency Conjecture Is Offered",
     "Nested regions of synthetic parties: any party, parties with designed and stable objectives, and the designed-incentive regime that also has an accountable principal.",
     "For any synthetic party the theory claims only that clause E(i) is necessary, for a party that cannot leave, to a relation that is not one of domination. The sufficiency conjecture is offered only inside the designed-incentive regime, whose criterion is the provenance and stability of the objective together with an accountable principal, not capability. Parties outside it, and the tissue-based parties of Chapter 8 considered in their own right, receive only the necessary condition."),
    ("typology-of-regimes", "03-formal-statement.md", "and build governance for the failures that exit cannot reach.", "after",
     "Figure 10 shows the five prototypes as a clause-level matrix.",
     "Five Prototypes of Exchange Regime by Clause Pattern",
     "A matrix of five regimes against nine clauses, with filled, open and half-filled cells for clauses that hold, fail or fail conditionally.",
     "Filled cells mark clauses that hold, open cells clauses that fail, and half-filled cells clauses that fail often or where another clause fails; n/a marks a clause that cannot be assessed because R(ii) fails. The prototypes are points on a continuum rather than a partition, and the present data economy lies between the marketplace of the desperate and the company town (Section 3.9)."),
    ("capacity-unit-claim", "04-economic-layer.md", "and to the convention's ability to see credit extended off the ledger, which Chapter 7 records as a limitation.", "after",
     "Figure 11 shows the circuit from capacity to claims to redemption.",
     "Capacity, Unit and Claim: How the Compute Dividend Is Issued, Redeemed and Retired",
     "A flow diagram from measured capacity through issuance of claims to redemption with owners of capacity, with a demurrage loop that retires idle claims.",
     "Capacity is physical and perishable; the unit is the reference-workload measure of Section 4.3; a claim is a ledger balance. A share θ of measured capacity is credited equally to the N persons enrolled, claims are redeemed at par for the reference workload up to the obligated share of capacity, and a rationing rule governs redemption beyond it. Demurrage retires idle claims; the next period's dividend is computed from capacity, not from the stock of claims."),
    ("share-vs-fixed-quantity", "04-economic-layer.md", "the premise asserts this, and the design cannot ensure it.", "after",
     "Figure 12 contrasts the two rules under illustrative growth.",
     "A Fixed Quantity of Compute Loses Real Value as Compute Grows Abundant; a Share Tracks the Real Purchasing Power of All Compute",
     "Two curves over ten years: the real value of a fixed quantity of compute declining, and the real value of a fixed share of compute rising.",
     "Illustrative: capacity doubles every two years, the goods price of a unit of compute rises 20 percent a year, and population is constant. A fixed quantity's real value is proportional to 1/p and falls; a fixed share's real value is proportional to C/p and rises while capacity grows faster than its relative price falls (Appendix A.2). The two-year doubling is the order of magnitude Hobbhahn et al. (2023) report for price-performance; the price path is an assumption."),
    ("survival-share-binding-minimum", "04-economic-layer.md", "Chapter 5 returns to the governance of the floor standard, and Chapter 7 records it as a limitation.", "after",
     "Figure 13 plots the rule.",
     "The Survival Share Is a Percentage With a Binding Physical Minimum",
     "The survival share plotted against the per-person allocation: one where the allocation is below the floor, the floor's value divided by the allocation in between, and the ordinary share where the allocation is ample.",
     "σ(t) = min{1, max{σ₀, f̄(t)/a(t)}}, drawn with σ₀ = 0.3 and f̄ = 3 units (Appendix A.2). Where the whole allocation falls short of the floor the share is one and the floor cannot be met without raising θ; where the allocation is modest the minimum binds and the tier delivers exactly the floor; where it is ample the ordinary share applies and the remainder is discretionary."),
    ("demurrage-dynamics", "04-economic-layer.md", "rather than the history of who happened to accumulate first.", "after",
     "Figure 14 shows the two regimes.",
     "Idle Balances Compound Under Interest and Converge Under Demurrage",
     "Two panels: balances of two parties diverging without bound under a positive return, and converging to the same steady state under demurrage.",
     "Two parties with the same constant net inflow k and different starting balances, drawn with k = 1, r = 0.05 and δ = 0.1 per period (Appendix A.4). Under a positive return their balances grow without bound and diverge; under demurrage both converge to k/δ, the difference in endowments decaying with half-life ln 2/δ. The bound binds on idle balances only; capital and credit reopen compounding (Sections 4.6 and 4.8)."),
    ("information-gain-pricing", "04-economic-layer.md", "and so creates pressure against privacy.", "after",
     "Figure 15 shows the declining gain from similar data.",
     "Under Information-Gain Pricing the Price of Each Further Similar Datum Falls",
     "A bar chart of the information added by the n-th similar datum, falling with n, beside a bar for a novel datum at the first-observation gain.",
     "For a model estimating a parameter with a Gaussian prior and observation noise of unit variance, the n-th similar datum adds ½ ln(1 + 1/n) nats, the realized form of the expected-information criterion (Lindley, 1956). A datum about a parameter the model has not seen adds the first-observation gain again. The price follows novelty to the model, not status among people; the first qualification of Section 4.7 states what this computation presupposes."),
    ("channels-of-accumulation", "04-economic-layer.md", "ownership of productive capacity. Chapter 7 records this as a limitation.", "after",
     "Figure 16 shows the three channels and the instrument that acts on each.",
     "Three Channels of Accumulation and the Instrument That Acts on Each",
     "A diagram of discretionary income flowing into idle balances, loan claims and capacity, with the instrument beside each channel.",
     "Demurrage bounds idle balances; demurrage on loan claims lowers the lender's net return to r − δ without closing the channel; only a rule on capacity acts on the conversion of balances into compute-generating capacity, and the design leaves that rule to the convention. Without it, holders convert balances into capacity and the demurrage bound binds on nothing (Section 4.6)."),
    ("three-paths", "05-governance-layer.md", "That is as true when the dominant party is human as when it is synthetic.", "after",
     "Figure 17 shows the three paths of the Foreword as relations.",
     "Three Paths: Control in Either Direction Is One Relation With the Roles Exchanged; Synthesis Is a Different Relation",
     "Three small diagrams: people ruling systems, systems ruling people, and an exchange on fair terms between the two.",
     "In the first two paths one party rules and the other depends, and the relation is stable only while the ruler stays benevolent and strong; that they are one relation with the roles exchanged is a stipulation of Section 3.8. In the third, each party has a floor it cannot be forced to bargain away and can leave, and the terms are set behind a veil; the body argues that such an arrangement does not need goodwill in order to persist, subject to the enforcement presupposition of Chapter 4."),
    ("credentials-uniqueness-without-substrate", "05-governance-layer.md", "records it below as a third pre-veil decision.", "after",
     "Figure 18 shows the credential system and its two gaps.",
     "Credentials Attest Uniqueness Without Disclosing Substrate: The Issuer Partition and Its Two Gaps",
     "Three issuers, each certifying a disjoint population of persons, systems and hybrids, feed one credential each into a blinded pool that seats one participant per credential.",
     "Each issuer certifies a disjoint population and grants each principal one credential attesting that it is one bearer of obligations, without disclosing whether it is a person or a system (Adler et al., 2024; Douceur, 2002). The pool seats one participant per credential. Gap 1: a principal certified by two issuers holds two credentials unless the partition is kept disjoint, a pre-veil decision. Gap 2: an operator controlling several legal persons could hold several seats; the criterion resists copying models, not companies."),
    ("blind-convention", "05-governance-layer.md", "## 5.7 The symbiosis standard", "before",
     "Figure 19 shows what the veil conceals and what is decided before it descends.",
     "The Blind Convention: What Is Decided Before the Veil and What Lies Behind It",
     "Nested regions: four pre-veil decisions outside; weak blindness, under which counterparties' kind is concealed; strong blindness, under which one's own classification is concealed; and at the center the formulas the convention chooses.",
     "The four pre-veil decisions are visible and revisable. Weak blindness prevents coalitions and vote trading by substrate while each participant still knows its own kind; strong blindness has force in proportion to the share of participants who expect to be borderline, and none for present principals and owners of capacity (Section 5.5). The convention chooses general formulas rather than figures, aiming at Rawlsian impartiality by public-choice means (Brennan & Buchanan, 1985). Enforcement is presupposed (Chapter 4), and the symbiosis standard is a requirement the institutions must grow into (Section 5.7)."),
    ("ostrom-principles-mapped", "05-governance-layer.md", "(Cox et al., 2010, Table 3).", "after",
     "Figure 20 summarizes the mapping and the strength of each correspondence.",
     "Ostrom's Eight Design Principles Mapped Onto the Framework, With the Strength of Each Mapping",
     "A table of the eight principles against the framework element each maps onto, with a three-level indicator of how well the mapping holds.",
     "The indicator is this dissertation's judgment of the mapping as argued in Section 5.9: three filled marks where the element supports the principle, two where the correspondence is partial, one where it is weak. Boundaries are a constraint rather than a support, collective choice maps only partly onto the blind convention, monitoring rests on a trusted authority, and nested enterprises has the weakest evidence of the eight (Cox et al., 2010). Ostrom (1990, 2010) presented the principles as regularities of successful cases, not sufficient conditions."),
    ("convergent-remediation", "06-transition.md", "from question answering to code, as in Premise 2.", "after",
     "Figure 21 shows how convergent remediation turns many partly correlated exposures into one.",
     "Convergent Remediation: Many Organizations, Few Models, One Shared Exposure",
     "Before and after diagrams: eight organizations fixing a flaw independently with differing fixes, and the same eight routing their fixes through the same few models so that the fixes converge.",
     "Before: organizations fix the same class of flaw independently, their fixes differ, and a defect in one fix exposes one organization. After: the same few models propose and check the fixes for all of them, the fixes converge, and a shared defect is reproduced across all; the number of dependent systems is unchanged and only the diversity of their fixes falls. The premises and the workflow condition are those of Section 6.3."),
    ("strain-trigger-window", "06-transition.md", "already visible candidate for the trigger.", "after",
     "Figure 22 shows the layered model as a timeline.",
     "Slow Strain, a Discrete Trigger, and a Window That Opens Onto Two Branches",
     "A timeline on which slow strain accumulates toward a threshold, a trigger opens a policy window, and the window closes onto either a fair founding or an authoritarian consolidation.",
     "Three slow pressures, labor displacement, energy and physical resources, and strategic competition (Section 6.2), accumulate beneath a threshold (Pierson, 2004); a discrete trigger, the correlated-patch catastrophe, opens a policy window (Kingdon, 1984/2003). The window closes onto a fair founding only if a design was prepared in advance, and any design that distributes control would fit (Section 6.7); it can as easily close onto the authoritarian branch of Section 6.5. The trigger is a candidate, not a prediction."),
    ("convergence-two-sides", "08-convergence.md", "who is a party to the exchange at all.", "after",
     "Figure 23 places the chapter's cases on the two axes of convergence.",
     "Convergence From Two Sides: The Question Changes From How Parties Exchange to Who Counts as a Party",
     "Two axes, people incorporating machines and machines becoming biological, with the chapter's cases placed on each and the point where they meet marked as the question of who counts as a party.",
     "Along one axis people incorporate machines: records, implanted devices, and speech neuroprostheses with personal voice models (Card et al., 2024). Along the other, machines become biological: neuromorphic hardware, organoid reservoirs, and candidates for sentience. The conditions stay substrate-neutral; what convergence changes is their content and their sufficiency (Section 8.5), and exit from an implanted system must include ownership and portability of the personal models the exchange produces (Section 8.3)."),
]


def block(slug, title, alt, note):
    n = NUMBERS[slug]
    return (f"**Figure {n}**\n\n*{title}*\n\n![{alt}](../figures/{filename(slug)})\n\n*Note.* {note}\n")


def place():
    placed = 0
    for slug, chapter, anchor, mode, mention, title, alt, note in PLACEMENTS:
        path = os.path.join(CH, chapter)
        with open(path, "r", encoding="utf-8", newline="") as f:
            text = f.read()
        if filename(slug) in text:
            continue
        nl = "\r\n" if "\r\n" in text else "\n"
        paras = text.split(nl + nl)
        if mode == "after":
            hits = [i for i, p in enumerate(paras) if anchor in p]
            if len(hits) != 1:
                raise SystemExit(f"{chapter}: anchor for {slug} found {len(hits)} times: {anchor!r}")
            i = hits[0]
            paras[i] = paras[i].rstrip() + " " + mention
            paras.insert(i + 1, block(slug, title, alt, note).replace("\n", nl).rstrip())
        else:
            hits = [i for i, p in enumerate(paras) if p.strip() == anchor]
            if len(hits) != 1:
                raise SystemExit(f"{chapter}: heading for {slug} found {len(hits)} times: {anchor!r}")
            i = hits[0]
            paras[i - 1] = paras[i - 1].rstrip() + " " + mention
            paras.insert(i, block(slug, title, alt, note).replace("\n", nl).rstrip())
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write((nl + nl).join(paras))
        placed += 1
    return placed


def list_of_figures():
    path = os.path.join(CH, "00-front-matter.md")
    with open(path, "r", encoding="utf-8", newline="") as f:
        text = f.read()
    nl = "\r\n" if "\r\n" in text else "\n"
    entries = sorted(((NUMBERS[s], t) for s, _, _, _, _, t, _, _ in PLACEMENTS))
    body = nl.join(f"{n}. {t}" for n, t in entries)
    new = re.sub(r"(# List of Figures\s+).*?(?=(\r?\n# |\Z))", lambda m: m.group(1) + body + nl, text, count=1, flags=re.S)
    if new == text:
        raise SystemExit("List of Figures heading not found in 00-front-matter.md")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(new)


if __name__ == "__main__":
    n = place()
    list_of_figures()
    print(f"placed {n} figures; list of figures written")
