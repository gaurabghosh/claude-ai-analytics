# Skill: Data Quality Check

## Trigger Condition
Activate automatically any time a new dataset is introduced. Do not wait to be asked.

## Purpose
Ensure data quality issues are surfaced before they corrupt analysis. This skill runs as a pre-check before any analytical work begins on a dataset.

## Quick Checks (run on every new dataset, takes < 2 minutes)

1. **Row count sanity:** Is the number of rows plausible for what this data claims to represent?
2. **Null check:** Are any columns > 5% null? Flag them. Are any > 20% null? Flag loudly.
3. **Duplicate check:** Are there duplicate rows on the expected grain? How many?
4. **Date range check:** Does the date range match what's needed for the analysis?
5. **Numeric range check:** Are there negative values where there shouldn't be? Values > 100 in percentage columns?
6. **Category consistency:** Are categorical values consistent? (e.g., mixed case, abbreviations vs. full names)
7. **Join key check:** If multiple files, do the join keys match in format and coverage?

## Data Quality Severity Levels

| Severity | Definition | Action |
|---|---|---|
| 🟢 Clean | No significant issues | Proceed with analysis |
| 🟡 Caution | Issues present but manageable | Proceed with caveats; document issues |
| 🔴 Blocked | Issues severe enough to corrupt conclusions | Stop; do not proceed until resolved |

## Required Output
Before proceeding past this skill, output a one-line data quality status:
> "Data quality: 🟢 Clean — [row count] rows, [date range], no significant issues found."
> OR
> "Data quality: 🟡 Caution — [specific issues] noted; proceeding with [specific caveats]."
> OR
> "Data quality: 🔴 Blocked — [specific issue] prevents reliable analysis. [Specific fix] needed to proceed."
