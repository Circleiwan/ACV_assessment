import pandas as pd
import csv
import numpy as np
import os

file_csv = []

for file in os.listdir():
	f, e = os.path.splitext(file)
	if e == '.csv':
		file_csv.append(file)
print(file_csv)
data1 = pd.read_csv(file_csv[0])
data2 = pd.read_csv(file_csv[1])
print(data1)
print(data2)
output = data1.merge(data2,	on= 'index', how = 'outer')
output.to_csv('merged_data.csv', index=False)