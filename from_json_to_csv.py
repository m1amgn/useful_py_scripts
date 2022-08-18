import json, csv

with open("data.json") as file:
    data = json.load(file)
    

emp_details = data['emp_details']


with open("data.csv", 'w', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(emp_details[0].keys())
    for row in emp_details:
        csv_writer.writerow(row.values())
