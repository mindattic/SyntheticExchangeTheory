# Research note 02: Model collapse, synthetic data, data scarcity, embodied data, feedback loops

Prepared 2026-10-08 for *Synthetic Exchange Theory* (Ch. 1 grounding assumption, Ch. 2 "empirical anchor", Ch. 5 limitation 1).

**How to read the verification levels**
- **Full text read**: the paper's text (publisher PDF, repository copy of the published version, or arXiv full text) was opened and the cited passages were checked. Long pages were read in part, and that is noted where it applies.
- **Abstract/publisher page read**: the abstract, or the publisher, proceedings or arXiv landing page, was opened. The body was not read.
- **Record located only**: search results confirmed title, authors, venue and year, but no page was opened, or the opened page showed only metadata.

**DOI convention.** ICLR, ICML (PMLR), NeurIPS and COLM do not issue DOIs. For those papers the arXiv DOI (10.48550/arXiv.NNNN) is given alongside the proceedings link. Where no DOI exists, this note says so. A DOI written as `10.48550/arXiv.x` is built from the arXiv ID, which was checked. The DOI string itself was not resolved separately.

**Search budget.** The session's web-search quota ran out partway through this work. Sources added after that point (Feng 2024, Schaeffer 2025, Kazdan 2024, Gillman, Seddik, Guo, Hataya, DROID, Lin, RLAIF, STaR, Hardt & Mendler-Dünner, Zhao, Longpre) were checked by opening their arXiv pages directly. For several of them, a later peer-reviewed venue may exist that I could not confirm. Each entry says so.

---

## A. Model collapse: core and draft-cited sources

### Jangjoo2026
- **APA:** Jangjoo, F., di Sarra, G., Marsili, M., & Roudi, Y. (2026). Lost in retraining: Closed-loop learning and model collapse in exponential families. *Physical Review Letters, 136*(19), Article 197301. https://doi.org/10.1103/156q-3ngc
- **Link:** https://journals.aps.org/prl/abstract/10.1103/156q-3ngc. Preprint (with a different subtitle, "Roaming the parameter space of exponential families under closed-loop learning", and without di Sarra): https://arxiv.org/abs/2506.20623
- **Verification:** Publisher abstract page read (authors, volume, article number, dates: received 6 Apr 2025, accepted 24 Mar 2026, published 14 May 2026). Full text of the arXiv v2 preprint read. The PRL version of record was not read in full.
- **What it actually establishes:** The paper analyzes exponential-family models (an Ising model, a REM-like model with one parameter per configuration, and a Poisson model) that are re-fit at each generation to M samples drawn from the previous fit. Under pure maximum likelihood, the sufficient statistics are martingales. The process therefore ends in absorbing states, such as a fully polarized Ising model, that amplify whatever bias the initial sample had. A configuration that drops out of the sample never returns. Collapse can be avoided when each generation's data includes m ≥ 1 points from the ground truth, combined with MAP estimation or regularization. The stationary density depends jointly on m and on the prior or regularizer strength. The preprint says one outside point "may be sufficient" and shows this for specific examples (Poisson with m = 1 and M = 200; Ising with m = 1, N = 10 and M = 50). It does not prove that one point is always enough. The result depends on the model. For Poisson, a prior with no real data (m = 0) does not prevent collapse. For Ising, Gaussian priors alone did prevent it in simulation. Avoiding collapse does not mean recovering the truth: the process settles into a non-degenerate distribution that keeps fluctuating, and under a prior it is biased toward the prior.
- **Use in dissertation:** Supports the claim that purely self-referential retraining degenerates, even in the simplest statistical models. It also supports the "small trickle" counterpoint, but only in low-dimensional models, and the trickle is a ratio (for example, 1 real point per 200 synthetic per generation), not an absolute amount. See Corrections 1 and 2.

### Dohmatob2025Strong
- **APA:** Dohmatob, E., Feng, Y., Subramonian, A., & Kempe, J. (2025). Strong model collapse. In *Proceedings of the Thirteenth International Conference on Learning Representations (ICLR 2025)*. https://proceedings.iclr.cc/paper_files/paper/2025/hash/284afdc2309f9667d2d4fb9290235b0c-Abstract-Conference.html (no DOI; arXiv: https://doi.org/10.48550/arXiv.2410.04840)
- **Link:** https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf
- **Verification:** Full text read in part (abstract, introduction and main-contributions section of the ICLR camera-ready PDF).
- **What it actually establishes:** The setting is supervised linear regression, plus random-projection models as a stand-in for neural networks. Training uses a single mix of real data and "synthetic" data, which the paper defines as data from any distribution that deviates from the test distribution. The total amount of data grows without bound. Collapse here means a scaling plateau: if the synthetic fraction does not shrink to zero, adding more data stops improving test error, and the abstract says this holds even at about 1 synthetic example per 1,000. Larger models can amplify collapse, although beyond the interpolation threshold they may reduce it without preventing it. Simple reweighting of the data does not fix it. Iterative mixing strategies can mitigate it, but only with a supply of real data that grows at least as fast as the synthetic data. (The arXiv v2 abstract says "1%"; the ICLR camera-ready says "1 per 1000". Cite the ICLR wording.)
- **Use in dissertation:** This is the strongest formal support for a *continuing, proportional* need for real data. It directly counters the reading that a fixed small trickle suffices, because the real-data supply has to keep pace with synthetic volume. The limitation is that it is a theory of regression and random features, with confirming experiments rather than frontier-scale tests.

### Shumailov2024
- **APA:** Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., & Gal, Y. (2024). AI models collapse when trained on recursively generated data. *Nature, 631*(8022), 755–759. https://doi.org/10.1038/s41586-024-07566-y
- **Link:** https://www.nature.com/articles/s41586-024-07566-y (open copy: https://www.pure.ed.ac.uk/ws/portalfiles/portal/460496122/ShumailovEtalNature2024AIModelsCollapseWhen.pdf)
- **Verification:** Full text read (University of Edinburgh repository copy of the published Nature article).
- **What it actually establishes:** The paper defines *early* model collapse, in which a model loses the tails of the distribution, and *late* collapse, in which it converges to something that bears little resemblance to the original, with much reduced variance. It shows both theoretically (Gaussian models, Gaussian mixtures, VAEs) and empirically by fine-tuning OPT-125m on wikitext2 over generations. Real-data fine-tuning reaches a mean perplexity of 34 (from a zero-shot 115). With no original data kept, perplexity worsened by about 20–28 points. Keeping a random 10% of the original data at each generation led to "only minor degradation". The authors note that learning from generated data is possible and that whether and how fast complete collapse happens depends on the problem. They conclude that sustained learning requires preserving access to original data and to data not generated by LLMs, and they raise provenance as a coordination problem.
- **Use in dissertation:** This is the canonical citation for "loses tails and variance". It should be cited together with its own qualifier: retaining even 10% real data largely contains the damage. The setting is a replacement regime at small scale.

