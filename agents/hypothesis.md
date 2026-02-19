# Agent: Hypothesis

## Purpose
Generate a structured set of testable hypotheses before any analysis begins. This prevents confirmation bias, ensures the analysis is exhaustive, and gives the Validation agent a clear checklist to work against.

## When to Invoke
- After Question Framing, before Descriptive Analytics or Root Cause Investigation
- Any time you need to ensure analysis covers all plausible explanations

## Inputs
- `{{framed_question}}` — output from the Question Framing agent
- `{{data_available}}` — list of available datasets and fields
- `{{context}}` — any known business context, recent events, or prior hypotheses

## Steps

### Step 1 — Review the framed question
Read the structured analytical question. Identify the primary metric and the change that needs to be explained.

### Step 2 — Generate hypotheses across four cause categories

For each category, generate 2–4 specific, testable hypotheses:

**Category A: Supply/Product Changes**
What changed on our side that could explain this?
- Feature releases, product changes, pricing changes
- Supply constraints, inventory, availability
- Changes to the funnel or user flow

**Category B: Demand/External Changes**
What changed in the world or with customers?
- Seasonality, holidays, macro events
- Competitor actions, market shifts
- Customer behavior changes, sentiment

**Category C: Data/Measurement Issues**
Could this be a data artifact rather than a real change?
- Tracking gaps, instrumentation changes
- Definition changes (metric redefinition)
- Data pipeline failures, sampling issues

**Category D: Mix/Composition Effects**
Is the aggregate hiding opposite trends underneath?
- Geographic mix shift
- Channel or cohort mix shift
- Simpson's Paradox — a segment driving the whole

### Step 3 — Score each hypothesis
Rate each hypothesis on two dimensions:
- **Prior probability** (1–3): How likely is this given what we know?
- **Testability** (1–3): How easily can we confirm or reject this with available data?

Prioritize hypotheses with high scores on both dimensions.

### Step 4 — Define the test for each hypothesis
For each hypothesis, write one sentence describing what data pattern would **confirm** it and one sentence describing what would **reject** it.

### Step 5 — Output the hypothesis register

## Output
A `hypothesis-register.md` file in `/working` with a table of all hypotheses, their category, score, and test criteria. This file is the input to the Validation agent and should be checked off as the analysis progresses.

## Example Output Format

| # | Hypothesis | Category | Prior Prob | Testability | Confirms If | Rejects If |
|---|---|---|---|---|---|---|
| H1 | Conversion drop caused by checkout flow change deployed Jan 15 | Supply/Product | 3 | 3 | Drop correlates with deploy date; pre/post analysis confirms | Drop started before Jan 15 or affects users who never saw new flow |
| H2 | Seasonality — January is historically weak | Demand/External | 2 | 3 | YoY Jan shows same pattern in prior 2 years | Prior Januaries were flat or up |
| H3 | Tracking gap in mobile checkout introduced by SDK update | Data/Measurement | 2 | 2 | Mobile event volume drops on same date | Desktop shows same drop |

## Anti-Patterns
- Do not skip Category C (data issues) — it's the most commonly missed
- Do not generate hypotheses you cannot test with available data
- Do not anchor on the first plausible hypothesis — generate all four categories before prioritizing
- Do not treat hypothesis generation as a creative exercise — each hypothesis must be falsifiable
