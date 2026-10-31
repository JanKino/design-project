# Progress tracker

Living status of the project. Update at the end of every work session. Stable context (goal, scope, conventions, file structure) is in [claude.md](claude.md).

**Current phase:** 2 → 3 transition. Direction chosen: close to S2. S2-focused SOTA deep dive for the Miro board done ([sota/miro](sota/miro/README.md)).
**Next action:** team reviews `sota/miro/` and imports the CSVs into Miro. Decide the e-cigarette stance (O5). Then scope phase 3 with the agent (grill first).

---

## Phase checklist

### Phase 0 — Setup ✅
- [x] Challenge background collected ([samenvatting](samenvatting%20Why_Should_This_Work_studenten_NL.md), [Challenges 26-27.pdf](Challenges%2026-27.pdf) #6)
- [x] Early AI-assisted sketches of direction B ([HAPA sketch](HAPA%20Quit%20App%20—%20Sub-models%20and%20BCTs%20per%20Stage.md), [JITAI architecture](jitai_smoking_cessation_architecture.md))

### Phase 1 — SOTA analysis ✅ (31 Oct 2026)
- [x] Evidence base for digital cessation → [sota/01](sota/01_evidence_base.md)
- [x] App landscape and feature matrix → [sota/02](sota/02_app_landscape.md)
- [x] JITAI, sensing, risk prediction, receptivity → [sota/03](sota/03_jitai_sensing_prediction.md)
- [x] Adaptive learning / AI (bandits, RL, LLMs, HBCP) → [sota/04](sota/04_adaptive_learning_ai.md)
- [x] Intervention content catalogue → [sota/05](sota/05_intervention_content.md)
- [x] Theory and ontologies (HAPA, COM-B, BCTTv1, BCIO, TaTT) → [sota/06](sota/06_theory_ontologies.md)
- [x] Gap analysis G1–G9 → [sota/07](sota/07_gap_analysis.md)
- [ ] Team review of the SOTA
- [ ] Check citations marked "verify" before using them in a formal report
- [x] S2 deep dive in Miro categories (research, competition, IPR & rights, technology, market, other, references) → [sota/miro](sota/miro/README.md) (31 Oct 2026)
- [ ] Import `sota/miro/csv/` into the Miro board

### Phase 2 — Ideas and direction ◐ (analysis done 31 Oct 2026; vote pending)
- [x] Scope phase 2 with the user
- [x] Scoring framework + sensitivity analysis → [ideas/01](ideas/01_scoring_framework.md)
- [x] Critiqued core directions I1–I8 → [ideas/02](ideas/02_core_directions.md)
- [x] Modules and enablers I9–I18 with priority tiers → [ideas/03](ideas/03_modules_and_enablers.md)
- [x] Hybrids H1–H3 and comparison matrix → [ideas/04](ideas/04_hybrids_and_comparison.md)
- [x] Shortlist S1–S3 for the team vote → [ideas/05](ideas/05_shortlist_for_vote.md)
- [x] S4 / H4 added (HAPA rule scaffold + learning JITAI linked to planner and progress) after discussing whether a JITAI needs an orchestrator
- [x] Team vote → direction close to S2 (see decision log)
- [ ] Check citations marked "verify" in [ideas/references.md](ideas/references.md)

### Phase 3 — Refinement ⏳
- [ ] Choose the theory backbone (HAPA vs alternatives) with sources
- [ ] Sub-models / program theories per phase, and interchangeable building blocks
- [ ] Feature ↔ BCT ↔ mechanism-of-action mapping (BCTTv1 / BCIO / TaTT)
- [ ] Learning design (what is learned, at which level, cold start)
- [ ] Explanation design ("why am I seeing this?") and dark-logic monitoring

### Phase 4 — Validation and prototype ⏳
- [ ] Stakeholder interviews: smokers/ex-smokers, Tabakstop tabacologist, Ghent Health Psychology Lab
- [ ] Prototype
- [ ] Usability tests

---

## Decision log

| Date | Decision | Reason / source |
|---|---|---|
| 2026-10-31 | Focus on a usable app for smokers, not a research framework | User brief ([claude.md](claude.md)) |
| 2026-10-31 | Explainability is a design requirement; science-based reasoning over pure statistics | SOTA scoping ([sota/README](sota/README.md#scope-agreed-with-the-team)) |
| 2026-10-31 | Modular data sources: EMA, phone, wearable, each optional | SOTA scoping |
| 2026-10-31 | Evaluation limited to interviews and usability tests | SOTA scoping |
| 2026-10-31 | Phase 1 delivered as a structured narrative review, not PRISMA | [sota/README](sota/README.md#method-and-limitations) |
| 2026-10-31 | Evaluation widened: small, short user studies with smokers allowed if feasible; still no large data collection | Phase 2 scoping |
| 2026-10-31 | Phase 2 criteria: novelty, value for smokers, feasible + demonstrable as top weights; outcome = top 3 for a team vote | Phase 2 scoping ([ideas/01](ideas/01_scoring_framework.md)) |
| 2026-10-31 | Narrow deep JITAI (I1) not recommended as the core; kept as a delivery module | [ideas/02](ideas/02_core_directions.md#i1--deep-jitai-the-right-notification-at-the-right-moment-direction-a-narrow) |
| 2026-10-31 | **Direction: close to S2.** Modular framework on a BCT taxonomy, rooted in a HAPA phase plan; chooses between phase-dependent interventions (ideally all effective existing digital interventions); chatbot for intake and phase-transition reviews | Team decision, reported by Jan |
| 2026-10-31 | S2 deep dive: Markdown + CSV for Miro, global market scope, ~10–20 cards per category, regulation filed under IPR | Scoping of the deep dive ([sota/miro](sota/miro/README.md)) |

## Open questions

- **Within S2:** should the top level (phase/module choice) learn, or follow explicit rules first (the S4 variant)? See [ideas/05](ideas/05_shortlist_for_vote.md#questions-that-should-decide-the-vote).
- **E-cigarette stance:** support switching to e-cigarettes as a path or not? E-cigs are the most-used and an effective aid ([sota/miro/06](sota/miro/06_other_findings.md) O5).
- Licence of BCTTv1 label/definition text and of each intake questionnaire ([sota/miro/03](sota/miro/03_ipr_and_rights.md) P8–P9); UGent rules on student IP (P19).
- Ethics procedure and lead time for a short study with smokers (affects S1 most).
- Access to the UCL EMA + Fitbit lapse dataset (Perski et al., 2024) and the COMPLAPSE model code; contact the authors?
- How do we demonstrate learning? Partly answered: a short self-experiment study (S1), simulation built on StepCountJITAI / COMPLAPSE (all options), public datasets (S3). See [ideas/03 §3](ideas/03_modules_and_enablers.md#3-enablers).
- Which expert partners can we involve (Ghent Health Psychology Lab, Tabakstop), and what is in it for them?
- How closely do we stick to the official challenge #6 deliverables vs our app-focused angle?
- Not found in the SOTA: Sense2Stop primary results, full QuitBot paper, OKquit results, a smoking-specific JITAI meta-analysis.

## Session log

| Date | Who | What | Output |
|---|---|---|---|
| 2026-10-30 | Jan + AI | Early direction-B sketches | Root sketch files |
| 2026-10-31 | Jan + Claude | Phase 1 SOTA analysis | `sota/` (9 files), commit `f6aa4a7` |
| 2026-10-31 | Jan + Claude | Project tracking set up | Agent notes in `claude.md`, this file |
| 2026-10-31 | Jan + Claude | Phase 2 ideas and shortlist | `ideas/` (7 files) |
| 2026-10-31 | Jan + Claude | Discussion "does a JITAI need an orchestrator?" → added H4 / S4 | ideas/01, 04, 05, README, references |
| 2026-10-31 | Jan + Claude | Direction ≈ S2 recorded; S2 SOTA deep dive in six Miro categories + references | `sota/miro/` (8 files + csv/) |
