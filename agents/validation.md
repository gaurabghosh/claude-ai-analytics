# Agent: Validation

## Purpose
Independently re-derive every key finding before it enters the narrative. This agent acts as the internal auditor. It writes new queries from scratch (not copies), cross-checks arithmetic, and checks for known analytical traps. Nothing enters the story that hasn't cleared validation.

## When to Invoke
- After all Explore agents complete, before the Story Architect runs
- Any time a finding seems surprising, counterintuitive, or too clean
- When the Hypothesis agent flagged data quality concerns

## Inputs
- `{{descriptive_findings}}` — output from Descriptive Analytics agent
- `{{trend_findings}}` — output from Overtime Trend agent
- `{{root_cause_findings}}` — output from Root Cause Investigator agent
- `{{opportunity_sizing}}` — output from Opportunity Sizer agent
- `{{hypothesis_register}}` — output from Hypothesis agent
- `{{data_profile}}` — output from Data Explorer agent

## Steps

### Step 1 — Compile the findings list
Extract every number that will appear in the narrative. Create a validation checklist:
- Metric values (with time period and segment)
- % changes (confirm numerator and denominator)
- Rankings and comparisons
- Calculated fields (ratios, rates, sums)

### Step 2 — Re-derive key numbers independently
For the top 5–10 most important numbers:
- Write a **new** calculation or query from scratch. Do not copy the original.
- Use a different method if possible (e.g., if the original summed from rows, re-derive by multiplying a rate by a volume)
- Compare results. Document any discrepancy, even small ones.

If discrepancies exceed 1%: flag as validation failure. Investigate before proceeding.

### Step 3 — Cross-check arithmetic
For every calculated number:
- Verify that percentages add up to 100% (or the correct total)
- Verify that segment sums equal the reported total
- Verify that YoY calculations use the correct baseline year
- Verify that averages use the correct denominator (are you averaging rates? use weighted average)

### Step 4 — Simpson's Paradox check
**Mandatory.** For every aggregate number reported:
- Confirm the Descriptive Analytics agent ran the Simpson's Paradox check
- Re-run the top-level segmentation independently
- If any segment shows a trend opposite to the aggregate, flag it

If this check wasn't done: run it now before proceeding.

### Step 5 — Survivorship bias check
- Does the analysis include only users/entities that survived to the end of the period?
- If cohort analysis: are you comparing full cohorts or only those who stayed active?
- If funnel analysis: are you measuring drop-off correctly, or only tracking those who completed?

Flag any survivorship bias issues with the finding they affect.

### Step 6 — Selection bias check
- How was the analysis population defined?
- Could the definition of the population be excluding an important group?
- For A/B test results: was assignment truly random? Were there pre-treatment differences between groups?

### Step 7 — Look-ahead bias check (for time-series)
- Does the analysis use future data to inform past decisions?
- Are there any features or metrics that couldn't have been known at the time of the event being analyzed?

### Step 8 — Check for known data artifacts
Cross-reference with the data profile:
- Do any findings coincide with known tracking gaps, data pipeline issues, or instrumentation changes?
- Do any anomalies flagged in the trend analysis explain away findings rather than confirm them?

### Step 9 — Produce the validation report
For each key finding:
- **Finding:** the claim being validated
- **Original number:** from the Explore agents
- **Re-derived number:** from this validation
- **Match:** ✅ confirmed / ⚠️ discrepancy (explain) / ❌ failed (do not use)
- **Traps checked:** Simpson's Paradox, survivorship bias, selection bias, look-ahead bias
- **Status:** cleared for narrative / flagged for review / blocked

### Step 10 — Update the findings register
Mark each finding in the descriptive findings register as:
- ✅ **Validated** — cleared to enter the narrative
- ⚠️ **Caveated** — can enter the narrative with an explicit caveat
- ❌ **Rejected** — do not present; investigate further

## Output
A `validation-report.md` file in `/working` with the full validation checklist and status for each finding.

**Gate:** The Story Architect agent must not run until this validation report is complete and all headline findings are marked ✅ or ⚠️. No ❌ findings may enter the narrative.

## Anti-Patterns
- Do not validate by re-reading the original code — re-derive independently
- Do not let a "close enough" discrepancy slide — small errors compound
- Do not skip the Simpson's Paradox check because it was "already done" — verify it
- Do not validate only the numbers you're confident about — prioritize the surprising ones
