after  evaluating 40 outputs:

# conclusions:
1. PR as a collumn is a red herring. can be progresterone receptor status.
2. cancer score col > 1, or refine bio disease, or cancer text > 1
3. search sample metadata for drug or treatment names. neoadjuvant. chemo. etc. need to have a large source. 


# source: 
## evaluted:
=== TOP 40 EXPERIMENTS WITH RESPONSE DATA ===

1. GSE21653 (262 samples)
   Title: A gene expression signature identifies two prognostic subgroups of basal breast cancer
   overall design: The IPC series contained frozen tumor samples obtained from 266 early breast cancer patients who underwent initial surgery in our institution between 1992 and 2004. They included 227 cases previously reported {Finetti, 2008 #1758} and 39 additional cases, all similarly profiled using Affymetrix U133 Plus 2.0 human oligonucleotide microarrays as previously described {Finetti, 2008 #1758}. The study was approved by the IPC review board, and informed consent was available for each case. Gene expression data of 266 BCs  were quantified by using whole-genome DNA microarrays (HG-U133 plus 2.0, Affymetrix).
   Response columns (1):
     - characteristics_ch1_pr ihc (2 unique values): [0.0, 1.0]

   Sample summary (random sample from GSE21653):
score_age: 1
score_stage: 1
score_tissue: 1
score_histology: 1
score_primary_human_text: 3
net_score: 7
primary_score: 7
score_cancer_cols: 2
score_cancer_text: 2
refinebio_title: BC150
refinebio_age: 52.0
refinebio_source_database: GEO
refinebio_specimen_part: breast cancer tumor
description: n/a

2. GSE16716 (17 samples)
   Title: MicroArray Quality Control Phase II (MAQC-II) Project
   overall design: Refer to individual Series
   Response columns (2):
     - characteristics_ch1_pcr_vs_rd (2 unique values): ['pCR', 'RD']
     - characteristics_ch1_pr_status (2 unique values): ['P', 'N']

   Sample summary (random sample from GSE16716):
score_age: 1
score_tissue: 1
score_histology: 1
score_primary_human_text: 16
net_score: 19
primary_score: 19
score_cancer_cols: 1
score_cancer_text: 8
refinebio_title: BR_FNA_US097
refinebio_age: 46.0
refinebio_source_database: GEO
refinebio_specimen_part: breast cancer cells
description: ['MAQC_Distribution_Status: MAQC_Q -- Not used', 'Please see the GSE20194_MDACC_Sample_Info.xls file on the GSE20194 Series record for additional information on the Sample characteristics']
treatment_protocol_ch1: Patients received pretreatment fine-needle aspiration (FNA) of the primary breast tumor or ipsilateral axillary metastasis before starting chemotherapy as part of an ongoing pharmacogenomic marker discovery program. The aspiration was performed using a 23- or 25-gauge needle. Cells from two to three passes were collected in vials containing 1 mL RNA later solution (Ambion, Austin, TX) and stored at -80C. FNA samples on average contain 80% neoplastic cells and contain little or no stromal cells or normal breast epithelium.

3. GSE24742 (23 samples)
   Title: Effects of Rituximab on global gene expression profiles in the RA synovium
   overall design: Twenty patients with RA (17 women and 3 men, average age +/- SEM: 52,6+/-3,8 years) were included in the study. All patients met the American College of Rheumatology classification criteria for the diagnosis of RA. All patients had active disease at the time of tissue sampling and were resistant to TNF blockade. They all had erosive changes imaged on conventional x-rays of the hands and/or feet. All of them had a swollen knee at inclusion. Rituximab therapy was administrated at a dose of 1,000 mg IV at baseline (T0) and at week 2, together with 125 mg IV Methylprednisolone. Clinical parameters at baseline (T0) and 12 weeks after the initiation of therapy (T12) was evaluated using DAS(28)-CRP scores and clinical responses were assessed using EULAR response criteria. Synovial biopsies were obtained by needle-arthroscopy of an affected knee from all patients at T0 and T12. For each procedure, 4 to 8 synovial samples were kept overnight at 4°C in a RNA stabilizing solution (RNALater, Ambion, Applied Biosystems, TX, USA) and then stored at –80°C for later RNA extraction. The same amount of tissue was snap-frozen in liquid nitrogen and kept at –80°C for immunostaining experiments on frozen sections. The remaining material was fixed in 10% formaldehyde and paraffin embedded for conventional optical evaluation and immunostaining of selected markers. All the experiments (RNA extraction, histology, immunohistochemistry) were performed on at least 4 biopsies harvested during every procedure in order to correct for variations related to the potential heterogeneous distribution of synovial inflammation. The study was approved by the ethics committee of the Université catholique de Louvain and informed consent was obtained from all patients.

At least 1 µg total RNA could be extracted from 12 paired samples at T0 and T12 for further processing.
   Response columns (1):
     - characteristics_ch1_response (3 unique values): ['EULAR Moderate-responder', 'EULAR Poor-responder', 'EULAR Good-responder']

   Sample summary (random sample from GSE24742):
score_age: 1
score_sex: 1
score_stage: 1
score_tissue: 1
score_primary_human_text: 17
net_score: 21
primary_score: 21
score_cancer_cols: 1
refinebio_title: RTX1 T12
refinebio_disease: synovial knee biopsy
refinebio_disease_stage: rheumatoid arthritis
refinebio_sex: female
refinebio_source_database: GEO
refinebio_specimen_part: synovium
refinebio_treatment: 12 weeks of rtx therapy
description: twenty patients with ra (17 women and 3 men, average age +/- sem: 52,6+/-3,8 years) were included in the study. All patients met the American College of Rheumatology classification criteria for the diagnosis of RA. All patients had active disease at the time of tissue sampling and were resistant to TNF blockade. They all had erosive changes imaged on conventional x-rays of the hands and/or feet. All of them had a swollen knee at inclusion. Rituximab therapy was administrated at a dose of 1,000 mg IV at baseline (T0) and at week 2, together with 125 mg IV Methylprednisolone. Clinical parameters at baseline (T0) and 12 weeks after the initiation of therapy (T12) was evaluated using DAS(28)-CRP scores and clinical responses were assessed using EULAR response criteria. Synovial biopsies were obtained by needle-arthroscopy of an affected knee from all patients at T0 and T12. For each procedure, 4 to 8 synovial samples were kept overnight at 4C in a RNA stabilizing solution (RNALater, Ambion, Applied Biosystems, TX, USA) and then stored at 80C for later RNA extraction. The same amount of tissue was snap-frozen in liquid nitrogen and kept at 80C for immunostaining experiments on frozen sections. The remaining material was fixed in 10% formaldehyde and paraffin embedded for conventional optical evaluation and immunostaining of selected markers. All the experiments (RNA extraction, histology, immunohistochemistry) were performed on at least 4 biopsies harvested during every procedure in order to correct for variations related to the potential heterogeneous distribution of synovial inflammation. The study was approved by the ethics committee of the Universit catholique de Louvain and informed consent was obtained from all patients.

4. GSE22152 (24 samples)
   Title: Gene expression data of glucocorticoid resistant and sensitive acute lymphoblastic leukemia cell lines
   overall design: Gene expression profiles of glucocorticoid (GC) resistant and sensitive T-ALL cells during GC treatment and corresponding control samples (cells treated with carrier control). GC induced regulation of PFKFB2 was determined in the various cell lines based on the expression intensities of the corresponding probe sets in GC treated and control samples.
   Response columns (1):
     - characteristics_ch1_gc resistant (2 unique values): [False, True]

   Sample summary (random sample from GSE22152):
score_primary_human_text: 1
net_score: 1
primary_score: 1
score_cancer_text: 5
refinebio_title: GC resistant clone C7H2-R19E5 treated for 6 hours with EtOH
refinebio_source_database: GEO
refinebio_specimen_part: lymphoblastic leukemia
refinebio_treatment: etoh
description: GC resistant clone C7H2-R19E5 treated for 6 hours with 0.1% ethanol (carrier control).
growth_protocol_ch1: Cell lines were cultured in RPMI 1640 supplemented with 10% fetal calf serum and 2mM L-glutamine at 37C, 5% carbon-dioxide and saturated humidity. The cells were free of mycoplamsa infection.
treatment_protocol_ch1: Cells were treated with 100nM dexametasone (Sigma, Vienna, Austria) or 0.1% ethanol as carrier control.

5. GSE37180 (11 samples)
   Title: Gene expression profiles of ovarian tumor biopsies from Phase I dasatinib trial
   overall design: Global profiles of expression were characterized using unsupervised clustering methods and gene- and pathway-analyses of differential expression.
   Response columns (3):
     - characteristics_ch1_status for progression free survival (1=death, 0=censored) (2 unique values): [0.0, 1.0]
     - characteristics_ch1_objective response (1 = cr or pr, 0= sd) (3 unique values): ['<NA>', '1', '0']
     - characteristics_ch1_indicator of clinical response (cr=1/pr=2/sd=3) (4 unique values): ['2', '1', '<NA>', '3']

   Sample summary (random sample from GSE37180):
score_patient: 1
score_primary_human_text: 3
net_score: 4
primary_score: 4
score_cancer_text: 1
refinebio_title: 001-012
refinebio_subject: 001-012
refinebio_source_database: GEO
description: 001-012

6. GSE39133 (29 samples)
   Title: Gene expression profiling of microdissected HRS cells
   overall design: Gene expression profilies of micodissected Hodkin Reed Sternberg cells (n=29) were compared to microdissected germinal centers (n=5)
   Response columns (1):
     - characteristics_ch1_code progression-free survival (2 unique values): [0.0, 1.0]

   Sample summary (random sample from GSE39133):
score_age: 1
score_sex: 1
score_stage: 1
score_tissue: 1
score_histology: 1
score_primary_human_text: 1
net_score: 6
primary_score: 6
score_cancer_cols: 2
score_cancer_text: 1
refinebio_title: microdissected HRS cells, replicate 10
refinebio_age: 36.0
refinebio_disease: diagnostic
refinebio_sex: male
refinebio_source_database: GEO
refinebio_specimen_part: lymph node
description: Gene expression data from microdissected HRS cells

7. GSE46819 (23 samples)
   Title: Inhibitor of apoptosis protein antagonist BV6 – potential for new combinatorial treatment strategies in acute myeloid leukemia
   overall design: Gene expression was profiled in 24 AML samples [n=12 untreated, diagnostic samples of BV6 resistant (n=6) and sensitive (n=6) cases; n=6 paired samples (BV6 sensitive n=3 and resistant n=3 cases) treated for 24 hours with either DMSO or BV6].
   Response columns (1):
     - characteristics_ch1_bv6 response (2 unique values): ['resistant', 'sensitive']

   Sample summary (random sample from GSE46819):
score_age: 1
score_sex: 1
net_score: 2
primary_score: 2
score_cancer_text: 2
refinebio_title: AML_51
refinebio_age: 47.0
refinebio_sex: female
refinebio_source_database: GEO
refinebio_treatment: untreated
description: AML_51
treatment_protocol_ch1: Primary AML samples were cultivated using RPMI 1640 (Biochrom AG, Berlin, Germany), supplemented with 20% FCS (Sigma-Aldrich, St. Louis, MO, USA), 2 mM L-Glutamin (Biochrom AG), and Penicillin/Streptomycin (GIBCO, Invitrogen Corporation, Grand Island, NY, USA). Prior to treatment, cells were stained with trypan blue (Sigma-Aldrich), counted, and diluted to a density of 1.0x106 cells/ml. Thawing of viably frozen samples followed the DSMZ (German Collection of microorganisms and cell lines, Braunschweig) guideline. Agents used to treat primary AML sample for 24 hours in vitro were DMSO (control/carrier; dimethyl sulfoxide; Sigma-Aldrich) and BV6 was synthesized at Genentech, Inc. (South San Francisco, CA, USA).

8. GSE42296 (77 samples)
   Title: Distinct, non-overlapping gene panels of peripheral blood gene expression predict response to infliximab therapy in rheumatoid arthritis and Crohn's disease
   overall design: Peripheral blood samples were obtained at week 0 and week 2 of inxliximab treatment and global gene expression profiling identified markers of responder status.
   Response columns (1):
     - characteristics_ch1_response (2 unique values): ['NR - non-responder', 'R - responder']

   Sample summary (random sample from GSE42296):
score_stage: 1
score_primary_human_text: 1
net_score: 2
primary_score: 2
score_cancer_cols: 1
refinebio_title: Before treatment (week 0) IBDB18
refinebio_subject: patient 3
refinebio_disease: crohn's disease
refinebio_disease_stage: crohn's disease
refinebio_source_database: GEO
refinebio_specimen_part: pbmc
refinebio_treatment: before treatment
treatment_protocol_ch1: Treatment was infliximab infusion at week 0 and at week 2.

9. GSE85047 (275 samples)
   Title: Gene expression data from primary neuroblastoma tumors
   overall design: 283 primary untreated neuroblastoma tumors were analyzed. No replicates were included.
   Response columns (1):
     - characteristics_ch1_event_progression_free (2 unique values): ['no', 'yes']

   Sample summary (random sample from GSE85047):
score_age: 1
score_primary_human_text: 4
net_score: 5
primary_score: 5
score_cancer_text: 1
refinebio_title: primary NB tumor_nrc4024
refinebio_source_database: GEO

10. GSE58911 (29 samples)
   Title: Gene expression in normal and tumor samples from patients with HNSCC
   overall design: Fifteen paired normal and tumor samples from individual patients were analyzed (a total of 30 samples).
   Response columns (1):
     - characteristics_ch1_patient 2 yr disease free survival outcome (3 unique values): ['no', 'unknown', 'yes']

   Sample summary (random sample from GSE58911):
score_age: 1
score_patient: 1
score_stage: 1
score_tissue: 1
score_primary_human_text: 7
net_score: 11
primary_score: 11
score_cancer_cols: 1
score_cancer_text: 6
refinebio_title: HNSCC sample patient 076
refinebio_subject: 76
refinebio_age: 43.0
refinebio_source_database: GEO
refinebio_specimen_part: hnscc
description: ['Gene expression data from HNSCC patient 076', '076T']

11. GSE25055 (3 samples)
   Title: Discovery cohort for genomic predictor of response and survival following neoadjuvant taxane-anthracycline chemotherapy in breast cancer
   overall design: Neoadjuvant study of 310 HER2-negative breast cancer cases treated with taxane-anthracycline chemotherapy pre-operatively and endocrine therapy if ER-positive.  Response was assessed at the end of neoadjuvant treatment and distant-relapse-free survival was followed for at least 3 years post-surgery.
   Response columns (2):
     - characteristics_ch1_rcb_0_i_prediction (2 unique values): ['RCB-II/III', 'RCB-0/I']
     - characteristics_ch1_pr_status_ihc (2 unique values): ['P', 'N']

   Sample summary (random sample from GSE25055):
score_age: 1
score_stage: 1
score_tissue: 1
score_primary_human_text: 9
net_score: 12
primary_score: 12
score_cancer_cols: 1
score_cancer_text: 2
refinebio_title: 1205
refinebio_disease_stage: na
refinebio_source_database: GEO
refinebio_specimen_part: breast cancer tumor
treatment_protocol_ch1: Patients prospectively consented to a research biopsy by fine needle aspiration (FNA) or  core biopsy (CBX) prior to any systemic therapy, and to the future assessment of pathologic  response and/or survival endpoints

12. GSE11237 (23 samples)
   Title: Celecoxib pre-treatment in human colorectal adenocarcinoma patients.
   overall design: Patients undergoing surgical resection of histologically proven primary colorectal adenocarcinomas were consented for participation in the study.  The patients enrolled in this study were randomized to receive either 400 mg celecoxib two times per day (n=11) or no COX-2 inhibitor (n=12) for 7 days prior to surgical resection. Total RNA (5 ug) from each sample was converted to double stranded cDNA using a dT-T7 promoter primer.  The double stranded cDNA was then used as a template to synthesize biotinylated RNA, which was fragmented and hybridized to the Affymetrix HG_U95av2 microarray chip using Affymetrix’s labeling and hybridization protocol.
   Response columns (3):
     - characteristics_ch1_Pathological M (2 unique values): [0.0, 1.0]
     - characteristics_ch1_Pathological N (3 unique values): [0.0, 1.0, 2.0]
     - characteristics_ch1_Pathological T (4 unique values): [1.0, 2.0, 3.0, 4.0]

   Sample summary (random sample from GSE11237):
score_sex: 1
score_stage: 1
score_primary_human_text: 6
net_score: 8
primary_score: 8
score_cancer_cols: 2
score_cancer_text: 2
refinebio_title: CRC_celecoxib_F4873
refinebio_disease_stage: moderate
refinebio_sex: female
refinebio_source_database: GEO
refinebio_treatment: yes
description: 4873
treatment_protocol_ch1: Patients undergoing surgical resection of histologically proven primary colorectal adenocarcinomas were consented for participation in the study.  The patients enrolled in this study were randomized to receive either 400 mg celecoxib two times per day (n=11) or no COX-2 inhibitor (n=12) for 7 days prior to surgical resection.

13. GSE40020 (19 samples)
   Title: Gene expression characterization of HPV positive head and neck cancer to predict response to Chemoradiation
   overall design: HPV-positive head and neck squamous cell carcinoma (HNSCC) has a good prognosis with a large percentage of patients responding to therapy. However, a certain percentage of patients do not respond. Gene expression data from Affymetrix Human Exon 1.0ST microarrays was utilized to compare patients that responded to therapy with those that did not respond.
   Response columns (1):
     - characteristics_ch1_response to chemoradiation (2 unique values): ['Complete Response', 'Post-treatment Failure']

   Sample summary (random sample from GSE40020):
score_stage: 1
net_score: 1
primary_score: 1
score_cancer_cols: 1
score_cancer_text: 3
refinebio_title: HPV+ HNSCC_R1138_Complete Responder
refinebio_disease: hpv-positive hnscc
refinebio_disease_stage: hpv-positive hnscc
refinebio_source_database: GEO
description: Human head and neck squamous cell carcinoma (HNSCC)

14. GSE25066 (1 samples)
   Title: Genomic predictor of response and survival following neoadjuvant taxane-anthracycline chemotherapy in breast cancer
   overall design: Refer to individual Series

   Response columns (2):
     - characteristics_ch1_rcb_0_i_prediction (1 unique values): ['RCB-II/III']
     - characteristics_ch1_pr_status_ihc (1 unique values): ['N']

   Sample summary (random sample from GSE25066):
score_age: 1
score_stage: 1
score_tissue: 1
score_primary_human_text: 5
net_score: 8
primary_score: 8
score_cancer_cols: 1
score_cancer_text: 1
refinebio_title: 1064
refinebio_disease_stage: 3
refinebio_source_database: GEO
refinebio_specimen_part: breast cancer tumor
treatment_protocol_ch1: Patients prospectively consented to a research biopsy by fine needle aspiration (FNA) or  core biopsy (CBX) prior to any systemic therapy, and to the future assessment of pathologic  response and/or survival endpoints

15. GSE68465 (214 samples)
   Title: caArray_jacob-00182: Gene expression-based survival prediction in lung adenocarcinoma: a multi-site, blinded validation study
   overall design: jacob-00182
Assay Type: Gene Expression
Provider: Affymetrix
Array Designs: HG-U133A
Organism: Homo sapiens (ncbitax)
Material Types: cell, synthetic_RNA, organism_part, whole_organism, total_RNA
Disease States: Lung Adenocarcinoma
   Response columns (1):
     - characteristics_ch1_first_progression_or_relapse (4 unique values): ['Unknown', 'Yes', '--', 'No']

   Sample summary (random sample from GSE68465):
score_age: 1
score_sex: 1
score_stage: 1
score_histology: 1
score_primary_human_text: 2
net_score: 6
primary_score: 6
score_cancer_cols: 2
score_cancer_text: 2
refinebio_title: jacob-00182: 311
refinebio_age: 55.0
refinebio_disease: lung adenocarcinoma
refinebio_disease_stage: pn0pt2
refinebio_sex: female
refinebio_source_database: GEO
refinebio_specimen_part: lung

16. GSE66525 (22 samples)
   Title: A gene expression profile associated with relapse of cytogenetically normal acute myeloid leukemia is enriched for leukemia stem cell genes
   overall design: Paired peripheral blood samples from the times of diagnosis and relapse were obtained from 11 patients with cytogenetically normal AML. cRNA was hybridized to Affymetrix human ST1.1 arrays.
   Response columns (1):
     - characteristics_ch1_response (2 unique values): ['PR', 'CR']

   Sample summary (random sample from GSE66525):
score_age: 1
score_sex: 1
score_primary_human_text: 4
net_score: 6
primary_score: 6
score_cancer_cols: 1
score_cancer_text: 4
refinebio_title: CN AML patient 3 R
refinebio_age: 36.0
refinebio_sex: female
refinebio_source_database: GEO
growth_protocol_ch1: Ficoll purified, vitally frozen primary patient samples

17. GSE54747 (15 samples)
   Title: An intrahepatic gene expression signature of enhanced immune activity predicts response to peginterferon and adefovir in chronic hepatitis B patients
   overall design: 15 liver biopsies of chronic hepatitis B patients were selected for RNA extraction and hybridization on Affymetrix microarrays. Expression values in 9 biopsies of patients with a combined response to therapy were compared with 6 biopsies of non-responders.
Differentially expressed genes between responders and non-responders were determined using filtering on minimal average expression, fold change (1.5 fold) and p-values from 2-sided t-tests (0 permutations) in GenePattern.
   Response columns (1):
     - characteristics_ch1_response (2 unique values): ['non-responder to treatment with peg-IFN and adefovir', 'responder to treatment with peg-IFN and adefovir']

   Sample summary (random sample from GSE54747):
score_stage: 1
score_tissue: 1
score_primary_human_text: 3
net_score: 5
primary_score: 5
score_cancer_cols: 1
refinebio_title: HBeAg_POS_Resp_22
refinebio_disease: hbeag-positive chronic hepatitis b
refinebio_disease_stage: hbeag-positive chronic hepatitis b
refinebio_source_database: GEO
refinebio_specimen_part: liver
treatment_protocol_ch1: Chronic hepatitis B patients (HBeAg-positive or -negative) with HBV-DNA levels above 17,182 IU/mL (100,000 copies/mL) received a combination of peginterferon alfa-2a 180 mg subcutaneously once a week, and adefovir dipivoxil 10 mg daily. After 48 weeks, treatment was discontinued and a treatment-free follow-up period started.

18. GSE58598 (10 samples)
   Title: Stromal and epithelial changes in breast cancer following endocrine treatment
   overall design: Post-treatment samples from three responding patients (A29, B42, B61) and three non-responding patients (A15, A19, B59) were identified as suitable for this study and underwent LCM.
   Response columns (1):
     - characteristics_ch1_response (2 unique values): ['non-responding', 'responding']

   Sample summary (random sample from GSE58598):
score_age: 1
score_sex: 1
score_patient: 1
score_stage: 1
score_tissue: 1
score_primary_human_text: 12
net_score: 17
primary_score: 17
score_cancer_cols: 3
score_cancer_text: 1
refinebio_title: stromal compartment of non-responding patient A19
refinebio_subject: a19
refinebio_disease_stage: 2
refinebio_sex: female
refinebio_source_database: GEO
refinebio_specimen_part: stromal
refinebio_treatment: tamoxifen
description: ['A19 s', 'S_NR_06.CEL']
treatment_protocol_ch1: ['Tissue preservation protocol: Breast cancer tumour biopsies were formalin-fixed paraffin-embedded (FFPE). The implemented protocol for this process is unavailable. (At the time of LCM, these samples had been preserved for more than 20 years.)', '10 m thick tissue sections from FFPE blocks were mounted on metal-framed polyethylene terephthalate (PET) membrane slides (membrane thickness 1.4 m, steel frames, Order no. 11505151, Leica Microsystems) and underwent deparaffinisation, staining and dehydration prior to Laser Capture Microdissection (LCM). Staining was carried out using Hematoxylin (Shandon Gill 1, Thermo Scientific). Epithelial cells and stromal cells were isolated from each section by LCM which was conducted using Leica LMD6000 Laser Microdissection System (Leica Microsystems).']

19. GSE15622 (35 samples)
   Title: Expression data from the CTCR-OV01 study
   overall design: Patients with suspected ovarian cancer had a biopsy obtained before and after 3 cycles of either Carboplatin or Paclitaxel. Samples were immediately frozen for RNA extraction.
   Response columns (1):
     - characteristics_ch1_response (2 unique values): ['sensitive', 'resistant']

   Sample summary (random sample from GSE15622):
score_primary_human_text: 6
net_score: 6
primary_score: 6
score_cancer_text: 1
refinebio_title: Patient 1, post-treatment
refinebio_source_database: GEO
refinebio_treatment: carboplatin
description: Non-responder

20. GSE18864 (84 samples)
   Title: Tumor expression data from neoadjuvant trial of cisplatin monotherapy in triple negative breast cancer patients
   overall design: Pretreatment tumor samples from the clinical trial (N=24 with adequate tissue) were used for RNA extraction, linear amplification, biotin labeling and hybridization to Affymetrix U133 plus 2.0 arrays.  A reference set of 51 primary breast tumors representing all subtypes of breast cancer were processed in a similar manner to include linear amplification, and hybridized to Affymetrix arrays.
   Response columns (1):
     - characteristics_ch1_miller-payne response (7 unique values): ['3', '1', '0', 'n/a']

   Sample summary (random sample from GSE18864):
score_age: 1
score_stage: 1
score_primary_human_text: 1
net_score: 3
primary_score: 3
score_cancer_cols: 1
score_cancer_text: 6
refinebio_title: Reference tumor 96
refinebio_age: 54.0
refinebio_disease_stage: ii
refinebio_source_database: GEO
description: Gene expression data from reference primary breast tumor
treatment_protocol_ch1: Two 5 frozen sections were stained with hematoxylin and eosin, manually scraped to remove normal stroma and enrich for tumor cells.

21. GSE31852 (21 samples)
   Title: An EGFR-mutation signature reveals features of the EGFR-dependent phenotype and identifies MACC1 as an EGFR-associated regulator of MET.
   overall design: Gene expression profiles were measured in 124 core biopsies from patients with refractory non-small cell lung cancer in the  Biomarker-integrated Approaches of Targeted Therapy for Lung Cancer Elimination (BATTLE) trial. We used the BATTLE dataset to test an EGFR-mutation gene expression signature trained in chemo-naive lung adenocarcinoma. The signature was computed as an index, called EGFR index.
   Response columns (1):
     - characteristics_ch1_progression-free survival status (1 unique values): [1.0]

   Sample summary (random sample from GSE31852):
score_primary_human_text: 5
net_score: 5
primary_score: 5
score_cancer_text: 1
refinebio_title: LM116
refinebio_source_database: GEO
refinebio_treatment: erlotinib
description: ['Human Gene 1.0 ST_525_LM_116_05_13_08', 'Inclusion number in the clinical trial : 133']
growth_protocol_ch1: Core biopsies from patients included in the Biomarker-integrated Approaches of Targeted Therapy for Lung Cancer Elimination (BATTLE)
treatment_protocol_ch1: Samples were OCT-embedded and frozen before RNA extraction

22. GSE64085 (11 samples)
   Title: MYC-negative BL frequent in posttransplant patients (expression)
   overall design: Seven cases of PTLD with BL features were selected from a cohort of 174 posttransplant patients diagnosed with PTLD between 1989 and 2012 at the University Hospitals of KU Leuven (Leuven, Belgium). In addition, five classic BL cases were selected as immunocompetent controls (IC-BL). Morphologic, immunophenotypic, clinical and cytogenetic characteristics of the selected cases were reviewed.
   Response columns (1):
     - characteristics_ch1_response (2 unique values): ['PD', 'CR']

   Sample summary (random sample from GSE64085):
score_age: 1
score_sex: 1
score_primary_human_text: 2
net_score: 4
primary_score: 4
score_cancer_text: 3
refinebio_title: Burkitt Lymphoma 10
refinebio_age: 18.0
refinebio_sex: male
refinebio_source_database: GEO
refinebio_treatment: chop/rtx
growth_protocol_ch1: Patients diagnosed with BL were biopsied and tumor tissues were frozen.
treatment_protocol_ch1: Frozen tissue sections were immediately dissolved in Trizol.

23. GSE157738 (102 samples)
   Title: Monocyte-derived DC Expression Data from Advanced Staged Melanoma Patients
   overall design: 34/35 patient DCs were analyzed for each DC subtype (iDC, mDC, AdVTMM2 DC) using the Affymetrix Human Gene 2.0 ST Array. We investigated  gene expression profiles that correlated with overall survival  and favorable clinical outcomes in late-stage melanoma patients.
   Response columns (1):
     - characteristics_ch1_clinical outcome (5 unique values): ['NED1', 'PR', 'SD', 'NED2']

   Sample summary (random sample from GSE157738):
score_patient: 1
score_primary_human_text: 5
net_score: 6
primary_score: 6
score_cancer_text: 3
refinebio_title: Day 5 Immature DC_Patient 3
refinebio_subject: patient 3
refinebio_source_database: GEO
refinebio_specimen_part: dendritic cell
description: Gene expression data from monocyte-derived iDC, melanoma
growth_protocol_ch1: Patient immature dendritic cells were generated from elutriated monocytes using GM-CSF and IL-4 for 5 days. On day 6, immature DC were matured using IFNG and LPS for 24hrs. 24hrs. Post-maturation, mDC were transduced with the adenovirus vaccine for 3hrs.
treatment_protocol_ch1: Matured DC (mDC) were transduced with the recombinant Adenovirus vaccine (encoding three full length antigens: Tyrosinase, MART-1, MAGE-A6) for 3hrs at 37°C.

24. GSE39925 (21 samples)
   Title: Transcriptional characterization of a prospective series of primary plasma cell leukemia revealed genes associated with tumor progression and poorest outcome
   overall design: This series of microarray experiments contains the gene expression profiles of purified plasma cells (PCs) obtained from 21 pPCL and 55 MM at diagnosis. PCs were purified from bone marrow samples using CD138 immunomagnetic microbeads according to the manufacturer's instructions (MidiMACS system, Miltenyi Biotec); the purity of the positively selected PCs was assessed by morphology and flow cytometry and was > 90% in all cases. 5.5 micrograms of single-stranded DNA target obtained from 100 ng of purified total RNA was fragmented and then labeled using the WT Terminal Labeling Kit according to the standard Affymetrix protocol (GeneChip¨ Whole Transcript (WT) Sense Target Labeling Assay Manual). The fragmented labeled single-stranded DNA target was hybridized for 16 hours and 30 minutes at 45¡C on GeneChip¨ Gene 1.0 ST array according to the standard Affymetrix protocol. Washing and scanning were performed using GeneChip System of Affymetrix (GeneChip Hybridization Oven 640, GeneChip Fluidics Station 450 and GeneChip Scanner 7G). Log2-transformed expression values were extracted from CEL files and normalized using NetAffx Transcript Cluster Annotations, Release 31 and robust multi-array average (RMA) procedure in Expression Console software (Affymetrix Inc.). Non-annotated transcript clusters were discarded. The expression values of transcript cluster ID specific for loci representing naturally occurring read-through transcriptions or mapped to more than one chromosomal location were summarized as median value for each sample.
gene expression analysis of 21 primary Plasma Cell Leukemia and 55 multiple myeloma tumors
   Response columns (1):
     - characteristics_ch1_response (5 unique values): ['VGPR', 'nd', 'CR', 'PR']

   Sample summary (random sample from GSE39925):
score_age: 1
score_sex: 1
score_tissue: 1
score_primary_human_text: 6
net_score: 9
primary_score: 9
score_cancer_text: 5
refinebio_title: PCL-019_GENE10_2
refinebio_age: 67.0
refinebio_sex: female
refinebio_source_database: GEO
refinebio_specimen_part: human primary plasma cell leukemia
description: Gene expression profiling data from human primary plasma cell leukemia patient PCL-019
treatment_protocol_ch1: Plasma cells were purified from bone marrow samples using CD138 immunomagnetic microbeads according to the manufacturer's instructions (MidiMACS system, Miltenyi Biotec); the purity of the positively selected PCs was assessed by morphology and flow cytometry and was > 90% in all cases.

25. GSE106977 (118 samples)
   Title: Triple negative breast cancer subtypes and pathologic complete response rate to neoadjuvant chemotherapy
   overall design: We performed a retrospective analysis in paraffined pre-treatment tumor biopsies from 119 triple negative breast cancer patients (88 patients treated with neoadjuvant anthracyclines and/or taxanes and 31 with anthracyclines and/or taxanes plus carboplatin). We determined Lehmann subtypes by gene-expression profiling with the GeneChip® Human Transcriptome Array 2.0. (Affymetrix). Data were normalized with the Robust Multichip Analysis (RMA) algorithm in the Affymetrix Expression Console (EC, v.1.4.1) and annotated in the statistical computing environment R (v.3.2.3) using hg19 human genome built. Duplicated genes were mean summarized.
   Response columns (1):
     - characteristics_ch1_pathological complete response (2 unique values): ['yes', 'no']

   Sample summary (random sample from GSE106977):
score_tissue: 1
score_primary_human_text: 4
net_score: 5
primary_score: 5
score_cancer_text: 1
refinebio_title: 3V
refinebio_source_database: GEO
refinebio_specimen_part: breast cancer
refinebio_treatment: anthracyclines and/or taxanes
description: Gene expression data from pretreatment biopsies of a triple negative breast cancer patient

26. GSE29561 (21 samples)
   Title: Response prediction to neoadjuvant chemotherapy
   overall design: 22 Samples from breast cancer patients with corresponding treatment response indicators
   Response columns (1):
     - characteristics_ch1_treatment response in vivo (2 unique values): [0.0, 1.0]

   Sample summary (random sample from GSE29561):
score_primary_human_text: 1
net_score: 1
primary_score: 1
score_cancer_text: 1
refinebio_title: Pre-treatment breast cancer cells sample 5
refinebio_source_database: GEO
refinebio_specimen_part: breast cancer cells

27. GSE115577 (429 samples)
   Title: Tumor & Tumor-Adj Gene Expression in the Nurses' Health Study Cohorts
   overall design: Total of 1577 samples which includes 882 tumor and 695 tumor-adjacent tissues from participants of the Nurses' Heath Study I and II diagnosed with invasive breast cancer. This deposit contains 467 files; remaining 1110 files are in GSE93601.
   Response columns (1):
     - characteristics_ch1_pr ihc (2 unique values): [0.0, 1.0]

   Sample summary (random sample from GSE115577):
score_age: 1
score_stage: 1
score_primary_human_text: 2
net_score: 4
primary_score: 4
score_cancer_cols: 2
score_cancer_text: 2
refinebio_title: FFPE X213779342 [X195_M379]
refinebio_disease_stage: 2
refinebio_source_database: GEO
refinebio_treatment: mixed
description: X195_M379

28. GSE35640 (9 samples)
   Title: Identification of a predictive gene signature to recMAGE A3 antigen-specific cancer immunotherapy in metastatic melanoma and non-small-cell lung cancer
   overall design: Patients were participants in two Phase II studies of the recombinant MAGE‑A3 antigen combined with immunological adjuvants.  mRNA from tumor samples (biopsies) collected before MAGE-A3 immunotherapy was analyzed by microarray hybridization and by quantitative polymerase chain reaction (qRT-PCR).  The melanoma microarray dataset was used to discover and crossvalidate a gene expression signature and classifier discriminative of Responders (R) versus Non-Responders (NR) patients; the gene signature and classifier were then applied to an adjuvant lung cancer study. Patients that were not included for analysis are denoted as NE (Non-evaluable).
GSK Biologicals
   Response columns (2):
     - characteristics_ch1_treatment response for gene profiling (1 unique values): ['NE']
     - characteristics_ch1_response (1 unique values): ['not evaluable']

   Sample summary (random sample from GSE35640):
score_tissue: 1
score_primary_human_text: 5
net_score: 6
primary_score: 6
score_cancer_text: 9
refinebio_title: Melanoma tumor sample from patient 58
refinebio_source_database: GEO
refinebio_specimen_part: melanoma tumor biopsy prior to mage-a3 immunotherapy

29. GSE15258 (73 samples)
   Title: Whole blood transcript profiling of rheumatoid arthritis patients
   overall design: Patients' response to anti-TNF was assessed using EULAR score and patients were classified as responders, moderate responders and non-responders. Genes correlating with the response status have been identified.
   Response columns (1):
     - characteristics_ch1_response to anti-tnf therapy (3 unique values): ['MEDIUM', 'NORESPONSE', 'RESPONSE']

   Sample summary (random sample from GSE15258):
score_stage: 1
score_tissue: 1
net_score: 2
primary_score: 2
score_cancer_cols: 1
refinebio_title: PNS033
refinebio_disease: rheumatoid arthritis
refinebio_disease_stage: rheumatoid arthritis
refinebio_source_database: GEO
refinebio_specimen_part: whole blood
description: no additional information
treatment_protocol_ch1: anti-TNF therapy

30. GSE28826 (15 samples)
   Title: Differentially expressed genes after treatment with chemotherapy in breast cancer and their correlation with pathologic bad response (Miller & Payne grades 1 and 2)
   overall design: After informed consent, patients with a histologically confirmed diagnosis of breast cancer and scheduled chemotherapy treatment based on Anthracyclines and Taxanes (Treatment A: Epirubicin 90 mg/m2-Cyclophosphamide 600 mg/m2, 3 cycles bi-weekly and Taxol 150 mg/m2-Gemcitabine 2500 mg/m2, 6 cycles bi-weekly ± weekly Herceptin 4 mg/Kg during the first week, 2 mg/Kg for the remaining 11 cycles; Treatment B: Doxorubicin 60 mg/m2-Pemetrexed 500 mg/m2, 4 cycles tri-weekly and Taxotere 100 mg/m2, 4 cycles tri-weekly; Treatment C: Doxorubicin 60 mg/m2-Cyclophosphamide 600 mg/m2, 4 cycles tri-weekly and Taxotere 100 mg/m2, 4 cycles tri-weekly ) were recruited for this study. Pre-chemotherapy and post-chemotherapy biopsies were examined by a pathologist who determined the Miller & Payne grade for each patient. Matching pairs of pre-chemotherapy and post-chemotherapy samples were divided into 3 groups according to Miller & Payne grade: group of bad response (Miller & Payne grades 1 and 2), group of mid response(Miller & Payne grade 3) and group of good response (Miller & Payne grades 4 and 5). Gene expression analysis was performed in paired samples as follows: bad response group post-chemotherapy biopsy vs pre-chemotherapy biopsy (Bad Final vs Initial). For this assay were necessary 28 samples being chosen according to histopathologic criteria (Miller & Payne grades 1 and 2). Of them, 26 samples were paired, 1 pre-chemotherapy sample and 1 post-chemotherapy sample from patients that experienced a bad response to chemotherapy were also included in this experimental series. Other comparisons in which this group of samples was involved include: Initial Bad vs Good, Initial Bad vs Mid, Final Bad vs Good and Final Bad vs Mid. This gene expression profiling was carried out making use of Affymetrix’s GeneChip technology, with the Affymetrix’s HG-U133 Plus 2.0 array from this provider. All the protocols and apparatus were recommended by Affymetrix. Total RNA from frozen mammary tumors was directly extracted by a RNeasy Mini kit and homogenized by QIAshredder columns under manufacturer’s instructions. The quality and quantity of the obtained RNA, was checked out through agarose electrophoresis and later spectrophotometry at 260/280 nm. Biotinylated cRNA was synthesized following the IVT labeling kit from Affymetrix and purified by the GeneChip Sample Cleanup Module from Affymetrix. Once again, the quality and quantity of the obtained cRNA, was checked out through agarose electrophoresis and posterior spectrophotometry at 260/280 nm. After hybridization, slides were washed and scanned following the manufacturer’s standard protocol. Intensity values were normalized by Robust Multichip Average method and subsequently these were filtered for remove the control sequences and those with a hybridization signal near to background. The spike controls were: BioB, BioC, BioD and Cre; because BioB was the less presented in the samples, it was used to estimate the sensitivity of the experiment. The housekeeping control was GAPDH. After non-supervised PCA analysis and clustering, gene expression statistical significances were identified by two regression models taking into account the pathologic response to chemotherapy and if the sample was obtained before or after chemotherapy treatment. Supervised PCA analysis and clustering were performed with processed data. Partek Genomics Suite v7.3.1 (Partek) software was employed for the statistic analysis and clustering.
   Response columns (1):
     - characteristics_ch1_pathologic response to chemotherapy (miller & payne grade) (2 unique values): [1.0, 2.0]

   Sample summary (random sample from GSE28826):
score_age: 1
score_sex: 1
score_tissue: 1
score_primary_human_text: 10
net_score: 13
primary_score: 13
score_cancer_cols: 1
score_cancer_text: 3
refinebio_title: Breast tumor biopsy_Postchemotherapy_08SE143
refinebio_age: 73.0
refinebio_sex: female
refinebio_source_database: GEO
refinebio_specimen_part: breast tumor
refinebio_treatment: a
description: Affymetrix Standard Protocol
treatment_protocol_ch1: RNA processing: snap frozen in liquid nitrogen and preserved at -80C. Before RNA extraction protocol, samples were sectioned in a cryostat to evalute the celularity.

31. GSE11001 (30 samples)
   Title: Genome-wide expression profiling from formalin-fixed paraffin-embedded breast cancer core biopsies
   overall design: RNA from 24 breast cancer biopsies extracted with kit A, RNA from 6 breast cancer biopsies extracted with kit B
   Response columns (1):
     - characteristics_ch1_PR (2 unique values): ['negative', 'positive']

   Sample summary (random sample from GSE11001):
score_stage: 1
score_primary_human_text: 17
net_score: 18
primary_score: 18
score_cancer_cols: 2
score_cancer_text: 1
refinebio_title: biopsy17_kitA
refinebio_disease_stage: 3
refinebio_source_database: GEO
description: FFPE core needle biopsy

32. GSE84334 (6 samples)
   Title: Gene expression analysis of DAC treated AML: high impact or tumor suppressor gene expression changes
   overall design: Gene expression was profiled in 45 AML samples in DAC treated patients prior to therapy. Response n=20, non response n=18, unknown n=7)
   Response columns (1):
     - characteristics_ch1_response to dac (1 unique values): ['na']

   Sample summary (random sample from GSE84334):
