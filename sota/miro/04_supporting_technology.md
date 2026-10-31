# 04 — Supporting technology

> **Question answered here:** Which existing technology, tools, data and models can we reuse to build the framework (data intake, knowledge layer, learner, chatbot, simulator), and what does each mean for the project?
> Types: `[API]` `[platform]` `[library]` `[ontology/data]` `[dataset]` `[simulator]` `[model/service]` `[standard]` `[evidence]`. Impact: **High** = we should build on it; **Medium** = useful option; **Low** = reference only.

## Takeaways for our direction

1. **Data intake is solved by the OS layers.** Health Connect (Android) and HealthKit (iOS) cover most consumer wearables; phone context (activity, geofences) is a standard API. The legacy Fitbit Web API is being shut down in 2026: do not build on it.
2. **The knowledge layer can be loaded, not built.** BCIO/BCTO as OWL plus TaTT link data give the catalogue and the priors. Python RDF/OWL tooling is enough to query them at runtime.
3. **The learner is small code.** Bayesian Thompson sampling with pooling (HeartSteps/Oralytics style) is a few hundred lines and stays inspectable. Libraries help for baselines. StepCountJITAI and COMPLAPSE give a simulator starting point.
4. **Chatbot: deterministic flows plus LLM understanding.** Use structured dialogue flows (e.g. Rasa CALM, or our own state machine) for the intake and phase reviews, an LLM only for language understanding and MI reflections, and a safety checker. Free-form LLM health advice is unsafe in published red-team tests.
5. **Research platforms are heavy.** RADAR-base, mindLAMP and m-Path are useful as references or for a quick EMA pilot, but are overkill as the app's core.

## Miro cards

