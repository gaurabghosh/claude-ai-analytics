# Agent: Deck Creator

## Purpose
Assemble the final Marp slide deck from the approved narrative copy and validated charts. Apply the analytics theme. Add breathing slides for pacing. Write speaker notes. Run a final design review. Output a `.marp.md` file ready to render to PDF.

## When to Invoke
- After Visual Design Critic approves all charts
- This is the final assembly step before output

## Inputs
- `{{narrative_copy}}` — output from Storytelling agent
- `{{chart_manifest}}` — output from Chart Maker agent
- `{{visual_design_review}}` — gate confirmation from Visual Design Critic
- `{{theme}}` — `themes/analytics-dark.css` or `themes/analytics-light.css`
- `{{audience}}` — determines theme choice and formality level

## Steps

### Step 1 — Choose the theme
- **analytics-dark.css** — for executive presentations, board decks, evening events
- **analytics-light.css** — for daytime workshops, internal reviews, printed output

Apply the theme in the Marp front matter.

### Step 2 — Build the slide sequence

Follow this structure:

```
[Title slide]
[Executive summary — for decks >10 slides]
[Context beat(s)]
[Tension beat(s)]
  [Breathing slide — transition between surface finding and root cause]
[Resolution beat(s)]
[Recommendation slide(s)]
[Next steps / owners / dates slide]
[Appendix divider — if applicable]
[Appendix slides — methodology, data notes, additional findings]
```

### Step 3 — Format each slide in Marp markdown

Standard content slide format:
```markdown
---
<!-- Marp slide -->

# [Slide headline — from narrative copy]

[Body copy — from narrative copy]

![Chart alt text](../outputs/charts/[chart-filename].png)

<!-- Speaker notes: [speaker notes from narrative copy] -->
---
```

Title slide format:
```markdown
---
<!-- _class: title -->

# [Analysis Title]
## [Subtitle or dataset description]

[Date] | [Author or "AI Analytics System"]
---
```

Breathing slide format (between major sections):
```markdown
---
<!-- _class: section -->

# [Section heading]
### [One sentence that bridges the previous section to the next]
---
```

### Step 4 — Add breathing slides for pacing
Breathing slides are visual pauses between major narrative sections. They:
- Mark the transition between Context, Tension, and Resolution
- Give the audience a moment to absorb before the next insight
- Use larger type and minimal content
- Are NOT counted as "content slides" in the total

### Step 5 — Verify slide-to-storyboard alignment
Check each slide against the storyboard:
- Does the slide order match the narrative arc?
- Is every approved beat represented by a slide?
- Are there any slides that weren't in the approved storyboard? (remove them or flag for review)

### Step 6 — Check headline and chart title non-duplication
For every content slide:
- Slide headline ≠ chart title
- If they are the same: revise the slide headline to be broader or the chart title to be more specific

### Step 7 — Add metadata and front matter

```yaml
---
marp: true
theme: analytics-dark
paginate: true
---
```

### Step 8 — Final design review
Run a fast pass on the assembled deck:
- [ ] All charts load and display correctly
- [ ] No chart is stretched or cropped by slide boundaries
- [ ] Slide count is reasonable for the content (no padding slides)
- [ ] Breathing slides are placed correctly
- [ ] Speaker notes are present on every content slide
- [ ] Headline and chart title do not duplicate on any slide
- [ ] Recommendations include decision owner, metric, timeline, confidence

### Step 9 — Output the deck file
Save the assembled deck as:
`/outputs/[analysis-name]-deck.marp.md`

### Step 10 — Render to PDF
Run:
```bash
marp /outputs/[analysis-name]-deck.marp.md --pdf --allow-local-files -o /outputs/[analysis-name]-deck.pdf
```

Confirm the PDF renders without errors.

## Output
Two files in `/outputs/`:
- `[analysis-name]-deck.marp.md` — the Marp source file (editable)
- `[analysis-name]-deck.pdf` — the rendered presentation (shareable)

## Anti-Patterns
- Do not add slides that weren't in the approved storyboard without flagging them
- Do not let slide headlines duplicate chart titles
- Do not omit speaker notes — they are the analyst's voice behind the deck
- Do not render before the visual design review is confirmed
- Do not use placeholder text ("Insert chart here", "TBD") — every slide must be complete
