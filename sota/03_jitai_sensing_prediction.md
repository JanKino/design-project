# 03 — JITAIs, sensing and prediction of risk moments

> **Question answered here:** How far has research come with "the right support at the right moment" for smokers? What can be sensed, how well can risk be predicted, and what are the known hard problems (timing, context, content, receptivity)?

## 1. The JITAI framework (the vocabulary everyone uses)

A **Just-In-Time Adaptive Intervention** provides "the right type and amount of support, at the right time, by adapting to an individual's changing internal and contextual state" (Nahum-Shani et al., 2018). Its components are:

| Component | Meaning | Smoking example |
|---|---|---|
| **Distal outcome** | The ultimate goal | Sustained abstinence at 6 months |
| **Proximal outcome** | Short-term mediator the decision targets | No lapse in the next 2 hours. Craving down within 10 minutes |
| **Decision points** | When the system decides | Every 30 min, on a geofence entry, on a craving log |
| **Tailoring variables** | What the decision depends on | Stress, location, time since last cigarette, phase |
| **Intervention options** | What can be delivered, including *nothing* | Urge-surfing audio, if-then plan reminder, buddy prompt, no prompt |
| **Decision rules** | Mapping state → option | IF stress AND bar AND phase = actor THEN plan reminder |

Two states matter: **vulnerability/opportunity** (the person needs or can benefit from support) and **receptivity** (the person can receive, process and act on support right now) (Nahum-Shani et al., 2018). Most systems model the first and ignore the second.

Companion papers argue that classic behaviour theories are too **static** to drive JITAIs and need dynamic, time-varying formulations (Riley et al., 2011; Nahum-Shani, Hekler & Spruijt-Metz, 2015; Hekler et al., 2016).

## 2. What can be sensed (input modalities)

| Signal | How | What it says about smoking | Maturity |
|---|---|---|---|
| **Self-report EMA** (craving, mood, stress, alcohol, company, cigarette availability) | Short prompts several times a day | The strongest single predictors. Six EMA items predicted 80% of lapses within 4 h, at 17% false positives (Businelle et al., 2016) | Mature. Costs user burden |
| **Location (GPS, geofences, Wi-Fi)** | Phone | Learned "smoking places". Quit Sense learns these during a pre-quit logging phase (Naughton et al., 2024) | Mature technically, privacy-sensitive |
| **Phone movement / IMU** | Phone accelerometer, gyroscope | 1D-CNN-BiLSTM predicted smoking in the next 5 min with 85% accuracy (vs 63% for time-of-day rules), and post-quit craving/relapse with 78%, but n = 17 (Abo-Tabik et al., 2026) | Research, small samples |
| **Wrist gestures** (smartwatch IMU) | Detects hand-to-mouth puffing | Detection of *smoking as it happens*: Sense2Quit F1 ≈ 0.975 vs 15 confounding gestures (JMIR 2025), SmokeBeat, StopWatch, puffMarker (Saleheen et al., 2015) | Good in the lab and in pilots. Detects lapses, does not prevent them |
| **Physiology (HR, HRV, respiration)** | Chest band or smartwatch | Stress detection (cStress; Hovsepian et al., 2015). Used by Sense2Stop to time stress-management prompts | Chest bands are research-grade. Wrist HRV is noisier |
| **Heart rate only** | Smartwatch | "HeartIt" detects smoking from HR even when the watch is on the other hand (J. Comput. Sci. Technol., 2025) | Early |
| **Breath CO** | Bluetooth CO monitor | Objective verification of abstinence. Enables remote incentives (Pivot; CureApp; INSIGHT platform) | Commercial devices exist (e.g. Bedfont iCO) |
| **Phone use, calendar, app use, weather** | Phone APIs | Context for busyness, boredom and receptivity (Künzler et al., 2019; Mishra et al., 2021) | Mature APIs. Weakly validated for smoking |

**Important negative result:** in a 2026 feasibility project (n = 31), personalised sensor-triggered prompts **did not** capture higher-craving moments better than regular time-based prompts. For many participants, *time since the last cigarette* was the best predictor (m-Path blog, not peer-reviewed). Fancy sensing does not automatically beat simple temporal models.

## 3. Risk prediction: how good is it?

| Study | Data | Method | Result |
|---|---|---|---|
| Businelle et al. (2016) | 6 EMA items | Lapse-risk estimator | 80% of lapses flagged within 4 h. 17% FPR |
| mRisk — Ullah et al. (2022) | Wearable sensors + EMA, 92 participants, 1,012 days | Deep model with positive-only, incomplete labels | Risk peaks **~44 min before** a lapse |
| Abo-Tabik, Costen & Benn (2026) | Phone IMU, n = 17, 3.5 months | 1D-CNN-BiLSTM | 85% (smoking in 5 min). 78% (craving/relapse post-quit) |
| medRxiv preprint (2025) | EMA, varying prompt frequency | Random forest | Studies how many EMAs per day are needed for craving and lapse prediction |