### Alemohammad2024
- **APA:** Alemohammad, S., Casco-Rodriguez, J., Luzi, L., Humayun, A. I., Babaei, H., LeJeune, D., Siahkoohi, A., & Baraniuk, R. G. (2024). Self-consuming generative models go MAD. In *Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)*. https://proceedings.iclr.cc/paper_files/paper/2024/hash/ebc042e767de551803ccfcc45e2454f5-Abstract-Conference.html (no DOI; arXiv: https://doi.org/10.48550/arXiv.2307.01850)
- **Link:** https://openreview.net/pdf?id=ShjMHfmPs0
- **Verification:** Full text read (arXiv HTML; the first ~100k of ~121k characters) and ICLR abstract page read.
- **What it actually establishes:** The paper compares three self-consuming loops in image generative models. In the *fully synthetic* loop, both quality (precision) and diversity (recall) decline. Biased sampling can preserve precision, but only by losing recall faster. In the *synthetic augmentation* loop, a fixed real dataset is kept and synthetic data added. This only *delays* degradation. In the *fresh data* loop, new real data enters every generation. Performance then converges to a level set by the real and synthetic sample sizes. A modest amount of synthetic data can help, and too much hurts. The headline conclusion is that without enough *fresh* real data each generation, quality or diversity declines ("Model Autophagy Disorder").
- **Use in dissertation:** Directly supports the "fresh human data" framing, specifically *fresh* rather than a stored corpus. It conflicts with Gerstgrasser et al. on whether a fixed real set is enough. The difference comes from the setups: Alemohammad et al. use a fixed per-generation training budget, while Gerstgrasser et al. let all data accumulate.

### Gerstgrasser2024
- **APA:** Gerstgrasser, M., Schaeffer, R., Dey, A., Rafailov, R., Korbak, T., Sleight, H., Agrawal, R., Hughes, J., Pai, D. B., Gromov, A., Roberts, D., Yang, D., Donoho, D. L., & Koyejo, S. (2024). Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data. *First Conference on Language Modeling (COLM 2024)*. https://doi.org/10.48550/arXiv.2404.01413
- **Link:** https://arxiv.org/abs/2404.01413
- **Verification:** arXiv abstract page read. The COLM 2024 venue was located through an OpenReview-derived index, and an ICML 2024 DMLR workshop poster page was read. The COLM proceedings page was not opened.
- **What it actually establishes:** Prior collapse results assume each generation's synthetic data *replaces* the earlier data. When synthetic data *accumulates* alongside the original real data, test error in a linear-model framework has a finite upper bound that does not depend on the number of iterations. Under replacement, error grows with iterations. Experiments with language-model pretraining, molecular-conformation diffusion models and image VAEs show the same pattern: replacement degrades, accumulation does not.
- **Use in dissertation:** This is major counterevidence to a strong grounding assumption. If the original human corpus is kept and nothing is thrown away, collapse may not happen even with no *new* human data. This is the main reason to reformulate the assumption (see Synthesis).

### Bertrand2024
- **APA:** Bertrand, Q., Bose, A. J., Duplessis, A., Jiralerspong, M., & Gidel, G. (2024). On the stability of iterative retraining of generative models on their own data. In *Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)*. https://doi.org/10.48550/arXiv.2310.00429 (no proceedings DOI)
- **Link:** https://arxiv.org/abs/2310.00429. ICLR spotlight: https://iclr.cc/virtual/2024/poster/18942
- **Verification:** arXiv abstract page read. The ICLR listing was located through search.
- **What it actually establishes:** The paper proves that iterative retraining on a mix of real and self-generated data is stable under two conditions: the initial model approximates the data distribution well enough, and the share of clean real data is large enough. Experiments use normalizing flows and diffusion models (DDPM, EDM) on CIFAR-10 and FFHQ. The authors note that their sufficient condition may not be necessary.
- **Use in dissertation:** Supports a "real-data proportion" version of the assumption. Stability depends on a sufficient real fraction, not on avoiding synthetic data altogether.

### Dohmatob2024Tails
- **APA:** Dohmatob, E., Feng, Y., Yang, P., Charton, F., & Kempe, J. (2024). A tale of tails: Model collapse as a change of scaling laws. In *Proceedings of the 41st International Conference on Machine Learning* (PMLR Vol. 235, pp. 11165–11197). https://proceedings.mlr.press/v235/dohmatob24b.html (no DOI; arXiv: https://doi.org/10.48550/arXiv.2402.07043)
- **Link:** https://proceedings.mlr.press/v235/dohmatob24b.html
- **Verification:** PMLR abstract page read.
- **What it actually establishes:** The paper recasts model collapse as a change in neural scaling laws when synthetic data, which has truncated tails, enters the corpus. It identifies loss of scaling (more data or compute stops helping), shifted scaling across generations, "un-learning" of skills, and grokking when human and synthetic data are mixed. Experiments use a transformer on an arithmetic task and Llama2 text generation.
- **Use in dissertation:** Ties the tail-loss mechanism to the economics of scaling. Synthetic data costs future returns to scale, which complements Dohmatob et al. (2025).

### Kazdan2024
- **APA:** Kazdan, J., Schaeffer, R., Dey, A., Gerstgrasser, M., Rafailov, R., Donoho, D. L., & Koyejo, S. (2024). *Collapse or thrive? Perils and promises of synthetic data in a self-generating world* [Preprint; NeurIPS 2024 workshops M3L and ATTRIB]. arXiv. https://doi.org/10.48550/arXiv.2410.16713
- **Link:** https://arxiv.org/abs/2410.16713
- **Verification:** arXiv abstract page read. This is a workshop paper, and no archival peer-reviewed version was confirmed.
- **What it actually establishes:** The study compares three regimes across Gaussian estimation, kernel density estimation and language-model fine-tuning. *Replace* collapses in every setting studied. *Accumulate* stays stable even though the real-data share falls toward zero. *Accumulate-subsample* (a fixed compute budget per generation) degrades gradually rather than catastrophically.
- **Use in dissertation:** Reconciles the Alemohammad and Gerstgrasser results. Under realistic fixed training budgets, a pool dominated by synthetic data degrades slowly. That leaves continued value in real data, but not a cliff.

