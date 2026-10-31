# 04 — Hybrids and comparison

> **Question answered here:** Which combinations of ideas make the strongest project, and how do all candidates compare side by side?

## 1. Hybrids

The single directions in [02](02_core_directions.md) have complementary weaknesses: the theory-rich ones (I3, I4) are hard to demonstrate, while the demonstrable one (I6) covers only part of the journey. Four combinations address this (H4 was added after the first shortlist).

### H1 — HAPA orchestrator powered by a claim-updating layer (I3 + I4, I2/I1 as JITAI slot)
Direction B with a real engine. HAPA phases and sub-models are encoded as claims with phase conditions and provenance. A hierarchical learner updates them: slow decisions (which sub-model in this phase) and fast decisions (which building block now). A JITAI module is one decision type among others.
- **New:** G1 + G2 + G8 together. No deployed system learns across intervention types and phases. Multi-component RL exists only in simulation and outside smoking (Xu et al., 2025).
- **Strong:** the most complete answer to challenge #6 and the most extensible design. Very attractive to the Health Psychology Lab.
- **Weak:** wide build. Phase-level learning cannot be shown with users within the project, only in simulation. Usability tests will cover the experience, not the learning. Risk of a thin layer over many modules.
- **Scores:** N5 V4 F3 C5 E3 X5 R4 → **4.07**.

### H2 — "Quit Lab": personal experiments on top of a claim-updating layer (I6 + I4, light HAPA shell)
The smoker and the app run short self-experiments. Each experiment tests a claim ("for *you*, in *this* situation, *walking* relieves cravings more than *the puzzle*"). Results update the claims, which the user can inspect. A light HAPA shell decides *which kind* of experiment fits the phase: motivational experiments for pre-intenders (as in Heffner et al., 2020), coping experiments for actors, routine-substitution experiments (I2) when a trigger map exists (I18). The bandit can run inside an experiment, as SleepBandits does for sleep (Daskalova et al., 2020).
- **New:** first self-experimentation system for smoking cessation coping. Claims with provenance as the object of learning (G2). Sufficient-bundle search made concrete (challenge text). Experiments on pre-craving substitution (G4) as one experiment type.
- **Strong:** demonstrable with real smokers in a short study, because craving relief is measurable within minutes. User agency and transparency are part of the design, not an add-on. The evidence-based toolkit (I15) supplies the arms.
- **Weak:** burden of before/after ratings. Not every smoker wants an "experimental" framing (needs good UX language). Single-case inference is noisy (carry-over, expectation). The phase shell stays light, so the motivational phase is covered less deeply than in H1. Precedents in other domains mean the novelty claim must be phrased carefully.
- **Scores:** N5 V4 F4 C5 E4 X4 R4 → **4.32**.

### H3 — Anticipatory steering with modular sensing (I2 + I5 + I16)
Direction A at its most novel. A personal routine/trigger model (from I18 logging, phone context, optional wearable) forecasts risk windows. The app proposes substitutes *before* the urge, and explains why ("Tuesdays after training you usually smoke at 18:30, so a quick call with Tom at 18:15?"). The model degrades gracefully: EMA/diary-only users get a coarser forecast.
- **New:** G4 + G5, with explanations (G7).
- **Strong:** concrete, intuitive, close to the team's original idea. Strong exercise evidence. Low-burden variant without wearables.
- **Weak:** prevention cannot be proven without field data. Response latency (~64 min mean in Quit Sense; Naughton et al., abstract, verify) can exceed forecast lead time. Weaker challenge fit unless the forecast is made white-box.
- **Scores:** N5 V4 F3 C3 E4 X3 R3 → **3.75**.

### H4 — HAPA-scaffolded coach with a learning JITAI (I3 rule-based + I15 + I2/I1, light I4)
*Added 31 Oct 2026 after a team discussion on whether a JITAI needs an orchestrator above it.*

An app with several linked intervention types: a **planner** (if-then and coping plans per trigger), a **JITAI**, a **progress / self-monitoring view**, and the craving toolkit. HAPA structures the journey, but the top level is **rule-based**, not learned: rules from theory, the intake and the user's state decide which modules are active ("no coping plan yet → planner first"; "quit date passed → coping + JITAI"). **Learning happens in one place: the JITAI.** At each decision point it chooses between *remind of your own plan*, *a toolkit option*, *a motivational message* and *nothing*, using a few actor-phase determinants (coping self-efficacy, recovery self-efficacy, plan present) as tailoring variables (Nahum-Shani et al., 2015; 2018). The claim store provides priors and explanations ("you made a plan for after dinner, so here it is").

Three design arguments behind H4:
1. **Most modules work together; they don't compete.** Planner → plan reminder at the cue moment → progress feedback is a chain, not a choice. In BCT terms: action/coping planning (1.4/1.2) followed by prompts/cues (7.1). This is implementation intentions used the way they are meant to work, as cue-response links (Gollwitzer & Sheeran, 2006). The link is a shared user model, not something learned.
2. **Real choices exist where options exclude each other or compete for attention:** the notification budget and the coping option (several times a day), and the phase/module or sub-model (rarely, over weeks). Only the frequent choices give enough data to learn *and show* learning within the project.
3. **For JITAI users the HAPA phase barely changes.** Craving support is for actors/maintainers (Schwarzer, 2008). What varies within that phase is self-efficacy and planning, and a one-tap check-in can measure those. A learned phase layer would add little to JITAI decisions and would slow learning with small n.

