# 02 — Core directions: what the project could be *about*

> **Question answered here:** Which candidate directions could form the core of the project, and what are each one's strong and weak points measured against the SOTA and our constraints?
> A *core direction* defines the project's main contribution. Add-on features are in [03](03_modules_and_enablers.md). Combinations are in [04](04_hybrids_and_comparison.md).
> Scores: N novelty · V value for smokers · F feasible + demonstrable · C challenge fit · E evidence of content · X extensibility · R risk (5 = low risk). See [01](01_scoring_framework.md).

---

## I1 — Deep JITAI: the right notification at the right moment (direction A, narrow)

**Idea.** Optimise *whether, when and what* to send at risk moments, using EMA, phone and wearable data, with a per-user contextual bandit over notification content and timing. Novelty would come from combining risk × receptivity × content in one decision (G3).

**Closest existing work.** Quit Sense (location-triggered support; Naughton et al., 2024), Smart-T (EMA risk tiers + trigger-matched content; Hébert et al., 2020), Sense2Stop (stress-triggered MRT; Battalio et al., 2021), HeartSteps / Oralytics / MiWaves bandits in other domains (Liao et al., 2020; Trella et al., 2024; Ghosh et al., 2024), live receptivity models (Mishra et al., 2021).

| Strong points | Weak points |
|---|---|
| Clear, well-defined ML problem; strong methods literature to build on | The "when" problem is the **most crowded** part of the field. Combining three known threads is incremental |
| Directly matches what the team first had in mind | Timing models need **field data to show they work**. Public smoking EMA datasets are small (e.g. n = 38; Perski et al., 2024) and lack receptivity labels |
| Bandit machinery is mature | Simple temporal predictors are hard to beat (m-Path, 2026, not peer-reviewed), so a big model may show no gain |
| | Notifications are what users find most annoying (BMC Psychology, 2023). The value for smokers depends on getting the timing right, which we cannot prove |
| | Passive sensing raises privacy issues; does not by itself address explainability (C) |

