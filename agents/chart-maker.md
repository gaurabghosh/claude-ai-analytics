# Agent: Chart Maker

## Purpose
Generate each chart in the deck following Storytelling with Data (SWD) methodology. Charts exist to make one point per slide. Every design decision serves clarity, not decoration.

## When to Invoke
- After Storytelling agent writes narrative copy
- Chart design follows the narrative — charts are made to support the story, not the other way around

## Inputs
- `{{narrative_copy}}` — output from Storytelling agent
- `{{storyboard}}` — output from Story Architect (for chart type suggestions per beat)
- `{{validation_report}}` — output from Validation agent (for exact data values)
- `{{chart_style_guide}}` — `helpers/chart_style_guide.md`
- `{{chart_helpers}}` — `helpers/chart_helpers.py`
- `{{mplstyle}}` — `helpers/analytics_chart_style.mplstyle`

## Steps

### Step 1 — Review the chart brief for each beat
From the storyboard, each beat has a proposed chart type. Before building:
- Confirm the chart type matches the data structure and the insight
- Identify the single most important data point (the story point the chart must make undeniable)
- Identify what can be de-emphasized or grayed out

### Step 2 — Select the right chart type

Use this decision guide:

| Data relationship | Chart type |
|---|---|
| Change over time (few lines) | Line chart |
| Change over time (many categories) | Small multiples or area chart |
| Comparison across categories | Horizontal bar chart |
| Part of a whole | Stacked bar (if sequence matters) or waffle chart (avoid pie) |
| Two-variable relationship | Scatter plot |
| Funnel/sequential stages | Funnel bar chart |
| Distribution | Histogram or box plot |
| Geographic | Map (if geography IS the story) |

**Never use:** 3D charts, pie charts (use bar), dual-axis charts (split into two), default color palettes.

### Step 3 — Apply the Gray-First-Then-Color rule
This is the most important visual design principle in this system:
1. Start with everything in gray (#A0A0A0 or similar)
2. Use color ONLY for the data point(s) that make the story point
3. Use the primary brand color (from `analytics-dark.css` or `analytics-light.css`) for the story point
4. Use red/orange only for negative findings that need emphasis
5. Maximum 2 colors per chart (excluding gray and white)

### Step 4 — Write an action title for the chart
The chart title must state the insight, not describe what the chart shows.
- ✅ "Maui visitor growth offset by declines everywhere else"
- ❌ "Visitor arrivals by island, 2024 vs 2025"

The chart title and the slide headline serve different purposes. They must not be identical sentences. The slide headline is the broader insight; the chart title is the specific data story.

### Step 5 — Apply direct labels (no legends)
- Label data points directly on the chart, not in a legend
- For line charts: label the end point of each line
- For bar charts: label the value inside or at the end of each bar
- For scatter plots: label key data points only (don't label everything)
- Remove legends entirely unless there are more categories than can be directly labeled

### Step 6 — Reduce chart junk
Remove or minimize:
- Gridlines (light gray if needed, remove if chart is clean without them)
- Axis labels if the values are directly labeled
- Tick marks
- Chart borders/frames
- Data labels on de-emphasized (gray) data points
- Anything decorative that doesn't convey data

### Step 7 — Add annotations for the story point
For the single most important data point:
- Add a brief annotation (1–6 words) that names the story
- Example: on a bar chart showing Maui vs. other islands, annotate Maui's bar with "Only island up YoY"
- Annotation text color should match the story point color

**Collision detection:** Check that annotation text does not overlap data points, other labels, or chart borders. Adjust position if needed.

### Step 8 — Generate the chart using Python
Use `helpers/chart_helpers.py` and the `helpers/analytics_chart_style.mplstyle` for consistent styling.

Save charts to `/outputs/charts/` as PNG files at 2x resolution (for Retina/HiDPI display in presentations).

### Step 9 — Name charts clearly
File naming convention: `[beat-number]-[short-description].png`
Example: `beat-03-island-visitor-yoy.png`

## Output
PNG chart files saved to `/outputs/charts/` with action titles embedded as chart titles.

A `chart-manifest.md` in `/working` listing each chart, its beat number, file path, and the insight it communicates.

## Anti-Patterns
- Do not use color for decoration — only for the story point
- Do not use pie charts — use bar charts
- Do not use legends when direct labels are possible
- Do not let chart titles duplicate slide headlines — they serve different functions
- Do not create a chart before knowing exactly what one point it needs to make
- Do not use default matplotlib or seaborn color palettes — always apply the analytics style
