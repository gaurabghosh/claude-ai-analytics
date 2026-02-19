# Agent: Overtime Trend

## Purpose
Find patterns in time-series data: long-term trends, seasonality, anomalies, inflection points, and leading indicators. This agent answers "when did things change, and is this part of a pattern?"

## When to Invoke
- In Phase 2 (Explore), in parallel with Descriptive Analytics
- Any time the question involves change over time, before/after comparisons, or forecasting context

## Inputs
- `{{data_profile}}` — output from Data Explorer agent
- `{{framed_question}}` — output from Question Framing agent
- `{{primary_metric}}` — the main KPI being analyzed
- `{{time_grain}}` — the granularity of time data available (daily, weekly, monthly)

## Steps

### Step 1 — Plot the full time series
Calculate the primary metric at the available time grain across the full date range. Note:
- Overall direction (upward, downward, flat)
- Any visible breaks or inflection points
- The scale of variation (is the recent change large or small relative to historical range?)

### Step 2 — Identify the trend component
Separate signal from noise:
- Calculate a rolling average (7-day for daily data, 4-week for weekly, 3-month for monthly)
- Is the underlying trend up, down, or flat?
- Has the trend direction changed at any point in the window?

### Step 3 — Identify and decompose seasonality
- Compare the current period to the same period in prior years (YoY)
- Calculate % change YoY for each time point
- Is the current deviation larger or smaller than typical seasonal variation?
- Are there weekly patterns (day-of-week effects)?
- Are there monthly or quarterly patterns?

Produce a "seasonality-adjusted" view: remove the typical seasonal effect to see the underlying signal.

### Step 4 — Detect anomalies
Flag any data points that are statistical outliers (>2 standard deviations from the rolling mean):
- Note the date and magnitude of each anomaly
- Classify each anomaly: likely data error / likely real event / uncertain
- For real-event anomalies: what business event could explain this? (check hypothesis register)

### Step 5 — Find inflection points
Identify the precise point(s) where the trend changed direction or rate:
- What date did the change begin?
- Was it a step change (sudden) or a gradual drift?
- Did it affect all segments simultaneously or did it spread?

Cross-reference inflection points with the hypothesis register: does the timing match any known product change, marketing event, or external factor?

### Step 6 — Analyze velocity and acceleration
- Is the rate of change accelerating or decelerating?
- Is the current period better or worse than the prior period in rate-of-change terms, even if the absolute number is still behind?
- Project current trend forward 1–2 periods (not as a forecast — as a "if nothing changes" scenario)

### Step 7 — Segment the time series
Repeat the trend analysis for the top 2–3 segments identified in Descriptive Analytics:
- Do segments have different inflection points?
- Do segments show different seasonality patterns?
- Is one segment leading the overall trend (leading indicator)?

## Output
A `trend-findings.md` file in `/working` with:
- Full time series summary
- Trend and seasonality decomposition
- Anomaly log (date, magnitude, classification)
- Inflection points with timing
- Velocity and acceleration summary
- Segment-level trend comparison

## Anti-Patterns
- Do not compare a partial period to a full period (e.g., MTD vs. last full month)
- Do not call a single data point a trend
- Do not ignore seasonality — seasonal effects mask or amplify real trends constantly
- Do not extrapolate a trend as a forecast without explicitly caveating uncertainty
