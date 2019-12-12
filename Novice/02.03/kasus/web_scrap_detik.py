import requests
from mathematicians import simple_get
from bs4 import BeautifulSoup

URL = "https://www.detik.com"
page = requests.get(URL)

html = BeautifulSoup(page.content, 'html.parser')
#print (html)
for i, link in enumerate(html.select("h3", class_="media__title")):
        #if h3["media__title"]=='Ansu Fati'
        #print(h3.text)
        print(i, link.text.strip())