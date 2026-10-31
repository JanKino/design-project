# SOTA deep dive for direction S2: Miro board edition

Phase 1 follow-up, compiled 31 Oct 2026, after the team chose a direction close to **S2** ([ideas/05](../../ideas/05_shortlist_for_vote.md#s2--white-box-hapa-coach-an-orchestrator-that-knows-why-h1)).
This folder restructures and extends the phase-1 SOTA ([../README.md](../README.md)) into the six categories the Miro board needs, plus a bibliography.

## The direction this analysis serves

A **modular framework**, rooted in a **phase plan (HAPA)** and coded with a **BCT taxonomy/ontology**. Per phase, it **chooses between interchangeable interventions** (ideally every effective digital intervention found in apps or research) according to the person and the situation. A **chatbot** runs the intake questionnaire and reviews the user at moments relevant to phase transitions.

## Scope agreed with the team

| Decision | Choice |
|---|---|
| Output | Markdown analysis files (source of truth) + one CSV per category for import into Miro |
| Market scope | Global, with Belgium/EU as examples |
| Depth | ~10–20 prioritised cards per category, each with a "relevance for our project" line |
| Regulation | Filed under IPR & rights (EU MDR, GDPR, AI Act, platform rules) |

## File structure

```
sota/miro/
├── README.md                        ← you are here: scope, file map, summary, Miro how-to
├── 01_research_topics.md            ← research topics, key findings, relevance (R1–R21)
├── 02_competitive_analysis.md       ← apps, DTx, research systems; strong/weak; differentiation (C1–C18)
├── 03_ipr_and_rights.md             ← patents, copyright, licences, MDR, GDPR, AI Act (P1–P19)
├── 04_supporting_technology.md      ← reusable APIs, platforms, ontologies, learners, simulators (T1–T21)
├── 05_target_group_and_market.md    ← market size, needs, willingness to pay, segments (M1–M20)
├── 06_other_findings.md             ← findings that fit nowhere else (O1–O14)
├── references.md                    ← all references used in this folder
├── build_csv.py                     ← regenerates csv/ from the "## Miro cards" tables
└── csv/                             ← 01–06 card tables + 07_references.csv, for Miro
```

Card IDs (R, C, P, T, M, O + number) are stable. Use them on the board so cards can be traced back to the markdown and its sources. Gap IDs G1–G9 refer to [../07_gap_analysis.md](../07_gap_analysis.md).

## Summary in 8 points

1. **Content and fit drive effect, not the app format.** Apps as a category: RR 1.00. Specific ACT/CBT + medication programmes work. A framework that picks and sequences proven content is therefore well grounded (R1–R4).
2. **Theory and ontology layers exist but are unused at runtime.** HAPA, BCTTv1/BCTO, BCIO and TaTT are mature and openly licensed (CC BY 4.0), yet no smoking app uses them live (R5–R9, P7, T10–T11).
3. **Learning exists only for one flat decision.** Bandits and RL are deployed in HeartSteps, Oralytics, MiWaves and the TU Delft coach. Choosing *which intervention model per phase* is open (R12–R13, C17–C18; G1).
4. **No competitor adapts across intervention types and explains why.** Consumer apps are static; DTx use fixed programmes plus coaches; research systems learn but are not transparent (C1–C18). That top-right quadrant is our position.
5. **Chatbots help delivery, not proven outcomes.** QuitBot's RCT was null, and LLMs give unsafe health answers in red-team tests. The chatbot is the orchestrator's interface, with guard-rails (R16, T21, O8).
6. **Legal path: wellbeing prototype now, medical device later.** The intended purpose decides MDR status. GDPR Art. 9 explicit consent per data source fits our modular data design. AI Act Art. 50 requires the chatbot to disclose that it is an AI. Patent overlap is conceptual (IBM, eHealth RL) and low risk for a prototype (P1–P19).
7. **Large group, low consumer WTP, real payer routes.** 1.2 billion tobacco users; most quit attempts use no aid; most smokers are not ready to quit. Consumers pay a few dollars; insurers (DiGA ~€361), employers and councils pay more. In Belgium, partner with Tabakstop and tabacologists (M1–M18).
8. **Most components can be reused.** Health Connect/HealthKit, BCIO OWL, TaTT, published bandit designs, StepCountJITAI + COMPLAPSE for simulation, Rasa-style flows + LLM. What we build ourselves is the hierarchical selector, the content and the explanations (T1–T21).

## How to get the cards onto Miro

1. Regenerate the CSVs after editing any markdown: `python sota/miro/build_csv.py`.
2. Open a CSV in Google Sheets or Excel. In Excel with a Belgian locale, use *Data → From Text/CSV* and pick comma as the delimiter.
3. Select the rows and paste them onto the board. Miro turns pasted spreadsheet cells into sticky notes or a table, depending on your Miro version: check which you get. Use one frame per category and keep the ID column visible.
4. Put the full reference list (07_references.csv) in a separate frame, or link to this folder.

## Method and limitations

- Builds on the phase-1 structured narrative review ([../README.md](../README.md#method-and-limitations)). New searches were run in October 2026 for IPR, regulation, market, technology and recent competitors.
- **Market figures** come from commercial market-research summaries and differ widely; they are reported as ranges. **Patent** statuses are taken from Google Patents listings, and claims were not analysed. **Legal** items are orientation, not legal advice.
- Items marked "verify" (in the card or in [references.md](references.md)) have details taken from secondary summaries or abstracts.