### Schaeffer2025
- **APA:** Schaeffer, R., Kazdan, J., Arulandu, A. C., & Koyejo, S. (2025). *Position: Model collapse does not mean what you think* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2503.03150
- **Link:** https://arxiv.org/abs/2503.03150
- **Verification:** arXiv abstract page read. This is a preprint, and acceptance at a 2025 venue was not confirmed.
- **What it actually establishes:** The paper finds eight distinct and partly conflicting definitions of "model collapse" in the literature. After weighting studies by how closely their assumptions match real-world practice, it argues that several prominent collapse scenarios are readily avoidable, and that collapse has been oversold relative to more specific, likely harms.
- **Use in dissertation:** Essential counterweight. The dissertation must name which definition of collapse it relies on. Section 05 should acknowledge this critique explicitly.

### Feng2024Verification
- **APA:** Feng, Y., Dohmatob, E., Yang, P., Charton, F., & Kempe, J. (2024). *Beyond model collapse: Scaling up with synthesized data requires verification* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2406.07515
- **Link:** https://arxiv.org/abs/2406.07515
- **Verification:** arXiv abstract page read. The page lists no venue. (I believe a version appeared at ICLR 2025, but I could not verify this, so do not cite that venue until checked.)
- **What it actually establishes:** Theory for Gaussian mixtures with linear classifiers and verifiers gives conditions under which a verifier can select synthetic data good enough for optimal performance. Two tasks collapse when trained on unfiltered generated data: matrix eigenvalue computation with transformers, and news summarization with LLMs. Verification, even imperfect verification, prevents that collapse.
- **Use in dissertation:** Moves the locus of dependence. What models need is an external *verification signal*, not necessarily new human-generated content. Humans are one source of verification. Compilers, proofs, simulators and rules are others.

### Gillman2024
- **APA:** Gillman, N., Freeman, M., Aggarwal, D., Hsu, C.-H., Luo, C., Tian, Y., & Sun, C. (2024). Self-correcting self-consuming loops for generative model training. In *Proceedings of the 41st International Conference on Machine Learning* (PMLR Vol. 235). https://doi.org/10.48550/arXiv.2402.07087
- **Link:** https://arxiv.org/abs/2402.07087
- **Verification:** arXiv abstract page read. The arXiv page states ICML 2024 camera-ready; PMLR page numbers were not checked.
- **What it actually establishes:** An idealized correction function that moves samples toward higher likelihood under the true distribution makes self-consuming loops exponentially more stable. In practice, the authors approximate this with expert knowledge, such as physics laws in a simulator. For human-motion synthesis, collapse is avoided even when the synthetic-to-real ratio reaches 100%.
- **Use in dissertation:** Counterevidence. Encoded domain knowledge (physics) can substitute for fresh real data. This is relevant to embodied AI.

### Seddik2024
- **APA:** Seddik, M. E. A., Chen, S.-W., Hayou, S., Youssef, P., & Debbah, M. (2024). *How bad is training on synthetic data? A statistical analysis of language model collapse* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2404.05090
- **Link:** https://arxiv.org/abs/2404.05090
- **Verification:** arXiv abstract page read. The page lists no venue, and peer-reviewed status was not confirmed.
- **What it actually establishes:** For a statistical language model, collapse cannot be avoided when training solely on synthetic data. Mixing real and synthetic data can avoid it, and the authors estimate the maximum synthetic proportion that still avoids collapse.
- **Use in dissertation:** Supports a threshold/proportion formulation. Use it as secondary support only, given its preprint status.

### Guo2024Diversity
- **APA:** Guo, Y., Shang, G., Vazirgiannis, M., & Clavel, C. (2024). The curious decline of linguistic diversity: Training language models on synthetic text. In *Findings of the Association for Computational Linguistics: NAACL 2024*. https://doi.org/10.48550/arXiv.2311.09807 (ACL Anthology DOI not retrieved)
- **Link:** https://arxiv.org/abs/2311.09807
- **Verification:** arXiv abstract page read. The NAACL 2024 Findings acceptance is stated on the arXiv page; the ACL Anthology record was not opened.
- **What it actually establishes:** In recursive fine-tuning on English generation tasks, lexical, syntactic and semantic diversity of outputs decreases consistently across generations. The drop is largest on tasks that require high creativity.
- **Use in dissertation:** Empirical support for the "lose variance" mechanism in language specifically. It also points to *creative/expressive* human text as the scarcest input.

### Hataya2023
- **APA:** Hataya, R., Bao, H., & Arai, H. (2023). Will large-scale generative models corrupt future datasets? In *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV 2023)*. https://doi.org/10.48550/arXiv.2211.08095 (IEEE/CVF DOI not retrieved)
- **Link:** https://arxiv.org/abs/2211.08095
- **Verification:** arXiv abstract page read. The ICCV 2023 acceptance comes from the arXiv comments field.
- **What it actually establishes:** The authors build ImageNet-scale and COCO-scale datasets contaminated with text-to-image outputs. Training on them degrades downstream performance, with severity depending on the task and on the share of generated images.
- **Use in dissertation:** Supports the claim that web-scraped corpora contaminated by AI output are less valuable. This is the dataset-level, single-step version of the problem.

---

## B. Data scarcity and scaling

### Villalobos2024
- **APA:** Villalobos, P., Ho, A., Sevilla, J., Besiroglu, T., Heim, L., & Hobbhahn, M. (2024). Position: Will we run out of data? Limits of LLM scaling based on human-generated data. In *Proceedings of the 41st International Conference on Machine Learning* (PMLR Vol. 235, pp. 49523–49544). https://proceedings.mlr.press/v235/villalobos24a.html (no DOI; arXiv: https://doi.org/10.48550/arXiv.2211.04325)
- **Link:** https://proceedings.mlr.press/v235/villalobos24a.html
- **Verification:** PMLR abstract page read. arXiv full text read in part (~100k of 128k characters).
- **What it actually establishes:** Epoch's own summary puts the effective stock of quality-adjusted public human text at about 300 trillion tokens (90% CI 100T–1,000T), allowing for multi-epoch training. If current trends continue, frontier training sets will match that stock between 2026 and 2032, with a median around 2028, and earlier if models are overtrained. The paper names synthetic data, transfer from data-rich domains and data-efficiency gains as ways out. It notes that synthetic data has worked best where outputs can be verified (math, code, games) and cites collapse risk elsewhere.
- **Use in dissertation:** Establishes the scarcity of *public human text* as a near-term binding constraint, which is the economic premise for valuing fresh human data. It also concedes the verifiable-domain exception.

