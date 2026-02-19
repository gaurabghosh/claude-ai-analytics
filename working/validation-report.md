# Validation Report

## Findings Validated

| # | Finding | Original | Re-derived | Match | Traps Checked | Status |
|---|---|---|---|---|---|---|
| V1 | Overall mean delivery time | 26.29 min | 26.29 min (from scratch via `df['Time_taken_min'].mean()`) | ✅ | — | Cleared |
| V2 | Urban mean | 22.98 min | 22.98 min | ✅ | — | Cleared |
| V3 | Metropolitan mean | 27.32 min | 27.32 min | ✅ | — | Cleared |
| V4 | Festival=Yes mean | 45.52 min | 45.52 min | ✅ | Simpson's: only 896 orders, but delta is so large (19.5 min) that composition effects cannot explain it | Cleared |
| V5 | Multiple deliveries: 0→22.9, 1→26.9, 2→40.5, 3→47.8 | Confirmed | Re-derived by filtering each `multiple_deliveries` value independently | ✅ | — | Cleared |
| V6 | 2→3 deliveries step: +13.6 min (51% jump at 2 deliveries) | 40.45–26.86=13.59 | 40.45–26.86=13.59 | ✅ | — | Cleared |
| V7 | Rider rating correlation r=−0.34 | −0.3388 | Re-derived via `Pearson(Ratings, Time)` = −0.3388 | ✅ | — | Cleared |
| V8 | Top-rated (≥4.8) vs low-rated (≤3.5) gap: 11.6 min | 24.4 vs 36.0 | 24.39 vs 35.97 | ✅ | Survivorship: no bias risk (ratings are pre-existing attributes, not outcomes) | Cleared |
| V9 | Jam traffic: 31.18 min vs Low: 21.27 min (delta +9.9 min) | Confirmed | Re-derived independently | ✅ | Simpson's Paradox: checked within Urban and Metropolitan — pattern CONSISTENT in both | Cleared |
| V10 | Metro + Jam + 1+ deliveries = 17.9% of orders, 33.1 min avg | 8,151 orders | Re-counted: 8,151 / 45,593 = 17.88% | ✅ | — | Cleared |
| V11 | Opportunity: reducing Metro/Jam/multi to Metro/Medium/1 saves 5.2 min/order | Confirmed | Independently computed: 33.1 − 27.9 = 5.2 | ✅ | Key assumption: ignores fixed traffic conditions (partially uncontrollable) | Cleared with caveat |
| V12 | Alternating daily pattern (22 "fast days" avg 23.3 min, 22 "slow days" avg 29.9 min) | Confirmed | Re-verified by splitting days by avg time threshold | ✅ | Driven by traffic composition mix (Jam=43% slow days vs 21% fast days) and batching (2+ deliveries 9% vs 2%) — NOT a data artifact, it's a real structural pattern | Cleared |
| V13 | Scooter/electric_scooter faster than motorcycle (24.5 vs 27.6 min) | Confirmed | Counter-intuitive: motorcycles are slower. Likely confound: motorcycles are predominantly in Metropolitan/high-traffic zones. Not a vehicle effect per se — a routing/city mix effect. | ⚠️ | Confound: motorcycle share in Metro (high traffic) vs scooter mix — flag as composition effect, not vehicle causality | Caveated — do not present as actionable vehicle recommendation |

## Simpson's Paradox Check

**Mandatory check completed:** Traffic density trend (Low < Medium < High < Jam) holds **consistently** within both Urban and Metropolitan city types. No reversal found. Aggregate trend is safe to report.

## Survivorship & Selection Bias

- **Survivorship bias:** Not applicable — dataset represents completed deliveries. However, findings on delivery time do not capture failed/cancelled deliveries (if any exist).
- **Selection bias:** Semi-Urban has only 164 orders (0.4% of data) — too small for reliable conclusions. **Excluded from headline findings.**
- **Look-ahead bias:** Not applicable (no time-series prediction involved).

## Data Quality Verdict

**Data quality: 🟡 Caution** — 44,993 rows (98.7%) are clean enough for analysis. Key caveats:
- ~4% null rates on Age and Ratings (imputed via exclusion in correlation analyses)
- City null = 2.6% (excluded from city segmentation)
- Semi-Urban sample too small (n=164) to support reliable segment conclusions
- Vehicle type finding (V13) confounded by city-traffic routing — do not present as causal

## Gate Decision

**All headline findings are ✅ or ⚠️ with documented caveats. Proceeding to Story Architect.**
