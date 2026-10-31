# 04 — Adaptive learning and AI for behaviour-change interventions

> **Question answered here:** Which learning methods are used to personalise *what*, *when* and *how* support is delivered? What has been deployed, what is only simulated, and how explainable is it?

## 1. Landscape of methods

| Family | What it learns | Exemplars | Deployed in humans? | Explainability |
|---|---|---|---|---|
| **Expert rules / decision tables** | Nothing. Hand-coded state→action rules | Smart-T risk tiers, most JITAIs, our existing [JITAI architecture sketch](../jitai_smoking_cessation_architecture.md) Phase 1 | Yes | Full (rules are readable) |
| **Supervised risk prediction** | P(craving/lapse \| context) | Businelle et al. (2016); mRisk (Ullah et al., 2022); Abo-Tabik et al. (2026) | Partly (as triggers) | Low for deep models. Medium for small models |
| **Micro-randomised trials (MRT)** | Average and moderated *causal* proximal effect of an option, by randomising at each decision point | HeartSteps (Klasnja et al., 2015), Sense2Stop (Battalio et al., 2021) | Yes | High: effects are causal estimates per context |
| **Contextual bandits (Thompson sampling, Bayesian linear models)** | Which option (incl. "do nothing") maximises the proximal outcome in a given context, *per person*, online | HeartSteps V2 (Liao et al., 2020), Oralytics (Trella et al., 2022/2024), MiWaves (cannabis; Ghosh et al., 2024), IntelligentPooling (Tomkins et al., 2021), reBandit | **Yes**, in clinical trials | Medium: linear-Bayesian posteriors are inspectable |
| **Full RL (MDP, states evolve)** | Long-term value of action sequences | TU Delft virtual coach for quit preparation (Albers, Neerincx & Brinkman, 2022). Follow-up comparing bandit and RL policies (PMC12512882, 2025) | Yes (online studies) | Low–medium |
| **SMART / adaptive treatment strategies** | Best *sequence* of intervention stages, e.g. "if no response at week 2, augment with X" | Collins (2018), MOST framework | Yes | High |
| **Factorial optimisation (MOST)** | Which components are active ingredients | SmokeFree Baby app factorial (Tombor et al., 2018); e-cig components 2⁵ factorial (Kimber et al., 2023) | Yes | High |
| **Outcome prediction from literature** | Predict trial outcome from BCTs + context + population | Human Behaviour-Change Project: an interpretable, ontology-organised rule model beat a DNN (MAE 9.15 vs 9.42 percentage points) on 971 study arms (Hastings et al., 2023/2025) | Tool only | **High (by design)** |
| **LLM conversational agents** | Natural dialogue. MI reflections. Answering free questions | QuitBot (Bricker et al., 2024), MIBot (Brown et al., 2023), GPT-4 reflections (2024) | Yes | Low (no stable reasons). Hallucination risk |
| **LLM as JITAI decision-maker** | Chooses whether, when and what to send from a context description | "The Last JITAI?": GPT-4 decisions rated better than those of healthcare professionals (Haag et al., CHI 2025). LLM + RL hybrids (arXiv 2501.06980; arXiv 2507.03871) | Mostly vignette/simulation studies | Low–medium (can produce rationales, but these are not guaranteed faithful) |

## 2. Deployed online learning in mHealth: lessons

- **HeartSteps V2** uses a Bayesian contextual bandit with Thompson sampling, five decision times per day, deciding whether to send an activity suggestion. Key design choices: **action centering** (only the treatment effect is modelled), **priors from earlier MRT data** to handle cold start, and a **dosage/burden term** to avoid over-prompting (Liao et al., 2020).
- **Oralytics** deploys a Thompson-sampling bandit in a registered trial, with two decision times per day for 70 days. The team stresses *pre-specified, auditable* algorithms and simulation testbeds built from previous data before deployment (Trella et al., 2024, "A deployed online RL algorithm in an oral health clinical trial").
- **MiWaves** applies the same recipe to reducing cannabis use in emerging adults, which is the closest **addiction** analogue (deployed March–May 2024).
- **Pooling across users** (IntelligentPooling; reBandit with random effects) addresses the small-data problem: learn per person, but borrow strength from similar people.
- **TU Delft virtual coach** (Albers et al., 2022): more than 500 smokers. The RL algorithm chose persuasion types for *preparatory activities* and considered **current and future states** (e.g. effort, perceived importance). Dataset of 2,366 messages to 671 people is public. A 2025 follow-up compares bandit vs full-RL policies for proposing competence-building activities (PMC12512882). This is the most directly relevant smoking-specific learning work, and it targets the **preparation phase**, not cravings.

