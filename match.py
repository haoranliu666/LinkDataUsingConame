import json
import pandas as pd
from string_grouper import match_strings, match_most_similar, \
	group_similar_strings, compute_pairwise_similarities, \
	StringGrouper

with open('/Users/haoranliu/Downloads/match_tri_crsp/cleaned/tri_us_name_newname.json') as f:
	tri_name = json.load(f)

with open('/Users/haoranliu/Downloads/match_tri_crsp/cleaned/tri_us_name_id.json') as f:
	tri_id = json.load(f)

with open('/Users/haoranliu/Downloads/match_tri_crsp/cleaned/crsp_name_newname.json') as f:
	crsp_name = json.load(f)

with open('/Users/haoranliu/Downloads/match_tri_crsp/cleaned/crsp_name_id.json') as f:
	crsp_id = json.load(f)

tri = pd.DataFrame()
tri['name'] = tri_name
tri['id'] = tri_id

crsp = pd.DataFrame()
crsp['name'] = crsp_name
crsp['id'] = crsp_id

# num = 0.9 #12018
# # matches = match_strings(master = tri['name'], master_id = tri['id'], duplicates = crsp['name'], duplicates_id = crsp['id'], min_similarity = num)
# # matches.to_stata(f'tri_crsp{num}.dta', version = 117)
# num = 0.8 #26809
# matches = match_strings(master = tri['name'], master_id = tri['id'], duplicates = crsp['name'], duplicates_id = crsp['id'], min_similarity = num)
# matches = match_strings(master = crsp['name'], master_id = crsp['id'], duplicates = tri['name'], duplicates_id = tri['id'], min_similarity = num)
# matches.to_stata(f'tri_crsp{num}.dta', version = 117)
num = 0.7 #106902
matches = match_strings(master = tri['name'], master_id = tri['id'], duplicates = crsp['name'], duplicates_id = crsp['id'], min_similarity = num)
matches.to_stata(f'tri_crsp{num}.dta', version = 117)
#num = 0.6 #497379
# matches = match_strings(master = tri['name'], master_id = tri['id'], duplicates = crsp['name'], duplicates_id = crsp['id'], min_similarity = num)
matches.to_stata(f'tri_crsp{num}.dta', version = 117)

#string_grouper.match_strings()
#(master, master_id, duplicates, duplicates_id, min_similarity)