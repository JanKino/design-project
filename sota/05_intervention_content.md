# 05 — Intervention content: which techniques have evidence, and what is under-used in apps

> **Question answered here:** What could the app actually *deliver*? Which techniques have good evidence, and which research findings have barely been turned into app features? This file lists the candidate building blocks an adaptive system could choose between.

## 1. Catalogue of candidate building blocks

Evidence strength: ●●● strong (meta-analysis / large RCT) · ●● moderate (RCTs, mixed) · ● preliminary (lab, pilot) · ○ theory only.
"In apps?" = how common the technique is in available apps (see [02](02_app_landscape.md)).

| Building block | Mechanism / theory | Evidence for smoking | In apps? | Notes |
|---|---|---|---|---|
| **Pharmacotherapy prompting & adherence** (varenicline, cytisine, combination NRT) | Withdrawal relief | ●●● (Cochrane pharmacotherapy reviews) | Rare / weak (Abroms et al., 2013; Bustamante et al., 2021) | The app could *raise uptake and adherence*. This is high-value and under-used |
| **Financial incentives / contingency management** with CO verification | Operant reinforcement | ●●● (Notley et al., 2019) | Pivot, CureApp (CO), research (INSIGHT, NCT04881630) | Needs a CO device and funding. Non-monetary variants (Re-Connect, personalised smartphone rewards) are under study |
| **Acceptance & Commitment Therapy** (urge acceptance, values) | Experiential acceptance | ●● (iCanQuit RCT, Bricker et al., 2020) | iCanQuit only | Outperformed avoidance-based content |
| **CBT skills** (trigger analysis, coping) | Cognitive-behavioural | ●● (Quit Genius, industry RCT) | Several | Standard |
| **Mindfulness / urge surfing** | Decoupling craving → smoking | ● / ●● (Craving to Quit: mechanism effect, no outcome effect; Garrison et al., 2020) | Several | Best as one option among others, not the whole program |
| **Brief physical activity for cravings** | Acute craving reduction | ●●● for the *acute* effect: IPD meta-analysis, SMD ≈ −1.9 to −2.0 for desire to smoke; moderate/vigorous intensity works best (Haasova et al., 2013; 2014) | Mentioned as a tip | **Under-used**: a strong acute effect that could be triggered or verified with wearables |
| **Visuospatial distraction** (e.g. Tetris-like 3-min game) | Elaborated Intrusion theory: craving is imagery-based, and visuospatial load competes with it | ● lab + field: ~20–24% craving reduction (Skorka-Brown et al., 2014; 2015). Visual imagery tasks reduce cigarette craving (May et al., 2010) | **Not found in apps** as an evidence-based feature | Cheap to build. Matches the "distraction" idea |
| **Functional imagery / episodic future thinking** | Motivational imagery | ● | Rare | Related to EI theory |
| **Approach bias modification** (push away smoking cues) | Retrain automatic action tendencies | ● / mixed: app-based ApBM reduced smoking vs no training, but not clearly vs sham (Machulska et al., 2023). Modif-i Tobacco RCT ongoing (ACTRN12624000633583) | Research apps only | Gamifiable training |
| **Implementation intentions / coping plans** (if-then) | Automatic cue-response linkage | ●● across behaviours. Planning and self-efficacy rise in digital smoking programs (Happy Ending RCT), volitional processes are key around the quit date (daily diary studies) | Partial | Central in the [HAPA sketch](../HAPA%20Quit%20App%20—%20Sub-models%20and%20BCTs%20per%20Stage.md) |
| **Social support / buddy / community** | Social support, accountability | ●● for engagement. Network integration predicts abstinence (BecomeAnEX; Graham et al., 2017) | Community forums common. Real **buddy** mechanics rare | The quality of the tie matters more than the feature |
| **Motivational interviewing** (pre-intenders) | Resolve ambivalence | ●● (human MI). ● for chatbot MI (Brown et al., 2023) | Rare | About 80% of smokers are ambivalent, so this is a large under-served group |
| **Self-affirmation, EPPM-style risk + efficacy messages** | Reduce defensiveness | ● / ●● (general health communication) | Rare | Phase 1 candidates in the HAPA sketch |
| **Gamification** (levels, badges) | Operant / engagement | ● (correlational; Rajani et al., 2023) | Very common | Engagement tool, not an active ingredient by itself |
| **Identity change** ("I am a non-smoker") | PRIME theory | ● / ●● (SmokeFree Baby identity component tested in a factorial trial; Tombor et al., 2018) | Rare | Maintenance phase |
| **Slip/lapse recovery** (abstinence-violation-effect reframing) | Relapse prevention (Marlatt) | ●● (theory and EMA evidence on lapse → relapse dynamics; Shiffman et al., 1996; Shiffman & Waters, 2004) | Some apps simply reset counters | A first lapse caused by negative affect is more likely to progress to relapse. Abstinence confidence after the lapse predicts relapse |
| **E-cigarettes as a quit aid** | Nicotine substitution | ●●● (Cochrane living review on e-cigarettes, high-certainty for NRT comparison) | Rare, sensitive | A policy and ethics choice for the team. Be explicit about it |

## 2. Lapse and relapse dynamics (what the app must anticipate)