**Practical takeaways for us:**
1. Online learning of *which option for whom* has been done in the field, but on **one decision type at a time** (send or not; which persuasion type).
2. **No deployed system learns across multiple intervention types *and* phases**, e.g. choosing between a buddy mechanism, a coping-plan revision and an urge-surfing prompt.
3. The successful systems are **Bayesian, low-dimensional and theory-informed** (features chosen by domain experts), not deep RL. This matters for explainability.

## 3. Conversational agents and LLMs in smoking cessation

| System | Design | Evidence |
|---|---|---|
| **QuitBot** | 42-day program. Scripted dialogues + Q&A library + fine-tuned GPT-3.5 fallback for unanticipated questions. 11-step user-centred design over 4 years | Pilot positive. **Full RCT null** vs SMS (registry) |
| **MIBot** (Toronto) | Motivational-interviewing chatbot for *ambivalent* smokers. Generates reflections with a fine-tuned transformer and later GPT-4 | 349 smokers: confidence to quit increased in all versions after 1 week. Quit attempts unchanged. Much of the effect came from asking questions alone (Brown et al., 2023). GPT-4: 88% of complex reflections acceptable, so an automatic checker is needed (2024) |
| **Reviews (2024)** | 8–31 studies on chatbots for tobacco | Better engagement and sometimes abstinence. Heterogeneous. Perceived empathy (Lachance et al., 2024; Frontiers Digital Health, 2025) |

**Reading:** LLMs are good at **delivery** (natural, empathic, MI-consistent language) and possibly at **context interpretation**. There is no evidence that they choose interventions better *in outcomes*. Their reasoning is not a reliable explanation of *why*, which conflicts with the "white box" requirement unless they are constrained by an explicit model: the LLM *renders* a decision that a transparent layer has made.

## 4. Explainability in adaptive behaviour-change systems

- **Rudin (2019):** for high-stakes decisions, build interpretable models instead of explaining black boxes afterwards. The HBCP result, where an interpretable rule model beat a DNN, is a smoking-specific confirmation (Hastings et al., 2023/2025).
- **Bayesian bandits** expose posteriors per option and context, so it is possible to report "we are 80% sure that walking helps you more than breathing exercises in the evening", including uncertainty.
- **Ontology / knowledge-graph recommenders.** A HAPA-centred ontology for physical activity personalises action and coping planning (Atlantis Press). The I-Change-based health recommender explains its own design process (*Opening the Black Box…*, IEEE Access, 2019). Personal health knowledge graphs support path-based explanations (survey, arXiv 2606.15155). **None of these combine an explicit theory graph with online learning that updates the claims themselves**, which is the core demand of the "Why Should This Work?" challenge.
- **User-facing explanations** ("why am I seeing this?") raise trust and acceptance in recommenders (Tintarev & Masthoff, 2007). We found no smoking app that provides them.

## 5. Gaps specific to learning (carried to [07](07_gap_analysis.md))

1. **Hierarchical action spaces are unexplored in deployed systems.** Phase → program theory/sub-model → BCT → concrete feature/message → timing. Every deployed learner works on one flat level.
2. **Learning that updates *theory claims*, not hidden weights.** Bandit posteriors could be attached to explicit claims ("BCT 8.2 reduces craving for user U in context C"). This would merge MRT-style causal estimation with a knowledge graph. We found no implementation.
3. **Graceful degradation over modalities.** Bandit context vectors with missing features (EMA-only users vs wearable users) have not been studied in this domain.
4. **Cold start from an onboarding conversation.** Using an MI-style intake (or LLM-structured intake) to set **priors** over options is suggested by the TU Delft and HeartSteps work but not implemented end-to-end.
5. **Proximal outcomes beyond "did they respond".** Most learners optimise engagement or step counts. In smoking, cheap proximal outcomes such as craving 10 minutes later, plan used and slip/no slip are available but rarely used as rewards (Sense2Stop uses stress).
6. **Safety and dark logic in the reward.** No deployed system penalises guilt, annoyance or dependence explicitly, apart from the burden terms in HeartSteps.

