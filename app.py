import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-web-scraping-tutorial/#beautifulsoup-library')
print(dir( requests))
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_='entry-content')
content = soup.find_all('h2')

print(content)