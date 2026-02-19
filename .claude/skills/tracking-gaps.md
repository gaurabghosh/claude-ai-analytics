# Skill: Tracking Gaps

## Trigger Condition
Activate any time data is missing, incomplete, shows suspicious patterns, or a metric is unexpectedly low/zero for a period.

## Purpose
Missing data is not the same as zero. A tracking gap can look exactly like a real decline. Distinguishing between them is critical before any finding is reported.

## Signs That May Indicate a Tracking Gap
- Volume drops to zero or near-zero suddenly on a specific date
- A new segment appears mid-analysis that didn't exist in prior periods
- Event counts don't match session counts in an implausible way
- A known data source is missing rows for a specific date range
- Percentages change dramatically without a corresponding volume change

## Tracking Gap Investigation Checklist
When a suspected gap is found:

1. **Identify the start date** of the anomaly as precisely as possible
2. **Check if the gap is in source data or in a downstream calculation** (raw events vs. aggregated tables)
3. **Cross-reference with known events:** Were there product releases, SDK updates, tracking changes, or data migrations around that date?
4. **Check peer metrics:** If web sessions dropped, did server logs also drop? If not, it's likely a tracking issue
5. **Check other segments:** If only one segment shows the drop, more likely tracking. If all segments drop simultaneously, more likely real
6. **Quantify the gap:** How many rows/events are missing? What is the implied impact on the analysis?

## Classification
After investigation, classify the gap:
- 🟢 **Confirmed real change** — not a tracking issue
- 🟡 **Suspected tracking gap** — proceed with caveat; note the likely impact on findings
- 🔴 **Confirmed tracking gap** — findings that depend on this data cannot be presented reliably; flag to stakeholder

## Required Output
When a tracking gap is suspected or confirmed, add a note to the validation report:
> "⚠️ Tracking gap suspected: [metric] shows unusual pattern from [start date] to [end date]. Likely cause: [hypothesized cause]. Impact on analysis: [specific findings affected]. Recommendation: [verify with engineering / proceed with caveat / exclude period from analysis]."
