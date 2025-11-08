# Clinical Sample Validation Plan

## Executive Summary

**Objective:** Validate 12,100 potential clinical samples to identify real patient data (not cell lines) with treatment response labels.

**Current Status:**
- 12,100 candidate samples identified via regex detection from Refine.bio metadata (actual: 12,100 samples × 1,063 columns)
- 1,386 response-related columns detected (from response_column_shortlist_from_full_lazy.parquet)
- ✅ **Step 1 Complete:** Deduplicated against existing 11,735 clinical samples → **9,201 novel samples to validate**
- **Target:** Identify ~5,000 novel, validated clinical samples from the 9,201 candidates

**Definition of Done:** For each unique experiment ID (GSE), determine:
1. Are samples from real patients (not cell lines)?
2. Do samples have valid response labels?
3. Can response labels be mapped to binary (0 = non-response, 1 = response)?

---

## Data Files Overview

### Input Files (in `data/`)

1. **potential_clin_data.csv** (12,100 samples × 1,063 columns)
   - Subset of Refine.bio metadata where response columns have non-null values
   - Sample IDs: `refinebio_accession_code` (format: `GSMXXXXXX`)
   - Experiment IDs: `experiment_accession` (format: `GSEXXXXX`)
   - ⚠️ **Note:** Contains mixed-type columns; use `ignore_errors=True` and `infer_schema_length=10000` when loading with Polars

2. **clin_obs.csv** (12,380 rows × 13 columns, contains 11,735 unique samples)
   - Already curated clinical data
   - Use `sample_id` column to filter duplicates
   - **Actual overlap:** 2,899 samples (24% of potential_clin_data)
   - **Novel samples after deduplication:** 9,201

3. **response_column_shortlist_from_full_lazy.parquet** (1,386 response columns × 8 columns)
   - Columns identified as containing response data
   - Schema: `colname`, `dtype`, `n_non_null`, `n_unique`, `is_binary_numeric`, `is_response_like`, `coverage`, `tokens_sample`
   - Coverage = fraction of values matching known response terms

4. **experiment_data.csv** (91 experiments × 13 columns)
   - Metadata per GSE experiment
   - Columns: `series` (GSE ID), `title`, `summary`, `overall_design`, `n_samples`, `platform`
   - Use for joining experiment-level context

### Output Files (to create)

1. **validated_experiments_summary.csv**
   - Prioritized list of experiments for manual validation
   - Sorted by likelihood of being real patient samples

2. **sample_scores.parquet**
   - Individual sample-level scores and flags
   - Includes primary_sample_score, cell_line_score, net_score

3. **high_confidence_samples.csv**
   - Filtered samples with net_score ≥ threshold
   - Ready for response label extraction

---

## Implementation Steps

**Progress Tracker:**
- ✅ Step 1: Data Loading & Deduplication (COMPLETE)
- ✅ Step 2: Define Column Indicator Mappings (COMPLETE)
- ✅ Step 2.5: EDA - Analyze Identified Columns (COMPLETE)
- ⏳ Step 3: Column Content Analysis & Scoring (PENDING)
- ⏳ Step 4: Group by Experiment ID & Join Metadata (PENDING)
- ⏳ Step 5: Map Response Columns (PENDING)
- ⏳ Step 6: Generate Prioritized Summary Report (PENDING)
- ⏳ Step 7: Export Results (PENDING)

**Current Status:** EDA complete with 47 columns analyzed. Ready for Step 3 implementation with validated indicators.

---

### Step 1: Data Loading & Deduplication ✅

**Status:** COMPLETE (implemented in `nbs/verify_clin.ipynb` cells 1-3)

**Goal:** Load all data and remove samples already in clinical database

