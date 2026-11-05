# Philosophy paper: "What Freedom Fair Exchange Requires"

**Article:** "What Freedom Fair Exchange Requires: Voluntariness, Domination and Responsibility Between People and Synthetic Intelligence".
**Role among the papers:** the dissertation states the whole idea; the popular-science article draws readers in; "The Right of Abstention" (`submissions/philosophy-and-technology/`) is the formal core (exit priority, bargaining); this paper takes the philosophical questions those leave: what freedom consent requires, when a choice made under dependence is voluntary, what domination means, who is responsible for what a synthetic system does, and what is owed to parties of uncertain moral status. It summarizes the dissertation's formal argument where it needs it and does not repeat the bargaining analysis.
**Byline:** MindAttic (Ryan's choice of author for these pieces, 2026-11-04).
**Length:** about 7,900 words of main text, abstract 245 words, six keywords.

## Sources

Works already in the dissertation's reference list are used only for claims the dissertation supports with them (verification in Appendix C). The eight works new to this paper (seven Stanford Encyclopedia of Philosophy entries and Santoni de Sio and Mecacci, 2021) were opened and read in the cited passages; `references/research-notes/free-will-and-morality.md` records what was read and which sentence each passage supports. Primary works reported through those surveys (Nozick, Wertheimer, Zimmerman, McGregor, Olsaretti, Pettit, Matthias, Strawson, Frankfurt) were not opened and are cited only through the survey that reports them.

## Files

| File | Purpose | Exported to |
|---|---|---|
| `manuscript.md` | The paper: title, byline, abstract, keywords, body, note on method and AI use, references, version history | `ePub\MindAttic\SET\Free Will and Morality\`, and committed as `exports/What Freedom Fair Exchange Requires - Voluntariness, Domination and Responsibility Between People and Synthetic Intelligence.{md,pdf,docx}` |
| `export-manuscript.json` | MindAttic.Export config (pdf and docx) | |

To re-export after an edit, run this from this folder (PowerShell; Git Bash mangles the backslashes):

```
dotnet run --project ..\..\..\MindAttic.Export\MindAttic.Export.Cli -c Release -- --config export-manuscript.json
```

Then copy `manuscript.md` and the new `V<N>.pdf`/`.docx` from the `ePub` folder over the three files in `exports/` (the colon in the title becomes " - " in the file name). Versions are whole numbers; the manuscript's "Version history" section is the changelog, and the current version is the number of entries plus one. As committed, the export is **V2**.

## Open items

1. No target journal chosen. Candidates with the right scope include *Philosophy & Technology* (already receiving the companion paper, so probably not both at once), *Minds and Machines*, *AI & Society* and *Ethics and Information Technology*; check each one's current guidelines, word limits and anonymization rules before choosing. If the journal reviews double-blind, the manuscript's self-citations to the dissertation (cited as MindAttic, 2026) and the byline will need anonymizing.
2. Journals require a named human author; the MindAttic byline would need to change for submission (see the `set-publication` memory: journal pieces have used Ryan DeBraal, MindAttic as affiliation).
3. Primary sources reported through surveys could be opened (through a library) and cited directly, which a philosophy journal's reviewers may expect: Olsaretti (1998, 2004), Wertheimer (1987), Pettit (1997), Matthias (2004), Strawson (1962).