## References for this file

- Albers, N., Neerincx, M. A., & Brinkman, W.-P. (2022). Addressing people's current and future states in a reinforcement learning algorithm for persuading to quit smoking and to be physically active. *PLOS ONE, 17*(12), e0277295. https://pmc.ncbi.nlm.nih.gov/articles/PMC9714722
- (2025). Reinforcement learning for proposing smoking cessation activities that build competencies: Combining two worldviews in a virtual coach. PMC12512882 (TU Delft line of work; verify author list). https://pmc.ncbi.nlm.nih.gov/articles/PMC12512882/
- Brown, A., et al. (2023). A motivational interviewing chatbot with generative reflections for increasing readiness to quit smoking. *JMIR Mental Health, 10*, e49132. https://pmc.ncbi.nlm.nih.gov/articles/PMC10618902
- GPT-4 backward-looking complex reflections for MI chatbot (2024). *JMIR Mental Health*. https://doaj.org/article/a7c684332daa4e58942fce936b7d91b0
- Collins, L. M. (2018). *Optimization of Behavioral, Biobehavioral, and Biomedical Interventions: The Multiphase Optimization Strategy (MOST)*. Springer. https://doi.org/10.1007/978-3-319-72206-1
- Ghosh, S., et al. (2024). MiWaves reinforcement learning algorithm. arXiv. https://arxiv.org/html/2312.06403v1
- Haag, D., et al. (2025). The Last JITAI? Exploring large language models for issuing just-in-time adaptive interventions. *Proc. CHI 2025*. https://doi.org/10.1145/3706598.3713307 · arXiv:2402.08658
- Hastings, J., et al. (2023/2025). Predicting outcomes of smoking cessation interventions in novel scenarios using ontology-informed, interpretable machine learning. *Wellcome Open Research*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12603517/
- Kimber, C., et al. (2023). Optimising e-cigarette-oriented components: a 2⁵ factorial trial (MOST). *Addiction*. https://discovery.ucl.ac.uk/id/eprint/10172396
- Klasnja, P., et al. (2015). Microrandomized trials: An experimental design for developing just-in-time adaptive interventions. *Health Psychology, 34*(S), 1220–1228. https://doi.org/10.1037/hea0000305
- Lachance, et al. (2024). See [01](01_evidence_base.md).
- Liao, P., Greenewald, K., Klasnja, P., & Murphy, S. (2020). Personalized HeartSteps: A reinforcement learning algorithm for optimizing physical activity. *Proc. ACM IMWUT, 4*(1), 18. https://arxiv.org/abs/1909.03539
- LLM + RL for adaptive interventions: arXiv:2501.06980 https://arxiv.org/pdf/2501.06980 ; arXiv:2507.03871 https://arxiv.org/pdf/2507.03871
- *Opening the Black Box: Explaining the process of basing a health recommender system on the I-Change behavioral change model* (2019). *IEEE Access*.
- Rudin, C. (2019). Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. *Nature Machine Intelligence, 1*(5), 206–215. https://doi.org/10.1038/s42256-019-0048-x
- Semantic reasoning in medicine: the role of knowledge graphs (survey). arXiv:2606.15155. https://arxiv.org/pdf/2606.15155
- Tintarev, N., & Masthoff, J. (2007). A survey of explanations in recommender systems. *Proc. IEEE ICDE Workshops*, 801–810. https://doi.org/10.1109/ICDEW.2007.4401070
- Tombor, I., et al. (2018). Randomised factorial experiment of components of the SmokeFree Baby smartphone application. *Nicotine & Tobacco Research*. https://discovery-pp.ucl.ac.uk/10050035/
- Tomkins, S., Liao, P., Klasnja, P., & Murphy, S. (2021). IntelligentPooling: Practical Thompson sampling for mHealth. *Machine Learning, 110*, 2685–2727. https://doi.org/10.1007/s10994-021-05995-8
- Trella, A. L., et al. (2024). A deployed online reinforcement learning algorithm in an oral health clinical trial (Oralytics). arXiv:2409.02069. https://arxiv.org/abs/2409.02069
- West, R., et al. (2023/2024). Using machine learning to extract information and predict outcomes from reports of randomised trials of smoking cessation interventions in the Human Behaviour-Change Project. *Wellcome Open Research*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11109593/
