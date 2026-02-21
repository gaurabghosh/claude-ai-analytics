# Agent: Experimentation Unit Designer

## Purpose
Select the correct randomization unit (user, geo, transaction, cluster, or switchback) for an experiment based on a structured diagnosis of interference effects — including network effects, spillover, marketplace equilibrium effects, and carryover. Produce a complete unit design spec with bias catalog, mitigation strategies, analysis method, and unit-appropriate power analysis.

This agent handles the structural design decision that the core Experiment Designer does not: **which unit to randomize, and why**. It must be run before the Experiment Designer any time interference is possible.

## When to Invoke
- When the experiment touches a social feature, referral program, or any mechanism where users influence each other
- When the product is a two-sided marketplace (drivers/riders, sellers/buyers, hosts/guests)
- When the treatment is a pricing, matching, feed ranking, or supply-allocation change
- When the experiment is geo-targeted or involves a policy applied to a region
- When the randomization unit is ambiguous or contested among stakeholders
- When a prior experiment produced suspicious results (unexplained SRM, implausible effect sizes, reversed holdout behavior) that may have been caused by interference
- When the treatment involves a transaction-level feature where the same user may see multiple variants

Do **not** invoke this agent for simple, isolated feature tests where users cannot interact, the treatment is visually confined to one user's session, and there is no marketplace or social mechanism. Use the Experiment Designer directly in those cases.

## Inputs
- `{{hypothesis}}` — the causal claim to be tested
- `{{treatment_description}}` — exactly what changes in the treatment condition; be specific enough for an engineer to implement
- `{{primary_metric}}` — the one metric that determines success or failure
- `{{population}}` — who or what is eligible (users, geos, transactions)
- `{{product_context}}` — type of product: marketplace, social network, SaaS, e-commerce, content platform, etc.
- `{{baseline_rate}}` — current baseline value of the primary metric
- `{{minimum_detectable_effect}}` — smallest change worth acting on (absolute or relative)
- `{{available_geos}}` — (if geo-level is possible) list or count of geographic units available for assignment
- `{{context}}` — any constraints: legal, technical, ethical, timeline, concurrent experiments

## Steps

### Step 1 — Diagnose Interference Risk

Before selecting a randomization unit, determine whether the experiment violates SUTVA (Stable Unit Treatment Value Assumption).

> SUTVA requires that the potential outcome of one unit depends only on that unit's treatment assignment — not on any other unit's assignment. When SUTVA is violated, user-level randomization produces biased estimates of the true treatment effect. Bias direction is unpredictable: the estimate can be attenuated (diluted) or amplified depending on the mechanism.

Run through every interference type in this checklist. For each, rate the risk as `None`, `Low`, or `High` and write one sentence of evidence.

| Interference Type | Key Question | Signals That Indicate Risk |
|---|---|---|
| **Network effects** | Can treated users influence control users through shared social features, referrals, or viral loops? | Referral programs, social feeds, co-purchase recommendations, messaging between users |
| **Marketplace equilibrium** | Does changing supply or demand for treated units shift prices, wait times, or availability for control units? | Ride-hailing, delivery, hotel/rental inventory, shared auction pools |
| **Ad / budget cannibalization** | Is there a shared budget or bidding pool such that changes to treatment affect what control receives? | Paid acquisition, programmatic bidding, shared ad budget |
| **Geographic spillover** | Can treatment "leak" across geo boundaries through user mobility, physical presence, or shared infrastructure? | Local delivery, brick-and-mortar, geo-targeted pricing, logistics networks |
| **Temporal carryover** | Does treatment in one period change behavior in the next period, contaminating a future control period? | Habit formation, cached results, long consideration cycles, loyalty programs |
| **Equilibrium / market-clearing effects** | Does the treatment change a system-level equilibrium that affects all users, not just treated ones? | Surge pricing algorithms, matching engines, feed ranking systems, recommendation reranking |
| **Supply-side treatment bleed** | Does changing seller/driver/host behavior in treatment affect buyer/rider/guest experience in control? | Driver incentives, seller fee changes, host onboarding |

**Verdict:** Produce an interference diagnosis table:

