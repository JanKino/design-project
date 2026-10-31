# 02 — Competitive analysis

> **Question answered here:** Which apps, digital therapeutics and research systems are we up against? What do they do well and badly, what can we learn from them, and how do we differentiate?
> Feature claims for commercial apps come from stores and vendor pages: `[vendor]`. Check the current version before quoting. Detailed feature matrix: [../02_app_landscape.md](../02_app_landscape.md).

## Takeaways for our direction

1. **The market splits into three groups.** (a) Free or freemium consumer apps: trackers, gamification, some structured content. (b) Paid or reimbursed digital therapeutics: CBT or ACT programmes with coach, medication or CO sensor, sold through employers, insurers or prescription. (c) Research prototypes: JITAIs, bandits, RL coaches. **No product in any group chooses between intervention models per person and phase and explains why.**
2. **What to copy:** Smoke Free's BCT-coded missions and its DiGA route; iCanQuit's ACT content; Pelago's and Pivot's medication and coach linkage; QuitBot's free, low-barrier conversational onboarding; Quit Sense's modest use of context.
3. **What to avoid:** feature piles with no evidence (badges, trackers), chatbots sold as the treatment, sensor-heavy designs that most users cannot use, and vendor-only evidence.
4. **Differentiation statement:** *"The app that works out which proven quit method fits you at each stage, switches when it is not working, and tells you why."*

## Positioning (for a Miro 2×2)

- **X axis:** how far the app adapts *across intervention types and phases* (none → fixed stage content → learns per person).
- **Y axis:** how transparent its reasoning is to the user (black box → theory shown → per-person explanation).
- Most consumer apps sit bottom-left. DTx sit at "fixed stage content", with reasoning hidden. Research bandits and RL learn but are not transparent to users. **Our target is top-right, which is empty.**

## Miro cards

