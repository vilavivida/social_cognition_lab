import shutil
from pathlib import Path
import os
import csv
from toolz import unique

# Download from BOX: https://uofi.app.box.com/folder/123866057353

# Importing files
source = 'Data_analysis_articles_all/'
dest1 = 'Included Studies/'
dest2 = 'Excluded Studies/'
files = os.listdir(source)

# Importing CSV
lst = []
data_table = "Data-Table_1.csv"
with open(data_table, 'r') as csvfile: 
	content = csv.reader(csvfile)
	for row in content:
		lst.append(row)

data_lst = list(map(list, unique(map(tuple,lst))))

# Manually clean the csv file
# Remove column names
for paper in data_lst:
	if paper == ['LeadAuthor', 'Year']:
		data_lst.remove(paper)

str_lst = []
for paper in data_lst:
	f_str = paper[0] + " " + paper[1] + ".pdf"
	str_lst.append(f_str)

# TODO: Change dir_path.

# str_lst is from the csv file
# files is from the folder
for f in files:
    if f in str_lst:	
        shutil.move((path + f), dest1)
    else:
        shutil.move((path+f), dest2)