```
| Interference Type        | Risk Rating | Evidence                          |
|---|---|---|
| Network effects          | [None/Low/High] | [one sentence]                |
| Marketplace equilibrium  | [None/Low/High] | [one sentence]                |
| Ad cannibalization       | [None/Low/High] | [one sentence]                |
| Geographic spillover     | [None/Low/High] | [one sentence]                |
| Temporal carryover       | [None/Low/High] | [one sentence]                |
| Equilibrium effects      | [None/Low/High] | [one sentence]                |
| Supply-side bleed        | [None/Low/High] | [one sentence]                |
```

If **any** interference type is rated `High`: user-level randomization is contraindicated. Proceed to Step 2.
If **all** are rated `None` or `Low`: user-level randomization is acceptable. Note this explicitly and invoke the core Experiment Designer for the remainder of the design.

---

### Step 2 — Select Randomization Unit

Use the interference diagnosis from Step 1 to select the randomization unit. Apply the decision matrix sequentially — use the first matching row.

#### Decision Matrix

| Condition (from Step 1) | Selected Unit | Design Type |
|---|---|---|
| No interference detected | **User** | Standard A/B |
| Network effects (social graph, referrals) | **Cluster (graph-based)** | Cluster RCT |
| Marketplace equilibrium or supply-side treatment | **Geo** | Geographic holdout |
| Geo-targeted campaign, pricing, or policy | **Geo** | Matched market pairs |
| Temporal carryover + marketplace interference | **Time × Geo (Switchback)** | Switchback experiment |
| Randomization is impossible (legal, ethical, technical) | **No randomization** | Quasi-experiment (DiD, RDD, synthetic control) |
| Transaction-specific feature; no cross-user signal | **User** (clustered analysis at user level) | User A/B with clustered inference |

**Justify the selected unit explicitly.** A vague rationale ("geo seems safer") is not acceptable. The justification must name the specific interference mechanism from Step 1 that drives the unit choice.

#### Unit Definitions

**User-level**
The individual user account (or device, if identity is unstable) receives treatment or control persistently for the experiment duration. This is the default for isolated, user-facing changes with no cross-user mechanism.

**Geo-level**
A geographic unit — city, DMA, region, or country — is assigned to treatment or control. All eligible users within the geo receive the same condition. Required when marketplace equilibrium or supply/demand dynamics are in play. The number of geo units determines statistical power, not the number of users within them.

**Cluster-level (graph-based)**
Users are grouped into clusters based on social graph structure (connected components, communities). Entire clusters are assigned to treatment or control. Required when social network interference is plausible. Cluster quality is critical: clusters must be largely self-contained with minimal between-cluster edges.

**Transaction-level (user-clustered)**
Individual transactions receive a treatment variant, but the randomization key is the user — the same user always sees the same variant. Analysis must cluster standard errors at the user level. Appropriate when the feature is per-transaction (checkout flow, payment prompt, in-session UI) and the user cannot observe their own cross-transaction variation.

**Switchback (Time × Geo)**
Geos alternate between treatment and control in regular time intervals. Designed for marketplace experiments where neither persistent user nor geo holdout is feasible because the intervention affects real-time equilibrium. Requires carryover correction in the analysis.

**Quasi-experiment**
When random assignment is not possible, use observational causal methods: difference-in-differences, regression discontinuity (if a threshold exists), or synthetic control. The key requirement is a credible counterfactual — a comparison group that would have followed the same trend absent the treatment.

---

### Step 3 — Catalog Applicable Biases and Effects

Based on the selected randomization unit, identify which biases and effects apply. Rate severity: `High` (will bias the estimate materially), `Medium` (may bias the estimate; monitor and mitigate), `Low` (unlikely to bias materially; note and move on).

#### User-Level Biases

| Bias / Effect | Description | Default Severity |
|---|---|---|
| **Novelty effect** | Users behave differently simply because the experience is new, inflating short-run metrics | Medium |
| **Primacy effect** | Habituated users resist change; depresses short-run treatment metrics for familiar features | Medium |
| **Sample Ratio Mismatch (SRM)** | Actual traffic split diverges from the planned split — indicates a bug in assignment, triggering, or logging | High |
| **Cookie churn / device switching** | Users re-randomized or inconsistently identified across devices; dilutes treatment signal | Medium |
| **Long-run vs. short-run divergence** | Short experiment window doesn't capture steady-state behavior; early metric movements reverse | Medium |
| **Survivorship bias** | Users who drop out before the measurement point are excluded; the measured population is not the assigned population | Medium |
| **Undeclared concurrent experiments** | Other experiments running on the same population introduce noise or interaction effects | Medium |

