### User note

In this folder, i would like to perform a SOTA analysis for our project in building a smoking cessation app. The idea would be, that in most smoking apps, different techniques are used:
* most of them are progress trackers, tracking saved money
* Some of them provide a gameification mechanism
* Some research aims on prediction phases of high need for a cigarette, and sending a notification for eg. a chatbot conversation or something else.
    * This method does run into some difficulties: it is hard to know when to send the right notifications, in which context, and which notifications to send.

What we want to do is build an intelligent app or framework that combines such mechanisms with intelligent learning.
It would get as input, the data the user provides (or chooses to provide). Like location, wearable data. Etc. Based on this information we would then provide adaptive interventions. We would initialize the use of the app with an initial conversation/questionaire. And learn about the user throughout the use of the app what might work best for them.

For example, if an intervention is: sending notification at a time of craving. We could learn to send notifications about different topics. Or when to or not to send notifications. But we could also employ different Behaviour Change Techniques, like building a stopping plan, using a buddy mechanism, etc. The question now is, where to directly steer our project towards.
* If we do focus on sending the right notification at the right time. This becomes a specific method of JITAI. The question is, if we use such a deep dive model. If we will still be able (and want) to add other mechanisms of intervention. And if this is realistic, and different enough from what already exists.
    * In this case we could do something new by: Learning to steer the behaviour of the smoker in adaptive, and subconscious ways. Like initiating other activities. Providing distraction etc. To prevent the user from reaching the point of wanting a cigarette. Or to help them overcome such weak moments.   
* I also looked at the possibility, to make our project more broad. Where the main project would be to build a framework. Where we use for example the HAPA model, to guide the broad behaviour change model. Then we would use, for different phases, different program theories/models to change a certain behaviour (determinant). And for each of these program theories, we could interchange different digital interventions in our app. Containing the Behaviour Change Techniques. Our model would then learn, based on the person to:
    * choose between these intervention models for each phase
    * Possibly learn to choose between conceptually equivalent building blocks for these intervention models
    * And then even further, if we have the possibility, and if we do not already have a model that does this. Improve one intervention model, like a type of JITAI. By eg. learning which notifications to send.
    For this path, two possible AI assisted sketch ideas for the project are listed in this folder.
    * The above described method of the adaptive notifications could still be added to this framework. But only as a separate sub modele. And this might not receive full focus, or be neglected, due to time constraints.  

We are computer scientists. This is a software project (we could call in help from experts). But likely the help from psychologists will be easiest if they have a use in this project.
The initial setup of the project challenge was presented in the dutch file "D:\school_grote_files\1e_master\design project\samenvatting Why_Should_This_Work_studenten_NL.md" But we are not constrained to this challenge. The main stakeholders need not be researchers specifically. We have the idea of shifting our focus more towards building a usable app for the smokers, instead of building a research framework.

We already have 2 files, where I, with the use of AI. Tried to think out a direction for the HAPA based construction of our idea.

What we need to do: step by step.
**Perform a proper SOTA analysis:** 
* Which methods exist in the field(s) that we are thinking about. What is already implemented and available in possible apps.
* And definitely: what is not yet done. Where can we improve, and be new in the field.
* What research could be used (that might not yet be implemented) for our use cases.

**Based on this**
* Where should we steer our project. What part of the model should we focus on.
* Which ideas to go towards have I not tought about.
* Build a list of possible ideas to go towards, critiquing each. Noting strong and weak points. And finally concluding what the best choice is.

**Once we have a strong idea for the project**
* Find literature and models to refine the idea: eg. do we use the HAPA model, or another. Which behaviour change methods/models could we use to interchange inside HAPA phases
* Which models exist to link the app features to BCTs and to 

The SOTA search should always contain proper sources for its information and references to this.
The agent should contain nice insightfull structure. Create different files for different important parts in this search and analysis. And document the file structure.


**Grill the user before proceding** Before going to work. Make sure the plan is clear. And ask the user if needed

### AGent notes

*Stable orientation for agents and team members. The changing state (phase status, decisions, open questions, session log) lives in [PROGRESS.md](PROGRESS.md). Read that first, and update it at the end of every work session.*

#### Project in one paragraph
UGent master Design Project (2026–27), loosely based on challenge 6 *"Why Should This Work?"* (Crombez & Tack, Ghent Health Psychology Lab). We are a CS team designing an **adaptive smoking-cessation app**: it combines established Behaviour Change Techniques (BCTs) with per-user learning from data the user chooses to share (self-report, phone sensors, wearables). We focus on a **usable app for smokers**, not a research framework. The challenge's demand that the app be **explainable** ("why was this chosen?", program theory inside the system) is kept as a design principle.

#### Phases (status in [PROGRESS.md](PROGRESS.md))
1. **SOTA analysis**: what exists, what is missing, what research is not yet implemented. → `sota/`
2. **Ideas and direction**: a critiqued list of project directions with strong and weak points, ending in a recommendation. → `ideas/` (to create)
3. **Refinement**: theory backbone (HAPA or an alternative), sub-models per phase, BCT ↔ feature ↔ mechanism-of-action mapping, learning and explanation design. → `design/` (to create)
4. Later: stakeholder interviews, prototype, usability tests.

