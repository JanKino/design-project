# 01 — Research topics, references and key findings

> **Question answered here:** Which research topics underpin a modular, HAPA-phased, BCT-coded app that chooses between interventions per person, and which findings matter most for it?
> Evidence tags as in [../README.md](../README.md#method-and-limitations): `[SR/MA]` `[RCT]` `[pilot]` `[obs]` `[guideline]` `[industry]` `[registry]` `[method]` (framework or method paper). Full entries in [references.md](references.md).

## Takeaways for our direction

1. **What drives effect is content and fit, not "being an app".** Apps as a category show no proven effect, while specific evidence-based programmes (ACT, CBT plus medication) do. This supports a framework whose job is to **pick and sequence proven content** (rows R1–R4).
2. **The theory backbone exists, but smoking apps have never been built on it.** HAPA is well supported across behaviours, and BCTTv1, BCIO and TaTT give a machine-readable BCT → mechanism layer. No smoking app uses this layer at runtime (R5–R9, gaps G1, G2 and G8).
3. **The learning machinery exists, but only for one flat decision.** Deployed bandits (HeartSteps, Oralytics, MiWaves) and one smoking RL coach (TU Delft) learn *one* choice. Learning *which intervention model per phase* is open (R12–R14, G1).
4. **Chatbots help delivery, not proven outcomes.** Use the chatbot for intake, phase-transition check-ins and motivational interviewing (MI) for pre-intenders. It is not the active ingredient (R15–R16).
5. **There is a ready-to-use content catalogue for the interchangeable building blocks:** exercise and visuospatial tasks for cravings, trigger-matched messages, lapse-recovery flows (R17–R19).

## Miro cards

| ID | Topic | Important finding | Reference | Type | Relevance for our project |
|---|---|---|---|---|---|
| R1 | Effect of digital cessation tools | SMS support has moderate-certainty benefit. Apps as a category: RR 1.00 (0.66–1.52) vs minimal support, low certainty | Whittaker et al. (2019) | [SR/MA] | Our value has to come from *which* content is delivered to *whom*, not from the app format |
| R2 | ACT-based apps | iCanQuit (ACT) beat NCI QuitGuide: 28.2% vs 21.1% 30-day abstinence at 12 months, n = 2,415 | Bricker et al. (2020) | [RCT] | ACT (acceptance) vs CBT (avoidance) coping is a natural pair of interchangeable sub-models for the action phase |
| R3 | Clinical guideline | First WHO cessation guideline: digital tools (SMS, apps, internet) as adjuncts or self-management, next to behavioural support and medication (varenicline, NRT, bupropion, cytisine) | WHO (2024) | [guideline] | Medication support and referral must be building blocks. Position the app as a complement to care |
| R4 | Financial incentives | High-certainty evidence that incentives raise long-term quit rates | Notley et al. (2019) | [SR/MA] | Candidate building block (non-monetary or CO-verified rewards) in the action and maintenance phases |
| R5 | HAPA model | Meta-analysis supports the HAPA paths: intention → planning → behaviour, with self-efficacy at each stage | Zhang et al. (2019); Schwarzer (2008) | [SR/MA] | Justifies HAPA as the phase backbone (motivational, volitional, maintenance and recovery) |
| R6 | Measuring HAPA in smokers | Validated HAPA scales for smoking cessation exist (e.g. Chinese smokers) | HAPA psychometrics (2024), Sci Rep | [obs] | Intake chatbot and check-ins can measure phase constructs with validated items instead of ad-hoc questions |
| R7 | BCT taxonomy | BCTTv1: 93 techniques in 16 groups. Trained coders identify BCTs reliably | Michie et al. (2013); Abraham et al. (2015) | [method] | Shared vocabulary for coding every app feature. Our "interchangeable building blocks" = sets of BCTs |
| R8 | BCT → mechanism links | Literature synthesis and expert consensus link BCTs to mechanisms of action. The online Theory & Techniques Tool (TaTT) gives each link with its evidence | Carey et al. (2019); Connell et al. (2019); Johnston et al. (2021) | [method] | Priors for the selector and the "why was this chosen?" explanation |
| R9 | Ontologies | BCIO (upper level + modules) and BCTO (successor to BCTTv1) are machine-readable OWL ontologies | Michie et al. (2021); Marques et al. (2023) | [method] | Runtime schema for the intervention catalogue. Nobody uses it inside an app yet (G2) |
| R10 | JITAI framework | JITAI components: decision points, tailoring variables, intervention options, decision rules, proximal outcomes | Nahum-Shani et al. (2018) | [method] | Vocabulary for the JITAI sub-module and for every "when to offer what" decision |
| R11 | Risk prediction | Six EMA items predict 80% of lapses within 4 h. Wearable risk peaks ~44 min before a lapse | Businelle et al. (2016); Ullah et al. (2022) | [pilot] [obs] | Lets the action-phase module work with EMA only and improve with a wearable (modular data, G5) |
| R12 | Online learning in mHealth | Thompson-sampling contextual bandits deployed in trials (HeartSteps, Oralytics, MiWaves). Pooling across users speeds up learning | Liao et al. (2020); Trella et al. (2024); Ghosh et al. (2024); Tomkins et al. (2021) | [RCT-embedded] | Proven engine for the fast "which building block" learner. Pooling solves part of the cold start |
| R13 | RL for smoking | TU Delft virtual coach learns which preparatory activity to propose per smoker; considers current and future states | Albers et al. (2022); PMC12512882 (2025) | [RCT-online] | Closest prior work. Learns *within* one phase, not across phases or models: this is our gap |
| R14 | Optimisation designs | MOST, factorial trials and SMART designs optimise components and sequences ("if no response at week 2, switch to X") | Collins (2018); Kimber et al. (2023) | [method] | Gives the formal logic for phase-dependent switching rules and how to evaluate them |
| R15 | Motivational interviewing chatbots | MI chatbot with generated reflections raised readiness to quit. GPT-4 reflections ~88% acceptable when checked | Brown et al. (2023); JMIR Mental Health (2024) | [pilot] | Pre-intender module plus the intake conversation, with a guard-rail checker |
| R16 | LLM chatbots for cessation | QuitBot (LLM Q&A + 42-day programme): good engagement, but the full RCT was null at 12 months (OR 0.96) | Bricker et al. (2024); NCT04308759 | [RCT] [registry] | The chatbot is the interface, not the treatment. Content and orchestration must carry the effect |
| R17 | Craving management | Short bouts of moderate exercise cut cravings acutely. 3-min visuospatial games (Tetris) cut craving ~20% | Haasova et al. (2013); Skorka-Brown et al. (2015) | [SR/MA] [RCT] | Interchangeable "craving SOS" blocks the selector can compare per user |
| R18 | Tailored messages | Trigger-matched messages outperformed generic ones in Smart-T | Hébert et al. (2020) | [pilot] | Content-selection rule and prior for the JITAI sub-module |
| R19 | Lapse and relapse | First lapses follow negative affect and falling abstinence confidence. Lapses predict relapse | Shiffman et al. (1996); Shiffman & Waters (2004) | [obs] | Recovery phase of HAPA needs its own sub-model (slip-recovery flow, recovery self-efficacy) |
| R20 | Engagement | Engagement is both behaviour and experience. "Effective engagement" matters, not maximum use | Perski et al. (2017); Yardley et al. (2016) | [SR] | The selector should optimise for useful engagement, not screen time |
| R21 | Interpretable models | Interpretable rule models match deep models for smoking-outcome prediction (HBCP). Interpretable models should be preferred in high-stakes settings | Hastings et al. (2023/2025); Rudin (2019) | [obs] [method] | Supports a white-box selector, which is required by our explainability principle |

## Research threads to watch (not yet strong enough for a card)

- **Smoking-specific JITAI meta-analysis:** not found. The closest is the substance-use JITAI review (Perski et al., 2022).
- **Sense2Stop primary results:** not found as of October 2026.
- **LLMs coding BCTs automatically:** we found no validated study. Human-coder reliability is the baseline (Abraham et al., 2015). ChatGPT reached κ 0.72–0.82 as a second coder in a related content-analysis task (JMIR, 2024). This matters if we want an LLM to tag new content with BCTs; treat it as unproven.
- **LLMs issuing JITAIs:** feasible in vignettes (Haag et al., 2025), not tested in the field.
