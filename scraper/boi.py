from selenium import webdriver
from bs4 import BeautifulSoup
import requests

url = 'https://bankofindia.co.in/recruitment-notice'

driver = webdriver.Chrome()
driver.get(url)


soup = BeautifulSoup(driver.page_source, 'html.parser')

recruitments = soup.find_all('div', class_='section-1')

# Loop through all recruitment notices and print their content
for recruitment in recruitments:
    # Get the recruitment notice title and content
    title = recruitment.find('h2')
    content = recruitment.find('div', class_='content')

    if title and content:
        print(title.text)
        print(content.text)

driver.quit()