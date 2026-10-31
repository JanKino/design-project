# 02 — App landscape: what is available to smokers today

> **Question answered here:** Which mechanisms do available apps actually use, how adaptive are they, and where is the market saturated?
> Note: feature descriptions of commercial apps come from app stores, vendor sites and consumer roundups. Treat them as **`[vendor]`** claims unless a study is cited. Store listings change often, so check the current version before quoting a feature in a report.

## 1. Taxonomy of what exists

We sort available products into six archetypes. Most apps combine 2–3 of them.

| # | Archetype | Typical features | Examples | Adaptivity |
|---|---|---|---|---|
| A | **Progress tracker** | Days smoke-free, cigarettes not smoked, money saved, health-recovery timeline | QuitNow!, Smoke Free, Flamy, Kwit, Tabakstop app, NHS Quit Smoking | None: the same for everyone, only the numbers change |
| B | **Gamified tracker** | Levels, badges, challenges, streaks, achievements | Kwit, Flamy, Smoke Free (badges and missions) | Rule-based unlocks |
| C | **Structured program (CBT/ACT/mindfulness)** | Day-by-day course, exercises, audio, craving tools | iCanQuit (ACT), Quit Genius (CBT), Craving to Quit (mindfulness), QuitSure (a structured multi-day "program") | Linear. Some branch on quit date |
| D | **Coach / clinician-connected digital therapeutic** | Human coach chat, NRT delivery, clinician dashboard, sometimes a CO sensor | Quit Genius/Pelago, Pivot, CureApp SC, Tabakstop (phone coaching + app) | Human-in-the-loop adaptivity |
| E | **Community / social** | Forums, buddy, sharing milestones | QuitNow! (community), BecomeAnEX, Smoke Free (community features) | None |
| F | **Conversational agent** | Rule-based or LLM chatbot, Q&A, MI-style dialogue | QuitBot (research), MIBot (research), generic LLM wellness apps | Conversation-level adaptivity, no learning of *what works* |

Research-only archetypes, not available in app stores at scale:

| G | **Context-aware JITAI** | Sensor- or EMA-triggered support at risk moments | Quit Sense, Smart-T, Sense2Stop, SmokeBeat/Sense2Quit | Rule-based or ML risk detection |
|---|---|---|---|---|
| H | **Learning / optimising system** | Bandits or RL choose *when* or *what* to send | HeartSteps (activity), Oralytics (oral health), MiWaves (cannabis), TU Delft virtual coach (smoking preparation) | Online learning |

## 2. Feature–mechanism matrix of notable products

✔ = core feature · ◐ = present but minor or limited · — = absent (based on public descriptions)

| Product | Tracking | Gamification | Structured therapy | Craving SOS tools | Medication support | Human coach | Social | Chatbot | Context sensing | Learns per user | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Smoke Free** | ✔ | ✔ | ◐ (daily missions, BCT-coded) | ✔ | ◐ | ◐ (paid) | ◐ | — | — | — | Exploratory RCT `[industry]` |
| **QuitNow!** | ✔ | ◐ (achievements) | — | ◐ | — | — | ✔ community | ◐ (FAQ bot) | — | — | None found |
| **Kwit** | ✔ | ✔ | ◐ (CBT-based) | ✔ | ◐ | — | ◐ | — | — | — | Observational `[industry]` |
| **Flamy** | ✔ | ✔ | — | ◐ | — | — | — | — | — | — | None found |
| **QuitSure** | ◐ | — | ✔ (multi-day program, reframing) | ◐ | — | ◐ (coach chat) | ✔ | — | — | — | Vendor claims only |
| **iCanQuit** | ◐ | ◐ | ✔ (ACT) | ✔ | — | — | — | — | — | — | Large RCT ✔ |
| **Quit Genius / Pelago** | ✔ | — | ✔ (CBT) | ✔ | ✔ (NRT delivered) | ✔ | — | — | — | — | RCT `[industry]` |
| **Pivot** | ✔ (+ CO sensor) | — | ✔ | ✔ | ✔ | ✔ | ✔ | — | ◐ (CO only) | — | Cohort + pilot RCT `[industry]` |
| **CureApp SC** | ✔ (+ CO checker) | — | ✔ | ✔ | ✔ (via clinic) | ✔ (doctor) | — | ◐ | ◐ (CO) | — | RCT, regulatory approval |
| **Tabakstop app** (BE) | ✔ (savings) | ◐ (challenges, quiz) | — | — | — | ✔ (phone line, separate) | ◐ (testimonials) | — | — | — | None found |
| **Quit Sense** (research) | ✔ | — | ✔ | ✔ | ◐ | — | — | — | ✔ (location, phone context) | ◐ (learns smoking locations) | Feasibility RCT |
| **Smart-T** (research) | ✔ (EMA) | — | ◐ | ✔ | ◐ | ◐ (quitline link) | — | — | ◐ (EMA-based risk) | — (fixed risk model) | Pilot RCT |

