# Skill: Analysis Design Spec

## Trigger Condition
Activate before starting any multi-step analysis. Runs after question framing, before data exploration.

## Purpose
Create a lightweight spec before doing work. Prevents scope creep, wasted effort on wrong analyses, and surprises at the end.

## Spec Template (fill before analysis begins)

```
ANALYSIS SPEC
─────────────────────────────
Question: [framed analytical question]
Primary metric: [name, definition, unit]
Time period: [start date – end date]
Population: [who/what is included; who/what is excluded]
Data sources: [list of files/tables to use]
Dimensions available: [list of fields available for segmentation]

Planned analyses:
  1. [agent name]: [what it will produce]
  2. [agent name]: [what it will produce]
  ...

Expected output:
  - [file type and destination]

Assumptions:
  - [assumption 1]
  - [assumption 2]

Known data limitations:
  - [limitation 1]
```

## Rule
This spec does not need to be perfect. It needs to exist. Writing it takes 5 minutes and prevents hours of rework.

Output the spec in `/working/analysis-spec.md` before proceeding.