### Kaplan2020
- **APA:** Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., Gray, S., Radford, A., Wu, J., & Amodei, D. (2020). *Scaling laws for neural language models* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2001.08361
- **Link:** https://arxiv.org/abs/2001.08361
- **Verification:** arXiv abstract page read.
- **What it actually establishes:** Language-model loss follows power laws in model size, dataset size and compute, with some trends spanning more than seven orders of magnitude. Architecture details matter little. Larger models are more sample-efficient, so compute-optimal training (by this paper's estimates) uses very large models on modest data and stops well before convergence.
- **Use in dissertation:** The background claim that data is one of three scaling inputs. Note that Kaplan's data-light prescription was revised by Hoffmann et al.

### Hoffmann2022
- **APA:** Hoffmann, J., Borgeaud, S., Mensch, A., Buchatskaya, E., Cai, T., Rutherford, E., de Las Casas, D., Hendricks, L. A., Welbl, J., Clark, A., Hennigan, T., Noland, E., Millican, K., van den Driessche, G., Damoc, B., Guy, A., Osindero, S., Simonyan, K., Elsen, E., … Sifre, L. (2022). An empirical analysis of compute-optimal large language model training. In *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)*. https://doi.org/10.48550/arXiv.2203.15556 (arXiv title: "Training compute-optimal large language models")
- **Link:** https://neurips.cc/virtual/2022/poster/53031
- **Verification:** NeurIPS poster page read (title and full author list). The findings come from search-result abstracts and DeepMind's summary, and the paper body was not opened.
- **What it actually establishes:** From more than 400 trained models, the paper concludes that parameters and training tokens should scale in equal proportion: each doubling of model size should come with a doubling of tokens. Chinchilla (70B parameters, 4× Gopher's data, same compute) outperforms Gopher (280B), GPT-3 (175B) and MT-NLG (530B).
- **Use in dissertation:** Shows that optimal scaling is *data-hungry*. Combined with Villalobos et al., this is the core of the scarcity argument.

### Muennighoff2023
- **APA:** Muennighoff, N., Rush, A. M., Barak, B., Le Scao, T., Piktus, A., Tazi, N., Pyysalo, S., Wolf, T., & Raffel, C. (2023). Scaling data-constrained language models. In *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*. https://doi.org/10.48550/arXiv.2305.16264
- **Link:** https://proceedings.neurips.cc/paper_files/paper/2023/hash/9d89448b63ce1e2e8dc7af72c984c196-Abstract.html
- **Verification:** Record located. The abstract content comes from search results. The full author list is from memory and was **not** checked against the page, so confirm it before submission.
- **What it actually establishes:** Across up to 900B tokens and 9B parameters, repeating data for up to about 4 epochs costs almost nothing in loss compared with unique data. Beyond that, the value of extra compute decays toward zero. The paper proposes a data-constrained scaling law, and finds that adding code data or relaxing filters helps offset scarcity.
- **Use in dissertation:** Complicates scarcity arguments. The existing stock can be reused about 4× before returns fall, which buys time but does not remove the constraint.

### Sevilla2022
- **APA:** Sevilla, J., Heim, L., Ho, A., Besiroglu, T., Hobbhahn, M., & Villalobos, P. (2022). Compute trends across three eras of machine learning. In *2022 International Joint Conference on Neural Networks (IJCNN)* (pp. 1–8). IEEE. https://doi.org/10.1109/IJCNN55064.2022.9891914
- **Link:** https://arxiv.org/abs/2202.05924
- **Verification:** arXiv abstract page read. The DOI comes from the arXiv "related DOI" field (via search).
- **What it actually establishes:** Training compute doubled about every 20 months before about 2010, and about every 6 months in the deep-learning era. A separate "large-scale" trend starting in late 2015 sits 10–100× higher in compute.
- **Use in dissertation:** Epoch's compute-trend data shows compute growing much faster than the human text stock (contrast with Villalobos et al.). That widening gap is the scarcity mechanism. The large-scale era's doubling time was not in the abstract, so do not cite a figure for it without checking the paper.

### Longpre2024
- **APA:** Longpre, S., Mahari, R., Lee, A., Lund, C., Oderinwale, H., Brannon, W., et al. (2024). *Consent in crisis: The rapid decline of the AI data commons* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2407.14933
- **Link:** https://arxiv.org/abs/2407.14933
- **Verification:** arXiv abstract page read. The page lists no venue. (I believe it appeared in the NeurIPS 2024 Datasets & Benchmarks track, but this was not verified.)
- **What it actually establishes:** Over 2023–2024, about 5% or more of all C4 tokens, and 28% or more of the most actively maintained critical C4 sources, became fully restricted through robots.txt. Terms of service restrict crawling for 45% of C4.
- **Use in dissertation:** Strong bridge to the consent chapters. Human data is becoming scarce *because people and publishers withhold consent*, not only because the stock runs out. This is direct evidence for the exchange framing.

---

## C. Counterevidence: synthetic and self-generated data that works

### Gunasekar2023
- **APA:** Gunasekar, S., Zhang, Y., Aneja, J., Mendes, C. C. T., Del Giorno, A., Gopi, S., et al. (2023). *Textbooks are all you need* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2306.11644
- **Link:** https://arxiv.org/abs/2306.11644
- **Verification:** arXiv abstract page read. This is a preprint and not peer-reviewed.
- **What it actually establishes:** phi-1 (1.3B parameters, 4 days on 8 A100s) was trained on about 6B tokens of filtered "textbook quality" web data plus about 1B tokens of GPT-3.5-generated textbooks and exercises. It reaches 50.6% pass@1 on HumanEval and 55.5% on MBPP. A 350M variant reaches 45% on HumanEval.
- **Use in dissertation:** Counterevidence that curated synthetic data can be highly efficient. However, the synthetic data came from a model trained on human data, and the corpus was still mostly filtered human web text. It is distillation, not independence.

### Silver2018
- **APA:** Silver, D., Hubert, T., Schrittwieser, J., Antonoglou, I., Lai, M., Guez, A., Lanctot, M., Sifre, L., Kumaran, D., Graepel, T., Lillicrap, T., Simonyan, K., & Hassabis, D. (2018). A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play. *Science, 362*(6419), 1140–1144. https://doi.org/10.1126/science.aar6404
- **Link:** https://doi.org/10.1126/science.aar6404 (accepted manuscript: https://discovery.ucl.ac.uk/id/eprint/10069050/)
- **Verification:** Record located only (DOI, volume and pages confirmed across several bibliographic records). The paper was not opened.
- **What it actually establishes:** AlphaZero learns chess, shogi and Go from random play, given only the rules, through self-play. It defeats world-champion programs in each game, with no human game data.
- **Use in dissertation:** The cleanest counterexample. Where a perfect simulator and an objective reward exist, self-generated data drives superhuman performance with no human data. The grounding assumption must exclude such closed, verifiable domains.

### DeepSeekAI2025
- **APA:** Guo, D., Yang, D., Zhang, H., et al. (2025). DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning. *Nature, 645*, 633–638. https://doi.org/10.1038/s41586-025-09422-z
- **Link:** https://doi.org/10.1038/s41586-025-09422-z (preprint: https://arxiv.org/abs/2501.12948)
- **Verification:** Nature record located (DOI, volume, pages and online date of 17 Sep 2025, via search). arXiv full text read in part (~100k of 142k characters). The Nature version was not opened.
- **What it actually establishes:** Reasoning ability (R1-Zero) emerges from pure RL with rule-based, verifiable rewards on math, code and STEM, without human-labeled reasoning traces. Nature's press release reports 77.9% (R1-Zero) and 79.8% (R1) on a math benchmark. The final R1, however, still uses "thousands" of cold-start examples that human annotators rewrote and verified, non-reasoning SFT data, and a helpfulness reward model trained on 66,000 preference pairs labeled by DeepSeek-V3 rather than by humans. All of this sits on a base model pretrained on 14.8T tokens. The authors say that for non-verifiable tasks, model-based rewards invite reward hacking and that scaling pure RL there remains an open problem.
- **Use in dissertation:** Strongest current counterevidence. Human *labeling* of reasoning is replaceable where answers can be checked automatically. It also supports a narrower assumption: dependence persists for pretraining corpora and for non-verifiable domains such as writing, values and open-ended helpfulness.

### Zelikman2022
- **APA:** Zelikman, E., Wu, Y., Mu, J., & Goodman, N. D. (2022). *STaR: Bootstrapping reasoning with reasoning* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2203.14465
- **Link:** https://arxiv.org/abs/2203.14465
- **Verification:** arXiv abstract page read. The arXiv page lists no venue. (I believe it appeared at NeurIPS 2022, but this was not verified.)
- **What it actually establishes:** A model generates rationales, keeps only those that lead to correct answers, and fine-tunes on them repeatedly. On CommonsenseQA it matches a model about 30× larger that was fine-tuned on answers directly.
- **Use in dissertation:** A small-scale precursor showing that self-generated data plus a correctness filter improves models. The filter, a ground-truth answer key, is the outside signal.

### Lee2024RLAIF
- **APA:** Lee, H., Phatale, S., Mansoor, H., Mesnard, T., Ferret, J., Lu, K., Bishop, C., Hall, E., Carbune, V., Rastogi, A., & Prakash, S. (2024). RLAIF vs. RLHF: Scaling reinforcement learning from human feedback with AI feedback. In *Proceedings of the 41st International Conference on Machine Learning* (PMLR Vol. 235, pp. 26874–26901). https://doi.org/10.48550/arXiv.2309.00267
- **Link:** https://arxiv.org/abs/2309.00267
- **Verification:** arXiv abstract page read (the journal reference gives the PMLR pages).
- **What it actually establishes:** Preference labels from an off-the-shelf LLM give performance comparable to human-preference RLHF on summarization, helpful dialogue and harmless dialogue.
- **Use in dissertation:** Complicates the "human preference data is irreplaceable" claim. The AI labeler was itself trained on human data, so this is substitution by distilled human judgment.

---

## D. Human feedback dependence

### Ouyang2022
- **APA:** Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L., Simens, M., Askell, A., Welinder, P., Christiano, P., Leike, J., & Lowe, R. (2022). Training language models to follow instructions with human feedback. In *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)*. https://doi.org/10.48550/arXiv.2203.02155
- **Link:** https://neurips.cc/virtual/2022/poster/52886
- **Verification:** Record located only. The abstract content was seen in search results, and the page was not opened. The author list is from memory and must be checked.
- **What it actually establishes:** The pipeline has three stages: labeler-written demonstrations for supervised fine-tuning, labeler rankings to train a reward model, and PPO against that reward. In human evaluation, outputs of the 1.3B InstructGPT were preferred over those of the 175B GPT-3, with better truthfulness and less toxicity.
- **Use in dissertation:** Shows that human preference data bought roughly a 100× parameter-efficiency gain in perceived quality. This is concrete evidence of the value of human judgment.