```python
import polars as pl
import pandas as pd
from pathlib import Path

# Paths
data_dir = Path('../data')

# Load data (with error handling for mixed-type columns)
potential_clin = pl.read_csv(
    data_dir / 'potential_clin_data.csv',
    ignore_errors=True,
    infer_schema_length=10000
)
clin_obs = pd.read_csv(data_dir / 'clin_obs.csv')
response_shortlist = pl.read_parquet(data_dir / 'response_column_shortlist_from_full_lazy.parquet')
experiment_data = pd.read_csv(data_dir / 'experiment_data.csv')

# Get existing sample IDs
existing_ids = set(clin_obs['sample_id'].values)

# Filter out duplicates
novel_samples = potential_clin.filter(
    ~pl.col('refinebio_accession_code').is_in(existing_ids)
)

print(f"Original samples: {len(potential_clin):,}")
print(f"Existing clinical samples: {len(existing_ids):,}")
print(f"Novel samples to validate: {len(novel_samples):,}")
```

**Actual Output:**
- Original samples: **12,100**
- Existing clinical samples: **11,735**
- Novel samples to validate: **9,201**
- Duplicate samples removed: **2,899**

---

### Step 2: Define Column Indicator Mappings ✅

**Status:** COMPLETE (implemented in `nbs/verify_clin.ipynb` cells 4-7)

**Goal:** Create regex patterns to identify cell line vs primary sample indicators

#### Cell Line Indicators (Negative Signals)

**Column name patterns:**
```python
import re

CELL_LINE_COLUMN_PATTERNS = [
    r'.*cell[_\s]line.*',
    r'.*celltype.*',
    r'.*cell\s+type.*',
]

# Compile regex
cell_line_col_regex = re.compile('|'.join(CELL_LINE_COLUMN_PATTERNS), re.IGNORECASE)
```

**Value patterns (known cell line names):**
```python
CELL_LINE_NAMES = {
    'MCF7', 'MCF-7', 'HELA', 'HeLa', 'K562', 'A549', 'HEK293', 'HEK-293',
    'JURKAT', 'U937', 'THP1', 'THP-1', 'CACO2', 'Caco-2', 'HCT116',
    'SW480', 'DLD1', 'DLD-1', 'RKO', 'MDA-MB-231', 'T47D', 'BT474',
    'SKBR3', 'ZR-75-1', 'PC3', 'LNCaP', 'DU145', 'H1299', 'H460',
    'NCI-H', 'HUVEC', 'NIH3T3', 'COS7', 'CHO', 'BHK', 'MDCK',
    # Add more as needed
}

def is_cell_line_value(value):
    """Check if value contains cell line name"""
    if pd.isna(value):
        return False
    value_upper = str(value).upper()
    return any(name.upper() in value_upper for name in CELL_LINE_NAMES)
```

**Key columns to check:**
- `refinebio_cell_line`
- `characteristics_ch1_cell line`
- `characteristics_ch1_celltype`
- `characteristics_ch1_cell type`
- Any column matching cell_line_col_regex

#### Primary Sample Indicators (Positive Signals)

**Column name patterns:**
```python
PRIMARY_SAMPLE_PATTERNS = {
    'age': r'.*\bage\b.*',
    'sex': r'.*\b(sex|gender)\b.*',
    'patient': r'.*\bpatient\b.*',
    'subject': r'.*\bsubject\b.*',
    'stage': r'.*\b(stage|grade)\b.*',
    'tissue': r'.*\b(tissue|biopsy|specimen)\b.*',
}

# Compile each pattern
primary_sample_regex = {
    key: re.compile(pattern, re.IGNORECASE)
    for key, pattern in PRIMARY_SAMPLE_PATTERNS.items()
}
```

**Age-specific logic:**
- Non-null numeric age (especially if < 120 years) → strong primary sample indicator
- Age values like "cell line" → cell line indicator

**Key columns to check:**
- `refinebio_age`
- `refinebio_sex`
- `characteristics_ch1_Age*` (many variants)
- `characteristics_ch1_Sex*`
- `characteristics_ch1_Gender*`
- `characteristics_ch1_*stage*`
- `characteristics_ch1_*tissue*`

#### Implementation Results

