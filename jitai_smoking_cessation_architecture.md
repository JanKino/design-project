# Architecture Document: Modular JITAI Smoking Cessation Framework

## 1. Executive Summary
This document outlines the architecture for a **Just-In-Time Adaptive Intervention (JITAI)** smoking cessation application. Rather than a static app, this is a dynamic behavioral framework. It ingests contextual data (wearables, location, user inputs), processes it through a clinical psychological rules engine, and deploys modular interventions (chatbots, media routing, trackers) based on standard Behavior Change Techniques (BCTs).

## 2. The Theoretical Stack (The "Brain")
To prevent the app from randomly firing interventions that confuse or frustrate the user, the orchestration layer relies on a stacked psychological architecture. We do not switch between models; we use them in a specific hierarchy.

### A. The Macro-Layer: HAPA (Health Action Process Approach)
**Purpose:** Manages the user's overarching timeline and state.
**How it works:** HAPA recognizes that a user's psychological needs change fundamentally based on where they are in their quit journey. It divides the timeline into two distinct phases:
*   **Motivational Phase (Pre-Quit):** Interventions focus on building intention (e.g., showing health risks, calculating money wasted, building confidence).
*   **Volitional Phase (Post-Quit):** Interventions shift to execution and survival (e.g., deploying coping plans, trigger management, and streak tracking).
**In Practice:** HAPA acts as a global filter. If the user is in the Volitional Phase, the system locks out motivational BCTs (they already want to quit) and only allows action-oriented BCTs to be deployed.

### B. The Micro-Layer: COM-B (Capability, Opportunity, Motivation - Behavior)
**Purpose:** Analyzes the immediate, real-time context of a craving.
**How it works:** When a trigger is detected, COM-B diagnoses *why* the user is at risk of smoking at that exact moment:
*   **Capability:** Do they lack the mental bandwidth to resist? (e.g., high stress detected via HRV).
*   **Opportunity:** Is the environment triggering them? (e.g., GPS shows them at a favorite bar).
*   **Motivation:** Have they momentarily forgotten their "why"? 
**In Practice:** COM-B routes the user to the correct category of intervention based on the immediate barrier. If the barrier is Opportunity (location), it deploys a different BCT than if the barrier is Capability (stress).

## 3. The Execution Layer: BCTs (Behavior Change Techniques)
**Purpose:** The actual, deployable modules (the "active ingredients").
**How it works:** Instead of vague modules ("play a video"), every intervention in the app is tagged with a scientifically validated BCT (e.g., *BCT 1.2 Problem Solving*, *BCT 4.2 Information about Antecedents*).
**In Practice:** The BCTs are the variables. HAPA and COM-B decide *what kind* of help is needed, and the system pulls a specific BCT module from the database to deliver it (via a chatbot prompt, a Spotify playlist, or an Urge Surfing audio clip). 

## 4. System Workflow (Putting it into Practice)

1.  **Inputs (The Sensors):**
    *   *Passive:* Wearable data (Heart Rate/HRV for stress), Location (GPS for trigger zones), Calendar (Agenda for high-stress meetings).
    *   *Active:* User-logged cravings, self-reported mood, daily check-ins.
2.  **The Orchestration Engine (The Logic):**
    *   Determines HAPA State (e.g., *User is in Volitional Phase*).
    *   Analyzes COM-B Context (e.g., *HRV spike indicates a Capability barrier / Stress*).
    *   Selects the optimal BCT (e.g., *Deploy BCT 11.2: Reduce negative emotions*).
3.  **Outputs (The Modules):**
    *   The framework triggers the UI to deploy the selected BCT. For example, routing the user to a 2-minute "Urge Surfing" mindfulness audio track, or sending a chatbot message asking them to reframe their stress.

## 5. Phased Implementation Plan

*   **Phase 1: Deterministic Rules Engine.** Do not start with Machine Learning. Build a rigid "If/Then" rules engine based strictly on HAPA and COM-B. (e.g., *IF State=Volitional AND Trigger=Location, THEN Deploy BCT 1.2*).
*   **Phase 2: Zero-Party Data Onboarding.** Solve the "cold start" problem by having users explicitly map their triggers and preferred interventions during account creation.
*   **Phase 3: The "Slip" Protocol.** Implement HAPA's *Recovery Self-Efficacy*. If a user relapses, do not reset their "Days Quit" tracker to zero. Deploy a compassionate chatbot flow to analyze the slip and adjust their coping plan, keeping them engaged.
*   **Phase 4: Machine Learning Optimization.** Once you have enough user data flowing through the rigid HAPA/COM-B rules engine, deploy ML to optimize *which specific BCT module* (e.g., Video A vs. Audio B) works best for individual users under specific conditions.

## 6. Does this already exist?

The components of your idea exist across different sectors, but a fully unified, commercialized "operating system" that dynamically routes modular Behavior Change Techniques (BCTs) using wearable data and a multi-theory architecture (HAPA + COM-B) remains largely untapped in the mainstream market.Currently, the landscape is fragmented between highly advanced academic trials and commercially successful, but structurally rigid, digital therapeutics.

**What Already Exists in Academic and Clinical Trials (The Cutting Edge)**
Research institutions are actively testing Just-In-Time Adaptive Interventions (JITAIs) for smoking cessation, proving that the underlying logic of your framework is scientifically valid.
* **Quit Sense:** A heavily researched JITAI app that uses smartphone sensors and location data to predict cue-induced cravings in real-time, delivering in-situ support. It successfully maps environmental triggers to interventions but lacks the broad modularity of third-party media routing.
* **Sense2Stop:** A landmark research project that utilized wearable physiological data (heart rate, respiration) to detect stress and automatically trigger interventions before the user even consciously registered the craving.
* **iCoach:** A massive European Commission initiative that explicitly routed its interventions based on the Transtheoretical Model (Stages of Change), though it relied on manual user input rather than passive wearable data.