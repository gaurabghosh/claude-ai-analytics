# Narrative Copy: Food Delivery Performance Analysis

---

## Executive Summary (for a reader who reads only one slide)

- Average delivery time across 45,593 orders is 26.3 minutes — but the range runs from 10 to 54 minutes, and three factors explain most of that variation.
- Jam traffic adds 9.9 minutes and affects 31% of all orders; batching 2+ deliveries simultaneously adds another 13.6 minutes in a near-step-function; low-rated riders are 11.6 minutes slower than top-rated ones.
- These three factors compound: Metropolitan + Jam + multi-delivery accounts for 17.9% of all orders and averages 33.1 minutes.
- Festival orders — fully predictable from the calendar — run 19.5 minutes above baseline with no evidence of current mitigation.
- **Three targeted actions can recover an estimated 42,000+ rider-minutes per equivalent period at conservative assumptions.**

---

## Beat 1: Context

**Slide headline:** 45,500 deliveries, 26 minutes average — the surface looks fine

**Body copy:** This analysis covers 45,593 food delivery orders placed across Indian cities between February and April 2022. The headline metric — average delivery time — sits at 26.3 minutes. For an operations team, that number alone doesn't raise alarms. But averages compress everything that matters. Delivery times in this dataset range from 10 minutes to 54 minutes, and the shape of that distribution tells a different story.

**Speaker notes:** Set the stage quickly. The audience probably knows the 26-minute number. The job of this slide is to create just enough unease to make them want to see what's underneath it. Don't linger here — you want them asking "so what's driving the variation?" within 30 seconds.

---

## Beat 2: Traffic is the loudest signal

**Slide headline:** Jam traffic adds 10 minutes to every delivery it touches

**Body copy:** Traffic density is the single strongest predictor of delivery time. Orders fulfilled in Jam conditions average 31.2 minutes — 9.9 minutes longer than orders in Low traffic (21.3 min). This isn't a tail event. Jam conditions affect 31% of all orders in this dataset, making it the most common high-traffic state after Low. Medium and High conditions cluster together around 27 minutes; the real break is between anything below Jam and Jam itself.

**Speaker notes:** The Simpson's Paradox check is already done — this pattern holds consistently within both Urban and Metropolitan cities, so it's not a city-mix artifact. If someone asks "is this because most Jam orders happen in Metro cities?" — the answer is yes, but the *within-Metro* Jam effect is just as strong (Metro/Jam = 31.9 min vs Metro/Low = 22.1 min). The direction doesn't change.

---

## Beat 3: Batching 2+ orders isn't efficiency — it's a 51% time penalty

**Slide headline:** Two simultaneous deliveries adds 14 minutes — a non-linear step

**Body copy:** Multiple deliveries per run show a striking pattern that operations should treat as a hard constraint, not a continuous trade-off. Single-delivery runs average 26.9 minutes. Batching two deliveries jumps to 40.5 minutes — a 13.6-minute increase, or 51%. Three deliveries average 47.8 minutes. The jump from 1 to 2 is not gradual; it's a threshold effect. And it happens on 2,346 orders in this dataset — roughly 5% of all runs.

**Speaker notes:** The "why" behind the step-function is routing: a rider completing two separate drop-offs must fully complete the first delivery before reaching the second customer, compounding waiting time at both ends. The implication is that batching 2+ deliveries in high-complexity conditions isn't a capacity gain — it's a guaranteed time penalty to one or more customers.

---

## Beat 4: One in five orders sits in the worst combination

**Slide headline:** Metro + Jam + multi-delivery: 17.9% of orders, 7 minutes above average

**Body copy:** These three factors — Metropolitan city, Jam traffic, and batching — don't just add independently. They compound. Orders that combine all three conditions average 33.1 minutes, which is 6.8 minutes above the overall mean and 10 minutes above what the same rider would achieve in Low traffic on a single run. This segment represents 8,151 orders — nearly 1 in 5 of every order in the dataset. It is the primary operational target.

**Speaker notes:** This is the "so what" moment of the analysis. The business has a 26-minute average because Metropolitan/Low/single-delivery orders (averaging 20 minutes) are pulling the mean down against this 33-minute cluster. The question to raise with the audience: "Do your routing and dispatching systems treat these conditions differently today?" The answer in most standard delivery systems is: no.

---

## Beat 5: Rider quality adds another 12-minute gap

**Slide headline:** Low-rated riders deliver 12 minutes slower — and they're assigned to the hardest routes