**Patterns Created:**
- 3 cell line column regex patterns
- 57 known cell line names for value matching
- 6 primary sample indicator patterns (age, sex, patient, subject, stage, tissue)
- 2 helper functions: `is_cell_line_value()` and `parse_age_value()`

**Columns Found in Data (9,201 novel samples):**
- **Cell line indicators:** 4 columns
  - `refinebio_cell_line`
  - `characteristics_ch1_cell line`
  - `characteristics_ch1_cell type`
  - `characteristics_ch1_celltype`

- **Primary sample indicators:**
  - Age: 4 columns (e.g., `characteristics_ch1_baseline age (years)`)
  - Sex: 0 columns
  - Patient: 3 columns (e.g., `characteristics_ch1_age of patient at diagnosis (years)`)
  - Subject: 0 columns
  - Stage: 32 columns (e.g., `characteristics_ch1_AJCC Stage`)
  - Tissue: 4 columns (e.g., `characteristics_ch1_primary tissue`)

**Helper Functions Tested:**
- `is_cell_line_value()`: Successfully detects cell line names in values
- `parse_age_value()`: Handles numeric ages, ranges (e.g., "60-70"), and text formats (e.g., "75 years")

---

### Step 2.5: EDA - Analyze Identified Columns ✅

**Status:** COMPLETE (implemented in `nbs/verify_clin.ipynb` cells 17-19)

**Goal:** Generate detailed report of all identified columns to validate indicators and flag misleading columns

**Implementation:**
```python
def analyze_column(col_name, df):
    """Generate EDA report for a single column"""
    col_data = df[col_name]

    # Count nulls
    n_null = col_data.null_count()
    n_total = len(df)
    pct_null = (n_null / n_total) * 100

    # Get unique values
    n_unique = col_data.n_unique()

    # Get top 10 value counts
    value_counts = (
        col_data
        .value_counts()
        .sort('count', descending=True)
        .limit(10)
    )

    return {
        'column': col_name,
        'n_null': n_null,
        'pct_null': pct_null,
        'n_unique': n_unique,
        'top_values': value_counts
    }

# Analyze all 47 identified columns
column_reports = []
for col in sorted(all_identified_cols):
    report = analyze_column(col, novel_samples)
    column_reports.append(report)
```

**Key Findings:**

**Columns with HIGH null rates (>99%, likely not useful):**
- `characteristics_ch1_bmn grade` (100% null)
- `characteristics_ch1_bmn.grade` (100% null)
- `characteristics_ch1_clinical stage` (100% null)
- `characteristics_ch1_clinical t stage` (100% null)
- `characteristics_ch1_figo stage` (100% null)
- `characteristics_ch1_prechemo t stage` (100% null)
- `characteristics_ch1_tumor grade (g1 - well differentiated...)` (100% null)
- `characteristics_ch1_primary tissue` (100.0% null, only 1 value)

**Cell line indicators (good signals):**
- `refinebio_cell_line`: 171 non-null values (1.9%), 34 unique cell lines
  - Top: rt112 (24), hcc38 (18), mda-mb-468 (17)
- `characteristics_ch1_cell line`: 171 non-null values (1.9%), 34 unique
  - Matches refinebio_cell_line (duplicate data)
- `characteristics_ch1_cell type`: 1,078 non-null values (11.7%), 27 unique
  - Top: lymphoblasts (131), PBMC (116), primary hepatocyte (116), primary cell (111)
  - **IMPORTANT**: Contains mix of cell lines AND primary cells!
- `characteristics_ch1_celltype`: 26 non-null values (0.3%)
  - All say "Ductal carcinoma in situ" (clinical diagnosis, NOT cell type)

**Age columns (strong primary sample indicators):**
- `characteristics_ch1_patient age (years)`: 202 non-null (2.2%), all unique numeric ages
  - Clean, high-precision ages (e.g., 52.052, 60.9391)
- `characteristics_ch1_baseline age (years)`: 22 non-null (0.2%)
  - Ages: 56-87 years
