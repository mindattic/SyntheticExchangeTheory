# 03 — Transition problem: crisis-driven change, correlated software failure, automation and AI resource demand

Prepared for Chapter 1A ("The Transition Problem"). Research date: 2026-10-08.

Verification levels used:
- **Full text read**: the document itself was opened and the relevant passages were read.
- **Abstract/publisher page read**: the abstract, publisher page, or an official summary was read, not the full text.
- **Record located only**: a bibliographic record (DOI registry, publisher listing, or reliable secondary listing) confirms the work exists with these details. Content claims rest on that record or on secondary descriptions and still need checking against the text.

Process note: the session's shared web-search quota ran out partway through. After that, records were checked only by fetching known DOI registry entries (Crossref), publisher pages, or reference pages directly. Items marked "record located only" or "secondary" should be checked in a library before the defense.

---

## A. Sources cited in the draft (verified against the claims)

### Sajadi2025-SWEbenchSecurity
- APA: Sajadi, A., Damevski, K., & Chatterjee, P. (2025). *How safe are AI-generated patches? A large-scale study on security risks in LLM and agentic automated program repair on SWE-bench* (arXiv:2507.02976v3) [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2507.02976 (v1, June 2025, was titled "Are AI-generated fixes secure? Analyzing LLM and agent patches on SWE-bench")
- Link: https://arxiv.org/abs/2507.02976
- Verification: full text read (v3 HTML main body; v1 abstract read). It is a preprint, and no peer-reviewed venue is listed as of v3 (Dec 29, 2025).
- What it actually establishes: The study looks at patches for about 21,000 ordinary SWE-bench GitHub issues (bug reports and feature requests), not security fixes. It compares developer patches with patches from a standalone LLM (Llama 3.3 70B) and three agent frameworks (OpenHands, AutoCodeRover, HoneyComb). After static-analysis alerts, majority voting, and manual confirmation, Llama introduced 135 confirmed new vulnerabilities against 12 for developers. v3 calls this "nearly 11x"; the v1 abstract called it "nearly 9x more new vulnerabilities than developers". OpenHands, the agent with the most autonomy, produced far more vulnerabilities than ACR or HC (44 confirmed against 3 and 2). Risk rose with more files touched, more generated lines, and issue reports that lacked code snippets or reproduction steps. **The paper never counts vulnerabilities fixed, so it has no "introduced vs. fixed" ratio.**
- Use in dissertation: Cite it as evidence that LLM-written code changes bring in new vulnerabilities far more often than human changes, and that more agent autonomy raises the risk. Do not cite it as a study of security patching.

### Mierczuk2026-FLAWED
- APA: Mierczuk, A., Michaels, S., & Hoodlet, K. (2026). *Frontier models' vulnerability patches are often F.L.A.W.E.D.: Fix-like artifacts with embedded defects: Common failure modes of LLM-generated security patches* [White paper]. Off-by-1 Labs, 1Password. https://1password.com/files/resources/frontier-models-vulnerability-patches-flawed.pdf
- Link: PDF above. Harness: https://github.com/Off-by-1-Labs/FLAWED
- Verification: full text read (49-page PDF: abstract, design, limitations, discussion, and case studies read). **Industry white paper. It is not peer-reviewed in the scholarly sense**: the companion blog thanks named practitioners for informal review.
- What it actually establishes: The authors used GPT-5.5 and Claude Opus 4.8 to patch six high-impact, high-complexity CVEs (including "Copy Fail") in one-shot, validator-assisted, and exploratory modes, for 6,080 valid iterations. Results: 26.0% fully fixed the vulnerability with no side effects. 20.1% fixed it but changed behaviour. 2.3% fixed it but added a security issue. 49.3% left at least one exploit path open. 2.2% failed and also added a new exploit path. The authors conclude that the expected value of an unreviewed, fully LLM-generated patch is "net-negative." **Most relevant to Ch. 1A (§4.4):** on Copy Fail, both models independently reproduced the same off-by-one regression that kernel maintainers had once shipped, in 32% (GPT-5.5) and 31% (Claude) of non-cheat patches. Their own automated validator mostly missed it. The authors caution that convergence is not proof of shared origin, because the space of "obvious" fixes is narrow. Stated limitations: the CVEs chosen are harder than average, results depend on model versions, and grading relied mostly on LLM validators with at least 10% manual review. A Trail of Bits critique (seen only in secondary coverage) argues that the 26% figure mixes adversarial and degraded scenarios.
- Use in dissertation: This is the closest empirical support for "convergent remediation": different frontier models arrive at the same defective fix, and the same-class validator passes it. Label it as industry research and pair it with the peer-reviewed sources below.

### Hoodlet2026-FLAWEDblog (secondary to the above)
- APA: Hoodlet, K. (2026, August 6; updated 2026, September 16). *Why AI-generated vulnerability patches still require expert human review* [Blog post]. 1Password. https://1password.com/blog/why-ai-generated-patches-still-require-human-review
- Verification: full text read. It is a corporate blog.
- What it actually establishes: This is the launch post for the FLAWED paper. It gives the same headline figures, including 53.9% "FLAWED" (failed, introduced a vulnerability, or both), a $2.11–$2.81 cost per patch, and more than a third of "successful" patches being fragile input-specific guards. It also contains an internal inconsistency (6,080 vs. "6,480" patches). **SOCFortress is not mentioned here, and no search result linked SOCFortress to the study.**
- Use in dissertation: Do not cite it. Cite the white paper directly. The draft's attribution "Off-by-1 Labs, reported in SOCFortress, 2026" should be replaced (see Corrections).

### CSA2026-AIStackMonoculture
- APA: Cloud Security Alliance AI Safety Initiative. (2026, May 13). *AI stack monoculture: Systemic risk in the open-source ecosystem* [AI-assisted rapid research report]. CSAI Foundation. https://labs.cloudsecurityalliance.org/research/ai-developer-ecosystem-monoculture-risk-v1-csa-styled/
- Link: PDF at https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/05/ai-developer-ecosystem-monoculture-risk-v1-csa-styled.pdf
- Verification: full text read (PDF extracted).
- What it actually establishes: The PDF says it "was generated with AI assistance and has not undergone official CSA review." It argues that AI application development is concentrated on a few open-source packages (PyTorch, Transformers, LangChain, LiteLLM), cites supply-chain compromises such as LiteLLM and Axios, and includes a short "Model Monoculture as a Parallel Risk" section built on a non-peer-reviewed preprint. Its definition (identical OS and patch level means one exploit compromises all) is the textbook definition. The draft's sentence closely paraphrases this definition. Many of its references are news sites and blogs. It does not discuss LLM-generated patches as a correlated risk.
- Use in dissertation: Do not use it as the authority for the monoculture concept. At most, cite it as practitioner evidence that AI-stack concentration is a live concern in 2026, and flag it as unreviewed and AI-generated. Cite Geer et al. (2003), Stamp (2004), and Birman & Schneider (2009) for the concept.

### CSA2026-ClearinghouseRush (additional, found in passing)
- APA: Cloud Security Alliance AI Safety Initiative. (2026, July 11). *The clearinghouse rush: Concentration risk in AI patching* [Research note]. https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-vuln-clearinghouse-concentration-risk-2/
- Verification: abstract/publisher page read (web page). Grey literature.
- What it actually establishes: Frontier-model vulnerability discovery (Anthropic's Project Glasswing, OpenAI's Daybreak) is outrunning coordinated disclosure. Commercial "vulnerability clearinghouses" are emerging and could become single points of failure. The note addresses concentration among remediation intermediaries, not correlated defects in AI-written patches.
- Use in dissertation: Optional context showing that AI-driven patching at scale is already institutionalised in 2026, which supports the draft's "already standard practice" sentence better than the draft's current sources do. Grey literature.

---

## B. Software monoculture and correlated failure

### Geer2003-CyberInsecurity
- APA: Geer, D., Bace, R., Gutmann, P., Metzger, P., Pfleeger, C. P., Quarterman, J. S., & Schneier, B. (2003). *CyberInsecurity: The cost of monopoly—How the dominance of Microsoft's products poses a risk to security*. Computer & Communications Industry Association. https://ccianet.org/wp-content/uploads/2003/09/cyberinsecurity%20the%20cost%20of%20monopoly.pdf
- Link: also at https://www.schneier.com/essays/archives/2003/09/cyberinsecurity_the.html
- Verification: full text read (Schneier-hosted copy). It is a policy report commissioned and published by an industry association (CCIA), and is not peer-reviewed.
- What it actually establishes: Near-universal deployment of one operating system lets a single flaw be exploited across most machines at once, which explains the fast spread of worms like Slammer. Redundancy does not help, because "having more computers with the same vulnerabilities cannot help." The authors recommend diversification, including capping any single OS at 50% of the installed base in critical sectors and government.
- Use in dissertation: The canonical statement of the monoculture-as-correlated-risk argument. Use it in place of CSA (2026).

### Stamp2004-RisksMonoculture
- APA: Stamp, M. (2004). Risks of monoculture. *Communications of the ACM, 47*(3), 120. https://doi.org/10.1145/971617.971650
- Link: https://cacm.acm.org/opinion/risks-of-monoculture
- Verification: abstract/publisher page read (content seen through the ACM page and search extracts). It is a column ("Inside Risks"), not a research article.
- What it actually establishes: Uses the 2003 Blaster worm, which infected more than 1.4 million Windows systems in under a month, to argue that monocultures raise both vulnerability and the attacker's payoff. Diversity is a public good, so individual incentives favour monoculture: a "tragedy of the (security) commons."
- Use in dissertation: Shows why organizations converge on the same tools even when diversity would be safer for everyone. This applies directly to choosing the same LLM for remediation.

### Birman2009-MonocultureContext
- APA: Birman, K. P., & Schneider, F. B. (2009). The monoculture risk put into context. *IEEE Security & Privacy, 7*(1), 14–17. https://doi.org/10.1109/MSP.2009.24
- Link: https://www.cs.cornell.edu/fbs/publications/IEEEspMonoculture.pdf
- Verification: full text read (opening sections). DOI checked against Crossref.
- What it actually establishes: Argues that the "terror" of monoculture is overstated. A single, locked-down configuration defends better against configuration attacks, and monoculture combined with *automated diversity* (randomization) is a sensible defense against technology attacks. Attacks are split into configuration, technology, and trust attacks.
- Use in dissertation: The main counterargument. Standardization has real security benefits, so the correlated-patch scenario has to explain why LLM-mediated sameness lacks the "automated diversity" that rescues ordinary monoculture. **Venue correction: this is in IEEE Security & Privacy, not CACM.**

### Kleinberg2021-AlgorithmicMonoculture
- APA: Kleinberg, J., & Raghavan, M. (2021). Algorithmic monoculture and social welfare. *Proceedings of the National Academy of Sciences, 118*(22), e2018340118. https://doi.org/10.1073/pnas.2018340118
- Link: https://arxiv.org/abs/2101.05853
- Verification: abstract/publisher page read (arXiv abstract plus Crossref record).
- What it actually establishes: A formal model in which several decision-makers adopt the same algorithm. Overall decision quality can fall even when that algorithm is more accurate than each decision-maker's alternative, and "unexpected shocks are therefore not needed" to expose monoculture risk.
- Use in dissertation: A formal basis for the claim that shared tools can be individually rational and collectively harmful, even in normal times.

### Bommasani2021-FoundationModels
- APA: Bommasani, R., Hudson, D. A., Adeli, E., et al. (2021). *On the opportunities and risks of foundation models* (arXiv:2108.07258) [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2108.07258
- Link: https://arxiv.org/abs/2108.07258
- Verification: abstract/publisher page read. Technical report with 114 authors, never peer-reviewed as a whole.
- What it actually establishes: Introduces "homogenization." Building many systems on a few foundation models gives leverage, but "defects of the foundation model are inherited by all the adapted models downstream."
- Use in dissertation: The basic statement that one model's flaw becomes everyone's flaw. This is the mechanism behind convergent remediation.

### Bommasani2022-PickingSamePerson
- APA: Bommasani, R., Creel, K. A., Kumar, A., Jurafsky, D., & Liang, P. (2022). Picking on the same person: Does algorithmic monoculture lead to outcome homogenization? In *Advances in Neural Information Processing Systems 35* (NeurIPS 2022). https://proceedings.neurips.cc/paper_files/paper/2022/hash/17a234c91f746d9625a75cf8a8731ee2-Abstract.html
- Verification: abstract/publisher page read. Page numbers not confirmed. arXiv:2211.13972.
- What it actually establishes: Defines outcome homogenization and the "component-sharing hypothesis." More data sharing reliably increased homogenization on fairness benchmarks. **For foundation models, results were mixed:** the adaptation method strongly affected how much homogenization occurred.
- Use in dissertation: Empirical support with an important caveat. Sharing a base model does not automatically produce identical failures, because fine-tuning and prompting choices matter. The correlated-patch scenario should not assume identical outputs.

### Kim2025-CorrelatedErrors
- APA: Kim, E. M., Garg, A., Peng, K., & Garg, N. (2025). Correlated errors in large language models. In *Proceedings of the 42nd International Conference on Machine Learning* (PMLR Vol. 267, pp. 30038–30066). https://proceedings.mlr.press/v267/kim25e.html
- Verification: abstract/publisher page read.
- What it actually establishes: Covers more than 350 LLMs. On one leaderboard dataset, "models agree 60% of the time when both models err." Larger and more accurate models have highly correlated errors even across different architectures and providers. The authors connect this to algorithmic monoculture in hiring and in LLM-as-judge evaluation.
- Use in dissertation: **The strongest peer-reviewed evidence for the correlation premise.** It also undercuts "re-scan with the same class of tool," because an LLM judge tends to share the patching model's blind spots. It also suggests that switching vendors may not provide real diversity.

### Hedden2026-MonocultureCritics
- APA: Hedden, B., & Raghavan, M. (2026). *Algorithmic monoculture and its critics* (arXiv:2604.06047v3) [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2604.06047
- Verification: abstract/publisher page read. Preprint.
- What it actually establishes: Reviews objections to algorithmic monoculture (systemic exclusion, agency and gaming, information aggregation) and concludes that monoculture is "less problematic than its critics have supposed." No objection is decisive in general.
- Use in dissertation: A counterargument to address directly. Its framing is decision-making in hiring and lending, so the dissertation should argue that adversarial software security is a domain where correlation is more dangerous.

### Pearce2022-Asleep
- APA: Pearce, H., Ahmad, B., Tan, B., Dolan-Gavitt, B., & Karri, R. (2022). Asleep at the keyboard? Assessing the security of GitHub Copilot's code contributions. In *2022 IEEE Symposium on Security and Privacy (SP)* (pp. 754–768). IEEE. https://doi.org/10.1109/SP46214.2022.9833571
- Link: https://arxiv.org/abs/2108.09293 (later version in *Communications of the ACM, 68*(2), 96–105, 2025, https://doi.org/10.1145/3610721)
- Verification: abstract/publisher page read. Crossref record confirmed.
- What it actually establishes: Across 89 CWE-oriented scenarios and 1,689 Copilot-generated programs, about 40% were vulnerable.
- Use in dissertation: Baseline evidence that LLM-suggested code is often insecure.

### Perry2023-InsecureCode
- APA: Perry, N., Srivastava, M., Kumar, D., & Boneh, D. (2023). Do users write more insecure code with AI assistants? In *Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security* (CCS '23). ACM. https://doi.org/10.1145/3576915.3623157
- Link: https://arxiv.org/abs/2211.03622
- Verification: full text read (arXiv v3).
- What it actually establishes: A user study with 47 analysed participants (33 with a codex-davinci-002 assistant, 14 controls). Assistant users wrote less secure code on four of five tasks. For example, 36% wrote SQL-injectable code against 7% of controls, and 3% wrote secure ECDSA signing against 21% of controls. They were also *more* confident that their code was secure.
- Use in dissertation: Supports the human side of the scenario: AI help reduces scrutiny exactly when verification matters. The sample is small, so use it as supporting evidence only.

### Pearce2023-ZeroShotRepair
- APA: Pearce, H., Tan, B., Ahmad, B., Karri, R., & Dolan-Gavitt, B. (2023). Examining zero-shot vulnerability repair with large language models. In *2023 IEEE Symposium on Security and Privacy (SP)* (pp. 2339–2356). IEEE. https://doi.org/10.1109/SP46215.2023.10179324
- Link: https://arxiv.org/abs/2112.02125
- Verification: abstract/publisher page read.
- What it actually establishes: Testing five commercial models, one open model, and one locally trained model, LLMs collectively repaired 100% of synthetic and hand-crafted vulnerable scenarios. Historical real-world cases, however, revealed problems with producing functionally correct fixes.
- Use in dissertation: A balancing source. LLMs can fix simple, well-specified bugs, and the risk lies in real, complex cases.

### Wu2023-NeuralVulnRepair
- APA: Wu, Y., Jiang, N., Pham, H. V., Lutellier, T., Davis, J., Tan, L., Babkin, P., & Shah, S. (2023). How effective are neural networks for fixing security vulnerabilities. In *Proceedings of the 32nd ACM SIGSOFT International Symposium on Software Testing and Analysis* (ISSTA '23) (pp. 1282–1294). ACM. https://doi.org/10.1145/3597926.3598135
- Link: https://arxiv.org/abs/2305.18607
- Verification: abstract/publisher page read (abstract plus conference page via search summary). Crossref confirmed.
- What it actually establishes: On Java vulnerability benchmarks (Vul4J and the new VJBench), the best model, Codex, fixed only about 20% (10.2 of 50) of vulnerabilities, and many patches did not compile. Some CWE categories were consistently missed by all models.
- Use in dissertation: Peer-reviewed evidence that LLM vulnerability repair has low success rates, and that failures cluster by vulnerability type across models (correlated blind spots).

### Smith2015-Overfitting
- APA: Smith, E. K., Barr, E. T., Le Goues, C., & Brun, Y. (2015). Is the cure worse than the disease? Overfitting in automated program repair. In *Proceedings of the 2015 10th Joint Meeting on Foundations of Software Engineering* (ESEC/FSE 2015) (pp. 532–543). ACM. https://doi.org/10.1145/2786805.2786825
- Verification: record located only (Crossref plus abstract in search summary). It received a 2025 FSE Test-of-Time honorable mention.
- What it actually establishes: Automated repair tools (GenProg, TrpAutoRepair) produce patches that pass the test suite used to make them but break untested intended behaviour ("overfitting"). Judging patches with the same tests used to create them cannot tell correct patches from plausible ones.
- Use in dissertation: **The peer-reviewed predecessor of FLAWED.** "Fix-shaped but wrong" patches are a known automated-repair failure going back a decade. The validation loop the draft describes (generate, then re-check with the same class of tool) repeats the evaluation flaw Smith et al. identified.

### Vero2025-BaxBench
- APA: Vero, M., Mündler, N., Chibotaru, V., Raychev, V., Baader, M., Jovanović, N., He, J., & Vechev, M. (2025). BaxBench: Can LLMs generate correct and secure backends? In *Proceedings of the 42nd International Conference on Machine Learning* (PMLR Vol. 267, pp. 61344–61390). https://mlanthology.org/icml/2025/vero2025icml-baxbench
- Link: https://arxiv.org/abs/2502.11844
- Verification: abstract/publisher page read.
- What it actually establishes: On 392 backend-generation tasks, the best model (OpenAI o1) reached only 62% functional correctness. On average, the authors could exploit about half of each model's *correct* programs.
- Use in dissertation: Recent peer-reviewed evidence that functionally correct LLM code is often exploitable, which supports the gap between "passes tests" and "is secure."

### CrowdStrike2024-RCA
- APA: CrowdStrike. (2024, August 6). *External technical root cause analysis—Channel File 291* [Incident report]. https://crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf (executive summary: https://crowdstrike.com/wp-content/uploads/2024/08/Executive-Summary_Root-Cause-Analysis_Channel-File-291.pdf)
- Verification: full text read for the 2-page executive summary. Record located only for the 12-page full RCA. Vendor self-report.
- What it actually establishes: On July 19, 2024, a Rapid Response Content update to the Falcon Windows sensor supplied 21 input fields where the sensor expected 20. The resulting out-of-bounds read crashed hosts. The fixes include staged deployment rings, extra Content Validator checks, bounds checking, customer control over content rollout, and two independent third-party code reviews. In other words, the remedy was to restore independent, staged verification.
- Use in dissertation: The best real-world analogue. One unverified update, pushed simultaneously to a large installed base, produced a correlated global failure. Be precise: this was a vendor-pushed configuration update, not many organizations independently applying the same AI-written patch.

### Weston2024-MicrosoftCrowdStrike
- APA: Weston, D. (2024, July 20). *Helping our customers through the CrowdStrike outage* [Blog post]. Microsoft. https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/
- Verification: full text read (short post). Corporate blog, but the primary source for the count.
- What it actually establishes: Estimates that about 8.5 million Windows devices were affected, "less than one percent of all Windows machines." It also notes that the impact was large because affected enterprises run critical services.
- Use in dissertation: The authoritative scale figure. It also shows that concentration in *critical* nodes matters more than overall market share.

### FCA2024-CrowdStrikeLessons
- APA: Financial Conduct Authority. (2024, October 31). *CrowdStrike outage: Lessons for operational resilience*. https://www.fca.org.uk/firms/operational-resilience/crowdstrike-outage-lessons-operational-resilience
- Verification: full text read (web page). Regulator publication, not peer-reviewed.
- What it actually establishes: Impact on UK regulated firms varied and consumer harm was minimal. The FCA highlights dependence on unregulated third parties, single points of failure (suggesting different builds or operating systems), testing updates before deployment, and phased rollouts.
- Use in dissertation: An independent, authoritative post-incident assessment. The "minimal consumer harm" finding also supports the counterargument that correlated IT failures are often recoverable shocks, not regime-changing crises. Note: no peer-reviewed journal analysis of the CrowdStrike outage was found before the search quota ran out. That gap should be searched again (e.g., *Journal of Cybersecurity*, *Risk Analysis*).

### Przymus2025-XZ
- APA: Przymus, P., & Durieux, T. (2025). Wolves in the repository: A software engineering analysis of the XZ Utils supply chain attack. In *Proceedings of the 22nd International Conference on Mining Software Repositories* (MSR 2025). https://doi.org/10.48550/arXiv.2504.17473
- Link: https://arxiv.org/abs/2504.17473 ; program listing: https://2025.msrconf.org/details/msr-2025-technical-papers/30/
- Verification: abstract/publisher page read. Acceptance confirmed through the MSR 2025 program. The IEEE proceedings DOI was not confirmed, so cite the arXiv DOI until it is.
- What it actually establishes: Reconstructs the XZ Utils backdoor (CVE-2024-3094) from GitHub events. Attackers built legitimacy over years with seemingly helpful contributions to infrastructure, maintenance, and CI, and parts of the backdoor existed only in release tarballs. Software engineering practices themselves became the attack vector.
- Use in dissertation: Shows how one compromised dependency nearly spread into major Linux distributions, and that trust in the process (not the code) is the vulnerable layer. It is a close analogue for trusting an AI remediation pipeline.

### Perrow1999-NormalAccidents
- APA: Perrow, C. (1999). *Normal accidents: Living with high-risk technologies* (Updated ed.). Princeton University Press. https://doi.org/10.1515/9781400828494 (Original work published 1984)
- Link: https://press.princeton.edu/books/paperback/9780691004129/normal-accidents
- Verification: abstract/publisher page read. The publisher page gives Oct 17, 1999 with copyright 2000, and Crossref gives 2000 as the print date. Use 1999 with "Updated ed."; the original 1984 publisher, Basic Books, was not confirmed online.
- What it actually establishes: In systems with interactive complexity and tight coupling, accidents are "normal": inevitable outcomes of system structure. Adding safety devices can increase complexity and create new failure modes.
- Use in dissertation: The theory behind why an automated patch-and-verify loop (tightly coupled, opaque) is accident-prone. It also explains why adding another AI scanner may not add safety.

### Cook1998-ComplexSystemsFail
- APA: Cook, R. I. (1998). *How complex systems fail* [Unpublished technical report]. Cognitive Technologies Laboratory, University of Chicago.
- Link: https://worrydream.com/booklets/Cook_1998_-_How_Complex_Systems_Fail_(booklet).pdf (unofficial reproduction)
- Verification: record located only. Multiple consistent reproductions exist, and it was never journal-published.
- What it actually establishes: Eighteen short propositions. Catastrophe requires several small failures to combine, complex systems always run in degraded mode, and hindsight bias distorts post-accident analysis.
- Use in dissertation: Supports the "slack removal" framing. Strain does not cause failure directly but erodes the defenses that keep latent faults from combining. Cite it as grey literature.

### Taleb2012-Antifragile
- APA: Taleb, N. N. (2012). *Antifragile: Things that gain from disorder*. Random House.
- Link: https://www.penguinrandomhouse.com/books/176227/antifragile-by-nassim-nicholas-taleb/
- Verification: record located only (publisher page: hardcover Nov 27, 2012).
- What it actually establishes: A popular argument that systems optimised for efficiency become fragile to rare large shocks, and that redundancy is a hedge. It is not peer-reviewed.
- Use in dissertation: Optional rhetorical support only. Perrow and Cook carry the scholarly weight.

---

## C. Crisis and institutional change

### Polanyi1944-GreatTransformation
- APA: Polanyi, K. (2001). *The great transformation: The political and economic origins of our time* (2nd ed.). Beacon Press. (Original work published 1944 by Farrar & Rinehart)
- Verification: record located only (secondary reference listing: 1944 Farrar & Rinehart; Beacon 2001 edition with foreword by Stiglitz and introduction by Block).
- What it actually establishes: Market society treats land, labour, and money as "fictitious commodities." Their unregulated commodification provokes a protective "double movement," and the collapse of the 19th-century liberal order led to the institutional reconstruction of the 1930s and 1940s.
- Use in dissertation: The classic account of how the strain of market dislocation, combined with the failure of the old order, produces new institutions. It is a close parallel to the slow-strain-plus-trigger argument.

### Kingdon-PolicyWindows
- APA: Kingdon, J. W. (2003). *Agendas, alternatives, and public policies* (2nd ed.). Longman/Pearson. (Original work published 1984 by Little, Brown)
- Verification: record located only (secondary listing gives the 2nd ed., Pearson 2003). The original 1984 Little, Brown edition was not confirmed online; check the colophon.
- What it actually establishes: Policy change happens when the separate problem, policy, and politics streams come together during a brief "policy window." Focusing events can open windows, but only solutions already developed get adopted.
- Use in dissertation: Important refinement. A crisis opens a window but does not supply the design. This justifies building the Ch. 3–4 framework *before* the crisis, which is Friedman's "ideas lying around" point in political-science form.

### Capoccia2007-CriticalJunctures
- APA: Capoccia, G., & Kelemen, R. D. (2007). The study of critical junctures: Theory, narrative, and counterfactuals in historical institutionalism. *World Politics, 59*(3), 341–369. https://doi.org/10.1017/S0043887100020852
- Verification: abstract/publisher page read (Crossref abstract).
- What it actually establishes: Critical junctures are relatively short periods in which structural constraints loosen and agents' choices set path-dependent trajectories. "Contingency is the key characteristic of critical junctures." Analysing them requires counterfactual and narrative methods.
- Use in dissertation: The formal concept for the moment the chapter describes. It also stresses that outcomes are contingent, so a crisis need not produce *fair* institutions.

### Pierson2004-PoliticsInTime
- APA: Pierson, P. (2004). *Politics in time: History, institutions, and social analysis*. Princeton University Press. https://doi.org/10.1515/9781400841080
- Verification: record located only (Crossref).
- What it actually establishes: Explains path dependence and increasing returns. Institutions persist because of self-reinforcing dynamics, and slow-moving causes can build up beneath thresholds before producing rapid change.
- Use in dissertation: Supports "slow strain removes slack" with Pierson's concepts of slow-moving causal processes and threshold effects.

### Olson1982-RiseDecline
- APA: Olson, M. (1982). *The rise and decline of nations: Economic growth, stagflation, and social rigidities*. Yale University Press.
- Verification: record located only (secondary). The publisher page could not be fetched.
- What it actually establishes: Over time, stable societies accumulate distributional coalitions that lobby for narrow benefits and slow growth. Olson argues that upheavals which destroy these coalitions (e.g., in postwar Germany and Japan) can clear the way for growth. The second claim was not confirmed in what was read; check against the text.
- Use in dissertation: The interest-group explanation for why working-but-unfair orders resist voluntary reform, and why disruption can reset them.

### Higgs1987-CrisisLeviathan
- APA: Higgs, R. (1987). *Crisis and Leviathan: Critical episodes in the growth of American government*. Oxford University Press.
- Verification: record located only (secondary). The publisher was not confirmed online; check it.
- What it actually establishes: The "ratchet" hypothesis. US government growth from the 1880s to the 1980s came in spurts after real or perceived crises (wars, depressions), and post-crisis rollback was only partial.
- Use in dissertation: Evidence that crises drive lasting institutional change. Also a warning, from a libertarian author, that crisis-born institutions are not necessarily better ones.

### Scheidel2017-GreatLeveler
- APA: Scheidel, W. (2017). *The great leveler: Violence and the history of inequality from the Stone Age to the twenty-first century*. Princeton University Press. https://doi.org/10.1515/9781400884605
- Verification: record located only (Crossref). The thesis summary rests on a secondary source. The "four horsemen" (mass-mobilization war, transformative revolution, state failure, pandemic) should be confirmed in the text.
- What it actually establishes: Historically, large reductions in inequality have come mainly from violent shocks, not peaceful reform.
- Use in dissertation: Strong, sobering support for "fair institutions follow failure." It also implies that the cost of the trigger may be very high, which the chapter should acknowledge.

### Streeck2005-BeyondContinuity
- APA: Streeck, W., & Thelen, K. (Eds.). (2005). *Beyond continuity: Institutional change in advanced political economies*. Oxford University Press. (Introduction, pp. 1–39; typology at pp. 19–31)
- Verification: record located only (secondary citation with ISBN 978-0-19-928046-9).
- What it actually establishes: Significant institutional transformation often happens *gradually and without crisis* through displacement, layering, drift, conversion, and exhaustion.
- Use in dissertation: **The essential counterargument.** The chapter's claim that institutions are adopted "only after the prior order failed" is too strong. Gradual paths such as layering new data-rights institutions onto existing law are well documented. Reframe accordingly (see Corrections).

### Steil2013-BrettonWoods
- APA: Steil, B. (2013). *The battle of Bretton Woods: John Maynard Keynes, Harry Dexter White, and the making of a new world order*. Princeton University Press.
- Link: https://press.princeton.edu/books/hardcover/9780691149097/the-battle-of-bretton-woods
- Verification: abstract/publisher page read (hardcover Feb 24, 2013). The subtitle is from the book's standard listing and was not displayed on the fetched page; confirm it.
- What it actually establishes: Bretton Woods (1944) was shaped as much by US Treasury efforts to displace Britain as by shared lessons from depression and war. Its design was negotiated under wartime conditions and reflected US power.
- Use in dissertation: Supports "two world wars preceded Bretton Woods," but adds nuance. Crisis-born institutions reflect the power balance of the moment, not only fairness. (Eichengreen's *Globalizing Capital* was not verified this session.)

### Friedman1982-OnlyACrisis
- APA: Friedman, M. (1982). Preface. In *Capitalism and freedom* (pp. vii–ix). University of Chicago Press. (Original work published 1962)
- Verification: record located only (secondary quotation source giving "Preface (1982 edition), p. ix"). The primary text was not opened. Page numbering differs in the 2002 40th-anniversary edition.
- What it actually establishes: The quote is "Only a crisis—actual or perceived—produces real change." The next sentence (paraphrased) says that what happens then depends on ideas already available.
- Use in dissertation: The quote fits Ch. 1A well, but cite it as the 1982 preface to a 1962 book, and use the second sentence. It supports preparing institutional designs in advance.

---

## D. Automation displacement

### Acemoglu2020-RobotsJobs
- APA: Acemoglu, D., & Restrepo, P. (2020). Robots and jobs: Evidence from US labor markets. *Journal of Political Economy, 128*(6), 2188–2244. https://doi.org/10.1086/705716
- Verification: abstract/publisher page read (NBER abstract plus Crossref).
- What it actually establishes: One more robot per thousand workers reduces the employment-to-population ratio by about 0.18–0.34 percentage points and wages by 0.25–0.5% in affected US commuting zones (1990–2007).
- Use in dissertation: Causal evidence that automation can displace workers locally.

### Eloundou2024-GPTsAreGPTs
- APA: Eloundou, T., Manning, S., Mishkin, P., & Rock, D. (2024). GPTs are GPTs: Labor market impact potential of LLMs. *Science, 384*(6702), 1306–1308. https://doi.org/10.1126/science.adj0998
- Verification: abstract/publisher page read (arXiv 2303.10130 abstract plus Crossref).
- What it actually establishes: About 80% of US workers have at least 10% of tasks *exposed* to LLMs, and about 19% have at least 50% exposed. Including LLM-powered software raises the share of tasks completable faster from about 15% to 47–56%.
- Use in dissertation: Measures exposure, not displacement. Do not present it as job-loss evidence.

### Brynjolfsson2025-GenAIatWork
- APA: Brynjolfsson, E., Li, D., & Raymond, L. (2025). Generative AI at work. *The Quarterly Journal of Economics, 140*(2), 889–942. https://doi.org/10.1093/qje/qjae044
- Verification: abstract/publisher page read.
- What it actually establishes: Among 5,172 customer-support agents, an AI assistant raised productivity (issues resolved per hour) by about 15% on average. Gains were largest for novice and low-skill workers, with small quality declines for the most experienced.
- Use in dissertation: Counterweight. In this setting AI complemented workers rather than displacing them.

### Autor2015-StillJobs
- APA: Autor, D. H. (2015). Why are there still so many jobs? The history and future of workplace automation. *Journal of Economic Perspectives, 29*(3), 3–30. https://doi.org/10.1257/jep.29.3.3
- Verification: abstract/publisher page read.
- What it actually establishes: Automation substitutes for some tasks but complements others and raises demand. Commentators tend to overstate displacement. Labor-market polarization is the main observed effect.
- Use in dissertation: The standard skeptical position. The "slow strain" premise should engage it rather than assume mass unemployment.

### Brynjolfsson2025-Canaries
- APA: Brynjolfsson, E., Chandar, B., & Chen, R. (2025). *Canaries in the coal mine? Six facts about the recent employment effects of artificial intelligence* [Working paper; revised August 12, 2026]. Stanford Digital Economy Lab. https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/
- Verification: abstract/publisher page read (revised-version page). Not peer-reviewed.
- What it actually establishes: ADP payroll data through June 2026 show no economy-wide displacement. However, employment of workers aged 22–25 in AI-exposed occupations is 19% below the trend of less-exposed peers (August 2026 revision), and the gap has widened since first documented in August 2025. The adjustment comes through reduced hiring, not layoffs, and is concentrated where AI substitutes for tasks. The authors describe it as descriptive, not causal, and the effect weakens when controlling for education. The ~13% figure often quoted for the 2025 version was not verified here.
- Use in dissertation: The best current evidence that strain is emerging at the entry level, with honest caveats.

---

## E. AI resource demand

### IEA2025-EnergyAI
- APA: International Energy Agency. (2025). *Energy and AI*. IEA. https://www.iea.org/reports/energy-and-ai
- Verification: abstract/publisher page read (executive summary).
- What it actually establishes: Data centres used about 415 TWh in 2024 (about 1.5% of global electricity), up about 12% per year since 2017. Use is projected to reach about 945 TWh by 2030 in the base case. The US accounts for the largest share of growth, and data centres account for nearly half of US electricity-demand growth to 2030.
- Use in dissertation: The authoritative global figure for power competition.

### Shehabi2024-LBNL
- APA: Shehabi, A., Smith, S. J., Hubbard, A., Newkirk, A., Lei, N., Siddik, M. A. B., Holecek, B., Koomey, J., Masanet, E., & Sartor, D. (2024). *2024 United States data center energy usage report* (LBNL-2001637). Lawrence Berkeley National Laboratory. https://doi.org/10.71468/P1WC7Q
- Link: https://escholarship.org/uc/item/32d6m0d1
- Verification: full text read (executive summary pages of the PDF).
- What it actually establishes: US data centres used about 176 TWh in 2023 (4.4% of US electricity), up from about 60 TWh in 2014–2016. Use is projected at roughly 325–580 TWh in 2028 (6.7–12.0% of US electricity; 74–132 GW at 50% utilization), driven by GPU-accelerated servers.
- Use in dissertation: The authoritative US figure.

### Li2025-Thirsty
- APA: Li, P., Yang, J., Islam, M. A., & Ren, S. (2025). Making AI less "thirsty." *Communications of the ACM, 68*(7), 54–61. https://doi.org/10.1145/3724499
- Link: https://arxiv.org/abs/2304.03271
- Verification: abstract/publisher page read (arXiv abstract plus Crossref record).
- What it actually establishes: Training GPT-3 in Microsoft's US data centres could directly evaporate about 700,000 litres of freshwater. Global AI demand is projected to account for 4.2–6.6 billion m³ of water withdrawal in 2027, more than the annual withdrawal of 4–6 Denmarks or half of the UK.
- Use in dissertation: The water-competition premise. These are model-based estimates with wide uncertainty, so say so.

### deVries2023-Joule
- APA: de Vries, A. (2023). The growing energy footprint of artificial intelligence. *Joule, 7*(10), 2191–2194. https://doi.org/10.1016/j.joule.2023.09.004
- Verification: record located only (Crossref). The publisher page returned 403, so specific figures were not checked.
- What it actually establishes: A short commentary with supply-chain-based scenarios for AI electricity use. Its numeric projections should be checked in the text before quoting.
- Use in dissertation: An early warning source. Prefer IEA (2025) and LBNL (2024) for the numbers.

---

## Corrections to the draft

1. **"Nearly nine times more new vulnerabilities than they fixed" is wrong.** Sajadi et al. compare vulnerabilities *introduced by Llama 3.3* with those *introduced by human developers* (v1: "nearly 9x"; v3: "nearly 11x," 135 vs. 12). They never measure vulnerabilities fixed. The study also covers general SWE-bench issue resolution, not security patching. Suggested wording: "a large-scale study of AI-generated fixes for some 20,000 GitHub issues found that a standalone LLM introduced roughly nine to eleven times as many new vulnerabilities as human developers did on the same issues (Sajadi et al., 2025, preprint)." Give the full title, not "SWE-bench security study."
2. **FLAWED attribution.** The source is a white paper by Mierczuk, Michaels & Hoodlet (2026), Off-by-1 Labs/1Password. No link to SOCFortress was found. Cite the paper, label it industry research, and pair it with Smith et al. (2015) and Wu et al. (2023). The paper itself supports the draft better than the paraphrase: about half of patches left an exploit path open, and both models converged on the *same* off-by-one in about 31–32% of Copy Fail patches.
3. **CSA "AI Stack Monoculture" is AI-generated and unreviewed** by CSA's own statement. Its monoculture definition is the textbook one, which the draft repeats. Cite Geer et al. (2003) and Stamp (2004) for the concept. Mention CSA only as 2026 practitioner concern, if at all.
4. **"This is not a hypothetical workflow; it is already standard practice at a growing number of organizations."** None of the three cited sources documents prevalence of the full no-independent-testing loop. FLAWED and CSA (2026b) show that AI patching at scale (Glasswing, Daybreak, "Patch the Planet") is real, but not that orgs ship without testing. Soften to "is increasingly feasible and is being promoted at scale," or find survey evidence.
5. **"Fair institutions are adopted only after the prior order failed"** is too strong given Streeck & Thelen (2005) and Kingdon. Prefer "large-scale redesigns have usually followed..." and acknowledge gradual paths.
6. **Bretton Woods / New Deal**: fine as illustrations. Note that Steil (2013) shows the design reflected US power as well as lessons from crisis.
7. Birman & Schneider (2009) is in *IEEE Security & Privacy*, not CACM (if the reference list says CACM).
8. Friedman quote: cite as the 1982 preface to *Capitalism and Freedom* (orig. 1962), p. ix, and check the edition.

## Synthesis notes

**Stating the transition argument rigorously.** The defensible claim is conditional and probabilistic, not a historical law. The critical-junctures literature (Capoccia & Kelemen, 2007) and Kingdon's policy windows give a precise vocabulary. Structural constraints normally keep institutions on their path (Pierson, 2004; Olson, 1982). Some shocks loosen those constraints for a short time. What gets adopted in that window depends on which designs are already worked out and on the balance of power at the time (Friedman's "ideas lying around"; Steil, 2013). Polanyi, Higgs, and Scheidel supply the historical pattern: large redistributive or regulatory reorderings have tended to follow severe dislocation, and Scheidel's evidence suggests the shocks that level inequality most are often catastrophic. Two qualifications must stay in the text. First, Streeck & Thelen (2005) show that major change also happens gradually through layering, drift, and conversion, so "only after failure" should become "most often after failure, though gradual layering is also possible." Second, critical junctures are contingent. Crises have produced the New Deal and Bretton Woods, but also authoritarian outcomes, and Higgs shows that crisis-born state growth outlives the crisis. The dissertation's honest position is that crises open windows, and the framework is offered so that a fair design is available when one opens.

**Slow strain as slack removal.** Cook (1998) and Perrow (1984/1999) explain why strain matters without causing collapse: it wears down the buffers that keep latent faults from combining. The labour evidence is mixed and should be presented that way. Exposure is broad (Eloundou et al., 2024), local robot effects are real (Acemoglu & Restrepo, 2020), and early-career hiring in AI-exposed occupations is falling (Brynjolfsson et al., 2025/2026). But aggregate displacement has not appeared, and AI often complements workers (Brynjolfsson, Li & Raymond, 2025; Autor, 2015). Resource strain is better documented: LBNL projects US data centres at 6.7–12% of electricity by 2028, and IEA projects global use more than doubling by 2030. The water figures (Li et al., 2025) are model estimates.

**Stating the correlated-patch scenario rigorously.** Split it into premises, each with its own evidence:
1. *LLM patches are often wrong in ways that look right.* Supported by FLAWED (about 26% clean fixes), Smith et al. (2015, overfitting), Wu et al. (2023), BaxBench (about half of correct programs exploitable), and Perry et al. (2023, overconfidence).
2. *Errors are correlated across models, not independent.* Supported by Kim et al. (2025: 60% agreement when both models err, rising with capability), Bommasani et al. (2021), Kleinberg & Raghavan (2021), and FLAWED §4.4, where two vendors' models reproduced the same off-by-one in about a third of patches.
3. *Same-class verification does not catch it.* Kim et al.'s LLM-as-judge results, FLAWED's validator missing the regression, and Smith et al.'s point about evaluating patches with the tests that made them.
4. *Simultaneous deployment turns a shared defect into a systemic event.* CrowdStrike (8.5 million devices from a single unverified update), xz-utils, and the classic monoculture literature (Geer et al., 2003; Stamp, 2004).

The new contribution is the combination: a monoculture of *remediation process* rather than of installed software.

**Counterarguments to address.** (a) Birman & Schneider (2009) and Hedden & Raghavan (2026): standardization can improve security, and monoculture critiques are often overstated. (b) Correlation is partial. Bommasani et al. (2022) find adaptation choices change homogenization, and patches for one CVE differ in context across codebases. (c) Patches roll out on different schedules, which limits simultaneity. CrowdStrike was a single vendor push, which is a different mechanism. (d) Correlated IT failures so far have been recoverable. The FCA found minimal consumer harm from CrowdStrike, so the jump from "bad week for IT" to "renegotiating economic arrangements" needs the strain conditions argued separately. (e) The evidence base for premises 1–3 in 2026 is partly industry white papers. Present the scenario as a plausible, mechanistically specified candidate trigger, not a forecast.