**Body copy:** Rider rating correlates meaningfully with delivery time (r = −0.34). Riders rated 4.75–5.0 average 24.4 minutes. Riders rated below 3.5 average 36.0 minutes — an 11.6-minute difference on the same order types. The concern isn't just the average gap. It's that in the absence of quality-aware dispatching, low-rated riders are no less likely to be assigned to Metropolitan + Jam + multi-delivery runs than high-rated ones.

**Speaker notes:** Correlation, not causation — this could reflect that better riders self-select into favourable conditions, or that lower-rated riders are newer and still learning routes. Either way, the operational implication is the same: quality-aware dispatching (prioritising high-rated riders for complex multi-stop runs in congested areas) is a lever that costs nothing in infrastructure.

---

## Beat 6: Festival spikes are fully predictable — and we're adding 19.5 minutes to every one

**Slide headline:** Festival orders take 45 minutes — a predictable surge with no visible mitigation

**Body copy:** Festival orders average 45.5 minutes — 19.5 minutes above the non-festival baseline of 26.0 minutes. These 896 orders are knowable in advance from the public calendar. Unlike weather or traffic, festivals are not surprises. The absence of any visible flattening of this spike in the data suggests no structured pre-staffing or routing adjustment is currently in place for festival periods.

**Speaker notes:** 896 orders is 2% of the dataset, so the total volume impact is modest. But the per-customer experience during festivals is severe: a customer who normally gets their order in 26 minutes waits 45 minutes. These are often high-intent orders (celebrations, gatherings) with higher average basket sizes. The reputational cost of a 45-minute festival delivery likely exceeds the operational cost of a targeted pre-staffing response.

---

## Beat 7: Three levers. One priority order.

**Slide headline:** Cap batching, pre-staff festivals, and match riders to conditions

**Recommendation 1: Cap batch size at 1 for Metro + Jam conditions**
- **Rationale:** Batching 2+ deliveries adds 13.6 minutes per order in already-congested conditions. Applying a single-delivery cap to Metro/Jam dispatching targets the 8,151-order high-impact cluster directly.
- **Decision owner:** Head of Dispatch Operations
- **Success metric:** Average delivery time for Metro/Jam orders reduced from 31.9 min to ≤28 min within 60 days of policy implementation
- **Timeline:** Implement in dispatch routing logic within 30 days
- **Confidence:** Medium — assumes dispatch system can enforce a routing constraint by city+traffic condition
- **Key risk:** Rider utilisation may drop in Metro/Jam zones during peak periods; model the capacity impact before full rollout

**Recommendation 2: Pre-staff and route festival orders as singles**
- **Rationale:** Festival orders are calendar-predictable and run 19.5 min above baseline. A targeted pre-staffing and single-order routing protocol during festival periods would directly address the spike.
- **Decision owner:** City Operations Manager
- **Success metric:** Festival order average delivery time reduced from 45.5 min to ≤35 min in next festival period
- **Timeline:** Define festival calendar trigger criteria within 14 days; test in one city in next festival event
- **Confidence:** Medium — volume is modest (896 orders), making this low-risk to pilot
- **Key risk:** Festival definitions may vary by city; require city-level calendar input

**Recommendation 3: Implement quality-aware dispatching for complex runs**
- **Rationale:** Top-rated riders (≥4.8) deliver 11.6 min faster than low-rated riders (≤3.5). Prioritising high-rated riders for Metro+Jam+multi-delivery assignments closes a gap that currently costs nothing except a dispatching rule change.
- **Decision owner:** Product Manager, Dispatch Algorithms
- **Success metric:** Rider rating of dispatched riders in Metro/Jam/multi-delivery segment increases from current mix to ≥4.5 avg within 45 days
- **Timeline:** Dispatching algorithm update within 45 days
- **Confidence:** Low-Medium — correlation does not establish causation; pilot recommended before full rollout
- **Key risk:** High-rated rider availability may not match Metro/Jam peak demand timing; monitor for unintended fairness effects on rider earnings

**Opportunity size (conservative):**
- Metro+Jam+multi-delivery: 8,151 orders. Reducing avg from 33.1 to 27.9 min = 5.2 min saved per order
- Total: 8,151 × 5.2 = **42,383 rider-minutes saved** per equivalent 54-day period
- Base case: 5.2 min/order. Conservative: 3.0 min/order (24,453 min). Optimistic: 8.0 min/order (65,208 min)

**Speaker notes:** The goal of this slide is a decision, not a discussion. Ask the room: which of these three can we move on this quarter? Rec 1 and Rec 2 are low-infrastructure changes — dispatching rules and staffing protocols. Rec 3 requires algorithm work but has the largest potential upside if the correlation reflects genuine skill differences rather than route self-selection.
