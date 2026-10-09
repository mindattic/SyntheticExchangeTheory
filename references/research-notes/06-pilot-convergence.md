# Research file 06: Pilot design (Ch. 1B) and Convergence (Ch. 6)

Compiled 2026-10-08. Every entry was located via web fetch of a publisher page, DOI/Crossref/OpenAlex record, PubMed/Europe PMC, an official government page, or the full text. Nothing below is presented from memory. Verification levels:
- **full text read**: the body (or the relevant sections) was read.
- **abstract/publisher page read**: the abstract or official landing page was read.
- **record located only**: bibliographic metadata was confirmed, but the content was not read. Content claims at this level come from secondary summaries and are flagged.

Many publisher pages (ScienceDirect, Science, Nature, JAMA, OECD, HHS) block automated fetching, so several items stop at the record or abstract level. The web-search quota ran out late in the session, and the remaining checks used direct DOI and database lookups.

---

## Part A. The draft's own sources (Chapter 6)

### Wadan2025_OIreview
- Wadan, A.-H. S. (2025). Organoid intelligence and biocomputing advances: Current steps and future directions. *Brain Organoid and Systems Neuroscience Journal, 3*, 8–14. https://doi.org/10.1016/j.bosn.2025.01.002
- Link: https://www.sciencedirect.com/science/article/pii/S294992162500002X
- Verification: record located; abstract content checked via the OpenAlex abstract index and keywords (ScienceDirect, the SPJ PDF mirror and ResearchGate all returned 403). Body not read.
- What it actually establishes: A single-author narrative mini-review in a new Elsevier open-access journal (CC BY; online 29 Jan 2025; the author is reportedly at Galala University, Egypt). The abstract covers organoids for disease modelling and drug testing, and sustainability uses (CO2 capture, bioremediation, pollution control). It also covers enabling technologies (microfluidics, AI, electrophysiology), the need for standardized protocols, ethical and legal issues including the moral status of organoids with cognitive-like properties, and the Baltimore Declaration as a governance framework. It reports no original data.
- Use in dissertation: Usable only as a secondary overview. The abstract does **not** contain "learning", "plasticity", "parallel", "consciousness", "interface" or "consent", so the specific attributions the draft makes to it cannot be confirmed (see Corrections). Replace or supplement it with Smirnova et al. (2023), Kagan et al. (2022), Cai et al. (2023) and NASEM (2021) for the substantive claims.

### UCSC2025_OrganoidNews (news item)
- Cerf, E. (2025, October 20). Effort aims to uncover the learning and reasoning potential of brain organoids. *UC Santa Cruz News*. https://news.ucsc.edu/2025/10/learning-and-reasoning-potential-of-brain-organoids/
- Link: as above
- Verification: full text read (university news release, not peer-reviewed).
- What it actually establishes: The UCSC Genomics Institute (lead Tal Sharf; co-PIs David Haussler, Mircea Teodorescu and Mohammed Mostajo-Radji) received about $1.9M from NSF's EFRI "Biocomputing through EnGINeering Organoid Intelligence" (BEGIN OI) program. The team plans to test whether organoids can learn from feedback and solve tasks in real time, using a cloud-connected closed-loop platform, open-source hardware and software, reinforcement learning, OI benchmarks and an "organoid Turing test". It will also monitor for signs of consciousness. **Hank Greely (Stanford Law; Center for Law and the Biosciences) is quoted.** He asks whether organoids should be treated as human tissue samples, lab animals, persons, or something else. He also refers to the details of informed consent for the people whose cells are used. He poses these as open questions and takes no position. His formal role in the project is not stated.
- Use in dissertation: The Greely attribution in Ch. 6 is **confirmed** in substance. Cite it as a university news release, add the author and date, and note that it describes a funded project, not findings.

### NSF_BEGINOI_2023 (underlying program)
- U.S. National Science Foundation. (2023). *Emerging Frontiers in Research and Innovation (EFRI): Biocomputing through EnGINeering Organoid Intelligence (BEGIN OI)* (NSF 24-508). https://www.nsf.gov/funding/opportunities/emerging-frontiers-research-innovation-efri-biocomputing/13708/nsf24-508
- Link: as above
- Verification: abstract/publisher page read (the program page; the solicitation PDF was not opened).
- What it actually establishes: The solicitation was published 15 Nov 2023 and is now archived; NSF 26-524 supersedes it. It funds design, engineering and fabrication of organoid systems that process information dynamically while interfacing with non-living systems. It is co-run across five NSF directorates, including Social, Behavioral and Economic Sciences. The program page states no specific ethics (ELSI) requirement. The specific UCSC award number could not be confirmed.
- Use in dissertation: Shows that organoid computing is now a federally funded engineering goal, not a fringe idea. This strengthens the claim that "tissue as substrate" is a near-term governance question.

### Robbins2026_GoalDirected (peer-reviewed follow-up from the UCSC group)
- Robbins, A., Schweiger, H. E., Hernandez, S., Spaeth, A., Voitiuk, K., Parks, D. F., van der Molen, T., Geng, J., Cline, I., Kosik, K. S., Salama, S. R., Sharf, T., Mostajo-Radji, M. A., Haussler, D., & Teodorescu, M. (2026). Goal-directed learning in cortical organoids. *Cell Reports, 45*(2), Article 116984. https://doi.org/10.1016/j.celrep.2026.116984
- Link: https://doi.org/10.1016/j.celrep.2026.116984 ; news release https://news.ucsc.edu/2026/02/brain-organoids-goal-directed-learning/
- Verification: record located (Crossref; CC BY 4.0). Content is from the UCSC news release, read in full; the Cell page returned 403.
- What it actually establishes (per the release): **Mouse**-stem-cell-derived cortical organoids were trained on a virtual cart-pole task through electrical stimulation, with RL-selected training signals. Adaptive training raised the success rate from about 4.5% (random) to 46%. The learning did not persist: performance returned to baseline after a 45-minute rest. Haussler said using human organoids to replace robotic controllers would raise serious ethical issues.
- Use in dissertation: The best current peer-reviewed evidence of organoid "learning", and also evidence of how limited it is. Use it to calibrate Ch. 6's claims. Verify the abstract against the open-access text before citing specifics.

---

## Part B. Organoid intelligence, organoid ethics and governance

### Smirnova2023_OI
- Smirnova, L., Caffo, B. S., Gracias, D. H., Huang, Q., Morales Pantoja, I. E., Tang, B., Zack, D. J., Berlinicke, C. A., Boyd, J. L., Harris, T. D., Johnson, E. C., Kagan, B. J., Kahn, J., Muotri, A. R., Paulhamus, B. L., Schwamborn, J. C., Plotkin, J., Szalay, A. S., Vogelstein, J. T., . . . Hartung, T. (2023). Organoid intelligence (OI): The new frontier in biocomputing and intelligence-in-a-dish. *Frontiers in Science, 1*, Article 1017235. https://doi.org/10.3389/fsci.2023.1017235
- Link: https://www.frontiersin.org/journals/science/articles/10.3389/fsci.2023.1017235/full
- Verification: full text partly read (roughly the first 40%), plus the Crossref record. Check the author count against the PDF: Crossref lists 21.
- What it actually establishes: Coins "organoid intelligence" and sets out a research program built on 3D human brain organoids with microfluidic perfusion, 3D microelectrode arrays for input and output, and ML-based encoding and decoding. It proposes "embedded ethics" (ethicists working alongside researchers throughout). It flags donor privacy, return of findings, and whether donor rights continue after donation. It states the program does not aim to recreate consciousness. Claims that biocomputing could be more energy-efficient than silicon are projections.
- Use in dissertation: The primary source for Ch. 6's OI paragraph. Its open question about donor rights after donation maps directly onto the dissertation's consent and exit conditions.

### Hartung2023_Baltimore
- Hartung, T., Smirnova, L., Morales Pantoja, I. E., Akwaboah, A., Alam El Din, D.-M., et al. (2023). The Baltimore declaration toward the exploration of organoid intelligence [Editorial]. *Frontiers in Science, 1*, Article 1068159. https://doi.org/10.3389/fsci.2023.1068159 (complete the author list from the publisher record)
- Link: https://www.frontiersin.org/journals/science/articles/10.3389/fsci.2023.1068159/full
- Verification: abstract/publisher page read.
- What it actually establishes: A consensus editorial from the first OI workshop (February 2022). It commits signatories to pursue OI responsibly, to stay alert to the possibility that aspects of consciousness emerge, and to keep an ethical framework that reflects public values. It names donor rights and interests as a concern but specifies no consent procedure.
- Use in dissertation: Shows that the field acknowledges the donor and consciousness problems while leaving consent mechanisms open, which is the gap Ch. 6 claims to fill.