score_age: 1
score_sex: 1
score_primary_human_text: 1
net_score: 3
primary_score: 3
score_cancer_text: 2
refinebio_title: 16-05PB2678
refinebio_age: 70.0
refinebio_sex: female
refinebio_source_database: GEO
description: 16-05PB2678
treatment_protocol_ch1: Primary AML samples were taken at the time of diagnosis prior to treatment with DAC. For the analysis patients were then grouped based on the response to DAC which was given later during the course of the disease. In this study, DAC was given three times daily on 3 consecutive days (total dose 135mg/m, repeated every 6 weeks).

33. GSE46106 (42 samples)
   Title: Patient-derived Human Breast Cancer Xenografts
   overall design: The study was designed to determine how stable patient-derived xenografts are across multiple transplant generations in mice, and to determine how closely xenografts established with pre-treatment samples cluster with xenografts established with post-treatment samples. Overall, pre-treatment and post-treatment samples derived from the same patient cluster together, and multiple transplant generations of xenografts derived from an individual patient cluster together.
   Response columns (1):
     - characteristics_ch1_pr.ihc (2 unique values): ['P', 'N']

   Sample summary (random sample from GSE46106):
score_tissue: 1
score_primary_human_text: 8
net_score: 9
primary_score: 9
score_cancer_text: 5
refinebio_title: 3104TG3_U133plus2
refinebio_source_database: GEO
refinebio_specimen_part: xenograft
growth_protocol_ch1: Patient-derived xenografts are grown by transplantation into the epithelium-free mammary fat pad of recipient SCID/Bg mice. Transplantation was performed without intervening culture in vitro or experimental manipulation of any kind
treatment_protocol_ch1: Tumor fragments were excised and frozen at -80C prior to RNA extraction