#### Agreed scope decisions (do not re-litigate without the user)
| Topic | Decision |
|---|---|
| Stakeholder focus | Smokers as end users. Researchers are secondary |
| Explainability | Required. Logical, science-based reasoning is preferred over pure statistics. BCT ontologies (BCTTv1, BCIO) may be used but are not required |
| Data sources | Self-report/EMA, phone sensors, consumer wearables. **Modular**: the app must also work with only some of them |
| Evaluation during the project | Interviews and usability tests, plus **small, short user studies with smokers** if feasible (updated 31 Oct 2026). No large data collection, so slow learning components must be shown on public datasets or in simulation |
| Capacity | 5–6 people, a bit more than one semester, using agentic coding. Software is cheap; people-time for prototypes and user tests is the bottleneck |
| Chosen direction (31 Oct 2026) | Close to **S2**: modular framework on a BCT taxonomy, rooted in a HAPA phase plan, choosing between phase-dependent interventions; chatbot for intake and phase-transition reviews |
| Candidate directions | Phase 2 shortlist for the team vote: S1 Quit Lab (personal experiments + claim layer), S2 White-box HAPA coach (direction B + claim layer), S3 One step ahead (anticipatory steering, new form of direction A), S4 HAPA rule scaffold + learning JITAI linked to planner/progress (added after discussion). See [ideas/05](ideas/05_shortlist_for_vote.md) |

#### File structure
```
design project/
├── claude.md                     ← user brief + these agent notes (stable)
├── PROGRESS.md                   ← living tracker: phase checklist, decision log, open questions, session log
├── samenvatting Why_Should_This_Work_studenten_NL.md   ← original challenge background (Dutch)
├── Challenges 26-27.pdf          ← all course challenges. Ours is #6 (p. 12)
├── Design dash and group formation reflection report.pdf  ← course reflection, not project content
├── HAPA Quit App — Sub-models and BCTs per Stage.md     ← early AI-assisted sketch of direction B (HAPA stages → sub-models → BCTs)
├── jitai_smoking_cessation_architecture.md            ← early AI-assisted sketch (HAPA + COM-B JITAI stack). Partly corrected in sota/07 §5
├── sota/                         ← phase 1 (done, 31 Oct 2026)
│   ├── README.md                 ← scope, file map, 10-point summary, method. START HERE
│   ├── 01_evidence_base.md … 06_theory_ontologies.md   ← topic files
│   ├── 07_gap_analysis.md        ← done/not-done matrix, gaps G1–G9, ready-to-implement research
│   ├── references.md             ← consolidated bibliography
│   └── miro/                     ← S2 deep dive in Miro categories (31 Oct 2026). README = start
│       ├── 01_research_topics.md … 06_other_findings.md  ← card tables (IDs R, C, P, T, M, O)
│       ├── references.md         ← bibliography of the deep dive
│       ├── build_csv.py          ← regenerates csv/ from the "## Miro cards" tables
│       └── csv/                  ← CSV per category + 07_references.csv for Miro import
├── ideas/                        ← phase 2 (done, 31 Oct 2026; awaiting team vote)
│   ├── README.md                 ← scope, file map, summary, ID scheme. START HERE
│   ├── 01_scoring_framework.md   ← criteria, weights, sensitivity analysis
│   ├── 02_core_directions.md     ← I1–I8 candidate cores, critiqued and scored
│   ├── 03_modules_and_enablers.md← I9–I18 add-ons and enablers, priority tiers
│   ├── 04_hybrids_and_comparison.md ← H1–H4, score matrix, gap coverage
│   ├── 05_shortlist_for_vote.md  ← S1–S4 project sketches + vote questions
│   └── references.md             ← phase-2 bibliography
└── design/                       ← phase 3 (planned)
```
Keep this tree current when adding folders or key files. Each phase folder has its own `README.md` with a file map.

#### Conventions
- **Sources are mandatory.** Every factual claim gets an inline citation (Author, Year) plus an entry in the folder's `references.md`. Tag evidence strength: `[SR/MA]`, `[RCT]`, `[pilot]`, `[obs]`, `[industry]`, `[registry]`, `[vendor]`. Mark unverified bibliographic details with "verify".
- **Gap IDs are shared vocabulary.** Refer to gaps as G1–G9 from [sota/07_gap_analysis.md](sota/07_gap_analysis.md). Ideas use the stable IDs I1–I18, hybrids H1–H4, shortlist S1–S4 ([ideas/README](ideas/README.md#id-scheme)).
- Each analysis file opens with a `> Question answered here:` line. Files are numbered in reading order.
- Write in English. Source material may be Dutch.
- The early sketches in the root are inputs. Do not edit them; note corrections in the analysis files instead.

#### Working rules for agents
- **Grill before working**: confirm the scope of each phase with the user before starting it (see user note).
- Stop at the end of each phase for user review. Do not run into the next phase uninvited.
- At the end of a session: update [PROGRESS.md](PROGRESS.md) (checklist, decisions, open questions, log line) and the file tree above if it changed.
- Commit only when the user asks.