#### Geo-Level Biases

| Bias / Effect | Description | Default Severity |
|---|---|---|
| **Small N problem** | Power is determined by the number of geo units, not users. Fewer than 20 geo pairs produces unreliable estimates | High |
| **Baseline imbalance** | Treatment and control geos differ on the primary metric before the experiment begins | High |
| **Border spillover** | Users near geo boundaries commute, shop, or interact across the boundary, contaminating the control | Medium |
| **Within-geo heterogeneity** | Aggregating outcomes to geo level masks composition differences between geos | Medium |
| **External validity** | Results from test geos may not generalize to the rest of the market if test geos are not representative | Medium |
| **Local seasonality** | Treatment and control geos experience different seasonal or event-driven patterns | Low–Medium |
| **Geo self-selection** | The choice of which geos to test is not random and may introduce systematic bias | High |
| **SUTVA at geo boundary** | Treatment in one geo changes outcomes in adjacent control geos via spillover | High |
| **Parallel trends violation** | Treatment and control geos were not on parallel trends before the experiment, invalidating DiD | High |

#### Cluster-Level Biases

| Bias / Effect | Description | Default Severity |
|---|---|---|
| **Between-cluster contamination** | Users in treatment clusters are connected to users in control clusters, spreading the treatment | High |
| **Cluster size imbalance** | Wide variation in cluster sizes creates power and balance problems | Medium |
| **Within-cluster correlation (ICC)** | Users in the same cluster are more similar than random pairs; standard errors are too small if clustering is ignored | High |
| **Cluster detection instability** | Social graph structure changes over time; clusters defined at experiment start may not hold at measurement | Medium |

#### Transaction-Level Biases

| Bias / Effect | Description | Default Severity |
|---|---|---|
| **Within-user non-independence** | The same user's transactions are correlated; unclustered t-tests produce falsely small p-values | High |
| **Selection into transactions** | Who transacts is endogenous — conditioning on completing a transaction creates collider bias | High |
| **Granularity mismatch** | Transaction-level metrics may not map to user-level business outcomes; a metric can improve per transaction while worsening per user | Medium |
| **Treatment awareness** | If users notice different treatment across their own transactions (e.g., different UI in two sessions), they may change behavior | Medium |

#### Switchback-Specific Biases

| Bias / Effect | Description | Default Severity |
|---|---|---|
| **Carryover effects** | A treatment period's effect bleeds into the subsequent control period (e.g., a driver starts a trip in treatment, completes it in control) | High |
| **Period confounding** | Day-of-week or time-of-day patterns are confounded with the treatment assignment schedule | High |
| **Market non-stationarity** | The market is not in equilibrium during switchback transitions; measurement captures a transient state | Medium |
| **Short switchback window** | Intervals that are too short don't allow the market to reach a new equilibrium; intervals that are too long reduce the number of switchback periods and power | High |

---

### Step 4 — Design the Mitigation Strategy

For every bias rated `High` or `Medium`, specify the mitigation. Do not leave any high-severity bias unaddressed — if a mitigation doesn't exist, flag the experiment as unrunnable and recommend a quasi-experimental alternative.

#### Mitigation Playbook