34. GSE93984 (27 samples)
   Title: Expression data from DLBCL tumor biopsies
   overall design: Gene expression in ibrutinib pretreated tumor biopsy samples from ABC-DLBCL patients was detected by U133 plus 2.0 arrays and the correlation of BCL2 expression and patient response to ibrutinib or PFS after ibrutinib treatment was analyzed. There are total 28 ABC-DLBCL samples. 17 of them are non-responders (PD+SD) and 11 of them are responders (PR+CR). For this analysis restricted to ABC-DLBCL subtype, only the ABC-DLBCL samples were used and normalized separately.

Data was processed with all subsets of DLBCL samples (60 samples) and also separately for 28 ABC-DLBCL samples ('re-analysis' samples).

The values in the sample 'characteristics' field represent:
response:
CR=complete response, PR=partial response, SD=stable disease, PD=progression disease
class:
NR=non-responder, RR=responder
subtype:
ABC=ABC-DLBCL, GCB=GCB-DLBCL, UNC=unclassified subtype
progression_free_survival_censor:
censored case = 1; event (death/progression) = 0 in the censoring variable for the progression free survival analysis
   Response columns (2):
     - characteristics_ch1_progression_free_survival_censor (2 unique values): [0.0, 1.0]
     - characteristics_ch1_response (4 unique values): ['PR', 'CR', 'PD', 'SD']

   Sample summary (random sample from GSE93984):
