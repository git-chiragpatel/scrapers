from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

driver_service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=driver_service)

success = []
failure = []
scrapers_report = []
news_articles = []

try:
    url = "https://tnou.ac.in/news-and-events/"
    base_url = "https://tnou.ac.in/"
    name = 'Tamil Nadu Open University'
    scrapers_report.append([url,base_url,name])
    driver.get(url)
    time.sleep(3)
    results = driver.find_elements(By.CLASS_NAME,"entry-title")
    for i in results:
        headline = i.find_element(By.TAG_NAME , "a").text
        link = i.find_element(By.TAG_NAME , "a").get_attribute('href')
        if "http" not in link:
            link = base_url + link
        news_articles.append(("Tamil Nadu Open University",headline,link))
    success.append('Tamil Nadu Open University')
    driver.quit()
except Exception as e:
    driver.quit()
    failure.append((name,e))
    pass