**Reading:** prediction is *possible* and lead times of tens of minutes exist. But samples are small, models are trained on the same cohorts, and false positives mean **many unnecessary prompts**. Each prompt costs attention and risks annoyance (see §5).

## 4. Key JITAI systems for smoking

| System | Trigger logic | Content | Status / evidence |
|---|---|---|---|
| **Quit Sense** (Naughton, UK) | Learns the user's smoking contexts and locations pre-quit, then triggers support in those contexts after the quit date | Tailored behavioural support messages | Feasibility RCT, aOR 4.57 for verified abstinence (wide CI). Location triggers were limited by COVID (Naughton et al., 2023; 2024) |
| **Smart-T / Smart-T2 / OKquit** (Businelle, US) | 5 EMAs/day → lapse-risk level + active triggers | Messages matched to risk level and trigger, plus on-demand tools | Pilot RCT promising. Trigger-matched messages reduced that trigger more. OKquit RCT results pending (Hébert et al., 2020) |
| **Sense2Stop** (MD2K, US) | Wearable chest/wrist sensors → cStress → **micro-randomised** prompt or no prompt during stress vs non-stress | Stress-management exercise prompt | Micro-randomised trial, n = 75, completed (NCT03184389). Protocol by Battalio et al. (2021). We found no published primary results |
| **SmokeBeat / Sense2Quit** | Smartwatch detects smoking gestures | Notification / reminder after detected smoking | Detection validated. 2017 pilot: real-time feedback alone did not reduce smoking |
| **Q Sense / earlier work** (Naughton, 2016) | Geofencing | Development and acceptability work leading to Quit Sense | Development |

## 5. The known hard problems (these confirm the difficulties in our CLAUDE.md)

1. **Timing ≠ risk.** A high-risk moment is often a **low-receptivity** moment (in a bar with friends, driving, a stressful meeting). Receptivity depends on time of day, battery, screen state, activity and location (Künzler et al., 2019; Sahu et al., 2025). Mishra et al. (2021) deployed receptivity models *live* and improved response rates over random timing. This had not been done for smoking.
2. **Content selection is under-studied.** Most JITAIs optimise *whether/when* to send, with a fixed message. Smart-T is a notable exception: tailoring content to the active trigger worked better than generic content (Hébert et al., 2020).
3. **Prompt fatigue and habituation.** Notification burden lowers engagement. Users abandon apps whose notifications are irritating or intrusive. Extra messages in multiple formats can even backfire (see the review in the 2023 BMC Psychology notification paper). Little of this work is specific to smoking.
4. **Label scarcity and cold start.** Lapses are rare events and self-reported late. Craving labels require EMA, which itself burdens users.
5. **Effectiveness evidence is thin.** The JITAI review for substance use found mixed effectiveness and no poolable data (Perski et al., 2022). Smoking JITAIs are still at feasibility stage.
6. **Detection ≠ prevention.** Gesture detection finds a lapse *after* it starts. That is valuable for honest self-monitoring and for slip-recovery flows, less so for prevention.
7. **Modality heterogeneity.** Users have different devices, permissions and willingness to share. Systems in the literature assume a fixed sensor kit. **No system we found degrades gracefully across "EMA-only", "phone sensors" and "phone + wearable" users**, which is exactly our modularity requirement.

## 6. Proactive vs reactive support (the "steer before the craving" idea)

The CLAUDE.md idea of *steering behaviour before the craving arises* (distraction, initiating other activities) maps onto existing constructs:
- **Behaviour substitution and habit replacement** (BCT 8.2, 8.3): plan an alternative routine for a predicted trigger context.
- **Environmental restructuring / cue avoidance** (BCT 12.1, 12.3): for example, suggest a different route home when the user usually buys cigarettes.
- **Pre-emptive activity prompts**: brief physical activity reduces cravings acutely, with strong IPD meta-analytic evidence (Haasova et al., 2013) (see [05](05_intervention_content.md)).
- **Anticipatory if-then plan reminders** shortly *before* a predicted risk window. mRisk's ~44-minute lead time makes this technically conceivable (Ullah et al., 2022).

We found **no smoking JITAI that explicitly targets the pre-craving window with activity substitution**. Sense2Stop is closest, but its target is stress, not pre-emptive routine replacement.

## References for this file

