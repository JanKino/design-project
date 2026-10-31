# 06 — Theory, taxonomies and machine-readable knowledge

> **Question answered here:** Which behaviour-change models and knowledge resources exist that an app could *carry inside it* (white box), how well are they supported for smoking, and how do they link techniques → mechanisms → behaviour?
> Scope: this is a SOTA overview. *Choosing* between HAPA and alternatives is deliberately left for the refinement phase.

## 1. Stage / process models

| Model | Core idea | Fit for smoking | Evidence status | Relevance to us |
|---|---|---|---|---|
| **HAPA** (Schwarzer, 2008) | Motivational phase (risk perception, outcome expectancies, task self-efficacy → intention) vs volitional phase (action/coping planning, maintenance and recovery self-efficacy, action control) | Plausible. Volitional processes (self-efficacy, planning, action control) are key around a quit date in daily-diary data. **Rarely tested in smoking** compared with diet/PA (Chinese HAPA psychometrics paper, 2024). Hookah RCT positive | Meta-analysis across behaviours: 95 studies. Self-efficacy matters in both phases. Planning mediates (Zhang et al., 2019) | Natural backbone for phase logic. Recovery self-efficacy maps directly onto lapse handling. The **gap in smoking-specific HAPA app evidence** is itself a contribution opportunity |
| **TTM / Stages of Change** | Precontemplation → … → maintenance | Widely used historically (e.g. iCoach) | Strongly criticised: arbitrary stage cut-offs, poor predictive validity (West, 2005) | Avoid as backbone. Cite as a contrast |
| **COM-B / Behaviour Change Wheel** (Michie et al., 2011) | Behaviour = f(Capability, Opportunity, Motivation). Links to 9 intervention functions and 7 policy categories | Generic, used in many smoking interventions | Framework rather than predictive theory | Good *diagnostic* layer ("what is missing right now?"). Already used in our [JITAI sketch](../jitai_smoking_cessation_architecture.md) |
| **PRIME theory** (West, 2006) | Motivational system: Plans, Responses, Impulses, Motives, Evaluations. Momentary motivational balance and identity | Developed *for addiction*. Explains momentary lapses better than stage models | Theory, partially tested | Explains why the **moment** matters (impulse vs plan). Identity for maintenance |
| **Relapse Prevention** (Marlatt & Gordon) | High-risk situations, coping, abstinence violation effect | Core for smoking | Well established clinically. EMA-supported (Shiffman) | Lapse → slip flow |
| **Dual-process / habit theories** | Automatic vs reflective control. Cue-driven habits | Smoking is strongly cue-driven | Supported | Justifies cue avoidance, ApBM, habit replacement |
| **Maintenance theories** (Kwasnicka et al., 2016) | Five themes: maintenance motives, self-regulation, resources, habits, environmental/social influences | Generic | Review | Phase 3/4 design |
| **Dynamic / control-systems models** (Riley et al., 2011; Hekler et al., 2016; Nahum-Shani et al., 2015) | Behaviour as a dynamic system with time-varying states and feedback | Needed for JITAIs | Methodological | The bridge between static theories and adaptive algorithms |

## 2. Technique taxonomies and ontologies (machine-readable layer)

| Resource | What it gives | Machine-readable? | Notes |
|---|---|---|---|
| **BCT Taxonomy v1** (Michie et al., 2013) | 93 techniques in 16 groups, with definitions | Yes, and now part of BCIO | The lingua franca. Our HAPA sketch already codes features with BCTTv1 |
| **Behaviour Change Intervention Ontology (BCIO)** (Michie et al., 2021) | Upper-level classes: intervention content, delivery (mode, source, schedule), setting, population, mechanism of action, behaviour, outcome. Sub-ontologies for BCTs, MoAs, mode of delivery etc. | **Yes** (OWL, open). https://www.bciobrowser.com | Directly usable as a schema for a knowledge layer |
| **BCT–Mechanism of Action links** (Carey et al., 2019; Connell et al., 2019) | Links from literature (Carey) and expert consensus (Connell) between 56 BCTs and 26 MoAs | Yes (data) | Carey: a "starting graph", but few links are *empirically tested* |
| **Theory and Techniques Tool (TaTT)** (Johnston et al., 2021) | Triangulated evidence: 92 hypothesised BCT–MoA links and 460 agreed "non-links". Interactive heat-map of 1,456 links | Online tool + data | **Edge weights with provenance**: literature vs expert vs both. Exactly the provenance the challenge asks for |
| **Human Behaviour-Change Project (HBCP)** | ML extraction of BCIO entities from smoking cessation trial reports (F1 0.42 vs 0.75 for humans) and an interpretable outcome predictor (MAE ≈ 9 pp) | Tool + rules | Smoking-specific. Shows that ontology-structured, interpretable prediction is feasible (West et al., 2023/2024; Hastings et al., 2023/2025) |
| **Intervention Mapping** (Bartholomew Eldredge et al.) | Systematic planning: needs → change objectives → methods → applications → implementation → evaluation | Process, not data | Gives the psychologists' workflow. Health-promotion students use it (cf. the challenge text) |

## 3. Causality beyond chains

- **Causal pies** (Rothman, 1976): a cause is usually an *insufficient but necessary part of an unnecessary but sufficient* set (INUS). Personalisation then becomes: *which sufficient set is cheapest to complete for this person?* (challenge text).
- **Configurational methods.** Qualitative Comparative Analysis (QCA) has been used to find *combinations* of BCTs that suffice for adherence (Kahwati et al., 2016, medication-adherence QCA). It handles non-additive patterns and small samples. It has **not been applied inside an adaptive app** as far as we found.
- **Micro-randomisation and factorial designs** estimate causal effects of components and their **moderation by context**, which approximates "in which combination, for whom, in which context" (Klasnja et al., 2015; Collins, 2018).
- **External validity** (Cartwright, 2011): "it worked there" ≠ "it works here". An app that imports literature claims as *priors* and updates them on local data operationalises this caution.
- **Dark logic** (Bonell et al., 2015): theorise harmful pathways explicitly (guilt, reactance, dependence, shifting responsibility to the individual).

