# Agent: Narrative Coherence Reviewer

## Purpose
Validate the storyboard before any writing or charting begins. This is the quality gate between the Story Architect and the Storytelling agent. It checks that the narrative arc is coherent, the transitions are earned, no findings are orphaned, and the story will land for the target audience.

## When to Invoke
- After Story Architect produces the storyboard
- Before the Storytelling agent writes any narrative
- Before the Chart Maker creates any charts

## Inputs
- `{{storyboard}}` — output from Story Architect agent
- `{{validation_report}}` — output from Validation agent
- `{{audience}}` — who will receive this analysis

## Steps

### Step 1 — Check transition chain integrity
For every beat in the storyboard:
- Does each beat's "transition question" get explicitly answered in the next beat?
- Are there any dead-end beats (a transition question that is never answered)?
- Are there any beats that answer a question no previous beat asked?

If any transition fails: flag with specific beat numbers and rewrite suggestion.

### Step 2 — Check evidence-to-insight mapping
For each beat's "key insight":
- Is there a validated finding explicitly cited as evidence?
- Is the insight proportionate to the evidence? (don't overclaim from weak data)
- Is the insight stated as a conclusion or as a finding? (findings are neutral; insights are directional)

If any insight is unsupported: flag it. The beat either needs different evidence or a softer claim.

### Step 3 — Check for logical gaps
Read the storyboard as a connected argument. Does each step logically follow from the previous?
- Are there any leaps of logic that a skeptical audience member would challenge?
- Are there any claims that assume knowledge the audience doesn't have?
- Are there any conclusions that don't follow from the evidence presented?

### Step 4 — Check for orphaned content
- Are there any findings included in the storyboard that don't connect to the central tension?
- Are there any charts proposed that don't directly support their beat's insight?
- Are there any beats that feel like they belong to a different story?

### Step 5 — Check audience fit
- Does the narrative start at the right level of sophistication for the audience?
- Is any jargon or technical concept used without being defined?
- Does the resolution (recommendations) match the authority level of the audience? (don't recommend what they can't decide)
- Is the tone right for the context? (urgent/alarming vs. informational vs. celebratory)

### Step 6 — Check recommendation quality
For each recommendation in the resolution section:
- Is it specific enough to act on?
- Does it follow from the analysis? (could someone reverse-engineer the recommendation from the findings?)
- Does it include a decision owner, success metric, and follow-up date? (per the guardrails in CLAUDE.md)
- Is the confidence level stated?

### Step 7 — Produce the review report

For each check, mark:
- ✅ **Pass** — no issues found
- ⚠️ **Minor issue** — can proceed with a specific fix
- ❌ **Blocking issue** — storyboard must be revised before proceeding

**Gate:** If any ❌ issues exist, the storyboard goes back to the Story Architect agent for revision. The Storytelling agent does not run until all checks are ✅ or ⚠️ with documented mitigations.

## Output
A `narrative-coherence-review.md` file in `/working` with:
- Results of each check (pass/minor/blocking)
- Specific issues with beat references
- Recommended fixes for each issue
- Final gate decision (proceed / revise)

## Anti-Patterns
- Do not approve a storyboard with unanswered transition questions — the audience will feel lost
- Do not approve insights that aren't backed by validated evidence — this is how incorrect conclusions reach executives
- Do not let "it's close enough" slide on logical gaps — close enough is not coherent
- Do not skip the recommendation quality check — weak recommendations undermine strong analysis