- `characteristics_ch1_gest age at delivery (weeks)`: 323 non-null (3.5%)
  - Gestational ages: 33-41 weeks (pregnancy data)
- `characteristics_ch1_gest age at sampling (weeks)`: 323 non-null (3.5%)
  - Gestational ages: 18-32 weeks

**Stage columns (strong clinical indicators):**
- `characteristics_ch1_sbr grade`: 504 non-null (5.5%), good signal
  - Values: Grade 1 (87), Grade 2 (175), Grade 3 (242)
- `characteristics_ch1_histological grade`: 196 non-null (2.1%)
  - Values: Grade 1-3
- `characteristics_ch1_tumor stage`: 223 non-null (2.4%)
  - Values: 1a, 1b, 2a, 2b, 3a, 3b, 4
- `characteristics_ch1_pathological stage`: 212 non-null (2.3%)
  - Values: IA, IB, II
- Most other stage columns have <100 non-null values (1%)

**Misleading columns (flagged for review):**
- `characteristics_ch1_celltype`: Actually contains clinical diagnosis, not cell type
- `characteristics_ch1_cell type`: Mix of cell lines (lymphoblasts) AND primary cells
- Several date columns stored as Excel serial numbers (e.g., patient death dates)

**Recommendations for Step 3:**
1. **Skip 100% null columns** in scoring logic
2. **Carefully handle `cell type` column**: Contains both cell lines and primary cells
3. **Prioritize `patient age` column**: Cleanest age data with 202 samples
4. **Use stage columns as strong indicators**: 504 samples have SBR grade (5.5% coverage)
5. **Consider gestational age separately**: 323 samples are pregnancy-related (separate cohort)

---

### Step 3: Column Content Analysis & Scoring

**Goal:** Create sample-level scores based on indicator counts

```python
def score_sample(row, all_columns):
    """
    Score a single sample row

    Returns:
        (primary_score, cell_line_score, net_score, indicators_found)
    """
    primary_score = 0
    cell_line_score = 0
    indicators = {
        'age_cols': [],
        'sex_cols': [],
        'patient_cols': [],
        'stage_cols': [],
        'tissue_cols': [],
        'cell_line_cols': [],
        'cell_line_values': []
    }

    # Check each column
    for col in all_columns:
        value = row[col]

        # Skip null values
        if pd.isna(value):
            continue

        # Check cell line indicators
        if cell_line_col_regex.search(col):
            cell_line_score += 1
            indicators['cell_line_cols'].append(col)

        if is_cell_line_value(value):
            cell_line_score += 2  # Stronger signal
            indicators['cell_line_values'].append(f"{col}={value}")

        # Check primary sample indicators
        for indicator_type, regex in primary_sample_regex.items():
            if regex.search(col):
                primary_score += 1
                indicators[f'{indicator_type}_cols'].append(col)

                # Bonus for age with numeric value
                if indicator_type == 'age':
                    try:
                        age_val = float(str(value).replace(' ', ''))
                        if 0 < age_val < 120:
                            primary_score += 2  # Strong indicator
                    except:
                        pass

    net_score = primary_score - cell_line_score

    return primary_score, cell_line_score, net_score, indicators

# Apply to dataframe
scores = []
for idx, row in novel_samples.iter_rows(named=True):
    p_score, c_score, n_score, indicators = score_sample(row, novel_samples.columns)
    scores.append({
        'refinebio_accession_code': row['refinebio_accession_code'],
        'experiment_accession': row['experiment_accession'],
        'primary_score': p_score,
        'cell_line_score': c_score,
        'net_score': n_score,
        'indicators': str(indicators)
    })

scores_df = pl.DataFrame(scores)
```

**Scoring Logic:**
- Primary sample score: +1 per indicator column, +2 bonus for valid age
- Cell line score: +1 per cell line column name, +2 per cell line value match
- Net score: primary_score - cell_line_score
- **High confidence threshold:** net_score ≥ 2

