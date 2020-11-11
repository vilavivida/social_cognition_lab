#	Cross-checking two files
#	Mark files that only included in data_table as 9



import csv

dir_path = "Data_ALL_IVOp2and3/"
hosted_file = "Included-Studies-(2020)-Table-1.csv"
master_file = "Data-Table-1.csv"

f1 = open(dir_path + hosted_file, 'r')
f2 = open(dir_path + master_file, 'r')
f3 = open('results_1.csv', 'w')

c1 = csv.reader(f1) 
c2 = csv.reader(f2)
c3 = csv.writer(f3)

masterlist = list(c2)

for hosts_row in c1:
    row = 1
    found = False
    for master_row in masterlist:
        results_row = hosts_row
        #hosted = targeted_file
        #master = data_table
        if hosts_row[0] == master_row[2]:
            results_row.append('')
            found = True
            break
        row = row + 1
    if not found:
        results_row.append('9')
    c3.writerow(results_row)

f1.close()
f2.close()
f3.close()