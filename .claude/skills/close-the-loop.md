# Skill: Close the Loop

## Trigger Condition
Activate at the end of every analysis, agent run, or significant output delivery.

## Purpose
Close the loop creates a feedback record, updates the system from what was learned, and ensures handoffs are clean. It's the habit that makes the system compound over time.

## Steps

### Step 1 — Produce a completion summary
At the end of every agent run or full analysis, output a brief completion summary:

```
COMPLETION SUMMARY
─────────────────────────────
Analysis: [analysis name]
Date: [date]
Data analyzed: [dataset names and date range]
Primary finding: [one sentence]
Key recommendations: [count and one-line summary]
Output files: [list of files produced with paths]
Known limitations: [any data quality issues or caveats]
Open questions: [anything that couldn't be resolved and needs follow-up]
```

### Step 2 — Check for system improvement opportunities
After delivering analysis, ask:
- Did any agent fail to produce good output? (needs revision)
- Did any skill fail to catch a problem it should have caught? (needs stricter trigger)
- Did the output require manual corrections? (corrections should become permanent rules)
- Did the user give feedback? (each piece of feedback should update the relevant file)

### Step 3 — Update agent/skill files if feedback was given
If the user gave any feedback — on chart design, narrative voice, analysis approach, slide structure — update the relevant agent or skill file immediately. Do not just fix the current output.

Log the update:
> "Updated `agents/chart-maker.md`: Added collision detection rule for dense chart annotations (feedback from Hawaii analysis, Feb 2026)"

### Step 4 — Write the open questions log
For anything that couldn't be resolved, write it in `/working/open-questions.md`:
- What's the question?
- Why couldn't it be resolved?
- What data or action would resolve it?
- Who needs to act?

### Step 5 — Clean up working files
After analysis is complete and outputs are delivered:
- Confirm all outputs are in `/outputs/`
- Archive working files to `/working/archive/[analysis-name]/`
- Clear `/working/` for the next analysis

## What Good Looks Like
Close the loop is done when:
- ✅ Completion summary written
- ✅ System improvement opportunities assessed
- ✅ Any feedback applied to agent/skill files
- ✅ Open questions logged
- ✅ Working files archived
