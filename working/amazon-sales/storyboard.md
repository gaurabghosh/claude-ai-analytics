# Storyboard: Amazon India Sales — The Discount Erosion Story

## Audience Brief
Commercial and sales leadership team. They see ₹642M in revenue and want to understand the performance drivers. They are likely proud of the absolute revenue number. They fear that tightening discounts will reduce order volume and damage topline. They need to decide whether to revise the discount policy for Q2 2026 before the pricing cycle resets.

## Central Tension
> "We generated ₹642M in sales — but quietly handed ₹113M of it back in discounts that didn't buy us a single extra unit."

## Findings NOT Included (and why)
- **Feb vs Jan daily trend (-3.7%):** Partial period (10 days); statistically unreliable. In appendix.
- **State-level geography:** US state names in India dataset — unreliable for actionable insight. In appendix.
- **Payment method breakdown:** Perfectly uniform distribution (25% each). No story here.
- **Brand analysis:** 500+ brands, no brand >0.2% of revenue. Not actionable.
- **Product-level analysis:** Product names are placeholder text. Impossible to analyze.

---

## Beat-by-Beat Storyboard

```
Beat 1: Context — "₹642M in sales from 10,000 orders"
──────────────────────────────────────────────────────
Narrative question:  What is the scale of the business we're analyzing?
Key insight:         Amazon India generated ₹642M in revenue across 10,000 orders,
                     Jan 1–Feb 10, 2026. Avg order value: ₹64,213.
Evidence:            V1 — ₹642,129,106 total; 10,000 orders confirmed.
Chart:               KPI summary (no chart — text-heavy context slide)
Transition question: How is this revenue distributed across categories?
```

```
Beat 2: Context — "Three categories, nearly identical in share"
──────────────────────────────────────────────────────────────
Narrative question:  Where is revenue coming from?
Key insight:         Electronics leads (34.2%) but Home (33.4%) and Fashion (32.4%) are within
                     1.8 percentage points. No single category dominates.
Evidence:            V10 — Electronics ₹219.4M | Home ₹214.8M | Fashion ₹208.0M
Chart:               Horizontal bar chart: 3 categories. All gray (no story hero here — the point
                     is uniformity). Labels show revenue and %.
                     Chart title: "Revenue is split almost equally — no category pulls ahead"
Transition question: If categories are equal, what IS creating variation in revenue?
```

```
Beat 3: Tension — "₹113M walked out the door in discounts"
────────────────────────────────────────────────────────────
Narrative question:  Where is value being lost?
Key insight:         ₹112.9M in discounts were given on ₹754.2M gross — 15% of potential
                     revenue never collected.
Evidence:            V2, V3 — gross ₹754.2M; discounts ₹112.9M; formula verified.
Chart:               Waterfall bar: Gross Revenue → minus Discounts → Net Revenue.
                     Discount bar highlighted in negative red.
                     Chart title: "One rupee in seven given away before the sale closes"
Transition question: Did those discounts at least drive more orders or larger baskets?
```

```
Beat 4: Tension — "Higher discounts don't move volume"
───────────────────────────────────────────────────────
Narrative question:  Are discounts at least buying incremental units?
Key insight:         Quantity per order is identical across all discount tiers: 3.01 units at 0–10%
                     discount, 3.01 units at 20–30% discount. Max deviation: 0.015 units.
Evidence:            V8, V9 — confirmed flat at 3.013 vs 3.008.
Chart:               Horizontal bar chart: 3 discount buckets × avg quantity.
                     All bars the same height. Annotation: "Volume doesn't budge."
                     Chart title: "Discounts buy nothing — quantity is flat across every tier"
Transition question: If units don't change, what happens to revenue per order?
```

```
Beat 5: Tension — "Each discount tier costs ₹6–9K per order"
──────────────────────────────────────────────────────────────
Narrative question:  What is the actual per-order cost of each discount tier?
Key insight:         AOV drops monotonically: ₹71K (0–10%) → ₹64K (10–20%) → ₹56K (20–30%).
                     The top discount tier generates 21% less revenue per order.
Evidence:            V5, V6, V7 — AOV by bucket confirmed; pattern holds across all 3 categories.
Chart:               Horizontal bar chart: 3 discount buckets × avg order value.
                     20–30% bucket highlighted in red. Annotation: "-21% vs low-discount orders"
                     Chart title: "Deep discounts cut revenue per order by ₹15K — with no volume gain"
Transition question: What's the total scale of the opportunity?
```

```
Beat 6: Opportunity — "₹39M recovery is within reach"
───────────────────────────────────────────────────────
Narrative question:  If we fixed the discount problem, how much is on the table?
Key insight:         If the 3,162 orders in the 20–30% discount tier were repriced to 10% discount,
                     revenue increases by ₹39.1M — a 6.1% gain on current ₹642M.
Evidence:            V12 — ₹39.1M uplift confirmed (assumes zero volume loss — upper bound).
Chart:               Sensitivity table (3 scenarios). Story color on base case.
                     Chart title: "Capping deep discounts recovers ₹23–39M in 41 days"
Transition question: Is this the whole opportunity, or just the start?
```

```
Beat 7: Opportunity — "Premium customers are the growth engine — protect them"
────────────────────────────────────────────────────────────────────────────────
Narrative question:  Where should we focus to maximize the discount recovery?
Key insight:         74.2% of revenue comes from Premium+Luxury unit prices (>₹25K).
                     Budget segment (<₹10K) = only 4.1% of revenue with 20% of the catalog.
Evidence:            V11 — Premium+Luxury ₹476.6M; Budget ₹26.4M.
Chart:               Horizontal bar: 4 price tiers by revenue. Premium+Luxury highlighted.
                     Chart title: "Three in four revenue rupees come from premium-priced items"
Transition question: What do we do about this?
```

```
Beat 8: Resolution — "Two decisions. One timeline."
─────────────────────────────────────────────────────
Narrative question:  What should leadership decide?
Key insight:         Rec 1: Cap max discount at 20% immediately (remove 20–30% tier)
                     Rec 2: Run 30-day A/B test to validate volume elasticity
                     Rec 3: Protect Premium/Luxury segment — no deep discounts on high-ticket items
Evidence:            All findings above.
Chart:               Structured recommendation table (decision owner, metric, timeline, confidence)
Transition question: —
```

---

## Narrative Coherence Review

**Transition chain:**
- Beat 1→2 (revenue scale → distribution) ✅
- Beat 2→3 (categories equal → so what varies? discounts) ✅
- Beat 3→4 (discounts cost → did they buy volume?) ✅
- Beat 4→5 (no volume → so what do they cost per order?) ✅
- Beat 5→6 (cost per order → what's the total opportunity?) ✅
- Beat 6→7 (opportunity → where to focus it?) ✅
- Beat 7→8 (focus → what decisions?) ✅

**Logical gaps:** None. Each beat answers the transition question from the previous beat.

**Orphaned content:** Feb trend, geography, payment method, brand — all moved to appendix. None in main arc.

**Audience fit:** Commercial leadership. No statistical jargon. All numbers in rupees. Recommendations include decision owner, metric, timeline, confidence.

**Gate decision: ✅ Proceed to Storytelling**
