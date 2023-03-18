import requests
from bs4 import BeautifulSoup


scrapers_report = []
title = []

url = 'https://tnau.ac.in/news-events/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Find all the news/events articles
articles = soup.find_all('article')

try:
    url = "https://tnau.ac.in/news-events/"
    base_url = "https://tnau.ac.in/"
    name = 'TNAU'
    scrapers_report.append([url,base_url,name])
    for article in articles[1:9]:
        title_tag = article.find('h3')
        if title_tag:
         title = title_tag.text.strip()
        else:
         title = title_tag
    link = article.find('a')['href']
    print(title)
    print(link)
except Exception as e:
    pass
    print(scrapers_report)