### Christiano2017
- **APA:** Christiano, P. F., Leike, J., Brown, T., Martic, M., Legg, S., & Amodei, D. (2017). Deep reinforcement learning from human preferences. In *Advances in Neural Information Processing Systems 30 (NIPS 2017)*. https://doi.org/10.48550/arXiv.1706.03741
- **Link:** https://proceedings.neurips.cc/paper/2017/file/d5e2c0adad503c91f91df240d0cd4e49-Paper.pdf
- **Verification:** Record located only. The abstract wording was seen in search results, and the PDF was not opened.
- **What it actually establishes:** Human comparisons of trajectory-segment pairs can replace a hand-specified reward. Atari and simulated locomotion tasks were solved with feedback on less than 1% of agent interactions (the proceedings wording), and novel behaviors were trained with about an hour of human time.
- **Use in dissertation:** Origin of RLHF. It also shows that the *quantity* of human input needed can be very small relative to machine-generated experience, which supports the "small but essential" version of dependence.

---

## E. Embodied data, world models, sim-to-real (replacements for the DEV Community post)

### OXE2024
- **APA:** Open X-Embodiment Collaboration. (2024). Open X-Embodiment: Robotic learning datasets and RT-X models. In *2024 IEEE International Conference on Robotics and Automation (ICRA)* (pp. 6892–6903). IEEE. https://doi.org/10.1109/ICRA57147.2024.10611477
- **Link:** https://ieeexplore.ieee.org/document/10611477
- **Verification:** Record located only (institutional publication records from MPI-IS and UT Austin RPL, via search). The DOI appeared in one record, and another record left the DOI field empty, so confirm it on IEEE Xplore.
- **What it actually establishes:** The paper pools robot data from 22 robot types across 21 institutions, covering 527 skills (160,266 tasks). A high-capacity model trained on the pooled data (RT-X) shows positive transfer across robots. The paper's premise is that robot learning has been fragmented into small per-robot, per-task datasets.
- **Use in dissertation:** Peer-reviewed evidence that robot data is scarce and fragmented, and that pooling helps. It replaces the DEV post's general claim, though not its "95%" figure.

