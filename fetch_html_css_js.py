# Fetch HTML with Python 

# pip install requests
# pip install seleniumimport requests as req

from selenium import webdriver


def Fetch_Static():
    r= req.get("https://www.example.com")
    if r.status_code == 200:
        return r.text

def Fetch_Dynamic():
    browser = webdriver.Chrome()
    browser.get("https://www.example.com")
    return browser.page_source
