from selenium import webdriver
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome()

driver.get("https://www.nmimsbengaluru.org/")

html = requests.get(driver.current_url).text

soup = BeautifulSoup(html, "html.parser")

news_section = soup.find("div", {"class": "col-md-8"})

news_articles = news_section.find_all("div", {"class": "news__block"})

for article in news_articles:
    title = article.find("h5", {"class": "news__title"}).text.strip()
    date = article.find("p", {"class": "news__date"}).text.strip()
    print(f"{title} - {date}")

driver.quit()