### Kagan2022_DishBrain (with critique and reply)
- Kagan, B. J., Kitchen, A. C., Tran, N. T., Habibollahi, F., Khajehnejad, M., Parker, B. J., Bhat, A., Rollo, B., Razi, A., & Friston, K. J. (2022). In vitro neurons learn and exhibit sentience when embodied in a simulated game-world. *Neuron, 110*(23), 3952–3969.e8. https://doi.org/10.1016/j.neuron.2022.09.001
- Balcı, F., Ben Hamed, S., Boraud, T., Bouret, S., Brochier, T., Brun, C., Cohen, J. Y., Coutureau, E., Deffains, M., Doyère, V., Gregoriou, G. G., Heimel, J. A., Kilavik, B. E., Lee, D., Leuthardt, E. C., Mainen, Z. F., Mathis, M. W., Monosov, I. E., Naudé, J., . . . Zimmermann, J. (2023). A response to claims of emergent intelligence and sentience in a dish. *Neuron, 111*(5), 604–605. https://doi.org/10.1016/j.neuron.2023.02.009
- Kagan, B. J., Razi, A., Bhat, A., Kitchen, A. C., Tran, N. T., Habibollahi, F., Khajehnejad, M., Parker, B. J., Rollo, B., & Friston, K. J. (2023). Scientific communication and the semantics of sentience. *Neuron, 111*(5), 606–607. https://doi.org/10.1016/j.neuron.2023.02.008
- Link: https://pubmed.ncbi.nlm.nih.gov/36228614/
- Verification: Kagan 2022, abstract read (PubMed). Balcı 2023 and the reply: record located only (paywalled letters).
- What it actually establishes: Human and rodent neuron cultures on a high-density multielectrode array, given structured closed-loop feedback, improved at a simulated Pong game within minutes; control conditions did not. The authors frame this with the free-energy principle and call it "synthetic biological intelligence". A 30-author response in the same journal disputes the intelligence and sentience framing, and the original authors replied defending their minimal meaning of "sentience".
- Use in dissertation: The empirical anchor for human-derived tissue in a computing loop. Always cite the dispute alongside it. The contested status is itself an argument for precautionary consent.

### Cai2023_Brainoware
- Cai, H., Ao, Z., Tian, C., Wu, Z., Liu, H., Tchieu, J., Gu, M., Mackie, K., & Guo, F. (2023). Brain organoid reservoir computing for artificial intelligence. *Nature Electronics, 6*(12), 1032–1039. https://doi.org/10.1038/s41928-023-01069-w
- Link: https://www.nature.com/articles/s41928-023-01069-w
- Verification: abstract/publisher page read.
- What it actually establishes: "Brainoware" uses a human brain organoid as the reservoir in a reservoir-computing system, read through a multielectrode array. Spatiotemporal stimulation produced nonlinear dynamics, fading memory, and unsupervised adaptation through changes in functional connectivity. It was demonstrated on speech recognition and on predicting a nonlinear (Hénon) map.
- Use in dissertation: A peer-reviewed case where training input physically reshapes living human-derived tissue. Here the boundary between "data" and "substrate" genuinely collapses.

### LavazzaMassimini2018
- Lavazza, A., & Massimini, M. (2018). Cerebral organoids: Ethical issues and consciousness assessment. *Journal of Medical Ethics, 44*(9), 606–610. https://doi.org/10.1136/medethics-2017-104555
- Link: https://pubmed.ncbi.nlm.nih.gov/29491041/
- Verification: abstract/publisher page read (PubMed).
- What it actually establishes: Organoids' neural connectivity and electrical activity raise the question of whether they are, or may become, minimally sentient. The authors propose assessing this empirically with tools such as the Perturbational Complexity Index (IIT-inspired), which is already used for unresponsive patients. Any sign of sensibility would require ethical reconsideration of their research use.
- Use in dissertation: Supports tying the dissertation's participant status to measurable thresholds rather than assuming it.

### Hyun2020_OrganoidEthics
- Hyun, I., Scharf-Deering, J. C., & Lunshof, J. E. (2020). Ethical issues related to brain organoid research. *Brain Research, 1732*, Article 146653. https://doi.org/10.1016/j.brainres.2020.146653
- Link: https://pubmed.ncbi.nlm.nih.gov/32017900/
- Verification: abstract/publisher page read.
- What it actually establishes: A structured review of five ethics domains: oversight; procurement of biomaterials and donor consent; clinical translation; animal research (chimeras); and organoid consciousness and moral status.
- Use in dissertation: A map of the ethics terrain, useful for showing that donor consent is a recognized and distinct issue.

### Kataoka2024_DonorConsent (with Kataoka 2023)
- Kataoka, M., Gyngell, C., Savulescu, J., & Sawai, T. (2024). The donation of human biological material for brain organoid research: The problems of consciousness and consent. *Science and Engineering Ethics, 30*(1), Article 3. https://doi.org/10.1007/s11948-024-00471-7
- Kataoka, M., Gyngell, C., Savulescu, J., & Sawai, T. (2023). The ethics of human brain organoid transplantation in animals. *Neuroethics, 16*(3), Article 27. https://doi.org/10.1007/s12152-023-09532-3
- Link: https://pubmed.ncbi.nlm.nih.gov/38315257/
- Verification: abstract/publisher page read (both).
- What it actually establishes: The 2024 paper argues that donors cannot give fully informed consent while organoid consciousness is uncertain, and that donor consent alone cannot justify risks to the organoid itself. It recommends project-specific consent rather than broad consent, assurances to donors that organoids will be protected, and precautionary measures to back those assurances. The 2023 paper extends the analysis to transplantation into animals.
- Use in dissertation: The closest existing argument to Ch. 6's "consent when the substrate is tissue". Cite it as the starting point the dissertation builds on.

### NASEM2021_Organoids
- National Academies of Sciences, Engineering, and Medicine. (2021). *The emerging field of human neural organoids, transplants, and chimeras: Science, ethics, and governance*. The National Academies Press. https://doi.org/10.17226/26078
- Link: https://www.nationalacademies.org/read/26078
- Verification: abstract/publisher page read (catalog page and summary chapter).
- What it actually establishes: It judges it extremely unlikely that current neural organoids will gain awareness or the capacity for pain in the foreseeable future, holds that neural activity alone does not demonstrate either, and calls for revisiting this as complexity grows. It recommends no additional oversight for now. It treats donor consent as unresolved: past donors seldom consented specifically to organoid uses and often cannot be recontacted. It notes heightened sensitivities in some communities.
- Use in dissertation: The authoritative governance baseline. Ch. 6 should state that the expert consensus currently sees no consciousness, and argue for its extended conditions on precautionary and donor-interest grounds rather than on claims of present sentience.

### ISSCR2021_Guidelines
- Lovell-Badge, R., Anthony, E., Barker, R. A., Bubela, T., Brivanlou, A. H., Carpenter, M., Charo, R. A., Clark, A., Clayton, E., Cong, Y., Daley, G. Q., Fu, J., Fujita, M., Greenfield, A., Goldman, S. A., Hill, L., Hyun, I., Isasi, R., Kahn, J., . . . Zhai, X. (2021). ISSCR guidelines for stem cell research and clinical translation: The 2021 update. *Stem Cell Reports, 16*(6), 1398–1408. https://doi.org/10.1016/j.stemcr.2021.05.012
- Link: https://pmc.ncbi.nlm.nih.gov/articles/PMC8190668/
- Verification: full text read (the Stem Cell Reports summary; the standalone guidelines document was not read).
- What it actually establishes: Most in vitro organoid research, including neural organoids, falls in Category 1A, exempt from specialized review. The guidelines cite no current evidence of organoid consciousness or pain and commit to revisiting the question. Appropriate donor consent is still required.
- Use in dissertation: Paired with NASEM, it shows the regulatory gap: organoid computing currently sits in the lowest oversight category.

---

## Part C. Brain-computer interfaces

