# 05 — Shortlist for the team vote

> **Question answered here:** Which directions should the team vote on (S1–S3, plus S4 added after discussion), what would each project concretely look like, and which questions should decide the vote?
> Background and scores: [02](02_core_directions.md), [03](03_modules_and_enablers.md), [04](04_hybrids_and_comparison.md).

## 0. What all three options share

Whatever wins (S1–S4), these parts are in the project ("Must" tier in [03](03_modules_and_enablers.md)):
- **Explicit claims with provenance** as the place where the program theory lives (at least in a light form).
- **Evidence-based craving toolkit** (I15): exercise snack, visuospatial puzzle, urge surfing / ACT, if-then plan, supporter contact.
- **"Why am I seeing this?" + dark-logic monitor** (I16).
- **Slip and recovery flow** (I9).
- **Modular data**: every option must work with self-report only.
- **No progress tracker or badges as a selling point.** A simple tracker may exist, but it is not the contribution.

---

## S1 — Quit Lab: find out together what works for you (H2)

**Pitch.** A quit app in which the smoker and the app run short, explicit experiments ("walk or puzzle for evening cravings?"). The results update a visible personal program theory, which the app uses and explains in its later suggestions.

**What we build.**
1. Claim store (BCT → mechanism → outcome, with phase/context conditions and provenance from TaTT and the literature).
2. Experiment engine: plans a 1–2 week experiment, randomises options at craving moments, collects before/after craving ratings, does small-n Bayesian analysis, proposes the next experiment (optionally with a bandit as in SleepBandits).
3. Light HAPA shell choosing the experiment *type*: motivational experiments (pre-intenders), coping experiments (actors), substitution experiments (with a trigger map).
4. Must modules + conversational intake that sets priors (I17).

**What we can show.**
- With smokers (ethics permitting): 10–20 participants run one experiment for 1–2 weeks. We report per-person posteriors, how often individual "winners" differ from the population average, burden, and interview results on the experience and the explanations.
- In simulation: convergence and the quality of decisions with few data points.

**Contribution claim.** First self-experimentation approach to smoking cessation coping, with the results stored as testable claims inside the system. This is a direct operationalisation of the challenge's "personalisation as a search for the sufficient bundle".

**Value for partners.** Psychologists get a tool that produces within-person evidence about BCTs and mechanisms. Tabacologists get a summary of "what works for this client".

**Main risks → mitigation.**
| Risk | Mitigation |
|---|---|
| Rating burden, drop-out | Single-tap ratings; short experiments; option to stop any time |
| "Experiment" framing feels clinical | User-test the language early ("try-outs", "find your best trick") |
| Noisy single-case inference | Present results with uncertainty; Bayesian pooling across users; claims, not proof |
| Recruiting smokers who are quitting during our window | Start recruitment and ethics early; also accept smokers who are cutting down |

**Deliberately left out.** Deep sensing, a full multi-phase learner, LLM decision-making.

---

## S2 — White-box HAPA coach: an orchestrator that knows why (H1)

**Pitch.** An app that guides the whole quit journey through HAPA phases, chooses between interchangeable sub-models and BCT-coded features per person, and keeps its reasoning as explicit, updatable claims that it can show to the user and to experts.

**What we build.**
1. Claim store as in S1, extended with phase conditions, sufficient bundles and dark-logic paths.
2. Hierarchical decision layer: phase estimation (with fall-back), sub-model selection per phase (slow learner), building-block selection (fast learner), JITAI slot.
3. Sub-models for at least two phases (e.g. MI + decisional balance for pre-intenders; implementation intentions + ACT vs CBT coping for actors), each with 2+ interchangeable features.
4. Must modules + pre-intender MI conversation (I7) + intake (I17).

**What we can show.**
- With users: usability of the full journey, comprehension and trust of the explanations, expert review of the claims (Health Psychology Lab, tabacologist).
- In simulation: hierarchical learning behaviour, cold start, phase fall-back.
- **Not** with users: whether the learning picks better sub-models (too slow for our study window).

**Contribution claim.** First system that orchestrates and learns across intervention types *and* phases in smoking cessation (G1), with the program theory inside the system (G2, G8).

