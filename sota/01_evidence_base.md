# 01 — Evidence base: do digital smoking-cessation interventions work?

> **Question answered here:** What does the trial evidence say about apps, text messaging, chatbots and other digital formats, and what seems to make the difference?
> Evidence tags: `[SR/MA]` systematic review / meta-analysis · `[RCT]` randomised trial · `[pilot]` pilot/feasibility trial · `[obs]` observational · `[industry]` funded or authored by the vendor · `[registry]` results only on a trial registry.

## 1. The headline picture

| Format | Best current evidence | Verdict |
|---|---|---|
| **Automated text messaging (SMS)** | Cochrane review, 26 RCTs, n = 33,849 `[SR/MA]` (Whittaker et al., 2019) | **Moderate-certainty benefit** over minimal support. |
| **Smartphone apps (as a category)** | Same Cochrane review: 5 studies, n = 3,079, RR 1.00 (0.66–1.52) for apps vs minimal support or less intensive apps `[SR/MA]` (Whittaker et al., 2019) | **No proven benefit as a category** (low certainty). NIHR summarised this as "*text messaging helps smokers quit but apps not yet shown to work*". |
| **Specific well-designed apps** | iCanQuit (ACT) vs NCI QuitGuide, n = 2,415, 12-month 30-day abstinence **28.2% vs 21.1%**, OR 1.49 `[RCT]` (Bricker et al., 2020) | Individual apps **can** work. Content and theory matter more than "being an app". |
| **Financial incentives / contingency management** | Cochrane: **high-certainty** evidence that incentives raise long-term quit rates `[SR/MA]` (Notley et al., 2019; updated 2025) | One of the strongest techniques overall. Remote versions with smartphone-paired CO monitors exist but are mostly feasibility-stage. |
| **Chatbots / conversational agents** | Several 2024 reviews report promising results, but the studies are heterogeneous and small `[SR]` (Lachance et al., 2024; Chen et al., 2024). Full QuitBot RCT (n ≈ 1,650): **null** at 12 months (OR 0.96) `[registry]` | **Promising engagement, unproven added effect**. |
| **JITAIs (context-triggered support)** | Review of JITAIs for substance use: engagement moderate to high, **effectiveness mixed**, no meta-analysis possible `[SR]` (Perski et al., 2022) | **Under-tested**. The best smoking JITAI evidence is a feasibility RCT (Quit Sense). |

**Key takeaway.** The field does not lack apps. It lacks **apps with evidence**. Effects come from specific content (ACT, CBT, incentives, medication uptake) delivered with enough engagement. Features alone (trackers, badges) have not been shown to produce effects.

## 2. Key trials of named apps and programs

