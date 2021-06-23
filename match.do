cd /Users/haoranliu/Downloads/match_tri_crsp

use /Users/haoranliu/Downloads/match_tri_crsp/tri_crsp0.7.dta, clear
gsort left_id -similarity
by left_id: keep if _n == 1
keep left_id right_id
save tri_crsp_idpair.dta, replace

*link
use /Users/haoranliu/Downloads/match_tri_crsp/raw_data/tri_us_name.dta, clear
rename id left_id
rename name tri_name

*crsp id = permno
merge 1:1 left_id using /Users/haoranliu/Downloads/match_tri_crsp/tri_crsp_idpair.dta
drop _merge
rename right_id id
merge m:n id using /Users/haoranliu/Downloads/match_tri_crsp/raw_data/crsp_name.dta
drop if _merge == 2
drop _merge
rename name crsp_name
rename id crsp_id
rename left_id tri_id

*
count //6,268
count if crsp_id != "" //1,241

keep if crsp_name != ""

gen flag = 0
sort tri_name crsp_id 

order flag tri_name crsp_name

rename crsp_name conml
rename crsp_id gvkey
rename tri_id tri_name_id

save matched.dta, replace
export excel using matched, firstrow(variable) replace
