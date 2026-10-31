# Phase 2 — Ideas and direction

A critiqued list of project directions for the adaptive smoking-cessation app, built on the SOTA in [../sota/](../sota/README.md). It ends in a **shortlist for a team vote** (three options, plus a fourth added after discussion).
Compiled 31 Oct 2026.

## Scope agreed with the user

| Topic | Choice |
|---|---|
| Capacity | 5–6 people, a bit more than one semester. Agentic coding makes software cheap; **people-time for prototypes and user tests is the bottleneck** |
| Main criteria | Novelty vs SOTA, value for smokers, feasible + demonstrable (equal top weight). Challenge fit, evidence, extensibility and risk count less |
| User testing | Small, short studies with smokers are possible. Large data collection is not. Simulation and public data are allowed |
| Breadth | SOTA candidates + new ideas + hybrids, with targeted extra searches |
| Outcome | Top 2–3 for a team vote (not a single choice) |

## File structure

```
ideas/
├── README.md                     ← you are here: scope, file map, summary
├── 01_scoring_framework.md       ← criteria, weights, constraints, sensitivity analysis
├── 02_core_directions.md         ← I1–I8: candidate cores, each with strong/weak points and a score
├── 03_modules_and_enablers.md    ← I9–I18 + enablers: add-ons with priority tiers (Must/Should/Could/Not now)
├── 04_hybrids_and_comparison.md  ← H1–H4, full score matrix, gap coverage
├── 05_shortlist_for_vote.md      ← S1–S4: concrete project sketches + questions that should decide the vote
└── references.md                 ← sources for this phase (new ones marked)
```

Suggested reading order: **README → 05 (shortlist) → 04 (comparison)**, then 02/03 for the arguments behind each score.

## ID scheme

- **I1–I18**: single ideas (I1–I8 cores in [02](02_core_directions.md), I9–I18 modules in [03](03_modules_and_enablers.md), I11 is an enabler).
- **H1–H4**: hybrids ([04](04_hybrids_and_comparison.md)). H4 was added after the first shortlist.
- **S1–S4**: shortlist options for the vote ([05](05_shortlist_for_vote.md)). S1 = H2, S2 = H1, S3 = H3, S4 = H4.
- Gaps keep their SOTA IDs **G1–G9** ([../sota/07](../sota/07_gap_analysis.md)).

## Summary

1. **A narrow deep JITAI (I1) should not be the core.** Timing is the most crowded part of the field and needs field data to demonstrate. It scores last under every weighting (2.32).
2. **The new variant of direction A, pre-craving steering (I2), is novel and well grounded**, but prevention cannot be shown without field data, and users react slowly (~64 min mean engagement delay in Quit Sense) compared with the forecast lead time (~44 min in mRisk).
3. **Direction B (HAPA orchestrator, I3) is a strong frame but needs an engine.** Paired with a claim-updating knowledge layer (I4) it becomes H1, the most complete answer to challenge #6 (4.07). Its learning can only be shown in simulation within our window.
4. **New idea: personal experiments (I6).** The smoker and the app run short randomised try-outs of coping options. Craving relief moves within minutes, so per-person learning is **visible in a 1–2 week user study**. Self-experimentation systems exist for sleep and IBS (SleepCoacher, SleepBandits, TummyTrials) but **not for smoking coping**. The only smoking precedent is a motivational, non-learning pilot (Heffner et al., 2020).
5. **Shortlist for the vote:**
   - **S1 Quit Lab (H2, 4.32):** personal experiments + claim layer + light HAPA shell. Best demonstrability with real users.
   - **S2 White-box HAPA coach (H1, 4.07):** full-journey orchestrator with the theory inside. Best challenge fit and extensibility.
   - **S3 One step ahead (H3, 3.75):** anticipatory steering with modular sensing. Most novel version of direction A.
   - **S4 HAPA scaffold + learning JITAI (H4, 4.07; added after team discussion):** planner, JITAI and progress linked through a shared user model; HAPA as explicit rules on top; learning in the JITAI, which can remind users of their own plans. Most complete *usable app* whose learning can still be shown with users.
6. **The ranking is robust**: S1/S2 lead under all five weightings tested. S4 ties S2 under the main and equal weightings and passes it when feasibility or value for smokers weighs more ([01 §3](01_scoring_framework.md#3-sensitivity-analysis)).
7. **Shared by every option:** claims with provenance, an evidence-based craving toolkit (exercise, visuospatial puzzle, urge surfing, if-then plans), "why am I seeing this?" with dark-logic monitoring, a slip-recovery flow, and self-report-only operation.
8. **Agent's lean:** S1, designed to grow towards S2; S4 if the team prefers a complete app over one sharp contribution (S1 and S4 share their learning engine). Reasons and counter-arguments are in [05](05_shortlist_for_vote.md#agents-lean-for-transparency-not-a-decision).

## New sources found in this phase (highlights)

- Self-experimentation systems: SleepCoacher, SleepBandits, TummyTrials, StudyMe; smoking "personal experiments" pilot (Heffner et al., 2020).
- Simulation: StepCountJITAI (gymnasium JITAI simulator); **COMPLAPSE**, a computational lapse-risk model for smokers with open R code (MSCA, Tampere, 2022–2025). This is a possible collaboration and calibration source.
- Multi-component RL with one agent per component (Xu et al., 2025), in simulation, outside smoking.
- LLM cessation chatbot RCTs underway (HKU Quit to Win 2025/2026). This area is crowded and moving fast.
- Data: UCL EMA + Fitbit lapse dataset (n = 38; Perski et al., 2024), participants consented to open sharing.
- Evidence checks: deposit contracts have very low uptake (13.7%; Halpern et al., 2015); a buddy app had low engagement (SWAPP); app medication-adherence support is preliminary (Sifat et al., 2023).

## Limitations

- Scores are reasoned judgements, not measurements ([01 §4](01_scoring_framework.md#4-caveats)).
- Targeted searches, not systematic. Several new entries are marked "verify" in [references.md](references.md).
- Ethics approval for any study with smokers is not yet scoped; its lead time affects S1 most.

## Next steps

1. Team reads [05](05_shortlist_for_vote.md) and votes. Record the decision in [../PROGRESS.md](../PROGRESS.md).
2. Check the ethics procedure and timeline for a short study with smokers.
3. Contact potential partners: Ghent Health Psychology Lab, Tabakstop, and possibly the COMPLAPSE / UCL authors for model and data access.
4. Phase 3 (refinement) for the chosen option: theory backbone, claim schema, BCT ↔ feature ↔ MoA mapping, learning and explanation design.
