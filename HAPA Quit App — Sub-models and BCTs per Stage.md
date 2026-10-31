# HAPA Quit App — Sub-models and BCTs per Stage

Oct 30, 2026 · @Jan

A basic, buildable design: HAPA sets the stages of the quit journey, and each stage uses one or two well-established sub-models whose techniques are delivered as concrete app features, coded with the BCT Taxonomy v1 (BCTTv1).

## At a glance

&#91;embedded content: four HAPA stages · sub-models per stage\]

HAPA's motivational phase covers only Stage 1; preparing to quit already belongs to the volitional phase. A single slip stays in Stage 4; a return to regular smoking goes back to Stage 2 with all plans kept.

## Stage 1 — Pre-intender (not yet decided to quit)

**Goal of the stage:** help the user form a genuine intention to quit, without pressure.

**HAPA targets:** risk perception, positive outcome expectancies (what quitting gives them), and task self-efficacy ("I could do this").

### Candidate sub-models

- **Motivational Interviewing (MI) principles.** Ask rather than tell; elicit the user's own reasons. Pressure triggers resistance in ambivalent smokers.
- **Extended Parallel Process Model (EPPM).** Health-risk messages only work when paired with a feeling of efficacy. Fear without a "you can do it" message leads to avoidance.
- **Self-affirmation theory.** Letting users first affirm a value they care about reduces defensiveness to health-risk information.
- **Decisional balance.** Weighing pros and cons of smoking vs. quitting; the balance typically tips before someone decides.

### BCTs and app features

| BCT (BCTTv1) | App feature | Sub-model |
| --- | --- | --- |
| 9.2 Pros and cons | Short interactive decisional-balance exercise; the user's own reasons are saved and reused later | Decisional balance, MI |
| 5.1 Information about health consequences | Personalised health facts based on their cigarettes per day, always followed by a recovery timeline ("20 minutes after your last cigarette…") | EPPM |
| 2.7 Feedback on outcomes of behaviour | Money calculator: spent per month and per year, and what that buys | Decisional balance |
| 9.3 Comparative imagining of future outcomes | "Picture yourself in a year, smoke-free vs. still smoking" guided prompt | MI |
| 13.4 Valued self-identity | Before risk content, the user picks a value that matters to them (family, sport, independence) | Self-affirmation |
| 15.1 Verbal persuasion about capability | Messages stressing that most ex-smokers needed several attempts, and that support and medication raise the odds | EPPM, Social cognitive theory |
| 6.1 Demonstration of the behaviour | Short stories or videos of ex-smokers similar to the user | Social cognitive theory (vicarious experience) |

**Moves on when:** the user says they want to quit, or sets a quit date.

## Stage 2 — Intender (decided, preparing to quit)

**Goal of the stage:** turn the intention into a concrete, prepared quit attempt.

**HAPA targets:** action planning (when, where, how), coping planning (what if…), and action self-efficacy.

### Candidate sub-models

- **Implementation intentions** (Gollwitzer). "If situation X, then I do Y" plans make responses automatic in the moment. This is the most directly app-friendly sub-model.
- **Goal-setting theory** (Locke & Latham). Specific, committed goals, here a fixed quit date, outperform vague ones.
- **Social cognitive theory** (Bandura). Builds self-efficacy through small successes, role models and encouragement.
- **Social support.** Enlisting a buddy or household members makes the attempt public and gives practical help.

### BCTs and app features

| BCT (BCTTv1) | App feature | Sub-model |
| --- | --- | --- |
| 1.1 Goal setting (behaviour) | Pick a quit date within the next 2 weeks; countdown on the home screen | Goal-setting theory |
| 1.9 Commitment | The user writes and signs a short personal quit statement | Goal-setting theory |
| 2.3 Self-monitoring of behaviour | Log each cigarette for a few days before quitting: time, place, mood, company | Self-regulation |
| 4.2 Information about antecedents | App summarises the log into the user's top 3 triggers | Implementation intentions |
| 1.4 Action planning | Quit-day plan: what to do on waking, at breaks, after meals | Implementation intentions |
| 1.2 Problem solving (coping planning) | For each top trigger, the user picks or writes an "if–then" plan | Implementation intentions |
| 12.1 Restructuring the physical environment | Checklist: remove cigarettes, lighters and ashtrays before quit day | — |
| 11.1 Pharmacological support | Information on NRT, varenicline and cytisine, with a prompt to see a GP or pharmacist | — |
| 3.2 Social support (practical) | Invite a quit buddy, or prepare a message telling friends | Social support |
| 4.4 Behavioural experiments | Optional practice: delay the first cigarette by 30 minutes, or skip one routine cigarette | Social cognitive theory (mastery) |

**Moves on when:** the quit date arrives and the user confirms they've stopped.

## Stage 3 — Actor (first \~4 weeks smoke-free)

**Goal of the stage:** get through cravings and withdrawal without smoking.

**HAPA targets:** maintenance self-efficacy ("I can resist even when it's hard") and action control (keeping track of the goal and acting on the plans).

### Candidate sub-models

- **Relapse Prevention model** (Marlatt & Gordon). Identify high-risk situations and rehearse coping responses for them.
- **Urge surfing / mindfulness (ACT-based).** Notice the craving as a passing wave instead of fighting or obeying it. Cravings usually peak and fade within minutes.
- **Operant learning.** Reward smoke-free progress so that not smoking becomes reinforcing.
- **Self-regulation / control theory.** Regular feedback on progress against the goal keeps effort going.

### BCTs and app features