score_stage: 1
score_primary_human_text: 10
net_score: 11
primary_score: 11
score_cancer_cols: 1
score_cancer_text: 9
refinebio_title: FFPE embedded lymph node at baseline [CH_SNSA_madbID120528_re-analysis]
refinebio_disease_stage: diffuse large b-cell lymphoma (dlbcl) patient
refinebio_source_database: GEO
description: gene expression data from DLBCL patient tumor

35. GSE41408 (48 samples)
   Title: Co-expression of genes with ERG in prostate cancers
   overall design: 48 Prostate cancer samples from radical prostatectomies were included in this study. These samples contained more than 70% cancer and less than 30% stromal tissue. Each sample was analyzed once.
   Response columns (1):
     - characteristics_ch1_psa progression (2 unique values): ['yes', 'no']

   Sample summary (random sample from GSE41408):
score_stage: 1
score_metastasis: 1
score_primary_human_text: 2
net_score: 4
primary_score: 4
score_cancer_cols: 2
refinebio_title: Prostate_Cancer [G124]
refinebio_source_database: GEO
growth_protocol_ch1: Samples are radical prostatectomy tissues directly taken from the patient
treatment_protocol_ch1: Samples were taken from the surgically removed prostate and fresh frozen in liq N2-cooled iso-pentane