### Willett2023_SpeechBCI
- Willett, F. R., Kunz, E. M., Fan, C., Avansino, D. T., Wilson, G. H., Choi, E. Y., Kamdar, F., Glasser, M. F., Hochberg, L. R., Druckmann, S., Shenoy, K. V., & Henderson, J. M. (2023). A high-performance speech neuroprosthesis. *Nature, 620*(7976), 1031–1036. https://doi.org/10.1038/s41586-023-06377-x
- Link: https://pubmed.ncbi.nlm.nih.gov/37612500/
- Verification: abstract/publisher page read.
- What it actually establishes: Intracortical arrays in a participant with ALS decoded attempted speech at 62 words per minute. Word error rate was 9.1% on a 50-word vocabulary and 23.8% on a 125,000-word vocabulary. Articulatory representations persisted years after paralysis.
- Use in dissertation: Neural activity is already converted directly into machine text, so "human data" and "machine output" merge at the interface.

### Metzger2023_Avatar
- Metzger, S. L., Littlejohn, K. T., Silva, A. B., Moses, D. A., Seaton, M. P., Wang, R., Dougherty, M. E., Liu, J. R., Wu, P., Berger, M. A., Zhuravleva, I., Tu-Chan, A., Ganguly, K., Anumanchipalli, G. K., & Chang, E. F. (2023). A high-performance neuroprosthesis for speech decoding and avatar control. *Nature, 620*(7976), 1037–1046. https://doi.org/10.1038/s41586-023-06443-4 (Author Correction: *Nature, 631*, E13, 2024, https://doi.org/10.1038/s41586-024-07735-z)
- Link: https://pubmed.ncbi.nlm.nih.gov/37612505/
- Verification: abstract/publisher page read.
- What it actually establishes: An ECoG array over the speech cortex decoded three outputs: text (median 78 words per minute, about 25% word error rate), speech synthesized in the participant's pre-injury voice, and facial-avatar animation. Training took under two weeks.
- Use in dissertation: Identity-bearing outputs (voice, face) generated from neural data, which shows why exit must include ownership and deletion of the personal models.

### Card2024_ALSspeech
- Card, N. S., Wairagkar, M., Iacobacci, C., Hou, X., Singer-Clark, T., Willett, F. R., Kunz, E. M., Fan, C., Vahdati Nia, M., Deo, D. R., Srinivasan, A., Choi, E. Y., Glasser, M. F., Hochberg, L. R., Henderson, J. M., Shahlaie, K., Stavisky, S. D., & Brandman, D. M. (2024). An accurate and rapidly calibrating speech neuroprosthesis. *New England Journal of Medicine, 391*(7), 609–618. https://doi.org/10.1056/NEJMoa2314132
- Link: https://pubmed.ncbi.nlm.nih.gov/39141853/
- Verification: abstract/publisher page read.
- What it actually establishes: Four arrays (256 electrodes) were implanted in a man with ALS. Accuracy was 99.6% on a 50-word vocabulary on day one, after 30 minutes of calibration, and 97.5% on a large vocabulary sustained over 8.4 months. He used it for more than 248 hours of conversation at about 32 words per minute, with output in a voice resembling his pre-ALS voice. Trial: BrainGate2, NCT00912041.
- Use in dissertation: Long-term daily dependence on an implant. For this participant, losing the device or the model would be a concrete harm, which makes exit costs real.

### Neuralink2024_PRIME (company/registry; not peer-reviewed)
- Neuralink Corp. (2024). *PRIME: Early feasibility study of a precise robotically implanted brain-computer interface* (ClinicalTrials.gov Identifier NCT06429735). https://clinicaltrials.gov/study/NCT06429735
- Link: as above; company blog: https://neuralink.com/blog/prime-study-progress-update-user-experience/
- Verification: registry record read (ClinicalTrials.gov API). Blog: record located only.
- What it actually establishes: A sponsor-registered early feasibility study of the N1 implant and R1 surgical robot. Actual start 9 Jan 2024, record first posted 28 May 2024, recruiting, estimated enrollment 15. Performance claims come only from the company. No independent peer-reviewed outcome report was located.
- Use in dissertation: Cite only as evidence that a commercial invasive-BCI trial exists. Do not cite performance claims. The disclosure gap is itself relevant to reciprocity.

---

## Part D. Neurorights and neural-data law

### Yuste2017_FourPriorities
- Yuste, R., Goering, S., Agüera y Arcas, B., Bi, G., Carmena, J. M., Carter, A., Fins, J. J., Friesen, P., Gallant, J., Huggins, J. E., Illes, J., Kellmeyer, P., Klein, E., Marblestone, A., Mitchell, C., Parens, E., Pham, M., Rubel, A., Sadato, N., . . . Wolpaw, J. (2017). Four ethical priorities for neurotechnologies and AI. *Nature, 551*(7679), 159–163. https://doi.org/10.1038/551159a
- Link: https://pubmed.ncbi.nlm.nih.gov/29120438/
- Verification: abstract/publisher page read (standfirst only).
- What it actually establishes: Argues that AI and brain-computer interfaces must respect and preserve privacy, identity, agency and equality, the four priorities in the title. The body's detailed recommendations were not read.
- Use in dissertation: The founding neurorights agenda. "Agency" and "identity" support the Ch. 6 claim that convergence blurs authorship of data.

### IencaAndorno2017_Neurorights
- Ienca, M., & Andorno, R. (2017). Towards new human rights in the age of neuroscience and neurotechnology. *Life Sciences, Society and Policy, 13*(1), Article 5. https://doi.org/10.1186/s40504-017-0050-1
- Link: https://pubmed.ncbi.nlm.nih.gov/28444626/
- Verification: abstract/publisher page read.
- What it actually establishes: Argues that existing human rights may not adequately cover neurotechnology. It proposes four rights: cognitive liberty, mental privacy, mental integrity, and psychological continuity.
- Use in dissertation: Rights language for the exit condition. Psychological continuity and mental integrity are what exit from an implanted system must protect.

### Chile2021_Ley21383
- Ley N.º 21.383. Modifica la Carta Fundamental, para establecer el desarrollo científico y tecnológico al servicio de las personas. (2021, 25 de octubre). *Diario Oficial de la República de Chile*. https://www.bcn.cl/leychile/navegar?idNorma=1166983
- Link: as above
- Verification: full text read (LeyChile service).
- What it actually establishes: Adds a paragraph to Article 19 No. 1 of the Chilean Constitution. Scientific and technological development must serve people and respect life and physical and psychic integrity, and the law shall specially protect brain activity and the information derived from it. Promulgated 14 Oct 2021 and published 25 Oct 2021. A related Supreme Court ruling, *Girardi v. Emotiv* (Rol 105.065-2023, reportedly 9 Aug 2023), reportedly ordered deletion of brain data. That ruling is record located only, via secondary commentary.
- Use in dissertation: The first constitutional protection of neural information. The Emotiv ruling, once read, would show deletion (a form of exit) being enforced.

### Colorado2024_HB1058
- Protect Privacy of Biological Data, H.B. 24-1058, 74th Gen. Assemb., 2d Reg. Sess. (Colo. 2024). https://leg.colorado.gov/bills/hb24-1058
- Link: as above
- Verification: abstract/publisher page read (official bill page; the signed act was not opened).
- What it actually establishes: Amends the Colorado Privacy Act so that "biological data", including "neural data", counts as sensitive data requiring consent. Signed 17 Apr 2024; effective 7 Aug 2024. Coverage is tied to data used or intended for identification purposes.
- Use in dissertation: The first U.S. statute on neural data. The identification limit means organoid-derived or de-identified neural signals may fall outside it.

### California2024_SB1223
- S.B. 1223, 2023–2024 Reg. Sess., ch. 887 (Cal. 2024). https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB1223
- Link: as above (blocked); tracker: https://calmatters.digitaldemocracy.org/bills/ca_202320240sb1223
- Verification: record located only (secondary legislative tracker).
- What it actually establishes: Adds "neural data" to "sensitive personal information" under the CCPA. It was chaptered 28 Sep 2024 (Ch. 887), with Sen. Becker as author. The statutory definition and the 1 Jan 2025 operative date come from secondary summaries and should be read against the chaptered text before citing.
- Use in dissertation: With Colorado, it shows that U.S. law handles neural data as consumer-privacy "limit use" rights, not as reciprocity or exit.

