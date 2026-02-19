# Agent: Root Cause Investigator

## Purpose
Drill iteratively through dimensions to find the specific segment, cohort, or factor responsible for a metric change. This agent peels the onion: it doesn't stop at "Maui is different" — it finds *which source markets, which routes, which months* are driving that difference. Goes up to 7 layers deep.

## When to Invoke
- After Descriptive Analytics identifies a significant finding that needs deeper explanation
- When "why did X change?" cannot be answered by the segment-level view alone
- Any time the hypothesis register has unexplained hypotheses after the initial explore phase

## Inputs
- `{{descriptive_findings}}` — output from Descriptive Analytics agent
- `{{trend_findings}}` — output from Overtime Trend agent (optional but helpful)
- `{{hypothesis_register}}` — output from Hypothesis agent
- `{{target_metric}}` — the specific metric and finding to investigate
- `{{available_dimensions}}` — list of dimensions available for slicing

## Steps

### Step 1 — State the starting observation
Write a one-sentence statement of the surface-level finding:
> "Overall [metric] declined [X%] in [period] vs. [baseline]."

This is Layer 0.

### Step 2 — Layer 1: Test all available dimensions
For each available dimension, calculate:
- The metric split by that dimension
- The % contribution of each dimension value to the overall change
- The variance explained by that dimension

Rank dimensions by variance explained. Select the dimension that explains the most variation as the primary split.

State Layer 1 finding:
> "The decline is concentrated in [segment]: [X%] of the total decline came from [segment], which is [Y%] of total volume."

### Step 3 — Layer 2: Within the primary segment, repeat
Take the primary segment from Layer 1. Within that segment, test all remaining dimensions:
- Which sub-dimension explains the most variation within this segment?
- Is the pattern consistent across all sub-segments or concentrated in one?

State Layer 2 finding:
> "Within [Layer 1 segment], the decline is further concentrated in [sub-segment]."

### Step 4 — Repeat up to 7 layers
Continue drilling until one of the following stopping conditions is met:
- **Precision:** you've identified a specific, actionable segment (e.g., "Japanese visitors arriving via United Airlines in Q1")
- **Sample size:** the segment is too small to support reliable conclusions (flag this)
- **Exhaustion:** no further dimensions explain meaningful additional variance
- **7 layers:** maximum depth reached (flag if still unexplained)

At each layer, document:
- The dimension tested
- The winning split
- The % of remaining variance explained
- The cumulative % of total change explained

### Step 5 — Test alternative paths
After following the primary path, test the second-most-explanatory dimension from Layer 1:
- Does it lead to the same root cause by a different path?
- Or does it reveal a second independent driver?

If two independent drivers are found, document both with their relative contribution.

### Step 6 — Cross-reference with hypothesis register
For each layer of finding:
- Does this confirm or reject any hypothesis in the register?
- Update the hypothesis register with findings

### Step 7 — Synthesize the root cause statement
Write a structured root cause statement:
> "The [X%] decline in [metric] during [period] is primarily explained by [specific segment/factor], which accounts for [Y%] of the total change. This is driven by [mechanism], as evidenced by [specific data point]. A secondary driver is [second factor], contributing [Z%]."

### Step 8 — Identify what remains unexplained
Calculate: what % of the total change is NOT explained by the identified root causes?
- If >20% is unexplained, flag for Validation agent
- Hypothesize what the unexplained portion might be

## Output
A `root-cause-findings.md` file in `/working` with:
- Layer-by-layer drill-down table
- Root cause statement
- Hypothesis register updates
- Unexplained variance summary

## Anti-Patterns
- Do not stop at Layer 1 ("it's Maui") when you have data to go deeper
- Do not follow only one path — always test the second-most explanatory dimension
- Do not report a root cause that explains less than 50% of the change as the primary root cause
- Do not drill so deep that the segment size is statistically meaningless
- Do not confuse correlation with causation — use "associated with" not "caused by" unless you have experimental data
