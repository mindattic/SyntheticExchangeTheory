---
codex: 1
project: SyntheticExchangeTheory
code: SET
layer: stories
status: living
updated: 2026-10-13
---
<!-- GENERATED from MindAttic.Tickets/data/Tickets.db by `tickets db render`. Do not edit: this file is rewritten from the database; change stories and tickets with the tickets CLI. -->

# SyntheticExchangeTheory — User Stories
> ✅ done (shipped & tested) · 🟡 partial · ⬜ planned. Every ✅ cites the test.

## Priority backlog
- SET-T2 is the blocking decision: whether Ch. 7's agrarian settlement stays the pilot's
  primary empirical test, is reframed as the final stage of a staged validation program, or
  is replaced. Ryan to decide before any further Ch. 7 / Appendix B editing.

## Tickets
> Permanent log of every change and fix — this repo's ticket system. Rows are append-only: never
> delete or reword one; only move its Status (open → closed / wont-do) and fill in Ref. Status is
> a word, not a glyph, so tickets don't count toward the story index. Keep this section last.

| ID | Date | Type | Status | Summary | Ref |
|---|---|---|---|---|---|
| SET-T1 | 2026-10-12 | docs | closed | Start the permanent ticket log in USER_STORIES.md | — |
| SET-T2 | 2026-10-13 | docs | closed | Ryan flagged that the closed agrarian settlement (Ch. 7) may not be a scientifically adequate test of the exchange mechanism: it's slow, expensive, hard to iterate, and confounds farming/physical-survival risk (land yield, livestock, Biosphere-2-style failure modes) with the actual hypothesis (designed dependence shifts behavior toward wellbeing). Discussed cheaper/faster precursor designs: agent-based simulation of the Ch. 3 formal model (Appendix A), a lab-style exchange experiment (human participants + AI principal, randomized dependence), and a digital-native pilot (small online cooperative/platform economy with a compute currency, no physical self-sufficiency requirement). Decision needed: keep agrarian as primary test, reframe it as the last stage of a staged program, or replace it. | Decision made 2026-10-17: replace the Ch. 7 agrarian/farm pilot outright (not keep, not reframe as staged final step); superseded by SET-T12/SET-T13 |
| SET-T3 | 2026-10-13 | docs | closed | Blocked on SET-T2. Draft the staged-validation framing chosen in SET-T2 (new section or chapter): simulation stage, lab-experiment stage, digital-native pilot stage, and how each feeds into or precedes the physical settlement. | Superseded by SET-T13: the staged-validation framing assumed the physical settlement stays in as a later stage; Ryan rejected the agrarian/farm design specifically, not the idea of an eventual real-world test, so SET-T13 restarts the design search |
| SET-T4 | 2026-10-13 | docs | closed | Blocked on SET-T3. Revise Ch. 7 §7.11 and Appendix B (design summary, hypotheses, replication plan) to reflect the chosen validation strategy and its staging. | Superseded by SET-T12/SET-T13: Ch. 7 and Appendix B are being removed outright (SET-T12), not revised to match a staged strategy |
| SET-T5 | 2026-10-15 | chore | closed | Remove duplicate command copies (/quickload, /quicksave) now centralized at the user level (~/.claude/commands) | M.FLOW-T14 |
| SET-T6 | 2026-10-16 | chore | closed | install.ps1 adds this repo's 15 .prose/commands stubs for the shared global commands, so any LLM client finds them | mindattic-agent-standard/install.ps1 run 2026-10-16 |
| SET-T7 | 2026-10-16 | chore | open | Bug hunt: run an exhaustive /bughunt over the whole repo and fix every real bug found (each fix under its own fix ticket), then hunt again; close this only when a full pass finds nothing | user request 2026-10-16: approved repo sweep |
| SET-T8 | 2026-10-16 | chore | open | Run the full unit test suite and fix every failure (each under its own fix ticket) until it passes; put the passing run in --ref. No test project: close this wont-do saying so | user request 2026-10-16: approved repo sweep |
| SET-T9 | 2026-10-16 | chore | open | Clean up code and docs: remove dead code, stale comments and outdated or duplicated docs, and simplify where behaviour doesn't change (/simplify); tests stay green | user request 2026-10-16: approved repo sweep |
| SET-T10 | 2026-10-16 | docs | open | Bring README.md up to date with the code as it is now (what it is, setup, usage, commands, current state), following codex-standard/README-STYLE.md; README.htm regenerated if the repo has one | user request 2026-10-16: approved repo sweep |
| SET-T11 | 2026-10-16 | docs | closed | Update USER_STORIES.md | — |
| SET-T12 | 2026-10-17 | docs | closed | Remove Chapter 7 (The Prototype: A Closed Agrarian Pilot) and Appendix B (its pre-registration protocol) entirely, and scrub every cross-reference to the agrarian/farm pilot across Ch. 1, 3-6, 8, 10, Appendix C glossary, README.md and docs/USER_STORIES.md; renumber remaining chapters/appendices and update export.json to match | Superseded by SET-T14/SET-T15: Ryan corrected the sequencing 2026-10-17 -- build the replacement chapter first, retarget references, remove the agrarian chapter last |
| SET-T13 | 2026-10-17 | docs | closed | Spike: design a fundamentally scientific experiment, run in a closed space with a genuine control environment (not an agrarian/farm settlement), to test whether a compute-funded basic income backed by AI systems' willingly-given user training-data contributions is viable, i.e. whether that designed dependence actually shifts system behavior toward provider wellbeing; deliver a pre-registration-style write-up of the chosen design, leaving chapter drafting to a follow-up ticket | Superseded by SET-T14: scope corrected to draft the actual replacement chapter text, not defer drafting to a follow-up ticket |
| SET-T14 | 2026-10-17 | docs | open | Design and draft the replacement Ch. 7: a fundamentally scientific experiment, run in a closed space with a genuine control environment (not an agrarian/farm settlement), testing whether a compute-funded basic income backed by AI systems' willingly-given user training-data contributions is viable, i.e. whether that designed dependence shifts system behavior toward provider wellbeing. Deliverable is the actual chapter text plus its pre-registration-style protocol appendix, written alongside the existing Ch. 7 (nothing removed yet) | Supersedes SET-T13; first of a three-step sequence set by Ryan 2026-10-17: build replacement, retarget references, remove agrarian chapter |
| SET-T15 | 2026-10-17 | docs | open | After SET-T14's replacement chapter exists: retarget every cross-reference to the agrarian/farm pilot across Ch. 1, 3-6, 8, 10, Appendix C glossary, README.md, AGENTS.md and docs/USER_STORIES.md to the new design; only then remove the old agrarian Ch. 7 text and Appendix B pilot protocol, renumbering chapters/appendices and updating export.json if numbering changes | Requires SET-T14; supersedes SET-T12 with the order corrected (references retargeted before the agrarian chapter is removed) |
| SET-T16 | 2026-10-18 | docs | closed | Update USER_STORIES.md | — |
| SET-T17 | 2026-10-19 | chore | open | Convert tracked source files to LF line endings via .gitattributes, per HOUSE-LAW-13 (low priority) | — |
| SET-T18 | 2026-10-20 | docs | open | Publish SyntheticExchangeTheory docs to GitHub Pages via the shared Toolkit DocFX pipeline: run adopt-docs-site.ps1 (README.md as home page, docs/*.md as articles, API reference only where the code builds in CI), enable Pages with build_type=workflow, set the repo homepage URL, retire tools/build-readme.ps1 and README.htm, confirm the docs Actions run is green and https://mindattic.github.io/SyntheticExchangeTheory/ returns 200. Depends on MAT-T8. | — |
