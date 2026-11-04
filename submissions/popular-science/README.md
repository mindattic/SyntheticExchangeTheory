# Popular-science article: "What Neither Side Can Take by Force"

**Article:** "What Neither Side Can Take by Force" — a magazine-style treatment of Synthetic Exchange Theory, written for a general audience (the kind of national readership *Scientific American* reaches), without exhaustive formalism.
**Source:** drawn from the dissertation's thesis, Chapter 1's framing scenarios, Chapter 3's three conditions, Chapter 4's compute economy and demurrage, Chapter 5's blind convention, Chapter 6's correlated-patch catastrophe, and Chapter 8's convergence horizon. Every factual claim carries a citation to a work in the dissertation's verified reference list (Appendix C); the "Further reading" list at the end of the manuscript gives the APA 7 form for each.
**Byline:** MindAttic (2026-11-04: Ryan decided MindAttic is the author of record for both the book and this article, resolving the earlier "no byline" draft of the same day).

## Files

| File | Purpose | Exported to |
|---|---|---|
| `manuscript.md` | The article: title, deck, byline, body (about 3,500 words), a further-reading list, and a version history. | `ePub\MindAttic\SET\Popular Science\` |
| `export-manuscript.json` | MindAttic.Export config (pdf and docx) | |

To re-export after an edit, run this from this folder:

```
dotnet run --project ..\..\..\MindAttic.Export\MindAttic.Export.Cli -c Release -- --config export-manuscript.json
```

MindAttic.Export numbers the bundle itself (V1, V2, V3, ... by scanning the output folder) and archives the previous one, the same mechanism `scripts\export.ps1` uses for the dissertation. As committed, the current export is **V1**. Unlike `exports/` for the dissertation itself, the PDF/DOCX are not copied back into this repo (same as `submissions/philosophy-and-technology`) — they live only at the `ePub` path above; this folder keeps the Markdown source and the config.

## Versioning and the changelog

Per Ryan's instruction (2026-11-04): version numbers are whole numbers, forever (v1, v2, v3, v4, ...), never decimals, matching MindAttic.Export's own bundle numbering. The manuscript's "Version history" section at the end is the changelog: **the current version number is always the count of changelog entries, plus one.** V1 has zero entries because nothing has changed yet; the first edit after V1 adds the first entry (describing what changed to produce V2) and so on. Keep the two numbers in sync by hand: whenever you re-export a new version, add the matching changelog entry to `manuscript.md` in the same edit.

This convention is new and, so far, applied only to this article. The dissertation's own Appendix C (the verification-ledger passes, C.1–C.13) is not currently reconciled with its export version (V23) under this rule — the counts don't match (13 ledger entries vs. V23), because the ledger logs review passes, not every export cut. Ask Ryan before retrofitting this exact scheme onto the dissertation; it would mean deciding what counts as a "changelog entry" there and whether to renumber anything.

## What's settled and what isn't

- **Byline is "MindAttic"**, decided 2026-11-04 (see above and the `set-publication` memory).
- **Real submission still needs a contact person.** Magazines — including *Scientific American* — don't accept anonymous submissions: even with a house byline, someone has to be reachable for correspondence. Worth a decision from Ryan before this leaves the repo: who is the contact of record.
- **Target outlet is assumed, not confirmed.** The brief said "fit for... a magazine... that would get a national audience discussing the ideas," with *Scientific American* as the stylistic bar. Its actual freelance pitching process, word-count norms, and current openness to unsolicited feature pitches (as opposed to shorter opinion/Voices pieces) haven't been checked against its current submission guidelines. Other outlets with a similar register and reach (*The Atlantic*, *Wired*, *Aeon*, *Noema*) are reasonable alternatives if *Scientific American* doesn't fit once its current guidelines are checked.

## Open items

1. Who is the contact of record for submission (see above).
2. Which outlet to target, after checking that outlet's current pitch/submission process.
3. Whether to trim toward a tighter word count once a specific outlet's norms are known.
4. Whether to retrofit the whole-number-version / changelog-count rule onto the dissertation's own versioning (see above) — not done without asking.
