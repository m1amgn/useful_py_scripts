# Get your API : https://newscatcherapi.com/

import requests


query = "Tesla"
country = "US"
URL = f"https://api.newscatcherapi.com/v2/search?q=\"{query}\"&lang=en&countries={country}"

payload={}
headers = {
  'X-API-KEY': 'Your API Key'
}

r = requests.get(URL, headers=headers, data=payload)
news = r.text
print(news)