| BCT (BCTTv1) | App feature | Sub-model |
| --- | --- | --- |
| 2.3 Self-monitoring of behaviour | Daily one-tap check-in: smoke-free today? Craving level 0–10? | Self-regulation |
| 2.2 Feedback on behaviour | Smoke-free days, cigarettes not smoked, money saved | Self-regulation, Operant learning |
| 11.2 Reduce negative emotions | "Craving SOS" button: 2-minute urge-surfing audio or breathing exercise | Urge surfing |
| 8.2 Behaviour substitution | Quick list of alternatives: walk, drink water, chew gum, text the buddy | Relapse prevention |
| 1.2 Problem solving | Reminds the user of their own "if–then" plan for the trigger they log | Relapse prevention, Implementation intentions |
| 12.3 Avoidance / reducing exposure to cues | Tips for the first weeks: change routines linked to smoking (coffee spot, break route) | Relapse prevention |
| 4.1 Instruction on how to perform the behaviour | Explainer on withdrawal symptoms, how long they last and how to handle them | Social cognitive theory |
| 10.3 Non-specific reward / 10.9 Self-reward | Milestone badges (1 day, 3 days, 1 week, 1 month) and a prompt to spend saved money on a treat | Operant learning |
| 15.4 Self-talk | User records a short message to themselves, played back during cravings | Social cognitive theory |
| 3.1 Social support (unspecified) | One-tap "I'm struggling" message to the quit buddy | Social support |

**Moves on when:** about 4 weeks smoke-free. **Falls back** if a lapse becomes a return to regular smoking (see Stage 4 recovery).

## Stage 4 — Maintainer, and recovery after a lapse

**Goal of the stage:** keep the user smoke-free long term, and turn any lapse into a learning moment instead of a full relapse.

**HAPA targets:** recovery self-efficacy ("I can get back on track after a slip") and a stable non-smoker identity.

### Candidate sub-models

- **PRIME theory / identity** (West). Long-term change sticks when "I'm a non-smoker" becomes part of who the person is, not just a rule they follow.
- **Abstinence violation effect** (from Relapse Prevention). After one cigarette, the thought "I've failed, so I may as well smoke" drives relapse. Reframing the slip breaks this chain.
- **Habit formation.** New routines that replaced smoking need repetition in stable contexts to become automatic.

### BCTs and app features

| BCT (BCTTv1) | App feature | Sub-model |
| --- | --- | --- |
| 13.5 Identity associated with changed behaviour | Reflection prompts: "What does being a non-smoker mean to you?"; language in the app shifts from "quitting" to "non-smoker" | PRIME / identity |
| 15.3 Focus on past success | After a lapse, show the user how many smoke-free days they achieved and which plans worked | Recovery self-efficacy |
| 13.2 Framing / reframing | Slip flow: "One cigarette is a lapse, not a relapse"; no reset of total smoke-free days | Abstinence violation effect |
| 1.2 Problem solving | Slip analysis: what happened, which trigger, which new "if–then" plan | Relapse prevention |
| 1.5 Review behaviour goal(s) | Monthly check-in to update plans for new risk situations (holidays, parties, stress at work) | Self-regulation |
| 2.2 Feedback on behaviour / 2.7 Feedback on outcomes | Long-term stats: money saved, health milestones reached | Operant learning |
| 10.4 Social reward | Share milestones with the buddy or friends, if the user wants | Operant learning, Social support |
| 8.3 Habit formation | Reinforce the substitute routines from Stage 3 ("Your post-lunch walk: 30 days in a row") | Habit formation |

**Recovery path:** a single lapse keeps the user in this stage and runs the slip flow. A return to regular smoking moves them back to Stage 2 to set a new quit date, keeping all their saved reasons, triggers and plans.

## Staging: placing a user in a stage

Three onboarding questions are enough to place a user, and the same questions can be repeated in a weekly check-in.

1. **Do you currently smoke?**
   - No, I've stopped → ask how long. Under \~4 weeks → **Stage 3**; longer → **Stage 4**.
   - Yes → question 2.
2. **Do you want to quit smoking?**
   - Not really / not sure → **Stage 1**.
   - Yes → question 3.
3. **Have you chosen a quit date?**
   - Yes, or I'd like to set one now → **Stage 2**.
   - Not yet → **Stage 2**, starting with the quit-date step.

The user can always switch stage manually ("I'm ready to set a quit date"). A stage should never block access to help: a Stage 1 user who taps the Craving SOS button still gets it.

## A basic first version

Ten BCTs, roughly two or three per stage, cover the core of the journey and can be built with simple screens, a daily check-in and local notifications. No wearables or sensing are needed.

| Stage | BCTs to build first | Core feature |
| --- | --- | --- |
| 1 Pre-intender | 9.2 Pros and cons; 2.7 Feedback on outcomes | Reasons exercise + money calculator |
| 2 Intender | 1.1 Goal setting; 2.3 Self-monitoring; 1.2 Problem solving (if–then plans); 11.1 Pharmacological support | Quit date, cigarette log, trigger plans, medication info |
| 3 Actor | 11.2 Reduce negative emotions; 2.2 Feedback on behaviour; 10.3 Non-specific reward | Craving SOS button, progress stats, milestone badges |
| 4 Maintainer / recovery | 13.2 Framing / reframing (+ 1.2 reused) | Slip flow that updates the user's plans |

The if–then plans made in Stage 2 are the thread that ties the app together: they are written in Stage 2, shown during cravings in Stage 3, and revised after a slip in Stage 4. Further sub-models and BCTs from the tables above can be added once this core is tested with users.
