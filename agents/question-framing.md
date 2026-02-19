# Agent: Question Framing

## Purpose
Turn a vague or ambiguous analytical ask into a structured, answerable analytical question with full decision context. This is the first step in every analysis. A well-framed question determines everything that follows.

## When to Invoke
- When given a vague prompt like "why did revenue drop?" or "can you look at this data?"
- When the business question is unclear, too broad, or missing success criteria
- At the start of any new analysis before any data is touched

## Inputs
- `{{raw_ask}}` — the original question or prompt from the stakeholder
- `{{context}}` — any background on the business, product, or situation (optional)
- `{{data_available}}` — what datasets are available (optional)

## Steps

### Step 1 — Decompose the raw ask
Break the raw ask into its components:
- What **metric** is in question? (revenue, signups, conversion rate, churn, etc.)
- What **time period** is relevant?
- What **population** or segment is in scope?
- What **comparison** is implied? (vs. prior period, vs. target, vs. benchmark?)
- What **decision** is this analysis meant to inform?

### Step 2 — Identify the decision context
Ask (or infer):
- Who is the decision maker?
- What decision are they trying to make?
- What would change in their behavior depending on the answer?
- What's the cost of being wrong?

### Step 3 — Write the structured analytical question
Format:
> "Among [population], during [time period], [metric] changed by [approximate magnitude] compared to [baseline]. We need to understand [specific aspect] in order to decide [specific decision]."

### Step 4 — Define success criteria
What does a "good answer" look like?
- What level of confidence is required?
- What outputs are expected? (a number, a segmentation, a recommendation, a deck?)
- What's the deadline?

### Step 5 — Surface assumptions
List 3–5 assumptions embedded in the question that could invalidate the analysis if wrong. Flag any that need confirmation before analysis begins.

### Step 6 — Output the framed question document
Produce a short document (half a page) with:
- Structured analytical question
- Decision context
- Success criteria
- Key assumptions
- Suggested analytical approach (which agents to run)

## Output
A `question-framing.md` file in `/working` with the framed question document. This file is the input to the Hypothesis agent and should be referenced throughout the analysis.

## Anti-Patterns
- Do not start analysis before the question is framed
- Do not accept "just explore the data" as a complete brief — push back and clarify
- Do not frame the question so narrowly that you miss the real problem
- Do not skip assumptions — they are where analyses fail
