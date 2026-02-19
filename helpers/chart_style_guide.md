# Chart Style Guide

This guide governs all charts produced by the AI Analytics system. Follow this in conjunction with the Visualization Patterns skill.

## Typography
- **Title font:** System sans-serif (Helvetica Neue, Arial, or system default)
- **Title size:** 14–16pt
- **Label size:** 10–12pt
- **Annotation size:** 9–11pt
- **Axis label size:** 9–10pt
- **Font weight:** Regular for labels; Semi-bold for title and annotations

## Color System

### Dark Theme (`analytics-dark.css`)
| Role | Hex |
|---|---|
| Background | #1A1A2E |
| Text primary | #E8E8F0 |
| Text secondary | #9090A8 |
| Story color (highlight) | #4FC3F7 |
| Negative emphasis | #EF5350 |
| Positive emphasis | #66BB6A |
| Gray (de-emphasis) | #555570 |
| Grid lines | #2A2A45 |

### Light Theme (`analytics-light.css`)
| Role | Hex |
|---|---|
| Background | #FAFAFA |
| Text primary | #1A1A2E |
| Text secondary | #5A5A72 |
| Story color (highlight) | #1565C0 |
| Negative emphasis | #C62828 |
| Positive emphasis | #2E7D32 |
| Gray (de-emphasis) | #B0B0C0 |
| Grid lines | #E8E8F0 |

## Chart Dimensions
- Standard slide chart: 10" × 5.5" (landscape)
- Full-bleed chart: 13.33" × 7.5"
- Small multiple cell: 4" × 3"
- Export resolution: 200 DPI minimum (use `dpi=200` in matplotlib)

## Spacing and Padding
- Chart area padding: 0.15" on all sides
- Title top margin: 0.1"
- Label padding from bar/point: 4–6px
- Annotation padding from data point: 8–12px

## Line Weights
- Story point line (line charts): 2.5pt
- Context lines: 1.0pt
- Grid lines: 0.5pt
- Axis spine: 1.0pt (bottom and left only; remove top and right spines)

## Bar Chart Specifics
- Bar width: 0.6 (matplotlib default is 0.8; narrower looks cleaner)
- Spacing between bars in grouped charts: 0.05
- Bar corner radius: 0 (no rounded corners — they distort perception)

## Line Chart Specifics
- Story point: solid line, 2.5pt, story color
- Context lines: solid line, 1.0pt, gray
- Marker size (if used): 5pt circle, story color for story point, gray for context

## Annotation Format
- Annotations go above/beside the annotated data point, never overlapping it
- Arrow style (if used): simple, no arrowhead, 0.5pt line
- Text box: no box border; background transparent or very slightly tinted
