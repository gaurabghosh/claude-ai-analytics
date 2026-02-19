# Skill: Run Pipeline

## Trigger Condition
Activate when asked to run a full end-to-end analysis. Invoked explicitly via prompts like:
- "Analyze this dataset"
- "Run the full pipeline on [data]"
- "Give me a full analysis and deck"
- "Go analyze this"

## Purpose
Orchestrate the full 6-phase pipeline from raw data to finished deck. This skill is the conductor — it doesn't do the work itself, it sequences the agents and manages the checkpoints.

## Pipeline Sequence

```
INPUT: Dataset(s) + analytical question (or just dataset)

PHASE 1: FRAME
  ├─ Question Framing agent → /working/question-framing.md
  └─ Hypothesis agent → /working/hypothesis-register.md

PHASE 2: EXPLORE (parallelize where possible)
  ├─ Data Explorer agent → /working/data-profile.md
  ├─ Descriptive Analytics agent → /working/descriptive-analytics-findings.md
  ├─ Overtime Trend agent → /working/trend-findings.md
  ├─ Root Cause Investigator agent → /working/root-cause-findings.md
  ├─ Opportunity Sizer agent → /working/opportunity-sizing.md
  └─ [Experiment Designer agent → /working/experiment-design.md — only if applicable]

  [CHECKPOINT 1: All explore outputs present? → Proceed / Wait]

PHASE 3: VALIDATE
  └─ Validation agent → /working/validation-report.md

  [CHECKPOINT 2: All headline findings validated? → Proceed / Block]

PHASE 4: STORY
  ├─ Story Architect agent → /working/storyboard.md
  ├─ Narrative Coherence Reviewer agent → /working/narrative-coherence-review.md
  └─ Storytelling agent → /working/narrative-copy.md

  [CHECKPOINT 3: Narrative coherence passed? → Proceed / Revise]

PHASE 5: CHARTS
  ├─ Chart Maker agent → /outputs/charts/*.png + /working/chart-manifest.md
  └─ Visual Design Critic agent → /working/visual-design-review.md

  [CHECKPOINT 4: All charts passed design review? → Proceed / Revise]

PHASE 6: DELIVER
  ├─ Deck Creator agent → /outputs/[analysis-name]-deck.marp.md
  ├─ Render PDF → /outputs/[analysis-name]-deck.pdf
  └─ Close the Loop skill → completion summary

OUTPUT: Finished deck PDF + Marp source + all working files
```

## Checkpoint Behavior
At each checkpoint, before proceeding:
1. Confirm all required inputs for the next phase are present
2. If any inputs are missing: pause, state what's missing, wait for resolution
3. If any checkpoint gate failed (validation failures, coherence failures, design failures): pause, explain the failure, and run the necessary revision before proceeding
4. Do not silently skip a failed checkpoint

## Progress Reporting
At the start of each phase, briefly report:
> "▶ Starting Phase 2: Explore. Running Data Explorer, Descriptive Analytics, Overtime Trend, Root Cause Investigator, and Opportunity Sizer in parallel."

At checkpoint:
> "✅ Checkpoint 1: All explore agents complete. Proceeding to Phase 3: Validate."
OR
> "⚠️ Checkpoint 1: Validation agent output missing. Waiting on root-cause-findings.md before proceeding."

## Time Estimates (approximate)
- Phase 1 (Frame): 2–5 minutes
- Phase 2 (Explore): 5–10 minutes
- Phase 3 (Validate): 3–5 minutes
- Phase 4 (Story): 3–5 minutes
- Phase 5 (Charts): 5–10 minutes
- Phase 6 (Deliver): 2–5 minutes
- **Total: 20–40 minutes for a full analysis**
