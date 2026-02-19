# Skill: Metric Spec

## Trigger Condition
Activate any time a metric is introduced or calculated that hasn't been formally defined in the current analysis.

## Purpose
Undefined metrics cause silent errors. Two analysts calculating "conversion rate" with different denominators will get different numbers and neither will be wrong — they're just measuring different things. Always specify.

## Metric Spec Format
For every metric introduced in an analysis, write a one-line spec:

```
Metric: [metric name]
Definition: [precise calculation — numerator / denominator]
Unit: [%, count, $, minutes, etc.]
Time grain: [daily, weekly, monthly]
Population: [who is included; who is excluded]
Data source: [field names or tables used to calculate it]
Caveats: [known issues, edge cases, or limitations]
```

## Example
```
Metric: Checkout conversion rate
Definition: orders completed / sessions that reached cart page
Unit: %
Time grain: daily
Population: logged-in users only; excludes guest checkout (not tracked)
Data source: events.order_complete / events.cart_view
Caveats: mobile sessions undercounted due to SDK gap before Jan 15
```

## Rule
If a metric doesn't have a spec, write one before using it. If you can't write one (because the definition is unclear), flag it as an undefined metric and do not use it in the narrative until it's resolved.

Store metric specs in `/working/metric-specs.md`.
