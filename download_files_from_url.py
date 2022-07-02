# Download Files from URL

url = "https://instagram.com/favicon.ico"

# Method 1
# pip install requests

import requests

r = requests.get(url)

with open("favicon.ico", "wb") as f:
    f.write(r.content)

# Method 2
# pip install wget

import wget

r = wget.download(url, "favicon.ico")

# Method 3
# pip install urllib3

import urllib.request

urllib.request.urlretrieve(url, "favicon.ico")