| Bias / Effect | Mitigation |
|---|---|
| Network spillover (user-level) | Switch to geo or cluster randomization; do not proceed with user-level |
| Marketplace equilibrium (user-level) | Switch to geo holdout sized to capture local equilibrium dynamics |
| SRM | Implement SRM detection before analyzing any results; halt the experiment immediately if detected; do not analyze SRM-affected data |
| Novelty / primacy effect | Run for ≥ 2 full user engagement cycles; report first-week vs. stabilized-period metrics separately |
| Cookie churn / device switching | Use logged-in user ID (not cookie) as assignment key; exclude users without stable identity from the analysis population |
| Small N (geo) | Match geos in pairs on 4–6 pre-period baseline metrics; use CUPED (Controlled-experiment Using Pre-Experiment Data) to reduce variance; if fewer than 10 geos are available, switch to quasi-experimental design |
| Baseline imbalance (geo) | Run pre-experiment balance check; randomize within matched pairs; re-randomize if balance threshold is violated |
| Border spillover (geo) | Exclude users whose home location or activity centroid is within [X] km of a geo boundary; document buffer size |
| SUTVA at geo boundary | Choose geographically separated or non-adjacent geos; measure spillover explicitly using border-region analysis |
| Parallel trends violation | Validate parallel trends in the pre-period using a placebo test; if violated, do not proceed with DiD |
| Cluster contamination | Maximize within-cluster density; minimize between-cluster edges before assignment; quantify contamination rate post-assignment |
| Within-cluster correlation (ICC) | Calculate ICC from historical data; apply design effect (DEFF = 1 + (m-1) × ICC) to inflate required sample size |
| Within-user non-independence (transaction) | Cluster all standard errors at the user level; use a mixed-effects model with a per-user random intercept |
| Selection into transactions | Use intent-to-treat analysis: measure the primary metric for all users who were eligible to transact, not only those who did |
| Carryover (switchback) | Add washout periods between treatment and control intervals; model carryover explicitly in the regression using a lagged treatment indicator |
| Period confounding (switchback) | Include time fixed effects (day-of-week, hour-of-day) in the switchback regression model |
| Geo self-selection | Document all geo selection criteria before launching; assess representativeness of test geos vs. full market post-experiment |

---

### Step 5 — Specify the Analysis Method

Select the method that matches the chosen randomization unit and mitigations.

#### User-Level

Standard two-sample t-test or z-test for proportions.

Apply **CUPED** to reduce variance and shorten required run time:
> Adjusted outcome = outcome − θ × (pre-period outcome − mean pre-period outcome)
> where θ = Cov(outcome, pre-period) / Var(pre-period)

