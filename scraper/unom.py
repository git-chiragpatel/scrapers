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
    url = "https://www.unom.ac.in/index.php?route=administration/announcement"
    base_url = "https://www.unom.ac.in/"
    name = 'University of Madras'
    scrapers_report.append([url,base_url,name])
    driver.get(url)
    time.sleep(3)
    results = driver.find_elements(By.CLASS_NAME,"media-body")
    for i in results:
        headline = i.find_element(By.TAG_NAME , "a").text
        link = i.find_element(By.TAG_NAME , "a").get_attribute('href')
        if "http" not in link:
            link = base_url + link
        news_articles.append(("University of Madras",headline,link))
    success.append('University of Madras')
    driver.quit()
except Exception as e:
    driver.quit()
    failure.append((name,e))
    pass
