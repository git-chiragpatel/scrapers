import time
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome()
driver.get("https://tnou.ac.in/news-and-events/")

time.sleep(3)

page = requests.get(driver.current_url)
soup = BeautifulSoup(page.content, "html.parser")

# Find the news section and print the headlines
news_section = soup.find("div", class_="et_pb_column et_pb_column_1_2 et_pb_column_0 et_pb_css_mix_blend_mode_passthrough")
news_headlines = news_section.find_all("h2", class_="entry-title")

for headline in news_headlines:
    print(headline.text)

# Find the events section and print the headlines
events_section = soup.find("div", class_="et_pb_column et_pb_column_1_2 et_pb_column_1 et_pb_css_mix_blend_mode_passthrough")
events_headlines = events_section.find_all("h2", class_="entry-title")

for headline in events_headlines:
    print(headline.text)

driver.quit()