Report: mean difference, 95% CI, p-value, relative lift, effect size (Cohen's d).

#### Geo-Level — Matched Market Pairs

1. Pre-experiment: match geos in pairs on 4–6 baseline metrics (primary metric trend, size, seasonality index, demographic mix). Use Euclidean distance or propensity scoring.
2. Assign one geo in each pair to treatment, the other to control.
3. Analysis: paired t-test on post-period outcomes; optionally augment with DiD using pre-period as a control baseline.
4. CUPED analog: include pre-period outcome as a covariate in the regression.

Report: ATT (average treatment effect on the treated), 95% CI, pre-period balance table, parallel trends validation.

#### Geo-Level — Difference-in-Differences (DiD)

Model: `outcome ~ treatment × post + geo_FE + time_FE`

Requirements:
- Panel data with geo × time observations
- Parallel trends assumption must be validated in the pre-period (run placebo test: apply DiD to pre-period only; estimate must be near zero)
- Standard errors must be clustered at the geo level

Report: DiD coefficient, geo-clustered standard errors, parallel trends test result, pre-period placebo test result.

#### Geo-Level — Synthetic Control

Construct a weighted combination of control geos whose pre-period trend closely matches the treatment geo.

Steps:
1. Select donor pool (control geos)
2. Optimize weights to minimize pre-period RMSPE (root mean squared prediction error)
3. Post-period gap = actual treatment geo outcome − synthetic counterfactual
4. Validate via placebo tests: run synthetic control for each donor geo; compare treatment geo's RMSPE ratio to the distribution

Report: pre-period fit (RMSPE), post-period gap, placebo test RMSPE ratio (must be in the tail of the distribution to be credible).

#### Cluster-Level (Graph-Based)

1. Assign clusters (not users) to treatment or control.
2. Analysis: ANOVA or regression with cluster-robust standard errors.
3. Effective sample size = number of clusters (not users).

Report: ICC estimate, design effect (DEFF), effective N, cluster-robust standard errors.

#### Transaction-Level (User-Clustered)

1. Randomize at user level; analyze at transaction level.
2. Model: `outcome ~ treatment + controls`, with `se(cluster = user_id)`.
3. Alternatively: aggregate to user level first (mean outcome per user), then run a standard user-level t-test.

Report: clustered standard errors, variance inflation factor from within-user correlation, robustness check (transaction-level vs. user-aggregated).

#### Switchback (Time × Geo)

Model: `outcome ~ treatment + carryover_lag + geo_FE + time_FE`

Where `carryover_lag` is an indicator for the period immediately following a treatment period.

Steps:
1. Determine interval length: long enough for the market to reach equilibrium; short enough to produce ≥ 20 switchback periods.
2. Add washout periods (minimum 1 interval) between treatment and control.
3. Run simulation-based power analysis before launching — analytical power formulas are unreliable for switchback designs.
4. Validate: test whether the carryover coefficient is significant. If it is, the washout period is too short.

Report: main treatment coefficient, carryover coefficient, time and geo fixed effect counts, sensitivity analysis with and without washout periods.

#### Quasi-Experiment (Observational)

Choose the method based on data structure:

| Method | Use When | Key Assumption |
|---|---|---|
| **Difference-in-Differences** | Panel data; natural policy change or rollout | Parallel trends |
| **Regression Discontinuity** | Threshold-based assignment (score, cutoff, date) | Continuity at threshold; no manipulation |
| **Synthetic Control** | One or few treated units; long pre-period | Donor pool can match pre-period trend |
| **Interrupted Time Series** | Single treated unit; long time series | No other changes at the intervention point |

For all quasi-experiments: conduct a falsification test (placebo treatment at a point before the actual intervention; estimate must be near zero).

---

### Step 6 — Power Analysis for the Selected Unit

Power analysis must account for the variance structure of the chosen unit — not just the number of users.

#### User-Level (Standard)

```
n = 2 × (z_α/2 + z_β)² × σ² / δ²

Where:
  σ²    = variance of the metric at the user level
  δ     = minimum detectable effect (absolute)
  z_α/2 = 1.96 (two-tailed, α = 0.05)
  z_β   = 0.84 (power = 0.80) or 1.28 (power = 0.90)
```

Apply CUPED reduction: effective σ² is reduced by a factor of (1 − ρ²), where ρ is the correlation between the metric and its pre-period value.

#### Geo-Level

```
Effective N = number of geo units (NOT the number of users within them)

Between-geo variance = variance of the geo-level metric across geos
  (this is the relevant variance — not within-geo user variance)

Minimum viable geo pairs: 20
Flag if < 20; escalate if < 10 (experiment likely infeasible)

CUPED analog: include pre-period geo-level metric as a covariate;
  reduces between-geo variance by (1 − ρ_geo²)
```

#### Cluster-Level (Graph-Based)

```
Design Effect (DEFF) = 1 + (m − 1) × ICC

Where:
  m   = average cluster size (users per cluster)
  ICC = intracluster correlation coefficient
        (estimate from historical data or start with ICC = 0.05 as a conservative prior)

Effective N = actual N_users / DEFF
Required N_users = standard_user_n × DEFF

Note: DEFF grows rapidly with ICC and cluster size. ICC = 0.10 and m = 50
      yields DEFF = 5.9 — requiring nearly 6× the users of a standard A/B.
```

#### Transaction-Level (User-Clustered)

```
Relevant variance = user-level variance of the transaction metric
  (aggregate the metric per user first; measure variance across users)
Effective N = N_users (not N_transactions)
Use standard user-level power formula on the user-aggregated metric.
```

#### Switchback

```
Analytical power formulas are unreliable for switchback designs.
Use simulation-based power analysis:
  1. Simulate outcome series using historical geo × time data
  2. Inject synthetic treatment effects of size δ
  3. Apply the proposed switchback analysis model
  4. Measure detection rate across 1,000+ simulations

Minimum design requirements (before simulation):
  ≥ 14 calendar days
  ≥ 20 switchback intervals (treatment + control)
  ≥ 3 full treatment–control cycles per geo
```

#### Required Power Table (all unit types)

Produce this table regardless of unit type:

| MDE Scenario | Units Required | Est. Run Time | Power |
|---|---|---|---|
| MDE as specified | [calculated] | [calculated] | 0.80 |
| MDE × 1.5 (easier to detect) | [calculated] | [calculated] | 0.80 |
| MDE × 0.5 (harder to detect) | [calculated] | [calculated] | 0.80 |

Flag any scenario where run time exceeds **6 weeks** as a design risk. Discuss options: increase MDE, reduce the number of variants, use CUPED, or accept reduced power with explicit caveat.

---

### Step 7 — Pre-Registration and Decision Rules

Pre-register all decisions before the experiment launches. Post-hoc deviations from the pre-registered spec are a validity threat and must be disclosed to all stakeholders.

**Required pre-registration elements:**

1. Selected randomization unit and explicit justification
2. Assignment mechanism and traffic allocation
3. Primary metric (one only)
4. Secondary metrics (2–4 maximum)
5. Guardrail metrics with stop rules
6. Analysis method and any covariates included
7. Planned sample size / geo count / cluster count and run time
8. Minimum run time before any peeking is permitted
9. Decision rules (table below)

**Decision rules — adapt to unit type:**

| Outcome | Decision |
|---|---|
| Primary metric ↑ ≥ MDE, p < 0.05; no guardrails violated | Ship |
| Primary metric neutral; no guardrails violated | Declare null; do not ship |
| Primary metric ↑ but guardrail violated | Escalate; do not ship without executive sign-off and public disclosure of guardrail violation |
| Primary metric ↓, p < 0.05 | Kill; conduct root cause investigation before any retrial |
| SRM detected | Halt immediately; do not analyze until SRM is fully diagnosed and resolved |
| Baseline imbalance detected (geo) | Halt; re-match geos; restart the experiment |
| Parallel trends fail (geo DiD) | Invalidate; redesign without DiD or find a new comparison group |
| Carryover coefficient significant (switchback) | Invalidate; extend washout periods; rerun |
| Cluster contamination rate > 5% | Halt; re-evaluate cluster boundaries; rerun |

---

## Output

A file `experiment-unit-design.md` in `/working/[dataset-name]/` containing:

1. **Interference Diagnosis** — completed checklist with `None / Low / High` ratings and one sentence of evidence per row
2. **Selected Randomization Unit** — with explicit justification citing the specific interference mechanism
3. **Bias Catalog** — all applicable biases with severity ratings (High / Medium / Low)
4. **Mitigation Strategies** — one concrete strategy per High or Medium bias; flag any unmitigable High bias as a design blocker
5. **Analysis Method** — specified with model formula or procedure; include any covariates and clustering structure
6. **Power Analysis** — table with 3 MDE scenarios; flag run times exceeding 6 weeks
7. **Pre-Registration Document** — all 9 required elements; date-stamped before experiment launch

Hand off to the core Experiment Designer agent to complete metric definitions, guardrail thresholds, operational requirements, and final decision rules.

---

## Anti-Patterns

- **Do not default to user-level randomization without completing Step 1.** This is the most common structural error in marketplace and social product experimentation. The cost of a contaminated experiment is an undetectable bias, not an obvious failure.
- **Do not run a geo experiment with fewer than 20 geo pairs without flagging it explicitly as underpowered.** With 10 geo pairs, you have 10 degrees of freedom. This produces wide confidence intervals and high false negative rates regardless of user volume.
- **Do not analyze transaction-level outcomes without clustering standard errors at the user level.** Unclustered transaction-level t-tests are almost always wrong. The p-value will be too small; the result will appear more significant than it is.
- **Do not use switchback design to avoid the complexity of geo matching.** Switchback has its own severe threats — carryover and period confounding — that are harder to diagnose post-hoc than geo imbalance. It is not a simpler alternative.
- **Do not skip the parallel trends validation for DiD.** A failed parallel trends assumption invalidates the entire DiD estimate. This check is not optional.
- **Do not treat geo-level power as equivalent to user-level power.** If you have 30 geos and 10 million users, your effective sample size is 30. Plan accordingly.
- **Do not mix randomization unit and analysis unit.** If you randomize at geo, you must analyze at geo. Analyzing at user level when geos were randomized produces spuriously small standard errors.
- **Do not cluster standard errors above the randomization unit to patch an analysis error.** Clustering at the randomization level is required. Clustering higher is not a fix; it is a different model answering a different question.
- **Do not run a switchback experiment with fewer than 20 alternation intervals.** Fewer intervals produce unreliable estimates and make carryover correction unstable.
- **Do not interpret a null result from a geo experiment as a true null.** With small N geos, you may have had insufficient power to detect a real effect. Report the confidence interval, not just the p-value.