| ID | Competitor | Category | What it does | What they do well (learn from) | Weak points | How we differentiate | Evidence | Reference |
|---|---|---|---|---|---|---|---|---|
| C1 | Smoke Free | Consumer app (freemium) + DiGA in Germany | Tracker, badges, daily BCT-coded missions, craving tools, paid coaching | Missions are explicitly BCT-coded. Large user base. Councils and NHS buy premium for residents. Reimbursed DiGA in Germany | Same programme for everyone. Personalisation limited to onboarding numbers | We choose and switch missions/sub-models per person and phase and explain the choice | [industry] exploratory RCT | Crane et al. (2019); smokefreeapp.com; apotheke adhoc (DiGA) |
| C2 | NichtraucherHelden | Prescription app (DiGA, Germany) | Guideline-based multi-week course | Proved a payer-reimbursed route for smoking apps (permanent DiGA listing 2023) | Linear course. German only. Price dispute in arbitration | Adaptive sequencing; HAPA phases instead of a fixed course | [RCT] for DiGA listing (verify) | Ärzte Zeitung; IWW (DiGA listing) |
| C3 | iCanQuit | Research-derived consumer app (free) | ACT programme: values, urge acceptance, levels | Strongest app RCT to date. Content model is clear | Static ACT for all; no alternative for users ACT does not suit | ACT is one interchangeable sub-model; we learn per user whether ACT or CBT coping works better | [RCT] | Bricker et al. (2020) |
| C4 | NCI QuitGuide / Smokefree.gov apps | Government app (free) | Information, tracking, tips | Free, trusted, standard RCT comparator | Low engagement. Weaker than ACT in the head-to-head | Trust can be built through partners (Tabakstop, UGent) as in the DCE finding | [RCT] as comparator | Bricker et al. (2020) |
| C5 | Pelago (formerly Quit Genius) | Digital therapeutic, employer-paid (US/UK) | CBT programme, human coach, NRT delivered home | Medication + coach + app bundle. B2B employer model. $151M raised | Coach-heavy (costly). Vendor-reported outcomes. Logic not visible to users | Automated orchestration gives a cheaper "coach logic", and it is explainable | [RCT] [industry] | Webb et al. (2020, 2022); Pelago press releases |
| C6 | Pivot (Carrot) | Digital therapeutic + CO breath sensor | App + FDA-cleared CO sensor + coach + NRT | Objective CO feedback as motivator. Patented sensor | Hardware cost. US employer market. Patents on sensor-based smoking prediction | We stay hardware-optional (modular data); CO is an optional data tier | Cohort + pilot RCT [industry] | Marler et al. (2021, 2022); FDA K201206 |
| C7 | CureApp SC | Prescription DTx (Japan) | App + CO checker + clinic follow-up | First approved prescription smoking app in Asia (2020) | Tied to clinic visits; fixed programme | Self-guided, adaptive, can still hand over to a tabacologist | [RCT] | Masaki et al. (2020); CureApp (2020) |
| C8 | QuitBot (Fred Hutch) | Free LLM chatbot app (research → public) | 42-day conversational programme + free-form LLM Q&A | Low-barrier onboarding through conversation. Careful 11-step user-centred design | Full RCT null at 12 months. Chat does not choose between treatment models | The chatbot serves the orchestrator (intake, phase check-ins). Effect comes from the selected BCTs | [RCT] [registry] | Bricker et al. (2024); quitbot.net |
| C9 | New LLM coach apps (e.g. QuitPath AI, Quit Kit) | Consumer apps with GPT-style coach (subscription) | Timer + AI "roadmap" + craving chat | Fast to market. Users like on-demand chat | No evidence. No theory. Safety of free-form LLM advice unclear | Theory-bound, BCT-coded, safety-guarded conversation with explanations | [vendor] | App Store listings (2026) |
| C10 | Kwit | Consumer app (freemium) | Gamified CBT-inspired tracker | Polished gamification; strong retention design | Gamification has weak outcome evidence | Gamification only as an optional engagement block, never the core | [obs] [industry] | Rajani et al. (2023) |
| C11 | QuitNow! | Consumer app (freemium) | Tracker + large community | Community and social proof at scale | No structured therapy; no adaptation | Social support / buddy as one selectable building block for users it suits | None found | Consumer roundups |
| C12 | QuitSure | Consumer app (paid programme) | Multi-day "reframing" programme + community | Strong marketing, clear programme story | Single-arm vendor studies only | Evidence-graded content and transparent claims | [obs] [industry] | QuitSure single-arm studies (2023) |
| C13 | Tabakstop (BE) | Public quitline + tracker app (free) | Phone/chat coaching with tabacologists; app with savings, quiz, challenges | Free, trusted, linked to reimbursed tabacologist care | App is a basic tracker; no adaptivity; calls declining | Partner, not competitor: our app could share the user's plan and trigger profile with the coach | Service, no app evidence | Solidaris (2024); kanker.be brochures; Brussels Times |
| C14 | Quit Sense (research) | Research JITAI (UK) | Learns smoking locations; context-triggered support | Low-burden sensing (location) that works without wearables | Feasibility only; one intervention type | Becomes one sub-module inside our action phase | [pilot] | Naughton et al. (2024) |
| C15 | Smart-T (research) | Research JITAI (US) | EMA-based risk → tailored messages | Simple risk model with real predictive power; trigger-matched content | Fixed rules; no learning | Its risk model and messages fit our EMA-only data tier | [pilot] | Businelle et al. (2016); Hébert et al. (2020) |
| C16 | Sense2Stop / mCerebrum (research) | Research JITAI with chest-band sensors | Stress detection → stress-management prompts (MRT) | Rigorous MRT design; open sensing stack | Research hardware; results not found | We use consumer wearables only and stay sensor-optional | [RCT-MRT] protocol | Battalio et al. (2021) |
| C17 | TU Delft virtual coach (research) | RL coach for quit preparation | Learns which preparatory activity to propose | Only smoking system that learns per user what to propose | One phase only; text-based research prototype | We learn across phases and models, and show the learned claims to the user | [RCT-online] | Albers et al. (2022) |
| C18 | HeartSteps, Oralytics, MiWaves (other domains) | Research learning systems | Bandits learn when/what to send | Safe, deployed online learning with pooling | One flat decision; not smoking | Adopt the engine; extend it to a hierarchy (phase → model → building block) | [RCT-embedded] | Liao et al. (2020); Trella et al. (2024); Ghosh et al. (2024) |

## What we can learn: patterns across competitors

| Pattern | Seen in | Lesson for us |
|---|---|---|
| Trust and ratings drive uptake more than descriptions | All store apps; Szinay et al. (2025) DCE | Partner branding (UGent, Tabakstop) and a good first-week experience matter more than feature lists |
| Payer routes exist but demand evidence | DiGA (C1, C2), DTx (C5–C7) | Keep claims "wellbeing / research prototype" during the project; design logging so later evidence is possible (see [03](03_ipr_and_rights.md)) |
| Medication and human support are the strongest levers | C5, C6, C7, C13 | Medication-support and referral blocks are *must-haves*, not extras |
| Chat improves onboarding but is not the treatment | C8, C9 | Chat is the orchestrator's interface: intake, phase review, MI |
| Sensing helps only if it is cheap for the user | C14 vs C16 | Location, phone use and EMA first; wearable optional |
