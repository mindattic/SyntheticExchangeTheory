# Synthetic Exchange Theory

*Consent-Based Compute Economics and Blind-Convention Governance*

**Author:** MindAttic. Developed as a human–AI collaborative project; see the Statement on Authorship and Method in the front matter.
**Status:** Complete dissertation manuscript (October 2026). About 48,000 words of body text across ten chapters (about 64,000 with front matter, references and four appendices), with about 250 references whose verification level is recorded in Appendix D.

## Thesis in one paragraph

The line between a good and a bad future with artificial intelligence is drawn by the **terms of exchange** between people and synthetic systems (consent, reciprocal value and real exit), not by the character of the systems. The three conditions are ordered, and exit is foundational: consent presupposes the ability to refuse without falling below a survival floor. Fair terms are self-enforcing only in proportion to how much each synthetic party depends on human input. The theory is implemented through a basic income paid in **compute**, split at source into an inalienable survival tier and a tradable discretionary tier subject to **demurrage**, and governed through a **blind constitutional convention** grounded in Ostrom's commons-governance principles. It is tested by a bounded, self-sufficient agrarian pilot with pre-registered failure thresholds.

## Read it

- **Single file:** `D:\Projects\MindAttic\ePub\MindAttic\SET\SET V<N>.pdf` (also `.docx`, `.txt`, `.md`), rendered by the shared MindAttic.Export library.
- **By chapter:** `chapters/`

| File | Contents |
|---|---|
| `00-front-matter.md` | Abstract, authorship statement, abbreviations |
| `01-introduction.md` | 1. Introduction: The Terms of Exchange |
| `02-literature.md` | 2. Literature and Grounding |
| `03-formal-statement.md` | 3. A Formal Statement of Synthetic Exchange Theory |
| `04-economic-layer.md` | 4. The Economic Layer: Compute as Currency |
| `05-governance-layer.md` | 5. The Governance Layer: The Blind Convention |
| `06-transition.md` | 6. The Transition Problem |
| `07-prototype.md` | 7. The Prototype: A Closed Agrarian Pilot |
| `08-limitations.md` | 8. Limitations and Objections |
| `09-convergence.md` | 9. The Convergence Horizon |
| `10-conclusion.md` | 10. Conclusion |
| `11-references.md` | References (APA 7), the reference list of record |
| `12-appendix-a-formal-model.md` | A. Formal model (bargaining, demurrage dynamics, power-dependence) |
| `13-appendix-b-pilot-protocol.md` | B. Pilot pre-registration protocol (draft) |
| `14-appendix-c-glossary.md` | C. Glossary |
| `15-appendix-d-verification-ledger.md` | D. Source verification ledger and corrections log |

## Other folders

- `references/`: `VERIFICATION.md` and `research-notes/` with the full source-by-source verification notes.
- `transcripts/`: the working-session history that produced the original draft.
- `archive/working-draft-2026-10-03/`: the original working draft (nine short chapters and its exports), kept for comparison.
- `export.json` and `scripts/export.ps1`: the export definition and its runner.

## Exporting

```
powershell -File scripts\export.ps1                 # every format in export.json
powershell -File scripts\export.ps1 -Formats pdf    # a subset
```

Exports go through the shared **MindAttic.Export** library (`..\MindAttic.Export`, github.com/mindattic/MindAttic.Export), the same engine that renders Prose books and book reports. Each run writes a versioned bundle `SET V<N>.*` with `description.txt` and `keywords.txt` into `D:\Projects\MindAttic\ePub\MindAttic\SET\`, archiving the previous bundle into `Archives\v<N>\` first. Chapters are read in file-name order; every `#` heading starts a new page and an entry in the generated contents page.

## License

Not yet chosen. Decide before publishing; CC BY or CC BY-SA are the usual choices for written work.
