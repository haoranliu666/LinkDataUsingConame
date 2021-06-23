# LinkDataUsingConame

You got two corporate databases, but one or two of them don't have a standard linking indenfitier, like Permno, Gvkey or Cusip, so you have to link these two databases using company names.

### Step 1: Pre-clean

Firsty, you need to make two stata files(.dta) containing unique company name and its unique id. Name the name as name and id as id.

<img src="https://github.com/haoranliu666/LinkDataUsingConame/blob/main/pics/1.png" width="50%" height="50%">

### Step 2: Clean

Secondly, clean two pre-cleaned databases using clean.py, note, you can freely change the clean method, and how you clean the data can affect the matching result.

For my clean step, see https://github.com/haoranliu666/TrademarkMatch/blob/main/Clean_name/document.md.

### Step 3: Match

Thirdly, match two cleaned databases using match.py.

This step uses tf-idf to calculate cosine similarities, see https://github.com/Bergvca/string_grouper.

### *Step 4: Manually Check

Fourthly, use match.do rebuild the matched data. Fuzzy matched data contains wrongly matched data, you might want to manually pick out the wrong pairs.

<img src="https://github.com/haoranliu666/LinkDataUsingConame/blob/main/pics/2.png" width="50%" height="50%">

### Step 5: Link

Finally, link two databases using matched data.
