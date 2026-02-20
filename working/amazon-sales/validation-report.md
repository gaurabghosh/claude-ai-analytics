# Validation Report — Amazon India Sales

## Validation Checklist

| # | Finding | Original Number | Re-derived Number | Match | Status |
|---|---|---|---|---|---|
| V1 | Total revenue | ₹642,129,106 | ₹642,129,106 | ✅ Exact | Cleared |
| V2 | Gross revenue before discount | ₹754,214,601 | ₹754,214,601 | ✅ Exact | Cleared |
| V3 | Total discount given | ₹112,936,028 | ₹112,936,028 | ✅ Exact | Cleared |
| V4 | Discount as % of gross | 15.0% | 15.0% | ✅ Exact | Cleared |
| V5 | AOV at 0–5% discount | ₹74,224 | ₹74,224 | ✅ Exact | Cleared |
| V6 | AOV at 25–30% discount | ₹55,456 | ₹55,456 | ✅ Exact | Cleared |
| V7 | AOV gap (low vs high discount) | -25.3% | -25.3% | ✅ Exact | Cleared |
| V8 | Quantity mean (0–10% disc bucket) | 3.013 | 3.013 | ✅ Exact | Cleared |
| V9 | Quantity mean (20–30% disc bucket) | 3.008 | 3.008 | ✅ Exact | Cleared |
| V10 | Electronics revenue share | 34.2% | 34.2% | ✅ Exact | Cleared |
| V11 | Premium+Luxury revenue share | 74.2% | 74.2% | ✅ Exact | Cleared |
| V12 | Uplift if 20%+ disc capped at 10% | ₹39.1M | ₹39.1M | ✅ Exact | Cleared |
| V13 | High-discount tier orders | 3,162 | 3,162 | ✅ Exact | Cleared |
| V14 | Total_sales formula | (price×qty×(1−disc))+shipping | Verified exactly | ✅ Exact | Cleared |

---

## Analytical Trap Checks

### Simpson's Paradox ✅ PASSED
AOV decline with higher discount is consistent across ALL three categories (Electronics, Fashion, Home). No segment shows an opposite trend. Aggregate is not misleading.

### Survivorship Bias ✅ N/A
All 10,000 orders are "Delivered." No partial-period survivorship issue — all orders are in the final state. No cohort analysis was performed.

### Selection Bias ✅ N/A
No population filter was applied. The dataset represents all orders in the period.

### Look-Ahead Bias ✅ N/A
All analysis uses order_date as the event timestamp. No future data used to inform historical analysis.

### Partial Period Flag ✅ FLAGGED APPROPRIATELY
February data covers only 10 of 28 days. The -3.7% MoM decline in daily average is flagged as low-confidence and **excluded from the narrative** (F8 in descriptive findings).

### Data Artifacts ✅ ISOLATED
Ship/delivery date anomalies affect only logistics metrics — not used in any revenue calculation. Product name placeholders acknowledged — sub_category used instead.

### Weighted Average Check ✅ PASSED
Overall AOV (₹64,213) cross-checked: sum(total_sales)/count(orders) = 642,129,106 / 10,000 = ₹64,213. ✅

---

## Findings Cleared for Narrative

| Finding | Status |
|---|---|
| F1: ₹112.9M in discounts (15% of gross) | ✅ Validated — cleared |
| F2: AOV declines 25.3% from lowest to highest discount; quantity flat | ✅ Validated — cleared |
| F3: Electronics leads (34.2%) but categories within 1.8% of each other | ✅ Validated — cleared |
| F5: Furniture is #1 sub-category (₹111.8M, 17.4%) | ✅ Validated — cleared |
| F6: Premium+Luxury = 74.2% of revenue | ✅ Validated — cleared |
| F7: ₹39.1M recovery if 20–30% disc capped at 10% | ✅ Validated — cleared (with medium confidence caveat) |
| F8: Feb daily run rate -3.7% vs Jan | ❌ Excluded — partial period; not in narrative |

## Gate Decision

**All headline findings are ✅ or ⚠️ with documented caveats. Proceeding to Story Architect.**