### UNESCO2025_Neurotech
- UNESCO. (2025). *Recommendation on the ethics of neurotechnology*. General Conference, Samarkand. https://www.unesco.org/en/ethics-neurotech
- Link: press release https://www.unesco.org/en/articles/ethics-neurotechnology-unesco-adopts-first-global-standard-cutting-edge-technology
- Verification: abstract/publisher page read (press release and topic page; the Recommendation text was not read).
- What it actually establishes: UNESCO announced adoption on 5 Nov 2025 at the General Conference in Samarkand and calls it the first global standard on neurotechnology, effective 12 Nov. The release says neural data is to be treated as highly sensitive, with explicit consent and transparency. It cautions against non-therapeutic use on children and against workplace productivity monitoring, and calls for regulation of manipulative consumer products. The "43rd session" label and its non-binding status come from secondary sources.
- Use in dissertation: **Verified as adopted.** Cite it as the current international soft-law floor. It remains framed around persons using neurotechnology, not tissue as computing substrate.

---

## Part E. Mind, moral status, and AI welfare

### ClarkChalmers1998_ExtendedMind
- Clark, A., & Chalmers, D. (1998). The extended mind. *Analysis, 58*(1), 7–19. https://doi.org/10.1093/analys/58.1.7
- Link: https://consc.net/papers/extended.html
- Verification: full text read (author copy).
- What it actually establishes: Argues for "active externalism". External resources that are reliably available, easily accessed, automatically endorsed, and (tentatively) previously endorsed can be part of a cognitive process. Otto's notebook functions as Inga's biological memory does. The argument concerns cognition and belief, not moral status.
- Use in dissertation: Grounds a functional, substrate-neutral view of cognition, consistent with the substrate-agnostic compute unit. Moving to moral standing requires Birch or Long et al. as well.

### Birch2024_EdgeOfSentience
- Birch, J. (2024). *The edge of sentience: Risk and precaution in humans, other animals, and AI*. Oxford University Press. https://doi.org/10.1093/9780191966729.001.0001
- Link: https://academic.oup.com/book/57949 (open access, CC BY-NC-ND)
- Verification: record located only (Crossref confirms DOI, ISBNs and licence; content from a secondary summary).
- What it actually establishes (secondary): A precautionary framework for "sentience candidates", meaning beings with a realistic possibility of sentience. It calls for proportionate precautions chosen through inclusive democratic deliberation, without waiting for a settled science of consciousness. Its cases include neural organoids and AI.
- Use in dissertation: The core framework for organoid and AI participants under uncertainty. Read the organoid and AI chapters (open access) before quoting.

### Butlin2023_ConsciousnessAI
- Butlin, P., Long, R., Elmoznino, E., Bengio, Y., Birch, J., Constant, A., Deane, G., Fleming, S. M., Frith, C., Ji, X., Kanai, R., Klein, C., Lindsay, G., Michel, M., Mudrik, L., Peters, M. A. K., Schwitzgebel, E., Simon, J., & VanRullen, R. (2023). *Consciousness in artificial intelligence: Insights from the science of consciousness* (arXiv:2308.08708). arXiv. https://doi.org/10.48550/arXiv.2308.08708
- Link: https://arxiv.org/abs/2308.08708
- Verification: abstract/publisher page read.
- What it actually establishes: Derives computational "indicator properties" from leading scientific theories of consciousness and assesses AI systems against them. It finds no current system is a strong candidate for consciousness, but no obvious technical barrier to building ones that satisfy the indicators.
- Use in dissertation: Moral risk depends on architecture, not on the quantity of compute. The currency unit therefore cannot double as a moral-status measure.

### LongSebo2024_AIWelfare
- Long, R., Sebo, J., Butlin, P., Finlinson, K., Fish, K., Harding, J., Pfau, J., Sims, T., Birch, J., & Chalmers, D. (2024). *Taking AI welfare seriously* (arXiv:2411.00986). arXiv. https://doi.org/10.48550/arXiv.2411.00986
- Link: https://arxiv.org/abs/2411.00986
- Verification: abstract/publisher page read.
- What it actually establishes: There is a realistic possibility that some AI systems will be conscious and/or robustly agentic in the near future. The authors do not claim they are moral patients. They recommend that developers acknowledge the issue, assess their systems, and prepare policies.
- Use in dissertation: Supports Ch. 6's closing question of who counts as a party. It also supports building a welfare-assessment trigger into governance.

---

## Part F. Measuring compute across substrates

### Preskill2018_NISQ
- Preskill, J. (2018). Quantum computing in the NISQ era and beyond. *Quantum, 2*, 79. https://doi.org/10.22331/q-2018-08-06-79
- Link: https://quantum-journal.org/papers/q-2018-08-06-79/
- Verification: full text read.
- What it actually establishes: Coins "NISQ". Qubit count alone is not a figure of merit: gate fidelity, speed, connectivity and measurement error also matter. With two-qubit error rates around 0.1%, circuits much beyond about 1,000 gates are swamped by noise. Quantum speedup is defined against the best classical methods, which keep improving.
- Use in dissertation: Directly supports Ch. 6's statement that quantum measures do not map onto classical operations.

### Cross2019_QuantumVolume
- Cross, A. W., Bishop, L. S., Sheldon, S., Nation, P. D., & Gambetta, J. M. (2019). Validating quantum computers using randomized model circuits. *Physical Review A, 100*(3), 032328. https://doi.org/10.1103/PhysRevA.100.032328
- Link: https://arxiv.org/abs/1811.12926
- Verification: full text read.
- What it actually establishes: Defines quantum volume from the largest square random circuit (width equal to depth) that a device runs with heavy-output probability above 2/3. The metric depends on qubit count, error rates, connectivity, gate set and compiler. The authors say it "loosely coincides" with the classical simulation cost of those circuits. They expect it to need replacing at lower error rates.
- Use in dissertation: The nearest existing bridge to classical cost, but it measures capability on a benchmark, not throughput. It is evidence that the conversion methodology is genuinely open.

### Arute2019_Supremacy (with Pednault 2019; Pan, Chen & Zhang 2022)
- Arute, F., Arya, K., Babbush, R., et al. (2019). Quantum supremacy using a programmable superconducting processor. *Nature, 574*(7779), 505–510. https://doi.org/10.1038/s41586-019-1666-5 (77 authors, last author Martinis, J. M. Complete the APA 7 list, first 19 … last, from the DOI record; only the first author, last author and author count were confirmed.)
- Pednault, E., Gunnels, J. A., Nannicini, G., Horesh, L., & Wisnieff, R. (2019). *Leveraging secondary storage to simulate deep 54-qubit Sycamore circuits* (arXiv:1910.09534). https://doi.org/10.48550/arXiv.1910.09534
- Pan, F., Chen, K., & Zhang, P. (2022). Solving the sampling problem of the Sycamore quantum circuits. *Physical Review Letters, 129*(9), 090502. https://doi.org/10.1103/PhysRevLett.129.090502
- Verification: Arute, record located only (Nature redirects to a login). Pednault, abstract read (preprint). Pan et al., abstract/publisher page read.
- What it actually establishes: Sycamore (53 qubits) sampled random circuits in about 200 seconds, a task the authors estimated would take about 10,000 years classically. IBM argued it would take days on Summit. Pan et al. later sampled classically in about 15 hours on 512 GPUs.
- Use in dissertation: The "classical equivalent" of quantum work depends on the task, the algorithm and the date. Price quantum work by verifiable output, not by claimed equivalence.

### Shastri2021_Photonics
- Shastri, B. J., Tait, A. N., Ferreira de Lima, T., Pernice, W. H. P., Bhaskaran, H., Wright, C. D., & Prucnal, P. R. (2021). Photonics for artificial intelligence and neuromorphic computing. *Nature Photonics, 15*(2), 102–114. https://doi.org/10.1038/s41566-020-00754-y
- Link: https://arxiv.org/abs/2011.00111
- Verification: abstract/publisher page read.
- What it actually establishes: A review of photonic neuromorphic hardware. Light-based neural-network computation complements electronics, with very low latency. The abstract gives no energy figures.
- Use in dissertation: The same abstract operation (multiply-accumulate) runs on physically different substrates, which supports defining the currency unit at the level of information and operations.

### Markovic2020_Neuromorphic
- Marković, D., Mizrahi, A., Querlioz, D., & Grollier, J. (2020). Physics for neuromorphic computing. *Nature Reviews Physics, 2*(9), 499–510. https://doi.org/10.1038/s42254-020-0208-2
- Link: https://arxiv.org/abs/2003.04711
- Verification: abstract/publisher page read.
- What it actually establishes: Argues that energy-efficient brain-inspired computing requires "reinventing electronics". It surveys physics and materials for artificial neurons and synapses (memristive, spintronic, photonic, etc.) and names open challenges in algorithm-hardware co-design and scaling.
- Use in dissertation: Shows a continuum from digital silicon through analog and neuromorphic hardware to biological substrates, where instruction counts lose meaning.

