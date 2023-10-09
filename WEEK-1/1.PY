import pandas as pd
import csv
df = csv.reader(open('WEEK-1\cereal.csv', 'r'), delimiter=';')

csv_rows =[]
for row in df:
    csv_rows.append(row)
    # print(row)
# print(type(csv_rows))
# print(csv_rows)

for l in csv_rows:
    print(l)


