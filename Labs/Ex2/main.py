#!/usr/bin/python3

#Exercise 2: Improvised ETL
#1/31/2024
#Author - Daniel Kaszuba

import datetime
import json

# Format file name in YYYYDDMM
curDate = datetime.date.today()
formatDate = curDate.strftime("%Y%m%d")
genFile = f"{formatDate}.csv"

file = 'data.json'
keys = ["name", "creditcard"]

# Open data file for reading
with open(file, 'r') as json_file:
    data = json.load(json_file)

# Format header and write data from data.json
with open(genFile, 'w') as csv_file:
    header = ','.join(keys) + '\n'
    csv_file.write(header)

    for row in data:
    	if row.get("creditcard") is not None:
        	row_values = ','.join(str(row.get(key, '')) for key in keys) + '\n'
        	csv_file.write(row_values)

print(genFile + " has been created.")
