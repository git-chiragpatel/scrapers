import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.unom.ac.in/index.php?route=administration/announcement")

driver.implicitly_wait(10)
page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')

# Find the news section
news_section = soup.find('div', {'class': 'blog'})

# Extract the news items
news_items = news_section.find_all('div', {'class': 'media'})

for item in news_items:
    title = item.find('h4', {'class': 'media-heading'}).text.strip()
    date = item.find('span', {'class': 'date'}).text.strip()
    print(f'{title} ({date})\n')
    
driver.quit()