from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

context = ssl._create_unverified_context()

article=[]
links = []
success=[]
failure=[]
scrapers_report=[]

try:
    name ="Mpbsc"
    url = "https://mpbse.nic.in/latest-circulars.html"
    base_url = "https://mpbse.nic.in"

    scrapers_report.append([url,base_url,name])
    res = urlopen(url,context=context)
    soup =BeautifulSoup(res,"html.parser")
    results = soup.find_all("tr")

    for i in results:
        link = i.find('a')
        if link != None:
            u= f"{base_url}/{link.get('href')}"
            links.append(u)


    for i in results:
        art = i.find("b")
        if art != None:
            article.append(art.string)

    success.append(name)
except Exception as e:
    failure.append((name,e))