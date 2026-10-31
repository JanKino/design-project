# 07 — Gap analysis: what is not yet done

> **Question answered here:** Combining files 01–06, where is the field thin or empty, where could a CS team contribute something new, and which research is ready to be implemented?
> This file deliberately stops **before** choosing a direction. The critiqued list of project directions is the next step (see [README](README.md#next-steps)).

## 1. Done / partly done / not done matrix

| Capability | Commercial apps | Research prototypes | Status |
|---|---|---|---|
| Progress, money, health tracking | ✔ everywhere | ✔ | **Saturated** |
| Gamification | ✔ common | ◐ | **Saturated**, weak evidence |
| Structured CBT/ACT program | ✔ (iCanQuit, Quit Genius) | ✔ | Done. Evidence for some |
| Human coaching + app | ✔ (Pelago, Pivot, Tabakstop phone line) | ✔ | Done |
| CO verification + incentives | ◐ (Pivot, CureApp) | ✔ feasibility | Partly done |
| Chatbot (scripted / LLM) | ◐ | ✔ (QuitBot, MIBot) | Partly done. Full trial null |
| EMA-triggered risk-tailored messages | — | ✔ (Smart-T) | Research only |
| Location-triggered support | — | ✔ (Quit Sense) | Research only, feasibility |
| Wearable stress-triggered support | — | ✔ (Sense2Stop) | Research only, MRT, results not found |
| Smoking-gesture detection | ◐ (SmokeBeat) | ✔ | Detection done. Prevention value unclear |
| Learning *when to send* per user (bandit) | — | ✔ in other domains (HeartSteps, Oralytics, MiWaves) | **Not yet in smoking** |
| Learning *which persuasion/activity* per user | — | ✔ (TU Delft coach, preparation phase) | One smoking example |
| Learning *which intervention type / sub-model per phase* | — | — | **Not done** |
| Receptivity-aware delivery | — | ✔ in PA / mental health (Mishra et al., 2021) | **Not in smoking** |
| Runtime use of BCT ontology to choose and justify | — | ◐ (ontology-based PA coaching) | **Not done for smoking** |
| Claims (BCT→MoA→behaviour, with conditions and provenance) **updated by user data** | — | — | **Not done** |
| User-facing "why am I seeing this?" | — | — | **Not done** |
| Graceful degradation across data sources (EMA-only ↔ phone ↔ wearable) | — | — | **Not done** |
| Dark-logic monitoring (guilt, annoyance, dependence) | — | ◐ (burden terms in HeartSteps) | **Mostly not done** |
| Pre-craving activity substitution (steer before the urge) | — | — | **Not done** as an explicit JITAI target |
| Support for pre-intenders (MI) in apps | ◐ (money calculator only) | ◐ (MIBot) | Under-served |
| Medication uptake/adherence nudging | ◐ rare | ◐ | Under-served relative to its evidence |

## 2. The main gaps, with evidence

### G1 — Nobody orchestrates *across* intervention types and phases
Deployed learners optimise **one flat decision** (send/not send, or which message). Stage-based apps use **fixed** stage → content mappings. No system chooses between program theories or sub-models (e.g. ACT vs avoidance coping, buddy vs self-regulation) per person and phase, and learns from that choice ([04](04_adaptive_learning_ai.md) §2, [06](06_theory_ontologies.md) §4).

### G2 — Learned knowledge is stored as hidden weights, not as inspectable claims
HBCP produces interpretable rules at the trial level. Bandits produce per-user posteriors. TaTT provides literature priors with provenance. **These three have not been connected**, so no system can say "the claim *BCT 8.2 lowers your evening cravings* went from prior 0.6 (expert consensus) to 0.2 (your data); we have stopped suggesting it". This is the gap the "Why Should This Work?" challenge describes. It is also a usable feature for smokers ("the app learns what works for *me* and tells me").

### G3 — JITAI "when" and "what" problems are solved separately, and receptivity is ignored in smoking
Risk prediction (mRisk, Businelle, Abo-Tabik) and receptivity detection (Künzler, Mishra) exist as separate threads. Content tailoring has evidence (Smart-T trigger-matching). **No smoking system combines risk × receptivity × content choice** ([03](03_jitai_sensing_prediction.md) §5).

### G4 — Proactive, pre-craving steering has not been tried
All smoking JITAIs are reactive (stress detected, location entered, craving logged). The lead time (~44 min before lapse in mRisk) and the strong acute effect of physical activity on cravings make **anticipatory substitution** ("you usually smoke after this meeting; a 5-minute walk now?") an open, well-grounded idea ([03](03_jitai_sensing_prediction.md) §6, [05](05_intervention_content.md)).

### G5 — Modular, missing-data-tolerant sensing
Every research JITAI assumes a fixed sensor kit. **Graceful degradation** (EMA-only users get a coarser but valid model; wearable users get finer timing) is unaddressed. It also matters for privacy and adoption.

### G6 — Evidence-strong ingredients are under-delivered by apps
Medication, incentives (CO-verified), exercise for cravings, ACT-style urge acceptance and trigger-matched content all have better evidence than trackers and badges, yet they are rarely the core of consumer apps ([01](01_evidence_base.md), [05](05_intervention_content.md)).

### G7 — Explanation and dark logic for the end user
No product explains its suggestions. None monitors negative side effects (guilt after slips, notification annoyance, over-reliance). Both are cheap to prototype and evaluable in **interviews and usability tests** (our constraint).

### G8 — Smoking-specific evidence for HAPA-driven apps
HAPA is well supported across behaviours, but smoking-app evidence is scarce. A HAPA-based app with measurable HAPA constructs (validated smoking HAPA scales exist) would contribute to the field.

### G9 — Cold start via conversation
Onboarding questionnaires are standard. Using an **MI-style intake conversation** (possibly LLM-assisted but schema-constrained) to set **priors** over intervention options and phase placement is suggested by several threads but not implemented.

## 3. Research ready to be implemented (low-hanging fruit)

| Finding | Source | Could become |
|---|---|---|
| Six EMA items predict 80% of lapses within 4 h | Businelle et al. (2016) | Baseline risk model for EMA-only users (G5) |
| Trigger-matched messages beat generic ones | Hébert et al. (2020) | Content-selection rule and a bandit prior |
| Moderate activity cuts cravings acutely | Haasova et al. (2013, 2014) | Craving option + wearable verification + pre-craving nudge (G4) |
| 3-min visuospatial game lowers craving ~20% | Skorka-Brown et al. (2014, 2015) | Distraction module (fits the "subconscious steering" idea) |
| ACT acceptance > avoidance on average | Bricker et al. (2020) | Two coping "styles" to compare per user (G1) |
| Thompson-sampling bandits with pooling, deployed safely | Liao et al. (2020); Tomkins et al. (2021); Trella et al. (2024) | Learning engine that works with few users |
| Receptivity models deployed live | Mishra et al. (2021) | Delivery-timing layer (G3) |
| BCIO + TaTT provide machine-readable BCT→MoA links with provenance | Michie et al. (2021); Johnston et al. (2021) | Knowledge layer schema + priors (G2) |
| Interpretable rules ≥ DNN for smoking outcome prediction | Hastings et al. (2023/2025) | Argument and design pattern for white-box learning |
| MI chatbot raises confidence. GPT-4 reflections are 88% acceptable with a checker | Brown et al. (2023); JMIR MH (2024) | Pre-intender module with a guard-rail (G9) |
| Lapse → relapse dynamics (negative affect, confidence) | Shiffman (1996; 2004) | Slip-recovery flow and recovery self-efficacy measurement |

## 4. Observations relevant to the two directions under consideration

These are SOTA observations only, not a recommendation. The critiqued comparison comes next.

**Direction A, the deep JITAI (right notification at the right moment):**
- The *pure* timing problem is already well covered (Quit Sense, Smart-T, Sense2Stop, bandit work in other domains). Novelty would have to come from G3 (risk × receptivity × content jointly), G4 (pre-craving steering) and G5 (modular sensing).
- Evaluation of timing models needs real field data. With interviews and usability only, we would rely on **public datasets or simulation**, which limits what we can claim.

**Direction B, the HAPA framework that orchestrates interchangeable sub-models:**
- Directly addresses G1, G2, G7 and G8, which are the emptiest cells in the matrix.
- Risk: breadth. A thin layer over many modules may look like "yet another stage-based app" unless the learning and explanation layer (G2) is real and demonstrable.
- A JITAI sub-module could still be included as **one decision type** within the orchestration, so the two directions are not mutually exclusive.

## 5. Corrections to our earlier sketches

- [jitai_smoking_cessation_architecture.md](../jitai_smoking_cessation_architecture.md) §6 says Sense2Stop triggered interventions "*before the user even consciously registered the craving*". Sense2Stop micro-randomised **stress-management prompts during detected stress**. It did not detect cravings ([03](03_jitai_sensing_prediction.md) §4). The iCoach/TTM claim in that document was not verified in this SOTA. Also note the TTM critique (West, 2005).
- The same document proposes COM-B as a *real-time* diagnostic layer. That is a reasonable design choice, but COM-B is a framework, not a predictive model. Real-time COM-B diagnosis from sensors has **no validation** that we found.
- [HAPA Quit App sketch](../HAPA%20Quit%20App%20—%20Sub-models%20and%20BCTs%20per%20Stage.md): its BCT choices are consistent with the evidence in [05](05_intervention_content.md). Missing candidates with good evidence: **financial incentives / CO verification**, **exercise for cravings** (only "walk" as a tip), **ACT-style acceptance** (urge surfing is included, but ACT is not named as a sub-model), and **medication adherence** (only information about medication is included).