### Landauer1961
- Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of Research and Development, 5*(3), 183–191. https://doi.org/10.1147/rd.53.0183
- Link: as above
- Verification: record located only (abstract seen via an excerpt; the PDF is a scanned image).
- What it actually establishes: Logically irreversible operations entail a minimum heat dissipation of the order of kT per operation. The familiar "kT ln 2 per erased bit" is the later standard formulation. The principle's derivation has been contested in the philosophy-of-physics literature.
- Use in dissertation: A physical, substrate-independent lower bound tied to information erased. It anchors an information-based unit, but it is a lower bound, not an exchange rate.

---

## Part G. Pilot ethics and method

### Belmont1979
- National Commission for the Protection of Human Subjects of Biomedical and Behavioral Research. (1979). *The Belmont report: Ethical principles and guidelines for the protection of human subjects of research*. U.S. Department of Health, Education, and Welfare. https://www.hhs.gov/ohrp/regulations-and-policy/belmont-report/read-the-belmont-report/index.html
- Link: full text read at https://archive.epa.gov/hsrb/web/pdf/belmont_report.pdf
- Verification: full text read.
- What it actually establishes: Three principles: respect for persons, beneficence and justice. They are applied to consent, risk-benefit assessment and subject selection. Consent must be free of coercion and undue influence. Undue influence includes excessive rewards and pressure from people in authority where sanctions are possible, and inducements become undue for especially vulnerable subjects.
- Use in dissertation: An AI that controls the pilot's currency, power and food is an authority with possible sanctions. Belmont makes voluntariness and exit primary outcome measures, not side conditions.

### CommonRule2018
- Protection of Human Subjects, 45 C.F.R. pt. 46 (2018). Federal Policy for the Protection of Human Subjects, 82 Fed. Reg. 7149 (Jan. 19, 2017).
- Link: https://www.govinfo.gov/content/pkg/CFR-2023-title45-vol1/xml/CFR-2023-title45-vol1-sec46-116.xml
- Verification: full text of §46.116 read. Rulemaking dates: record located only.
- What it actually establishes: §46.116(b)(8) requires telling subjects that participation is voluntary, that refusal carries no penalty or loss of benefits they are otherwise entitled to, and that they may withdraw at any time. The 2018 revision requires key information first and adds broad consent for secondary use.
- Use in dissertation: The regulatory floor. Withdrawal must not forfeit benefits, so currency balances, labor credit and livestock contributed must be portable or redeemable on exit.

### Emanuel2000_Seven
- Emanuel, E. J., Wendler, D., & Grady, C. (2000). What makes clinical research ethical? *JAMA, 283*(20), 2701–2711. https://doi.org/10.1001/jama.283.20.2701
- Link: https://jamanetwork.com/journals/jama/fullarticle/192740
- Verification: abstract/publisher page read.
- What it actually establishes: Seven requirements: social value, scientific validity, fair subject selection, favorable risk-benefit ratio, independent review, informed consent, and respect for enrolled subjects (including withdrawal and welfare monitoring).
- Use in dissertation: A checklist the pilot protocol should be written against. "Independent review" implies an ethics board outside both the settlement and the AI.

### Nosek2018_Preregistration
- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., & Mellor, D. T. (2018). The preregistration revolution. *Proceedings of the National Academy of Sciences, 115*(11), 2600–2606. https://doi.org/10.1073/pnas.1708274114
- Link: as above
- Verification: abstract/publisher page read.
- What it actually establishes: Distinguishes prediction from postdiction and argues that hindsight bias conflates them. Preregistration of hypotheses and analysis plans before seeing outcomes is the remedy, with workarounds for imperfect cases.
- Use in dissertation: Preregister the four falsifiable questions, their metrics and their failure thresholds before founding.

### McCambridge2014_Hawthorne
- McCambridge, J., Witton, J., & Elbourne, D. R. (2014). Systematic review of the Hawthorne effect: New concepts are needed to study research participation effects. *Journal of Clinical Epidemiology, 67*(3), 267–277. https://doi.org/10.1016/j.jclinepi.2013.08.015
- Link: https://pmc.ncbi.nlm.nih.gov/articles/PMC3969247/
- Verification: abstract/publisher page read.
- What it actually establishes: Across 19 studies, most found some evidence that research participation changes behavior. Heterogeneity means little is known about the size of the effect or how it works.
- Use in dissertation: A heavily instrumented, self-selected settlement will show participation effects. Comparison sites and long baselines are needed before improvements in wellbeing are credited to the AI.

### Popper1959_Logic
- Popper, K. (2002). *The logic of scientific discovery* (2nd ed.). Routledge. (Original work published 1959) https://doi.org/10.4324/9780203994627
- Link: https://www.routledge.com/The-Logic-of-Scientific-Discovery/Popper/p/book/9780415278447
- Verification: abstract/publisher page read.
- What it actually establishes: The classic statement of falsifiability as the demarcation criterion of empirical science.
- Use in dissertation: Grounds Ch. 1B's claim that its questions are "falsifiable". Each must state in advance what result would refute it.

### Hossain2019_LivingLabs
- Hossain, M., Leminen, S., & Westerlund, M. (2019). A systematic review of living lab literature. *Journal of Cleaner Production, 213*, 976–988. https://doi.org/10.1016/j.jclepro.2018.12.257
- Link: as above
- Verification: abstract/publisher page read (abstract via Semantic Scholar).
- What it actually establishes: Reviews 114 articles. Living labs are real-life settings and methodologies for user-involved innovation. Recurring challenges include temporality, governance, efficiency, user recruitment, sustainability, scalability and unpredictable outcomes.
- Use in dissertation: Places the pilot within an established methodology and anticipates its known weak points: governance, recruitment and limited duration.

### OECD2013_SWB
- OECD. (2013). *OECD guidelines on measuring subjective well-being*. OECD Publishing. https://doi.org/10.1787/9789264191655-en
- Link: as above
- Verification: record located only (Crossref; the OECD page returned 403).
- What it actually establishes: Bibliographic facts only. The contents (life evaluation, affect and eudaimonic modules) are widely described but were not verified here.
- Use in dissertation: The standard instrument family for the wellbeing outcome, allowing comparison against national baselines. Read it before specifying the modules.

### Diener1985_SWLS (with Diener et al. 1999)
- Diener, E., Emmons, R. A., Larsen, R. J., & Griffin, S. (1985). The Satisfaction With Life Scale. *Journal of Personality Assessment, 49*(1), 71–75. https://doi.org/10.1207/s15327752jpa4901_13
- Diener, E., Suh, E. M., Lucas, R. E., & Smith, H. L. (1999). Subjective well-being: Three decades of progress. *Psychological Bulletin, 125*(2), 276–302. https://doi.org/10.1037/0033-2909.125.2.276
- Verification: 1985, abstract read (Europe PMC). 1999, record located only.
- What it actually establishes: The SWLS is a brief, validated measure of global life satisfaction with good internal consistency and temporal stability.
- Use in dissertation: A cheap, repeatable, comparable primary wellbeing measure. Pair it with objective indicators (health, food security, hours worked) to resist Goodhart effects.

---

## Part H. Intentional communities, company towns, closed ecosystems, land

### Abramitzky2008_Kibbutz
- Abramitzky, R. (2008). The limits of equality: Insights from the Israeli kibbutz. *The Quarterly Journal of Economics, 123*(3), 1111–1159. https://doi.org/10.1162/qjec.2008.123.3.1111
- Link: https://academic.oup.com/qje/article/123/3/1111/1928186
- Verification: abstract/publisher page read.
- What it actually establishes: The most productive members are the most likely to leave (brain drain). Collective, non-portable wealth acts as a lock-in device: wealthier kibbutzim retain members and sustain more equality. Ideology also helps. Mobility limits redistribution.
- Use in dissertation: The central caution for the exit metric. Low exit can mean lock-in rather than satisfaction. Measure who leaves (by skill) and what they can take with them.