**Value for partners.** The closest to the original challenge #6. A reusable framework for the Health Psychology Lab.

**Main risks → mitigation.**
| Risk | Mitigation |
|---|---|
| Breadth: many thin modules | Build two phases deeply instead of four thinly |
| Learning cannot be shown live | Strong simulator (I11, COMPLAPSE-based); be explicit about what is simulated |
| Looks like "another stage-based app" in user tests | Put the explanation and the visible personal model at the centre of the UX |

**Deliberately left out.** Deep sensing; full JITAI optimisation (slot only).

---

## S3 — One step ahead: anticipatory steering (H3)

**Pitch.** The app learns your personal smoking routines and nudges you to a substitute activity *before* the craving builds, with whatever data you choose to share, and tells you why.

**What we build.**
1. Trigger map from a short logging period (I18) + optional phone context and wearable.
2. White-box risk-window forecaster with explicit data tiers (diary-only → phone → wearable).
3. Substitution planner using the toolkit (I15), timed to the forecast, with an explanation.
4. Must modules.

**What we can show.**
- Offline: forecast quality per data tier on public data (e.g. Perski et al., 2024 dataset, if accessible).
- With users: acceptability and perceived timing in scenario walk-throughs and a short field-lite test.
- **Not**: whether anticipatory nudges prevent lapses.

**Contribution claim.** First smoking JITAI that targets the pre-craving window with substitution (G4), designed for modular data (G5).

**Main risks → mitigation.**
| Risk | Mitigation |
|---|---|
| Lead time vs response latency | Nudge early (planning nudge 30–60 min ahead), not at the last moment |
| Public datasets too small or not accessible | Contact the UCL/COMPLAPSE authors early; fall back to our own diary data |
| Weak challenge fit | Keep the forecaster rule-based or small-Bayesian; show its reasons |

**Deliberately left out.** Phase orchestration; MI module.

---

## S4 — HAPA-scaffolded coach with a learning JITAI (H4)

*Added 31 Oct 2026 after a team discussion: a range of intervention types (planner, JITAI, progress) needs something that coordinates them. Does that mean S2's learning orchestrator?*

**Pitch.** A complete quit app with linked modules: you make if-then plans for your triggers, the app reminds you of *your own plan* at the right moment, or offers another coping option, and shows you what worked. HAPA structures the journey through transparent rules. The app learns per person *which* in-the-moment support to give, and explains why.

