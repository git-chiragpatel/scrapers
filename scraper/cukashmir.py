import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()

url = 'https://www.cukashmir.ac.in/default.aspx'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# navigate to the news & updates section using Selenium
driver.get(url)
driver.find_element_by_link_text('News & Updates').click()

# get news & updates content using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
news = soup.find_all('div', class_='cuk-news-events-block')

for n in news:
    print(n.text.strip())