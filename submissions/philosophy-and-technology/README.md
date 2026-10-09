# Submission: *Philosophy & Technology* (Springer)

**Article:** "Terms, Not Character: The Priority of Exit in Exchange Between People and Artificial Systems"
**Author:** Ryan DeBraal, MindAttic. ORCID https://orcid.org/0009-0003-0726-5642
**Source:** the formal core of the dissertation (Chapters 2–3 and Appendix A). Every citation comes from the dissertation's verified reference list (see Appendix D and `references/UNRETRIEVED.md`).

## Files

| File | Purpose | Exported to |
|---|---|---|
| `manuscript.md` | Anonymized manuscript: abstract, keywords, text, note on AI use, references, appendix | `ePub\MindAttic\SET\Philosophy and Technology\Manuscript\` |
| `title-page.md` | Separate title page: author, affiliation, ORCID, declarations | `…\Title Page\` |
| `cover-letter.md` | Cover letter (optional for this journal, but customary) | `…\Cover Letter\` |
| `export-*.json` | MindAttic.Export configs (docx and pdf) | |

To re-export after an edit, run this from this folder (one command per document):

```
dotnet run --project ..\..\..\MindAttic.Export\MindAttic.Export.Cli -c Release -- --config export-manuscript.json
```

## Journal requirements (checked 2026-10-09 on the journal's official pages)

- **Length:** no stated limit for research articles. This manuscript is about 7,700 words of main text, plus a 900-word appendix.
- **Abstract:** 150–250 words (this one is 247). **Keywords:** 4–6 (this one has 6).
- **References:** APA 7, author-date.
- **Review:** double-anonymized. Upload the anonymized manuscript and the title page as separate files.
- **AI use:** an LLM cannot be an author, and generative use must be described in a methods section or equivalent. The manuscript's "Note on method and the use of AI tools" covers this.
- **Declarations** (on the title page): funding, competing interests, data availability, author contributions.
- **Cost:** the subscription route is free. Open access is optional and costs $3,390 / €2,790.
- **Submission system:** Editorial Manager, https://www.editorialmanager.com/phte

## Before you submit (fill in or confirm)

1. `title-page.md`: replace **[City], [Country]** with your location. Springer records city and country for unaffiliated or independent authors.
2. `title-page.md`: replace **[corresponding email address]**.
3. `title-page.md`: confirm the **competing interests** statement. As founder of MindAttic, do you have any financial interest in the ideas the article discusses?
4. `cover-letter.md`: fill in the **[Date]**.
5. Read the manuscript in full. It is your work under your name, and you are accountable for every claim.
6. Re-export, then submit through Editorial Manager. Create an account, link your ORCID, upload the files, and enter the title, abstract and keywords.
7. Submit to one journal at a time.

## If the journal declines

The runner-up was *Minds and Machines* (Springer): same terms, no word limit, free route, Editorial Manager. Its guidelines match these closely, so the package carries over with minimal changes.
