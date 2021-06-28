import json
import pandas as pd
from string_grouper import match_strings

with open('dir/a_newname.json') as f:
	a_name = json.load(f)

with open('dir/a_id.json') as f:
	a_id = json.load(f)

with open('dir/b_newname.json') as f:
	b_name = json.load(f)

with open('dir/b_id.json') as f:
	b_id = json.load(f)

a = pd.DataFrame()
a['name'] = a_name
a['id'] = a_id

b = pd.DataFrame()
b['name'] = b_name
b['id'] = b_id

num = 0.7 
matches = match_strings(master = a['name'], master_id = a['id'], duplicates = b['name'], duplicates_id = b['id'], min_similarity = num)
matches.to_stata(f'a_b{num}.dta', version = 117)