Sources: Smoke Free (Crane et al., 2019; smokefreeapp.com); QuitNow!, Kwit, Flamy and QuitSure (consumer roundups, e.g. Medical News Today, Healthline, and vendor pages; Rajani et al., 2023 for Kwit); iCanQuit (Bricker et al., 2020); Quit Genius (Webb et al., 2020); Pivot (Marler et al., 2021; 2022); CureApp (Masaki et al., 2020); Tabakstop (Solidaris flyer 2024, tabakstop.be); Quit Sense (Naughton et al., 2024); Smart-T (Hébert et al., 2020). Full references in [references.md](references.md).

## 3. Belgian / Flemish context

- **Tabakstop** (run by Stichting tegen Kanker / Kom op tegen Kanker) offers a free phone line (0800 111 00), chat, mail and a free **Tabakstop app** with quizzes, a savings calculator, challenges and testimonials. The app is a **type A/B tracker**, with no adaptive or context-aware support. The phone programme gives about 8 sessions with a **tabacologist** (Solidaris, 2024; Vlaanderen.be "Stoppen met roken").
- **SmartStop** is another app listed on the Belgian App Store. It was originally tied to tabacologist follow-up and is now open to everyone.
- **Opportunity:** Belgium has a professional role, the **tabacologist**, and a funded quitline. An app that *hands over* to or *augments* these (sharing the user's plan and trigger profile with the coach) would plug into an existing care pathway. Funding of the Tabakstop management agreement ran 2021–2025, so its status in 2026 should be checked with the stakeholders.

## 4. What is saturated vs what is missing in the market

**Saturated (do not compete here):**
- Money and health-timeline trackers (archetype A): every app has one.
- Badges and streaks (archetype B): common, cheap to copy, weak evidence beyond engagement correlations (Rajani et al., 2023).
- Static tip libraries and "craving SOS" lists.

**Under-served in available apps:**
1. **Per-user adaptivity based on outcomes.** No consumer app we found *learns which technique works for this person*. Personalisation is limited to onboarding answers (cigarettes per day, price, quit date).
2. **Context awareness.** Sensing-based support exists only in research (Quit Sense, Smart-T, Sense2Stop).
3. **Theory-driven phase logic.** Apps treat "preparing", "quit day", "early abstinence" and "maintenance" mainly as a timer. Few model *motivation vs volition* or *lapse recovery* explicitly. Smoke Free's lapse handling and HAPA-like recovery self-efficacy are partial exceptions.
4. **Medication and quitline linkage.** Content analyses repeatedly find that few apps actively promote evidence-based medication or professional support (Abroms et al., 2013; Hoeppner et al., 2016; Bustamante et al., 2021), although these are the strongest levers.
5. **Explainability to the user.** No app tells the user *why* it is suggesting something ("because you told us coffee breaks are a trigger and the last two times the walk helped"). Explanations are a known driver of trust and acceptance in recommender systems (Tintarev & Masthoff, 2007).
6. **Pre-intenders.** Most apps assume the user has already decided to quit. About 80% of smokers are ambivalent (Brown et al., 2023 MIBot paper), yet motivational-phase support in apps is limited to a money calculator.
7. **Unintended effects.** No product we found monitors guilt, notification annoyance or app dependency ("dark logic", Bonell et al., 2015).

## 5. Implications

- Differentiation cannot come from *features*. It has to come from **how features are chosen, sequenced and justified for a person** (orchestration), and possibly from **context-aware delivery** done better than in research prototypes.
- A Belgian deployment angle (Tabakstop / tabacologists) is a realistic stakeholder hook for interviews, which fits our "interviews and usability only" constraint.

## References for this file

See [references.md](references.md). Main ones: Abroms et al. (2013); Bonell et al. (2015); Bricker et al. (2020); Brown et al. (2023); Bustamante et al. (2021); Crane et al. (2019); Hébert et al. (2020); Hoeppner et al. (2016); Marler et al. (2021, 2022); Masaki et al. (2020); Naughton et al. (2024); Rajani et al. (2023); Tintarev & Masthoff (2007); Webb et al. (2020).

Non-academic sources used for feature descriptions:
- Solidaris (2024). Flyer Tabak NL. https://www.solidaris-brabant.be/sites/default/files/uploads/Publications/Flyer_Tabak_NL_2024.pdf
- Vlaanderen.be — Stoppen met roken. https://www.vlaanderen.be/stoppen-met-roken
- SmartStop (App Store BE). https://apps.apple.com/be/app/smartstop/id922839269?l=nl
- Smoke Free practices & procedures. https://smokefreeapp.com/practices-and-procedures/
- Medical News Today — best quit-smoking apps. https://www.medicalnewstoday.com/articles/317633
- Healthline — top quit-smoking apps. https://www.healthline.com/health/quit-smoking/top-iphone-android-apps
