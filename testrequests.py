import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")

soup = BeautifulSoup(page.content, 'html.parser')

var = soup.find_all('p')

var2 = map(lambda x: x.get_text(), var)

print(var)
print(list(var2))