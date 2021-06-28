cd /dir

use a_b0.7.dta, clear
gsort left_id -similarity
by left_id: keep if _n == 1
keep left_id right_id
save a_b_idpair.dta, replace

*link
use a.dta, clear
rename id left_id
rename name a_name

merge 1:1 left_id using a_b_idpair.dta
drop _merge
rename right_id id
merge m:n id using b_name.dta
drop if _merge == 2
drop _merge
rename name b_name
rename id b_id
rename left_id a_id

*
count
count if crsp_id != ""

keep if crsp_name != ""

gen flag = 0
sort tri_name crsp_id 

order flag a_name b_name

save matched.dta, replace
