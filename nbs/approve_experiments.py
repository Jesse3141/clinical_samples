import polars as pl
from pathlib import Path

data_dir = Path('../data')

score_df = pl.read_csv(data_dir / 'clean_score_df.csv')
novel_samples = pl.read_csv(data_dir / 'novel_samples.csv', 
    ignore_errors=False,
    infer_schema_length=14000)
candidate_experiments = pl.read_csv(data_dir / 'candidate_experiments.csv')

text_search_cols = ['series_title', 'series_summary', 'series_overall_design', 'refinebio_title', 'refinebio_description', 
    'refinebio_source_name', 'refinebio_subject', 'refinebio_age', 'refinebio_cell_line', 'refinebio_disease', 
    'refinebio_disease_stage', 'refinebio_sex', 'refinebio_source_database', 'refinebio_specimen_part', 
    'refinebio_treatment', 'description', 'extraction_protocol_ch1', 'growth_protocol_ch1', 'treatment_protocol_ch1']

def sample_summary(accession):
    sample_data = novel_samples.filter(pl.col('refinebio_accession_code') == accession)
    sample_scores = score_df.filter(pl.col('refinebio_accession_code') == accession)
    for col in sample_scores.columns:
        if col not in ['refinebio_accession_code', 'experiment_accession']:
            score = sample_scores.select(pl.col(col)).to_series()[0]
            if score != 0: print(f"{col}: {score}")
    for col in text_search_cols:
        if col in sample_data.columns:
            value = sample_data.select(pl.col(col)).to_series()[0]
            if value is not None and str(value).strip() != '': print(f"{col}: {value}")

approved_experiments = []
total_samples = 0

for i in range(len(candidate_experiments)):
    exp = candidate_experiments[i]
    exp_id = exp['experiment_accession'][0]
    n_samples = exp['n_samples'][0]
    
    exp_samples = score_df.filter(pl.col('experiment_accession') == exp_id)
    sample_ids = exp_samples['refinebio_accession_code'].to_list()[:1]
    
    print(f"\n{'='*80}")
    print(f"Experiment {i+1}/{len(candidate_experiments)}: {exp_id}")
    print(f"Samples in experiment: {n_samples}")
    print(f"Samples approved so far: {total_samples}/1000")
    print(f"{'='*80}\n")
    
    for j,sid in enumerate(sample_ids,1):
        print(f"\n--- Sample {j}/2: {sid} ---")
        sample_summary(sid)
    
    response = input("\n[y]es / [n]o / [q]uit: ").strip().lower()
    
    if response == 'q': break
    if response == 'y':
        approved_experiments.append(exp_id)
        total_samples += n_samples
        if total_samples >= 1000: break

print(f"\n\nApproved {len(approved_experiments)} experiments with {total_samples} total samples")

approved_df = pl.DataFrame({'experiment_accession': approved_experiments})
approved_df.write_csv(data_dir / 'approved_experiments.csv')
print(f"Saved to {data_dir / 'approved_experiments.csv'}")
