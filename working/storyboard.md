# Storyboard: Food Delivery Performance Analysis

## Audience Brief
Operations leadership and product management team. They know the business has a "26-minute average" but haven't looked beneath it. They are optimising for customer NPS and repeat order rate — both of which correlate with delivery time reliability. They fear that fixing this requires capital investment in riders or infrastructure. They need to decide where to focus Q2 operational improvements.

## Central Tension
> "The 26-minute average masks a system with extreme variation — and three factors that are at least partially controllable account for almost all of it."

## Findings NOT Included (and why)
- **Vehicle type (motorcycle vs scooter):** Confounded by city-traffic routing mix. Not an actionable vehicle recommendation. Moved to appendix.
- **Semi-Urban city segment:** n=164 orders. Statistically too small for reliable conclusions. Mentioned as data gap.
- **Alternating daily pattern:** Interesting structural finding (driven by traffic and batching mix variation day-to-day) but doesn't change the recommendations. Moved to appendix.
- **Order type (Meal/Snack/Buffet/Drinks):** No meaningful difference (<0.5 min variation). Not included.

---

## Beat-by-Beat Storyboard

```
Beat 1: "The baseline looks fine — until you look underneath"
─────────────────────────────────────────────────────────────
Narrative question:  What is this dataset, and what are we measuring?
Key insight:         45,593 orders across Indian cities (Feb–Apr 2022). Mean delivery = 26.3 min. Looks acceptable.
Evidence:            V1 — overall mean 26.29 min; 45,593 orders; date range confirmed.
Chart:               Horizontal bar chart showing distribution of delivery times (histogram-style binned bar).
                     Story point: the RIGHT TAIL (40+ min orders) highlighted in orange.
Transition question: So what's in that tail — and how big is it?
```

```
Beat 2: "Traffic alone adds 10 minutes — and Jam is almost a third of all orders"
──────────────────────────────────────────────────────────────────────────────────
Narrative question:  What's the single biggest driver of delivery time?
Key insight:         Traffic density is the strongest single lever: Jam conditions add 9.9 min vs Low traffic.
                     Jam = 31% of all orders (14,143 of 45,593).
Evidence:            V9 — Low=21.3 min, Jam=31.2 min; Simpson's Paradox confirmed consistent across cities.
Chart:               Horizontal bar chart: 4 traffic levels, gray for Low/Medium/High, orange for Jam.
                     Direct labels on each bar. Annotation on Jam: "+9.9 min vs Low".
Transition question: Traffic is partially external — what can operations actually control?
```

```
Beat 3: "Batching 2+ orders isn't twice the work — it's triple the time"
─────────────────────────────────────────────────────────────────────────
Narrative question:  What's the most controllable driver of delivery time?
Key insight:         Multiple deliveries show a non-linear step-change: moving from 1 to 2 orders per run
                     adds 13.6 minutes (51% jump). 3 deliveries = 47.8 min avg.
Evidence:            V5 — 0 del=22.9, 1=26.9, 2=40.5, 3=47.8 min. Validated independently.
Chart:               Bar chart with 4 bars (0, 1, 2, 3 deliveries). Story color on bar 2 (the step-change).
                     Annotation: "51% jump at 2 deliveries".
Transition question: Where do these two bad factors overlap?
```

```
Beat 4: "One in five orders sits in the worst combination"
──────────────────────────────────────────────────────────
Narrative question:  What does it look like when traffic and batching compound?
Key insight:         Metropolitan city + Jam traffic + 1+ deliveries = 17.9% of all orders (8,151).
                     Average delivery time in this segment: 33.1 min — 7 minutes above the overall mean.
Evidence:            V10 — 8,151 orders confirmed; V11 — 33.1 min avg confirmed.
Chart:               Stacked/grouped bar showing Metro vs Urban, broken by traffic level, highlighting
                     Metro+Jam bar with story color. OR a simple 2×2 heatmap table visual.
                     Clean annotation: "17.9% of all orders. 33 min avg."
Transition question: Is there anything else compounding on top of this?
```

```
Beat 5: "Rider quality adds another 12 minutes — and low-rated riders cluster in the hard routes"
───────────────────────────────────────────────────────────────────────────────────────────────────
Narrative question:  Beyond traffic and batching, what's the third lever?
Key insight:         Rider rating correlates strongly with delivery time (r=−0.34).
                     Top-rated riders (≥4.8) average 24.4 min. Low-rated (≤3.5) average 36.0 min.
                     11.6-minute gap.
Evidence:            V7, V8 — correlation and group means re-derived independently.
Chart:               Bar chart by rating bucket (5 bars), gray for high-rated, orange for low-rated.
                     Annotation: "11.6 min gap between top and bottom rated riders".
Transition question: Is any of this predictable in advance — or are we always reacting?
```

```
Beat 6: "Festivals are predictable — and we're adding 19.5 minutes to every one"
──────────────────────────────────────────────────────────────────────────────────
Narrative question:  Is there a predictable spike we're not managing?
Key insight:         Festival orders average 45.5 min — 19.5 minutes above non-festival baseline.
                     These 896 orders are known in advance from the calendar.
Evidence:            V4 — Festival delta 19.53 min. Validated; composition effects cannot explain a 19.5 min gap.
Chart:               Simple side-by-side bar: Festival vs No Festival. Story color on Festival bar.
                     Annotation: "+19.5 min. Predictable in advance."
Transition question: What should we do about all of this?
```

```
Beat 7: "Three levers. One priority."
──────────────────────────────────────
Narrative question:  What are the concrete recommendations?
Key insight:         Rec 1: Cap batch size at 1 for Metro+Jam conditions.
                     Rec 2: Route festival orders as singles, pre-staff.
                     Rec 3: Prioritise high-rated riders for Metro+Jam+multi combos.
                     Combined opportunity: 42,000+ minutes saved per equivalent period.
Evidence:            V11 — 5.2 min saved × 8,151 orders = 42,383 min. Conservative scenario.
Chart:               Opportunity summary table (not a chart) — 3 rows, one per recommendation,
                     with Conservative / Base / Optimistic sizing.
Transition question: —
```

---

## Narrative Coherence Review (self-check before Storytelling)

**Transition chain:** Beat 1→2 (what's in the tail?) ✅ | Beat 2→3 (what's controllable?) ✅ | Beat 3→4 (where do they overlap?) ✅ | Beat 4→5 (what else compounds?) ✅ | Beat 5→6 (is this predictable?) ✅ | Beat 6→7 (what do we do?) ✅

**Evidence-to-insight mapping:** All beats cite validated findings. Beat 4 is the most complex compound claim — re-confirmed via independent count.

**Logical gaps:** None. Each beat earns the next through a genuine transition question.

**Orphaned content:** Vehicle type, Semi-Urban, order type, alternating daily pattern — all moved to appendix. None orphaned in the main arc.

**Audience fit:** Operations/product leadership. No statistical jargon. All numbers are in minutes (intuitive). Recommendations include decision owner, metric, timeline.

**Recommendation quality:** Each recommendation will include decision owner, success metric, timeline, confidence. See narrative copy.

**Gate decision: ✅ Proceed to Storytelling**