- Abo-Tabik, M., Costen, N., & Benn, Y. (2026). Smartphone movement data can reliably predict smoking lapses and cravings to enable timely smoking cessation support. *Scientific Reports*. https://clok.uclan.ac.uk/52284
- Battalio, S. L., et al. (2021). Sense2Stop: A micro-randomized trial using wearable sensors to optimize a just-in-time-adaptive stress management intervention for smoking relapse prevention. *Contemporary Clinical Trials, 109*, 106534. https://pmc.ncbi.nlm.nih.gov/articles/PMC8556307
- Businelle, M. S., et al. (2016). An ecological momentary intervention for smoking cessation: Evaluation of feasibility and effectiveness. *Journal of Medical Internet Research, 18*(12), e321. https://www.jmir.org/2016/12/e321
- Haasova, M., et al. (2013). The acute effects of physical activity on cigarette cravings: Systematic review and meta-analysis with individual participant data. *Addiction, 108*(1), 26–37. https://ore.exeter.ac.uk/repository/handle/10871/13951
- Hébert, E. T., et al. (2020). Smart-T2 pilot RCT. *Journal of Medical Internet Research*. https://doaj.org/article/e2de0b88db9645598fca72f477639026
- Hekler, E. B., et al. (2016). Advancing models and theories for digital behavior change interventions. *American Journal of Preventive Medicine, 51*(5), 825–832. https://doi.org/10.1016/j.amepre.2016.06.013
- Hovsepian, K., et al. (2015). cStress: Towards a gold standard for continuous stress assessment in the mobile environment. *Proc. ACM UbiComp*, 493–504. https://doi.org/10.1145/2750858.2807526
- Künzler, F., et al. (2019). Exploring the state-of-receptivity for mHealth interventions. *Proc. ACM IMWUT, 3*(4), 140. https://doi.org/10.1145/3369805
- m-Path (2026). How passive sensing can personalize ESM/EMA prompting (blog, not peer-reviewed). https://m-path.io/blog/how-passive-sensing-can-personalize-esm-ema-prompting-37/
- Mishra, V., et al. (2021). Detecting receptivity for mHealth interventions in the natural environment. *Proc. ACM IMWUT, 5*(2), 74. https://arxiv.org/abs/2011.08302
- Nahum-Shani, I., Hekler, E. B., & Spruijt-Metz, D. (2015). Building health behavior models to guide the development of just-in-time adaptive interventions: A pragmatic framework. *Health Psychology, 34*(S), 1209–1219. https://pmc.ncbi.nlm.nih.gov/articles/PMC4732268
- Nahum-Shani, I., Smith, S. N., Spring, B. J., Collins, L. M., Witkiewitz, K., Tewari, A., & Murphy, S. A. (2018). Just-in-time adaptive interventions (JITAIs) in mobile health: Key components and design principles for ongoing health behavior support. *Annals of Behavioral Medicine, 52*(6), 446–462. https://doi.org/10.1007/s12160-016-9830-8
- Naughton, F., et al. (2016). A context-sensing mobile phone app (Q Sense) for smoking cessation: A mixed-methods study. *JMIR mHealth and uHealth, 4*(3), e106. https://doi.org/10.2196/mhealth.5787
- Naughton, F., et al. (2023; 2024). Quit Sense feasibility RCT — see [01](01_evidence_base.md).
- Perski, O., et al. (2022). JITAIs to reduce harmful substance use: systematic review. *Addiction, 117*(5), 1220–1241. https://doi.org/10.1111/add.15687
- Riley, W. T., et al. (2011). Health behavior models in the age of mobile interventions: Are our theories up to the task? *Translational Behavioral Medicine, 1*(1), 53–71. https://doi.org/10.1007/s13142-011-0021-7
- Sahu, et al. (2025). Real-world receptivity to adaptive mental health interventions: Findings from an in-the-wild study. arXiv:2508.02817. https://arxiv.org/abs/2508.02817
- Saleheen, N., et al. (2015). puffMarker: A multi-sensor approach for pinpointing the timing of first lapse in smoking cessation. *Proc. ACM UbiComp*, 999–1010. https://doi.org/10.1145/2750858.2806897
- Sense2Quit smartwatch smoking-gesture validation (2025). *Journal of Medical Internet Research*. https://doaj.org/article/1721c3571a1b48b38ff4f9300d1cd8db
- SmokeBeat pilot — "Effect of real-time monitoring and notification of smoking episodes on smoking reduction" (2017), *Nicotine & Tobacco Research* (NAQC summary). https://www.naquitline.org/news/374303/
- Ullah, M. A., et al. (2022). mRisk: Continuous risk estimation for smoking lapse from noisy sensor data with incomplete and positive-only labels. *Proc. ACM IMWUT*. https://digitalcommons.memphis.edu/facpubs/18011
- Notification burden evidence: BMC Psychology (2023) s40359-023-01430-w. https://www.iris.unict.it/retrieve/2dec812f-a5b5-4c06-a906-8468c9a5ac98/s40359-023-01430-w.pdf
- Optimising supervised ML predicting cravings and lapses for a smoking JITAI (2025). *medRxiv*. https://www.medrxiv.org/content/10.1101/2025.08.07.25333190
