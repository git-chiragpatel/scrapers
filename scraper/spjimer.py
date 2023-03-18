from bs4 import BeautifulSoup
import requests
from selenium import webdriver

driver = webdriver.Chrome()

url = "https://www.spjimr.org/newsroom"
driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

news_updates_section = soup.find("div", {"class": "views-element-container"})

articles = news_updates_section.find_all("div", {"class": "views-row"})

for article in articles:
    title = article.find("h3").text.strip()
    link = article.find("a")["href"]
    print(title)
    print(link)
    print()
    
driver.quit()