---

### Step 4: Group by Experiment ID & Join Metadata

**Goal:** Aggregate scores by experiment and add context

```python
# Join scores with original data
scored_samples = novel_samples.join(
    scores_df,
    on=['refinebio_accession_code', 'experiment_accession']
)

# Group by experiment
experiment_summary = scored_samples.group_by('experiment_accession').agg([
    pl.count('refinebio_accession_code').alias('n_samples'),
    pl.mean('primary_score').alias('avg_primary_score'),
    pl.mean('cell_line_score').alias('avg_cell_line_score'),
    pl.mean('net_score').alias('avg_net_score'),
    pl.max('net_score').alias('max_net_score'),
    pl.min('net_score').alias('min_net_score'),
])

# Join with experiment metadata
experiment_summary = experiment_summary.join(
    pl.from_pandas(experiment_data),
    left_on='experiment_accession',
    right_on='series',
    how='left'
)
```

---

### Step 5: Map Response Columns

**Goal:** Identify which response columns have data for each experiment

```python
# Get response column names from shortlist
response_cols = response_shortlist['colname'].to_list()

# Filter to columns that exist in our data
available_response_cols = [
    col for col in response_cols
    if col in scored_samples.columns
]

# For each experiment, find which response columns have data
response_mapping = []

for gse in scored_samples['experiment_accession'].unique():
    exp_samples = scored_samples.filter(
        pl.col('experiment_accession') == gse
    )

    response_cols_with_data = []
    response_coverage = []

    for col in available_response_cols:
        non_null_count = exp_samples[col].is_not_null().sum()
        if non_null_count > 0:
            coverage = non_null_count / len(exp_samples)
            response_cols_with_data.append(col)
            response_coverage.append(f"{col}:{coverage:.1%}")

    response_mapping.append({
        'experiment_accession': gse,
        'response_cols': ', '.join(response_cols_with_data),
        'response_coverage': ', '.join(response_coverage),
        'n_response_cols': len(response_cols_with_data),
        'avg_response_coverage': (
            sum(float(c.split(':')[1].strip('%'))/100
                for c in response_coverage) / len(response_coverage)
            if response_coverage else 0
        )
    })

response_map_df = pl.DataFrame(response_mapping)

# Join with experiment summary
final_summary = experiment_summary.join(
    response_map_df,
    on='experiment_accession',
    how='left'
)
```

**Response Column Types to Track:**
- PCR/RD columns (pathological complete response / residual disease)
- CR/PR/SD/PD columns (complete/partial response, stable/progressive disease)
- Binary 0/1 columns
- RCB columns (residual cancer burden)
- Custom response categories

---

### Step 6: Generate Prioritized Summary Report

**Goal:** Create final ranked list for manual validation

```python
# Add GEO URL for easy lookup
final_summary = final_summary.with_columns(
    pl.format(
        'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc={}',
        pl.col('experiment_accession')
    ).alias('geo_url')
)

# Sort by priority
final_summary = final_summary.sort(
    ['avg_net_score', 'avg_response_coverage', 'n_samples'],
    descending=[True, True, True]
)

# Add priority flags
final_summary = final_summary.with_columns([
    (pl.col('avg_net_score') >= 2).alias('high_confidence_primary'),
    (pl.col('avg_cell_line_score') == 0).alias('no_cell_line_indicators'),
    (pl.col('avg_response_coverage') >= 0.5).alias('high_response_coverage'),
])

# Create validation priority
final_summary = final_summary.with_columns(
    (
        pl.col('high_confidence_primary').cast(pl.Int8) * 4 +
        pl.col('no_cell_line_indicators').cast(pl.Int8) * 2 +
        pl.col('high_response_coverage').cast(pl.Int8) * 1
    ).alias('validation_priority')
)

# Select key columns for display
display_cols = [
    'experiment_accession',
    'validation_priority',
    'n_samples',
    'avg_net_score',
    'avg_primary_score',
    'avg_cell_line_score',
    'n_response_cols',
    'avg_response_coverage',
    'response_cols',
    'title',
    'geo_url'
]

final_summary_display = final_summary.select(display_cols)

# Print top candidates
print("\n=== TOP 20 EXPERIMENTS FOR MANUAL VALIDATION ===\n")
print(final_summary_display.head(20))

# Print summary statistics
print(f"\n=== SUMMARY STATISTICS ===")
print(f"Total experiments: {len(final_summary)}")
print(f"High confidence primary (net_score ≥ 2): {final_summary['high_confidence_primary'].sum()}")
print(f"No cell line indicators: {final_summary['no_cell_line_indicators'].sum()}")
print(f"High response coverage (≥50%): {final_summary['high_response_coverage'].sum()}")
print(f"Priority 7 (all flags): {(final_summary['validation_priority'] == 7).sum()}")
print(f"Priority 6 or 7: {(final_summary['validation_priority'] >= 6).sum()}")
```