**What we build.**
1. **Shared user model:** triggers, plans, determinant check-ins (coping and recovery self-efficacy, plan present), history. Every module reads and writes it, and this is what links the JITAI to the planner.
2. **Rule-based HAPA scaffold:** explicit, readable rules (from theory, the intake and the user's state) that switch modules on and off and set their priority. Psychologists can write and review these. Built behind an interface so a learner (S2) can replace it later.
3. **Planner:** if-then and coping plans per trigger (BCT 1.4 / 1.2), building on a short trigger log (I18).
4. **Learning JITAI:** at each decision point it chooses *plan reminder*, *toolkit option*, *motivational message* or *nothing*, within a daily notification budget. A contextual bandit uses determinants and context as tailoring variables and the claim store as priors. Proximal outcomes: prompt opened, plan used, one-tap craving rating.
5. **Progress / self-monitoring view** with feedback on which plans and options worked (BCT 2.2 feedback on behaviour, 2.3 self-monitoring).
6. Must modules + intake (I17). Pre-intender support (MI) stays small or rule-based.

**What we can show.**
- With smokers: 10–20 participants for 1–2 weeks. Usability of the full plan → prompt → progress loop, acceptance and perceived timing of the prompts, how often plan reminders are used, per-person divergence of the learned policy, and understanding of the explanations.
- In simulation: bandit convergence, cold start with claim-based priors, effect of the notification budget.
- **Not:** whether the rule-based scaffold beats a learned orchestrator, or long-term abstinence effects.

**Contribution claim.** A smoking-cessation app in which the in-the-moment support is chosen by the user's HAPA determinants and their own plans, learned per person and explained. Cross-module coordination is explicit program theory, not a black box (G3 content side, G8, G7, G1 rule-based).

**Value for partners.** Psychologists write and review the scaffold rules and claims, a direct use for them. Tabacologists get the client's plans and "what helped" summary.

**Main risks → mitigation.**
| Risk | Mitigation |
|---|---|
| Breadth: many modules, each thin | Build the actor/maintainer phase deeply (planner + JITAI + progress); keep pre-intender support minimal |
| Noisy learning signal (no controlled experiment design) | One-tap proximal ratings; claim priors; optionally an explicit "try-out" mode borrowed from S1 |
| Notification burden | Hard daily budget; "nothing" is always an option; user can lower the frequency |
| Novelty challenged as "just a well-built app" | Frame the contribution around determinant- and plan-driven content selection with explanations; compare against a non-adaptive version in the user study |
| Timing without sensing is coarse | Plan reminders anchored to the user's own trigger times; sensing as an optional tier (I5) |

**Deliberately left out.** A learned phase / sub-model orchestrator (rules instead, with an open interface), deep sensing, LLM decision-making.

**Smallest version.** Only the actor phase: planner + learning JITAI + progress. This is essentially S3 with a determinant layer instead of a forecaster, and a fallback if time runs short.

---

## Side-by-side

| | S1 Quit Lab | S2 White-box HAPA coach | S3 One step ahead | S4 HAPA scaffold + learning JITAI |
|---|---|---|---|---|
| Score ([04](04_hybrids_and_comparison.md#2-score-matrix)) | 4.32 | 4.07 | 3.75 | 4.07 |
| Main gaps | G2, G7, G6, G4 (partly) | G1, G2, G8, G7 | G4, G5, G3 | G3, G8, G7, G1 (rule-based) |
| Where the learning sits | Inside explicit experiments | Phase + sub-model + building block | Risk forecast | JITAI content and timing |
| Learning visible with real users? | **Yes** (days) | No (simulation) | Partly (forecast offline) | **Yes**, but noisier than S1 |
| Covers the whole journey | Partly | **Yes** | No | **Yes** (actor phase deep, rest rule-based) |
| Closest to the original brief | B, reframed | **B** | **A** | A inside B |
| Challenge #6 fit | High | **Highest** | Medium | High |
| Build breadth | Medium | **Large** | Medium | Large |
| Data / privacy demand | Low | Low–medium | Medium–high | Low–medium |
| Grows into another option later? | → S2 (add phases) and S3 (add forecast) | Contains S1/S3 as modules | → experiment type in S1 | → S2 (swap rules for a learner); S1 try-out mode as JITAI option |

## Questions that should decide the vote

1. **Do we want to show that the app *learns* with real smokers, or is simulation enough?** If real users matter → S1 or S4.
2. **Is the white-box framework itself our main deliverable (challenge #6), or a usable app?** Framework → S2. App → S4, S1 or S3.
3. **What excites the team most: the "right moment" (S3), "learning together with the user" (S1), "the whole journey with theory inside" (S2), or "a full app whose in-the-moment support builds on your own plans" (S4)?** Motivation matters over a long project.
4. **Can we secure a partner?** Psychology Lab involvement favours S2, S4 (rule writing) or S1. A tabacologist partner helps all four.
5. **Should the top level (which modules, which phase) learn, or follow explicit rules?** Learn → S2. Rules, with learning lower down → S4.

## Agent's lean (for transparency, not a decision)

**S1, designed so it can grow towards S2.** It is the only option where the core claim — the app learns what works for *this* smoker and can say why — can be shown with real users within our window. It keeps the white-box ambition of S2 in the claim store and absorbs the best part of S3 as an experiment type. If the team values the full-journey framework over live demonstration, S2 is the better choice. S3 is the right choice only if the "right moment" problem is what motivates the team most.

**Update after adding S4.** S4 is the strongest option if the team wants a **complete, usable app** (our stated focus) rather than one sharp contribution, and it beats S2 for us because its learning can be shown with users. S1 and S4 share their core engine, choosing between toolkit options at craving moments, so the choice between them is mostly about **framing and breadth**: visible experiments the user takes part in (S1, sharper novelty, cleaner data) versus a quiet learner inside a full plan → prompt → progress app (S4, more app-like, broader). A middle path is S4 with S1's try-out mode as one of the JITAI options.