36. GSE36295 (43 samples)
   Title: Transcriptomic analysis of breast cancer
   overall design: Total RNA isolated from 45 surgically resected breast cancer tissues and 8 healthy breast tissues (3 from Affymetrix) and purified, labeled, and hybridized to Affymetrix Human Gene 1.0 ST Array.
   Response columns (1):
     - characteristics_ch1_pr   (1= positive, 0= negative) (3 unique values): ['0', '1', 'Normal']

   Sample summary (random sample from GSE36295):
score_age: 1
score_stage: 1
score_tissue: 1
score_histology: 1
score_primary_human_text: 1
net_score: 5
primary_score: 5
score_cancer_cols: 2
score_cancer_text: 1
refinebio_title: Breast cancer 6
refinebio_disease_stage: 3
refinebio_source_database: GEO
refinebio_specimen_part: breast cancer tumor
description: Fresh Tissue

37. GSE28583 (9 samples)
   Title: Differentially expressed genes after treatment with chemotherapy in breast cancer and their correlation with pathologic mid-response (Miller & Payne grade 3)
   overall design: After informed consent, patients with a histologically confirmed diagnosis of breast cancer and scheduled chemotherapy treatment based on Anthracyclines and Taxanes (Treatment A: Epirubicin 90 mg/m2-Cyclophosphamide 600 mg/m2, 3 cycles bi-weekly and Paclitaxel 150 mg/m2-Gemcitabine 2500 mg/m2, 6 cycles bi-weekly ± weekly Herceptin 4 mg/Kg during the first week, 2 mg/Kg for the remaining 11 cycles; Treatment B: Doxorubicin 60 mg/m2-Pemetrexed 500 mg/m2, 4 cycles tri-weekly and Docetaxel 100 mg/m2, 4 cycles tri-weekly; Treatment C: Doxorubicin 60 mg/m2-Cyclophosphamide 600 mg/m2, 4 cycles tri-weekly and Docetaxel 100 mg/m2, 4 cycles tri-weekly ) were recruited for this study. Pre-chemotherapy and post-chemotherapy biopsies were examined by a pathologist who determined the Miller & Payne grade for each patient. Matching pairs of pre-chemotherapy and post-chemotherpy samples were divided into 3 groups according to Miller & Payne grade: group of bad response (Miller & Payne grades 1 and 2), group of mid response (Miller & Payne grade 3) and group of good response (Miller & Payne grades 4 and 5). Gene expression analysis was performed in paired samples as follows: mid response group post-chemotherapy biopsy vs pre-chemotherapy biopsy (Mid final vs initial). For this assay were necessary 20 samples being chosen according to histopathologic criteria (Miller & Payne grade 3). Other comparisons in which this group of samples was involved include: Initial Good vs Mid, Initial Bad vs Mid, Final Bad vs Mid and Final Good vs Mid. This gene expression profiling was carried out making use of Affymetrix’s GeneChip technology, with the Affymetrix’s HG-U133 Plus 2.0 array from this provider. All the protocols and apparatus were recommended by Affymetrix. Total RNA from frozen mammary tumors was directly extracted by a RNeasy Mini kit and homogenized by QIAshredder columns under manufacturer’s instructions. The quality and quantity of the obtained RNA, was checked out through agarose electrophoresis and later spectrophotometry at 260/280 nm. Biotinylated cRNA was synthesized following the IVT labeling kit from Affymetrix and purified by the GeneChip Sample Cleanup Module from Affymetrix. Once again, the quality and quantity of the obtained cRNA, was checked out through agarose electrophoresis and posterior spectrophotometry at 260/280 nm. After hybridization, slides were washed and scanned following the manufacturer’s standard protocol. Intensity values were normalized by Robust Multichip Average method and subsequently these were filtered for remove the control sequences and those with a hybridization signal near to background. The spike controls were: BioB, BioC, BioD and Cre; because BioB was the less presented in the samples, it was used to estimate the sensitivity of the experiment. The housekeeping control was GAPDH. After non-supervised PCA analysis and clustering, gene expression statistical significances were identified by two regression models taking into account the pathologic response to chemotherapy and if the sample was obtained before or after chemotherapy treatment. Supervised PCA analysis and clustering were performed with processed data. Partek Genomics Suite v7.3.1 (Partek) software was employed for the statistic analysis and clustering.
   Response columns (1):
     - characteristics_ch1_pathologic response to chemotherapy (miller & payne grade) (1 unique values): [3.0]

   Sample summary (random sample from GSE28583):