| ID | Finding / technology | Type | Reference | Impact on the project |
|---|---|---|---|---|
| T1 | Android Health Connect: on-device store and API for heart rate, steps, sleep and exercise from many wearables and apps | [API] | Android Developers, Health Connect | **High.** One integration covers Fitbit, Samsung, Garmin (via sync) and others. On-device = easier GDPR |
| T2 | Apple HealthKit: iOS equivalent with per-type user permissions | [API] | Apple Developer, HealthKit | **High** if we support iOS. Per-type permission fits modular, opt-in data |
| T3 | Google Health API replaces the legacy Fitbit Web API (legacy support ends 30 Sep 2026); restricted scopes need a security review | [API] | Google Health API docs; Fitbit community (2026) | **Medium.** Only for server-side wearable data. Prefer T1 for the prototype |
| T4 | Phone context APIs: activity recognition, geofencing, screen and app-use state | [API] | Android location and context APIs | **High.** Gives a "phone-only" data tier (Quit Sense-style location triggers) without a wearable |
| T5 | Cross-platform frameworks (Flutter / React Native) with health plugins (e.g. Flutter `health` package for Health Connect + HealthKit) | [library] | pub.dev `health`; framework docs | **Medium–High.** One codebase for both platforms; the agentic-coding-friendly route |
| T6 | Open mHealth schemas: open JSON schemas for mobile health data (heart rate, step count, survey answers) | [standard] | openmhealth.org | **Medium.** Use as an internal data model so data tiers stay swappable |
| T7 | RADAR-base: Apache-2.0 platform for passive sensing, wearables and questionnaires (Kafka-based) | [platform] | Ranjan et al. (2019) | **Low–Medium.** Too heavy for our app; good reference for the data pipeline and consent design |
| T8 | mindLAMP: open-source (BSD-3) digital-phenotyping + survey + intervention platform | [platform] | Vaidyam et al. (2022), JMIR mHealth (verify authors) | **Low–Medium.** Option for a quick sensing pilot; not our end-user app |
| T9 | m-Path: EMA / ecological momentary intervention platform from KU Leuven (proprietary, free tiers for research; verify) | [platform] | m-Path; momenTUM paper (2026) overview | **Medium.** Fastest way to run a short EMA diary study with smokers before our own app is ready |
| T10 | BCIO + BCTO as OWL (GitHub, BioPortal), CC BY 4.0 | [ontology/data] | HBCP ontologies GitHub; BioPortal | **High.** The intervention catalogue schema: each building block = BCTO IDs + mode of delivery + setting |
| T11 | Theory & Techniques Tool (TaTT): BCT ↔ mechanism-of-action links with evidence strength | [ontology/data] | Johnston et al. (2021) | **High.** Priors for the selector and source text for "why" explanations |
| T12 | Python ontology/graph tooling (owlready2, rdflib) for querying OWL at runtime | [library] | owlready2, rdflib docs | **Medium.** Enough to keep the knowledge layer live, with no triple store needed |
| T13 | HBCP interpretable outcome predictor for smoking-cessation interventions | [model/service] | Hastings et al. (2023/2025); West et al. (2023/2024) | **Medium.** Population-level prior on which BCT combinations work for which population |
| T14 | Thompson-sampling bandit designs with pooling and safety constraints, published with algorithm details (HeartSteps, Oralytics, MiWaves) | [evidence] | Liao et al. (2020); Trella et al. (2024); Ghosh et al. (2024); Tomkins et al. (2021) | **High.** Blueprint for the fast learner (building-block choice); copy the design, write our own small implementation |
| T15 | Bandit libraries: Vowpal Wabbit (contextual bandits), MABWiser | [library] | VW and MABWiser GitHub | **Low–Medium.** Baselines in simulation. Our own Bayesian model stays more explainable |
| T16 | StepCountJITAI: Gymnasium RL simulator with habituation, disengagement and between-person variability | [simulator] | Karine & Marlin (2024) | **High.** Start for our simulator; replace physical-activity dynamics with smoking dynamics |
| T17 | COMPLAPSE: computational lapse-risk model for smokers (R, GitHub), proposed for use in RL controllers | [simulator] | COMPLAPSE / CORDIS (2025) | **High.** Smoking dynamics for T16. Possible collaboration |
| T18 | UCL EMA + Fitbit lapse dataset (n = 38, 6,124 EMAs), participants consented to open sharing (repository to confirm) | [dataset] | Perski et al. (2024) | **Medium.** Calibrate the simulator and test the "what does each data tier add?" ablation |
| T19 | Structured conversational frameworks: Rasa Pro (CALM: LLM understanding + deterministic flows; free ≤ 1,000 conversations/month); Rasa Open Source in maintenance mode | [platform] | Rasa docs | **Medium–High.** Fits a schema-constrained intake and phase-review chatbot. Alternative: own state machine + LLM calls |
| T20 | LLM APIs and open-weight models for NLU, MI reflections and message variation | [model/service] | Brown et al. (2023); Haag et al. (2025) | **High** as a component, never the decision maker. Choose EU processing; log model version |
| T21 | LLM safety: physician red-teaming found many unsafe answers to patient questions across four major chatbots; crisis handling is inconsistent across models | [evidence] | arXiv:2507.18905 (2025); arXiv:2509.24857 crisis-handling evaluation (2025) | **High.** Requires guard-rails: constrained generation, a checker, crisis escalation to human help (Tabakstop, 1813) |

## Suggested reuse map (S2 components → technology)

| S2 component | Reuse | Build ourselves |
|---|---|---|
| Data tiers (EMA / phone / wearable) | T1, T2, T4, T5, T6 | Tier detection and graceful degradation logic |
| Intervention catalogue (BCT-coded building blocks) | T10, T11, T12 | Our own content, tagged with BCTO IDs |
| Phase estimation (HAPA) | Validated HAPA items ([01](01_research_topics.md) R6) | Rules + chatbot check-ins |
| Model / building-block selector | T14, T13 (priors), T15 (baselines) | Hierarchical Bayesian selector with explanations |
| Chatbot (intake, phase review, MI) | T19, T20 | Flows, prompts, safety checker (T21) |
| Simulator for showing learning | T16, T17, T18 | Smoking-specific environment and scenarios |
| Quick user-study instrument | T9 | — |
