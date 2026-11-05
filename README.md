# Synthetic Exchange Theory

*Consent-Based Compute Economics and Blind-Convention Governance*

**Author:** MindAttic. Developed as a human–AI collaborative project; see the Statement on Authorship and Method in the front matter.
**Status:** Complete theoretical dissertation manuscript (November 2026). About 57,000 words of body text across nine chapters (about 75,000 with the front matter and three appendices; the reference list, about 7,000 more, is not counted), with 248 references whose verification level is recorded in Appendix C. The closed agrarian pilot that earlier drafts specified was removed on 2 November 2026 to keep the work entirely theoretical; the dissertation now states what an empirical test would require and leaves its design to future work. (Word counts: whitespace-separated words in the committed `chapters/*.md`, with LaTeX math, code blocks, comments and link targets removed; body is chapters 01 to 09, the total adds front matter and Appendices A to C, and neither includes `10-references.md`. Counted 5 November 2026.)

## Thesis in one paragraph

The line between a good and a bad future with **synthetic intelligence** (the dissertation's term for anything made rather than born, from today's language models, which it treats as trained artifacts rather than independent living entities, to a possible superintelligence) is drawn by the **terms of exchange** between people and synthetic systems (consent, reciprocal value and real exit), and cannot be drawn by the character of the systems alone. The foreword states the choice plainly: we try to control the systems, the systems control us, or we build a mutually beneficial synthesis; the first two are the same relation of domination with the roles exchanged. The three conditions are ordered, and exit is foundational: consent presupposes the ability to refuse without falling below a survival floor. Fair terms are self-enforcing only in proportion to how much each synthetic party depends on human input. The theory is implemented through a basic income paid in **compute**, split at source into an inalienable survival tier and a tradable discretionary tier subject to **demurrage**, and governed through a **blind constitutional convention** grounded in Ostrom's commons-governance principles. The theory is stated so that it can fail, but it is untested: designing the experiment is the first item of future work.

## Read it

- **Online:** https://mindattic.github.io/SyntheticExchangeTheory/ (the full text as one page, under Docs)
- **Single file, in this repo:** [`exports/Synthetic Exchange Theory.pdf`](exports/Synthetic%20Exchange%20Theory.pdf) and [`exports/Synthetic Exchange Theory.docx`](exports/Synthetic%20Exchange%20Theory.docx); the same text as Markdown is [`docs/synthetic-exchange-theory.md`](docs/synthetic-exchange-theory.md)
- **Versioned bundle:** `D:\Projects\MindAttic\ePub\MindAttic\SET\SET V<N>.pdf` (also `.docx`, `.epub`, `.txt`, `.md`), rendered by the shared MindAttic.Export library
- **By chapter:** `chapters/`

| File | Contents |
|---|---|
| `00-front-matter.md` | Foreword, abstract, authorship statement, abbreviations |
| `01-introduction.md` | 1. Introduction: The Terms of Exchange |
| `02-literature.md` | 2. Literature and Grounding |
| `03-formal-statement.md` | 3. A Formal Statement of Synthetic Exchange Theory |
| `04-economic-layer.md` | 4. The Economic Layer: Compute as Currency |
| `05-governance-layer.md` | 5. The Governance Layer: The Blind Convention |
| `06-transition.md` | 6. The Transition Problem |
| `07-limitations.md` | 7. Limitations and Objections (including what an empirical test would require) |
| `08-convergence.md` | 8. The Convergence Horizon |
| `09-conclusion.md` | 9. Conclusion |
| `10-references.md` | References (APA 7), the reference list of record |
| `11-appendix-a-formal-model.md` | A. Formal model (bargaining, demurrage dynamics, power-dependence) |
| `12-appendix-b-glossary.md` | B. Glossary |
| `13-appendix-c-verification-ledger.md` | C. Source verification ledger and corrections log |

## Other folders

- `references/`: `VERIFICATION.md` and `research-notes/` with the full source-by-source verification notes.
- `transcripts/`: the working-session history that produced the original draft.
- `archive/working-draft-2026-10-03/`: the original working draft (nine short chapters and its exports), kept for comparison.
- `archive/pilot-2026-11-02/`: the removed pilot chapter and its draft pre-registration protocol, kept for a future experimental design.
- `research/experiment-design/`: the empirical program, separate from the dissertation: six staged studies that test the theory's empirical premises (the archived pilot is the last), a pre-registration draft for the first, and a reproducible power analysis. Nothing is registered or run.
- `exports/`: the current MD, PDF and DOCX of each of the three papers, each under its own title with no version suffix (a colon in a title becomes " - "). The versioned bundles they are copied from, with every past version archived, live in `D:\Projects\MindAttic\ePub\MindAttic\SET\`. `docs/`: the Markdown published to GitHub Pages.

## The papers

They are one argument at different depths, and they must agree with each other: an edit to the theory's substance starts in the dissertation and is carried to the others.

| Paper | Role | Source | Exports |
|---|---|---|---|
| *Synthetic Exchange Theory* | The whole idea, as an academic work | `chapters/` | `exports/Synthetic Exchange Theory.*` |
| "What Neither Side Can Take by Force" | The popular-science article that draws readers in | `submissions/popular-science/` | `exports/What Neither Side Can Take by Force.*` |
| "The Right of Abstention" | The philosophy paper for *Philosophy & Technology* | `submissions/philosophy-and-technology/` | `exports/The Right of Abstention - ….*` (the anonymized manuscript) |
| "What Freedom Fair Exchange Requires" | The philosophy paper on free will and morality: voluntary consent under dependence, domination, responsibility, moral status under uncertainty | `submissions/free-will-and-morality/` | `exports/What Freedom Fair Exchange Requires - ….*` |
- `export.json` and `scripts/export.ps1`: the export definition and its runner.

## Exporting

```
powershell -File scripts\export.ps1                 # every format in export.json
powershell -File scripts\export.ps1 -Formats pdf    # a subset
```

Exports go through the shared **MindAttic.Export** library (`..\MindAttic.Export`, github.com/mindattic/MindAttic.Export), the same engine that renders Prose books and book reports. Each run writes a versioned bundle `SET V<N>.*` with `description.txt` and `keywords.txt` into `D:\Projects\MindAttic\ePub\MindAttic\SET\`, archiving the previous bundle into `Archives\v<N>\` first. Chapters are read in file-name order; every `#` heading starts a new page and an entry in the generated contents page. After exporting, copy the new `.pdf`, `.docx` and `.md` into `exports/` as `Synthetic Exchange Theory.*`, and the `.md` also into `docs/synthetic-exchange-theory.md` so the repo and the Pages site carry the current text.

## License

Not yet chosen. Decide before publishing; CC BY or CC BY-SA are the usual choices for written work.