score_age: 1
score_sex: 1
score_tissue: 1
score_primary_human_text: 10
net_score: 13
primary_score: 13
score_cancer_cols: 1
score_cancer_text: 3
refinebio_title: Breast tumor biopsy_Postchemotherapy_08SE141
refinebio_age: 58.0
refinebio_sex: female
refinebio_source_database: GEO
refinebio_specimen_part: breast tumor
refinebio_treatment: a
description: Affymetrix Standard Protocol
treatment_protocol_ch1: RNA processing: snap frozen in liquid nitrogen and preserved at -80C. Before RNA extraction protocol, samples were sectioned in a cryostat to evalute the celularity.

38. GSE18948 (16 samples)
   Title: Personalized medicine in psoriasis: developing a genomic classifier to predict histological response to Alefacept
   overall design: Microarray data from 16  patients was analyzed to generate a treatment response classifier. We used a discriminant analysis method that performs sample classification from gene expression data, via nearest shrunken centroid method.
   Response columns (1):
     - characteristics_ch1_histological response (2 unique values): ['R', 'NR']

   Sample summary (random sample from GSE18948):
score_age: 1
score_sex: 1
score_patient: 1
score_tissue: 1
score_histology: 1
score_primary_human_text: 3
net_score: 8
primary_score: 8
score_cancer_cols: 1
refinebio_title: Patient 11
refinebio_subject: 11
refinebio_age: 44.0
refinebio_sex: male
refinebio_source_database: GEO
refinebio_specimen_part: blood
description: blood, Patient 11
growth_protocol_ch1: Peripheral blood draws were taken before alefacept administration. PBMCs were isolated and stored at -80C, until required
treatment_protocol_ch1: Patients with moderate-to-severe psoriasis were treated with alefacept (7.5mg weekly i.v. x12 weeks)