| App / program | Approach | Design and result | Caveats |
|---|---|---|---|
| **iCanQuit** (Fred Hutch) | Acceptance and Commitment Therapy: *accept* urges rather than avoid them | RCT n = 2,415 vs QuitGuide. 12-mo 30-day PPA 28.2% vs 21.1% (OR 1.49, 95% CI 1.22–1.83). Retention 87% `[RCT]` (Bricker et al., 2020) | Self-reported abstinence. Patent held by the institution. |
| **Quit Genius** (now Pelago) | Digital CBT + coaching + NRT | RCT n = 556 vs *very brief advice*. 4-week 7-day PPA 44.5% vs 28.7% (RR 1.55) `[RCT][industry]` (Webb et al., 2020). Biochemically verified difference significant at 26 weeks, not at 52 (Webb et al., 2022) | Weak comparator. Authors employed by the company. |
| **Smoke Free** | BCT-rich app with daily "missions" (push notifications) | Exploratory RCT, ~28,000 users, full vs reduced version. Missions associated with ≈1.9× odds of 3-month abstinence `[RCT][industry]` (Crane et al., 2019) | Very low follow-up, not pre-registered. Lead author owns the app. |
| **Pivot** (Carrot Inc.) | App + personal breath-CO sensor + coaching + NRT | Cohort n = 319, ITT 30-day PPA 31.3% at follow-up `[obs][industry]` (Marler et al., 2021). Pilot RCT vs QuitGuide: higher engagement `[pilot][industry]` (Marler et al., 2022) | Company-run. Not a definitive RCT. |
| **CureApp SC** (Japan) | Prescription app + doctor app + home CO checker | Approved by Japan's MHLW in 2020 and reimbursed by public insurance (first such approval for nicotine dependence) `[RCT]` (Masaki et al., 2020; CureApp press release) | Used alongside clinic treatment, not standalone. |
| **Quit Sense** (UK) | JITAI: learns the user's smoking locations and contexts during a pre-quit phase, then gives location-triggered support | Feasibility RCT n = 209. 6-month verified abstinence **11.5% vs 2.9%** (aOR 4.57, 95% CI 1.23–16.94) `[pilot]` (Naughton et al., 2023; 2024) | Wide CI. COVID limited the location-based support. Only 51% of installers engaged for more than one week. |
| **Smart-T / Smart-T2** (Oklahoma) | EMA-driven lapse-risk estimator → risk-tailored messages | Pilot RCT n = 84. Verified 7-day PPA at 12 weeks: 22% vs 15% vs 15% `[pilot]` (Hébert et al., 2020). Messages tailored to a specific trigger reduced that trigger more than generic ones | Small sample. The successor (OKquit) RCT has no published results yet. |
| **QuitBot** (Fred Hutch / Microsoft) | Conversational agent with a scripted Q&A library and a fine-tuned GPT-3.5 fallback | Pilot: 63% vs 38.5% (complete-case) `[pilot]` (Bricker et al., 2024). **Full RCT: 186/821 vs 191/826, OR 0.96 (null)** `[registry]` (NCT04308759) | Shows that a strong pilot can fail to replicate. |
| **Craving to Quit** | App-based mindfulness training | RCT: **no difference** in smoking vs control app, but the craving→smoking link weakened `[RCT]` (Garrison et al., 2020) | Mechanism effect without an outcome effect. |
| **Kwit** | Gamified CBT: levels, diary | n = 44. Each unlocked level was associated with OR 1.22 for 7-day abstinence `[obs][industry]` (Rajani et al., 2023) | Correlational. Engaged users unlock more levels. |
| **BecomeAnEX** (Truth Initiative) | Web program + online community | 2×2 factorial (social network × NRT), n ≈ 5,290. Higher adherence. Integration into the network predicted abstinence `[RCT]` (Graham et al., 2017; Cutrona et al.) | Web, not app. Effects were mainly on engagement. |

## 3. What seems to drive effectiveness

1. **Content and theory, not just the medium.** iCanQuit beat QuitGuide with the same delivery channel. The difference was the *therapeutic model* (acceptance vs avoidance) (Bricker et al., 2020).
2. **Engagement is the bottleneck.** Engagement with digital behaviour change interventions depends on the intervention (content and delivery), the context and the target behaviour, and engagement moderates effectiveness (Perski et al., 2017). Quit Sense lost half of its installers within a week (Naughton et al., 2024). The target is "*effective engagement*" (enough to work), not maximal engagement (Yardley et al., 2016).
3. **Most apps under-use evidence-based techniques.** Content analyses consistently find low adherence to treatment guidelines, and few apps promote medication or behavioural support (Abroms et al., 2013; Hoeppner et al., 2016; Haskins et al., 2017). In a French analysis of 14 popular apps, only 42% collected the information needed to advise on medication, and BCT counts ranged from 4 to 38 per app (Bustamante et al., 2021).
4. **Strong pilots often shrink.** QuitBot is the clearest example: a positive pilot followed by a null full trial. Plan for honest evaluation, and treat pilot effect sizes as optimistic.
5. **High-certainty "active ingredients" exist outside apps:** pharmacotherapy (varenicline, cytisine, combination NRT), e-cigarettes as a quit aid, financial incentives and behavioural support. An app that *connects* people to these (prompts, adherence support, CO-verified rewards) builds on strong evidence.

