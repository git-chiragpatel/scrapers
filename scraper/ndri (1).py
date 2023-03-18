import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime

url = 'https://www.uudoon.in/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

driver = webdriver.Chrome()
driver.get(url)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
driver.close()

latest_notifications = soup.find('div', {'class': 'latest-news'})

notifications = latest_notifications.find_all('a')

news_articles = []
for notification in notifications:
    title = notification.find('h4').get_text().strip()
    link = notification['href']
    print(title, link)
    news_articles.append({'title': title, 'link': link})

scrapers_report = f"Scraping Report ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})\n"
scrapers_report += f"URL Scraped: {url}\n"
scrapers_report += f"Number of Notifications Scraped: {len(news_articles)}\n"

print(scrapers_report)