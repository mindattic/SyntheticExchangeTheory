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
| SET-T2 | 2026-10-13 | design | open | Ryan flagged that the closed agrarian settlement (Ch. 7) may not be a scientifically adequate test of the exchange mechanism: it's slow, expensive, hard to iterate, and confounds farming/physical-survival risk (land yield, livestock, Biosphere-2-style failure modes) with the actual hypothesis (designed dependence shifts behavior toward wellbeing). Discussed cheaper/faster precursor designs: agent-based simulation of the Ch. 3 formal model (Appendix A), a lab-style exchange experiment (human participants + AI principal, randomized dependence), and a digital-native pilot (small online cooperative/platform economy with a compute currency, no physical self-sufficiency requirement). Decision needed: keep agrarian as primary test, reframe it as the last stage of a staged program, or replace it. | — |
| SET-T3 | 2026-10-13 | docs | open | Blocked on SET-T2. Draft the staged-validation framing chosen in SET-T2 (new section or chapter): simulation stage, lab-experiment stage, digital-native pilot stage, and how each feeds into or precedes the physical settlement. | — |
| SET-T4 | 2026-10-13 | docs | open | Blocked on SET-T3. Revise Ch. 7 §7.11 and Appendix B (design summary, hypotheses, replication plan) to reflect the chosen validation strategy and its staging. | — |
| SET-T5 | 2026-10-15 | chore | closed | Remove duplicate command copies (/quickload, /quicksave) now centralized at the user level (~/.claude/commands) | WF-T14 |
