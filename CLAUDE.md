# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository focuses on identifying and validating clinical RNA samples from NCBI GEO via the Refine.bio metadata. The goal is to find ~5,000 new human clinical samples with:
1. RNA expression data from real patients (not cell lines)
2. Treatment response labels (e.g., complete response, partial response, progressive disease)

**Why this matters:** Cancer treatment often involves trial-and-error with expensive therapies. Predicting drug response from gene expression could reduce patient exposure to ineffective treatments and accelerate personalized medicine. The bottleneck is **paired data** (RNA + treatment + response). Only ~1% of 1M available RNA samples have this pairing.

**Current status**: 7,639 potential samples identified via regex/heuristics from 6,700 metadata columns. Of these, 5,086 are NOT in the existing clinical data store (clin_obs.csv).

### About Refine.bio

[Refine.bio](https://www.refine.bio/) uniformly processed ~400K RNA samples from NCBI GEO with SCAN + quantile normalization. They provide structured metadata (universal `refinebio_*` columns + union of all original GEO columns) queryable as a single table, plus 120GB normalized expression TSV (converted to zarr format in a separate pipeline).

## Data Architecture

### Primary Data Files (in `data/`)

- **metadata_HOMO_SAPIENS.parquet** (71 MB, originally 3 GB TSV)
  - Full Refine.bio human sample metadata with 6,700+ columns
  - **DO NOT load into memory without lazy scanning** (uses ~40GB RAM when fully loaded)
  - Use `pl.scan_parquet()` for lazy operations
  - Git LFS required to access this file

- **potential_clin_data.csv**
  - 7,639 samples × 662 columns
  - Subset of metadata where response-related columns have non-null values
  - Sample IDs format: `GSMXXXXX`, Experiment IDs: `GSEXXXX`

- **clin_obs.csv**
  - 12,380 existing clinical samples (already curated)
  - Use `sample_id` column to filter out duplicates

- **experiment_data.csv**
  - Metadata per experiment (GSE accession)
  - Contains: title, summary, overall_design for each experiment

- **response_column_shortlist.parquet**
  - 85 columns identified as likely containing response data
  - Includes coverage scores, unique value counts, and token samples

### Sample Identification

- **Sample IDs**: GEO sample accessions in format `GSMXXXXX` (e.g., `GSM1186556`)
- **Experiment IDs**: GEO series accessions in format `GSEXXXX` (e.g., `GSE48905`)
- Look up experiments at: `https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi` (search in geo_accession box)

## Analysis Workflow

The repository implements a pipeline to detect potential clinical samples from RNA expression metadata:

1. **Data conversion** (`nbs/RB_tsv_to_parquet.ipynb`):
   - Converts 3GB TSV → 71MB Parquet using Polars
   - Handles schema inference with 420K row scan
   - Fixes malformed values (e.g., barcode overflow: `5503934202250110435328`)

2. **Response column detection** (`nbs/detect_potential_clin.ipynb`):
   - Uses regex patterns on column names and values to identify response-related fields
   - Looks for terms like: PCR, CR, PR, SD, PD, response, remission, progression, etc.
   - Filters to 414 candidate columns → 85 high-confidence columns
   - Creates `potential_clin_data.csv` with 7,639 samples

3. **Validation** (`nbs/veriify_clin.ipynb`):
   - Manual inspection workflow to verify samples are:
     - From real patients (not cell lines)
     - Have valid response labels

## Setup

Install dependencies:
```bash
pip install -r requirements.txt
```

Dependencies (see `requirements.txt`):
- `polars` - Memory-efficient dataframe operations with lazy evaluation
- `pandas`, `numpy` - Traditional data processing
- `pyarrow` - Parquet I/O
- `tqdm` - Progress bars

## Working with Notebooks

All analysis is in Jupyter notebooks under `nbs/`:
- Use Polars (not Pandas) for large data operations
- Always use lazy evaluation (`pl.scan_parquet()`) for metadata_HOMO_SAPIENS.parquet
- Import structure:
  ```python
  import polars as pl
  import pandas as pd
  from pathlib import Path
  from tqdm import tqdm
  ```

## Key Technical Details

### Response Label Detection
The codebase includes sophisticated regex-based detection for clinical response values:
- **Value tokens**: PCR, RD, CR, NR, R, SD, PPR, PD, VGPR, PR, etc.
- **Column name terms**: RESPONSE, REMISSION, PROGRESSIVE_DISEASE, BURDEN, etc.
- **Binary indicators**: 0/1, YES/NO, TRUE/FALSE

See `nbs/detect_potential_clin.ipynb` cells for the full token lists and normalization logic.

### Memory Management
- Metadata TSV requires ~60GB RAM to read entirely
- Parquet with lazy scanning is the only practical approach
- All notebooks use `low_memory=True` for CSV operations

## Validation Criteria

For each unique experiment ID (GSE), determine:
1. **Not cell lines**: Look for columns like `age`, `tissue`, patient identifiers
2. **Has response label**: Check if response columns contain recognized clinical terms
3. **Definition of Done**: Binary response label (0 = non-response, 1 = response)

Suggested approach from README:
- Use `experiment_accession` column to join with experiment metadata
- Flag samples with `age` values as likely human
- Check for contradictions between columns
- Manually inspect experiment descriptions on GEO for final validation

## Important Notes

- **No Python scripts**: All code is in Jupyter notebooks
- Sample overlap check: 5,086 of 7,639 samples are new (not in clin_obs.csv)
- Response labels must map to binary: 0 (non-response) or 1 (response)
- note that this repo is part of a portfolio, showing how i use data to create valuable insights, and technichal ability