39. GSE95770 (16 samples)
   Title: Sorafenib promotes graft-versus-leukemia activity in mice and humans through IL-15 production in FLT3-ITD mutant leukemia cells
   overall design: Peripheral blood mononuclear cells (PBMC) from patients relapsing after allograft transplantation were extracted three days before and six days after treatment with sorafenib. 4 patients, marked as responders, showed a favorable outcome event after 6 months, while 4 patients. marked as non-responders. did not respond to sorafenib treatment.
   Response columns (1):
     - characteristics_ch1_treatment response (2 unique values): ['non-responder', 'responder']

   Sample summary (random sample from GSE95770):
score_primary_human_text: 4
net_score: 4
primary_score: 4
score_cancer_text: 9
refinebio_title: PBMC_Responder_Patient1_6d
refinebio_source_database: GEO
refinebio_specimen_part: peripheral blood mononuclear cell
refinebio_treatment: sorafenib
description: Gene expression data from PBMCs of a responder patient six days after Sorafenib treatment.
treatment_protocol_ch1: RNA from peripheral blood mononuclear cell of 8 patients at 2 different time points (3 days before and 6 days after Sorafenib treatment) were extractied from 8 ml of blood.

40. GSE28694 (8 samples)
   Title: Differentially expressed genes after treatment with chemotherapy in breast cancer and their correlation with pathologic good response (Miller & Payne grades 4 and 5)
   overall design: After informed consent, patients with a histologically confirmed diagnosis of breast cancer and scheduled chemotherapy treatment based on Anthracyclines and Taxanes (Treatment A: Epirubicin 90 mg/m2-Cyclophosphamide 600 mg/m2, 3 cycles bi-weekly and Taxol 150 mg/m2-Gemcitabine 2500 mg/m2, 6 cycles bi-weekly ± weekly Herceptin 4 mg/Kg during the first week, 2 mg/Kg for the remaining 11 cycles; Treatment B: Doxorubicin 60 mg/m2-Pemetrexed 500 mg/m2, 4 cycles tri-weekly and Taxotere 100 mg/m2, 4 cycles tri-weekly; Treatment C: Doxorubicin 60 mg/m2-Cyclophosphamide 600 mg/m2, 4 cycles tri-weekly and Taxotere 100 mg/m2, 4 cycles tri-weekly) were recruited for this study. Pre-chemotherapy and post-chemotherapy biopsies were examined by a pathologist who determined the Miller & Payne grade for each patient. Matching pairs of pre-chemotherapy and post-chemotherapy samples were divided into 3 groups according to Miller & Payne grade: group of bad response (Miller & Payne grades 1 and 2), group of mid response (Miller & Payne grade 3) and group of good response (Miller & Payne grades 4 and 5). Gene expression analysis was performed in paired samples as follows: bad response group post-chemotherapy biopsy vs pre-chemotherapy biopsy (Bad Final vs Initial). For this assay were necessary 13 samples being chosen according to histopathologic criteria (Miller & Payne grades 4 and 5). Of them, 10 samples were paired and 3 pre-chemotherapy samples from patients that experienced a good response to chemotherapy were also included in this experimental series. Other comparisons in which this group of samples was involved include: Initial Bad vs Good, Initial Good vs Mid, Final Mid vs Good and Final Bad vs Good. This gene expression profiling was carried out making use of Affymetrix’s GeneChip technology, with the Affymetrix’s HG-U133 Plus 2.0 array from this provider. All the protocols and apparatus were recommended by Affymetrix. Total RNA from frozen mammary tumors was directly extracted by a RNeasy Mini kit and homogenized by QIAshredder columns under manufacturer’s instructions. The quality and quantity of the obtained RNA, was checked out through agarose electrophoresis and later spectrophotometry at 260/280 nm. Biotinylated cRNA was synthesized following the IVT labeling kit from Affymetrix and purified by the GeneChip Sample Cleanup Module from Affymetrix. Once again, the quality and quantity of the obtained cRNA, was checked out through agarose electrophoresis and posterior spectrophotometry at 260/280 nm. After hybridization, slides were washed and scanned following the manufacturer’s standard protocol. Intensity values were normalized by Robust Multichip Average method and subsequently these were filtered for remove the control sequences and those with a hybridization signal near to background. The spike controls were: BioB, BioC, BioD and Cre; because BioB was the less presented in the samples, it was used to estimate the sensitivity of the experiment. The housekeeping control was GAPDH. After non-supervised PCA analysis and clustering, gene expression statistical significances were identified by two regression models taking into account the pathologic response to chemotherapy and if the sample was obtained before or after chemotherapy treatment. Supervised PCA analysis and clustering were performed with processed data. Partek Genomics Suite v7.3.1 (Partek) software was employed for the statistic analysis and clustering.
   Response columns (1):
     - characteristics_ch1_pathologic response to chemotherapy (miller & payne grade) (2 unique values): [4.0, 5.0]

   Sample summary (random sample from GSE28694):
