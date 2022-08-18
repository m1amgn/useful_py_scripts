# Convert CSV to JSON

import csv
import json


def CSV_to_JSON(csv_file):
    data = {}  
    with open(csv_file, encoding = 'utf-8') as f:  
        csvrows = csv.DictReader(f)  
        for rows in csvrows:        
            key = rows['Name']  
            data[key] = rows    with open("output.json", 'w', encoding = 'utf-8') as f:  
        f.write(json.dumps(data, indent = 4))
        
CSV_to_JSON('test.csv')
