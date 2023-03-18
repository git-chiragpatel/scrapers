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
    url = "http://ndri.res.in/"
    base_url = url
    name = 'NDRI'
    scrapers_report.append([url,base_url,name])
    driver.get(url)
    time.sleep(5)
    results = driver.find_elements(By.CLASS_NAME,"height-box")
    for i in results[1:9]:
        li = i.find_elements(By.TAG_NAME, "li")
        for j in li:
            headline = j.text
            link = j.find_element(By.TAG_NAME , "a").get_attribute('href')
            if "http" not in link:
                link = base_url + link
            news_articles.append(("NDRI",headline,link))
    success.append('NDRI')
    driver.quit()
except Exception as e:
    driver.quit()
    failure.append((name,e))
    pass
print(news_articles)
