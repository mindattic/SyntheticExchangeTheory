# AGENTS.md: Synthetic Exchange Theory

Shared workflow: read [`../MINDATTIC_AGENT.md`](../MINDATTIC_AGENT.md) and `../mindattic-agent-standard/AGENTS.md`. This file adds project context only.

You are continuing a dissertation project with Ryan DeBraal. Read this file first, then `README.md`, then the chapters you are working on. The original working draft is preserved in `archive/working-draft-2026-10-03/`, and the pilot chapter removed on 2026-11-02 in `archive/pilot-2026-11-02/`. The session history is in `transcripts/`, and the source-verification notes are in `references/research-notes/`.

## The thesis in brief

Outcomes between humans and synthetic systems depend on the terms of exchange (consent, reciprocity, exit), not on machine character. The conditions are ordered, with exit foundational (Ch. 3). Fair terms are self-enforcing only in proportion to AI's dependence on human input, which is the grounding assumption, stated narrowly in Ch. 2. The economic layer (Ch. 4) is a basic income paid in **compute**, split into a survival tier and a discretionary tier, with demurrage. The governance layer (Ch. 5) is a blind constitutional convention plus Ostrom. Ch. 6 covers the transition, Ch. 7 limitations (including Section 7.5 on the absence of an empirical test), Ch. 8 convergence and Ch. 9 the conclusion, whose research agenda (Section 9.3) puts the design of a test first.

## Decisions Ryan made earlier (do not relitigate without asking)

- **Name:** Synthetic Exchange Theory. "Synthetic" is substrate-neutral. Old working title: "Symthetic Ethics".
- **Currency unit:** compute. "Quantum dollar" and "shannon" were rejected.
- **Allocation:** equal per person, indexed as a percentage of global compute.
- **Two tiers:** split by percentage at the source. The survival tier is non-tradable and non-borrowable; the discretionary tier is tradable.
- **Demurrage** on idle discretionary balances. It does not fully solve concentration, and the text says so.
- **The dissertation is entirely theoretical (2026-11-02).** Ryan removed the closed agrarian pilot (old Ch. 7 and Appendix B) because designing a scientific experiment would take a long time and is outside the dissertation's scope. The text now says what a test would require (Ch. 7.5, Ch. 9.3) and leaves its design to future work. The removed text is archived in `archive/pilot-2026-11-02/` for when that work starts; its design decisions (closed, volunteer, self-sufficient agrarian settlement; open-weight base model fine-tuned on settlement data; sub-AGI lead system orchestrating narrow sub-agents) still hold for a future experiment. Do not reintroduce the pilot into the dissertation without asking.
- **Transition trigger:** the correlated-patch catastrophe, also called convergent remediation.
- **Infrastructure control:** "structural interdependence," chosen over "trust" and "dual accountability."

## Decisions made in the 2026-10-08 dissertation pass (Ryan should review)

These were open items or gaps. They were resolved in the text to complete the manuscript, but Ryan has not yet approved them.

1. **Chapter order.** Since the 2026-11-02 removal of the pilot the order is 1 Intro, 2 Literature, 3 Formal theory, 4 Economic, 5 Governance, 6 Transition, 7 Limitations, 8 Convergence, 9 Conclusion, with Appendices A (formal model), B (glossary) and C (verification ledger). The transition chapter was moved after the design because it refers to it.
2. **Scope of the blindness** (the old unanswered doc comment). The text adopts *strong blindness*, specified as blindness about how the rules will **classify** parties, not about one's own substrate (Ch. 5.5). Weak blindness, meaning concealment of counterparties' type, is kept as the minimum.
3. **Identity/Sybil problem.** A two-layer credential system is proposed: it attests uniqueness without disclosing substrate. The text concedes that seat allocation between classes is a genesis rule outside the veil (Ch. 5.6).
4. **Control frame.** The text accepts *transitional* containment and AI-control protocols, and rejects *permanent* sovereignty (Ch. 5.2). It names the cooperative strand of AI safety as an ally.
5. **Grounding assumption** narrowed to: models need information from outside their generative loop, and only humans can supply it where the target is human meaning, preference, value or culture (Ch. 2.9).
6. **Capital channel of concentration.** Three capacity rules are offered (utilization charge, cap, collective ownership above a threshold) and the choice is left to the convention (Ch. 4.8).
7. **Authoritarian-capture objection and people-during-transition** are now answered (Ch. 6.5–6.6).
8. **Pilot additions** (superseded). The 2026-10-08 pass added bootstrapping, agrivoltaic siting, an exit package, stop rules, a base-vs-fine-tuned control, replication and a population size to the pilot chapter. That chapter was removed on 2026-11-02; the additions survive in the archived copy.
9. **Practitioner vignette.** Ryan's professional observation of LLM remediation shipped without testing is disclosed in Ch. 1.7 and used in Ch. 6.3 as a vignette, not as evidence of prevalence.
10. **AI-assisted authorship statement** added to the front matter.

## Open items

1. The license has not been chosen.
2. Pre-submission verification items are listed in Appendix C.5.
3. Degree program, institution, committee and formatting requirements are unknown. Ask Ryan before formatting for submission.
4. The earlier ethics paper this work grew from is not in the repo. Ask Ryan whether it should be cited or acknowledged.
5. The experimental design is future work. When Ryan starts it, begin from `archive/pilot-2026-11-02/` and from Ch. 7.5 and Ch. 9.3, which list what the test must contain.

## How we work

- Ryan often dictates by voice, so expect transcription artifacts and confirm words that look like mishearings.
- Pattern: discuss the idea, say honestly where it is weak, propose a concrete edit, and write it only after Ryan says yes.
- Name tensions instead of papering over them; Ryan prefers "state it as a limitation."
- Citations are APA 7, inline. **Never present an unopened source as verified.** Record the verification level in Appendix C and add notes to `references/research-notes/`.
- Write the chapters as prose, not bullet lists. Quote sparingly and paraphrase.

## Repo conventions

- One chapter per file under `chapters/`, numbered in reading order. Subsections use `##` and `###`.
- `chapters/10-references.md` is the reference list of record. Exports are generated by `powershell -File scripts\export.ps1` (MindAttic.Export, configured by `export.json`) into `D:\Projects\MindAttic\ePub\MindAttic\SET\`; never hand-edit an export. Edit the chapters, then re-export, then copy the new `.pdf` and `.docx` into `exports/` and the `.md` into `docs/synthetic-exchange-theory.md` (the file GitHub Pages publishes).
- Each chapter file starts with exactly one `#` heading (`# Chapter N: Title`, `# Appendix X: Title`, `# References`, or a front-matter section); the title page and contents are generated from `export.json`.
- When adding a citation, add the reference entry, add its verification level to Appendix C, and check that in-text and reference-list forms match. APA disambiguating initials are used for same-surname first authors (D. Guo / Y. Guo; Y. Wu). When removing a citation, check whether the reference entry is now orphaned and remove it too.
