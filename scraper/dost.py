from bs4 import BeautifulSoup,Comment
from urllib.request import urlopen
import ssl
import re


context = ssl._create_unverified_context()


article=[]
links = []
success=[]
failure=[]
scrapers_report=[]
link=[]

try:
    name ="Dost"
    url = "https://dost.cgg.gov.in/"    
    base_url = "https://dost.cgg.gov.in/"

    scrapers_report.append([url,base_url,name])
    res = urlopen(url,context=context)
    soup =BeautifulSoup(res,"html.parser")
    results = soup.find("marquee").findChildren()[0]
    results = results.findChildren()

    for i in results:
        has_link = False
        t = i.text.strip()
        if (t not in article) and (t != ''):
            article.append(t)
            if 'Click Here' in t:
                l = i.find('a', href=True)
                if l is not None:
                    has_link = True
                    link.append(base_url+l.get("href"))
            if not has_link:
                link.append("")

    success.append(name)

except Exception as e:
    failure.append([name,e])


print(link)
print(article)