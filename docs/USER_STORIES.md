---
codex: 1
project: SyntheticExchangeTheory
code: SET
layer: stories
status: living
updated: 2026-10-13
---
<!-- GENERATED from MindAttic.Workflow/data/workflow.db by `workflow db render`. Do not edit: this file is rewritten from the database; change stories and tickets with the workflow CLI. -->

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
| SET-T2 | 2026-10-13 | docs | open | Ryan flagged that the closed agrarian settlement (Ch. 7) may not be a scientifically adequate test of the exchange mechanism: it's slow, expensive, hard to iterate, and confounds farming/physical-survival risk (land yield, livestock, Biosphere-2-style failure modes) with the actual hypothesis (designed dependence shifts behavior toward wellbeing). Discussed cheaper/faster precursor designs: agent-based simulation of the Ch. 3 formal model (Appendix A), a lab-style exchange experiment (human participants + AI principal, randomized dependence), and a digital-native pilot (small online cooperative/platform economy with a compute currency, no physical self-sufficiency requirement). Decision needed: keep agrarian as primary test, reframe it as the last stage of a staged program, or replace it. | — |
| SET-T3 | 2026-10-13 | docs | open | Blocked on SET-T2. Draft the staged-validation framing chosen in SET-T2 (new section or chapter): simulation stage, lab-experiment stage, digital-native pilot stage, and how each feeds into or precedes the physical settlement. | — |
| SET-T4 | 2026-10-13 | docs | open | Blocked on SET-T3. Revise Ch. 7 §7.11 and Appendix B (design summary, hypotheses, replication plan) to reflect the chosen validation strategy and its staging. | — |
| SET-T5 | 2026-10-15 | chore | closed | Remove duplicate command copies (/quickload, /quicksave) now centralized at the user level (~/.claude/commands) | M.FLOW-T14 |
| SET-T6 | 2026-10-16 | chore | closed | install.ps1 adds this repo's 15 .prose/commands stubs for the shared global commands, so any LLM client finds them | mindattic-agent-standard/install.ps1 run 2026-10-16 |
| SET-T7 | 2026-10-16 | chore | open | Bug hunt: run an exhaustive /bughunt over the whole repo and fix every real bug found (each fix under its own fix ticket), then hunt again; close this only when a full pass finds nothing | user request 2026-10-16: approved repo sweep |
| SET-T8 | 2026-10-16 | chore | open | Run the full unit test suite and fix every failure (each under its own fix ticket) until it passes; put the passing run in --ref. No test project: close this wont-do saying so | user request 2026-10-16: approved repo sweep |
| SET-T9 | 2026-10-16 | chore | open | Clean up code and docs: remove dead code, stale comments and outdated or duplicated docs, and simplify where behaviour doesn't change (/simplify); tests stay green | user request 2026-10-16: approved repo sweep |
| SET-T10 | 2026-10-16 | docs | open | Bring README.md up to date with the code as it is now (what it is, setup, usage, commands, current state), following codex-standard/README-STYLE.md; README.htm regenerated if the repo has one | user request 2026-10-16: approved repo sweep |
| SET-T11 | 2026-10-16 | docs | closed | Update USER_STORIES.md | — |