- Most first lapses happen in **high-risk situations**: when smoking is permitted, cigarettes are available, other smokers are present, and alcohol is involved (Shiffman et al., 1996).
- **Negative affect rises in the hours before a first lapse**, and stress-attributed lapses are especially predictable from it (Shiffman & Waters, 2004). Negative affect × smoking cues act synergistically.
- **Confidence after a lapse** predicts whether it becomes a relapse (Shiffman et al., 2005). This is the HAPA *recovery self-efficacy* construct and a clear app target.
- Mixed findings: some EMA studies find weak within-person affect–smoking links, and anhedonia or low positive affect can matter more than negative affect. This argues for **per-person** models rather than one global rule.

## 3. Under-used research findings (could be implemented, largely aren't)

1. **Exercise "snacks" for cravings**: strong acute evidence, wearable-verifiable, rarely operationalised as an *adaptive* option.
2. **Visuospatial distraction games** grounded in Elaborated Intrusion theory: cheap, testable, absent from evidence-based apps.
3. **Trigger-matched content** (Smart-T secondary analysis): tailoring the message to the *currently active* trigger works better than generic messages.
4. **Medication uptake and adherence nudges**: the strongest lever, the least present in apps.
5. **Non-monetary personalised rewards** (Re-Connect project) and CO-verified incentives.
6. **MI for pre-intenders via a constrained conversational agent.**
7. **Acceptance-based (ACT) craving handling** as an alternative to avoidance. The two styles could be *compared per person*.
8. **Receptivity-aware delivery** (from the physical activity and mental health literature) applied to smoking.

## References for this file

- Abroms et al. (2013); Bustamante et al. (2021) — see [01](01_evidence_base.md).
- Bricker et al. (2020) — see [01](01_evidence_base.md).
- Brown et al. (2023) — see [04](04_adaptive_learning_ai.md).
- Garrison et al. (2020) — see [01](01_evidence_base.md).
- Graham et al. (2017) — see [01](01_evidence_base.md).
- Haasova, M., et al. (2013). The acute effects of physical activity on cigarette cravings: Systematic review and meta-analysis with individual participant data. *Addiction, 108*(1), 26–37. https://ore.exeter.ac.uk/repository/handle/10871/13951
- Haasova, M., et al. (2014). The acute effects of physical activity on cigarette cravings: Exploration of potential moderators, mediators and physical activity attributes using individual participant data. *Psychopharmacology, 231*, 1267–1275. https://researchportal.plymouth.ac.uk/en/publications/the-acute-effects-of-physical-activity-on-cigarette-cravings-expl-2/
- Happy Ending fully automated internet + mobile program (2008). *Journal of Medical Internet Research, 10*(5), e51. https://jmir.org/2008/5/e51
- Machulska, A., et al. (2023). Mobile phone-based approach bias retraining for smokers seeking abstinence: A randomized-controlled study. *International Journal of Mental Health and Addiction*. https://link.springer.com/content/pdf/10.1007/s11469-023-01107-w.pdf
- May, J., Andrade, J., Panabokke, N., & Kavanagh, D. (2010). Visuospatial tasks suppress craving for cigarettes. *Behaviour Research and Therapy, 48*(6), 476–485. https://pearl.plymouth.ac.uk/handle/10026.1/991
- Modif-i Tobacco trial, ACTRN12624000633583. https://anzctr.org.au/ACTRN12624000633583.aspx
- Notley et al. (2019) — see [01](01_evidence_base.md).
- Re-Connect: Personalized, non-monetary smartphone-based rewards for smoking cessation (University of Kentucky project). https://scholars.uky.edu/en/projects/re-connect-personalized-non-monetary-smartphone-based-rewards-for/
- Shiffman, S., Paty, J. A., Gnys, M., Kassel, J. A., & Hickcox, M. (1996). First lapses to smoking: Within-subjects analysis of real-time reports. *Journal of Consulting and Clinical Psychology, 64*(2), 366–379. https://doi.org/10.1037/0022-006X.64.2.366
- Shiffman, S., & Waters, A. J. (2004). Negative affect and smoking lapses: A prospective analysis. *Journal of Consulting and Clinical Psychology, 72*(2), 192–201. https://doi.org/10.1037/0022-006X.72.2.192
- Shiffman, S., et al. (2005), as summarised in later EMA work: day-to-day abstinence confidence predicts relapse after a first lapse. https://pmc.ncbi.nlm.nih.gov/articles/PMC3336035
- Skorka-Brown, J., Andrade, J., & May, J. (2014). Playing 'Tetris' reduces the strength, frequency and vividness of naturally occurring cravings. *Appetite, 76*, 161–165. https://pearl.plymouth.ac.uk/handle/10026.1/2925
- Skorka-Brown, J., Andrade, J., Whalley, B., & May, J. (2015). Playing Tetris decreases drug and other cravings in real world settings. *Addictive Behaviors, 51*, 165–170. https://doi.org/10.1016/j.addbeh.2015.07.020
- Tombor et al. (2018); Rajani et al. (2023) — see [04](04_adaptive_learning_ai.md) and [01](01_evidence_base.md).
- Lindson, N., et al. (2024). Electronic cigarettes for smoking cessation. *Cochrane Database of Systematic Reviews* (living review). https://doi.org/10.1002/14651858.CD010216