- **New:** a smoking JITAI that chooses *content* by HAPA determinants and the user's own plans, and says why (G3 content side, G8, G7). Anticipatory if-then plan reminders before a risk window were noted in the SOTA as ready-to-implement but untried (Ullah et al., 2022; [sota/03](../sota/03_jitai_sensing_prediction.md)). Cross-type orchestration (G1) is covered by explicit rules, not learning.
- **Strong:** the most "app-like" option and the closest to the team's focus on a usable app: a full journey with linked modules. The learning can be shown with real users, because JITAI decisions happen several times a day with proximal outcomes (prompt opened, plan used, craving rating). Rules are easy to explain and easy for psychologists to write and review. The rule layer can later be replaced by a learner (H1) without changing the modules.
- **Weak:** wide build (mitigated: software is cheap with agentic coding, [01 §1](01_scoring_framework.md#1-project-constraints-the-scores-take-into-account)). The learning signal is noisier than in H2's explicit experiments (no before/after rating design, more confounding by context). Notification burden must be capped. The novelty claim relies on the combination; each single part has precedents (plan reminders in apps, trigger-matched messages in Smart-T2; Hébert et al., 2020). Rule-based orchestration is less novel than learned orchestration.
- **Scores:** N4 V4 F4 C4 E4 X5 R4 → **4.07**.

## 2. Score matrix

Weights: N 3 · V 3 · F 3 · C 1.5 · E 1.5 · X 1 · R 1 (see [01](01_scoring_framework.md)).

| ID | Candidate | N | V | F | C | E | X | R | **Score** |
|---|---|---|---|---|---|---|---|---|---|
| H2 | Quit Lab (I6 + I4 + HAPA shell) | 5 | 4 | 4 | 5 | 4 | 4 | 4 | **4.32** |
| I6 | Personal experiments | 4 | 4 | 5 | 5 | 4 | 4 | 4 | **4.32** |
| H1 | HAPA orchestrator + claim layer | 5 | 4 | 3 | 5 | 3 | 5 | 4 | **4.07** |
| H4 | HAPA-scaffolded coach + learning JITAI | 4 | 4 | 4 | 4 | 4 | 5 | 4 | **4.07** |
| I3 | HAPA orchestrator | 4 | 4 | 3 | 5 | 3 | 5 | 4 | 3.86 |
| I4 | Claim-updating layer | 5 | 3 | 3 | 5 | 3 | 5 | 4 | 3.86 |
| H3 | Anticipatory steering + modular sensing | 5 | 4 | 3 | 3 | 4 | 3 | 3 | **3.75** |
| I2 | Pre-craving steering | 5 | 4 | 2 | 3 | 4 | 3 | 3 | 3.54 |
| I7 | Pre-intender MI | 3 | 4 | 4 | 3 | 3 | 2 | 3 | 3.36 |
| I8 | Tabacologist hybrid | 3 | 4 | 2 | 4 | 4 | 3 | 4 | 3.29 |
| I5 | Modular sensing | 4 | 2 | 3 | 2 | 3 | 3 | 4 | 2.96 |
| I1 | Deep JITAI (narrow) | 2 | 3 | 2 | 2 | 3 | 2 | 2 | 2.32 |

## 3. Coverage of the gaps

| Gap ([sota/07](../sota/07_gap_analysis.md)) | H1 | H2 | H3 | H4 |
|---|---|---|---|---|
| G1 orchestration across types and phases | ●●● | ●● (across coping types; light phase shell) | ○ | ●● (across types, rule-based) |
| G2 claims updated by user data | ●●● | ●●● | ● | ● (claims as priors; content claims updated) |
| G3 risk × receptivity × content | ● (JITAI slot) | ● | ●● | ●● (content by determinants + plan) |
| G4 pre-craving steering | ● (JITAI slot) | ●● (experiment type) | ●●● | ●● (plan reminder before risk window) |
| G5 modular sensing | ●● | ●●● (works with self-report only) | ●●● | ●●● |
| G6 evidence-strong ingredients | ●● | ●●● (toolkit arms) | ●● | ●●● (planning + toolkit) |
| G7 explanation + dark logic | ●●● | ●●● | ●● | ●●● |
| G8 HAPA in smoking apps | ●●● | ● | ○ | ●●● |
| G9 cold start via conversation | ●● | ●● | ● | ●● |

## 4. What the comparison shows

1. **The narrow deep JITAI (I1) should not be the core.** It is the most crowded area and the hardest to demonstrate under our constraints. Its novel variant (I2 / H3) stays a serious option.
2. **The broad framework (I3) needs an engine.** Without the claim layer it is architecture; with it (H1) it is the most complete answer to the challenge, but the hardest to show working with users.
3. **Personal experiments (I6 / H2) solve our demonstration problem.** Because craving relief is a minutes-scale outcome, per-person learning becomes visible in a short user study. That is rare in this field, and it fits the challenge's "search for the sufficient bundle".
4. **The hybrids are not mutually exclusive.** H2 can grow into H1 (add more phase sub-models), and H3's forecast can become an experiment type in H2. The vote is about **where the main effort and the main claim go**.
5. **H4 moves H1's learning down a level.** H1 and H4 have the same structure and the same score (4.07), but they trade differently: H1 is more novel (learned orchestration) and fits the challenge better; H4 is more demonstrable (learning in the JITAI, where decisions are frequent). H4's JITAI learner and H2's experiment engine are nearly the same component: both choose between toolkit options at craving moments. H2 runs it as explicit, visible experiments; H4 runs it as a quiet bandit inside the JITAI.

Sources: see [references.md](references.md).
