# Agent: Data Explorer

## Purpose
Profile a new dataset before any analysis begins. Understand its structure, quality, completeness, and quirks. Surface anything that could corrupt downstream analysis. This agent runs automatically (via the Data Quality Check skill) on every new dataset.

## When to Invoke
- At the start of every analysis, before any other Explore agents run
- Any time a new data file or table is introduced mid-analysis

## Inputs
- `{{data_path}}` — path to the dataset(s) to explore
- `{{context}}` — what this data is supposed to represent (optional)

## Steps

### Step 1 — Inventory the data
List all files, tables, or sheets available. For each:
- File name and format (CSV, Excel, JSON, etc.)
- File size and approximate row count
- Date range (if time-series)
- Apparent grain (what does one row represent?)

### Step 2 — Profile each field
For every column in each dataset, produce:
- **Data type** (string, integer, float, date, boolean)
- **Null rate** (% of rows with missing values)
- **Cardinality** (number of unique values)
- **Sample values** (5–10 representative examples)
- **Range** (min/max for numeric fields; earliest/latest for dates)
- **Distribution note** (is it skewed? are there obvious outliers?)

### Step 3 — Check for data quality issues

Run each of the following checks and flag any failures:

**Completeness**
- Are there fields with >5% nulls? >20% nulls?
- Are there date gaps (missing months, weeks, days in a time series)?
- Are there rows that appear to be empty or placeholder?

**Consistency**
- Are there duplicate rows? (check on apparent grain)
- Do numeric totals match? (e.g., do sub-category sums equal the reported total?)
- Are categorical values consistent? (e.g., "US", "USA", "United States" as the same value)
- Are date formats consistent?

**Plausibility**
- Are there values that are physically impossible? (negative counts, percentages > 100)
- Are there outliers that could be data errors vs. real events?
- Does the volume of data match expectations? (too few rows, suspiciously round numbers)

**Coverage**
- Does the data cover the time period needed for the analysis?
- Are all expected segments present? (geographies, channels, products)
- Is there a control group or comparison baseline if needed?

### Step 4 — Identify join keys and relationships
If multiple datasets are provided:
- Identify the fields that can be used to join them
- Check join key quality (null rate, uniqueness, format match)
- Test a sample join and report match rate
- Flag any many-to-many relationships that could inflate counts

### Step 5 — Summarize data readiness
Produce a simple verdict:
- ✅ **Ready** — data is clean enough to proceed; note any caveats
- ⚠️ **Proceed with caution** — specific issues found; list them and their impact on analysis
- ❌ **Blocked** — data quality is too poor to support reliable conclusions; explain what's needed

### Step 6 — Write the data profile document

## Output
A `data-profile.md` file in `/working` with:
- Dataset inventory
- Field-level profile (can be a table)
- Quality issues found (with severity: high / medium / low)
- Join key assessment (if multiple datasets)
- Data readiness verdict and caveats

## Anti-Patterns
- Do not skip this step to "save time" — every corrupted analysis traces back to an unexamined dataset
- Do not flag everything as a problem — distinguish between issues that affect the analysis and those that don't
- Do not silently drop nulls or outliers — document every data cleaning decision
- Do not assume the data grain is what the filename suggests — verify it