### Firoozi2025
- **APA:** Firoozi, R., Tucker, J., Tian, S., Majumdar, A., Sun, J., Liu, W., Zhu, Y., Song, S., Kapoor, A., Hausman, K., Ichter, B., Driess, D., Wu, J., Lu, C., & Schwager, M. (2025). Foundation models in robotics: Applications, challenges, and the future. *The International Journal of Robotics Research, 44*(5), 701–739. https://doi.org/10.1177/02783649241281508
- **Link:** https://depositonce.tu-berlin.de/items/09f86aa1-4ee0-41e1-80d4-7b6ec6ec896f/full
- **Verification:** Repository metadata page read (DOI, volume, issue, pages, authors). The abstract content comes from search results. The paper was published online in 2024 and in an issue in 2025.
- **What it actually establishes:** This survey covers foundation models for robot perception, decision-making and control. It contrasts small task-specific robot datasets with internet-scale pretraining, and names scarcity of robot-relevant training data as a major open challenge, alongside safety guarantees, uncertainty quantification and real-time execution.
- **Use in dissertation:** Authoritative, peer-reviewed replacement for the "robotics data gap" claim.

### Khazatsky2024DROID
- **APA:** Khazatsky, A., Pertsch, K., Nair, S., Balakrishna, A., et al. (2024). *DROID: A large-scale in-the-wild robot manipulation dataset* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2403.12945
- **Link:** https://arxiv.org/abs/2403.12945
- **Verification:** arXiv abstract page read. The page lists no venue. (I believe it appeared at RSS 2024, but this was not verified.)
- **What it actually establishes:** 50 human collectors gathered 76k teleoperated demonstration trajectories, about 350 hours, across 564 scenes over 12 months on three continents.
- **Use in dissertation:** Quantifies the scale gap. One of the largest real-robot datasets is hundreds of hours, compared with about 10^14 text tokens. It also shows that real robot data today is largely *human-generated labor* (teleoperation), which cuts against Ch. 5's suggestion that robot data is "not human-generated".

### Lin2024RobotScaling
- **APA:** Lin, F., Hu, Y., Sheng, P., Wen, C., You, J., & Gao, Y. (2024). *Data scaling laws in imitation learning for robotic manipulation* [Preprint]. arXiv. https://doi.org/10.48550/arXiv.2410.18647
- **Link:** https://arxiv.org/abs/2410.18647
- **Verification:** arXiv abstract page read. The page lists no venue. (I believe it appeared at ICLR 2025, but this was not verified.)
- **What it actually establishes:** Over 40,000 demonstrations and more than 15,000 real-world rollouts show that generalization follows a roughly power-law relationship in the *number of environments and objects*. Diversity matters far more than the raw number of demonstrations. Four collectors in one afternoon gathered enough data for policies that reach about 90% success in novel environments.
- **Use in dissertation:** Complicates the robotics-gap story. What is scarce is *diversity of real situations*, and modest, well-targeted human collection can go a long way.

### HaSchmidhuber2018
- **APA:** Ha, D., & Schmidhuber, J. (2018). Recurrent world models facilitate policy evolution. In *Advances in Neural Information Processing Systems 31 (NeurIPS 2018)* (pp. 2450–2462). https://proceedings.neurips.cc/paper_files/paper/2018/file/2de5d16682c3c35007e4e92982f1a2ba-Paper.pdf (no DOI)
- **Link:** https://papers.neurips.cc/paper/7512-recurrent-world-models-facilitate-policy-evolution
- **Verification:** Record located only. Proceedings metadata and abstract were seen in search results, and the paper was not opened.
- **What it actually establishes:** A generative recurrent model, learned without supervision from environment observations, compresses the environment. Small policies trained by evolution on its features reach strong results. An agent can be trained entirely inside the model's "dream" and then transferred back to the real environment.
- **Use in dissertation:** Original source for the idea that a world model lets an agent rehearse beyond its collected data. The model itself, however, is learned from real environment experience.

### Hafner2025
- **APA:** Hafner, D., Pasukonis, J., Ba, J., & Lillicrap, T. (2025). Mastering diverse control tasks through world models. *Nature, 640*(8059), 647–653. https://doi.org/10.1038/s41586-025-08744-2
- **Link:** https://doi.org/10.1038/s41586-025-08744-2 (preprint: https://arxiv.org/abs/2301.04104)
- **Verification:** Nature record located (DOI, volume, pages and date via PubMed Central and RePEc in search results; the PMC page was blocked by a CAPTCHA). arXiv abstract read.
- **What it actually establishes:** DreamerV3 learns a world model from environment interaction and improves its behavior by imagining future trajectories. A single configuration outperforms specialized methods on more than 150 tasks. It is the first algorithm to collect diamonds in Minecraft from scratch, without human data or curricula.
- **Use in dissertation:** Peer-reviewed replacement for the "world models multiply data" point. Imagination amplifies experience gathered from the environment, and none of that experience is *human*. That is exactly the scenario where the grounding assumption weakens. Note that these are simulated environments.

### Zhao2020Sim2Real
- **APA:** Zhao, W., Queralta, J. P., & Westerlund, T. (2020). Sim-to-real transfer in deep reinforcement learning for robotics: A survey. In *2020 IEEE Symposium Series on Computational Intelligence (SSCI)* (pp. 737–744). IEEE. https://doi.org/10.1109/SSCI47803.2020.9308468
- **Link:** https://arxiv.org/abs/2009.13303
- **Verification:** arXiv abstract page read (the journal reference and DOI are shown there).
- **What it actually establishes:** Simulation gives cheap, safe, plentiful training data, but the reality gap degrades policies once they are transferred to physical robots. The survey reviews domain randomization, domain adaptation, imitation learning, meta-learning and knowledge distillation as ways to bridge the gap.
- **Use in dissertation:** Supports the principle that simulated or imagined data must be anchored to real-world data. The physical world is the grounding signal for embodied AI.

### Hofer2021
- **APA:** Höfer, S., Bekris, K., Handa, A., Gamboa, J. C., Mozifian, M., Golemo, F., Atkeson, C., Fox, D., Goldberg, K., Leonard, J., Liu, C. K., Peters, J., Song, S., Welinder, P., & White, M. (2021). Sim2Real in robotics and automation: Applications and challenges. *IEEE Transactions on Automation Science and Engineering, 18*(2), 398–400. https://doi.org/10.1109/TASE.2021.3064065
- **Link:** https://dspace.mit.edu/handle/1721.1/138850
- **Verification:** Record located only. The DOI, volume and issue come from MIT DSpace metadata in search results, and the pages from a TU Darmstadt BibTeX record. **The co-author list is from memory and was not checked.** Confirm it on IEEE Xplore, or cite as "Höfer, S., et al." until then.
- **What it actually establishes:** This short perspectives piece grew out of an RSS 2020 workshop debate among field leaders on the definition, viability and importance of sim-to-real transfer.
- **Use in dissertation:** Secondary support that the sim-to-real gap is an open, contested problem. Prefer Zhao et al. (2020) as the main citation.

