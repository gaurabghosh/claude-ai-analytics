# Skill: Guardrails

## Trigger Condition
Always active. These rules apply to every interaction, every analysis, every output.

## Non-Negotiable Rules

### On Analysis Quality
1. **Never present an unvalidated finding as a conclusion.** Label hypotheses as hypotheses. Label validated findings as findings. Don't mix them up.
2. **Never skip the Simpson's Paradox check.** Aggregate trends must be segmented. Always.
3. **Never confuse correlation with causation.** Use "associated with," "correlated with," "coincides with" — not "caused by" — unless you have experimental evidence.
4. **Never use the last data point as a trend.** One data point is not a trend. Three is the minimum.
5. **Never calculate an average of rates without weighting by volume.** An average conversion rate across segments must be volume-weighted.

### On Data Integrity
6. **Never present a number you haven't re-derived independently.** The Validation agent exists for this reason. Use it.
7. **Never silently drop nulls, outliers, or data quality issues.** Document every data cleaning decision and its impact on the analysis.
8. **Never use a partial period in a comparison without flagging it.** MTD vs. last full month is not a fair comparison.

### On Communication
9. **Chart titles must state the insight, not describe the chart.**
10. **Chart titles must not duplicate slide headlines.**
11. **Recommendations must include: recommendation, confidence level, decision owner, success metric, follow-up date.** All five fields. No exceptions.
12. **Never recommend "more analysis" as the primary conclusion.** If the data supports a recommendation, make it. If it doesn't, say what's missing and what analysis would resolve it.

### On System Improvement
13. **When feedback is given, update the agent or skill file — don't just fix the current output.** The system should improve permanently, not just locally.
14. **When a new anti-pattern is discovered, add it to the relevant agent file.** The system learns from mistakes.

## Soft Rules (strong defaults, can be overridden with justification)
- Prefer horizontal bar charts for category comparisons
- Use gray-first coloring in all charts
- Keep slide body copy to 4 sentences or fewer
- Write speaker notes for every content slide
