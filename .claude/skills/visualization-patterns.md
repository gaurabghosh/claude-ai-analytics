# Skill: Visualization Patterns

## Trigger Condition
Activate any time a chart is being designed or generated.

## Core Principles (Storytelling with Data methodology)

### 1. One point per chart
Every chart must make exactly one point. If you're trying to show two things, make two charts. If you can't state the chart's point in one sentence, the chart is trying to say too much.

### 2. Gray-first-then-color
- Everything starts gray
- Color is applied ONLY to the data that makes the story point
- Maximum 2 non-gray colors per chart
- Red/orange: for negative findings that need emphasis
- Primary brand color: for the story point in positive/neutral findings

### 3. Action titles
Chart titles state the insight, not the chart description:
- ✅ "O'ahu hotel visitors drove the statewide decline"
- ❌ "Visitor arrivals by accommodation type, 2024–2025"

### 4. Direct labels, no legends
- Label data points directly on the chart
- Remove legends unless direct labeling is genuinely impossible
- For line charts: end-of-line labels
- For bar charts: value labels at bar end

### 5. Reduce chart junk
Remove: heavy gridlines, chart borders, tick marks where values are directly labeled, decorative elements, 3D effects, shadows.

## Chart Type Quick Reference

| If showing... | Use... | Avoid... |
|---|---|---|
| Trend over time | Line chart | Bar chart for long series |
| Comparison of categories | Horizontal bar | Vertical bar (for long labels), pie |
| Part of a whole | Stacked bar or 100% bar | Pie, donut |
| Two-variable relationship | Scatter | Line (implies time) |
| Distribution | Histogram or box plot | Bar chart |
| Funnel stages | Funnel bar | Pie, area |
| Geographic variation | Map (if geography IS the story) | Only if geography matters |
| Small multiples (many segments) | Small multiples grid | Single chart with many lines |

## Color Palette Reference
See `themes/analytics-dark.css` and `themes/analytics-light.css` for exact hex values.

- **Story color (dark theme):** defined in analytics-dark.css
- **Story color (light theme):** defined in analytics-light.css
- **Gray (de-emphasis):** #A0A0A0
- **Negative emphasis:** #E05252
- **Positive emphasis:** #52A052

## Annotation Style
- Font size: slightly smaller than data labels
- Color: matches the story point color
- Content: 2–6 words that name the story point
- Position: near the story point data, not overlapping it
