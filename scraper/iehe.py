import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime

url = 'https://www.iehe.ac.in/Index.aspx?ID=En'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

driver = webdriver.Chrome()
driver.get(url)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
driver.close()

latest_updates = soup.find('div', {'class': 'LatestUpdates'})

articles = latest_updates.find_all('a')

news_articles = []
for article in articles:
    title = article.get_text()
    link = article['href']
    print(title, link)
    news_articles.append({'title': title, 'link': link})

scrapers_report = f"Scraping Report ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})\n"
scrapers_report += f"URL Scraped: {url}\n"