## 4. Implications for our project (evidence only — no direction chosen yet)

- A "progress tracker + badges" app is **not** differentiating and has **no evidence** of effect on its own.
- Any intelligent layer must improve **engagement quality** and **delivery of proven content**. Intelligence that cannot be linked to an active ingredient adds complexity without a mechanism.
- Because we can only do interviews and usability tests, our evaluation claims must stay at the level of **acceptability, usability, perceived usefulness and mechanism plausibility**, not efficacy. That makes **transparent reasoning** (why this, for whom, which assumption) more valuable: it is something we can show without an RCT.

## References for this file

- Abroms, L. C., Lee Westmaas, J., Bontemps-Jones, J., Ramani, R., & Mellerson, J. (2013). A content analysis of popular smartphone apps for smoking cessation. *American Journal of Preventive Medicine, 45*(6), 732–736. https://doi.org/10.1016/j.amepre.2013.07.008
- Bricker, J. B., Watson, N. L., Mull, K. E., Sullivan, B. M., & Heffner, J. L. (2020). Efficacy of smartphone applications for smoking cessation: A randomized clinical trial. *JAMA Internal Medicine, 180*(11), 1472–1480. https://doi.org/10.1001/jamainternmed.2020.4055
- Bricker, J. B., et al. (2024). Conversational chatbot for cigarette smoking cessation: Results from the 11-step user-centered design development process and randomized controlled trial. *JMIR mHealth and uHealth, 12*, e57318. https://mhealth.jmir.org/2024/1/e57318
- ClinicalTrials.gov NCT04308759. An innovative conversational agent (Quitbot) for smoking cessation — posted results. https://clinicaltrials.gov/study/NCT04308759
- Bustamante, L. A., et al. (2021). Behavior change techniques in popular mobile apps for smoking cessation in France: Content analysis. *JMIR mHealth and uHealth, 9*(5), e26082. https://mhealth.jmir.org/2021/5/e26082
- Chen, et al. (2024). Natural-language-processing chatbots for health behaviour change: systematic review of RCTs (search to July 2024) — as summarised in search results; verify full citation before reuse.
- Crane, D., Ubhi, H. K., Brown, J., & West, R. (2019). Relative effectiveness of a full versus reduced version of the 'Smoke Free' mobile application for smoking cessation: An exploratory randomised controlled trial. *F1000Research, 7*, 1524. https://f1000research.com/articles/7-1524
- CureApp (2020). Asia's first prescription digital therapeutic approved in Japan (press release). https://www.businesswire.com/news/home/20200826005812/en/
- Garrison, K. A., et al. (2020). Craving to Quit: A randomized controlled trial of smartphone app-based mindfulness training for smoking cessation. *Nicotine & Tobacco Research, 22*(3), 324–331. https://pmc.ncbi.nlm.nih.gov/articles/PMC7747804
- Graham, A. L., Papandonatos, G. D., Cha, S., et al. (2017). Improving adherence to smoking cessation treatment: Intervention effects in a web-based randomized trial. *Nicotine & Tobacco Research, 19*(3), 324–332 (BecomeAnEX factorial trial; NCT01544153). https://clinicaltrials.gov/study/NCT01544153 · Truth Initiative summary: https://truthinitiative.org/research-resources/quitting-smoking-vaping/how-online-social-relationships-help-smokers-quit
- Haskins, B. L., Lesperance, D., Gibbons, P., & Boudreaux, E. D. (2017). A systematic review of smartphone applications for smoking cessation. *Translational Behavioral Medicine, 7*(2), 292–299. https://doi.org/10.1007/s13142-017-0492-2
- Hébert, E. T., et al. (2020). An automated smartphone-based smoking cessation intervention (Smart-T2): pilot RCT. *Journal of Medical Internet Research*. https://doaj.org/article/e2de0b88db9645598fca72f477639026
- Hoeppner, B. B., et al. (2016). How smart are smartphone apps for smoking cessation? A content analysis. *Nicotine & Tobacco Research, 18*(5), 1025–1031. https://doi.org/10.1093/ntr/ntv117
- Lachance, et al. (2024). Interactive conversational agents for cigarette-smoking and vaping cessation: A mixed-methods systematic review. *Multimodal Technologies and Interaction, 8*(11), 101. https://www.mdpi.com/2414-4088/8/11/101
- Marler, J. D., et al. (2021). Outcomes of a comprehensive mobile smoking cessation program with NRT (Pivot). *Journal of Medical Internet Research, 23*(2), e25578. https://www.jmir.org/2021/2/e25578
- Marler, J. D., et al. (2022). Pivot vs QuitGuide remote pilot RCT. *JMIR mHealth and uHealth, 10*(11), e41658. https://mhealth.jmir.org/2022/11/e41658
- Masaki, K., et al. (2020). A randomized controlled trial of a smoking cessation smartphone application with a carbon monoxide checker. *npj Digital Medicine, 3*, 35. https://doi.org/10.1038/s41746-020-0243-5
- Naughton, F., et al. (2023). An automated online feasibility RCT of a just-in-time adaptive intervention for smoking cessation (Quit Sense). *Nicotine & Tobacco Research*. https://nottingham-repository.worktribe.com/output/19465753
- Naughton, F., et al. (2024). A smoking cessation smartphone app that delivers real-time 'context aware' behavioural support: the Quit Sense feasibility RCT. *Public Health Research*. https://doaj.org/article/05ed671e381740259ce4afd6bcfed4b4
- Notley, C., et al. (2019). Incentives for smoking cessation. *Cochrane Database of Systematic Reviews*, CD004307.pub6. https://ueaeprints.uea.ac.uk/id/eprint/71783/
- Perski, O., Blandford, A., West, R., & Michie, S. (2017). Conceptualising engagement with digital behaviour change interventions: A systematic review using principles from critical interpretive synthesis. *Translational Behavioral Medicine, 7*(2), 254–267. https://pmc.ncbi.nlm.nih.gov/articles/PMC5526809
- Perski, O., et al. (2022). Technology-mediated just-in-time adaptive interventions (JITAIs) to reduce harmful substance use: A systematic review. *Addiction, 117*(5), 1220–1241. https://doi.org/10.1111/add.15687
- Rajani, N. B., et al. (2023). Kwit gamified app: engagement and abstinence. *JMIR Serious Games, 11*, e39975. https://games.jmir.org/2023/1/e39975
- Webb, J., et al. (2020). The efficacy of a smartphone-based digital therapeutic (Quit Genius) vs very brief advice: RCT. *JMIR Mental Health, 7*(10), e22833. https://mental.jmir.org/2020/10/e22833
- Webb, J., et al. (2022). Long-term follow-up of Quit Genius RCT. *Nicotine & Tobacco Research*. https://doi.org/10.1093/ntr/ntac113
- Whittaker, R., McRobbie, H., Bullen, C., Rodgers, A., Gu, Y., & Dobson, R. (2019). Mobile phone text messaging and app-based interventions for smoking cessation. *Cochrane Database of Systematic Reviews*, CD006611.pub5. https://cochranelibrary.com/cdsr/doi/10.1002/14651858.CD006611.pub5/information · NIHR summary: https://evidence.nihr.ac.uk/alert/text-messaging-support-helps-smokers-quit-but-apps-not-yet-shown-to-work
- Yardley, L., et al. (2016). Understanding and promoting effective engagement with digital behavior change interventions. *American Journal of Preventive Medicine, 51*(5), 833–842. https://doi.org/10.1016/j.amepre.2016.06.015