**Validation Priority Score (0-7):**
- +4: High confidence primary (avg_net_score ≥ 2)
- +2: No cell line indicators
- +1: High response coverage (≥50%)

**Priority 7:** All three flags → Start manual validation here
**Priority 6:** Primary + no cell lines OR Primary + high response
**Priority 4-5:** Primary only OR response only
**Priority 0-3:** Lower confidence, validate if needed

---

### Step 7: Export Results

**Goal:** Save all outputs for downstream processing

```python
# 1. Experiment summary (for manual validation)
final_summary.write_csv(data_dir / 'validated_experiments_summary.csv')
print(f"✅ Saved: validated_experiments_summary.csv ({len(final_summary)} experiments)")

# 2. Sample scores (all novel samples)
scored_samples.write_parquet(data_dir / 'sample_scores.parquet')
print(f"✅ Saved: sample_scores.parquet ({len(scored_samples)} samples)")

# 3. High confidence samples (net_score ≥ 2)
high_confidence = scored_samples.filter(pl.col('net_score') >= 2)
high_confidence.write_csv(data_dir / 'high_confidence_samples.csv')
print(f"✅ Saved: high_confidence_samples.csv ({len(high_confidence)} samples)")

# 4. Response column mapping (for label extraction)
response_map_df.write_parquet(data_dir / 'response_column_mapping.parquet')
print(f"✅ Saved: response_column_mapping.parquet ({len(response_map_df)} experiments)")

print("\n=== VALIDATION PIPELINE COMPLETE ===")
print(f"Next step: Manually validate top {(final_summary['validation_priority'] >= 6).sum()} experiments")
print("Use the geo_url column to inspect experiment details on NCBI GEO")
```

---

## Manual Validation Checklist

For each high-priority experiment (validation_priority ≥ 6):

1. **Open GEO page** using `geo_url` from summary
2. **Check experiment type:**
   - [ ] Clinical trial / patient cohort study
   - [ ] Primary tissue samples (not cell lines)
   - [ ] Treatment intervention mentioned

3. **Verify sample sources:**
   - [ ] Patient biopsies / tissue samples
   - [ ] Age/sex demographics present
   - [ ] No cell line names in description

4. **Confirm response labels:**
   - [ ] Treatment outcome mentioned (response, remission, progression)
   - [ ] Response assessment method specified (RECIST, PCR, clinical criteria)
   - [ ] Labels can map to binary (response vs non-response)

5. **Flag for inclusion:**
   - [ ] ✅ VALIDATED: Real patients + valid response labels
   - [ ] ⚠️ UNCERTAIN: Need additional review
   - [ ] ❌ REJECTED: Cell lines or no response data

---

## Expected Outcomes

### Quantitative Targets
- **~50-100 validated experiments** (out of ~300-500 total)
- **~3,000-5,000 validated clinical samples**
- **80-90% reduction in manual review effort** through automated scoring