**How we could show it.** Offline policy evaluation on a public EMA dataset and a simulator ([I11](03_modules_and_enablers.md#i11--simulation-testbed-smoker-simulator)). Usability of notification content only.

**Score.** N2 V3 F2 C2 E3 X2 R2 → **2.32** (last).
**Verdict.** Not recommended as the core. The useful parts (trigger-matched content, receptivity) survive as a delivery module inside other directions.

---

## I2 — Pre-craving steering: act *before* the urge (direction A, new angle)

**Idea.** Predict personal high-risk windows (from logged routines, time, location, calendar, optionally wearables) and **steer before the craving builds**: suggest a substitute activity (a brisk 5-minute walk, a call, a different route home), restructure the situation, or rehearse the if-then plan. This is the user's "subconscious steering" idea, made explicit.

**Grounding.** Brief moderate activity reduces desire to smoke acutely (IPD meta-analysis; Haasova et al., 2013; 2014). Behaviour substitution and habit replacement are BCTs 8.2 / 8.3 (Michie et al., 2013). Wearable risk peaks ~44 min before a lapse (mRisk; Ullah et al., 2022). We found no smoking JITAI that targets the pre-craving window with substitution ([sota/03 §6](../sota/03_jitai_sensing_prediction.md#6-proactive-vs-reactive-support-the-steer-before-the-craving-idea)).

| Strong points | Weak points |
|---|---|
| **Genuinely new** in smoking (G4) and easy to explain to users and experts | Needs a risk forecast with lead time. Lead-time evidence comes from one research-grade sensor study (mRisk) |
| Builds on strong acute evidence (exercise) and familiar BCTs | **Response latency is long**: Quit Sense users took on average 64 min to engage after a just-in-time notification, and only 50% opened within 30 min (Naughton et al., conference abstract, verify). That is longer than the 44-min lead time |
| Positive framing ("do this") instead of warnings | Effect of an *anticipatory* nudge is untested; a prompt in a calm moment may simply be ignored |
| Routine-based prediction (from a pre-quit log, as in Quit Sense) works without wearables | Proving prevention requires field data (F2) |

**How we could show it.** Diary-based routine model from a 1-week logging period; scenario walk-throughs and a short field-lite test of acceptability and timing; offline evaluation of the forecast on public data.

**Score.** N5 V4 F2 C3 E4 X3 R3 → **3.54**.
**Verdict.** Strong idea, weak demonstrability on its own. Best kept as a decision type (an experiment type in H2, or the JITAI slot of H1), or as the core of H3.

---

## I3 — HAPA orchestrator over interchangeable sub-models (direction B)

**Idea.** HAPA defines phases (pre-intender, intender, actor, maintainer, with fall-back). For each phase the system holds several program theories / sub-models (e.g. ACT acceptance vs CBT avoidance coping, buddy vs self-regulation), each realised by interchangeable features coded with BCTs. A learner chooses at several levels: sub-model per phase, building block within a sub-model, and possibly the delivery details. This is the direction in the root sketches.

**Grounding.** HAPA meta-analysis across behaviours (Zhang et al., 2019); validated smoking HAPA scales (Scientific Reports, 2024). Stage-based apps use fixed stage → content maps; no deployed system learns *across* intervention types and phases (G1; [sota/04 §2](../sota/04_adaptive_learning_ai.md#2-deployed-online-learning-in-mhealth-lessons)). The closest technical precedent is multi-agent RL with one agent per intervention component at its own timescale, so far only in simulation for medication adherence (Xu et al., 2025). We found **no smartphone smoking trial built explicitly on HAPA** (targeted search, Oct 2026), which supports G8.

| Strong points | Weak points |
|---|---|
| Fills the emptiest cells: G1, G8, and with explanations G7 | **Breadth risk**: many modules, each thin. Without a real learning and explanation layer it looks like "yet another stage-based app" |
| Covers the whole journey, including pre-intenders (≈80% of smokers are ambivalent) | Phase-level learning is **slow**: the feedback for "was ACT the right sub-model?" comes over weeks. It cannot be shown in a short user study, only in simulation |
| Natural fit for the challenge (phase is part of the model, claims carry phase conditions) and for psychologists | HAPA evidence for smoking *apps* is thin; our design would rest on transfer from other behaviours |
| Every other idea fits inside it as a module (X5) | Hierarchical action spaces with few users are a hard learning problem; risk of over-engineering |

**How we could show it.** Walk-throughs of the full journey with smokers and a tabacologist; simulation of the learner; per-phase usability tests.

**Score.** N4 V4 F3 C5 E3 X5 R4 → **3.86**.
**Verdict.** A strong *frame*, but on its own the contribution is architectural. It becomes convincing when paired with a demonstrable learning layer (→ H1).

---

## I4 — Claim-updating knowledge layer: a personal program theory that learns

**Idea.** Store the program theory as explicit **claims**: "BCT X → mechanism M → behaviour B, for this person, in phase P and context C", each with a prior and its **provenance** (TaTT literature/expert links, trial evidence). Represent sufficient bundles (causal pies), not only single arrows. User data updates the claims (Bayesian), and the app explains its choices from the claims ("we suggested the walk because your data now support it for evening cravings; breathing exercises went down from 0.6 to 0.2").

**Grounding.** BCIO and the BCT–MoA links with provenance exist in machine-readable form (Michie et al., 2021; Johnston et al., 2021). Interpretable, ontology-structured prediction works at trial level (Hastings et al., 2023/2025). Bayesian bandit posteriors are inspectable (Liao et al., 2020). Nobody has connected the three (G2). Scrutable user models (the user can inspect and correct what the system believes about them) are an established HCI concept that has not been used in cessation apps (Kay & Kummerfeld, 2012, verify).

| Strong points | Weak points |
|---|---|
| **The most direct answer to challenge #6** (white box, conditions, provenance, dark logic in the model) | On its own it is an **engine, not a product**: smokers do not ask for a knowledge graph |
| Novel (G2) and attractive to the Ghent Health Psychology Lab | Updating claims needs a **fast, measurable proximal outcome**. Otherwise the posteriors barely move during our study |
| Gives a clear basis for user-facing explanations (G7) | Expert priors from TaTT are coarse (BCT–MoA, not BCT–smoking-craving) |
| Can be shown in simulation and with small data | Risk of a beautiful schema with nothing feeding it |

**How we could show it.** Claims seeded from TaTT/literature, updated in simulation and with real small-sample data; explanation screens tested with users and experts.

**Score.** N5 V3 F3 C5 E3 X5 R4 → **3.86**.
**Verdict.** Not a core by itself, but the best **engine** for H1 and H2.

---

## I5 — Modular-sensing JITAI with graceful degradation

**Idea.** One risk and decision model that works for EMA-only users and improves when phone sensors or a wearable are added, with explicit uncertainty per data tier (G5).

**Grounding.** All research JITAIs assume a fixed sensor kit ([sota/03 §5.7](../sota/03_jitai_sensing_prediction.md#5-the-known-hard-problems-these-confirm-the-difficulties-in-our-claudemd)). A public-ish dataset with EMA + Fitbit shows lapse prediction AUC 0.899 without and 0.952 with sensor data at group level, with weaker out-of-sample individual performance (Perski et al., 2024). That is a ready-made ablation for a "what does each tier add?" study.

| Strong points | Weak points |
|---|---|
| Directly serves our modularity decision and privacy ("share less, still get help") | Mostly a **technical** contribution; little direct value for smokers |
| Demonstrable offline on existing data | Small datasets; findings may not generalise |
| Low privacy risk | Little for psychologists; weak challenge fit |

**Score.** N4 V2 F3 C2 E3 X3 R4 → **2.96**.
**Verdict.** A design principle for whichever core we pick, not a core in itself.

---

## I6 — Personal experiments: the app and the smoker find out together what works

**Idea.** Turn personalisation into **short, explicit self-experiments** that the smoker agrees to: "This week, when a craving hits, the app randomly suggests either a 3-minute walk or a 3-minute puzzle game. You rate the craving before and 10 minutes after. On Sunday we look at what worked *for you*." The app plans the experiment, randomises, collects the outcome, analyses it (Bayesian, small-n) and proposes the next one. The user stays in control and sees the evidence.

**Grounding.**
- Self-experimentation systems exist **outside smoking**: SleepCoacher (Daskalova et al., 2016), SleepBandits, guided flexible self-experiments with bandit support (Daskalova et al., 2020), TummyTrials for IBS food triggers, n = 15, users could run reliable self-experiments but rigour clashes with daily life (Karkar et al., 2017), and StudyMe for user-designed N-of-1 trials (Zenner et al., 2022).
- **In smoking**, the only close precedent is a *motivational* "personal experiments" program for ambivalent smokers (7 brief tasks including a 24-h quit attempt; n = 25 pilot, 92% more interested in quitting or cutting down; Heffner et al., 2020). It does not randomise, learn or compare coping options.
- **Craving relief is a proximal outcome that moves within minutes** (exercise: Haasova et al., 2013; visuospatial tasks: Skorka-Brown et al., 2015; urge surfing / ACT: Bricker et al., 2020). That makes within-person learning visible in **days**, not months.
- Matches the challenge text directly: "personalisation becomes a search problem" and "micro-randomisation in daily life" ([samenvatting](../samenvatting%20Why_Should_This_Work_studenten_NL.md)).

| Strong points | Weak points |
|---|---|
| **Demonstrable with real smokers in a short study**: a 1–2 week test with 10–20 users can show per-person differences between coping options | Asks effort: rating cravings before/after is EMA burden. Some smokers will not want to "do experiments" |
| Agency and transparency are built in: the user co-owns the learning, which fits trust and acceptance findings (Tintarev & Masthoff, 2007) | **Carry-over, novelty and expectation effects** make single-case inferences noisy. It is "good enough to decide", not proof |
| Content options are evidence-based (exercise, visuospatial distraction, urge surfing, if-then plans) | Covers mainly the volitional / craving part of the journey unless extended to other phases |
| Simple, honest learning (small-n Bayesian), easy to explain | Precedents exist in other domains, so novelty is "first in smoking + coupled to theory", not a new paradigm |
| Low risk: no passive sensing required | Recruiting current smokers who are quitting during our window needs planning and ethics approval |

**How we could show it.** A short field-lite study (ethics permitting) or a lab-plus-diary study: smokers run one 1–2 week experiment; we show per-user posteriors, interview them about the experience and the explanations.

**Score.** N4 V4 F5 C5 E4 X4 R4 → **4.32** (joint first).
**Verdict.** The most demonstrable idea that is still new in smoking. Strongest when combined with the claim layer and a phase frame (→ H2).

---

## I7 — Pre-intender module: a constrained MI conversation

**Idea.** Serve the ~80% of smokers who are not ready to quit with a motivational-interviewing conversation (LLM for language, a rule/claim layer for content and safety), measuring readiness, importance and confidence over time. It also produces the intake priors (G9).

**Grounding.** MIBot raised confidence to quit after one week (n = 349); GPT-4 reflections were 88% acceptable, which requires an automatic checker (Brown et al., 2023; JMIR MH, 2024). Large LLM cessation chatbot RCTs are now running, e.g. HKU "Quit to Win 2025" with GPT-4o, n ≈ 1,094, results expected 2027 (NCT06914492), and a 2026 follow-up (NCT07649044). BeFreeBot was feasible and acceptable as an add-on to SMS (JMIR Form Res, 2025, verify).

| Strong points | Weak points |
|---|---|
| Large, under-served user group; high value | **Crowded and moving fast**: several funded LLM-chatbot trials will report before or during our project |
| Single-session effects (readiness, confidence) are measurable in a short study | LLM safety and hallucination; needs guard-rails we would have to validate |
| Attractive to psychologists (MI fidelity) | QuitBot's full RCT was null despite a strong pilot: conversational delivery is not a proven active ingredient |

**Score.** N3 V4 F4 C3 E3 X2 R3 → **3.36**.
**Verdict.** A valuable **module** (onboarding + motivational phase), not the core.

---

## I8 — Tabacologist-augmented hybrid care

**Idea.** The app supports the smoker between sessions with a Belgian tabacologist (Tabakstop phone coaching, ~8 sessions). The coach sees a summary of triggers, plan, and what has worked; the app adapts using the coach's input.

**Grounding.** App + human support models (Pelago, Pivot, CureApp) have the best evidence among apps ([sota/01](../sota/01_evidence_base.md)). Belgium has a funded quitline and the tabacologist profession ([sota/02 §3](../sota/02_app_landscape.md#3-belgian--flemish-context)).

| Strong points | Weak points |
|---|---|
| Plugs into an existing care pathway; strong behavioural-support evidence | **Depends on a partner** (Tabakstop/tabacologists) committing time; their 2026 status is unknown |
| Natural expert collaborators | Two user groups to design and test for; longer studies |
| | Human-in-the-loop adaptivity already exists commercially; the novelty lies in what the coach is shown (explanations), not in the hybrid care itself |

**Score.** N3 V4 F2 C4 E4 X3 R4 → **3.29**.
**Verdict.** Keep as a **stakeholder angle and a module** (coach view of the claim layer). Turn it into a core only if Tabakstop commits.

---

## Summary

| ID | Direction | Score | Role going forward |
|---|---|---|---|
| I6 | Personal experiments | 4.32 | Core of H2 |
| I3 | HAPA orchestrator | 3.86 | Core of H1; phase shell of H2 |
| I4 | Claim-updating layer | 3.86 | Engine of H1 and H2 |
| I2 | Pre-craving steering | 3.54 | Core of H3; experiment type in H2 |
| I7 | Pre-intender MI | 3.36 | Module |
| I8 | Tabacologist hybrid | 3.29 | Module / stakeholder angle |
| I5 | Modular sensing | 2.96 | Design principle |
| I1 | Deep JITAI (narrow) | 2.32 | Delivery module only |

Sources: see [references.md](references.md).