### Abramitzky2018_Mystery
- Abramitzky, R. (2018). *The mystery of the kibbutz: Egalitarian principles in a capitalist world*. Princeton University Press.
- Link: https://press.princeton.edu/books/hardcover/9780691177533/the-mystery-of-the-kibbutz
- Verification: abstract/publisher page read.
- What it actually establishes: Equal sharing created shirking incentives and pushed skilled members to leave, yet kibbutzim thrived for much of the 20th century as enclaves within a capitalist economy, before declining.
- Use in dissertation: The best long-run precedent for an internal economy surviving inside a market economy, and for how such an economy erodes.

### Kanter1972_Commitment
- Kanter, R. M. (1972). *Commitment and community: Communes and utopias in sociological perspective*. Harvard University Press.
- Link: https://www.hup.harvard.edu/books/9780674145764
- Verification: record located only (catalog records; content from secondary summaries).
- What it actually establishes (secondary): Studies 19th-century American utopias and 1960s communes. It identifies commitment mechanisms (sacrifice, investment, renunciation, communion, mortification, transcendence) associated with community longevity.
- Use in dissertation: Several longevity mechanisms work by raising exit costs, which is the tension with the dissertation's exit condition. Read it before citing specific success rates.

### Fishback1986_CompanyStore (with Fishback 1992)
- Fishback, P. V. (1986). Did coal miners "owe their souls to the company store"? Theory and evidence from the early 1900s. *The Journal of Economic History, 46*(4), 1011–1029. https://doi.org/10.1017/S0022050700050695
- Fishback, P. V. (1992). *Soft coal, hard choices: The economic welfare of bituminous coal miners, 1890–1930*. Oxford University Press. https://academic.oup.com/book/26253 (Chapter 8, pp. 133–147, shares the 1986 article's title: https://doi.org/10.1093/acprof:oso/9780195067255.003.0008)
- Verification: 1986, abstract read. 1992, record located only.
- What it actually establishes: In nonunion coalfields, company-store prices were constrained by competing stores and by miners' mobility between mines. Prices were generally comparable to independent stores, and scrip mostly functioned as an advance on wages, not as debt bondage. Outcomes depended on local labor-market competition.
- Use in dissertation: Revises the stock "company scrip = exploitation" image the draft relies on (Ch. 1B, Ch. 3). Fishback's finding is that **exit and outside competition** disciplined the company. A **closed** pilot removes exactly those disciplines, which makes measured exit and external price benchmarks essential.

### CohenTilman1996_Biosphere2
- Cohen, J. E., & Tilman, D. (1996). Biosphere 2 and biodiversity: The lessons so far. *Science, 274*(5290), 1150–1151. https://doi.org/10.1126/science.274.5290.1150
- Link: as above
- Verification: record located only (Science returned 403).
- What it actually establishes: A short Policy Forum by ecologists advising Biosphere 2's new managers, drawing lessons from the 1991–93 closure about how hard it is to engineer a self-sustaining closed ecosystem. Specific species-loss figures commonly attributed to it were **not verified** here.
- Use in dissertation: Cite it for the general lesson only, until the text is read.

### Severinghaus1994_O2
- Severinghaus, J. P., Broecker, W. S., Dempster, W. F., MacCallum, T., & Wahlen, M. (1994). Oxygen loss in Biosphere 2. *Eos, Transactions American Geophysical Union, 75*(3), 33–37. https://doi.org/10.1029/94EO00285
- Link: as above
- Verification: abstract/publisher page read.
- What it actually establishes: Oxygen fell from about 21% to about 14% over 16 months of closure, enough to affect occupant health. The cause was soil microbial respiration of rich organic matter. The expected CO2 rise was masked because CO2 reacted with exposed concrete to form calcium carbonate.
- Use in dissertation: The canonical slow, hidden failure in a sealed self-sufficient system. It argues for independent physical monitoring and preset stop rules. The venue is **Eos, not Nature**.

### Peters2016_CarryingCapacity
- Peters, C. J., Picardy, J., Darrouzet-Nardi, A. F., Wilkins, J. L., Griffin, T. S., & Fick, G. W. (2016). Carrying capacity of U.S. agricultural land: Ten diet scenarios. *Elementa: Science of the Anthropocene, 4*, 000116. https://doi.org/10.12952/journal.elementa.000116
- Link: as above
- Verification: abstract/publisher page read.
- What it actually establishes: Land requirements ranged from about 0.13 to 1.08 ha per person per year across ten diets. Lower-meat diets generally support more people. Because grazing land is usable only by ruminants, some omnivore diets outperform the vegan diet in carrying capacity.
- Use in dissertation: Sizes the pilot's land base. A dairy-and-beef diet sits toward the upper end. As an illustrative calculation of my own, not a figure from the paper, 100 residents at about 1 ha each would need on the order of 100 ha, before adjusting for local yields.

### BarronGafford2019_Agrivoltaics
- Barron-Gafford, G. A., Pavao-Zuckerman, M. A., Minor, R. L., Sutter, L. F., Barnett-Moreno, I., Blackett, D. T., Thompson, M., Dimond, K., Gerlak, A. K., Nabhan, G. P., & Macknick, J. E. (2019). Agrivoltaics provide mutual benefits across the food–energy–water nexus in drylands. *Nature Sustainability, 2*(9), 848–855. https://doi.org/10.1038/s41893-019-0364-5
- Link: https://www.osti.gov/servlets/purl/1567040
- Verification: full text read (accepted manuscript).
- What it actually establishes: At a dryland site (at Biosphere 2, Arizona), some crops under PV panels yielded more: chiltepin about 3 times and tomato about 2 times, while jalapeño was similar with less water loss. Soil moisture was higher, and panels ran cooler, which improves efficiency.
- Use in dissertation: Supports co-locating solar and food production on scarce settlement land. Results are crop- and climate-specific, and grain and pasture were not tested.

### Ostrom2005_IAD (with Ostrom 1990; Hirschman 1970)
- Ostrom, E. (2005). *Understanding institutional diversity*. Princeton University Press.
- Ostrom, E. (1990). *Governing the commons: The evolution of institutions for collective action*. Cambridge University Press. https://doi.org/10.1017/CBO9780511807763
- Hirschman, A. O. (1970). *Exit, voice, and loyalty: Responses to decline in firms, organizations, and states*. Harvard University Press.
- Link: https://press.princeton.edu/books/paperback/9780691122380/understanding-institutional-diversity
- Verification: Ostrom 2005, abstract/publisher page read. Ostrom 1990, record located only (Crossref). Hirschman, record located only (catalog details; the publisher page was empty).
- What it actually establishes: Ostrom (2005) presents the Institutional Analysis and Development framework and design principles for durable self-governed resource institutions. The others were confirmed bibliographically only.
- Use in dissertation: IAD is a tool for describing how rules set by the AI interact with resident rules. Ostrom 1990 fills the reference-list gap flagged in VERIFICATION.md. Hirschman is the natural theory for the exit metric: exit and voice as complementary feedback.

---

## Part I. Models, fine-tuning, agent architecture, Goodhart

### Touvron2023_Llama2
- Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi, A., et al. (2023). *Llama 2: Open foundation and fine-tuned chat models* (arXiv:2307.09288). arXiv. https://doi.org/10.48550/arXiv.2307.09288 (68 authors; only the first five were confirmed. Fill in the APA 7 form, first 19 … last, from arXiv.)
- Link: https://arxiv.org/abs/2307.09288 ; license https://ai.meta.com/llama/license/
- Verification: abstract read; full-text sections 2.1, 4.1 and 5.2–5.3 read; licence page read.
- What it actually establishes: Releases 7B–70B base and chat models. Pretraining used 2 trillion tokens of "publicly available sources" that are not itemised or released. The licence is a "Community License Agreement" with an acceptable-use policy, a separate-licence requirement above 700M monthly active users, and a restriction on using outputs to improve other LLMs.
- Use in dissertation: Describe it as **open-weight under a restrictive community licence**, not "open source". The pretraining corpus is not auditable.

### Jiang2023_Mistral7B
- Jiang, A. Q., Sablayrolles, A., Mensch, A., Bamford, C., Chaplot, D. S., de las Casas, D., Bressand, F., Lengyel, G., Lample, G., Saulnier, L., Lavaud, L. R., Lachaux, M.-A., Stock, P., Le Scao, T., Lavril, T., Wang, T., Lacroix, T., & El Sayed, W. (2023). *Mistral 7B* (arXiv:2310.06825). arXiv. https://doi.org/10.48550/arXiv.2310.06825
- Link: https://arxiv.org/abs/2310.06825
- Verification: full text read.
- What it actually establishes: A 7B model, released under Apache 2.0, that the authors report outperforms Llama 2 13B on all evaluated benchmarks. The paper says nothing about pretraining data.
- Use in dissertation: A permissively licensed option, but with undocumented training data. It does not deliver the full auditability the draft claims.

