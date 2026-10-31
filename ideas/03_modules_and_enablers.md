# 03 — Modules and enablers: what can be added to any core

> **Question answered here:** Which smaller features (modules) and supporting tools (enablers) are worth adding to whichever core we choose, and in what priority?
> Modules are user-facing building blocks. Enablers help *us* build or demonstrate the system. Each gets a priority tier: **Must** (part of any shortlist option), **Should**, **Could**, **Not now**.

## 1. Overview

| ID | Module / enabler | Type | Value for smokers | Evidence of content | Novelty | People-time cost | Tier |
|---|---|---|---|---|---|---|---|
| I15 | Evidence-based craving toolkit | Module | High | ●●● / ● | Medium | Low | **Must** |
| I16 | "Why am I seeing this?" + dark-logic monitor | Module | Medium–high | ○ / ● | High (G7) | Low | **Must** |
| I9 | Slip and recovery flow | Module | High | ●● | Medium | Low | **Must** |
| I17 | Conversational intake that sets priors | Module | Medium | ● | Medium–high (G9) | Medium | **Should** |
| I18 | Pre-quit trigger map from logging | Module | High | ●● | Low | Low | **Should** |
| I12 | Medication and quit-aid companion | Module | High | ●●● (aids) / ● (app support) | Low | Low | **Should** |
| I10 | LLM rendering layer ("the model decides, the LLM speaks") | Module | Medium | ● | Medium | Medium | **Could** |
| I11 | Simulation testbed (smoker simulator) | Enabler | — | — | Medium | Medium | **Should** |
| I13 | Buddy / supporter | Module | Medium | ● | Low | Medium | **Could** |
| I14 | Commitment contracts and incentives | Module | High | ●●● | Low | High | **Not now** |
| I7 | Pre-intender MI conversation | Module | High | ●● / ● | Medium | Medium | **Should** (see [02](02_core_directions.md#i7--pre-intender-module-a-constrained-mi-conversation)) |
| I1 | Notification timing / receptivity | Module | Medium | ● | Low | High (needs field data) | **Could** |

Evidence dots as in [sota/05](../sota/05_intervention_content.md): ●●● SR/MA or large RCT · ●● RCTs or mixed · ● pilot/lab · ○ theory.

## 2. Module notes

### I15 — Evidence-based craving toolkit
Options that the learner can choose between: a 3–5 minute **brisk walk or exercise snack** (Haasova et al., 2013; 2014), a **visuospatial puzzle** of ~3 minutes, from Elaborated Intrusion theory (Skorka-Brown et al., 2014; 2015; May et al., 2010), **urge surfing / ACT acceptance** (Bricker et al., 2020), **if-then plan recall**, a **call or message** to a supporter. It is the content that every shortlist option needs, and it supplies the arms of the experiments in H2.
- *Strong:* evidence-based and cheap to build. Gives distinct, measurable options.
- *Weak:* the Tetris effect comes from small studies. Craving relief is not abstinence.

### I16 — Explanation screen and dark-logic monitor
"Why am I seeing this?" on every suggestion, generated from the claims (I4), not from free LLM text. Plus light monitoring of unintended effects: guilt after a slip, annoyance at notifications, over-reliance on the app ("dark logic"; Bonell et al., 2015). Feeds back into the decision (e.g. fewer prompts when annoyance rises).
- *Strong:* empty cell (G7), cheap, evaluable in usability tests, central to the challenge. Users value control over automation in health apps (app-review study, arXiv 2208.10705) and transparency raises trust in persuasive systems (BCSS 2025, verify).
- *Weak:* risk of explanation overload. Faithfulness depends on the decision really being made by the claim layer.

### I9 — Slip and recovery flow
After a lapse, prevent the abstinence violation effect: no counter reset as punishment, reframing, analysis of what happened, a plan update, and a check of **recovery self-efficacy** (HAPA). Grounding: confidence after a first lapse predicts relapse (Shiffman et al., 2005, as cited in [sota/05](../sota/05_intervention_content.md)); first lapses cluster in high-risk situations (Shiffman et al., 1996). In our targeted search we found no trial of a dedicated *post-lapse* app flow; lapse-related work focuses on prevention (Quit Sense, Smart-T).
- *Strong:* a high-stakes moment that most apps handle badly. Easy to test with scenarios.
- *Weak:* little direct digital evidence; we rely on theory and EMA studies.

### I17 — Conversational intake that sets priors
Replace the onboarding questionnaire with a short MI-style conversation that maps answers onto **priors** in the claim layer (phase placement, likely triggers, preferred coping styles, data the user is willing to share). Cold start is the known weak point of per-user learners (HeartSteps used priors from earlier trial data; Liao et al., 2020).
- *Strong:* G9, useful in every option, short-study measurable (do the priors predict early choices?).
- *Weak:* mapping free text to priors needs validation; an LLM must be schema-constrained.

### I18 — Pre-quit trigger map
A few days of quick cigarette logging before the quit date (time, place, mood, company) → personal trigger map → the contexts in which the system should act. This is how Quit Sense learns smoking locations (Naughton et al., 2024) and BCT 2.3/4.2 in the HAPA sketch.
- *Strong:* proven, simple, gives data for I2 and for the experiments in H2.
- *Weak:* not new; logging adherence drops quickly.

### I12 — Medication and quit-aid companion
Information, a prompt to see a GP or pharmacist, and adherence reminders for varenicline, cytisine or combination NRT. Medication is the strongest lever and the least present in apps ([sota/01](../sota/01_evidence_base.md)). App-based adherence support is promising but preliminary: in a 2×2 feasibility RCT (n = 34), reminder recipients were adherent on more days (57.8 vs 39.9; Sifat et al., 2023), and a larger factorial trial is registered (NCT07099638). The Stop-Tabac app did not raise quit rates but did raise use of nicotine medication (Etter & Khazaal, 2022, verify).
- *Strong:* very high value per unit of effort; strong evidence for the aid itself.
- *Weak:* little novelty; must avoid giving medical advice (refer to professionals).

### I10 — LLM rendering layer
The transparent layer chooses *what* to do and *why*. The LLM only phrases the message and handles free conversation within that choice, with a checker. This answers the challenge's warning that LLM rationales are not explanations ([sota/04 §3](../sota/04_adaptive_learning_ai.md#3-conversational-agents-and-llms-in-smoking-cessation)). LLM-only decision-making (Haag et al., 2025) stays out of the core.
- *Strong:* natural language without giving up the white box.
- *Weak:* extra safety work; not a contribution in itself.

### I13 — Buddy / supporter
An invited supporter gets guidance on how to help. The SmokeFree Buddy trial (SWAPP) had **low engagement and low perceived usefulness** (JMIR, 2021, verify authors), reviews show no clear effect of partner or peer support interventions, and only 2.7% of Android cessation apps contain social-support content (same source). It is a good candidate *arm* in an experiment, not a pillar.

### I14 — Commitment contracts and incentives
High-certainty evidence for incentives (Notley et al., 2019). In the largest trial, deposit contracts were accepted by only 13.7% vs 90.0% for rewards, but among people who would accept either, deposits were more effective (Halpern et al., 2015). Needs money flows, CO verification hardware and ethics approval. **Not now**; mention it as a future extension and in the interviews.

## 3. Enablers

### I11 — Simulation testbed (smoker simulator)
A simulator of within-person craving and lapse dynamics, used to test the learner before any user sees it, as Oralytics did before deployment (Trella et al., 2024). Building blocks:
- **StepCountJITAI**: an open-source gymnasium simulator for physical-activity JITAIs with habituation and disengagement (Karine & Marlin, 2024). A design template.
- **COMPLAPSE**: an EU MSCA project (Tampere University, 2022–2025) that built a dynamic computational model of lapse risk in smokers (difference equations in R, code on GitHub) and explicitly proposes it for use inside an RL controller. Simulations reproduced relapse, prolapse and abstinence; validation against EMA/sensor data was ongoing (CORDIS, 2025).
- **Data to calibrate on**: the UCL EMA + Fitbit lapse dataset (n = 38, 6,124 EMAs; Perski et al., 2024; Leppin et al., 2026), whose participants consented to open data sharing (repository to be confirmed), and the public TU Delft virtual-coach dataset (Albers et al., 2022).
- *Value:* lets us show learning behaviour (cold start, convergence, effect of each data tier) honestly, and labels it as simulation. Potential collaboration: COMPLAPSE authors.
- *Risk:* simulations encode our own assumptions. Results must be presented as "the algorithm behaves sensibly", not as efficacy.

### Wizard-of-Oz and scenario studies
For any idea whose adaptivity cannot be shown live, a human operator can play the adaptive engine in a short study, or users can react to scripted day scenarios. We found no smoking JITAI evaluated this way, but it is standard HCI practice. It is cheap in software and expensive in people-time.

Sources: see [references.md](references.md).
