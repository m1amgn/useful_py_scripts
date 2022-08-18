# Parse JSON

import json
import requests


# Parse Json from URL
url = "https://www.example.com/api"
response = requests.get(url)
data = response.json()

# Load Json File
with open('example.json') as json_file:
    json_data = json.load(json_file)

test = {"product": "test", 
        "price": "10.00", 
        "quantity": "1"}

# Find Price
price = test["price"]

# Write to Json File
with open('example.json', 'w') as out:
    json.dump(test, out)


# Write Json with Format
with open('example.json', 'w') as out:
    json.dump(test, out, indent=4)