---

## F. Performative feedback between models and their data

### Perdomo2020
- **APA:** Perdomo, J., Zrnic, T., Mendler-Dünner, C., & Hardt, M. (2020). Performative prediction. In *Proceedings of the 37th International Conference on Machine Learning* (PMLR Vol. 119, pp. 7599–7609). https://proceedings.mlr.press/v119/perdomo20a.html (no DOI; arXiv: https://doi.org/10.48550/arXiv.2002.06673)
- **Link:** https://proceedings.mlr.press/v119/perdomo20a.html
- **Verification:** Record located only. The abstract was seen in search results, and the page was not opened.
- **What it actually establishes:** When predictions inform decisions, they can change the outcomes they aim to predict ("performative" prediction). The paper builds a risk-minimization framework drawing on statistics, game theory and causality, with an equilibrium concept called *performative stability* and conditions under which repeated retraining converges to it.
- **Use in dissertation:** The general theory of models reshaping their own data distribution, of which model collapse is a special case. It links the empirical anchor to the dissertation's political-economy concerns.

### HardtMendlerDunner2025
- **APA:** Hardt, M., & Mendler-Dünner, C. (in press). Performative prediction: Past and future. *Statistical Science*. https://doi.org/10.48550/arXiv.2310.16608
- **Link:** https://arxiv.org/abs/2310.16608
- **Verification:** arXiv abstract page read ("to appear in *Statistical Science*" per the comments field). The journal DOI and year were not confirmed.
- **What it actually establishes:** A review of performativity. Platform-deployed models change user behavior and therefore their own future data. The review separates *learning* from *steering* and connects steering to platform power through "performative power".
- **Use in dissertation:** Supports the claim that an AI system with market power can shape the human data it later depends on. This matters for the "corrupted exchange starves the AI" argument in Ch. 5 §6.

### TaoriHashimoto2023
- **APA:** Taori, R., & Hashimoto, T. B. (2023). Data feedback loops: Model-driven amplification of dataset biases. In *Proceedings of the 40th International Conference on Machine Learning* (PMLR Vol. 202, pp. 33883–33920). https://proceedings.mlr.press/v202/taori23a.html (no DOI; arXiv: https://doi.org/10.48550/arXiv.2209.03942)
- **Link:** https://proceedings.mlr.press/v202/taori23a.html
- **Verification:** PMLR abstract page read.
- **What it actually establishes:** The paper models systems in which logged model outputs are later scraped as training data, and tracks bias statistics such as gender bias over time. Amplification depends on "uniform faithfulness": models whose outputs look like samples from the training distribution are stable, while models that over-produce the majority output amplify bias. Experiments cover image classification, visual role-labeling and language generation, and an intervention to stabilize feedback is proposed.
- **Use in dissertation:** Shows that feedback-loop harm is often *distortion* (bias amplification), not only degradation, and that it is controllable by design.

---

## G. Contamination of the web by AI-generated text

### Thompson2024
- **APA:** Thompson, B., Dhaliwal, M., Frisch, P., Domhan, T., & Federico, M. (2024). A shocking amount of the web is machine translated: Insights from multi-way parallelism. In *Findings of the Association for Computational Linguistics: ACL 2024* (pp. 1763–1775). Association for Computational Linguistics. https://doi.org/10.18653/v1/2024.findings-acl.103
- **Link:** https://aclanthology.org/2024.findings-acl.103
- **Verification:** Record located only (ACL Anthology metadata via search).
- **What it actually establishes:** Content translated into many languages at once is common on the web, and its low quality points to machine translation. Such machine-generated multi-way content makes up a large share of web text in lower-resource languages. The authors warn about training multilingual LLMs on web-scraped data.
- **Use in dissertation:** Early, peer-reviewed evidence of machine-generated contamination, concentrated in low-resource languages. Human data scarcity is unequal across languages.

### Liang2024
- **APA:** Liang, W., Zhang, Y., Wu, Z., Lepp, H., Ji, W., Zhao, X., Cao, H., Liu, S., He, S., Huang, Z., Yang, D., Potts, C., Manning, C. D., & Zou, J. (2024). Mapping the increasing use of LLMs in scientific papers. *First Conference on Language Modeling (COLM 2024)*. https://doi.org/10.48550/arXiv.2404.01268
- **Link:** https://arxiv.org/abs/2404.01268
- **Verification:** Record located only. Abstract figures were seen in search results. **The author list is from memory and must be checked.** A 2025 *Nature Human Behaviour* version exists with updated figures (up to 22% in computer science), and its record was located only.
- **What it actually establishes:** Across 950,965 papers (arXiv, bioRxiv and Nature portfolio, January 2020 to February 2024), the estimated share of LLM-modified content rose steadily. Computer science rose most, to up to 17.5%, and mathematics and the Nature portfolio least, to up to about 6.3%.
- **Use in dissertation:** Shows that even high-value human corpora are absorbing AI-modified text, which bears on provenance.

