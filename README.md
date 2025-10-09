# find up to 5000 new clinical smaples!
my original data had 6700 metadata collumns.
I used regexp and some heuristics to find collumns that may have response data. 
out of a total of 7691 samples found this way, 5086 are currently **not** in my clinical data store.

reminder: every sample, has a sample ID. in this case all of them come from the GEO repository, with an id in the format 'GSMXXXXX'. those files also have an experiment id in the format 'GSEXXXX'
for exmaple, some of the samples come from `GSE48905`. you can find info in geo about it by lookign it up either in google, or better: `https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi`  and then search in the geo_accession box. in this example, you will se that `GSM1186556` is part of that experiment. 



we need to figure out if this data is actully clinically meaningfull.
1. did the experiment invlove samples from real patients (as opposed to cell lines)?
2. do we have a respone label for the patient? ultimately, we will want 0 indicating non response, and 1 indicating response.
Defintion of Done: for each unique expeirment ID in the data: was the answer to the two previous question correct?

data files: 
1. clin_obs.csv: a dataframe of the metadata of the clinical samples I already have. the sample_id collumn should be used to ignore samples.
2.  potential_clin_data.csv - the main data to process. 7600 samples. 600 collumns. lots of trash. 
3. experiment_data.csv- a file with on every experiment in the relevant data.
4. response_collumn_shortlist.csv - a file of the collumns that i suspect have clinical response data. it lists the name, how many rows aren't empty and shows all the differnet unique values that there were in that collumn. 
4. metadata_HOMO_SAPIENS.parquet - the full original metadata file. **do not open!! takes 40GB of RAM**. parquet is a very efficent format for storing files with lots of empty cells. 
**note**: to access the main metadata parquet (unecessary here), **git LFS is reuqired**: `https://git-lfs.com/`
hints:
not a cell line: which collumns might inidicate a ceall line? which are probably realted to a person?
use the the experiment_accession collumn: use the all_gse_annotated to add collumns of experiment title, summary and overall design. 
figure out which collumns and patterns will help you answer the questions. 
i suggest manully inspecting a few smaples and getting an idea of what to search for.
lets say you assume that if a sample has an 'age' value, then its human. how many experiements does this flag? are there cases in which collumns may contradict themselves?

of course, at then end you can manully inspect the epxeriment description to decide, but the goal here is to learn to play with data to get answers. 

further things to look up: what terms indicate responses? 




