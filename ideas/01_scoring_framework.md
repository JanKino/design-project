# 01 — Scoring framework: how ideas are judged

> **Question answered here:** Against which criteria, weights and project constraints are the candidate ideas scored, and how robust is the ranking to those choices?

## 1. Project constraints the scores take into account

| Constraint | Value (agreed 31 Oct 2026) | Effect on scoring |
|---|---|---|
| Team | 5–6 CS students, a bit more than one semester | Large builds are possible |
| Development | Agentic coding: software is cheap to produce | Build size counts little. **People-time counts a lot**: recruiting, ethics, studies with smokers |
| Evaluation | Interviews and usability tests. **Small, short user studies with smokers are possible**. Large data collection is not | An idea scores well on feasibility if its core claim can be shown with ~10–20 users over days to a couple of weeks, or on public data / simulation |
| End user | Smokers first. Researchers second | "Value for smokers" is a top criterion |
| Explainability | Required (challenge #6) | Ideas that keep the reasoning *inside* the system score higher on "challenge fit" |
| Data | Modular: EMA, phone, wearable, each optional | Ideas that need a fixed sensor kit lose points on feasibility and risk |

## 2. Criteria and weights

Scale per criterion: 1 (poor) – 5 (excellent). The final score is the weighted mean, so it also lands on 1–5.

| Code | Criterion | Weight | What a 5 means | What a 1 means |
|---|---|---|---|---|
| **N** | Novelty vs SOTA | **3** | Fills an empty cell of [sota/07](../sota/07_gap_analysis.md) (G1–G9) with no close precedent in smoking | Already done in apps or research prototypes |
| **V** | Value for smokers | **3** | Addresses a real, frequent need with evidence-based content; likely to be valued in interviews | Mostly interesting to researchers or engineers |
| **F** | Feasible + demonstrable | **3** | Core claim can be shown in a short, small user study, or convincingly on public data / simulation | Only an RCT or large field deployment can show it works |
| C | Challenge #6 fit & expert appeal | 1.5 | Program theory machine-readable inside the system, testable claims, attractive to Ghent Health Psychology Lab / Tabakstop | Black box, nothing for psychologists |
| E | Evidence behind the delivered content | 1.5 | Active ingredients with SR/MA or RCT evidence for smoking | Content without evidence |
| X | Extensibility | 1 | Other modules (JITAI, buddy, medication…) plug in naturally | Dead end |
| R | Risk profile (ethics, privacy, safety) | 1 | Low data and safety risk | Sensitive passive sensing, unsupervised LLM, money handling |

The three criteria the user selected (N, V, F) carry 9 of the 14 weight points. The others still count.

## 3. Sensitivity analysis

The same raw scores ([04](04_hybrids_and_comparison.md#2-score-matrix)) under five weightings:

| Weighting | N | V | F | C | E | X | R | Top 3 |
|---|---|---|---|---|---|---|---|---|
| **Main** (used in this folder) | 3 | 3 | 3 | 1.5 | 1.5 | 1 | 1 | I6 4.32 · **H2 4.32** · **H1 4.07** |
| Equal | 1 | 1 | 1 | 1 | 1 | 1 | 1 | I6 4.29 · H2 4.29 · H1 4.14 |
| Novelty-heavy | 5 | 3 | 3 | 1.5 | 1.5 | 1 | 1 | H2 4.41 · I6 4.28 · H1 4.19 |
| Feasibility-heavy | 3 | 3 | 5 | 1.5 | 1.5 | 1 | 1 | I6 4.41 · H2 4.28 · H1 3.94 |
| Smoker-first | 2 | 5 | 3 | 1 | 2 | 1 | 1.5 | I6 4.26 · H2 4.19 · H1 3.94 |

**H4 (added later, [04](04_hybrids_and_comparison.md#h4--hapa-scaffolded-coach-with-a-learning-jitai-i3-rule-based--i15--i2i1-light-i4)) under the same weightings:** Main 4.07 (tied with H1) · Equal 4.14 (tied with H1) · Novelty-heavy 4.06 (below H1 4.19) · Feasibility-heavy 4.06 (above H1 3.94, enters the top 3) · Smoker-first 4.06 (above H1 3.94, enters the top 3). H4 has no low scores, so its total barely moves with the weights. H1 gains when novelty counts more, H4 when feasibility or value for smokers counts more.

**Reading:** the top of the ranking does not depend on the weighting. The "personal experiments" family (I6 / H2) and the HAPA-plus-claims hybrid (H1) lead under every weighting. Pure deep JITAI (I1) is last under every weighting. Positions 4–8 shift a little; the third shortlist slot ([05](05_shortlist_for_vote.md)) goes to H3 because it is the strongest option for direction A and adds variety to the vote, not because of a fixed score cut-off.

## 4. Caveats

- Scores are **our judgement**, grounded in the sources cited per idea, not a measurement. Disagreeing with a score is a good way to start the team discussion. The scoring script is trivial to rerun with other numbers.
- I6 and H2 are the same family (H2 = I6 + the claim layer + a phase shell). They are not two independent winners.
- Novelty is judged against what we found ([sota/](../sota/README.md) plus the targeted searches for this phase). A missed paper could lower a novelty score.
