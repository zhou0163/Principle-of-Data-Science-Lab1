import csv
f = open('TB_burden_countries_2014-09-29.csv')
num_row = 0
for row in csv.reader(f):
    num_row += 1
print (num_row)

with open('TB_burden_countries_2014-09-29.csv') as f: 
    f_csv = csv.reader(f)
    headers = next(f_csv)
    average = 0.0
    sum = 0.0
    row_count = 0
    for row in f_csv:
       if row[11].strip():
         n=float(row[11])
         sum += n
         row_count += 1
    average = sum / row_count
print(average)

with open('TB_burden_countries_2014-09-29.csv') as f: 
    f_csv = csv.reader(f)
    headers = next(f_csv)
    average = 0.0
    sum = 0.0
    row_count = 0
    for row in f_csv:
        if row[11].strip() and row[5] in ['1999', '2011']:
            n = float(row[11])
            sum += n
            row_count += 1
    average = sum / row_count
print(average)
