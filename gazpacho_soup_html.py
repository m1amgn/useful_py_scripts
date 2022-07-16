# Parse and Extract HTML

# pip install gazpacho

import gazpacho

# Extract HTML from URL
url = 'https://www.example.com/'
html = gazpacho.get(url)
print(html)

# Extract HTML with Headers
headers = {'User-Agent': 'Mozilla/5.0'}
html = gazpacho.get(url, headers=headers)
print(html)

# Parse HTML
parse = gazpacho.Soup(html)

# Find single tags
tag1 = parse.find('h1')
tag2 = parse.find('span')

# Find multiple tags
tags1 = parse.find_all('p')
tags2 = parse.find_all('a')

# Find tags by class
tag = parse.find('.class')

# Find tags by Attribute
tag = parse.find("div", attrs={"class": "test"})

# Extract text from tags
text = parse.find('h1').text
text = parse.find_all('p')[0].text
