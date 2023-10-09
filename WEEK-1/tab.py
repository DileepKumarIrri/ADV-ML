# Python program to convert .tsv file to .csv file
# importing pandas library
import pandas as pd

tsv_file='WEEK-1\cereal.tsv'

# reading given tsv file
csv_table=pd.read_table(tsv_file,sep='\t')

# converting tsv file into csv
csv_table.to_csv('WEEK-1\cereal',index=False)

# output
print("Successfully made csv file")