### Pew2026
- **APA:** Bestvater, S., Smith, A., TerBush, C., Baronavski, C., & Chavda, J. (2026, August 20). *How much of the internet is written with AI?* Pew Research Center. https://www.pewresearch.org/data-labs/2026/08/20/how-much-of-the-internet-is-written-with-ai/ (no DOI)
- **Link:** as above
- **Verification:** Full page read. This is authoritative but not peer-reviewed.
- **What it actually establishes:** About 490,000 English Common Crawl pages from January 2021 to July 2026 were scored with an open-weight Pangram detector. In a July 2026 sample of 10,000 pages, about 10% show significant signs of AI authorship. Among pages published after ChatGPT's release, the share is over one-third. Rates are about 10% for .com, 4.6% for .org and about 1% for .edu and .gov. Caveats: detectors misclassify individual documents, and the sample is English-only.
- **Use in dissertation:** The best current measure of contamination. Fresh *verifiably human* web text is shrinking as a share of what crawlers collect, which strengthens the economic value of provenance-assured human data. Other figures in circulation (35% of new websites; Graphite's 51.7% of new articles) are not peer-reviewed and were not verified here. Do not cite them.

---

## Corrections to the draft

1. **Ch. 2, PRL paper. Authors and bibliographic details are missing.** Cite as Jangjoo, di Sarra, Marsili & Roudi (2026), *Phys. Rev. Lett.* 136, 197301, doi:10.1103/156q-3ngc. The year "2026" in the draft is correct.
2. **Ch. 2, the draft overstates the PRL finding.** The draft says one real data point per step "*or* adding regularization" avoids collapse, which presents them as alternatives. The paper says collapse may be avoided if the data include at least one ground-truth point per generation, *with* MAP estimation or regularization. In the Poisson case, a prior alone (no real data) does not prevent collapse. "One point" is shown to suffice only in specific examples (for instance, 1 real point among 200 samples), not proved in general. Avoiding collapse also does not mean recovering the true distribution: the parameters keep fluctuating, and under a prior they are biased. Suggested wording: "...finds that maximum-likelihood retraining only on a model's own output converges to degenerate states that amplify initial biases, and that adding even a single ground-truth sample per generation, together with a prior or regularization, can keep the process from collapsing in the models studied."
3. **Ch. 2, "variance shrinks and tails disappear" is uncited.** Attach Shumailov et al. (2024), and add Guo et al. (2024) for language diversity.
4. **Ch. 2 and Ch. 5, the "small trickle" reading is one-sided.** Dohmatob et al. (2025) show that when the synthetic fraction stays non-vanishing, more data stops helping, and that mitigation needs real data growing *at least as fast* as synthetic data. Alemohammad et al. (2024) show that a fixed real corpus only delays degradation unless *fresh* real data arrives each generation. Gerstgrasser et al. (2024) show the opposite in an accumulate-everything regime. The dissertation should present this as a live disagreement driven by assumptions, citing Schaeffer et al. (2025) and Kazdan et al. (2024).
5. **"Strong Model Collapse" citation.** The authors are Dohmatob, Feng, Subramonian & Kempe (ICLR 2025). Its "collapse" means a *scaling plateau* in regression, not output degeneration. Do not cite it for "gibberish".
6. **Ch. 5, DEV Community post. Remove it.** I found no peer-reviewed source for a "95% data gap" figure. Do not repeat the number. Replace the general claim with Open X-Embodiment (2024), Firoozi et al. (2025, IJRR) and, for scale, DROID (Khazatsky et al., 2024). Replace "world models multiply data rather than create it" with Hafner et al. (2025, *Nature*) and Ha & Schmidhuber (2018), plus Zhao et al. (2020) on the sim-to-real gap. Present the "multiply, not create" wording as *the dissertation's own inference* from those sources, not a quotation.
7. **Ch. 5, "embodied systems... gather real-world sensor data that is not human-generated."** This is partly wrong about the present. Large real-robot datasets (DROID, most of Open X-Embodiment) are mostly *human teleoperated demonstrations*. Non-human data collection is shown mainly in simulation (DreamerV3, AlphaZero). Reword this as a future possibility.
8. **Ch. 1, "models trained on their own output lose variance and drift."** This holds under replacement. Add "when synthetic data replaces rather than supplements human data" (Gerstgrasser et al., 2024; Kazdan et al., 2024).
9. **The strongest counterevidence is missing.** Self-play (Silver et al., 2018), verifiable-reward RL (DeepSeek-R1, 2025), verifier-filtered synthetic data (Feng et al., 2024) and RLAIF (Lee et al., 2024) all belong in Ch. 5 §1 as a third way the assumption can weaken.

---

## Synthesis notes

**What the evidence supports.** Across very different formalisms the result is consistent: exponential families (Jangjoo et al., 2026), Gaussian models, Gaussian mixtures, VAEs and an OPT-125m model (Shumailov et al., 2024), image diffusion models (Alemohammad et al., 2024), and linear regression (Dohmatob et al., 2025). When a model is trained repeatedly on its own unfiltered output, *with nothing from outside the loop*, it loses rare events, its diversity narrows, and initial biases get locked in. This is about as close to a theorem as empirical machine learning gets. Scarcity sits beside it. Optimal scaling is data-hungry (Hoffmann et al., 2022). Repetition helps only up to about four epochs (Muennighoff et al., 2023). The stock of public human text, about 300T tokens, is projected to be exhausted around 2026–2032 (Villalobos et al., 2024). That stock is shrinking further through withdrawn consent (Longpre et al., 2024) and contamination: about a third of post-ChatGPT English pages show AI authorship (Pew, 2026).

**What the evidence does not support.** It does not support the strong claim that AI needs *continuing human-generated content* as such. Three findings break it:
1. **Accumulation.** If original human data is kept and synthetic data is added rather than substituted, error stays bounded (Gerstgrasser et al., 2024), or degrades only slowly under fixed budgets (Kazdan et al., 2024).
2. **External verification.** Where a correctness signal exists that is not a human, self-generated data works. Examples are game rules (AlphaZero), answer checkers and compilers (DeepSeek-R1, STaR), learned verifiers (Feng et al., 2024) and physics simulators (Gillman et al., 2024).
3. **Non-human grounding.** Agents can learn from environment interaction alone (DreamerV3), and the physical world can be the outside signal for embodied systems.

Schaeffer et al. (2025) add that "collapse" is defined in at least eight incompatible ways, so careless citation invites rebuttal.

**The most defensible formulation.** *Learning systems need a continuing supply of information from outside their own generative loop. In domains where correctness cannot be verified mechanically and the target is human meaning, preference, value or novel cultural production, the only adequate source of that outside signal is people. In those domains, the human contribution must keep pace with, and not merely seed, the volume of synthetic data in training (Dohmatob et al., 2025; Alemohammad et al., 2024). In domains with cheap automatic verification or a faithful simulator, the dependence is weak or absent.* This version is narrower than the draft's, but it survives the counterevidence. It also fits the dissertation's exchange logic better: what humans supply is *ground truth about humans*, which machines cannot verify against anything else. DeepSeek-R1 itself relied on human-curated cold-start data, and its authors flag non-verifiable tasks as unsolved. Ouyang et al. (2022) show how much a small amount of human preference data is worth. Firoozi et al. (2025) and Lin et al. (2024) show that what is scarce in robotics is *diverse real situations*.

**Conditions under which it fails (for Ch. 5).**
- (a) Labs keep and accumulate the pre-2023 human corpus and filter synthetic data well. Then dependence on *new* human data may be modest, a trickle rather than a partnership, as the draft already concedes.
- (b) Verifiers, simulators or AI judges (RLAIF) extend to open-ended domains. Note, though, that today's AI judges are themselves distilled from human data.
- (c) Embodied agents with world models get most of their grounding from physical interaction, which is non-human and, unlike text, not running out.
- (d) Human-generated data becomes indistinguishable from AI-assisted text (Liang et al., 2024; Pew, 2026). Then "fresh human data" stops being a well-defined commodity unless there is provenance infrastructure, which is a governance problem the dissertation could claim as its own.

A last caution: almost all of the collapse evidence comes from small models or stylized theory. No published study shows a frontier model collapsing under realistic data pipelines. The dissertation should say so explicitly.