score_age: 1
score_sex: 1
score_tissue: 1
score_primary_human_text: 10
net_score: 13
primary_score: 13
score_cancer_cols: 1
score_cancer_text: 3
refinebio_title: Breast tumor biopsy_Prechemotherapy_08SE190
refinebio_age: 47.0
refinebio_sex: female
refinebio_source_database: GEO
refinebio_specimen_part: breast tumor
refinebio_treatment: none (prechemotherapy)
description: Affymetrix Standard Protocol
treatment_protocol_ch1: RNA processing: snap frozen in liquid nitrogen and preserved at -80C. Before RNA extraction protocol, samples were sectioned in a cryostat to evalute the celularity.


## annotations:




['GSE21653', no reason: progresterone receptor (PR)
 'GSE16716', yes
 'GSE24742', no reason: not cancer. RA. score_cancer_cols: 1
 'GSE22152', no. cell lines. primary_score: 1
 'GSE37180', yes
 'GSE39133', no reason: progresterone receptor (PR)
 'GSE46819', yes
 'GSE42296', no reason: RA
 'GSE85047', no reason: prognostic data
 'GSE58911', no reason: prognostic data
 'GSE25055', yes
 'GSE11237', no DE upon treatment, not clinical response
 'GSE40020', yes
 'GSE25066', yes
 'GSE68465', no reason: prognostic data
 'GSE66525', no reason: prognostic data
 'GSE54747', no reason: prognostic data
 'GSE58598', no reason: not cancer.
 'GSE15622', yes
 'GSE18864', yes
 'GSE31852', yes
 'GSE64085', no. repsonse to transplant. 
 'GSE157738', no reason: prognostic data
 'GSE39925', no reason: prognostic data
 'GSE106977', yes. 'neoadjuvant chemo'
 'GSE29561', yes
 'GSE115577', no. 
 'GSE35640', yes. MAGE 'immunotherapy'
 'GSE15258', no. not cancer. 
 'GSE28826', yes
 'GSE11001', no . PR status
 'GSE84334', yes
 'GSE46106', no. xenografts.
 'GSE93984', yes. 
 'GSE41408', no. surgery response. 
 'GSE36295', no
 'GSE28583', yes
 'GSE18948', no. psoraisis
 'GSE95770', yes
 'GSE28694', yes. cheome