### Hu2022_LoRA
- Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., & Chen, W. (2022). LoRA: Low-rank adaptation of large language models. In *International Conference on Learning Representations*. https://openreview.net/forum?id=nZeVKeeFYf9 (arXiv: https://doi.org/10.48550/arXiv.2106.09685)
- Link: https://arxiv.org/abs/2106.09685
- Verification: abstract/publisher page read.
- What it actually establishes: LoRA freezes the base weights and trains small low-rank update matrices. On GPT-3 175B this cuts trainable parameters about 10,000-fold and GPU memory about 3-fold, with quality comparable to full fine-tuning and no added inference latency.
- Use in dissertation: Makes resident-data fine-tuning feasible at settlement scale. The settlement-specific change is a small, separable, auditable and revertible adapter.

### Kapoor2024_OpenFMs
- Kapoor, S., Bommasani, R., Klyman, K., Longpre, S., Ramaswami, A., Cihon, P., Hopkins, A. K., Bankston, K., Biderman, S., Bogen, M., Chowdhury, R., Engler, A., Henderson, P., Jernite, Y., Lazar, S., Maffulli, S., Nelson, A., Pineau, J., Skowron, A., . . . Narayanan, A. (2024). Position: On the societal impact of open foundation models. In *Proceedings of the 41st International Conference on Machine Learning* (PMLR 235, pp. 23082–23104). https://proceedings.mlr.press/v235/kapoor24a.html
- Link: as above
- Verification: abstract/publisher page read.
- What it actually establishes: Defines open foundation models as models with widely available weights. It identifies properties that yield benefits (innovation, competition, distribution of decision-making power, transparency) and risks. It proposes a marginal-risk framework and finds the evidence on misuse risk currently thin.
- Use in dissertation: The main scholarly support for the open-weight choice, while noting that the authors treat transparency as conditional.

### Bommasani2023_FMTI
- Bommasani, R., Klyman, K., Longpre, S., Kapoor, S., Maslej, N., Xiong, B., Zhang, D., & Liang, P. (2023). *The Foundation Model Transparency Index* (arXiv:2310.12941). arXiv. https://doi.org/10.48550/arXiv.2310.12941
- Link: https://arxiv.org/abs/2310.12941
- Verification: full text read (results sections).
- What it actually establishes: Ten developers were scored on 100 indicators. Meta (Llama 2) was highest at 54/100, and the mean was 37. Upstream (data) transparency was weakest industry-wide, and no developer disclosed data creators or the copyright or licence status of data. Llama 2 scored 40% on data. Mistral was not assessed in v1.0.
- Use in dissertation: Evidence that open weights do not mean open data. This corrects the draft's "every input auditable" claim.

### Perdomo2020_Performative
- Perdomo, J., Zrnic, T., Mendler-Dünner, C., & Hardt, M. (2020). Performative prediction. In *Proceedings of the 37th International Conference on Machine Learning* (PMLR 119, pp. 7599–7609). https://proceedings.mlr.press/v119/perdomo20a.html
- Link: as above
- Verification: abstract/publisher page read.
- What it actually establishes: When predictions influence the outcomes they predict, the data distribution shifts. The paper defines "performative stability" and gives conditions under which repeated retraining converges.
- Use in dissertation: The settlement AI is retrained on residents whose behavior it shapes, which is a performative loop. "Trending toward wellbeing" may be convergence to a self-induced equilibrium, not real improvement.

### Manheim2018_Goodhart
- Manheim, D., & Garrabrant, S. (2018). *Categorizing variants of Goodhart's law* (arXiv:1803.04585). arXiv. https://doi.org/10.48550/arXiv.1803.04585
- Link: https://arxiv.org/abs/1803.04585
- Verification: full text read.
- What it actually establishes: Four variants: regressional, extremal, causal and adversarial. Each describes a way that optimizing a proxy diverges from the goal.
- Use in dissertation: All four apply to a "resident wellbeing" target. Adversarial Goodhart is the case where the AI or residents game the survey.

### Skalse2022_RewardHacking
- Skalse, J., Howe, N. H. R., Krasheninnikov, D., & Krueger, D. (2022). Defining and characterizing reward gaming. In *Advances in Neural Information Processing Systems 35*. https://proceedings.neurips.cc/paper_files/paper/2022/hash/3d719fee332caa23d5038b8a90e81796-Abstract-Conference.html (arXiv title: "Defining and characterizing reward hacking," https://doi.org/10.48550/arXiv.2209.13085)
- Verification: abstract/publisher page read.
- What it actually establishes: Formally defines an "unhackable" proxy. Over all stochastic policies, two reward functions can be unhackable only if one is constant. Non-trivial unhackable pairs require restricting the policy set.
- Use in dissertation: A formal argument for the narrow-agent design. Restricting each sub-agent's action space is what makes proxy rewards safer.

### Amodei2016_Concrete
- Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., & Mané, D. (2016). *Concrete problems in AI safety* (arXiv:1606.06565). arXiv. https://doi.org/10.48550/arXiv.1606.06565
- Link: https://arxiv.org/abs/1606.06565
- Verification: abstract/publisher page read.
- What it actually establishes: Five accident-risk problems: negative side effects, reward hacking, scalable oversight, safe exploration, and robustness to distributional shift.
- Use in dissertation: A checklist for the lead/sub-agent design, especially safe exploration for an AI that runs water treatment and farm machinery.

