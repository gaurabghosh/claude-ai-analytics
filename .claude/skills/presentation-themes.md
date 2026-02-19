# Skill: Presentation Themes

## Trigger Condition
Activate any time slides are being assembled.

## Theme Selection Guide

| Theme | File | Use for |
|---|---|---|
| Dark | `themes/analytics-dark.css` | Executive presentations, board decks, evening events, external audiences |
| Light | `themes/analytics-light.css` | Internal reviews, daytime workshops, documents that will be printed |

When unsure: ask the user which theme to use. Default to dark for external, light for internal.

## Slide Type Classes

| Slide type | Marp class | Use for |
|---|---|---|
| Title | `<!-- _class: title -->` | First slide only |
| Section break | `<!-- _class: section -->` | Between major narrative sections |
| Standard content | (no class) | All content slides |
| Full-bleed image | `<!-- _class: image -->` | When a chart or image should fill the slide |
| Appendix divider | `<!-- _class: appendix -->` | Before appendix slides |

## Marp Front Matter Template
```yaml
---
marp: true
theme: analytics-dark
paginate: true
---
```

## Spacing and Layout Principles
- Charts should occupy 60–70% of the slide area
- Headlines at top; charts below; body copy to the side or below the chart
- Do not crowd slides — if a chart needs more space, let it have the slide
- Breathing slides use 30–50% font size scaling for the section heading

## Slide Count Guidelines
These are guidelines, not targets. Let the story determine the length.
- Executive brief: 8–12 slides
- Full analysis: 15–25 slides
- Appendix: as many as needed (not counted in the main deck length)

Breathing slides (section transitions) are not counted toward the main deck total.
