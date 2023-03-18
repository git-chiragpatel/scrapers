import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.mnit.ac.in/news/newsall.php?type=latest")
driver.implicitly_wait(10)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

latest_news_section = soup.find("div", class_="span9")

news_items = latest_news_section.find_all("div", class_="item")

for news in news_items:
    headline = news.find("h3").text.strip()
    details = news.find("p").text.strip()
    print(headline)
    print(details)
    print("=" * 50)

driver.quit()