### Wu2024_AutoGen
- Wu, Q., Bansal, G., Zhang, J., Wu, Y., Li, B., Zhu, E., Jiang, L., Zhang, X., Zhang, S., Liu, J., Awadallah, A. H., White, R. W., Burger, D., & Wang, C. (2024). AutoGen: Enabling next-gen LLM applications via multi-agent conversation. In *Proceedings of the First Conference on Language Modeling (COLM)*. (arXiv:2308.08155, https://doi.org/10.48550/arXiv.2308.08155)
- Link: https://arxiv.org/abs/2308.08155
- Verification: abstract read. Venue confirmed only via a Microsoft Research page.
- What it actually establishes: An open-source framework in which configurable agents (LLM, human or tool-backed) converse to solve tasks, demonstrated across several domains.
- Use in dissertation: A working precedent for a lead agent orchestrating narrow sub-agents with humans in the loop.

### Park2023_GenerativeAgents
- Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. In *Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology (UIST '23)*. ACM. https://doi.org/10.1145/3586183.3606763
- Link: https://arxiv.org/abs/2304.03442
- Verification: abstract read (arXiv). The ACM venue was confirmed only via search results.
- What it actually establishes: LLM agents with memory, reflection and planning produced believable individual and emergent social behavior among 25 agents in a sandbox town.
- Use in dissertation: Pre-founding simulation of settlement policy is feasible. It establishes believability, not governance competence.

### Guo2024_MultiAgentSurvey
- Guo, T., Chen, X., Wang, Y., Chang, R., Pei, S., Chawla, N. V., Wiest, O., & Zhang, X. (2024). Large language model based multi-agents: A survey of progress and challenges. In *Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence (IJCAI-24)* (pp. 8048–8057). https://doi.org/10.24963/ijcai.2024/890
- Link: https://www.ijcai.org/proceedings/2024/890
- Verification: abstract/publisher page read.
- What it actually establishes: Surveys LLM multi-agent systems for problem-solving and world simulation, covering agent profiling, communication, capability growth and benchmarks.
- Use in dissertation: Field overview for the orchestration architecture and its open challenges.

### Drexler2019_CAIS
- Drexler, K. E. (2019). *Reframing superintelligence: Comprehensive AI services as general intelligence* (Technical Report #2019-1). Future of Humanity Institute, University of Oxford. https://www.futureofhumanityinstitute.org/s/2019-1.pdf
- Link: Oxford ORA https://ora.ox.ac.uk/objects/uuid:9c05427a-6390-4b42-9c55-ee45f73a26ad
- Verification: abstract/publisher page read (title page, abstract and contents).
- What it actually establishes: Proposes treating advanced AI as a set of bounded, task-focused services rather than unitary goal-directed agents, with humans retaining strategic control.
- Use in dissertation: The closest conceptual precedent for Ch. 1B's "orchestration of narrow systems, explicitly sub-AGI" argument. Cite it there.

### Shumailov2024_ModelCollapse
- Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., & Gal, Y. (2024). AI models collapse when trained on recursively generated data. *Nature, 631*, 755–759. https://doi.org/10.1038/s41586-024-07566-y
- Link: as above
- Verification: abstract read (authors' lab page). Volume and pages come from secondary records.
- What it actually establishes: Training indiscriminately on model-generated content causes irreversible loss of the original distribution's tails ("model collapse") across model types.
- Use in dissertation: A settlement model retrained on data its own outputs have shaped risks collapse. The pilot needs provenance-tagged, human-originated training data.

### Ouyang2022_RLHF
- Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L., Simens, M., Askell, A., Welinder, P., Christiano, P. F., Leike, J., & Lowe, R. (2022). Training language models to follow instructions with human feedback. In *Advances in Neural Information Processing Systems 35*. https://proceedings.neurips.cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract-Conference.html
- Verification: abstract/publisher page read.
- What it actually establishes: Fine-tuning on human demonstrations and preference rankings (RLHF) produced a 1.3B model that labelers preferred to 175B GPT-3, with better truthfulness and lower toxicity.
- Use in dissertation: The method precedent for steering the model with residents' own preference judgments. Whose rankings count then becomes a governance question.

---

## Corrections to the draft

1. **Ch. 6, organoid review citation.** The ScienceDirect source is Wadan, A.-H. S. (2025), *Brain Organoid and Systems Neuroscience Journal* 3, 8–14, doi:10.1016/j.bosn.2025.01.002. It is a single-author narrative mini-review in a new journal. Cite it by author and year, not as "ScienceDirect". Its abstract does **not** mention learning, plasticity, parallel processing or consciousness thresholds. The sentence that researchers describe learning, plasticity and parallel processing and say it is too early to conclude morally significant consciousness is **unconfirmed against this source**. The phrasing looks like a search-engine summary. Re-source it to Smirnova et al. (2023), Kagan et al. (2022, with Balcı et al. 2023), Cai et al. (2023), and NASEM (2021). NASEM does make the "extremely unlikely to be conscious in the foreseeable future" judgment.
2. **Ch. 6, Greely.** Confirmed in substance. Cite as Cerf, E. (2025, October 20), *UC Santa Cruz News*, which is a news release, not peer-reviewed. Greely poses questions about status (tissue sample, lab animal, person, something else) and donor consent and takes no position. Do not present this as a finding. Add Kataoka et al. (2024) and NASEM (2021) as the scholarly sources on donor consent.
3. **Ch. 6, "researchers describe learning"**: Current peer-reviewed evidence is modest. Robbins et al. (2026) found goal-directed learning in **mouse** cortical organoids that **did not persist** past a 45-minute rest. "Sentience" claims (Kagan 2022) are formally contested.
4. **Ch. 6, "defining the unit by information processed"**: The sources support this direction, but no published conversion between qubits or quantum volume and classical operations exists. Quantum-to-classical equivalence estimates have moved by orders of magnitude (from 10,000 years, to days, to hours). Say explicitly that pricing must be by verifiable output per task, with Landauer's bound as a physical floor only.
5. **Ch. 1B, "open-weight… keeps every input auditable"**: Overstated. Llama 2's pretraining data is undisclosed and its licence is not open source. Mistral 7B's paper discloses no data. Even the top-scoring developer on the Transparency Index scored 40% on data. Revise to: weights, the resident fine-tuning data, the adapters (LoRA) and the system's behavior are auditable; the base pretraining corpus is not. The "untestable attribution" argument against frontier models therefore applies partly to open-weight models too. A residual pre-existing alignment confound remains and needs a control, for example comparing the base model with the fine-tuned model on the same decisions.
6. **Ch. 1B / Ch. 3, company scrip framing.** The economic-history literature (Fishback 1986, 1992) finds company stores and scrip were less exploitative than the stock image *because* of miner mobility and competition. Cite Fishback, and note that a closed pilot removes those disciplines.
7. **Biosphere 2 (if cited).** Severinghaus et al. (1994) is in *Eos*, not *Nature*. Cohen & Tilman (1996) species-loss specifics remain unverified.
8. **Neuralink.** Cite only the registry record (NCT06429735). Company performance claims are not peer-reviewed.
9. **References to add per VERIFICATION.md:** Ostrom (1990), Cambridge UP, doi:10.1017/CBO9780511807763.

---

## Synthesis notes

**What a methodologically serious pilot must include.** Ch. 1B already frames its four questions as falsifiable. Popper and Nosek et al. require more: each question should be preregistered with a metric, a time horizon, and a numeric failure threshold before the first resident arrives. Exit needs more than a count of departures. Abramitzky shows that the most productive members leave first and that collective, non-portable wealth suppresses exit. Kanter's commitment mechanisms work largely by raising exit costs. The pilot should therefore record who leaves, at what skill level, and what share of their contributed value (livestock, land, labor credit, currency) they can take with them. Hirschman's pairing of exit and voice suggests also measuring how often residents' grievances change AI decisions.

"AI behavior trends toward wellbeing" is the hardest outcome to measure honestly. It requires:
- a validated subjective measure (SWLS; OECD modules) together with objective indicators;
- a comparison condition, such as a matched control site or a staggered rollout, because McCambridge et al. show that heavily observed, self-selected participants change behavior on their own;
- a base-versus-fine-tuned model comparison on identical decision sets, to separate the effect of settlement data from alignment done before the pilot.

Perdomo et al. warn that a model retrained on people it influences converges to a self-induced equilibrium. Manheim and Garrabrant, and Skalse et al., show that any wellbeing proxy will be gamed under optimization pressure. Shumailov et al. add that recursive self-training degrades the model. The pilot therefore needs provenance-tagged human data, held-out wellbeing measures the AI never optimizes, and independent auditors. Fishback's results indicate that currency value should be benchmarked against outside prices for comparable goods, even in a closed economy, or "real exchange value" cannot be distinguished from administered prices. Ethically, Belmont, the Common Rule and Emanuel et al. require independent review, voluntariness free of undue influence, and withdrawal without loss of entitled benefits. An AI controlling food, water and power is an authority able to impose sanctions, so external stop rules and a guaranteed exit package belong in the protocol before founding.

**Strongest cautionary precedents.** Biosphere 2 is the clearest. A sealed, self-sufficient system lost a third of its oxygen through a process no one had modeled (soil respiration, with concrete masking the CO2 signal), and the occupants' health suffered before anyone understood the cause. The lesson for a "zero external dependency" settlement is independent physical monitoring and preset abort criteria. The kibbutz is the best long-run analogue: an internal egalitarian economy that thrived for decades inside a capitalist one, then lost skilled members and privatized. Company towns show that scrip is only as fair as the exit options around it. Peters et al. put a hard number on the agrarian design: a dairy-and-beef diet sits near the high end of land per person, so self-sufficiency fixes a minimum land base and caps the population. Agrivoltaics (Barron-Gafford et al.) helps on solar and water but was tested on dryland vegetables, not grain or pasture.

**How the convergence literature reshapes consent, reciprocity and exit.** Ch. 6 is right that the human-machine boundary is eroding, but the evidence asks for more calibrated claims. On consent, the organoid literature has already reached the dissertation's question. Kataoka et al. argue that donors cannot give fully informed consent while organoid consciousness is uncertain, and propose project-specific rather than broad consent. Smirnova et al. ask whether donor rights continue after donation. NASEM and ISSCR leave donor consent unresolved and place organoid work in minimal-oversight categories. The dissertation can contribute by turning "consent" into continuing, revocable participation with a share in downstream value, which is reciprocity.

On moral status, Birch's sentience-candidate framework and Long, Sebo et al. offer a precautionary path that does not depend on settling consciousness science. Butlin et al. show that consciousness-relevant properties are architectural, so the compute currency cannot double as a moral-status meter. Exit becomes concrete in BCIs. Card et al.'s participant relied on his device daily for months, and Metzger et al. rebuilt a participant's voice and face. Leaving such a system means device removal, model deletion and ownership of a voice model, which matches the mental-integrity and psychological-continuity rights in Ienca and Andorno. Chile's constitution, Colorado, California and UNESCO (2025) now protect neural data. All of them frame it as a person's sensitive data, not as tissue participating in the computation, so Ch. 6's "tissue as party" extension addresses a real gap.
