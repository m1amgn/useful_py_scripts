# Scrape News Headlines
# pip install GoogleNews

from GoogleNews import GoogleNews

gnews = GoogleNews()# Search news by keyword
gnews.search('python')
gnews.results()# Get News Titles
gnews.get_texts()
gnews.results()# Get News url
gnews.get_urls()
gnews.results()# Search news by lang
gnews.search('python', lang='en', region= 'UK')
gnews.results()