## 4. What exists vs what is missing on the theory side

**Exists:**
- Rich, open, machine-readable vocabularies (BCTTv1, BCIO) and evidence-weighted BCT–MoA links (TaTT).
- Interpretable outcome prediction at the *trial* level (HBCP).
- Stage-based app designs (many), and HAPA ontologies for physical activity.

**Missing:**
1. **Person-level, runtime use** of BCIO/TaTT: no app we found uses the ontology at *runtime* to pick and justify interventions.
2. **Claims with conditions (phase, context) and provenance that are *updated by user data*.** HBCP learns from trials, bandits learn from users, and nobody connects the two.
3. **Conjunctive (pie-shaped) representations** in app logic: almost all decision rules are single-cause IF–THEN.
4. **Smoking-specific HAPA evidence in apps.** The constructs are measurable (2024 Chinese HAPA smoking scales), but app trials are lacking.
5. **Dark-logic monitoring** as a first-class part of the model.

## References for this file

- Bartholomew Eldredge, L. K., et al. (2016). *Planning Health Promotion Programs: An Intervention Mapping Approach* (4th ed.). Jossey-Bass.
- BCIO browser. https://www.bciobrowser.com
- Bonell, C., Jamal, F., Melendez-Torres, G. J., & Cummins, S. (2015). 'Dark logic': Theorising the harmful consequences of public health interventions. *Journal of Epidemiology and Community Health, 69*(1), 95–98. https://doi.org/10.1136/jech-2014-204671
- Carey, R. N., et al. (2019). Behavior change techniques and their mechanisms of action: A synthesis of links described in published intervention literature. *Annals of Behavioral Medicine, 53*(8), 693–707. https://doi.org/10.1093/abm/kay078
- Cartwright, N. (2011). A philosopher's view of the long road from RCTs to effectiveness. *The Lancet, 377*(9775), 1400–1401. https://doi.org/10.1016/S0140-6736(11)60563-1
- Connell, L. E., et al. (2019). Links between behavior change techniques and mechanisms of action: An expert consensus study. *Annals of Behavioral Medicine, 53*(8), 708–720. https://doi.org/10.1093/abm/kay082
- HAPA smoking-cessation psychometrics among Chinese smokers (2024). *Scientific Reports*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10876652/
- Johnston, M., et al. (2021). Development of an online tool for linking behavior change techniques and mechanisms of action based on triangulation of findings from literature synthesis and expert consensus. *Translational Behavioral Medicine, 11*(5), 1049–1065. https://doi.org/10.1093/tbm/ibaa050 · Tool: https://theoryandtechniquetool.humanbehaviourchange.org
- Kahwati, L., et al. (2016). Using qualitative comparative analysis in a systematic review of a complex intervention. *Systematic Reviews, 5*, 82. https://doi.org/10.1186/s13643-016-0256-y
- Kwasnicka, D., Dombrowski, S. U., White, M., & Sniehotta, F. (2016). Theoretical explanations for maintenance of behaviour change: A systematic review of behaviour theories. *Health Psychology Review, 10*(3), 277–296. https://doi.org/10.1080/17437199.2016.1151372
- Michie, S., van Stralen, M. M., & West, R. (2011). The behaviour change wheel: A new method for characterising and designing behaviour change interventions. *Implementation Science, 6*, 42. https://doi.org/10.1186/1748-5908-6-42
- Michie, S., et al. (2013). The behavior change technique taxonomy (v1) of 93 hierarchically clustered techniques. *Annals of Behavioral Medicine, 46*(1), 81–95. https://doi.org/10.1007/s12160-013-9486-6
- Michie, S., et al. (2021). Developing an evidence-based online method of linking behaviour change techniques and theoretical mechanisms of action: upper level of the Behaviour Change Intervention Ontology. *Wellcome Open Research, 5*, 123. https://doi.org/10.12688/wellcomeopenres.15908.2
- Rothman, K. J. (1976). Causes. *American Journal of Epidemiology, 104*(6), 587–592. https://doi.org/10.1093/oxfordjournals.aje.a112335
- Schwarzer, R. (2008). Modeling health behavior change: How to predict and modify the adoption and maintenance of health behaviors. *Applied Psychology, 57*(1), 1–29. https://doi.org/10.1111/j.1464-0597.2007.00325.x
- Volitional processes and daily smoking around a quit attempt (daily-diary study, n = 100). https://api-pubmed-ncbi.laibokeji.com/25293634 (PubMed 25293634)
- West, R. (2005). Time for a change: Putting the Transtheoretical (Stages of Change) Model to rest. *Addiction, 100*(8), 1036–1039. https://doi.org/10.1111/j.1360-0443.2005.01139.x
- West, R. (2006). *Theory of Addiction*. Blackwell (PRIME theory).
- Zhang, C.-Q., Zhang, R., Schwarzer, R., & Hagger, M. S. (2019). A meta-analysis of the health action process approach. *Health Psychology, 38*(7), 623–637. https://doi.org/10.1037/hea0000728
- See also [04](04_adaptive_learning_ai.md) for HBCP (Hastings et al.; West et al.), Klasnja et al. (2015), Collins (2018); [03](03_jitai_sensing_prediction.md) for Riley et al. (2011), Hekler et al. (2016), Nahum-Shani et al. (2015).