### Quality Metrics
- **Precision:** >90% of priority 7 experiments should be valid
- **Recall:** Capture >80% of true clinical experiments in top 100
- **Response coverage:** >70% of validated samples have extractable response labels

### Next Steps After Validation
1. Map response values to binary labels (0/1)
2. Extract gene expression data from Refine.bio zarr
3. Merge with existing clinical dataset
4. Quality control: check for batch effects, outliers
5. Final dataset ready for ML model training

---

## Troubleshooting & Notes

### Common Issues

**Issue:** High cell_line_score for known patient samples
- **Cause:** Columns like `% tumor cells` contain "cell" keyword
- **Solution:** Refine regex to exclude `tumor_cells`, `blood_cells`, etc.

**Issue:** Age values like "60-70" or "60 years"
- **Cause:** Non-numeric age formats
- **Solution:** Add parsing logic for age ranges and text formats

**Issue:** Response columns with cryptic values
- **Cause:** Non-standard response coding
- **Solution:** Manual inspection of `tokens_sample` in response_shortlist to understand encoding

### Column Name Variations to Watch

**Age columns:**
- `age (years)`, `age (y)`, `age at diagnosis`, `age at surgery`, `age.at.diagnosis`

**Sex/Gender columns:**
- `sex`, `Sex`, `gender`, `Gender`, `sex of patient`

**Stage/Grade:**
- `AJCC Stage`, `TNM Stage`, `Ann Arbor Stage`, `tumor grade`, `histological grade`

**Response columns:**
- `pcr`, `PCR`, `pathological response`, `clinical response`, `RECIST`, `response to treatment`

### Performance Notes
- Lazy evaluation recommended for large dataframes
- Use Polars for speed (10-50x faster than Pandas for this workload)
- Expected runtime: 2-5 minutes for full pipeline on 12K samples

---

## Code Implementation Template

**File:** `nbs/verify_clin.ipynb`

**Suggested cell structure:**

1. **Cell 1:** Imports and setup
2. **Cell 2:** Load data
3. **Cell 3:** Deduplicate against clin_obs
4. **Cell 4:** Define indicator patterns and functions
5. **Cell 5:** Score samples
6. **Cell 6:** Group by experiment
7. **Cell 7:** Map response columns
8. **Cell 8:** Generate summary report
9. **Cell 9:** Export results
10. **Cell 10:** Display top candidates for validation

Each step should be modular and testable independently.

---

## Version History

- **v1.0** (2025-10-10): Initial validation plan
- **v1.1** (2025-10-10): Updated with Step 1 actual results
  - Confirmed 9,201 novel samples after deduplication
  - Updated file dimensions based on actual data loads
  - Documented CSV loading parameters for mixed-type columns
  - Marked Step 1 as complete in `nbs/verify_clin.ipynb`
- **v1.2** (2025-10-10): Updated with Step 2 actual results
  - Implemented cell line and primary sample indicator patterns
  - Created 57 cell line names for matching
  - Defined 6 primary sample indicator types (age, sex, patient, subject, stage, tissue)
  - Built helper functions for cell line value detection and age parsing
  - Found 4 cell line columns and 43 primary sample indicator columns in data
  - Marked Step 2 as complete in `nbs/verify_clin.ipynb` (cells 4-7)
- **v1.3** (2025-10-12): Added Step 2.5 EDA analysis
  - Analyzed all 47 identified columns (actual count after deduplication)
  - Generated detailed reports: null counts, unique values, top 10 value frequencies
  - Flagged 8 columns with 100% null rates (should skip in scoring)
  - Identified misleading columns (e.g., `celltype` contains diagnosis, not cell type)
  - Found strongest indicators: `patient age` (202 samples), `sbr grade` (504 samples)
  - Discovered pregnancy cohort: 323 samples with gestational age data
  - Marked Step 2.5 as complete in `nbs/verify_clin.ipynb` (cells 17-19)
- Future: Add automated response label mapping logic
- Future: Integrate with expression data pipeline
