# SOTA analysis — adaptive smoking-cessation app

State-of-the-art analysis for our design project: an intelligent, adaptive smoking-cessation app that combines established behaviour-change mechanisms with per-user learning.
Compiled 31 Oct 2026. Phase 1 of the plan in [../claude.md](../claude.md): **SOTA only**. The ideas list and direction choice come in phase 2.

## Scope agreed with the team

| Decision | Choice |
|---|---|
| Scope of this run | SOTA only: what exists, what is missing, what research is not yet implemented |
| Role of the "Why Should This Work?" challenge | Grounded in science and **explainable** ("why was this chosen?"). BCT ontologies may be used but are not required. Logical, science-based reasoning is preferred over purely statistical methods |
| Data sources | Self-report/EMA, phone sensors and consumer wearables, **modular**: the app must also work when a user provides only some of them |
| Evaluation possible during the project | Interviews and usability tests only (no field deployment) |

## File structure

```
sota/
├── README.md                        ← you are here: scope, file map, summary, method
├── 01_evidence_base.md              ← Do digital cessation tools work? Cochrane, key RCTs, what drives effect
├── 02_app_landscape.md              ← Which apps exist, feature × mechanism matrix, Belgian context, saturation
├── 03_jitai_sensing_prediction.md   ← JITAI framework, sensing modalities, risk prediction, receptivity, hard problems
├── 04_adaptive_learning_ai.md       ← Rules, MRTs, bandits/RL, MOST, HBCP, chatbots/LLMs, explainability
├── 05_intervention_content.md       ← Catalogue of deliverable building blocks + evidence + under-used research
├── 06_theory_ontologies.md          ← HAPA, COM-B, PRIME, TTM; BCTTv1, BCIO, TaTT; causal pies, dark logic
├── 07_gap_analysis.md               ← Done/not-done matrix, gaps G1–G9, ready-to-implement research, notes on our sketches
└── references.md                    ← Consolidated bibliography (all files)
```

Suggested reading order: **README → 07 (gaps) → 02 (market) → 01 (evidence)**, then 03–06 as background for whichever direction we choose.

## Summary in 10 points

1. **Apps as a category are unproven.** The Cochrane review finds RR 1.00 for apps vs minimal support (low certainty). Text messaging has moderate-certainty benefit. Some *specific* apps work: iCanQuit (ACT) beat QuitGuide, 28% vs 21% at 12 months. → [01](01_evidence_base.md)
2. **Content and engagement drive effects, not features.** Trackers and badges are saturated and have weak evidence. Strong ingredients (medication, incentives, ACT/CBT content) are under-delivered. → [01](01_evidence_base.md), [02](02_app_landscape.md), [05](05_intervention_content.md)
3. **Context-aware smoking JITAIs exist only as research prototypes** (Quit Sense, Smart-T, Sense2Stop), at feasibility or pilot stage, with promising but imprecise results. → [03](03_jitai_sensing_prediction.md)
4. **Risk prediction is feasible but noisy.** It works with 6 EMA items (80% of lapses), wearables (risk peaks ~44 min before a lapse) and phone IMU (small n). Simple temporal models are hard to beat. → [03](03_jitai_sensing_prediction.md)
5. **Receptivity is ignored in smoking JITAIs**, although live receptivity models exist in other domains. → [03](03_jitai_sensing_prediction.md)
6. **Online learning (bandits) is deployed in mHealth** (HeartSteps, Oralytics, MiWaves for cannabis), but **not yet in smoking cessation**, and always on *one flat decision*. → [04](04_adaptive_learning_ai.md)
7. **LLM chatbots improve delivery, not proven outcomes.** QuitBot's full RCT was null. LLMs cannot serve as the "why" layer on their own. → [04](04_adaptive_learning_ai.md)
8. **The machine-readable theory layer exists** (BCTTv1, BCIO, TaTT with provenance, HBCP interpretable predictor), but **no app uses it at runtime**, and no system updates its claims with user data. → [06](06_theory_ontologies.md)
9. **Biggest open cells:** orchestration across intervention types and phases (G1), learning that updates explicit claims (G2), joint risk × receptivity × content (G3), pre-craving steering (G4), modular sensing (G5), user-facing explanations and dark-logic monitoring (G7). → [07](07_gap_analysis.md)
10. **Under-used research ready for implementation:** exercise for cravings, visuospatial distraction, trigger-matched content, ACT vs avoidance per person, MI for pre-intenders, medication adherence nudges, CO-verified rewards. → [05](05_intervention_content.md), [07](07_gap_analysis.md)

## Method and limitations

- **Search:** web and literature search (Cochrane, PubMed/PMC, JMIR, ACM IMWUT/CHI, arXiv/medRxiv, trial registries, vendor and app-store pages), October 2026. This is a *structured narrative review*, not a PRISMA systematic review.
- **Evidence tags** (`[SR/MA]`, `[RCT]`, `[pilot]`, `[obs]`, `[industry]`, `[registry]`, `[vendor]`) mark the strength and independence of each claim.
- **Verify before formal citation:** some bibliographic details (exact year or volume for online-first papers, a few author lists marked "verify") were taken from abstracts and indexes rather than full texts. Commercial feature descriptions come from public listings and change often.
- **Not found / open:** published primary results of Sense2Stop, the full QuitBot paper (only registry results), OKquit results, and any smoking-specific JITAI meta-analysis.

## Next steps

1. **Phase 2 (ideas):** a critiqued list of project directions with strong and weak points and a concluding recommendation. It should cover the two current candidates (deep JITAI vs HAPA orchestration framework) and alternatives revealed by the gaps (e.g. claim-updating knowledge layer, proactive steering module, modular-sensing JITAI, pre-intender MI module, coach/tabacologist-augmentation tool).
2. **Phase 3 (refinement):** pick the theory backbone (HAPA vs alternatives), the sub-models per phase, the BCT ↔ feature ↔ MoA mapping (BCIO/TaTT), and the learning and explanation design.
3. **Stakeholder interviews:** smokers and ex-smokers, a Tabakstop tabacologist, health-psychology students and researchers (Ghent Health Psychology Lab).
